#!/usr/bin/env python3
"""Unit tests for the zero-selected-carry continuation (CARRY_FLUX.md).

Fast (calibration shells only) plus exhaustive small-case checks, mutation controls
and the regression for the repaired IAD-04 progression corollary.  Nothing here
tests, or could test, any open claim.
"""
from __future__ import annotations

import json
import math
import sys
import unittest
from fractions import Fraction as F
from pathlib import Path

_HERE = Path(__file__).resolve().parent
if str(_HERE) not in sys.path:
    sys.path.insert(0, str(_HERE))

import iad_core as ic  # noqa: E402
import probe_zsc as pz  # noqa: E402
import zsc_core as zc  # noqa: E402


class QuickProbe(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.res, cls.ok = pz.run(quick=True)

    def test_all_theorem_grade_checks_pass(self):
        self.assertTrue(self.ok, self.res["meta"])
        self.assertGreater(self.res["meta"]["theorem_grade_checks"], 40000)
        self.assertEqual(self.res["meta"]["theorem_grade_failures"], 0)

    def test_mutation_controls_are_rejected(self):
        m = self.res["mutation_controls_rejected"]
        for key in ("ZM-1", "ZM-2", "ZM-3", "ZM-4", "ZM-5"):
            self.assertTrue(m[key], key)
        # the preregistered ZM-1 input was mis-specified; it must stay recorded as such
        self.assertFalse(m["ZM-1_preregistered_input"])

    def test_zero_seed_has_no_seam_on_quick_horizon(self):
        z = self.res["ZC-6_case_table"]["zero_seed"]
        self.assertEqual((z["seam_positions"], z["sixteen_events"], z["max_carry"]), (0, 0, 15))


class CommittedResults(unittest.TestCase):
    def test_committed_results_record_a_clean_full_run(self):
        res = json.loads((_HERE / "RESULTS_zsc.json").read_text())
        self.assertFalse(res["meta"]["quick"])
        self.assertTrue(res["meta"]["all_theorem_grade_pass"])
        self.assertEqual(res["meta"]["holdout_shells"], [243, 420, 811, 1210])
        self.assertEqual(res["meta"]["theorem_grade_failures"], 0)
        self.assertEqual(sorted(res["predictions"]), ["ZP-1", "ZP-2", "ZP-3", "ZP-4", "ZP-5"])


class IAD04Repair(unittest.TestCase):
    def test_iad04_progression_occupied_cells(self):
        S = ic.Source(300)
        # the retired display is false at the audit's counterexample: singleton cells, negative bound
        lhs, rhs = pz.iad04_retired_display(S, 100, 1, 1, 1000)
        self.assertAlmostEqual(lhs, 1.0, places=12)
        self.assertLess(rhs, 0)
        # the hypothesis checker of the repaired statement rejects it (q > B - l)
        with self.assertRaises(AssertionError):
            pz.iad04_repaired_holds(S, 100, 1, 1, 1000)
        # and the repaired statement holds on occupied cells, including q = B - l
        for B, ell, h, q in ((64, 2, 1, 62), (64, 4, 1, 7), (128, 5, 1, 3), (100, 2, 1, 98)):
            ok, lhs, rhs = pz.iad04_repaired_holds(S, B, ell, h, q)
            self.assertTrue(ok, (B, ell, h, q, lhs, rhs))


class SavingExponentLaw(unittest.TestCase):
    def test_stretch_lemma_is_tight_on_an_antialigned_tail(self):
        B, N = 64, 34
        d = [3] * B + [0] * N + [7] * (2 * B + zc.TRUNC)
        fr = pz.fracs_of(d, 2 * B + 2)
        reW = pz.shell(pz.prefix(pz.phases(fr, 1)), B).real
        self.assertGreaterEqual(reW, (2 * N - B) / B - 1e-9)           # (1.1) with ||16^m xi|| = 0
        self.assertLess(reW, (2 * N - B + 1) / B)                      # and no better by 1/B

    def test_law_exponent_values(self):
        for eta, expo in ((F(1), F(1, 3)), (F(1, 2), F(3, 5)), (F(2, 3), F(1, 2))):
            self.assertEqual((2 - eta) / (2 + eta), expo)
            # choice of N and B in the proof
            for m in range(math.ceil((2 + eta) / eta), 400):
                N = math.ceil(m * (2 - eta) / (2 + eta)) + 1
                B = -((-(m + N)) // 2)
                self.assertTrue(1 <= N <= m and m <= 2 * B and B <= m and m + N <= 2 * B)
                self.assertGreaterEqual(2 * N - (2 - eta) * B, eta)

    def test_shallit_point_is_coherent_on_dyadic_shells(self):
        d = zc.shallit_digits(1200)
        fr = pz.fracs_of(d, 1100)
        self.assertLessEqual(ic.dist_to_int(fr[256]), F(2, 16 ** zc.TRUNC) + F(2, 16 ** 256))
        self.assertGreater(pz.shell(pz.prefix(pz.phases(fr, 1)), 512).real, 0.999)


class LocalityLemma(unittest.TestCase):
    def test_exhaustive_grid(self):
        """Both parts of the lemma for every y = i/(15*256*8), i.e. a grid 8 times finer than the
        threshold, using exact two-digit expansions."""
        den = 15 * 256 * 8
        for i in range(den):
            y = F(i, den)
            d0 = int(16 * y)
            d1 = int(16 * (16 * y - d0))
            t = zc.dist15(y)
            if d0 == d1:
                self.assertLessEqual(t, F(15, 256))
            if t < F(1, 256):
                self.assertEqual(d0, d1, i)
        # the threshold 1/256 is attained: equality case has a change
        y = F(14, 15) + F(1, 15 * 256)                                  # = 239/256 = 0.EF
        self.assertEqual(zc.dist15(y), F(1, 256))
        self.assertNotEqual(int(16 * y), int(16 * (16 * y - int(16 * y))))


class Renewal(unittest.TestCase):
    def test_J_bounds(self):
        for n in range(1, 3000):
            J = zc.renewal_J(n)
            self.assertGreater(4 ** (J + 1), 2 * n)                    # J >= floor(log_4 2n)
            self.assertLessEqual(F(16, 15) * 16 ** J * ic.r(n + 1), 1)
            self.assertGreater(F(16, 15) * 16 ** (J + 1) * ic.r(n + 1), 1)

    def test_sixteen_is_followed_by_J_zeros(self):
        t = pz.Tally()
        pz.renewal_direct(t, range(1, 120))
        self.assertEqual(t.bad, [])


class SourceModuli(unittest.TestCase):
    def test_rank_and_null_vector(self):
        rank, ker = zc.baker_rank()
        self.assertEqual(rank, 7)
        self.assertEqual([c * 8 / ker[0][0] for c in ker[0]], [F(c) for c in zc.A_NULL])

    def test_null_relation_by_antiderivative_endpoints(self):
        # F(z) = (1/2) log|z^2 - 2| - (1/2) log(z^2 - 2z + 2) vanishes at 0 and at 1:
        self.assertEqual(abs(0 - 2), 0 * 0 - 2 * 0 + 2)                # |z^2-2| = z^2-2z+2 at z = 0
        self.assertEqual(abs(1 - 2), 1 - 2 + 2)                        # and at z = 1
        lo, hi = zc.L_enclosure(zc.A_NULL)
        self.assertTrue(lo < 0 < hi)

    def test_hostile_source_is_coherent_with_zero_seed(self):
        H = zc.GSource(zc.G_HOSTILE, 200)
        self.assertEqual(H.U[0], 0)
        self.assertEqual(sum(zc.G_HOSTILE), 0)
        for n in range(1, 201):
            T = 2 * 16 ** n - H.U[n]
            self.assertTrue(0 < T < F(3, 8 * n + 1))
        self.assertTrue(all(k == 15 for k in H.carries()[2:]))
        self.assertEqual(zc.proper_form(zc.G_HOSTILE), (tuple(F(c) for c in zc.A_NULL), F(2)))

    def test_carries_and_seam_are_not_gauge_invariant(self):
        """Audit finding D4: (g_H, 0) and its proper form (A_0, 2) are gauge-equivalent with the
        same completed point 2, yet their literal carries are 15 and 0 respectively."""
        g_proper, seed = zc.proper_form(zc.G_HOSTILE)
        self.assertEqual(seed, 2)
        H = zc.GSource(zc.G_HOSTILE, 120)
        P = zc.GSource(g_proper, 120, seed=seed)
        self.assertTrue(all(k == 15 for k in H.carries()[2:]))
        self.assertTrue(all(k == 0 for k in P.carries()[1:]))
        # gauge relation with h = 3 - 2z: U^H_n = U^P_n - a(n), a(n) = 3/(8n+1) - 2/(8n+2)
        self.assertTrue(all(P.U[n] - H.U[n] == F(3, 8 * n + 1) - F(2, 8 * n + 2) for n in range(121)))

    def test_pole_counts_along_the_pi_line(self):
        for rho, poles in ((F(0), 4), (F(1), 7), (F(-1, 4), 6), (F(-1, 2), 4), (F(3, 7), 7)):
            A = [a + rho * b for a, b in zip(zc.A_PI, zc.A_NULL)]
            self.assertEqual(sum(1 for c in A if c != 0), poles)
            self.assertEqual(sum(A), -15 * rho)

    def test_gauge_changes_seed_and_poles_but_not_the_completion(self):
        S = ic.Source(80)
        h = (F(5, 3),)
        g2 = zc.gauge_transform(zc.G_PI, h)
        self.assertEqual(g2[0], 4 - F(80, 3))
        self.assertEqual(g2[8], F(5, 3))
        S2 = zc.GSource(g2, 80, seed=F(5, 3))
        self.assertTrue(all(S2.U[n] - S.U[n] == F(5, 3) / (8 * n + 1) for n in range(81)))


if __name__ == "__main__":
    unittest.main()
