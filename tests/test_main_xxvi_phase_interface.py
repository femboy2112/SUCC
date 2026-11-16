"""Calibrated exact checks for the new carry/Gamma interface."""
from fractions import Fraction as F
import importlib.util
from pathlib import Path
import unittest

PATH = Path(__file__).resolve().parents[1] / "scripts/main_xxvi_source_phase_probe.py"
SPEC = importlib.util.spec_from_file_location("main_xxvi_interface", PATH)
probe = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(probe)


class MainXXVIPhaseInterface(unittest.TestCase):
    def test_original_rational_and_growing_crt_agree(self):
        self.assertEqual(probe.carry_prefix(16)[:2], [3, 2])

    def test_phase_orientation_is_calibrated(self):
        report = probe.phase_controls()
        self.assertEqual(report["exact_transport_cases"], 15)
        self.assertTrue(report["orientation_mutant_rejected"])
        self.assertTrue(report["forgotten_winding_mutant_rejected"])

    def test_zero_response_cannot_be_inverted(self):
        with self.assertRaises(ValueError):
            probe.div((F(1),F(0)), (F(0),F(0)))

    def test_erasing_carry_winding_changes_readout(self):
        for c in (1, 2):
            self.assertEqual(probe.decode(probe.zi(c)), 1)
            self.assertEqual(probe.decode(probe.zi(0)), 0)

    def test_source_domain_is_explicit(self):
        with self.assertRaises(ValueError):
            probe.r(0)
        with self.assertRaises(ValueError):
            probe.carry_prefix(0)


if __name__ == "__main__":
    unittest.main()
