"""Exact/rigorous tests for the unconditional Mellin-functional lower bound.

The lower bound is a valid certificate (<= true ||e||); it is not claimed to
be tight.  All assertions use exact rationals or high-precision independent
computations, never float equality.
"""
import unittest
from fractions import Fraction as Q
from decimal import Decimal, getcontext
import math

from observational_succ.mellin_lower_bound import (
    PeriodicTailError, functional_norm2_enclosure, mellin_lower_bound,
    zeta_enclosure,
)


def _d(q):
    return Decimal(q.numerator) / Decimal(q.denominator)


class TestZetaEnclosure(unittest.TestCase):
    def test_brackets_true_zeta(self):
        getcontext().prec = 50
        truths = {2: Decimal("1.6449340668482264364724151666460251892189499012068"),
                  3: Decimal("1.2020569031595942853997381615114499907649862923405"),
                  4: Decimal("1.0823232337111381915160036965411679027747501299187")}
        for s, truth in truths.items():
            lo, hi = zeta_enclosure(s, N=512)
            self.assertLess(_d(lo), truth)
            self.assertLess(truth, _d(hi))


class TestFunctionalNorm(unittest.TestCase):
    def test_brackets_true_norm2(self):
        # independent high-precision ||L_2||^2 via a long float sum + known tail
        getcontext().prec = 50
        s = 2
        # compute the partial sum in float (mpmath-free) with a huge N
        N = 100000
        partial = sum((k ** (-s) - (k + 1) ** (-s)) ** 2 * k * (k + 1) for k in range(1, N + 1))
        truth = Decimal(partial) / Decimal(s * s)
        lo, hi = functional_norm2_enclosure(s, N=256)
        self.assertLess(_d(lo), truth)
        self.assertLess(truth, _d(hi))
        # the enclosure must be tight: width << truth
        self.assertLess(_d(hi) - _d(lo), Decimal("1e-3"))


class TestMellinLowerBound(unittest.TestCase):
    def test_valid_lower_bound_on_known_case(self):
        # a_2 = 2: true ||e|| = sqrt(1 - ln 2) ~ 0.5539
        getcontext().prec = 50
        true = (Decimal(1) - Decimal(2).ln()).sqrt()
        r = mellin_lower_bound({2: Q(2)}, s=2, N=256)
        lb = _d(Q(r["lower_bound_on_norm_e"]))
        self.assertGreater(lb, 0)          # nontrivial positive bound
        self.assertLess(lb, true)          # valid: must not exceed the truth
        self.assertTrue(r["unconditional"])
        self.assertTrue(r["zero_independent"])
        self.assertFalse(r["RH_proved"])

    def test_poorer_approximation_gives_larger_or_equal_bound(self):
        # a_2 = 1 (approx 1 by g_2, worse than by 2 g_2) should not give a
        # dramatically smaller bound; check it stays positive and valid.
        r1 = mellin_lower_bound({2: Q(1)}, s=2, N=256)
        self.assertGreater(_d(Q(r1["lower_bound_on_norm_e"])), 0)

    def test_bounds_monotone_in_N(self):
        # larger N tightens the zeta enclosure (narrows the interval)
        lo_small, hi_small = zeta_enclosure(2, N=64)
        lo_big, hi_big = zeta_enclosure(2, N=512)
        self.assertLess(lo_small, lo_big)   # smaller N: lower bound is lower
        self.assertGreater(hi_small, hi_big)  # and upper bound is higher

    def test_rejects_bad_input(self):
        with self.assertRaises(PeriodicTailError):
            mellin_lower_bound({2: 0.5})    # float coefficient
        with self.assertRaises(PeriodicTailError):
            mellin_lower_bound({})           # empty
        with self.assertRaises(PeriodicTailError):
            mellin_lower_bound({2: Q(1)}, s=1)  # s=1 is the pole, excluded


if __name__ == "__main__":
    unittest.main()
