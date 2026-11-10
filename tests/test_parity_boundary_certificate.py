"""Hostile finite checks; analytic quantifiers live in the accompanying proofs."""
import unittest
from fractions import Fraction as Q
from math import floor

import mpmath as mp

from observational_succ import parity_boundary_certificate as p


class SourceEnclosureTests(unittest.TestCase):
    def test_reduced_endpoint_alias_is_not_a_digit_certificate(self):
        self.assertIsNone(p.PhaseEnclosure(Q(0), Q(1)).digit())
        self.assertIsNone(p.PhaseEnclosure(Q(31, 32), Q(33, 32)).digit())
        self.assertIsNone(p.PhaseEnclosure(Q(1, 16), Q(2, 16)).digit())
        self.assertEqual(p.PhaseEnclosure(Q(19, 16), Q(39, 32)).digit(), 3)

    def test_adaptive_certificate_and_explicit_budget(self):
        digit, depth, iv = p.certified_source_digit(0, initial_depth=0)
        self.assertEqual(digit, 3)
        self.assertGreater(depth, 0)
        self.assertEqual(iv.digit(), 3)
        with self.assertRaises(RuntimeError):
            p.certified_source_digit(0, initial_depth=0, max_depth=0)

    def test_common_horizon_is_exact_source_orbit(self):
        intervals = p.common_horizon_enclosures(13, 29)
        for a, b in zip(intervals, intervals[1:]):
            self.assertEqual(16*a.lo % 1, b.lo % 1)
            self.assertEqual(16*a.radius, b.radius)
        local = p.source_phase_enclosures(13, 20)
        for a, b in zip(intervals, local):
            # The narrower independent local certificate has the same digit.
            self.assertEqual(a.digit(), b.digit())

    def test_all_sixteen_boundaries_include_cayley_infinity(self):
        for j in range(16):
            self.assertEqual(p.distance_to_digit_boundary(Q(j, 16)), 0)
            self.assertEqual(p.distance_to_digit_boundary(Q(j, 16)+Q(1, 64)), Q(1, 64))
        self.assertEqual(p.distance_to_digit_boundary(Q(1, 2)), 0)

    def test_invalid_exact_inputs(self):
        with self.assertRaises(TypeError):
            p.PhaseEnclosure(0.1, 0.2)
        with self.assertRaises(ValueError):
            p.common_horizon_enclosures(5, 8)
        with self.assertRaises(ValueError):
            p.source_phase_enclosures(True)
        with self.assertRaises(ValueError):
            p.fejer_error_budget([p.PhaseEnclosure(0, 0)], 8, Q(1, 16))


