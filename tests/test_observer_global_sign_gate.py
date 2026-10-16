"""Exact rational sign-gluing, source-defined Suzuki small Gram and no-ghost."""
import unittest
from fractions import Fraction as Q
from itertools import product

from observational_succ.observer_global_sign_gate import (
    GrowthGateError, certify_finite_growth, exact_scalar_schur_source_gate,
    checked_finite_gram_tower, unseen_sign_mutant,
    true_suzuki_anchored_two_point_source, dense_smooth_source_gate,
)


class FiniteObserverSchurGrowthTests(unittest.TestCase):
    def test_scalar_necessary_and_sufficient_schur_for_all_exact_small_controls(self):
        for a,b,d in product((0,Q(1,2),1,2),(0,Q(-2),Q(-1),Q(1,2),3),
                             (0,Q(-1),Q(1,3),1,4)):
            z=exact_scalar_schur_source_gate(a,b,d)
            matrix=certify_finite_growth(((a,),),(b,),d)
            self.assertEqual(z["PSD"],matrix.cross_interactions_positive)
            self.assertFalse(z["RH_proved"])
            if z["explicit_negative_direction"] is not None:
                x,y=z["explicit_negative_direction"]
                q=a*x*x+2*b*x*y+d*y*y
                self.assertLess(q,0)
                self.assertFalse(matrix.cross_interactions_positive)

    def test_local_positive_both_directions_but_cross_fails(self):
        actual=exact_scalar_schur_source_gate(1,2,1)
        self.assertEqual(actual["status"],"NEGATIVE_SCHUR_CROSS")
        self.assertEqual(actual["explicit_negative_direction"],(-2,1))
        self.assertEqual(actual["signed_source_value"],-3)
        z=certify_finite_growth(((1,),),(2,),1)
        self.assertTrue(z.each_component_positive)
        self.assertFalse(z.cross_interactions_positive)
        self.assertLess(z.negative_principal_determinant,0)

    def test_singular_range_obstruction_not_diagonal(self):
        z=exact_scalar_schur_source_gate(0,1,1)
        self.assertEqual(z["status"],"ZERO_RANGE_CROSS_OBSTRUCTION")
        self.assertFalse(z["PSD"])
        self.assertLess(z["signed_source_value"],0)
        good=exact_scalar_schur_source_gate(0,0,1)
        self.assertTrue(good["PSD"])
        self.assertEqual(good["status"],"SINGULAR_RANGE_COMPATIBLE")

    def test_source_preserving_finite_positive_tower_only_certifies_prefix(self):
        t=checked_finite_gram_tower((
            ((1,),),
            ((1,0),(0,1)),
            ((1,0,0),(0,1,0),(0,0,0)),
        ))
        self.assertTrue(t["all_supplied_source_stages_PSD"])
        self.assertEqual(t["finite_levels"],3)
        self.assertEqual(t["checked_principal_minors"],1+3+7)
        self.assertFalse(t["entire_infinite_tower_verified"])
        self.assertFalse(t["global_positive_proved"])
        self.assertFalse(t["RH_proved"])

    def test_late_stage_break_preserves_prior_models_but_refutes_sign(self):
        t=checked_finite_gram_tower((
            ((1,),),
            ((1,0),(0,1)),
            ((1,0,0),(0,1,0),(0,0,-1)),
        ))
        self.assertTrue(t["finite_stage_failure"])
        self.assertEqual(t["first_negative_stage_dimension"],3)
        self.assertLess(t["negative_principal"][1],0)

    def test_false_old_source_compatibility_refused(self):
        for stages in (
            (((1,),),((2,0),(0,1))),
            (((1,),),((0,),)),
            (((1,0),(0,1)),((1,0,0),(0,2,0),(0,0,1))),
        ):
            with self.assertRaises(GrowthGateError):
                checked_finite_gram_tower(stages)

    def test_exact_future_hidden_negative_witness_for_every_budget(self):
        for n in range(1,7):
            x=unseen_sign_mutant(n)
            self.assertEqual(x["identical_on_first"],n)
            self.assertEqual(x["new_negative_at"],n+1)
            self.assertTrue(x["two_global_sources_indistinguishable_on_tested_prefix"])
            self.assertFalse(x["original_Weil_negative_witness"])
            self.assertFalse(x["RH_proved"])

    def test_wrong_quadratic_types_and_sources_are_explicit(self):
        for args in (
            (((1,0),(0,1)),(1,),1),
            (((1,2),(0,1)),(1,2),1),
            (((-1,),),(0,),1),
            (((1,),),(True,),1),
            (((1,),),(0,),0.7),
        ):
            with self.assertRaises(GrowthGateError):
                certify_finite_growth(*args)


class AuthenticSignedArithmeticSeparationTests(unittest.TestCase):
    def test_exact_source_original_suzuki_positive_two_point_minors(self):
        z=true_suzuki_anchored_two_point_source(Q(1,4),Q(1,2),128)
        self.assertEqual(z["source"],"SHA_PINNED_AUTHENTIC_SIGNED_WEIL_SUZUKI")
        self.assertEqual(z["certified_finite_sign"],"POSITIVE")
        self.assertGreater(z["Kxx"][0],0)
        self.assertGreater(z["Kyy"][0],0)
        self.assertGreater(z["determinant"][0],0)
        self.assertFalse(z["global_all_test_sign_proved"])
        self.assertFalse(z["RH_proved"])

    def test_source_truth_not_replaced_by_anarbitrary_grammar_gram(self):
        z=true_suzuki_anchored_two_point_source(Q(-1,4),Q(1,2),64)
        self.assertIn(z["certified_finite_sign"],("POSITIVE","NEGATIVE","AMBIGUOUS"))
        self.assertEqual(z["source"],"SHA_PINNED_AUTHENTIC_SIGNED_WEIL_SUZUKI")
        for args in (
            (0,Q(1,2),128),
            (Q(1,4),Q(1,4),128),
            (Q(1,4),Q(1,2),129),
            (Q(-1,4),Q(1,2),128), # source exponent J/radius >128
            (Q(3),Q(1,2),128),
            (True,Q(1,2),128),
        ):
            with self.assertRaises(GrowthGateError):
                true_suzuki_anchored_two_point_source(*args)

    def test_global_dense_test_criterion_correctly_conditional(self):
        d=dense_smooth_source_gate()
        self.assertEqual(d["test_topology"],"C_c_infinity_LF_continuous_Weil_distribution")
        self.assertEqual(d["negative_real_witness_implies_finite_rational_probe"],
                         "CONDITIONAL_ON_CONTINUITY")
        self.assertFalse(d["finite_prefix_positive_implies_RH"])
        self.assertFalse(d["ambient_operator_bounded_L2_assumed"])
        self.assertFalse(d["RH_proved"])


if __name__=="__main__":
    unittest.main()
