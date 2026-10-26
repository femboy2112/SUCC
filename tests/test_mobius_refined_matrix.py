"""Independent exact finite witnesses; no sampled asymptotic authority."""
import unittest
from dataclasses import replace
from fractions import Fraction as Q
from itertools import product
from math import gcd

from observational_succ import mobius_refined_matrix as M
from observational_succ.succ_internal_matrix_walk import (
    PhasePoly as P, MatrixWalk, authentic_r, frequency_boundary_witness,
    temporal_derivative_boundary, finite_koopman_phases,
)


def independent_r(n):
    return Q(120*n*n-89*n+16, (2*n-1)*(4*n-1)*(8*n-7)*(8*n-3))


def power(matrix, other):
    return tuple(tuple(sum(matrix[i][k]*other[k][j] for k in range(len(matrix)))
                       for j in range(len(matrix))) for i in range(len(matrix)))


def projection(labels, weights=None):
    n = len(labels)
    weights = (Q(1, n),)*n if weights is None else weights
    return tuple(tuple(weights[j]/sum(weights[k] for k in range(n) if labels[k] == labels[i])
                       if labels[i] == labels[j] else Q() for j in range(n)) for i in range(n))


def matrix_sub(a, b):
    return tuple(tuple(x-y for x, y in zip(r, s)) for r, s in zip(a, b))


class AuthenticSourceAndCharts(unittest.TestCase):
    def test_independent_forcing_and_zero_selector(self):
        u = Q()
        for n, value in enumerate(M.source_states(80), 1):
            u = 16*u+independent_r(n)
            self.assertEqual(value, u)
        self.assertEqual(M.authenticate(M.source_states(10)), M.source_states(10))

    def test_changed_seed_and_integer_carry_rejected(self):
        history = M.source_states(8)
        for delta in (Q(1), Q(1, 17)):
            mutant = tuple(x+16**n*delta for n, x in enumerate(history, 1))
            with self.assertRaises(M.RefinementError): M.authenticate(mutant)
        with self.assertRaises(M.RefinementError): M.authenticate(tuple(x % 1 for x in history))

    def test_p3_p5_charts_do_not_reduce_illegally(self):
        x = M.source_states(1)[0]
        self.assertEqual(x, Q(47, 15))
        for p in (3, 5):
            with self.assertRaises(M.RefinementError): M.integral_residue(x, p, 2)
            v, unit = M.valuation_chart(x, p, 2)
            self.assertEqual(v, -1)
            self.assertEqual(unit, M.integral_residue(p*x, p, 2))

    def test_dyadic_integer_lift_is_not_fractional_part(self):
        x = Q(47, 15)
        self.assertEqual((M.integral_residue(x, 2, 3)-M.integral_residue(x % 1, 2, 3)) % 8, 3)
        for x in M.source_states(30):
            self.assertEqual(x.denominator % 2, 1)
            self.assertIsInstance(M.integral_residue(x, 2, 4), int)

    def test_zero_and_negative_valuation_chart(self):
        self.assertEqual(M.valuation_chart(Q(), 3, 2), (None, 0))
        self.assertEqual(M.valuation_chart(Q(-9, 5), 3, 2), (2, 7))

    def test_malformed_inputs_fail_closed(self):
        for x in (True, 1.0, '2'):
            with self.assertRaises(M.RefinementError): M.source_states(x)
            with self.assertRaises(M.RefinementError): M.rational(x)
        for p in (1, 4, 6, 9):
            with self.assertRaises(M.RefinementError): M.prime(p)
        with self.assertRaises(M.RefinementError): M.integral_residue(Q(1), 3, 0)


