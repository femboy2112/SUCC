"""APOLLO finite-window authentic positive-minus-negative Hilbert-Krein factor."""
import unittest
from fractions import Fraction as F
from itertools import product

from observational_succ.one_object_transport import OneObjectError
from observational_succ.apollo_krein_factor import (
    brownian_increment_kernel,triangle_overlap,triangle_increment_kernel,
    prime_hinge_kernel,prime_krein_identity,exact_rational_gram_psd,
    original_suzuki_krein_finite_window,source_feature_contraction_diagnostic,
    prime_mixed_second_source_coefficients,gamma_mixed_second_source_coefficients,
    neutral_prime_activation_pair,authentic_prime_two_activation_on_old_window,
    authentic_small_window_brownian_coercivity,
    authentic_sharp_small_window_hilbert_factor, _exp_odd_taylor_lower,
    authentic_small_window_completed_weil_coercivity,
    brownian_compact_weak_derivative_certificate,
)


class ExactSourceFreeKreinLaws(unittest.TestCase):
    def test_triangular_and_brownian_prime_identity_all_hostile_positions(self):
        checks=0
        for x,y,b in product((F(-2),F(-3,4),F(0),F(1,4),F(1),F(3)),
                             (F(-5,2),F(-1,3),F(0),F(1,2),F(7,4)),
                             (F(1,7),F(1,2),F(1),F(3,2),F(5))):
            datum=prime_krein_identity(x,y,b)
            self.assertEqual(datum["signed"],
                             datum["positive_triangle"]-datum["negative_brownian"])
            self.assertTrue(datum["identity_exact"])
            self.assertEqual(datum["signed"],prime_hinge_kernel(x,y,b))
            checks+=1
        self.assertEqual(checks,150)

    def test_two_true_hilbert_feature_grans_are_exact_psd(self):
        pts=(F(-2),F(-1,2),F(0),F(1,3),F(3,2))
        for w in (F(1,4),F(1,2),F(1),F(3)):
            for kind in ("triangle","brownian"):
                g=exact_rational_gram_psd(pts,kind,w)
                self.assertTrue(g["all_principal_minors_nonnegative"])
                self.assertEqual(g["strictly_negative_principal_minors"],())
                self.assertFalse(g["RH_proved"])
            for x in pts:
                self.assertEqual(triangle_increment_kernel(x,0,w),0)
                self.assertEqual(brownian_increment_kernel(x,0),0)

    def test_triangular_primitive_fourier_autocorrelation(self):
        for w in (F(1,2),F(1),F(5,3)):
            self.assertEqual(triangle_overlap(0,w),1)
            self.assertEqual(triangle_overlap(w,w),0)
            self.assertEqual(triangle_overlap(w/2,w),F(1,2))
            self.assertEqual(triangle_overlap(-w/2,w),F(1,2))
            self.assertEqual(triangle_overlap(2*w,w),0)

    def test_signs_look_like_signed_sources_not_positive_each_entry(self):
        witness=prime_krein_identity(F(1,2),F(3,2),F(1))
        self.assertLess(witness["signed"],0)
        self.assertGreaterEqual(witness["positive_triangle"],0)
        self.assertGreaterEqual(witness["negative_brownian"],0)
        cross=prime_krein_identity(F(1),F(-2),F(1,2))
        self.assertEqual(cross["negative_brownian"],0)

    def test_fake_domains_critical_rejected(self):
        for b in (F(0),F(-1),True,0.5):
            with self.assertRaises(OneObjectError):
                prime_krein_identity(1,1,b)
        for kind in ("unknown",None,"connes"):
            with self.assertRaises(OneObjectError):
                exact_rational_gram_psd((F(1),),kind)


