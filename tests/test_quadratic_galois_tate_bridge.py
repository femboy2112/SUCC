"""Quadratic Pisot/Galois/Tate carrier: exact-source arithmetic controls.

Research only. These tests do NOT prove RH, a global Tate functional equation,
or source-selected pi-normality. Companion:
research/2026-11-06/quadratic_galois_tate_bridge/RESEARCH.md.
No third-party dependencies; focus on exact arithmetic plus labeled finite
numerical controls.
"""
from __future__ import annotations

import cmath
from decimal import Decimal, localcontext
from math import acos, acosh, cosh, exp, isclose, log, pi, sqrt
import unittest


def multiply(x: tuple[int, int], y: tuple[int, int]) -> tuple[int, int]:
    """Coordinates (a,b) for a+b*phi, where phi^2=phi+1."""
    a, b = x
    c, d = y
    return a * c + b * d, a * d + b * c + b * d


def conjugate(x: tuple[int, int]) -> tuple[int, int]:
    """phi -> 1-phi."""
    a, b = x
    return a + b, -b


def power(x: tuple[int, int], n: int) -> tuple[int, int]:
    if n < 0:
        raise ValueError("test powering uses nonnegative exponents")
    result = (1, 0)
    while n:
        if n & 1:
            result = multiply(result, x)
        x = multiply(x, x)
        n >>= 1
    return result


def norm(x: tuple[int, int]) -> int:
    return multiply(x, conjugate(x))[0]


def trace(x: tuple[int, int]) -> int:
    return x[0] * 2 + x[1]


def chi5(n: int) -> int:
    if n % 5 == 0:
        return 0
    return 1 if n % 5 in (1, 4) else -1


def matmul(a: tuple[tuple[int, int], tuple[int, int]],
           b: tuple[tuple[int, int], tuple[int, int]]
           ) -> tuple[tuple[int, int], tuple[int, int]]:
    return tuple(
        tuple(sum(a[i][k] * b[k][j] for k in range(2)) for j in range(2))
        for i in range(2)
    )


