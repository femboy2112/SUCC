#!/usr/bin/env python3
"""Root-level regression suite for the Five-Front BBP Pi-Normality Mega-Round (PCN-01..PCN-18).

Covers:
1. Front 1 (PCN-01..PCN-04): Prime-cofiber carry recurrence, Midy complementarity,
   twisted-Gauss bilinear cofiber bound, and higher-octave stroboscope unification.
2. Front 2 (PCN-05..PCN-08): Parametric Diophantine thresholds (#304, #321) and
   universal radix-B variational coercivity (#311 norm unification, direct k-step gain).
3. Front 3 (PCN-09..PCN-12): All-order Laurent EGF Aurifeuillian dyadic collapse,
   Gevrey-1 factorial asymptotics & optimal truncation, Fejér diagonal restoration
   of SZB-02, and finite-window zero-seed discriminators against s_* = -pi/16.
4. Front 4 (PCN-13..PCN-15): Three-progression prime-power birth law, stratified
   spill-censored non-vacuous mode transport (< 1 at all N >= 2^8), and 4-bit
   Walsh-Fourier MSB block-triangular codec.
5. Front 5 (PCN-16..PCN-18): p == 5 (mod 8) odd-order half-degree cyclotomic
   divisibility law, cyclotomic divisor-product order sieve, and small-order
   exception census (p=13, p=109 uniqueness).
6. Adversarial countermodels, input-validation guards, deterministic JSON receipt
   verification, and Lean 4.14.0 kernel verification.
"""

from __future__ import annotations

from fractions import Fraction
import json
from pathlib import Path
import sys
import unittest

REPO_ROOT = Path(__file__).resolve().parent.parent
DOSSIER_DIR = REPO_ROOT / "research" / "2026-11-02" / "prime_cofactor_nonconspiracy"
sys.path.insert(0, str(DOSSIER_DIR))

import independent_oracle as oracle  # noqa: E402
import mega_round_engine as engine  # noqa: E402


