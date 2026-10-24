"""Exact walk/bound controls plus clearly numerical, independent finite checks."""
import importlib.util
import unittest
from fractions import Fraction as Q
from math import factorial

from observational_succ.interacting_arithmetic_hamiltonian import (
    SourceError, adjacency_walks, unitary_minor_series,
    adjacency_minor_lower_bound, interacting_minor_lower_bound,
    certified_linear_entropy_bound, cutoff_first_leakage,
    finite_hamiltonian, finite_thermal_diagnostics,
)


class ExactInteractingTest(unittest.TestCase):
    def test_half_line_walks_and_boundary(self):
        self.assertEqual(adjacency_walks(1, 2), {1: 1, 3: 1})
        self.assertEqual(adjacency_walks(2, 3), {1: 2, 3: 3, 5: 1})
        self.assertEqual(adjacency_walks(1, 3, 2), {2: 1})

    def test_exact_minor_taylor_coefficient(self):
        coeffs = unitary_minor_series(8)
        self.assertEqual(coeffs[0], 0)
        self.assertEqual(coeffs[1], Q(-1, 2))
        # Independent explicit path matrix powers, no adjacency_walks call.
        size = 12
        powers = [[1, 1]+[0]*(size-2)]
        for _ in range(8):
            prev = powers[-1]
            powers.append([(prev[i-1] if i else 0)+(prev[i+1] if i+1 < size else 0)
                           for i in range(size)])
        for k in range(9):
            want = sum((Q(powers[j][0]*powers[k-j][5]-powers[j][1]*powers[k-j][2],
                          2*factorial(j)*factorial(k-j)) for j in range(k+1)), Q())
            self.assertEqual(coeffs[k], want)

    def test_certified_nonzero_time_windows(self):
        self.assertEqual(adjacency_minor_lower_bound(Q(1, 64)), Q(1, 256))
        self.assertEqual(certified_linear_entropy_bound(0, Q(1, 64), True), Q(1, 32768))
        self.assertEqual(interacting_minor_lower_bound(1, Q(1, 128)), Q(9, 4096))
        for g in (Q(-3), Q(-1, 10), Q(1, 10), Q(1), Q(7)):
            a = abs(g)
            t = a/(4*(13*a*a+12*a+3))
            self.assertGreater(interacting_minor_lower_bound(g, t), 0)
        self.assertEqual(certified_linear_entropy_bound(0, Q(1, 100)), 0)
        self.assertEqual(certified_linear_entropy_bound(1, 1), 0)

    def test_cutoff_leakage_is_exposed(self):
        for cutoff in (2, 4, 7):
            d = cutoff_first_leakage(2, cutoff)
            for k in range(d):
                self.assertEqual(adjacency_walks(2, k), adjacency_walks(2, k, cutoff))
            self.assertNotEqual(adjacency_walks(2, d), adjacency_walks(2, d, cutoff))

    def test_wrong_parameter_types(self):
        with self.assertRaises(SourceError):
            adjacency_minor_lower_bound(0.1)
        with self.assertRaises(SourceError):
            adjacency_walks(1, True)


@unittest.skipUnless(importlib.util.find_spec('numpy') and importlib.util.find_spec('scipy'),
                     'Optional numpy/scipy numerical diagnostics unavailable')
class NumericalInteractingTest(unittest.TestCase):
    def test_spectral_partition_and_tfd(self):
        import numpy as np
        for cutoff in (6, 12, 24):
            for g in (-1.0, 0.0, 0.4):
                for beta in (0.5, 1.0, 2.0):
                    result = finite_thermal_diagnostics(cutoff, g, beta)
                    self.assertLessEqual(result['max_eigenvalue_comparison_defect'], 1e-12)
                    self.assertAlmostEqual(result['tfd_norm_squared'], 1, places=12)
                    self.assertLess(result['tfd_reduction_defect'], 1e-12)
                    self.assertLess(result['independent_expm_defect'], 1e-12)
                    z0 = np.sum(np.arange(1, cutoff+1, dtype=float)**(-beta))
                    zg = np.exp(result['log_partition'])
                    self.assertGreaterEqual(zg, np.exp(-2*beta*abs(g))*z0-1e-11)
                    self.assertLessEqual(zg, np.exp(2*beta*abs(g))*z0+1e-11)
        self.assertFalse(result['infinite_trace_certified_by_this_computation'])

    def test_independent_expm_unitary_minor(self):
        import numpy as np
        from scipy.linalg import expm
        for g in (-1, 0, 1):
            h = finite_hamiltonian(16, g)
            initial = np.zeros(16); initial[:2] = 1/np.sqrt(2)
            for t in (1/256, 1/128):
                v = expm(1j*t*h)@initial
                determinant = v[0]*v[5]-v[1]*v[2]
                self.assertAlmostEqual(float(np.vdot(v, v).real), 1, places=13)
                lower = float(interacting_minor_lower_bound(g, Q(t)))
                self.assertGreaterEqual(abs(determinant), lower-1e-15)
                if g:
                    self.assertGreater(abs(determinant), 0)
                else:
                    self.assertEqual(determinant, 0)

    def test_prefix_cutoff_countercontrol(self):
        result = finite_thermal_diagnostics(6, 0, 2)
        self.assertGreater(result['prime_product_frobenius_defect'], 0)
        self.assertTrue(result['finite_prefix_induces_correlations_even_at_g_zero'])

    def test_nonfinite_parameters_rejected(self):
        for action in (lambda: finite_hamiltonian(4, float('nan')),
                       lambda: finite_thermal_diagnostics(4, 1, 0)):
            with self.assertRaises(SourceError):
                action()


if __name__ == '__main__':
    unittest.main()
