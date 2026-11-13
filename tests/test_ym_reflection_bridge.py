"""Finite exact witnesses for the accompanying paper proofs, with mutations."""

from fractions import Fraction as F
import unittest

from observational_succ.ym_reflection_bridge import (
    TaylorWilsonState,
    finite_hilbert_correlation,
    haar_moment,
    haar_moment_recurrence,
    haar_polynomial,
    hilbert_correlation,
    is_psd_exact,
    lattice_physical_mass_bounds,
    lattice_transfer_eigenvalue,
    physical_defect_bound,
    physical_time_correlation,
    polynomial_product,
    polynomial_sup_bound,
    quadratic_form,
    quarter_turn_cos,
    reflection_matrix,
    taylor_coefficients,
    toeplitz_matrix,
)


class WilsonSliceTests(unittest.TestCase):
    def test_haar_normalization_symmetry_and_known_values(self):
        self.assertEqual([haar_moment(n) for n in range(7)],
                         [F(1), F(0), F(1, 4), F(0), F(1, 8), F(0), F(5, 64)])

    def test_independent_catalan_and_integration_by_parts_routes(self):
        for n in range(81):
            self.assertEqual(haar_moment(n), haar_moment_recurrence(n))
        # Fresh degrees beyond the small algebraic examples in the note.
        for n in (97, 100, 126, 181, 200):
            self.assertEqual(haar_moment(n), haar_moment_recurrence(n))

    def test_beta_zero_is_exact_haar_at_every_even_order(self):
        for order in (0, 2, 10, 24):
            state = TaylorWilsonState(F(0), order)
            self.assertEqual(state.partition, 1)
            for n in range(15):
                self.assertEqual(state.expectation([0] * n + [1]), haar_moment(n))
            self.assertEqual(state.error_bound(F(7, 3)), 0)

    def test_first_nontrivial_partition_and_observables(self):
        state = TaylorWilsonState(F(3), 2)
        self.assertEqual(state.partition, F(17, 8))
        self.assertEqual(state.expectation([0, 1]), F(6, 17))
        self.assertEqual(state.expectation([0, 0, 1]), F(13, 34))
        self.assertEqual(state.expectation([1, -2, 1]), F(23, 34))

    def test_positive_real_polynomial_gram_controls(self):
        basis = [tuple([0] * j + [1]) for j in range(7)]
        # Negative beta also has a positive exponential and even approximant.
        for beta, order in ((F(1, 3), 0), (F(3), 2), (F(-7, 2), 6), (F(5, 4), 12)):
            state = TaylorWilsonState(beta, order)
            self.assertGreater(state.partition, 0)
            self.assertTrue(is_psd_exact(state.gram(basis)))
        # Duplicate/zero observables test the semidefinite, not merely definite, case.
        self.assertTrue(is_psd_exact(TaylorWilsonState(2, 8).gram(((1,), (1,), (), (0, 1)))))

    def test_odd_truncation_is_a_real_negative_square_mutation(self):
        weight = taylor_coefficients(F(3), 1)  # 1+3x has a negative region.
        f_squared = polynomial_product((1, -1), (1, -1))
        partition = haar_polynomial(weight)
        value = haar_polynomial(polynomial_product(f_squared, weight)) / partition
        self.assertEqual(partition, 1)
        self.assertEqual(value, F(-1, 4))
        signed_gram = ((F(1), F(3, 4)), (F(3, 4), F(1, 4)))
        self.assertEqual(quadratic_form(signed_gram, (1, -1)), F(-1, 4))
        self.assertFalse(is_psd_exact(signed_gram))
        with self.assertRaises(ValueError):
            TaylorWilsonState(3, 1)

    def test_error_bound_is_rational_and_converges_in_fresh_orders(self):
        f = (F(1, 3), F(-2, 5), F(3, 7))
        bound = polynomial_sup_bound(f)
        self.assertEqual(bound, F(122, 105))
        beta = F(7, 5)
        approximants = [TaylorWilsonState(beta, n) for n in (8, 18, 32)]
        errors = [a.error_bound(bound) for a in approximants]
        self.assertGreater(errors[0], errors[1])
        self.assertGreater(errors[1], errors[2])
        self.assertLess(errors[2], F(1, 10**25))
        # Two independently normalized approximants must obey the sum of their
        # proved error budgets; this does not test against a floating oracle.
        for i, a in enumerate(approximants):
            for j, b in enumerate(approximants):
                self.assertLessEqual(abs(a.expectation(f) - b.expectation(f)), errors[i] + errors[j])

    def test_exact_input_and_domain_contracts(self):
        with self.assertRaises(TypeError):
            TaylorWilsonState(0.5, 2)
        with self.assertRaises(ValueError):
            haar_moment(-1)
        with self.assertRaises(ValueError):
            TaylorWilsonState(1, 2).error_bound(-1)


