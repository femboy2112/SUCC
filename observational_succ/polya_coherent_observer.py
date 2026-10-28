"""Source-marked coherent lifts of the authentic nearest-neighbor Oily compiler.

This is finite Hilbert-space algebra, not a physical quantum implementation.
The exact integer Gram identities certify a two-Kraus Pólya channel.  Square
roots are kept out of this module: squared coefficients and quadratic forms
are rational, and the separate SymPy oracle checks the actual amplitudes.

The channel preserves a specified square-root source vector.  It does not
create or identify the original signed zero-seeded BBP phase history.
"""
from __future__ import annotations

from fractions import Fraction
from math import comb
from typing import Sequence

from observational_succ.oily_prime_growth_compiler import (
    conditional_split,
    polya_birth,
    unique_local_birth_probability,
)


def _dimension(m: int) -> int:
    if type(m) is not int or m < 1:
        raise ValueError("positive integer source-fiber dimension required")
    return m


def _rational(value) -> Fraction:
    if type(value) not in (int, Fraction):
        raise TypeError("integer or Fraction input required")
    return Fraction(value)


def polya_coherent_numerator(m: int) -> tuple[tuple[int, ...], ...]:
    """B=sqrt(m(m+1))*K0, for source dimension m and target m+1.

    K0=sqrt((m+1)/m)*P, where P is the original stochastic Pólya matrix.
    This rescaling is a Kraus operator only with its explicit K1 complement.
    """
    _dimension(m)
    out = [[0] * m for _ in range(m + 1)]
    for k in range(m):
        out[k][k] = m - k
        out[k + 1][k] = k + 1
    return tuple(map(tuple, out))


def polya_laplacian(m: int) -> tuple[tuple[int, ...], ...]:
    """L with edge weights l(m-l), l=1,...,m-1; K1* K1=L/(m(m+1))."""
    _dimension(m)
    out = [[0] * m for _ in range(m)]
    for ell in range(1, m):
        w = ell * (m - ell)
        out[ell - 1][ell - 1] += w
        out[ell][ell] += w
        out[ell - 1][ell] -= w
        out[ell][ell - 1] -= w
    return tuple(map(tuple, out))


def leakage_spectrum(m: int) -> tuple[Fraction, ...]:
    """Exact Hahn spectrum of K1* K1; proof is in the linked dossier."""
    _dimension(m)
    return tuple(Fraction(r * (r + 1), m * (m + 1)) for r in range(m))


def hahn_eigenvector(m: int, degree: int) -> tuple[Fraction, ...]:
    """Q_degree(k;0,0,m-1), an exact independent spectral witness.

    A finite binomial representation, with first coordinate 1.  No floating
    eigensolver or tabulated zero is used.
    """
    _dimension(m)
    if type(degree) is not int or not 0 <= degree < m:
        raise ValueError("degree must be an integer in [0,m)")
    return tuple(
        sum(
            (Fraction((-1) ** t * comb(degree, t) * comb(degree + t, t)
                      * comb(k, t), comb(m - 1, t))
             for t in range(min(degree, k) + 1)),
            Fraction(0),
        )
        for k in range(m)
    )


def leakage_quadratic(vector: Sequence[Fraction | int]) -> Fraction:
    """||K1 vector||^2 for an arbitrary real rational (not necessarily unit) input."""
    v = tuple(map(_rational, vector))
    m = _dimension(len(v))
    return sum((Fraction(ell * (m - ell), m * (m + 1))
                * (v[ell] - v[ell - 1]) ** 2
                for ell in range(1, m)), Fraction(0))


def accepted_quadratic(vector: Sequence[Fraction | int]) -> Fraction:
    """||K0 vector||^2, computed independently by actual row application."""
    v = tuple(map(_rational, vector))
    m = _dimension(len(v))
    rows = polya_coherent_numerator(m)
    return sum((sum((Fraction(a) * z for a, z in zip(row, v)), Fraction(0)) ** 2
                for row in rows), Fraction(0)) / (m * (m + 1))


