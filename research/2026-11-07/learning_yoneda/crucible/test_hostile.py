"""Focused semantic regressions for the hostile controls."""
import unittest
from itertools import product
from fractions import Fraction as Q
from hostile_oracle import (
    c5_source_world, independent_decoder_possible, autocorrelation,
    bernoulli_cdf_at_hex_rational, source, unwrapped,
)
from observational_succ.interobserver_channels import exact_minimum_channel


class HostileTests(unittest.TestCase):
    def test_conditional_memory_reuses_existing_solver(self):
        _, world = c5_source_world()
        code = exact_minimum_channel(world)
        self.assertEqual((code.codewords, code.fixed_width_bits), (3, 2))
        self.assertFalse(any(independent_decoder_possible(world, colors)
                             for colors in product(range(2), repeat=5)))

    def test_original_forcing_exact_zero_and_unwrapped_lift(self):
        self.assertEqual(source(1), Q(47, 15))
        a, b = unwrapped(Q(), 8), unwrapped(Q(1, 16**3), 8)
        self.assertEqual(a[0], 0)
        self.assertTrue(all((a[n]%1 == b[n]%1) == (n >= 3) for n in range(9)))
        self.assertTrue(all(b[n]-a[n] == Q(16)**(n-3) for n in range(9)))

    def test_homometry_is_not_equality(self):
        a, b = (0, 1, 4, 6), (0, 1, 3, 7)
        self.assertNotEqual(a, b)
        self.assertEqual(autocorrelation(a, 12), autocorrelation(b, 12))
        self.assertNotEqual(autocorrelation(a, 12), autocorrelation((0, 1, 3, 6), 12))

    def test_calibrated_lattice_is_not_uniform_digits(self):
        p = [Q(1, 16)]*16
        p[2] += Q(1, 64)
        p[3] -= Q(1, 64)
        self.assertEqual(bernoulli_cdf_at_hex_rational(p, Q(1, 2*16**5)), Q(1, 2*16**5))
        self.assertGreater(sum(x*x for x in p), Q(1, 16))


if __name__ == "__main__":
    unittest.main()
