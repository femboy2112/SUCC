"""Hostile exact audits of the 1/24 coincidence and Tate/eta source transport."""
import unittest
from fractions import Fraction as F

from observational_succ.tate_eta_bernoulli import (
    EtaTransportError, bernoulli_heat_ledger, original_weil_margin_ablation,
    eta_modular_s_defect, eta_T_multiplier_exponent,
    sigma_one, eta_q_log_derivative_coefficients,
    formal_dirichlet_log_derivative, eta_eisenstein_prime_transducer,
    sigma_one_dirichlet_tail_majorant, primary_source_interface_status,
    modular_discriminant_formal_passport, completed_two_critical_track_passport,
)


class BernoulliOneTwentyFourthClaim(unittest.TestCase):
    def test_sign_is_negative_half_zeta_minus_one_not_plus(self):
        d=bernoulli_heat_ledger()
        self.assertEqual(d["B2"], F(1,6))
        self.assertEqual(d["zeta_of_minus_one"], F(-1,12))
        self.assertEqual(d["heat_laurent_constant"], F(-1,12))
        self.assertEqual(d["heat_laurent_t_squared"], F(1,240))
        self.assertEqual(d["canonical_eta_exponent"], F(1,24))
        self.assertEqual(-d["zeta_of_minus_one"]/2,F(1,24))
        self.assertFalse(d["RH_proved"])

    def test_actual_original_weil_margin_falsifies_canonical_identification(self):
        c=original_weil_margin_ablation()
        self.assertEqual(c["source"],"SHA_PINNED_ORIGINAL_ZETA")
        self.assertEqual(c["original_source_lower"],
                         F(18140507408283703,386282620694770800))
        self.assertTrue(c["one_twenty_fourth_works"])
        self.assertTrue(c["one_twenty_second_works"])
        self.assertTrue(c["one_twenty_first_not_certified_by_this_bound"])
        self.assertFalse(c["equal_to_eta_exponent"])
        self.assertFalse(c["arithmetic_eta_normalization_inferred_from_Weil_bound"])
        self.assertFalse(c["RH_proved"])


class DedekindModularSourceGates(unittest.TestCase):
    def test_eta_exponent_fixed_by_S_on_multiple_clocks(self):
        for c in (F(1,2),F(1),F(2),F(3),F(4),F(11,2)):
            a=eta_modular_s_defect(F(1,24),c)
            self.assertEqual(a["log_defect_over_minus_pi"],0)
            self.assertTrue(a["S_transport_passes_at_this_clock"])
            self.assertTrue(a["all_positive_clocks_S_transport"])
        m=eta_modular_s_defect(F(1,22),1)
        self.assertNotEqual(m["log_defect_over_minus_pi"],0)
        self.assertFalse(m["S_transport_passes_at_this_clock"])
        self.assertFalse(m["all_positive_clocks_S_transport"])

    def test_self_dual_probe_blind_spot_and_T_mod_one_are_adversarial(self):
        wrong=F(25,24)  # passes T character, fails S except at t=2*pi
        same=eta_modular_s_defect(wrong,2)
        fresh=eta_modular_s_defect(wrong,3)
        self.assertTrue(same["S_transport_passes_at_this_clock"])
        self.assertTrue(same["self_dual_false_pass_possible"])
        self.assertFalse(fresh["S_transport_passes_at_this_clock"])
        self.assertFalse(fresh["self_dual_false_pass_possible"])
        self.assertTrue(eta_T_multiplier_exponent(wrong)["canonical_T_character"])
        self.assertTrue(eta_T_multiplier_exponent(wrong)["S_still_required_to_fix_integer_gauge"])
        self.assertEqual(eta_T_multiplier_exponent(F(1,24))["eta_power_24_cusp_order"],1)
        self.assertFalse(eta_T_multiplier_exponent(F(1,22))["canonical_T_character"])

    def test_independent_finite_q_product_logarithmic_coefficients(self):
        for N in (1,2,6,12,32,64):
            result=eta_q_log_derivative_coefficients(N)
            self.assertEqual(result[0],F(1,24))
            self.assertEqual(result[1:],tuple(-sigma_one(n) for n in range(1,N+1)))
            self.assertEqual(
                eta_q_log_derivative_coefficients(N,F(1,22))[1:],result[1:])
        self.assertEqual(eta_q_log_derivative_coefficients(6),
                         (F(1,24),F(-1),F(-3),F(-4),F(-7),F(-6),F(-12)))

    def test_hostile_inputs_cannot_launder_source_clocks(self):
        for a,t in ((0,0),(F(1,24),0),(F(1,24),-1),(True,1),(0,0.2)):
            with self.assertRaises(EtaTransportError):
                eta_modular_s_defect(a,t)
        for n in (0,True,0.5,300):
            with self.assertRaises(EtaTransportError):
                eta_q_log_derivative_coefficients(n)


