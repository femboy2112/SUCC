"""Source-passive countermodels and analogical inference regression tests."""
import unittest
from fractions import Fraction as Q
from observational_succ.categorical_repair_synthesis import positive_passive_alias
from observational_succ.heuristic_bridge_discovery import (
    holdout_shape_demo,cross_context_analogy_demo,passive_probe,
    exact_response_probe,declared_sensor,
)
from observational_succ.contextual_heuristics import (
    ModelShape,ModelProbe,ProbeReceipt,HeuristicTower,HeuristicError,
)


class StructuralHeuristicsTests(unittest.TestCase):
    def test_unknown_modal_shape_four_samples_still_aliased(self):
        d=holdout_shape_demo()
        self.assertEqual((d["lower_degree"],d["higher_degree"]),(2,3))
        self.assertEqual(d["prior"],{"two-mode":Q(2,3),"three-mode":Q(1,3)})
        self.assertEqual(d["posterior_after_four_independent_reports"],d["prior"])
        self.assertTrue(d["first_four_frequency_responses_equal"])
        self.assertEqual(d["s4_expected_target_gini_gain"],Q(2,1946711832863))
        self.assertTrue(d["s4_exact_report_would_separate"])
        self.assertFalse(d["actual_source_authenticated"])
        self.assertFalse(d["formal_proof_from_positive_posterior"])

    def test_exact_heldout_discriminator_but_not_guaranteed_physical_instrument(self):
        a=positive_passive_alias((0,1,2,3))
        laws={"two":a.lower,"three":a.higher}
        p=exact_response_probe(laws,Q(4))
        self.assertEqual(len(p.outcomes),2)
        self.assertEqual({p.law(k) for k in laws},{(Q(1),Q(0)),(Q(0),Q(1))})

    def test_analogy_transports_prediction_not_ontology(self):
        d=cross_context_analogy_demo()
        self.assertEqual(d["translated_posterior"],d["thermal_prior"])
        self.assertFalse(d["physical_source_shared"])

    def test_cost_sensitive_action_planning_exact(self):
        alias=positive_passive_alias((0,1,2,3))
        models=(ModelShape("l","c",frozenset(),4,"lower"),
                ModelShape("h","c",frozenset(),4,"higher"))
        t=HeuristicTower(models,frozenset(),source_id="s",epoch=0,basis_id="b")
        laws={"l":alias.lower,"h":alias.higher}
        p4=passive_probe(laws,Q(4),context="c",cost=10)
        p0=passive_probe(laws,Q(0),context="c",cost=1)
        ranking=t.rank_probes((p0,p4))
        self.assertEqual(ranking[0][0],p4.name)
        self.assertEqual(ranking[1][2],0)
        self.assertGreater(ranking[0][2],0)

    def test_randomized_finite_alias_family_has_zero_gain_until_heldout(self):
        for offset in (0,3,5,9,17):
            samples=tuple(Q(j+offset) for j in range(4))
            alias=positive_passive_alias(samples)
            laws={"lower":alias.lower,"higher":alias.higher}
            models=(ModelShape("lower","c",frozenset(),3,"2"),
                    ModelShape("higher","c",frozenset(),3,"3"))
            t=HeuristicTower(models,frozenset(),source_id="S",epoch=0,basis_id="B")
            for x in samples:
                self.assertEqual(t.expected_gini_gain(passive_probe(laws,x,context="c")),0)
            self.assertGreater(t.expected_gini_gain(passive_probe(laws,alias.first_holdout,context="c")),0)

    def test_finite_noisy_probe_may_have_tiny_information_gain(self):
        alias=positive_passive_alias((0,1,2,3))
        laws={"lower":alias.lower,"higher":alias.higher}
        models=(ModelShape("lower","c",frozenset(),3,"2"),
                ModelShape("higher","c",frozenset(),3,"3"))
        t=HeuristicTower(models,frozenset(),source_id="S",epoch=0,basis_id="B")
        gain=t.expected_gini_gain(passive_probe(laws,4,context="c"))
        self.assertGreater(gain,0)
        self.assertLess(gain,Q(1,1_000_000_000))

    def test_reject_negative_network_response(self):
        with self.assertRaises(HeuristicError):declared_sensor(Q(-1,10))

if __name__=="__main__":unittest.main()
