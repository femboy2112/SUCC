"""Exact controls distinguish factorization, coherence, and entanglement."""
import unittest
from fractions import Fraction as Q

from observational_succ.arithmetic_entanglement import (
    SourceError, prime_split, crt_split, rational_ray_density,
    reduced_density, partial_transpose, purity, dephase,
    exact_eigenvector, successor_entanglement_witness,
)


class ArithmeticEntanglementTest(unittest.TestCase):
    def test_prime_source_bijection_and_local_fucc(self):
        for p in (2, 3, 5, 7):
            for n in range(1, 81):
                k, m = prime_split(n, p)
                self.assertEqual(p**k*m, n)
                self.assertNotEqual(m % p, 0)
                self.assertEqual(prime_split(p*n, p), (k+1, m))
        with self.assertRaises(SourceError):
            prime_split(12, 6)

    def test_successor_creates_bell_entanglement(self):
        report = successor_entanglement_witness()
        self.assertEqual(report['before_purity'], 1)
        self.assertEqual(report['after_purity'], Q(1, 2))
        self.assertTrue(report['negative_eigenpair_verified'])
        self.assertFalse(report['successor_is_unitary'])

    def test_full_partial_transpose_spectrum_independent_eigenpairs(self):
        pt = partial_transpose(rational_ray_density({2: 1, 3: 1}))
        a, b, c, d = (0, 1), (0, 3), (1, 1), (1, 3)
        for vector, eigenvalue in (
                ({b: 1}, Q(1, 2)), ({c: 1}, Q(1, 2)),
                ({a: 1, d: 1}, Q(1, 2)), ({a: 1, d: -1}, Q(-1, 2))):
            self.assertTrue(exact_eigenvector(pt, vector, eigenvalue))
        self.assertFalse(exact_eigenvector(pt, {a: 1, d: -1}, Q(1, 2)))

    def test_direct_partial_trace_oracle(self):
        rho = rational_ray_density({2: 1, 3: 1})
        self.assertEqual(reduced_density(rho), {(0, 0): Q(1, 2), (1, 1): Q(1, 2)})
        self.assertEqual(reduced_density(rho, 1), {(1, 1): Q(1, 2), (3, 3): Q(1, 2)})
        self.assertEqual(partial_transpose(partial_transpose(rho)), rho)

    def test_classical_correlation_has_no_negative_pt(self):
        rho = dephase(rational_ray_density({2: 1, 3: 1}))
        self.assertEqual(partial_transpose(rho), rho)
        self.assertEqual(purity(reduced_density(rho)), Q(1, 2))
        # Same marginal purity as Bell does not establish mixed-state entanglement.
        self.assertEqual(purity(rho), Q(1, 2))

    def test_crt_factorization_changes_entanglement(self):
        prime_rho = rational_ray_density({1: 1, 2: 1})
        crt_rho = rational_ray_density({1: 1, 2: 1}, lambda n: crt_split(n, 2, 3))
        self.assertEqual(purity(reduced_density(prime_rho)), 1)
        self.assertEqual(purity(reduced_density(crt_rho)), Q(1, 2))
        for n in range(6):
            a, b = crt_split(n, 2, 3)
            self.assertEqual(crt_split((n+1) % 6, 2, 3), ((a+1) % 2, (b+1) % 3))
        self.assertEqual((2*0) % 6, (2*3) % 6)  # finite dilation is not an isometry

    def test_prime_rectangle_free_state_and_fucc_stay_product(self):
        amplitudes = {n: Q(1, n) for n in (1, 2, 3, 6)}
        state = rational_ray_density(amplitudes)
        moved = rational_ray_density({2*n: a for n, a in amplitudes.items()})
        self.assertEqual(purity(reduced_density(state)), 1)
        self.assertEqual(purity(reduced_density(moved)), 1)

    def test_malformed_or_colliding_sources_rejected(self):
        for action in (lambda: rational_ray_density({1: 0}),
                       lambda: rational_ray_density({1: 0.5}),
                       lambda: rational_ray_density({1: 1, 7: 1}, lambda n: crt_split(n % 6, 2, 3)),
                       lambda: crt_split(1, 2, 4),
                       lambda: prime_split(True)):
            with self.assertRaises(SourceError):
                action()


if __name__ == '__main__':
    unittest.main()
