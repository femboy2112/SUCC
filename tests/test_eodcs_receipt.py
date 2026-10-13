"""Deterministic science-receipt guard; test the actual exporter."""
import unittest

from scripts.eodcs_probe import receipt


class TestEODCSReceipt(unittest.TestCase):
    def test_exact_source_firewalls_and_live_obstructions(self):
        r = receipt()
        self.assertEqual(r["status"], "EXACT_FINITE_EODCS_CONDITIONAL_SOURCE")
        self.assertEqual(r["poset_quotient_and_adjunction"]["verified_hom_set_pairs"], 6)
        c = r["obstruction_trivializing_cover"]["parity_triangle"]
        self.assertEqual(c["minimal_connected_trivializing_cover_degree"], 2)
        self.assertEqual(c["minimal_cover_vertices"], 6)
        self.assertEqual(c["minimal_cover_arcs"], 6)
        self.assertEqual(r["dependent_uncertain_observations"][
            "robust_posterior_interval"], ["2/3", "1"])
        self.assertEqual(r["blinded_8_to_4_source"]["seed_count"], 20)
        b = r["blinded_8_to_4_source"]
        self.assertEqual(b["genetic_successes"]+
                         b["genetic_failures_rescued_by_exact_oracle"], 20)
        self.assertTrue(b["all_sources_exhaustively_certified"])
        self.assertFalse(r["scope"]["Lean_kernel_checked"])
        self.assertFalse(r["scope"]["completed_Weil_form_positivity_or_RH_proved"])
        self.assertFalse(r["scope"]["physical_source_authenticated"])


if __name__ == "__main__":
    unittest.main()
