"""The zero-divisor source-invariance vs global conditioning no-go."""
import unittest
from fractions import Fraction as Q
from observational_succ.shadow_source_inference import ShadowSourceError
from observational_succ.shadow_zero_divisor import (
    distinct_prime_scale_shadows,offcritical_vs_line_shadow,
    two_prime_shadow_conditioning_obstruction,normalized_gaussian_scale_pair)

class ZeroDivisorShadowTests(unittest.TestCase):
    def test_distinct_prime_scale_auxiliary_zeros_are_disjoint(self):
        for p,q in ((2,3),(3,5),(5,13)):
            r=distinct_prime_scale_shadows(p,q)
            self.assertTrue(r.certificate()['does_not_input_unknown_zeta_zero_positions'])
            self.assertIn('min(ord(F*C1)',r.certificate()['divisor_rule'])
            self.assertFalse(r.certificate()['RH_or_Weil_positivity_proved'])

    def test_fake_prime_and_duplicate_source_rejected(self):
        for p,q in ((4,3),(6,5),(2,2),(1,7)):
            with self.assertRaises(ShadowSourceError):
                distinct_prime_scale_shadows(p,q)
        with self.assertRaises(ShadowSourceError):
            offcritical_vs_line_shadow(Q(10,11),6)

    def test_offcritical_auxiliary_zeros_disjoint_from_line_zeros(self):
        self.assertIn('!=1/2',offcritical_vs_line_shadow(Q(10,11)).disjoint_reason)
        for e in (Q(4,5),Q(1),Q(1,2)):
            with self.assertRaises(ShadowSourceError):
                offcritical_vs_line_shadow(e)

    def test_two_coprime_shadows_still_not_uniformly_invertible(self):
        r=two_prime_shadow_conditioning_obstruction(2,3)
        self.assertTrue(r['exact_auxiliary_zero_sets_disjoint'])
        self.assertEqual(r['infimum_of_sum_of_absolute_multipliers_on_critical_line'],0)
        self.assertFalse(r['global_uniformly_bounded_bezout_decoder_exists'])
        self.assertFalse(r['unknown_zeta_zero_positions_used'])

    def test_normalized_scale_pair_weights_exact(self):
        self.assertEqual(normalized_gaussian_scale_pair(Q(2)),(Q(1,3),Q(2,3)))
        self.assertEqual(normalized_gaussian_scale_pair(Q(3)),(Q(1,4),Q(3,4)))

if __name__=='__main__':unittest.main()

class AnalyticShadowGluingConstructionTests(unittest.TestCase):
    def test_two_independent_test_shadows_construct_global_source(self):
        from observational_succ.shadow_zero_divisor import construct_global_polynomial_from_shadows
        # F=z^2+1, C1=z-1, C2=z+1. F is NOT given to solver.
        r=construct_global_polynomial_from_shadows((-1,1),(1,1),(-1,1,-1,1),(1,1,1,1))
        # For C1*F: (z-1)(z²+1)=-1+z-z²+z³.
        self.assertEqual(r['status'],'GLOBAL_SOURCE_CONSTRUCTED')
        self.assertEqual(r['global_polynomial'],(1,0,1))
        self.assertFalse(r['global_factor_was_given_as_input'])

    def test_bad_cross_observer_report_refuses_global_source(self):
        from observational_succ.shadow_zero_divisor import construct_global_polynomial_from_shadows
        r=construct_global_polynomial_from_shadows((-1,1),(1,1),(-1,1,-1,1),(1,1,1,2))
        self.assertEqual(r['status'],'INCOMPATIBLE_SOURCE_SHADOWS')
        self.assertTrue(any(r['commuting_square_defect']))

    def test_coprimality_is_not_assumed_from_identical_report_shapes(self):
        from observational_succ.shadow_zero_divisor import construct_global_polynomial_from_shadows
        r=construct_global_polynomial_from_shadows((-1,1),(-1,1),(-1,1,-1,1),(-1,1,-1,1))
        self.assertEqual(r['status'],'NONCOPRIME_UNCERTIFIED')
        self.assertEqual(r['common_multiplier'],(-1,1))

    def test_fake_nonrational_input_and_zero_multiplier(self):
        from observational_succ.shadow_zero_divisor import construct_global_polynomial_from_shadows
        with self.assertRaises(ShadowSourceError):
            construct_global_polynomial_from_shadows((0,),(1,1),(1,),(1,))
        with self.assertRaises(ShadowSourceError):
            construct_global_polynomial_from_shadows((0.5,),(1,1),(1,),(1,))

if __name__=='__main__':unittest.main()

class FinitePrimeFamilyInstabilityTests(unittest.TestCase):
    def test_any_finite_prime_list_lacks_full_height_lower_frame_bound(self):
        from observational_succ.shadow_zero_divisor import finite_prime_shadow_conditioning_obstruction
        for ps in ((2,3),(2,3,5),(3,5,13,17,19),(2,3,5,7,11,13,17)):
            r=finite_prime_shadow_conditioning_obstruction(ps)
            self.assertEqual(r['infimum_joint_absolute_multiplier_amplitude'],0)
            self.assertFalse(r['height_uniform_bounded_decoder_exists'])
            self.assertTrue(r['multipliers_pairwise_no_exact_common_zero'])
            self.assertTrue(r['all_unknown_zeta_zeros_avoided'])

    def test_finite_prime_family_source_signature_mutants(self):
        from observational_succ.shadow_zero_divisor import finite_prime_shadow_conditioning_obstruction
        for ps in ((2,2),(2,4),(2,6,5),(2,1),(),(3,)):
            with self.assertRaises(ShadowSourceError):
                finite_prime_shadow_conditioning_obstruction(ps)
