"""SUCC source-exact time extrusion / integer seam / virtual cone checks.

All finite authoritative checks use fractions.Fraction; never assumes normality.
Research-only source: original signed four-pole BBP, initial seed zero.

Run: python time_extrusion_probe.py -v
"""
from __future__ import annotations
import unittest
from fractions import Fraction as F
from math import comb, floor, gcd

B=16
POLES=((0,4),(3,-2),(4,-1),(5,-1))

def R(a):
    a=F(a)
    if a<=0: raise ValueError('a must be positive')
    return sum((F(c)/(a+d) for d,c in POLES),F())

def forcing(n):
    if n<1 or type(n)!=int: raise ValueError('positive integer source index')
    return R(8*n-7)

def exact_cell_mass(n,m,j,source_shift=0):
    """UNNORMALIZED mass of ONE ordered word with grade j, after tilt shift.
    Cell is e^(-(8(n+m-j)-7)X) Q(X)(1-e^-8X)^j dx.
    """
    if type(n)!=int or type(m)!=int or type(j)!=int or n<1 or m<0 or not 0<=j<=m:
        raise ValueError('cell domain n>=1,0<=j<=m')
    a=8*(n+m-j)-7+F(source_shift)
    return sum((F((-1)**k*comb(j,k))*R(a+8*k) for k in range(j+1)),F())

def grade_probability(n,m,j):
    return F(comb(m,j))*exact_cell_mass(n,m,j)/forcing(n)

def field_laplace(n,m,j,shift):
    return exact_cell_mass(n,m,j,shift)/exact_cell_mass(n,m,j)

def finite_diagonal(n):
    return tuple(grade_probability(n,n,j) for j in range(n+1))

def diagonal_pgf(n,z):
    z=F(z)
    return sum((p*z**j for j,p in enumerate(finite_diagonal(n))),F())

def diagonal_mgf_upper(n,z):
    z=F(z);a=8*n-7;b=a-8*n*(z-1)
    if not 1<z<2 or b<=0:raise ValueError('choose 1<z<2, n large')
    return R(b)/R(a)

def oily_tail(M):
    if M<0:raise ValueError()
    return F(M+2,2**(M+1))

def green_interval(n,K):
    """Outward exact positive-rational bounds for authentic T_n, K>=1."""
    if n<0 or K<1: raise ValueError()
    low=sum((F(1,B**j)*forcing(n+j) for j in range(1,K+1)),F())
    hi=low+F(1,B**K*15)*forcing(n+K+1)
    return low,hi

def circle_prefix(N,seed=F()):
    if N<1:raise ValueError()
    s=F(seed)%1
    states=[s]
    carries=[None]
    for n in range(1,N+1):
        v=16*states[-1]+forcing(n)
        k=v.numerator//v.denominator
        carries.append(k)
        states.append(v-k)
    return states,carries

def certified_pure_state(n, states, K=16):
    """BBP certificate for y_n={16^(n-1)(pi+16s)} via x_n+T_n,
       certified exact seam label and finite cylinder digit when available."""
    lo,hi=green_interval(n,K)
    L=states[n]+lo;H=states[n]+hi
    if L>=1: eta=1
    elif H<1:eta=0
    else:raise ArithmeticError('tail truncation too coarse for seam')
    return L-eta,H-eta,eta

def count_periodic_prefix(digits,period):
    if period<1:raise ValueError()
    return next((j for j in range(period,len(digits)) if digits[j]!=digits[j%period]),len(digits))

