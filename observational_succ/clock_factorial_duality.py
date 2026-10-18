"""Exact factorial/LCM Möbius duality and source-typed response diagnostics.

All computations use integers/Fractions and a divisor-incidence Möbius sieve.
The ambient N and floor arithmetic are imported metatheoretically; the module
is NOT a source-free construction of N or a proof of RH / signed Weil positivity.
"""
from __future__ import annotations

from fractions import Fraction
from math import factorial, gcd, isqrt
from typing import Sequence


def _horizon(value: int, maximum: int = 512) -> int:
    if type(value) is not int or not 1 <= value <= maximum:
        raise ValueError(f"horizon must be an integer in [1,{maximum}]")
    return value


def incidence_mobius(horizon: int) -> tuple[int, ...]:
    """Divisor-poset inverse of zeta; no prime species or Euler input."""
    n = _horizon(horizon)
    mu = [0] * (n + 1)
    mu[1] = 1
    # Incidence recursion: sum_{d|n} mu(d) = [n=1].
    for d in range(1, n + 1):
        for multiple in range(2 * d, n + 1, d):
            mu[multiple] -= mu[d]
    return tuple(mu)


def mertens_prefix(mu: Sequence[int]) -> tuple[int, ...]:
    if not mu or len(mu) < 2 or mu[1] != 1:
        raise ValueError("valid incidence array with mu(1)=1 required")
    running = 0
    m = [0]
    for value in mu[1:]:
        running += value
        m.append(running)
    return tuple(m)


def inverse_floor_sum(values: Sequence[int | Fraction]) -> Fraction:
    """Invert F(N)=sum_{k<=N}A(floor(N/k)); values[m-1]=F(m)."""
    n = _horizon(len(values))
    mu = incidence_mobius(n)
    return sum((mu[d] * values[n // d - 1] for d in range(1, n + 1)), Fraction(0))


def weighted_factorial_clock(horizon: int, mu: Sequence[int] | None = None) -> Fraction:
    """Product_{d<=N}(floor(N/d)!)^mu(d), exact signed rational."""
    n = _horizon(horizon)
    if mu is None:
        mu = incidence_mobius(n)
    if len(mu) <= n:
        raise ValueError("Möbius incidence table too short")
    numerator, denominator = 1, 1
    for d in range(1, n + 1):
        weight = mu[d]
        factor = factorial(n // d)
        if weight >= 0:
            numerator *= factor ** weight
        else:
            denominator *= factor ** (-weight)
    return Fraction(numerator, denominator)


def weighted_unit_clock(horizon: int, mu: Sequence[int] | None = None) -> Fraction:
    """Product_{m<=N}m^M(floor(N/m)), independent unit factorization."""
    n = _horizon(horizon)
    if mu is None:
        mu = incidence_mobius(n)
    if len(mu) <= n:
        raise ValueError("Möbius incidence table too short")
    m_prefix = mertens_prefix(mu)
    numerator, denominator = 1, 1
    for m in range(1, n + 1):
        weight = m_prefix[n // m]
        if weight >= 0:
            numerator *= m ** weight
        else:
            denominator *= m ** (-weight)
    return Fraction(numerator, denominator)


def lcm_clock(horizon: int) -> int:
    """Independent canonical superclock via sequential gcd/lcm, no prime oracle."""
    n = _horizon(horizon)
    acc = 1
    for k in range(2, n + 1):
        acc = acc // gcd(acc, k) * k
    return acc


def response_kernel(horizon: int, mu: Sequence[int] | None = None) -> tuple[int, ...]:
    """Coefficients for U_N(ell)=sum_m ell(m)*M(floor(N/m))."""
    n = _horizon(horizon)
    if mu is None:
        mu = incidence_mobius(n)
    if len(mu) <= n:
        raise ValueError("Möbius incidence table too short")
    prefix = mertens_prefix(mu)
    return tuple(prefix[n // m] for m in range(1, n + 1))


def cumulative_incidence_inverse(values: Sequence[int | Fraction]) -> Fraction:
    """Direct divisor convolution followed by summation (independent order)."""
    n = _horizon(len(values))
    mu = incidence_mobius(n)
    acc = Fraction(0)
    for j in range(1, n + 1):
        local = Fraction(0)
        for d in range(1, j + 1):
            if j % d == 0:
                local += mu[d] * values[j // d - 1]
        acc += local
    return acc


def single_site_response(horizon: int, position: int) -> int:
    """Response to a local delta perturbation at position m (not source lawful)."""
    n = _horizon(horizon)
    if type(position) is not int or not 1 <= position <= n:
        raise ValueError("reading position out of range")
    mu = incidence_mobius(n)
    return mertens_prefix(mu)[n // position]


def valuation_at(n: int, p: int) -> int:
    """p-adic valuation for user-declared prime p; mathematical oracle only."""
    if type(n) is not int or n < 1 or type(p) is not int or p < 2:
        raise ValueError("positive n and p>=2 required")
    # A composite 'p' does not yield a completely additive valuation.
    if any(p % d == 0 for d in range(2, isqrt(p) + 1)):
        raise ValueError("valuation generator must be prime")
    val = 0
    while n % p == 0:
        val += 1
        n //= p
    return val


def prime_weight_response(horizon: int, p: int) -> tuple[int, int]:
    """Comparison of µ-inversion of v_p(n) with prime-jet depth floor(log_p N)."""
    n = _horizon(horizon)
    values = [valuation_at(m, p) for m in range(1, n + 1)]
    via_incidence = cumulative_incidence_inverse(values)
    depth, power = 0, p
    while power <= n:
        depth += 1
        power *= p
    if via_incidence.denominator != 1:
        raise AssertionError("integral valuation current expected")
    return (int(via_incidence), depth)


def row_conditioning(horizon: int) -> dict[str, int]:
    """ℓ∞ -> absolute output norm on arbitrary real input readings."""
    n = _horizon(horizon)
    coeffs = response_kernel(n)
    return {
        "coefficient_sum": sum(coeffs),
        "linf_operator_norm": sum(abs(a) for a in coeffs),
        "unconditional_linear_lower_bound": (n + 1) // 2,
        "single_site_m2": coeffs[1] if n >= 2 else 0,
    }


def primitive_increment(horizon: int) -> Fraction:
    """L_N/L_(N-1), to calibrate n=6 and genuine p-power jets."""
    n = _horizon(horizon)
    return Fraction(lcm_clock(n), lcm_clock(n-1) if n > 1 else 1)