class EisensteinToGenuinePrimeJet(unittest.TestCase):
    def test_dirichlet_and_q_series_are_different_but_related(self):
        d=eta_eisenstein_prime_transducer(80)
        self.assertEqual(d["source_type"],"EISENSTEIN_SIGMA1")
        self.assertTrue(d["transport_preserves_genuine_von_mangoldt"])
        self.assertEqual(d["mismatch_indices"],())
        self.assertEqual(d["composite_six_residual_prime_log_basis"],{})
        self.assertTrue(d["source_authentic"])
        self.assertFalse(d["all_critical_line_transport_certified"])
        self.assertFalse(d["original_Weil_Gamma_contact_identified"])
        self.assertFalse(d["RH_proved"])

    def test_expected_true_prime_power_two_channel_weights(self):
        N=36
        coeff=(0,)+(tuple(sigma_one(n) for n in range(1,N+1)))
        d=formal_dirichlet_log_derivative(coeff)
        self.assertEqual(d[2],{2:3})
        self.assertEqual(d[4],{2:5})
        self.assertEqual(d[8],{2:9})
        self.assertEqual(d[9],{3:10})
        self.assertEqual(d[25],{5:26})
        for n in (6,10,12,15,18,20,21,30,36):
            self.assertEqual(d[n],{},msg=f"composite source defect n={n}")

    def test_fake_composite_six_is_detected_exactly(self):
        c=eta_eisenstein_prime_transducer(48,True)
        self.assertFalse(c["source_authentic"])
        self.assertFalse(c["transport_preserves_genuine_von_mangoldt"])
        self.assertIn(6,c["mismatch_indices"])
        self.assertEqual(c["composite_six_residual_prime_log_basis"],{2:1,3:1})
        self.assertFalse(c["RH_proved"])

    def test_exact_finite_dirichlet_tail_does_not_become_critical_strip_bound(self):
        self.assertEqual(sigma_one_dirichlet_tail_majorant(4,16),F(1,16))
        self.assertEqual(sigma_one_dirichlet_tail_majorant(5,16),F(1,512))
        self.assertEqual(sigma_one_dirichlet_tail_majorant(6,10),F(1,3000))
        for sigma,N in ((3,100),(4,1),(4,True),(4,1.2),(True,9)):
            with self.assertRaises(EtaTransportError):
                sigma_one_dirichlet_tail_majorant(sigma,N)

    def test_changing_zeta_and_original_eta_gammas_is_type_error(self):
        s=primary_source_interface_status()
        self.assertEqual(s["canonical_Bernoulli_eta_q_exponent"],F(1,24))
        self.assertEqual(s["original_zeta_Weil_half_density"],F(1,2))
        self.assertEqual(s["eta_heat_archimedean"],"Gamma(s)")
        self.assertEqual(s["original_zeta_archimedean"],"pi^(-s/2)*Gamma(s/2)")
        self.assertNotEqual(s["eta_heat_archimedean"],s["original_zeta_archimedean"])
        self.assertTrue(s["eta_modular_transport_is_not_Weil_positivity"])
        self.assertFalse(s["RH_proved"])



