"""Exact source-gluing positive recursion, singular Schur, ghost controls."""
import unittest
from fractions import Fraction as F

from observational_succ.source_field_gluing import (
    FieldGluingError, exact_scalar_schur_gluing,
    recursive_positive_gram_stage, paired_neutral_source_birth,
)


class FiniteToGlobalPositiveSimpleProof(unittest.TestCase):
    def test_one_source_recursive_Gram_law_proves_uniform_all_n(self):
        for t in (F(0),F(1,3),F(1,2),-F(1,2)):
            prev=None
            for n in range(1,11):
                x=recursive_positive_gram_stage(n,t)
                self.assertTrue(x["exact_factorization_G_equals_L_Lstar"])
                self.assertTrue(x["all_n_compatible_prefix_law_by_formula"])
                self.assertEqual(x["uniform_infinite_positive_gap"],(1-abs(t))**2)
                self.assertEqual(x["finite_G_matrix"][0][0],F(1))
                self.assertFalse(x["all_infinite_matrices_physically_evaluated"])
                self.assertFalse(x["RH_proved"])
                if prev is not None:
                    self.assertEqual(
                        tuple(tuple(row[:n-1]) for row in x["finite_G_matrix"][:n-1]),prev
                    )
                prev=x["finite_G_matrix"]

    def test_source_law_is_not_arbitrarily_positive_for_any_parameter(self):
        for n,t in ((0,F(1,2)),(21,F(1,2)),(2,1),(2,-1),
                    (2,F(3,2)),(2,0.5),(True,F(1,2))):
            with self.assertRaises(FieldGluingError):
                recursive_positive_gram_stage(n,t)


class HonestSingularGluingGate(unittest.TestCase):
    def test_true_valid_schur_has_source_signed_correlation(self):
        d=exact_scalar_schur_gluing(1,F(1,2),F(1,4))
        self.assertTrue(d["complete_block_PSD"])
        self.assertEqual(d["principal_determinant"],0)
        self.assertEqual(d["true_schur_when_defined"],0)
        self.assertTrue(d["cross_in_parent_range"])
        self.assertFalse(d["RH_proved"])

    def test_positive_diagonals_do_not_guarantee_globally_positive_block(self):
        bad=exact_scalar_schur_gluing(1,1,F(1,2))
        self.assertTrue(bad["separate_parent_and_newborn_PSD"])
        self.assertFalse(bad["complete_block_PSD"])
        self.assertEqual(bad["true_schur_when_defined"],-F(1,2))
        self.assertEqual(bad["principal_determinant"],-F(1,2))

    def test_singular_parent_requires_real_range_gate(self):
        hidden=exact_scalar_schur_gluing(0,F(1,2),1)
        good=exact_scalar_schur_gluing(0,0,1)
        self.assertTrue(hidden["separate_parent_and_newborn_PSD"])
        self.assertFalse(hidden["cross_in_parent_range"])
        self.assertFalse(hidden["complete_block_PSD"])
        self.assertIsNone(hidden["true_schur_when_defined"])
        self.assertTrue(good["cross_in_parent_range"])
        self.assertTrue(good["complete_block_PSD"])
        self.assertEqual(good["true_schur_when_defined"],1)

    def test_wrong_source_epoch_and_illegal_numeric_inputs_rejected(self):
        for v in (True,0.5):
            with self.assertRaises(FieldGluingError):
                exact_scalar_schur_gluing(1,v,1)
        with self.assertRaises(FieldGluingError):
            exact_scalar_schur_gluing(-1,0,1)
        with self.assertRaises(FieldGluingError):
            exact_scalar_schur_gluing(1,0,1,parent_source="original",child_source="phantom")
        with self.assertRaises(FieldGluingError):
            exact_scalar_schur_gluing(1,0,1,parent_source="",child_source="")


class APOLLOPairedNeutralSourceContrast(unittest.TestCase):
    def test_zero_signed_delta_does_not_mean_zero_features(self):
        r=paired_neutral_source_birth(F(3),F(2),F(1,4))
        self.assertEqual(r["old_signed_source_value"],1)
        self.assertEqual(r["new_signed_source_value"],1)
        self.assertTrue(r["signed_old_window_unchanged"])
        self.assertTrue(r["both_feature_carriers_changed"])
        self.assertTrue(r["independent_feature_nesting_is_not_a_contraction_proof"])
        self.assertFalse(r["original_source_a_genuine_all_radii_contraction_proved"])
        self.assertFalse(r["RH_proved"])

    def test_illegal_neutral_source_weights_rejected(self):
        for a,b,w in ((-1,0,1),(0,-1,1),(1,1,0),(1,1,-1),(1,1,0.2)):
            with self.assertRaises(FieldGluingError):
                paired_neutral_source_birth(a,b,w)


if __name__=="__main__":
    unittest.main()
