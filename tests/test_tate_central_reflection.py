"""Hostile exact arithmetic and true-source controls for Tate 1-s prime reflection."""
import unittest
from fractions import Fraction as F

from observational_succ.tate_central_reflection import (
    TateReflectionGateError, reflected_local_prime_central_jet,
    original_finite_prime_reflection_slope, real_reflection_diodes,
    central_Gamma_Brownian_contact, actual_center_high_prime_power_tail,
    high_jet_reflection_residual_contract,
    finite_prime_reflection_counterterm_tape,
    reflected_center_jet_offline_mutant, theta_selfdual_reflection_gauge,
)
from observational_succ.source_weil_hierarchy import (
    contact_iv, log_iv, sqrt_inverse,
)
from observational_succ.tate_local_contract import (
    unramified_ball_pair, chi_mod3,
)


class OriginalLocalTateReflection(unittest.TestCase):
    def test_original_zeta_local_ratio_at_two_and_selfdual_reflection(self):
        for p in (2,3,5,7,11,13,17):
            local=reflected_local_prime_central_jet(p)
            parent=unramified_ball_pair(p,0,2,1)
            self.assertEqual(local["local_Tate_forward_over_reflected_at_s_two"],
                             parent.forward_over_dual)
            self.assertEqual(local["opposite_common_local_gamma_at_s_two"],
                             parent.inverse_tate_gamma)
            self.assertEqual(local["local_Tate_forward_over_reflected_at_center"],1)
            self.assertLess(local["local_center_logarithmic_slope_interval"][1],0)
            self.assertTrue(local["on_critical_line_unramified_local_ratio_unit_modulus"])
            self.assertTrue(local["center_first_jet_detects_omega_parity"])
            self.assertFalse(local["valid_global_gamma_conductor_epsilon_completion_constructed"])
            self.assertFalse(local["RH_proved"])

    def test_actual_odd_chi3_unramified_p2_phase_reverses_slope(self):
        self.assertEqual(chi_mod3(2),-1)
        z=reflected_local_prime_central_jet(2,"zeta")
        c=reflected_local_prime_central_jet(2,"chi_minus_3")
        self.assertLess(z["local_center_logarithmic_slope_interval"][1],0)
        self.assertGreater(c["local_center_logarithmic_slope_interval"][0],0)
        self.assertEqual(c["omega"],-1)
        self.assertEqual(c["local_Tate_forward_over_reflected_at_s_two"],
                         unramified_ball_pair(2,0,2,-1).forward_over_dual)
        self.assertEqual(reflected_local_prime_central_jet(
            7,"chi_minus_3")["omega"],1)
        with self.assertRaises(TateReflectionGateError):
            reflected_local_prime_central_jet(3,"chi_minus_3")

    def test_fake_local_prime_wrong_profile_and_float_hard_fail(self):
        for p,prof in ((6,"zeta"),(1,"zeta"),(True,"zeta"),
                       (2.0,"zeta"),(2,"fake-untwisted-conductor"),
                       (3,"chi_minus_3")):
            with self.assertRaises(TateReflectionGateError):
                reflected_local_prime_central_jet(p,prof)


class OriginalGlobalGammaCentralContact(unittest.TestCase):
    def test_source_Archimedean_contact_is_exact_center_reflection_jet(self):
        c=central_Gamma_Brownian_contact()
        exact=contact_iv()
        self.assertEqual(c["source_contact_C_infinity_interval"],(exact.lo,exact.hi))
        self.assertEqual(c["zeta_log_derivative_center_interval"],
                         (exact.lo/2,exact.hi/2))
        self.assertEqual(c["Gamma_R_reflection_ratio_log_slope_interval"],
                         (-exact.hi,-exact.lo))
        self.assertEqual(c["analytic_global_finite_reflection_log_slope_interval"],
                         (exact.lo,exact.hi))
        self.assertEqual(c["completed_Lambda_central_log_derivative"],0)
        self.assertTrue(c["zeta_half_nonzero_by_positive_alternating_eta"])
        self.assertTrue(c["source_contact_equals_twice_analytic_zeta_log_derivative"])
        self.assertFalse(c["completed_RH_positive_Weil_form_proved"])
        self.assertFalse(c["RH_proved"])

    def test_finite_local_center_probe_is_blind_but_slope_diverges(self):
        previous=None
        for P in (2,3,5,11,19,37):
            z=original_finite_prime_reflection_slope(P)
            self.assertEqual(z["finite_Tate_ratio_exact_value_at_center"],1)
            self.assertLess(z["finite_logarithmic_slope_interval"][1],0)
            self.assertTrue(z["all_prime_raw_center_slope_diverges_to_negative_infinity"])
            self.assertFalse(z["finite_enumeration_alone_proves_divergence"])
            if previous is not None:
                self.assertLess(z["finite_logarithmic_slope_interval"][1],previous)
            previous=z["finite_logarithmic_slope_interval"][0]
        globe=central_Gamma_Brownian_contact()
        self.assertGreater(globe["analytic_global_finite_reflection_log_slope_interval"][0],0)

    def test_real_reflection_diodes_not_a_functional_equation_from_raw_primes(self):
        for x,relation,limit in (
            (F(1,4),">","+infinity"),
            (F(2,5),">","+infinity"),
            (F(1,2),"=","1"),
            (F(3,5),"<","0"),
            (F(3,4),"<","0"),
        ):
            z=real_reflection_diodes(x)
            self.assertEqual(z["each_finite_p_factor_relation_to_one"],relation)
            self.assertEqual(z["ordinary_all_prime_product_extended_limit"],limit)
            self.assertTrue(z["raw_prime_product_and_Gamma_R_do_NOT_give_Global_Tate_continuation"])
            self.assertFalse(z["RH_proved"])
        for s in (F(0),F(1),F(-1),True,0.6):
            with self.assertRaises(TateReflectionGateError):
                real_reflection_diodes(s)


