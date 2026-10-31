#!/usr/bin/env python3
"""Finite, exact regression checks for the SUCC summation-snapshot dossier.

These are calibration tests; claims quantified over infinite families require
mathematical proofs stated in the accompanying dossier.
"""
from __future__ import annotations
from fractions import Fraction
from math import comb, factorial, exp
import unittest


def bernoulli(n: int) -> list[Fraction]:
    """Compute Bernoulli numbers in the B1=-1/2 convention."""
    b = [Fraction(1)]
    for m in range(1, n + 1):
        b.append(-sum(comb(m + 1, j) * b[j] for j in range(m)) / (m + 1))
    return b


def from_germ(m: int, b: list[Fraction]) -> Fraction:
    """(-1)^m m! [t^m](1/(e^t-1))."""
    return (-1) ** m * b[m + 1] / (m + 1)


def partial_sum(a: tuple[int, ...], n: int) -> int:
    return sum(a[:n + 1])


def rotafiniteness(a: tuple[int, ...], b: tuple[int, ...], n: int):
    """Rota-Baxter weight -1 with inclusive partial sums."""
    lhs = partial_sum(a, n) * partial_sum(b, n)
    rhs = sum(a[i] * partial_sum(b, i) + b[i] * partial_sum(a, i)
              - a[i] * b[i] for i in range(n + 1))
    return lhs, rhs


def borel_geometric_square_coefficient(n: int) -> Fraction:
    return Fraction(n + 1, factorial(n))


def square_borel_geometric_coefficient(n: int) -> Fraction:
    return Fraction(2 ** n, factorial(n))


class SummationSnapshotRegression(unittest.TestCase):
    def test_complete_germ_negative_values(self):
        b = bernoulli(33)
        values = {0: Fraction(-1, 2), 1: Fraction(-1, 12),
                  2: Fraction(0), 3: Fraction(1, 120),
                  4: Fraction(0), 5: Fraction(-1, 252),
                  7: Fraction(1, 240), 9: Fraction(-1, 132),
                  11: Fraction(691, 32760)}
        for m, expected in values.items():
            with self.subTest(m=m):
                self.assertEqual(from_germ(m, b), expected)

    def test_laurent_coefficient_bernoulli_generator(self):
        b = bernoulli(30)
        # K(t) = sum_(j>=0) B_j t^(j-1) / j! is a Laurent germ.
        # Nontrivial recurrence: (exp(t)-1)K(t)=1 coefficientwise.
        for degree in range(1, 21):
            coeff = sum(Fraction(1, factorial(j)) *
                        Fraction(b[degree + 1 - j], factorial(degree + 1 - j))
                        for j in range(1, degree + 2))
            self.assertEqual(coeff, 0)

    def test_finite_cutoff_derivative_does_not_commute(self):
        for n in range(1, 101):
            coefficient = -sum(range(1, n + 1))
            self.assertEqual(coefficient, -n * (n + 1) // 2)
            self.assertNotEqual(Fraction(coefficient), Fraction(1, 12))
        # Completed kernel has [t] K(t)=+1/12 instead.
        self.assertEqual(bernoulli(2)[2] / 2, Fraction(1, 12))

    def test_triangle_stuffle_finite(self):
        for N in range(1, 13):
            a = {n: Fraction(1, n ** 2) for n in range(1, N + 1)}
            b = {n: Fraction(1, n ** 3) for n in range(1, N + 1)}
            upper = sum((a[n] * b[m] for n in a for m in b if n > m), Fraction(0))
            lower = sum((a[n] * b[m] for n in a for m in b if n < m), Fraction(0))
            diag = sum((a[n] * b[n] for n in a), Fraction(0))
            self.assertEqual(sum(a.values()) * sum(b.values()), upper + lower + diag)

    def test_rota_baxter_inclusive_weight_minus_one(self):
        a = (2, -1, 3, 0, 4, -7, 1)
        b = (1, 5, -2, 3, 0, 6, -1)
        for n in range(len(a)):
            lhs, rhs = rotafiniteness(a, b, n)
            self.assertEqual(lhs, rhs)

    def test_dirichlet_product_multiplicative_index(self):
        for N in range(1, 12):
            A = sum((Fraction(1, n * n) for n in range(1, N + 1)), Fraction(0))
            C = {}
            for a in range(1, N + 1):
                for b in range(1, N + 1):
                    C[a * b] = C.get(a * b, 0) + 1
            rhs = sum((Fraction(count, k * k) for k, count in C.items()), Fraction(0))
            self.assertEqual(A * A, rhs)

    def test_borel_is_linear_not_multiplicative(self):
        for n in range(2, 13):
            self.assertNotEqual(borel_geometric_square_coefficient(n),
                                square_borel_geometric_coefficient(n))
        self.assertEqual(borel_geometric_square_coefficient(2), Fraction(3, 2))
        self.assertEqual(square_borel_geometric_coefficient(2), Fraction(2))

    def test_kernel_inclusion_obstruction(self):
        a, b = (Fraction(1), Fraction(0)), (Fraction(0), Fraction(1))
        q0 = lambda v: v[0] + v[1]
        q2 = lambda v: v[0] + v[1] / 4
        self.assertEqual(q0(a), q0(b))
        self.assertNotEqual(q2(a), q2(b))

    def test_geometric_continuation_not_ordinary_sum(self):
        for q in (Fraction(1, 2), Fraction(3, 5)):
            for N in range(1, 16):
                self.assertEqual(sum((q ** n for n in range(N)), Fraction(0)),
                                 (1 - q ** N) / (1 - q))
        self.assertEqual(Fraction(1, 1 - 2), Fraction(-1))
        self.assertGreater(sum(2 ** n for n in range(20)), 0)

    def test_flat_positive_control_finite_samples(self):
        def h(t):
            return (t - 1) ** 2 * exp(-t - 1 / t)
        self.assertEqual(h(1), 0)
        for t in (0.05, 0.25, 0.5, 1.5, 3.0):
            self.assertGreater(h(t), 0)
        # This is a sampled sanity check, not proof of all-order flatness.


if __name__ == '__main__':
    unittest.main(verbosity=2)