class SourcePoleArithmetic(unittest.TestCase):
    def test_small_prime_first_depth_requires_second_digit(self):
        for p, residues, denominator in ((3, 8, 9), (5, 14, 25)):
            grid = M.PrimeGrid((p,), (1,))
            self.assertEqual(grid.modulus, denominator)
            self.assertEqual(sum(grid.signature(n)[0] for n in range(1, denominator+1)), residues)
            self.assertEqual(M.pole_tail_density(p, 1), Q(residues, denominator))
            self.assertTrue(any(grid.signature(n) != grid.signature(n+p) for n in range(1, denominator+1)))

    def test_exceptional_residue_description(self):
        for n in range(1, 901):
            self.assertEqual(M.valuation(independent_r(n), 3) < 0, n % 9 != 8)
            self.assertEqual(M.valuation(independent_r(n), 5) < 0,
                             n % 5 in (1, 3, 4) and n % 25 != 24)

    def test_deep_four_pole_counts_and_periodicity(self):
        for p in (3, 5, 7, 11, 13):
            for k in range(1, 4):
                q = p**max(k, 2) if p in (3, 5) else p**k
                count = 0
                for n in range(1, q+1):
                    hit = M.valuation(independent_r(n), p) <= -k
                    count += hit
                    self.assertEqual(hit, M.valuation(independent_r(n+q), p) <= -k)
                self.assertEqual(Q(count, q), M.pole_tail_density(p, k))

    def test_dyadic_pole_grid_is_blind_but_digits_are_not(self):
        grid = M.PrimeGrid((2,), (5,))
        self.assertEqual(grid.modulus, 1)
        self.assertEqual({grid.signature(n) for n in range(1, 100)}, {(0,)})
        self.assertEqual(grid.density((0,)), 1)
        self.assertTrue(all(grid.density((j,)) == 0 for j in range(1, 6)))
        self.assertGreater(len({M.integral_residue(x, 2, 3) for x in M.source_states(8)}), 1)

    def test_joint_crt_atom_densities_and_incomplete_period_bounds(self):
        for grid in (M.PrimeGrid((3, 5), (1, 1)), M.PrimeGrid((3, 7), (2, 1)),
                     M.PrimeGrid((2, 7), (2, 2)), M.PrimeGrid((7, 11), (1, 1))):
            q = grid.modulus
            counts = {a: 0 for a in grid.cells}
            for n in range(1, q+1): counts[grid.signature(n)] += 1
            self.assertEqual(sum(grid.density(a) for a in grid.cells), 1)
            for a in grid.cells: self.assertEqual(counts[a], q*grid.density(a))
            for n in (1, q-1, q+3, 2*q+1):
                observed = {a: 0 for a in grid.cells}
                for j in range(1, n+1): observed[grid.signature(j)] += 1
                for a in grid.cells:
                    low, high = grid.count_bounds(n, a)
                    self.assertLessEqual(low, observed[a]); self.assertLessEqual(observed[a], high)

    def test_grids_and_coordinates_are_typed(self):
        for args in (((3, 3), (1, 1)), ((5, 3), (1, 1)), ((6,), (1,)), ((3,), (0,)), ((3,), ())):
            with self.assertRaises(M.RefinementError): M.PrimeGrid(*args)
        grid = M.PrimeGrid((3,), (2,))
        for a in ((3,), (True,), (), [1]):
            with self.assertRaises(M.RefinementError): grid.check_cell(a)
        with self.assertRaises(M.RefinementError): grid.signature(0)