class HalfDensityPrimeJets(unittest.TestCase):
    def test_local_first_derivative_expands_into_exact_source_prime_powers(self):
        z=finite_prime_reflection_counterterm_tape((2,3),order=4)
        self.assertEqual(z["source_coefficients_n_parent_and_exact_1overk"],(
            (2,2,F(1)),(4,2,F(1,2)),(8,2,F(1,3)),(16,2,F(1,4)),
            (3,3,F(1)),(9,3,F(1,2)),(27,3,F(1,3)),(81,3,F(1,4)),
        ))
        self.assertFalse(z["primitive_composite_six_in_tape"])
        self.assertTrue(z["center_first_derivative_k_cancels_denominator"])
        self.assertEqual(z["true_source_half_density_weight_formula"],
                         "Lambda(p^k)/sqrt(p^k)=log(p)/p^(k/2)")
        self.assertFalse(z["all_prime_sum_of_low_jet_renormalized"])
        self.assertFalse(z["RH_proved"])

    def test_genuine_high_k_ge_three_is_absolute_convergent_not_low_renormalized(self):
        z=actual_center_high_prime_power_tail(29)
        self.assertEqual(z["source"],"SHA_PINNED_TRUE_VON_MANGOLD_HALF_DENSITY")
        self.assertEqual(z["prime_labels"],(2,3,5,7,11,13,17,19,23,29))
        self.assertLess(F(0),z["k_at_least_three_positive_source_partial_interval"][0])
        self.assertLess(z["reflection_slope_partial_high_jet_interval"][1],0)
        self.assertTrue(z["k_at_least_three_all_prime_source_absolutely_convergent"])
        self.assertTrue(z["k_one_and_k_two_source_prime_sums_both_diverge"])
        self.assertFalse(z["low_k_one_two_renormalized_source_sign_established"])

    def test_exact_strip_renormalization_tail_is_source_honest(self):
        for P in (16,32,64,256):
            for N in (7,8,11):
                z=high_jet_reflection_residual_contract(P,N)
                self.assertEqual(z["complex_log_residual_tail_absolute_upper"],
                                 F(1,2*P))
                self.assertEqual(z["first_residual_jet_order"],N+1)
                self.assertEqual(z["real_strip_closed"],(F(1,4),F(3,4)))
                self.assertTrue(z["valid_for_every_imaginary_part"])
                self.assertTrue(z["critical_line_residual_unit_modulus"])
                self.assertTrue(z["residual_holomorphic_nonzereo_and_normal_convergence"])
                self.assertFalse(z["raw_global_Euler_product_convergence_claimed"])
                self.assertFalse(z["global_completed_Weil_positivity_proved"])
                self.assertFalse(z["RH_proved"])
        for P,N in ((15,7),(16,6),(True,7),(16,7.0),(998,7)):
            with self.assertRaises(TateReflectionGateError):
                high_jet_reflection_residual_contract(P,N)

    def test_jets_do_not_admit_fake_composite_or_repeated_places(self):
        for primes in ((2,6),(3,2),(2,2),(True,3),(),(2.0,3)):
            with self.assertRaises(TateReflectionGateError):
                finite_prime_reflection_counterterm_tape(primes,2)


