"""Dimension-uniform exact binomial corrections and entropy enclosures.

No floating point is used. Logarithm bounds are rational bounds on -log of
the exact volume ratio, not rational approximations promoted to equality.
See research/2026-10-21/VIII_SECTION_LATTICES_AND_SIMPLEX_LAWS.md.
"""
from dataclasses import dataclass
from fractions import Fraction
from math import comb, factorial


class SimplexAsymptoticError(ValueError):
    pass


def _nat(value, name, minimum=0):
    if type(value) is not int or value < minimum:
        raise SimplexAsymptoticError(f"{name} must be an integer >= {minimum}")
    return value


@dataclass(frozen=True)
class BinomialLogCorrection:
    population: int
    dimension: int
    depth: int
    count: int
    volume_ratio: Fraction
    correction: Fraction
    remainder_lower: Fraction
    remainder_upper: Fraction

    @property
    def negative_log_interval(self):
        return (self.correction + self.remainder_lower,
                self.correction + self.remainder_upper)


def binomial_log_correction(N, m, depth=1):
    """For 1<=m<=N, certify -log(m! binom(N,m)/N^m)=L_depth+R.

    R lies in the returned rational interval. The proof sums the positive
    log-series tail for j/N, j=0,...,m-1. The worst j is always strictly <N,
    including at m=N; the bound stays valid there but can be very loose.
    """
    _nat(N, "population", 1)
    _nat(m, "dimension", 1)
    _nat(depth, "depth", 1)
    if m > N:
        raise SimplexAsymptoticError("zero counts have no finite logarithm")
    correction = sum((Fraction(sum(j ** k for j in range(m)), k * N ** k)
                      for k in range(1, depth + 1)), Fraction(0))
    first_tail = Fraction(sum(j ** (depth + 1) for j in range(m)),
                          (depth + 1) * N ** (depth + 1))
    upper = first_tail / (1 - Fraction(m - 1, N))
    count = comb(N, m)
    ratio = Fraction(factorial(m) * count, N ** m)
    return BinomialLogCorrection(N, m, depth, count, ratio, correction, first_tail, upper)


@dataclass(frozen=True)
class EntropyEnclosure:
    count: int
    lower: Fraction
    upper: Fraction


def binomial_entropy_enclosure(N, m):
    """E/(N+1)<=binom(N,m)<=E, E=N^N/(m^m (N-m)^(N-m)).

    Endpoint values use 0^0=1. If m>N the count and both bounds are zero.
    This is an additive log error <=log(N+1), not a relative-error asymptotic.
    """
    _nat(N, "population")
    _nat(m, "dimension")
    if m > N:
        return EntropyEnclosure(0, Fraction(0), Fraction(0))
    entropy_exp = Fraction(N ** N, m ** m * (N - m) ** (N - m))
    count = comb(N, m)
    return EntropyEnclosure(count, entropy_exp / (N + 1), entropy_exp)


def residue_population(modulus, cutoff, residues):
    """Convert one canonical residue vector to its exact stars-and-bars N.

    The count is binom(N,m) when N>=m and zero otherwise. The residue shift
    and floor are retained. Empty vectors and non-exact cutoffs are rejected.
    """
    W = _nat(modulus, "modulus", 1)
    rs = tuple(residues)
    if not rs:
        raise SimplexAsymptoticError("positive dimension required")
    if any(type(r) is not int or not 0 <= r < W for r in rs):
        raise SimplexAsymptoticError("canonical integer residues required")
    if type(cutoff) not in (int, Fraction) or cutoff < 0:
        raise SimplexAsymptoticError("nonnegative exact rational cutoff required")
    positive_sum = sum(r if r else W for r in rs)
    n = (Fraction(cutoff) - positive_sum) // W
    return n + len(rs)


def residue_log_correction(modulus, cutoff, residues, depth=1):
    """One occupied residue's exact correction; None for an empty stratum."""
    rs = tuple(residues)
    _nat(depth, "depth", 1)
    N = residue_population(modulus, cutoff, rs)
    return None if N < len(rs) else binomial_log_correction(N, len(rs), depth)
