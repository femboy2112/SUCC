"""Exact dual-range criterion and infinite soft/hard spectral controls."""
import unittest
from fractions import Fraction as F
from observational_succ.source_surplus_range import (
    SurplusRangeError,source_surplus_rank_one_gate,
    infinite_diagonal_surplus_obstruction,
    positive_diagonal_not_rank_one_certificate,
)


class SourceSurplusRangeTests(unittest.TestCase):
    def test_singular_positive_range_and_wrong_direction(self):
        A=((F(1),F(1)),(F(1),F(1)))
        aligned=source_surplus_rank_one_gate(A,(F(1),F(1)))
        wrong=source_surplus_rank_one_gate(A,(F(1),F(0)))
        self.assertTrue(aligned["square_root_range_holds"])
        self.assertEqual(aligned["best_delta"],F(1))
        self.assertFalse(wrong["square_root_range_holds"])
        self.assertFalse(wrong["positive_delta_exists"])

    def test_anisotropic_full_rank_sharp_remainder(self):
        result=source_surplus_rank_one_gate(
            ((F(1,4),F(0)),(F(0),F(4))),
            (F(1),F(1)))
        self.assertEqual(result["dual_squared"],F(17,4))
        self.assertEqual(result["best_delta"],F(4,17))
        self.assertTrue(result["verified_not_psd_above_best"])

    def test_missing_source_premise_rejected(self):
        with self.assertRaises(SurplusRangeError):
            source_surplus_rank_one_gate(((F(1),F(2)),(F(2),F(1))),(1,0))
        with self.assertRaises(SurplusRangeError):
            source_surplus_rank_one_gate(((F(1),),),(F(0),))
        with self.assertRaises(SurplusRangeError):
            source_surplus_rank_one_gate(((F(1),),),(True,))

    def test_infinite_prefixes_prove_nonuniformity(self):
        for N in (1,2,4,10,100):
            r=infinite_diagonal_surplus_obstruction(N)
            self.assertEqual(r["hard_dual_squared"],N)
            self.assertEqual(r["hard_exact_finite_delta"],F(1,N))
            self.assertTrue(r["soft_partial_delta_gt_half"])
            self.assertFalse(r["RH_proved"])
        cert=positive_diagonal_not_rank_one_certificate()
        self.assertTrue(cert["positive_diagonal"])
        self.assertFalse(cert["wrong_direction_delta_exists"])
        self.assertEqual(cert["aligned_direction_best_delta"],F(1))


if __name__=="__main__":unittest.main()