class QuadraticGaloisTateBridgeTests(unittest.TestCase):
    def test_field_arithmetic_and_galois(self):
        phi = (0, 1)
        self.assertEqual(multiply(phi, phi), (1, 1))
        self.assertEqual(conjugate(phi), (1, -1))
        self.assertEqual(conjugate(conjugate(phi)), phi)
        self.assertEqual(norm(phi), -1)
        for n in range(64):
            x = power(phi, n)
            self.assertEqual(norm(x), (-1) ** n)
            self.assertEqual(multiply(x, conjugate(x)), ((-1) ** n, 0))

    def test_integral_order_discriminants(self):
        # Trace Gram determinants in bases (1,phi) and (1,sqrt(5)).
        disc_maximal = 2 * 3 - 1 * 1
        disc_nonmaximal = 2 * 10
        self.assertEqual((disc_maximal, disc_nonmaximal), (5, 20))
        self.assertEqual(disc_nonmaximal // disc_maximal, 2 ** 2)

    def test_lucas_trace_and_norm_parity(self):
        phi = (0, 1)
        previous, current = 2, 1
        for n in range(40):
            x = power(phi, n)
            self.assertEqual(trace(x), previous)
            self.assertEqual(norm(x), (-1) ** n)
            previous, current = current, previous + current

    def test_pisot_matrix_reflection(self):
        A = ((1, 1), (1, 0))
        C = ((-1, 0), (1, 1))
        Ainv = ((0, 1), (1, -1))
        neg_Ainv = tuple(tuple(-v for v in row) for row in Ainv)
        self.assertEqual(matmul(C, C), ((1, 0), (0, 1)))
        self.assertEqual(matmul(A, Ainv), ((1, 0), (0, 1)))
        self.assertEqual(matmul(matmul(C, A), C), neg_Ainv)
        self.assertEqual(
            matmul(matmul(C, matmul(A, A)), C),
            matmul(neg_Ainv, neg_Ainv),
        )

    def test_frobenius_matches_quadratic_character(self):
        # Also includes p=2 (where ordinary Legendre exponent is unavailable).
        primes = (2, 3, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53)
        for p in primes:
            with self.subTest(p=p):
                actual = tuple(v % p for v in power((0, 1), p))
                expected = (0, 1) if chi5(p) == 1 else (1, -1)
                self.assertEqual(actual, tuple(v % p for v in expected))
                self.assertEqual(chi5(p), 1 if p % 5 in (1, 4) else -1)
        self.assertEqual(chi5(5), 0)  # ramified, excluded

    def test_local_euler_artin_polynomials(self):
        # det(1-t*Frob) = (1-t)(1-chi_5(p)*t).
        for p in (2, 3, 7, 11, 13, 19, 29, 31):
            character = chi5(p)
            coeff = (1, -(1 + character), character)
            target = (1, -2, 1) if character == 1 else (1, 0, -1)
            self.assertEqual(coeff, target)
        self.assertEqual(chi5(5), 0)  # branch over p=5, not unramified factor

    def test_norm_parity_is_not_frobenius_character(self):
        # phi^p has norm -1 for both split and inert odd primes.
        self.assertEqual(norm(power((0, 1), 11)), -1)
        self.assertEqual(norm(power((0, 1), 13)), -1)
        self.assertEqual(chi5(11), 1)
        self.assertEqual(chi5(13), -1)
        self.assertEqual(abs(norm(power((0, 1), 7))), 1)
        self.assertEqual(abs(norm(power((0, 1), 8))), 1)

    def test_unit_mellin_twisted_reflection(self):
        # u=(-1)^e phi^n; sigma(u)=(-1)^(e+n) phi^(-n).
        R = log((1 + sqrt(5)) / 2)
        z = 0.19 + 0.37j
        def character(n: int, e: int, dz: int, w: complex) -> complex:
            return (-1) ** (dz * e) * cmath.exp(n * R * w)
        for n in range(-8, 9):
            for e in range(2):
                for d in range(2):
                    with self.subTest(n=n, e=e, d=d):
                        galois = character(-n, (e + n) % 2, d, z)
                        spectral = character(n, e, d, -z + 1j * pi * d / R)
                        self.assertLess(abs(galois - spectral), 2e-11)

    def test_cyclotomic_gauss_atom_and_fourier_eigenvector(self):
        w = cmath.exp(2j * pi / 5)
        chi = [chi5(j) for j in range(5)]
        tau = sum(chi[r] * w ** r for r in range(5))
        self.assertAlmostEqual(tau.real, sqrt(5), places=12)
        self.assertAlmostEqual(tau.imag, 0, places=12)
        self.assertLess(abs((1 + w + w ** -1) - (1 + sqrt(5)) / 2), 1e-12)
        for k in range(5):
            y = sum(chi[r] * w ** (r * k) for r in range(5)) / sqrt(5)
            self.assertLess(abs(y - chi[k]), 1e-12)

    def test_class_number_regulator_value_finite_only(self):
        # Numerical Dirichlet series for L(1,chi5): sanity check only.
        N = 20000
        truncated = sum(chi5(n) / n for n in range(1, N + 1))
        expected = 2 * log((1 + sqrt(5)) / 2) / sqrt(5)
        self.assertLess(abs(truncated - expected), 0.0002)

    def test_harmonic_lucas_residual_finite_only(self):
        # High precision finite control; Euler-Maclaurin supplies the proof.
        with localcontext() as ctx:
            ctx.prec = 75
            one, two = Decimal(1), Decimal(2)
            phi = (one + Decimal(5).sqrt()) / two
            gamma = Decimal(
                "0.5772156649015328606065120900824024310421593359399235988057672348848"
            )
            for n in (12, 13, 16, 17):
                L = trace(power((0, 1), n))
                H = sum((one / k for k in range(1, L + 1)), Decimal(0))
                residual = phi ** (2 * n) * (
                    H - n * phi.ln() - gamma - one / (2 * phi ** n)
                )
                target = Decimal((-1) ** n) - one / 12
                self.assertLess(abs(residual - target), Decimal("0.002"))

    def test_symmetric_positive_control_has_off_line_zero(self):
        # Repo PPF-10: positivity-on-line + reflection does NOT imply RH.
        delta = acosh(2) / 4
        s = 0.5 + delta + 1j * pi / 4
        G = lambda w: 2 + cmath.cosh(4 * (w - 0.5))
        self.assertGreater(delta, 0)
        self.assertLess(delta, 0.5)
        self.assertLess(abs(G(s)), 1e-12)
        self.assertLess(abs(G(s) - G(1 - s)), 1e-12)
        for t in (0, 0.3, 0.9, 3, 7):
            self.assertGreaterEqual(G(0.5 + 1j * t).real, 1 - 1e-12)


if __name__ == "__main__":
    unittest.main()
