"""Exact positive, negative and mutation probes for two-observer SUCC ladders."""
from dataclasses import replace
from itertools import product
import json
import unittest

from observational_succ.absorbing_frames import HornRule
from observational_succ.observer_traps import FiniteProbeWorld
from observational_succ.knowledge_ladder import (
    AgentKnowledge, SharedKnowledgeBasis, ProbeBatch, KnowledgeLadderError,
    encode_strict_relay, decode_strict_relay,
    minimal_snapshot_delta, encode_snapshot_relay, decode_snapshot_relay,
    knowledge_ladder_demo, complementary_observers_demo,
)


def chain_basis(horizon=3, a_feasible=None, b_feasible=None):
    probes = tuple(f"p{i}" for i in range(horizon))
    world = FiniteProbeWorld(
        ("A", "B"), probes, (("same",)*(horizon-1)+("A",),
                               ("same",)*(horizon-1)+("B",)),
    )
    rules = tuple(HornRule((f"obs:p{i}:same",), f"can:p{i+1}")
                  for i in range(horizon-1))
    return SharedKnowledgeBasis(
        world, ("can:p0",), rules,
        (("Alice", probes if a_feasible is None else a_feasible),
         ("Bob", probes if b_feasible is None else b_feasible)),
    )


class KnowledgeLadderTests(unittest.TestCase):
    def test_three_rung_alternating_ladder_and_true_source(self):
        report = knowledge_ladder_demo()
        self.assertEqual(report["status"], "EXACT_FINITE_INTEROBSERVER_KNOWLEDGE_LADDER")
        self.assertEqual(report["discovery_succ_steps"], 6)
        self.assertEqual(report["receiver_knowledge_aided_steps"], 3)
        self.assertEqual(report["end_source_class"], ["B"])
        self.assertEqual([x["local_discovery_steps"] for x in report["rungs"]], [2,2,2])
        self.assertEqual([x["receiver_informed_steps"] for x in report["rungs"]], [1,1,1])
        self.assertEqual([x["discoverer"] for x in report["rungs"]],
                         ["Alice", "Bob", "Alice"])
        self.assertTrue(report["full_shared_semantics_and_causal_records_match"])
        self.assertFalse(report["sender_outcomes_cryptographically_authenticated"])
        self.assertFalse(report["physical_time_speedup_proved"])
        self.assertFalse(report["infinite_ladder_executed"])

    def test_complementary_instruments_construct_joint_xor_knowledge(self):
        report = complementary_observers_demo()
        self.assertEqual(report["status"], "EXACT_DISTRIBUTED_EPISTEMIC_COMPLEMENTARITY")
        self.assertEqual(report["alice_only"], ["10", "11"])
        self.assertEqual(report["bob_only"], ["00", "10"])
        self.assertFalse(report["alice_only_xor_identified"])
        self.assertFalse(report["bob_only_xor_identified"])
        self.assertEqual(report["shared_source"], ["10"])
        self.assertEqual(report["shared_xor"], "1")
        self.assertTrue(report["replayed_remote_knowledge_not_local_measurement"])
        self.assertFalse(report["full_continuation_equivalence_of_physical_devices_claimed"])
        self.assertFalse(report["RH_claimed"])

    def test_strict_k_local_frames_become_one_b_informed_step(self):
        basis = chain_basis(4)
        a0, b0 = AgentKnowledge("Alice"), AgentKnowledge("Bob")
        a = a0.advance(basis, "B", 3)
        self.assertEqual(a.local_frames, 3)
        self.assertEqual(len(a.observations()), 3)
        packet = encode_strict_relay(a, b0, basis)
        caught = decode_strict_relay(b0, packet, basis)
        self.assertEqual(caught.local_frames, 0)
        self.assertEqual(caught.informed_steps, 1)
        self.assertEqual(caught.placement(basis), a.placement(basis))
        self.assertEqual(caught.batches, a.batches)
        self.assertEqual(caught.model(basis).epistemically_accessible,
                         a.model(basis).epistemically_accessible)
        a_next = a.local_succ(basis, "B")
        b_next = caught.local_succ(basis, "B")
        # Shared semantics, same hardware and identical recorded probe values
        # give the same subsequent placement although origin labels differ.
        self.assertEqual(a_next.placement(basis), b_next.placement(basis))
        self.assertEqual(a_next.model(basis).compatible, ("B",))
        self.assertNotEqual(a_next.batches[-1].origin, b_next.batches[-1].origin)
        self.assertEqual(b_next.local_frames, 1)

    def test_hardware_difference_does_not_prevent_knowledge_alignment(self):
        basis = chain_basis(3, b_feasible=("p0",))
        a = AgentKnowledge("Alice").advance(basis, "B", 2)
        b = AgentKnowledge("Bob")
        caught = decode_strict_relay(b, encode_strict_relay(a,b,basis), basis)
        self.assertEqual(caught.placement(basis), a.placement(basis))
        self.assertEqual(caught.local_frames, 0)
        self.assertEqual(caught.model(basis).epistemically_accessible,
                         ("p0","p1","p2"))
        self.assertEqual(caught.local_succ(basis, "B"), caught)
        self.assertEqual(a.local_succ(basis, "B").model(basis).compatible, ("B",))
        # Knowledge alignment was NOT an isomorphism of physical capabilities.

    def test_compact_snapshot_redundancy_is_not_causal_replay(self):
        world = FiniteProbeWorld(("A","B"), ("p0","p1"),
                                 (("same","same"),("same","same")))
        rules = (HornRule(("obs:p0:same",), "can:p1"),)
        basis = SharedKnowledgeBasis(world,("can:p0",),rules,
                                     (("Alice",world.probes),("Bob",world.probes)))
        a = AgentKnowledge("Alice").advance(basis,"A",2)
        b = AgentKnowledge("Bob")
        witness = minimal_snapshot_delta(a,b,basis)
        self.assertEqual(witness.full_fact_count, 2)
        self.assertEqual(witness.minimal_fact_count, 1)
        self.assertEqual(witness.facts, (("p0","same"),))
        self.assertFalse(witness.causal_history_certified)
        self.assertFalse(witness.future_equivalence_certified)
        strict = encode_strict_relay(a,b,basis)
        compact = encode_snapshot_relay(a,b,basis)
        self.assertLess(len(compact),len(strict))
        reduced = decode_snapshot_relay(b,compact,basis)
        strong = decode_strict_relay(b,strict,basis)
        self.assertEqual(reduced.placement(basis),strong.placement(basis))
        self.assertNotEqual(reduced.batches,strong.batches)
        self.assertEqual(reduced.observations(),(("p0","same"),))
        self.assertEqual(strong.observations(),(("p0","same"),("p1","same")))
        # A received all p0/p1 outcomes; B's compact snapshot did not.
        # At the next local SUCC, B redundantly probes p1 while A is done.
        self.assertEqual(reduced.local_succ(basis,"A").local_frames,1)
        self.assertEqual(strong.local_succ(basis,"A").local_frames,0)

    def test_source_fiber_alone_is_insufficient_for_operational_placement(self):
        basis = chain_basis(2)
        a = AgentKnowledge("Alice").advance(basis,"A",1)
        b = AgentKnowledge("Bob")
        self.assertEqual(a.model(basis).compatible,b.model(basis).compatible)
        self.assertNotEqual(a.placement(basis),b.placement(basis))
        self.assertEqual(minimal_snapshot_delta(a,b,basis).minimal_fact_count,1)

    def test_true_source_label_never_needed_by_recipient_decoder(self):
        basis=chain_basis(2)
        a=AgentKnowledge("Alice").advance(basis,"B",2)
        b=AgentKnowledge("Bob")
        packet=encode_strict_relay(a,b,basis)
        data=json.loads(packet.decode("utf-8"))
        self.assertNotIn("actual_source",data)
        self.assertNotIn("true_source",data)
        self.assertEqual(decode_strict_relay(b,packet,basis).model(basis).compatible,
                         ("B",))

    def test_stale_prefix_and_cross_basis_wire_are_rejected(self):
        basis=chain_basis(3)
        a=AgentKnowledge("Alice").advance(basis,"B",2)
        b=AgentKnowledge("Bob")
        packet=encode_strict_relay(a,b,basis)
        stale=b.local_succ(basis,"B")
        with self.assertRaises(KnowledgeLadderError):
            decode_strict_relay(stale,packet,basis)
        with self.assertRaises(KnowledgeLadderError):
            encode_strict_relay(a,stale,basis)
        changed=SharedKnowledgeBasis(
            basis.world,basis.axioms,basis.rules,
            (("Alice",basis.world.probes),("Bob",("p0",))),
        )
        with self.assertRaises(KnowledgeLadderError):
            decode_strict_relay(b,packet,changed)

    def test_forged_or_unenabled_sequence_rejected(self):
        basis=chain_basis(3)
        a=AgentKnowledge("Alice").advance(basis,"B",2)
        b=AgentKnowledge("Bob")
        packet=json.loads(encode_strict_relay(a,b,basis).decode())
        for events in [
            [[["p1","same"]]],   # p1 unavailable before p0
            [[["p0","same"],["p1","same"]]],  # p1 cannot be in same causal batch
            [[["p0","wrong"]],[["p1","same"]]],  # contradicts model source
            [[["p0","same"]],[["p0","same"]]],   # repeated actualized probe
            [[["p0","same"]],[["p1","A"]]],      # forged physical outcome
        ]:
            altered=dict(packet,events=events)
            with self.subTest(events=events):
                with self.assertRaises(KnowledgeLadderError):
                    decode_strict_relay(b,json.dumps(altered).encode(),basis)
        broken=dict(packet,end="0"*64)
        with self.assertRaises(KnowledgeLadderError):
            decode_strict_relay(b,json.dumps(broken).encode(),basis)
        with self.assertRaises(KnowledgeLadderError):
            decode_strict_relay(b,b"not json",basis)

    def test_compact_transmission_rejects_unjustified_placement(self):
        basis=chain_basis(3)
        a=AgentKnowledge("Alice").advance(basis,"B",2)
        b=AgentKnowledge("Bob")
        original=json.loads(encode_snapshot_relay(a,b,basis).decode())
        wrong=dict(original,end="BAD")
        with self.assertRaises(KnowledgeLadderError):
            decode_snapshot_relay(b,json.dumps(wrong).encode(),basis)
        false=dict(original,events=[["p2","B"]])
        with self.assertRaises(KnowledgeLadderError):
            decode_snapshot_relay(b,json.dumps(false).encode(),basis)

    def test_attestation_cannot_launder_remote_third_party_events(self):
        basis=chain_basis(3)
        a=AgentKnowledge("Alice").advance(basis,"B",1)
        b=AgentKnowledge("Bob")
        b_received=decode_strict_relay(b,encode_strict_relay(a,b,basis),basis)
        # Alice cannot directly certify a batch observed by Bob to a stale
        # third party which did not share Alice's new recorded basis.
        stale=AgentKnowledge("Bob")
        with self.assertRaises(KnowledgeLadderError):
            encode_strict_relay(b_received,stale,basis)

    def test_compact_relay_cannot_launder_third_party_source_events(self):
        basis = chain_basis(3)
        a = AgentKnowledge("Alice").advance(basis, "B", 1)
        b0 = AgentKnowledge("Bob")
        b = decode_strict_relay(b0, encode_strict_relay(a, b0, basis), basis)
        with self.assertRaises(KnowledgeLadderError):
            minimal_snapshot_delta(b, b0, basis)
        with self.assertRaises(KnowledgeLadderError):
            encode_snapshot_relay(b, b0, basis)
        packet = json.loads(encode_snapshot_relay(a, b0, basis).decode())
        packet["sender"] = "Bob"
        with self.assertRaises(KnowledgeLadderError):
            decode_snapshot_relay(b0, json.dumps(packet).encode(), basis)

    def test_exact_small_world_mutations(self):
        # All 16 binary 2-source × 2-probe tables with both probes initially
        # enabled. Each origin orientation produces one bounded local batch.
        cases=0
        for xs in product(("0","1"),repeat=4):
            world=FiniteProbeWorld(("A","B"),("p","q"),
                                   (tuple(xs[:2]),tuple(xs[2:])))
            basis=SharedKnowledgeBasis(world,("can:p","can:q"),(),
                                       (("Alice",world.probes),("Bob",world.probes)))
            for actual in ("A","B"):
                a=AgentKnowledge("Alice").local_succ(basis,actual)
                b=AgentKnowledge("Bob")
                got=decode_strict_relay(b,encode_strict_relay(a,b,basis),basis)
                self.assertEqual(a.placement(basis),got.placement(basis))
                self.assertEqual(a.observations(),got.observations())
                self.assertEqual(got.local_frames,0)
                self.assertEqual(got.informed_steps,1)
                cases+=1
        self.assertEqual(cases,32)

    def test_invalid_basis_bad_events_and_nonfinite_steps(self):
        b=chain_basis(2)
        with self.assertRaises(KnowledgeLadderError):
            AgentKnowledge("Alice").advance(b,"B",-1)
        with self.assertRaises(KnowledgeLadderError):
            AgentKnowledge("Alice").advance(b,"B",True)
        with self.assertRaises(KnowledgeLadderError):
            ProbeBatch("Alice",(("p0","same"),("p0","same")))
        with self.assertRaises(KnowledgeLadderError):
            ProbeBatch("Alice",())
        with self.assertRaises(KnowledgeLadderError):
            SharedKnowledgeBasis(b.world,b.axioms,b.rules,
                                 (("Alice",b.world.probes),("Alice",b.world.probes)))
        with self.assertRaises(KnowledgeLadderError):
            AgentKnowledge("unregistered").model(b)


if __name__=="__main__":
    unittest.main()
