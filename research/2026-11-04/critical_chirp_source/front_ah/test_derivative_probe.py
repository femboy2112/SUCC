"""Independent exact oracle and hostile mutation checks for the paper theorem."""
from fractions import Fraction as F
import unittest

import derivative_probe as p


class TailDerivativeProbeTests(unittest.TestCase):
    def test_two_derivative_oracles(self):
        for n in (1, 2, 7, 31, 128):
            for k in range(8):
                self.assertEqual(p.signed_pole_derivative(n, k), p.positive_moment_derivative(n, k))
                self.assertGreater(p.positive_moment_derivative(n, k), 0)

    def test_monotonicity_needed_for_remainder(self):
        for k in range(8):
            values = [p.positive_moment_derivative(n, k) for n in range(1, 30)]
            self.assertTrue(all(a > b > 0 for a, b in zip(values, values[1:])))

    def test_derivative_intervals_nest(self):
        for n in (3, 19, 71):
            for k in range(6):
                a, b = p.tail_derivative_interval(n, k, 6)
                c, d = p.tail_derivative_interval(n, k, 12)
                self.assertLess(a, c)
                self.assertLess(d, b)

    def test_sharper_zero_order_coefficient(self):
        self.assertLess(F(7, 512), F(1, 64))
        for n in (1, 2, 7, 31, 128):
            a, b = p.tail_derivative_interval(n, 0)
            low, high = p.claimed_interval(n, 0)
            self.assertLess(low, a)
            self.assertLess(b, high)

    def test_preregistered_exact_holdouts_and_mutation(self):
        receipt = p.receipt()
        self.assertEqual(len(receipt["rows"]), 18)
        self.assertTrue(receipt["dropped_fourth_pole_detected"])

    def test_rejects_bad_domains(self):
        for n, k in ((0, 0), (1, -1), (True, 0), (1, False), (1.0, 0)):
            with self.assertRaises(ValueError):
                p.signed_pole_derivative(n, k)
        with self.assertRaises(ValueError):
            p.tail_derivative_interval(1, 0, 0)


if __name__ == "__main__":
    unittest.main()
