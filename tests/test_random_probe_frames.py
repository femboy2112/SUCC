"""Exact budget arithmetic and independent finite-distribution controls."""

from fractions import Fraction as Q
from math import comb
import unittest

from observational_succ.random_probe_frames import (
    ceil_log2_ratio, frame_sampling_certificate,
)


class TestRandomProbeFrames(unittest.TestCase):
    def test_binary_log_boundary_and_large_exact_inputs(self):
        for k in range(1, 80):
            self.assertEqual(ceil_log2_ratio(1 << k), k)
            self.assertEqual(ceil_log2_ratio(Q((1 << (k + 1)) - 1, 2)), k)
            self.assertEqual(ceil_log2_ratio(Q((1 << (k + 1)) + 1, 2)), k + 1)
        self.assertEqual(ceil_log2_ratio(1), 0)

    def test_recommended_constants_are_exact(self):
        c = frame_sampling_certificate(16, Q(1, 4))
        self.assertEqual(c.independent_rows, 16 * 16 * 11)
        self.assertEqual(c.failure_probability_upper, Q(1, 64))
        self.assertEqual(c.gram_eigenvalue_lower, Q(3, 8))
        self.assertEqual(c.gram_eigenvalue_upper, Q(15, 8))
        self.assertEqual(c.gram_condition_upper, 5)

    def test_budget_pays_exponent_without_float_log(self):
        for b in (1, 2, 7, 31, 257, 4096):
            for eta in (Q(0), Q(1, 4), Q(7, 8)):
                for epsilon, delta in ((Q(1, 2), Q(1, 64)), (Q(2, 3), Q(3, 100))):
                    c = frame_sampling_certificate(b, eta, epsilon, delta)
                    exponent = Q(c.independent_rows) * epsilon**2 * (1 - eta) / (3 * b)
                    self.assertGreaterEqual(exponent, c.binary_log_budget)
                    self.assertLessEqual(c.failure_probability_upper, delta)
                    self.assertGreater(c.gram_eigenvalue_lower, 0)

    def test_independent_two_axis_census(self):
        # Population rows (1,+1),(1,-1), each probability 1/2: G=I.
        c = frame_sampling_certificate(2, 0, Q(3, 4), Q(1, 3))
        count = c.independent_rows
        failures = sum(comb(count, plus) for plus in range(count + 1)
                       if abs(Q(2 * plus - count, count)) > c.relative_error)
        self.assertLessEqual(Q(failures, 2**count), c.failure_probability_upper)
        self.assertGreater(failures, 0)

    def test_whitened_nonuniform_two_axis_census(self):
        # P(+)=3/4 gives population eigenvalues 3/2 and 1/2.
        c = frame_sampling_certificate(2, Q(1, 2), Q(3, 4), Q(1, 3))
        count = c.independent_rows
        failure = Q(0)
        for plus in range(count + 1):
            q = Q(2 * plus - count, count)
            lower_ok = (1 + q >= (1 - c.relative_error) * Q(3, 2)
                        and 1 - q >= (1 - c.relative_error) * Q(1, 2))
            upper_ok = (1 + q <= (1 + c.relative_error) * Q(3, 2)
                        and 1 - q <= (1 + c.relative_error) * Q(1, 2))
            if not (lower_ok and upper_ok):
                failure += Q(comb(count, plus) * 3**plus, 4**count)
        self.assertLessEqual(failure, c.failure_probability_upper)
        self.assertGreater(failure, 0)

    def test_copying_a_single_row_is_not_independent_sampling(self):
        # Every number of copies has Gram eigenvalues (2,0), regardless of sign.
        c = frame_sampling_certificate(2, 0)
        for shared_sign in (-1, 1):
            determinant = 1 - shared_sign**2
            self.assertEqual(determinant, 0)
        self.assertGreater(c.gram_eigenvalue_lower, 0)
        self.assertLess(c.failure_probability_upper, 1)

    def test_normalized_readout_noise_carries_dimension(self):
        # An orthogonal unnormalized phase matrix has RMS ||Ac||=||c||.
        # Dividing echoes by B makes aligned mean-error amplification sqrt(B).
        b = 9
        c = frame_sampling_certificate(b, 0, Q(1, 2))
        self.assertEqual(c.normalized_echo_mean_noise_gain_squared, 2 * b)
        self.assertEqual(c.normalized_echo_vector_noise_gain_squared, 2 * b**2)
        self.assertEqual(c.normalized_echo_vector_noise_gain_squared,
                         b * c.normalized_echo_mean_noise_gain_squared)

    def test_population_error_one_is_not_invertible(self):
        for eta in (-1, 1, Q(3, 2)):
            with self.assertRaises(ValueError):
                frame_sampling_certificate(2, eta)

    def test_probability_and_error_domains(self):
        for q in (Q(0), Q(1), Q(-1, 2), Q(3, 2)):
            with self.assertRaises(ValueError):
                frame_sampling_certificate(2, Q(1, 4), failure_probability=q)
            with self.assertRaises(ValueError):
                frame_sampling_certificate(2, Q(1, 4), relative_error=q)

    def test_reject_bool_float_and_outside_implementation_budget(self):
        for b in (True, 0, 4097, 2.0):
            with self.assertRaises(ValueError):
                frame_sampling_certificate(b, Q(1, 4))
        for q in (True, 0.25, '1/4'):
            with self.assertRaises(ValueError):
                frame_sampling_certificate(2, q)
        with self.assertRaises(ValueError):
            ceil_log2_ratio(Q(1, 2))


if __name__ == '__main__':
    unittest.main()
