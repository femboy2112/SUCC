"""Exact finite controls; no numerical fit is used as an asymptotic proof."""
from fractions import Fraction as Q
from itertools import product
from math import isqrt, prod
import unittest

from pointwise_certificates import (
    filtered_response, grade_response, leakage, recover_integer_count,
    tail_certificate, tail_factors, tail_weight, witness_margin,
)


def interpolation_response(grade, degree, t):
    """Independent Lagrange-weight route, distinct from product evaluation."""
    nodes = [t ** r for r in range(1, degree + 1)]
    weights = [prod((-nodes[k] / (nodes[r] - nodes[k])
                     for k in range(degree) if k != r), start=Q(1))
               for r in range(degree)]
    return sum((weight * node ** grade for weight, node in zip(weights, nodes)), Q())


def is_prime(n):
    return n >= 2 and all(n % divisor for divisor in range(2, isqrt(n) + 1))


def omega(n):
    count, divisor = 0, 2
    while divisor * divisor <= n:
        while n % divisor == 0:
            count += 1
            n //= divisor
        divisor += 1
    return count + (n > 1)


def arithmetic_histogram(n):
    histogram = [0]
    for a in range(n - 1):
        h = omega(n - a) + omega(n + a) - 2
        histogram.extend([0] * max(0, h + 1 - len(histogram)))
        histogram[h] += 1
    return histogram


