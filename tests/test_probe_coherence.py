"""Exact hostile controls for finite proof-carrier backaction and typed support."""
from dataclasses import replace
from itertools import product
import unittest

from observational_succ.probe_coherence import (
    InitialSource, Reading, DestructiveCarrier, CarrierHorizonError,
    fixed_probe_trace, indistinguishable_source_pairs,
    local_carrier_no_go, independent_carrier_repair,
    nondestructive_probe_repair, prior_law_repair, probe_coherence_demo,
    probe_family_determines_target, minimal_logical_probe_supports,
    proof_induced_question_rewiring_demo,
)


class ProbeCoherenceTests(unittest.TestCase):
    def test_first_a_probe_destroyed_initial_b_meaning_but_not_current_b(self):
        src=InitialSource(0,1)
        first=DestructiveCarrier.from_source(src).probe("a")
        self.assertEqual(first.a,0)
        self.assertEqual(first.b,0)
        self.assertEqual(first.initial_support(),{"a":0})
        self.assertFalse(first.b_refers_to_initial)
        self.assertEqual(first.coherent_original_probes_remaining(),())
        self.assertIsNone(first.target_certificate())
        second=first.probe("b")
        self.assertEqual(second.trace[-1].outcome,0)
        self.assertEqual(second.trace[-1].before_version,1)
        self.assertFalse(second.trace[-1].refers_to_initial_source)
        self.assertEqual(second.initial_support(),{"a":0})
        self.assertIsNone(second.target_certificate())
        self.assertEqual(src.parity,1)
        self.assertNotEqual(second.trace[-1].outcome,src.b)

    def test_first_b_probe_destroyed_original_a_support(self):
        src=InitialSource(1,0)
        first=DestructiveCarrier.from_source(src).probe("b")
        self.assertEqual(first.initial_support(),{"b":0})
        self.assertEqual(first.coherent_original_probes_remaining(),())
        later=first.probe("a")
        self.assertFalse(later.trace[-1].refers_to_initial_source)
        self.assertEqual(later.initial_support(),{"b":0})
        self.assertIsNone(later.target_certificate())

    def test_exact_adaptive_protocol_no_go_by_first_action(self):
        receipt=local_carrier_no_go()
        self.assertEqual(receipt["status"],
                         "FINITE_SINGLE_CARRIER_SOURCE_COHERENCE_NO_GO")
        self.assertEqual(receipt["first_a_indistinguishable_pair"],["00","01"])
        self.assertEqual(receipt["first_b_indistinguishable_pair"],["00","10"])
        self.assertTrue(receipt["proof_support_unreachable_with_one_carrier"])
        self.assertFalse(receipt["global_logical_unprovability_claimed"])
        self.assertFalse(receipt["RH_claimed"])

    def test_every_finite_nonrepeating_order_retains_opposite_parity_worlds(self):
        for first in ("a","b"):
            for rest in [(),("a",),("b",),("a","b"),("b","a"),
                         ("a","a","b"),("b","b","a")]:
                rival=indistinguishable_source_pairs((first,)+rest)
                self.assertGreater(len(rival),0)
                self.assertTrue(all(a.parity != b.parity for a,b in rival))
        self.assertEqual(len(indistinguishable_source_pairs(())),4)

    def test_two_independent_identical_preparations_repair_every_world(self):
        for values in product((0,1),repeat=2):
            src=InitialSource(*values)
            self.assertEqual(independent_carrier_repair(src),src.parity)
        # An actual second source copy is a substantive added resource, not
        # a one-step magical undo operation after the destructive measurement.
        first=DestructiveCarrier.from_source(InitialSource(0,1)).probe("a")
        self.assertFalse(first.b_refers_to_initial)

    def test_read_only_probe_repairs_every_world(self):
        for values in product((0,1),repeat=2):
            source=InitialSource(*values)
            self.assertEqual(nondestructive_probe_repair(source),source.parity)

    def test_valid_mathematical_prior_can_make_a_probe_redundant(self):
        all_sources=tuple(InitialSource(a,b) for a,b in product((0,1),repeat=2))
        self.assertIsNone(prior_law_repair(all_sources))
        self.assertEqual(prior_law_repair((InitialSource(0,0),InitialSource(1,1))),0)
        self.assertEqual(prior_law_repair((InitialSource(0,1),InitialSource(1,0))),1)
        self.assertEqual(prior_law_repair((InitialSource(1,0),)),1)
        # Conditional mathematical implications do not prove the prior holds:
        # changing the source class is a new axiom / evidence premise.

    def test_logical_probe_graph_minimum_and_carrier_support_are_distinct(self):
        universe=tuple(InitialSource(a,b) for a,b in product((0,1),repeat=2))
        self.assertFalse(probe_family_determines_target(universe,()))
        self.assertFalse(probe_family_determines_target(universe,("a",)))
        self.assertFalse(probe_family_determines_target(universe,("b",)))
        self.assertTrue(probe_family_determines_target(universe,("a","b")))
        self.assertEqual(minimal_logical_probe_supports(universe),(("a","b"),))
        for source in universe:
            for order in (("a","b"),("b","a")):
                support=fixed_probe_trace(source,order).initial_support()
                self.assertLess(len(support),2)
        with self.assertRaises(CarrierHorizonError):
            probe_family_determines_target(universe,("a","a"))

    def test_verified_premise_contracts_and_rewires_minimum_probe_graph(self):
        universe=tuple(InitialSource(a,b) for a,b in product((0,1),repeat=2))
        a_zero=tuple(s for s in universe if s.a==0)
        equality=tuple(s for s in universe if s.a==s.b)
        self.assertEqual(minimal_logical_probe_supports(a_zero),(("b",),))
        self.assertEqual(minimal_logical_probe_supports(equality),((),))
        report=proof_induced_question_rewiring_demo()
        self.assertEqual(report["unrestricted_minimal_probe_supports"],[["a","b"]])
        self.assertEqual(report["with_verified_a_zero_law"],[["b"]])
        self.assertEqual(report["with_verified_a_equal_b_law"],[[]])
        self.assertFalse(report["same_carrier_can_jointly_realize_unrestricted_support"])
        self.assertTrue(report["single_b_probe_works_after_valid_a_zero_law"])
        self.assertFalse(report["globally_minimal_proof_encoding_claimed"])
        # False premise cannot turn conditional support into unconditional truth.
        bad=InitialSource(1,0)
        observed_b=fixed_probe_trace(bad,("b",)).initial_support()["b"]
        self.assertEqual(observed_b,0)
        self.assertNotEqual(observed_b,bad.parity)

    def test_no_single_carrier_trace_can_legitimately_contain_both_initial_bits(self):
        for values in product((0,1),repeat=2):
            src=InitialSource(*values)
            for length in range(5):
                for order in product(("a","b"),repeat=length):
                    state=fixed_probe_trace(src,tuple(order))
                    self.assertLessEqual(len(state.initial_support()),1)
                    self.assertIsNone(state.target_certificate())
                    self.assertEqual(state.version,length)
                    self.assertEqual(len(state.trace),length)

    def test_mutating_source_tag_cannot_serve_as_correct_certificate(self):
        src=InitialSource(0,1)
        carrier=fixed_probe_trace(src,("a","b"))
        bad=replace(carrier.trace[-1],refers_to_initial_source=True)
        forged=replace(carrier,trace=carrier.trace[:-1]+(bad,))
        # This private mutation bypasses the trusted transition semantics.
        # A bare self-authored record proves nothing about the physical world.
        self.assertNotEqual(forged.initial_support(),carrier.initial_support())
        self.assertEqual(forged.target_certificate(),0)
        self.assertNotEqual(forged.target_certificate(),src.parity)
        # The source-protocol validator rejects any such physically impossible
        # purported initial-origin annotation by replaying the source actions.
        actual=fixed_probe_trace(src,tuple(e.probe for e in forged.trace))
        self.assertNotEqual(actual.trace,forged.trace)

    def test_constructor_negative_controls(self):
        with self.assertRaises(CarrierHorizonError):
            InitialSource(True,0)
        with self.assertRaises(CarrierHorizonError):
            InitialSource(0,2)
        with self.assertRaises(CarrierHorizonError):
            DestructiveCarrier(1,0,a_refers_to_initial=1)
        with self.assertRaises(CarrierHorizonError):
            Reading("c",0,0,1,True)
        with self.assertRaises(CarrierHorizonError):
            Reading("a",0,0,3,True)
        with self.assertRaises(CarrierHorizonError):
            fixed_probe_trace(InitialSource(0,1),("c",))
        with self.assertRaises(CarrierHorizonError):
            fixed_probe_trace(InitialSource(0,1),("a",)*65)
        with self.assertRaises(CarrierHorizonError):
            prior_law_repair(())

    def test_reproducible_status_stays_within_theorem_scope(self):
        d=probe_coherence_demo()
        self.assertTrue(d["proof_support_unreachable_with_one_carrier"])
        self.assertEqual(d["proof_graph_rewiring"]["status"],
                         "PROOF_INDUCED_MINIMAL_DEPENDENCY_REWIRING")
        self.assertTrue(d["two_independent_preparations_repair_target"])
        self.assertTrue(d["non_destructive_probe_repairs_target"])
        self.assertTrue(d["lawful_source_prior_can_decide_without_experiment"])
        self.assertTrue(d["second_probe_current_value_is_still_defined"])
        self.assertTrue(d["second_probe_original_source_value_is_no_longer_defined"])
        self.assertFalse(d["global_logical_unprovability_claimed"])
        self.assertFalse(d["RH_claimed"])


if __name__=="__main__":
    unittest.main()
