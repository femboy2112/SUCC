"""Replay the exact deterministic round-II source/proof boundary receipt."""
import unittest

from scripts.eodcs_causal_probe import receipt


class TestEODCSCausalReceipt(unittest.TestCase):
    def test_source_witnesses_no_laundered_search_and_scope(self):
        r=receipt()
        self.assertEqual(r["status"],
                         "EXACT_FINITE_EODCS_II_CAUSAL_AND_PROBE_RECEIPT")
        causal=r["source_changing_square"]
        self.assertEqual(causal["one_step_source_obstruction"]["pair"],
                         ["00","01"])
        self.assertFalse(causal["one_step_source_obstruction"]["one_step_v_exists"])
        self.assertEqual(causal["one_step_source_obstruction"]["minimum_new_binary_bits"],1)
        self.assertTrue(causal["second_step_observational_identity"])
        nerode=r["finite_observer_stabilization"]
        self.assertEqual(nerode["source_relative_stabilization_horizon"],6)
        self.assertEqual(nerode["Nerode_class_counts"],[2,3,4,5,6,7,8])
        greedy=r["greedy_not_global_minimum"]
        self.assertEqual(greedy["greedy_cost"],6)
        self.assertEqual(greedy["exact_cost"],4)
        self.assertEqual(greedy["greedy_offsets"],[0,1,2])
        self.assertEqual(greedy["independently_exhaustive_offsets"],[0,2])
        birth=r["composite_probe_birth"]
        self.assertEqual(birth["synthesized_minimum_word"],["A","B"])
        self.assertTrue(r["closed_toolkit_darkness"][
            "all_finite_words_unable_to_separate"])
        rotated=r["curvature_rotated_by_new_instrument"]
        self.assertEqual(rotated["previously_dark_state_now_delayed"],
                         [["x",["C"]]])
        genetic=r["genetic_probe_language"]
        self.assertTrue(genetic["tight_budget_genetic_failed"])
        self.assertTrue(genetic["tight_budget_exact_oracle_rescued"])
        self.assertEqual(genetic["twenty_seeded_genetic_successes"]+
                         genetic["twenty_seeded_genetic_failures"],20)
        self.assertTrue(genetic["dark_source_finite_grammar_empty"])
        self.assertFalse(any(v for k,v in r["scope"].items()
                             if k!="finite_complete_declared_source"))


if __name__=="__main__":
    unittest.main()
