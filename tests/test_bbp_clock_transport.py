"""Exact sharpness, source mutations, and all-weight seed controls."""
from dataclasses import replace
from fractions import Fraction as Q
from itertools import product
from math import gcd
import unittest

from observational_succ.bbp_clock_transport import (
    balanced_clock_weights, clock_transport_budget, conditional_energy,
    congruent_seed_control, rational_valuation, refinement_gain,
    root_energy_transport_squared, seed_gain_upper, seed_matrix_deficit_upper,
    verify_congruent_seed_control, weighted_feature_difference_squared,
    weighted_spectral_excess,
)
from observational_succ.finite_fourier_carrier import CyclotomicElement
from observational_succ.pi_source_genesis import character_interval
from observational_succ.succ_internal_matrix_walk import (
    PhasePoly, source_cyclotomic_quotient,
)


def real_interval(polynomial):
    """Independent outward character evaluation, not a float comparison."""
    assert polynomial == polynomial.star()
    low = high = Q()
    for phase, coefficient in polynomial.terms:
        box = character_interval(phase, phase).outward(60)
        left, right = coefficient*box.real_low, coefficient*box.real_high
        low += min(left, right)
        high += max(left, right)
    return low, high


def rational_evaluation(polynomial):
    value = source_cyclotomic_quotient(polynomial, modulus_cap=256)
    if len(value.polynomial) > 1:
        raise AssertionError("test expected a rational cyclotomic value")
    return value.polynomial[0]


class SharpTransportTests(unittest.TestCase):
    def test_sharp_constant_on_every_small_uniform_grid(self):
        for H in range(2, 13):
            xs = tuple(Q(j, H) for j in range(H))
            baseline = (Q(1, H),)*H
            amount = Q(1, 3*H)
            changed = list(baseline)
            changed[0] += amount
            changed[1] -= amount
            changed = tuple(changed)
            empty = source_cyclotomic_quotient(
                weighted_spectral_excess(xs, baseline, H))
            self.assertEqual(empty, CyclotomicElement.scalar(empty.modulus, 0))
            cap = root_energy_transport_squared(H, 2*amount)
            self.assertEqual(rational_evaluation(
                weighted_spectral_excess(xs, changed, H)), cap)
            self.assertEqual(rational_evaluation(
                weighted_feature_difference_squared(xs, changed, baseline, H)), cap)

    def test_half_sized_constant_is_refuted_exactly(self):
        H = 5
        xs = tuple(Q(j, H) for j in range(H))
        baseline = (Q(1, H),)*H
        changed = (Q(3, 10), Q(1, 10), Q(1, 5), Q(1, 5), Q(1, 5))
        exact = rational_evaluation(weighted_spectral_excess(xs, changed, H))
        self.assertEqual(exact, Q(1, 10))
        self.assertGreater(exact, Q(H, 4)*Q(1, 5)**2)

    def test_dimension_order_is_necessary(self):
        # Grid-Haar plus a point mass: E=(H-1)t^2. A dimension-free l1
        # estimate cannot replace the sqrt(H) root-energy cost.
        for H in (4, 8, 16):
            xs = tuple(Q(j, H) for j in range(H))
            t = Q(1, 4)
            baseline = (Q(1, H),)*H
            changed = ((1-t)/H+t,)+((1-t)/H,)*(H-1)
            self.assertEqual(rational_evaluation(
                weighted_spectral_excess(xs, changed, H)), (H-1)*t*t)
            delta = sum((abs(a-b) for a, b in zip(changed, baseline)), Q())
            self.assertEqual(delta, 2*t*Q(H-1, H))

    def test_exhaustive_antipodal_measure_differences(self):
        xs = (Q(), Q(1, 2))
        for H in (2, 3, 6, 9):
            for a, b in product(range(7), repeat=2):
                first = (Q(a, 6), Q(6-a, 6))
                second = (Q(b, 6), Q(6-b, 6))
                delta = 2*abs(first[0]-second[0])
                energy = rational_evaluation(
                    weighted_feature_difference_squared(xs, first, second, H))
                self.assertLessEqual(energy, root_energy_transport_squared(H, delta))

    def test_width_one_and_equal_measures(self):
        xs, ws = (Q(), Q(2, 7)), (Q(1, 3), Q(2, 3))
        self.assertEqual(weighted_spectral_excess(xs, ws, 1), PhasePoly.zero())
        self.assertEqual(root_energy_transport_squared(1, 2), 0)
        self.assertEqual(weighted_feature_difference_squared(xs, ws, ws, 5),
                         PhasePoly.zero())

    def test_probability_types_and_domains(self):
        for weights in ((Q(1), Q(1)), (Q(-1), Q(2)), (0.5, 0.5), (True, False)):
            with self.assertRaises(ValueError):
                weighted_spectral_excess((Q(), Q(1, 3)), weights, 3)
        for H, delta in ((0, Q(1)), (True, Q(1)), (2, Q(-1)), (2, Q(3)), (2, 0.5)):
            with self.assertRaises(ValueError):
                root_energy_transport_squared(H, delta)


