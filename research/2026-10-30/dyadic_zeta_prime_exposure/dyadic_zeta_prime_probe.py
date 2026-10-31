#!/usr/bin/env python3
"""Exact, stdlib-only probes for the SUCC dyadic/eta/zeta prime-exposure dossier.

Finite computations test stated exact identities; they cannot prove their
unbounded quantifiers. Full mathematical proofs are in README.md.
"""
from __future__ import annotations

from fractions import Fraction
from math import comb, factorial
import unittest


def stirling_second_row(n: int) -> list[int]:
    """S(n,j) by the independent integer partition recurrence."""
    if n < 0:
        raise ValueError("n must be nonnegative")
    row = [1]
    for i in range(1, n + 1):
        row = [0] + [j * (row[j] if j < len(row) else 0) + row[j - 1]
                     for j in range(1, i + 1)]
    return row


def eta_at_negative(m: int) -> Fraction:
    """Continued eta(-m), m>=1, by finite Stirling-rational calculus."""
    if m < 1:
        raise ValueError("m must be >=1")
    row = stirling_second_row(m)
    num = -sum((-1) ** j * factorial(j) * row[j] * 2 ** (m - j)
               for j in range(1, m + 1))
    return Fraction(num, 2 ** (m + 1))


def bernoulli_to(n: int) -> list[Fraction]:
    """B_0,...,B_n independently, by exp-generating-function recurrence."""
    if n < 0:
        raise ValueError("n must be nonnegative")
    result = [Fraction(1)]
    for i in range(1, n + 1):
        result.append(-sum(comb(i + 1, j) * result[j] for j in range(i))
                      / (i + 1))
    return result


def zeta_negative_from_eta(m: int) -> Fraction:
    return eta_at_negative(m) / (1 - 2 ** (m + 1))


def zeta_negative_from_bernoulli(m: int, bernoulli: list[Fraction]) -> Fraction:
    return -bernoulli[m + 1] / (m + 1)


def dyadic_partial(m: int, levels: int) -> Fraction:
    """Archimedean partial (finite, dyadic) for zeta(-m)."""
    if m < 1 or levels < 0:
        raise ValueError("m>=1 and levels>=0")
    d = m + 1
    return -eta_at_negative(m) * sum((Fraction(1, 2 ** (d * r))
                                      for r in range(1, levels + 1)),
                                     Fraction(0))


def p_valuation(q: Fraction, p: int) -> int:
    """v_p(q); accepts nonzero rationals and p>=2 (caller ensures prime)."""
    if not q or p < 2:
        raise ValueError("nonzero rational and p>=2 required")
    a, b, v = abs(q.numerator), q.denominator, 0
    while a % p == 0:
        a //= p
        v += 1
    while b % p == 0:
        b //= p
        v -= 1
    return v


def is_two_power(n: int) -> bool:
    return n > 0 and (n & (n - 1)) == 0


def primes_upto(limit: int) -> list[int]:
    return [n for n in range(2, limit + 1)
            if all(n % d for d in range(2, int(n ** 0.5) + 1))]


def invert_rational_matrix(matrix: list[list[Fraction]]) -> list[list[Fraction]]:
    n = len(matrix)
    aug = [[Fraction(x) for x in matrix[i]] +
           [Fraction(int(i == j)) for j in range(n)] for i in range(n)]
    for i in range(n):
        pivot = next(j for j in range(i, n) if aug[j][i])
        aug[i], aug[pivot] = aug[pivot], aug[i]
        d = aug[i][i]
        aug[i] = [v / d for v in aug[i]]
        for j in range(n):
            if i != j:
                coeff = aug[j][i]
                if coeff:
                    aug[j] = [a - coeff * b for a, b in zip(aug[j], aug[i])]
    return [row[n:] for row in aug]


def exact_cycle_pseudoinverse(n: int) -> list[list[Fraction]]:
    """Independent rational linear-algebra construction; N>=3."""
    if n < 3:
        raise ValueError("cycle requires N>=3")
    j = Fraction(1, n)
    shifted = [[Fraction(2 * int(i == h) - int(h == (i + 1) % n)
                           - int(h == (i - 1) % n)) + j
                for h in range(n)] for i in range(n)]
    return [[x - j for x in row] for row in invert_rational_matrix(shifted)]


def trace_powers(g: list[list[Fraction]], order: int) -> Fraction:
    if order not in (1, 2):
        raise ValueError("only orders 1 and 2 required by the probe")
    n = len(g)
    return sum((g[i][i] if order == 1 else
                sum(g[i][j] * g[j][i] for j in range(n)))
               for i in range(n))


