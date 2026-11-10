"""Independent exact oracles and hostile controls for the Cayley instrument."""

from fractions import Fraction as Q
from math import comb
import unittest

from observational_succ.cayley_source_observer import (
    ProjectivePoint,
    band_phase_error_coefficient,
    cayley_mode,
    common_horizon_epoch_linear_bound,
    common_horizon_epoch_log_bound,
    common_horizon_epoch_phase_bound,
    coupled_horizon,
    projective_power,
    projective_rotate,
    quadratic_resonance_frequency,
    resonance_chord_lower_bound,
    resonance_turn_interval,
    source_completed_interval,
    source_phase_error_coefficient,
)


def four_poles(n):
    return Q(4, 8*n-7)-Q(2, 8*n-4)-Q(1, 8*n-3)-Q(1, 8*n-2)


def binomial_components(point, degree):
    real = sum((Q((-1)**(j//2)*comb(degree, j))*point.x**(degree-j)*point.y**j
                for j in range(0, degree+1, 2)), Q())
    imag = sum((Q((-1)**((j-1)//2)*comb(degree, j))*point.x**(degree-j)*point.y**j
                for j in range(1, degree+1, 2)), Q())
    return real, imag


class CayleyProjectiveTests(unittest.TestCase):
    def test_homogeneous_gauge_and_infinity(self):
        self.assertEqual(ProjectivePoint(-6, 15), ProjectivePoint(2, -5))
        self.assertEqual(ProjectivePoint(0, -7), ProjectivePoint(0, 1))
        for h in range(-6, 7):
            self.assertEqual(cayley_mode(ProjectivePoint(0, 1), h), (Q((-1)**h), Q()))

    def test_power_against_independent_binomial_oracle(self):
        points = [ProjectivePoint(1, 0), ProjectivePoint(0, 1),
                  ProjectivePoint(3, 5), ProjectivePoint(-7, 2)]
        for point in points:
            for degree in (1, 2, 3, 8, 16, 17):
                expected = ProjectivePoint(*binomial_components(point, degree))
                self.assertEqual(projective_power(point, degree), expected)

    def test_power_intertwines_every_tested_signed_mode(self):
        for point in [ProjectivePoint(1, 2), ProjectivePoint(2, -3), ProjectivePoint(0, 1)]:
            for degree in (2, 3, 16):
                for h in (-3, -1, 0, 1, 4):
                    self.assertEqual(cayley_mode(projective_power(point, degree), h),
                                     cayley_mode(point, degree*h))

    def test_radix_map_is_defined_at_tangent_poles(self):
        infinity = ProjectivePoint(0, 1)
        self.assertEqual(projective_power(ProjectivePoint(1, 1), 2), infinity)
        self.assertEqual(projective_power(infinity, 16), ProjectivePoint(1, 0))
        self.assertEqual(projective_power(infinity, 3), infinity)

    def test_rotation_mode_product_and_negative_gauge(self):
        point, rotation = ProjectivePoint(2, 3), ProjectivePoint(5, -1)
        rotated = projective_rotate(point, rotation)
        self.assertEqual(rotated, ProjectivePoint(13, 13))
        for h in (-5, 0, 4):
            a, b = cayley_mode(point, h)
            c, d = cayley_mode(rotation, h)
            self.assertEqual(cayley_mode(rotated, h), (a*c-b*d, a*d+b*c))

    def test_invalid_exact_inputs_fail_closed(self):
        for args in ((0, 0), (0.5, 1), (True, 1), (1, "2")):
            with self.assertRaises(ValueError):
                ProjectivePoint(*args)
        for degree in (0, -1, True, 2.0):
            with self.assertRaises(ValueError):
                projective_power(ProjectivePoint(1, 2), degree)
        for frequency in (True, 0.5):
            with self.assertRaises(ValueError):
                cayley_mode(ProjectivePoint(1, 2), frequency)


class SourceClockTests(unittest.TestCase):
    def test_prefix_certificate_against_independent_four_poles(self):
        for horizon in (0, 1, 3, 8, 17):
            prefix = sum((four_poles(j)/16**j for j in range(1, horizon+1)), Q())
            tail = four_poles(horizon+1)/(15*16**horizon)
            for time in (0, horizon):
                self.assertEqual(source_completed_interval(time, horizon),
                                 (16**time*prefix, 16**time*(prefix+tail)))

    def test_strict_nesting_and_finite_naturality(self):
        for time in range(6):
            for horizon in range(time, time+4):
                a, b = source_completed_interval(time, horizon)
                c, d = source_completed_interval(time, horizon+1)
                self.assertLess(a, c)
                self.assertLess(d, b)
                if time < horizon:
                    self.assertEqual((16*a, 16*b), source_completed_interval(time+1, horizon))

    def test_actual_source_square_and_zero_seed(self):
        state = Q()
        for time in range(9):
            if time:
                state = 16*state+four_poles(time)
            for horizon in (time, time+2, time+4):
                finite_tail = sum((four_poles(j)/16**(j-time)
                                   for j in range(time+1, horizon+1)), Q())
                self.assertEqual(state+finite_tail, source_completed_interval(time, horizon)[0])

    def test_band_payment_controls_each_time_and_signed_frequency(self):
        n, horizon, cutoff = 8, 11, 72
        paid = band_phase_error_coefficient(n, horizon, cutoff)
        for time in range(n+1):
            a, b = source_completed_interval(time, horizon)
            for frequency in (-72, -8, 0, 7, 72):
                coefficient = source_phase_error_coefficient(time, horizon, frequency)
                self.assertEqual(coefficient, abs(frequency)*(b-a))
                self.assertLessEqual(coefficient, paid)

    def test_coupled_horizon_is_minimal_and_finite(self):
        for time, cutoff, tolerance in [(0, 0, Q(1, 100)), (3, 10**6, Q(1, 10000)),
                                        (20, 32*20**2, Q(1, 10**8))]:
            horizon = coupled_horizon(time, cutoff, tolerance)
            self.assertLessEqual(band_phase_error_coefficient(time, horizon, cutoff), tolerance)
            if horizon > time:
                self.assertGreater(band_phase_error_coefficient(time, horizon-1, cutoff), tolerance)

    def test_quadratic_hostile_mode_has_certified_near_maximal_error(self):
        # A rational enclosure plus an analytic chord inequality, not floating pi.
        lower = resonance_chord_lower_bound(128, 12)
        self.assertGreater(lower, Q(99, 50))
        turns = resonance_turn_interval(128, 12)
        self.assertLess(turns[0], turns[1])
        self.assertLess(turns[1], Q(1, 2))
        self.assertEqual(quadratic_resonance_frequency(128), 524288)
        self.assertGreater(resonance_chord_lower_bound(128, 12),
                           resonance_chord_lower_bound(8, 12))

    def test_cofinal_clocks_without_coupling_do_not_pay(self):
        # L_n=n and H_n=32*n^2 both grow, but their bound does not approach zero.
        for time in (8, 32, 128):
            self.assertGreater(band_phase_error_coefficient(time, time, 32*time*time), Q(2, 5))
            self.assertLess(band_phase_error_coefficient(time, time, time), Q(1, time))

    def test_circle_observer_does_not_authenticate_seed(self):
        original = shifted = Q()
        shifted = Q(1, 16)
        for n in range(1, 9):
            original = 16*original+four_poles(n)
            shifted = 16*shifted+four_poles(n)
            self.assertEqual(shifted-original, 16**(n-1))
            self.assertEqual(shifted % 1, original % 1)
        # Losing the lift is the reason; increasing the oscillator band cannot fix it.

    def test_common_horizon_clipping_against_literal_sum(self):
        for start in (1, 2, 7, 32):
            for cutoff in (0, 1, start**2, 16**start, 16**(2*start)):
                scale = 7*cutoff*four_poles(2*start+1)/15
                expected = sum((min(Q(2), scale/16**j)
                                for j in range(1, start+1)), Q())/start
                self.assertEqual(common_horizon_epoch_phase_bound(start, cutoff), expected)
                self.assertLessEqual(expected, common_horizon_epoch_linear_bound(start, cutoff))
                threshold, log_bound = common_horizon_epoch_log_bound(start, cutoff)
                self.assertLessEqual(expected, log_bound)
                self.assertLessEqual(scale/16**threshold, 2)
                if threshold:
                    self.assertGreater(scale/16**(threshold-1), 2)

    def test_common_horizon_controls_each_certificate(self):
        start, cutoff = 13, 10**8
        literal = Q()
        for time in range(start, 2*start):
            a, b = source_completed_interval(time, 2*start)
            literal += min(Q(2), 7*cutoff*(b-a))
        self.assertEqual(literal/start, common_horizon_epoch_phase_bound(start, cutoff))
        self.assertEqual(common_horizon_epoch_phase_bound(start, 0), 0)

    def test_common_horizon_accepts_subexponential_high_bands(self):
        # H=16**sqrt(A) is far above A**2; the finite logarithmic payment
        # decreases on these square epochs.  The all-A statement has a proof.
        bounds = [common_horizon_epoch_log_bound(m*m, 16**m)[1] for m in (8, 16, 32)]
        self.assertGreater(bounds[0], bounds[1])
        self.assertGreater(bounds[1], bounds[2])
        self.assertLess(bounds[-1], Q(1, 16))
        for args in ((0, 1), (-1, 1), (2, -1), (True, 4), (1, 2.0)):
            with self.assertRaises(ValueError):
                common_horizon_epoch_phase_bound(*args)

    def test_clock_validation_rejects_tautological_or_bad_inputs(self):
        for args in ((2, 1, 3), (True, 3, 4), (0, 0, -1), (0, 1, 1.5)):
            with self.assertRaises(ValueError):
                band_phase_error_coefficient(*args)
        for tolerance in (0, -1, 0.1, True):
            with self.assertRaises(ValueError):
                coupled_horizon(1, 4, tolerance)


if __name__ == "__main__":
    unittest.main()
