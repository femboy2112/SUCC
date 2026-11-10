"""Exact tests for the lag-1 source autocorrelation bound (F-6)."""
import unittest
from fractions import Fraction as Q

from observational_succ import source_lag1_autocorrelation as lag
from observational_succ import duck_bbp


class Lag1AutocorrelationTests(unittest.TestCase):
    def test_bound_holds_many(self):
        for n in range(1, 500):
            self.assertLess(lag.lag1_product(n), lag.lag1_bound(n), n)

    def test_bound_is_asymptotically_sharp_constant(self):
        # r(n) ~ 15/(4 n^2), so r(n)r(n+1) ~ (15/4)^2/(n(n+1))^2; the bound has
        # the correct asymptotic constant (no wasted factor).
        self.assertEqual(lag.lag1_bound(1), Q(225, 16) / 4)

    def test_positive_coefficient_certificate(self):
        c = lag.polynomial_positive_coefficients()
        self.assertTrue(c['all_positive'])
        self.assertGreater(c['min'], 0)

    def test_forcing_positive(self):
        for n in range(1, 50):
            self.assertGreater(duck_bbp.forcing(n), 0)


if __name__ == '__main__':
    unittest.main()
