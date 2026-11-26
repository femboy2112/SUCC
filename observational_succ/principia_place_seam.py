"""Exact rational samples of the absolute-value observer seam on Q.

Each coefficient pair (p, a) represents a *formal* a*log(p), with rational a.
No numerical logarithm, floating exponentiation or approximate zero is used.
The source rational, place and normalization exponent remain in each readout.

Ostrowski's classical theorem makes the trivial absolute value compulsory on
any pointwise-continuous path between distinct places. These finite exact
samples illustrate that theorem; they do not prove continuity or RH.

At the trivial norm every nonzero magnitude is 1, hence its logarithm is 0.
This is a magnitude-null display, not a claim of zero information for every
toolkit: the trivial norm of q-a still tests the equality q=a.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import isqrt
from typing import Iterable, Literal


Place = int | Literal["infinity", "trivial"]
LogCoefficients = tuple[tuple[int, Fraction], ...]


def _rational(value: int | Fraction, name: str) -> Fraction:
    if type(value) not in (int, Fraction):
        raise TypeError(f"{name} must be an exact int or Fraction")
    return Fraction(value)


def _is_prime(value: int) -> bool:
    return (
        type(value) is int
        and value >= 2
        and all(value % d for d in range(2, isqrt(value) + 1))
    )


def _check_place(place: Place) -> None:
    if type(place) is str and place in ("infinity", "trivial"):
        return
    if not _is_prime(place):
        raise ValueError("place must be 'infinity', 'trivial', or a genuine prime")


def _factor_positive(n: int) -> dict[int, int]:
    factors: dict[int, int] = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors[d] = factors.get(d, 0) + 1
            n //= d
        d = 3 if d == 2 else d + 2
    if n > 1:
        factors[n] = factors.get(n, 0) + 1
    return factors


def rational_prime_exponents(source: int | Fraction) -> tuple[tuple[int, int], ...]:
    """Return the finite signed prime valuations of a nonzero rational."""
    q = _rational(source, "source")
    if not q:
        raise ValueError("log magnitude is defined here only for a nonzero source")
    factors = _factor_positive(abs(q.numerator))
    for prime, exponent in _factor_positive(q.denominator).items():
        factors[prime] = factors.get(prime, 0) - exponent
    return tuple(sorted((p, e) for p, e in factors.items() if e))


def _coefficients(
    source: Fraction, place: Place, exponent: Fraction
) -> LogCoefficients:
    factors = dict(rational_prime_exponents(source))
    if not exponent or place == "trivial":
        return ()
    if place == "infinity":
        return tuple((p, exponent * e) for p, e in sorted(factors.items()))
    coefficient = -exponent * factors.get(place, 0)
    return ((place, coefficient),) if coefficient else ()


@dataclass(frozen=True)
class PlaceReadout:
    """A source-retaining, exactly normalized formal logarithmic observation."""

    source: Fraction
    place: Place
    exponent: Fraction
    log_coefficients: LogCoefficients

    def __post_init__(self) -> None:
        if type(self.source) is not Fraction or type(self.exponent) is not Fraction:
            raise TypeError("readout source and exponent must be exact Fractions")
        if not self.source:
            raise ValueError("zero has no finite logarithmic magnitude")
        _check_place(self.place)
        if self.exponent < 0:
            raise ValueError("absolute-value exponents must be nonnegative")
        if self.place == "infinity" and self.exponent > 1:
            raise ValueError("Archimedean exponent must be at most one")
        if self.place == "trivial" and self.exponent != 0:
            raise ValueError("the trivial place uses exponent zero")
        if type(self.log_coefficients) is not tuple or any(
            type(term) is not tuple
            or len(term) != 2
            or type(term[0]) is not int
            or type(term[1]) is not Fraction
            for term in self.log_coefficients
        ):
            raise TypeError("log coefficients must be immutable exact prime/Fraction pairs")
        expected = _coefficients(self.source, self.place, self.exponent)
        if self.log_coefficients != expected:
            raise ValueError("log coefficients do not match the retained source and place")

    def as_dict(self) -> dict[int, Fraction]:
        return dict(self.log_coefficients)


def place_readout(
    source: int | Fraction, place: Place, exponent: int | Fraction = 1
) -> PlaceReadout:
    """Construct log(|source|_place**exponent) without numerical logs."""
    q = _rational(source, "source")
    power = _rational(exponent, "exponent")
    _check_place(place)
    return PlaceReadout(q, place, power, _coefficients(q, place, power))


@dataclass(frozen=True)
class PathReadout:
    """Retain endpoint place labels even when the current display is trivial."""

    parameter: Fraction
    start_place: Place
    end_place: Place
    observation: PlaceReadout


def path_via_trivial(
    source: int | Fraction,
    parameter: int | Fraction,
    start_place: Place,
    end_place: Place,
) -> PathReadout:
    """Sample a path with unit endpoint exponents and trivial midpoint.

    The two endpoint places must be nontrivial. Distinct places make this a
    necessary seam by the paper theorem. Equal places also admit this path,
    but can instead be joined without a seam by keeping the exponent positive.
    """
    q = _rational(source, "source")
    t = _rational(parameter, "parameter")
    _check_place(start_place)
    _check_place(end_place)
    if start_place == "trivial" or end_place == "trivial":
        raise ValueError("this constructor uses nontrivial endpoint places")
    if not 0 <= t <= 1:
        raise ValueError("path parameter must lie in [0, 1]")
    if t < Fraction(1, 2):
        result = place_readout(q, start_place, 1 - 2 * t)
    elif t > Fraction(1, 2):
        result = place_readout(q, end_place, 2 * t - 1)
    else:
        result = place_readout(q, "trivial", 0)
    return PathReadout(t, start_place, end_place, result)


def archimedean_to_prime(
    source: int | Fraction, parameter: int | Fraction, prime: int
) -> PathReadout:
    """Sample the explicit infinity -> trivial -> p observer path."""
    if not _is_prime(prime):
        raise ValueError("the endpoint must be a genuine rational prime")
    return path_via_trivial(source, parameter, "infinity", prime)


def sum_log_coefficients(vectors: Iterable[LogCoefficients]) -> LogCoefficients:
    """Add exact prime-log vectors; reject counterfeit prime basis labels."""
    total: dict[int, Fraction] = {}
    for vector in vectors:
        for prime, coefficient in vector:
            if not _is_prime(prime):
                raise ValueError("log basis labels must be genuine primes")
            a = _rational(coefficient, "log coefficient")
            total[prime] = total.get(prime, Fraction(0)) + a
    return tuple(sorted((p, a) for p, a in total.items() if a))


def product_formula_readouts(source: int | Fraction) -> tuple[PlaceReadout, ...]:
    """Return all nonzero normalized terms in the rational product formula.

    The real term is always included. At all omitted primes the log readout
    is zero. Every returned observation retains the SAME source rational.
    """
    q = _rational(source, "source")
    primes = (p for p, _ in rational_prime_exponents(q))
    return (place_readout(q, "infinity"),) + tuple(
        place_readout(q, p) for p in primes
    )


def canonical_seam_germs(
    source: int | Fraction, prime: int
) -> tuple[LogCoefficients, LogCoefficients]:
    """Exact left and right derivatives of log readout at t=1/2.

    The left derivative is -2*log|q|_infinity, the right 2*log|q|_p.
    Unlike the zero seam value, these generally retain arithmetic content.
    """
    if not _is_prime(prime):
        raise ValueError("the endpoint must be a genuine rational prime")
    left = place_readout(source, "infinity").log_coefficients
    right = place_readout(source, prime).log_coefficients
    return (
        tuple((p, -2 * coefficient) for p, coefficient in left),
        tuple((p, 2 * coefficient) for p, coefficient in right),
    )


def trivial_magnitude(source: int | Fraction) -> int:
    """The trivial norm retains zero versus nonzero, including equality tests."""
    return int(bool(_rational(source, "source")))


@dataclass(frozen=True)
class RationalCapacity:
    """Checked lower capacity on one explicitly retained rational witness."""

    source: Fraction
    clearing_denominator: int
    integral_witness: int
    prime_powers: tuple[tuple[int, int], ...]
    divisor: int
    magnitude_lower_bound: Fraction


def rational_capacity(
    source: int | Fraction,
    clearing_denominator: int,
    prime_powers: Iterable[tuple[int, int]],
) -> RationalCapacity:
    """Check M|D*source != 0 and certify |source| >= M/D.

    Duplicate prime labels are rejected: repeating one valuation certificate
    is not an independent multiplicity gain. An analytic upper bound, if used
    elsewhere, must concern this same source and paid denominator.
    """
    q = _rational(source, "source")
    if not q:
        raise ValueError("the nonzero-witness capacity requires source != 0")
    if type(clearing_denominator) is not int or clearing_denominator <= 0:
        raise ValueError("clearing denominator must be a positive integer")
    n = clearing_denominator * q
    if n.denominator != 1:
        raise ValueError("declared denominator does not clear this source")
    items: list[tuple[int, int]] = []
    seen: set[int] = set()
    divisor = 1
    for prime, exponent in prime_powers:
        if not _is_prime(prime):
            raise ValueError("valuation label must be a genuine prime")
        if prime in seen:
            raise ValueError("duplicate prime certificate is not independent")
        if type(exponent) is not int or exponent < 0:
            raise ValueError("valuation lower bound must be a nonnegative integer")
        seen.add(prime)
        power = prime**exponent
        if n.numerator % power:
            raise ValueError("declared prime-power divisibility is false for this source")
        divisor *= power
        items.append((prime, exponent))
    return RationalCapacity(
        q,
        clearing_denominator,
        n.numerator,
        tuple(sorted(items)),
        divisor,
        Fraction(divisor, clearing_denominator),
    )
