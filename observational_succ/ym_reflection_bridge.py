"""Exact finite Wilson and reflection-positivity research instruments.

This module reproduces a one-plaquette SU(2) Wilson *ingredient*, not the
four-dimensional continuum construction.  Universal statements are proved in
research/2026-11-13/yang_mills_succ/WILSON_REFLECTION_SLICE.md.  Fractions here
provide finite witnesses and mutation controls; they do not certify a QFT.
"""

from dataclasses import dataclass
from fractions import Fraction
from math import comb, factorial
from typing import Callable, Sequence


Rational = int | Fraction
Polynomial = tuple[Fraction, ...]
Matrix = tuple[tuple[Fraction, ...], ...]


def _q(value: Rational) -> Fraction:
    """Require exact input instead of silently interpreting a float as exact."""
    if not isinstance(value, (int, Fraction)):
        raise TypeError("an int or Fraction is required")
    return Fraction(value)


def _degree(n: int) -> int:
    if not isinstance(n, int) or n < 0:
        raise ValueError("degree must be a nonnegative integer")
    return n


def haar_moment(n: int) -> Fraction:
    """Integral of x**n for x=Tr(U)/2 and normalized Haar U in SU(2)."""
    _degree(n)
    if n % 2:
        return Fraction(0)
    k = n // 2
    return Fraction(comb(2 * k, k), (k + 1) * 4**k)


def haar_moment_recurrence(n: int) -> Fraction:
    """Independent arithmetic route: integration-by-parts moment recurrence."""
    _degree(n)
    if n % 2:
        return Fraction(0)
    result = Fraction(1)
    for j in range(0, n, 2):
        result *= Fraction(j + 1, j + 4)
    return result


def polynomial_product(a: Sequence[Rational], b: Sequence[Rational]) -> Polynomial:
    if not a or not b:
        return ()
    result = [Fraction(0) for _ in range(len(a) + len(b) - 1)]
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            result[i + j] += _q(x) * _q(y)
    return tuple(result)


def haar_polynomial(coefficients: Sequence[Rational]) -> Fraction:
    return sum((_q(a) * haar_moment(n) for n, a in enumerate(coefficients)), Fraction(0))


def taylor_coefficients(beta: Rational, order: int) -> Polynomial:
    """Coefficients of sum_(j=0)^order (beta*x)**j/j!; may be signed."""
    beta = _q(beta)
    _degree(order)
    return tuple(beta**j / factorial(j) for j in range(order + 1))


def polynomial_sup_bound(coefficients: Sequence[Rational]) -> Fraction:
    """Triangle-inequality bound for |f| on [-1,1]."""
    return sum((abs(_q(c)) for c in coefficients), Fraction(0))


@dataclass(frozen=True)
class TaylorWilsonState:
    """Positive, normalized, even-Taylor approximant of the SU(2) Wilson law.

    The original one-plaquette density is exp[-beta*(1-x)].  Its constant
    exp(-beta) cancels from normalized expectations, leaving exp(beta*x).
    Real rational polynomial observations are evaluated exactly.
    """

    beta: Rational
    order: int

    def __post_init__(self) -> None:
        object.__setattr__(self, "beta", _q(self.beta))
        _degree(self.order)
        if self.order % 2:
            raise ValueError("a positive approximant requires even Taylor order")

    @property
    def weight(self) -> Polynomial:
        return taylor_coefficients(self.beta, self.order)

    @property
    def partition(self) -> Fraction:
        return haar_polynomial(self.weight)

    def expectation(self, coefficients: Sequence[Rational]) -> Fraction:
        return haar_polynomial(polynomial_product(coefficients, self.weight)) / self.partition

    def gram(self, polynomials: Sequence[Sequence[Rational]]) -> Matrix:
        return tuple(
            tuple(self.expectation(polynomial_product(a, b)) for b in polynomials)
            for a in polynomials
        )

    def error_bound(self, sup_bound: Rational) -> Fraction:
        """Bound |exact exponential expectation - this expectation|.

        The caller supplies M >= sup |f|.  The bound is
        2 M 3**(2 ceil |beta|) |beta|**(order+1)/(order+1)!.
        It can be loose or exceed 2M; no useful precision is then claimed.
        """
        sup_bound = _q(sup_bound)
        if sup_bound < 0:
            raise ValueError("supremum bound must be nonnegative")
        b = abs(self.beta)
        ceiling = (b.numerator + b.denominator - 1) // b.denominator
        return (
            2 * sup_bound * 3 ** (2 * ceiling) * b ** (self.order + 1)
            / factorial(self.order + 1)
        )


