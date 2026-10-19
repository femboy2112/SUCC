"""Exact and adversarial checks for the factorial/clock transfer map."""
import random
import unittest
from fractions import Fraction

from observational_succ.clock_factorial_duality import (
    cumulative_incidence_inverse, incidence_mobius, inverse_floor_sum, lcm_clock,
    prime_weight_response, primitive_increment,
    response_kernel, row_conditioning, single_site_response,
    weighted_factorial_clock, weighted_unit_clock, valuation_at,
)


class ClockFactorialDualityTests(unittest.TestCase):
    def test_independent_exact_superclock_oracles(self):
        for n in range(1, 121):
            exact = lcm_clock(n)
            self.assertEqual(weighted_factorial_clock(n), exact, n)
            self.assertEqual(weighted_unit_clock(n), exact, n)

    def test_divisor_incidence_is_exact_inverse(self):
        mu = incidence_mobius(120)
        for n in range(1, 121):
            self.assertEqual(sum(mu[d] for d in range(1, n + 1) if n % d == 0), int(n == 1), n)

    def test_period_ratios_and_negative_controls(self):
        self.assertEqual([primitive_increment(n) for n in range(1, 13)],
                         [1, 2, 3, 2, 5, 1, 7, 2, 3, 1, 11, 1])
        self.assertEqual(primitive_increment(6), 1)  # Fake composite impulse rejected
        self.assertEqual(primitive_increment(8), 2)  # Prime-power depth retained
        self.assertNotEqual(lcm_clock(6) * 6, weighted_factorial_clock(6))

    def test_row_sum_but_unbounded_worst_case_norm(self):
        for n in range(1, 121):
            row = row_conditioning(n)
            self.assertEqual(row['coefficient_sum'], 1, n)
            self.assertGreaterEqual(row['linf_operator_norm'], (n + 1) // 2)
        self.assertEqual(row_conditioning(24)['linf_operator_norm'], 23)

    def test_single_spike_green_kernel_and_direct_convolution(self):
        for n in range(2, 90):
            for m in {1, 2, max(1, n // 3), n}:
                basis = [0] * n
                basis[m - 1] = 1
                self.assertEqual(cumulative_incidence_inverse(basis),
                                 single_site_response(n, m), (n, m))
                self.assertEqual(response_kernel(n)[m - 1], single_site_response(n, m))

    def test_global_prime_weight_mutation_is_coherent(self):
        for n in (2, 3, 5, 8, 12, 24, 64, 90):
            for p in (2, 3, 5, 7):
                self.assertEqual(*prime_weight_response(n, p))
        self.assertEqual(valuation_at(4, 2), 2 * valuation_at(2, 2))
        # Single-site injection at n=2 violates log(ab) additivity at 4.
        local_delta = {2: 1}
        self.assertNotEqual(local_delta.get(4, 0), 2 * local_delta.get(2, 0))
        with self.assertRaises(ValueError):
            valuation_at(12, 6)

    def test_hostile_mutated_mobius_and_sign(self):
        mu = list(incidence_mobius(24))
        self.assertEqual(mu[6], 1)
        mu[6] = 0
        self.assertNotEqual(weighted_factorial_clock(12, mu), lcm_clock(12))
        self.assertNotEqual(weighted_unit_clock(12, mu), lcm_clock(12))
        mu = list(incidence_mobius(12))
        mu[2] = 1
        self.assertNotEqual(weighted_factorial_clock(6, mu), lcm_clock(6))

    def test_generic_positive_input_does_not_remain_positive(self):
        # h(n)=[n>=2] is pointwise nonnegative and nondecreasing.
        # Floor-sum inversion (not unit-weight inversion!) has M(floor(6/2))=-1.
        self.assertEqual(inverse_floor_sum([int(i >= 2) for i in range(1, 7)]), -1)

    def test_random_integer_inputs_direct_against_green_kernel(self):
        rng = random.Random(20261017)
        for n in (4, 9, 16, 35, 63):
            kernel = response_kernel(n)
            for _ in range(40):
                values = [rng.randrange(-5, 6) for _ in range(n)]
                self.assertEqual(cumulative_incidence_inverse(values),
                                 sum(x * a for x, a in zip(values, kernel)))

    def test_kernel_gram_is_source_blind(self):
        n = 24
        kernel = response_kernel(n)
        source_blind_gram_trace = sum(k * k for k in kernel)
        counterfeit = [0] * n
        counterfeit[5] = 1  # Fake unit-readout impulse at composite 6.
        self.assertNotEqual(sum(k * v for k, v in zip(kernel, counterfeit)), 0)
        self.assertEqual(source_blind_gram_trace,
                         sum(k * k for k in response_kernel(n)))

    def test_source_type_boundaries(self):
        for bad in (0, -1, 2.5, True, 513):
            with self.assertRaises(ValueError):
                lcm_clock(bad)
        with self.assertRaises(ValueError):
            single_site_response(8, 9)
        with self.assertRaises(ValueError):
            weighted_unit_clock(8, [0, 1])


if __name__ == '__main__':
    unittest.main()