class FullModularVsEisensteinSourceFirewall(unittest.TestCase):
    def test_delta_cusp_series_is_not_divisor_sigma1_even_though_dlog_is_E2(self):
        c=modular_discriminant_formal_passport(12)
        self.assertEqual(c["Delta_q_coefficients_through_degree_N"][:7],
                         (0,1,-24,252,-1472,4830,-6048))
        self.assertEqual(c["q_dlog_Delta_coefficients_through_degree_N_minus_one"][:7],
                         (1,-24,-72,-96,-168,-144,-288))
        self.assertTrue(c["E2_comparison_exact"])
        self.assertTrue(c["Delta_is_eta_to_24_power"])
        self.assertTrue(c["cusp_order_exactly_one"])
        self.assertFalse(c["Delta_Ramanujan_tau_coefficients_are_sigma1"])
        self.assertFalse(c["Gamma_of_Delta_L_series_identified_with_Gamma_zeta"])
        self.assertFalse(c["RH_proved"])

    def test_original_zeta_cannot_be_replaced_by_two_shifted_completed_copies(self):
        d=completed_two_critical_track_passport()
        self.assertEqual(d["symmetry_center_real_part"],F(1))
        self.assertEqual(d["conditional_on_RH_two_real_tracks"],(F(1,2),F(3,2)))
        self.assertEqual(d["functional_equation"],"X(2-s)=X(s)")
        self.assertFalse(d["nontrivial_zero_locations_used_as_inputs"])
        self.assertTrue(d["single_track_at_center_not_implied"])
        self.assertTrue(d["source_projection_out_shifted_factor_required"])
        self.assertFalse(d["RH_proved"])

    def test_discriminant_q_cutoff_mutations_fail(self):
        for N in (0,1,2,True,49,3.5):
            with self.assertRaises(EtaTransportError):
                modular_discriminant_formal_passport(N)


class IndependentClassicalNumericHoldouts(unittest.TestCase):
    """Separate independent numerical calibrations, never rigorous proof."""

    def test_eta_S_inversion_and_cusp_are_correct(self):
        import mpmath as mp
        with mp.workdps(75):
            def eta_heat(t,alpha):
                q=mp.exp(-t)
                # at t=pi the omitted n>=128 factors are <1e-170
                return mp.exp(-alpha*t)*mp.fprod(1-q**n for n in range(1,128))
            t=mp.pi
            td=4*mp.pi
            a=mp.mpf(1)/24
            lhs=eta_heat(t,a)
            rhs=mp.sqrt(2*mp.pi/t)*eta_heat(td,a)
            self.assertLess(abs(lhs-rhs),mp.mpf("1e-70"))
            wrong=mp.mpf(1)/22
            wronglhs=eta_heat(t,wrong)
            wrongrhs=mp.sqrt(2*mp.pi/t)*eta_heat(td,wrong)
            self.assertGreater(abs(wronglhs-wrongrhs),mp.mpf("1e-3"))

    def test_selfdual_Lambert_series_exact_modular_value(self):
        """This is a numeric holdout; analytical authority is classical eta S."""
        import mpmath as mp
        with mp.workdps(85):
            lhs=mp.fsum(
                sigma_one(n)*mp.exp(-2*mp.pi*n) for n in range(1,80)
            )
            rhs=mp.mpf(1)/24 - 1/(8*mp.pi)
            self.assertLess(abs(lhs-rhs),mp.mpf("1e-80"))
            self.assertGreater(lhs,0)

    def test_independent_zeta_product_vs_finite_divisor_source_with_proved_tail(self):
        import mpmath as mp
        N=4000
        with mp.workdps(50):
            finite=mp.fsum(mp.mpf(sigma_one(n))/n**5 for n in range(1,N+1))
            infinite=mp.zeta(5)*mp.zeta(4)
            bound=sigma_one_dirichlet_tail_majorant(5,N)
            self.assertLess(abs(infinite-finite),mp.mpf(bound.numerator)/bound.denominator)
            self.assertGreater(infinite-finite,0)


if __name__=="__main__":
    unittest.main()
