"""Exact finite contracts for adaptive grade-zero certificates.

This module verifies algebraic budgets, not the source of a histogram or
response. Arithmetic/source authentication and every integral-count promise
remain caller obligations. No computation here proves an asymptotic theorem.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import prod


Q = Fraction


def rational(value: int | Q) -> Q:
    if type(value) not in (int, Q):
        raise ValueError("an exact integer or Fraction is required")
    return Q(value)


def parameters(degree: int, t: Q = Q(1, 2)) -> tuple[int, Q]:
    if type(degree) is not int or degree < 2 or degree % 2:
        raise ValueError("degree must be an even integer at least two")
    t = rational(t)
    if not 0 < t <= Q(1, 2):
        raise ValueError("the certified parameter range is 0 < t <= 1/2")
    return degree, t


def leakage(degree: int, t: Q = Q(1, 2)) -> Q:
    degree, t = parameters(degree, t)
    return t ** (degree * (degree + 1) // 2)


def grade_response(grade: int, degree: int, t: Q = Q(1, 2)) -> Q:
    """Evaluate the product filter directly at one nonnegative integer grade."""
    degree, t = parameters(degree, t)
    if type(grade) is not int or grade < 0:
        raise ValueError("grade must be a nonnegative integer")
    z = t ** grade
    return z * prod(
        ((z - t ** j) / (1 - t ** j) for j in range(1, degree)),
        start=Q(1),
    )


def _histogram(histogram) -> tuple[Q, ...]:
    counts = tuple(rational(count) for count in histogram)
    if any(count < 0 for count in counts):
        raise ValueError("histogram masses must be nonnegative")
    return counts


def filtered_response(histogram, degree: int, t: Q = Q(1, 2)) -> Q:
    degree, t = parameters(degree, t)
    return sum(
        (count * grade_response(h, degree, t)
         for h, count in enumerate(_histogram(histogram))),
        start=Q(),
    )


def tail_weight(histogram, degree: int, t: Q = Q(1, 2)) -> Q:
    """The EXTRA observable sum_(h>=degree) c_h t^h, not inferred from F(t)."""
    degree, t = parameters(degree, t)
    return sum(
        (count * t ** h
         for h, count in enumerate(_histogram(histogram)) if h >= degree),
        start=Q(),
    )


def witness_margin(mass: int, degree: int, t: Q = Q(1, 2),
                   filtered_error: Q = Q()) -> Q:
    """Sharp mass-only worst margin for a positive INTEGER zero count.

    If |reported_B - genuine_B| <= filtered_error and the certificate is
    reported_B - filtered_error, its worst margin is
    1 - epsilon*(mass-1) - 2*filtered_error.
    A strictly positive result is necessary and sufficient for success for
    EVERY histogram of integer total mass <= mass and EVERY allowed noise.
    """
    if type(mass) is not int or mass < 1:
        raise ValueError("a positive integer mass budget is required")
    error = rational(filtered_error)
    if error < 0:
        raise ValueError("the filtered error must be nonnegative")
    return 1 - leakage(degree, t) * (mass - 1) - 2 * error


def _ceil(value: Q) -> int:
    return -((-value.numerator) // value.denominator)


def _floor(value: Q) -> int:
    return value.numerator // value.denominator


def recover_integer_count(value: Q, mass: int, degree: int,
                          t: Q = Q(1, 2)) -> int:
    """Recover max(0, ceil(B)) under the sharp mass-only completeness budget.

    Assumes an authentic exact response, nonnegative histogram mass <= mass,
    and an integral zero count. It rejects insufficient budgets and packets
    inconsistent with the necessary scalar model bounds. These checks do
    not authenticate the source or establish the integral-count promise.
    """
    value = rational(value)
    eps = leakage(degree, t)
    if type(mass) is not int or mass < 0:
        raise ValueError("mass must be a nonnegative integer")
    if mass == 0:
        if value != 0:
            raise ValueError("zero mass requires zero response")
        return 0
    if witness_margin(mass, degree, t) <= 0:
        raise ValueError("the mass-only exact-recovery budget is not strict")
    lower = max(Q(), value)
    upper = min(Q(mass), (value + eps * mass) / (1 + eps))
    answer = max(0, _ceil(value))
    if upper < lower or not lower <= answer <= upper:
        raise ValueError("packet contradicts the declared integer-count model")
    return answer


def tail_factors(degree: int, t: Q = Q(1, 2)) -> tuple[Q, Q]:
    """Sharp lower factor and limiting upper factor for tail-weight leakage."""
    degree, t = parameters(degree, t)
    lower = t ** (degree * (degree - 1) // 2)
    upper = lower / prod((1 - t ** j for j in range(1, degree)), start=Q(1))
    return lower, upper


def _interval(pair) -> tuple[Q, Q]:
    pair = tuple(pair)
    if len(pair) != 2:
        raise ValueError("an interval requires two rational endpoints")
    lower, upper = map(rational, pair)
    if lower > upper:
        raise ValueError("interval endpoints are reversed")
    return lower, upper


@dataclass(frozen=True)
class TargetInterval:
    lower: Q
    upper: Q
    integer_lower: int | None = None
    integer_upper: int | None = None
    source_authentication_required: bool = True

    @property
    def positive(self) -> bool:
        return self.lower > 0

    @property
    def count_recovered(self) -> bool:
        return (self.integer_lower is not None
                and self.integer_lower == self.integer_upper)


def tail_certificate(filtered_interval, tail_weight_interval, mass: Q,
                     degree: int, t: Q = Q(1, 2), *,
                     tail_mass_upper: Q | None = None,
                     integral_counts: bool = False) -> TargetInterval:
    """Certify c_0 using an authenticated filtered response AND tail weight.

    The tail observable is T=sum_(h>=d)c_h*t^h. Its interval is additional
    information; the function does not construct it from unmasked moments.
    If lambda <= -q(h)/t^h <= K for h>=d, then
    B+lambda*T <= c_0 <= B+K*T.
    The result also intersects the original total-mass and optional
    tail-mass leakage bounds. Integral rounding needs an explicit promise.
    """
    degree, t = parameters(degree, t)
    mass = rational(mass)
    if mass < 0 or type(integral_counts) is not bool:
        raise ValueError("nonnegative mass and a boolean count promise required")
    b_lo, b_hi = _interval(filtered_interval)
    tail_lo, tail_hi = _interval(tail_weight_interval)
    tail_lo = max(Q(), tail_lo)
    tail_hi = min(tail_hi, mass * t ** degree)
    if tail_mass_upper is not None:
        tail_mass_upper = rational(tail_mass_upper)
        if tail_mass_upper < 0:
            raise ValueError("tail mass upper bound must be nonnegative")
        tail_mass_upper = min(tail_mass_upper, mass)
        tail_hi = min(tail_hi, tail_mass_upper * t ** degree)
    if tail_hi < tail_lo:
        raise ValueError("tail interval contradicts the declared mass bounds")
    factor_lo, factor_hi = tail_factors(degree, t)
    eps = leakage(degree, t)
    lower = max(Q(), b_lo + factor_lo * tail_lo)
    upper = min(mass, b_hi + factor_hi * tail_hi,
                (b_hi + eps * mass) / (1 + eps))
    if tail_mass_upper is not None:
        upper = min(upper, b_hi + eps * tail_mass_upper)
    if upper < lower:
        raise ValueError("response packet contradicts the declared grade model")
    if not integral_counts:
        return TargetInterval(lower, upper)
    integer_lower, integer_upper = _ceil(lower), _floor(upper)
    if integer_lower > integer_upper:
        raise ValueError("response packet contradicts the integral-count promise")
    return TargetInterval(lower, upper, integer_lower, integer_upper)
