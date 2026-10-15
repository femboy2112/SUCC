"""APOLLO finite-window authentic positive-minus-negative Hilbert-Krein factor."""
import unittest
from fractions import Fraction as F
from itertools import product

from observational_succ.one_object_transport import OneObjectError
from observational_succ.apollo_krein_factor import (
    brownian_increment_kernel,triangle_overlap,triangle_increment_kernel,
    prime_hinge_kernel,prime_krein_identity,exact_rational_gram_psd,
    original_suzuki_krein_finite_window,source_feature_contraction_diagnostic,
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


if __name__=="__main__":
    unittest.main()
