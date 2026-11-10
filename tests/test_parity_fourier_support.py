"""Exact tests for the parity Fourier support theorem (F-10)."""
import unittest
from fractions import Fraction as Q

from observational_succ import parity_fourier_support as pfs


class ParityFourierSupportTests(unittest.TestCase):
    def test_support_exactly_8_mod_16(self):
        for m in range(1, 300):
            self.assertEqual(pfs.fourier_support(m), m % 16 == 8, m)

    def test_geometric_sum_identity(self):
        # sum_{a}(-1)^a z^a = 16 iff z=-1 iff m ≡ 8 (mod 16), else 0.
        for m in range(1, 300):
            expected = Q(16) if m % 16 == 8 else Q(0)
            self.assertEqual(pfs.geometric_sum_identity(m), expected, m)

    def test_coefficient_scale(self):
        self.assertEqual(pfs.exact_coefficient_scale(8), Q(2))
        self.assertEqual(pfs.exact_coefficient_scale(24), Q(2, 3))
        self.assertEqual(pfs.exact_coefficient_scale(1), Q(0))

    def test_support_is_arithmetic_progression(self):
        nonzero = [m for m in range(1, 200) if pfs.fourier_support(m)]
        self.assertTrue(all(m % 16 == 8 for m in nonzero))
        self.assertEqual(nonzero[:4], [8, 24, 40, 56])


if __name__ == '__main__':
    unittest.main()