class DyadicZetaPrimeTests(unittest.TestCase):
    def test_exact_special_values(self):
        expected = [Fraction(-1, 12), Fraction(1, 120),
                    Fraction(-1, 252), Fraction(1, 240),
                    Fraction(-1, 132), Fraction(691, 32760),
                    Fraction(-1, 12), Fraction(3617, 8160)]
        for k, want in enumerate(expected, 1):
            self.assertEqual(zeta_negative_from_eta(2 * k - 1), want)

    def test_independent_bernoulli_triangle(self):
        b = bernoulli_to(52)
        self.assertEqual(b[1], Fraction(-1, 2))
        self.assertEqual(b[2], Fraction(1, 6))
        self.assertEqual(b[4], Fraction(-1, 30))
        for m in range(1, 51):
            with self.subTest(m=m):
                self.assertEqual(zeta_negative_from_eta(m),
                                 zeta_negative_from_bernoulli(m, b))

    def test_integer_stirling_numerator_dyadic_eta(self):
        for m in range(1, 51):
            eta = eta_at_negative(m)
            self.assertTrue(is_two_power(eta.denominator))
            self.assertEqual(eta, (1 - 2 ** (m + 1)) * zeta_negative_from_eta(m))

    def test_odd_denominator_divides_power_of_two_minus_one(self):
        for m in range(1, 51, 2):
            den = zeta_negative_from_eta(m).denominator
            odd = den // (den & -den)
            self.assertEqual((2 ** (m + 1) - 1) % odd, 0)

    def test_prime_first_appearance(self):
        b = bernoulli_to(45)
        for p in primes_upto(43):
            if p == 2:
                continue
            for m in range(1, p - 2, 2):
                self.assertNotEqual(
                    zeta_negative_from_bernoulli(m, b).denominator % p, 0)
            first = zeta_negative_from_bernoulli(p - 2, b)
            self.assertEqual(p_valuation(first, p), -1)

    def test_exposure_is_not_survival(self):
        self.assertEqual((2 ** 8 - 1) % 17, 0)
        self.assertNotEqual(zeta_negative_from_eta(7).denominator % 17, 0)
        self.assertEqual((2 ** 10 - 1) % 31, 0)
        self.assertNotEqual(zeta_negative_from_eta(9).denominator % 31, 0)

    def test_finite_dyadic_cauchy_in_reals(self):
        for m in (1, 3, 5, 7, 9):
            zeta = zeta_negative_from_eta(m)
            for levels in range(0, 7):
                x = dyadic_partial(m, levels)
                self.assertTrue(is_two_power(x.denominator))
                self.assertEqual(zeta - x,
                                 zeta * Fraction(1, 2 ** ((m + 1) * levels)))

    def test_not_p_adically_cauchy(self):
        for m in (1, 3, 5):
            for p in (2, 3, 5, 7):
                valuations = [p_valuation(dyadic_partial(m, r + 1) -
                                          dyadic_partial(m, r), p)
                              for r in range(1, 6)]
                if p == 2:
                    self.assertTrue(all(valuations[i + 1] < valuations[i]
                                        for i in range(len(valuations) - 1)))
                else:
                    self.assertEqual(len(set(valuations)), 1)

    def test_finite_circle_green_traces(self):
        for n in range(3, 11):
            g = exact_cycle_pseudoinverse(n)
            self.assertEqual(trace_powers(g, 1), Fraction(n * n - 1, 12))
            self.assertEqual(trace_powers(g, 2),
                             Fraction(n ** 4 + 10 * n * n - 11, 720))
            self.assertEqual(sum(g[0]), 0)

    def test_cycle_dyadic_basel_bridge(self):
        # Exact finite Green-trace refinement for N=2^r, r>=2.
        for r in range(2, 10):
            n = 2 ** r
            old = Fraction(1 - Fraction(1, n * n), 12)
            new = Fraction(1 - Fraction(1, 4 * n * n), 12)
            self.assertEqual(new - old, Fraction(1, 16 * n * n))
        self.assertEqual(-sum((Fraction(1, 4 ** r * 16)
                              for r in range(8)), Fraction(0)),
                         Fraction(-1, 12) * (1 - Fraction(1, 4 ** 8)))

    def test_geometric_series_boundary_scope(self):
        for r in range(2, 20):
            partial_zero = sum(2 ** j for j in range(r + 1))
            self.assertEqual(partial_zero - 2 ** (r + 1), -1)
            self.assertEqual(partial_zero - 1 - 2 ** (r + 1), -2)


if __name__ == "__main__":
    unittest.main(verbosity=2)
