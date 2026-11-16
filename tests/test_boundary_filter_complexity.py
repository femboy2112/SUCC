"""Calibration and hostile cases for finite boundary-rank certificates."""
import unittest
from fractions import Fraction as Q

from observational_succ.boundary_filter_complexity import (
    certify_bbp_boundary_rank, completed_source_interval,
    gram_from_phase_intervals, sqrt_upper,
)
from observational_succ.duck_bbp import forcing, lifted_orbit, tail_interval


class BoundaryFilterComplexityTests(unittest.TestCase):
    def test_source_four_poles(self):
        for n in range(1, 65):
            self.assertEqual(forcing(n), Q(4, 8*n-7)-Q(2, 8*n-4)-Q(1, 8*n-3)-Q(1, 8*n-2))

    def test_source_matches_lift_and_local_tail(self):
        for n in (0, 1, 7, 19):
            horizon = 25
            low, high = completed_source_interval(horizon)
            tl, th = tail_interval(n, horizon-n)
            self.assertEqual(16**n*low, lifted_orbit(n)+tl)
            self.assertEqual(16**n*high, lifted_orbit(n)+th)

    def test_sqrt_outward_and_sharp_grid(self):
        for q in (Q(), Q(1), Q(2), Q(1, 3), Q(81, 16), Q(1, 10**50)):
            root = sqrt_upper(q, 40)
            self.assertGreaterEqual(root*root, q)
            if root:
                self.assertLess((root-Q(1, 2**40))**2, q)

    def test_coherent_zero_fails_rank(self):
        _, lower = gram_from_phase_intervals([(Q(), Q())]*8, 2)
        self.assertEqual(lower, 0)

    def test_nonzero_fixed_point_fails_rank(self):
        _, lower = gram_from_phase_intervals([(Q(1, 15), Q(1, 15))]*8, 2)
        self.assertEqual(lower, 0)

    def test_period_two_fails_three_columns(self):
        phases = [(Q(16**n % 17, 17),)*2 for n in range(8)]
        _, lower = gram_from_phase_intervals(phases, 2)
        self.assertEqual(lower, 0)

    def test_uniform_grid_positive_control(self):
        # Distinct exponents 1,16,256 modulo 257 give exact orthogonality.
        phases = [(Q(n, 257),)*2 for n in range(257)]
        _, lower = gram_from_phase_intervals(phases, 2)
        self.assertGreater(lower, Q(999, 1000))

    def test_authentic_window_positive(self):
        cert = certify_bbp_boundary_rank(17, 17, 1)
        self.assertEqual(cert.verdict, "FULL_COLUMN_RANK")
        self.assertGreater(cert.eigenvalue_lower, 0)

    def test_hermitian_intervals_and_exact_diagonal(self):
        gram, _ = gram_from_phase_intervals([(Q(1, 9),)*2, (Q(4, 9),)*2], 2)
        for j in range(3):
            self.assertEqual((gram[j][j].real_low, gram[j][j].real_high), (1, 1))
            for k in range(3):
                self.assertEqual(gram[j][k].real_low, gram[k][j].real_low)
                self.assertEqual(gram[j][k].imag_low, -gram[k][j].imag_high)

    def test_negative_harmonic_conjugates(self):
        phases = [(Q(1, 7),)*2, (Q(2, 7),)*2]
        pos, _ = gram_from_phase_intervals(phases, 1)
        neg, _ = gram_from_phase_intervals(phases, 1, -1)
        self.assertLessEqual(neg[0][1].imag_low, -pos[0][1].imag_low)
        self.assertGreaterEqual(neg[0][1].imag_high, -pos[0][1].imag_high)

    def test_wide_interval_inconclusive(self):
        _, lower = gram_from_phase_intervals([(Q(), Q(1))], 2)
        self.assertEqual(lower, 0)

    def test_reject_float_reversed_and_bool(self):
        for phases in ([], [(0.0, 0.0)], [(Q(1), Q())]):
            with self.assertRaises(ValueError):
                gram_from_phase_intervals(phases, 1)
        for args in ((True, 2, 1), (0, 0, 1), (0, 2, -1)):
            with self.assertRaises(ValueError):
                certify_bbp_boundary_rank(*args)
        with self.assertRaises(ValueError):
            certify_bbp_boundary_rank(0, 1, 1, lookahead=8192)


if __name__ == "__main__":
    unittest.main()
