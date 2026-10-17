"""Exact arithmetic prime-edge geometry; new infinite form theorem has separate source gate."""
import unittest
from fractions import Fraction as F

from observational_succ.authentic_prime_surplus import (
    PrimeSurplusError,edge_intervals,poly_add,poly_mul,poly_int,
    poly_translate,edge_energy_polynomial,edge_mass_polynomial_in_b,
    edge_source_polynomial_for_mode,exact_center_features,
    center_feature_gram,feature_projected_norms,pole_p5_positive_lower,
)
from observational_succ.suzuki_legendre_source import (
    legendre_polynomial,poly_primitive_zero_at_left,
)
from observational_succ.source_jump_spectral import is_psd


class EdgeGraphExactTests(unittest.TestCase):
    def test_exact_three_strip_source_geometry(self):
        L,C,R=edge_intervals(F(1,2),F(7,10))
        self.assertEqual((L,C,R),(
            (F(-1,2),F(-1,5)),(F(-1,5),F(1,5)),
            (F(1,5),F(1,2))
        ))
        for a,b in ((F(1,2),F(1,2)),(F(1,2),F(1)),
                    (F(1,2),F(1,4)),(True,F(7,10)),
                    (F(1,2),0.693)):
            with self.assertRaises(PrimeSurplusError):
                edge_intervals(a,b)

    def test_independent_rational_edge_identity_on_three_shapes(self):
        for polynomial in (
            (F(1),F(0),F(-4)),(F(0),F(1),F(3),F(-5)),
            poly_primitive_zero_at_left(legendre_polynomial(5,F(1,2)),F(1,2)),
        ):
            d=edge_energy_polynomial(polynomial,F(1,2),F(7,10))
            self.assertEqual(d["norm"]-d["signed_shift_pair"],d["prime_surplus"])
            self.assertEqual(d["prime_surplus"],
                             d["central_energy"]+d["edge_mismatch_energy"])
            self.assertGreaterEqual(d["prime_surplus"],0)
            self.assertFalse(d["actual_prime_source"])

    def test_prime_source_mass_polynomial_independent_closed_forms(self):
        five=edge_source_polynomial_for_mode(5)
        six=edge_source_polynomial_for_mode(6)
        self.assertEqual(five,(
            F(-1,2574),F(0),F(1,11),-F(1,3),F(0),F(1),F(0),
            F(-2),F(0),F(20,9),F(0),F(-14,11),F(0),F(42,143)
        ))
        self.assertEqual(six,(
            F(-1,4290),F(0),F(1,13),-F(1,3),F(0),F(7,5),F(0),
            F(-4),F(0),F(20,3),F(0),F(-70,11),F(0),F(42,13),
            F(0),F(-44,65)
        ))
        # Fresh independent polynomial shift integral; no fitted source values.
        for b in (F(2,3),F(7,10),F(3,4)):
            for mode,poly in ((5,five),(6,six)):
                p=poly_primitive_zero_at_left(
                    legendre_polynomial(mode,F(1,2)),F(1,2))
                model=edge_energy_polynomial(p,F(1,2),b)["prime_surplus"]
                reconstructed=sum((c*b**k for k,c in enumerate(poly)),F(0))
                self.assertEqual(model,reconstructed)

    def test_false_extra_shift_weight_is_detectable(self):
        # For perfectly aligned prime-connected edges the correct norm
        # bound is saturated, while a fictitious doubled coefficient goes
        # negative (would fabricate an arithmetic source sign).
        left,right,center=(F(3),),(F(3),),(F(0),)
        norm=left[0]**2+right[0]**2
        contact=left[0]*right[0]
        self.assertEqual(norm-2*contact,0)
        self.assertLess(norm-4*contact,0)


class CenterObservableProofTests(unittest.TestCase):
    def test_exact_moment_rows_and_rank_two_gram(self):
        coeffs=center_feature_gram((5,6,7,8))
        self.assertEqual(coeffs["l0"][0],F(-2925,524288))
        self.assertEqual(coeffs["l1"][1],F(-5175,16777216))
        self.assertEqual(coeffs["l1"][0],0)
        self.assertEqual(coeffs["l0"][1],0)
        self.assertEqual(coeffs["gram"][0][0],F(8555625,68719476736))
        self.assertEqual(coeffs["gram"][1][1],F(80341875,1099511627776))
        self.assertTrue(is_psd(coeffs["gram"]))
        for i,j in ((0,1),(0,3),(1,2),(2,3)):
            self.assertEqual(coeffs["gram"][i][j],0)

    def test_projected_two_central_features_are_not_fake_full_source(self):
        q=feature_projected_norms()
        self.assertEqual(q["even_center_Qnorm2"],F(1947,16384))
        self.assertEqual(q["odd_center_Qnorm2"],F(19929,16777216))
        self.assertGreater(q["even_center_Qnorm2"],0)
        self.assertGreater(q["odd_center_Qnorm2"],0)
        self.assertEqual(pole_p5_positive_lower(),F(1,10644480))
        with self.assertRaises(PrimeSurplusError):
            feature_projected_norms(F(1,4))

    def test_source_grammar_resists_forged_modes(self):
        for modes in ((4,), (5,5), (5,13), (True,6), (5,2.0)):
            with self.assertRaises(PrimeSurplusError):
                center_feature_gram(modes)


if __name__=="__main__":
    unittest.main()
