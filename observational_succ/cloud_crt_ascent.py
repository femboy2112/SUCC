"""Exact residue counting and explicit primitive transfer, independent cloud lane A.

Classical lattice counting / Mobius inversion with a new-to-project explicit
error budget. Universal statements are proved in CLOUD_CRT_ASCENT.md; finite
checks alone are not their proofs. All public numerical outputs are rational.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import gcd, isqrt
from typing import Iterable

Residues = Iterable[tuple[int, int]]


def _positive_int(n: int, name: str) -> int:
    if type(n) is not int or n < 1:
        raise ValueError(f"{name} must be a positive integer")
    return n


def _cutoff(x: int | Fraction) -> Fraction:
    if type(x) not in (int, Fraction) or x < 0:
        raise ValueError("cutoff must be a nonnegative int or Fraction")
    return Fraction(x)


def normalize_residues(W: int, residues: Residues) -> frozenset[tuple[int, int]]:
    _positive_int(W, "W")
    result = set()
    for pair in residues:
        if len(pair) != 2 or any(type(n) is not int for n in pair):
            raise ValueError("residue pairs must contain two integers")
        result.add((pair[0] % W, pair[1] % W))
    return frozenset(result)


@dataclass(frozen=True)
class RationalInterval:
    lower: Fraction
    upper: Fraction

    def contains(self, value: int | Fraction) -> bool:
        return self.lower <= value <= self.upper


def triangle_count(X: int | Fraction, W: int, residues: Residues) -> int:
    """Exact count of positive a,b with a+b<=X in the given residue SET."""
    X = _cutoff(X)
    total = 0
    for r, s in normalize_residues(W, residues):
        r, s = r or W, s or W
        n = (X - r - s) // W
        if n >= 0:
            total += (n + 1) * (n + 2) // 2
    return total


def triangle_enclosure(X: int | Fraction, W: int, residues: Residues) -> RationalInterval:
    """Sharp leading discrepancy constant 3/2; see theorem A1."""
    X = _cutoff(X)
    size = len(normalize_residues(W, residues))
    center = size * X * X / (2 * W * W)
    error = size * (3 * X / (2 * W) + 1)
    return RationalInterval(max(Fraction(0), center - error), center + error)


def cell_enclosure(X: int | Fraction, W: int, residues: Residues) -> RationalInterval:
    """Independent unit-cell sandwich; uses no floor-sum formula."""
    X = _cutoff(X)
    size = len(normalize_residues(W, residues))
    t = X / W
    return RationalInterval(size * max(t - 2, 0) ** 2 / 2, size * (t + 2) ** 2 / 2)


def rectangle_count(A: int | Fraction, B: int | Fraction, W: int, residues: Residues) -> int:
    A, B = _cutoff(A), _cutoff(B)
    total = 0
    for r, s in normalize_residues(W, residues):
        r, s = r or W, s or W
        total += max(0, (A - r) // W + 1) * max(0, (B - s) // W + 1)
    return total


def rectangle_enclosure(A: int | Fraction, B: int | Fraction, W: int, residues: Residues) -> RationalInterval:
    A, B = _cutoff(A), _cutoff(B)
    size = len(normalize_residues(W, residues))
    center = size * A * B / (W * W)
    error = size * ((A + B) / W + 1)
    return RationalInterval(max(Fraction(0), center - error), center + error)


def mobius(n: int) -> int:
    _positive_int(n, "n")
    result, p = 1, 2
    while p * p <= n:
        if n % p == 0:
            n //= p
            result = -result
            if n % p == 0:
                return 0
        p += 1
    return -result if n > 1 else result


def primitive_residues(W: int, residues: Residues) -> frozenset[tuple[int, int]]:
    """Remove classes impossible for global gcd(a,b)=1."""
    return frozenset((r, s) for r, s in normalize_residues(W, residues) if gcd(gcd(r, s), W) == 1)


def _scaled_residues(W: int, residues: frozenset[tuple[int, int]], d: int) -> frozenset[tuple[int, int]]:
    inv = pow(d, -1, W)
    return frozenset((r * inv % W, s * inv % W) for r, s in residues)


def primitive_triangle_count(X: int | Fraction, W: int, residues: Residues) -> int:
    """Exact Mobius identity, independently checkable against a gcd census."""
    X = _cutoff(X)
    allowed = primitive_residues(W, residues)
    return sum(mobius(d) * triangle_count(X / d, W, _scaled_residues(W, allowed, d))
               for d in range(1, int(X // 2) + 1) if gcd(d, W) == 1)


def primitive_density_enclosure(W: int, residues: Residues, D: int) -> RationalInterval:
    """Enclose |R_prim|/W² * product_{p not dividing W}(1-p^-2)."""
    _positive_int(D, "D")
    size = len(primitive_residues(W, residues))
    factor = Fraction(size, W * W)
    partial = sum((Fraction(mobius(d), d * d) for d in range(1, D + 1) if gcd(d, W) == 1), Fraction())
    radius = Fraction(1, D)
    return RationalInterval(factor * max(Fraction(1, 2), partial - radius), factor * min(Fraction(1), partial + radius))


@dataclass(frozen=True)
class PrimitiveBudget:
    """A finite, exact interval certificate; no claimed asymptotic at unsafe W."""
    local_residue_count: int
    cutoff_D: int
    center: Fraction
    lattice_error: Fraction
    omitted_divisor_error: int

    @property
    def enclosure(self) -> RationalInterval:
        error = self.lattice_error + self.omitted_divisor_error
        return RationalInterval(max(Fraction(0), self.center - error), self.center + error)


def primitive_triangle_budget(X: int | Fraction, W: int, residues: Residues, D: int) -> PrimitiveBudget:
    """Finite Mobius main term plus separate boundary and omitted-divisor errors.

    D is between 1 and floor(X/2). Empty triangles are handled explicitly.
    The omitted error is a universal union bound, not a probabilistic assumption.
    """
    X = _cutoff(X)
    _positive_int(D, "D")
    allowed = primitive_residues(W, residues)
    size, M = len(allowed), int(X // 2)
    if M == 0:
        if D != 1:
            raise ValueError("empty triangles use D=1")
        return PrimitiveBudget(size, D, Fraction(0), Fraction(0), 0)
    if D > M:
        raise ValueError("D exceeds floor(X/2)")
    partial = sum((Fraction(mobius(d), d * d) for d in range(1, D + 1) if gcd(d, W) == 1), Fraction())
    center = size * X * X * partial / (2 * W * W)
    # Removing zero Mobius coefficients and nonunits is an optional tighter bound.
    active = [d for d in range(1, D + 1) if gcd(d, W) == 1 and mobius(d)]
    lattice = size * sum((3 * X / (2 * W * d) + 1 for d in active), Fraction())
    omitted = sum(int(X // d) * (int(X // d) - 1) // 2 for d in range(D + 1, M + 1)) if size else 0
    return PrimitiveBudget(size, D, center, lattice, omitted)


def is_prime(p: int) -> bool:
    return type(p) is int and p >= 2 and all(p % d for d in range(2, isqrt(p) + 1))


def valuation_pattern(p: int, i: int, j: int, k: int) -> tuple[int, frozenset[tuple[int, int]]]:
    """Exact finite residues for v_p(a)=i,v_p(b)=j,v_p(a+b)=k, locally primitive.

    An enumeration utility for bounded research probes, not a large-modulus sieve.
    Incompatible occupations yield an empty set. Composite clocks are rejected.
    """
    if not is_prime(p) or any(type(v) is not int or v < 0 for v in (i, j, k)):
        raise ValueError("genuine prime and nonnegative integer valuations required")
    modulus = p ** (max(i, j, k) + 1)
    if sum(v > 0 for v in (i, j, k)) > 1:
        return modulus, frozenset()
    units = tuple(n for n in range(modulus) if n % p)
    if max(i, j, k) == 0:
        return modulus, frozenset((a, b) for a in units for b in units if (a + b) % p)
    h = max(i, j, k)
    occupied = tuple(p ** h * n for n in range(1, p))
    if i:
        residues = frozenset((a, b) for a in occupied for b in units)
    elif j:
        residues = frozenset((a, b) for a in units for b in occupied)
    else:
        residues = frozenset((a, (c - a) % modulus) for a in units for c in occupied)
    return modulus, residues


def combine_coprime_patterns(patterns: Iterable[tuple[int, Residues]]) -> tuple[int, frozenset[tuple[int, int]]]:
    """CRT product of independently sourced coprime moduli, preserving all pairs."""
    W, current = 1, frozenset({(0, 0)})
    for V, residues in patterns:
        next_residues = normalize_residues(V, residues)
        if gcd(W, V) != 1:
            raise ValueError("CRT factors must have coprime moduli")
        inv = pow(W, -1, V)
        current = frozenset((a + W * ((r - a) * inv % V), b + W * ((s - b) * inv % V))
                            for a, b in current for r, s in next_residues)
        W *= V
    return W, current
