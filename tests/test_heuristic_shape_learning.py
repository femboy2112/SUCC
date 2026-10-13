"""Independent task meta-prior: update, calibration scope and data-leak gates."""
import unittest
from fractions import Fraction as Q
from observational_succ.contextual_heuristics import HeuristicError,ModelShape
from observational_succ.heuristic_shape_learning import (
    ShapeHeuristic,IndependentSolvedTask,HeuristicMetaLearner,learning_demo,
)


class MetaHeuristicTests(unittest.TestCase):
    def setUp(self):
        self.models=(ModelShape("a","c",frozenset(("storage",)),3,"a"),
                     ModelShape("b","c",frozenset(),3,"b"))
        self.schemes=(ShapeHeuristic("shape-aware",{"storage":2}),
                      ShapeHeuristic("flat",{}))
        self.learn=HeuristicMetaLearner(self.schemes,{"shape-aware":Q(1,2),"flat":Q(1,2)})

    def task(self,task_id="1",source_id="s1",winner="a"):
        return IndependentSolvedTask(task_id,source_id,self.models,frozenset(("storage",)),
                                     winner,"synthetic independent solver receipt")

    def test_learning_is_exact_bayesian_hyperposterior(self):
        self.assertEqual(self.learn.prior_for_new_context(self.models,frozenset(("storage",))),
                         {"a":Q(13,20),"b":Q(7,20)})
        posterior=self.learn.update_from_verified_task(self.task())
        self.assertEqual(posterior,{"shape-aware":Q(8,13),"flat":Q(5,13)})
        next_prior=self.learn.prior_for_new_context(self.models,frozenset(("storage",)))
        self.assertEqual(next_prior["a"],Q(8,13)*Q(4,5)+Q(5,13)*Q(1,2))
        self.assertGreater(next_prior["a"],Q(13,20))

    def test_failed_analogy_can_update_heurstic_weight_down(self):
        post=self.learn.update_from_verified_task(self.task(winner="b"))
        self.assertEqual(post["shape-aware"],Q(2,7))
        self.assertEqual(post["flat"],Q(5,7))

    def test_no_double_count_source_or_event(self):
        self.learn.update_from_verified_task(self.task())
        for task in (self.task(),self.task("2","s1")):
            with self.assertRaises(HeuristicError):self.learn.update_from_verified_task(task)
        self.assertEqual(len(self.learn.verified_tasks),1)

    def test_only_features_relevant_to_current_context_contribute(self):
        prior=self.learn.prior_for_new_context(self.models,frozenset(("other",)))
        self.assertEqual(prior,{"a":Q(1,2),"b":Q(1,2)})

    def test_declared_shape_prior_can_be_explicitly_uninformative(self):
        demo=learning_demo()
        self.assertEqual(demo["pretraining_model_prior"]["memory"],Q(13,20))
        self.assertTrue(demo["shape_confidence_changed"])
        self.assertFalse(demo["formal_truth_of_new_model_proved"])
        self.assertFalse(demo["empirical_calibration_authenticated"])

    def test_scheme_bounds_and_missing_certificate(self):
        with self.assertRaises(HeuristicError):ShapeHeuristic("bad",{"x":100})
        with self.assertRaises(HeuristicError):self.task(winner="not-a-model")
        with self.assertRaises(HeuristicError):
            IndependentSolvedTask("1","s",self.models,frozenset(),"a","")

    def test_train_on_multiple_independent_sources(self):
        self.learn.update_from_verified_task(self.task())
        after=self.learn.update_from_verified_task(self.task("2","s2"))
        self.assertEqual(after["shape-aware"],Q(64,89))
        self.assertGreater(after["shape-aware"],Q(8,13))

if __name__=="__main__":unittest.main()
