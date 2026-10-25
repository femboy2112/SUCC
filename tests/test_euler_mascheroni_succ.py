"""Exact source identities and hostile controls for the gamma finite interface.

Optional mpmath readouts calibrate proved interval formulae; they are not
certificates of the infinite theorems. All production endpoints are Fractions.
"""
from fractions import Fraction as Q
from itertools import product
import unittest

from observational_succ.euler_mascheroni_succ import (
    continuum_prefix_bounds, finite_mellin_kernel, finite_mellin_value,
    finite_successor_boundary, gamma_bounds, harmonic_prefix,
    hurwitz_boundary_bounds, hurwitz_difference_bounds,
    jet_counterfeit_coefficients, mellin_tail_bound, paired_boundary_correction,
    paired_boundary_limit_bounds, paired_raw_prefix, polynomial_moment,
    rational_log_bounds, refinement_affine_data, regularized_prefix_bounds,
    successor_cell_defect,
)


def determinant(matrix):
    """Independent exact Gaussian elimination, including singular matrices."""
    rows = [list(row) for row in matrix]
    result = Q(1)
    for i in range(len(rows)):
        pivot = next((j for j in range(i, len(rows)) if rows[j][i]), None)
        if pivot is None:
            return Q()
        if pivot != i:
            rows[pivot], rows[i] = rows[i], rows[pivot]
            result = -result
        diagonal = rows[i][i]
        result *= diagonal
        for j in range(i+1, len(rows)):
            ratio = rows[j][i]/diagonal
            for k in range(i+1, len(rows)):
                rows[j][k] -= ratio*rows[i][k]
    return result


def atan_bracket(argument, terms):
    partial = sum(((-1)**k*argument**(2*k+1)/Q(2*k+1)
                   for k in range(terms)), Q())
    following = (-1)**terms*argument**(2*terms+1)/Q(2*terms+1)
    return min(partial, partial+following), max(partial, partial+following)