class DirectedMatrixSystem(unittest.TestCase):
    def test_mobius_chain_not_parity_conjugation(self):
        grid = M.PrimeGrid((3,), (2,))
        self.assertEqual(grid.mobius((0,), (2,)), 0)
        self.assertEqual(grid.mobius((0,), (1,)), -1)
        self.assertEqual(grid.mobius((2,), (1,)), 0)

    def test_zeta_inverse_on_products_of_chains(self):
        for grid in (M.PrimeGrid(), M.PrimeGrid((3,), (3,)), M.PrimeGrid((2, 5), (2, 2))):
            cells = grid.cells
            z = tuple(tuple(int(all(x <= y for x, y in zip(a, b))) for b in cells) for a in cells)
            m = tuple(tuple(grid.mobius(a, b) for b in cells) for a in cells)
            identity = tuple(tuple(int(i == j) for j in range(len(cells))) for i in range(len(cells)))
            self.assertEqual(power(z, m), identity); self.assertEqual(power(m, z), identity)

    def test_mobius_blocks_equal_direct_grams(self):
        for grid in (M.PrimeGrid(), M.PrimeGrid((3, 5), (2, 1)), M.PrimeGrid((2, 7), (2, 2))):
            walk = M.RefinedMatrixWalk.build(12, grid, (0, 1, 3))
            self.assertEqual(M.invert_thresholds(grid, walk.thresholds(), 3), dict(walk.blocks))
            for a, block in walk.blocks:
                indices = [n for n in range(1, 13) if grid.signature(n) == a]
                for i, h in enumerate(walk.frequencies):
                    for j, k in enumerate(walk.frequencies):
                        self.assertEqual(block[i][j], sum((P.monomial((h-k)*walk.history[n-1]) for n in indices), P.zero()))

    def test_rank_one_succ_and_parent_matrix_integration(self):
        grid = M.PrimeGrid((3, 7), (2, 1))
        walk = M.RefinedMatrixWalk.build(0, grid, (0, 1, 2))
        parent = MatrixWalk.initial(3)
        for n in range(1, 9):
            previous = dict(walk.blocks); walk = walk.succ(); parent = parent.succ()
            self.assertEqual(walk.gram(), parent.gram)
            changed = grid.signature(n)
            for a, block in walk.blocks:
                delta = M.rank_one(walk.history[-1], walk.frequencies) if a == changed else M.zero_matrix(3)
                self.assertEqual(block, M.matrix_add(previous[a], delta))

    def test_commuting_time_prime_depth_and_frequency_growth(self):
        coarse = M.PrimeGrid((7,), (1,)); fine = M.PrimeGrid((3, 7), (2, 2))
        w = M.RefinedMatrixWalk.build(7, coarse, (0, 1))
        richer = w.refine(fine, (0, 1, 16))
        self.assertEqual(richer.coarsen(coarse, (0, 1)), w)
        self.assertEqual(w.succ().refine(fine, (0, 1, 16)), richer.succ())
        self.assertEqual(richer.prefix(4).coarsen(coarse, (0, 1)), w.prefix(4))
        intermediate = w.refine(M.PrimeGrid((3, 7), (1, 1)), (0, 1))
        self.assertEqual(intermediate.refine(fine, (0, 1, 16)), richer)

    def test_psd_is_a_sum_of_actual_squares(self):
        w = M.RefinedMatrixWalk.build(8, M.PrimeGrid((3,), (2,)), (0, 1, 4))
        c = (Q(2), Q(-3, 2), Q(1, 7))
        for a, block in w.blocks:
            quadratic = sum((c[i]*c[j]*block[i][j] for i in range(3) for j in range(3)), P.zero())
            witness = sum((M.abs2(sum((c[i]*P.monomial(w.frequencies[i]*x) for i in range(3)), P.zero()))
                           for n, x in enumerate(w.history, 1) if w.grid.signature(n) == a), P.zero())
            self.assertEqual(quadratic, witness)

    def test_incomplete_factorial_and_forged_source_are_rejected(self):
        w = M.RefinedMatrixWalk.build(5, M.PrimeGrid((3,), (1,)), (0, 1))
        t = w.thresholds(); t.pop((1,))
        with self.assertRaises(M.RefinementError): M.invert_thresholds(w.grid, t, 2)
        with self.assertRaises(M.RefinementError): replace(w, history=tuple(x+1 for x in w.history))
        with self.assertRaises(M.RefinementError): w.refine(M.PrimeGrid(), (0, 1))
        with self.assertRaises(M.RefinementError): w.coarsen(w.grid, (0, 17))

    def test_fucc_time_transport_not_scalar_multiplication(self):
        history = M.source_states(24)
        for n, p in ((1, 2), (3, 5), (2, 7)):
            paths = M.affine_source_paths(history, n, p)
            self.assertEqual(paths['left'][-1], paths['right'][-1])
            self.assertEqual(paths['full_gradient_holonomy'], 0)
            self.assertNotEqual(history[p*n-1], p*history[n-1])
        with self.assertRaises(M.RefinementError): M.affine_source_paths(history, 1, 6)
        with self.assertRaises(M.RefinementError): M.source_index_view(history, (25,))

    def test_frequency_boundary_is_not_removed(self):
        self.assertEqual(finite_koopman_phases(5, 1, 6)['finite_compression_boundary_squared_norm'], 1)
        for j in range(5):
            self.assertEqual(frequency_boundary_witness(j)['limiting_twist'], Q(15, 64))
            self.assertEqual(temporal_derivative_boundary(j)['limiting_drift'], Q(15, 32))


