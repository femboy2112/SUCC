"""Exact controls for the local Connes scaling/half-density bridge."""
import unittest
from fractions import Fraction as Q

from observational_succ.connes_oriented_scaling import (
    ConnesBridgeError, ContactSingularity, RationalScale, local_fixed_point,
    orientation_square_check, diagonal_rational_product, affine_word_fixed_point,
    idelic_place_vs_diagonal, succ_does_not_descend, prime_jet_half_density,
)
from observational_succ.affine_pontryagin_transfer import AffineSourceWord


class ConnesLocalOrientedTrace(unittest.TestCase):
    def test_unit_and_nonunit_scalings_off_identity(self):
        cases = ((Q(4), 3, Q(3)), (Q(3), 2, Q(2)),
                 (Q(1, 2), 2, Q(1, 2)), (Q(2), 2, Q(1)),
                 (Q(-1), 2, Q(2)), (Q(5, 3), 3, Q(1, 3)))
        for u, p, expected in cases:
            with self.subTest(u=u, p=p):
                got = local_fixed_point(RationalScale(u), p, 4)
                self.assertTrue(got.stabilized)
                self.assertEqual(got.off_identity_coefficient, expected)
                self.assertEqual(got.finite_delta_coefficient, expected)

    def test_independent_brute_congruence_oracle(self):
        for p in (2, 3, 5, 7):
            for u in (Q(4), Q(3, 2), Q(1, 5), Q(-5, 3), Q(17, 16)):
                if u == 1:
                    continue
                for depth in (1, 2, 3):
                    receipt = local_fixed_point(RationalScale(u), p, depth)
                    n = p**depth
                    brute = sum(((u.numerator - u.denominator)*z) % n == 0 for z in range(n))
                    self.assertEqual(receipt.residue_fixed_points, brute)
                    self.assertEqual(receipt.finite_delta_coefficient, receipt.chart_volume*brute)
                    if receipt.stabilized:
                        self.assertEqual(receipt.finite_delta_coefficient, receipt.off_identity_coefficient)

    def test_insufficient_depth_does_not_prove_the_limit(self):
        r = local_fixed_point(RationalScale(Q(1+3**5)), 3, 2)
        self.assertFalse(r.stabilized)
        self.assertEqual(r.finite_delta_coefficient, Q(9))
        self.assertEqual(r.off_identity_coefficient, Q(243))
        self.assertTrue(local_fixed_point(RationalScale(Q(1+3**5)), 3, 5).stabilized)

    def test_half_density_orientation_invariance(self):
        for u in (Q(4), Q(1, 4), Q(-1, 2), Q(3, 7), Q(6), Q(19, 16)):
            for p in (2, 3, 5, 7):
                x = orientation_square_check(RationalScale(u), p)
                self.assertEqual(x["symmetric_squared"],
                                 local_fixed_point(RationalScale(1/u), p, 4).half_density_coefficient_squared)
                self.assertFalse(x["positive_type_established"])
        self.assertNotEqual(local_fixed_point(RationalScale(Q(1, 3)), 3, 4).off_identity_coefficient,
                            local_fixed_point(RationalScale(Q(3)), 3, 4).off_identity_coefficient)

    def test_diagonal_rational_product_formula(self):
        for a, b in ((4, 1), (1, 4), (-3, 2), (2, 3), (6, 35),
                     (25, 12), (17, 19), (-1, 1), (1, 999)):
            x = diagonal_rational_product(RationalScale(Q(a, b)))
            self.assertEqual(x["finite_half_density_squared_product"]*x["arch_half_density_squared"], 1)
            self.assertEqual(x["finite_plain_product"]*x["arch_plain_factor"], 1)
            self.assertFalse(x["this_is_a_global_trace_formula"])

    def test_negative_contact_control_survives_orientation_flip(self):
        # u=4 at p=3 gives C=3 off identity. Artificial c=1 contact
        # gives indefinite [[1,3],[3,1]], eigenvalues 4,-2.
        x = orientation_square_check(RationalScale(Q(4)), 3)
        self.assertEqual(x["symmetric_squared"], Q(9))
        C, c = Q(3), Q(1)
        self.assertEqual((c+C, c-C), (4,-2))
        self.assertLess(c*c-C*C, 0)  # NOT a zeta/Connes contact claim

    def test_source_words_and_affine_fixed_points(self):
        word = AffineSourceWord((("S",1),("V",3)))
        x = affine_word_fixed_point(word)
        self.assertEqual(x["normal_form"], (3,3))
        self.assertEqual(x["fixed_point"], Q(-3,2))
        self.assertEqual(local_fixed_point(x["local_scale"],2,4).off_identity_coefficient, Q(2))
        self.assertEqual(affine_word_fixed_point(AffineSourceWord((("S",1),)))["kind"],"no_fixed_point")
        self.assertEqual(affine_word_fixed_point(AffineSourceWord(()))["kind"],"identity_contact")
        self.assertFalse(succ_does_not_descend()["S_action_descends_to_Connes_X"])

    def test_existing_repo_idele_class_interface(self):
        for p in (2,3,7):
            x = idelic_place_vs_diagonal(p,source_id="Q-standard-Tate",epoch=2)
            self.assertEqual(x["local_one_place_norm"],Q(1,p))
            self.assertEqual(x["diagonal_rational_norm"],1)
            self.assertFalse(x["same_idele_class"])

    def test_prime_jet_half_density_and_missing_trace(self):
        for p in (2,3,5,7):
            for k in (1,2,3,5):
                x = prime_jet_half_density(p,k)
                self.assertEqual(x["half_density_coefficient_squared"],Q(1,p**k))
                self.assertEqual(x["local_fixed_point_scalar"],1)
                self.assertFalse(x["full_Connes_trace_and_sign_verified"])
        with self.assertRaises(ConnesBridgeError):
            prime_jet_half_density(6,1)

    def test_fake_place_wrong_depth_contact_and_source_mutants(self):
        for u in (True,1.25,Q(0)):
            with self.assertRaises(ConnesBridgeError): RationalScale(u)
        for p in (0,1,4,6,True,2.5):
            with self.assertRaises(ConnesBridgeError):
                local_fixed_point(RationalScale(Q(5)),p,3)
        for d in (0,-1,True,2.5,33):
            with self.assertRaises(ConnesBridgeError):
                local_fixed_point(RationalScale(Q(5)),2,d)
        for bad in ("",None,True):
            with self.assertRaises(ConnesBridgeError):
                RationalScale(Q(2),source_id=bad)
        with self.assertRaises(ConnesBridgeError):
            RationalScale(Q(2),epoch=True)
        with self.assertRaises(ConnesBridgeError):
            affine_word_fixed_point(None)
        with self.assertRaises(ContactSingularity):
            local_fixed_point(RationalScale(Q(1)),2,3)
        with self.assertRaises(ContactSingularity):
            diagonal_rational_product(RationalScale(Q(1)))


if __name__=="__main__":
    unittest.main()
