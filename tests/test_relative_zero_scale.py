"""Calibrated fixed-radius source observer and critical-carry scale separation.

No pi-digit normality claim: all explicit model measures are constructed controls.

Precision discipline (repair 2026-11-05): every mpmath evaluation runs inside a
locally scoped ``mp.workdps(DPS)`` block.  The original module set
``mp.mp.dps=55`` once at import time; in the full suite the global context is
later mutated by ``observational_succ/prime_form_heat.py`` (its helpers assign
``mp.mp.dps=dps`` and ``tests/test_prime_form_heat.py`` last calls them with
``dps=36``), so tests 04/05 ran at 36 digits and failed the 1e-43 tolerance
(CI run 42141608952; reproduced bit-exactly).  The tolerances below are
UNCHANGED; only the precision is now owned locally.  ``AmbientPrecisionHostile``
re-runs the numeric checks under hostile ambient precision as a regression.
"""
import unittest
from fractions import Fraction as F
import mpmath as mp

DPS = 55
TOL = '1e-43'


def z(q):
    return mp.mpf(q.numerator) / q.denominator


def coeff(R, h):
    if h == 0:
        return z(R)
    return (mp.e ** (2j * mp.pi * h * z(R)) - 1) / (2j * mp.pi * h)


class RelativeZeroScale(unittest.TestCase):
    def test_01_root_grid_exact_character_zeros(self):
        for q in (17, 257):
            for h in (1, 2, 3, 8, 16):
                self.assertNotEqual(h % q, 0)  # uniform q-grid Fourier exactly 0
                # Strengthened (was a bare residue check): evaluate the q-grid
                # character sum itself; it is an exact zero for q not | h.
                with mp.workdps(DPS):
                    s = mp.fsum(mp.expjpi(mp.mpf(2 * h * j) / q) for j in range(q))
                    self.assertLess(abs(s), mp.mpf('1e-45'))

    def test_02_full_fixed_radius_root_discrepancy_positive(self):
        with mp.workdps(DPS):
            r = mp.mpf('.5')
            for q in (3, 17, 257):
                exact = -mp.log1p(-r ** q) / q
                self.assertGreater(exact, 0)
                self.assertLess(abs(exact - mp.fsum(r ** (q * j) / (q * j) for j in range(1, 25))), mp.mpf('1e-18'))

    def test_03_r_derivative_jet_recovers_mode_power(self):
        # Q_r for a q-grid has Taylor series r^q/q+O(r^(2q));
        # all derivatives of orders 1..q-1 vanish at r=0,
        # and q-th derivative equals (q-1)!.
        from math import factorial
        import sympy as sp
        r = sp.symbols('r')
        for q in (2, 3, 5):
            for k in range(1, q):
                coeff_rk = (1 if k % q == 0 else 0) / k
                self.assertEqual(coeff_rk, 0)
            self.assertEqual(factorial(q) / q, factorial(q - 1))
            # Strengthened (the two lines above are arithmetic tautologies):
            # differentiate the actual q-grid functional -log(1-r^q)/q.
            Q = -sp.log(1 - r ** q) / q
            for k in range(1, q):
                self.assertEqual(sp.simplify(sp.diff(Q, r, k).subs(r, 0)), 0)
            self.assertEqual(sp.simplify(sp.diff(Q, r, q).subs(r, 0)), factorial(q - 1))

    def test_04_window_fourier_coefficient_vs_direct_integral(self):
        with mp.workdps(DPS):
            for R in (F(1, 7), F(1, 4), F(2, 5)):
                for h in (-3, -2, -1, 1, 2, 3):
                    # Direct integration on the B-folded unit cell, no pi digits.
                    direct = mp.quad(lambda y: mp.e ** (-2j * mp.pi * h * y), [1 - z(R), 1])
                    self.assertLess(abs(direct - coeff(R, h)), mp.mpf(TOL))

    def test_05_distributional_carry_derivative_boundary(self):
        with mp.workdps(DPS):
            for R in (F(1, 4), F(2, 5)):
                B = 16 ** 2
                for h in (1, 2, 3):
                    # D_x step Fourier coefficient is 2 pi i hB * c_h.
                    analytic = (2j * mp.pi * h * B) * coeff(R, h)
                    boundary = B * (mp.e ** (2j * mp.pi * h * z(R)) - 1)
                    self.assertLess(abs(analytic - boundary), mp.mpf(TOL))

    def test_06_fixed_radius_misses_critical_window(self):
        with mp.workdps(DPS):
            r = mp.mpf('.5'); R = F(1, 4); eps = mp.mpf(1)
            for B in (16, 256, 4096):
                # Density: 1+eps*cos(2pi B x). High-mode only.
                Q = (eps ** 2) * r ** B / (4 * B)
                bias = eps * mp.sin(2 * mp.pi * z(R)) / (2 * mp.pi)
                self.assertGreater(abs(bias), mp.mpf('.15'))
                self.assertLess(Q, mp.mpf('0.000001') if B >= 256 else mp.mpf('.0001'))
                self.assertAlmostEqual(float(z(R) + bias), float(mp.mpf('.25') + 1 / (2 * mp.pi)), places=13)

    def test_07_source_null_jet_is_degenerate_at_fixed_frequency(self):
        # Polynomial algebra: d^k/dlambda^k exp(i*kappa*(u+lambda*z))
        # at lambda0 equals (i*kappa*z)^k exp(i*kappa*u).
        import sympy as sp
        v, lam, t = sp.symbols('v lam t')
        f = sp.exp(t * lam * v)
        for k in (1, 2, 3):
            self.assertEqual(sp.simplify(sp.diff(f, lam, k).subs(lam, 0)), t ** k * v ** k)

    def test_08_fixed_radius_quadratic_has_no_third_measure_jet(self):
        import sympy as sp
        t, a, b, q = sp.symbols('t a b q', real=True)
        quadratic = q * (a + t * b) ** 2
        self.assertEqual(sp.diff(quadratic, t, 3), 0)
        self.assertEqual(sp.diff(quadratic, t, 2), 2 * q * b * b)


class AmbientPrecisionHostile(unittest.TestCase):
    """Regression for the CI order dependence: the numeric checks must hold
    whatever global precision an earlier test leaked (36 = the observed leak)."""

    def test_numeric_checks_independent_of_ambient_dps(self):
        saved = mp.mp.dps
        try:
            for ambient in (15, 36, 40, 120):
                mp.mp.dps = ambient
                case = RelativeZeroScale()
                case.test_01_root_grid_exact_character_zeros()
                case.test_02_full_fixed_radius_root_discrepancy_positive()
                case.test_04_window_fourier_coefficient_vs_direct_integral()
                case.test_05_distributional_carry_derivative_boundary()
                case.test_06_fixed_radius_misses_critical_window()
                self.assertEqual(mp.mp.dps, ambient)  # tests no longer mutate global state
        finally:
            mp.mp.dps = saved


if __name__ == '__main__':
    unittest.main()
