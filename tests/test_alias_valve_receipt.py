"""Replay AV finite exact-Fraction SHA256 receipt from the pushed code."""
import subprocess
import sys
import unittest
from pathlib import Path


class AliasValveReceipt(unittest.TestCase):
    def test_exact_fraction_receipt_replay(self):
        root=Path(__file__).resolve().parents[1]
        path=root/"research"/"2026-11-04"/"alias_valve"
        r=subprocess.run([sys.executable,str(path/"receipt_probe.py"),
                          "--verify",str(path/"FINITE_RECEIPT.json")],
                         capture_output=True,text=True,timeout=45,check=True)
        self.assertIn("EXACT_FRACTION_VALVE_RECEIPT_VERIFIED",r.stdout)
