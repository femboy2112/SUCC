#!/usr/bin/env python3
"""Unit tests for LIMIT_FACES.md (LMF-01..06).

Fast: the probe is run in quick mode (authentication on a short overlap and the
calibration shells only; the holdout shells are never touched here), plus exact
small-case checks, the mutation controls RM-1..3 of PREREGISTRATION_RUNGS.md and a
regression test for every constant.  Nothing here tests, or could test, an open
claim.
"""
from __future__ import annotations

import json
import math
import random
import sys
import unittest
from fractions import Fraction as F
from pathlib import Path

_HERE = Path(__file__).resolve().parent
if str(_HERE) not in sys.path:
    sys.path.insert(0, str(_HERE))

import faces_core as fc  # noqa: E402
import probe_rungs as pr  # noqa: E402
import iad_core as ic  # noqa: E402
import zsc_core as zc  # noqa: E402


def delta(p):
    return [(F(p), F(1))]


class QuickProbe(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.res, cls.ok = pr.run(quick=True)

    def test_all_theorem_grade_checks_pass(self):
        self.assertTrue(self.ok, self.res["meta"])
        self.assertGreater(self.res["meta"]["theorem_grade_checks"], 15000)
        self.assertEqual(self.res["meta"]["theorem_grade_failures"], 0)

    def test_quick_mode_never_touches_the_holdout(self):
        self.assertEqual(sorted(self.res["pi_shells"]), ["128", "64"])
        self.assertEqual(self.res["predictions"], {})

    def test_mutation_controls(self):
        m = self.res["mutation_controls"]
        self.assertTrue(m["RM-1"])                       # constant digits: W1 >= 4/225, c_B = 0
        self.assertTrue(m["RM-2"])                       # Q := identity is noticed by the checks
        self.assertTrue(m["RM-2_vacuous_pass_flagged"])  # ... although RP-2 alone would pass vacuously
        self.assertTrue(m["RM-3"])                       # 256-adic grid: W1 <= 1/512
        self.assertEqual(m["RM-3_value"], "1/512")

    def test_hostile_controls_are_on_the_far_side_of_every_threshold(self):
        w = self.res["witnesses_largest_shell"]
        for name in pr.ABOVE_ALL:
            self.assertFalse(w[name]["below_W1_threshold_1/60"], name)
            self.assertFalse(w[name]["below_D_threshold_1/60"], name)
        for name in ("coherent_zero", "W2", "shallit_K"):
            self.assertFalse(w[name]["below_mode1_threshold_1/4"], name)


class CommittedResults(unittest.TestCase):
    def test_committed_results_record_a_clean_full_run(self):
        res = json.loads((_HERE / "RESULTS_rungs.json").read_text())
        self.assertFalse(res["meta"]["quick"])
        self.assertTrue(res["meta"]["all_theorem_grade_pass"])
        self.assertEqual(res["meta"]["theorem_grade_failures"], 0)
        self.assertEqual(res["meta"]["holdout_shells"], [3301, 4099, 5003, 6007])
        self.assertEqual(res["authentication"]["overlap_A_vs_carrier"], [1, 2600])
        self.assertEqual(sorted(res["predictions"]), ["RP-1", "RP-2", "RP-3", "RP-4"])
        for key in ("RP-1", "RP-2", "RP-3", "RP-4"):     # recorded as met or missed, never absent
            self.assertIn(res["predictions"][key]["met"], (True, False))
        self.assertEqual(res["thresholds"]["provisional_w_star"], "4/225")
        self.assertEqual(res["thresholds"]["proved_w_star"], "1/60")


class Constants(unittest.TestCase):
    def test_dual_certificate_and_primal_point(self):
        c = fc.fix16_dual_certificate()
        self.assertEqual(set(c["dual_w1_vertex_values"]), {F(1, 60)})
        self.assertEqual(set(c["dual_defect_vertex_values"]), {F(1, 60)})
        self.assertEqual((c["primal_w1"], c["primal_defect"]), (F(1, 60), F(1, 60)))
        self.assertEqual(sum(fc.M_STAR), 1)

    def test_convexity_brute_force_agrees_with_the_certificate(self):
        """Random points of the simplex never beat 1/60 (W1 and defect)."""
        rng = random.Random(7)
        for _ in range(300):
            raw = [rng.randrange(0, 12) for _ in range(16)]
            if not sum(raw):
                continue
            nu = fc.fix16([F(x, sum(raw)) for x in raw])
            self.assertGreaterEqual(fc.w1_lebesgue(nu), F(1, 60))
            self.assertGreaterEqual(fc.child_defect(nu), F(1, 60))

    def test_fifteen_point_minimum_is_the_provisional_constant(self):
        self.assertEqual(fc.min_w1_fix15(), F(4, 225))
        rng = random.Random(8)
        for _ in range(300):                             # endpoint 1 forbidden: never below 4/225
            raw = [rng.randrange(0, 12) for _ in range(15)]
            if not sum(raw):
                continue
            nu = fc.fix16([F(x, sum(raw)) for x in raw] + [F(0)])
            self.assertGreaterEqual(fc.w1_lebesgue(nu), F(4, 225))

    def test_provisional_threshold_is_refuted_by_an_explicit_shell(self):
        d, B = fc.superblock_shell_digits(40)
        w1 = fc.seg_w1_lebesgue(fc.fracs_from_digits(d, B, 2 * B))
        self.assertEqual(F(fc.k_changes(d, B, 2 * B), B), F(1, 80))
        self.assertLess(w1, F(4, 225))                   # below the provisional threshold ...
        self.assertGreater(w1, F(1, 60) - F(1, 256))     # ... with change density only 1/80

    def test_coherent_control_and_single_deltas(self):
        self.assertEqual(fc.haar_defect(delta(0)), F(15, 32))
        self.assertEqual(fc.w1_lebesgue(delta(0)), F(1, 2))
        for j in range(16):
            self.assertGreaterEqual(fc.child_defect(delta(F(j, 15))), F(1, 4))
            self.assertGreaterEqual(fc.w1_lebesgue(delta(F(j, 15))), F(113, 450))
        half = [(F(0), F(1, 2)), (F(1), F(1, 2))]
        self.assertEqual((fc.w1_lebesgue(half), fc.child_defect(half)), (F(1, 4), F(1, 4)))

    def test_child_average_of_the_triangle_wave_is_constant(self):
        for h in (1, 3, 15, 17, 2, 4, 8, 24, 255):
            for y in (F(0), F(1, 7), F(5, 11), F(1)):
                for th in (F(0), F(1, 2), F(2, 9)):
                    self.assertEqual(fc.child_average_tri(h, th, y), F(1, 4 * h))
        self.assertNotEqual(fc.child_average_tri(16, F(0), F(1, 3)), F(1, 64))

    def test_kantorovich_bound_is_attained(self):
        mid = [(F(2 * i + 1, 30), F(1, 15)) for i in range(15)]
        self.assertEqual(fc.mean_tri(mid, 15, F(1, 2)), 0)
        self.assertEqual(fc.w1_lebesgue(mid), F(1, 60))
        self.assertEqual(fc.kantorovich_floor(mid, 15, F(1, 2)), F(1, 60))
        nu = fc.fix16(fc.M_STAR)
        self.assertEqual(fc.kantorovich_floor(nu, 15), F(1, 60))

    def test_fix_mass_lemma_equality_and_half_prefix(self):
        for a in (F(1), F(1, 2), F(1, 3)):
            self.assertEqual(fc.fix_mass_floor([a * m for m in fc.M_STAR]), a * a / 60)
        rho = fc.half_prefix_extremal(3600)
        w = fc.w1_lebesgue(rho)
        self.assertGreaterEqual(w, F(1, 240))
        self.assertLess(w, F(1, 200))                    # so the provisional 1/120 is false
        self.assertGreaterEqual(fc.child_defect(rho), F(1, 256))

    def test_jump_lemma(self):
        """LMF-05 (c): mass >= J in an arc of length l <= J forces W_1 >= (J - l)^2 / 4."""
        rng = random.Random(5)
        for _ in range(300):
            J, l = F(rng.randrange(20, 101), 100), F(rng.randrange(0, 20), 100)
            rest = [(F(rng.randrange(0, 201), 200), (1 - J) / 3) for _ in range(3)]
            p = F(rng.randrange(0, 81), 100)                                  # plain arc [p, p + l]
            arc = [(p + l * F(i, 4), J / 5) for i in range(5)]
            self.assertGreaterEqual(fc.w1_lebesgue(fc.normalize(arc + rest)), (J - l) ** 2 / 4)
            a = J * F(rng.randrange(0, 11), 10)                               # arc through 0 = 1
            wrap = [(l / 2 * F(rng.randrange(0, 5), 4), a), (1 - l / 2 * F(rng.randrange(0, 5), 4), J - a)]
            self.assertGreaterEqual(fc.w1_lebesgue(fc.normalize(wrap + rest)), (J - l) ** 2 / 4)
        half = [(F(0), F(1, 2)), (F(1), F(1, 2))]                             # equality: J = 1, l = 0
        self.assertEqual(fc.w1_lebesgue(half), F(1, 4))

    def test_operators(self):
        nu = [(F(1, 3), F(1, 2)), (F(5, 7), F(1, 2))]
        self.assertEqual(fc.total_mass(fc.child(nu)), 1)
        self.assertEqual(fc.push_T(delta(F(7, 15))), delta(F(7, 15)))
        self.assertEqual(fc.push_T(delta(1)), delta(1))
        self.assertEqual(fc.w1_between(fc.child(nu), fc.child(delta(F(1, 2)))),
                         fc.w1_between(nu, delta(F(1, 2))) / 16)       # C contracts by exactly 1/16
        rng = random.Random(3)
        for _ in range(40):                                            # W_1(C nu, lambda) = W_1(nu, lambda)/16
            atoms = fc.normalize((F(rng.randrange(0, 61), 60), F(1, 5)) for _ in range(5))
            self.assertEqual(fc.w1_lebesgue(fc.child(atoms)), fc.w1_lebesgue(atoms) / 16)


class Faces(unittest.TestCase):
    """LMF-02: the invariant measures with |mu^(h)| = 1 live on K_(h,j) = {p periodic : h p = j/15 mod 1}."""

    @staticmethod
    def periodic(p: F) -> bool:
        return p.denominator % 2 == 1

    def test_unimodular_cosets(self):
        for h in (1, 2, 3, 5, 15, 17, 30, 255):
            for j in range(15):
                K = [(F(j, 15) + i) / h for i in range(h)]
                K = [p for p in K if self.periodic(p)]
                Kset = set(K)
                for p in K:                                            # K_(h,j) is T-invariant
                    q = 16 * p - (16 * p).__floor__()
                    self.assertIn(q, Kset, (h, j, p))
            for th in (F(1, 7), F(1, 30), F(1, 2), F(3, 16)):          # other cosets hold no full orbit
                for i in range(h):
                    p = (th + i) / h
                    p -= p.__floor__()
                    q = 16 * p - (16 * p).__floor__()
                    self.assertNotEqual(fc.dist_int(h * q - th), 0, (h, th, i))

    def test_mode_one_and_mode_fifteen(self):
        self.assertEqual([(F(j, 15) + 0) / 1 for j in range(15)], [F(j, 15) for j in range(15)])
        K0 = [F(i, 15) for i in range(15)]                             # K_(15,0) = Fix
        self.assertTrue(all((16 * p - p).denominator == 1 for p in K0))
        K1 = [(F(1, 15) + i) / 15 for i in range(15)]                  # K_(15,1): no fixed point
        self.assertTrue(all((15 * p).denominator != 1 for p in K1))


class Rungs(unittest.TestCase):
    L = 3100

    def shell(self, d, B=1500):
        return pr.Shell(d, B)

    def test_R1_holds_R2_fails_on_two_alternating_long_runs(self):
        sh = self.shell(fc.two_runs_digits(1, 2, self.L))
        self.assertLess(sh.cB, F(1, 20))                               # (CH) fails in the limit
        self.assertLess(abs(sh.mean_e(1)), 0.985)                      # yet mode 1 saves (limit cos(pi/15))
        self.assertGreater(sh.mean_e(15).real, 0.99)

    def test_R0_holds_R1_fails_on_one_nonzero_digit(self):
        sh = self.shell(fc.sparse_excursion_digits(1, 2, self.L))
        self.assertGreater(abs(sh.mean_e(1)), 0.995)                   # no modulus saving at mode 1
        self.assertLess(sh.mean_e(1).real, 0.93)                       # but the real part saves (cos(2 pi/15))
        exact = pr.Shell([1] * 400, 128)                               # the rational point 1/15 itself
        self.assertAlmostEqual(abs(exact.mean_e(1)), 1.0, places=12)
        self.assertAlmostEqual(exact.mean_e(1).real, math.cos(2 * math.pi / 15), places=12)

    def test_R0_fails_on_runs_of_0_and_F_and_meets_the_mode_one_thresholds(self):
        d = fc.two_runs_digits(0, 15, self.L)
        sh = self.shell(d)
        self.assertGreater(sh.mean_e(1).real, 0.997)                   # 1 - Re W = O(transitions / B)
        bits = fc.bits_of_digits(d[1500:3002])
        self.assertLess(sum(1 for m in range(6000) if bits[m] != bits[m + 1]), 60)
        self.assertLess(abs(sh.w1 - F(1, 4)), F(1, 100))               # thresholds 1/4 are approached
        self.assertLess(abs(sh.D - F(1, 4)), F(1, 100))

    def test_period_k_rungs(self):
        d = zc.periodic_digits([0, 15], 400)                           # 1/17: (CH_1) holds, (CH_2) fails
        self.assertEqual(fc.k_changes(d, 64, 128, 1), 64)
        self.assertEqual(fc.k_changes(d, 64, 128, 2), 0)
        sh = pr.Shell(d, 64)
        self.assertAlmostEqual(sh.mean_e(255).real, 1.0, places=12)
        self.assertLess(sh.mean_e(15).real, 0.75)
        mix = fc.period_mix_digits(self.L)                             # every (CH_k) holds on the mix
        for k in (1, 2, 3, 4):
            self.assertGreater(F(fc.k_changes(mix, 1500, 3000, k), 1500), F(1, 20), k)

    def test_binary_signed_representation_identity(self):
        """xi - b_0 = sum_m (b_(m+1) - b_m) 2^(-(m+1)) on a rational point with periodic bits."""
        d = zc.periodic_digits([2, 13, 7], 60)
        bits = fc.bits_of_digits(d)
        xi = F(int("".join("%x" % x for x in [2, 13, 7]), 16), 16 ** 3 - 1)
        N = 200
        lhs = sum(F(bits[m + 1] - bits[m], 2 ** (m + 1)) for m in range(N))
        self.assertLess(abs((xi - bits[0]) - lhs), F(2, 2 ** N))

    def test_R0_diophantine_cost_on_finite_strings(self):
        """If every binary shell [M, 2M), M0 <= M <= M1, has change density >= c, then a run of
        equal bits starting at m >= max(2 M0, 2/c) with m + L <= 2 M1 has
        L <= ((1-c)(m+1) + 2)/(1+c)."""
        rng = random.Random(11)
        strings = [fc.bits_of_digits(fc.two_runs_digits(3, 12, 700)),
                   fc.bits_of_digits(zc.xi_lambda_digits(F(1, 2), 700)),
                   [rng.randrange(2) for _ in range(2800)]]
        for bits in strings:
            M0, M1 = 16, 1200
            pre = [0]
            for m in range(len(bits) - 1):
                pre.append(pre[-1] + (bits[m] != bits[m + 1]))
            c = min(F(pre[2 * M] - pre[M], M) for M in range(M0, M1 + 1))
            if c == 0:
                continue
            start = max(2 * M0, math.ceil(2 / c))
            for m in range(start, M1):
                L = 1
                while m + L < 2 * M1 and bits[m + L] == bits[m]:
                    L += 1
                if m + L <= 2 * M1 and L <= m:
                    self.assertLessEqual(L * (1 + c), (1 - c) * (m + 1) + 2, (m, L, c))
                    self.assertGreaterEqual(fc.dist_int(F(int("".join(map(str, bits[m:m + 60])), 2), 2 ** 60)
                                                        + F(1, 2 ** 61)), F(1, 2 ** (L + 2)))


class DataPath(unittest.TestCase):
    def test_three_routes_agree_on_a_short_overlap(self):
        M = 260
        XA, XB = ic._x_scaled(M), fc.x_scaled_from_source(M)
        self.assertEqual(XA, XB)
        dA = fc.digits_from_scaled(XA, M, 200)
        self.assertEqual(dA, zc.pi_digits(200))
        self.assertEqual(fc.digits_from_carrier(150)[1:], dA[1:151])

    def test_route_B_refuses_an_undecided_floor(self):
        with self.assertRaises(RuntimeError):
            fc.x_scaled_from_source(40, guard=1)          # slack L + 1 = 44 exceeds 16^1

    def test_decimal_strings_are_truncations(self):
        self.assertEqual(fc.dec(F(1, 60), 6), "0.016666")
        self.assertEqual(fc.dec(F(-1, 3), 3), "-0.333")
        self.assertEqual(fc.dec(F(5, 4), 2), "1.25")


if __name__ == "__main__":
    unittest.main()
