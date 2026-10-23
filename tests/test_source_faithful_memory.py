import unittest
from fractions import Fraction as Q

from observational_succ.source_faithful_memory import (
    basis_moments, carry_matrix, hankel_determinant, memory_kernels, moment,
    reconstruct_with_memory, transfer_numerator,
)


class CarryMemoryTests(unittest.TestCase):
    def test_independent_basis_oracle_and_hidden_elimination(self):
        for a in (2, 3, 5, 7):
            for z in (-1, 1, Q(2, 3)):
                expected = tuple(moment(a, z, n) for n in range(3*a+2))
                self.assertEqual(basis_moments(a, z, 3*a+1), expected)
                self.assertEqual(reconstruct_with_memory(a, z, 3*a+1), expected)

    def test_false_markov_mutation_is_rejected(self):
        for a in (2, 3, 6, 11):
            for z in (-1, Q(2, 3)):
                error = moment(a, z, 2)-moment(a, z, 1)**2
                self.assertEqual(error, -(Q(z)-1)**2/a**2)
                self.assertNotEqual(error, 0)
                self.assertEqual(memory_kernels(a, z, 1), (error,))

    def test_transfer_denominator_recurrence(self):
        for a in (2, 3, 5, 11):
            for z in (-1, Q(2, 3)):
                values = basis_moments(a, z, 4*a)
                numerator = transfer_numerator(a, z)
                for n in range(len(values)):
                    coefficient = values[n]-(Q(z)*values[n-a] if n >= a else 0)
                    self.assertEqual(coefficient, numerator[n] if n < a else 0)

    def test_minimality_witness_and_constant_mode_null(self):
        for a in (2, 3, 5, 7, 11):
            for z in (-1, Q(2, 3)):
                self.assertNotEqual(hankel_determinant(a, z, a), 0)
                self.assertEqual(hankel_determinant(a, z, a+1), 0)
            self.assertEqual(hankel_determinant(a, 1, 2), 0)
            self.assertEqual(memory_kernels(a, 1, 4), (Q(0),)*4)

    def test_exact_binary_antiperiodic_control(self):
        self.assertEqual(carry_matrix(2, -1), ((0, -1), (1, 0)))
        self.assertEqual(basis_moments(2, -1, 6), (1, 0, -1, 0, 1, 0, -1))
        self.assertEqual(memory_kernels(2, -1, 4), (-1, 0, 0, 0))

    def test_source_contracts(self):
        for bad in (True, 1, 2.0):
            with self.assertRaises(ValueError):
                moment(bad, 1, 0)
        with self.assertRaises(ValueError):
            moment(2, 0.5, 0)
        with self.assertRaises(ValueError):
            moment(2, 1, -1)


if __name__ == '__main__':
    unittest.main()
