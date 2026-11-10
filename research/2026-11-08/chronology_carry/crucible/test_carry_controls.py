import sys
from pathlib import Path
from fractions import Fraction as Q
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parent))
import carry_controls as cc


class CarryInformationControls(unittest.TestCase):
    def test_arbitrary_forcing_full_cells(self):
        for base in (2, 3, 5, 16):
            for depth in (1, 2, 3):
                row = cc.cell_receipt(base, [Q((-1)**j*(j+1), j+7) for j in range(depth)])
                self.assertGreaterEqual(Q(row['full_mass']), Q(row['proved_lower']))

    def test_integer_forcing_leaves_full_uniform_tail(self):
        for base in (2, 5, 16):
            for depth in (1, 2, 3):
                row = cc.cell_receipt(base, [Q((-1)**j*j) for j in range(depth)])
                self.assertEqual(Q(row['full_mass']), 1)

    def test_original_finite_green_coupling(self):
        for t in (1, 7, 37):
            for depth in (1, 2, 3):
                row = cc.green_coupling_receipt(t, depth)
                self.assertLessEqual(Q(row['exact_word_mismatch_measure']), Q(row['union_upper']))
                self.assertLess(Q(row['source_upper']), Q(row['asymptotic_upper']))

    def test_same_prefix_antipodal_and_odd_denominator(self):
        for prefix in (0, 1, 3, 8, 16):
            for h in (1, 3, -5):
                row = cc.phase_pair_receipt(prefix, h)
                self.assertLess(Q(row['exact_antipodal_seed']), Q(row['sigma']))
                self.assertGreater(Q(row['squared_minimax_radius_lower']), Q(99,100))

    def test_future_carry_cells(self):
        self.assertEqual(cc.future_digit_receipt()['exact_future_digit_cylinders'], 24)


if __name__ == '__main__':
    unittest.main()
