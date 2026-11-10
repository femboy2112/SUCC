import unittest
from fractions import Fraction as Q
from itertools import combinations
from oracle import (Z, history, authenticate_original, source_cycle,
                    autocorrelation_multisets, polynomial_source_difference_check,
                    dft4, project_modes, norm2, mean, inner, centered,
                    partition_projection)


class CovarianceForgeTests(unittest.TestCase):
    def test_original_source_gate(self):
        self.assertTrue(authenticate_original(history(40)))
        self.assertFalse(authenticate_original(history(40, Q(1, 3))))
        self.assertFalse(authenticate_original([x % 1 for x in history(40)]))

    def test_all_tones_autocorrelation_rearrangement(self):
        for p in (17, 41, 73):
            a, _ = source_cycle(p)
            for k in range(len(a)):
                self.assertEqual(*autocorrelation_multisets(p, 1, k))

    def test_source_frequency_and_prime_domain(self):
        for p, h in ((41, 41), (9, 1), (7, 1)):
            with self.assertRaises(ValueError):
                source_cycle(p, h)

    def test_polynomial_chirp_elimination_keeps_nonzero_source(self):
        for degree in (1, 2, 3, 4):
            self.assertGreater(polynomial_source_difference_check(
                193, 3, degree, (1,)*degree), 0)

    def test_sparse_dual_is_attained_by_flat_coherent_control(self):
        a = [Z(Q(1)), Z(Q(1)), Z(Q(1)), Z(Q(-1))]
        self.assertTrue(all(x.abs2() == Q(1, 4) for x in dft4(a)))
        for s in range(5):
            for support in combinations(range(4), s):
                residual = [x-y for x, y in zip(a, project_modes(a, support))]
                self.assertEqual(norm2(residual), 1-Q(s, 4))

    def test_history_refinement_trades_prediction_for_leakage(self):
        a = [Z(Q(1)), Z(Q(1)), Z(Q(1)), Z(Q(-1))]
        u = centered(a)
        coarse = partition_projection(u, (0, 0, 0, 0))
        fine = partition_projection(u, (0, 1, 2, 3))
        self.assertEqual(norm2(coarse), 0)
        self.assertEqual(norm2(fine), norm2(u))
        self.assertEqual(inner(u, u), Z(norm2(u)))


if __name__ == '__main__':
    unittest.main()
