import unittest
from fractions import Fraction as Q

from observational_succ.pi_lag_carry import (
    bbp_carry_path, centered, close_run_gate, close_run_interval,
    forcing_gap, forcing_gap_bounds, lag_close_counts, lag_step,
    nonpositive_escape_bound, repeated_clock_pairs,
)
from observational_succ.pi_source_collision import bbp_forcing, prime_window, small_ball_pairs


class PiLagCarryTests(unittest.TestCase):
    def test_source_against_unwrapped_partial_sums(self):
        path = bbp_carry_path(55)
        unwrapped = Q(0)
        integer_lift = 0
        for n in range(1, 56):
            unwrapped += bbp_forcing(n)/16**n
            integer_lift = 16*integer_lift+path.carries[n-1]
            self.assertEqual(16**n*unwrapped, path.states[n]+integer_lift)
            self.assertEqual(path.states[n], (16**n*unwrapped) % 1)

    def test_centered_and_unwrapped_carries(self):
        path = bbp_carry_path(70)
        nonzero_offsets = 0
        for lag in range(1, 18):
            for n in range(70-lag):
                s = lag_step(path, n, lag)
                self.assertEqual(s.raw_next, 16*s.raw-s.forcing_gap-s.source_carry_difference)
                self.assertEqual(s.centered_next, 16*s.centered-s.forcing_gap-s.centered_carry)
                self.assertEqual(s.centered, centered(s.raw))
                nonzero_offsets += s.centering_offset != 0
        self.assertGreater(nonzero_offsets, 0)
        self.assertEqual(centered(Q(1, 2)), -Q(1, 2))

    def test_zero_centered_carry_does_not_erase_source_carries(self):
        # Authentic boundary-crossing witness, checked entirely as Fractions.
        s = lag_step(bbp_carry_path(1305), 1174, 130)
        self.assertLess(abs(s.centered), Q(1, 32))
        self.assertLess(abs(s.centered_next), Q(1, 32))
        self.assertEqual(s.source_carry_difference, 15)
        self.assertEqual((s.centering_offset, s.next_centering_offset), (1, 1))
        self.assertEqual(s.centered_carry, 0)

    def test_source_gap_bounds_and_monotonicity(self):
        for lag in (1, 2, 7, 31):
            for n in range(80):
                f = forcing_gap(n, lag)
                lo, hi = forcing_gap_bounds(n, lag)
                self.assertLess(lo, f)
                self.assertLess(f, hi)
                self.assertGreater(f, forcing_gap(n+1, lag))

    def test_lag_count_independent_all_pairs(self):
        path = bbp_carry_path(100)
        for start, length in ((0, 1), (3, 20), (26, 75)):
            values = path.states[start:start+length]
            for radius in (Q(0), Q(1, 256), Q(1, 16), Q(1, 3)):
                all_pairs = sum(min((a-b) % 1, (b-a) % 1) <= radius
                                for a in values for b in values)
                result = lag_close_counts(path, start, length, radius)
                self.assertEqual(result.ordered_pairs, all_pairs)
                self.assertEqual(result.ordered_pairs, small_ball_pairs(values, radius))

    def test_exact_close_run_cylinder_and_gate(self):
        tau = Q(1, 256)
        for n, lag in ((5, 1), (12, 17), (33, 8)):
            self.assertTrue(close_run_gate(n, lag, tau))
            for steps in (0, 1, 2, 5):
                lo, hi = close_run_interval(n, lag, steps, tau)
                self.assertEqual(hi-lo, 2*tau/16**steps)
                for initial, expected in ((lo, True), (hi, True), ((lo+hi)/2, True),
                                          (lo-Q(1, 16**(steps+8)), False),
                                          (hi+Q(1, 16**(steps+8)), False)):
                    value, close = initial, abs(initial) <= tau
                    for i in range(steps):
                        value = centered(16*value-forcing_gap(n+i, lag))
                        close = close and abs(value) <= tau
                    self.assertEqual(close, expected)
        with self.assertRaises(ValueError):
            close_run_interval(0, 1, 3, tau)

    def test_actual_adjacent_visits_have_zero_centered_carry(self):
        path = bbp_carry_path(100)
        tau, hits = Q(1, 32), 0
        for lag in range(1, 50):
            for n in range(5, 100-lag):
                s = lag_step(path, n, lag)
                if abs(s.centered) <= tau and abs(s.centered_next) <= tau:
                    self.assertLess(17*tau+s.forcing_gap, 1)
                    self.assertEqual(s.centered_carry, 0)
                    hits += 1
        self.assertGreater(hits, 0)

    def test_directional_escape_certificate(self):
        tau = Q(1, 256)
        for n, lag in ((10, 1), (100, 3), (1000, 300)):
            steps = next(k for k in range(1, 30)
                         if nonpositive_escape_bound(n, lag, k, tau))
            lo, _ = close_run_interval(n, lag, steps, tau)
            self.assertGreater(lo, 0)

    def test_clock_count_and_authenticated_nonresonant_denominator(self):
        for length in range(1, 40):
            for period in range(1, 20):
                direct = sum((i-j) % period == 0 for i in range(length) for j in range(length))
                self.assertEqual(repeated_clock_pairs(length, period), direct)
        for p in (17, 41, 73, 97):
            window = prime_window(p)
            self.assertEqual(repeated_clock_pairs(window.length, window.period),
                             window.length**2//window.period)
            for i in range(window.length):
                for j in range(i):
                    difference = window.states[i]-window.states[j]
                    self.assertEqual(difference.denominator % p == 0, (i-j) % window.period != 0)
                    self.assertNotEqual(difference.denominator % (p*p), 0)

    def test_reject_inexact_and_invalid_inputs(self):
        with self.assertRaises(ValueError):
            centered(0.1)
        with self.assertRaises(ValueError):
            bbp_carry_path(True)
        with self.assertRaises(ValueError):
            lag_close_counts(bbp_carry_path(5), 0, 7, Q(1, 16))
        with self.assertRaises(ValueError):
            lag_close_counts(bbp_carry_path(5), 0, 5, Q(1, 2))
        with self.assertRaises(ValueError):
            lag_step(bbp_carry_path(5), 4, 1)


if __name__ == '__main__':
    unittest.main()
