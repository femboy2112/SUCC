from fractions import Fraction as Q
import unittest

import exact_oracle as oracle


class SignedLagTests(unittest.TestCase):
    def test_signed_pair_identity(self):
        values = ((1,0), (0,1), (-1,0), (Q(3,5), Q(4,5)))
        for h in range(1,9):
            self.assertEqual(oracle.direct_energy(values,h), oracle.pair_energy(values,h))

    def test_absolute_values_erase_cancellation(self):
        values = ((1,0),(-1,0))*16
        self.assertEqual(oracle.pair_energy(values,8),Q(1,256))
        self.assertGreater(oracle.pair_energy(values,8,absolute=True),Q(9,10))

    def test_zero_diagonal_is_not_unit(self):
        values = ((0,0),)*7
        self.assertEqual(oracle.direct_energy(values,3),0)
        self.assertEqual(oracle.pair_energy(values,3),0)

    def test_literal_source_transport(self):
        values = oracle.literal_history(25)
        for n in (1,5,17):
            for lag in (1,3,7):
                self.assertEqual(values[n+lag]-values[n],
                                 (16**lag-1)*values[n]+oracle.source_sum(n,lag))

    def test_full_order_is_degenerate(self):
        for p in (17,41,73):
            order = oracle.order16(p)
            self.assertEqual(pow(16,order,p),1)
            self.assertTrue(all(pow(16,j,p)!=1 for j in range(1,order)))

    def test_sqrt_comparison(self):
        self.assertTrue(oracle.sqrt_le_sqrt_plus(Q(9),Q(4),Q(1)))
        self.assertFalse(oracle.sqrt_le_sqrt_plus(Q(10),Q(4),Q(1)))
        with self.assertRaises(ValueError):
            oracle.sqrt_le_sqrt_plus(Q(-1),Q(0),Q(0))


if __name__ == "__main__":
    unittest.main()
