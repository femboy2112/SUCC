#!/usr/bin/env python3
"""Tests for probe_analytic.py (IAD-01 .. IAD-06; PR-1.1 .. PR-1.6 on quick parameters).

Two kinds of test:

* the quick probe (B in {64, 200}) is run through its real CLI entry point and every PR-1 check
  must pass with a positive number of checks per preregistered ID;
* for every theorem IAD-01 .. IAD-06 at least one MUTATION control recomputes the relevant
  quantities independently at B = 64 and shows that a deliberately wrong normalization, constant,
  forcing (pole mutation) or sign makes the corresponding identity/inequality FAIL on a concrete
  instance, while the true statement passes on the same instance.

Run from the repository root:
    python -m unittest discover -s research/2026-11-11/innovation_arithmetic_decoupling -p 'test_*.py'
"""
from __future__ import annotations

import json
import math
import sys
import tempfile
import unittest
from fractions import Fraction
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

import probe_analytic as pa  # noqa: E402  (imports iad_core, which puts the repo root on sys.path)
import iad_core as core  # noqa: E402
from iad_core import CompletedOrbit, Source, r, r_real, tail_interval  # noqa: E402
from observational_succ.selected_orbit import four_pole_forcing  # noqa: E402

B0 = 64
PR1_IDS = ("PR-1.1", "PR-1.2", "PR-1.3", "PR-1.4", "PR-1.5", "PR-1.6")


def innovation(n: int, l: int, forcing=r) -> Fraction:
    return sum((16 ** (l - j) * forcing(n + j) for j in range(1, l + 1)), Fraction(0))


def mutant_wide(n: int) -> Fraction:
    """Pole mutation with nonzero pole-coefficient sum (r ~ 1/(8n)): breaks the 1/n^2 cancellation."""
    return four_pole_forcing(n, weights=(4, -2, -1, 0))


def mutant_shift(n: int) -> Fraction:
    """Pole mutation keeping the coefficient sum 0 but moving a pole (asymptotic constant 16, not 15)."""
    return four_pole_forcing(n, poles=(7, 4, 3, 1))


def tails_for(forcing, n: int, depth: int = 40) -> tuple[Fraction, Fraction]:
    lo = sum((Fraction(forcing(n + j), 16 ** j) for j in range(1, depth + 1)), Fraction(0))
    return lo, lo + Fraction(forcing(n + depth + 1), 15 * 16 ** depth)


class Fixture:
    """Independent B = 64 reconstruction of the quantities used by the mutation controls."""

    def __init__(self, B: int = B0):
        self.B = B
        self.src = Source(2 * B + 64)
        self.lo = {n: tail_interval(n)[0] for n in range(B, 2 * B + 20)}
        omega = sum((Fraction(1, n * n) for n in range(B, 2 * B)), Fraction(0))
        self.p = np.array([float(Fraction(1, n * n) / omega) for n in range(B, 2 * B)])
        co = CompletedOrbit(2 * B + 64)
        self.Y = [pa.frac_pair(co.frac(n)) for n in range(B, 2 * B)]
        self.U = [pa.frac_pair(self.src.U[n]) for n in range(B, 2 * B)]
        self.Ucoh = [pa.frac_pair(-self.lo[n]) for n in range(B, 2 * B)]   # U_n(-x) = -T_n

    def w_true(self, h):
        return np.array([pa.phase(h * a, d) for a, d in self.Y])

    def Z(self, h, l, forcing=r):
        return np.array([pa.phase_fr(h * innovation(n, l, forcing)) for n in range(self.B, 2 * self.B - l)])

    def A(self, h, l, Upairs):
        m = h * (16 ** l - 1)
        return np.array([pa.phase(m * a, d) for a, d in Upairs[: self.B - l]])

    def C_true(self, h, l):
        m = h * (16 ** l - 1)
        return np.array([pa.phase(m * a, d) for a, d in self.Y[: self.B - l]])

    def tau_phase(self, h, l, sign=-1):
        return np.array([pa.phase_fr(sign * h * (self.lo[n + l] - self.lo[n])) for n in range(self.B, 2 * self.B - l)])

    def cU_coherent(self, h, d):
        return complex(sum(pa.phase_fr(h * (self.lo[n] - self.lo[n + d])) for n in range(self.B, 2 * self.B - d))
                       / self.B)


FIX: Fixture | None = None


def fixture() -> Fixture:
    global FIX
    if FIX is None:
        FIX = Fixture()
    return FIX