class AuthenticKreinSourceTests(unittest.TestCase):
    def test_original_gamma_poles_contact_prime_glue(self):
        import mpmath as mp
        for a,x,y,J,expect in (
            (F(1,2),F(1,4),F(1,2),0,(2,)),
            (F(1,2),F(1,4),F(-1,4),3,(2,)),
            (F(1,2),F(1,2),F(1,2),7,(2,)),
            (F(1),F(3,4),F(-1,2),4,(2,3,4,5,7)),
            (F(1),F(1),F(1,4),10,(2,3,4,5,7)),
            (F(1),F(-3,4),F(-1),2,(2,3,4,5,7)),
        ):
            o=original_suzuki_krein_finite_window(x,y,a,J,75)
            self.assertEqual(o["prime_labels"],expect)
            self.assertLess(o["residual_abs"],mp.mpf("1e-58"))
            self.assertTrue(o["gamma_modes_are_positive_Hilbert_features"])
            self.assertTrue(o["triangular_prime_terms_are_positive_Hilbert_features"])
            self.assertTrue(o["brownian_contact_term_is_negative_Hilbert_feature"])
            self.assertFalse(o["source_hilbert_contraction_proved"])
            self.assertFalse(o["RH_proved"])

    def test_algebraic_signed_features_do_not_imply_full_contractivity(self):
        c=source_feature_contraction_diagnostic(
            ((F(1),F(0)),(F(0),F(1))),
            ((F(2),F(0)),(F(0),F(0))),
        )
        self.assertTrue(c["positive_feature_psd"])
        self.assertTrue(c["negative_feature_psd"])
        self.assertFalse(c["combined_signed_psd_on_selected_finite_set"])
        self.assertLess(c["combined_minors"][0],0)
        self.assertFalse(c["full_source_contraction_proved"])

    def test_accurate_zero_and_nonsingular_positive_gram(self):
        c=source_feature_contraction_diagnostic(
            ((F(1),F(0)),(F(0),F(1))),
            ((F(1,2),F(0)),(F(0),F(1,3))),
        )
        self.assertTrue(c["combined_signed_psd_on_selected_finite_set"])
        self.assertFalse(c["full_source_contraction_proved"])

    def test_reject_forged_window_source(self):
        for vals in ((F(1),F(1),F(1,2)),(F(0),F(0),F(0)),
                     (F(1),F(0),F(3)),(True,F(1,2),F(1))):
            with self.assertRaises(OneObjectError):
                original_suzuki_krein_finite_window(*vals,J=4)
        with self.assertRaises(OneObjectError):
            source_feature_contraction_diagnostic(
                ((F(1),F(2)),(F(2),F(1))),
                ((F(1),F(0)),(F(0),F(1))),
            )


class ApolloDistributionalMixedSecondTests(unittest.TestCase):
    def test_authentic_prime_triangle_and_brownian_contacts_cancel_exactly(self):
        for weight in (F(1,100),F(1,3),F(1),F(7,2)):
            d=prime_mixed_second_source_coefficients(weight)
            self.assertEqual(d["positive_triangle_origin"],2*weight)
            self.assertEqual(d["negative_brownian_origin"],-2*weight)
            self.assertEqual(d["combined_origin"],0)
            self.assertEqual(d["combined_plus_logprime_impulse"],-weight)
            self.assertEqual(d["combined_minus_logprime_impulse"],-weight)
            self.assertTrue(d["canonical_contact_cancelled"])
        for bad in (0,-1,True,0.25):
            with self.assertRaises(OneObjectError):
                prime_mixed_second_source_coefficients(bad)

    def test_true_gamma_ou_normalization_derivative_distribution(self):
        for j in (0,1,2,3,7,16,64,127):
            k=gamma_mixed_second_source_coefficients(j)
            d=4*j+1
            self.assertEqual(k["origin_delta_coefficient"],F(4,d))
            self.assertEqual(k["positive_feature_weight"],F(4,d*d))
            self.assertEqual(k["smooth_exponential_coefficient"],-1)
            self.assertEqual(k["alpha"],F(d,2))
            self.assertTrue(k["separate_infinite_origin_series_is_illegal"])
        for bad in (-1,True,513):
            with self.assertRaises(OneObjectError):
                gamma_mixed_second_source_coefficients(bad)


