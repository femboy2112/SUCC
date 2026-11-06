"""Exact source checks for CF1--CF13. No finite test proves normality.

Run directly for unittest; --receipt emits the deterministic finite evidence.
Uses independent four-term and tap-vector source evaluators, Fraction tails,
and exact differentiated rational taps. No pi digits or floating phases.
"""
from fractions import Fraction as Q
from math import comb, factorial
import json
from pathlib import Path
import sys
import unittest

ORIGINAL = ((4, 7), (-2, 4), (-1, 3), (-1, 2))
DUAL_MINUS_TWO = ((-8, 7), (8, 6), (4, 5), (8, 4), (2, 3), (2, 2), (-1, 1))


def r(n):
    return Q(4, 8*n-7)-Q(2, 8*n-4)-Q(1, 8*n-3)-Q(1, 8*n-2)


def tapped(n, m, taps):
    return sum((Q((-1)**m*factorial(m)*8**m*c, (8*n-e)**(m+1))
                for c, e in taps), Q(0))


def radial(n):
    # Separate native eight-slot source, not defined by subtracting r and dual.
    weights = (Q(2), Q(-2), Q(-1), Q(-2), Q(-1, 2), Q(-1, 2), Q(1, 4), Q(0))
    return sum((w/Q(8*(n-1)+j) for j, w in enumerate(weights, 1)), Q(0))


def tail(n, m=0, radial_channel=False, K=12):
    taps = DUAL_MINUS_TWO if radial_channel else ORIGINAL
    scale = Q(1, 4) if radial_channel else Q(1)
    value = scale*sum((tapped(n+k, m, taps)/16**k for k in range(1, K+1)), Q(0))
    mass = sum(abs(c) for c, _ in taps)
    error = scale*Q(factorial(m)*8**m*mass,
                    15*16**K*(8*(n+K+1)-7)**(m+1))
    return value-error, value+error


def linear_interval(terms):
    lo=Q(0)
    hi=Q(0)
    for coefficient, (left, right) in terms:
        lo += coefficient*(left if coefficient >= 0 else right)
        hi += coefficient*(right if coefficient >= 0 else left)
    return lo, hi


def radial_increment(A, Lambda, n, k, ell):
    H=A*A*Lambda
    return linear_interval(((H, tail(n+1+ell, radial_channel=True)),
                            (-H, tail(n+1+k, radial_channel=True)),
                            (-H, tail(n+ell, radial_channel=True)),
                            (H, tail(n+k, radial_channel=True))))


def geometric_moments(order):
    values=[Q(1,15)]
    for p in range(1, order+1):
        values.append((1+sum((comb(p,k)*values[k] for k in range(p)),Q(0)))/15)
    return values


def tail_laurent(taps, order, scale=Q(1)):
    moments=geometric_moments(order-1)
    answer={}
    for power in range(1,order+1):
        degree=power-1
        answer[power]=scale*sum((Q(c,8)*(-1)**degree*sum(
            (comb(degree,k)*(-Q(e,8))**(degree-k)*moments[k]
             for k in range(degree+1)),Q(0)) for c,e in taps),Q(0))
    return answer


def exact_source_states(N):
    U=[Q(0)]
    Y=[Q(0)]
    Z=[Q(0)]
    carries=[]
    x=Q(0)
    for n in range(1,N+1):
        U.append(16*U[-1]+r(n))
        Z.append(16*Z[-1]+radial(n))
        Y.append(16*Y[-1]+r(n)-radial(n))
        uncentered=16*x+r(n)
        carry=uncentered.numerator//uncentered.denominator
        x=uncentered-carry
        assert x==U[n] % 1
        carries.append(carry)
    return U,Y,Z,carries