class EnergyAndClockCalibration(unittest.TestCase):
    def test_nested_refinement_positive_squares_and_telescope(self):
        states = M.source_states(10)
        labels = ((0,)*10, tuple(n % 2 for n in range(10)),
                  tuple(n % 4 for n in range(10)), tuple(range(10)))
        gain = P.zero()
        for a, b in zip(labels, labels[1:]):
            delta, squares = M.refinement_energy(states, a, b)
            self.assertEqual(delta, sum((m*M.abs2(s) for m, s in squares), P.zero()))
            gain += delta
        self.assertEqual(gain+M.conditional_energy(states, labels[0]), P.one())

    def test_unnested_projection_refused(self):
        with self.assertRaises(M.RefinementError): M.refinement_energy((Q(0), Q(1, 2), Q(1, 3)), (0, 0, 1), (0, 1, 0))

    def test_distinct_correlated_features_have_negative_mobius_energy(self):
        phases = (Q(), Q(), Q(1, 2)); a = (0, 0, 1); b = (0, 1, 1)
        mixed = M.boolean_energy_contrast(phases, (a, b))
        self.assertEqual(M.half_turn_evaluation(mixed), Q(-2, 9))
        pa, pb = projection(a), projection(b)
        self.assertNotEqual(power(pa, pb), power(pb, pa))

    def test_balanced_crt_projections_commute_but_raw_ones_do_not(self):
        n, q = 8, 6
        a = tuple(j % 2 for j in range(1, n+1)); b = tuple(j % 3 for j in range(1, n+1))
        raw_a, raw_b = projection(a), projection(b)
        self.assertNotEqual(power(raw_a, raw_b), projection((0,)*n))
        weights = M.balanced_weights(n, q)
        balanced_a, balanced_b = projection(a, weights), projection(b, weights)
        self.assertEqual(power(balanced_a, balanced_b), projection((0,)*n, weights))
        self.assertEqual(power(balanced_a, balanced_b), power(balanced_b, balanced_a))

    def test_balancing_cost_is_exact_and_sharp(self):
        for n in range(1, 40):
            for q in range(1, n+1):
                weights = M.balanced_weights(n, q)
                exact = sum(abs(w-Q(1, n)) for w in weights)
                self.assertEqual(exact, M.balancing_cost(n, q))
                self.assertLessEqual(exact, Q(q, 2*n))
                for a in range(q):
                    self.assertEqual(sum(w for j, w in enumerate(weights, 1) if j % q == a), Q(1, q))

    def test_missing_crt_residues_cannot_be_fabricated(self):
        with self.assertRaises(M.RefinementError): M.balanced_weights(5, 6)
        with self.assertRaises(M.RefinementError): M.primitive_clock_budget(M.source_states(5), 6)

    def test_energy_transport_exhaustive_sign_controls(self):
        for n in range(2, 8):
            for q in range(1, n+1):
                weights = M.balanced_weights(n, q)
                cap = M.clock_transport_caps(n, q)['conditional_energy_error']
                for bits in product((0, 1), repeat=n):
                    phases = tuple(Q(b, 2) for b in bits)
                    labels = tuple(i % 3 for i in range(n))
                    a = M.half_turn_evaluation(M.conditional_energy(phases, labels))
                    b = M.half_turn_evaluation(M.conditional_energy(phases, labels, weights=weights))
                    self.assertLessEqual(abs(a-b), cap)

    def test_matrix_dimension_error_budget_is_not_dropped(self):
        a = M.clock_transport_caps(101, 30, 9)
        self.assertEqual(a['purity_error'], 2*9**2*a['mean_error'])
        self.assertEqual(a['gram_operator_error'], 9*a['mean_error'])
        self.assertEqual(M.clock_transport_caps(120, 30, 9)['purity_error'], 0)

    def test_gcd_clock_projector_and_primitive_orthogonality(self):
        for q in (4, 6, 12):
            values = tuple(P.monomial(Q(a, 17)) for a in range(q))
            for d in M.divisors(q):
                for e in M.divisors(q):
                    self.assertEqual(M.clock_projection(M.clock_projection(values, e), d),
                                     M.clock_projection(values, gcd(d, e)))
            budget = M.primitive_clock_budget(tuple(Q(a, 17) for a in range(q)), q)
            components = budget['components']
            for d, e in product(components, repeat=2):
                if d != e:
                    self.assertEqual(sum((x*y.star() for x, y in zip(components[d], components[e])), P.zero()), P.zero())
            self.assertEqual(sum(budget['energies'].values(), P.zero()), P.one())

    def test_complete_clock_budget_with_real_source_and_nonfull_period(self):
        states = M.source_states(13)
        b = M.primitive_clock_budget(states, 6)
        self.assertEqual(b['within_residue']+sum(b['energies'].values(), P.zero()), P.one())
        weights = M.balanced_weights(13, 6)
        self.assertEqual(b['balanced_mean_squared'], M.conditional_energy(states, (0,)*13, weights=weights))

    def test_balanced_boolean_contrast_nonnegative_exhaustively(self):
        n, q = 8, 6
        features = (tuple(j % 2 for j in range(1, n+1)), tuple(j % 3 for j in range(1, n+1)))
        weights = M.balanced_weights(n, q)
        for bits in product((0, 1), repeat=n):
            result = M.boolean_energy_contrast(tuple(Q(b, 2) for b in bits), features, weights=weights)
            self.assertGreaterEqual(M.half_turn_evaluation(result), 0)

    def test_singleton_resolution_floor(self):
        self.assertEqual(M.singleton_energy_floor(tuple(range(8))), 1)
        self.assertEqual(M.singleton_energy_floor((0, 0, 1, 2)), Q(1, 2))
        states = M.source_states(8)
        self.assertEqual(M.conditional_energy(states, tuple(range(8))), P.one())


