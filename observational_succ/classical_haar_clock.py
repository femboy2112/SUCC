"""Normalized real Haar clocks for source-centered SUCC/FUCC observations.

Finite Z/p^rZ probability carriers only; Fractions are exact real-rational
weights, never claimed to be bounded Q_p-valued Haar integration.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import gcd, isqrt
from typing import Iterable

from .classical_unit_origin import (
    ClassicalOriginError, chart_multiplier, chart_successor,
)


def _p(n: int) -> bool:
    if type(n) is not int or n < 2:
        return False
    return all(n % d for d in range(2, isqrt(n) + 1))


@dataclass(frozen=True)
class PrimeHaarClock:
    """Uniform REAL probability on residues of Z/p^r, with source chart."""

    p: int
    r: int
    chart: str = "n_minus_one"

    def __post_init__(self) -> None:
        if not _p(self.p) or type(self.r) is not int or self.r < 1:
            raise ClassicalOriginError("A genuine prime and positive integral precision are required")
        if self.chart not in ("n_minus_one", "one_minus_n"):
            raise ClassicalOriginError("Choose a source-centered chart")
        if self.p**self.r > 256:
            raise ClassicalOriginError("Explicit finite clock budget exceeded")

    @property
    def size(self) -> int:
        return self.p**self.r

    def succ(self, x: int, step: int = 1) -> int:
        return chart_successor(x, step, self.chart) % self.size

    def multiplier(self, x: int, m: int) -> int:
        return chart_multiplier(x, m, self.chart) % self.size

    def image(self, m: int) -> tuple[int, ...]:
        return tuple(sorted({self.multiplier(x, m) for x in range(self.size)}))

    def fibers(self, m: int) -> tuple[int, ...]:
        return tuple(sum(self.multiplier(x, m) == y for x in range(self.size))
                     for y in range(self.size))


def _vec(clock: PrimeHaarClock, values: Iterable[Fraction | int]) -> tuple[Fraction, ...]:
    if not isinstance(clock, PrimeHaarClock):
        raise ClassicalOriginError("Declared finite prime clock required")
    values = tuple(values)
    if len(values) != clock.size or any(type(v) not in (int, Fraction) for v in values):
        raise ClassicalOriginError("Full vector of exact rational amplitudes required")
    return tuple(Fraction(v) for v in values)


def haar_inner(clock: PrimeHaarClock, a: Iterable, b: Iterable) -> Fraction:
    """Exact normalized real L2 inner product; complex version is sesquilinear."""
    a, b = _vec(clock, a), _vec(clock, b)
    return sum((x * y for x, y in zip(a, b)), Fraction(0)) / clock.size


def _pair(low: PrimeHaarClock, high: PrimeHaarClock) -> None:
    if (not isinstance(low, PrimeHaarClock) or not isinstance(high, PrimeHaarClock)
            or low.p != high.p or low.r + 1 != high.r or low.chart != high.chart):
        raise ClassicalOriginError("Adjacent same-prime/source-chart precision levels required")


def pullback(low: PrimeHaarClock, high: PrimeHaarClock, f: Iterable) -> tuple[Fraction, ...]:
    """Pi^*:L2(Z/p^r)->L2(Z/p^(r+1)), an isometric cylinder embedding."""
    _pair(low, high)
    f = _vec(low, f)
    return tuple(f[x % low.size] for x in range(high.size))


def condition(high: PrimeHaarClock, low: PrimeHaarClock, f: Iterable) -> tuple[Fraction, ...]:
    """(Pi^*)^*: exact Haar conditional expectation, average over p lifts."""
    _pair(low, high)
    f = _vec(high, f)
    return tuple(sum((f[a + j*low.size] for j in range(low.p)), Fraction(0)) / low.p
                 for a in range(low.size))


def succ_observable(clock: PrimeHaarClock, f: Iterable, step: int) -> tuple[Fraction, ...]:
    """Koopman pullback f->f(S_step(x)); note action order reversal."""
    f = _vec(clock, f)
    return tuple(f[clock.succ(x, step)] for x in range(clock.size))


def multiply_observable(clock: PrimeHaarClock, f: Iterable, m: int) -> tuple[Fraction, ...]:
    """Koopman pullback of TRUE affine source chart multiplier."""
    f = _vec(clock, f)
    return tuple(f[clock.multiplier(x, m)] for x in range(clock.size))


def multiplier_operator_norm_squared(clock: PrimeHaarClock, m: int) -> int:
    """Exact ||f->f(m*x+offset)||² operator norm is gcd(m,p^r)."""
    if type(m) is not int or m < 1:
        raise ClassicalOriginError("Positive exact integer multiplication required")
    return gcd(m, clock.size)


def image_energy(clock: PrimeHaarClock, f: Iterable, m: int) -> Fraction:
    """||1_(image A_m) f||² for the declared real Haar measure."""
    f = _vec(clock, f)
    return sum((f[j] * f[j] for j in clock.image(m)), Fraction(0)) / clock.size


def p_adic_size_of_uniform_atom(clock: PrimeHaarClock) -> int:
    """p-adic absolute value |p^(-r)|_p = p^r (not real Haar norm)."""
    return clock.size


def classical_haar_clock_probe() -> dict:
    """Deterministic exact Hilbert cylinder and nonunit-multiplier receipt."""
    low = PrimeHaarClock(3, 1)
    high = PrimeHaarClock(3, 2)
    f = (Fraction(1, 2), Fraction(-2, 3), Fraction(3, 4))
    g = tuple(Fraction((2*j) % 7 - 3, 5) for j in range(high.size))
    pf = pullback(low, high, f)
    eg = condition(high, low, g)
    assert haar_inner(low, f, f) == haar_inner(high, pf, pf)
    assert haar_inner(high, pf, g) == haar_inner(low, f, eg)
    assert condition(high, low, pf) == f
    for m in (2, 3, 4, 6):
        vm = multiply_observable(high, g, m)
        assert haar_inner(high, vm, vm) == gcd(m, high.size) * image_energy(high, g, m)
        assert multiply_observable(high, pf, m) == pullback(low, high, multiply_observable(low, f, m))
    # Nonunit multiplier fails to intertwine uniform conditional expectations.
    low2, high2 = PrimeHaarClock(2, 1), PrimeHaarClock(2, 2)
    delta_one = (Fraction(0), Fraction(1), Fraction(0), Fraction(0))
    left = condition(high2, low2, multiply_observable(high2, delta_one, 2))
    right = multiply_observable(low2, condition(high2, low2, delta_one), 2)
    assert left != right
    return {
        "kind": "CLASSICAL_HAAR_CLOCK_EXACT_RECEIPT",
        "source_chart": "n_minus_one",
        "real_haar_pullback_isometric": True,
        "real_haar_conditional_expectation_adjoint": True,
        "condition_after_pullback_identity": True,
        "multiplication_p_on_3_squared_norm": multiplier_operator_norm_squared(high, 3),
        "multiplication_unit_on_3_squared_norm": multiplier_operator_norm_squared(high, 2),
        "multiplication_p_image": list(high.image(3)),
        "nonunit_multiplication_breaks_conditional_commutation": left != right,
        "finite_p_multiplier_has_kernel": len(set(high.multiplier(x, 3) for x in range(high.size))) < high.size,
        "complex_Haar_is_NOT_bounded_Qp_valued_Haar": True,
        "p_adic_atom_absolute_values_grow": [p_adic_size_of_uniform_atom(PrimeHaarClock(2, r)) for r in (1,2,3)],
        "global_p_adic_injective_limit_verified_by_computation": False,
        "global_weil_positivity_or_RH_proved": False,
    }
