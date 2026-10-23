"""Exact controls for the infinite arithmetic source theorem and enclosures."""
import unittest
from fractions import Fraction as Q
from observational_succ.reality_pin_arithmetic import (
    ArithmeticSourceError, log_interval, primes_through, source_channels,
    arithmetic_matrix_interval, perturbation_bound, shift, boundary_moments,
    finite_second_moment, finite_third_moment_interval, finite_boundary_interval,
    boundary_resolvent_enclosure, galerkin_norm_bound, scalar_tail_bound,
    prime_cutoff_resolvent_bound, source_word_endpoint, reciprocal_cutoff_defect,
)
from observational_succ.boundary_realization_selection import matrix_inverse


class ArithmeticCarrierTests(unittest.TestCase):
    def test_log_positive_negative_and_null_controls(self):
        self.assertEqual(log_interval(1), (Q(), Q()))
        for x in (2, 3, 5, 7, 12, 29):
            a, b = log_interval(x, 3)
            c, d = log_interval(x, 10)
            self.assertLessEqual(a, c)
            self.assertLessEqual(d, b)
            self.assertLess(c, d)
        # Independent rational integral bounds: (x-1)/x <= log(x) <= x-1.
        for x in range(2, 20):
            a, b = log_interval(x, 10)
            self.assertGreaterEqual(a, Q(x-1, x))
            self.assertLessEqual(b, x-1)
        for x in (0, -1, 1.5, True):
            with self.assertRaises(ArithmeticSourceError):
                log_interval(x)

    def test_log_power_additivity_enclosures(self):
        for x in (2, 3, 5):
            for k in (2, 3, 4):
                a, b = log_interval(x)
                c, d = log_interval(x**k)
                self.assertLessEqual(max(k*a, c), min(k*b, d))

    def test_channel_collision_is_not_overwritten(self):
        channels = [x for x in source_channels(4) if x[1:3] == (1, 2)]
        self.assertEqual(channels, [("S", 1, 2, Q(1)), ("V_2", 1, 2, Q(1, 4))])
        lo, hi = arithmetic_matrix_interval(4)
        self.assertEqual(lo[0][1], Q(5, 4))
        self.assertEqual(hi[0][1], Q(5, 4))

    def test_second_moment_independent_matrix_oracle(self):
        for n in range(1, 13):
            for lam in (Q(-1), Q(), Q(1, 3), Q(1)):
                for sigma in (2, 3):
                    lo, hi = arithmetic_matrix_interval(n, lam, sigma, 3)
                    expected = finite_second_moment(n, lam, sigma)
                    self.assertEqual(boundary_moments(lo, 2)[2], expected)
                    self.assertEqual(boundary_moments(hi, 2)[2], expected)

    def test_third_moment_prime_jet_formula(self):
        for n in range(1, 12):
            for lam in (Q(-1, 2), Q(), Q(1)):
                lo, hi = arithmetic_matrix_interval(n, lam, 2, 4)
                self.assertEqual(finite_third_moment_interval(n, lam, 2, 4),
                                 (boundary_moments(lo, 3)[3], boundary_moments(hi, 3)[3]))

    def test_mutant_missing_SUCC_FUCC_cross_term_fails(self):
        n, lam, sigma = 7, Q(2, 3), 2
        false = shift(lam, sigma)**2 + lam**2 + sum(
            (Q(1, p**(2*sigma)) for p in primes_through(n)), Q())
        self.assertEqual(finite_second_moment(n, lam, sigma)-false,
                         2*lam*Q(1, 2**sigma))

    def test_fake_composite_primitive_changes_second_moment(self):
        for composite in (4, 6, 8, 9):
            lo, _ = arithmetic_matrix_interval(composite)
            matrix = [list(row) for row in lo]
            eta = Q(1, 17)
            matrix[0][composite-1] += eta
            matrix[composite-1][0] += eta
            delta = boundary_moments(matrix, 2)[2]-boundary_moments(lo, 2)[2]
            self.assertEqual(delta, eta*eta)
            with self.assertRaises(ArithmeticSourceError):
                source_word_endpoint((composite,))

    def test_affine_relation_does_not_authenticate_primality(self):
        # This identity holds for composites too; it cannot serve as a prime test.
        for a in range(2, 12):
            for n in range(1, 10):
                self.assertEqual(a*(n+1), a*n+a)
        self.assertEqual(source_word_endpoint((2, 2)), 4)
        with self.assertRaises(ArithmeticSourceError):
            source_word_endpoint((4,))

    def test_all_basis_states_accessible_by_source_words(self):
        for n in range(1, 30):
            self.assertEqual(source_word_endpoint(("S",)*(n-1)), n)
        for p in (2, 3, 5, 7):
            self.assertEqual(source_word_endpoint(("S", p)),
                             source_word_endpoint((p,)+("S",)*p))

    def test_reciprocal_horizon_rank_one(self):
        for n in range(2, 30):
            for p in (2, 3, 5, 7):
                for j in range(1, n+1):
                    q = n//p
                    expected = {q+1: Q(-1)} if n >= p and j == p*q else {}
                    self.assertEqual(reciprocal_cutoff_defect(n, p, j), expected)

    def test_finite_enclosures_shrink_with_log_precision(self):
        for n in (2, 4, 7):
            a, b = finite_boundary_interval(n, terms=3)
            c, d = finite_boundary_interval(n, terms=8)
            self.assertLessEqual(a, c)
            self.assertLessEqual(d, b)
            self.assertLess(c, d)

    def test_schur_horizon_bound_against_larger_independent_matrix(self):
        # Matrix inversion is independent of the paper Schur error formula.
        for n, larger in ((1, 4), (2, 7), (4, 9)):
            a, b = finite_boundary_interval(n, s=2, terms=8)
            c, d = finite_boundary_interval(larger, s=2, terms=8)
            self.assertGreater(c, b)
            self.assertLess(d-a, scalar_tail_bound(n, s=2))
            full_lo, full_hi = boundary_resolvent_enclosure(n, s=2)
            self.assertLessEqual(full_lo, c)
            self.assertGreaterEqual(full_hi, d)

    def test_error_budgets_decrease(self):
        for fn in (galerkin_norm_bound, scalar_tail_bound, prime_cutoff_resolvent_bound):
            values = [fn(n, s=3) for n in (1, 2, 5, 11)]
            self.assertTrue(all(values[j] > values[j+1] for j in range(3)))
        self.assertEqual(perturbation_bound(Q(-1, 2), 3), Q(2))

    def test_full_source_labelled_response_recovers_matrix(self):
        # Controlled words S^(n-1) give the complete resolvent matrix, not only R_11.
        matrix, _ = arithmetic_matrix_interval(5)
        s = Q(3)
        shifted = tuple(tuple(x+(s if i == j else 0) for j, x in enumerate(row))
                        for i, row in enumerate(matrix))
        response = matrix_inverse(shifted)
        recovered = matrix_inverse(response)
        self.assertEqual(recovered, shifted)

    def test_old_arithmetic_gibbs_state_not_stationary_for_new_operator(self):
        for lam in (Q(-1), Q(), Q(2)):
            matrix, _ = arithmetic_matrix_interval(3, lam=lam)
            # Normalization is a common positive scalar and does not affect commutation.
            rho = (Q(1), Q(1, 4), Q(1, 9))
            commutator_13 = matrix[0][2]*(rho[2]-rho[0])
            self.assertEqual(commutator_13, Q(-8, 81))
            self.assertNotEqual(commutator_13, 0)

    def test_reject_unjustified_exact_weights_and_negative_laplace_parameter(self):
        with self.assertRaises(ArithmeticSourceError):
            prime_cutoff_resolvent_bound(Q(199, 100), sigma=10)
        # Hostile noninteger-cutoff mutant: tail includes p=2 and defeats integral_P.
        self.assertGreater(Q(1, 2**10), Q(100, 199)**9 / 9)
        with self.assertRaises(ArithmeticSourceError):
            arithmetic_matrix_interval(3, sigma=1)
        with self.assertRaises(ArithmeticSourceError):
            arithmetic_matrix_interval(3, lam=0.1)
        with self.assertRaises(ArithmeticSourceError):
            finite_boundary_interval(3, s=-1)


if __name__ == "__main__":
    unittest.main()
