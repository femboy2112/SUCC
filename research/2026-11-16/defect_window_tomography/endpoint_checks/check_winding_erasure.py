"""Exact independent calibration of terminal winding erasure (not R0)."""
from fractions import Fraction as F
from math import gcd
import json


def source(n):
    # Independently combined rational oracle, not the test module's four taps.
    return F(120*n*n-89*n+16,
             (2*n-1)*(4*n-1)*(8*n-7)*(8*n-3))


def torus(t):
    t = F(t) % 1
    return min(t, 1-t)


def energy(u, B):
    return sum((torus(u/F(16**k))**2 for k in range(1,B+1)),F(0))/B


def oddpart(n):
    while n % 2 == 0:
        n //= 2
    return n


def odd_primary_class(t):
    """Full odd-order component of t in Q/Z, encoded as a Fraction modulo 1."""
    t = F(t)
    q = oddpart(t.denominator)
    if q == 1:
        return F(0)
    power2 = t.denominator//q
    return F((t.numerator*pow(power2,-1,q)) % q,q)


def run():
    shells=(1,2,3,7,16,37,73,149,293,577)
    maxn=4*max(shells)+4
    states=[F(0)]
    for n in range(1,maxn+1):
        states.append(16*states[-1]+source(n))
    rows=[]
    checks=0
    for B in shells:
        u=states[2*B]
        C=u.numerator//u.denominator
        v=u-C
        D=C%(16**B)
        M=D+16**B
        s=-F(M,16**(2*B))
        altered=u+(16**(2*B))*s
        exact=v*v*(1-F(1,16**(2*B)))/F(255*B)
        assert F(1,16**B)<=abs(s)<F(2,16**B)
        assert s != 0
        assert altered == (16**B)*(C//(16**B)-1)+v
        assert altered%1==u%1
        assert altered.denominator==u.denominator
        assert (altered.numerator-u.numerator)%u.denominator==0
        measured=energy(altered,B)
        assert measured==exact
        assert measured<F(1,255*B)
        checks+=8
        for n in (0,1,B,max(0,2*B-1),2*B,2*B+1,3*B):
            shifted=states[n]+(16**n)*s
            assert odd_primary_class(shifted)==odd_primary_class(states[n])
            assert oddpart(shifted.denominator)==oddpart(states[n].denominator)
            if n>=2*B:
                assert (shifted-states[n]).denominator==1
                assert shifted%1==states[n]%1
                checks+=2
            checks+=2
        for A in (2*B,2*B+1):
            # Symbolic integer shifts certify every backward projection;
            # avoid needlessly squaring enormous entire A-shell fractions.
            for k in (1,A//2,A):
                displacement=F(16**(2*A),16**k)*s
                assert displacement.denominator==1
                assert torus(states[2*A]/16**k+displacement)==torus(states[2*A]/16**k)
                checks+=2
        for L in (1,3,7):
            Q=16**L
            a=(Q*v).numerator//(Q*v).denominator
            s_fine=-(F(M)+F(a,Q))/16**(2*B)
            residual=v-F(a,Q)
            fine=u+16**(2*B)*s_fine
            assert F(1,16**B)<=abs(s_fine)<F(2,16**B)
            assert 0<=residual<F(1,Q)
            assert energy(fine,B)==residual**2*(1-F(1,16**(2*B)))/(255*B)
            assert energy(fine,B)<F(1,255*B*Q*Q)
            assert odd_primary_class(fine)==odd_primary_class(u)
            assert (16**(2*B+L)*s_fine).denominator==1
            checks+=6
        # Mutation: changing the terminal value by one instead of the actual
        # trailing block is generally not the erasure asserted by E3/E4.
        wrong=energy(u+1,B)
        rows.append({'B':B,'authentic_R':float(energy(u,B)),
                     'erased_R':float(measured),'upper':1/(255*B),
                     'wrong_one_shift_rejected':wrong!=exact,
                     'seed_nonzero':True,'odd_class_preserved':True,
                     'terminal_fraction_preserved':True})
    assert sum(r['wrong_one_shift_rejected'] for r in rows)>=8
    checks+=1
    return {'status':'PASS','exact_assertions':checks,'shells':rows,
            'boundary':'finite calibration plus separately supplied proof; no R0 claim'}


if __name__=='__main__':
    print(json.dumps(run(),indent=2))
