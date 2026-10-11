"""Independent finite controls for relative path/value and evolving-basis transport."""
import json
import unittest
from itertools import product

from observational_succ.absorbing_frames import HornRule
from observational_succ.knowledge_ladder import (
    AgentKnowledge, SharedKnowledgeBasis, KnowledgeLadderError,
    encode_strict_relay, encode_snapshot_relay, decode_snapshot_relay,
)
from observational_succ.observer_traps import FiniteProbeWorld
from observational_succ.relative_delta import (
    RelativeDeltaError, DerivedBooleanConcept,
    encode_relative_delta, decode_relative_delta,
    operational_position, certify_finite_continuation,
    probe_option_result, extend_shared_basis,
    encode_concept_upgrade, receive_concept_upgrade,
    frozen_base_minimum_worst_case_bits, relative_delta_demo,
    prove_probe_value, verify_probe_value, ProbeValueProof,
    encode_position_delta, decode_position_delta,
)


def chain(n=3, *, long_names=False, bob_feasible=None):
    p = tuple(("multiword_explicit_empirical_probe_"+str(i)
               if long_names else "p"+str(i)) for i in range(n))
    world = FiniteProbeWorld(
        ("A","B"),p,
        (("same",)*(n-1)+("A",),("same",)*(n-1)+("B",)),
    )
    rules = tuple(HornRule((f"obs:{p[i]}:same",),f"can:{p[i+1]}")
                  for i in range(n-1))
    basis=SharedKnowledgeBasis(
        world,(f"can:{p[0]}",),rules,
        (("Alice",p),("Bob",p if bob_feasible is None else bob_feasible)),
    )
    return basis


