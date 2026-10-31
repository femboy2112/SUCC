"""Exact all-order spectral shadow with a rational completed boundary.

This deliberately CHANGES the original BBP forcing after a declared prefix.
It is a hostile control, never an implementation of pi's source.
"""
from __future__ import annotations

from fractions import Fraction as F


def source(n: int, u=F(0)) -> F:
    if n < 1:
        raise ValueError("source time must be positive")
    a = 8 * n - 7 + F(u)
    if a <= 0:
        raise ValueError("this positive-source API requires 8*n-7+u > 0")
    return 4 / a - 2 / (a + 3) - 1 / (a + 4) - 1 / (a + 5)


def source_derivative(n: int, order: int, u=F(0)) -> F:
    from math import factorial
    if n < 1 or order < 0:
        raise ValueError("invalid time or derivative order")
    a = 8 * n - 7 + F(u)
    if a <= 0:
        raise ValueError("this positive-source API requires 8*n-7+u > 0")
    return (-1) ** order * factorial(order) * sum(
        (F(c) / (a + d) ** (order + 1)
         for c, d in [(4, 0), (-2, 3), (-1, 4), (-1, 5)]), F(0))


def validate_parameters(prefix: int, depth: int):
    if not isinstance(prefix, int) or not isinstance(depth, int) or prefix < 0 or depth < 1:
        raise ValueError("prefix must be >= 0 and depth >= 1")


def tail_length(n: int, prefix: int, depth: int) -> int:
    validate_parameters(prefix, depth)
    if n < 0:
        raise ValueError("time must be nonnegative")
    return prefix + depth - n if n <= prefix else depth + n - prefix


def truncated_tail(n: int, length: int, u=F(0)) -> F:
    if n < 0 or length < 0:
        raise ValueError("negative time or tail length")
    return sum((source(n + j, u) / 16 ** j for j in range(1, length + 1)), F(0))


def boundary(prefix: int, depth: int, u=F(0)) -> F:
    validate_parameters(prefix, depth)
    return truncated_tail(0, prefix + depth, u)


def shadow_source(n: int, prefix: int, depth: int, u=F(0)) -> F:
    validate_parameters(prefix, depth)
    value = source(n, u)
    if n <= prefix:
        return value
    ell = depth + n - prefix - 1
    return value - source(n + ell, u) / 16 ** ell - source(n + ell + 1, u) / 16 ** (ell + 1)


def shadow_source_derivative(n: int, order: int, prefix: int, depth: int, u=F(0)) -> F:
    validate_parameters(prefix, depth)
    value = source_derivative(n, order, u)
    if n <= prefix:
        return value
    ell = depth + n - prefix - 1
    return (value - source_derivative(n + ell, order, u) / 16 ** ell
            - source_derivative(n + ell + 1, order, u) / 16 ** (ell + 1))


def orbit(n: int, prefix: int, depth: int, u=F(0)) -> F:
    validate_parameters(prefix, depth)
    if n < 0:
        raise ValueError("negative time")
    value = F(0)
    for time in range(1, n + 1):
        value = 16 * value + shadow_source(time, prefix, depth, u)
    return value


def orbit_from_boundary(n: int, prefix: int, depth: int, u=F(0)) -> F:
    return 16 ** n * boundary(prefix, depth, u) - truncated_tail(n, tail_length(n, prefix, depth), u)


def relative_error_bound(prefix: int, depth: int) -> F:
    validate_parameters(prefix, depth)
    return F(17, 16 ** (depth + 1))


def dirichlet_defect_partial(s: int, cutoff: int, prefix: int, depth: int, u=F(0)) -> F:
    """Exact at integer s; the entire-function assertion has a paper proof."""
    return sum(((shadow_source(n, prefix, depth, u) - source(n, u)) * F(n) ** (-s)
                for n in range(1, cutoff + 1)), F(0))


def turns(value: F) -> F:
    return value % 1
