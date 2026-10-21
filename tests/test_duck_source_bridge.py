from dataclasses import FrozenInstanceError
from fractions import Fraction
from math import gcd
import unittest

from observational_succ.duck_source_bridge import (
    conditional_fourier_budget, log_zeta2_partial, prime_power_terms,
    residual_square_consequence, thue_morse_digit, thue_morse_prefix_interval,
)


class DuckSourceBridgeTests(unittest.TestCase):
    def test_prime_power_weights_independent_factorization(self):
        import sympy as sp
        for cutoff in (2, 3, 4, 6, 16, 101, 257):
            expected = []
            for n in range(2, cutoff + 1):
                factors = sp.factorint(n)
                if len(factors) == 1:
                    p, k = next(iter(factors.items()))
                    expected.append((int(p), int(k), n, Fraction(1, int(k) * n * n)))
            self.assertEqual(prime_power_terms(cutoff), tuple(expected))
        self.assertIn((2, 2, 4, Fraction(1, 32)), prime_power_terms(6))
        self.assertNotIn(6, [atom[2] for atom in prime_power_terms(6)])

    def test_prime_support_mutations_change_source(self):
        genuine = log_zeta2_partial(6)
        self.assertEqual(genuine, Fraction(1, 4) + Fraction(1, 9) +
                         Fraction(1, 32) + Fraction(1, 25))
        self.assertNotEqual(genuine, genuine + Fraction(1, 36))  # fake six
        self.assertNotEqual(genuine, genuine - Fraction(1, 32))  # omit p²
        self.assertNotEqual(genuine, genuine + Fraction(1, 32))  # wrong 1/k

    def test_rh_budget_exact_scope_and_large_precision(self):
        first = conditional_fourier_budget(101, 1, 1)
        self.assertEqual(first.psi_constant, Fraction(1, 24))
        self.assertLess(first.log_tail_error_upper, 1)
        self.assertIn("CONDITIONAL", first.status)
        for exponent in (5, 8, 12):
            x = 16**exponent
            budget = conditional_fourier_budget(x, exponent, 3)
            # This sufficient regime is far stronger than merely holding X fixed.
            self.assertLess(budget.mean_difference_upper, Fraction(1, 16**(exponent // 3)))
        self.assertEqual(conditional_fourier_budget(101, 100, 1).mean_difference_upper, 2)
        with self.assertRaises(FrozenInstanceError):
            first.status = "PROVED_RH"

    def test_thue_morse_independent_substitution_and_forbidden_words(self):
        word = "0"
        for _ in range(12):
            word = "".join("01" if letter == "0" else "10" for letter in word)
        self.assertEqual(tuple(map(int, word)), tuple(thue_morse_digit(k) for k in range(4096)))
        self.assertNotIn("000", word)
        self.assertNotIn("111", word)
        self.assertNotIn(2, [thue_morse_digit(k) for k in range(4096)])
        # Frequency balance of one-letter binary samples does not fix missing triples.
        self.assertEqual(word.count("0"), word.count("1"))

    def test_thue_morse_nested_exact_prefix_intervals(self):
        for base in (2, 3, 16):
            for length in (0, 1, 4, 17, 41):
                lo, hi = thue_morse_prefix_interval(base, length)
                next_lo, next_hi = thue_morse_prefix_interval(base, length + 19)
                self.assertLessEqual(lo, next_lo)
                self.assertLessEqual(next_hi, hi)
                self.assertEqual(hi - lo, Fraction(1, (base - 1) * base**length))

    def test_abc_residual_bound_and_gcd_independently(self):
        import sympy as sp
        checked = 0
        for p in range(1, 9):
            for q in range(1, 6):
                for a in range(1, 10):
                    if p * 16 == q * a:
                        continue
                    # A large finite K guarantees this single tested premise,
                    # not the universally quantified abc conjecture.
                    k = 100
                    result = residual_square_consequence(p, q, a, 2, 4, k)
                    self.assertEqual(result.common_gcd, gcd(p * 16, q * a))
                    self.assertEqual(gcd(result.u, result.v), 1)
                    self.assertEqual(result.radical_uv, int(sp.prod(sp.factorint(result.u * result.v))))
                    self.assertLessEqual(result.squared_residual_lower, result.residual**2)
                    self.assertLessEqual(result.squared_distance_lower, result.actual_squared_distance)
                    self.assertEqual(result.actual_squared_distance, Fraction((16 * p - q * a)**2, 256 * q * q))
                    checked += 1
        self.assertGreater(checked, 300)
        # Nontrivial reduction must survive: raw determinant and primitive residual differ.
        example = residual_square_consequence(22, 7, 314, 10, 2, 1)
        self.assertEqual((example.common_gcd, example.residual), (2, 1))

    def test_false_abc_premise_rejected(self):
        with self.assertRaisesRegex(ValueError, "premise is false"):
            residual_square_consequence(1, 1, 3, 2, 1, Fraction(1, 100))
        with self.assertRaisesRegex(ValueError, "zero residual"):
            residual_square_consequence(1, 2, 8, 2, 4, 1)

    def test_exact_input_guards(self):
        for bad in (True, 2.0, Fraction(2), float("nan"), float("inf")):
            with self.assertRaises(ValueError):
                prime_power_terms(bad)
        for bad in (False, 101.0, Fraction(101)):
            with self.assertRaises(ValueError):
                conditional_fourier_budget(bad, 2, 1)
        for bad in (True, 0, 1.0):
            with self.assertRaises(ValueError):
                conditional_fourier_budget(101, 2, bad)
        for bad in (True, 0.1, 0, -1):
            with self.assertRaises(ValueError):
                conditional_fourier_budget(101, 2, 1, bad)
        with self.assertRaises(ValueError):
            conditional_fourier_budget(101, 2, 1, 1000)
        with self.assertRaises(ValueError):
            prime_power_terms(10001)


if __name__ == "__main__":
    unittest.main()