class FejerCertificateTests(unittest.TestCase):
    @staticmethod
    def _mpq(x):
        return mp.mpf(x.numerator)/x.denominator

    def test_sine_certificate_exact_special_values(self):
        for t, value in ((Q(), 0), (Q(1, 4), 1), (Q(1, 2), 0),
                         (Q(3, 4), -1), (Q(-1, 4), -1)):
            lo, hi = p.sine_turns_enclosure(t)
            self.assertLessEqual(lo, value)
            self.assertGreaterEqual(hi, value)
            self.assertLess(hi-lo, Q(1, 10**12))

    def test_sine_certificate_independent_high_precision_diagnostic(self):
        with mp.workdps(90):
            for t in (Q(1, 113), Q(37, 251), Q(-73, 101), Q(10**80+17, 10**80+51)):
                lo, hi = p.sine_turns_enclosure(t)
                v = mp.sin(2*mp.pi*self._mpq(t % 1))
                self.assertLessEqual(self._mpq(lo), v)
                self.assertGreaterEqual(self._mpq(hi), v)

    def test_sharp_lipschitz_coefficient_and_optimal_grid(self):
        self.assertEqual(p.fejer_lipschitz(7), 0)
        self.assertEqual(p.fejer_lipschitz(8), Q(64, 9))
        for k in range(1, 20):
            H = 16*k-1
            self.assertEqual(p.fejer_lipschitz(H), 2*(H+1))
        for H in range(100):
            self.assertGreaterEqual(p.fejer_lipschitz(H), 0)
            self.assertLessEqual(p.fejer_lipschitz(H), 2*(H+1))

    def test_rational_fejer_interval_contains_independent_sum(self):
        points = (Q(17, 113), Q(-19, 997), Q(1, 2), Q(1, 10**8))
        lo, hi = p.fejer_mean_enclosure(points, 87)
        with mp.workdps(80):
            val = mp.mpf(0)
            for t in points:
                for m in range(8, 88, 16):
                    val += 32/(mp.pi*m)*(1-mp.mpf(m)/88)*mp.sin(2*mp.pi*m*self._mpq(t))
            val /= len(points)
            self.assertLessEqual(self._mpq(lo), val)
            self.assertGreaterEqual(self._mpq(hi), val)
        self.assertLess(hi-lo, Q(1, 10**10))

    def test_uniform_fourier_truncation_mutant_fails(self):
        # A positive phase arbitrarily near a jump has f=+1 but a tiny
        # symmetric Fourier sum.  This refutes a uniform O(1/H) tail.
        t, H = Q(1, 10**9), 1024
        with mp.workdps(50):
            s = sum(32/(mp.pi*m)*mp.sin(2*mp.pi*m*self._mpq(t))
                    for m in range(8, H+1, 16))
            self.assertGreater(abs(1-s), mp.mpf('0.99'))
        budget = p.fejer_error_budget([p.PhaseEnclosure(t, t)], H, Q(1, 10**6))
        self.assertEqual(budget['possible_boundary_count'], 1)
        self.assertEqual(budget['error_bound'], 2)

    def test_full_source_certificate_contains_exact_digit_mean(self):
        intervals = p.source_phase_enclosures(17, 8)
        budget = p.fejer_error_budget(intervals, 127, Q(1, 256))
        lo, hi = p.fejer_mean_enclosure((iv.center for iv in intervals), 127)
        exact = Q(sum((-1)**iv.digit() for iv in intervals), len(intervals))
        self.assertLessEqual(lo-budget['error_bound'], exact)
        self.assertGreaterEqual(hi+budget['error_bound'], exact)

    def test_source_payment_uses_bounded_readout(self):
        intervals = [p.PhaseEnclosure(0, 100), p.PhaseEnclosure(Q(1, 3), Q(1, 3))]
        budget = p.fejer_error_budget(intervals, 255, Q(1, 1024))
        self.assertEqual(budget['clipped_source_payment'], 1)
        self.assertLess(budget['clipped_source_payment'],
                        budget['lipschitz_constant']*budget['mean_radius'])


class StationaryBoundaryTests(unittest.TestCase):
    @staticmethod
    def orbit(start, length):
        out = [start]
        for _ in range(length):
            out.append(16*out[-1] % 1)
        return out

    def test_exact_recursion_and_other_fourteen_fibers(self):
        phases = self.orbit(Q(7, 113), 97)
        receipt = p.stationary_boundary_recursion(phases, 4)
        for row in receipt['rows']:
            self.assertEqual(row['identity_residual'], 0)
            r = row['radius']/16
            # Independent preimage enumeration at all 16 distinct roots.
            count = sum(any(p.circle_distance(8*t % 1, Q(k, 16)) < r
                            for k in range(16) if k not in (0, 8))
                        for t in phases[:-1])
            self.assertEqual(row['other_fourteen_fibers'], Q(count, 97))
        self.assertLessEqual(receipt['boundary_mass'], receipt['upper_bound'])
        self.assertTrue(any(row['other_fourteen_fibers'] > 0 for row in receipt['rows']))

    def test_constant_wrong_orbit_keeps_maximal_boundary_mass(self):
        receipt = p.stationary_boundary_recursion([Q(0)]*17, 5)
        self.assertEqual(receipt['boundary_mass'], 1)
        self.assertEqual(receipt['upper_bound'], 1)
        self.assertTrue(all(row['signed_half_turn_contrast'] == 1 for row in receipt['rows']))

    def test_open_ball_convention_avoids_double_counting(self):
        receipt = p.stationary_boundary_recursion([Q(1, 32), Q(1, 2)], 0)
        self.assertEqual(receipt['initial_boundary_mass'], 0)

    def test_non_orbit_rejected(self):
        with self.assertRaises(ValueError):
            p.stationary_boundary_recursion([Q(1, 3), Q(1, 4)], 2)


if __name__ == '__main__':
    unittest.main()
