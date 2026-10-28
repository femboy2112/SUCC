"""Exact certificates and hostile controls for the branch-coercivity theorem."""
import unittest
from fractions import Fraction as Q

from observational_succ.bbp_branch_coercivity import (
    BLOCK_LOSS, BRANCH_NORM_SQUARED, COSINE_COERCIVITY, LIFT_RADIUS,
    approximation_coefficient_bound, authentic_block_certificate,
    coercive_inverse_certificate, coercivity_floor, conditional_budget,
    diophantine_scale_comparison, exact_margins, terminal_zero_control,
    transition_difference_coefficients, usable_block_count,
)
from observational_succ.bbp_diophantine_coherence import (
    circle_distance, terminal_control_loss_upper,
)


def literal_history(end, initial=Q()):
    values = [initial]
    forcing = []
    for n in range(1, end+1):
        r = Q(4, 8*n-7)-Q(2, 8*n-4)-Q(1, 8*n-3)-Q(1, 8*n-2)
        forcing.append(r)
        values.append(16*values[-1]+r)
    return values, forcing


class BranchCoercivityFiniteTests(unittest.TestCase):
    def test_rational_margins(self):
        margins = exact_margins()
        self.assertEqual(margins['branch_margin'], Q(2329025, 37950062592))
        self.assertEqual(margins['cosine_margin'], Q(12559091, 51861600))
        self.assertEqual(margins['lift_radius_squared_margin'], Q(7, 52200))
        for key in ('branch_margin', 'cosine_margin', 'lift_radius_squared_margin'):
            self.assertGreater(margins[key], 0)
        self.assertEqual(margins['adjacent_norm_squared'], 546)
        self.assertEqual(margins['separated_norm_squared'], 514)

    def test_independent_transition_vectors_and_sharp_adjacency(self):
        for length in (3, 4, 7, 13, 31):
            for j in range(length-1):
                for k in range(length-1):
                    if j == k:
                        continue
                    got = transition_difference_coefficients(length, j, k)
                    expected = tuple((int(i == j+1)-16*int(i == j)
                                      -int(i == k+1)+16*int(i == k))
                                     for i in range(length))
                    self.assertEqual(got, expected)
                    norm2 = sum(x*x for x in got)
                    self.assertEqual(norm2, 546 if abs(j-k) == 1 else 514)
                    self.assertLessEqual(norm2, BRANCH_NORM_SQUARED)
        # Mutation control: using the disjoint-transition constant universally fails.
        c = transition_difference_coefficients(3, 0, 1)
        self.assertGreater(sum(x*x for x in c), 514)

    def test_cauchy_equality_witnesses_and_invalid_global_cosine_mutant(self):
        for length, j, k in ((3, 0, 1), (5, 0, 3), (9, 7, 2)):
            c = transition_difference_coefficients(length, j, k)
            norm = sum(x*x for x in c)
            q = tuple(Q(x, norm) for x in c)
            self.assertEqual(sum(x*y for x, y in zip(c, q)), 1)
            self.assertEqual(sum(x*x for x in q), Q(1, norm))
        # At q=1/2 the true deficit is exactly 2, not >=19q^2.
        self.assertLess(Q(2), COSINE_COERCIVITY*Q(1, 2)**2)

    def test_authentic_source_zero_anchor_and_holdout_arcs(self):
        for m, h in ((8, 1), (17, -4), (37, 19), (41, -26)):
            c = authentic_block_certificate(m, h)
            history, forcing = literal_history(8*m)
            self.assertTrue(c.authentic_zero_anchor)
            self.assertEqual(c.inverse.initial, history[m+1])
            self.assertEqual(c.terminal_state, history[-1])
            self.assertEqual(c.inverse.forcing, tuple(forcing[m+1:]))
            self.assertEqual(c.backward_identity_defect, 0)
            self.assertEqual(c.inverse.observations, 7*m)
            self.assertEqual(c.inverse.absolute_loss_threshold, BLOCK_LOSS)
            self.assertGreater(c.inverse.distinct_branch_deficit_floor, BLOCK_LOSS)
            self.assertTrue(c.inverse.outside_arcs)

    def test_same_forcing_changed_seed_control(self):
        for m in (8, 17, 37):
            c = terminal_zero_control(m)
            history, forcing = literal_history(8*m, c.source_initial)
            self.assertFalse(c.authentic_zero_anchor)
            self.assertEqual(c.terminal_state, 0)
            self.assertEqual(c.inverse.distance_to_centers, 0)
            self.assertFalse(c.inverse.outside_arcs)
            self.assertEqual(c.inverse.initial, history[m+1])
            self.assertEqual(c.inverse.forcing, tuple(forcing[m+1:]))
            self.assertLess(terminal_control_loss_upper(m), BLOCK_LOSS)

    def test_all_arc_centers_and_exact_boundary(self):
        forcing = (Q(1, 997), Q(1, 1009), Q(1, 1013))
        weighted = sum((r/Q(16**j) for j, r in enumerate(forcing, 1)), Q())
        for h in (-2, 3):
            proto = coercive_inverse_certificate(Q(1, 11), forcing, h)
            grid = 15*abs(h)
            direct = min(circle_distance(proto.initial+weighted-Q(k, grid))
                         for k in range(grid))
            self.assertEqual(proto.distance_to_centers, direct)
            for k in range(grid):
                center = Q(k, grid)-weighted
                boundary = coercive_inverse_certificate(center+proto.arc_radius,
                                                        forcing, h)
                outside = coercive_inverse_certificate(center+2*proto.arc_radius,
                                                       forcing, h)
                self.assertFalse(boundary.outside_arcs)
                self.assertTrue(outside.outside_arcs)

    def test_zero_forcing_fixed_phases(self):
        for h in (-2, 1, 5):
            for initial in (Q(), Q(1, 15), Q(8, 15)):
                c = coercive_inverse_certificate(initial, (0,)*7, h)
                self.assertEqual(c.distance_to_centers, 0)
                self.assertFalse(c.outside_arcs)

    def test_frequency_and_forcing_sign_symmetries(self):
        forcing = (Q(-1, 1001), Q(-1, 1013), Q(-1, 1031))
        a = coercive_inverse_certificate(Q(13, 37), forcing, 2)
        b = coercive_inverse_certificate(Q(13, 37), forcing, -2)
        c = coercive_inverse_certificate(-Q(13, 37), tuple(-r for r in forcing), 2)
        for other in (b, c):
            self.assertEqual(a.arc_radius, other.arc_radius)
            self.assertEqual(a.distance_to_centers, other.distance_to_centers)
            self.assertEqual(a.forcing_span, other.forcing_span)

    def test_uniform_approximation_constant(self):
        self.assertEqual(approximation_coefficient_bound(1), Q(6447953, 2822400))
        for m in (1, 8, 39, 128, 65537):
            for h in (1, -3, m*m):
                self.assertLess(approximation_coefficient_bound(m, h), 3)

    def test_diophantine_comparison_pays_factor_nine(self):
        for m, h, c in ((64, 4096, Q(1)), (64, 4096, Q(1, 10**20)),
                        (128, -16384, Q(1, 10**20))):
            denominator = 15*abs(h)*16**m
            direct = Q(9, 16**(16*m)) < c*c/Q(denominator**15)
            self.assertEqual(diophantine_scale_comparison(m, h, c), direct)
        # Tuned exact boundary: omitting factor 9 reverses this result.
        c = Q(15**8, 2*16**16)
        self.assertGreater(c*c*16**32, 15**15)
        self.assertFalse(diophantine_scale_comparison(32, 1, c))

    def test_block_count_independent_enumeration_and_conditional_status(self):
        for n in (1, 63, 64, 511, 512, 4096, 100000):
            for h in (1, 2, 64, 65, 4096):
                for j0 in (0, 1, 3, 7):
                    starts = [8**j for j in range(20)
                              if 8**(j+1) <= n and j >= j0 and 64*h <= 64**j]
                    got = usable_block_count(n, h, j0)
                    self.assertEqual(got, len(starts))
                    budget = conditional_budget(n, h, j0)
                    self.assertEqual(budget['fourier_modulus_upper'], n-BLOCK_LOSS*got)
                    self.assertFalse(budget['threshold_numerically_certified'])

    def test_domain_and_forcing_mutants_rejected(self):
        for args in ((0, (0, 1), 1), (0, (0, Q(1, 100)), 1),
                     (0, (0, 0), 0), (0.0, (0, 0), 1), (0, (True, 0), 1),
                     (0, (0,), 1)):
            with self.assertRaises(ValueError):
                coercive_inverse_certificate(*args)
        with self.assertRaises(ValueError):
            authentic_block_certificate(8, 2)
        with self.assertRaises(ValueError):
            transition_difference_coefficients(3, 0, 0)
        with self.assertRaises(ValueError):
            coercivity_floor(1)
