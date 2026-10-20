"""Independent principal-minor oracle and hostile certificate mutations."""

from fractions import Fraction as Q
from itertools import combinations, product
from random import Random
import unittest

from observational_succ.cloud_schur_certificates import (
    NegativeWitness, RationalGram, certify, quadratic_value, verify_certificate,
)


def determinant_leibniz(matrix):
    # Deliberately independent of elimination; small exhaustive oracle only.
    from itertools import permutations
    n = len(matrix)
    answer = Q(0)
    for perm in permutations(range(n)):
        parity = sum(perm[i] > perm[j] for i in range(n) for j in range(i + 1, n))
        term = Q((-1) ** parity)
        for i in range(n):
            term *= matrix[i][perm[i]]
        answer += term
    return answer


def principal_minor_psd(matrix):
    n = len(matrix)
    return all(determinant_leibniz([[matrix[i][j] for j in ids] for i in ids]) >= 0
               for k in range(1, n + 1) for ids in combinations(range(n), k))


class CloudSchurTests(unittest.TestCase):
    def compare_oracle(self, matrix):
        result = certify(matrix)
        self.assertTrue(verify_certificate(matrix, result))
        self.assertEqual(type(result) is RationalGram, principal_minor_psd(matrix))

    def test_all_small_symmetric_matrices(self):
        for n, values in ((2, range(-2, 3)), (3, range(-1, 2))):
            positions = [(i, j) for i in range(n) for j in range(i, n)]
            for entries in product(values, repeat=len(positions)):
                matrix = [[Q(0)] * n for _ in range(n)]
                for (i, j), entry in zip(positions, entries):
                    matrix[i][j] = matrix[j][i] = Q(entry)
                self.compare_oracle(matrix)

    def test_seeded_larger_fresh_region(self):
        rng = Random(20261020)
        for n in (4, 5):
            for _ in range(60):
                matrix = [[Q(0)] * n for _ in range(n)]
                for i in range(n):
                    for j in range(i, n):
                        matrix[i][j] = matrix[j][i] = Q(rng.randint(-7, 7), rng.randint(1, 9))
                self.compare_oracle(matrix)

    def test_empty_and_rank_deficient(self):
        for matrix in ([], [[0]], [[0, 0], [0, 2]], [[1, 2, 3], [2, 4, 6], [3, 6, 9]]):
            self.compare_oracle(matrix)

    def test_narrow_negative_cone_no_float_or_denominator_limit(self):
        d = 10 ** 100
        matrix = [[Q(d * d), Q(d)], [Q(d), 1 - Q(1, d * d)]]
        result = certify(matrix)
        self.assertIs(type(result), NegativeWitness)
        self.assertEqual(quadratic_value(matrix, result.vector), -Q(1, d * d))

    def test_zero_pivot_coupling_value_minus_one(self):
        matrix = [[Q(0), Q(1, 10 ** 100)], [Q(1, 10 ** 100), Q(10 ** 100)]]
        result = certify(matrix)
        self.assertEqual(quadratic_value(matrix, result.vector), -1)

    def test_zero_pivot_after_schur(self):
        self.compare_oracle([[1, 1, 0], [1, 1, 1], [0, 1, 2]])

    def test_reject_forged_gram_and_negative_witness(self):
        positive = [[1, 0], [0, 1]]
        negative = [[1, 0], [0, -1]]
        self.assertFalse(verify_certificate(negative, certify(positive)))
        self.assertFalse(verify_certificate(positive, NegativeWitness((1, 0))))
        self.assertFalse(verify_certificate(positive, RationalGram((-1, -1), ((1, 0), (0, 1)))))
        self.assertFalse(verify_certificate(positive, RationalGram((1,), ((1,),))))
        self.assertFalse(verify_certificate(positive, lambda: True))
        self.assertFalse(verify_certificate(positive, {"verified": True}))

    def test_reject_lossy_or_malformed_input(self):
        for matrix in ([[1.0]], [[True]], [["1"]], [[1, 2]], [[1, 2], [0, 1]]):
            with self.assertRaises((TypeError, ValueError)):
                certify(matrix)
        self.assertFalse(verify_certificate([[1]], RationalGram((1.0,), ((1,),))))
        self.assertFalse(verify_certificate([[-1]], NegativeWitness((1.0,))))


if __name__ == "__main__":
    unittest.main()
