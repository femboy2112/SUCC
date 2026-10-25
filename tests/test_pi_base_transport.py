"""Coupling validity, boundary budgets, and controls for base-transfer probes."""
import itertools
import unittest
from fractions import Fraction as Q

from observational_succ.pi_base_transport import (
    cantor_two_digit_sample, circular_distance, multiplication_coupling,
    outward_decimal, sorted_multiplication_coupling,
    source_successor_transport_bound, source_to_pi_coupling_budget,
)
from observational_succ.pi_source_collision import bbp_states, tail_upper


class BaseTransportTests(unittest.TestCase):
    def test_uniform_grid_and_non_coprime_control(self):
        values = [Q(j, 17) for j in range(17)]
        for q in (2, 3, 5, 7, 11, 13, 16):
            coupling = sorted_multiplication_coupling(values, q)
            self.assertEqual(coupling.cost, 0)
        collapsed = sorted_multiplication_coupling(values, 17)
        self.assertEqual(collapsed.cost, Q(72, 289))
        self.assertEqual(collapsed.observable_lower_bound, collapsed.cost)

    def test_same_index_does_not_test_invariance(self):
        values = [Q(j, 17) for j in range(17)]
        same = multiplication_coupling(values, 3, tuple(range(17)))
        self.assertEqual(same.cost, Q(72, 289))
        self.assertEqual(sorted_multiplication_coupling(values, 3).cost, 0)

    def test_cantor_control_has_exact_nonzero_tripling_defect(self):
        for depth in range(1, 8):
            values = cantor_two_digit_sample(depth)
            coupling = sorted_multiplication_coupling(values, 3)
            predicted = (1 - Q(1, 16**depth))/15
            self.assertEqual(coupling.cost, predicted)
            self.assertEqual(coupling.observable_lower_bound, predicted)

    def test_every_permutation_satisfies_lipschitz_lower_bound(self):
        values = [Q(0), Q(1, 9), Q(4, 9), Q(8, 9)]
        for q in (3, 5, 16):
            for permutation in itertools.permutations(range(4)):
                coupling = multiplication_coupling(values, q, permutation)
                manual = sum((min(abs((q*values[i]) % 1 - values[j]),
                                  1 - abs((q*values[i]) % 1 - values[j]))
                              for i, j in enumerate(permutation)), Q(0))/4
                self.assertEqual(coupling.cost, manual)
                self.assertLessEqual(coupling.observable_lower_bound, manual)

    def test_duplicates_wrap_and_negative_input(self):
        values = [Q(0), Q(0), Q(-1, 11), Q(10, 11), Q(1, 2)]
        coupling = sorted_multiplication_coupling(values, 3)
        self.assertEqual(sorted(coupling.permutation), list(range(5)))
        self.assertEqual(circular_distance(Q(99, 100), Q(1, 100)), Q(1, 50))

    def test_automatic_source_successor_bound(self):
        states = bbp_states(80)
        for start, length in ((1, 1), (1, 9), (13, 27), (41, 40)):
            values = states[start:start+length]
            permutation = tuple(range(1, length)) + (0,)
            coupling = multiplication_coupling(values, 16, permutation)
            self.assertLessEqual(coupling.cost,
                                 source_successor_transport_bound(start, length))

    def test_shadow_budget_preserves_coupling_and_wrap(self):
        # Arbitrary independently chosen displacements within the rigorous
        # tail envelope validate the finite transport inequality itself.
        states = bbp_states(36)
        start, length = 9, 28
        values = states[start:start+length]
        shadow = [(x + (Q(1, 2) if i % 2 else Q(3, 4))*tail_upper(start+i)) % 1
                  for i, x in enumerate(values)]
        for q in (3, 5, 13, 16):
            before = sorted_multiplication_coupling(values, q)
            after = multiplication_coupling(shadow, q, before.permutation)
            budget = source_to_pi_coupling_budget(start, length, q)
            self.assertLessEqual(abs(after.cost-before.cost), budget)

    def test_invalid_or_non_bijective_matching_rejected(self):
        for permutation in ((0, 0), (0,), (0, 2), (False, 1)):
            with self.assertRaises(ValueError):
                multiplication_coupling([Q(0), Q(1, 3)], 3, permutation)
        for values, q in (([], 3), ([0.1], 3), ([0], 0), ([0], True)):
            with self.assertRaises(ValueError):
                sorted_multiplication_coupling(values, q)

    def test_decimal_enclosures_include_negative_values(self):
        for value in (Q(1, 3), Q(-1, 3), Q(1, 8), Q(0)):
            lo, hi = outward_decimal(value, 6)
            self.assertLessEqual(lo, value)
            self.assertGreaterEqual(hi, value)
            self.assertLessEqual(hi-lo, Q(1, 10**6))
        self.assertEqual(outward_decimal(Q(1, 8), 3), (Q(1, 8), Q(1, 8)))


if __name__ == "__main__":
    unittest.main()