class ClockBudgetTests(unittest.TestCase):
    def test_exact_balancing_cost_all_small_clocks(self):
        for N in range(1, 31):
            for modulus in range(1, N+1):
                weights = balanced_clock_weights(N, modulus)
                cost = sum((abs(w-Q(1, N)) for w in weights), Q())
                c = clock_transport_budget(N, modulus, 7)
                self.assertEqual(c.l1_distance, cost)
                self.assertEqual(c.squared_root_energy_error, Q(7, 2)*cost*cost)
                self.assertLessEqual(c.squared_root_energy_error, c.coarse_squared_error)
                self.assertFalse(c.balanced_energy_proved_small)
                self.assertFalse(c.normality_proved)
                for residue in range(modulus):
                    self.assertEqual(sum((w for n, w in enumerate(weights, 1)
                                          if n % modulus == residue), Q()), Q(1, modulus))

    def test_complete_period_has_zero_transport_cost(self):
        for N, modulus in ((12, 3), (35, 7), (80, 16)):
            self.assertEqual(clock_transport_budget(N, modulus, 11).squared_root_energy_error, 0)

    def test_missing_residues_rejected(self):
        with self.assertRaises(ValueError):
            balanced_clock_weights(5, 6)
        with self.assertRaises(ValueError):
            clock_transport_budget(5, 0, 2)

    def test_new_joint_schedule_is_strictly_more_permissive(self):
        # N=k^8, H=k^4, Q=k^5+1: sqrt(H)Q/N~1/k, HQ/N~k.
        # The explicit nondividing Q retains a nonzero actual clock debt.
        for k in (2, 3):
            N, H, modulus = k**8, k**4, k**5+1
            c = clock_transport_budget(N, modulus, H)
            self.assertLess(c.coarse_squared_error, Q(1, 2))
            self.assertGreater(Q(H*modulus, N), 1)


