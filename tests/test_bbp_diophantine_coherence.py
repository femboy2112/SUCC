"""Exact independent checks of the finite core, not asymptotic pi tests."""
import unittest
from fractions import Fraction as Q

from observational_succ.bbp_diophantine_coherence import (
    ARC_PARAMETER, BLOCK_LOSS, approximation_coefficient_bound,
    authentic_block_certificate, ceil_log, circle_distance,
    conditional_budget, diophantine_scale_comparison, floor_log,
    inverse_seed_certificate, prescribed_width, terminal_control_loss_upper,
    terminal_zero_control, uniform_threshold_comparison, usable_block_count,
)


def literal_forcing(n):
    return Q(4, 8*n-7)-Q(2, 8*n-4)-Q(1, 8*n-3)-Q(1, 8*n-2)


def independent_history(end, initial=Q()):
    history = [initial]
    for n in range(1, end+1):
        history.append(16*history[-1]+literal_forcing(n))
    return history


class ExactInverseCertificates(unittest.TestCase):
    def test_literal_source_full_lifts_and_backward_identity(self):
        for m, h in ((1, 1), (3, -2), (7, 5), (17, -289)):
            c = authentic_block_certificate(m, h)
            history = independent_history(8*m)
            self.assertEqual(c.inverse.initial, history[m+1])
            self.assertEqual(c.terminal_state, history[-1])
            self.assertEqual(c.inverse.forcing,
                             tuple(literal_forcing(n) for n in range(m+2, 8*m+1)))
            self.assertEqual(c.backward_identity_defect, 0)
            self.assertTrue(c.authentic_zero_anchor)
            self.assertEqual(c.inverse.observations, 7*m)
            self.assertEqual(c.inverse.absolute_loss_threshold, BLOCK_LOSS)

    def test_held_out_authentic_arc_exclusions(self):
        # Finite witnesses only. These do not establish the all-m threshold.
        for m, h in ((23, -17), (23, 529), (37, 1), (37, -1369)):
            c = authentic_block_certificate(m, h)
            self.assertTrue(c.inverse.outside_arcs)
            self.assertLess(c.inverse.branch_span, Q(919, 1600))
            self.assertEqual(c.inverse.normalized_loss_threshold, Q(1, 8750*m))

    def test_grid_compression_against_all_centers(self):
        forcing = tuple(literal_forcing(n) for n in range(11, 16))
        for h in (-3, -1, 2):
            c = inverse_seed_certificate(Q(19, 47), forcing, h)
            grid = 15*abs(h)
            exhaustive = min(circle_distance(c.initial+c.weighted_source-Q(j, grid))
                             for j in range(grid))
            self.assertEqual(c.distance_to_centers, exhaustive)

    def test_exact_arc_boundaries_and_lifts(self):
        forcing = (Q(1, 113), Q(1, 127), Q(1, 149))
        source = sum((r*Q(1, 16**j) for j, r in enumerate(forcing, 1)), Q())
        for h in (-2, 3):
            reference = inverse_seed_certificate(0, forcing, h)
            radius = reference.arc_radius
            for j in range(15*abs(h)):
                center = Q(j, 15*abs(h))-source
                for sign in (-1, 1):
                    inside = inverse_seed_certificate(center+sign*radius+7, forcing, h)
                    outside = inverse_seed_certificate(center+sign*2*radius-9, forcing, h)
                    self.assertEqual(inside.distance_to_centers, radius)
                    self.assertFalse(inside.outside_arcs)
                    self.assertTrue(outside.outside_arcs)

    def test_negative_frequency_and_signed_forcing_symmetry(self):
        forcing = (Q(-1, 101), Q(-1, 113), Q(-1, 127))
        a = inverse_seed_certificate(Q(7, 31), forcing, 2)
        b = inverse_seed_certificate(Q(7, 31), forcing, -2)
        self.assertEqual(a.distance_to_centers, b.distance_to_centers)
        self.assertEqual(a.arc_radius, b.arc_radius)
        self.assertEqual(a.branch_span, b.branch_span)

    def test_zero_forcing_and_rational_fixed_phase_remain_inside(self):
        for h in (1, -3):
            for initial in (Q(), Q(1, 15), Q(7, 15)):
                c = inverse_seed_certificate(initial, (0,)*11, h)
                self.assertFalse(c.outside_arcs)
                self.assertEqual(c.distance_to_centers, 0)
                self.assertEqual((16**11-1)*initial % 1, 0)

    def test_same_forcing_changed_anchor_is_rejected_and_coherent(self):
        for m in (3, 7, 19):
            c = terminal_zero_control(m)
            self.assertFalse(c.authentic_zero_anchor)
            self.assertLess(c.source_initial, 0)
            self.assertEqual(c.terminal_state, 0)
            self.assertEqual(c.backward_identity_defect, 0)
            self.assertEqual(c.inverse.distance_to_centers, 0)
            self.assertFalse(c.inverse.outside_arcs)
            self.assertLess(terminal_control_loss_upper(m), BLOCK_LOSS)
            history = independent_history(8*m, c.source_initial)
            self.assertEqual(history[m+1], c.inverse.initial)
            self.assertEqual(history[-1], 0)
            for n in range(m+1, 8*m+1):
                self.assertLess(abs(history[n]), Q(1, 64*n*n))

    def test_single_impulse_cannot_masquerade_as_authentic_source(self):
        c = terminal_zero_control(7)
        original = independent_history(56)
        changed = independent_history(56, c.source_initial)
        # Reproduce the changed orbit from zero with an impulse at n=1.
        impulse = 16*c.source_initial
        state = literal_forcing(1)+impulse
        self.assertNotEqual(state, original[1])
        self.assertEqual(state, changed[1])
        for n in range(2, 57):
            state = 16*state+literal_forcing(n)
            self.assertEqual(state, changed[n])
        self.assertNotEqual(impulse, 0)


