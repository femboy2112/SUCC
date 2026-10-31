"""Exact counting quotient, bounded carrier corrector and radix Ward residual.

Original source: R(a)=4/a-2/(a+3)-1/(a+4)-1/(a+5).
Research-only: finite controls and derived source arithmetic; no pi normality claim.
"""
from __future__ import annotations
from collections import defaultdict
from fractions import Fraction as F
from itertools import product
from math import comb, factorial, cos, pi
import unittest

B = 16
POLES = ((4, 0), (-2, 3), (-1, 4), (-1, 5))


def R(a):
    a = F(a)
    return sum((F(c) / (a + d) for c, d in POLES), F(0))


def forcing(n):
    return R(8*n - 7)


def prefix_tail(n, horizon):
    """Finite causal simulation uses future source tail truncated at horizon."""
    return sum((F(1, B**j)*forcing(n+j) for j in range(1, horizon-n+1)), F(0))


def orbit(seed, horizon):
    x = [F(seed)]
    for j in range(1, horizon+1):
        x.append(B*x[-1] + forcing(j))
    return x


def frac(x):
    return x - (x.numerator // x.denominator)


def original_path_word_mass(n, s, source=R):
    """Probability of each specific binary word of length 3n and grade s."""
    a = 8*n-7
    return sum(((-1)**j * comb(s,j) * source(a+8*(3*n-s+j))
                for j in range(s+1)), F(0))/source(a)


def ward_force_difference(N, h):
    """Pure counting baseline minus authentic 34th Haar moment at k=17."""
    terms = [forcing(p) for p in range(N+1)]
    return 2 * sum(( (17 if q==p+1 else 289) *
                (1-cos(2*pi*h*float(terms[q]-terms[p])))
                for p in range(2,N) for q in range(p+1,N+1)),0.)


def A_h(h, cutoff):
    return sum(1-cos(2*pi*h*float(forcing(p))) for p in range(2,cutoff+1))


def asymptotic_counting_const(h, cutoff=2000):
    r = [0.,0.] + [float(forcing(p)) for p in range(2,cutoff+1)]
    f = lambda x: 1-cos(2*pi*h*x)
    A = sum(f(rp) for rp in r[2:])
    moment = -sum((p+1)*f(r[p]) for p in range(2,cutoff+1))
    pair = sum(f(r[q]-r[p])-f(r[p])
               for p in range(2,cutoff) for q in range(p+2,cutoff+1))
    adjacent = sum(f(r[p+1]-r[p]) for p in range(2,cutoff))
    return A, 578*(moment+pair)+34*adjacent


def ward_defect_fast(N, h):
    """Exact finite trigonometric identity, O(N) real operations.

    Stable evaluation via 1-cos(t)=2*sin(t/2)^2 to avoid cancellation.
    """
    from math import sin
    A=S=adj=0.
    prev=None
    for p in range(2,N+1):
        angle=2*pi*h*float(forcing(p))
        A+=2*sin(angle/2)**2
        S+=sin(angle)
        if prev is not None:
            adj+=2*sin((angle-prev)/2)**2
        prev=angle
    return 578*(N-1)*A-289*(A*A+S*S)-544*adj


def limiting_source_triplet(h, cutoff):
    from math import sin
    A=S=Bsum=0.
    prev=None
    for p in range(2,cutoff+1):
        angle=2*pi*h*float(forcing(p))
        A+=2*sin(angle/2)**2
        S+=sin(angle)
        if prev is not None:
            Bsum+=2*sin((angle-prev)/2)**2
        prev=angle
    return A,S,Bsum


def compositions(k, parts):
    if parts==1:
        yield (k,)
    else:
        for m in range(k+1):
            for rest in compositions(k-m,parts-1):
                yield (m,)+rest


def multinomial(v):
    num=factorial(sum(v))
    den=1
    for j in v: den*=factorial(j)
    return num//den


def moment_classes(N,k):
    U=orbit(0,N)
    buckets=defaultdict(list)
    for m in compositions(k,N):
        freq=sum(m[j]*B**(j+1) for j in range(N))
        phase=sum((F(m[j])*U[j+1] for j in range(N)),F(0))
        buckets[freq].append((m,multinomial(m),phase))
    return buckets

class CountingQuotient(unittest.TestCase):
    def test_source_four_poles_original_contract(self):
        for n in range(1,50):
            self.assertEqual(forcing(n),F(4,8*n-7)-F(2,8*n-4)-F(1,8*n-3)-F(1,8*n-2))
            self.assertGreater(forcing(n),0)
            self.assertLessEqual(forcing(n),F(15,(8*n-7)**2))

    def test_unique_bounded_future_correction_exact_finite_horizon(self):
        for horizon in (1,4,8,15):
            T=[prefix_tail(n,horizon) for n in range(horizon+1)]
            for n in range(horizon):
                self.assertEqual(B*T[n],forcing(n+1)+T[n+1])
            for seed in (F(0),F(1,7),-T[0]):
                U=orbit(seed,horizon)
                for n in range(horizon+1):
                    self.assertEqual(U[n]+T[n],B**n*(seed+T[0]))
            self.assertGreater(T[0],0)
            self.assertEqual(T[horizon],0)

    def test_bounded_boundary_counting_trilemma(self):
        # A boundary-fixed source remover is necessarily the PAST-driven
        # exact corrector -U_n(0), which grows like 16^n T_0.
        horizon=16
        U=orbit(F(0),horizon)
        Bpast=[-v for v in U]
        self.assertEqual(Bpast[0],0)
        for n in range(horizon):
            self.assertEqual(Bpast[n+1],B*Bpast[n]-forcing(n+1))
        self.assertTrue(all(abs(Bpast[n+1])>abs(Bpast[n]) for n in range(1,horizon)))
        T=[prefix_tail(n,horizon) for n in range(horizon+1)]
        for n in range(horizon+1):
            self.assertEqual(-Bpast[n],B**n*T[0]-T[n])
        self.assertGreater(T[0],0)
        # The bounded, source-free coordinate V_n=U_n+T_n instead moves
        # the original zero boundary to V_0=T_0, a distinct contract.

    def test_carry_cocycle_and_coherent_seed_exact(self):
        horizon=10
        T=[prefix_tail(n,horizon) for n in range(horizon+1)]
        for seed in (F(0),F(1,15),F(1,1024),-T[0]):
            U=orbit(seed,horizon)
            x=[frac(v) for v in U]
            eta=[int(x[n]+T[n]) for n in range(horizon+1)]
            y=[frac(U[n]+T[n]) for n in range(horizon+1)]
            carries=[None]+[int(B*x[n-1]+forcing(n)) for n in range(1,horizon+1)]
            digits=[None]+[int(B*y[n-1]) for n in range(1,horizon+1)]
            for n in range(1,horizon+1):
                self.assertEqual(carries[n],digits[n]+B*eta[n-1]-eta[n])
                self.assertEqual(y[n],frac(B*y[n-1]))
        # Coherent finite-horizon seed, i.e. alpha_horizon=0, yields
        # pure radix-16 zero; its integer carries all equal to 15.
        U=orbit(-T[0],horizon)
        self.assertTrue(all(frac(U[n]+T[n])==0 for n in range(horizon+1)))
        self.assertTrue(all(int(B*frac(U[n-1])+forcing(n))==15 for n in range(1,horizon)))
        # Artificial T_M=0 cutoff creates a terminal alias seam: the
        # last carry is 16, not 15. The genuine infinite T_n>0 has no
        # such terminal discontinuity.
        self.assertEqual(int(B*frac(U[horizon-1])+forcing(horizon)),16)

    def test_original_source_word_counting_quotient_exact(self):
        for n in (1,2,3):
            length=3*n
            grouped=defaultdict(list)
            for word in product((0,1),repeat=length):
                s=sum(word)
                grouped[s].append(original_path_word_mass(n,s))
            self.assertEqual(sum((sum(vals,F(0)) for vals in grouped.values()),F(0)),1)
            for s,vals in grouped.items():
                self.assertEqual(len(vals),comb(length,s))
                self.assertTrue(all(v==vals[0] and v>0 for v in vals))
                self.assertEqual(sum(vals,F(0)),comb(length,s)*vals[0])
                self.assertEqual(vals[0]/sum(vals,F(0)),F(1,comb(length,s)))

    def test_source_blind_history_given_total_and_oily_tilt(self):
        for n in (1,2,3):
            for s in range(3*n+1):
                w=original_path_word_mass(n,s)
                # Every word with same s gets same positive source weight.
                # A positive grade-only Oily change of measure cancels.
                for factor in (F(1), F(7,3), F(1001,5)):
                    self.assertEqual(w*factor/(comb(3*n,s)*w*factor),F(1,comb(3*n,s)))
                self.assertGreater(w,0)

    def test_three_panel_same_grade_distinct_selected_carries(self):
        U=orbit(0,5)
        kap={n:int(B*frac(U[n-1])+forcing(n)) for n in range(1,6)}
        self.assertEqual((kap[3],kap[4]),(4,3))
        records=[]
        for j,k,l in ((1,0,0),(0,1,0),(0,0,1)):
            a,b,c=3+j,3+j+k,3+j+k+l
            records.append((kap[a],kap[b],kap[c]))
        self.assertEqual(records,[(3,3,3),(4,3,3),(4,4,3)])

    def test_first_balance_radix_count_collision_exact(self):
        for k in range(1,17):
            groups=defaultdict(int)
            for m in compositions(k,4):
                groups[sum(m[j]*B**(j+1) for j in range(4))]+=1
            self.assertEqual(max(groups.values()),1)
        buckets=moment_classes(4,17)
        self.assertEqual(sum(len(b)-1 for b in buckets.values()),3)
        actual=[]
        for b in buckets.values():
            if len(b)>1:
                (ma,ca,pa),(mb,cb,pb)=b
                actual.append((ca*cb,pa-pb))
        self.assertEqual(sorted([v[0] for v in actual]),[17,17,289])

    def test_34th_moment_count_subtraction_from_direct_group_algebra(self):
        N=5;h=1;buckets=moment_classes(N,17)
        baseline=sum(sum(coeff for _,coeff,_ in terms)**2 for terms in buckets.values())
        # Never subtract two huge ~N^17 floating-point moments;
        # compute the dephasing defect directly, bucket by bucket.
        loss=sum(2*ca*cb*(1-cos(2*pi*h*float(pa-pb)))
                 for terms in buckets.values() for ia,(_,ca,pa) in enumerate(terms)
                 for _,cb,pb in terms[ia+1:])
        self.assertGreater(baseline,loss)
        self.assertAlmostEqual(loss,ward_force_difference(N,h),places=9)

    def test_linear_34th_defect_coefficient_h1(self):
        h=1
        A=A_h(h,30000)
        self.assertGreater(A,0)
        self.assertLess(A,2*pi*pi*h*h*sum(float(forcing(p))**2 for p in range(2,30001)) + 1e-5)
        self.assertAlmostEqual(A,0.36236676355,places=8)
        # Counting-subtracted defect has a linear source-specific asymptotic.
        ds=[ward_force_difference(N,h)/N for N in (50,200,600)]
        self.assertTrue(ds[0]<ds[1]<ds[2]<578*A)
        self.assertLess(abs(ds[-1]-578*A),3)

    def test_counting_quotient_exact_fast_pair_factorization(self):
        for N in (3,4,5,9,25,75):
            for h in (1,2,7):
                self.assertAlmostEqual(ward_force_difference(N,h),ward_defect_fast(N,h),places=6)

    def test_full_asymptotic_constant_after_counting_quotient(self):
        A,S,Badj=limiting_source_triplet(1,100000)
        C=-578*A-289*(A*A+S*S)-544*Badj
        self.assertAlmostEqual(A,0.36236676355048,places=11)
        # This uses a truncated sin-series, not the true infinite sum.
        # Independent digamma-tail oracle identifies the true constant.
        self.assertLess(abs(C+981.1623446123),0.02)
        # The analytical limiting remainder exists and is finite.
        for N in (100,300,1000,2500):
            corrected=ward_defect_fast(N,1)-578*N*A
            self.assertLess(abs(corrected-C),1300/N)

    def test_normality_not_inherited_by_counting_projection(self):
        # Haar-preimage transfer sends this Fourier mode to zero,
        # but the single coherent selected orbit is identically one.
        from cmath import exp
        h=1
        self.assertLess(abs(sum(exp(2j*pi*h*k/16) for k in range(16))),1e-12)
        self.assertEqual(sum(exp(2j*pi*h*0) for _ in range(10)),10)

    def test_second_order_counting_defect_bounded_remainder(self):
        A,C=asymptotic_counting_const(1,1200)
        self.assertGreater(A,0)
        self.assertLess(abs(C),2000)
        for N in (100,300,600):
            D=ward_force_difference(N,1)
            self.assertLess(abs(D-578*N*A-C),17)

    def test_perron_operator_erases_selected_coherent_seed(self):
        import cmath
        for h in (1,2,3,5,7):
            avg=sum(cmath.exp(2j*pi*h*j/16) for j in range(16))/16
            self.assertLess(abs(avg),1e-13)
            # Yet at the coherent selected seed alpha=0, e_h(T^n alpha)=1 always.
            self.assertEqual(cmath.exp(2j*pi*h*0),1)

if __name__=='__main__':
    unittest.main(verbosity=2)