def distance_from_uniform_ray_squared(vector: Sequence[Fraction | int]) -> Fraction:
    """Squared distance to the span of the marked uniform vector, not to a unit vector."""
    v = tuple(map(_rational, vector))
    m = _dimension(len(v))
    mean = sum(v, Fraction(0)) / m
    return sum(((z - mean) ** 2 for z in v), Fraction(0))


def minimal_environment_dimension(m: int) -> int:
    """Sharp dimension for the fully positive Pólya two-neighbor isometric lift."""
    return 1 if _dimension(m) == 1 else 2


def forbidden_scalar_overlap_squared(m: int, k: int) -> Fraction:
    """Phase-independent squared column overlap without an auxiliary system.

    Adjacent columns k,k+1 share exactly one output row.  A nonzero value
    forbids scalar-amplitude isometry, regardless of chosen edge phases.
    """
    _dimension(m)
    if type(k) is not int or not 0 <= k < m - 1:
        raise ValueError("adjacent source columns required")
    return polya_birth(m - 1, k) * (1 - polya_birth(m - 1, k + 1))


def nearest_neighbor_source_flux(
    source: Sequence[Fraction | int], birth: Sequence[Fraction | int]
) -> tuple[tuple[Fraction, Fraction, Fraction], ...]:
    """Return (stay flux, birth flux, target mass) at each output row.

    Strictly positive source probabilities and strictly interior births are
    the nondegenerate theorem domain.  Each row has at most two parents;
    distinct source columns overlap in at most one target row.
    """
    mu = tuple(map(_rational, source))
    p = tuple(map(_rational, birth))
    m = _dimension(len(mu))
    if len(p) != m or sum(mu, Fraction(0)) != 1 or any(z <= 0 for z in mu):
        raise ValueError("strictly positive normalized source and one birth rate per state")
    if any(not 0 < z < 1 for z in p):
        raise ValueError("strictly interior birth probabilities required")
    rows = []
    for ell in range(m + 1):
        x = mu[ell] * (1 - p[ell]) if ell < m else Fraction(0)
        y = mu[ell - 1] * p[ell - 1] if ell > 0 else Fraction(0)
        rows.append((x, y, x + y))
    return tuple(rows)


def oily_source_flux(x: Fraction | int, grade: int):
    """Source-imported full-x Oily flux; x=0 is outside the reachable-birth theorem."""
    if type(grade) is not int or grade < 0:
        raise ValueError("nonnegative integer grade required")
    mu = tuple(conditional_split(x, grade, k) for k in range(grade + 1))
    p = tuple(unique_local_birth_probability(x, grade, k) for k in range(grade + 1))
    return nearest_neighbor_source_flux(mu, p)


def compositions(grade: int, channels: int) -> tuple[tuple[int, ...], ...]:
    """Weak compositions used only as origin-labelled prime-power fibers."""
    if type(grade) is not int or grade < 0:
        raise ValueError("nonnegative integer grade required")
    if type(channels) is not int or channels < 2:
        raise ValueError("at least two channels required")

    def recur(total, count):
        if count == 1:
            return ((total,),)
        return tuple((first,) + rest for first in range(total + 1)
                     for rest in recur(total - first, count - 1))

    return recur(grade, channels)


def higher_rank_polya_kernel(grade: int, channels: int):
    """Uniform Dirichlet-multinomial Pólya birth on c-channel compositions.

    Returns (source_labels, target_labels, column-stochastic rational matrix).
    This is a higher-rank marked-prior theorem, not a replacement BBP source.
    """
    source, target = compositions(grade, channels), compositions(grade + 1, channels)
    index = {label: i for i, label in enumerate(target)}
    matrix = [[Fraction(0)] * len(source) for _ in target]
    for k, state in enumerate(source):
        for channel in range(channels):
            nxt = list(state)
            nxt[channel] += 1
            matrix[index[tuple(nxt)]][k] = Fraction(state[channel] + 1, grade + channels)
    return source, target, tuple(map(tuple, matrix))


def higher_rank_minimal_environment(grade: int, channels: int) -> int:
    """Sharp dimension min(channels, grade+1) under the theorem's locality/source rules."""
    if type(grade) is not int or grade < 0 or type(channels) is not int or channels < 2:
        raise ValueError("nonnegative grade and at least two channels required")
    return min(channels, grade + 1)
