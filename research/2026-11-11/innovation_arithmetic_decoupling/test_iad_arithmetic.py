"""Tests for probe_arithmetic.py: PR-1.7 ... PR-1.11 on small parameters, each with mutation
controls that must FAIL (so a passing test is not an echo of hardcoded numbers).

Run from the repository root:
    PYTHONPATH=. python -m unittest discover -s research/2026-11-11/innovation_arithmetic_decoupling -p 'test_*.py'
"""
from __future__ import annotations

import contextlib
import io
import json
import sys
import tempfile
import unittest
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

import iad_core as ic  # noqa: E402
import probe_arithmetic as pa  # noqa: E402
from observational_succ.selected_orbit import four_pole_forcing  # noqa: E402

S = ic.Source(700)


def failing_primes(check: dict) -> set[int]:
    return {f[1] for f in check["first_failures"]}


# ------------------------------------------------------------------------------ PR-1.7

class TestIAD07Hijack(unittest.TestCase):
    B = 16

    @classmethod
    def setUpClass(cls):
        cls.primes = pa.primes_upto(16 * cls.B)
        cls.times = list(range(0, 2 * cls.B + 1))
        cls.hj = pa.hijack_construct(cls.B)
        cls.res = pa.hijack_checks(S, cls.hj, cls.primes, cls.times, pa.M_HIJACK_FACTORS, ell_list=(1, 3))

    def test_theorem_holds_exactly_on_small_shell(self):
        self.assertTrue(self.res["pass"], {k: v for k, v in self.res["checks"].items() if not v["pass"]})
        self.assertNotEqual(self.hj["s"], 0)
        self.assertEqual(self.hj["a"] % pa.M_HIJACK, 0)
        self.assertGreaterEqual(self.hj["Q"], pa.M_HIJACK * 16 ** (self.hj["K"] + 2))
        self.assertLess(pa.Q_HIJACK ** (self.hj["k"] - 1), pa.M_HIJACK * 16 ** (self.hj["K"] + 2))  # k minimal
        # the seed really is coherent on the shell while the true seed is not
        for h, w in self.res["W"].items():
            self.assertTrue(w["hijack_bound_holds"])
            self.assertLess(w["hijack_abs_W_minus_1_upper"], w["bound_pi_h_over_3840B"])
            self.assertLess(w["true_seed_abs_W"], 0.9)

    def test_mutation_q_inside_the_census_breaks_class_equality(self):
        hj = pa.hijack_construct(self.B, q=13)  # 13 divides M: q is not a unit at 13
        res = pa.hijack_checks(S, hj, self.primes, self.times, pa.M_HIJACK_FACTORS, with_W=False,
                               exclude_q=False)
        self.assertFalse(res["checks"]["preconditions"]["gcd_q_M_eq_1"])
        chk = res["checks"]["item2_i_QpZp_classes_equal_all_p_le_16B"]
        self.assertFalse(chk["pass"])
        self.assertEqual(failing_primes(chk), {13})

    def test_mutation_M_missing_a_prime_square_breaks_residue_equality(self):
        hj = pa.hijack_construct(self.B, M=pa.M_HIJACK // 13 ** 2)
        res = pa.hijack_checks(S, hj, self.primes, self.times, pa.M_HIJACK_FACTORS, with_W=False)
        self.assertTrue(res["checks"]["item2_i_QpZp_classes_equal_all_p_le_16B"]["pass"])  # Q_p/Z_p blind
        self.assertFalse(res["checks"]["item2_ii_vp_difference_ge_j_for_pj_exactly_dividing_M"]["pass"])
        self.assertIn(13, failing_primes(res["checks"]["item2_ii_class_mod_pj_equal"]))

    def test_mutation_a_not_multiple_of_M_breaks_residue_at_3(self):
        hj = dict(self.hj)
        hj["a"] = self.hj["a"] + pa.M_HIJACK // 9
        hj["s"] = Fraction(hj["a"], hj["Q"])
        res = pa.hijack_checks(S, hj, self.primes, self.times, pa.M_HIJACK_FACTORS, with_W=False)
        self.assertFalse(res["checks"]["item2_ii_16n_a_divisible_by_M"]["pass"])
        self.assertEqual(failing_primes(res["checks"]["item2_ii_vp_difference_ge_j_for_pj_exactly_dividing_M"]), {3})

    def test_mutation_qk_too_small_breaks_coherence(self):
        hj = pa.hijack_construct(self.B, k=self.hj["k"] - 3)
        res = pa.hijack_checks(S, hj, self.primes, self.times, pa.M_HIJACK_FACTORS)
        self.assertFalse(res["checks"]["preconditions"]["Qk_ge_M_16pow_K_plus_2"])
        self.assertFalse(res["checks"]["item3_abs_Y_n_le_half_16pow_n_minus_K_minus_2_all_n_le_K"]["pass"])
        self.assertFalse(res["checks"]["item3_abs_W_B_minus_1_le_pi_h_over_3840B"]["pass"])
        # the finite-place items do not see the change
        self.assertTrue(res["checks"]["item2_i_QpZp_classes_equal_all_p_le_16B"]["pass"])

    def test_authentication_rejects_hijack_but_not_true_seed(self):
        P = [S.U[n] / 16 ** n for n in self.times]  # P_n = 16^-n U_n(0)
        for n, Pn in zip(self.times, P):
            Z_hijack = (S.U[n] + 16 ** n * self.hj["s"]) / 16 ** n - Pn
            self.assertEqual(Z_hijack, self.hj["s"])
            self.assertNotEqual(Z_hijack, 0)
            self.assertEqual(S.U[n] / 16 ** n - Pn, 0)  # the literal seed authenticates
        self.assertTrue(self.res["checks"]["authentication_Z_n_eq_s_ne_0"]["pass"])


# ------------------------------------------------------------------------------ PR-1.8

class TestIAD08Wall(unittest.TestCase):
    def test_81_holds_on_seeded_synthetic_cases(self):
        cases = pa.synthetic_81_cases(n_cases=40, seed=pa.SEED + 108)
        results = [pa.check_81(c["y"], c["m"], c["N"], c["theta"], c["h"]) for c in cases]
        self.assertTrue(all(r["holds"] for r in results))
        self.assertGreater(sum(1 for r in results if r.get("rhs_lt_1")), 5)  # informative cases exist
        self.assertGreater(sum(1 for r in results if not r["lhs_exactly_zero"]), 20)

    def test_81_is_nearly_sharp_for_tiny_same_sign_phases(self):
        y = Fraction(1, 16 ** 30)
        r = pa.check_81(y, 0, 6, 1, 1)
        self.assertTrue(r["holds"])
        self.assertGreater(r["lhs_upper"] / r["rhs_lower"], 1 - 2 * 16 ** -6)

    def test_mutation_eps_at_wrong_time_is_violated(self):
        y = Fraction(1, 16 ** 5) + Fraction(1, 16 ** 40)
        m, N = 0, 8
        wrong_eps = ic.dist_to_int(16 ** (m + N - 1) * y)  # epsilon read at the last time
        self.assertFalse(pa.check_81(y, m, N, 1, 1, eps=wrong_eps)["holds"])
        self.assertTrue(pa.check_81(y, m, N, 1, 1)["holds"])

    def test_mutation_bound_without_16_power_is_violated(self):
        y = Fraction(1, 16 ** 30)
        r = pa.check_81(y, 0, 6, 1, 1, eps=ic.dist_to_int(y) / 16 ** 5)  # (8.1) with 16^N -> 16
        self.assertFalse(r["holds"])

    def test_one_seventeenth_meets_the_wall_but_does_not_cancel(self):
        for B in range(0, 60):
            self.assertEqual(ic.dist_to_int(16 ** B * Fraction(1, 17)), Fraction(1, 17))
        _, _, pr3 = pa.section_iad08(40, (24,))
        self.assertTrue(pr3["pass"])
        self.assertAlmostEqual(pr3["means"]["B24_h1"]["mean"][0], 0.9324722294043558, places=12)


# ------------------------------------------------------------------------------ PR-1.9

class TestIAD09FreshPrimes(unittest.TestCase):
    B = 24

    @classmethod
    def setUpClass(cls):
        p_cap = 16 * cls.B + 200
        cls.direct = pa.first_events_direct([p for p in pa.primes_upto(p_cap) if p >= 7])
        cls.events = pa.event_table(3 * cls.B, p_cap)
        cls.ells = pa.ell_pair(cls.B)

    def test_birth_law_by_brute_force(self):
        res = pa.births_check(self.B, self.direct, self.events)
        self.assertTrue(res["pass"], res)
        self.assertGreater(res["n_events"], 100)
        for m in range(self.B, 2 * self.B + max(self.ells) + 1):
            brute = sorted(p for p, (mm, _) in self.direct.items() if mm == m)
            self.assertEqual(sorted(p for p, _, _ in ic.births_at(m)), brute)

    def test_mutation_wrong_birth_formula_is_caught(self):
        def wrong(p):
            return ((p + 5) // 8, "8m-7") if p % 8 == 1 else pa.birth_formula(p)
        self.assertFalse(pa.births_check(self.B, self.direct, self.events, formula=wrong)["birth_formula"]["pass"])

        def swapped(p):
            m, pole = pa.birth_formula(p)
            return (m, "8m-7") if pole == "8m-3" else (m, pole)
        self.assertFalse(pa.births_check(self.B, self.direct, self.events, formula=swapped)["pass"])

    def _windows(self, **kw):
        rows = []
        for ell in self.ells:
            for n in range(self.B - 1, 2 * self.B + 1):
                res = pa.fresh_window(S, n, ell, events=self.events, **kw)
                if res is not None:
                    rows.extend(res["rows"])
        return rows

    def test_exact_fresh_component(self):
        rows = self._windows()
        self.assertGreater(len(rows), 50)
        for row in rows:
            for c in pa.ROW_CHECKS:
                self.assertTrue(row[c], (c, row))
        self.assertEqual({r["pole"] for r in rows}, {"8m-7", "8m-3", "4m-1"})

    def test_mutation_wrong_rho_is_caught(self):
        def rho_no_half(pole, k, p):
            return -pow(16, k, p) % p if pole == "4m-1" else pa.rho_expected(pole, k, p)
        rows = self._windows(rho_fn=rho_no_half)
        self.assertTrue(any(not r["component_eq_rho_over_p"] for r in rows if r["pole"] == "4m-1"))

        def rho_age_shift(pole, k, p):
            return pa.rho_expected(pole, k + 1, p)
        self.assertTrue(any(not r["component_eq_rho_over_p"] for r in self._windows(rho_fn=rho_age_shift)))

    def test_mutation_wrong_birth_pole_is_caught(self):
        def births_wrong(m):
            out = []
            for p, pole, c in ((8 * m - 7, "8m-7", Fraction(4)), (8 * m - 5, "8m-3", Fraction(-1)),
                               (4 * m - 1, "4m-1", Fraction(-1, 2))):
                if p >= 7 and ic.is_prime(p):
                    out.append((p, pole, c))
            return out
        rows = self._windows(births_fn=births_wrong)
        self.assertTrue(any(not r["v_p_eq_minus_1"] for r in rows))

    def test_inequation_hD_not_integer(self):
        for ell in self.ells:
            for n in range(self.B, 2 * self.B):
                res = pa.fresh_window(S, n, ell)
                if res is None:
                    continue
                for h in pa.MODES:
                    self.assertNotEqual((h * res["D"]).denominator, 1)

    def test_iad09d_literal_weld_fails_exactly_at_half_coefficient_age_zero(self):
        """Pins a defect in the literal IAD-09(d) statement (see RESULTS theorem_statement_findings):
        the term -1/(2p) of the 4m-1 pole at age 0 has Q_p/Z_p class (p-1)/(2p) but real value
        mod 1 (2p-1)/(2p); the product-formula form {t}_p + {t}_2 = t mod 1 always holds."""
        rows = [r for r in self._windows() if r["weld_applicable"]]
        fails = [r for r in rows if not r["weld_literal_p_component_eq_real_mod_1"]]
        self.assertTrue(fails)
        self.assertTrue(all(r["pole"] == "4m-1" and r["j"] == r["ell"] for r in fails))
        self.assertTrue(all(r["weld_literal_p_component_eq_real_mod_1"] for r in rows if r["weld_integral_coefficient"]))
        self.assertTrue(all(r["weld_product_formula_p_plus_2_component"] for r in rows))
        p = fails[0]["p"]
        t = Fraction(-1, 2 * p)
        self.assertEqual(ic.p_adic_component(t, p), Fraction(p - 1, 2 * p))
        self.assertEqual(pa.ffrac(t), Fraction(2 * p - 1, 2 * p))

    def test_ell_pair_matches_float_formula_on_holdout_shells(self):
        import math
        for B in pa.HOLDOUT_SHELLS:
            l0, l1 = pa.ell_pair(B)
            self.assertEqual(l0, math.ceil(2.25 * math.log(B, 16)))
            self.assertEqual(l1, math.floor(4.5 * math.log(B, 16)))


# ------------------------------------------------------------------------------ PR-1.10

class TestSeamLaw(unittest.TestCase):
    N = 300

    def test_machin_instrument_calibration(self):
        known = int("3243F6A8885A308D313198A2E0370734", 16)  # pi = 3.243F6A8885A308D313198A2E0370734...
        self.assertEqual(pa.pi_floor_bits(4 * 31), known)
        self.assertEqual(pa.pi_floor_hex_mpmath(31), known)
        self.assertEqual(pa.x_scaled_machin(500), ic._x_scaled(500))

    def test_true_seed_seam_law_against_independent_pi(self):
        res = pa.true_seed_seam(S, self.N, self.N + 100)
        for name, c in res["checks"].items():
            self.assertTrue(c["pass"], (name, c))
        self.assertEqual(res["counts"]["eps_events_calibration"], 0)
        self.assertTrue(res["swt04"]["pass"])

    def test_mutation_pole_mutated_forcing_breaks_digit_agreement(self):
        n_max, n_src = 60, 90
        Mh = n_max + 66
        X = pa.x_scaled_machin(Mh)
        H = [X >> (4 * (Mh - n)) for n in range(n_max + 2)]
        pi_digits = [H[n + 1] - 16 * H[n] for n in range(n_max + 1)]

        def run(forcing, sup):
            U = [Fraction(0)]
            for n in range(1, n_src + 1):
                U.append(16 * U[-1] + forcing(n))

            def tail(n):
                s = sum((Fraction(forcing(n + j), 16 ** j) for j in range(1, 49)), Fraction(0))
                rem = Fraction(sup, 15 * 16 ** 48)
                return s - rem, s + rem
            return pa.carry_and_seam(U, forcing, n_max, n_src, tail, H=None, lookahead=False)["d"]

        self.assertEqual(run(ic.r, 8), pi_digits)  # control: true forcing, source-side digits

        def mutant(n):
            return four_pole_forcing(n, poles=(7, 4, 3, 1))
        self.assertNotEqual(run(mutant, 8), pi_digits)

    def _forced(self, n0, a_run, horizon):
        s = pa.forced_seam_seed(S, n0, a_run)
        n_src = horizon + 60
        U = [S.U[n] + 16 ** n * s for n in range(n_src + 1)]
        Mh = horizon + 66
        lo, hi, _ = pa.x_interval(Mh)
        H = [pa.ffloor(16 ** n * (lo + s)) for n in range(horizon + 2)]
        self.assertEqual(H, [pa.ffloor(16 ** n * (hi + s)) for n in range(horizon + 2)])
        return U, H, n_src

    def test_forced_seam_control_satisfies_items_3_to_5(self):
        res = pa.forced_seam_control(S, 60, 2, horizon=120)
        self.assertTrue(res["pass"], {k: v for k, v in res["checks"].items() if not v["pass"]})
        self.assertLessEqual({60, 61, 62}, set(res["eps_event_positions"]))
        self.assertNotIn(63, res["eps_event_positions"])
        self.assertIn(63, res["carry16_positions"])
        self.assertGreaterEqual(res["antecedents_item3_item4"]["item4_kappa16"], 1)

    def test_mutation_dropping_carry_16_breaks_reconstruction(self):
        U, H, n_src = self._forced(60, 0, 120)

        def clamped(frac_prev, r_n):
            return min(pa.kappa_swt02(frac_prev, r_n), 15)
        good = pa.carry_and_seam(U, ic.r, 120, n_src, ic.tail_interval, H)
        bad = pa.carry_and_seam(U, ic.r, 120, n_src, ic.tail_interval, H, lookahead=False, kappa_fn=clamped)
        self.assertTrue(good["checks"]["C_equals_sum_16pow_kappa"]["pass"])
        self.assertFalse(bad["checks"]["C_equals_sum_16pow_kappa"]["pass"])
        self.assertFalse(bad["checks"]["seam_law_d_eq_kappa_plus_eps_minus_16eps"]["pass"])

    def test_mutation_wrong_cocycle_sign_is_caught(self):
        U, H, n_src = self._forced(60, 1, 120)
        ev = pa.carry_and_seam(U, ic.r, 120, n_src, ic.tail_interval, H)
        kap, eps = ev["kappa"], ev["eps"]
        d = [H[n + 1] - 16 * H[n] for n in range(121)]
        self.assertTrue(all(d[n] == kap[n + 1] + eps[n + 1] - 16 * eps[n] for n in range(121)))
        self.assertFalse(all(d[n] == kap[n + 1] - eps[n + 1] + 16 * eps[n] for n in range(121)))

    def test_coherent_seed_control(self):
        res = pa.coherent_seed_control(S, horizon=100)
        self.assertTrue(res["pass"], res["checks"])
        self.assertTrue(res["item5_expected_failure"]["item5_fails_as_expected"])
        self.assertEqual(res["eps_rule_boundary_case"]["n_with_overlapping_enclosures"], 102)


# ------------------------------------------------------------------------------ PR-1.11 / SWT-05

class TestTransport(unittest.TestCase):
    def test_swt01_on_planted_streams(self):
        for seed in (1, 2):
            v, w, pos = pa.planted_stream(pa.SEED + 900 + seed, length=4000)
            self.assertEqual(len(pos), 63)
            self.assertTrue(pa.swt01_check(v, w, N_list=[500, 2000, 3998])["pass"])

    def test_swt01_bound_is_attained_and_halved_bound_fails(self):
        v, w, pos = pa.planted_stream(pa.SEED + 950, length=4000, target_letter=0)
        res = pa.swt01_check(v, w, N_list=[3998])
        self.assertTrue(res["pass"])
        k1 = [r for r in res["rows"] if r["k"] == 1][0]
        self.assertEqual(k1["max_abs_difference"], sum(1 for i in pos if i < 3998))  # letter 0 gains every edit
        self.assertLessEqual(k1["edits_before_N_plus_k"] - k1["max_abs_difference"], 1)  # bound sharp for k = 1
        self.assertFalse(pa.swt01_check(v, w, N_list=[3998], bound_fn=lambda k, E: k * E // 2)["pass"])

    def test_swt05b_isotone_and_mutation(self):
        A, P = 64, 256
        orbit = ic.CompletedOrbit(2 * A)
        pts, delta = pa.orbit_points(orbit, range(A, 2 * A), P)
        self.assertTrue(pa.swt05b_check(pts, P, delta)["pass"])
        self.assertFalse(pa.swt05b_check(pts, P, delta, with_q_factor=False)["pass"])


# ------------------------------------------------------------------------------ AT-07 control

class TestAT07(unittest.TestCase):
    def test_null_source_bounds_and_depths(self):
        res = pa.at07_section(n_max=120, B=0)
        self.assertTrue(res["z_eq_w_minus_2r"]["pass"])
        self.assertTrue(res["bounds_minus_1_over_8n_plus_1_lt_E_n_lt_0"]["pass"])
        self.assertTrue(res["conductor_depth_v_p_E_ceil_Q_over_8_eq_minus_a"]["pass"])
        self.assertEqual(res["z_1"], "-8/105")

    def test_mutated_null_vector_breaks_bounds(self):
        Z = list(pa.AT07_Z)
        Z[6] = -2
        res = pa.at07_section(n_max=120, B=0, Z=tuple(Z))
        self.assertFalse(res["bounds_minus_1_over_8n_plus_1_lt_E_n_lt_0"]["pass"])


# ------------------------------------------------------------------------------ end-to-end

class TestQuickRun(unittest.TestCase):
    def test_quick_probe_exit_zero_and_deterministic(self):
        with tempfile.TemporaryDirectory() as tmp, contextlib.redirect_stdout(io.StringIO()):
            a, b = Path(tmp) / "a.json", Path(tmp) / "b.json"
            self.assertEqual(pa.main(["--quick", "--out", str(a)]), 0)
            self.assertEqual(pa.main(["--quick", "--out", str(b)]), 0)
            self.assertEqual(a.read_bytes(), b.read_bytes())
            R = json.loads(a.read_text())
        self.assertTrue(R["PR-1_all_pass"])
        for key in ("PR-1.7", "PR-1.8", "PR-1.9", "PR-1.10", "PR-1.11"):
            self.assertTrue(R["PR-1"][key]["pass"], key)
        self.assertIsNone(R["PR-2"]["PR-2.6"]["met"])  # holdout seam range is not run in quick mode


if __name__ == "__main__":
    unittest.main()
