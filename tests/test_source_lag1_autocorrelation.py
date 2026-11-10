"""Exact tests for the lag-1 source autocorrelation bound (F-6)."""
import unittest
from fractions import Fraction as Q

from observational_succ import source_lag1_autocorrelation as lag
from observational_succ import duck_bbp


class Lag1AutocorrelationTests(unittest.TestCase):
    def test_bound_holds_many(self):
        for n in range(1, 500):
            self.assertLess(lag.lag1_product(n), lag.lag1_bound(n), n)

    def test_legacy_bound_constant_is_not_asymptotically_sharp(self):
        # Keep the legacy finite value, but test the actual leading rational
        # coefficients independently: numerator 120, denominator 2*4*8*8.
        self.assertEqual(lag.lag1_bound(1), Q(225, 16) / 4)
        self.assertEqual(lag.SOURCE_ASYMPTOTIC_CONSTANT, Q(120, 2*4*8*8))
        self.assertEqual(lag.LAG_ASYMPTOTIC_CONSTANT, Q(225, 4096))
        n = 10000
        scaled = lag.lag1_product(n)*(n*(n+1))**2
        self.assertLess(abs(scaled-lag.LAG_ASYMPTOTIC_CONSTANT), Q(1, 10000))
        self.assertGreater(abs(scaled-Q(225, 16)), 14)

    def test_sharp_envelope_against_four_original_poles(self):
        for n in (1, 2, 5, 31, 127, 997):
            for k in (1, 3, 97, 100003):
                def source(t):
                    return Q(4, 8*t-7)-Q(2, 8*t-4)-Q(1, 8*t-3)-Q(1, 8*t-2)
                lo, hi = lag.sharp_lag_envelope(n, k)
                product = source(n)*source(n+k)
                self.assertLess(lo, product)
                self.assertLess(product, hi)
                self.assertLess(hi, lag.lagk_bound(n, k))

    def test_positive_coefficient_certificate(self):
        c = lag.polynomial_positive_coefficients()
        self.assertTrue(c['all_positive'])
        self.assertGreater(c['min'], 0)

    def test_forcing_positive(self):
        for n in range(1, 50):
            self.assertGreater(duck_bbp.forcing(n), 0)

    def test_uniform_lagk_bound(self):
        for n in range(1, 60):
            for k in range(1, 60):
                self.assertLess(lag.lagk_product(n, k), lag.lagk_bound(n, k), (n, k))

    def test_lagk_coefficients_all_positive(self):
        for name, coeffs in lag.lagk_polynomial_coefficients():
            for c in coeffs:
                self.assertGreater(c, 0, (name, c))

    def test_full_polynomial_identity_by_independent_symbolic_expansion(self):
        import sympy as sp
        t, k = sp.symbols('t k')
        def numerator(x):
            return 120*x*x-89*x+16
        def denominator(x):
            return (2*x-1)*(4*x-1)*(8*x-7)*(8*x-3)
        n = t+1
        difference = sp.expand(sp.Rational(225, 16)*denominator(n)*denominator(n+k)
                               - numerator(n)*numerator(n+k)*n*n*(n+k)**2)
        coefficients = [sp.Rational(c.numerator, c.denominator) if isinstance(c, Q)
                        else sp.Integer(c) for c in lag.polynomial_positive_coefficients()['coeffs']]
        self.assertEqual(sp.Poly(difference.subs(k, 1), t).all_coeffs(), coefficients)
        for (name, expected), actual in zip(lag.lagk_polynomial_coefficients(),
                                            sp.Poly(difference, t).all_coeffs()):
            parsed = [sp.Rational(c.numerator, c.denominator) if isinstance(c, Q)
                      else sp.Integer(c) for c in expected]
            self.assertEqual(sp.Poly(actual, k).all_coeffs(), parsed, name)


if __name__ == '__main__':
    unittest.main()