class ApolloPrimeActivationGluing(unittest.TestCase):
    def test_pre_wavefront_source_features_are_exactly_neutral(self):
        sample=(F(-1,4),F(-1,8),F(0),F(1,8),F(1,4))
        for x,y in product(sample,sample):
            src=neutral_prime_activation_pair(x,y,F(3,4))
            self.assertEqual(src["positive_channel"],src["negative_channel"])
            self.assertEqual(src["signed_on_old_window"],0)
            self.assertTrue(src["signed_restriction_compatible"])
            self.assertFalse(src["independent_plus_minus_nesting_certified"])
        d=neutral_prime_activation_pair(F(1,4),F(1,4),F(3,4))
        self.assertEqual(d["positive_channel"],F(1,2))
        self.assertTrue(d["nontrivial_paired_features"])

    def test_actual_primitive_2_source_neutral_birth(self):
        d=authentic_prime_two_activation_on_old_window()
        self.assertEqual(d["source"],"ORIGINAL_PINNED_VON_MANGOLDT_2")
        self.assertTrue(d["Krein_neutral_source_birth"])
        self.assertTrue(d["signed_zero"])
        self.assertEqual(d["unweighted_plus_equal_minus"],F(1,2))
        self.assertGreater(d["prime_two_log_interval"][0],F(1,2))
        self.assertLess(d["prime_two_log_interval"][1],F(1))
        self.assertGreater(d["true_prime_weighted_positive_channel_interval"][0],0)
        self.assertFalse(d["all_a_Hilbert_contraction_proved"])

    def test_invalid_source_birth_boundary_rejected(self):
        for x,y,b in ((F(1,2),F(-1,2),F(1)),(F(1),F(0),F(1,2)),
                      (F(0),F(0),F(0)),(F(1),F(1),True)):
            with self.assertRaises(OneObjectError):
                neutral_prime_activation_pair(x,y,b)


class ApolloFullSmallIntervalPositiveKernel(unittest.TestCase):
    def test_original_source_rational_uniform_brownian_coercivity(self):
        for a in (F(1,24),F(1,32),F(1,64),F(1,500)):
            proof=authentic_small_window_brownian_coercivity(a)
            self.assertEqual(proof["gamma_modes_used"],8)
            self.assertGreater(proof["strict_K_dominates_B_lower"],F(1,10))
            self.assertEqual(proof["uniform_K_dominates_B_for_all_real_a_le_1over24"],F(1,10))
            self.assertTrue(proof["holds_for_all_finite_point_sets_and_complex_coefficients"])
            self.assertTrue(proof["gamma_tail_omitted_positive"])
            self.assertTrue(proof["first_prime_absent"])
            self.assertFalse(proof["all_RH_test_intervals_certified"])
            self.assertFalse(proof["RH_proved"])
        for bad in (0,-1,F(1,12),True,0.01):
            with self.assertRaises(OneObjectError):
                authentic_small_window_brownian_coercivity(bad)

    def test_exact_eight_rung_bound_is_rigorous_without_approximate_eigenvalues(self):
        proof=authentic_small_window_brownian_coercivity(F(1,24))
        S8=sum(F(4,4*j+1) for j in range(8))
        a=F(1,24)
        self.assertEqual(proof["strict_K_dominates_B_lower"],
                         S8-16*a-F(11,2)-a**3/(1-a))
        self.assertLess(proof["original_contact_upper"],F(6))
        self.assertGreater(proof["original_log2_lower"],F(1,12))
        self.assertGreater(proof["strict_K_dominates_B_lower"],F(1,10))

    def test_synthetic_exact_gram_minor_keeps_same_brownian_metric(self):
        pts=(F(-1,24),F(-1,48),F(1,72),F(1,24))
        br=exact_rational_gram_psd(pts,"brownian")
        self.assertTrue(br["all_principal_minors_nonnegative"])
        # A lower bound by B is not a uniform lower bound in coefficient ℓ²;
        # clustering points can make Brownian eigenvalues arbitrarily small.
        self.assertGreater(brownian_increment_kernel(F(1,100),F(1,100)),0)
        self.assertEqual(brownian_increment_kernel(F(1,100),F(-1,100)),0)


