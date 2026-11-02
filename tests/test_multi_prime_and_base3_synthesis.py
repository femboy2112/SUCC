#!/usr/bin/env python3
"""Root-level regression suite for Mega-Round II (MPB-01..MPB-18).

Multi-Prime & Base-3 Synthesis on branch research/prime-cofactor-nonconspiracy-2026-11-02.
Covers:
  1. Front 1 (MPB-01..04): Multi-prime simultaneous cofiber recurrence, two-prime Midy,
     prime-window overlap cone support, and 3-edge BBP decomposition.
  2. Front 2 (MPB-05..08): k-step Radix-B coercivity, cross-radix (16, 3) scale bridge,
     coupled two-radix Lagrange identity, and multi-step strided Diophantine thresholds.
  3. Front 3 (MPB-09..12): Reduced Laurent trinomial, Stirling-basis alpha_k, closed-form
     Eulerian moments, diagonal Padé approximants, and second-order difference discriminators.
  4. Front 4 (MPB-13..15): Midpoint-centered spill gauge halving mode transport bounds,
     nilpotent 4-step dyadic shift cascade, and Walsh block covariance representation.
  5. Front 5 (MPB-16..18): Aurifeuillian quarter-degree factorization of 4^L + 1 and
     coprime splitting of Phi_{2L}(4), exact 2-adic order law, and sharpened quarter-degree sieve.
  6. Independent second-algorithm cross-checks, adversarial countermodels, receipt check,
     and Lean 4.14.0 kernel verification (zero sorryAx, zero Classical.choice).
"""

from __future__ import annotations

from fractions import Fraction
import json
from pathlib import Path
import sys
import unittest

REPO_ROOT = Path(__file__).resolve().parent.parent
DOSSIER_DIR = REPO_ROOT / "research" / "2026-11-02" / "multi_prime_and_base3_synthesis"
sys.path.insert(0, str(DOSSIER_DIR))

import independent_oracle_2 as oracle  # noqa: E402
import mega_round_2_engine as engine  # noqa: E402


