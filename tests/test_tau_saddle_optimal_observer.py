"""Independent exact/rational checks for SUCC radial saddle threshold.

The moments use only the authenticated eight BBP radial rational taps, an
independent geometric-tail formula and a rigorous rational truncation bound.
No pi digits or numerical root-fitting enter proof checks.
"""
from __future__ import annotations
import unittest
from fractions import Fraction as Q
from math import sqrt

RAD=(Q(2),Q(-2),Q(-1),Q(-2),Q(-1,2),Q(-1,2),Q(1,4),Q(0))

def beta_fraction(a:Q, k:int)->Q:
    z=1/a
    for j in range(1,k+1):
        z=z*j/(a+j)
    return z

def moment_interval(n:int,k:int,T:int=24):
    """Return rigorous rational interval for I_k=(1-E)^k Z_n.

    Z_n=-sum_{m>=1}16**-m r_rad(n+m), and the finite difference
    of each pole has an EXACT rational beta integral. The omitted
    geometric tail is bounded term-by-term, since B(a,k+1) decreases in a.
    """
    estimate=Q(0); tail_abs=Q(0)
    for j,w in enumerate(RAD,1):
        if not w: continue
        for m in range(1,T+1):
            a=Q(n+m-1)+Q(j,8)
            estimate -= (w/Q(8))*Q(1,16**m)*beta_fraction(a,k)
        tail_abs+=abs(w)*beta_fraction(Q(n+T)+Q(j,8),k)
    tail_abs*=Q(1,120*16**T) # 1/(8*15) * 16**(-T)
    return estimate-tail_abs,estimate+tail_abs

def certified_sign(n:int,k:int)->int:
    lo,hi=moment_interval(n,k)
    if lo>0:return 1
    if hi<0:return -1
    raise AssertionError('uncertified sign: increase T')

class TauSaddle(unittest.TestCase):
    def test_01_original_radial_coefficients(self):
        assert RAD==(Q(2),Q(-2),Q(-1),Q(-2),Q(-1,2),Q(-1,2),Q(1,4),Q(0))
        self.assertEqual(sum(RAD),Q(-15,4))

    def test_02_exact_moment_crossing_n1(self):
        self.assertEqual(certified_sign(1,56),1)
        self.assertEqual(certified_sign(1,57),-1)

    def test_03_exact_moment_crossing_n2(self):
        self.assertEqual(certified_sign(2,125),1)
        self.assertEqual(certified_sign(2,126),-1)

    def test_04_exact_moment_crossing_n3(self):
        self.assertEqual(certified_sign(3,196),1)
        self.assertEqual(certified_sign(3,197),-1)

    def test_05_exact_moment_crossing_n5(self):
        self.assertEqual(certified_sign(5,338),1)
        self.assertEqual(certified_sign(5,339),-1)

    def test_06_radial_root_polynomial_identity(self):
        # If tau=2-sqrt(2), then tau^2-4*tau+2=0;
        # P_rad(tau)=0 follows by polynomial factorization of 4P_rad.
        import sympy as sp
        x=sp.symbols('x')
        p=sum(sp.Rational(w.numerator,w.denominator)*x**j
              for j,w in enumerate(RAD))
        q,rem=sp.div(p,x*x-4*x+2,domain=sp.QQ)
        self.assertEqual(rem,0)
        self.assertNotEqual(q,0)
        self.assertEqual(sp.simplify(p.subs(x,2-sp.sqrt(2))),0)

    def test_07_exact_algebraic_saddle_ratio(self):
        import sympy as sp
        x=2-sp.sqrt(2)
        ratio=sp.simplify(x**(-8)-1)
        self.assertEqual(ratio,sp.Rational(561,16)+sp.Rational(51,2)*sp.sqrt(2))
        self.assertAlmostEqual(float(ratio),71.12494584051392,places=10)

    def test_08_saddle_rho_sign_orientation(self):
        import sympy as sp
        x=sp.symbols('x');t=2-sp.sqrt(2)
        p=sum(sp.Rational(w.numerator,w.denominator)*x**j for j,w in enumerate(RAD))
        self.assertEqual(sp.simplify(sp.diff(p,x).subs(x,t)),96-72*sp.sqrt(2))
        self.assertLess(float(sp.diff(p,x).subs(x,t)),0)
        self.assertEqual(sp.simplify(p.subs(x,1)),sp.Rational(-15,4))

    def test_09_b_first_coefficients_independent(self):
        import sympy as sp
        s=sp.symbols('s')
        v=1-(1-s)**sp.Rational(1,8)
        f=4*v*(16/(1-s)-1)/(1-2*v-v*v)
        series=sp.series(f,s,0,5).removeO().expand()
        self.assertEqual([series.coeff(s,j) for j in range(1,5)],
            [sp.Rational(15,2),sp.Rational(421,32),sp.Rational(4551,256),sp.Rational(179123,8192)])

    def test_10_lambert_w_is_secondary_envelope_not_root(self):
        import mpmath as mp
        mp.mp.dps=45
        tau=2-mp.sqrt(2); sigma=1-tau**8
        delta=-mp.log(sigma)
        phi=lambda a:a*mp.log(a/sigma)-(1+a)*mp.log(1+a)
        a0=mp.findroot(phi,(400,650))
        w=-mp.lambertw(-delta/mp.e,-1)/delta
        self.assertGreater(a0,500)
        self.assertLess(a0,530)
        self.assertLess(abs(a0-w),mp.mpf('0.1'))
        self.assertLess(abs(phi(a0)),mp.mpf('1e-37'))


    def test_11_preregistered_fresh_crossing_n7(self):
        self.assertEqual(certified_sign(7,480),1)
        self.assertEqual(certified_sign(7,481),-1)

    def test_12_preregistered_fresh_crossing_n11(self):
        self.assertEqual(certified_sign(11,764),1)
        self.assertEqual(certified_sign(11,765),-1)

    def test_13_preregistered_fresh_crossing_n13(self):
        self.assertEqual(certified_sign(13,907),1)
        self.assertEqual(certified_sign(13,908),-1)

if __name__=='__main__':unittest.main()
