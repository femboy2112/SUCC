"""All-radius genuine Weil source high positivity and Zeno resource controls."""
import unittest
from fractions import Fraction as F

from observational_succ.tate_suzuki_all_radii import (
    AllRadiiSourceError, coarse_original_prime_polar_budget,
    all_radius_formal_high_certificate, gamma_harmonic_floor,
)
from observational_succ.apollo_derivative_jets import true_third_prime_wavefronts


class SourceWideGammaHighSector(unittest.TestCase):
    def test_every_finite_radius_can_have_an_explicit_finite_high_theorem(self):
        for a in (F(1,24),F(1,2),F(3,4),F(1),F(2),F(3)):
            c=all_radius_formal_high_certificate(a,F(1))
            self.assertEqual(c["source"],"ORIGINAL_ONE_REAL_GAMMA_PRIME_POWER_ZETA")
            self.assertGreater(c["original_Weil_strict_coercivity_lower"],F(1))
            self.assertGreater(
                c["Gamma_harmonic_multiplier_lower"],
                2*(c["prime_source_negative_budget"]+2)
            )
            self.assertEqual(c["low_Fourier_mass_strict_upper"],F(1,12))
            self.assertTrue(c["finite_high_source_positive_for_this_radius"])
            self.assertTrue(c["moment_rank_not_materialized"])
            self.assertFalse(c["finite_test_matrix_claimed_computed"])
            self.assertFalse(c["source_derived_low_Schur_positive"])
            self.assertFalse(c["all_radii_low_schur_verified"])
            self.assertFalse(c["RH_proved"])

    def test_original_real_positive_high_can_have_any_requested_finite_margin(self):
        a=F(1,2)
        c0=all_radius_formal_high_certificate(a,F(0))
        c1=all_radius_formal_high_certificate(a,F(1))
        c10=all_radius_formal_high_certificate(a,F(10))
        self.assertLess(c0["Gamma_index_cutoff_J_power_of_two_exponent"],
                        c1["Gamma_index_cutoff_J_power_of_two_exponent"])
        self.assertLess(c1["Gamma_index_cutoff_J_power_of_two_exponent"],
                        c10["Gamma_index_cutoff_J_power_of_two_exponent"])
        self.assertGreater(c10["original_Weil_strict_coercivity_lower"],F(10))

    def test_source_prime_majorants_do_not_forge_composite_Euler_places(self):
        for a in (F(1,2),F(1),F(3,2),F(2)):
            p=coarse_original_prime_polar_budget(a)
            active=true_third_prime_wavefronts(2*a)
            N=p["integer_prime_majorant_N"]
            self.assertTrue(all(j.n<N for j in active))
            self.assertGreater(
                p["all_source_negative_L2_bound_strict_upper"],F(43,8)
            )
            self.assertTrue(p["composite_indices_act_only_as_numerical_majorant"])
            self.assertEqual(p["primitive_fake_six_source_weight"],0)
            self.assertFalse(p["RH_proved"])
        b=coarse_original_prime_polar_budget(F(1,2))
        self.assertEqual(b["integer_prime_majorant_N"],8)
        self.assertEqual(b["polar_exponential_upper_E"],4)
        self.assertEqual(b["all_source_negative_L2_bound_strict_upper"],
                         F(635,8))

    def test_dyadic_harmonic_gamma_lower_is_exact_rational_and_strict(self):
        for J in (1,2,3,4,8,16,32,64,128):
            x=gamma_harmonic_floor(J)
            self.assertGreater(x["genuine_Gamma_multiplier_exact"],
                               x["analytic_harmonic_strict_lower"])
            self.assertFalse(x["RH_proved"])

    def test_coarse_proof_cost_is_idealhard_not_finite_operator_evaluation(self):
        x=all_radius_formal_high_certificate(F(2),F(1))
        self.assertGreater(x["Gamma_index_cutoff_J_power_of_two_exponent"],1000000)
        self.assertEqual(x["Fourier_Omega_exact_formula"],"8*2^M")
        self.assertEqual(x["moment_rank_exact_formula"],"ceil(32*a*2^M)+1")
        self.assertTrue(x["moment_rank_not_materialized"])
        self.assertFalse(x["finite_test_matrix_claimed_computed"])

    def test_domain_and_source_budget_guards(self):
        for a in (0,-1,True,0.5):
            with self.assertRaises(AllRadiiSourceError):
                coarse_original_prime_polar_budget(a)
        for a,margin in ((0,1),(F(1,2),-1),(F(1,2),True),
                         (F(1,2),0.5),(-1,F(0))):
            with self.assertRaises(AllRadiiSourceError):
                all_radius_formal_high_certificate(a,margin)
        for J in (0,129,True,3.5):
            with self.assertRaises(AllRadiiSourceError):
                gamma_harmonic_floor(J)


if __name__=="__main__":
    unittest.main()
