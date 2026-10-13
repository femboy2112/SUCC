"""Frozen, independently executed carrier-first scientific source receipt."""
import json
from pathlib import Path
import unittest

from scripts.carrier_indexed_probe import report


class TestCarrierIndexedReceipt(unittest.TestCase):
    def test_cross_python_source_receipt_has_not_drifted(self):
        expected=json.loads(Path(
            "research/2026-10-13/CARRIER_INDEXED_SOURCE_RECEIPT.json").read_text())
        actual=json.loads(json.dumps(report()))
        self.assertEqual(actual,expected)
        self.assertEqual(actual["status"],
                         "EXACT_SOURCE_INDEXED_CARRIER_HISTORY_AND_REPAIR")
        self.assertEqual(actual["actual_history"],
                         [["swap","ok"],["read/erase","right"]])
        self.assertEqual(actual["actual_original_source_support"],
                         ["s2","s3"])
        self.assertEqual(actual["final_original_posterior"],
                         ["0","0","1/2","1/2"])
        self.assertEqual(actual["evidence"],"1/2")
        self.assertTrue(actual["all_prefix_joint_laws_transport"])
        self.assertEqual(actual["one_step_minimal_refined_labels"],[0,1,2,2])
        self.assertEqual(actual["stationary_refinement_labels"],[0,1,2,3])
        self.assertTrue(actual["support_only_lumps_but_law_does_not"])
        self.assertFalse(actual["scope"]["empirically_authenticated_source"])
        self.assertFalse(actual["scope"]["unrestricted_causal_history_sheaf_proved"])
        self.assertFalse(actual["scope"]["completed_Weil_positivity_or_RH_proved"])
        self.assertFalse(actual["scope"]["main_merge_executed"])


if __name__=="__main__":
    unittest.main()
