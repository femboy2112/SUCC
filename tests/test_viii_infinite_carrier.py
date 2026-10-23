"""Exact independent finite checks supporting the infinite-carrier proofs."""

from fractions import Fraction
from itertools import product
import unittest

from observational_succ.viii_infinite_carrier import (
    InfiniteCarrierError, dyadic_energy_coefficients, dyadic_one_mode_mass,
    dyadic_partial_partition, dyadic_partition_enclosure, dyadic_tail_mass,
    dyadic_weight, finite_energy_coefficients, finite_partition,
    geometric_cylinder_probability, linear_budget_tail_bound, linear_energy_coefficients,
    linear_energy_tail_bound, linear_partition_enclosure, linear_tail_mass,
    linear_total_variation_bound,
)


class InfiniteCarrierTests(unittest.TestCase):
    def test_projective_consistency_with_exact_geometric_remainder(self):
        for q in (Fraction(1, 3), Fraction(2, 3)):
            prefix = geometric_cylinder_probability(q, (1, 3), (2, 1))
            for next_weight in (1, 2, 5):
                for cutoff in (0, 2, 7):
                    partial = sum(geometric_cylinder_probability(q, (1, 3, next_weight), (2, 1, n)) for n in range(cutoff + 1))
                    remainder = prefix * q ** (next_weight * (cutoff + 1))
                    self.assertEqual(partial + remainder, prefix)

    def test_finite_spectrum_coefficients_against_occupation_enumeration(self):
        for weights in ((1, 2, 4), (2, 2, 3), (1, 1, 1), ()):
            budget = 8
            census = [0] * (budget + 1)
            for occupations in product(*(range(budget // w + 1) for w in weights)):
                energy = sum(w * n for w, n in zip(weights, occupations))
                if energy <= budget:
                    census[energy] += 1
            self.assertEqual(finite_energy_coefficients(weights, budget), tuple(census))

    def test_linear_partition_calibration(self):
        self.assertEqual(linear_energy_coefficients(10), (1, 1, 2, 3, 5, 7, 11, 15, 22, 30, 42))
        self.assertEqual(sum(linear_energy_coefficients(5)), 19)
        # Independent Euler recurrence n*p(n)=sum_{k=1}^n sigma_1(k)*p(n-k).
        partition = linear_energy_coefficients(30)
        for n in range(1, 31):
            rhs = sum(sum(d for d in range(1, k + 1) if k % d == 0) * partition[n - k] for k in range(1, n + 1))
            self.assertEqual(n * partition[n], rhs)

    def test_linear_tail_and_partition_enclosures(self):
        for q, J in ((Fraction(1, 2), 4), (Fraction(2, 3), 7), (Fraction(1, 4), 1)):
            low, high = linear_partition_enclosure(q, J)
            larger = finite_partition(q, range(1, J + 13))
            self.assertLessEqual(low, larger)
            self.assertLessEqual(larger, high)
            finite_tail_prob = 1 - 1 / finite_partition(q, range(J + 1, J + 13))
            self.assertLessEqual(finite_tail_prob, linear_total_variation_bound(q, J))
            self.assertEqual(linear_tail_mass(q, J), sum(q**j for j in range(J + 1, J + 13)) + linear_tail_mass(q, J + 12))
            energy_partial = sum(j * q**j / (1 - q**j) for j in range(J + 1, J + 13))
            self.assertLessEqual(energy_partial, linear_energy_tail_bound(q, J))
        self.assertEqual(linear_total_variation_bound(Fraction(3, 4), 0), 1)
        with self.assertRaisesRegex(InfiniteCarrierError, "increase the cutoff"):
            linear_partition_enclosure(Fraction(3, 4), 1)

    def test_dyadic_complete_block_formulas(self):
        for K in range(7):
            weights = tuple(dyadic_weight(j) for j in range(1, 2**K))
            for q in (Fraction(1, 4), Fraction(1, 2), Fraction(2, 3)):
                self.assertEqual(dyadic_one_mode_mass(q, K), sum(q**w for w in weights))
                self.assertEqual(dyadic_partial_partition(q, K), finite_partition(q, weights))
            self.assertEqual(dyadic_one_mode_mass(Fraction(1, 2), K), Fraction(K, 2))
            self.assertGreaterEqual(dyadic_partial_partition(Fraction(1, 2), K), 1 + Fraction(K, 2))

    def test_energy_cutoff_is_separate_from_mode_cutoff(self):
        q, r, J = Fraction(1, 2), Fraction(2, 3), 8
        weights = tuple(range(1, J + 1))
        normalizer = finite_partition(q, weights)
        previous = Fraction(1)
        for budget in (3, 8, 20, 40):
            coefficients = finite_energy_coefficients(weights, budget)
            exact_finite_tail = 1 - sum(count * q**energy for energy, count in enumerate(coefficients)) / normalizer
            bound = linear_budget_tail_bound(q, r, budget, J)
            self.assertLessEqual(exact_finite_tail, bound)
            self.assertLessEqual(bound, previous)
            previous = bound
        with self.assertRaises(InfiniteCarrierError):
            linear_budget_tail_bound(q, q, 10, J)

    def test_dyadic_phase_boundary_and_finite_support_firewall(self):
        # Consistent cylinders exist on the full product even at criticality;
        # they do not establish a Gibbs probability on finite-support states.
        self.assertGreater(geometric_cylinder_probability(Fraction(1, 2), (1, 2, 2), (0, 0, 0)), 0)
        for q in (Fraction(1, 2), Fraction(2, 3)):
            with self.assertRaisesRegex(InfiniteCarrierError, "divergent"):
                dyadic_partition_enclosure(q, 3)
            with self.assertRaisesRegex(InfiniteCarrierError, "divergent"):
                dyadic_tail_mass(q, 3)
        q, K = Fraction(1, 4), 3
        low, high = dyadic_partition_enclosure(q, K)
        larger = dyadic_partial_partition(q, K + 3)
        self.assertLessEqual(low, larger)
        self.assertLessEqual(larger, high)
        self.assertEqual(dyadic_tail_mass(q, K), dyadic_one_mode_mass(q, K + 3) - dyadic_one_mode_mass(q, K) + dyadic_tail_mass(q, K + 3))

    def test_grouped_dyadic_counts_against_individual_modes(self):
        for budget in range(9):
            weights = [dyadic_weight(j) for j in range(1, 2**budget)]
            self.assertEqual(dyadic_energy_coefficients(budget), finite_energy_coefficients(weights, budget))
        self.assertEqual(dyadic_energy_coefficients(0), (1,))
        # Finite each time, even though the critical Gibbs partition diverges.
        self.assertEqual(dyadic_energy_coefficients(3), (1, 1, 3, 7))

    def test_invalid_exact_inputs_do_not_claim_certificates(self):
        for q in (True, 0.5, 0, 1, -1, Fraction(3, 2)):
            with self.assertRaises(InfiniteCarrierError):
                linear_partition_enclosure(q, 4)
        for bad in (True, 2.0, Fraction(2), -1):
            with self.assertRaises(InfiniteCarrierError):
                linear_energy_coefficients(bad)
        for weights in ((0,), (True,), (Fraction(1),), (1.0,)):
            with self.assertRaises(InfiniteCarrierError):
                finite_partition(Fraction(1, 2), weights)
        with self.assertRaises(InfiniteCarrierError):
            geometric_cylinder_probability(Fraction(1, 2), (1,), ())
        with self.assertRaises(InfiniteCarrierError):
            geometric_cylinder_probability(Fraction(1, 2), (1,), (True,))
        with self.assertRaises(InfiniteCarrierError):
            dyadic_weight(0)


if __name__ == "__main__":
    unittest.main()
