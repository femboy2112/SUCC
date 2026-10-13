"""Independent X01 enumeration and negative controls."""
import unittest

from scripts.swarm_x01_completion_transport_probe import (
    exhaustive_transport_controls, infinite_family_finite_controls,
    mutation_controls, unary_equivalent,
)


class CompletionTransportTests(unittest.TestCase):
    def test_complete_binary_source_and_map_enumeration(self):
        receipt = exhaustive_transport_controls()
        self.assertEqual(receipt['tables_examined'], 4 ** 6)
        self.assertGreater(receipt['strict_maps'], 0)
        self.assertGreater(receipt['nonsurjective_source_but_surjective_completion'], 0)
        self.assertGreater(receipt['source_bijection_but_noninjective_completion'], 0)

    def test_pair_orbit_detects_delayed_report(self):
        # Prefix length one is equal; an actual future update separates.
        self.assertFalse(unary_equivalent((1, 2, 2), (0, 0, 1), 0, 1))
        self.assertTrue(unary_equivalent((1, 0), (0, 0), 0, 1))

    def test_removed_hypotheses_have_countermodels(self):
        self.assertTrue(all(mutation_controls().values()))

    def test_symbolic_family_finite_obligations(self):
        controls = infinite_family_finite_controls()
        self.assertEqual(controls['patched_patterns'], 511)
        self.assertEqual(controls['ray_coordinate_checks'], 1320)


if __name__ == '__main__':
    unittest.main()