# ---------------------------------------------------------------------------------------------
class TestQuickProbe(unittest.TestCase):
    """The real CLI on the quick shells: every PR-1 check passes and is non-vacuous."""

    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory()
        cls.path = Path(cls.tmp.name) / "quick.json"
        cls.code = pa.main(["--quick", "--quiet", "--out", str(cls.path)])
        cls.text = cls.path.read_text()
        cls.data = json.loads(cls.text)

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def test_exit_code_zero_and_no_pr1_failure(self):
        self.assertEqual(self.code, 0)
        self.assertFalse(self.data["summary"]["any_PR1_failure"])
        for key, shell in self.data["shells"].items():
            for prid, subs in shell["PR-1"]["checks"].items():
                for sub, slot in subs.items():
                    self.assertGreater(slot["checks"], 0, (key, prid, sub))
                    self.assertEqual(slot["failures"], 0, (key, prid, sub, slot.get("counterexamples")))

    def test_every_preregistered_check_is_exercised_on_holdout_and_calibration(self):
        required = {
            "PR-1.1": ["identity_1.1_R_def_eq_(B/L)(E_L/L-S)", "inequality_1.2_|B|2_le_4/L+2maxR"],
            "PR-1.2": ["2.1_sqrt_gamma_L_le_sqrt_gamma_J_plus_J/L", "2.1_gamma_L_le_gamma_J_if_J_divides_L"],
            "PR-1.3": ["innovation_two_exact_routes_equal",
                       "3a_Delta_eq_16^l_T_n_minus_T_(n+l)_inside_tail_enclosure",
                       "3c_step_bracket_16^(l-1)delta(n+1)_to_(16/15)16^(l-1)delta(n+1)"],
            "PR-1.4": ["4.1_random_subintervals_|sum_I|_le_cot(pi lambda/2)",
                       "4.1_progression_|sum_(I, n=a mod q)|_le_cot(pi q lambda/2)",
                       "KL_step_in_[lambda,1/2]", "4.3_|e(hDelta)-1|_le_(pi/32)h16^l/B^2"],
            "PR-1.5": ["5.1_A_Z_eq_C_e(-h tau)", "5.1_A_eq_C_conj(Z)_e(-h tau)",
                       "corollary1_|Cov(A,Z)-E[C]|_le_|E[Z]|+(pi/32)h/B^2",
                       "5.2_| ||E[Z|F]||_1-||E[C|F]||_1 |_le_2a_F+(pi/32)h/B^2"],
            "PR-1.6": ["6a_transport_|c_d-c^U_d|_le_(pi/32)h/B^2", "6.1_random_H_|W|^2_le_rhs",
                       "6.1_AP_H_|W|^2_le_rhs"],
        }
        for B in ("64", "200"):
            checks = self.data["shells"][B]["PR-1"]["checks"]
            for prid, subs in required.items():
                for sub in subs:
                    self.assertGreater(checks[prid][sub]["checks"], 0, (B, prid, sub))
        glob = self.data["shells"]["global"]["PR-1"]["checks"]["PR-1.3"]
        for sub in ("bracket_r_4_15", "bracket_neg_r_prime_32_120", "r_second_derivative_positive",
                    "delta_m_bracket_1_over_16(m+1)^3_to_4_over_m^3", "moment_representation_numeric_quad"):
            self.assertGreater(glob[sub]["checks"], 0, sub)
        self.assertEqual(self.data["shells"]["64"]["role"], "calibration")
        self.assertEqual(self.data["shells"]["200"]["role"], "holdout")

    def test_every_control_runs_through_sequence_checks(self):
        roll = self.data["shells"]["200"]["PR-1"]["by_control"]
        for prid in ("PR-1.1", "PR-1.2", "PR-1.6"):
            for c in pa.SEQ_CONTROLS:
                self.assertGreater(roll[prid][c]["checks"], 0, (prid, c))
                self.assertEqual(roll[prid][c]["failures"], 0, (prid, c))
        for s in pa.SEEDS:
            self.assertGreater(roll["PR-1.5"][s]["checks"], 0, s)

    def test_pr2_is_recorded_not_enforced(self):
        for B in ("64", "200"):
            pr2 = self.data["shells"][B]["PR-2"]
            for pid in ("PR-2.1", "PR-2.2", "PR-2.3", "PR-2.4", "PR-2.5"):
                self.assertIn("predicted", pr2[pid])
                self.assertIn("observed", pr2[pid])
                self.assertTrue(any(k.startswith("met") for k in pr2[pid]), pid)
        # an unmet prediction must not change the exit status
        self.assertEqual(self.code, 0)

    def test_pr3_alias_and_hostile_seeds(self):
        for B in ("64", "200"):
            pr3 = self.data["shells"][B]["PR-3"]
            al = pr3["alias_1_16"]
            self.assertTrue(al["completed_phase_fraction_equal_for_1_le_n_le_horizon"])
            self.assertTrue(al["differs_at_n_0"])
            self.assertTrue(al["U_fraction_mod_1_equal_on_shell"])
            self.assertEqual(al["max_abs_diff_all_phase_statistics_vs_true"], 0.0)
            for s, rows in pr3["hostile_seeds_pass_PR1"].items():
                for prid, cnt in rows.items():
                    self.assertGreater(cnt["checks"], 0, (B, s, prid))
                    self.assertEqual(cnt["failures"], 0, (B, s, prid))
            hj = self.data["shells"][B]["controls"]["5_hijack"]
            for k in ("q_is_prime", "rounding_certified", "abs_x_plus_s_le_M_over_2qk", "k_minimal",
                      "M_over_2qk_le_half_16_pow_minus_K_minus_2", "q_pow_k_ge_M_16_pow_K_plus_2"):
                self.assertTrue(hj[k], (B, k))

    def test_output_is_deterministic_formatting_without_timestamps(self):
        self.assertEqual(pa.dumps_compact(pa.sanitize(json.loads(self.text))) + "\n", self.text)
        lowered = self.text.lower()
        for word in ("timestamp", "\"date\"", "elapsed", "wall_clock"):
            self.assertNotIn(word, lowered)