class PointwiseCertificateTests(unittest.TestCase):
    def test_product_matches_independent_interpolation(self):
        for degree, t in product((2, 4, 6), (Q(1, 2), Q(1, 3), Q(2, 5))):
            for grade in (0, 1, degree - 1, degree, degree + 1, 31):
                self.assertEqual(grade_response(grade, degree, t),
                                 interpolation_response(grade, degree, t))

    def test_strict_mass_threshold_is_sharp(self):
        self.assertEqual(leakage(2), Q(1, 8))
        self.assertEqual(witness_margin(8, 2), Q(1, 8))
        self.assertEqual(filtered_response((1, 0, 7), 2), Q(1, 8))
        self.assertEqual(witness_margin(9, 2), 0)
        self.assertEqual(filtered_response((1, 0, 8), 2), 0)
        self.assertLess(filtered_response((1, 0, 9), 2), 0)

    def test_clamping_recovers_when_old_epsilon_mass_budget_equals_one(self):
        histogram = (0, 0, 8)
        value = filtered_response(histogram, 2)
        self.assertEqual(leakage(2) * sum(histogram), 1)
        self.assertEqual(value, -1)
        self.assertEqual(recover_integer_count(value, 8, 2), 0)
        for ground in range(9):
            for grade_one in range(9 - ground):
                hist = (ground, grade_one, 8 - ground - grade_one)
                self.assertEqual(recover_integer_count(filtered_response(hist, 2), 8, 2),
                                 ground)

    def test_noisy_guarantee_pays_both_errors(self):
        genuine = filtered_response((1, 0, 7), 2)
        error = Q(1, 16)
        reported = genuine - error
        self.assertEqual(reported - error, 0)
        self.assertEqual(witness_margin(8, 2, filtered_error=error), 0)
        self.assertGreater(witness_margin(8, 2, filtered_error=Q(1, 32)), 0)

    def test_integrality_is_load_bearing(self):
        histogram = (Q(1, 16), 0, Q(15, 16))
        self.assertGreater(histogram[0], 0)
        self.assertEqual(sum(histogram), 1)
        self.assertGreater(witness_margin(1, 2), 0)
        self.assertEqual(filtered_response(histogram, 2), Q(-7, 128))

    def test_weighted_tail_rescues_the_sharp_failure(self):
        histogram = (1, 0, 8)
        value = filtered_response(histogram, 2)
        extra = tail_weight(histogram, 2)
        cert = tail_certificate((value, value), (extra, extra), 9, 2,
                                tail_mass_upper=8, integral_counts=True)
        self.assertEqual(value, 0)
        self.assertEqual(extra, 2)
        self.assertEqual((cert.lower, cert.upper), (1, 1))
        self.assertTrue(cert.positive)
        self.assertTrue(cert.count_recovered)

    def test_tail_bounds_for_small_histograms_and_far_grade(self):
        for hist in product(range(3), repeat=5):
            value, extra = filtered_response(hist, 2), tail_weight(hist, 2)
            cert = tail_certificate((value, value), (extra, extra), sum(hist), 2,
                                    tail_mass_upper=sum(hist[2:]), integral_counts=True)
            self.assertLessEqual(cert.lower, hist[0])
            self.assertGreaterEqual(cert.upper, hist[0])
        hist = [0] * 1001
        hist[0], hist[-1] = 3, 17
        value, extra = filtered_response(hist, 6), tail_weight(hist, 6)
        cert = tail_certificate((value, value), (extra, extra), 20, 6,
                                integral_counts=True)
        self.assertLessEqual(cert.lower, 3)
        self.assertGreaterEqual(cert.upper, 3)

    def test_tail_factor_lower_endpoint_and_limiting_upper(self):
        for degree in (2, 4, 6):
            t = Q(1, 2)
            lower, upper = tail_factors(degree, t)
            self.assertEqual(-grade_response(degree, degree, t) / t ** degree, lower)
            ratios = [-grade_response(h, degree, t) / t ** h
                      for h in (degree, degree + 1, 20, 100)]
            self.assertEqual(ratios, sorted(ratios))
            self.assertLess(ratios[-1], upper)

    def test_tail_interval_errors_preserve_authentic_count(self):
        histogram = (2, 4, 3, 2, 1, 7)
        value, extra = filtered_response(histogram, 4), tail_weight(histogram, 4)
        cert = tail_certificate((value - Q(1, 20), value + Q(1, 20)),
                                (extra - Q(1, 100), extra + Q(1, 100)),
                                sum(histogram), 4, integral_counts=True)
        self.assertLessEqual(cert.lower, 2)
        self.assertGreaterEqual(cert.upper, 2)

    def test_per_midpoint_degrees_obey_exact_aggregate_budget(self):
        total_count = total_response = total_budget = Q()
        for n in range(2, 66):
            degree = (2, 6, 4)[n % 3]
            histogram = arithmetic_histogram(n)
            count = sum(is_prime(n - a) and is_prime(n + a) for a in range(n - 1))
            self.assertEqual(histogram[0], count)
            value = filtered_response(histogram, degree)
            self.assertLessEqual(value, count)
            self.assertLessEqual(count - value, leakage(degree) * (n - 1))
            total_count += count
            total_response += value
            total_budget += leakage(degree) * (n - 1)
        self.assertLessEqual(total_response, total_count)
        self.assertLessEqual(total_count - total_response, total_budget)

    def test_threshold_failure_is_not_an_arithmetic_counterexample(self):
        histogram = arithmetic_histogram(10)
        self.assertEqual(witness_margin(9, 2), 0)
        self.assertEqual(histogram[0], 2)
        self.assertGreater(filtered_response(histogram, 2), 0)

    def test_chen_shaped_premise_and_positive_mean_do_not_force_each_zero_grade(self):
        no_ground = (0, 2)
        has_ground = (2, 0)
        self.assertEqual(filtered_response(no_ground, 2), 0)
        self.assertGreater(filtered_response(no_ground, 2)
                           + filtered_response(has_ground, 2), 0)
        self.assertEqual(no_ground[0], 0)

    def test_invalid_contracts_are_rejected(self):
        for degree, t in ((3, Q(1, 2)), (True, Q(1, 2)), (2, 0.5), (2, Q(3, 4))):
            with self.assertRaises(ValueError):
                leakage(degree, t)
        for grade in (-1, True, Q(1, 2)):
            with self.assertRaises(ValueError):
                grade_response(grade, 2)
        with self.assertRaises(ValueError):
            witness_margin(True, 2)
        with self.assertRaises(ValueError):
            filtered_response((1, -1), 2)
        with self.assertRaises(ValueError):
            recover_integer_count(0, 9, 2)
        with self.assertRaises(ValueError):
            recover_integer_count(Q(1, 10), 8, 2)
        with self.assertRaises(ValueError):
            tail_certificate((0, 0), (3, 3), 9, 2)
        with self.assertRaises(ValueError):
            tail_certificate((1, 0), (0, 0), 9, 2)
        with self.assertRaises(ValueError):
            tail_certificate((0, 0), (0, 0), 9, 2, integral_counts=1)


if __name__ == "__main__":
    unittest.main()
