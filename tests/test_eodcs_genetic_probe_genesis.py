"""Genetic proposal is never an exact source proof or physical instrument."""
import unittest
from random import Random
from itertools import product

from observational_succ.eodcs_multi_action_source import (
    ActionSource, shortest_distinguishing_word,
)
from observational_succ.eodcs_genetic_probe_genesis import (
    ProbeGenome,validate_word,mutate,crossover,genetic_probe_search,
    genetic_probe_demo,
)
from observational_succ.causal_nerode_succ import SourceTransportError


def two_step_source():
    return ActionSource("s",0,"typed",("x","y","u","v","c","d"),
                        ("0","0","0","0","0","1"),("A","B"),
                        (("u","v","u","v","c","d"),
                         ("x","y","c","d","c","d")))


class TestGeneticProbeGenesis(unittest.TestCase):
    def test_tight_budget_failure_and_independent_exact_rescue(self):
        src=two_step_source()
        r=genetic_probe_search(src,"x","y",seed=0,population=5,generations=1)
        self.assertFalse(r.genetic_succeeded)
        self.assertTrue(r.bounded_oracle_rescue)
        self.assertEqual(r.exact_shortest_separator,("A","B"))
        self.assertIsNone(r.genetic_verified_separator)
        self.assertFalse(r.physical_probe_materialized)

    def test_20_seeded_genetic_proposals_cannot_borrow_oracle_credit(self):
        src=two_step_source()
        for seed in range(20):
            r=genetic_probe_search(src,"x","y",seed=seed)
            self.assertEqual(r.exact_shortest_separator,("A","B"))
            self.assertEqual(r.bounded_oracle_rescue,not r.genetic_succeeded)
            if r.genetic_succeeded:
                self.assertNotEqual(src.observe("x",r.genetic_verified_separator),
                                    src.observe("y",r.genetic_verified_separator))
            else:
                self.assertIsNone(r.genetic_verified_separator)

    def test_mutation_and_crossover_preserve_grammar_types_for_800_rounds(self):
        src=two_step_source()
        rng=Random(44)
        a=ProbeGenome(())
        b=ProbeGenome(("A","B"))
        for _ in range(800):
            a=mutate(a,src.actions,rng,5)
            b=crossover(a,b,rng,5)
            validate_word(src,a,5)
            validate_word(src,b,5)
            self.assertLessEqual(len(a.word),5)
            self.assertLessEqual(len(b.word),5)
            self.assertTrue(set(a.word).issubset(src.actions))

    def test_external_lamp_not_synthesized_from_closed_dark_menu(self):
        states=("a","b","c","d")
        src=ActionSource("dark",0,"typed",states,("0","0","1","1"),
                         ("A","B"),
                         (("b","a","d","c"),("a","b","d","c")))
        r=genetic_probe_search(src,"a","b",seed=3)
        self.assertIsNone(r.exact_shortest_separator)
        self.assertIsNone(r.genetic_verified_separator)
        self.assertFalse(r.bounded_oracle_rescue)
        self.assertTrue(r.proven_dark_within_declared_action_grammar)
        self.assertFalse(r.physical_probe_materialized)

    def test_negative_source_and_bad_budget_genomes_rejected(self):
        src=two_step_source()
        with self.assertRaises(SourceTransportError):
            validate_word(src,ProbeGenome(("not-an-action",)),5)
        with self.assertRaises(SourceTransportError):
            genetic_probe_search(src,"x","ghost",seed=0)
        with self.assertRaises(SourceTransportError):
            genetic_probe_search(src,"x","y",seed=0,population=2)
        with self.assertRaises(SourceTransportError):
            genetic_probe_search(src,"x","y",seed=0,maximum_word_length=-1)
        r=genetic_probe_search(src,"x","y",seed=0,maximum_word_length=0)
        self.assertFalse(r.genetic_succeeded)
        self.assertTrue(r.bounded_oracle_rescue)

    def test_all_2_state_2_action_source_oracle_separates_at_empty_word(self):
        states=("0","1")
        for u,v in product(tuple(product(states,repeat=2)),repeat=2):
            src=ActionSource("s",0,"b",states,states,("A","B"),(u,v))
            r=genetic_probe_search(src,"0","1",seed=2,generations=1)
            self.assertEqual(r.exact_shortest_separator,())
            self.assertTrue(r.genetic_succeeded)
            self.assertEqual(r.genetic_verified_separator,())

    def test_moonshot_receipt_keeps_failures_and_source_darkness(self):
        r=genetic_probe_demo()
        self.assertTrue(r["tight_budget_genetic_failed"])
        self.assertTrue(r["tight_budget_exact_oracle_rescued"])
        self.assertEqual(r["source_derived_exact_shortest_word"],["A","B"])
        self.assertEqual(r["twenty_seeded_genetic_successes"]+
                         r["twenty_seeded_genetic_failures"],20)
        self.assertTrue(r["dark_source_finite_grammar_empty"])
        self.assertTrue(r["dark_source_external_probe_not_invented"])
        self.assertFalse(r["general_automatic_mathematics_invented"])


if __name__=="__main__":
    unittest.main()
