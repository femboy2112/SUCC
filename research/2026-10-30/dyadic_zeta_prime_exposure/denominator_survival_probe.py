#!/usr/bin/env python3
"""Independent exact denominator survival probe through even index 100.

Classical authority: von Staudt--Clausen + von Staudt's second theorem for
B_(2k)/(2k); this test is a finite check, not a general proof.
"""
from fractions import Fraction
from math import comb, isqrt
import unittest


def bernoulli_even_up_to(limit: int):
    b = [Fraction(1)]
    for n in range(1, limit + 1):
        b.append(-sum(comb(n + 1, j) * b[j] for j in range(n)) / (n + 1))
    return b


def primes_to(limit: int):
    return [p for p in range(2, limit + 1)
            if all(p % j for j in range(2, isqrt(p) + 1))]


def valuation(n: int, p: int):
    if n == 0:
        raise ValueError("valuation of zero undefined")
    v = 0
    while n % p == 0:
        n //= p
        v += 1
    return v


def predicted_denominator(m: int):
    product = 1
    for p in primes_to(m + 1):
        if m % (p - 1) == 0:
            product *= p ** (1 + valuation(m, p))
    return product


def stirling_dyadic_numerator(m: int):
    row = [1]
    for n in range(1, m + 1):
        row = [0] + [j * (row[j] if j < len(row) else 0)
                     + row[j - 1] for j in range(1, n + 1)]
    from math import factorial
    return -sum((-1) ** j * factorial(j) * row[j] * 2 ** (m - j)
                for j in range(1, m + 1))


class ExactDenominatorSurvival(unittest.TestCase):
    def test_full_prime_denominator_product_to_100(self):
        b = bernoulli_even_up_to(100)
        for m in range(2, 101, 2):
            with self.subTest(m=m):
                self.assertEqual((-b[m] / m).denominator, predicted_denominator(m))

    def test_integer_pascal_numerator_cancellation_rule_to_100(self):
        for m in range(2, 101, 2):
            c = stirling_dyadic_numerator(m - 1)
            a = 2 ** m - 1
            for p in primes_to(m + 1):
                if p == 2 or a % p:
                    continue
                actual = valuation(c, p)
                target = valuation(a, p)
                if m % (p - 1) == 0:
                    self.assertEqual(actual, target - 1 - valuation(m, p))
                else:
                    self.assertGreaterEqual(actual, target)

    def test_first_appearance_exact(self):
        b = bernoulli_even_up_to(100)
        for p in primes_to(101):
            if p == 2:
                continue
            self.assertEqual((-b[p - 1] / (p - 1)).denominator % p, 0)
            for m in range(2, p - 1, 2):
                self.assertNotEqual((-b[m] / m).denominator % p, 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