class TestExitCodeAndInstrument(unittest.TestCase):
    def test_exit_code_reacts_only_to_pr1(self):
        ok = pa.Ledger()
        ok.ineq("PR-1.1", "x", "c", [0.0], [1.0], ctx={})
        self.assertEqual(pa.exit_code([ok]), 0)
        bad = pa.Ledger()
        bad.ineq("PR-1.4", "x", "c", [2.0], [1.0], ctx={})
        self.assertEqual(pa.exit_code([ok, bad]), 1)
        other = pa.Ledger()
        other.ineq("PR-2.2", "x", "c", [2.0], [1.0], ctx={})
        self.assertEqual(pa.exit_code([ok, other]), 0)
        nan = pa.Ledger()
        nan.ineq("PR-1.1", "x", "c", [float("nan")], [1.0], ctx={})
        self.assertEqual(pa.exit_code([nan]), 1)

    def test_phase_matches_mpmath_kernel_on_huge_denominators(self):
        src = Source(140)
        for n in (64, 100, 140):
            for mult in (1, 3 * (16 ** 5 - 1), 8 * (16 ** 11 - 1)):
                x = mult * src.U[n]
                self.assertLess(abs(pa.phase_fr(x) - core.e(x)), 1e-14)

    def test_exact_lag_helpers_at_boundaries(self):
        # 256 = 16^2 is the exact-power edge: 4.5 log16 256 = 9 and 2.25 log16 256 = 4.5
        self.assertEqual((pa.lag_max(256), pa.ell0(256)), (9, 5))
        for B in pa.HOLDOUT_SHELLS + pa.CALIBRATION_SHELLS:
            lb = math.log(B) / math.log(16)
            if abs(4.5 * lb - round(4.5 * lb)) > 1e-9:
                self.assertEqual(pa.lag_max(B), math.floor(4.5 * lb))
            if abs(2.25 * lb - round(2.25 * lb)) > 1e-9:
                self.assertEqual(pa.ell0(B), math.ceil(2.25 * lb))
        self.assertEqual([pa.lag_max(B) for B in (200, 360, 729, 1000)], [8, 9, 10, 11])

    def test_kl_bound_float_agrees_with_tan(self):
        for lam in (Fraction(1, 7), Fraction(1, 1000), Fraction(1, 3)):
            self.assertAlmostEqual(pa.kl_bound(lam), 1 / math.tan(math.pi * float(lam) / 2), places=9)


