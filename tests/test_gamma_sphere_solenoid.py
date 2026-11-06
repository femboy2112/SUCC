"""Exact source-linked Gaussian sphere / Gamma lenses. Research tests only.

Run: python -m unittest -v test_gamma_sphere_solenoid.py
Requires SymPy and mpmath. No pi digits used as source inputs.
"""
import unittest
from fractions import Fraction

import mpmath as mp
import sympy as s

x, z = s.symbols('x z', real=True)
I = s.I
A, B = 1+I, 1-I
u, ub = A/2, B/2
D = (x-1)**2+1
F = (2-x*x)/D
KA = 4/D
KR = s.cancel(2*s.diff(F,x)/F)
q = (x-A)/(x-B)
W = s.cancel(-I*(2-x*x)/(x-B)**2)
WBAR = s.cancel(I*(2-x*x)/(x-A)**2)
tau = 2-s.sqrt(2)
H = lambda y: (y-1)/(y+1)
HINV = lambda y: (y+1)/(1-y)
LP = s.cancel(H(u*HINV(z)))

TAPS = (Fraction(4),0,0,Fraction(-2),Fraction(-1),Fraction(-1),0,0)
ANG = (Fraction(2),Fraction(2),Fraction(1),0,Fraction(-1,2),Fraction(-1,2),Fraction(-1,4),0)
RAD = tuple(a-b for a,b in zip(TAPS,ANG))

def force(n, taps=TAPS):
    return sum((Fraction(w,8*(n-1)+j) for j,w in enumerate(taps,1)),Fraction(0))

def states(nmax,taps=TAPS):
    acc=Fraction(0)
    for n in range(1,nmax+1):
        acc=16*acc+force(n,taps)
        yield acc

def tail(n,count=46):
    return sum((force(n+k)*Fraction(1,16**k) for k in range(1,count+1)),Fraction(0))

def tail_bound(n,count=46):
    # Original r(m) positive, <4/(8m-7), and decreases via this upper envelope.
    return Fraction(4,8*(n+count+1)-7)*Fraction(1,15*16**count)