class CertifiedControls(unittest.TestCase):
    def test_cosine_interval_known_cyclotomic_controls(self):
        for phase, exact in ((Q(), Q(1)), (Q(1, 2), Q(-1)), (Q(1, 3), Q(-1, 2)),
                             (Q(1, 4), Q()), (Q(1, 6), Q(1, 2))):
            e = P.monomial(phase)
            low, high = M.real_phase_interval((e+e.star())/2)
            self.assertLessEqual(low, exact); self.assertLessEqual(exact, high)
            self.assertLess(high-low, Q(1, 10**12))

    def test_interval_rejects_nonhermitian_and_halfturn_wrong_conductor(self):
        with self.assertRaises(M.RefinementError): M.real_phase_interval(P.monomial(Q(1, 3)))
        with self.assertRaises(M.RefinementError): M.half_turn_evaluation(P.monomial(Q(1, 3)))

    def test_authentic_p5_p7_mobius_contrast_is_certifiably_negative(self):
        states = M.source_states(3)
        columns = tuple(tuple(M.PrimeGrid((p,), (1,)).signature(n)[0] for n in range(1, 4))
                        for p in (5, 7))
        low, high = M.real_phase_interval(M.boolean_energy_contrast(states, columns))
        self.assertGreater(low, Q(-42062808675, 10**12))
        self.assertLess(high, Q(-42062808674, 10**12))

    def test_true_source_has_certified_nonzero_refinement_gain(self):
        states = M.source_states(8)
        labels = tuple(M.PrimeGrid((3,), (1,)).signature(n) for n in range(1, 9))
        gain, _ = M.refinement_energy(states, (0,)*8, labels)
        low, high = M.real_phase_interval(gain)
        self.assertGreater(low, 0); self.assertLess(high, 1)

    def test_changed_seed_preserves_all_forcing_and_odd_prime_charts(self):
        for n, start in ((8, 3), (20, 8), (48, 16)):
            control = M.coherent_seed_control(n, start, (3, 5, 7))
            previous = control['initial']
            self.assertEqual(previous.denominator % 2, 1)
            self.assertEqual(gcd(previous.denominator, 3*5*7), 1)
            for j, x in enumerate(control['states'], 1):
                self.assertEqual(x-16*previous, independent_r(j)); previous = x
                self.assertEqual(x.denominator % 2, 1)
            with self.assertRaises(M.RefinementError): M.authenticate(control['states'])
            self.assertTrue(all(abs(x) < control['radius'] for x in control['states'][start-1:]))

    def test_all_partition_counterfeit_bound_certified(self):
        control = M.coherent_seed_control(16, 8, (3, 5, 7))
        states = control['states'][7:]
        # Full singleton gain dominates every intermediate partition's gain.
        gain = 1-M.conditional_energy(states, (0,)*len(states))
        low, high = M.real_phase_interval(gain)
        self.assertGreaterEqual(low, -Q(1, 10**12))
        self.assertLess(high, control['all_partition_gain_cap_h1'])

    def test_fixed_nonnormal_control_is_uniformly_observer_resistant(self):
        states = M.counterfeit_states(12)
        gain = 1-M.conditional_energy(states, (0,)*12)
        _, high = M.real_phase_interval(gain)
        self.assertLess(high, M.counterfeit_gain_cap(12))
        with self.assertRaises(M.RefinementError): M.authenticate(states)

    def test_null_positive_and_mutation_controls(self):
        constant = (Q(1, 3),)*8
        self.assertEqual(M.conditional_energy(constant, (0,)*8), P.one())
        self.assertEqual(M.refinement_energy(constant, (0,)*8, tuple(range(8)))[0], P.zero())
        phases = (Q(), Q(1, 2))
        gain, _ = M.refinement_energy(phases, (0, 0), (0, 1))
        self.assertEqual(M.half_turn_evaluation(gain), 1)
        self.assertEqual(M.half_turn_evaluation(-gain), -1)  # wrong orientation killed


if __name__ == '__main__':
    unittest.main()
