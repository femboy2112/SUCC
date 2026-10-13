"""Frozen, independently executed positive-carrier Part II receipt."""
import json
from pathlib import Path
import unittest

from scripts.positive_carrier_ii_probe import report


class TestPositiveCarrierIIReceipt(unittest.TestCase):
    def test_receipt_has_not_drifted(self):
        expected = json.loads(Path(
            "research/2026-10-13/POSITIVE_CARRIER_II_RECEIPT.json").read_text())
        actual = json.loads(json.dumps(report()))
        self.assertEqual(actual, expected)
        self.assertEqual(actual["status"], "EXACT_POSITIVE_CARRIER_FIELD_OF_DEFINITION_AND_GHOST_FREEDOM")
        fib = actual["fibonacci_cat_system"]
        self.assertEqual(fib["linear_dimension"], 2)
        self.assertEqual(fib["words_checked_nonnegative"]["negative"], 0)
        self.assertEqual(fib["irrational_contact_certificate"]["verdict"], "FINITE_OBSTRUCTION")
        self.assertEqual(fib["positive_dimension_over_R"], 2)
        self.assertEqual(fib["positive_dimension_over_Q"], "infinity")
        self.assertTrue(fib["real_two_state_carrier_over_Q_sqrt5"]["nonnegative"])
        self.assertFalse(fib["real_two_state_carrier_over_Q_sqrt5"]["all_entries_rational"])
        self.assertEqual(fib["rational_interval_grid_search"]["verdict"], "UNRESOLVED")
        self.assertEqual(actual["dimension_two_dichotomy_positive_control"]["verdict"], "LAWFUL_REALIZATION")
        g = actual["ghost_freedom"]
        self.assertEqual((g["PH1"]["minimal_lawful_states"], g["PH1"]["bottom_completion_lower_bound"]), (1, 5))
        self.assertEqual((g["PH2"]["minimal_lawful_states"], g["PH2"]["bottom_completion_lower_bound"]), (1, 17))
        self.assertTrue(g["PH1_legal_source"]["same_operational_profile"])
        self.assertEqual(g["negative_control_availability_square"]["kind"], "menu_difference")
        b = actual["blind_spot_diagonal_contraction"]
        self.assertEqual(b["reachable_ray_refinement"]["verdict"], "UNRESOLVED")
        self.assertEqual(b["grid_search_verdict"], "LAWFUL_REALIZATION")
        self.assertEqual(b["carrier_dimension"], 3)
        self.assertTrue(all(b["orbit_rays_extreme_in_cone_of_others_and_axis"]))
        self.assertFalse(actual["scope"]["bottom_completion_is_weakest_repair"])
        self.assertTrue(actual["scope"]["cone_theorem_identities_lean_formalized_over_commutative_semiring"])
        self.assertFalse(actual["scope"]["cone_theorem_lean_formalized_over_Q"])
        self.assertFalse(actual["scope"]["main_merge_executed"])


if __name__ == "__main__":
    unittest.main()