# ---------------------------------------------------------------------------------------------
class TestIAD01Mutation(unittest.TestCase):
    def _quantities(self, v, L):
        B = len(v)
        S = float(np.sum(np.abs(v) ** 2))
        E = pa.window_energy(v, L)
        ls = pa.lag_sums(v, L)
        return B, S, E, ls

    def test_identity_holds_and_wrong_normalizations_fail(self):
        fx = fixture()
        for name, v in (("true", fx.p * fx.w_true(1)), ("coherent", fx.p.astype(complex))):
            for L in (2, 3, 5, 8, 16):
                B, S, E, ls = self._quantities(v, L)
                Ri = pa.R_identity(E, S, L, B)
                self.assertLess(abs(pa.R_definition(ls, L, B) - Ri), 1e-12, (name, L))
                if name == "coherent":
                    # mutation 1: factor B/L instead of 2B/L
                    self.assertGreater(abs(pa.R_definition(ls, L, B, factor=1.0) - Ri), 1e-3, L)
                    # mutation 2: drop the Fejer weight (1 - l/L)
                    no_fejer = 2 * B / L * sum(ls[l].real for l in range(1, L))
                    self.assertGreater(abs(no_fejer - Ri), 1e-3, L)

    def test_inequality_1_2_and_wrong_constant(self):
        fx = fixture()
        v = fx.p.astype(complex)            # coherent seed: Y == 0, |B_B(h)| = 1
        for L in (5, 8, 16, 32):
            B, S, E, ls = self._quantities(v, L)
            R = pa.R_identity(E, S, L, B)
            B2 = abs(complex(v.sum())) ** 2
            self.assertAlmostEqual(B2, 1.0, places=12)
            mid, maj = pa.bound_12(S, R, B, L)
            self.assertLessEqual(B2, mid + 1e-12)
            self.assertLessEqual(mid, maj + 1e-12)
            if L >= 16:   # where 4/L no longer dominates, the mutated constant 2 -> 1/2 is refuted
                _, maj_bad = pa.bound_12(S, R, B, L, c_R=0.5)
                self.assertGreater(B2, maj_bad + 1e-3, L)


class TestIAD02Mutation(unittest.TestCase):
    def test_monotonicity_and_mutants(self):
        fx = fixture()
        alt = fx.p * np.array([(-1.0) ** n for n in range(fx.B)])
        for v, name in ((alt, "alternating"), (fx.p * fx.w_true(3), "true_h3")):
            S = float(np.sum(np.abs(v) ** 2))
            gam = {L: pa.window_energy(v, L) / (L * L * S) for L in range(1, 17)}
            sq, dv = pa.iad02_margins(gam)
            self.assertGreaterEqual(min(m for *_, m in sq), -1e-12, name)
            self.assertGreaterEqual(min(m for *_, m in dv), -1e-12, name)
        S = float(np.sum(alt ** 2))
        gam = {L: pa.window_energy(alt.astype(complex), L) / (L * L * S) for L in range(1, 17)}
        self.assertGreater(gam[3], gam[2] + 0.05)   # 2 does not divide 3
        # mutation 1: monotonicity without divisibility
        _, dv_bad = pa.iad02_margins(gam, divisibility_only=False)
        self.assertIn((2, 3), [(J, L) for J, L, m in dv_bad if m < -1e-3])
        # mutation 2: slack J/L shrunk to J/(4L)
        sq_bad, _ = pa.iad02_margins(gam, slack_scale=0.25)
        self.assertLess(min(m for *_, m in sq_bad), -1e-3)


class TestIAD03Mutation(unittest.TestCase):
    def test_brackets_sharp_constant_and_pole_mutation(self):
        for t in (Fraction(10 ** 4), Fraction(10 ** 6), Fraction(3, 2), Fraction(1)):
            q2 = (8 * t - 7) * (8 * t - 6)
            self.assertTrue(Fraction(4) / q2 <= r_real(t) <= Fraction(15) / q2, t)
        t = Fraction(10 ** 4)
        q2 = (8 * t - 7) * (8 * t - 6)
        # mutated constant 15 -> 14.99 is refuted by the true forcing (constant 15 is asymptotically sharp)
        self.assertGreater(r_real(t), Fraction(1499, 100) / q2)
        # pole mutation (7,4,3,2) -> (7,4,3,1): coefficient sum still 0 but constant 16 > 15
        r_mut = sum((Fraction(c) / (8 * t - a) for c, a in zip((4, -2, -1, -1), (7, 4, 3, 1))), Fraction(0))
        self.assertGreater(r_mut, Fraction(15) / q2)
        self.assertEqual(mutant_shift(10 ** 4), r_mut)

    def test_innovation_routes_and_tail_identity_detect_pole_mutation(self):
        fx = fixture()
        B = fx.B
        Umut = [Fraction(0)]
        for n in range(1, B + 20):
            Umut.append(16 * Umut[-1] + mutant_shift(n))
        for n in (B, B + 7, 2 * B - 13):
            for l in (1, 3, 5):
                d_true = innovation(n, l)
                self.assertEqual(d_true, fx.src.innovation(n, l))
                if n + l < len(Umut):
                    self.assertNotEqual(Umut[n + l] - 16 ** l * Umut[n], d_true)
                lo_n, hi_n = tail_interval(n)
                lo_m, hi_m = tail_interval(n + l)
                self.assertTrue(16 ** l * lo_n - hi_m <= d_true <= 16 ** l * hi_n - lo_m)
                mlo_n, mhi_n = tails_for(mutant_shift, n)
                mlo_m, mhi_m = tails_for(mutant_shift, n + l)
                self.assertFalse(16 ** l * mlo_n - mhi_m <= d_true <= 16 ** l * mhi_n - mlo_m)

    def test_step_bracket_and_mutated_upper_constant(self):
        B = B0
        for l in (1, 4, 6):
            for n in (B, B + 31):
                D = innovation(n, l) - innovation(n + 1, l)
                dl = r(n + 1) - r(n + 2)
                self.assertTrue(16 ** (l - 1) * dl <= D <= Fraction(16, 15) * 16 ** (l - 1) * dl)
                if l >= 2:   # mutation: upper factor 16/15 -> 1 fails as soon as two terms contribute
                    self.assertGreater(D, 16 ** (l - 1) * dl)


