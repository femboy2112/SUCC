"""Effective fixed-divisor density for primitive abc triples (independent lemma).

For pairwise-coprime positive integers d,e,f with D=def, and real X>=1:

    | N_X(d,e,f) - rho_D * X^2 | <= X * tau(D) + D

where rho_D = (2 zeta(2) D)^-1 prod_{p|D} p/(p+1) and tau is the divisor function.

This is an ELEMENTARY paper lemma (see
research/2026-10-28/PRIMITIVE_ABC_EFFECTIVE_NOTE.md); the code below certifies the
finite agreement, NOT the theorem. No float, no imported abc module, no oracle.
"""
from __future__ import annotations

from fractions import Fraction
from math import gcd, isqrt


def _positive_int(n: int, name: str) -> None:
    if type(n) is not int or n < 1:
        raise ValueError(f"{name} must be a positive integer")


def divisor_count(n: int) -> int:
    _positive_int(n, "n")
    c = 0
    for i in range(1, isqrt(n) + 1):
        if n % i == 0:
            c += 2 if i * i != n else 1
    return c


def _radical(n: int) -> int:
    r = 1
    p = 2
    m = n
    while p * p <= m:
        if m % p == 0:
            r *= p
            while m % p == 0:
                m //= p
        p += 1
    if m > 1:
        r *= m
    return r


def _distinct_primes(n: int) -> tuple[int, ...]:
    out = []
    p = 2
    m = n
    while p * p <= m:
        if m % p == 0:
            out.append(p)
            while m % p == 0:
                m //= p
        p += 1
    if m > 1:
        out.append(m)
    return tuple(out)


def density_constant(d: int, e: int, f: int) -> Fraction:
    """rho_D = (2 zeta(2) D)^-1 prod_{p|D} p/(p+1), as an EXACT symbolic fraction.

    zeta(2) is kept symbolically (pi^2/6 is irrational); the returned value is the
    rational part D^-1 prod p/(p+1), i.e. rho_D * 2*zeta(2).  Callers must scale by
    1/(2 zeta(2)) to get the density.  Zero if the moduli are not pairwise coprime.
    """
    for name, value in (("d", d), ("e", e), ("f", f)):
        _positive_int(value, name)
    if gcd(d, e) != 1 or gcd(d, f) != 1 or gcd(e, f) != 1:
        return Fraction(0)
    D = d * e * f
    prod = Fraction(1)
    for x in (d, e, f):
        for p in _distinct_primes(x):
            prod *= Fraction(p, p + 1)
    return prod / D


def primitive_divisor_count(X: int, d: int, e: int, f: int) -> int:
    """Exact count of primitive triples a+b=c<=X with d|a, e|b, f|c.

    Direct enumeration; independent of the repo's cloud_abc_correlations.py.
    """
    for name, value in (("X", X), ("d", d), ("e", e), ("f", f)):
        _positive_int(value, name)
    if gcd(d, e) != 1 or gcd(d, f) != 1 or gcd(e, f) != 1:
        return 0
    cnt = 0
    for c in range(f, X + 1, f):
        for a in range(1, c):
            b = c - a
            if a % d or b % e:
                continue
            if gcd(a, b) != 1:
                continue
            cnt += 1
    return cnt


def effective_density_error_bound(X: int, d: int, e: int, f: int) -> Fraction:
    """The asserted uniform error bound X*tau(D) + D (exact, integer-valued)."""
    for name, value in (("X", X), ("d", d), ("e", e), ("f", f)):
        _positive_int(value, name)
    D = d * e * f
    return Fraction(X * divisor_count(D) + D)