class CongruentSeedTests(unittest.TestCase):
    def test_independent_forcing_and_local_holdouts(self):
        cases = ((8, 3, ((2, 3), (3, 4), (5, 2), (7, 3))),
                 (16, 8, ((3, 7), (11, 3), (13, 2))),
                 (37, 19, ((2, 8), (3, 5), (5, 5), (17, 3))))
        def combined(n):
            return Q(120*n*n-89*n+16, (2*n-1)*(4*n-1)*(8*n-7)*(8*n-3))
        for N, m, depths in cases:
            c = congruent_seed_control(N, m, depths)
            self.assertTrue(verify_congruent_seed_control(c))
            self.assertNotEqual(c.initial, 0)
            self.assertFalse(c.authentic_zero_initial)
            self.assertFalse(c.infinite_nonnormal_orbit_established)
            self.assertEqual(c.initial.denominator % 2, 1)
            self.assertEqual(gcd(c.initial.denominator, c.local_modulus), 1)
            previous_u, previous_v = Q(), c.initial
            for n, (u, v) in enumerate(zip(c.authentic_history, c.changed_history), 1):
                self.assertEqual(u-16*previous_u, combined(n))
                self.assertEqual(v-16*previous_v, combined(n))
                for p, depth in depths:
                    self.assertGreaterEqual(rational_valuation(v-u, p),
                                            depth+(4*n if p == 2 else 0))
                if n >= m:
                    self.assertLess(abs(v), c.window_radius)
                previous_u, previous_v = u, v

    def test_empty_local_probe_family_is_legal_control(self):
        c = congruent_seed_control(5, 2)
        self.assertEqual(c.local_modulus, 1)
        self.assertTrue(verify_congruent_seed_control(c))

    def test_false_source_labels_and_lift_mutations_rejected(self):
        c = congruent_seed_control(8, 4, ((3, 3), (5, 2)))
        mutants = (
            replace(c, initial=Q()),
            replace(c, authentic_zero_initial=True),
            replace(c, infinite_nonnormal_orbit_established=True),
            replace(c, changed_history=c.changed_history[:-1]+(c.changed_history[-1]+1,)),
            replace(c, authentic_history=c.authentic_history[:-1]+(c.authentic_history[-1]+Q(1, 7),)),
            replace(c, gain_upper_h1=Q()),
        )
        for mutant in mutants:
            with self.assertRaises(ValueError):
                verify_congruent_seed_control(mutant)

    def test_invalid_prime_constraints_rejected(self):
        for depths in (((6, 2),), ((3, 0),), ((3, 2), (3, 3)),
                       ((5, 2), (3, 2)), ((True, 2),), ((3, 1.5),)):
            with self.assertRaises(ValueError):
                congruent_seed_control(8, 4, depths)

    def test_all_weight_partition_bounds_certified_on_holdouts(self):
        c = congruent_seed_control(12, 8, ((2, 4), (3, 3), (7, 2)))
        xs = c.changed_history[c.start-1:]
        L = len(xs)
        weight_choices = (
            (Q(1, L),)*L,
            tuple(Q(j+1, L*(L+1)//2) for j in range(L)),
            (Q(1, 2),)+ (Q(1, 2*(L-1)),)*(L-1),
        )
        for weights in weight_choices:
            for h in (1, 3):
                full_gain = 1-conditional_energy(xs, (0,)*L, weights, h)
                low, high = real_interval(full_gain)
                self.assertGreaterEqual(low, -Q(1, 10**12))
                self.assertLess(high, seed_gain_upper(c, h))
                nested = refinement_gain(xs, (0,)*L,
                                         tuple(j % 2 for j in range(L)), weights, h)
                nested_low, nested_high = real_interval(nested)
                self.assertGreaterEqual(nested_low, -Q(1, 10**12))
                self.assertLess(nested_high, seed_gain_upper(c, h))

    def test_matrix_deficit_constant_and_actual_interval(self):
        c = congruent_seed_control(9, 6, ((3, 4), (5, 3)))
        xs = c.changed_history[c.start-1:]
        weights = tuple(Q(j+1, 10) for j in range(4))
        for H in (1, 3, 5):
            cap = seed_matrix_deficit_upper(c, H)
            explicit = sum((Q(2*(H-j), H)*seed_gain_upper(c, j)
                            for j in range(1, H)), Q())
            self.assertEqual(cap, explicit)
            deficit = (H-1)-weighted_spectral_excess(xs, weights, H)
            low, high = real_interval(deficit)
            self.assertLessEqual(low, high)
            if H == 1:
                self.assertEqual((low, high, cap), (0, 0, 0))
            else:
                self.assertLess(high, cap)

    def test_unnested_partitions_and_zero_frequency_rejected(self):
        xs = (Q(), Q(1, 3), Q(1, 2))
        weights = (Q(1, 3),)*3
        with self.assertRaises(ValueError):
            refinement_gain(xs, (0, 0, 1), (0, 1, 1), weights)
        with self.assertRaises(ValueError):
            conditional_energy(xs, (0, 0, 0), weights, 0)


if __name__ == "__main__":
    unittest.main()