class CanonicalRealThetaReflectionGauge(unittest.TestCase):
    def test_poisson_forces_quarter_density_in_log_heat_source(self):
        canonical=theta_selfdual_reflection_gauge()
        self.assertEqual(canonical["source"],"ORIGINAL_ONE_REAL_GAUSSIAN_THETA_POISSON")
        self.assertEqual(canonical["unique_exact_theta_selfdual_exponent"],F(1,4))
        self.assertEqual(canonical["log_reflection_ratio_slope_in_heat_log_coordinate"],0)
        self.assertTrue(canonical["full_theta_log_kernel_even_for_all_x"])
        self.assertFalse(canonical["derivative_detects_wrong_normalization"])
        self.assertTrue(canonical["real_Gamma_R_and_polar_completion_still_required"])
        self.assertFalse(canonical["RH_proved"])
        for w,slope in ((F(0),F(1,2)),(F(1,8),F(1,4)),
                        (F(1,2),F(-1,2))):
            x=theta_selfdual_reflection_gauge(w)
            self.assertTrue(x["value_only_at_reflection_fixed_heat_time_t_one_blind"])
            self.assertEqual(x["log_reflection_ratio_slope_in_heat_log_coordinate"],slope)
            self.assertTrue(x["derivative_detects_wrong_normalization"])
            self.assertFalse(x["full_theta_log_kernel_even_for_all_x"])
        with self.assertRaises(TateReflectionGateError):
            theta_selfdual_reflection_gauge(0.25)


class ReflectionWithoutArithmeticIsNotRH(unittest.TestCase):
    def test_mutant_matches_reflection_center_jets_and_pole_residues_but_offline_zeros(self):
        for m in (1,2,3,7):
            z=reflected_center_jet_offline_mutant(m)
            self.assertEqual(z["values_at_zero_center_one"],(F(1),F(1),F(1)))
            self.assertEqual(z["off_critical_line_zeros"],(F(1,4),F(3,4)))
            self.assertEqual(z["all_center_derivatives_through_order"],2*m-1)
            self.assertEqual(z["first_changed_center_derivative_order"],2*m)
            self.assertEqual(z["first_changed_center_derivative"],
                             -F(4**(2*m+1)*__import__("math").factorial(2*m),3))
            self.assertTrue(z["preserves_completed_xi_reflection_symmetry"])
            self.assertTrue(z["preserves_original_completed_pole_residues"])
            self.assertFalse(z["preserves_original_prime_Euler_multiplicativity"])
            self.assertTrue(z["center_jet_or_completion_alone_does_NOT_force_RH"])
            self.assertFalse(z["RH_proved"])
        for m in (0,True,17,1.2):
            with self.assertRaises(TateReflectionGateError):
                reflected_center_jet_offline_mutant(m)


class IndependentNumericalCalibrationOnly(unittest.TestCase):
    """Numerical holdouts cannot be promoted to mathematical proof."""

    def test_zeta_central_contact_and_local_p_center_derivatives(self):
        import mpmath as mp
        with mp.workdps(65):
            c=-mp.digamma(mp.mpf(1)/4)+mp.log(mp.pi)
            r=mp.diff(mp.zeta,mp.mpf(1)/2)/mp.zeta(mp.mpf(1)/2)
            self.assertLess(abs(2*r-c),mp.mpf("1e-54"))
            for p in (2,3,5):
                x=mp.mpf(p)
                deriv=-2*mp.log(x)/(mp.sqrt(x)-1)
                q=reflected_local_prime_central_jet(p)
                lo,hi=q["local_center_logarithmic_slope_interval"]
                self.assertLess(mp.mpf(lo.numerator)/lo.denominator,deriv)
                self.assertLess(deriv,mp.mpf(hi.numerator)/hi.denominator)

    def test_true_local_and_arch_unit_modulus_on_critical_line(self):
        import mpmath as mp
        with mp.workdps(60):
            s=mp.mpf(1)/2+mp.mpc(0,mp.mpf(7)/5)
            A=lambda z:mp.power(mp.pi,-z/2)*mp.gamma(z/2)
            self.assertLess(abs(abs(A(s)/A(1-s))-1),mp.mpf("1e-48"))
            for p in (2,3,5,7):
                p=mp.mpf(p)
                ratio=(1-mp.power(p,s-1))/(1-mp.power(p,-s))
                self.assertLess(abs(abs(ratio)-1),mp.mpf("1e-48"))

    def test_high_jet_residual_finite_prime_tail_agrees_with_rational_enclosure(self):
        import mpmath as mp
        with mp.workdps(55):
            s=mp.mpf(1)/2+mp.mpc(0,mp.mpf(2))
            P=64
            # Diagnostic only: an incomplete 2500-prime tail is NOT the
            # infinite upper bound, which is analytic in the paper.
            high=mp.mpc(0)
            for p in range(P+1,1000):
                if all(p%d for d in range(2,__import__('math').isqrt(p)+1)):
                    z=mp.power(p,-s)
                    w=mp.power(p,-(1-s))
                    high+=mp.fsum((z**k-w**k)/k for k in range(8,25))
            self.assertLess(abs(high),mp.mpf(1)/(2*P))


if __name__=="__main__":
    unittest.main()
