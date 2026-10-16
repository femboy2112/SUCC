from copy import deepcopy
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from observational_succ.formal_instance_bridge import (
    affine_packet, retract_packet, replay_packet, lean_source,
    digest, verify_pins, RUNTIME_PINS, BridgeError,
)


class FormalInstanceBridgeTests(unittest.TestCase):
    def setUp(self):
        self.affine = affine_packet([("S", 1), ("V", 2)], source_id="source", epoch=3)
        self.retract = retract_packet(4, 2, source_id="source", epoch=3)

    def rehash(self, packet):
        packet.pop("digest")
        packet["digest"] = digest(packet)
        return packet

    def test_actual_chronological_parameter_mapping(self):
        self.assertEqual(self.affine["outputs"], {"slope": 2, "offset": 2})
        src, names = lean_source(self.affine)
        self.assertIn("[.shift 1, .scale 2]", src)
        self.assertIn("all_inputs", src)
        self.assertEqual(len(names), 3)
        self.assertFalse(replay_packet(self.affine, source_id="source", epoch=3)["kernel_verification_performed"])

    def test_wrong_composition_with_fresh_hash_rejected(self):
        bad = deepcopy(self.affine)
        bad["outputs"]["offset"] = 1
        with self.assertRaises(BridgeError):
            replay_packet(self.rehash(bad), source_id="source", epoch=3)

    def test_full_cyclic_tables_counting_and_average(self):
        self.assertEqual(self.retract["outputs"]["average"][0], ["1/2", "0"])
        self.assertEqual(self.retract["outputs"]["project"][0], ["1/2", "0", "1/2", "0"])
        src, names = lean_source(self.retract)
        self.assertEqual(len(names), 4)
        self.assertIn("cyclic_average_pull 2 2", src)

    def test_wrong_normalization_with_fresh_hash_rejected(self):
        bad = deepcopy(self.retract)
        bad["outputs"]["average"][0][0] = "1"
        with self.assertRaises(BridgeError):
            replay_packet(self.rehash(bad), source_id="source", epoch=3)

    def test_source_epoch_and_domain_types(self):
        for source, epoch in (("wrong", 3), ("source", 4), ("source", True)):
            with self.assertRaises(BridgeError):
                replay_packet(self.affine, source_id=source, epoch=epoch)
        with self.assertRaises(ValueError):
            affine_packet([("V", 6)], source_id="source", epoch=3)
        with self.assertRaises(ValueError):
            retract_packet(4, 0, source_id="source", epoch=3)

    def test_premises_and_authority_cannot_be_erased(self):
        for key, value in (("source_obligations", []), ("universal_python_correctness", True),
                           ("requested_scope", "UNIVERSAL_PYTHON_PROOF")):
            bad = deepcopy(self.affine)
            bad[key] = value
            with self.assertRaises(BridgeError):
                replay_packet(self.rehash(bad), source_id="source", epoch=3)

    def test_fixed_source_pin_and_no_proof_text_injection(self):
        verify_pins(Path(__file__).resolve().parents[1], RUNTIME_PINS)
        with TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "false.txt").write_text("0=1")
            with self.assertRaises(BridgeError):
                verify_pins(root, {"false.txt": "0"*64})
        packet = affine_packet([], source_id='unsafe\naxiom bad : False', epoch=0)
        self.assertNotIn("axiom bad", lean_source(packet)[0])

    def test_budgets_are_not_mathematical_claims(self):
        with self.assertRaises(BridgeError):
            affine_packet([("S", 0)] * 25, source_id="s", epoch=0)
        with self.assertRaises(BridgeError):
            retract_packet(10, 2, source_id="s", epoch=0)