class TestIAD04Mutation(unittest.TestCase):
    def test_kusmin_landau_hypotheses_and_pole_mutation(self):
        B, h, l = B0, 7, 4
        self.assertTrue(pa.kl_admissible(B, h, l))
        lam = pa.kl_lambda(B, h, l)
        g = [h * (innovation(n, l) - innovation(n + 1, l)) for n in range(B, 2 * B - 1 - l)]
        self.assertTrue(all(lam <= x <= Fraction(1, 2) for x in g))
        self.assertTrue(all(g[i + 1] < g[i] for i in range(len(g) - 1)))
        gm = [h * (innovation(n, l, mutant_wide) - innovation(n + 1, l, mutant_wide)) for n in range(B, 2 * B - 1 - l)]
        self.assertGreater(max(gm), Fraction(1, 2))     # hypothesis g <= 1/2 refuted for the mutant forcing

    def test_kl_inequality_on_data_and_calibration_on_linear_phase(self):
        fx = fixture()
        B, h, l = fx.B, 3, 4
        Z = fx.Z(h, l)
        P = np.concatenate([[0j], np.cumsum(Z)])
        allmax = max(float(np.abs(P[i + 1:] - P[i]).max()) for i in range(len(Z)))
        self.assertLessEqual(allmax, pa.kl_bound(pa.kl_lambda(B, h, l)))
        # instrument calibration: a linear phase with constant step lam attains 1/sin(pi lam),
        # i.e. about half of cot(pi lam/2); a bound one third as large is refuted
        lam = Fraction(1, 50)
        z = np.array([pa.phase_fr(lam * n) for n in range(400)])
        Pz = np.concatenate([[0j], np.cumsum(z)])
        mz = max(float(np.abs(Pz[i + 1:] - Pz[i]).max()) for i in range(400))
        self.assertAlmostEqual(mz, 1 / math.sin(math.pi / 50), places=9)
        self.assertLessEqual(mz, pa.kl_bound(lam))
        self.assertGreater(mz, pa.kl_bound(lam) / 3)

    def test_deviation_bound_4_3_and_wrong_constant(self):
        fx = fixture()
        B, h, l = fx.B, 1, 1
        dev = np.abs(fx.Z(h, l) - 1)
        self.assertTrue(np.all(dev <= math.pi / 32 * h * 16 ** l / B ** 2))
        self.assertGreater(dev[0], math.pi / 40 * h * 16 ** l / B ** 2)   # constant pi/40 refuted at n = B


