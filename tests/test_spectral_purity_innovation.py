"""Exact controls for signed innovation and the authentic Green energy budget."""
from fractions import Fraction as Q
from itertools import product
import unittest

from observational_succ.spectral_purity_innovation import (
    SOURCE_ID, authentic_sequential_certificate, exceptional_budget,
    fejer_polynomial, mode_green_error_squared, sequential_certificate,
    spectral_green_budget,
)
from observational_succ.succ_internal_matrix_walk import (
    MatrixWalk, PhasePoly, source_cyclotomic_quotient,
)
from observational_succ.gamma_bbp_signed_coherence import (
    authentic_orbit_rational, green_tail_interval,
)
from observational_succ.finite_fourier_carrier import CyclotomicElement


class SequentialIdentityTests(unittest.TestCase):
    def test_independent_authentic_matrix_replay(self):
        for width in (2, 3, 5):
            walk = MatrixWalk.initial(width)
            for n in range(1, 8):
                walk = walk.succ()
                cert = authentic_sequential_certificate(n, width)
                self.assertEqual(cert.source_id, SOURCE_ID)
                self.assertEqual(cert.history, walk.history)
                self.assertEqual(cert.normalized_spectral_excess,
                                 walk.excess_by_fourier()/width)
                self.assertFalse(cert.normality_proved)

    def test_short_exhaustive_histories(self):
        # These generic holdouts contain repeated, antipodal, and 3-torsion
        # points. They are independent of the authentic discovery orbit.
        alphabet = (Q(0), Q(1, 2), Q(1, 3))
        for n in range(1, 4):
            for data in product(alphabet, repeat=n):
                for H in (1, 2, 4):
                    c = sequential_certificate(data, H)
                    pair = sum((fejer_polynomial(x-y, H)
                                for x in data for y in data), PhasePoly.zero())
                    self.assertEqual(c.normalized_spectral_excess,
                                     pair/Q(n*n*H)-1)

    def test_negative_innovation_is_retained(self):
        c = sequential_certificate((Q(0), Q(1, 2)), 2)
        evaluated = source_cyclotomic_quotient(c.innovations[0])
        self.assertEqual(evaluated, CyclotomicElement.scalar(evaluated.modulus, 0))
        negative = source_cyclotomic_quotient(c.weighted_signed_innovation)
        expected = source_cyclotomic_quotient(PhasePoly.monomial(0, -2))
        self.assertEqual(negative, expected)
        residual = source_cyclotomic_quotient(c.normalized_spectral_excess)
        self.assertEqual(residual, CyclotomicElement.scalar(residual.modulus, 0))

    def test_zero_forcing_is_maximally_reinforced(self):
        for N, H in ((1, 4), (3, 5), (8, 3)):
            c = sequential_certificate((Q(0),)*N, H)
            self.assertEqual(c.normalized_spectral_excess,
                             PhasePoly.monomial(0, H-1))
            self.assertEqual(c.weighted_signed_innovation,
                             PhasePoly.monomial(0, N*(N-1)*H*(H-1)//2))

    def test_source_authentication_rejects_lift_and_phase_mutants(self):
        data = tuple(authentic_orbit_rational(n) for n in range(1, 6))
        self.assertEqual(sequential_certificate(data, 3, authenticate=True).source_id,
                         SOURCE_ID)
        for offset in (Q(1), Q(1, 7)):
            mutant = data[:-1]+(data[-1]+offset,)
            with self.assertRaisesRegex(ValueError, "source or unwrapped lift"):
                sequential_certificate(mutant, 3, authenticate=True)
        with self.assertRaises(ValueError):
            sequential_certificate((Q(0),)*5, 3, authenticate=True)

    def test_chart_invariance_does_not_authenticate_rotated_source(self):
        c = authentic_sequential_certificate(5, 3)
        shifted = sequential_certificate(tuple(x+Q(2, 7) for x in c.history), 3)
        self.assertEqual(c.innovations, shifted.innovations)
        self.assertEqual(c.normalized_spectral_excess,
                         shifted.normalized_spectral_excess)
        self.assertNotEqual(shifted.source_id, SOURCE_ID)

    def test_formal_and_cyclotomic_equality_are_distinct(self):
        p = fejer_polynomial(Q(1, 2), 2)
        self.assertNotEqual(p, PhasePoly.zero())
        evaluated = source_cyclotomic_quotient(p)
        self.assertEqual(evaluated, CyclotomicElement.scalar(evaluated.modulus, 0))

    def test_exact_types_required(self):
        for data in ((0.0,), (True,), ()):
            with self.assertRaises(ValueError):
                sequential_certificate(data, 2)
        for width in (0, True, 2.0):
            with self.assertRaises(ValueError):
                sequential_certificate((Q(0),), width)


class ConditionalExceptionalTests(unittest.TestCase):
    def test_budget_keeps_actual_step_weights(self):
        c = exceptional_budget(10, 4, Q(1, 8), (2, 9))
        self.assertEqual(c.weighted_exceptional_mass, 11)
        self.assertEqual(c.normalized_excess_upper,
                         Q(3, 10)+Q(9, 80)+Q(88, 100))
        self.assertFalse(c.good_step_premise_verified)
        self.assertFalse(c.normality_proved)

    def test_rational_adversarial_row_bounds(self):
        # Entries include negative q-H. No cancellation is discarded on the
        # left; only the declared one-sided hypotheses control the bound.
        for N, H, eta, bad in ((7, 3, Q(1, 4), (2, 5)),
                               (8, 2, Q(0), (7,)),
                               (6, 4, Q(1, 3), ())):
            q = [Q(0) if m % 2 else H*(1+eta)
                 for m in range(1, N)]
            for m in bad:
                q[m-1] = Q(H*H)
            signed = sum((m*(v-H) for m, v in enumerate(q, 1)), Q(0))
            exact = Q(H-1, N)+Q(2, N*N*H)*signed
            self.assertLessEqual(exact,
                exceptional_budget(N, H, eta, bad).normalized_excess_upper)

    def test_bad_indices_and_negative_eta_rejected(self):
        for bad in ((0,), (4,), (2, 2), (2, 1), (True,)):
            with self.assertRaises(ValueError):
                exceptional_budget(4, 2, Q(0), bad)
        with self.assertRaises(ValueError):
            exceptional_budget(4, 2, Q(-1, 4), ())


class SourceGreenSpectralTests(unittest.TestCase):
    def test_source_tail_pointwise_bound(self):
        # Authenticated finite enclosures cover unused times as exact holdouts.
        for n in (1, 2, 7, 19, 64, 173, 1001):
            self.assertLess(green_tail_interval(n, 8).upper, Q(1, 64*n*n))

    def test_clipped_character_integral_bound_exact(self):
        # Test squared inequalities with exact arithmetic, not square roots.
        for h in (1, 2, 7, 31, 100, 4096):
            for N in (1, 8, 41, 137):
                total = sum((min(Q(2), Q(7*h, 64*n*n))
                             for n in range(1, N+1)), Q(0))
                self.assertLessEqual(total*total, Q(7*h, 8))

    def test_weighted_square_root_scaling_formula(self):
        for N, H in ((1, 1), (3, 2), (17, 13), (73, 59), (10000, 257)):
            c = spectral_green_budget(N, H)
            separate = sum((Q(2*(H-j), H)*Q(7*j, 8*N*N)
                            for j in range(1, H)), Q(0))
            self.assertEqual(c.square_root_scaling_upper, separate)
            self.assertLessEqual(c.squared_root_energy_error_upper, separate)
            self.assertFalse(c.normality_proved)
            self.assertEqual(c.source_id, SOURCE_ID)

    def test_full_sublinear_schedule_improves_lipschitz_budget(self):
        # A fixed H=floor(N^(3/4)) schedule lies beyond N^(2/3).
        # These finite budgets illustrate, rather than prove, the paper rate.
        values = []
        for k in (2, 3, 5):
            N, H = 2**(4*k), 2**(3*k)
            c = spectral_green_budget(N, H)
            self.assertLess(c.square_root_scaling_upper,
                            c.summable_lipschitz_upper)
            values.append(c.square_root_scaling_upper)
        self.assertGreater(values[0], values[1])
        self.assertGreater(values[1], values[2])

    def test_mode_budget_is_even_in_frequency(self):
        for h in (1, 13, 127):
            self.assertEqual(mode_green_error_squared(h, 59),
                             mode_green_error_squared(-h, 59))

    def test_source_green_typing(self):
        for h in (0, True, 1.0):
            with self.assertRaises(ValueError):
                mode_green_error_squared(h, 9)
        for N, H in ((0, 3), (2, 0), (True, 2), (2, 1.5)):
            with self.assertRaises(ValueError):
                spectral_green_budget(N, H)


if __name__ == "__main__":
    unittest.main()
