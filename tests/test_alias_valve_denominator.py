"""Exact finite tests for the original BBP AV-07 denominator escape ceiling."""
import importlib.util
import sys
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
FOLDER=ROOT/"research"/"2026-11-04"/"alias_valve"
sys.path.insert(0,str(FOLDER))
spec=importlib.util.spec_from_file_location("denominator_exit",FOLDER/"denominator_exit.py")
d=importlib.util.module_from_spec(spec)
spec.loader.exec_module(d)


class SourceDenominatorExit(unittest.TestCase):
    def test_original_source_divisibility(self):
        for A in (2,4,8,12,24,40):
            x=d.verify_original_epoch(A,4)
            self.assertGreaterEqual(x["envelope_bits"],x["source_conductor_bits"])
            self.assertGreaterEqual(x["guaranteed_depth"],1)

    def test_epoch_bounds(self):
        for A in (8,12,24):
            x=d.verify_original_epoch(A,8)
            self.assertGreaterEqual(16**x["guaranteed_depth"]*8,d.envelope(A))

    def test_invalid_epoch(self):
        with self.assertRaises(ValueError): d.envelope(0)
        with self.assertRaises(ValueError): d.envelope(-1)
