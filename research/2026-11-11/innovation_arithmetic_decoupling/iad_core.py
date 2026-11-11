#!/usr/bin/env python3
"""Shared exact kernel for the innovation x arithmetic-decoupling dossier.

Everything here is exact rational arithmetic on the frozen four-pole source, or
integer arithmetic on a pi enclosure with a stated error.  No statistical claim
is made by this module.  The canonical forcing is reused from
``observational_succ.selected_orbit.original_forcing`` (never redefined).

Conventions (identical to docs/PI_NORMALITY_FRONTIER.md):
    r(n) = 4/(8n-7) - 2/(8n-4) - 1/(8n-3) - 1/(8n-2),  U_0 = 0,
    U_n = 16 U_(n-1) + r(n),  T_n = sum_{j>=1} 16^-j r(n+j),
    Y_n = U_n + T_n = 16^n x,  x = pi/16.
"""
from __future__ import annotations

import sys
from fractions import Fraction
from functools import lru_cache
from pathlib import Path

import mpmath as mp

_ROOT = Path(__file__).resolve().parents[3]
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

from observational_succ.selected_orbit import original_forcing  # noqa: E402

GUARD_HEX = 48  # guard hexadecimal digits behind every certified fractional part


def r(n: int) -> Fraction:
    """The immutable four-pole forcing (exact)."""
    return original_forcing(n)


def neg_r_prime(t: Fraction) -> Fraction:
    """Exact -r'(t) for rational t > 7/8."""
    t = Fraction(t)
    return (Fraction(32) / (8 * t - 7) ** 2 - Fraction(16) / (8 * t - 4) ** 2
            - Fraction(8) / (8 * t - 3) ** 2 - Fraction(8) / (8 * t - 2) ** 2)


def r_real(t: Fraction) -> Fraction:
    """Exact r(t) for rational t > 7/8 (real-variable interpolation)."""
    t = Fraction(t)
    return (Fraction(4) / (8 * t - 7) - Fraction(2) / (8 * t - 4)
            - Fraction(1) / (8 * t - 3) - Fraction(1) / (8 * t - 2))


class Source:
    """Exact zero-seed source states U_0..U_N as Fractions."""

    def __init__(self, horizon: int):
        if type(horizon) is not int or horizon < 1:
            raise ValueError("horizon must be a positive integer")
        self.N = horizon
        U = [Fraction(0)]
        for n in range(1, horizon + 1):
            U.append(16 * U[-1] + r(n))
        self.U = U

    def innovation(self, n: int, lag: int) -> Fraction:
        """Delta_lag(n) = U_(n+lag) - 16^lag U_n (exact, seed independent)."""
        return self.U[n + lag] - 16 ** lag * self.U[n]

    def innovation_direct(self, n: int, lag: int) -> Fraction:
        """Independent route: sum_{j=1}^{lag} 16^(lag-j) r(n+j)."""
        return sum((16 ** (lag - j) * r(n + j) for j in range(1, lag + 1)), Fraction(0))

    def U_seed(self, n: int, seed: Fraction) -> Fraction:
        """U_n(s) = U_n(0) + 16^n s for a rational seed."""
        return self.U[n] + 16 ** n * Fraction(seed)


def tail_interval(n: int, depth: int = 40) -> tuple[Fraction, Fraction]:
    """Rational enclosure T_lo < T_n < T_hi from the source alone (no pi oracle)."""
    lo = sum((Fraction(r(n + j), 16 ** j) for j in range(1, depth + 1)), Fraction(0))
    hi = lo + Fraction(r(n + depth + 1), 15 * 16 ** depth)
    return lo, hi


@lru_cache(maxsize=8)
def _x_scaled(hex_digits: int) -> int:
    """floor(x * 16^hex_digits) for x = pi/16, by mpmath at ample precision."""
    with mp.workdps(int(hex_digits * 1.2042) + 80):
        return int(mp.floor(mp.pi / 16 * mp.mpf(16) ** hex_digits))


class CompletedOrbit:
    """Certified fractional parts of Y_n(s) = 16^n (a + b x), a, b rational.

    ``frac(n)`` returns a Fraction f with f <= {Y_n} < f + err, err = 16^-GUARD_HEX
    (times the integer scale of b), computed by integer arithmetic on
    floor(x 16^M).  ``a = 0, b = 1`` is the true seed; ``b = 0`` is a rational
    completed point (periodic controls); ``a = 0, b = 0`` is the coherent seed
    s = -x (completed orbit identically zero).
    """

    def __init__(self, horizon: int, a: Fraction = Fraction(0), b: Fraction = Fraction(1)):
        self.N = horizon
        self.a, self.b = Fraction(a), Fraction(b)
        self.M = horizon + GUARD_HEX
        self.X = _x_scaled(self.M)

    def frac(self, n: int) -> Fraction:
        if not 0 <= n <= self.N:
            raise ValueError("n outside certified horizon")
        # 16^n (a + b x) with x in [X, X+1)/16^M ; exact rational lower endpoint
        y = 16 ** n * (self.a + self.b * Fraction(self.X, 16 ** self.M))
        return y - (y.numerator // y.denominator)

    def frac_error(self) -> Fraction:
        return abs(self.b) * Fraction(1, 16 ** GUARD_HEX)

    def floor(self, n: int) -> int:
        y = 16 ** n * (self.a + self.b * Fraction(self.X, 16 ** self.M))
        return y.numerator // y.denominator


def e(t) -> complex:
    """e(t) = exp(2 pi i t) for a Fraction or float t (reduced mod 1 exactly first)."""
    if isinstance(t, Fraction):
        t = t - (t.numerator // t.denominator)
        with mp.workdps(40):
            z = mp.expjpi(2 * (mp.mpf(t.numerator) / t.denominator))
            return complex(z)
    with mp.workdps(40):
        return complex(mp.expjpi(2 * mp.mpf(t)))


def dist_to_int(t: Fraction) -> Fraction:
    f = t - (t.numerator // t.denominator)
    return min(f, 1 - f)


def p_adic_component(q: Fraction, p: int) -> Fraction:
    """The class of q in Q_p/Z_p as a rational in [0,1) with p-power denominator."""
    q = Fraction(q)
    d, k = q.denominator, 0
    while d % p == 0:
        d //= p
        k += 1
    if k == 0:
        return Fraction(0)
    pk = p ** k
    # q = a/(p^k d): component = (a * d^{-1} mod p^k)/p^k
    return Fraction((q.numerator * pow(d, -1, pk)) % pk, pk)


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


def births_at(m: int) -> list[tuple[int, str, Fraction]]:
    """Odd primes p >= 7 born at source time m, with their pole and coefficient c
    (the birth term is c/p).  beta(p) = (p+7)/8, (p+3)/8, (p+1)/4 by class."""
    out = []
    for p, pole, c in ((8 * m - 7, "8m-7", Fraction(4)), (8 * m - 3, "8m-3", Fraction(-1)),
                       (4 * m - 1, "4m-1", Fraction(-1, 2))):
        if p >= 7 and is_prime(p):
            out.append((p, pole, c))
    return out
