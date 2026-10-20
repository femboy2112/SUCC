"""Independent direct censuses and adversarial checks of cloud CRT formulas."""
import unittest
from fractions import Fraction as F
from itertools import product
from math import gcd

from observational_succ.cloud_crt_ascent import (
    cell_enclosure, combine_coprime_patterns, mobius, normalize_residues,
    primitive_density_enclosure, primitive_triangle_budget,
    primitive_triangle_count, rectangle_count, rectangle_enclosure,
    triangle_count, triangle_enclosure, valuation_pattern,
)


def census(X, W, residues, primitive=False):
    R = set(residues)
    return sum((a % W, b % W) in R and (not primitive or gcd(a, b) == 1)
               for a in range(1, int(X) + 1) for b in range(1, int(X) + 1) if a + b <= X)


class CloudCRTTests(unittest.TestCase):
    def test_exhaustive_single_classes_real_cutoffs(self):
        # Independent direct integer census; no use of quotient formula.
        for W in range(1, 9):
            for X2 in range(0, 65):
                X = F(X2, 2)
                for r, s in product(range(W), repeat=2):
                    R = {(r, s)}
                    actual = census(X, W, R)
                    self.assertEqual(triangle_count(X, W, R), actual)
                    self.assertTrue(triangle_enclosure(X, W, R).contains(actual))
                    self.assertTrue(cell_enclosure(X, W, R).contains(actual))

    def test_sets_empty_duplicate_and_normalization(self):
        for W in range(1, 10):
            R = {(a, b) for a, b in product(range(W), repeat=2) if (a + 2*b) % 3}
            self.assertEqual(triangle_count(47, W, R), census(47, W, R))
            self.assertEqual(triangle_count(47, W, []), 0)
        self.assertEqual(normalize_residues(3, [(1, 2), (4, -1)]), {(1, 2)})

    def test_discrepancy_coefficient_is_asymptotically_sharp(self):
        W, m = 1009, 10000
        X = m * W + 2
        error_over_t = (F(triangle_count(X, W, {(1, 1)})) - F(X*X, 2*W*W)) / F(X, W)
        self.assertGreater(error_over_t, F(149, 100))

    def test_modulus_scale_counterexample(self):
        # R={(0,0)}, W=X has predicted mass 1/2 and actual zero for every X.
        for X in (2, 3, 17, 101):
            self.assertEqual(triangle_count(X, X, {(0, 0)}), 0)
            self.assertEqual(F(X * X, 2 * X * X), F(1, 2))
        # Even locally primitive residue classes can be absent at W=X.
        self.assertEqual(triangle_count(101, 101, {(100, 100)}), 0)

    def test_unbalanced_rectangle(self):
        for W in range(1, 8):
            for A, B in ((F(5, 2), 100), (0, 8), (17, F(29, 3))):
                R = {(r, s) for r, s in product(range(W), repeat=2) if (r+s) % 2}
                actual = sum((a % W, b % W) in R for a in range(1, int(A)+1) for b in range(1, int(B)+1))
                self.assertEqual(rectangle_count(A, B, W, R), actual)
                self.assertTrue(rectangle_enclosure(A, B, W, R).contains(actual))
        self.assertEqual(rectangle_count(10000, 3, 3, {(0, 2)}), 3333)
        self.assertEqual(rectangle_count(10000, 2, 3, {(0, 0)}), 0)

    def test_primitive_mobius_against_gcd_census(self):
        for W in range(1, 9):
            for X in (F(1, 2), 2, F(17, 2), 31, 64):
                R = {(r, s) for r, s in product(range(W), repeat=2) if (r+2*s) % 3 != 1}
                self.assertEqual(primitive_triangle_count(X, W, R), census(X, W, R, True))
                for D in sorted({1, max(1, int(X // 4)), max(1, int(X // 2))}):
                    budget = primitive_triangle_budget(X, W, R, D)
                    self.assertTrue(budget.enclosure.contains(census(X, W, R, True)))
                    if X >= 2 and D == int(X//2):
                        self.assertEqual(budget.omitted_divisor_error, 0)

    def test_finite_prime_primitivity_is_not_global(self):
        # (5,5) passes primitivity at 2 and 3; it is globally nonprimitive.
        R = {(5, 5)}
        self.assertEqual(triangle_count(10, 6, R), 1)
        self.assertEqual(primitive_triangle_count(10, 6, R), 0)

    def test_mobius_identity_and_density_intervals(self):
        for n in range(1, 200):
            self.assertEqual(sum(mobius(d) for d in range(1, n+1) if n % d == 0), int(n == 1))
        for W in (1, 2, 6, 25):
            R = {(1 % W, 1 % W)}
            a = primitive_density_enclosure(W, R, 10)
            b = primitive_density_enclosure(W, R, 200)
            self.assertLessEqual(max(a.lower, b.lower), min(a.upper, b.upper))
        self.assertEqual(primitive_density_enclosure(6, {(0, 0)}, 20).upper, 0)

    def test_exact_valuation_cardinalities(self):
        for p in (2, 3, 5, 7):
            W, R = valuation_pattern(p, 0, 0, 0)
            self.assertEqual(W, p)
            self.assertEqual(len(R), (p-1)*(p-2))
            for h in (1, 2):
                for slot in range(3):
                    values = [0, 0, 0]
                    values[slot] = h
                    W, R = valuation_pattern(p, *values)
                    self.assertEqual(len(R), p**h * (p-1)**2)
            self.assertEqual(valuation_pattern(p, 1, 1, 0)[1], frozenset())

    def test_deep_occupation_at_cutoff_is_hostile(self):
        W, R = valuation_pattern(2, 12, 0, 0)
        X = 2**12 + 1
        self.assertEqual(W, 8192)
        self.assertEqual(len(R), 4096)
        self.assertEqual(triangle_count(X, W, R), 1)
        self.assertGreater(F(len(R)*X*X, 2*W*W), 500)

    def test_valuation_residue_identity_independent_enumeration(self):
        for p in (2, 3):
            for vals in ((0,0,0), (1,0,0), (0,2,0), (0,0,2)):
                W, R = valuation_pattern(p, *vals)
                def exact(n, v):
                    return n % (p**v) == 0 and n % (p**(v+1)) != 0
                expected = {(a,b) for a,b in product(range(W), repeat=2)
                            if all(exact(n,v) for n,v in zip((a,b,a+b),vals))}
                self.assertEqual(R, expected)

    def test_crt_product_and_source_mutations(self):
        patterns = [valuation_pattern(2, 1, 0, 0), valuation_pattern(3, 0, 0, 1)]
        W, R = combine_coprime_patterns(patterns)
        self.assertEqual(W, 36)
        self.assertEqual(len(R), len(patterns[0][1])*len(patterns[1][1]))
        self.assertEqual(triangle_count(100, W, R), census(100, W, R))
        self.assertEqual(primitive_triangle_count(100, W, R), census(100, W, R, True))
        with self.assertRaises(ValueError):
            valuation_pattern(4, 0, 0, 1)
        with self.assertRaises(ValueError):
            combine_coprime_patterns([(4, {(1, 1)}), (6, {(1, 1)})])

    def test_invalid_inputs(self):
        for W in (0, -2, True, F(3, 2)):
            with self.assertRaises(ValueError):
                triangle_count(10, W, {(1, 1)})
        for X in (-1, 1.5, True):
            with self.assertRaises(ValueError):
                triangle_count(X, 3, {(1, 1)})
        with self.assertRaises(ValueError):
            primitive_triangle_budget(10, 2, {(1, 1)}, 6)


if __name__ == '__main__':
    unittest.main()