class TestPrimeCofactorNonConspiracyMegaRound(unittest.TestCase):
    """Comprehensive tests for all 18 claims (PCN-01..PCN-18) and independent oracles."""

    @classmethod
    def setUpClass(cls) -> None:
        cls.full_receipt = oracle.build_full_receipt()
        cls.summary = cls.full_receipt["engine_summary"]
        cls.oracle_checks = cls.full_receipt["independent_oracle_checks"]

    # ------------------------------------------------------------------
    # Front 1: Prime-Cofiber Recurrence, Midy, Bilinear Bound, Stroboscope
    # ------------------------------------------------------------------
    def test_pcn01_prime_cofiber_recurrence_and_independent_long_division(self) -> None:
        f1 = self.summary["front_1_cofiber_and_stroboscope"]
        for key in ("cofiber_p13", "cofiber_p17", "cofiber_p29"):
            cert = f1[key]
            self.assertTrue(cert["p_local_integrality_verified"])
            self.assertTrue(cert["cofiber_recurrence_verified"])
            self.assertTrue(all(0 <= d <= 15 for d in cert["carry_digits"]))
        self.assertTrue(self.oracle_checks["long_division_vs_cofiber_carry_digits_match"])
        self.assertTrue(self.oracle_checks["closed_form_vs_iterative_orbit_match"])
        adv = self.oracle_checks["adversarial_countermodels"]
        self.assertTrue(adv["p257_true_step_sum_nonzero"])
        self.assertLess(adv["p257_E_true"], -0.5)

    def test_pcn02_midy_complementarity_and_half_period_lift(self) -> None:
        f1 = self.summary["front_1_cofiber_and_stroboscope"]
        for key in ("midy_p17", "midy_p97", "midy_p241", "midy_p257"):
            cert = f1[key]
            self.assertEqual(cert["order_L"] % 2, 0)
            self.assertTrue(cert["residue_complement_p_verified"])
            self.assertTrue(cert["carry_complement_15_verified"])
            self.assertTrue(cert["half_period_p_annihilation_verified"])
            for _, vp_val in cert["valuations_vp_Uj_plus_UjM"]:
                self.assertGreaterEqual(vp_val, 0)

    def test_pcn03_bilinear_cofiber_erosion_and_twisted_gauss_bound(self) -> None:
        f1 = self.summary["front_1_cofiber_and_stroboscope"]
        for key in ("bilinear_gauss_p17_h1", "bilinear_gauss_p29_h1", "bilinear_gauss_p37_h2"):
            cert = f1[key]
            self.assertTrue(cert["twisted_gauss_bound_holds"])
            self.assertTrue(cert["untwisted_bound_holds"])
            self.assertTrue(cert["plancherel_identity_holds"])
            self.assertTrue(cert["bilinear_identity_holds"])
            self.assertLessEqual(cert["max_twisted_gauss_abs"], cert["sqrt_p"] + 1e-9)

    def test_pcn04_higher_octave_stroboscope_and_p73_resonance(self) -> None:
        f1 = self.summary["front_1_cofiber_and_stroboscope"]
        for key in ("stroboscope_p37_k4", "stroboscope_p41_k4", "stroboscope_p73_k4_resonance"):
            cert = f1[key]
            self.assertTrue(cert["all_octaves_verified"])
        p73 = f1["stroboscope_p73_k4_resonance"]
        oct4 = p73["octaves"][3]
        self.assertEqual(oct4["octave"], 4)
        self.assertTrue(oct4["p_divides_num_U_l"])
        self.assertGreaterEqual(oct4["vp_at_4th_hit"], 0)
        adv = self.oracle_checks["adversarial_countermodels"]
        self.assertTrue(adv["p73_k4_u4_numerator_divisible_by_73"])
        self.assertEqual(tuple(adv["p73_octave_checkpoint_valuations"]), (-1, -1, -1, 0))
        self.assertTrue(adv["mutant_pole_vector_breaks_stroboscope_J4"])

    # ------------------------------------------------------------------
    # Front 2: Parametric Diophantine Thresholds & Universal Radix-B Coercivity
    # ------------------------------------------------------------------
    def test_pcn05_and_pcn06_parametric_diophantine_thresholds(self) -> None:
        f2 = self.summary["front_2_diophantine_and_coercivity"]
        c1 = f2["unit_constant_C1_mu_15_2"]
        self.assertEqual(c1["J0_stage304"], 17)
        self.assertEqual(c1["J2_stage321_band"], 4)
        mu2 = engine.parametric_diophantine_thresholds(Fraction(0), Fraction(2))
        self.assertEqual(mu2["J0_stage304"], 2)
        self.assertEqual(mu2["J2_stage321_band"], 4)

    def test_pcn07_and_pcn08_universal_radix_coercivity_and_norm_unification(self) -> None:
        f2 = self.summary["front_2_diophantine_and_coercivity"]
        b16 = f2["radix16_variational_duality"]
        self.assertTrue(b16["all_identities_verified"])
        self.assertEqual(b16["lambda_sum"], 289)
        self.assertEqual(b16["lambda_pair"], 257)
        self.assertEqual(b16["adjacent_branch_frob_norm_sq"], 546)
        self.assertEqual(b16["lambda_sum"] + b16["lambda_pair"], b16["adjacent_branch_frob_norm_sq"])
        k2 = b16["k_step_transport_gains"][0]
        self.assertEqual(k2["k"], 2)
        self.assertEqual(k2["direct_constant"], 66049)
        self.assertEqual(k2["iterated_constant"], 83521)
        self.assertEqual(k2["strict_gain"], 17472)

        b3 = f2["radix3_variational_duality"]
        self.assertTrue(b3["all_identities_verified"])
        self.assertEqual(b3["lambda_sum"], 16)
        self.assertEqual(b3["lambda_pair"], 10)
        self.assertEqual(b3["adjacent_branch_frob_norm_sq"], 26)

    # ------------------------------------------------------------------
    # Front 3: Laurent Clock Aurifeuillian Collapse, Gevrey-1, SZB-01/02
    # ------------------------------------------------------------------
    def test_pcn09_and_pcn10_laurent_aurifeuillian_and_gevrey1(self) -> None:
        cert = self.summary["front_3_laurent_and_zero_boundary"]["laurent_gevrey_certificate"]
        self.assertTrue(cert["all_c_tilde_odd_integers"])
        self.assertTrue(cert["all_match_eulerian_moments"])
        self.assertTrue(cert["all_strictly_alternating"])
        self.assertTrue(cert["remainder_sandwich_and_d_star_verified"])
        expected_first_six = [1, -7, 55, -595, 8551, -149467]
        actual_first_six = [r["c_tilde_odd_int"] for r in cert["coefficients"][:6]]
        self.assertEqual(actual_first_six, expected_first_six)
        self.assertTrue(self.oracle_checks["stirling_vs_hurwitz_laurent_numerators_match"])

    def test_pcn11_two_sided_fejer_curvature_repair(self) -> None:
        f3 = self.summary["front_3_laurent_and_zero_boundary"]
        for key in ("two_sided_fejer_d2_h1", "two_sided_fejer_d3_h3"):
            cert = f3[key]
            self.assertTrue(cert["two_sided_positivity_verified"])
            self.assertGreater(cert["two_sided_true_zero"], 0.0)
            self.assertGreater(cert["two_sided_comp_zero"], 0.0)

    def test_pcn12_zero_seed_discriminators_against_s_star(self) -> None:
        cert = self.summary["front_3_laurent_and_zero_boundary"]["zero_seed_discriminators"]
        self.assertTrue(cert["all_discriminators_verified"])
        self.assertEqual(len(cert["records"]), 8)

    # ------------------------------------------------------------------
    # Front 4: Three-Progression Birth Law, Stratified Transport, Walsh Codec
    # ------------------------------------------------------------------
    def test_pcn13_three_progression_birth_law(self) -> None:
        cert = self.summary["front_4_carry_transport_and_walsh"]["prime_power_birth_law"]
        self.assertTrue(cert["exact_three_progression_match"])
        self.assertEqual(cert["horizon"], 500)
        deep = engine.exact_prime_power_birth_certificate(1500)
        self.assertTrue(deep["exact_three_progression_match"])

    def test_pcn14_stratified_non_vacuous_mode_transport(self) -> None:
        cert = self.summary["front_4_carry_transport_and_walsh"]["non_vacuous_spill_transport"]
        self.assertTrue(cert["all_horizons_strictly_sub_unitary"])
        by_exp = {r["log2_N"]: r for r in cert["horizons"]}
        self.assertAlmostEqual(by_exp[16]["max_mode_upper"], 0.268406, places=5)
        self.assertAlmostEqual(by_exp[64]["max_mode_upper"], 0.108909, places=5)
        self.assertAlmostEqual(by_exp[256]["max_mode_upper"], 0.036604, places=5)
        for r in cert["horizons"]:
            self.assertTrue(r["strictly_sub_unitary"])
            self.assertLess(r["max_mode_upper"], 1.0)
        self.assertTrue(self.oracle_checks["midpoint_truncation_factors_exact"])

    def test_pcn15_walsh_fourier_msb_block_codec(self) -> None:
        cert = self.summary["front_4_carry_transport_and_walsh"]["walsh_fourier_codec"]
        self.assertTrue(cert["exact_walsh_inversion_verified"])
        self.assertTrue(cert["parseval_walsh_fourier_verified"])
        self.assertTrue(cert["odd_h_top_walsh_quarter_law_verified"])
        w16 = self.oracle_checks["walsh_4block_N16"]
        w40 = self.oracle_checks["walsh_4block_N40"]
        self.assertTrue(w16["four_block_unitary_selection_verified"])
        self.assertTrue(w40["four_block_unitary_selection_verified"])

    # ------------------------------------------------------------------
    # Front 5: p == 5 (mod 8) Cyclotomic Law & Order-Threshold Sieve
    # ------------------------------------------------------------------
    def test_pcn16_pcn17_pcn18_cyclotomic_sieve_and_census(self) -> None:
        cert = self.summary["front_5_cyclotomic_sieve"]
        self.assertTrue(cert["odd_order_law_verified"])
        self.assertTrue(cert["index_k_equivalence_verified"])
        self.assertTrue(cert["cyclotomic_phi_2L_divisibility_verified"])
        self.assertTrue(cert["cyclotomic_log_bound_verified"])
        self.assertEqual(cert["total_primes_1_mod_4"], 608)
        self.assertEqual(cert["total_large_order_gt_sqrt_p"], 569)
        k1_ex = [p for p, _, k in cert["mod8_5_small_order_exceptions"] if k == 1]
        k3_ex = [p for p, _, k in cert["mod8_5_small_order_exceptions"] if k == 3]
        self.assertEqual(k1_ex, [13])
        self.assertEqual(k3_ex, [109])
        self.assertTrue(self.oracle_checks["polynomial_division_vs_mobius_cyclotomic_match"])

    # ------------------------------------------------------------------
    # Input Validation Guards, Receipt Integrity & Lean 4 Kernel Check
    # ------------------------------------------------------------------
    def test_input_validation_guards(self) -> None:
        with self.assertRaises(ValueError):
            engine.p_adic_valuation_rational(Fraction(1, 2), 2)
        with self.assertRaises(ValueError):
            engine.multiplicative_order(16, 8)
        with self.assertRaises(ValueError):
            engine.authentic_r(0)
        with self.assertRaises(ValueError):
            engine.authentic_orbit(-1)
        with self.assertRaises(ValueError):
            engine.laurent_dyadic_numerator(0)
        with self.assertRaises(ValueError):
            engine.cyclotomic_phi_2L_at_4(4)

    def test_saved_receipt_and_lean4_kernel_verification(self) -> None:
        lean_cert = self.oracle_checks["lean_kernel_certificate"]
        self.assertTrue(lean_cert["verified"])
        self.assertEqual(lean_cert["exit_code"], 0)
        self.assertEqual(lean_cert["axiom_print_count"], 19)
        self.assertTrue(lean_cert["zero_sorryAx"])
        self.assertTrue(lean_cert["zero_classical_choice"])

        receipt_path = DOSSIER_DIR / "EXACT_MEGA_ROUND_RECEIPT.json"
        self.assertTrue(receipt_path.exists())
        saved = json.loads(receipt_path.read_text(encoding="utf-8"))
        fresh = json.loads(json.dumps(self.full_receipt))
        self.assertEqual(saved, fresh)


if __name__ == "__main__":
    unittest.main()