class DiophantineArithmeticAndBudgets(unittest.TestCase):
    def test_approximation_constant_is_uniform_and_strict(self):
        self.assertEqual(approximation_coefficient_bound(1), Q(1648007, 4704000))
        for m in (1, 2, 11, 127, 65537):
            for h in (1, -3, m*m):
                coefficient = approximation_coefficient_bound(m, h)
                self.assertLess(coefficient, 1)
                self.assertLessEqual(coefficient, Q(1648007, 4704000))

    def test_scale_comparison_has_no_pi_or_float_oracles(self):
        for m, h, constant in ((64, 4096, Q(1)), (64, 4096, Q(1, 10**20)),
                               (128, -16384, Q(1, 10**20))):
            q = 15*abs(h)*16**m
            # Independently compare squared errors before cancelling powers.
            direct = Q(1, 16**(16*m)) < constant**2/Q(q**15)
            self.assertEqual(diophantine_scale_comparison(m, h, constant), direct)
        self.assertTrue(uniform_threshold_comparison(64, 1))
        self.assertFalse(uniform_threshold_comparison(64, Q(1, 10**20)))
        self.assertTrue(uniform_threshold_comparison(128, Q(1, 10**20)))

    def test_polynomial_exponential_ratio_monotonicity_witnesses(self):
        for m in (64, 65, 127, 1024, 65537):
            self.assertGreater(16*m**30, (m+1)**30)
            self.assertGreater(16*(1-Q(30, m+1)), 1)

    def test_integer_log_boundaries(self):
        for base in (8, 64):
            for exponent in range(1, 10):
                power = base**exponent
                self.assertEqual(floor_log(power-1, base), exponent-1)
                self.assertEqual(floor_log(power, base), exponent)
                self.assertEqual(ceil_log(power, base), exponent)
                self.assertEqual(ceil_log(power+1, base), exponent+1)

    def test_block_counts_against_independent_enumeration(self):
        for n in (1, 7, 8, 63, 64, 511, 512, 4096, 100000):
            for h in (1, 2, 64, 65, 4096):
                for j0 in (0, 1, 3, 7):
                    starts = [8**j for j in range(20)
                              if 8**(j+1) <= n and j >= j0 and 64**j >= h]
                    self.assertEqual(usable_block_count(n, h, j0), len(starts))
                    self.assertLessEqual(sum(7*m for m in starts), n)

    def test_prescribed_schedule_and_finite_matrix_weight_sum(self):
        for n in (1, 2, 8, 64, 100, 1024, 65536):
            h = prescribed_width(n)
            self.assertLessEqual((h-1)**2, n)
            self.assertGreater(h*h, n)
            b = conditional_budget(n, h, 2)
            direct = sum((Q(2*(h-j), h)*(b.fourier_modulus_upper/n)**2
                          for j in range(1, h)), Q())
            self.assertEqual(b.normalized_purity_upper, direct)
            self.assertFalse(b.threshold_numerically_certified)
            self.assertIn("conditional", b.authority)
            self.assertEqual(b.fourier_modulus_upper, n-BLOCK_LOSS*b.usable_blocks)

    def test_quarter_log_frequency_cost(self):
        for n in (8**4, 8**7+17, 8**12-1, 8**16):
            h = prescribed_width(n)-1
            count = usable_block_count(n, h, 2)
            j = floor_log(n, 8)
            self.assertGreaterEqual(count, Q(3*j, 4)-4)

    def test_reject_inexact_or_out_of_domain_inputs(self):
        for initial in (0.1, True):
            with self.assertRaises(ValueError):
                inverse_seed_certificate(initial, (0,))
        for forcing in ((), (0.1,), (0, 1)):
            with self.assertRaises(ValueError):
                inverse_seed_certificate(0, forcing)
        for h in (0, True, 1.0):
            with self.assertRaises(ValueError):
                inverse_seed_certificate(0, (0,), h)
        with self.assertRaises(ValueError):
            inverse_seed_certificate(0, (0,), arc_parameter=Q(1, 34))
        with self.assertRaises(ValueError):
            authentic_block_certificate(2, 5)
        with self.assertRaises(ValueError):
            authentic_block_certificate(129)
        with self.assertRaises(ValueError):
            uniform_threshold_comparison(63, 1)
        with self.assertRaises(ValueError):
            diophantine_scale_comparison(64, 1, Q())
        with self.assertRaises(ValueError):
            conditional_budget(0, 2, 0)


if __name__ == "__main__":
    unittest.main()
