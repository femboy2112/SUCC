"""Focused original-BBP circle observer and radix collision-pressure controls.

Original unwrapped states, source and near-periodic completions use Fraction.
Trigonometric functions are final-stage finite diagnostics, NOT a proof of
pi's base-16 normality. Theorems are stated separately in PROOFS.md.
"""
from __future__ import annotations
from fractions import Fraction as Q
from functools import lru_cache
from math import pi
import cmath
import unittest

TAPS=(Q(4),Q(),Q(),Q(-2),Q(-1),Q(-1),Q(),Q())
ANG=(Q(2),Q(2),Q(1),Q(),Q(-1,2),Q(-1,2),Q(-1,4),Q())
RAD=(Q(2),Q(-2),Q(-1),Q(-2),Q(-1,2),Q(-1,2),Q(1,4),Q())

def injection(n,taps=TAPS):
    return sum((w/Q(8*(n-1)+j) for j,w in enumerate(taps,1)),Q())

def independent_injection(n):
    return Q(120*n*n-89*n+16,(2*n-1)*(4*n-1)*(8*n-7)*(8*n-3))

@lru_cache(None)
def source_states(N):
    out=[(Q(),Q(),Q())];u=y=z=Q()
    for n in range(1,N+1):
        u=16*u+independent_injection(n)
        y=16*y+injection(n,ANG)
        z=16*z+injection(n,RAD)
        assert u==y+z
        out.append((u,y,z))
    return tuple(out)

def pressure(values,m):
    M=16**m
    counts={}
    for v in values:
        f=(Q(v)%1)*M
        k=f.numerator//f.denominator
        counts[k]=counts.get(k,0)+1
    N=len(values)
    return Q(M*sum(c*c for c in counts.values()),N*N)

def tail(n,J=42):
    return sum((independent_injection(n+k)/16**k for k in range(1,J+1)),Q())

def alpha_interval(M):
    low=sum((independent_injection(n)/16**n for n in range(1,M+1)),Q())
    high=low+independent_injection(M+1)/Q(15*16**M)
    return low,high

def near_periodic(p):
    low,high=alpha_interval(p+10)
    q=16**p-1
    a=(q*low+Q(1,2)); b=(q*high+Q(1,2))
    k1=a.numerator//a.denominator
    k2=b.numerator//b.denominator
    assert k1==k2
    beta=Q(k1,q)
    dist=max(abs(beta-low),abs(beta-high))
    assert dist<=Q(1,2*q)
    return beta,dist

def char(v):
    return cmath.exp(2j*pi*float(Q(v)%1))

