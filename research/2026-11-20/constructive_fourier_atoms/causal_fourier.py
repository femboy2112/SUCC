"""Finite source-authenticated constructive Fourier atoms for SUCC.

This module is pure standard-library mathematics. All arithmetic sources are
explicit; it never claims a Weyl saving, π-normality, RH, or physical energy.

Original BBP source: four signed poles, literal zero initial seed.
Source-time Fourier and 3/5 clock Fourier are intentionally different probes
from the completed real-circle Fourier/Weyl observable.
"""

from __future__ import annotations

import cmath
import math
from fractions import Fraction
from collections.abc import Sequence

RADIX = 16
POLES = (7, 4, 3, 2)
COEFFICIENTS = (4, -2, -1, -1)


def forcing(n: int) -> Fraction:
    """Original signed BBP r(n), unchanged."""
    if type(n) is not int or n < 1:
        raise ValueError("n must be a positive integer")
    return sum((Fraction(c, 8*n - b) for c, b in zip(COEFFICIENTS, POLES)), Fraction(0))


def mutant_forcing(n: int) -> Fraction:
    """SOURCE-INVALID matched-first-Mellin-jet Q* = Q+(1-t)^2."""
    a = 8*n - 7
    return forcing(n) + Fraction(2, a*(a+1)*(a+2))


def source_coefficient(n: int) -> Fraction:
    return forcing(n) / RADIX**n


def clock(n: int, radix: int = RADIX) -> int:
    """Exact geometric clock J_n=(radix**n-1)/(radix-1)."""
    if type(n) is not int or n < 0 or type(radix) is not int or radix < 2:
        raise ValueError("invalid clock or radix")
    return (radix**n - 1) // (radix-1)


def valuation_integer(x: int, p: int) -> int:
    if type(x) is not int or x == 0 or type(p) is not int or p < 2:
        raise ValueError("nonzero integer and prime >=2 required")
    n, v = abs(x), 0
    while n % p == 0:
        v += 1
        n //= p
    return v


def clock_label(value: int, p: int, k: int, radix: int = RADIX) -> int:
    """Finite p-adic clock inverse n mod p**k via a complete exact table.

    Only use for the authenticated geometric odometer p=3 or p=5.
    This is a finite calibration, not an efficient general p-adic logarithm.
    """
    if p not in (3, 5) or k < 1 or radix != 16:
        raise ValueError("supported clock: original radix 16, p=3 or 5")
    mod = p**k
    lookup = {clock(n) % mod: n for n in range(mod)}
    if len(lookup) != mod:
        raise ArithmeticError("finite clock failed bijectivity")
    return lookup[value % mod]


def clock_character(p: int, k: int, a: int, value: int) -> complex:
    """Eigencharacter of the 3/5 clock successor, using exact discrete log."""
    q = p**k
    n = clock_label(value, p, k)
    return cmath.exp(2j*math.pi*((a*n) % q)/q)


def additive_state_character(p: int, k: int, a: int, value: int) -> complex:
    """Ordinary additive character of the p-power state coordinate J."""
    if p not in (3,5) or k < 1:
        raise ValueError("supported p=3,5; k>=1")
    q=p**k
    return cmath.exp(2j*math.pi*((a*value)%q)/q)


def clock_to_state_fourier_change(p: int, k: int) -> list[list[complex]]:
    """Unitary basis change: causal odometer eigenmodes vs additive J modes.

    Matrix C[a][b] = q^-1 Σ_(j mod q) χ_a(J_j) overline(ψ_b(J_j)).
    Each is an orthonormal Fourier basis, related by the permutation n->J_n.
    """
    if p not in (3,5) or k < 1:
        raise ValueError("supported p=3,5; k>=1")
    q=p**k
    J=[clock(n)%q for n in range(q)]
    return [[sum((cmath.exp(2j*math.pi*((a*n-b*J[n])%q)/q)
                  for n in range(q)), 0j)/q
             for b in range(q)] for a in range(q)]


def character(x: Fraction | int | float, h: int = 1) -> complex:
    """Circle character of a rational real lift, reduced before float."""
    if isinstance(x, (Fraction, int)):
        y = (Fraction(x)*h) % 1
        return cmath.exp(2j*math.pi*float(y))
    return cmath.exp(2j*math.pi*h*x)


