"""Replay exact Fraction heldout receipt (no precision-dependent phasors)."""
import subprocess,sys,unittest
from pathlib import Path

class CriticalChirpReceipt(unittest.TestCase):
    def test_preregistered_exact_tail_receipt(self):
        root=Path(__file__).resolve().parents[1]
        folder=root/'research'/'2026-11-04'/'critical_chirp'
        r=subprocess.run([sys.executable,str(folder/'receipt_probe.py'),
                          '--verify',str(folder/'FINITE_RECEIPT.json')],
                         check=True,text=True,capture_output=True,timeout=90)
        self.assertIn('CRITICAL_CHIRP_FRACTION_RECEIPT_VERIFIED',r.stdout)
