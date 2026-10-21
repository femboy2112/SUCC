"""Independent residue census; no floating point and no proof-status mocks."""

from collections import Counter
from fractions import Fraction
from itertools import product
from math import gcd
import unittest

from observational_succ.viii_valuation_clocks import (
    PrimeValuationCell, ValuationClockError, crt_cell_signature,
    local_coprime_density, missed_prime_tail_bound, residue_box_enclosure,
    sum_depth_distribution, sum_residue_count, truncated_valuation,
    unit_sum_count, valuation_sum_count,
)


def independent_depth(n, p, k):
    # Independent divisibility tests, unlike repeated division in the module.
    return sum(n % (p**j) == 0 for j in range(1, k + 1))


class ValuationClockTests(unittest.TestCase):
    def test_unit_phase_census(self):
        for p in (2, 3, 5, 7):
            for r in range(6):
                census = Counter(sum(xs) % p for xs in product(range(1, p), repeat=r))
                for phase in range(p):
                    self.assertEqual(unit_sum_count(p, r, phase), census[phase])

    def test_all_valuation_cells_against_independent_enumeration(self):
        # Every cell, including impossible ones and the zero-residue sentinel.
        for p, k, m in ((2, 1, 4), (2, 3, 3), (3, 2, 3), (5, 1, 3)):
            census = Counter()
            residue_census = Counter()
            for xs in product(range(p**k), repeat=m):
                depths = tuple(independent_depth(x, p, k) for x in xs)
                total = sum(xs) % (p**k)
                census[depths, independent_depth(total, p, k)] += 1
                residue_census[depths, total] += 1
            for depths in product(range(k + 1), repeat=m):
                self.assertEqual(sum(sum_depth_distribution(p, k, depths)), 1)
                for j in range(k + 1):
                    self.assertEqual(valuation_sum_count(p, k, depths, j), census[depths, j])
                for total in range(p**k):
                    self.assertEqual(sum_residue_count(p, k, depths, total), residue_census[depths, total])

    def test_unique_minimum_and_binary_parity(self):
        self.assertEqual(sum_depth_distribution(3, 5, (1, 3, 5)), (0, 1, 0, 0, 0, 0))
        self.assertEqual(sum_depth_distribution(2, 4, (0, 0)), (0, Fraction(1, 2), Fraction(1, 4), Fraction(1, 8), Fraction(1, 8)))
        self.assertEqual(sum_depth_distribution(2, 4, (0, 0, 0)), (1, 0, 0, 0, 0))
        self.assertEqual(sum_depth_distribution(3, 3, (3, 3)), (0, 0, 0, 1))

    def test_total_inclusive_pairwise_is_not_summand_only(self):
        for p in (2, 3, 5):
            for m in range(2, 6):
                for include_total in (False, True):
                    good = 0
                    for xs in product(range(p), repeat=m):
                        coordinates = xs + ((sum(xs) % p,) if include_total else ())
                        good += sum(x == 0 for x in coordinates) <= 1
                    self.assertEqual(local_coprime_density(m, p, pairwise=True, include_total=include_total), Fraction(good, p**m))
        self.assertEqual(local_coprime_density(3, 2), Fraction(7, 8))
        self.assertEqual(local_coprime_density(3, 2, pairwise=True), Fraction(1, 2))
        self.assertEqual(local_coprime_density(3, 2, pairwise=True, include_total=True), Fraction(1, 8))

    def test_crt_against_direct_combined_modulus(self):
        cells = (PrimeValuationCell(2, 2, (0, 0), 1), PrimeValuationCell(3, 1, (0, 0), 0))
        m, W, count, density = crt_cell_signature(cells)
        direct = sum(all(tuple(independent_depth(x, c.p, c.k) for x in xs) == c.depths and independent_depth(sum(xs), c.p, c.k) == c.total_depth for c in cells) for xs in product(range(W), repeat=m))
        self.assertEqual(count, direct)
        self.assertEqual(density, Fraction(direct, W**m))

    def test_box_transport_hostile_sparse_and_large_modulus(self):
        for m, W in ((2, 3), (3, 2)):
            for residue in product(range(W), repeat=m):
                for X in range(9):
                    direct = sum(all(x % W == r for x, r in zip(xs, residue)) for xs in product(range(1, X + 1), repeat=m))
                    low, high, main, error = residue_box_enclosure(m, W, 1, X)
                    self.assertLessEqual(low, direct)
                    self.assertLessEqual(direct, high)
                    self.assertLessEqual(abs(direct - main), error)
        self.assertEqual(residue_box_enclosure(3, 5, 1, 10), (8, 8, 8, 0))
        # Moving W=X: the zero class has exactly one point, whereas a sparse
        # class with one coordinate zero and another X-1 still has one. At
        # W=X+1 the zero class is empty despite a main term approaching one.
        self.assertGreater(residue_box_enclosure(2, 101, 1, 100)[2], Fraction(9, 10))
        self.assertEqual(residue_box_enclosure(2, 101, 1, 100)[0], 0)

    def test_global_tail_against_actual_gcd(self):
        primes = (2, 3, 5, 7, 11)
        for m, X in ((2, 11), (3, 7)):
            for P in (1, 2, 3, 5, X):
                for pairwise, include_total in ((False, False), (True, False), (True, True)):
                    missed = 0
                    for xs in product(range(1, X + 1), repeat=m):
                        ys = xs + ((sum(xs),) if include_total else ())
                        gs = [gcd(ys[i], ys[j]) for i in range(len(ys)) for j in range(i)] if pairwise else [gcd(*ys)]
                        finite_ok = all(g % p != 0 for p in primes if p <= P for g in gs)
                        missed += finite_ok and any(g > 1 for g in gs)
                    self.assertLessEqual(missed, missed_prime_tail_bound(m, X, P, pairwise=pairwise, include_total=include_total))

    def test_exact_input_and_immutability_guards(self):
        for invalid in (True, 2.0, Fraction(2), 4, 1):
            with self.assertRaises(ValuationClockError):
                unit_sum_count(invalid, 2)
        for invalid in (True, 1.5, Fraction(1), -1):
            with self.assertRaises(ValuationClockError):
                sum_depth_distribution(2, 3, (0, invalid))
        with self.assertRaises(ValuationClockError):
            sum_depth_distribution(2, 2, ())
        with self.assertRaises(ValuationClockError):
            sum_depth_distribution(2, 2, (3,))
        original = [0, 0]
        cell = PrimeValuationCell(2, 2, original, 1)
        original[0] = 2
        self.assertEqual(cell.depths, (0, 0))
        with self.assertRaises(ValuationClockError):
            crt_cell_signature((cell, cell))
        self.assertEqual(truncated_valuation(-8, 2, 4), 3)


if __name__ == "__main__":
    unittest.main()
