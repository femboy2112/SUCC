"""Assert frozen actual-source/boundary receipt, not invented infinite runs."""
import json
from pathlib import Path
import unittest

from scripts.voyager_observer_probe import receipt


class TestVoyagerReproducibility(unittest.TestCase):
    def test_frozen_source_relative_moonshot_receipt(self):
        expected=json.loads(Path(
            "research/2026-10-13/VOYAGER_OBSERVATIONAL_COMPLETION_RECEIPT.json").read_text())
        actual=json.loads(json.dumps(receipt()))
        self.assertEqual(actual,expected)
        self.assertEqual(actual["status"],
                         "EXACT_VOYAGER_OBSERVATIONAL_COMPLETION_BOUNDARY")
        self.assertEqual(actual["all_eventually_zero_prefix_stage_counts"],
                         [2**h for h in range(11)])
        self.assertTrue(actual["all_finite_stage_restrictions_surjective"])
        for data in actual["observational_memory_debt_by_horizon"]:
            self.assertEqual(data["source_memory_lower_bound"],2**data["k"])
            self.assertEqual(data["required_prefix"],2**(data["k"]+1)+1)
            self.assertGreaterEqual(data["constructed_witness_machine_states"],
                                    data["source_memory_lower_bound"])
        self.assertFalse(actual["eventual_zero_family"][
            "all_one_global_profile_realized_by_eventually_zero_source"])
        self.assertFalse(actual["scope"]["every_profinite_thread_is_original_state"])
        self.assertFalse(actual["scope"]["physical_all_future_executed"])
        self.assertFalse(actual["scope"]["arithmetic_RH_or_Weil_positivity_proved"])


if __name__=="__main__":
    unittest.main()
