"""Exact hostile controls for differential observation and mixed characters."""
from fractions import Fraction as Q
import unittest

from scripts.twisted_observer_joining_oracle import (
    differential, forcing_direct, grid_law, joining_receipt,
    source_receipt, source_trajectory, trajectory_law,
)


class TwistedObserverJoiningTests(unittest.TestCase):
    def test_complete_marginal_and_difference_histories_hide_sum(self):
        result = joining_receipt(31, 7)
        self.assertEqual(result["product_sum_history_count"], 31)
        self.assertEqual(result["antidiagonal_sum_history_count"], 1)
        self.assertEqual(result["exact_character_exponent_laws_checked"], 49)

    def test_distinct_prime_holdout_and_swap(self):
        q = 17
        product, anti = grid_law(q, "product"), grid_law(q, "antidiagonal")
        swapped = {(y, x): mass for (x, y), mass in anti.items()}
        self.assertEqual(swapped, anti)
        self.assertEqual(trajectory_law(product, q, 1, -1, 5),
                         trajectory_law(anti, q, 1, -1, 5))
        self.assertNotEqual(trajectory_law(product, q, 1, 1, 5),
                            trajectory_law(anti, q, 1, 1, 5))

    def test_source_values_against_hand_computed_fraction_controls(self):
        self.assertEqual(forcing_direct(1), Q(47, 15))
        self.assertEqual(forcing_direct(2), Q(106, 819))
        self.assertEqual(source_trajectory(Q(0), 2), (Q(0), Q(2, 15), Q(1076, 4095)))

    def test_same_source_differential_and_changed_common_signal(self):
        result = source_receipt(48)
        self.assertEqual(result["common_signal_shift_values"], ["1/7", "2/7", "4/7"])
        self.assertTrue(result["forcing_mutation_detected"])
        self.assertFalse(result["authentic_initial_zero_preserved_for_all_four_wires"])

    def test_nonconstant_differential_and_failed_forcing_mutation(self):
        a, b, delta = Q(0), Q(2, 13), Q(1, 7)
        horizon = 12
        expected = tuple(16 ** n * delta % 1 for n in range(horizon + 1))
        for initial in (a, b):
            left = source_trajectory(initial, horizon)
            right = source_trajectory(initial + delta, horizon)
            self.assertEqual(differential(left, right), expected)
        bad = source_trajectory(b + delta, horizon, impulse=(4, Q(1, 11)))
        self.assertNotEqual(differential(source_trajectory(b, horizon), bad), expected)

    def test_invalid_domains_fail_closed(self):
        for q in (True, 2, 9, 15, 31.0):
            with self.assertRaises(ValueError):
                grid_law(q, "product")
        with self.assertRaises(ValueError):
            source_trajectory(0.0, 4)
        with self.assertRaises(ValueError):
            differential((Q(0),), ())


if __name__ == "__main__":
    unittest.main()
