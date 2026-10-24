"""Adversarial exact tests for the dyadic/prime transfer report."""
from __future__ import annotations

from fractions import Fraction as Q
from math import gcd
import unittest

from observational_succ.pi_dyadic_prime_transfer import (
    _bbp_forcing, _bbp_states, cross_radix_bad_cylinders,
    decode_target_prefix, dyadic_carry_branch_certificate,
    opposite_sides_same_binary_prefix, ramanujan_power_two,
)


class CrossRadixExactTests(unittest.TestCase):
    def test_exact_cross_radix_boundary_count_independently(self):
        for base, digits, extra in ((2, 4, 0), (16, 2, 0), (3, 3, 2),
                                    (5, 2, 3), (6, 2, 2), (7, 1, 6),
                                    (11, 2, 2), (13, 1, 4)):
            q = base ** digits
            k = (q - 1).bit_length() + extra
            cert = cross_radix_bad_cylinders(base, digits, k)
            brute = sum(decode_target_prefix(j, k, base, digits) is None
                        for j in range(1 << k))
            self.assertEqual(brute, q - gcd(q, 1 << k))
            self.assertEqual(brute, cert['ambiguous_binary_cells'])
            self.assertLessEqual(cert['bad_haar_mass'], Q(1, 1 << extra))

    def test_base16_to_two_is_exact_at_four_bits(self):
        for n in range(1, 5):
            cert = cross_radix_bad_cylinders(16, n, 4 * n)
            self.assertEqual(cert['ambiguous_binary_cells'], 0)
            for index in range(16**n):
                self.assertEqual(decode_target_prefix(index, 4*n, 16, n), index)

    def test_odd_prime_has_no_uniform_finite_prefix_decoder(self):
        for p in (3, 5, 7, 11, 13):
            for bits in (1, 2, 3, 7, 16, 32, 64):
                left, right = opposite_sides_same_binary_prefix(p, bits)
                self.assertEqual((1 << bits) * left // 1,
                                 (1 << bits) * right // 1)
                self.assertNotEqual((p * left) // 1, (p * right) // 1)

    def test_prefix_decoder_refuses_crossing(self):
        self.assertEqual(decode_target_prefix(1, 2, 2, 1), 0)
        self.assertIsNone(decode_target_prefix(1, 2, 3, 1))
        with self.assertRaises(ValueError):
            cross_radix_bad_cylinders(3, 2, 2)
        with self.assertRaises(ValueError):
            decode_target_prefix(4, 2, 3, 1)


class DyadicCarryTests(unittest.TestCase):
    def test_four_pole_regrouping_and_odd_carrier(self):
        for n in range(1, 65):
            regrouped = (Q(4, 8*n-7) - Q(1, 8*n-3)
                         - Q(3*n-1, (2*n-1)*(4*n-1)))
            self.assertEqual(_bbp_forcing(n), regrouped)
        self.assertTrue(all(y.denominator % 2 for y in _bbp_states(64)))

    def test_exact_four_shell_character_identity(self):
        for label in range(16):
            self.assertEqual(1 + sum(ramanujan_power_two(j, label)
                                     for j in range(1, 5)),
                             16 if label == 0 else 0)

    def test_authenticated_exact_branch_tomography(self):
        for p in (41, 97, 257):
            for tau in (Q(1, 4), Q(1, 16), Q(1, 64)):
                result = dyadic_carry_branch_certificate(p, tau)
                n = result['window_length']
                hist = result['branch_histogram']
                self.assertEqual(sum(hist), result['dyadic_nested_counts'][0])
                self.assertEqual(hist[0], result['zero_centered_branch'])
                self.assertGreaterEqual(hist[0], n)
                self.assertEqual(result['dyadic_nested_counts'][4], hist[0])
                self.assertEqual(16*hist[0], sum(hist)+sum(result['ramanujan_shells']))
                for j in range(1, 5):
                    self.assertLessEqual(result['dyadic_nested_counts'][j],
                                         result['dyadic_nested_counts'][j-1])

    def test_mutants_dont_forge_uniformity(self):
        # Uniformity under all odd residue multipliers cannot force
        # the zero-branch weight to be 1/16: δ0 is invariant under all.
        point_mass = [16] + [0]*15
        for multiplier in (3, 5, 7, 11, 13):
            self.assertEqual(point_mass,
                [point_mass[(multiplier * k) % 16] for k in range(16)])
        self.assertNotEqual(point_mass[0], sum(point_mass) // 16)

    def test_domain_guards(self):
        with self.assertRaises(ValueError):
            dyadic_carry_branch_certificate(73, Q(1, 1000000))
        with self.assertRaises(ValueError):
            dyadic_carry_branch_certificate(31, Q(1, 4))
        with self.assertRaises(ValueError):
            ramanujan_power_two(5, 0)


if __name__ == '__main__':
    unittest.main()