def receipt():
    derivatives=[]
    for n in (137,509,911):
        lower,upper=tail(n,2,True)
        third=tail(n,3,True)
        assert Q(1,32*n**3) <= lower <= upper <= Q(1,8*n**3)
        assert third[1]<0
        derivatives.append({"n":n,"z_second_lower":str(lower),
                            "z_second_upper":str(upper),"third_negative":True})
    increments=[]
    for A in (191,509,911):
        for Lambda in (1,8,64):
            L=A//Lambda
            for n in (A,2*A-1):
                for k,ell in ((0,L),(L//2,L)):
                    lo,hi=radial_increment(A,Lambda,n,k,ell)
                    d=ell-k
                    boundlo=Q(d*Lambda,864*A)
                    boundhi=Q(d*Lambda,8*A)
                    assert boundlo<=lo<=hi<=boundhi<=Q(1,8)
                    nextlo,nexthi=radial_increment(A,Lambda,n+1,k,ell)
                    assert nexthi<lo
                    increments.append({"A":A,"Lambda":Lambda,"n":n,"k":k,"ell":ell,
                                       "lower":str(lo),"upper":str(hi),
                                       "minimum_bound":str(boundlo),"maximum_bound":str(boundhi),
                                       "strictly_decreasing_certified":True})
    correlation=[]
    for n in (137,509,911):
        for d in (1,2,5):
            lo,hi=linear_interval(((1,tail(n)),(-1,tail(n+d))))
            assert 0<lo<=hi<Q(d,32*n**3)
            correlation.append({"n":n,"d":d,"tail_decrement_lower":str(lo),
                                "tail_decrement_upper":str(hi),"bound":str(Q(d,32*n**3))})
    T=tail_laurent(ORIGINAL,4)
    Z=tail_laurent(DUAL_MINUS_TWO,4,Q(1,4))
    delta={p:sum((Z[k]*(-1)**(p-k)*comb(p-1,p-k)
                 for k in range(1,p)),Q(0)) for p in range(2,5)}
    return {"authority":"exact finite source components; not asymptotic proof",
            "derivatives":derivatives,"increments":increments,"coherent_lag":correlation,
            "tail_laurent":{str(k):str(v) for k,v in T.items()},
            "radial_laurent":{str(k):str(v) for k,v in Z.items()},
            "compensated_tail":{str(k):str(T[k]+delta[k]/2) for k in delta}}


class CoupledSourceTests(unittest.TestCase):
    def test_native_source_tap_maps(self):
        for n in (1,2,17,137,509,911):
            self.assertEqual(r(n),tapped(n,0,ORIGINAL))
            self.assertEqual(radial(n),-tapped(n,0,DUAL_MINUS_TWO)/4)

    def test_derivative_constants(self):
        C2=factorial(3)*(Q(1,30)+Q(167,3840)*Q(16,9)**4)
        C3=factorial(4)*(Q(1,30)+Q(167,3840)*Q(16,9)**5)
        self.assertEqual(C2,Q(18413,6561))
        self.assertEqual(C3,Q(5708452,295245))
        self.assertLess(32*C2,128)
        self.assertLess(Q(16,3)*C3,128)

    def test_source_and_carry_identity(self):
        U,Y,Z,c=exact_source_states(152)
        for n in (1,17,137):
            for d in (1,2,5):
                forcing=sum((16**(d-j)*r(n+j) for j in range(1,d+1)),Q(0))
                carry=sum(16**(d-j)*c[n+j-1] for j in range(1,d+1))
                x=U[n] % 1
                self.assertEqual(U[n+d] % 1,16**d*x+forcing-carry)
                self.assertEqual(U[n],Y[n]+Z[n])
                for H in (1,16**5):
                    self.assertEqual((H*(U[n+d]-U[n])) % 1,
                                     (H*((16**d-1)*x+forcing)) % 1)

    def test_common_gauge_gram_and_one_fifth(self):
        U,Y,Z,_=exact_source_states(145)
        for n in (1,17,137):
            for k,ell in ((0,1),(1,5),(0,7)):
                for H in (1,17,16**5):
                    expected=H*(Z[n+ell]-Z[n+k])
                    for common in (Q(0),Q(n*n,31),16**n*Q(1,5)):
                        left=H*(Y[n]+common+Z[n+ell])
                        right=H*(Y[n]+common+Z[n+k])
                        self.assertEqual(left-right,expected)
                    self.assertEqual((H*16**n*Q(1,5)) % 1,(Q(H,5)) % 1)

    def test_artificial_anticompanion_hits_any_coordinate(self):
        _,_,Z,_=exact_source_states(145)
        for n in (17,137):
            for ell0 in (0,1,5):
                anti=-Z[n+ell0]
                self.assertEqual(anti+Z[n+ell0],0)
                self.assertNotEqual(anti+Z[n+ell0+1],0)

    def test_parallel_transport_collapses_gram_rank(self):
        U,Y,Z,_=exact_source_states(145)
        for n in (17,137):
            for H in (1,17,16**5):
                transported=[H*(Y[n]+Z[n+ell])+H*(Z[n]-Z[n+ell])
                             for ell in range(8)]
                self.assertTrue(all(value==H*U[n] for value in transported))
                self.assertTrue(all(left-right==0 for left in transported
                                    for right in transported))

    def test_compensation_laurent(self):
        T=tail_laurent(ORIGINAL,4)
        Z=tail_laurent(DUAL_MINUS_TWO,4,Q(1,4))
        self.assertEqual(T[2],Q(1,64))
        self.assertEqual(T[3],-Q(7,512))
        self.assertEqual(Z[1],Q(1,32))
        self.assertEqual(Z[2],-Q(5,256))
        delta2=-Z[1]
        delta3=Z[1]-2*Z[2]
        self.assertEqual(T[2]+delta2/2,0)
        self.assertEqual(T[3]+delta3/2,Q(11,512))
        # Wrong compensation sign preserves, rather than kills, the n^-2 term.
        self.assertEqual(T[2]-delta2/2,Q(1,32))

    def test_exact_future_tail_forcing_defect(self):
        K=8
        for n in (137,509,911):
            Tn=sum((r(n+k)/16**k for k in range(1,K+1)),Q(0))
            Tprev=sum((r(n-1+k)/16**k for k in range(1,K+1)),Q(0))
            self.assertEqual(16*Tprev-Tn,r(n)-r(n+K)/16**K)

    def test_fresh_interval_receipt(self):
        data=receipt()
        self.assertEqual(len(data["increments"]),36)
        self.assertEqual(len(data["coherent_lag"]),9)


if __name__=="__main__":
    if sys.argv[1:]==["--receipt"]:
        print(json.dumps(receipt(),indent=2,sort_keys=True))
    elif sys.argv[1:]==["--verify"]:
        expected=json.loads(Path(__file__).with_name("FINITE_RECEIPT.json").read_text())
        assert receipt()==expected
        print("CF_COUPLED_SOURCE_RECEIPT_VERIFIED")
    else:
        unittest.main()
