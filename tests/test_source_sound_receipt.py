"""Replay exact research receipts and reject mutated artifacts."""
import sys
import unittest
from pathlib import Path
P=Path(__file__).resolve().parents[1]/'research'/'2026-11-04'/'source_sound_calculus'
sys.path.insert(0,str(P))
import receipt_probe

class SourceSoundReceipt(unittest.TestCase):
    def test_stored_exact_receipt(self):
        self.assertEqual((P/'FINITE_RECEIPT.json').read_text(),receipt_probe.content())
        self.assertEqual(receipt_probe.value()['pi_base16_normality'],'OPEN')
    def test_mutant_digest_rejected(self):
        x=receipt_probe.content()
        self.assertNotEqual(x.replace('OPEN','PROVED',1),x)
        self.assertNotEqual(x.replace('24,','25,',1),x)
