"""Positive history stationarity, signed cancellation, and degeneracy controls."""
import unittest
from fractions import Fraction as Q

from observational_succ.source_history_stationarity import (
    PositiveHistoryMixture, apply_history_filter,
    finite_stationarity_kernel_certificate, multiplication_pushforward,
    probability_measure, stationarity_certificate, total_variation_distance,
)


def periodic_cycle_count(modulus, multiplier):
    """Independent functional-graph count, including noninvertible maps."""
    seen = set()
    cycles = 0
    for start in range(modulus):
        if start in seen:
            continue
        path = set()
        current = start
        while current not in seen and current not in path:
            path.add(current)
            current = multiplier * current % modulus
        cycles += current in path
        seen.update(path)
    return cycles


class HistoryStationarityDomains(unittest.TestCase):
    def test_positive_nontrivial_probability_is_required(self):
        for bad in ((), (1,), (1, 0), (Q(1, 2), Q(1, 3)),
                    (0, 1, 1, -1), (0, 1.0), (0, True)):
            with self.subTest(bad=bad), self.assertRaises(ValueError):
                PositiveHistoryMixture(bad)
        mixture = PositiveHistoryMixture((Q(1, 4), 0, Q(3, 4), 0))
        self.assertEqual(mixture.weights, (Q(1, 4), 0, Q(3, 4)))
        self.assertEqual(mixture.support_gcd, 2)

    def test_exact_measure_and_operator_domains(self):
        for bad in ((), (Q(1, 2),), (2, -1), (0.5, 0.5), (True, 0)):
            with self.subTest(bad=bad), self.assertRaises(ValueError):
                probability_measure(bad)
        for bad in (0, -1, True, 3.0):
            with self.subTest(bad=bad), self.assertRaises(ValueError):
                multiplication_pushforward((1, 0, 0), bad)
        for bad in ((), (1.0,), (True,)):
            with self.subTest(bad=bad), self.assertRaises(ValueError):
                apply_history_filter((1, 0), 3, bad)
        with self.assertRaises(ValueError):
            total_variation_distance((1, 0), (1, 0, 0))
        with self.assertRaises(ValueError):
            stationarity_certificate((1, 0), 3, (0, 1))


class PositiveHistoryStationarity(unittest.TestCase):
    def test_all_measure_kernels_match_independent_periodic_cycles(self):
        mixtures = (
            PositiveHistoryMixture((Q(1, 2), Q(1, 2))),
            PositiveHistoryMixture((0, Q(1, 3), Q(2, 3))),
            PositiveHistoryMixture((0, 0, Q(1, 2), 0, Q(1, 2))),
            PositiveHistoryMixture((Q(1, 3), 0, 0, Q(2, 3))),
            PositiveHistoryMixture((0, 0, Q(1, 2), Q(1, 2))),
        )
        checks = 0
        for modulus in (1, 3, 4, 5, 6, 7, 8, 9, 10, 13, 16, 19, 25):
            for mixture in mixtures:
                certificate = finite_stationarity_kernel_certificate(
                    modulus, 3, mixture)
                self.assertTrue(certificate.kernels_equal)
                cycles = periodic_cycle_count(
                    modulus, pow(3, mixture.support_gcd, modulus))
                self.assertEqual(modulus - certificate.mixture_rank, cycles)
                checks += 1
        self.assertEqual(checks, 65)

    def test_support_gcd_is_necessary_even_with_radix_invariance(self):
        # Tripling cycle: 1/5 -> 3/5 -> 4/5 -> 2/5 -> 1/5.
        measure = (0, Q(3, 8), Q(1, 8), Q(1, 8), Q(3, 8))
        self.assertEqual(multiplication_pushforward(measure, 16), measure)
        self.assertNotEqual(multiplication_pushforward(measure, 3), measure)
        self.assertEqual(multiplication_pushforward(measure, 9), measure)
        certificate = stationarity_certificate(
            measure, 3, PositiveHistoryMixture((0, 0, Q(1, 2), 0, Q(1, 2))))
        self.assertEqual(certificate.support_gcd, 2)
        self.assertTrue(certificate.mixture_stationary)
        self.assertTrue(certificate.gcd_stationary)
        self.assertTrue(certificate.equivalence_holds)

    def test_nonstationary_and_stationary_measures_are_both_detected(self):
        mixture = PositiveHistoryMixture((0, Q(1, 3), Q(2, 3)))
        for measure, expected in (((0, 1, 0, 0, 0), False),
                                  ((0, Q(1, 4), Q(1, 4), Q(1, 4), Q(1, 4)), True)):
            certificate = stationarity_certificate(measure, 3, mixture)
            self.assertEqual(certificate.mixture_stationary, expected)
            self.assertEqual(certificate.gcd_stationary, expected)
            self.assertTrue(certificate.equivalence_holds)

    def test_noninvertible_and_singleton_carriers(self):
        mixture = PositiveHistoryMixture((0, 0, 1))
        certificate = stationarity_certificate((0, 0, 1), 3, mixture)
        self.assertEqual(certificate.gcd_image, (1, 0, 0))
        self.assertEqual(certificate.gcd_defect, 1)
        self.assertTrue(certificate.equivalence_holds)
        singleton = stationarity_certificate((1,), 3, mixture)
        self.assertTrue(singleton.mixture_stationary)
        self.assertTrue(singleton.gcd_stationary)


class FailureControls(unittest.TestCase):
    def test_signed_history_cancellation_fakes_gcd_one_stationarity(self):
        # The output is positive; that does not make the signed weights positive.
        measure = (0, Q(3, 8), Q(1, 8), Q(1, 8), Q(3, 8))
        self.assertEqual(multiplication_pushforward(measure, 16), measure)
        self.assertEqual(apply_history_filter(measure, 3, (0, 1, 1, -1)), measure)
        self.assertEqual(total_variation_distance(
            measure, multiplication_pushforward(measure, 3)), Q(1, 2))
        with self.assertRaises(ValueError):
            PositiveHistoryMixture((0, 1, 1, -1))

    def test_vanishing_nonidentity_weight_loses_uniform_information(self):
        measure = (0, 1, 0, 0, 0)
        for denominator in (2, 10, 100, 1000):
            epsilon = Q(1, denominator)
            certificate = stationarity_certificate(
                measure, 3, PositiveHistoryMixture((1 - epsilon, epsilon)))
            self.assertEqual(certificate.mixture_defect, epsilon)
            self.assertEqual(certificate.gcd_defect, 1)
            self.assertFalse(certificate.mixture_stationary)

    def test_history_averaging_preserves_mass_while_changing_source_law(self):
        measure = (0, 1, 0, 0, 0)
        averaged = apply_history_filter(measure, 3, (Q(1, 4),) * 4)
        self.assertEqual(averaged, (0, Q(1, 4), Q(1, 4), Q(1, 4), Q(1, 4)))
        self.assertEqual(multiplication_pushforward(averaged, 3), averaged)
        self.assertEqual(multiplication_pushforward(measure, 16), measure)
        self.assertNotEqual(averaged, measure)


if __name__ == "__main__":
    unittest.main()
