"""Replay finite exact Fraction source and Γ rational-window receipts."""
import subprocess,sys,unittest
from pathlib import Path

class GammaPigeonholeReceipt(unittest.TestCase):
    def test_deterministic_exact_fraction_receipt(self):
        root=Path(__file__).resolve().parents[1]
        folder=root/"research"/"2026-11-04"/"gamma_pigeonhole"
        p=subprocess.run([sys.executable,str(folder/"receipt_probe.py"),
                          "--verify",str(folder/"FINITE_RECEIPT.json")],
                         capture_output=True,text=True,check=True,timeout=90)
        self.assertIn("GAMMA_PIGEONHOLE_SOURCE_PIN_RECEIPT_VERIFIED",p.stdout)
