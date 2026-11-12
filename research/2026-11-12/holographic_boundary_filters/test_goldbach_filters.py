"""Calibrated exact tests; no unbounded arithmetic conclusion."""
from fractions import Fraction as Q
from itertools import product
import unittest

from goldbach_filters import (
    FilterData, certify_zero_mass, circular_sum_count, difference_counts,
    direct_goldbach_count, exact_zero_projector, histogram_data, moment_table,
    moment_matched_ground_twins, prime_grade_data, prime_grade_histogram,
    quadratic_filter, sum_counts,
)


class GoldbachBoundaryFilters(unittest.TestCase):
    def test_three_moments_certify_an_authentic_fiber(self):
        data = prime_grade_data(10, 2)
        self.assertEqual(tuple(lo for lo, _ in data.intervals), (9, 16, 46))
        result = certify_zero_mass(data, quadratic_filter(4))
        self.assertEqual(result.lower_bound, Q(1, 2))
        self.assertTrue(result.proves_positive)
        self.assertEqual(direct_goldbach_count(10), 2)

    def test_one_moment_counterfeit_survives(self):
        actual = prime_grade_data(10, 1)
        fake = histogram_data((0, 2, 7, 0, 0), 1, source_id="no-ground counterfeit")
        self.assertEqual(actual.intervals, fake.intervals)
        self.assertNotEqual(prime_grade_data(10, 2).intervals,
                            histogram_data((0, 2, 7, 0, 0), 2, source_id="fake").intervals)

    def test_exact_finite_interpolation_against_direct_primality(self):
        for n in range(2, 129):
            ceiling = (n * n).bit_length() - 3
            result = certify_zero_mass(prime_grade_data(n, ceiling),
                                       exact_zero_projector(ceiling))
            self.assertEqual(result.lower_bound, direct_goldbach_count(n))

    def test_quadratic_minorant_on_all_small_histograms(self):
        for ceiling in range(1, 5):
            for histogram in product(range(3), repeat=ceiling + 1):
                data = histogram_data(histogram, 2, source_id="enumerated toy")
                result = certify_zero_mass(data, quadratic_filter(ceiling))
                self.assertLessEqual(result.lower_bound, histogram[0])

    def test_binomial_twins_match_all_declared_moments(self):
        for degree in range(13):
            even, odd = moment_matched_ground_twins(degree)
            a = histogram_data(even, degree, source_id="even binomial")
            b = histogram_data(odd, degree, source_id="odd binomial")
            self.assertEqual(a.intervals, b.intervals)
            self.assertEqual((even[0], odd[0]), (1, 0))
            self.assertNotEqual(histogram_data(even, degree + 1, source_id="even").intervals,
                                histogram_data(odd, degree + 1, source_id="odd").intervals)

    def test_response_intervals_pay_the_signed_error(self):
        data = prime_grade_data(10, 2)
        noisy = FilterData(data.table, ((Q(9), Q(9)), (Q(159, 10), Q(161, 10)),
                                       (Q(183, 4), Q(185, 4))), data.source_id)
        result = certify_zero_mass(noisy, quadratic_filter(4))
        self.assertEqual(result.lower_bound, Q(5, 16))

    def test_bad_filter_sign_is_rejected(self):
        with self.assertRaises(ValueError):
            certify_zero_mass(prime_grade_data(10, 2), (1, 0, 0))

    def test_missing_normalization_is_rejected(self):
        with self.assertRaises(ValueError):
            certify_zero_mass(prime_grade_data(10, 2), (2, Q(-5, 2), Q(1, 2)))

    def test_float_and_bool_inputs_are_rejected(self):
        for bad in (1.0, True):
            with self.assertRaises(ValueError):
                certify_zero_mass(prime_grade_data(10, 2), (bad, Q(-5, 4), Q(1, 4)))
            with self.assertRaises(ValueError):
                prime_grade_data(bad, 2)

    def test_malformed_table_and_intervals_are_rejected(self):
        bad = (
            FilterData(((Q(1), Q(1)), (Q(0),)), ((Q(1), Q(1)),) * 2, "fake"),
            FilterData(((Q(1), Q(1)),), ((Q(2), Q(1)),), "fake"),
            FilterData(((Q(1), Q(1)),), ((Q(1), Q(1)),), ""),
            FilterData(((Q(1), Q(1)),), ((Q(1), Q(1)),) * 2, "fake"),
        )
        for data in bad:
            with self.assertRaises(ValueError):
                certify_zero_mass(data, (1,))

    def test_forged_support_ceiling_is_not_source_authentication(self):
        # The verifier cannot infer omitted support from a dishonest header.
        # This negative control exposes the exact external trust boundary.
        actual = prime_grade_data(10, 2)
        forged = FilterData(moment_table(3, 2), actual.intervals, "false ceiling")
        result = certify_zero_mass(forged, quadratic_filter(3))
        self.assertEqual(result.lower_bound, 3)
        self.assertGreater(result.lower_bound, direct_goldbach_count(10))
        self.assertEqual(len(prime_grade_histogram(10)) - 1, 4)

    def test_full_power_spectrum_does_not_determine_sum_coefficient(self):
        x, y = (0, 1, 4), (0, 10, 25)
        a = tuple(i + j for i in x for j in y)
        b = tuple(i + 25 - j for i in x for j in y)
        self.assertEqual(difference_counts(a), difference_counts(b))
        self.assertEqual((min(a), max(a), len(a)), (min(b), max(b), len(b)))
        self.assertEqual((sum_counts(a)[10], sum_counts(b)[10]), (2, 0))

    def test_circle_alias_is_not_ordinary_goldbach(self):
        primes = (2, 3, 5, 7)
        self.assertEqual(sum_counts(primes)[8], 2)
        self.assertEqual(circular_sum_count(primes, 8, 4), 5)
        for target in range(15):
            self.assertEqual(circular_sum_count(primes, target, 15),
                             sum_counts(primes)[target])

    def test_zero_support_and_empty_histogram(self):
        data = histogram_data((7,), 0, source_id="zero grade only")
        self.assertEqual(certify_zero_mass(data, quadratic_filter(0)).lower_bound, 7)
        with self.assertRaises(ValueError):
            histogram_data((), 2, source_id="empty")


if __name__ == "__main__":
    unittest.main()