class YonedaCollisionPressure(unittest.TestCase):
    def test_01_original_signed_four_pole_source(self):
        self.assertEqual(injection(1),Q(47,15))
        self.assertEqual(tuple(ANG[i]+RAD[i] for i in range(8)),TAPS)
        for n in (1,2,5,17,53,97):
            self.assertEqual(injection(n),independent_injection(n))
            self.assertGreater(injection(n),0)

    def test_02_exact_source_paired_fiber_natural_isomorphism(self):
        states=source_states(53)
        self.assertEqual(states[0],(Q(),Q(),Q()))
        for n,(u,y,z) in enumerate(states):
            c=Q(16)**n
            a,b=c+u/2,c-u/2
            self.assertEqual(a+b,2*c)
            self.assertEqual(a-b,u)
            if n<53:
                r=independent_injection(n+1)
                an,bn=16*a+r/2,16*b-r/2
                self.assertEqual(an-bn,states[n+1][0])
                self.assertEqual(an+bn,2*Q(16)**(n+1))

    def test_03_exact_circle_character_source_naturality(self):
        states=source_states(54)
        for n in (1,2,9,17,25,53):
            for h in (-3,-1,1,4,7):
                self.assertEqual((h*states[n][0])%1,
                    (16*h*states[n-1][0]+h*independent_injection(n))%1)
                self.assertEqual((h*states[n][0])%1,
                    (h*states[n][1]+h*states[n][2])%1)

    def test_04_original_forcing_summability_source_only(self):
        self.assertLess(Q(47,15)+Q(1920,2457),4)
        acc=Q()
        for n in range(1,257):
            acc+=independent_injection(n)
            if n>=2:self.assertLessEqual(independent_injection(n),Q(1920,2457*n*n))
        self.assertLess(acc,4)

    def test_05_same_four_pole_periodic_completions_near_zero(self):
        for p in (3,5,7,9):
            beta,err=near_periodic(p)
            self.assertLessEqual(err,Q(1,2*(16**p-1)))
            self.assertLess(16**(p-2)*err,Q(1,250))
            for n in (0,1,p-2,p,p+4):
                self.assertEqual((16**(n+p)*beta-16**n*beta).denominator,1)

    def test_06_hex_cell_pressure_exact_monotone(self):
        for A in (96,192,384):
            states=source_states(2*A-1)
            values=[states[n][0] for n in range(A,2*A)]
            ps=[pressure(values,m) for m in (1,2,3,4)]
            self.assertTrue(all(ps[j]<=ps[j+1] for j in range(3)))
            self.assertTrue(all(v>=1 for v in ps))

    def test_07_predeclared_original_finite_occupancies(self):
        expected={
            96:(Q(347,288),Q(11,3),Q(136,3)),
            192:(Q(599,576),Q(9,4),Q(68,3)),
            384:(Q(607,576),Q(491,288),Q(71,6))}
        for A,vals in expected.items():
            st=source_states(2*A-1)
            actual=tuple(pressure([st[n][0] for n in range(A,2*A)],m)
                         for m in (1,2,3))
            self.assertEqual(actual,vals)

    def test_08_same_source_coherent_wrong_seed_clusters(self):
        for A in (96,192,384):
            wrong=[-tail(n) for n in range(A,2*A)]
            for m in (1,2,3):
                self.assertEqual(pressure(wrong,m),16**m)
            # Bound future tail from the exact positive rational source.
            self.assertLess(tail(A),Q(128,2457*A*A))

    def test_09_uniform_roots_are_collision_minimizers(self):
        for m in (1,2,3):
            M=16**m
            roots=[Q(j,M) for j in range(M)]
            self.assertEqual(pressure(roots,m),1)

    def test_10_half_circle_overcrowds_but_obeys_finite_upper_bound(self):
        for m in (1,2):
            M=16**m
            half=[Q(j,2*M) for j in range(M)]
            self.assertEqual(pressure(half,m),2)
            self.assertNotEqual((16*half[1])%1,half[1]%1)

    def test_11_invariant_biased_bernoulli_digit_pressure_diverges(self):
        digit_weights=[Q(1,2)]+[Q(1,30)]*15
        self.assertEqual(sum(digit_weights),1)
        qsum=sum(w*w for w in digit_weights)
        self.assertEqual(qsum,Q(4,15))
        vals=[(16*qsum)**m for m in range(1,6)]
        self.assertEqual(vals,[Q(64,15)**m for m in range(1,6)])
        self.assertTrue(all(vals[i]<vals[i+1] for i in range(4)))

    def test_12_actual_source_approximate_fourier_invariance(self):
        for N in (64,128,256):
            us=source_states(N)
            exact_R=sum((independent_injection(n) for n in range(1,N+1)),Q())
            for h in (-2,1,3):
                m_h=sum(char(h*us[n][0]) for n in range(N))/N
                m_16h=sum(char(16*h*us[n][0]) for n in range(N))/N
                B=(2+2*pi*abs(h)*float(exact_R))/N
                self.assertLessEqual(abs(m_h-m_16h),B+1e-12)

    def test_13_different_invariant_measures_have_same_dynamics(self):
        for point in (Q(),Q(1,15)):
            self.assertEqual((16*point)%1,point)
        self.assertEqual(16*Q(1,16),1)

    def test_14_finite_sample_refinement_order_is_not_time_limit(self):
        finite=[Q(j,16) for j in range(16)]
        self.assertEqual(pressure(finite,1),1)
        self.assertEqual(pressure(finite,2),16)
        self.assertEqual(pressure(finite,3),256)

    def test_15_mutated_four_pole_forcing_is_not_authenticated(self):
        altered=list(TAPS);altered[0]+=1
        self.assertNotEqual(injection(1,tuple(altered)),independent_injection(1))
        # The affine paired-isomorphism algebra survives changed forcing;
        # therefore it alone cannot authenticate ORIGINAL source identity.
        for n in (1,2,3):
            r=injection(n,tuple(altered));x=Q(3,17)
            self.assertEqual((16*(1+x/2)+r/2)-(16*(1-x/2)-r/2),16*x+r)

if __name__=='__main__':unittest.main()
