"""Unit tests for Wave II theorems & countermodels (Agents G, H, I, K) and
Moonshot C parity-split Bessel coercivity.
"""
import unittest
from fractions import Fraction as F

from observational_succ.fucc_braid_resonance_capsules import (
    WaveTTCapsuleError,
    fucc_fractional_gamma_braid_certificate,
    fucc_self_carry_braid_certificate,
    fucc_succ_functoriality_obstructions,
    odd_bubble_offline_pair_certificate,
    even_sector_small_window_submersion_certificate,
    delayed_detection_aliasing_countermodels,
    build_rational_ldlt_schur_capsule,
    verify_rational_ldlt_schur_capsule,
    single_moment_contact_rigidity_certificate,
)
from observational_succ.tate_weighted_bessel_four_schur import (
    KAPPA_ODD_LOWER,
    KAPPA_EVEN_LOWER,
    source_parity_split_four_moment_coercivity_certificate,
)


class AgentGCategoricalBraidTests(unittest.TestCase):
    def test_fractional_gamma_gauss_legendre_and_cocycle(self):
        for p in (2, 3, 5):
            cert = fucc_fractional_gamma_braid_certificate(p=p, n_max=5)
            self.assertTrue(cert["all_gauss_legendre_factorizations_exact"])
            self.assertTrue(cert["all_kummer_valuations_equal_digit_sum"])
            self.assertFalse(cert["RH_proved"])

    def test_self_carry_frobenius_invariance_and_step_valuation(self):
        for p in (2, 3, 5):
            cert = fucc_self_carry_braid_certificate(p=p, n_max=15, k_max=3)
            self.assertTrue(cert["frobenius_scale_invariance_verified"])
            self.assertTrue(cert["successor_step_valuation_law_verified"])
            self.assertFalse(cert["RH_proved"])

    def test_functoriality_obstructions_and_composite_prime_reject(self):
        obs = fucc_succ_functoriality_obstructions()
        self.assertTrue(obs["G_O1_strict_additive_homomorphism_refuted"])
        self.assertTrue(obs["G_O2_strict_gamma_homomorphism_refuted"])
        self.assertTrue(obs["G_O3_single_prime_slice_misses_cross_prime_composite"])
        self.assertFalse(obs["RH_proved"])
        with self.assertRaises(WaveTTCapsuleError):
            fucc_fractional_gamma_braid_certificate(p=6)


class AgentHResonanceTests(unittest.TestCase):
    def test_odd_bubble_signature_and_submersion(self):
        odd_cert = odd_bubble_offline_pair_certificate(Delta=F(1, 4), gamma=F(14), a=F(1, 2))
        self.assertEqual(odd_cert["signature_on_4D_quadruplet_span"], (2, 2))
        self.assertEqual(odd_cert["odd_bubble_L2_norm_squared"], F(1, 840))
        self.assertEqual(odd_cert["odd_bubble_H1_seminorm_squared"], F(1, 20))
        self.assertFalse(odd_cert["RH_proved"])

        sub_cert = even_sector_small_window_submersion_certificate(
            Delta=F(1, 20), gamma=F(14), a=F(1, 4), T=F(20)
        )
        self.assertTrue(sub_cert["submerged_below_tail_at_T"])
        self.assertEqual(sub_cert["window_scaling_exponent_a"], 7)
        self.assertFalse(sub_cert["RH_proved"])

    def test_delayed_detection_aliasing_countermodels(self):
        cm = delayed_detection_aliasing_countermodels(Delta=F(1, 5), gamma=F(10), kappa=F(1, 2))
        self.assertTrue(cm["H_C2_strictly_positive_on_all_L2_minus_a_to_a"])
        self.assertTrue(cm["H_C3_strictly_negative_fourth_cumulant"])
        self.assertEqual(cm["H_C3_fourth_cumulant_discrepancy"], -F(16))
        self.assertFalse(cm["RH_proved"])


class AgentICapsuleTests(unittest.TestCase):
    def test_pd_psd_and_schur_capsules_verify_division_free(self):
        M_pd = ((F(4), F(2)), (F(2), F(3)))
        cap_pd = build_rational_ldlt_schur_capsule(M_pd, claim_fqid="PDQ-01", mode="PD")
        v_pd = verify_rational_ldlt_schur_capsule(cap_pd)
        self.assertTrue(v_pd["finite_algebra_verified"])
        self.assertTrue(v_pd["division_free_ring_check"])
        self.assertFalse(v_pd["analytic_premises_discharged_by_capsule"])
        self.assertFalse(v_pd["RH_proved"])

        M_schur = (
            (F(5), F(1), F(2)),
            (F(1), F(4), F(1)),
            (F(2), F(1), F(3)),
        )
        cap_s = build_rational_ldlt_schur_capsule(
            M_schur, claim_fqid="CFS-06", mode="SCHUR_COMPLEMENT", low_rank=1
        )
        v_s = verify_rational_ldlt_schur_capsule(cap_s)
        self.assertTrue(v_s["finite_algebra_verified"])

    def test_hostile_capsule_controls_fail_closed(self):
        # 1. Colliding bare claim ID rejected:
        for bare in ("PH-01", "PB-01", "TS-01", "WA-01", "FAKE-99"):
            with self.assertRaises(WaveTTCapsuleError):
                build_rational_ldlt_schur_capsule(((F(1),),), claim_fqid=bare, mode="PD")
        # 2. Disambiguated FQID accepted:
        cap = build_rational_ldlt_schur_capsule(((F(2),),), claim_fqid="PH.PROF-01", mode="PD")
        self.assertTrue(verify_rational_ldlt_schur_capsule(cap)["finite_algebra_verified"])
        # 3. Tampered pivot or RH_proved=True rejected:
        tampered = dict(cap, diagonal_D=(F(3),))
        with self.assertRaises(WaveTTCapsuleError):
            verify_rational_ldlt_schur_capsule(tampered)
        rh_tampered = dict(cap, RH_proved=True)
        with self.assertRaises(WaveTTCapsuleError):
            verify_rational_ldlt_schur_capsule(rh_tampered)


class AgentKContactRigidityTests(unittest.TestCase):
    def test_single_moment_contact_rigidity(self):
        cert = single_moment_contact_rigidity_certificate(
            c_perturbation=F(11, 7), a=F(1, 2), rank=6
        )
        self.assertTrue(cert["exact_single_moment_recovery"])
        self.assertEqual(cert["recovered_c_from_M11"], F(11, 7))
        self.assertTrue(cert["M_Ka_is_strictly_diagonal"])
        self.assertTrue(cert["K_galerkin_has_off_diagonal_coupling"])
        self.assertTrue(cert["boundary_moments_M31_M42_contact_invariant"])
        self.assertFalse(cert["RH_proved"])


class MoonshotCParityCoercivityTests(unittest.TestCase):
    def test_parity_split_coercivity_certificate(self):
        cert = source_parity_split_four_moment_coercivity_certificate()
        self.assertEqual(cert["odd_sector"]["kappa_odd_certified_rational"], KAPPA_ODD_LOWER)
        self.assertEqual(cert["even_sector"]["kappa_even_certified_rational"], KAPPA_EVEN_LOWER)
        self.assertGreater(cert["odd_sector"]["kappa_odd_exact_lower"], F(63, 500))
        self.assertGreater(cert["even_sector"]["kappa_even_exact_lower"], F(153, 500))
        self.assertEqual(cert["odd_sector"]["active_angular_modes"][0], 4)
        self.assertEqual(cert["even_sector"]["active_angular_modes"][0], 5)
        self.assertFalse(cert["RH_proved"])


if __name__ == "__main__":
    unittest.main()