def state(n: int, seed: Fraction = Fraction(0), mutant: bool = False) -> Fraction:
    """Unwrapped source recurrence U_0=seed, U_(n+1)=16U_n+r(n+1)."""
    if type(n) is not int or n < 0:
        raise ValueError("clock must be nonnegative")
    r = mutant_forcing if mutant else forcing
    u = Fraction(seed)
    for j in range(1, n+1):
        u = 16*u + r(j)
    return u


def source_prefix(M: int) -> Fraction:
    if type(M) is not int or M < 0:
        raise ValueError("terminal must be nonnegative")
    return sum((source_coefficient(j) for j in range(1, M+1)), Fraction(0))


def finite_tail(n: int, M: int) -> Fraction:
    if not (type(n) is int and type(M) is int and 0 <= n <= M):
        raise ValueError("require 0 <= n <= M")
    return sum((Fraction(forcing(j), RADIX**(j-n)) for j in range(n+1, M+1)), Fraction(0))


def completed_terminal(n: int, M: int, seed: Fraction = Fraction(0)) -> Fraction:
    return state(n, seed) + finite_tail(n, M)


def affine_causal_atom(terms: Sequence[Fraction], h: int = 1,
                       seed: Fraction = Fraction(0)) -> complex:
    """Covariant source Fourier atom product, with frequency transport.

    exp(2πih(16**n seed+Σ_1^n 16**(n-j)r_j))
      = exp(2πih16**n seed)*Π exp(2πih16**(n-j)r_j).
    """
    n = len(terms)
    z = character(Fraction(seed)*16**n, h)
    for j, pulse in enumerate(terms, 1):
        z *= character(Fraction(pulse)*16**(n-j), h)
    return z


def source_time_fourier(omega: float, terms: int = 20,
                        mutant: bool = False) -> complex:
    """Finite F(ω)=Σ16^-n r(n) exp(iωn); NOT an orbital Weyl sum."""
    if type(terms) is not int or terms < 1:
        raise ValueError("terms >=1")
    r = mutant_forcing if mutant else forcing
    return sum((float(r(n)/16**n)*cmath.exp(1j*omega*n)
                for n in range(1, terms+1)), 0j)


def finite_source_mass(terms: int) -> Fraction:
    return source_prefix(terms)


def finite_source_time_gap_lower(omega: float) -> float:
    """Exact coefficient 2*c1*c2 times (1-cos omega), approximate trig."""
    return float(2*source_coefficient(1)*source_coefficient(2))*(1-math.cos(omega))


def source_time_gap_constant() -> Fraction:
    return 2*source_coefficient(1)*source_coefficient(2)


def phase_from_terminal(n: int, M: int, h: int = 1) -> complex:
    """Exact rational terminal phase via all source terms in one product."""
    if not (0 <= n <= M):
        raise ValueError("require 0 <= n <= M")
    return character(RADIX**n*source_prefix(M), h)


def terminal_shell_error_bound(B: int, h: int = 1) -> float:
    """Uniform complex-phase error for M=2B and n in [B,2B).

    |theta_n - 16**n P_(2B)|_T < 1/(4096 B²), using
    T_(2B)<r(2B+1)/15<1/[64(2B)²].
    """
    if type(B) is not int or B < 1:
        raise ValueError("B must be positive")
    return 2*math.pi*abs(h)/(4096*B*B)


def affine_swap_defect(a: Fraction, b: Fraction, radix: int = RADIX) -> Fraction:
    """L_b o L_a - L_a o L_b for L_a(u)=radix*u+a."""
    return Fraction(radix-1)*(Fraction(a)-Fraction(b))


def finite_shell_character(B: int, M: int, h: int = 1,
                           seed: Fraction = Fraction(0)) -> complex:
    """Finite terminal rational phase mean on chronological shell."""
    if not (1 <= B and M >= 2*B):
        raise ValueError("M >=2B, B>=1")
    endpoint = source_prefix(M) + Fraction(seed)
    return sum((character(16**n*endpoint,h) for n in range(B,2*B)),0j)/B