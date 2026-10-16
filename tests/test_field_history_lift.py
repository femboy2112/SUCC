"""Finite-state versus causal-history source-gluing exact countermodels."""
import unittest

from observational_succ.field_history_lift import (
    HistoryLiftError,finite_successor_history_alias,
    exact_finite_refinement_repairs_fixed_history,
    diagonal_adelic_lift_history,history_faithfulness_requirement,
    exact_finite_source_periodization,
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


class TateSourceLatticeLiftPeriodizationTests(unittest.TestCase):
    def test_true_quotient_periodization_counts_multiple_original_source_lifts(self):
        for modulus in (2,3,4,6):
            z=exact_finite_source_periodization(modulus,((0,1),(modulus,2),(2*modulus,3)))
            self.assertEqual(z["correct_periodization"][0],6)
            self.assertEqual(z["naive_representative_evaluation"][0],1)
            self.assertEqual(z["lattice_lift_buckets"][0],(0,modulus,2*modulus))
            self.assertFalse(z["endpoint_quotient_alone_determines_periodization"])
            self.assertFalse(z["Tate_global_Poisson_proved"])
            self.assertFalse(z["RH_proved"])

    def test_source_support_with_one_lift_per_class_is_lawfully_simple(self):
        r=exact_finite_source_periodization(4,((-1,2),(1,3),(9,5)))
        self.assertEqual(r["correct_periodization"][1],8)
        self.assertEqual(r["naive_representative_evaluation"][1],3)
        self.assertEqual(r["correct_periodization"][3],2)
        b=exact_finite_source_periodization(4,((0,2),(1,3)))
        self.assertTrue(b["endpoint_quotient_alone_determines_periodization"])

    def test_lattice_source_duplicate_and_invalid_tools_refused(self):
        for modulus,data in (
            (1,((0,1),)),
            (2,()),
            (2,((0,1),(0,2))),
            (2,((0,1.0),)),
            (2,((True,1),)),
            (2,((0,True),)),
        ):
            with self.assertRaises(HistoryLiftError):
                exact_finite_source_periodization(modulus,data)


if __name__=="__main__":
    unittest.main()
