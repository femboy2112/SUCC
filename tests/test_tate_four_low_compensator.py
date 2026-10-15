"""Actual original signed Suzuki positive rank-four compensation theorem."""
import unittest
from fractions import Fraction as F
from observational_succ.tate_four_low_compensator import (
    source_rank_four_positive_completion,exact_low_high_short_toy,
    FourLowCompensatorError,
)


class RealSourceFourRankPositiveCompletion(unittest.TestCase):
    def test_source_original_G_plus_65over16_P4_is_PSD_all_original_u(self):
        z=source_rank_four_positive_completion()
        self.assertEqual(z["source"],
                         "SHA_PINNED_ORIGINAL_SUZUKI_PLUS_EXPLICIT_4RANK_COMPENSATOR")
        self.assertEqual(z["true_original_active_prime_powers"],(2,))
        self.assertEqual(z["source_rank_four_counterterm"],F(65,16))
        self.assertEqual(z["coarse_source_low_short_negative_bound"],F(649,160))
        self.assertEqual(z["strict_modified_low_L2_gap"],F(1,160))
        self.assertEqual(z["original_low_P4_Legendre_indices"],(1,2,3,4))
        self.assertEqual(z["true_original_infinite_high_positive_K_kappa"],F(1,50))
        self.assertEqual(z["true_original_zero_shift_R0_upper"],F(121,32))
        self.assertEqual(z["true_original_G_L2_operator_norm_upper"],F(11,40))
        self.assertTrue(z["G_plus_counterterm_P4_PSD_proved"])
        self.assertTrue(z["canonical_Hilbert_positive_sqrt_exists_if_PSD"])
        self.assertTrue(z["modified_positive_Hilbert_sqrt_does_NOT_prove_original_G_positive"])
        self.assertTrue(z["source_negative_Morse_index_bound_proved"])
        self.assertEqual(z["source_negative_Morse_index_at_most"],4)
        self.assertEqual(z["source_nullspace_dimension_at_most"],4)
        self.assertFalse(z["original_unmodified_G_positive_proved"])
        self.assertFalse(z["RH_proved"])

    def test_smaller_counterterm_cannot_inherit_unearned_positivity_claim(self):
        tiny=source_rank_four_positive_completion(F(0))
        self.assertFalse(tiny["G_plus_counterterm_P4_PSD_proved"])
        self.assertFalse(tiny["G_plus_counterterm_P4_nonnegative_if_low_gap_zero"])
        self.assertTrue(tiny["source_negative_Morse_index_bound_proved"])
        threshold=source_rank_four_positive_completion(F(649,160))
        self.assertFalse(threshold["G_plus_counterterm_P4_PSD_proved"])
        self.assertTrue(threshold["G_plus_counterterm_P4_nonnegative_if_low_gap_zero"])
        later=source_rank_four_positive_completion(F(33,8))
        self.assertGreater(later["strict_modified_low_L2_gap"],F(1,160))
        self.assertTrue(later["G_plus_counterterm_P4_PSD_proved"])
        self.assertFalse(later["original_unmodified_G_positive_proved"])

    def test_nonexact_counterterm_is_prohibited(self):
        for bad in (True,4.0625):
            with self.assertRaises(FourLowCompensatorError):
                source_rank_four_positive_completion(bad)


class IndependentSignedSchurToy(unittest.TestCase):
    def test_positive_high_alone_does_not_make_full_source_positive(self):
        bad=exact_low_high_short_toy()
        self.assertEqual(bad["original_low_short"],-F(9,32))
        self.assertFalse(bad["original_signed_matrix_PSD"])
        self.assertTrue(bad["compensated_matrix_PSD"])
        self.assertFalse(bad["source_original_zeta_identified"])
        self.assertFalse(bad["RH_proved"])

    def test_high_sign_with_no_coupling_still_needs_low_sign(self):
        neg=exact_low_high_short_toy(A=F(-1),B=0,D=F(2),compensation=0)
        pos=exact_low_high_short_toy(A=F(-1),B=0,D=F(2),compensation=2)
        self.assertFalse(neg["original_signed_matrix_PSD"])
        self.assertFalse(neg["compensated_matrix_PSD"])
        self.assertTrue(pos["compensated_matrix_PSD"])
        self.assertFalse(pos["source_original_zeta_identified"])

    def test_synthetic_wrong_domains_fail(self):
        for args in (
            dict(A=1.5),
            dict(B=True),
            dict(D=0),
            dict(D=-1),
            dict(compensation=3.125),
        ):
            with self.assertRaises(FourLowCompensatorError):
                exact_low_high_short_toy(**args)


if __name__=="__main__":
    unittest.main()