class GaussianSphereTests(unittest.TestCase):
    def setUp(self):
        self._original_mp_dps = mp.mp.dps

    def tearDown(self):
        mp.mp.dps = self._original_mp_dps

    def assertzero(self, expr):
        self.assertEqual(s.simplify(s.cancel(expr)), 0)

    def test_01_gaussian_atomic_scale_and_phase(self):
        self.assertzero(u/ub-I)
        self.assertzero(u**8-s.Rational(1,16))
        self.assertzero(ub**8-s.Rational(1,16))
        self.assertzero(A*B-2)

    def test_02_rational_semicircle(self):
        self.assertzero(W-(u-ub*q*q))
        self.assertzero((W-u)*(WBAR-ub)-s.Rational(1,2))
        self.assertzero(W.subs(x,0)-1)
        self.assertzero(W.subs(x,1)-I)
        self.assertzero(W.subs(x,tau)-(1+I))
        self.assertzero(KA**2-2*s.diff(W,x)*s.diff(WBAR,x))

    def test_03_chiral_dlog_and_residue(self):
        self.assertzero(KA-I*KR+2*I*s.diff(W,x)/W)
        self.assertzero(KA+I*KR-2*I*s.diff(WBAR,x)/WBAR)
        expected_a = {A:-2*I,B:2*I,s.sqrt(2):0,-s.sqrt(2):0}
        expected_r = {A:-2,B:-2,s.sqrt(2):2,-s.sqrt(2):2}
        for p,v in expected_a.items():
            self.assertzero(s.residue(KA,x,p)-v)
        for p,v in expected_r.items():
            self.assertzero(s.residue(KR,x,p)-v)
        self.assertzero(s.residue(KA-I*KR,x,A))
        self.assertzero(s.residue(KA+I*KR,x,B))

    def test_04_source_full_pole_reduction(self):
        p=lambda taps: sum(s.Rational(w.numerator,w.denominator)*x**j for j,w in enumerate(taps))
        denom=1-x**8/s.Integer(16)
        self.assertzero(p(TAPS)/denom-KA-KR)
        self.assertzero(p(ANG)/denom-KA)
        self.assertzero(p(RAD)/denom-KR)
        mutant=(Fraction(5),)+TAPS[1:]
        self.assertzero(p(mutant)/denom-KA-KR-1/denom)

    def test_05_exact_beta_pullback(self):
        sin2=x*(2-x)/D
        cos2=2*(1-x)/D
        self.assertzero(sin2**2+cos2**2-1)
        beta_coordinate=sin2**2
        self.assertzero(s.diff(beta_coordinate,x)/(sin2*cos2)-KA)
        self.assertzero(sin2.subs(x,0))
        self.assertzero(sin2.subs(x,1)-1)
        self.assertzero(s.tan(s.pi/8)-(s.sqrt(2)-1))

    def test_06_orthogonal_mobius_axes_and_noncommutativity(self):
        self.assertzero(H(s.Integer(0))+1)
        self.assertzero(LP-((u-1)+(u+1)*z)/((u+1)+(u-1)*z))
        self.assertzero(LP.subs(z,-1)+1)
        self.assertzero(LP.subs(z,1)-1)
        diff = s.cancel(u*LP.subs(z,0)-LP.subs(z,0))
        self.assertzero(diff-(-1-3*I)/10)
        self.assertNotEqual(s.simplify(diff),0)
        # Use homogeneous CP1 coordinates: some intermediate iterates hit infinity.
        matrix = s.Matrix([[u+1,u-1],[u-1,u+1]])
        h_matrix=s.Matrix([[1,-1],[1,1]])
        hinv_matrix=s.Matrix([[1,1],[-1,1]])
        for initial in (s.Rational(1,3),s.Rational(3,5),I):
            start=s.Matrix([initial,1])
            end=matrix**8*start
            expected=h_matrix*s.diag(u**8,1)*hinv_matrix*start
            self.assertzero(end[0]*expected[1]-end[1]*expected[0])
        mid=matrix**4*s.Matrix([s.Rational(3,5),1])
        self.assertzero(mid[1])  # exactly infinity: ordinary affine iteration fails here.

    def test_07_spherical_metric_jacobian(self):
        # For complex w, |H'(w)|^2/(1+|H(w)|^2)^2=1/(1+|w|^2)^2.
        p,q=s.symbols('p q', real=True)
        modz=p*p+q*q
        hden=(p+1)**2+q*q
        hnum=(p-1)**2+q*q
        modh=hnum/hden
        hprime_sq=4/hden**2
        self.assertzero(hprime_sq/(1+modh)**2-1/(1+modz)**2)
        # Euclidean metric without Jacobian is not preserved.
        self.assertNotEqual(s.simplify(hprime_sq.subs({p:0,q:0})),1)

    def test_08_exact_source_and_wrong_seed_holdout(self):
        src=list(states(37))
        ang=list(states(37,ANG))
        rad=list(states(37,RAD))
        for n in (11,19,37):
            self.assertEqual(src[n-1],ang[n-1]+rad[n-1])
            self.assertGreater(rad[n-1],0)
            self.assertLess(rad[n-1],Fraction(1,32*n+16))
            self.assertGreater(tail(n),0)
            self.assertLess(tail_bound(n),Fraction(1,10**20))
            # Source time U_n and the same-forcing coherent wrong seed -T_n differ.
            # Their analytic KA,KR,W are identical and therefore cannot select a seed.
            self.assertNotEqual(src[n-1] % 1,(-tail(n))%1)
        self.assertNotEqual(force(11), force(11,(Fraction(5),)+TAPS[1:]))

    def test_09_gamma_carrier_nonhaar_with_independent_periodization(self):
        mp.mp.dps=35
        L=mp.log(16)
        def density(v):
            return sum((mp.exp(v+j*L-mp.exp(v+j*L)) for j in range(-26,3)))
        for k in (0,1,3,4,8):
            omega=2*mp.pi*k/L
            numeric=mp.quad(lambda v:density(v)*mp.exp(-1j*omega*v),[0,L/2,L])
            analytic=mp.gamma(1-1j*omega)
            self.assertLess(abs(numeric-analytic),mp.mpf('2e-26'))
            if k==0:
                self.assertLess(abs(numeric-1),mp.mpf('2e-26'))
            else:
                self.assertGreater(abs(analytic),mp.mpf('1e-35'))
        # Positive Gamma density is NOT the uniform log16-circle law.
        self.assertGreater(abs(mp.gamma(1-2j*mp.pi/L)),mp.mpf('0.1'))

    def test_10_gamma_vs_succ_measure_lens(self):
        derivative=s.diff(s.exp(-x)*D/4,x)
        self.assertzero(derivative+s.exp(-x)*(x-2)**2/4)
        self.assertzero((s.exp(-x)*D/4).subs(x,0)-s.Rational(1,2))
        self.assertzero((s.exp(-x)*D/4).subs(x,1)-s.exp(-1)/4)
        mp.mp.dps=45
        self.assertLess(abs(mp.quad(lambda v:4/((v-1)**2+1),[0,1])-mp.pi),mp.mpf('1e-42'))
        self.assertLess(abs(mp.quad(lambda v:mp.exp(-v),[0,1])-(1-1/mp.e)),mp.mpf('1e-42'))

if __name__=='__main__':
    unittest.main()
