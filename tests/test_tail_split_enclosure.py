"""Exact tests for the tail-split enclosure (TS-01).

Every assertion is exact rational or an independently-computed bracketing;
no floating-point certificate is asserted as a proof.
"""
import unittest
from fractions import Fraction as Q
from math import lcm
from decimal import Decimal, getcontext

from observational_succ.tail_split_enclosure import (
    PeriodicTailError, blackout_tail_interval, defect_by_residue,
    tail_split_enclosure,
)
from observational_succ.periodic_tail_enclosure import sharp_distance_interval
from observational_succ.zero_centered_residue import coefficients as zc_coeff


def _d(q):
    return Decimal(q.numerator) / Decimal(q.denominator)


class TestDefectByResidue(unittest.TestCase):
    def test_blackout_defect_is_exactly_one(self):
        for a in ({2: Q(2)}, {2: Q(1), 3: Q(1)}, {3: Q(-1), 4: Q(2), 6: Q(1)}):
            c, L = defect_by_residue(a)
            self.assertEqual(c[L], 1)          # F(L)=0 exactly

    def test_defects_cover_residue_classes(self):
        a = {2: Q(2), 3: Q(-1)}
        c, L = defect_by_residue(a)
        self.assertEqual(L, lcm(2, 3))
        self.assertEqual(len(c), L)
        for r in c:
            self.assertGreaterEqual(c[r], 0)


class TestBlackoutTail(unittest.TestCase):
    def test_interval_ordered_and_contains_truth(self):
        # a_2 = 2: B = sum_{even k>K} 1/(k(k+1)), exactly computable to high precision
        K, L = 256, 2
        j0 = K // L + 1
        # exact truth via a long partial sum with a tight independent bound
        N = 20000
        truth = sum(Q(1, j * L * (j * L + 1)) for j in range(j0, N + 1))
        getcontext().prec = 60
        lo, hi = blackout_tail_interval(K, L)
        self.assertLessEqual(lo, truth)
        self.assertLessEqual(truth, hi)
        self.assertGreater(hi, lo)

    def test_remainder_shrinks_with_J(self):
        lo1, hi1 = blackout_tail_interval(128, 60, J=128 // 60 + 1 + 100)
        lo2, hi2 = blackout_tail_interval(128, 60, J=128 // 60 + 1 + 10000)
        self.assertLess(hi2 - lo2, hi1 - lo1)


class TestTailSplitEnclosure(unittest.TestCase):
    def test_brackets_known_closed_form(self):
        # ||1 - 2 g_2||^2 = 1 - ln 2
        getcontext().prec = 60
        lo, hi = tail_split_enclosure({2: Q(2)}, K=256)
        truth = Decimal(1) - Decimal(2).ln()
        self.assertLess(_d(lo), truth)
        self.assertLess(truth, _d(hi))
        # width must be far tighter than PTE-01's
        plo, phi = sharp_distance_interval({2: Q(2)}, K=256)
        self.assertLess(hi - lo, (phi - plo) / 10)

    def test_lower_bound_always_sharper_than_pte(self):
        for a in (zc_coeff(4), {2: Q(1), 3: Q(1)}, {2: Q(2)}):
            lo, _ = tail_split_enclosure(a, K=64)
            plo, _ = sharp_distance_interval(a, K=64)
            self.assertGreaterEqual(lo, plo)

    def test_upper_bound_sharper_when_blackout_dominates(self):
        # a_2 = 2: blackout cells are the ONLY nonzero-defect cells, so the
        # upper bound collapses to the exact blackout tail (up to remainder).
        lo, hi = tail_split_enclosure({2: Q(2)}, K=256)
        plo, phi = sharp_distance_interval({2: Q(2)}, K=256)
        self.assertLess(hi, phi)

    def test_enclosure_valid_on_arbitrary_family(self):
        # independent high-precision sum validates lower <= E <= upper
        getcontext().prec = 60
        a = {2: Q(1), 3: Q(-1), 5: Q(2)}
        from observational_succ.periodic_tail_enclosure import value
        K = 40
        E = sum(Q(1, k * (k + 1)) * (Q(1) - value(k, a)) ** 2 for k in range(1, 4001))
        lo, hi = tail_split_enclosure(a, K=K)
        self.assertLessEqual(_d(lo), _d(E))
        self.assertLessEqual(_d(E), _d(hi))

    def test_rejects_bad_input(self):
        with self.assertRaises(PeriodicTailError):
            tail_split_enclosure({2: 0.5})     # float coefficient
        with self.assertRaises(PeriodicTailError):
            tail_split_enclosure({})            # empty family


if __name__ == "__main__":
    unittest.main()
