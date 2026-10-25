"""Calibrated finite controls for gamma/character Tauberian interfaces."""
from fractions import Fraction as Q
import unittest

from observational_succ.bbp_source_memory import forcing, tail_interval
from observational_succ.gamma_character_bridge import (
    clock_total_variation_lower, dilation_path,
    dirichlet_clock_prefix_upper, dyadic_control_signed_count,
    dyadic_log_periodic_sign, geometric_clock_prefix_mass, harmonic_window,
    source_character_dirichlet_tail_bound, source_character_point_bound,
    source_character_window_bound, source_character_window_envelope,
)


class GammaCharacterBridgeTests(unittest.TestCase):
    def test_oriented_harmonic_window_cocycle(self):
        values = [Q((n*n + 3*n) % 11 - 5, 7) for n in range(1, 257)]
        for start in (Q(1), Q(7, 3), Q(9)):
            for u, v in ((3, -1), (-2, 3), (0, 0), (-1, -1)):
                path = dilation_path(u, v)
                terms = [harmonic_window(values, start*a, start*b)
                         for a, b in zip(path, path[1:])]
                direct = harmonic_window(values, start, start*path[-1])
                self.assertEqual(sum(terms, Q()), direct)
                self.assertEqual(harmonic_window(values, start*path[-1], start),
                                 -direct)

    def test_source_unchanged_against_independent_four_poles(self):
        for n in range(1, 129):
            direct = Q(4, 8*n-7)-Q(2, 8*n-4)-Q(1, 8*n-3)-Q(1, 8*n-2)
            self.assertEqual(forcing(n), direct)
        for n in (1, 2, 3, 8, 16, 64, 127):
            lo, hi = tail_interval(n, 6)
            self.assertTrue(0 < lo < hi < Q(1, 64*n*n))
            self.assertLess(Q(44, 7)*hi, source_character_point_bound(n))
        # A false factor-two tightening fails on the genuine source.
        self.assertGreater(tail_interval(64, 6)[0], Q(1, 128*64*64))

    def test_window_bound_and_analytic_envelope(self):
        for n in (1, 2, 7, 23, 64):
            for p in (2, 3, 5):
                bound = source_character_window_bound(n, p)
                actual_tail_upper = sum((Q(44, 7)*tail_interval(k, 3)[1]/k
                                        for k in range(n+1, p*n+1)), Q())
                self.assertLess(actual_tail_upper, bound)
                self.assertLess(bound, source_character_window_envelope(n, p))
                self.assertEqual(source_character_window_bound(n, p, -3), 3*bound)
        self.assertEqual(source_character_window_envelope(7, 2), Q(33, 896*49))
        self.assertEqual(source_character_window_envelope(7, 3), Q(11, 252*49))
        self.assertEqual(source_character_window_envelope(7, 3, 0), 0)

    def test_dirichlet_transport_tail(self):
        for m in (1, 4, 17):
            for sigma in range(4):
                finite = sum((source_character_point_bound(n)/n**sigma
                              for n in range(m+1, 8*m+1)), Q())
                self.assertLess(finite, source_character_dirichlet_tail_bound(m, sigma))
                self.assertEqual(source_character_dirichlet_tail_bound(m, sigma, -2),
                                 2*source_character_dirichlet_tail_bound(m, sigma))

    def test_gamma_clocks_are_separated_not_interchangeable(self):
        for epsilon in (Q(1, 3), Q(1, 7), Q(1, 16)):
            for m in (0, 1, 5, 30):
                finite = sum((epsilon*(1+epsilon)**(-n)
                              for n in range(1, m+1)), Q())
                self.assertEqual(finite, geometric_clock_prefix_mass(epsilon, m))
                self.assertEqual(finite + (1+epsilon)**(-m), 1)
        # The event n<=eps^-2 already separates over 4/5 of the probability.
        self.assertGreater(clock_total_variation_lower(Q(1, 64), 4096), Q(4, 5))
        self.assertEqual(dirichlet_clock_prefix_upper(Q(1), 3), 1)

    def test_one_prime_control_rejects_a_false_tauberian_theorem(self):
        values = [dyadic_log_periodic_sign(n) for n in range(1, 6145)]
        prefix = [Q()]
        total = 0
        for n, value in enumerate(values, 1):
            total += value
            prefix.append(prefix[-1]+Q(value, n))
            self.assertEqual(total, dyadic_control_signed_count(n))
        for n in range(1, 2049):
            # Riemann-sum bounded variation gives the PAPER all-N bound 5/N.
            self.assertLessEqual(abs(prefix[2*n]-prefix[n]), Q(5, n))
        # Tripling detects this exact same coefficient sequence.
        for n in (256, 512, 1024, 2048):
            self.assertGreater(prefix[3*n]-prefix[n], Q(1, 4))
        # Large exact block counts stay away from zero while doubling passes.
        for power in (12, 24, 48, 80):
            n = 2**power - 1
            mean = Q(dyadic_control_signed_count(n), n)
            self.assertTrue(-Q(1, 5) < mean < -Q(1, 6))

    def test_negative_and_null_controls(self):
        zeros = [0]*30
        self.assertEqual(harmonic_window(zeros, 3, 19), 0)
        self.assertEqual(source_character_point_bound(3, 0), 0)
        for call in (
            lambda: harmonic_window([1, 2], 0, 3),
            lambda: harmonic_window([1, 2], -1, 1),
            lambda: harmonic_window([1.0], 0, 1),
            lambda: source_character_point_bound(0),
            lambda: source_character_point_bound(1, 1.0),
            lambda: source_character_window_bound(1, 1),
            lambda: source_character_dirichlet_tail_bound(1, -1),
            lambda: geometric_clock_prefix_mass(0, 10),
            lambda: dirichlet_clock_prefix_upper(Q(-1, 2), 10),
            lambda: dilation_path(1.0, 2),
            lambda: dyadic_log_periodic_sign(0),
        ):
            with self.assertRaises(ValueError):
                call()


if __name__ == "__main__":
    unittest.main()
