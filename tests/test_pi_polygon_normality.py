"""Exact hostile tests for circle -> polygon -> digits normality research.

Finite certificates are intentionally NOT labeled as a proof of pi normality.
"""

import unittest
from math import isqrt
from fractions import Fraction as Q

from observational_succ.pi_polygon_normality import (
    certified_fractional_pi_digits, digit_block_total_variation,
    finite_digit_path, orbit_lipschitz_error_bound, polygon_pi_bracket,
    polygon_quantize, rational_sqrt_enclosure, uniform_grid_pushforward_counts,
    polygon_prefix_path, polygon_cylinder,
)


def machin_pi_bracket(terms=20):
    """Independent exact rational Machin + alternating-series pi enclosure.

    pi/4 = 4 atan(1/5) - atan(1/239), established by tangent addition.
    """
    def atan_interval(q):
        total = sum(((-1)**i * q**(2*i + 1) / (2*i + 1)
                     for i in range(terms)), Q(0))
        next_term = (-1)**terms * q**(2*terms + 1) / (2*terms + 1)
        return min(total, total + next_term), max(total, total + next_term)

    lo5, hi5 = atan_interval(Q(1, 5))
    lo239, hi239 = atan_interval(Q(1, 239))
    return 16 * lo5 - 4 * hi239, 16 * hi5 - 4 * lo239


class ExactPolygonGeometry(unittest.TestCase):
    def test_rational_sqrt_straddles_and_exact_square(self):
        for q in (Q(0), Q(1), Q(2), Q(1, 3), Q(9, 4), Q(3, 7)):
            a, b = rational_sqrt_enclosure(q, 64)
            self.assertLessEqual(a*a, q)
            self.assertGreaterEqual(b*b, q)
            self.assertLessEqual(b-a, Q(1, 1 << 64))
        self.assertEqual(rational_sqrt_enclosure(Q(9, 4), 64), (Q(3, 2), Q(3, 2)))
        with self.assertRaises(ValueError):
            rational_sqrt_enclosure(Q(-1))

    def test_archimedean_brackets_and_independent_exact_oracle(self):
        independent_lo, independent_hi = machin_pi_bracket()
        self.assertLess(independent_lo, independent_hi)
        last_lo, last_hi = Q(0), Q(4)
        for steps in range(0, 18):
            br = polygon_pi_bracket(steps, 256)
            self.assertEqual(br.sides, 4 * 2**steps)
            self.assertLess(br.lower, independent_lo)
            self.assertGreater(br.upper, independent_hi)
            self.assertGreaterEqual(br.lower, last_lo)
            self.assertLessEqual(br.upper, last_hi)
            # Classical bound: 0 < perimeter gap < 64/m^2 for m>=4.
            self.assertLess(br.upper - br.lower, Q(64, br.sides**2))
            last_lo, last_hi = br.lower, br.upper

    def test_certified_digit_prefix_only_from_polygon(self):
        word, br = certified_fractional_pi_digits(16, 10, 15, 256)
        self.assertEqual(word, '141592653')
        self.assertTrue(3 < br.lower < br.upper < Q(22, 7))
        short, _ = certified_fractional_pi_digits(0, 10, 10, 256)
        self.assertEqual(short, '')
        binary, _ = certified_fractional_pi_digits(18, 2, 25, 256)
        self.assertTrue(binary.startswith('001001000011'))

    def test_too_little_precision_fails_closed(self):
        with self.assertRaises(ArithmeticError):
            polygon_pi_bracket(30, 8)
        with self.assertRaises(ValueError):
            polygon_pi_bracket(-1)


