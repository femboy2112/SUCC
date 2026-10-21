"""Independent rational atanh, combinatorial, and entropy holdouts."""
import unittest
from fractions import Fraction
from itertools import product
from math import comb, factorial

from observational_succ.viii_simplex_asymptotics import (
    SimplexAsymptoticError, binomial_log_correction, binomial_entropy_enclosure,
    residue_population, residue_log_correction,
)


def negative_log_oracle(N, m, terms=100):
    """Independent atanh expansion of each factor, all rational incl. tail."""
    lower = upper = Fraction(0)
    for j in range(1, m):
        y = Fraction(j, 2 * N - j)
        partial = 2 * sum((y ** (2 * k + 1) / (2 * k + 1)
                           for k in range(terms)), Fraction(0))
        tail = 2 * y ** (2 * terms + 1) / ((2 * terms + 1) * (1 - y ** 2))
        lower += partial
        upper += partial + tail
    return lower, upper


class TestDimensionCorrections(unittest.TestCase):
    def test_log_enclosure_against_independent_atanh_series(self):
        for N in range(1, 20):
            for m in range(1, N + 1):
                lo, hi = negative_log_oracle(N, m)
                for depth in (1, 2, 4):
                    rec = binomial_log_correction(N, m, depth)
                    lower, upper = rec.negative_log_interval
                    self.assertLessEqual(lower, lo)
                    self.assertLessEqual(hi, upper)
                    self.assertEqual(rec.volume_ratio, Fraction(comb(N, m) * factorial(m), N ** m))

    def test_explicit_first_and_second_corrections(self):
        for N in (10, 100, 10000):
            for m in (1, 2, 7):
                one = binomial_log_correction(N, m, 1)
                two = binomial_log_correction(N, m, 2)
                self.assertEqual(one.correction, Fraction(m * (m - 1), 2 * N))
                self.assertEqual(two.correction - one.correction,
                                 Fraction(m * (m - 1) * (2 * m - 1), 12 * N ** 2))
                self.assertLessEqual(two.remainder_upper, one.remainder_upper)

    def test_entropy_enclosure_including_endpoints_and_zero_region(self):
        for N in range(81):
            for m in range(N + 3):
                rec = binomial_entropy_enclosure(N, m)
                self.assertEqual(rec.count, comb(N, m) if m <= N else 0)
                self.assertLessEqual(rec.lower, rec.count)
                self.assertLessEqual(rec.count, rec.upper)

    def test_residue_counts_by_direct_integer_census(self):
        for m in range(1, 4):
            for W in range(1, 4):
                for X in range(0, 13):
                    census = {rs: 0 for rs in product(range(W), repeat=m)}
                    for xs in product(range(1, X + 1), repeat=m):
                        if sum(xs) <= X:
                            census[tuple(x % W for x in xs)] += 1
                    for rs, count in census.items():
                        N = residue_population(W, X, rs)
                        self.assertEqual(count, comb(N, m) if N >= m else 0)
                        rec = residue_log_correction(W, X, rs)
                        self.assertEqual(count, rec.count if rec else 0)

    def test_real_cutoff_and_residue_shift_are_preserved(self):
        self.assertEqual(residue_population(3, Fraction(19, 2), (0, 1)), 3)
        self.assertEqual(residue_log_correction(3, Fraction(19, 2), (0, 1)).count, 3)
        # Dropping rho/floor changes occupied strata, even at the same W,X,m.
        self.assertEqual(residue_log_correction(3, 4, (1, 1)).count, 1)
        self.assertIsNone(residue_log_correction(3, 4, (0, 0)))

    def test_strict_exact_input_guards(self):
        for bad in (True, 3.0, Fraction(3)):
            with self.assertRaises(SimplexAsymptoticError):
                binomial_log_correction(bad, 1)
            with self.assertRaises(SimplexAsymptoticError):
                binomial_entropy_enclosure(5, bad)
            with self.assertRaises(SimplexAsymptoticError):
                residue_population(bad, 5, (0,))
        for args in ((0, 0), (2, 3), (3, 0)):
            with self.assertRaises(SimplexAsymptoticError):
                binomial_log_correction(*args)
        with self.assertRaises(SimplexAsymptoticError):
            residue_log_correction(1, 0, (0,), depth=False)
        with self.assertRaises(SimplexAsymptoticError):
            residue_population(3, 4.0, (1,))


if __name__ == "__main__":
    unittest.main()
