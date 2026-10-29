"""Hostile exact tests for the observer spectral and signed-boundary claims."""
from fractions import Fraction as Q
from itertools import product
import random
import unittest

from observational_succ.bbp_natural_carrier import (
    exact_forcing, orbit_state, source_tail_enclosure,
)
from observational_succ.divisor_observer_spectrum import (
    apply_adjoint_rational, apply_compressed_rational, boundary_multiplicities,
    divisor_summatory, exact_shell_residuals, formal_boundary_minus_weyl,
    formal_commutator_numerator, gauge_cycle_turn, hyperbolic_shell_receipt,
    original_bbp_turns, sharp_commutator_bound, weighted_inner,
)
from observational_succ.origin_fiber_arithmetic_observer import (
    compressed_channel_prime_overlap_sq, d,
)


class HyperbolicObserverTests(unittest.TestCase):
    def test_fiber_count_against_literal_pair_space(self):
        for limit in range(1, 45):
            pairs = {(a, b) for a in range(1, limit + 1)
                     for b in range(1, limit + 1) if a * b <= limit}
            self.assertEqual(divisor_summatory(limit), len(pairs))
            internal = sum((a + 1, b) in pairs for a, b in pairs)
            receipt = hyperbolic_shell_receipt(limit)
            self.assertEqual(receipt["internal_edges"], internal)
            self.assertEqual(receipt["active_pair_fibers"], limit)
            self.assertEqual(receipt["L_rayleigh"], Q(limit, len(pairs)))

    def test_hard_pinned_shell_exact_boundary(self):
        for cutoff in range(0, 9):
            for limit in range(max(1, cutoff + 1), 4 * cutoff + 9):
                pairs = {(a, b) for a in range(1, limit + 1)
                         for b in range(1, limit + 1)
                         if cutoff < a * b <= limit}
                receipt = hyperbolic_shell_receipt(limit, cutoff)
                self.assertEqual(receipt["squared_unnormalized_norm"], len(pairs))
                self.assertEqual(receipt["internal_edges"],
                                 sum((a + 1, b) in pairs for a, b in pairs))
                if limit >= 2 * cutoff:
                    self.assertEqual(receipt["active_pair_fibers"], limit)

    def test_weighted_adjoint_and_contraction(self):
        rng = random.Random(348)
        for _ in range(15):
            left = {n: Q(rng.randrange(-4, 5), rng.randrange(1, 6))
                    for n in range(1, 14)}
            right = {n: Q(rng.randrange(-4, 5), rng.randrange(1, 6))
                     for n in range(1, 18)}
            self.assertEqual(weighted_inner(left, apply_compressed_rational(right)),
                             weighted_inner(apply_adjoint_rational(left), right))
            image = apply_compressed_rational(left)
            self.assertLessEqual(weighted_inner(image, image), weighted_inner(left, left))

    def test_exact_residuals_below_proved_bound(self):
        for limit, cutoff in [(1, 0), (2, 0), (7, 0), (25, 0), (80, 0),
                              (21, 8), (40, 17), (61, 30), (67, 0)]:
            receipt = hyperbolic_shell_receipt(limit, cutoff)
            residual = exact_shell_residuals(limit, cutoff)
            self.assertEqual(residual["L_rayleigh"], receipt["L_rayleigh"])
            self.assertLessEqual(residual["I_minus_T_squared_norm"],
                                 receipt["residual_squared_upper"])
            self.assertLessEqual(residual["L_squared_norm"],
                                 receipt["residual_squared_upper"])

    def test_finite_forward_matrix_nilpotent_not_infinite_spectrum(self):
        limit = 8
        vector = {n: Q(1) for n in range(1, limit + 1)}
        for _ in range(limit):
            vector = {n: v for n, v in apply_compressed_rational(vector).items()
                      if n <= limit}
        self.assertEqual(vector, {})
        self.assertGreater(hyperbolic_shell_receipt(1000)["T_rayleigh"], Q(4, 5))