class ReflectionAndGapTests(unittest.TestCase):
    def test_psd_checker_positive_negative_null_and_zero_pivot_controls(self):
        self.assertTrue(is_psd_exact(((2, 1), (1, 2))))
        self.assertFalse(is_psd_exact(((1, 2), (2, 1))))
        self.assertTrue(is_psd_exact(((0, 0), (0, 1))))
        self.assertFalse(is_psd_exact(((0, 1), (1, 0))))
        self.assertFalse(is_psd_exact(((1, 0), (1, 1))))
        self.assertTrue(is_psd_exact(()))

    def test_toeplitz_positivity_does_not_imply_reflection_positivity(self):
        self.assertTrue(is_psd_exact(toeplitz_matrix(quarter_turn_cos, range(13))))
        self.assertEqual(reflection_matrix(quarter_turn_cos, (1,)), ((F(-1),),))
        self.assertFalse(is_psd_exact(reflection_matrix(quarter_turn_cos, (1,))))

    def test_hilbert_reflection_positivity_and_cauchy_determinant(self):
        self.assertTrue(is_psd_exact(reflection_matrix(hilbert_correlation, range(9))))
        fresh = reflection_matrix(hilbert_correlation, (1, 3, 8, 19))
        self.assertTrue(is_psd_exact(fresh))
        small = reflection_matrix(hilbert_correlation, (1, 2))
        self.assertEqual(small[0][0] * small[1][1] - small[0][1] ** 2, F(1, 240))

    def test_finite_gapped_spectral_models_converge_with_certified_budget(self):
        for size in (1, 2, 7, 23):
            kernel = lambda n: finite_hilbert_correlation(size, n)
            self.assertTrue(is_psd_exact(reflection_matrix(kernel, (0, 1, 3, 7))))
            for n in (0, 1, 2, 7, 18, 31):
                self.assertLessEqual(abs(kernel(n) - hilbert_correlation(n)), F(1, size))
        self.assertEqual(finite_hilbert_correlation(7, 1), F(1, 2))

    def test_physical_mass_collapses_despite_each_positive_lattice_gap(self):
        for denominator in (2, 5, 17, 61):
            a = F(1, denominator)
            q = lattice_transfer_eigenvalue(a)
            low, high = lattice_physical_mass_bounds(a)
            self.assertLess(0, q)
            self.assertLess(q, 1)
            self.assertEqual(low, a / (1 + a*a))
            self.assertEqual(high, a)
            self.assertTrue(is_psd_exact(reflection_matrix(lambda n: q**n, (0, 1, 4, 9))))
            for t in (F(0), F(1, 7), F(3, 2), F(5)):
                defect = 1 - physical_time_correlation(a, t)
                self.assertGreaterEqual(defect, 0)
                self.assertLessEqual(defect, physical_defect_bound(a, t))

    def test_gap_probe_rejects_bad_domains(self):
        with self.assertRaises(ValueError):
            lattice_transfer_eigenvalue(0)
        with self.assertRaises(ValueError):
            physical_time_correlation(1, -1)
        with self.assertRaises(ValueError):
            reflection_matrix(hilbert_correlation, (-1,))
        with self.assertRaises(ValueError):
            finite_hilbert_correlation(0, 1)


if __name__ == "__main__":
    unittest.main()
