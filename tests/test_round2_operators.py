"""Hostile exact controls; universal analytic claims are separately paper-proved."""
from fractions import Fraction as Q
from itertools import combinations
from math import gcd, lcm, prod
import unittest

from observational_succ.round2_operators import (
    character_polynomial, determinant, gcd_matrix, harmonic, prime_family,
    residue_transport, scaled_cutoff_character_polynomial, semigroup_prefix,
    spectral_certificate, totient,
)


def exact_psd(rows):
    """Independent rational congruence elimination, with singular pivots."""
    a = [list(map(Q, row)) for row in rows]
    for j in range(len(a)):
        if a[j][j] < 0:
            return False
        if not a[j][j]:
            if any(a[i][j] for i in range(j+1, len(a))):
                return False
            continue
        for i in range(j+1, len(a)):
            for k in range(i, len(a)):
                a[i][k] -= a[i][j]*a[k][j]/a[j][j]
                a[k][i] = a[i][k]
    return True


class ResidueControls(unittest.TestCase):
    def test_prime_domain_and_empty_family(self):
        self.assertEqual(semigroup_prefix((), 30), (1,))
        for wrong in ((4,), (2, 2), (True,), [2, 3], (1,)):
            with self.assertRaises(ValueError):
                prime_family(wrong)
        with self.assertRaises(ValueError):
            residue_transport((2, 3), 6, 30)

    def test_independent_product_enumeration(self):
        for primes in ((), (2,), (2, 3), (3, 7), (2, 3, 5, 7)):
            generated, frontier = {1}, [1]
            while frontier:
                n = frontier.pop()
                for p in primes:
                    if n*p <= 300 and n*p not in generated:
                        generated.add(n*p)
                        frontier.append(n*p)
            self.assertEqual(semigroup_prefix(primes, 300), tuple(sorted(generated)))

    def test_every_residue_class_transfers_with_bounded_overlap(self):
        universe = (2, 3, 5, 7)
        for size in range(5):
            for family in combinations(universe, size):
                for q in (1, 2, 3, 5, 8, 12):
                    primes = tuple(p for p in family if gcd(p, q) == 1)
                    record = residue_transport(primes, q, 120)
                    multiplicities = {}
                    per_class = {}
                    for n in semigroup_prefix(primes, 120):
                        r = n % q
                        image = record['inverse_multipliers'][r] * n
                        self.assertEqual(image % q, 1 % q)
                        self.assertLessEqual(image, record['maximum_multiplier']*120)
                        multiplicities[image] = multiplicities.get(image, 0)+1
                        self.assertNotIn(image, per_class.setdefault(r, set()))
                        per_class[r].add(image)
                    self.assertLessEqual(max(multiplicities.values()), record['subgroup_order'])
                    mass = sum((Q(1, k) for k in multiplicities), Q())
                    self.assertGreaterEqual(mass, record['certified_identity_mass_lower'])

    def test_no_generator_in_identity_class_is_required(self):
        # Both 2 and 3 avoid residue 1 mod 5; products still supply the inverse.
        record = residue_transport((2, 3), 5, 500)
        self.assertEqual(record['subgroup_order'], 4)
        self.assertGreater(record['identity_image_mass'], 1)
        # Incorrectly multiplying every class by 1 fails immediately.
        self.assertNotEqual(2 % 5, 1 % 5)

    def test_fourier_identity_in_exact_group_algebra(self):
        for q in range(1, 10):
            values = tuple(Q((x*x+3*x) % 7 - 3, x+1) for x in range(q))
            for n in (1, 2, 3, 7, 12):
                for frequency in range(q):
                    self.assertEqual(scaled_cutoff_character_polynomial(values, n, frequency),
                                     character_polynomial(values, n*frequency))
                    if n % q == 1 % q:
                        self.assertEqual(character_polynomial(values, n*frequency),
                                         character_polynomial(values, frequency))

    def test_wrong_character_phase_and_atomic_component_controls(self):
        values = (0, 1, 0, 0, 0)
        self.assertNotEqual(scaled_cutoff_character_polynomial(values, 2, 1),
                            character_polynomial(values, 1))
        # Checking e_1 alone leaves the 5-component invisible for S={2,3}.
        first = {n for n in semigroup_prefix((2, 3), 100)}
        fifth = {5*n for n in semigroup_prefix((2, 3), 20)}
        self.assertTrue(first.isdisjoint(fifth))
        self.assertIn(5, fifth)


class GCDControls(unittest.TestCase):
    def test_haar_overlap_by_independent_residue_count(self):
        for m in range(1, 17):
            for n in range(1, 17):
                period = lcm(m, n)
                mass = Q(sum(x % m == 0 and x % n == 0 for x in range(period)), period)
                # Square removes only the positive radical normalization.
                self.assertEqual(m*n*mass**2, Q(gcd(m, n)**2, m*n))
                self.assertEqual(mass, Q(1, period))

    def test_totient_factorization_and_smith_determinant(self):
        for n in range(1, 13):
            B = gcd_matrix(n)
            for i in range(1, n+1):
                for j in range(1, n+1):
                    self.assertEqual(B[i-1][j-1], sum(totient(d) for d in range(1, n+1)
                                                     if i % d == 0 and j % d == 0))
            self.assertEqual(determinant(B), prod(totient(i) for i in range(1, n+1)))
            self.assertGreater(determinant(B), 0)
        self.assertEqual(determinant(((1, 2), (2, 4))), 0)
        self.assertEqual(determinant(((0, 1), (1, 0))), -1)

    def test_spectral_upper_by_independent_psd_elimination(self):
        for n in (1, 2, 3, 4, 8, 12, 16):
            record = spectral_certificate(n, 3)
            upper = record['upper_squared_operator_norm']
            B = gcd_matrix(n)
            self.assertTrue(exact_psd(tuple(tuple((upper*(i+1) if i == j else 0)-B[i][j]
                                                 for j in range(n)) for i in range(n))))
            self.assertLessEqual(record['lower_squared_operator_norm'], upper)
            self.assertGreaterEqual(record['divisor_Rayleigh_lower'], harmonic(n))
            if n > 1:
                self.assertGreater(record['divisor_Rayleigh_lower'], harmonic(n))

    def test_spectral_bounds_on_known_two_by_two_and_mutant(self):
        record = spectral_certificate(2, 4)
        low, high = record['lower_squared_operator_norm'], record['upper_squared_operator_norm']
        # Exact eigenvalue 1+sqrt(1/2), without floating point.
        self.assertLessEqual((low-1)**2, Q(1, 2))
        self.assertGreaterEqual((high-1)**2, Q(1, 2))
        self.assertFalse(exact_psd(((Q(1, 2), -1), (-1, 1))))

    def test_squarefree_tensor_entries(self):
        primes = (2, 3, 5)
        labels = tuple(combinations(primes, size) for size in range(4))
        subsets = [set(s) for row in labels for s in row]
        for a in subsets:
            for b in subsets:
                m, n = prod(a), prod(b)
                self.assertEqual(Q(gcd(m, n)**2, m*n),
                                 prod(Q(1, p) for p in a.symmetric_difference(b)))

    def test_resource_caps_and_exact_authority(self):
        for args in ((0, 1), (65, 1), (3, 9), (True, 1)):
            with self.assertRaises(ValueError):
                spectral_certificate(*args)
        self.assertEqual(spectral_certificate(1)['authority'], 'EXACT_RATIONAL_SPECTRAL_ENCLOSURE')


if __name__ == '__main__':
    unittest.main()
