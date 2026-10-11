"""Exact finite controls for absorbing models, probe feasibility and finite reports."""
import json
import unittest
from dataclasses import replace

from observational_succ.observer_traps import FiniteProbeWorld
from observational_succ.absorbing_frames import (
    AbsorptionError, HornRule, least_horn_closure,
    AbsorbingProtocol, AbsorbingFrame, target_values,
    transmit_frame, receive_frame, absorbing_demo,
    minimal_target_witness, transmit_target_witness, receive_target_witness,
)


def setup_world(feasible=("coarse", "fine")):
    world = FiniteProbeWorld(
        ("A", "B"), ("coarse", "fine"),
        (("same", "A"), ("same", "B")),
    )
    return AbsorbingProtocol(
        world, ("can:coarse",),
        (HornRule(("obs:coarse:same",), "can:fine"),),
        feasible,
    )


class AbsorbingFramesTests(unittest.TestCase):
    def test_closure_is_monotone_and_idempotent(self):
        rules = (
            HornRule(("a",), "b"),
            HornRule(("b",), "c"),
            HornRule(("a", "c"), "d"),
        )
        one = least_horn_closure(("a",), rules)
        self.assertEqual(one.atoms, ("a", "b", "c", "d"))
        self.assertEqual(one.added_rounds, (("b",), ("c",), ("d",)))
        again = least_horn_closure(one.atoms, rules)
        self.assertEqual(again.atoms, one.atoms)
        self.assertEqual(again.added_rounds, ())
        self.assertTrue(one.stationary)
        more = least_horn_closure(("a", "extra"), rules)
        self.assertTrue(set(one.atoms).issubset(more.atoms))
        with self.assertRaises(AbsorptionError):
            HornRule(("a",), "obs:coarse:fake")
        with self.assertRaises(AbsorptionError):
            HornRule(("a",), "predict:coarse:fake")

    def test_noncontradictory_observation_unlocks_new_epistemic_probe(self):
        protocol = setup_world()
        start = AbsorbingFrame()
        before = start.absorb(protocol)
        self.assertEqual(before.compatible, ("A", "B"))
        self.assertEqual(before.epistemically_accessible, ("coarse",))
        self.assertEqual(before.predicted, (("coarse", "same"),))
        self.assertEqual(before.observed, ())
        self.assertIn("predict:coarse:same", before.closure.atoms)
        self.assertNotIn("obs:coarse:same", before.closure.atoms)
        first = start.succ(protocol, "B")
        first_model = first.absorb(protocol)
        self.assertEqual(first.observations, (("coarse", "same"),))
        self.assertEqual(first_model.compatible, ("A", "B"))
        self.assertEqual(first_model.epistemically_accessible, ("coarse", "fine"))
        self.assertIn("obs:coarse:same", first_model.closure.atoms)
        self.assertFalse(first_model.identified)
        second = first.succ(protocol, "B")
        self.assertEqual(second.observations[-1], ("fine", "B"))
        self.assertEqual(second.absorb(protocol).compatible, ("B",))
        self.assertTrue(second.quiescent(protocol))
        self.assertEqual(second.hard_succ(protocol, "B"), second)

    def test_model_is_full_version_space_not_preferred_candidate(self):
        protocol = setup_world()
        frame = AbsorbingFrame().succ(protocol, "B")
        model = frame.absorb(protocol)
        self.assertEqual(model.compatible, ("A", "B"))
        self.assertEqual(target_values(model, {"A":"same","B":"same"}), ("same",))
        self.assertEqual(target_values(model, {"A":"A","B":"B"}), ("A", "B"))
        self.assertNotIn("fine", tuple(p for p, _ in frame.observations))
        # No preferred "A" hypothesis can have been contradicted: no single
        # candidate was promoted to an actual claim in the first place.

    def test_epistemic_access_can_be_separated_from_physical_feasibility(self):
        protocol = setup_world(("coarse",))
        frame = AbsorbingFrame().hard_succ(protocol, "B")
        model = frame.absorb(protocol)
        self.assertEqual(frame.observations, (("coarse", "same"),))
        self.assertEqual(frame.blocked_attempts, ("fine",))
        self.assertEqual(model.epistemically_accessible, ("coarse", "fine"))
        self.assertEqual(model.physically_accessible, ("coarse",))
        self.assertEqual(model.physically_blocked, ("fine",))
        self.assertEqual(model.compatible, ("A", "B"))
        self.assertTrue(frame.quiescent(protocol))
        self.assertFalse(model.identified)
        with self.assertRaises(AbsorptionError):
            transmit_frame(frame, protocol, {"A": "A", "B": "B"})

        # Yet a specific target can still be completed and transmitted.
        packet = transmit_frame(frame, protocol, {"A": "COMMON", "B": "COMMON"})
        rebuilt, answer = receive_frame(packet, protocol, {"A": "COMMON", "B": "COMMON"})
        self.assertEqual(answer, "COMMON")
        self.assertEqual(rebuilt.absorb(protocol).compatible, ("A", "B"))

    def test_chain_of_positive_probe_discoveries(self):
        world = FiniteProbeWorld(
            ("A", "B", "C"), ("coarse", "fine", "deep"),
            (("same", "1", "a"), ("same", "1", "b"), ("same", "2", "c")),
        )
        rules = (
            HornRule(("obs:coarse:same",), "can:fine"),
            HornRule(("obs:fine:1",), "can:deep"),
        )
        protocol = AbsorbingProtocol(world, ("can:coarse",), rules, world.probes)
        frame = AbsorbingFrame()
        for expected in ((("coarse", "same"),), (("coarse", "same"), ("fine", "1")),
                         (("coarse", "same"), ("fine", "1"), ("deep", "b"))):
            frame = frame.succ(protocol, "B")
            self.assertEqual(frame.observations, expected)
        self.assertEqual(frame.absorb(protocol).compatible, ("B",))
        self.assertEqual(frame.hard_succ(protocol, "B"), frame)
        # Physical failure on exactly the final probe preserves A/B ambiguity.
        cut = AbsorbingProtocol(world, ("can:coarse",), rules, ("coarse", "fine"))
        blocked = AbsorbingFrame().hard_succ(cut, "B")
        self.assertEqual(blocked.absorb(cut).compatible, ("A", "B"))
        self.assertEqual(blocked.blocked_attempts, ("deep",))

    def test_finite_source_target_transmission_is_decoded_and_rechecked(self):
        protocol = setup_world()
        frame = AbsorbingFrame().hard_succ(protocol, "B")
        self.assertTrue(frame.quiescent(protocol))
        packet = transmit_frame(frame, protocol, {"A":"A", "B":"B"})
        self.assertIs(type(packet), bytes)
        self.assertLess(len(packet), 1024)
        rebuilt, answer = receive_frame(packet, protocol, {"A":"A", "B":"B"})
        self.assertEqual(answer, "B")
        self.assertEqual(rebuilt.observations, frame.observations)
        payload = json.loads(packet.decode("utf-8"))
        payload["target"] = "A"
        altered = json.dumps(payload).encode("utf-8")
        with self.assertRaises(AbsorptionError):
            receive_frame(altered, protocol, {"A":"A", "B":"B"})
        payload["target"] = "B"
        payload["observed"] = [["coarse", "same"]]
        with self.assertRaises(AbsorptionError):
            receive_frame(json.dumps(payload).encode("utf-8"), protocol,
                          {"A":"A", "B":"B"})

    def test_channel_is_not_a_physical_authentication_oracle(self):
        protocol = setup_world()
        # A malicious sender CAN fabricate data consistent with source B
        # even if the actual world were A. The receiver needs a genuinely
        # trusted measurement channel; syntax and model consistency alone
        # cannot prove the event actually happened.
        forged = AbsorbingFrame().hard_succ(protocol, "B")
        claimed = transmit_frame(forged, protocol, {"A":"A","B":"B"})
        decoded, result = receive_frame(claimed, protocol, {"A":"A","B":"B"})
        self.assertEqual(result, "B")
        self.assertEqual(decoded.absorb(protocol).compatible, ("B",))
        # This deliberately demonstrates lack of physical truth authentication.

    def test_false_model_class_requires_repair_not_excluded_middle_denial(self):
        protocol = setup_world()
        inconsistent = AbsorbingFrame((("coarse", "impossible"),))
        with self.assertRaises(AbsorptionError):
            inconsistent.absorb(protocol)
        with self.assertRaises(AbsorptionError):
            AbsorbingFrame((("fine", "B"), ("fine", "A")))
        with self.assertRaises(AbsorptionError):
            AbsorbingFrame((("fine", "B"),), ("fine",))
        with self.assertRaises(AbsorptionError):
            AbsorbingFrame((("fine", "B"),)).absorb(setup_world(("coarse",)))

    def test_protocol_refuses_fake_probe_knowledge_and_invalid_rules(self):
        world = setup_world().world
        with self.assertRaises(AbsorptionError):
            AbsorbingProtocol(world, ("obs:coarse:same",), (), world.probes)
        with self.assertRaises(AbsorptionError):
            AbsorbingProtocol(world, ("can:coarse",),
                              (HornRule(("obs:coarse:invented",), "can:fine"),),
                              world.probes)
        with self.assertRaises(AbsorptionError):
            AbsorbingProtocol(world, ("can:coarse",),
                              (HornRule(("obs:coarse:same",), "can:teleport"),),
                              world.probes)
        with self.assertRaises(AbsorptionError):
            AbsorbingProtocol(world, ("can:coarse",), (), ("teleport",))

    def test_bounded_finite_exhaustion_and_causal_no_rewriting(self):
        protocol = setup_world()
        step1 = AbsorbingFrame().succ(protocol, "B")
        alternative = step1.succ(protocol, "A")
        self.assertEqual(alternative.observations[0], step1.observations[0])
        self.assertEqual(alternative.observations[1], ("fine", "A"))
        self.assertTrue(alternative.absorb(protocol).identified)
        # The result's source label is NOT cryptographically authenticated;
        # only the existing recorded coarse outcome is checked. A can still
        # give a compatible coarse trace. There is deliberately no hidden
        # memory of the true source inside AbsorbingFrame itself.

    def test_minimal_target_witness_is_exact_and_does_not_claim_full_history(self):
        protocol = setup_world()
        full = AbsorbingFrame().hard_succ(protocol, "B")
        full_packet = transmit_frame(full, protocol, {"A": "A", "B": "B"})
        witness = minimal_target_witness(full, protocol, {"A": "A", "B": "B"})
        self.assertEqual(witness.observations, (("fine", "B"),))
        self.assertEqual(witness.minimal_probe_count, 1)
        self.assertEqual(witness.full_observation_count, 2)
        packet = transmit_target_witness(witness)
        self.assertLess(len(packet), len(full_packet))
        self.assertEqual(receive_target_witness(packet, protocol,
                                                {"A": "A", "B": "B"}), "B")
        body = json.loads(packet.decode("utf-8"))
        self.assertEqual(body["scope"], "target-only")
        self.assertTrue(witness.requires_independent_measurement_authentication)
        # This shorter witness cannot reproduce the lawful fine-probe unlock:
        # the missing coarse observation was the enablement cause.
        with self.assertRaises(AbsorptionError):
            transmit_frame(AbsorbingFrame((("fine", "B"),)), protocol,
                           {"A": "A", "B": "B"})
        with self.assertRaises(AbsorptionError):
            receive_frame(
                json.dumps({
                    "protocol": "obs-succ-absorbing-v1", "observed": [["fine", "B"]],
                    "blocked": [], "target": "B",
                }).encode("utf-8"),
                protocol, {"A": "A", "B": "B"})

    def test_optimal_target_witness_can_use_zero_observations(self):
        protocol = setup_world(("coarse",))
        full = AbsorbingFrame().hard_succ(protocol, "B")
        shared_target = {"A": "common", "B": "common"}
        witness = minimal_target_witness(full, protocol, shared_target)
        self.assertEqual(witness.minimal_probe_count, 0)
        self.assertEqual(witness.observations, ())
        self.assertEqual(receive_target_witness(
            transmit_target_witness(witness), protocol, shared_target), "common")
        # A zero-outcome target certificate is not a claim of knowing which
        # of the two compatible sources is actual.

    def test_self_supporting_observation_is_not_an_access_certificate(self):
        # An observation cannot be allowed to bootstrap its own enabling
        # instrument through circular post hoc use of the closure rules.
        world = FiniteProbeWorld(
            ("A", "B"), ("fine",), (("A",), ("B",))
        )
        cyclic = AbsorbingProtocol(
            world, (), (HornRule(("obs:fine:B",), "can:fine"),), ("fine",),
        )
        fake_history = AbsorbingFrame((("fine", "B"),))
        self.assertTrue(fake_history.absorb(cyclic).identified)
        self.assertTrue(fake_history.quiescent(cyclic))
        with self.assertRaises(AbsorptionError):
            transmit_frame(fake_history, cyclic, {"A": "A", "B": "B"})
        self.assertEqual(AbsorbingFrame().hard_succ(cyclic, "B"),
                         AbsorbingFrame())
        # Merely fitting the final truth isn't a lawful causal observation.

    def test_witness_rejection_of_false_or_mutated_target(self):
        protocol = setup_world()
        full = AbsorbingFrame().hard_succ(protocol, "B")
        w = minimal_target_witness(full, protocol, {"A": "A", "B": "B"})
        d = json.loads(transmit_target_witness(w).decode("utf-8"))
        d["target"] = "A"
        with self.assertRaises(AbsorptionError):
            receive_target_witness(json.dumps(d).encode(), protocol,
                                   {"A": "A", "B": "B"})
        d["target"] = "B"
        d["scope"] = "full-source-replay"
        with self.assertRaises(AbsorptionError):
            receive_target_witness(json.dumps(d).encode(), protocol,
                                   {"A": "A", "B": "B"})

    def test_demo_reports_both_access_boundaries(self):
        result = absorbing_demo()
        self.assertEqual(result["status"], "FINITE_ABSORBING_HARD_SUCC_CERTIFIED")
        self.assertTrue(result["full_hard_succ_identified"])
        self.assertEqual(result["blocked_epistemically_known"], ["fine"])
        self.assertEqual(result["physical_barrier_remaining_candidates"], ["A", "B"])
        self.assertEqual(result["receiver_reconstructed_target"], "B")
        self.assertFalse(result["authenticated_real_world_source"])
        self.assertFalse(result["infinite_physical_process_executed"])
        self.assertFalse(result["classical_LEM_refuted"])


if __name__ == "__main__":
    unittest.main()
