"""Proof checks for exact all-directions interval source Schur cone sign oracle."""
import unittest
from fractions import Fraction as F

from observational_succ.exact_source_two_dim_cone import (
    ExactConeError,exact_nonnegative_two_dimensional_source_cone
)
from observational_succ.source_four_phase_schur import CertifiedFourPrimeFullPhaseSchurTrial


class RationalConeDecision(unittest.TestCase):
    def test_empty_feature_matrix_Sylvester_sign(self):
        for A,ans in (
            (((1,0),(0,1)),True),
            (((0,0),(0,1)),True),
            (((-1,0),(0,1)),False),
            (((1,2),(2,1)),False)
        ):
            self.assertEqual(exact_nonnegative_two_dimensional_source_cone(
                A,())["robust_lower_nonnegative_for_ALL_real_directions"],ans)

    def test_exact_source_rank_one_repairs_negative_original_axis(self):
        A=((F(-1,2),0),(0,F(1)))
        c=exact_nonnegative_two_dimensional_source_cone(A,((F(1),F(0),F(0),F(0),F(1)),))
        self.assertTrue(c["robust_lower_nonnegative_for_ALL_real_directions"])
        self.assertTrue(c["tested_unbounded_tails"])
        self.assertTrue(c["tested_vertical_direction"])

    def test_interval_robust_cone_stronger_than_fixed_Young_Loewner(self):
        A=((F(0),0),(0,F(1,1000)))
        feature=(F(1),F(0),F(1,10),F(1,10),F(1))
        c=exact_nonnegative_two_dimensional_source_cone(A,(feature,))
        self.assertTrue(c["robust_lower_nonnegative_for_ALL_real_directions"])
        # Fixed eta=1/8 Young lower has a strictly negative second diagonal:
        # A22-7*e2*(e1+e2) < 0. No unsupported PSD matrix max/clamp.
        self.assertLess(A[1][1]-7*F(1,10)*F(1,5),0)

    def test_uncertainty_may_leave_computed_bound_negative(self):
        A=((F(-1,4),0),(0,F(1,1000)))
        feature=(F(1),F(0),F(1,10),F(1,10),F(1))
        result=exact_nonnegative_two_dimensional_source_cone(A,(feature,))
        self.assertFalse(result["robust_lower_nonnegative_for_ALL_real_directions"])
        self.assertIsNotNone(result["first_failure_of_LOWER_only"])

    def test_two_independent_source_features_and_cross_terms(self):
        A=((F(1),F(-2)),(F(-2),F(1)))
        g=((1,1,0,0,1),)
        self.assertTrue(exact_nonnegative_two_dimensional_source_cone(
            A,g)["robust_lower_nonnegative_for_ALL_real_directions"])
        self.assertFalse(exact_nonnegative_two_dimensional_source_cone(
            A,())["robust_lower_nonnegative_for_ALL_real_directions"])

    def test_reject_forged_input(self):
        cases=[
            (((1,2),(3,4)),()), # non-Hermitian
            (((1,0),(0,1)),((1,2,-1,0,1),)),
            (((1,0),(0,1)),((1,2,0,0,-1),)),
            (((1,0),(0,1)),((1,2,0,0,0.5),)),
            (((1,0),(0,1)),((True,2,0,0,1),)),
        ]
        for A,features in cases:
            with self.assertRaises(ExactConeError):
                exact_nonnegative_two_dimensional_source_cone(A,features)

    def test_genuine_source_full_four_all_real_cone_flag(self):
        original=CertifiedFourPrimeFullPhaseSchurTrial(
            J_center=64,J_G=64,J_deriv=2,J_edge=8,digits=100,eta=F(1,8)
        )
        self.assertEqual(original["source_sha"],
                         "0cc8510b71d178fc79e8d410a86d8b6014cf9178")
        blocks=original["source_parity_cone_certificates"]
        self.assertEqual(set(blocks),{"odd_derivative","even_derivative"})
        for sector in blocks.values():
            self.assertTrue(sector["tested_unbounded_tails"])
            self.assertTrue(sector["tested_vertical_direction"])
            self.assertFalse(sector["RH_proved"])
        self.assertEqual(
            original["source_positive_S4_first_window"],
            original["source_Loewner_lower_PSD"] or
            original["exact_all_direction_source_robust_cone_PSD"]
        )
        self.assertFalse(original["RH_proved"])


if __name__=="__main__":
    unittest.main()
