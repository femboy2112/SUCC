"""Independent measure, polynomial and graph routes for the SU(2) bridge."""

from fractions import Fraction as Q
from math import comb, factorial
import unittest

from observational_succ.ym_reflection_bridge import (
    TaylorWilsonState, haar_moment, haar_moment_recurrence,
    haar_polynomial, polynomial_product,
)
from observational_succ.ym_succ_character import (
    build_wilson_certificate, chebyshev_character, graph_return_moment,
    jacobi_action, polynomial_action, pure_state_error_bound, required_cutoff,
    wilson_graph_expectation, wilson_graph_vector,
)


class TestSuccessorCharacter(unittest.TestCase):
    def test_return_paths_recover_two_independent_haar_moment_formulas(self):
        for n in range(101):
            self.assertEqual(graph_return_moment(n), haar_moment(n))
            self.assertEqual(graph_return_moment(n), haar_moment_recurrence(n))

    def test_every_first_horizon_failure(self):
        for cutoff in range(15):
            for n in range(2 * cutoff + 2):
                self.assertEqual(graph_return_moment(n, cutoff), haar_moment(n))
            n = 2 * cutoff + 2
            self.assertEqual(haar_moment(n) - graph_return_moment(n, cutoff),
                             Q(1, 4**(cutoff + 1)))

    def test_character_orthonormality_against_actual_haar(self):
        for m in range(13):
            for n in range(13):
                p = polynomial_product(chebyshev_character(m), chebyshev_character(n))
                self.assertEqual(haar_polynomial(p), Q(m == n))

    def test_character_tensor_fusion_rule(self):
        for m in range(9):
            for n in range(9):
                product = polynomial_product(chebyshev_character(m), chebyshev_character(n))
                expected = [Q(0)] * (m + n + 1)
                for k in range(abs(m - n), m + n + 1, 2):
                    for j, c in enumerate(chebyshev_character(k)):
                        expected[j] += c
                self.assertEqual(product, tuple(expected))

    def test_cyclic_vector_generation(self):
        for n in range(15):
            root = (Q(1),) + (Q(0),) * 15
            expected = tuple(Q(j == n) for j in range(16))
            self.assertEqual(polynomial_action(chebyshev_character(n), root), expected)

    def test_bilateral_boundary_mutation_changes_the_state(self):
        for k in range(1, 8):
            bilateral = Q(comb(2 * k, k), 4**k)
            self.assertNotEqual(bilateral, graph_return_moment(2 * k))
        self.assertEqual(haar_moment(2), Q(1, 4))
        self.assertEqual(Q(comb(2, 1), 4), Q(1, 2))

    def test_wrong_cyclic_vector_changes_haar_moment(self):
        vector = (Q(0), Q(1), Q(0), Q(0))
        self.assertEqual(sum(a * b for a, b in zip(vector, polynomial_action((0, 0, 1), vector))), Q(1, 2))
        self.assertNotEqual(Q(1, 2), haar_moment(2))

    def test_compression_does_not_preserve_products(self):
        for cutoff in range(7):
            for index in range(cutoff + 1):
                large = tuple(Q(j == index) for j in range(cutoff + 2))
                compressed_square = polynomial_action((0, 0, 1), large)[:cutoff + 1]
                square_compressed = polynomial_action((0, 0, 1), large[:-1])
                defect = tuple(a - b for a, b in zip(compressed_square, square_compressed))
                expected = tuple(Q(1, 4) if j == cutoff == index else Q(0)
                                 for j in range(cutoff + 1))
                self.assertEqual(defect, expected)

    def test_wilson_vector_matches_independent_polynomial_measure(self):
        for beta in (Q(-3, 2), Q(0), Q(1), Q(7, 3)):
            for degree in (0, 1, 2, 5, 8):
                amplitude = tuple((beta / 2)**j / factorial(j) for j in range(degree + 1))
                density = polynomial_product(amplitude, amplitude)
                norm = haar_polynomial(density)
                for observable in ((1,), (0, 1), (2, -3, 1), (0, 0, 0, 1)):
                    expected = haar_polynomial(polynomial_product(density, observable)) / norm
                    self.assertEqual(wilson_graph_expectation(beta, degree, observable), expected)
                self.assertGreaterEqual(norm, 1)

    def test_full_state_norm_and_horizon_rejection(self):
        for degree in range(8):
            v = wilson_graph_vector(Q(3, 2), degree)
            self.assertGreaterEqual(sum(x * x for x in v), 1)
            self.assertEqual(required_cutoff(degree, 4), degree + 2)
            with self.assertRaises(ValueError):
                wilson_graph_expectation(1, degree, (0, 0, 0, 0, 1), degree + 1)
        with self.assertRaises(ValueError):
            wilson_graph_vector(1, 3, 2)

    def test_positivity_for_squared_polynomial_observables(self):
        for beta in (Q(-9, 4), Q(0), Q(11, 5)):
            for degree in (0, 1, 4):
                for p in ((1, -3), (0, 1), (2, 1, -5)):
                    self.assertGreaterEqual(wilson_graph_expectation(beta, degree, polynomial_product(p, p)), 0)

    def test_certificates_overlap_independent_positive_density_intervals(self):
        for beta in (Q(-5, 2), Q(3, 2), Q(1, 7)):
            for p in ((0, 1), (1, 0, -2), (0, 0, 0, 0, 1)):
                cert = build_wilson_certificate(beta, p, Q(1, 10**12))
                density = TaylorWilsonState(beta, 40)
                bound = sum(abs(c) for c in p)
                gap = abs(cert.expectation - density.expectation(p))
                self.assertLessEqual(gap, cert.error_bound + density.error_bound(bound))
                self.assertLessEqual(cert.error_bound, cert.tolerance)
                self.assertEqual(cert.norm_squared,
                                 sum(x * x for x in cert.unnormalized_vector))

    def test_zero_coupling_and_zero_observable_are_exact(self):
        cert = build_wilson_certificate(0, (0, 0, 0, 0, 1), Q(1, 10**30))
        self.assertEqual(cert.taylor_degree, 0)
        self.assertEqual(cert.expectation, Q(1, 8))
        self.assertEqual(cert.error_bound, 0)
        zero = build_wilson_certificate(100, (), Q(1, 10**30))
        self.assertEqual((zero.expectation, zero.error_bound), (0, 0))

    def test_exact_input_guards(self):
        for bad in (True, 1.0, -1):
            with self.assertRaises((TypeError, ValueError)):
                graph_return_moment(bad)
        with self.assertRaises(TypeError):
            wilson_graph_vector(0.5, 2)
        with self.assertRaises(ValueError):
            build_wilson_certificate(1, (1,), 0)
        with self.assertRaises(ValueError):
            pure_state_error_bound(1, 2, -1)
        with self.assertRaises(ValueError):
            jacobi_action(())


if __name__ == '__main__':
    unittest.main()
