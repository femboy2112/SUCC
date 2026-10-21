"""Exact holdouts for the new inverse correction, not source authentication."""
from fractions import Fraction as Q
from math import factorial
import unittest

from observational_succ import cloud_exact_moment_inverse as E
from observational_succ import cloud_operator_transport as C


def legendre(n):
    coefficients = [Q()]*(n+1)
    for k in range(n//2+1):
        coefficients[n-2*k] = Q((-1)**k*factorial(2*n-2*k),
            2**(2*k)*factorial(k)*factorial(n-k)*factorial(n-2*k))
    return tuple(coefficients)


def projected_pair(b, parity):
    cells = ((Q(-1, 2), Q(1, 2)-b),
             (Q(1, 2)-b, b-Q(1, 2)), (b-Q(1, 2), Q(1, 2)))
    modes = (4, 6) if parity == 'even' else (5, 7)
    return tuple(tuple((lo, hi, legendre(n)) for lo, hi in cells) for n in modes)


def multiply(a, b):
    return tuple(tuple(sum((a[i][k]*b[k][j] for k in range(2)), Q())
                       for j in range(2)) for i in range(2))


def transpose(a):
    return tuple(zip(*a))


class ExactMomentInverseTests(unittest.TestCase):
    def test_inverse_identity_large_rational_offdiagonal(self):
        h = 10**40
        a = ((Q(h+2), Q(h)), (Q(h), Q(h+3)))
        self.assertEqual(multiply(a, E.inverse2(a)), ((1, 0), (0, 1)))
        with self.assertRaises(ValueError):
            E.inverse2(((Q(1), Q(2)), (Q(2), Q(1))))

    def test_quadrature_independent_discretizations(self):
        for cells in (8, 14, 32):
            for parity in ('even', 'odd'):
                data = E.constraint_gram(Q(7, 10), Q(), Q(1, 4), parity, cells=cells)
                self.assertTrue(data['independent_quadrature_enclosures_verified'])
                self.assertTrue(E.matrix_psd(E.matrix_add(
                    data['quadrature_gram_upper'], data['nominal_gram'], -1)))
        value, error = E.simpson_enclosure((1, 2, 3, 4), Q(-1, 3), Q(1, 4), 8)
        self.assertEqual(error, 0)
        self.assertEqual(value, C.integrate((1, 2, 3, 4), Q(-1, 3), Q(1, 4)))

    def test_shift_matrix_enclosures_at_displaced_rational_points(self):
        b, db, kappa = Q(7, 10), Q(1, 100000), Q(1, 4)
        for parity in ('even', 'odd'):
            data = E.constraint_gram(b, db, kappa, parity)
            for displacement in (-db, -db/3, db/7, db):
                actual = E.constraint_gram(b+displacement, Q(), kappa, parity)['nominal_gram']
                self.assertTrue(E.matrix_psd(E.matrix_add(data['gram_upper'], actual, -1)))
                self.assertTrue(E.matrix_psd(E.matrix_add(
                    data['quadrature_gram_upper'], actual, -1)))

    def test_exact_weight_stronger_than_old_diagonal(self):
        b = Q(7, 10)
        for parity in ('even', 'odd'):
            result = E.exact_moment_constraint_saving(
                projected_pair(b, parity), b, Q(), Q(1, 4), parity)
            self.assertTrue(E.matrix_pd(result['exact_weight_excess']))
            self.assertTrue(E.matrix_pd(result['quadrature_weight_excess']))
            self.assertTrue(E.matrix_pd(result['exact_additional_saving_lower']))
            self.assertTrue(E.matrix_pd(result['quadrature_additional_saving_lower']))

    def test_complete_correction_bounds_true_displaced_inverse(self):
        b, db, kappa, w = Q(7, 10), Q(1, 10**10), Q(1, 4), Q(12, 25)
        for parity in ('even', 'odd'):
            residuals = projected_pair(b, parity)
            result = E.exact_moment_constraint_saving(residuals, b, db, kappa, parity)
            for shift in (b-db, b, b+db):
                gram = E.constraint_gram(shift, Q(), kappa, parity)['nominal_gram']
                z = tuple(tuple(C.piece_pairing(p,
                    C.inverse_polynomial_pieces(h, shift, kappa, w)) for p in residuals)
                    for h in E.constraints(parity))
                actual = multiply(multiply(transpose(z), E.inverse2(gram)), z)
                for prefix in ('exact', 'quadrature'):
                    lower = result[prefix+'_combined_constraint_saving_lower']
                    self.assertTrue(E.matrix_psd(E.matrix_add(actual, lower, -1)))

    def test_no_invented_improvement_when_zero_prime_weight(self):
        b = Q(7, 10)
        result = E.exact_moment_constraint_saving(
            projected_pair(b, 'even'), b, Q(), Q(1, 4), 'even', w=Q())
        self.assertFalse(result['exact_weight_excess_psd'])
        self.assertNotIn('exact_additional_saving_lower', result)

    def test_exact_domain_and_high_moment_guards(self):
        for bad in (True, 0.7, '7/10'):
            with self.assertRaises(ValueError):
                E.constraint_gram(bad, Q(), Q(1, 4), 'even')
        for cells in (True, 3, 0, Q(8)):
            with self.assertRaises(ValueError):
                E.constraint_gram(Q(7, 10), Q(), Q(1, 4), 'even', cells=cells)
        bad = tuple((lo, hi, (Q(1),)) for lo, hi, _ in projected_pair(Q(7, 10), 'even')[0])
        with self.assertRaises(ValueError):
            E.exact_moment_constraint_saving((bad, bad), Q(7, 10), Q(), Q(1, 4), 'even')

    def test_reverse_young_rejects_indefinite_weight(self):
        with self.assertRaises(ValueError):
            E._weighted_lower(((Q(1), Q(2)), (Q(2), Q(1))),
                              ((Q(1), Q()), (Q(), Q(1))),
                              ((Q(), Q()), (Q(), Q())), Q(1, 1024))


if __name__ == '__main__':
    unittest.main()
