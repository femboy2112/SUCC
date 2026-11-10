import unittest
from fractions import Fraction as F
from oracle import averaged_matrix, check_uniform_grid, circle_discrepancy, mean_product_from_cells


class FixedDepthTests(unittest.TestCase):
    def test_uniform_spectral_identity(self):
        for h in (1, 2, 8):
            self.assertGreater(check_uniform_grid(8, 2, h), 0)

    def test_repeated_positions(self):
        matrix = averaged_matrix([F(0), F(0)], [F(1, 3), F(2, 3)], 100)
        self.assertEqual(matrix, [[F(1, 3), F(2, 3)]] * 2)

    def test_sparse_empty_cells(self):
        matrix = averaged_matrix([F(0), F(1, 2)], [F(1, 3), F(2, 3)], 100)
        self.assertEqual(matrix, [[1, 0], [0, 1]])

    def test_nonuniform_pair_symmetry(self):
        x, w = [F(0), F(1, 7), F(3, 7)], [F(1, 6), F(2, 6), F(3, 6)]
        matrix = averaged_matrix(x, w, 3)
        self.assertEqual(w[0] * matrix[0][1], w[1] * matrix[1][0])
        self.assertEqual(mean_product_from_cells(x, w, 3, [1, -1, 0], [0, 1, -1]),
                         sum(w[i] * [0, 1, -1][i] * matrix[i][j] * [1, -1, 0][j]
                             for i in range(3) for j in range(3)))

    def test_discrepancy(self):
        self.assertEqual(circle_discrepancy([F(0), F(1, 2)], [F(1, 2)] * 2), F(1, 2))
        self.assertEqual(circle_discrepancy([F(1, 7)], [F(1)]), F(1))

    def test_bad_weights(self):
        with self.assertRaises(ValueError):
            averaged_matrix([F(0), F(1, 2)], [F(1), F(1)], 2)


if __name__ == "__main__":
    unittest.main()