class SourceAndPathMorphisms(unittest.TestCase):
    def test_two_balanced_pushforward_maps_are_not_identical(self):
        for base in (2, 3, 4):
            for level in range(4):
                for morphism in ('prefix', 'rotation'):
                    counts = uniform_grid_pushforward_counts(4, base, level, morphism)
                    self.assertEqual(set(counts), {base})
                    self.assertEqual(sum(counts), 4 * base**(level+1))
        x = Q(1, 7)
        q0, q1 = polygon_quantize(x, 4), polygon_quantize(x, 8)
        self.assertEqual(q0, 0)
        self.assertEqual(q1, Q(1, 8))
        self.assertNotEqual((2 * q1) % 1, q0)
        self.assertEqual(polygon_quantize(q1, 4), q0)

    def test_normality_requires_all_block_lengths(self):
        zero = (0,)*100
        self.assertEqual(digit_block_total_variation(zero, 2, 1), Q(1, 2))
        self.assertEqual(digit_block_total_variation(zero, 2, 3), Q(7, 8))
        alternating = (0,1)*50
        self.assertEqual(digit_block_total_variation(alternating, 2, 1), 0)
        self.assertGreater(digit_block_total_variation(alternating, 2, 2), Q(1, 3))
        squares = tuple(1 if i > 0 and isqrt(i)**2 == i else 0 for i in range(400))
        self.assertGreater(digit_block_total_variation(squares, 2, 1), Q(2, 5))

    def test_finite_known_normal_control_is_diagnostic_not_proof(self):
        # Champernowne-style binary concatenation is normal by a separate theorem.
        # These finitely many symbols are merely a calibrated sanity check.
        binary = "".join(format(n, "b") for n in range(1, 1500))[:8000]
        word = tuple(int(ch) for ch in binary)
        self.assertEqual(len(word), 8000)
        self.assertLess(digit_block_total_variation(word, 2, 1), Q(1, 20))
        self.assertLess(digit_block_total_variation(word, 2, 4), Q(9, 100))
        self.assertEqual(finite_digit_path(word[:16], 2, 30)[16:], (0,)*14)

    def test_terminating_prefix_is_eventually_zero_without_disproving_limit(self):
        prefix = (1, 0, 1, 1)
        self.assertEqual(finite_digit_path(prefix, 2, 9), (1,0,1,1,0,0,0,0,0))
        self.assertEqual(finite_digit_path(prefix, 2, 4), prefix)
        # Any completion has the same first N k-blocks if m>=N+k-1.
        for n in range(1, 4):
            for k in range(1, 5-n+1):
                self.assertGreaterEqual(len(prefix), n+k-1)
                future_a = prefix + (0,)*10
                future_b = prefix + (1,)*10
                blocks_a = tuple(future_a[j:j+k] for j in range(n))
                blocks_b = tuple(future_b[j:j+k] for j in range(n))
                self.assertEqual(blocks_a, blocks_b)

    def test_lipschitz_orbit_transport_bound(self):
        b, x, y, N = 2, Q(1, 7), Q(1, 8), 5
        def circular_distance(z):
            z = z % 1
            return min(z, 1-z)
        lhs = abs(sum(circular_distance((b**j*x)%1) for j in range(N))/N
                  - sum(circular_distance((b**j*y)%1) for j in range(N))/N)
        self.assertLessEqual(lhs, orbit_lipschitz_error_bound(b, N, abs(x-y)))
        self.assertGreater(orbit_lipschitz_error_bound(b, 30, Q(1, 2**10)), 1)
        with self.assertRaises(ValueError):
            digit_block_total_variation((0,), 2, 2)


class PrefixPathCircleQuotient(unittest.TestCase):
    def test_nested_cells_and_exact_uniform_cylinder_mass(self):
        for m in (3, 4, 5):
            for base in (2, 3):
                for index in range(m):
                    word = (base-1, 0, 1 % base, 0)
                    path = polygon_prefix_path(m, base, index, word)
                    for n in range(1, len(path)):
                        self.assertEqual(path[n] // base, path[n-1])
                        lo, hi, mass = polygon_cylinder(path[n], m, base, n)
                        prev_lo, prev_hi, _ = polygon_cylinder(path[n-1], m, base, n-1)
                        self.assertLessEqual(prev_lo, lo)
                        self.assertLessEqual(hi, prev_hi)
                        self.assertEqual(hi - lo, mass)
                        self.assertEqual(mass, Q(1, m * base**n))
                # The M fair cylinder masses sum to one at each level.
                for n in range(4):
                    self.assertEqual(sum(polygon_cylinder(j,m,base,n)[2]
                                         for j in range(m*base**n)), 1)

    def test_both_valid_prefix_paths_encode_the_same_circle_phase(self):
        # 1/4 = 0.01000... = 0.00111... in this m=4 refinement chart.
        for n in range(1, 12):
            right = polygon_prefix_path(4, 2, 1, (0,)*n)[-1]
            left = polygon_prefix_path(4, 2, 0, (1,)*n)[-1]
            rlo, _, _ = polygon_cylinder(right,4,2,n)
            _, lhi, _ = polygon_cylinder(left,4,2,n)
            self.assertEqual(rlo, Q(1,4))
            self.assertEqual(lhi, Q(1,4))
            self.assertNotEqual(left, right)
        with self.assertRaises(ValueError):
            polygon_prefix_path(4, 2, 4, ())
        with self.assertRaises(ValueError):
            polygon_cylinder(-1, 4, 2, 0)


if __name__ == '__main__':
    unittest.main()
