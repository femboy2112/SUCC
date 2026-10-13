"""Exact persisted adaptive source/no-go execution receipt."""
import json
from pathlib import Path
import unittest
from scripts.voyager_adaptive_probe import receipt


class TestVoyagerAdaptiveReceipt(unittest.TestCase):
    def test_exact_frozen_dual_tail_policy_receipt(self):
        expected=json.loads(Path(
            "research/2026-10-13/VOYAGER_ADAPTIVE_SOURCE_RECEIPT.json").read_text())
        actual=json.loads(json.dumps(receipt()))
        self.assertEqual(actual,expected)
        self.assertEqual(actual["status"],
                         "EXACT_VOYAGER_ADAPTIVE_SOURCE_PAIR_NO_GO")
        p=actual["finite_nonanticipatory_observer"]
        self.assertTrue(p["both_witnesses_replay_same_exact_transcript"])
        self.assertTrue(p["one_stream_eventually_zero"])
        self.assertFalse(p["other_stream_eventually_zero"])
        self.assertTrue(p["terminal_decision_for_both_source_classes_not_possible"])
        self.assertFalse(actual["source_class_boundary"]["physical_instruments_created"])
        self.assertFalse(actual["source_class_boundary"]["RH_or_Weil_positivity_proved"])


if __name__=="__main__":
    unittest.main()
