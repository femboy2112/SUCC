"""Exact source-moment seams for the original zero-seeded BBP carrier.

Paper authority: research/2026-11-26/principia_intermedia_continuation/BBP_MOMENT_SEAMS.md.
Finite computations implement classical orthogonal-polynomial constructions.
They do not prove a temporal Weyl estimate, R0, or pi normality. The positive
measure is an observer representation of the signed source, not randomness.
The moments depend on the forcing, not the homogeneous seed; canonical U0=0
is retained separately and is not authenticated by these moment tests.
"""

from fractions import Fraction

from .duck_bbp import forcing


def _nat(value, name, minimum=0):
    if type(value) is not int or value < minimum:
        raise ValueError(f"{name} must be an integer >= {minimum}")
    return value


def _rat(value):
    if type(value) not in (int, Fraction):
        raise TypeError("exact int or Fraction required")
    return Fraction(value)


def moment(k):
    """Integral of u**k against the genuine BBP Mellin measure, k >= 0."""
    return forcing(_nat(k, "moment order") + 1)


def gram(size):
    """The size-by-size rational moment Gram matrix; empty size is legal."""
    _nat(size, "size")
    return tuple(tuple(moment(i + j) for j in range(size)) for i in range(size))


def _solve(matrix, rhs):
    """Rational Gaussian elimination with explicit singularity rejection."""
    n = len(matrix)
    if len(rhs) != n or any(len(row) != n for row in matrix):
        raise ValueError("square system required")
    a = [[_rat(x) for x in row] + [_rat(y)] for row, y in zip(matrix, rhs)]
    for j in range(n):
        pivot = next((i for i in range(j, n) if a[i][j]), None)
        if pivot is None:
            raise ValueError("singular moment system")
        a[j], a[pivot] = a[pivot], a[j]
        q = a[j][j]
        a[j] = [x / q for x in a[j]]
        for i in range(n):
            if i != j:
                q = a[i][j]
                a[i] = [x - q * y for x, y in zip(a[i], a[j])]
    return tuple(row[-1] for row in a)


def orthogonal_polynomial(degree):
    """Monic P_degree, coefficients in ascending order, all exact rationals."""
    n = _nat(degree, "degree")
    return _solve(gram(n), tuple(-moment(n + j) for j in range(n))) + (Fraction(1),)


def evaluate(coefficients, u):
    u = _rat(u)
    value = Fraction(0)
    for c in reversed(tuple(coefficients)):
        value = value * u + _rat(c)
    return value


def moment_pair(coefficients, order=0):
    """Integral u**order P(u) dmu(u)."""
    _nat(order, "order")
    return sum((_rat(c) * moment(order + i) for i, c in enumerate(coefficients)), Fraction())


def inner(left, right):
    """Exact L2(mu) bilinear pairing including every signed cross term."""
    left = tuple(_rat(x) for x in left)
    right = tuple(_rat(x) for x in right)
    return sum((a * b * moment(i + j)
                for i, a in enumerate(left) for j, b in enumerate(right)), Fraction())


def resolvent_hasse_jet(coefficients, order):
    """Coefficient of z**order in integral P(u)/(16-u*z) dmu(u)."""
    _nat(order, "order")
    return moment_pair(coefficients, order) / 16 ** (order + 1)


def moment_ratio(k):
    """Unique seam of u**k*(u-t): t=m_(k+1)/m_k, strictly increasing in k."""
    _nat(k, "order")
    return moment(k + 1) / moment(k)


def inverse_gram(size):
    n = _nat(size, "size", 1)
    matrix = gram(n)
    columns = tuple(_solve(matrix, tuple(int(i == j) for i in range(n)))
                    for j in range(n))
    return tuple(tuple(columns[j][i] for j in range(n)) for i in range(n))


def residual_capacity(degree, denominator=1, multiple=1):
    """Rational lower bound for some moment of a nonzero constrained field.

    If P has degree <= degree, denominator*coeff(P) belongs to multiple*Z,
    and P != 0, then max_{0<=j<=degree}|integral u**j P dmu| is at least
    the returned multiple/(denominator*||H^{-1}||_infinity).
    The integer lattice, nonzeroness and coefficient denominator are premises.
    """
    _nat(degree, "degree")
    _nat(denominator, "denominator", 1)
    _nat(multiple, "multiple", 1)
    matrix = inverse_gram(degree + 1)
    inverse_norm = max(sum((abs(x) for x in row), Fraction()) for row in matrix)
    return Fraction(multiple, denominator) / inverse_norm


def verify_capacity(coefficients, denominator=1, multiple=1):
    """Return bound and measured residual; reject a false lattice/nonzero premise."""
    coefficients = tuple(_rat(x) for x in coefficients)
    _nat(denominator, "denominator", 1)
    _nat(multiple, "multiple", 1)
    if not coefficients or not any(coefficients):
        raise ValueError("nonzero polynomial required")
    if any((denominator * x / multiple).denominator != 1 for x in coefficients):
        raise ValueError("declared coefficient lattice is false")
    degree = len(coefficients) - 1
    lower = residual_capacity(degree, denominator, multiple)
    observed = max(abs(moment_pair(coefficients, j)) for j in range(degree + 1))
    if observed < lower:
        raise ArithmeticError("source-moment capacity contradiction")
    return lower, observed
