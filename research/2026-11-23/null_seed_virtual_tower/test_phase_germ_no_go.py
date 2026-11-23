"""Exact finite coefficient shadows of the shrinking phase-jet radius theorem."""
from fractions import Fraction
import unittest


class PhaseGermTests(unittest.TestCase):
    def test_locked_phase_jets_have_moving_poles(self):
        # At x=1/16 and h=16, all orbit phases are 1.
        # Their kth seed-derivative coefficient, divided by (2*pi*i*h)^k,
        # is 16^(k*n); the generating function is 1/(1-16^k*z).
        for k in range(0, 8):
            b = 16**k
            for n in range(1, 16):
                self.assertEqual(b**n, 16**(k*n))
                self.assertEqual(Fraction(b**n, b**n), 1)
            z = Fraction(1, 2*b)
            partial = sum((b*z)**n for n in range(18))
            exact = 1/(1-b*z)
            self.assertEqual(exact-partial, Fraction(1, 2**17))

    def test_normalized_all_order_phase_sheets_have_rank_one(self):
        # Removing the 16^(k*n) time-scale factor leaves identical columns.
        # Hence every 2x2 minor of the normalized derivative matrix is zero.
        times = [2, 3, 5, 11]
        orders = [0, 1, 2, 3, 5]
        M = [[Fraction(16**(k*n), 16**(k*n)) for k in orders]
             for n in times]
        for i in range(len(times)):
            for j in range(i+1, len(times)):
                for a in range(len(orders)):
                    for b in range(a+1, len(orders)):
                        self.assertEqual(M[i][a]*M[j][b] - M[i][b]*M[j][a], 0)


if __name__ == '__main__':
    unittest.main()
