"""Authentic Weil contact delta0 <-> Suzuki inverse Neumann spectral shift."""
import unittest
from fractions import Fraction as F
from observational_succ import one_object_contact_neumann as c

class ContactNeumannTests(unittest.TestCase):
    def test_true_original_source_K_identity_is_pinned(self):
        s=c.original_source_neumann_gate()
        self.assertEqual(s["radius"],F(1,2))
        self.assertEqual(s["raw_legendre_first_two_K"],
                         ((F(1,30),F()),(F(),F(1,210))))
        self.assertTrue(s["contact_delta0_maps_to_relative_K"])
        self.assertFalse(s["contact_normalization_from_Tate_Connes_glued"])
        self.assertFalse(s["signed_schur_positivity_proved"])

    def test_two_independent_integral_derivations_match_for_mixed_sources(self):
        for a in (F(1,4),F(1,2),F(1)):
            for u in ((1,-1),(1,1,-2),(1,-3,3,-1),(2,-1,-1,0),
                      (1,0,-1,0,0,0)):
                e1=c.neumann_antiderivative_energy(a,u)
                e2=c.signed_absolute_kernel_energy(a,u)
                self.assertEqual(e1,e2)
                self.assertGreater(e1,0)

    def test_proven_exact_contact_changes_weil_norm_not_prime_clocks(self):
        for c0 in (F(-3),F(-1,2),F(),F(1),F(3,2)):
            s=c.contact_shift_certificate(F(1,2),(1,-1),c0)
            self.assertEqual(s["original_mean_zero_energy"],F(1,12))
            self.assertEqual(s["difference_in_signed_Suzuki_form"],c0*F(1,12))
            self.assertEqual(s["difference_in_Weil_test_form"],c0*F(1,12))
            self.assertTrue(s["same_off_identity_Weil_distribution"])
            self.assertEqual(s["original_zeta_contact_authentic"],c0==0)
            self.assertFalse(s["Connes_off_identity_trace_sufficient_to_pin_contact"])
            self.assertFalse(s["rh_proved"])

    def test_contact_shift_rigid_generalized_spectrum_even_when_sign_changes(self):
        G=((F(-1),F()),(F(),F(2)))
        K=((F(1),F()),(F(),F(1,4)))
        for d in (-2,0,F(1,2),2,5):
            data=c.generalized_rayleigh_shift(G,K,(1,0),d)
            self.assertEqual(data["before"],-1)
            self.assertEqual(data["after"],-1+F(d))
            self.assertEqual(data["exact_shift"],d)
            self.assertFalse(data["genuine_completed_zeta_Weil_gram_authentic"])

    def test_second_independent_neumann_quadratic_modes(self):
        for u in ((1,2,-3),(2,0,-1,-1),(1,-1,1,-1)):
            for a in (F(1,4),F(3,4)):
                receipt=c.contact_shift_certificate(a,u,F(7,5))
                self.assertEqual(receipt["difference_in_signed_Suzuki_form"],
                                 receipt["difference_in_Weil_test_form"])
                self.assertGreater(receipt["original_mean_zero_energy"],0)


    def test_wrong_Connes_identity_contact_leaks_into_exactly_two_low_high_modes(self):
        one=c.contact_moment_boundary_channels(F(1))
        self.assertEqual(one["radius"],F(1,2))
        self.assertEqual(one["boundary_neumann_channels"],
                         ((29,31,F(-1,906948)),(30,32,F(-1,999180))))
        self.assertEqual(one["K_cross_rank_if_contact_discrepancy_nonzero"],2)
        self.assertEqual(one["mutated_relative_high_gap_lower"],
                         F(369,10000)+1)
        self.assertFalse(one["original_zeta_normalization_preserved"])
        self.assertFalse(one["finite_moment_Schur_cross_unchanged_under_wrong_contact"])
        self.assertFalse(one["Connes_off_identity_normalizes_contact"])

    def test_origin_normalization_preserves_only_original_source(self):
        genuine=c.contact_moment_boundary_channels(F())
        self.assertEqual(genuine["boundary_neumann_channels"],
                         ((29,31,F()),(30,32,F())))
        self.assertEqual(genuine["K_cross_rank_if_contact_discrepancy_nonzero"],0)
        self.assertTrue(genuine["original_zeta_normalization_preserved"])
        self.assertTrue(genuine["finite_moment_Schur_cross_unchanged_under_wrong_contact"])
        with self.assertRaises(c.ContactTransportError):
            c.contact_moment_boundary_channels(0.0)

    def test_negative_contact_can_destroy_relative_high_gap_certificate(self):
        kap=F(369,10000)
        for offset, positive in ((-kap/2,True),(-kap,False),(-2*kap,False)):
            r=c.contact_moment_boundary_channels(offset)
            self.assertEqual(r["mutated_relative_high_gap_lower"],kap+offset)
            self.assertEqual(r["strict_relative_high_gap_from_this_bound"],positive)
            self.assertFalse(r["rh_proved"])


    def test_normalized_contact_gauge_translates_full_schur_pencil(self):
        # SPD K has a genuine nonzero low/high cross entry. Correct contact
        # must adjust the high block and cross block, not merely the low.
        G=((F(4),F(1),F()),(F(1),F(3),F()),(F(),F(),F(3)))
        K=((F(2),F(1),F()),(F(1),F(2),F()),(F(),F(),F(1)))
        out=c.contact_generalized_schur_pencil(G,K,1,F(1,2),F(1,4))
        self.assertEqual(out["actual_gauge_Schur"],out["parameter_translated_Schur"])
        self.assertTrue(out["cross_channel_source_matters"])
        self.assertNotEqual(out["actual_gauge_Schur"],out["fake_low_only_contact_Schur"])
        self.assertEqual(out["transported_parameter"],F(-1,4))
        self.assertFalse(out["infinite_dimensional_D_inverse_constructed"])
        self.assertFalse(out["authentic_zeta_compressed_G_calculated"])
        self.assertFalse(out["rh_proved"])

    def test_contact_zero_is_identity_even_with_high_low_neumann_cross(self):
        G=((F(4),F(1)),(F(1),F(3)))
        K=((F(2),F(1)),(F(1),F(2)))
        original=c.contact_generalized_schur_pencil(G,K,1,F(0),F(1,4))
        self.assertEqual(original["actual_gauge_Schur"],original["fake_low_only_contact_Schur"])
        self.assertFalse(original["cross_channel_source_matters"])

    def test_contact_pencil_wrong_metric_and_source_types_refused(self):
        for fn in (
            lambda:c.contact_generalized_schur_pencil(((1,0),(0,1)),((1,2),(2,1)),1,1,0),
            lambda:c.contact_generalized_schur_pencil(((1,0),(0,1)),((1,0),(0,1)),2,1,0),
            lambda:c.contact_generalized_schur_pencil(((1,0),(0,1)),((1,0),(0,1)),1,1.0,0),
            lambda:c.contact_generalized_schur_pencil(((1,0),(0,1)),((1,0),(0,1)),1,1,0.0),
        ):
            with self.assertRaises(c.ContactTransportError):fn()

    def test_wrong_source_and_float_labels_rejected(self):
        for fn in (
            lambda:c.contact_shift_certificate(.5,(1,-1),2),
            lambda:c.contact_shift_certificate(F(1,2),(1.0,-1),2),
            lambda:c.contact_shift_certificate(F(1,2),(1,1),2),
            lambda:c.contact_shift_certificate(F(1,2),(1,-1),2.0),
            lambda:c.generalized_rayleigh_shift(((1,),),((0,),),(1,),2),
            lambda:c.generalized_rayleigh_shift(((1,),),((1,),),(1,),0.2),
        ):
            with self.assertRaises((c.ContactTransportError,)):fn()

if __name__=="__main__":
    unittest.main()