class ApolloUniformAuthenticPositiveHilbertFactorTests(unittest.TestCase):
    def test_full_real_interval_contraction_from_original_source(self):
        for a in (F(1,12),F(1,16),F(1,20),F(1,24),F(1,1000)):
            cert=authentic_sharp_small_window_hilbert_factor(a)
            self.assertEqual(cert["a"],a)
            self.assertEqual(cert["real_gamma_rungs_used"],20)
            self.assertEqual(cert["gamma_taylor_order"],9)
            self.assertGreater(cert["exact_positive_coercivity_margin"],F(1,100))
            self.assertTrue(cert["original_sha_pinned_source"])
            self.assertTrue(cert["all_finite_complex_source_gram_positive"])
            self.assertTrue(cert["contractive_Ta_exists_by_independent_coercivity_proof"])
            self.assertTrue(cert["positive_feature_Psi_a_exists_by_completion"])
            self.assertFalse(cert["feature_Psi_a_computed_in_closed_form"])
            self.assertFalse(cert["first_prime_crossed"])
            self.assertFalse(cert["all_a_and_RH_proved"])

    def test_exact_gamma_taylor_lower_is_monotone_and_positive_in_required_range(self):
        from math import factorial
        for j in (0,3,10,19):
            alpha=F(4*j+1,2)
            x=alpha*F(1,12)
            p=_exp_odd_taylor_lower(x)
            self.assertEqual(p,sum((F((-1)**k,factorial(k))*x**k
                                    for k in range(10)),F()))
            self.assertGreater(p,0)
            self.assertGreaterEqual(_exp_odd_taylor_lower(x/2),p)
        for bad in (-1,True,0.15):
            with self.assertRaises(OneObjectError):
                _exp_odd_taylor_lower(bad)
        for bad in (0,F(1,11),True,0.01):
            with self.assertRaises(OneObjectError):
                authentic_sharp_small_window_hilbert_factor(bad)

    def test_two_independently_derived_small_window_source_bounds_consistent(self):
        loose=authentic_small_window_brownian_coercivity(F(1,24))
        sharp=authentic_sharp_small_window_hilbert_factor(F(1,24))
        self.assertGreater(sharp["exact_positive_coercivity_margin"],
                           loose["strict_K_dominates_B_lower"])
        self.assertGreater(sharp["exact_positive_coercivity_margin"],F(1,100))


class ApolloFullOriginalSignedWeilSmallWindowTests(unittest.TestCase):
    def test_global_over_compact_tests_on_true_source_small_intervals(self):
        for a in (F(1,12),F(1,16),F(1,25),F(1,250)):
            o=authentic_small_window_completed_weil_coercivity(a)
            self.assertEqual(o["signed_source"],"AUTHENTIC_COMPLETED_WEIL_ZETA")
            self.assertEqual(o["uniform_original_weil_L2_lower"],F(1,100))
            self.assertTrue(o["holds_for_every_smooth_compact_test_on_window"])
            self.assertEqual(o["actual_prime_activity"],"none_on_this_small_window")
            self.assertFalse(o["all_global_Weil_tests_positive"])
            self.assertFalse(o["RH_proved"])

    def test_independently_exact_brownian_mixed_derivative_norm(self):
        for a,m in product((F(1,12),F(1,20)),(4,5,8)):
            c=brownian_compact_weak_derivative_certificate(a,m)
            self.assertGreater(c["Brownian_mixed_second_energy"],0)
            self.assertEqual(c["Brownian_mixed_second_energy"],
                             c["independent_beta_energy"])
            self.assertTrue(c["distributional_identity_calibrated"])
            self.assertFalse(c["source_Weil_quadratic_evaluated"])
        for a,power in ((0,4),(F(1,10),4),(F(1,12),3),(F(1,12),True)):
            with self.assertRaises(OneObjectError):
                brownian_compact_weak_derivative_certificate(a,power)


if __name__=="__main__":
    unittest.main()
