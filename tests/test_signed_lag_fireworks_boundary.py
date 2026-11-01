"""Exact finite controls of the paper proofs in signed_lag_fireworks/BOUNDARY.md."""
import importlib.util
import itertools
from fractions import Fraction as F
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


def load(name, relative):
    spec = importlib.util.spec_from_file_location(name, ROOT / relative)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


B = load('fireworks_boundary_exact', 'research/2026-10-31/signed_lag_fireworks/boundary.py')
L = load('fireworks_boundary_original_lag', 'research/2026-10-31/selected_lag_tomography/selected_lag.py')


def correlation_energy(z, K):
    """Independent pair expansion, rather than production sliding windows."""
    N = len(z)
    diagonal = K*sum(a*a+b*b for a, b in z)
    offdiagonal = 0
    for i in range(N):
        for j in range(i+1, N):
            if j-i < K:
                offdiagonal += 2*(K-(j-i))*(z[i][0]*z[j][0]+z[i][1]*z[j][1])
    return F(diagonal+offdiagonal, N*K*K)


class BoundaryTests(unittest.TestCase):
    def test_window_pair_oracle_exhaustive(self):
        phases = ((1, 0), (0, 1), (-1, 0), (0, -1))
        for z in itertools.product(phases, repeat=4):
            for K in (1, 2, 3, 4, 5, 8):
                self.assertEqual(B.window_energy(z, K), correlation_energy(z, K))

    def test_two_scale_exhaustive(self):
        phases = ((1, 0), (0, 1), (-1, 0), (0, -1))
        for z in itertools.product(phases, repeat=4):
            energies = {m: correlation_energy(z, m) for m in range(1, 10)}
            for K in range(1, 10):
                for m in range(1, K+1):
                    self.assertLessEqual(energies[K], B.two_scale_energy_upper(energies[m], K, m))

    def test_nonunit_and_rational_inputs(self):
        z = ((F(3, 5), F(4, 5)), (F(-1, 3), F(1, 7)), (0, 0), (1, 0))
        for K in range(1, 11):
            energy = B.window_energy(z, K)
            self.assertEqual(energy, correlation_energy(z, K))
            self.assertLessEqual(energy, 1)
            for m in range(1, K+1):
                self.assertLessEqual(energy, B.two_scale_energy_upper(B.window_energy(z, m), K, m))

    def test_remainder_is_necessary(self):
        # Coherent two-point sequence: omitting the remainder gives a false bound.
        z = ((1, 0), (1, 0))
        self.assertGreater(B.window_energy(z, 3), F(2, 3)*B.window_energy(z, 2))
        self.assertLessEqual(B.window_energy(z, 3), B.two_scale_energy_upper(B.window_energy(z, 2), 3, 2))

    def test_source_recurrence_matches_original(self):
        for M in range(1, 31):
            self.assertEqual(B.selected_state(M), L.original_states(M)[-1])
            # Independently sum exact weighted pole contributions without recurrence.
            closed = sum((16**(M-j)*sum((F(c, 8*j-a) for c, a in
                         ((4, 7), (-2, 4), (-1, 3), (-1, 2))), F(0))
                         for j in range(1, M+1)), F(0))
            self.assertEqual(B.selected_state(M), closed)

    def test_shadow_integer_target_and_defect(self):
        for M in (1, 2, 3, 7, 16, 32):
            for J in (0, 1, B.shadow_rounding_depth(M)):
                data = B.dyadic_shadow(M, J)
                self.assertGreaterEqual(data['rounding_defect'], 0)
                self.assertLess(data['rounding_defect'], F(1, 16**J))
                self.assertEqual(16**M*data['q'], B.selected_state(M)-data['rounding_defect'])
                for n in range(M+J, M+J+6):
                    for h in (-11, -1, 1, 3, 5, 7, 11):
                        self.assertEqual((h*16**n*data['q']).denominator, 1)

    def test_minimal_logarithmic_delay(self):
        for M in range(1, 201):
            J = B.shadow_rounding_depth(M)
            self.assertGreaterEqual(16**J, 64*M*M)
            self.assertLess(16**(J-1), 64*M*M)
            data = B.dyadic_shadow(M)
            self.assertLessEqual(data['seed_distance_upper'], F(1, 32*M*M*16**M))

    def test_independent_machin_seed_bracket(self):
        # Genuine irrational seed remains symbolic; these are rational outward bounds.
        lo, hi = L._machin_pi_bracket(40)
        for M in range(1, 7):
            data = B.dyadic_shadow(M)
            seed_lo, seed_hi = data['q']-hi/16, data['q']-lo/16
            self.assertLess(seed_hi, 0)
            self.assertGreater(seed_lo, -data['seed_distance_upper'])

    def test_prefix_weyl_bound_from_direct_geometric_sum(self):
        for M in (1, 3, 10, 32):
            data = B.dyadic_shadow(M)
            for h in (1, 3, 5, 7, 11):
                direct = F(44*h, 7)*data['seed_distance_upper']*sum(16**n for n in range(1, M+1))
                self.assertEqual(B.shadow_prefix_weyl_error_upper(M, h), direct)
                self.assertLess(direct, F(22*h, 105*M*M))

    def test_lag_sensitivity_direct_double_sum(self):
        for M, N, K in ((4, 3, 2), (8, 8, 4), (16, 11, 5)):
            d = B.dyadic_shadow(M)['seed_distance_upper']
            for h in (1, 3, 5, 7, 11):
                direct = sum((F(88*h, 7*K*N)*F(K-k, K)*(16**k-1)*16**n*d
                              for k in range(1, K) for n in range(1, N-k+1)), F(0))
                self.assertEqual(B.shadow_lag_error_upper(M, N, K, h), direct)

    def test_coherent_shadow_lower_at_increasing_horizons(self):
        for h in (1, 3, 5, 7, 11):
            previous = F(-10)
            for K in (3, 4, 5, 6, 7):
                lower = B.shadow_lag_lower(16**K, K, h, M=8)
                self.assertGreater(lower, previous)
                self.assertLess(lower, 1)
                previous = lower
            self.assertGreater(previous, F(4, 5))

    def test_reject_invalid_inputs(self):
        for args in ((-1, 4, 2), (F(3, 2), 4, 2), (F(1, 2), 2, 3)):
            with self.assertRaises(ValueError):
                B.two_scale_energy_upper(*args)
        with self.assertRaises(ValueError):
            B.window_energy(((1, 1),), 2)
        with self.assertRaises(ValueError):
            B.dyadic_shadow(0)
        with self.assertRaises(ValueError):
            B.dyadic_shadow(1, -1)
        with self.assertRaises(ValueError):
            B.shadow_lag_error_upper(3, 4, 2)
        with self.assertRaises(ValueError):
            B.shadow_prefix_weyl_error_upper(3, 0)


if __name__ == '__main__':
    unittest.main()