class RelativeDeltaTests(unittest.TestCase):
    def test_exact_path_value_delta_no_source_snapshot(self):
        basis = chain(3)
        a = AgentKnowledge("Alice").advance(basis,"B",3)
        b = AgentKnowledge("Bob")
        packet = encode_relative_delta(a,b,basis)
        r = json.loads(packet.decode())
        self.assertEqual(r["kind"],"relative-path-value-v1")
        self.assertEqual(r["steps"],[
            {"path":[0],"values":[None]},
            {"path":[0],"values":[None]},
            {"path":[0],"values":[1]},
        ])
        self.assertNotIn("sources",r)
        self.assertNotIn("world_state",r)
        self.assertNotIn("absolute_probe",r)
        caught = decode_relative_delta(b,packet,basis)
        self.assertEqual(a.batches,caught.batches)
        self.assertEqual(caught.local_frames,0)
        self.assertEqual(caught.informed_steps,1)
        self.assertEqual(operational_position(a,basis),
                         operational_position(caught,basis))
        future=certify_finite_continuation(a,caught,basis)
        self.assertTrue(future.equivalent)
        self.assertEqual(future.sources_checked,("B",))
        self.assertGreater(future.local_transitions_checked,0)

    def test_equality_of_knowledge_probe_access_reasoning_not_just_snapshot(self):
        world=FiniteProbeWorld(("A","B"),("p0","p1"),
                               (("same","same"),("same","same")))
        basis=SharedKnowledgeBasis(
            world,("can:p0",),
            (HornRule(("obs:p0:same",),"can:p1"),),
            (("Alice",world.probes),("Bob",world.probes)),
        )
        a=AgentKnowledge("Alice").advance(basis,"A",2)
        b=AgentKnowledge("Bob")
        snap=decode_snapshot_relay(b,encode_snapshot_relay(a,b,basis),basis)
        self.assertEqual(a.placement(basis),snap.placement(basis))
        self.assertNotEqual(operational_position(a,basis),
                            operational_position(snap,basis))
        self.assertFalse(certify_finite_continuation(a,snap,basis).equivalent)
        strict=decode_relative_delta(b,encode_relative_delta(a,b,basis),basis)
        self.assertTrue(certify_finite_continuation(a,strict,basis).equivalent)

    def test_strong_placement_refuses_inaccessible_hardware_even_when_knowledge_can_transfer(self):
        b=chain(3,bob_feasible=("p0",))
        a=AgentKnowledge("Alice").advance(b,"B",2)
        receiver=AgentKnowledge("Bob")
        # The original weak semantic transport is still possible.
        # Strong relative transport must refuse to call these equal
        # operational placements because their physical access differs.
        from observational_succ.knowledge_ladder import decode_strict_relay
        weak=decode_strict_relay(receiver,encode_strict_relay(a,receiver,b),b)
        self.assertEqual(a.placement(b),weak.placement(b))
        self.assertNotEqual(operational_position(a,b),operational_position(weak,b))
        self.assertFalse(certify_finite_continuation(a,weak,b).equivalent)
        with self.assertRaises(RelativeDeltaError):
            encode_relative_delta(a,receiver,b)

    def test_position_anchored_relay_works_without_same_causal_prefix(self):
        basis=chain(3)
        alice_before=AgentKnowledge("Alice").advance(basis,"B",1)
        bob_before=AgentKnowledge("Bob").advance(basis,"B",1)
        self.assertEqual(operational_position(alice_before,basis),
                         operational_position(bob_before,basis))
        self.assertNotEqual(alice_before.batches,bob_before.batches)
        alice_after=alice_before.advance(basis,"B",2)
        with self.assertRaises(RelativeDeltaError):
            encode_relative_delta(alice_after,bob_before,basis)
        patch=encode_position_delta(alice_before,alice_after,bob_before,basis)
        received=decode_position_delta(bob_before,patch,basis)
        self.assertEqual(operational_position(received,basis),
                         operational_position(alice_after,basis))
        self.assertEqual(received.batches[0].origin,"Bob")
        self.assertEqual([item.origin for item in received.batches[1:]],
                         ["Alice","Alice"])
        self.assertEqual(received.local_frames,1)
        self.assertEqual(received.informed_steps,1)
        self.assertNotEqual(received.batches,alice_after.batches)
        self.assertTrue(certify_finite_continuation(alice_after,received,basis).equivalent)

    def test_state_relative_consecutive_rungs_do_not_overwrite_independent_history(self):
        basis=chain(4)
        a=AgentKnowledge("Alice").advance(basis,"B",1)
        b=AgentKnowledge("Bob").advance(basis,"B",1)
        before=a
        for _ in range(3):
            advanced=before.local_succ(basis,"B")
            packet=encode_position_delta(before,advanced,b,basis)
            b=decode_position_delta(b,packet,basis)
            self.assertEqual(operational_position(advanced,basis),
                             operational_position(b,basis))
            self.assertEqual(b.batches[0].origin,"Bob")
            before=advanced
        self.assertEqual(before.model(basis).compatible,("B",))
        self.assertEqual(b.informed_steps,3)
        self.assertEqual(b.local_frames,1)

    def test_position_delta_rejects_bad_anchor_wrong_basis_and_wrong_sender(self):
        basis=chain(3)
        a=AgentKnowledge("Alice").advance(basis,"B",2)
        receiver=AgentKnowledge("Bob")
        packet=encode_position_delta(AgentKnowledge("Alice"),a,receiver,basis)
        data=json.loads(packet.decode())
        for key,val in [
            ("anchor","0"*64),("basis","BAD"),("source","Bob"),
            ("result","0"*64),
        ]:
            wrong=dict(data)
            wrong[key]=val
            with self.subTest(key=key):
                with self.assertRaises(RelativeDeltaError):
                    decode_position_delta(receiver,json.dumps(wrong).encode(),basis)
        changed=dict(data)
        changed["steps"]=[{"path":[0],"values":[0]}]+data["steps"][1:]
        with self.assertRaises(RelativeDeltaError):
            decode_position_delta(receiver,json.dumps(changed).encode(),basis)
        with self.assertRaises(RelativeDeltaError):
            encode_position_delta(a,AgentKnowledge("Alice"),receiver,basis)
        with self.assertRaises(RelativeDeltaError):
            decode_position_delta(receiver.local_succ(basis,"B"),packet,basis)

    def test_path_delta_composes_abstractly_across_rungs(self):
        b=chain(4)
        a0=AgentKnowledge("Alice")
        r0=AgentKnowledge("Bob")
        a2=a0.advance(b,"B",2)
        r2=decode_relative_delta(r0,encode_relative_delta(a2,r0,b),b)
        a4=a2.advance(b,"B",2)
        r4=decode_relative_delta(r2,encode_relative_delta(a4,r2,b),b)
        direct=decode_relative_delta(r0,encode_relative_delta(a4,r0,b),b)
        self.assertEqual(operational_position(r4,b),operational_position(direct,b))
        self.assertEqual(r4.batches,direct.batches)
        self.assertEqual(r4.informed_steps,2)
        self.assertEqual(direct.informed_steps,1)
        self.assertTrue(certify_finite_continuation(r4,a4,b).equivalent)

    def test_long_probe_names_are_saved_in_event_payload_not_guaranteed_total_bits(self):
        basis=chain(12,long_names=True)
        a=AgentKnowledge("Alice").advance(basis,"B",12)
        receiver=AgentKnowledge("Bob")
        relative=json.loads(encode_relative_delta(a,receiver,basis).decode())
        strict=json.loads(encode_strict_relay(a,receiver,basis).decode())
        self.assertLess(
            len(json.dumps(relative["steps"])),
            len(json.dumps(strict["events"])),
        )
        self.assertNotIn("multiword",json.dumps(relative["steps"]))
        self.assertEqual(
            decode_relative_delta(receiver,json.dumps(relative).encode(),basis).batches,
            a.batches,
        )

    def test_wrong_outcome_malformed_path_replay_stale_basis_fail_closed(self):
        basis=chain(3)
        alice=AgentKnowledge("Alice").advance(basis,"B",3)
        receiver=AgentKnowledge("Bob")
        correct=json.loads(encode_relative_delta(alice,receiver,basis).decode())
        for change in (
            lambda d:d["steps"][0].update(path=[1]),
            lambda d:d["steps"][0].update(values=[0]),
            lambda d:d["steps"][2].update(values=[None]),
            lambda d:d["steps"][2].update(values=[False]),
            lambda d:d["steps"][2].update(values=[4]),
            lambda d:d.update(to_position="0"*64),
            lambda d:d.update(from_="wrong"),
            lambda d:d.update(basis="wrong"),
            lambda d:d.update(sender="Bob"),
        ):
            modified=json.loads(json.dumps(correct))
            change(modified)
            with self.subTest(modification=modified):
                with self.assertRaises(RelativeDeltaError):
                    decode_relative_delta(receiver,json.dumps(modified).encode(),basis)
        stale=receiver.local_succ(basis,"B")
        with self.assertRaises(RelativeDeltaError):
            decode_relative_delta(stale,json.dumps(correct).encode(),basis)
        with self.assertRaises(RelativeDeltaError):
            decode_relative_delta(receiver,b"not-json",basis)

    def test_probe_option_is_not_observation_outcome(self):
        b=chain(2)
        a=AgentKnowledge("Alice")
        unknown=probe_option_result(a,b,"p1")
        self.assertFalse(unknown.is_an_epistemic_option)
        self.assertEqual(unknown.possible_values,("A","B"))
        self.assertFalse(unknown.inferable_without_measuring)
        a=a.local_succ(b,"B")
        enabled=probe_option_result(a,b,"p1")
        self.assertTrue(enabled.is_an_epistemic_option)
        self.assertFalse(enabled.inferable_without_measuring)
        p0=probe_option_result(a,b,"p0")
        self.assertEqual(p0.possible_values,("same",))
        self.assertTrue(p0.inferable_without_measuring)
        self.assertEqual(p0.inferred_value,"same")
        self.assertEqual(a.model(b).compatible,("A","B"))

    def test_proof_shape_can_certify_value_but_option_alone_cannot(self):
        basis=chain(2)
        initial=AgentKnowledge("Alice")
        p0=probe_option_result(initial,basis,"p0")
        p1=probe_option_result(initial,basis,"p1")
        self.assertTrue(p0.is_an_epistemic_option)
        self.assertTrue(p0.inferable_without_measuring)
        self.assertFalse(p1.inferable_without_measuring)
        proof=prove_probe_value(initial,basis,"p0")
        self.assertTrue(verify_probe_value(initial,basis,proof))
        self.assertEqual(proof.value,"same")
        self.assertEqual(initial.observations(),())
        with self.assertRaises(RelativeDeltaError):
            prove_probe_value(initial,basis,"p1")
        from dataclasses import replace
        with self.assertRaises(RelativeDeltaError):
            verify_probe_value(initial,basis,replace(proof,value="wrong"))
        new_frame=initial.local_succ(basis,"B")
        with self.assertRaises(RelativeDeltaError):
            verify_probe_value(new_frame,basis,proof)

    def test_conditional_probe_availability_requires_a_true_observation(self):
        # An option that exists for all models is not source information.
        # A physically checked 'ready' outcome, however, can discriminate.
        world=FiniteProbeWorld(
            ("X","Y"),("ready","fine"),
            (("yes","x"),("no","y")),
        )
        basis=SharedKnowledgeBasis(
            world,("can:ready","can:fine"),(),
            (("Alice",("ready",)),("Bob",("ready",))),
        )
        initial=AgentKnowledge("Alice")
        report=probe_option_result(initial,basis,"ready")
        self.assertTrue(report.is_an_epistemic_option)
        self.assertEqual(report.possible_values,("no","yes"))
        self.assertFalse(report.inferable_without_measuring)
        after=initial.local_succ(basis,"X")
        self.assertEqual(after.observations(),(("ready","yes"),))
        self.assertEqual(after.model(basis).compatible,("X",))
        self.assertTrue(probe_option_result(after,basis,"fine").inferable_without_measuring)
        self.assertNotIn("fine",dict(basis.observers)["Alice"])
        # The inferred fine result is not a fabricated physical measurement.
        self.assertEqual(after.observations(),(("ready","yes"),))

    def test_binary_recipe_is_verified_basis_change_not_extra_empirical_data(self):
        world=FiniteProbeWorld(
            ("00","01","10","11"),("left","right"),
            (("0","0"),("0","1"),("1","0"),("1","1")),
        )
        base=SharedKnowledgeBasis(
            world,("can:left","can:right"),(),
            (("Alice",world.probes),("Bob",world.probes)),
        )
        recipe=DerivedBooleanConcept("parity","xor",("left","right"))
        upgraded=extend_shared_basis(base,recipe)
        self.assertNotEqual(base.fingerprint,upgraded.fingerprint)
        self.assertEqual(upgraded.world.probes,("left","right","parity"))
        self.assertEqual(tuple(row[-1] for row in upgraded.world.outcomes),
                         ("0","1","1","0"))
        self.assertEqual(upgraded.observers,base.observers)
        old=AgentKnowledge("Alice")
        self.assertEqual(old.model(base).compatible,old.model(upgraded).compatible)
        opt=probe_option_result(old,upgraded,"parity")
        self.assertTrue(opt.is_an_epistemic_option)
        self.assertFalse(opt.inferable_without_measuring)
        self.assertNotIn("parity",dict(upgraded.observers)["Alice"])
        msg=encode_concept_upgrade(base,recipe)
        upgraded_receiver=receive_concept_upgrade(base,msg)
        self.assertEqual(upgraded.fingerprint,upgraded_receiver.fingerprint)
        explorer=old.local_succ(upgraded,"10")
        self.assertEqual(explorer.model(upgraded).compatible,("10",))
        self.assertEqual(probe_option_result(explorer,upgraded,"parity").inferred_value,"1")
        observer=AgentKnowledge("Bob")
        delta=encode_relative_delta(explorer,observer,upgraded)
        with self.assertRaises(RelativeDeltaError):
            decode_relative_delta(observer,delta,base)
        caught=decode_relative_delta(observer,delta,upgraded_receiver)
        self.assertTrue(certify_finite_continuation(explorer,caught,upgraded).equivalent)
        self.assertNotIn("parity",tuple(x for x,_ in caught.observations()))

    def test_frozen_base_must_accept_verified_basis_upgrade_before_later_delta(self):
        basis=chain(2)
        # A source-dependent probe availability measurement has an outcome;
        # merely knowing that probe exists in the common language does not.
        p=probe_option_result(AgentKnowledge("Bob"),basis,"p0")
        self.assertTrue(p.is_an_epistemic_option)
        self.assertTrue(p.inferable_without_measuring)
        with self.assertRaises(RelativeDeltaError):
            receive_concept_upgrade(basis,b'{"base":"WRONG","kind":"verified-concept-v1"}')

    def test_forged_invalid_concept_or_stale_upgrade_are_rejected(self):
        world=FiniteProbeWorld(("A","B"),("p","q"),(("0","1"),("1","0")))
        basis=SharedKnowledgeBasis(
            world,("can:p","can:q"),(),
            (("Alice",world.probes),("Bob",world.probes)))
        recipe=DerivedBooleanConcept("xor","xor",("p","q"))
        packet=encode_concept_upgrade(basis,recipe)
        later=receive_concept_upgrade(basis,packet)
        with self.assertRaises(RelativeDeltaError):
            receive_concept_upgrade(later,packet)
        broken=json.loads(packet.decode())
        broken["result"]="0"*64
        with self.assertRaises(RelativeDeltaError):
            receive_concept_upgrade(basis,json.dumps(broken).encode())
        with self.assertRaises(RelativeDeltaError):
            extend_shared_basis(basis,DerivedBooleanConcept("x","xor",("p","bad")))
        with self.assertRaises(RelativeDeltaError):
            extend_shared_basis(basis,DerivedBooleanConcept("p","xor",("p","q")))
        with self.assertRaises(RelativeDeltaError):
            DerivedBooleanConcept("x","random",("p",))

    def test_frozen_base_bit_bound_uses_counting_not_executed_infinity(self):
        self.assertEqual(frozen_base_minimum_worst_case_bits(0),0)
        for n in range(1,10):
            self.assertEqual(frozen_base_minimum_worst_case_bits(n),n)
            self.assertEqual(2**n-1,sum(2**i for i in range(n)))
            self.assertLess(sum(2**i for i in range(n)),2**n)
        with self.assertRaises(RelativeDeltaError):
            frozen_base_minimum_worst_case_bits(-1)
        with self.assertRaises(RelativeDeltaError):
            frozen_base_minimum_worst_case_bits(True)

    def test_independent_small_world_exhaustive_mutations(self):
        cases=0
        for bits in product(("0","1"),repeat=4):
            world=FiniteProbeWorld(("A","B"),("p","q"),
                                   (tuple(bits[:2]),tuple(bits[2:])))
            b=SharedKnowledgeBasis(
                world,("can:p","can:q"),(),
                (("Alice",world.probes),("Bob",world.probes)),
            )
            for actual in world.sources:
                sender=AgentKnowledge("Alice").local_succ(b,actual)
                receiver=AgentKnowledge("Bob")
                caught=decode_relative_delta(
                    receiver,encode_relative_delta(sender,receiver,b),b)
                self.assertEqual(operational_position(sender,b),
                                 operational_position(caught,b))
                self.assertTrue(certify_finite_continuation(sender,caught,b).equivalent)
                cases+=1
        self.assertEqual(cases,32)

    def test_reference_demo(self):
        report=relative_delta_demo()
        self.assertEqual(report["status"],"EXACT_RELATIVE_PATH_VALUE_RELAY")
        self.assertTrue(report["same_knowledge_empirical_access_and_reasoner"])
        self.assertEqual(report["physical_discovery_frames"],3)
        self.assertEqual(report["recipient_knowledge_steps"],1)
        self.assertFalse(report["infinite_communication_claimed"])
        self.assertFalse(report["source_authentication_claimed"])


if __name__=="__main__":
    unittest.main()
