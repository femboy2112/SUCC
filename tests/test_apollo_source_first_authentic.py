"""Authenticated true-prime-2 and original real Gamma positive-first recovery."""
import unittest
from fractions import Fraction as F
from observational_succ.apollo_source_first_interference import (
    PrimeInterferenceError,true_prime_two_source_phase_triad,
    gamma_positive_first_Brownian_recovery,source_first_prime_interference,
    authentic_full_negative_feature_transfer_bound)
from observational_succ.apollo_krein_factor import prime_mixed_second_source_coefficients

class OriginalSourcePhase(unittest.TestCase):
    def test_signed_original_prime_jet_has_three_phases(self):
        d=true_prime_two_source_phase_triad()
        self.assertEqual(d["true_prime_power_labels"],(2,))
        self.assertEqual(d["source"],"SHA_PINNED_ORIGINAL_PRIME_TWO_JET")
        self.assertGreater(d["true_log2_bounds"][0],F(1,2))
        self.assertGreater(d["true_half_density_weight_bounds"][0],0)
        self.assertEqual(d["two_bumps_combined_support_measure_at_most"],F(1,16))
        self.assertEqual(d["in_phase_prime_rayleigh"],"-log(2)/sqrt(2)")
        self.assertEqual(d["anti_phase_prime_rayleigh"],"+log(2)/sqrt(2)")
        self.assertEqual(d["quarter_phase_prime_rayleigh"],"0")
        self.assertTrue(d["same_true_prime_jet_all_three_cases"])
        self.assertFalse(d["completed_Weil_negative_witness_inferred"])
        self.assertFalse(d["RH_proved"])
    def test_prime_wavefront_source_contacts_cancel_not_pure_well(self):
        z=prime_mixed_second_source_coefficients(F(3,7))
        self.assertEqual(z["positive_triangle_origin"],F(6,7))
        self.assertEqual(z["negative_brownian_origin"],-F(6,7))
        self.assertEqual(z["combined_origin"],0)
        self.assertEqual(z["combined_plus_logprime_impulse"],-F(3,7))
        self.assertEqual(z["combined_minus_logprime_impulse"],-F(3,7))

class GammaFirstAndBrownianDeterminacy(unittest.TestCase):
    def test_real_gamma_positive_feature_has_no_unpinned_Brownian_mode(self):
        for a,margin in ((F(1,24),F(47,12)),(F(1,2),F(3)),
                         (F(1),F(2)),(F(4),F(1,4))):
            z=gamma_positive_first_Brownian_recovery(a)
            self.assertGreaterEqual(z["Gamma0_L2_relative_lower"],margin)
            self.assertEqual(z["source"],"SHA_PINNED_ORIGINAL_ONE_REAL_GAMMA")
            self.assertTrue(z["Gamma_positive_feature_injective_on_source_window"])
            self.assertTrue(z["Brownian_source_v_uniquely_determined_by_positive_Gamma0"])
            self.assertTrue(z["Brownian_recovery_map_bounded_by_coercivity"])
            self.assertFalse(z["physical_Gamma_first_time_order_proved"])
            self.assertFalse(z["all_positive_to_negative_contraction_proved"])
            self.assertFalse(z["RH_proved"])
    def test_full_original_Krein_negative_is_bounded_graph_of_positive_feature(self):
        for a,labels in ((F(1,12),()),(F(1,4),()),(F(1,2),(2,)),
                         (F(1),(2,3,4,5,7))):
            d=authentic_full_negative_feature_transfer_bound(a)
            self.assertEqual(d["true_active_prime_powers"],labels)
            self.assertTrue(d["negative_feature_determined_by_positive_without_assuming_sign"])
            self.assertTrue(d["unique_bounded_graph_on_minimal_positive_feature_span"])
            self.assertTrue(d["positive_feature_injective_on_compact_Brownian_carrier"])
            self.assertGreater(d["source_positive_to_negative_graph_operator_norm_squared_upper"],1)
            self.assertFalse(d["this_bound_itself_certifies_contraction"])
            self.assertFalse(d["RH_equivalent_all_windows_contraction_proved"])
            self.assertFalse(d["physical_actualization_order_proved"])
            self.assertFalse(d["RH_proved"])

    def test_illegal_timing_or_uncertified_numeric_input_cannot_be_accepted(self):
        for radius in (0,-1,True,2.0,129):
            with self.assertRaises(PrimeInterferenceError):
                gamma_positive_first_Brownian_recovery(radius)
        with self.assertRaises(PrimeInterferenceError):
            source_first_prime_interference(F(1),F(1,2),1,
                                            ((F(-2),F(-1),1,0),))

if __name__=="__main__":
    unittest.main()