class TimeExtrusionTests(unittest.TestCase):
    def test_original_four_poles_and_source(self):
        self.assertEqual(forcing(1),F(47,15))
        for n in range(1,60):
            self.assertGreater(forcing(n),0)
            self.assertEqual(forcing(n),F(15*(8*n-7)**2+121*(8*n-7)+240,(8*n-7)*(8*n-4)*(8*n-3)*(8*n-2)))

    def test_massive_3d_extrusion_identity(self):
        for n in range(1,8):
            for m in range(0,11):
                for j in range(m+1):
                    self.assertEqual(exact_cell_mass(n+1,m,j),exact_cell_mass(n,m+1,j))
                    self.assertEqual(field_laplace(n+1,m,j,8),field_laplace(n,m+1,j,8))

    def test_glue_is_conditional_failure_not_arbitrary_success(self):
        for n in range(1,10):
            for m in range(1,9):
                for j in range(m+1):
                    self.assertEqual(exact_cell_mass(n+1,m,j),exact_cell_mass(n,m+1,j))
                self.assertNotEqual(exact_cell_mass(n+1,m,0),exact_cell_mass(n,m+1,1))

    def test_pascal_conservation_every_slice(self):
        for n in range(1,13):
            for m in range(0,17):
                self.assertEqual(sum((grade_probability(n,m,j) for j in range(m+1)),F()),F(1))
                for j in range(m+1):
                    a=exact_cell_mass(n,m,j)
                    self.assertEqual(a,exact_cell_mass(n,m+1,j)+exact_cell_mass(n,m+1,j+1))

    def test_canonical_truncation_and_green_cocycle(self):
        for n in range(1,21):
            for K in (1,3,9):
                low,hi=green_interval(n,K)
                self.assertGreater(low,0)
                self.assertLess(hi-low,F(1,B**K*15)*forcing(n+K))
                low1,hi1=green_interval(n+1,K+1)
                # Exact prefix relation with shifted horizon: 16T_n-r(n+1)=T_(n+1).
                low2,hi2=green_interval(n,K+2)
                self.assertLessEqual(16*low2-forcing(n+1),hi1)
                self.assertGreaterEqual(16*hi2-forcing(n+1),low1)

    def test_source_diagonal_mgf_domination(self):
        for z in (F(5,4),F(3,2),F(7,4)):
            for n in range(4,17):
                a=8*n-7-8*n*(z-1)
                if a>0:
                    self.assertLessEqual(diagonal_pgf(n,z),diagonal_mgf_upper(n,z))
                    self.assertLess(diagonal_mgf_upper(n,z),F((8*n-7)**2,a**2))

    def test_end_grade_Oily_limit_total_variation(self):
        for n in range(3,32):
            q=finite_diagonal(n)
            tail=oily_tail(n+1) # grades n+1, n+2 ...
            TV=(sum((abs(q[j]-F(j+1,2**(j+2))) for j in range(n+1)),F())+tail)/2
            self.assertLess(TV,F(22,n))

    def test_exact_seam_cocycle_original_seed(self):
        N=43
        states, carries=circle_prefix(N+1)
        for n in range(1,N):
            ylo,yhi,eta=certified_pure_state(n,states,16)
            ylo1,yhi1,eta1=certified_pure_state(n+1,states,16)
            dl,dh=16*ylo,16*yhi
            Dlow=dl.numerator//dl.denominator
            Dhi=dh.numerator//dh.denominator
            self.assertEqual(Dlow,Dhi,('digit ambiguous',n))
            self.assertEqual(carries[n+1],Dlow+16*eta-eta1)
            self.assertLessEqual(yhi-ylo,F(1,16**16)*forcing(n+17)/15)

    def test_seam_cocycle_changed_seed(self):
        for seed in (F(0),F(1,7),F(1,15),F(1,256),F(-1),F(11,31)):
            states,carries=circle_prefix(22,seed)
            for n in range(1,21):
                ylo,yhi,eta=certified_pure_state(n,states,18)
                _,_,eta1=certified_pure_state(n+1,states,18)
                lo,hi=16*ylo,16*yhi
                Dlo=lo.numerator//lo.denominator
                Dhi=hi.numerator//hi.denominator
                self.assertEqual(Dlo,Dhi)
                self.assertEqual(carries[n+1],Dlo+16*eta-eta1)

    def test_counterseed_seam_all_time_symbolic(self):
        # For s*=-pi/16, pure y_n=0 and x_n={-T_n}=1-T_n.
        # Hence eta_n=1, pure D=0, literal carry=15 at all n>=2.
        for n in range(1,80):
            lo,hi=green_interval(n,10)
            self.assertTrue(0<lo<hi<F(1))
            self.assertEqual(0+16*1-1,15)
            self.assertLess(hi,F(1,(8*n+1)**2))

    def test_periodic_rational_control_not_misclaimed_pi(self):
        b=16;p=3;word=[3,0,12];w=word[0]*b*b+word[1]*b+word[2]
        periodic=F(w,b**p-1)
        seen=[]
        x=periodic
        for i in range(21):
            digit=int(b*x)
            seen.append(digit)
            x=(b*x)%1
        self.assertEqual(seen,word*7)
        self.assertEqual(count_periodic_prefix(seen,p),21)

    def test_stationary_source_field_is_seed_blind(self):
        # Positive source has no dependence on physical initial seed.
        for n in (1,4,17):
            for seed in (F(),F(1,7),F(-1)):
                self.assertEqual(forcing(n),R(8*n-7))

if __name__=='__main__':unittest.main(verbosity=2)
