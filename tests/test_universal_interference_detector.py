import itertools
import math
import unittest
from fractions import Fraction as Q

from observational_succ.universal_interference_detector import (
    EnergyInterval, completed_lag_benchmark, energy_from_unit_points,
    frequency_tail, frequency_weight, gamma_poisson_weight,
    haar_only_event_miss, mixed_pair_click, original_source_transfer,
    pair_kernel, periodic_alias_report, prefix_energy_interval,
    report_product_chi_squared,
)


def multiply(z, w):
    return z[0] * w[0] - z[1] * w[1], z[0] * w[1] + z[1] * w[0]


def squared_mean(points, h):
    # Independent repeated multiplication; no kernel formula is used.
    values = []
    for z in points:
        w = (Q(1), Q())
        for _ in range(h):
            w = multiply(w, z)
        values.append(w)
    re = sum(z[0] for z in values) / len(values)
    im = sum(z[1] for z in values) / len(values)
    return re * re + im * im


class UniversalInterferenceTests(unittest.TestCase):
    def test_gamma_integral_law_and_exact_tail(self):
        for k in range(32):
            gamma_integral = Q(math.factorial(k), math.factorial(k) * 2 ** (k + 1))
            self.assertEqual(gamma_poisson_weight(k), gamma_integral)
        for h in (0, 1, 2, 7, 19, 41):
            self.assertEqual(sum((frequency_weight(j) for j in range(1, h + 1)), Q())
                             + frequency_tail(h), 1)
            # Independent finite geometric derivative identity; tail of mean.
            partial_mean = sum((j * frequency_weight(j) for j in range(1, h + 1)), Q())
            self.assertEqual(partial_mean + Q(h + 2, 2 ** h), 2)

    def test_closed_kernel_against_chebyshev_series(self):
        for c in (Q(-1), Q(-4, 5), Q(-1, 3), Q(), Q(3, 5), Q(1)):
            old, cur, partial = Q(1), c, Q()
            for h in range(1, 42):
                partial += frequency_weight(h) * cur
                self.assertLessEqual(abs(pair_kernel(c) - partial), frequency_tail(h))
                old, cur = cur, 2 * c * cur - old

    def test_kernel_range_and_click_mutation(self):
        self.assertEqual(pair_kernel(-1), Q(-1, 3))
        self.assertEqual(pair_kernel(0), Q(-1, 5))
        self.assertEqual(pair_kernel(1), 1)
        for numerator in range(-31, 32):
            c = Q(numerator, 31)
            self.assertTrue(-Q(1, 3) <= pair_kernel(c) <= 1)
            self.assertTrue(0 <= mixed_pair_click(c) <= Q(2, 3))
        self.assertNotEqual(mixed_pair_click(0), Q(1, 2))

    def test_exact_locked_and_polygon_controls(self):
        roots = ((Q(1), Q()), (Q(), Q(1)), (Q(-1), Q()), (Q(), Q(-1)))
        self.assertEqual(energy_from_unit_points(roots), Q(1, 15))
        self.assertEqual(energy_from_unit_points(roots[:1]), 1)
        self.assertEqual(energy_from_unit_points((roots[0], roots[2])), Q(1, 3))
        self.assertEqual(energy_from_unit_points((roots[1],) * 17), 1)

    def test_fresh_rational_circle_holdouts(self):
        for size in (11, 13, 17):
            points = tuple((Q(1 - j * j, 1 + j * j), Q(2 * j, 1 + j * j))
                           for j in range(1, size + 1))
            energy = energy_from_unit_points(points)
            moments = tuple(squared_mean(points, h) for h in range(1, 18))
            interval = prefix_energy_interval(moments)
            self.assertLessEqual(interval.lower, energy)
            self.assertLessEqual(energy, interval.upper)
            self.assertEqual(energy_from_unit_points(tuple(reversed(points))), energy)

    def test_global_rotation_and_conjugation_invariance(self):
        points = ((Q(1), Q()), (Q(3, 5), Q(4, 5)), (Q(5, 13), Q(12, 13)))
        turn = (Q(8, 17), Q(15, 17))
        expected = energy_from_unit_points(points)
        self.assertEqual(energy_from_unit_points(tuple(multiply(z, turn) for z in points)), expected)
        self.assertEqual(energy_from_unit_points(tuple((x, -y) for x, y in points)), expected)

    def test_without_replacement_is_a_different_response(self):
        points = ((Q(1), Q()), (Q(-1), Q()))
        correct = energy_from_unit_points(points)
        no_diagonal = pair_kernel(-1)
        self.assertEqual(correct, Q(1, 3))
        self.assertEqual(no_diagonal, Q(-1, 3))
        self.assertNotEqual(correct, no_diagonal)

    def test_prefix_error_and_click_orientation(self):
        self.assertEqual(prefix_energy_interval(()), EnergyInterval(0, 1))
        self.assertEqual(prefix_energy_interval((1,) * 7), EnergyInterval(Q(127, 128), 1))
        interval = prefix_energy_interval((0,) * 13)
        self.assertEqual(interval.upper, Q(1, 8192))
        self.assertEqual(interval.click_interval, (Q(8191, 16384), Q(1, 2)))

    def test_original_green_budget_against_literal_source(self):
        def r(n):
            return Q(4, 8 * n - 7) - Q(2, 8 * n - 4) - Q(1, 8 * n - 3) - Q(1, 8 * n - 2)
        for b in (1, 2, 8, 19, 23, 31, 41):
            tail_mean_upper = sum((r(n + 1) / 15 for n in range(b, 2 * b)), Q()) / b
            cert = original_source_transfer(b)
            self.assertLess(Q(176, 7) * tail_mean_upper, cert.energy_error_upper)
            self.assertEqual(cert.energy_error_upper, 2 * cert.click_error_upper)

    def test_fixed_lag_resonance_and_wrong_product_haar(self):
        self.assertEqual(completed_lag_benchmark((-16, 1)), 1)
        self.assertEqual(completed_lag_benchmark((-256, 0, 1)), 1)
        self.assertEqual(completed_lag_benchmark((-1, 1)), 0)
        self.assertEqual(completed_lag_benchmark((1,)), 0)
        self.assertEqual(completed_lag_benchmark((0,)), 1)
        # Independent source identity on holdout clocks.
        states = [Q()]
        for n in range(1, 45):
            r = Q(4, 8*n-7)-Q(2, 8*n-4)-Q(1, 8*n-3)-Q(1, 8*n-2)
            states.append(16 * states[-1] + r)
        for n in range(19, 42):
            r = Q(4, 8*(n+1)-7)-Q(2, 8*(n+1)-4)-Q(1, 8*(n+1)-3)-Q(1, 8*(n+1)-2)
            self.assertEqual(states[n+1] - 16 * states[n], r)

    def test_periodic_alias_frequency_census(self):
        for period in (1, 3, 5, 9, 15, 25):
            report = periodic_alias_report(period)
            prefix = sum((frequency_weight(h) for h in range(1, 65) if h % period == 0), Q())
            self.assertTrue(prefix <= report.energy <= prefix + frequency_tail(64))
            self.assertEqual(report.click_rate, (1 - report.energy) / 2)

    def test_chi_squared_from_declared_two_cell_laws(self):
        for period in (1, 3, 5, 11, 13, 17):
            eps = periodic_alias_report(period).energy
            # Coarse frequency label: resonant/nonresonant, then click.
            null = (eps/2, eps/2, (1-eps)/2, (1-eps)/2)
            alt = (eps, Q(), (1-eps)/2, (1-eps)/2)
            chi = sum(((p-q)**2/q for p, q in zip(alt, null) if q), Q())
            report = periodic_alias_report(period)
            self.assertEqual(chi, report.labelled_chi_squared)
            p0, p1 = (1+eps)/2, (1-eps)/2
            forgotten = 2*(p0-Q(1, 2))**2 + 2*(p1-Q(1, 2))**2
            self.assertEqual(forgotten, report.unlabelled_chi_squared)

    def test_product_law_by_exact_event_tree(self):
        for period in (1, 3, 5):
            eps = periodic_alias_report(period).energy
            p = ((1+eps)/2, (1-eps)/2)
            for count in range(5):
                chi = Q()
                for bits in itertools.product((0, 1), repeat=count):
                    alt = math.prod(p[x] for x in bits)
                    null = Q(1, 2**count)
                    chi += (alt-null)**2/null
                self.assertEqual(chi, report_product_chi_squared(period, count, retain_frequency=False))

    def test_alias_budget_and_one_sided_detector(self):
        for period in (1, 3, 5, 11, 13, 17):
            report = periodic_alias_report(period)
            self.assertEqual(report.unlabelled_trials_strict_lower / report.labelled_trials_strict_lower,
                             1 / report.energy)
            self.assertEqual(haar_only_event_miss(period, 0), 1)
            self.assertEqual(haar_only_event_miss(period, 1), 1-report.energy/2)
            self.assertLess(haar_only_event_miss(period, 7), haar_only_event_miss(period, 3))

    def test_invalid_domains_and_finite_budgets(self):
        for value in (True, 0.5, -1, 4097):
            with self.assertRaises(ValueError): frequency_tail(value)
        for points in ((), ((0, 0),), ((1.0, 0),), ((True, 0),), ((1, 0),)*65):
            with self.assertRaises(ValueError): energy_from_unit_points(points)
        for values in ((Q(-1, 2),), (Q(3, 2),), (0.0,), (True,)):
            with self.assertRaises(ValueError): prefix_energy_interval(values)
        with self.assertRaises(ValueError): pair_kernel(Q(2))
        with self.assertRaises(ValueError): EnergyInterval(1, 0)
        with self.assertRaises(ValueError): report_product_chi_squared(3, 1, retain_frequency=1)
        with self.assertRaises(ValueError): report_product_chi_squared(3, 257, retain_frequency=True)
        with self.assertRaises(ValueError): original_source_transfer(0)


if __name__ == '__main__':
    unittest.main()
