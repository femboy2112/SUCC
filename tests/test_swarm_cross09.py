"""Independent exact checks of X09 bounds and donor boundary identities."""
import itertools
import unittest
from fractions import Fraction as Q
from math import comb

from observational_succ.swarm_arithmetic import gamma_cutoff_recurrence, mahler_prefix_ambiguity
from observational_succ.swarm_cross09 import (
    alternating_coefficient_lower_bound, alternating_data,
    binomial_polynomial_value, coefficient_prefix_enclosure,
    gamma_product_cutoff, interpolate, pairwise_difference_bound,
    polynomial_value, quarter_periodic_multiplier,
)


class AnalyticActualizationTests(unittest.TestCase):
    def test_rational_lagrange_phantom_and_diverging_required_bound(self):
        for count in range(2, 13):
            data = alternating_data(count)
            coefficients = interpolate(data)
            self.assertEqual(tuple(polynomial_value(coefficients, x) for x, _ in data),
                             tuple(y for _, y in data))
            self.assertGreaterEqual(max(map(abs, coefficients)),
                                    alternating_coefficient_lower_bound(count))
            # Predicted lower bound is necessary from the final adjacent pair.
            x, y = data[-2][0], data[-1][0]
            self.assertEqual(pairwise_difference_bound(
                alternating_coefficient_lower_bound(count), x, y), 2)

    def test_geometric_positive_control_saturates_tail_bound(self):
        for size in (0, 1, 2, 5, 20):
            for x in (Q(0), Q(1, 3), Q(1, 2), Q(9, 10)):
                low, high = coefficient_prefix_enclosure((Q(1),) * size, 1, x)
                self.assertEqual(high, 1 / (1 - x))
                self.assertLessEqual(low, high)
        # Negative x and sign-alternating coefficients saturate the same bound.
        for size in (0, 1, 8):
            x = Q(-2, 3)
            self.assertEqual(coefficient_prefix_enclosure(
                tuple(Q((-1) ** n) for n in range(size)), 1, x)[1], 3)

    def test_bound_covers_independent_tail_cube_enumeration(self):
        prefix = (Q(1, 2), Q(-1), Q(0))
        for x in (Q(-3, 4), Q(0), Q(2, 3)):
            low, high = coefficient_prefix_enclosure(prefix, 1, x)
            for tail in itertools.product((-1, 1), repeat=7):
                value = sum(a * x ** k for k, a in enumerate(prefix + tail))
                self.assertLessEqual(low, value)
                self.assertLessEqual(value, high)

    def test_pairwise_sharp_bound_and_joint_source_control(self):
        for x, y in ((Q(0), Q(1, 2)), (Q(1, 3), Q(1, 2))):
            bound = pairwise_difference_bound(1, x, y)
            for coefficients in itertools.product((-1, 1), repeat=7):
                diff = sum(a * (x ** n - y ** n) for n, a in enumerate(coefficients))
                self.assertLessEqual(abs(diff), bound)
            self.assertEqual(abs(1 / (1 - x) - 1 / (1 - y)), bound)
        # Each report separately fits the source class, but no common source fits both.
        for x, target in ((Q(0), Q(1)), (Q(1, 2), Q(-1))):
            lo, hi = coefficient_prefix_enclosure((), 1, x)
            self.assertLessEqual(lo, target)
            self.assertLessEqual(target, hi)
        self.assertGreater(2, pairwise_difference_bound(1, Q(0), Q(1, 2)))

    def test_gamma_independent_product_audit_and_cutoff_mutation(self):
        for cutoff in (2, 4, 19, 101):
            for z in (1, 3, 7, 13):
                ratio = gamma_product_cutoff(cutoff, z + 1) / gamma_product_cutoff(cutoff, z)
                donor = gamma_cutoff_recurrence(cutoff, z)
                self.assertEqual(ratio, donor['ratio'])
                self.assertEqual(z - ratio, Q(z * (z + 1), cutoff + z + 1))
                self.assertNotEqual(ratio, z)

    def test_gamma_periodic_gauge_survives_positive_integer_reports(self):
        for n in range(-12, 17):
            self.assertEqual(quarter_periodic_multiplier(n), quarter_periodic_multiplier(n + 4))
            self.assertGreater(quarter_periodic_multiplier(n), 0)
            if n % 4 == 0:
                self.assertEqual(quarter_periodic_multiplier(n), 1)
        self.assertEqual(quarter_periodic_multiplier(1), Q(3, 2))

    def test_mahler_polynomial_and_spike_independent_audit(self):
        for horizon in (0, 2, 8, 25):
            degree = horizon + 1
            for x in range(horizon + 1):
                self.assertEqual(binomial_polynomial_value(x, degree), 0)
            self.assertEqual(binomial_polynomial_value(degree, degree), 1)
            self.assertEqual(binomial_polynomial_value(degree + 3, degree), comb(degree + 3, degree))
            for prime in (2, 3, 5):
                donor = mahler_prefix_ambiguity(horizon, prime)
                self.assertGreater(donor['discontinuous_spike_first'], horizon)
                self.assertEqual(donor['discontinuous_spike_first'],
                                 prime ** donor['discontinuous_spike_exponent'])

    def test_domain_mutations_rejected(self):
        for args in (((2,), 1, Q(1, 2)), ((), -1, 0), ((), 1, 1), ((), 1, 0.5)):
            with self.assertRaises(ValueError):
                coefficient_prefix_enclosure(*args)
        for data in ((), ((0, 1), (0, 2))):
            with self.assertRaises(ValueError):
                interpolate(data)
        with self.assertRaises(ValueError):
            pairwise_difference_bound(1, Q(-1, 2), 0)
        with self.assertRaises(ValueError):
            gamma_product_cutoff(True, 1)


if __name__ == '__main__':
    unittest.main()