def quadratic_form(matrix: Sequence[Sequence[Rational]], c: Sequence[Rational]) -> Fraction:
    if len(matrix) != len(c) or any(len(row) != len(c) for row in matrix):
        raise ValueError("matrix and coefficient dimensions must agree")
    return sum(
        (_q(c[i]) * _q(matrix[i][j]) * _q(c[j]) for i in range(len(c)) for j in range(len(c))),
        Fraction(0),
    )


def is_psd_exact(matrix: Sequence[Sequence[Rational]]) -> bool:
    """Exact symmetric PSD test by Schur complements, including zero pivots."""
    n = len(matrix)
    if any(len(row) != n for row in matrix):
        raise ValueError("matrix must be square")
    a = [[_q(x) for x in row] for row in matrix]
    if any(a[i][j] != a[j][i] for i in range(n) for j in range(n)):
        return False
    for k in range(n):
        pivot = a[k][k]
        if pivot < 0:
            return False
        if pivot == 0:
            if any(a[k][j] for j in range(k + 1, n)):
                return False
            continue
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                a[i][j] -= a[i][k] * a[k][j] / pivot
    return True


def quarter_turn_cos(n: int) -> Fraction:
    """Exact cos(pi*n/2) on integer times, including negative differences."""
    if not isinstance(n, int):
        raise TypeError("integer time required")
    return Fraction((1, 0, -1, 0)[n % 4])


def toeplitz_matrix(kernel: Callable[[int], Fraction], times: Sequence[int]) -> Matrix:
    return tuple(tuple(kernel(s - t) for t in times) for s in times)


def reflection_matrix(kernel: Callable[[int], Fraction], times: Sequence[int]) -> Matrix:
    if any(not isinstance(t, int) or t < 0 for t in times):
        raise ValueError("reflection times must be nonnegative integers")
    return tuple(tuple(kernel(s + t) for t in times) for s in times)


def hilbert_correlation(n: int) -> Fraction:
    _degree(n)
    return Fraction(1, n + 1)


def finite_hilbert_correlation(size: int, n: int) -> Fraction:
    """Finite gapped spectral approximant of the gapless Hilbert correlation."""
    if not isinstance(size, int) or size < 1:
        raise ValueError("size must be a positive integer")
    _degree(n)
    return sum((Fraction(j, size + 1) ** n for j in range(1, size + 1)), Fraction(0)) / size


def lattice_transfer_eigenvalue(spacing: Rational) -> Fraction:
    spacing = _q(spacing)
    if spacing <= 0:
        raise ValueError("spacing must be positive")
    return 1 / (1 + spacing**2)


def lattice_physical_mass_bounds(spacing: Rational) -> tuple[Fraction, Fraction]:
    """Exact bounds for -log(q_a)/a, not a numerical logarithm evaluation."""
    spacing = _q(spacing)
    if spacing <= 0:
        raise ValueError("spacing must be positive")
    return spacing / (1 + spacing**2), spacing


def physical_time_correlation(spacing: Rational, time: Rational) -> Fraction:
    spacing, time = _q(spacing), _q(time)
    q = lattice_transfer_eigenvalue(spacing)
    if time < 0:
        raise ValueError("time must be nonnegative")
    return q ** (time // spacing)


def physical_defect_bound(spacing: Rational, time: Rational) -> Fraction:
    """Bound 0 <= 1-q_a**floor(time/a) <= min(1,time*a)."""
    spacing, time = _q(spacing), _q(time)
    lattice_transfer_eigenvalue(spacing)
    if time < 0:
        raise ValueError("time must be nonnegative")
    return min(Fraction(1), spacing * time)