class ExactGammaInterfaceTests(unittest.TestCase):
    def test_log_unit_inverse_and_power_coherence(self):
        self.assertEqual(rational_log_bounds(1), (0, 0))
        for q in (Q(2), Q(3, 7), Q(17, 4), Q(1024)):
            low, high = rational_log_bounds(q, 12)
            inv_low, inv_high = rational_log_bounds(1/q, 12)
            self.assertEqual((inv_low, inv_high), (-high, -low))
            sharper = rational_log_bounds(q, 24)
            self.assertLessEqual(low, sharper[0])
            self.assertLessEqual(sharper[1], high)
        l2, u2 = rational_log_bounds(2, 20)
        self.assertEqual(rational_log_bounds(1024, 20), (10*l2, 10*u2))
        self.assertGreater(l2, Q(2, 3))
        self.assertLess(u2, Q(7, 10))

    def test_harmonic_known_values_and_offset(self):
        self.assertEqual(harmonic_prefix(0), 0)
        self.assertEqual(harmonic_prefix(4), Q(25, 12))
        self.assertEqual(harmonic_prefix(3, Q(1, 2)), Q(46, 15))
        self.assertEqual(harmonic_prefix(2, 1, 2), Q(5, 4))

    def test_integer_continuum_and_source_succ(self):
        for n, s, a in product((1, 2, 7, 23), (1, 2, 3, 6),
                               (Q(1), Q(1, 4), Q(7, 3))):
            difference = harmonic_prefix(n, a+1, s)-harmonic_prefix(n, a, s)
            self.assertEqual(difference, finite_successor_boundary(n, a, s))
            self.assertNotEqual(difference, -a**(-s))
        self.assertEqual(continuum_prefix_bounds(4, 2), (Q(3, 4), Q(3, 4)))

    def test_compensated_two_clock_sum_exact(self):
        for n, s in product((1, 2, 5, 17), (2, 3, 4, 7)):
            corrected = paired_raw_prefix(n, s)+paired_boundary_correction(n, s)
            self.assertEqual(regularized_prefix_bounds(n, 1, s), (corrected, corrected))
            # Either missing boundary term produces a false finite identity.
            missing_geometric = paired_raw_prefix(n, s)+Q(n)**(1-s)/(s-1)
            self.assertNotEqual(missing_geometric, corrected)
            if n > 1:
                self.assertNotEqual(paired_raw_prefix(n, s), corrected)

    def test_removable_boundary_at_one(self):
        for n in (1, 2, 11, 50):
            low, high = paired_boundary_limit_bounds(n)
            raw_at_one = harmonic_prefix(n)-n
            expected = regularized_prefix_bounds(n)
            self.assertEqual((raw_at_one+low, raw_at_one+high), expected)
            self.assertGreater(low, 0)

    def test_exact_finite_residue_refinement(self):
        for p, n, s, a in product((2, 3, 5, 6), (1, 2, 7), (2, 3, 4),
                                  (Q(1), Q(1, 8), Q(9, 4))):
            mean = sum((regularized_prefix_bounds(n, (a+j)/p, s)[0]
                        for j in range(p)), Q())/p
            scale, (offset, high) = refinement_affine_data(p, s)
            self.assertEqual(offset, high)
            rhs = scale*regularized_prefix_bounds(p*n, a, s)[0]+offset
            self.assertEqual(mean, rhs)
            self.assertNotEqual(mean, rhs-offset)

    def test_s_equals_one_refinement_keeps_all_residues(self):
        for p, n, a in product((2, 3, 7), (1, 5, 13), (Q(1), Q(1, 4))):
            mean = sum((harmonic_prefix(n, (a+j)/p)
                        for j in range(p)), Q())/p
            self.assertEqual(mean, harmonic_prefix(p*n, a))
            mutant = sum((harmonic_prefix(n, (a+j)/p)
                          for j in range(p-1)), Q())/p
            self.assertNotEqual(mutant, harmonic_prefix(p*n, a))

    def test_affine_refinement_composition_all_composites(self):
        for p, q, s in product((2, 3, 6), (2, 5, 7), (2, 3, 5)):
            ap, (bp, _) = refinement_affine_data(p, s)
            aq, (bq, _) = refinement_affine_data(q, s)
            ar, (br, _) = refinement_affine_data(p*q, s)
            self.assertEqual(ar, ap*aq)
            self.assertEqual(br, bp+ap*bq)
            self.assertEqual(br, bq+aq*bp)
            self.assertNotEqual(br, bp+bq)
        self.assertEqual(refinement_affine_data(1, 4), (1, (0, 0)))

    def test_hurwitz_difference_antisymmetry_and_zero(self):
        for a, b in product((Q(1, 8), Q(1), Q(7, 2)), repeat=2):
            low, high = hurwitz_difference_bounds(a, b, 17)
            self.assertEqual(hurwitz_difference_bounds(b, a, 17), (-high, -low))
            if a == b:
                self.assertEqual((low, high), (0, 0))

    def test_hurwitz_successor_contains_exact_value(self):
        for a in (Q(1, 8), Q(1, 4), Q(1), Q(5, 2)):
            low, high = hurwitz_difference_bounds(a, a+1, 20)
            self.assertLess(low, 1/a)
            self.assertLess(1/a, high)
            self.assertLess(high-low, Q(1, 200))

    def test_quarter_hurwitz_pi_against_independent_machin(self):
        pi_low, pi_high = hurwitz_difference_bounds(Q(1, 4), Q(3, 4), 32)
        a0, a1 = atan_bracket(Q(1, 5), 20)
        b0, b1 = atan_bracket(Q(1, 239), 20)
        machin_low, machin_high = 16*a0-4*b1, 16*a1-4*b0
        self.assertLess(pi_low, machin_low)
        self.assertLess(machin_high, pi_high)
        self.assertLess(pi_high-pi_low, Q(1, 1000))
        # Reversing the signed offset orientation must fail the same target.
        self.assertLess(hurwitz_difference_bounds(Q(3, 4), Q(1, 4), 32)[1], 0)

    def test_gamma_interval_narrows_with_source_horizon(self):
        previous_width = Q(10)
        for n in (2, 8, 32, 128):
            low, high = gamma_bounds(n)
            self.assertGreater(low, Q(1, 2))
            self.assertLess(high, Q(2, 3))
            self.assertLess(high-low, previous_width)
            previous_width = high-low
            self.assertEqual(hurwitz_boundary_bounds(1, n), (low, high))

    def test_cell_kernel_matches_independent_integrals(self):
        for n, s in product(range(1, 12), range(2, 10)):
            integral = (n+1)*(Q(n)**(-s)-Q(n+1)**(-s))/s
            integral -= (Q(n)**(1-s)-Q(n+1)**(1-s))/(s-1)
            self.assertEqual(successor_cell_defect(n, s)/s, integral)
            self.assertGreater(integral, 0)

    def test_kernel_exact_psd_and_repeated_exponent_null(self):
        for n in (1, 3, 9):
            kernel = finite_mellin_kernel(n, (1, 2, 3, 5))
            for size in range(1, 5):
                self.assertGreater(determinant(tuple(row[:size] for row in kernel[:size])), 0)
            for c in product((-2, 0, 1), repeat=4):
                energy = sum((Q(c[i]*c[j])*kernel[i][j]
                              for i in range(4) for j in range(4)), Q())
                self.assertGreaterEqual(energy, 0)
        null_kernel = finite_mellin_kernel(3, (1, 1, 2))
        self.assertEqual(determinant(null_kernel), 0)
        # A sign-blind/off-diagonal mutation can fail the exact PSD guard.
        kernel = finite_mellin_kernel(3, (1, 2))
        mutant_cross = kernel[0][0]+kernel[1][1]
        self.assertLess(kernel[0][0]+kernel[1][1]-2*mutant_cross, 0)

    def test_kernel_prefix_and_tail_budget(self):
        for n, s in product((0, 1, 5, 17), (2, 3, 7)):
            gap = finite_mellin_value(n+19, s)-finite_mellin_value(n, s)
            self.assertGreater(gap, 0)
            self.assertLess(gap, mellin_tail_bound(n, s))

    def test_finite_jet_counterfeits_keep_exact_moments(self):
        for order in range(9):
            coefficients = jet_counterfeit_coefficients(order)
            for j in range(order+1):
                self.assertEqual(polynomial_moment(coefficients, j), 0)
            self.assertNotEqual(polynomial_moment(coefficients, order+1), 0)
            mutant = (coefficients[0]+1,)+coefficients[1:]
            self.assertNotEqual(polynomial_moment(mutant, 0), 0)
        self.assertEqual(jet_counterfeit_coefficients(0), (Q(-1), Q(8)))
        self.assertEqual(polynomial_moment(jet_counterfeit_coefficients(0), 1)/4,
                         Q(1, 384))

    def test_reject_approximate_and_invalid_sources(self):
        for call in (
            lambda: rational_log_bounds(0), lambda: rational_log_bounds(1.1),
            lambda: rational_log_bounds(True), lambda: gamma_bounds(0),
            lambda: harmonic_prefix(-1), lambda: harmonic_prefix(2, 0),
            lambda: harmonic_prefix(2, Q(1), 1.0),
            lambda: refinement_affine_data(0, 2),
            lambda: paired_raw_prefix(3, 1),
            lambda: finite_mellin_kernel(3, (0, 1)),
            lambda: finite_mellin_kernel(3, ()),
            lambda: polynomial_moment((0.5,), 1),
        ):
            with self.assertRaises(ValueError):
                call()


class NumericalCalibrationTests(unittest.TestCase):
    def test_proved_intervals_against_special_function_readouts(self):
        try:
            import mpmath as mp
        except ImportError:
            self.skipTest("optional mpmath diagnostic unavailable")
        def cast(q):
            return mp.mpf(q.numerator)/q.denominator
        with mp.workdps(70):
            for n in (1, 7, 64):
                low, high = gamma_bounds(n, 30)
                self.assertLess(cast(low), mp.euler)
                self.assertLess(mp.euler, cast(high))
            for a in (Q(1, 8), Q(1, 4), Q(1), Q(9, 2)):
                low, high = hurwitz_boundary_bounds(a, 40, 30)
                reference = -mp.digamma(cast(a))
                self.assertLess(cast(low), reference)
                self.assertLess(reference, cast(high))
            for n, s in product((1, 7, 25), (2, 3, 6)):
                value = (mp.zeta(s)-mp.mpf(1)/(s-1))/s
                partial = cast(finite_mellin_value(n, s))
                self.assertLess(partial, value)
                self.assertLess(value-partial, cast(mellin_tail_bound(n, s)))


if __name__ == "__main__":
    unittest.main()
