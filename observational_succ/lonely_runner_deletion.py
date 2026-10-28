"""Exact certificates for deleting one speed from an initial interval.

The exact value is Liu's Theorem 18 (2008), together with the elementary
upper-half case.  This module does not decide the general Lonely Runner
Conjecture.  See research/2026-10-28/lonely_runner/ALPHA.md for proofs,
the sharp minimum, and the distinction between a witness and an upper bound.
"""

from dataclasses import dataclass
from fractions import Fraction
from math import gcd


def _parameters(n: int, r: int) -> None:
    if type(n) is not int or type(r) is not int:
        raise TypeError("n and r must be integers, excluding booleans")
    if n < 3 or not 1 <= r <= n - 1:
        raise ValueError("require n >= 3 and 1 <= r <= n-1")


def retained_speeds(n: int, r: int) -> tuple[int, ...]:
    """The original unshifted speed set, with exactly r removed."""
    _parameters(n, r)
    return tuple(i for i in range(1, n) if i != r)


def circle_distance(x: Fraction) -> Fraction:
    """Exact distance to the nearest integer; no floating-point input."""
    if not isinstance(x, (int, Fraction)) or isinstance(x, bool):
        raise TypeError("exact integer or Fraction required")
    y = Fraction(x) % 1
    return min(y, 1 - y)


def value_at(n: int, r: int, time: Fraction) -> Fraction:
    """Evaluate the retained lower envelope at one exact rational time."""
    if not isinstance(time, (int, Fraction)) or isinstance(time, bool):
        raise TypeError("exact integer or Fraction time required")
    return min(circle_distance(i * time) for i in retained_speeds(n, r))


@dataclass(frozen=True)
class DeletionWitness:
    n: int
    r: int
    time: Fraction
    guarantee: Fraction
    strategy: str

    def verify(self) -> bool:
        """Finite certificate verification, not a proof of a global upper bound."""
        _parameters(self.n, self.r)
        return (
            isinstance(self.time, Fraction)
            and isinstance(self.guarantee, Fraction)
            and 0 <= self.time <= 1
            and 0 < self.guarantee <= value_at(self.n, self.r, self.time)
        )


def universal_witness(n: int, r: int) -> DeletionWitness:
    """Construct the user's 2/(2n-3) witness without a coprimality search.

    In the middle range use D=kr+1 and t=k/D.  This uses the inverse
    -k of r modulo D, up to the circle reflection t -> 1-t.
    """
    _parameters(n, r)
    if n < 5 or r > n - 2:
        raise ValueError("universal strict bound requires n >= 5, r <= n-2")
    if 2 * r > n - 1:
        return DeletionWitness(n, r, Fraction(1, r), Fraction(2, 2 * n - 3), "centre")
    k = 3 if n == 2 * r + 1 else (n + r - 2) // r + 1
    denominator = k * r + 1
    return DeletionWitness(
        n, r, Fraction(k, denominator), Fraction(2, 2 * n - 3), "inverse"
    )


def least_coprime_denominator(n: int, r: int) -> int:
    """Least D >= n+r coprime to r; valid even outside the optimal range."""
    _parameters(n, r)
    denominator = n + r
    while gcd(denominator, r) != 1:
        denominator += 1
    return denominator


def optimal_witness(n: int, r: int) -> DeletionWitness:
    """Exact optimizer, using Liu's formula and the centre upper bound."""
    _parameters(n, r)
    if 2 * r > n - 1:
        return DeletionWitness(n, r, Fraction(1, r), Fraction(1, r), "centre")
    denominator = least_coprime_denominator(n, r)
    numerator = pow(r, -1, denominator)
    return DeletionWitness(
        n, r, Fraction(numerator, denominator), Fraction(2, denominator), "Liu inverse"
    )


def exact_deletion_value(n: int, r: int) -> Fraction:
    """The proved formula; this is not a numerical maximization routine."""
    return optimal_witness(n, r).guarantee


def sharp_minimum(n: int) -> tuple[Fraction, tuple[int, ...]]:
    """Minimum over 1 <= r <= n-2, including ALL equality cases."""
    if type(n) is not int:
        raise TypeError("n must be an integer, excluding booleans")
    if n < 5:
        raise ValueError("require n >= 5")
    if n == 5:
        return Fraction(2, 7), (2,)
    if n == 6:
        return Fraction(2, 9), (2,)
    if n == 7:
        return Fraction(1, 5), (3, 5)
    return Fraction(1, n - 2), (n - 2,)
