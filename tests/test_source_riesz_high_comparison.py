"""Exact low/high K-Riesz source comparison and hostile Loewner controls."""
import unittest
from fractions import Fraction as F
from observational_succ.source_riesz_high_comparison import (
    SourceComparisonError,finite_K_riesz_profile,
    source_high_riesz_witness,coercivity_slack_no_go,
)
from observational_succ.direct_quotient_schur import exact_psd


class AbstractInfiniteFormLemmaFiniteCalibration(unittest.TestCase):
    def test_exact_rank_one_riesz_projector_and_dual_gain(self):
        K=((F(2),F(1,5)),(F(1,5),F(1)))
        r=finite_K_riesz_profile(K,(F(1),F(0)),F(1,50),F(1,40))
        self.assertTrue(r['finite_comparison_verified'])
        self.assertFalse(r['infinite_original_source_verified'])
        self.assertTrue(exact_psd(r['full_scalar_minus_comparator']))
        self.assertEqual(r['rank_one_coefficient'],F(1,200))
        self.assertEqual(r['dual_residual_gain_multiplier'],F(10))
        self.assertEqual(r['Kzz'],F(2))

    def test_missing_positivity_and_source_coercivity_are_refused(self):
        for K,z,k0,ks in (
            (((F(1),F(2)),(F(2),F(1))),(1,0),F(1,50),F(1,40)),
            (((F(1),),),(0,),F(1,50),F(1,40)),
            (((F(1),),),(1,),F(1,20),F(1,40)),
        ):
            with self.assertRaises(SourceComparisonError):
                finite_K_riesz_profile(K,z,k0,ks)

    def test_positive_finite_compression_is_not_infinite_source_gain(self):
        g=coercivity_slack_no_go()
        self.assertTrue(g['original_residual_PSD'])
        self.assertTrue(g['positive_finite_direction'])
        self.assertFalse(g['false_extra_rank_one_PSD'])


class AuthenticHighSectorCoercivity(unittest.TestCase):
    def test_genuine_odd_high_source_slack_and_positive_riesz(self):
        r=source_high_riesz_witness('odd',(5,7),(F(1),F(0)))
        self.assertEqual(r['source_sha'],
                         '0cc8510b71d178fc79e8d410a86d8b6014cf9178')
        self.assertEqual(r['genuine_prime_power_labels'],(2,))
        self.assertGreater(r['delta'],0)
        self.assertFalse(r['strict_gain_over_full_kappa_source_scalar'])
        self.assertTrue(r['infinite_form_valid_given_inherited_source_theorem'])
        self.assertFalse(r['RH_proved'])


if __name__=='__main__':unittest.main()
