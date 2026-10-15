"""Regression locks for the exact Gram/Möbius structural identities (T1-T4).

The identities are PROVED in research/2026-10-13/GRAM_MOBIUS_IDENTITIES.md;
these tests pin the numerical values so the exact statements cannot silently
drift.  High-precision mpmath, not a rational certificate.
"""
import unittest
import mpmath as mp
from math import lcm

from observational_succ.gram_mobius import (
    S_r, gram, mobius_cancellation, single_clock_optimum, target_inner,
)

mp.mp.dps = 50


class TestTargetInnerProduct(unittest.TestCase):
    def test_T1_one_equals_logn_over_n(self):
        # <1, r_n> = log(n)/n, partial sum at N=200000 is within ~1/N of exact
        for n in (2, 3, 5, 7, 11):
            got = target_inner(n, N=200_000)
            want = mp.log(n) / n
            self.assertLess(abs(got - want), mp.mpf('2e-4'))


class TestSingleClockOptimum(unittest.TestCase):
    def test_T2_exact_closed_form(self):
        r = single_clock_optimum()
        self.assertAlmostEqual(float(r["G_22"]), float(mp.log(2) / 4), places=14)
        self.assertAlmostEqual(float(r["b_2"]), float(mp.log(2) / 2), places=14)
        # a_opt = 2 exactly, E_2* = 1 - log 2 exactly
        self.assertAlmostEqual(float(r["a_opt"]), 2.0, places=14)
        self.assertTrue(r["E_2_star_is_1_minus_log2"])


class TestMobiusCancellation(unittest.TestCase):
    def test_T3_for_s_2_3_4(self):
        for s in (2, 3, 4):
            r = mobius_cancellation(s, N=200_000)
            # partial sum converges to -1/zeta(s); truncation error ~ 1/(N zeta-ish)
            self.assertLess(r["error"], mp.mpf('5e-4'))


class TestGramClosedForm(unittest.TestCase):
    def test_T4_diagonal_and_consistency(self):
        # G(2,2) = log2/4 exactly
        self.assertAlmostEqual(float(gram(2, 2)), float(mp.log(2) / 4), places=14)
        # sum over residues: S_r sums to 1 (telescoping <1,1> = 1)
        for L in (3, 4, 5, 6, 12):
            tot = mp.fsum(S_r(L, r) for r in range(1, L + 1))
            self.assertAlmostEqual(float(tot), 1.0, places=12)


if __name__ == "__main__":
    unittest.main()
