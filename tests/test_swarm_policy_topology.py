import unittest
from fractions import Fraction

from observational_succ.swarm_policy_topology import (
    compact_discontinuous_wait, destructive_xor_policy_exists,
    first_zero_wait, policy_topology_receipt,
)


class PolicyTopologyControls(unittest.TestCase):
    def test_constructive_noncompact_family_has_unbounded_lengths(self):
        for bound in (0, 1, 12, 150):
            history = first_zero_wait(bound)
            self.assertGreater(len(history), bound)
            self.assertEqual(history[-1], 0)
            self.assertTrue(all(x == 1 for x in history[:-1]))

    def test_compactness_without_continuous_readouts_is_insufficient(self):
        self.assertEqual(compact_discontinuous_wait(Fraction(0)), (1,))
        for bound in (1, 2, 9, 50):
            history = compact_discontinuous_wait(Fraction(1, bound))
            self.assertGreater(len(history), bound)
            self.assertEqual(history[-1], 1)

    def test_source_classes_fail_closed(self):
        for bad in (True, -1, 1.5):
            with self.assertRaises(ValueError):
                first_zero_wait(bad)
        for bad in (0.0, Fraction(-1), Fraction(2, 3)):
            with self.assertRaises(ValueError):
                compact_discontinuous_wait(bad)

    def test_counterfactual_decision_does_not_supply_reset_free_policy(self):
        self.assertTrue(all(not destructive_xor_policy_exists(depth)
                            for depth in range(7)))
        self.assertFalse(destructive_xor_policy_exists(1, erase=False))
        self.assertTrue(destructive_xor_policy_exists(2, erase=False))

    def test_scope_receipt(self):
        receipt = policy_topology_receipt()
        self.assertFalse(receipt["topological_compactness_verified_by_this_program"])
        self.assertFalse(receipt["infinite_source_or_policy_simulated"])


if __name__ == "__main__":
    unittest.main()
