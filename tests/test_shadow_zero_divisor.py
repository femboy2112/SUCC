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
