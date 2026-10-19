"""Exact finite certificates for arbitrarily late Beurling source mutations.

The infinite claims are proved in ARITHMETIC_SOURCE_MINIMALITY.md.  No zero
locations, floating transcendental values, or assumed positivity enter here.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import gcd, isqrt


def _integer(value: int, minimum: int = 1) -> int:
    if type(value) is not int or value < minimum:
        raise ValueError("expected an integer in the stated positive domain")
    return value


def _rational(value: int | Fraction) -> Fraction:
    if isinstance(value, bool) or not isinstance(value, (int, Fraction)):
        raise ValueError("exact int or Fraction required")
    value = Fraction(value)
    if value < 1:
        raise ValueError("horizon must be at least one")
    return value


def _is_prime(n: int) -> bool:
    return n >= 2 and all(n % d for d in range(2, isqrt(n) + 1))


def _next_prime(n: int) -> int:
    candidate = n + 1
    while not _is_prime(candidate):
        candidate += 1
    return candidate


def _powers(base: Fraction, cutoff: Fraction) -> tuple[Fraction, ...]:
    result = []
    value = Fraction(1)
    while value <= cutoff:
        result.append(value)
        value *= base
    return tuple(result)


@dataclass(frozen=True)
class LateBeurlingPair:
    """Replace genuine p,q by a,b; retain all other ordinary primes.

    p,q are externally authenticated ordinary primes, used to construct an
    adversarial model, not claimed to be discovered by this finite routine.
    """

    p: int
    q: int

    def __post_init__(self) -> None:
        _integer(self.p, 3)
        _integer(self.q, 2)
        if not _is_prime(self.p) or not _is_prime(self.q):
            raise ValueError("both deleted generators must be genuine primes")
        if self.q <= self.p * self.p:
            raise ValueError("require q > p squared")

    @classmethod
    def beyond(cls, horizon: int | Fraction) -> "LateBeurlingPair":
        cutoff = _rational(horizon)
        p = _next_prime(max(2, cutoff.numerator // cutoff.denominator))
        return cls(p, _next_prime(p * p))

    @property
    def a(self) -> Fraction:
        return Fraction(self.p * self.p, self.p - 1)

    @property
    def b(self) -> Fraction:
        p, q = self.p, self.q
        return Fraction(q * (p * p - p + 1), q + p * (p - 1))

    def density_multiplier(self) -> Fraction:
        """Exact residue/density multiplier, proved to be one for this family."""
        old = (1 - Fraction(1, self.p)) * (1 - Fraction(1, self.q))
        new = (1 - 1 / self.a) * (1 - 1 / self.b)
        return old / new

    def count(self, horizon: int | Fraction) -> int:
        """Count source words by independent integer inclusion-exclusion."""
        cutoff = _rational(horizon)
        total = 0
        for aj in _powers(self.a, cutoff):
            for bk in _powers(self.b, cutoff / aj):
                y = cutoff / (aj * bk)
                n = y.numerator // y.denominator
                total += n - n // self.p - n // self.q + n // (self.p * self.q)
        return total

    def atoms(self, horizon: int | Fraction, *, budget: int = 100_000) -> tuple[Fraction, ...]:
        """Enumerate exact word values, fail closed on duplicates or excess work."""
        cutoff = _rational(horizon)
        _integer(budget)
        values = set()
        work = 0
        for aj in _powers(self.a, cutoff):
            for bk in _powers(self.b, cutoff / aj):
                scale = aj * bk
                y = cutoff / scale
                for m in range(1, y.numerator // y.denominator + 1):
                    work += 1
                    if work > budget:
                        raise ValueError("enumeration budget exceeded")
                    if gcd(m, self.p * self.q) == 1:
                        value = m * scale
                        if value in values:
                            raise ArithmeticError("source word collision")
                        values.add(value)
        return tuple(sorted(values))

    def counting_error_bound(self, horizon: int | Fraction) -> Fraction:
        """Paper-proved bound on abs(count(X)-X), with no numeric logarithms."""
        cutoff = _rational(horizon)
        j1 = len(_powers(self.a, cutoff))
        k1 = len(_powers(self.b, cutoff))
        return 2 * j1 * k1 + j1 * (1 - 1 / self.a) + 1

    def first_braid_witness(self) -> dict[str, int]:
        """Compute the V_2 rank defect, rather than return its predicted value."""
        spectrum = self.atoms(self.p + 1)
        rank = {value: index + 1 for index, value in enumerate(spectrum)}
        x = (self.p - 1) // 2
        successor = spectrum[rank[Fraction(x)]]
        if successor.denominator != 1:
            raise ArithmeticError("unexpected first successor")
        return {
            "x": x,
            "successor_x": int(successor),
            "rank_V2_x": rank[Fraction(2 * x)],
            "rank_V2_successor_x": rank[2 * successor],
            "rank_2": rank[Fraction(2)],
            "defect": rank[2 * successor] - rank[Fraction(2 * x)] - rank[Fraction(2)],
        }


def incomplete_clock_witness(periods: tuple[int, ...], prime: int = 2) -> dict[str, int]:
    """All-prime-exposed supernatural clock shadow with one capped depth.

    Other prime exponents are infinite.  The queried periods all survive;
    prime**(cap+1) is the explicit next unavailable quotient.
    """
    _integer(prime, 2)
    if not _is_prime(prime):
        raise ValueError("a genuine prime place is required")
    cap = 1
    for period in periods:
        _integer(period)
        exponent = 0
        while period % prime == 0:
            period //= prime
            exponent += 1
        cap = max(cap, exponent)
    return {"prime": prime, "cap": cap, "missing_period": prime ** (cap + 1)}


def multiplication_compression_characteristic(prime: int) -> tuple[Fraction, ...]:
    """Coefficients of det(tI-P A_p P), descending in t.

    A_p=(I-p^-1/2 V_p)^*(I-p^-1/2 V_p), P onto span(e_1,e_p).
    Coefficients are rational even though its off-diagonal is -1/sqrt(p).
    """
    _integer(prime, 2)
    if not _is_prime(prime):
        raise ValueError("a genuine prime multiplier is required")
    diagonal = 1 + Fraction(1, prime)
    return (Fraction(1), -2 * diagonal, diagonal * diagonal - Fraction(1, prime))
