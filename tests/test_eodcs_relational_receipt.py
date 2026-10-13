"""Frozen exact EODCS III source-relative modal receipt replay."""
import json
from pathlib import Path
import unittest

from scripts.eodcs_relational_probe import receipt


class TestEODCSRelationalReceipt(unittest.TestCase):
    def test_receipt_is_exactly_reproducible_and_source_safe(self):
        expected=json.loads(
            Path("research/2026-10-13/EODCS_RELATIONAL_MODAL_RECEIPT.json").read_text())
        actual=receipt()
        self.assertEqual(actual,expected)
        self.assertEqual(actual["status"],"EXACT_FINITE_EODCS_III_RELATIONAL_SOURCE")
        report=actual["tight_may_common_observation"]
        self.assertEqual(report["may"],["cold","warm"])
        self.assertEqual(report["common_possible"],[])
        self.assertFalse(report["exact_source_support_descends"])
        self.assertEqual(report["event_cold"],"undecided_without_finer_observation")
        self.assertEqual(report["event_all"],"guaranteed_within_declared_support")
        self.assertEqual(report["event_empty"],"impossible_within_declared_support")
        probability=actual["probabilistic_firewall"]
        self.assertEqual(probability["source_law_s0"],
                         [["cold","1/4"],["warm","3/4"]])
        self.assertEqual(probability["source_law_s1"],
                         [["cold","3/4"],["warm","1/4"]])
        self.assertFalse(probability["law_probabilities_identified_by_support"])
        self.assertFalse(probability["empirical_likelihoods_calibrated"])
        self.assertFalse(actual["scope"]["physical_measurement_performed"])
        self.assertFalse(actual["scope"]["RH_or_completed_Weil_positivity_proved"])


if __name__=="__main__":
    unittest.main()