class TestIAD05Mutation(unittest.TestCase):
    def test_gauge_identity_and_mutations(self):
        fx = fixture()
        h, l = 3, 4
        A = fx.A(h, l, fx.U)
        Z = fx.Z(h, l)
        C = fx.C_true(h, l)
        T = fx.tau_phase(h, l)
        self.assertLess(float(np.abs(A * Z - C * T).max()), 1e-12)
        self.assertLess(float(np.abs(A - C * np.conj(Z) * T).max()), 1e-12)
        # mutation: sign of tau
        self.assertGreater(float(np.abs(A * Z - C * fx.tau_phase(h, l, sign=+1)).max()), 1e-7)
        # mutation: pole-mutated forcing in the innovation
        self.assertGreater(float(np.abs(A * fx.Z(h, l, mutant_shift) - C * T).max()), 1e-6)
        # mutation: completed correlation at the wrong lag
        C_wrong = fx.C_true(h, l + 1)
        n = len(C_wrong)
        self.assertGreater(float(np.abs(A[:n] * Z[:n] - C_wrong * T[:n]).max()), 0.1)

    def test_corollaries_and_dropped_terms(self):
        fx = fixture()
        B, h = fx.B, 3
        tb = math.pi / 32 * h / B ** 2
        # coherent seed s = -x: C == 1, A = conj(Z) e(-h tau)
        for l in (1, 4):
            A = fx.A(h, l, fx.Ucoh)
            Z = fx.Z(h, l)
            C = np.ones(len(Z), dtype=complex)
            EZ = complex(Z.mean())
            cov = complex((A * Z).mean()) - complex(A.mean()) * EZ
            self.assertLessEqual(abs(cov - 1), abs(EZ) + tb + 1e-12)
            if l == 1:      # mutation: drop |E[Z]|  (Z ~ 1 at low lag, so Cov ~ 0 while E[C] = 1)
                self.assertGreater(abs(cov - 1), tb + 0.5)
            lab = np.zeros(len(Z), dtype=np.int64)       # trivial filtration F = F_1
            lhs = abs(pa.l1_cond_mean(Z, lab, 1) - pa.l1_cond_mean(C, lab, 1))
            aF = pa.l1_deviation(A, lab, 1)
            self.assertLessEqual(lhs, 2 * aF + tb + 1e-12)
            if l == 4:      # window lag: mutation without the a_F term is refuted
                self.assertGreater(lhs, tb + 1e-3)


class TestIAD06Mutation(unittest.TestCase):
    def test_transport_bound_and_wrong_constant(self):
        fx = fixture()
        B, h = fx.B, 1
        ratios = []
        for d in range(1, 61):
            c_d = (B - d) / B                       # coherent seed: Y == 0
            ratios.append(abs(c_d - fx.cU_coherent(h, d)) / (math.pi / 32 * h / B ** 2))
        self.assertLessEqual(max(ratios), 1.0)
        self.assertGreater(max(ratios), 1 / 8)      # constant (pi/32)/8 is refuted on this instance
        # true seed, independent routes: pi-enclosure orbit vs rational source states
        w = fx.w_true(h)
        Eu = np.array([pa.phase(h * a, d) for a, d in fx.U])
        for d in (1, 5, 17, 60):
            c_d = complex(sum(pa.phase(h * (16 ** d - 1) * a, den) for a, den in fx.Y[: B - d]) / B)
            self.assertLess(abs(c_d - complex(np.vdot(w[: B - d], w[d:]) / B)), 1e-12)
            cU = complex(np.vdot(Eu[: B - d], Eu[d:]) / B)
            self.assertLessEqual(abs(c_d - cU), math.pi / 32 * h / B ** 2)

    def test_sparse_van_der_corput_and_dropped_factors(self):
        fx = fixture()
        B, l0 = fx.B, pa.ell0(fx.B)
        c_coh = {d: complex((B - d) / B) for d in range(1, 61)}
        W2 = 1.0
        for k in (2, 3, 4):
            H = [j * l0 for j in range(k)]
            self.assertLessEqual(W2, pa.vdc_rhs(H, c_coh, B) + 1e-12)
            self.assertAlmostEqual(pa.vdc_rhs(H, c_coh, B), pa.vdc_rhs_ap(k, l0, c_coh, B), places=12)
            self.assertGreater(W2, pa.vdc_rhs(H, c_coh, B, length_factor=False) + 1e-4)   # (1 + D/B) needed
            self.assertGreater(W2, pa.vdc_rhs(H, c_coh, B, cross=1.0) + 0.1)             # factor 2 needed
        # true seed with 50 seeded random H: (6.1) holds
        h = 3
        w = fx.w_true(h)
        W2t = abs(complex(w.mean())) ** 2
        c = {d: complex(np.vdot(w[: B - d], w[d:]) / B) for d in range(1, 61)}
        rg = pa.rng_for("test-vdc-H", B)
        for _ in range(50):
            H = sorted(rg.sample(range(0, 61), rg.randint(2, 6)))
            self.assertLessEqual(W2t, pa.vdc_rhs(H, c, B) + 1e-12, H)


if __name__ == "__main__":
    unittest.main()
