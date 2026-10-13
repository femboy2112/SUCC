"""Genetic search cannot masquerade as complete source-relative proof."""
import unittest
from random import Random

from observational_succ.finite_poset_synthesis import (
    chain, PairedPosetSource, PosetFunctor, all_functors,
)
from observational_succ.eodcs_evolutionary_discovery import (
    _proposal, _breed, genetic_functor_search, blind_source_demo,
)
from observational_succ.relational_model_genetics import GeneticsError


def holdout():
    a = chain(*(str(i) for i in range(6)))
    b = chain("cold", "warm", "hot")
    truth = ("cold", "cold", "warm", "warm", "hot", "hot")
    return PairedPosetSource("blind", 0, "order", a, b, tuple(
        (str(i), x, y) for i, (x, y) in enumerate(zip(a.objects, truth))), True)


class TestGeneticFunctorCEGIS(unittest.TestCase):
    def test_all_candidates_are_typed_monotone(self):
        t = holdout()
        rng = Random(9)
        for i in range(100):
            f = _proposal(t, {"0": "cold", "4": "hot"}, rng)
            self.assertIsNotNone(f)
            self.assertEqual(f("0"), "cold")
            self.assertEqual(f("4"), "hot")
            self.assertIn(f, all_functors(t.domain, t.codomain))

    def test_genetic_crossover_must_still_be_verified(self):
        t = holdout()
        rng = Random(88)
        for _ in range(100):
            f = _proposal(t, {}, rng)
            g = _proposal(t, {}, rng)
            child = _breed(f, g, rng)
            self.assertIn(child, all_functors(t.domain, t.codomain))

    def test_exclusions_are_actual_source_counterexamples(self):
        t = holdout()
        r = genetic_functor_search(t, seed=0, generations=8)
        oracle = t.oracle()
        for x, predicted, observed in r.no_good_clauses:
            self.assertEqual(observed, oracle[x])
            self.assertNotEqual(predicted, observed)

    def test_incomplete_probe_budget_is_not_genetic_source_proof(self):
        t = holdout()
        r = genetic_functor_search(t, seed=3, generations=2, population=4)
        self.assertFalse(r.genetically_discovered)
        self.assertEqual(len(r.source_probes), 2)
        self.assertEqual(r.exact_oracle_model,
                         ("cold", "cold", "warm", "warm", "hot", "hot"))
        self.assertTrue(r.exact_oracle_rescue)
        self.assertTrue(r.source_class_certified)

    def test_seeded_runs_do_not_get_fallback_credit(self):
        t = holdout()
        for seed in range(20):
            r = genetic_functor_search(t, seed=seed, generations=9)
            self.assertEqual(r.source_class_certified, True)
            self.assertEqual(r.exact_oracle_model,
                             ("cold", "cold", "warm", "warm", "hot", "hot"))
            self.assertEqual(r.exact_oracle_rescue, not r.genetically_discovered)
            if r.genetically_discovered:
                self.assertEqual(r.genetic_model, r.exact_oracle_model)
            else:
                self.assertIsNone(r.genetic_model)

    def test_source_missing_bijection_proof_triggers_grammar_growth(self):
        r = genetic_functor_search(holdout(), seed=11)
        self.assertEqual(r.grammar_expansion, "NO_ISOMORPHISM_CARDINALITY")

    def test_nonmonotone_source_is_not_saved_by_a_false_functor(self):
        a, b = chain("a", "b"), chain("cold", "warm")
        t = PairedPosetSource("s", 0, "b", a, b,
                             (("s0", "a", "warm"), ("s1", "b", "cold")), True)
        r = genetic_functor_search(t, seed=4, generations=4)
        self.assertIsNone(r.exact_oracle_model)
        self.assertFalse(r.genetically_discovered)
        self.assertFalse(r.source_class_certified)

    def test_blind_generated_source_has_no_preinstalled_partition(self):
        r = blind_source_demo(7)
        self.assertEqual(r["source_probes"], 8)
        self.assertTrue(r["full_source_relatively_certified"])
        self.assertEqual(sum(len(fiber) for fiber in r["source_partition"]), 8)
        self.assertFalse(r["physical_source_authenticated"])
        self.assertFalse(r["grammar_was_open_ended"])
        self.assertEqual(r["unqueried_training_version_space"], 4)
        self.assertFalse(r["training_source_certified"])
        self.assertTrue(r["withheld_true_source_within_prediction_sets"])
        self.assertEqual(r["sealed_holdout_prediction_sets"]["x7"], ["hot", "plasma"])

    def test_mutation_rejects_wrong_budget(self):
        with self.assertRaises(GeneticsError):
            genetic_functor_search(holdout(), seed=0, population=2)
        with self.assertRaises(GeneticsError):
            genetic_functor_search(holdout(), seed=0, generations=0)

    def test_partial_source_never_certifies_a_missing_global_law(self):
        t = holdout()
        t2 = PairedPosetSource(t.source_id, t.epoch, t.basis, t.domain,
                               t.codomain, t.observations[:2], False)
        r = genetic_functor_search(t2, seed=1, generations=8)
        self.assertIsNone(r.exact_oracle_model)
        self.assertFalse(r.source_class_certified)
        self.assertFalse(r.genetically_discovered)


if __name__ == "__main__":
    unittest.main()