class SignedCommutatorTests(unittest.TestCase):
    def test_boundary_degree_and_l1_norm(self):
        for limit in range(1, 100):
            counts = boundary_multiplicities(limit)
            for n, value in enumerate(counts, 1):
                literal = sum(n % b == 0 and n + b > limit for b in range(1, n + 1))
                self.assertEqual(value, literal)
                self.assertEqual(value == 0, n <= limit // 2)
            self.assertEqual(sum(counts), limit)
            self.assertEqual(sum(abs(c - 1) for c in counts), 2 * (limit // 2))

    def test_exhaustive_signs_and_sharp_attainer(self):
        for limit in range(1, 9):
            maximum = Q()
            for signs in product((-1, 1), repeat=limit):
                phase = tuple(Q(1, 2) if value == -1 else Q() for value in signs)
                raw = formal_commutator_numerator(phase)
                value = sum(coefficient * (1 if turn == 0 else -1)
                            for turn, coefficient in raw.items()) / divisor_summatory(limit)
                maximum = max(maximum, abs(value))
            self.assertEqual(maximum, sharp_commutator_bound(limit))
            attainer = (Q(1, 2),) * (limit // 2) + (Q(),) * (limit - limit // 2)
            raw = formal_commutator_numerator(attainer)
            actual = sum(c * (1 if t == 0 else -1) for t, c in raw.items())
            self.assertEqual(actual, 2 * (limit // 2))

    def test_original_zero_seed_signed_identity_as_formal_characters(self):
        for frequency in (-7, -1, 1, 2, 15):
            for limit in (1, 2, 7, 16, 31):
                turns = original_bbp_turns(limit, frequency)
                self.assertEqual(formal_commutator_numerator(turns),
                                 formal_boundary_minus_weyl(turns))

    def test_native_source_import_and_literal_four_poles(self):
        turns = original_bbp_turns(10)
        for n in range(1, 11):
            self.assertEqual(turns[n - 1], orbit_state(n).rational % 1)
            literal = Q(4, 8*n-7) - Q(2, 8*n-4) - Q(1, 8*n-3) - Q(1, 8*n-2)
            self.assertEqual(exact_forcing(n), literal)

    def test_wrong_seed_and_wrong_forcing_obey_same_operator_identity(self):
        authentic = original_bbp_turns(24)
        torsion = original_bbp_turns(24, seed=Q(1, 15))
        self.assertNotEqual(authentic, torsion)
        self.assertTrue(all((t - a) % 1 == Q(1, 15) for a, t in zip(authentic, torsion)))
        state, altered = Q(), []
        for n in range(1, 25):
            # Explicit altered first-pole coefficient 4 -> 5, never authentic.
            state = (16*state + exact_forcing(n) + Q(1, 8*n-7)) % 1
            altered.append(state)
        self.assertNotEqual(authentic, tuple(altered))
        for turns in (torsion, altered):
            self.assertEqual(formal_commutator_numerator(turns),
                             formal_boundary_minus_weyl(turns))

    def test_constant_phase_nonnormal_control(self):
        for limit in (1, 11, 64):
            constant = (Q(),) * limit
            self.assertEqual(formal_commutator_numerator(constant), {})
            self.assertEqual(formal_boundary_minus_weyl(constant), {})
            self.assertEqual(sum(boundary_multiplicities(limit)), limit)
            # Both signed boundary and Weyl sums are exactly N, not o(N).

    def test_alternating_boundary_with_rational_log_two_enclosure(self):
        # log 2 = 2 atanh(1/3); bound the positive geometric remainder.
        terms = 16
        log_lower = 2 * sum((Q(1, (2*j+1)*3**(2*j+1))
                             for j in range(terms)), Q())
        log_upper = log_lower + Q(9, 4*(2*terms+1)*3**(2*terms+1))
        for root in (8, 16, 32, 64):
            limit = root*root
            boundary = sum(c * (-1)**n for n, c in
                           enumerate(boundary_multiplicities(limit), 1))
            independent = sum((-1)**(b*(limit//b)) for b in range(1, limit+1))
            self.assertEqual(boundary, independent)
            self.assertGreaterEqual(boundary, limit*(1-log_upper) - 3*root)
            self.assertLessEqual(boundary, limit*(1-log_lower) + 3*root)
            self.assertEqual(sum((-1)**n for n in range(1, limit+1)), 0)
        self.assertGreater(boundary, Q(limit, 4))

    def test_coherent_same_forcing_control_uses_tail_not_fake_rational_seed(self):
        for n in range(1, 25):
            lower, upper = source_tail_enclosure(n, 8)
            self.assertGreater(lower, 0)
            self.assertLessEqual(upper, Q(1, 15 * (n + 1)**2))
        with self.assertRaises(TypeError):
            original_bbp_turns(3, seed=-0.19634954084936207)


class GaugeAndTypingControls(unittest.TestCase):
    def test_actual_cycle_holonomy_is_trivial_for_all_sources(self):
        cycles = ((2, 3, 4, 2), (3, 4, 6, 3), (1, 2, 3, 2, 1))
        phases = (original_bbp_turns(10), original_bbp_turns(10, seed=Q(1, 15)),
                  tuple(Q(n*n, 37) for n in range(10)))
        for phase in phases:
            for cycle in cycles:
                self.assertEqual(gauge_cycle_turn(phase, cycle), Q())
        with self.assertRaises(ValueError):
            gauge_cycle_turn(phases[0], (1, 3, 1))

    def test_finite_laplacian_gauge_conjugacy_exact_rational_phases(self):
        import sympy as s
        limit = 6
        def matrix_of(action):
            columns = [action({n: Q(1)}) for n in range(1, limit + 1)]
            return s.Matrix([[s.Rational(columns[n-1].get(m, Q()))
                              for n in range(1, limit + 1)] for m in range(1, limit + 1)])
        forward = matrix_of(apply_compressed_rational)
        backward = matrix_of(apply_adjoint_rational)
        laplacian = s.eye(limit) - (forward + backward) / 2
        phase = s.diag(1, s.I, -1, -s.I, 1, s.I)
        twisted = phase * laplacian * phase.conjugate().T
        pin = s.diag(7, 0, 0, 0, 0, 0)
        self.assertEqual((twisted + pin).charpoly().all_coeffs(),
                         (laplacian + pin).charpoly().all_coeffs())
        self.assertNotEqual(twisted, laplacian)

    def test_actual_integer_fiber_rejects_fake_composite_prime(self):
        with self.assertRaises(ValueError):
            compressed_channel_prime_overlap_sq(1, 6)
        self.assertEqual(d(6), 4)
        # A second primitive symbol "6" would add two duplicate split states.
        fake_fiber_dimension = sum((i+1)*(j+1)*(k+1)
                                  for i, j, k in product(range(3), repeat=3)
                                  if 2**i * 3**j * 6**k == 6)
        self.assertEqual(fake_fiber_dimension, 6)
        self.assertNotEqual(fake_fiber_dimension, d(6))

    def test_invalid_domains_and_probability_confusion(self):
        for invalid in (False, -1, Q(2), 2.0):
            with self.assertRaises(ValueError):
                divisor_summatory(invalid)
        with self.assertRaises(ValueError):
            hyperbolic_shell_receipt(4, 4)
        with self.assertRaises(TypeError):
            apply_compressed_rational({1: 0.5})
        image = apply_compressed_rational({1: Q(1)})
        self.assertEqual(image, {2: Q(1, 2)})
        self.assertEqual(weighted_inner(image, image), Q(1, 2))
        self.assertNotEqual(sum(image.values()), Q(1))


if __name__ == "__main__":
    unittest.main()
