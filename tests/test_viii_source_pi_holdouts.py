"""Independent exact holdouts for Main VIII source and polygon transport.

These controls certify finite identities and counterexamples, not Weil
positivity or pi normality. They do not reuse the source integration routine.
"""
from fractions import Fraction as Q
from itertools import product
from math import factorial
import unittest

import sympy as S

from observational_succ import pi_polygon_normality as P
from observational_succ.cloud_exact_moment_inverse import _weighted_lower


class SourceMomentHoldouts(unittest.TestCase):
    def test_constrained_inverse_nonorthogonal_constraints(self):
        # Four-dimensional models, with nonorthogonal columns. Directly solve
        # in a nullspace basis instead of reusing the inverse's rank correction.
        for scale in range(1, 6):
            T = S.Matrix([[1, 0, scale, 0], [0, 2, 0, 1],
                          [0, 0, 1, 1], [0, 0, 0, 3]])
            B = T.T * T + S.eye(4)
            L = S.Matrix([[1, 1], [0, 1], [1, 0], [0, scale]])
            V = S.Matrix.hstack(*L.T.nullspace())
            restricted = V * (V.T * B * V).inv() * V.T
            M = L.T * B.inv() * L
            corrected = B.inv() - B.inv() * L * M.inv() * L.T * B.inv()
            self.assertEqual(restricted, corrected)
            self.assertEqual(L.T * corrected, S.zeros(2, 4))
            self.assertTrue(corrected.is_positive_semidefinite)
            self.assertTrue((B.inv() - corrected).is_positive_semidefinite)
            # Nonorthogonality matters: erasing off-diagonal Gram information
            # does not reproduce the constrained inverse.
            diagonal = S.diag(*M.diagonal())
            self.assertNotEqual(corrected,
                B.inv() - B.inv()*L*diagonal.inv()*L.T*B.inv())

    def test_reverse_young_all_signed_error_corners(self):
        weight = ((Q(5), Q(-2)), (Q(-2), Q(3)))
        moments = ((Q(2, 3), Q(-7, 5)), (Q(-3, 7), Q(11, 13)))
        errors = ((Q(1, 101), Q(2, 103)), (Q(3, 107), Q(4, 109)))
        for theta in (Q(1, 8), Q(1, 3)):
            lower, _, _ = _weighted_lower(weight, moments, errors, theta)
            W = S.Matrix(weight)
            for signs in product((-1, 1), repeat=4):
                Z = S.Matrix(2, 2, lambda i, j:
                    moments[i][j] + signs[2*i+j]*errors[i][j])
                difference = Z.T * W * Z - S.Matrix(lower)
                self.assertTrue(difference.is_positive_semidefinite)


class PiExactBoundaryHoldouts(unittest.TestCase):
    def test_underflow_cannot_return_zero_certificate(self):
        # Before the repair, this returned 0.0 although the exact product > 0.
        for value in (1e-200, float('nan'), float('inf'), True):
            with self.subTest(value=value):
                with self.assertRaises(ValueError):
                    P.orbit_lipschitz_error_bound(2, 1, value, value)
        tiny = Q(1, 10**200)
        self.assertEqual(P.orbit_lipschitz_error_bound(2, 1, tiny, tiny), tiny*tiny)
        self.assertGreater(tiny*tiny, 0)

    def test_discrete_parameters_reject_numerical_impostors(self):
        for value in (True, 2.0, Q(2)):
            for function in (
                lambda: P.polygon_pi_bracket(value),
                lambda: P.polygon_pi_bracket(0, value),
                lambda: P.rational_sqrt_enclosure(Q(2), value),
                lambda: P.certified_fractional_pi_digits(2, value),
                lambda: P.uniform_grid_pushforward_counts(4, value, 1, 'prefix'),
                lambda: P.polygon_quantize(Q(1, 7), value),
                lambda: P.digit_block_total_variation((0, 1), value, 1),
                lambda: P.orbit_lipschitz_error_bound(value, 1, Q(1)),
                lambda: P.orbit_lipschitz_error_bound(2, value, Q(1)),
                lambda: P.finite_digit_path((0, 1), 2, value),
                lambda: P.polygon_prefix_path(4, 2, value, (0,)),
                lambda: P.polygon_cylinder(0, 4, 2, value),
            ):
                with self.assertRaises(ValueError):
                    function()
        for value in (True, 0.0, Q(0)):
            with self.assertRaises(ValueError):
                P.polygon_prefix_path(4, 2, 0, (value,))
            with self.assertRaises(ValueError):
                P.digit_block_total_variation((value,), 2, 1)
        for value in (True, 0.1):
            with self.assertRaises(ValueError):
                P.polygon_quantize(value, 4)
            with self.assertRaises(ValueError):
                P.rational_sqrt_enclosure(value)

    def test_rounded_width_is_not_the_geometric_gap(self):
        bracket = P.polygon_pi_bracket(1, 1)
        self.assertEqual((bracket.lower, bracket.upper), (Q(2), Q(4)))
        geometric_bound = Q(64, bracket.sides**2)
        self.assertGreater(bracket.upper-bracket.lower, geometric_bound)
        actual_budget = P.orbit_lipschitz_error_bound(
            2, 4, (bracket.upper-bracket.lower)/2)
        unjustified_budget = P.orbit_lipschitz_error_bound(2, 4, geometric_bound/2)
        self.assertGreater(actual_budget, unjustified_budget)

    def test_low_precision_refinement_never_invents_a_digit(self):
        # A separate exact Machin interval certifies the holdout decimal bins.
        def atan(q):
            partial = sum(((-1)**j*q**(2*j+1)/(2*j+1) for j in range(32)), Q())
            return partial, partial+q**65/65
        l5,u5 = atan(Q(1,5)); l239,u239 = atan(Q(1,239))
        true_lo,true_hi = 16*l5-4*u239, 16*u5-4*l239
        for bits in (1, 2, 4, 8, 16, 32, 128):
            for steps in range(12):
                try:
                    digits, bracket = P.certified_fractional_pi_digits(steps, 10, 12, bits)
                except ArithmeticError:
                    continue
                self.assertLess(bracket.lower, true_lo)
                self.assertGreater(bracket.upper, true_hi)
                if digits:
                    n = len(digits)
                    self.assertEqual((true_lo-3)*10**n // 1, int(digits))
                    self.assertEqual((true_hi-3)*10**n // 1, int(digits))


if __name__ == '__main__':
    unittest.main()