class TestMultiPrimeBase3SynthesisMegaRound(unittest.TestCase):
    """Comprehensive test suite for Mega-Round II (MPB-01..MPB-18)."""

    @classmethod
    def setUpClass(cls) -> None:
        cls.receipt = oracle.build_full_receipt_2()
        cls.summary = cls.receipt["engine_summary"]
        cls.oracle_checks = cls.receipt["independent_oracle_checks"]

    # ------------------------------------------------------------------
    # Front 1: Multi-Prime CRT Cofiber Recurrence & Geometric Coupling
    # ------------------------------------------------------------------
    def test_mpb01_simultaneous_multi_prime_cofiber(self) -> None:
        f1 = self.summary["front_1_multi_prime_cofiber"]
        c2 = f1["two_prime_p13_p17"]
        self.assertTrue(c2["simultaneous_recurrence_verified"])
        self.assertTrue(c2["all_primes_p_integral"])
        self.assertTrue(c2["zero_cross_coupling_verified"])

        c3 = f1["three_prime_p13_p17_p29"]
        self.assertTrue(c3["simultaneous_recurrence_verified"])
        self.assertTrue(c3["all_primes_p_integral"])
        self.assertTrue(self.oracle_checks["front1"]["multi_prime_carries_match_long_division"])

    def test_mpb02_two_prime_midy_and_twisted_gauss(self) -> None:
        f1 = self.summary["front_1_multi_prime_cofiber"]
        c_midy = f1["two_prime_midy_p17_p241"]
        self.assertTrue(c_midy["periodicity_verified"])
        self.assertTrue(c_midy["simultaneous_midy_holds"])
        self.assertTrue(c_midy["max_gauss_bound_holds"])

        c_coprime = f1["two_prime_coprime_p17_p29"]
        self.assertTrue(c_coprime["coprime_orders"])
        self.assertTrue(c_coprime["gauss_factorization_verified"])

    def test_mpb03_prime_window_overlap_cone_support(self) -> None:
        f1 = self.summary["front_1_multi_prime_cofiber"]
        c_cone = f1["overlap_cone_kernel_X250"]
        self.assertTrue(c_cone["strict_cone_support_verified"])
        self.assertTrue(c_cone["exact_mass_identity_verified"])

    def test_mpb04_three_edge_decomposition_and_pole_isolation(self) -> None:
        f1 = self.summary["front_1_multi_prime_cofiber"]
        c_edge = f1["three_edge_decomposition_H50"]
        self.assertTrue(c_edge["three_edge_identity_verified"])
        self.assertTrue(c_edge["mod8_pole_isolation_duality_verified"])
        self.assertTrue(self.oracle_checks["front1"]["three_edge_forcing_matches_bbp_r"])

    # ------------------------------------------------------------------
    # Front 2: Multi-Step & Cross-Radix (16, 3) Coercivity
    # ------------------------------------------------------------------
    def test_mpb05_and_mpb06_k_step_and_scale_bridge(self) -> None:
        f2 = self.summary["front_2_cross_radix_and_k_step"]
        c_scale = f2["k_step_and_scale_bridge"]
        self.assertEqual(c_scale["scale_proximity_16_sq_minus_3_pow5"], 13)
        self.assertEqual(c_scale["coercivity_gap_6513"], 6513)
        self.assertTrue(c_scale["gap_equals_13_times_501"])
        self.assertEqual(c_scale["joint_lambda_sum_16_3"], 400)
        self.assertEqual(c_scale["joint_lambda_pair_16_3"], 266)
        self.assertEqual(c_scale["joint_frob_norm_666"], 666)
        self.assertTrue(c_scale["coupled_lagrange_identity_verified"])
        self.assertTrue(self.oracle_checks["front2"]["k_step_algebraic_identity_verified"])

    def test_mpb07_and_mpb08_strided_diophantine_thresholds(self) -> None:
        f2 = self.summary["front_2_cross_radix_and_k_step"]
        c_str = f2["strided_thresholds_stride2"]
        self.assertEqual(c_str["saving_ratio"], "66049/83521")
        self.assertLess(c_str["saving_ratio_float"], 0.791)
        self.assertLessEqual(c_str["J0_strided"], c_str["J0_unstrided"])
        self.assertLessEqual(c_str["J2_strided"], c_str["J2_unstrided"])

    # ------------------------------------------------------------------
    # Front 3: Reduced Laurent Trinomial, Stirling Basis & Borel/Padé
    # ------------------------------------------------------------------
    def test_mpb09_reduced_trinomial_and_alphas(self) -> None:
        f3 = self.summary["front_3_reduced_laurent_trinomial"]
        c_trin = f3["reduced_trinomial_and_alphas"]
        expected_alphas = (1, -4, 13, -42, 140, -476, 1628, -5568)
        self.assertEqual(c_trin["alphas_1_to_8"], expected_alphas)
        self.assertTrue(c_trin["all_c_tilde_odd"])
        self.assertTrue(c_trin["mod8_congruence_verified"])

    def test_mpb10_eulerian_annihilation(self) -> None:
        f3 = self.summary["front_3_reduced_laurent_trinomial"]
        c_eul = f3["eulerian_annihilation"]
        self.assertTrue(c_eul["eulerian_moments_match_series"])
        self.assertTrue(c_eul["bbp_annihilates_15_pow_d_plus_1"])
        self.assertTrue(self.oracle_checks["front3"]["stirling_vs_eulerian_coefficients_match"])

    def test_mpb11_pade_borel_approximants(self) -> None:
        f3 = self.summary["front_3_reduced_laurent_trinomial"]
        c_pade = f3["pade_borel_p11"]
        self.assertEqual(c_pade["p11_at_n1"], "1/120")
        self.assertTrue(self.oracle_checks["front3"]["pade_p11_at_1_is_one_over_120"])

    def test_mpb12_second_order_difference_zero_seed(self) -> None:
        f3 = self.summary["front_3_reduced_laurent_trinomial"]
        c_diff = f3["second_order_difference"]
        self.assertTrue(c_diff["discriminators_verified"])
        self.assertEqual(c_diff["second_order_diff_d2_U0"], "180164/4095")

    # ------------------------------------------------------------------
    # Front 4: Midpoint-Centered Spill Gauge & Walsh Nilpotent Shift
    # ------------------------------------------------------------------
    def test_mpb13_midpoint_centered_transport(self) -> None:
        f4 = self.summary["front_4_midpoint_spill_and_walsh"]
        c_mid = f4["midpoint_centered_transport"]
        self.assertTrue(c_mid["all_horizons_sub_unitary"])
        by_exp = {r["log2_N"]: r for r in c_mid["rows"]}
        self.assertAlmostEqual(by_exp[16]["midpoint_centered_max_upper"], 0.134203, places=5)
        self.assertAlmostEqual(by_exp[64]["midpoint_centered_max_upper"], 0.054455, places=5)
        self.assertAlmostEqual(by_exp[256]["midpoint_centered_max_upper"], 0.018302, places=5)
        for r in c_mid["rows"]:
            self.assertTrue(r["exact_halving_verified"])

    def test_mpb14_nilpotent_dyadic_shift(self) -> None:
        f4 = self.summary["front_4_midpoint_spill_and_walsh"]
        c_shift = f4["nilpotent_dyadic_shift"]
        self.assertTrue(c_shift["cascade_order_verified"])
        self.assertTrue(c_shift["nilpotent_index_is_4"])
        self.assertEqual(c_shift["block_dimensions"], {"1": 1, "2": 2, "3": 4, "4": 8})
        self.assertTrue(self.oracle_checks["front4"]["dyadic_doubling_nilpotent_index_is_4"])

    def test_mpb15_walsh_block_covariance(self) -> None:
        f4 = self.summary["front_4_midpoint_spill_and_walsh"]
        c_cov = f4["block_covariance"]
        self.assertTrue(c_cov["block_orthogonality_verified"])

    # ------------------------------------------------------------------
    # Front 5: Aurifeuillian Quarter-Degree Factorization & Order Valuation
    # ------------------------------------------------------------------
    def test_mpb16_aurifeuillian_quarter_degree(self) -> None:
        f5 = self.summary["front_5_aurifeuillian_quarter_degree"]
        c_aurif = f5["aurifeuillian_factors_up_to_15"]
        self.assertTrue(c_aurif["all_products_match_four_pow_L_plus_1"])
        self.assertTrue(c_aurif["all_aurifeuillian_factors_coprime"])
        self.assertTrue(self.oracle_checks["front5"]["aurifeuillian_quarter_degree_products_verified"])

    def test_mpb17_ord16_two_adic_law(self) -> None:
        f5 = self.summary["front_5_aurifeuillian_quarter_degree"]
        c_ord = f5["ord16_two_adic_law"]
        self.assertTrue(c_ord["two_adic_formula_verified"])
        self.assertTrue(c_ord["trichotomy"]["mod8_5_all_odd"])

    def test_mpb18_sharpened_quarter_degree_sieve(self) -> None:
        f5 = self.summary["front_5_aurifeuillian_quarter_degree"]
        c_sieve = f5["sharpened_sieve_X10000"]
        self.assertTrue(c_sieve["bound_holds"])
        self.assertLess(c_sieve["sharpened_quarter_bound"], c_sieve["unsharpened_half_bound"])

    # ------------------------------------------------------------------
    # Adversarial Countermodels, Input Guards, Receipt & Lean 4 Kernel
    # ------------------------------------------------------------------
    def test_adversarial_countermodels_2(self) -> None:
        adv = self.oracle_checks["adversarial_countermodels"]
        self.assertTrue(adv["d2_zero_seed_strictly_positive"])
        self.assertTrue(adv["mutant_pole_vector_breaks_stroboscope"])
        self.assertTrue(adv["decimal_fails_hex_ternary_scale_proximity"])

    def test_input_guards(self) -> None:
        with self.assertRaises(ValueError):
            engine.bbp_r(0)
        with self.assertRaises(ValueError):
            engine.edge_f(0, 3)
        with self.assertRaises(ValueError):
            engine.multiplicative_order(16, 8)
        with self.assertRaises(ValueError):
            engine.aurifeuillian_factors(4)  # 4 is even

    def test_saved_receipt_and_lean4_kernel_verification(self) -> None:
        lean_cert = self.oracle_checks["lean_kernel_certificate"]
        self.assertTrue(lean_cert["verified"])
        self.assertEqual(lean_cert["exit_code"], 0)
        self.assertEqual(lean_cert["axiom_print_count"], 18)
        self.assertTrue(lean_cert["zero_sorryAx"])
        self.assertTrue(lean_cert["zero_classical_choice"])

        receipt_path = DOSSIER_DIR / "EXACT_MEGA_ROUND_2_RECEIPT.json"
        self.assertTrue(receipt_path.exists())
        saved = json.loads(receipt_path.read_text(encoding="utf-8"))
        fresh = json.loads(json.dumps(self.receipt))
        self.assertEqual(saved, fresh)


if __name__ == "__main__":
    unittest.main()
