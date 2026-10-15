"""Finite-state versus causal-history source-gluing exact countermodels."""
import unittest

from observational_succ.field_history_lift import (
    HistoryLiftError,finite_successor_history_alias,
    exact_finite_refinement_repairs_fixed_history,
    diagonal_adelic_lift_history,history_faithfulness_requirement,
)


class ActualSUCCSourceHistoryVsQuotientPointTests(unittest.TestCase):
    def test_source_successor_winding_nontrivial_but_quotient_endpoint_identical(self):
        for modulus in (2,3,4,5,7,11):
            for k in (1,2,3):
                z=finite_successor_history_alias(modulus,k*modulus)
                self.assertTrue(z.endpoint_collision)
                self.assertEqual(z.visible_start,z.visible_end)
                self.assertEqual(z.action_steps,k*modulus)
                self.assertFalse(z.original_history_trivial)
                self.assertFalse(z.source_event_faithful_from_endpoint_only)
                self.assertFalse(z.source_lift_observed)
                self.assertFalse(z.RH_proved)

    def test_fixed_integer_history_not_permanently_hidden_by_full_quotient_tower(self):
        for steps in (1,2,3,9,25,51):
            z=exact_finite_refinement_repairs_fixed_history(steps)
            self.assertEqual(z["sufficient_distinguishing_modulus"],steps+1)
            self.assertEqual(z["refined_endpoint"],steps)
            self.assertTrue(z["fixed_history_eventually_distinguished_by_residue_tower"])
            self.assertFalse(z["RH_proved"])

    def test_true_real_profinite_adelic_quotient_has_lift_history_alias(self):
        for k in (-7,-1,1,2,17,101):
            z=diagonal_adelic_lift_history(k)
            self.assertEqual(z["nontrivial_integer_lift_event"],k)
            self.assertFalse(z["quotient_endpoint_different"])
            self.assertTrue(z["source_event_nontrivial"])
            self.assertTrue(z["ordered_lift_path_suppressed_by_point_quotient"])
            self.assertTrue(z["source_lift_cocycle_must_be_retained_for_history_claim"])
            self.assertFalse(z["physical_action_event_performed"])
            self.assertFalse(z["RH_proved"])

    def test_source_model_of_model_point_not_full_history_functor(self):
        q=history_faithfulness_requirement()
        self.assertFalse(q["quotient_state_map_injective_on_events"])
        self.assertFalse(q["global_source_point_identified_implies_performed_history_identified"])
        self.assertFalse(q["actual_genuine_Weil_sign_proved"])
        self.assertFalse(q["RH_proved"])

    def test_illegal_event_inputs_rejected_without_source_forging(self):
        for args in ((1,1),(4,0),(4,-1),(4,True),(True,2),(5,1000001)):
            with self.assertRaises(HistoryLiftError):
                finite_successor_history_alias(*args)
        for v in (0,-1,True,100000):
            with self.assertRaises(HistoryLiftError):
                exact_finite_refinement_repairs_fixed_history(v)
        for v in (0,True,1000001):
            with self.assertRaises(HistoryLiftError):
                diagonal_adelic_lift_history(v)


if __name__=="__main__":
    unittest.main()
