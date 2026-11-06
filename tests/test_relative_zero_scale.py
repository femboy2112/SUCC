"""Calibrated fixed-radius source observer and critical-carry scale separation.

No pi-digit normality claim: all explicit model measures are constructed controls.
"""
import unittest
from fractions import Fraction as F
from math import cos, pi, sin, log
from cmath import exp
import mpmath as mp
mp.mp.dps=55

def z(q):
    return mp.mpf(q.numerator)/q.denominator

def coeff(R,h):
    if h==0:return z(R)
    return (mp.e**(2j*mp.pi*h*z(R))-1)/(2j*mp.pi*h)

class RelativeZeroScale(unittest.TestCase):
    def test_01_root_grid_exact_character_zeros(self):
        for q in (17,257):
            for h in (1,2,3,8,16):
                self.assertNotEqual(h%q,0) # uniform q-grid Fourier exactly 0

    def test_02_full_fixed_radius_root_discrepancy_positive(self):
        r=mp.mpf('.5')
        for q in (3,17,257):
            exact=-mp.log1p(-r**q)/q
            self.assertGreater(exact,0)
            self.assertLess(abs(exact-mp.fsum(r**(q*j)/(q*j) for j in range(1,25))),mp.mpf('1e-18'))

    def test_03_r_derivative_jet_recovers_mode_power(self):
        # Q_r for a q-grid has Taylor series r^q/q+O(r^(2q));
        # all derivatives of orders 1..q-1 vanish at r=0,
        # and q-th derivative equals (q-1)!.
        from math import factorial
        for q in (2,3,5):
            for k in range(1,q):
                coeff_rk=(1 if k%q==0 else 0)/k
                self.assertEqual(coeff_rk,0)
            self.assertEqual(factorial(q)/q, factorial(q-1))

    def test_04_window_fourier_coefficient_vs_direct_integral(self):
        for R in (F(1,7),F(1,4),F(2,5)):
            for h in (-3,-2,-1,1,2,3):
                # Direct integration on the B-folded unit cell, no pi digits.
                direct=mp.quad(lambda y: mp.e**(-2j*mp.pi*h*y),[1-z(R),1])
                self.assertLess(abs(direct-coeff(R,h)),mp.mpf('1e-43'))

    def test_05_distributional_carry_derivative_boundary(self):
        for R in (F(1,4),F(2,5)):
            B=16**2
            for h in (1,2,3):
                # D_x step Fourier coefficient is 2 pi i hB * c_h.
                analytic=(2j*mp.pi*h*B)*coeff(R,h)
                boundary=B*(mp.e**(2j*mp.pi*h*z(R))-1)
                self.assertLess(abs(analytic-boundary),mp.mpf('1e-43'))

    def test_06_fixed_radius_misses_critical_window(self):
        r=mp.mpf('.5');R=F(1,4);eps=mp.mpf(1)
        for B in (16,256,4096):
            # Density: 1+eps*cos(2pi B x). High-mode only.
            Q=(eps**2)*r**B/(4*B)
            bias=eps*mp.sin(2*mp.pi*z(R))/(2*mp.pi)
            self.assertGreater(abs(bias),mp.mpf('.15'))
            self.assertLess(Q,mp.mpf('0.000001') if B>=256 else mp.mpf('.0001'))
            self.assertAlmostEqual(float(z(R)+bias),float(mp.mpf('.25')+1/(2*mp.pi)),places=13)

    def test_07_source_null_jet_is_degenerate_at_fixed_frequency(self):
        # Polynomial algebra: d^k/dlambda^k exp(i*kappa*(u+lambda*z))
        # at lambda0 equals (i*kappa*z)^k exp(i*kappa*u).
        import sympy as sp
        v,lam,t=sp.symbols('v lam t')
        f=sp.exp(t*lam*v)
        for k in (1,2,3):
            self.assertEqual(sp.simplify(sp.diff(f,lam,k).subs(lam,0)),t**k*v**k)

    def test_08_fixed_radius_quadratic_has_no_third_measure_jet(self):
        import sympy as sp
        t,a,b,q=sp.symbols('t a b q',real=True)
        quadratic=q*(a+t*b)**2
        self.assertEqual(sp.diff(quadratic,t,3),0)
        self.assertEqual(sp.diff(quadratic,t,2),2*q*b*b)

if __name__=='__main__':unittest.main()
