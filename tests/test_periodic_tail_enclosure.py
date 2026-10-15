"""Exact tests for the sharp periodic-tail L2(w) enclosure.

All assertions are exact rational checks or independently-computed
bracketing checks; no floating-point certificate is asserted as a proof.
"""
import unittest
from fractions import Fraction as Q
from math import lcm

from observational_succ.periodic_tail_enclosure import (
    PeriodicTailError, defect_extremes, prefix_sum, residue,
    sharp_distance_interval, sharpening_report, value,
)
from observational_succ.zero_centered_residue import coefficients as zc_coeff


class TestResidueClock(unittest.TestCase):
    def test_residue_bounds_and_period(self):
        for n in (2, 3, 5, 7, 12):
            for k in range(1, 40):
                r = residue(k, n)
                self.assertGreaterEqual(r, 0)
                self.assertLess(r, 1)
                self.assertEqual(residue(k, n), residue(k + n, n))  # n-periodic

    def test_value_periodic_with_lcm(self):
        for fam in ({2: Q(1), 3: Q(1)}, {2: Q(2)}, {3: Q(-1), 4: Q(2), 6: Q(1)}):
            L = lcm(*fam)
            for k in range(1, 60):
                self.assertEqual(value(k, fam), value(k + L, fam))


class TestSharpEnclosure(unittest.TestCase):
    def test_exact_periodic_extremes_cover_defect(self):
        a = {2: Q(2), 3: Q(-1), 5: Q(1)}
        L = lcm(*a)
        m, M = defect_extremes(a)
        self.assertLessEqual(m, M)
        # every defect on the sampled period lies within [m, M] by construction
        for k in range(1, L + 1):
            d = (Q(1) - value(k, a)) ** 2
            self.assertLessEqual(m, d)
            self.assertLessEqual(d, M)

    def test_enclosure_ordered_and_positive_width(self):
        a = zc_coeff(4)  # the ZCR-04 perfect interpolant family
        lo, hi = sharp_distance_interval(a, K=128)
        self.assertLessEqual(lo, hi)
        self.assertGreater(hi, 0)

    def test_strictly_sharper_than_prior_bound(self):
        a = zc_coeff(4)
        r = sharpening_report(a, K=128)
        self.assertTrue(r["strictly_sharper_upper"])
        self.assertLess(Q(r["new_upper_coeff"]), Q(r["old_upper_coeff"]))
        # single clock is 4x sharper: M=1 vs (1+2)^2=9
        r2 = sharpening_report({2: Q(2)})
        self.assertEqual(Q(r2["new_upper_coeff"]), Q(1))
        self.assertEqual(Q(r2["old_upper_coeff"]), Q(9))

    def test_brackets_known_closed_form(self):
        # ||1 - 2 g_2||^2 = 1 - log 2  (independently: alternating harmonic tail)
        from decimal import Decimal, getcontext
        getcontext().prec = 40
        lo, hi = sharp_distance_interval({2: Q(2)}, K=256)
        # exact rationals -> Decimal for the comparison against the analytic value
        lo_d = Decimal(lo.numerator) / Decimal(lo.denominator)
        hi_d = Decimal(hi.numerator) / Decimal(hi.denominator)
        # 1 - ln 2, an analytic value computed by an independent route:
        #   sum_{j>=1} 1/[(2j)(2j+1)] = 1/2 - 1/3 + 1/4 - 1/5 + ... = 1 - ln 2
        truth = Decimal(1) - Decimal(2).ln()
        self.assertLess(lo_d, truth)
        self.assertLess(truth, hi_d)

    def test_lower_bound_strictly_positive_when_not_global(self):
        # a_2 = 1 does not interpolate 1 globally; its min defect over the
        # period is nonzero, so the lower bound must be strictly positive.
        r = sharpening_report({2: Q(1)}, K=64)
        self.assertTrue(r["strictly_positive_lower"])

    def test_rejects_float_and_empty(self):
        with self.assertRaises(PeriodicTailError):
            value(1, {})
        with self.assertRaises(PeriodicTailError):
            defect_extremes({2: 0.5})  # float coefficient forbidden


if __name__ == "__main__":
    unittest.main()


class TestRegressionRedTeam(unittest.TestCase):
    """Regression locks for the three red-team findings (2026-10-13)."""

    def test_lcm_beyond_k_budget_rejected_not_crash(self):
        # F1: lcm in (1e6, 1e8] used to crash inside residue(); now cleanly rejected.
        a = {999983: Q(1), 2: Q(1)}  # lcm = 1_999_966
        with self.assertRaises(PeriodicTailError):
            sharp_distance_interval(a, 64)
        with self.assertRaises(PeriodicTailError):
            defect_extremes(a)

    def test_all_zero_family_not_claimed_sharper(self):
        # F2: all-zero family has M == (1+sum|a|)^2 == 1; strictness is false.
        r = sharpening_report({2: Q(0)})
        self.assertFalse(r["strictly_sharper_upper"])
        self.assertEqual(Q(r["new_upper_coeff"]), Q(r["old_upper_coeff"]))

    def test_nonzero_family_still_sharper(self):
        self.assertTrue(sharpening_report({2: Q(2)})["strictly_sharper_upper"])
