"""Replay the source-native coherent wrong-seed exact Fraction receipt."""
import subprocess
import sys
import unittest
from pathlib import Path

class SourceNativeReceiptReplay(unittest.TestCase):
    def test_replay(self):
        root=Path(__file__).resolve().parents[1]
        folder=root/'research'/'2026-11-04'/'alias_valve'
        result=subprocess.run([sys.executable,str(folder/'source_native_receipt.py'),
                              '--verify',str(folder/'SOURCE_NATIVE_SEED_RECEIPT.json')],
                              capture_output=True,text=True,check=True,timeout=180)
        self.assertIn('SOURCE_NATIVE_SEED_FRACTION_RECEIPT_VERIFIED',result.stdout)
