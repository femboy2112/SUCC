"""Calibrated exact finite probes; universal conclusions live in the proof."""
from fractions import Fraction as F
import unittest

from flat_shadow import (source, source_derivative, boundary, tail_length, truncated_tail,
                         shadow_source, shadow_source_derivative, orbit, orbit_from_boundary,
                         relative_error_bound, dirichlet_defect_partial, turns)


class FlatShadowTests(unittest.TestCase):
    def test_source_against_grouped_positive_formula(self):
        for n in [1, 2, 3, 17, 53, 127]:
            for u in [F(-3, 4), F(0), F(2, 3)]:
                a = 8 * n - 7 + u
                grouped = 6 / (a * (a + 3)) + 4 / (a * (a + 4)) + 5 / (a * (a + 5))
                self.assertEqual(source(n, u), grouped)
                self.assertGreater(grouped, 0)

    def test_zero_seed_and_rational_boundary(self):
        for m, k in [(0, 1), (1, 2), (4, 3), (11, 5)]:
            self.assertEqual(orbit_from_boundary(0, m, k), 0)
            self.assertIsInstance(boundary(m, k), F)

    def test_independent_telescoping_against_forcing_recurrence(self):
        for m, k in [(0, 1), (1, 4), (5, 2), (13, 3)]:
            for u in [F(-1, 2), F(0), F(1, 3)]:
                for n in [0, 1, m, m + 1, m + 2, m + 9, m + 21]:
                    self.assertEqual(orbit(n, m, k, u), orbit_from_boundary(n, m, k, u))

    def test_exact_source_and_orbit_prefix(self):
        for m, k in [(0, 3), (6, 1), (17, 4)]:
            original = F(0)
            for n in range(1, m + 1):
                self.assertEqual(shadow_source(n, m, k), source(n))
                original = 16 * original + source(n)
                self.assertEqual(orbit(n, m, k), original)
            self.assertNotEqual(shadow_source(m + 1, m, k), source(m + 1))

    def test_positive_source_and_uniform_relative_budget(self):
        for m, k in [(0, 1), (2, 2), (9, 4)]:
            for u in [F(-7, 8), F(0), F(7, 8)]:
                for n in [1, m + 1, m + 2, m + 15, m + 60]:
                    r = source(n, u)
                    t = shadow_source(n, m, k, u)
                    self.assertGreater(t, 0)
                    self.assertLessEqual(t, r)
                    self.assertLessEqual((r - t) / r, relative_error_bound(m, k))

    def test_exact_exponential_defect_formula_and_bound(self):
        for m, k in [(0, 2), (3, 1), (8, 3)]:
            for n in [m + 1, m + 4, m + 17, m + 41]:
                ell = k + n - m - 1
                defect = source(n) - shadow_source(n, m, k)
                rhs = source(n + ell) / 16 ** ell + source(n + ell + 1) / 16 ** (ell + 1)
                self.assertEqual(defect, rhs)
                self.assertLess(defect, F(17, 16 ** (ell + 1)) * source(n))

    def test_shift_derivatives_are_not_confused_with_s_derivatives(self):
        for order in range(5):
            for n in [7, 12, 29]:
                m, k = 6, 2
                ell = k + n - m - 1
                expected = (source_derivative(n, order) - source_derivative(n + ell, order) / 16 ** ell
                            - source_derivative(n + ell + 1, order) / 16 ** (ell + 1))
                self.assertEqual(shadow_source_derivative(n, order, m, k), expected)

    def test_finite_boundary_sum_certificate(self):
        for m, k in [(0, 1), (4, 3), (9, 2)]:
            q = boundary(m, k)
            for n in [m + 1, m + 5, m + 20]:
                finite_sum = sum((shadow_source(j, m, k) / 16 ** j for j in range(1, n + 1)), F(0))
                d = truncated_tail(n, tail_length(n, m, k))
                self.assertEqual(q - finite_sum, d / 16 ** n)
                self.assertGreater(q - finite_sum, 0)
                self.assertLess(d, F(1, (8 * n + 1) ** 2))

    def test_rational_boundary_annihilates_a_nonzero_character(self):
        for m, k in [(0, 1), (2, 3), (7, 2)]:
            q = boundary(m, k)
            h = q.denominator
            for n in [1, m + 1, m + 9, m + 35]:
                d = truncated_tail(n, tail_length(n, m, k))
                self.assertEqual(turns(h * orbit(n, m, k)), turns(-h * d))
                self.assertEqual(turns(h * 16 ** n * q), 0)

    def test_entire_remainder_is_nonzero_at_real_arguments(self):
        # A negative partial sum is a sign calibration; convergence is proved on paper.
        for s in [-7, -3, -1, 0, 2, 5]:
            earlier = dirichlet_defect_partial(s, 8, 3, 2)
            later = dirichlet_defect_partial(s, 16, 3, 2)
            self.assertLess(later, earlier)
            self.assertLess(earlier, 0)

    def test_minimal_member_has_literal_carry_3_then_2_forever(self):
        self.assertEqual(boundary(0, 1), F(47, 240))
        previous = F(0)
        for n in range(1, 81):
            r = shadow_source(n, 0, 1)
            self.assertEqual(r, source(n) - source(2 * n) / 16 ** n
                             - source(2 * n + 1) / 16 ** (n + 1))
            current = 16 * previous + r
            literal = (16 * turns(previous) + r).__floor__()
            self.assertEqual(literal, 3 if n == 1 else 2)
            self.assertEqual(turns(current), F(2, 15) - truncated_tail(n, n + 1))
            previous = current

    def test_wrong_terminal_sign_is_rejected(self):
        m, k, n = 4, 2, 7
        ell = k + n - m - 1
        incorrect = source(n) - source(n + ell) / 16 ** ell + source(n + ell + 1) / 16 ** (ell + 1)
        d_previous = truncated_tail(n - 1, tail_length(n - 1, m, k))
        d_current = truncated_tail(n, tail_length(n, m, k))
        self.assertNotEqual(incorrect, 16 * d_previous - d_current)

    def test_invalid_parameters_fail_closed(self):
        for m, k in [(-1, 1), (1, 0), (0, -2)]:
            with self.assertRaises(ValueError):
                boundary(m, k)
        with self.assertRaises(ValueError):
            source(0)
        with self.assertRaises(ValueError):
            source(1, F(-1))


if __name__ == "__main__":
    unittest.main()
