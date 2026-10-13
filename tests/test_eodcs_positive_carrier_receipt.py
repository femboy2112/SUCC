"""Frozen, independently executed positive-carrier realization receipt."""
import json
from pathlib import Path
import unittest

from scripts.positive_carrier_probe import report


class TestPositiveCarrierReceipt(unittest.TestCase):
    def test_receipt_has_not_drifted(self):
        expected = json.loads(Path(
            "research/2026-10-13/POSITIVE_CARRIER_RECEIPT.json").read_text())
        actual = json.loads(json.dumps(report()))
        self.assertEqual(actual, expected)
        self.assertEqual(actual["status"], "EXACT_POSITIVE_CARRIER_REALIZATION_BOUNDARY")
        self.assertEqual(actual["calibration"]["rank"], 3)
        self.assertEqual(actual["calibration"]["fooling_set_size"], 4)
        pw1 = actual["path_walk_family"]["PW1"]
        self.assertEqual((pw1["linear_dimension"], pw1["positive_carrier_dimension"]), (3, 4))
        self.assertEqual(pw1["oracle_proposed_3"], "FINITE_OBSTRUCTION")
        self.assertEqual(pw1["oracle_proposed_4"], "LAWFUL_REALIZATION")
        self.assertEqual(actual["rational_clock"]["verdict"], "FINITE_OBSTRUCTION")
        self.assertEqual(actual["rational_clock"]["positive_carrier_dimension"], "infinity")
        self.assertTrue(all(g["im_mod_5"] == 4 for g in actual["rational_clock"]["gaussian_power_imaginary_parts"]))
        fam = {f["k"]: f for f in actual["cyclotomic_clocks"]["family"]}
        self.assertEqual((fam[30]["linear_dimension"], fam[30]["positive_carrier_dimension"]), (9, 30))
        self.assertTrue(all(f["orbit_cone_valid"] and not f["k_minus_1_generators_valid"]
                            and f["peripheral_lower_bound"] == f["k"] for f in fam.values()))
        self.assertTrue(actual["cyclotomic_clocks"]["C6_hankel_block_strictly_positive"])
        sq = actual["availability_square"]
        self.assertTrue(sq["legal_word_probabilities_agree"])
        self.assertEqual(sq["promotion_witness"]["coarse_menu"], ["a", "b"])
        self.assertTrue(sq["illegal_policy_rejected_in_fine"])
        self.assertFalse(actual["scope"]["main_merge_executed"])
        self.assertFalse(actual["scope"]["empirically_authenticated_source"])


if __name__ == "__main__":
    unittest.main()
