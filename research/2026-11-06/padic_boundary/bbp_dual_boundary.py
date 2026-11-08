"""Pure-Python exact source probes for the SUCC real/2-adic BBP dual-boundary dossier.

All calculations are over fractions or Z/(2^k). The 2-adic log proof is in
THEOREMS.md; no finite modular probe is used as a substitute for that proof.
"""
from __future__ import annotations
from fractions import Fraction


def source(z: int) -> Fraction:
    """The genuine four signed poles, continued to every integer z."""
    if type(z) is not int:
        raise TypeError("integer clock required")
    a = 120*z*z - 89*z + 16
    d = (2*z-1)*(4*z-1)*(8*z-7)*(8*z-3)
    return Fraction(a,d)


def four_pole(z: int) -> Fraction:
    return (Fraction(4, 8*z-7) - Fraction(2, 8*z-4)
            - Fraction(1, 8*z-3) - Fraction(1, 8*z-2))


def first_pole_mutant(z: int) -> Fraction:
    return source(z) + Fraction(1, 8*z-7)


def h(z: int) -> Fraction:
    return Fraction(z, (2*z-1)**4)


def coboundary_mutant(z: int) -> Fraction:
    return source(z) + h(z) - 16*h(z-1)


def isometric_coboundary_mutant(z: int) -> Fraction:
    """Mutant that preserves zero real/2-adic boundaries AND Z2 isometry."""
    return source(z) + 2*h(z) - 32*h(z-1)


def shadow_source(z: int) -> Fraction:
    """Hostile: Z2-isometric and zero-starting, but real phase tends to zero."""
    return h(z) - 16*h(z-1)


def mod_fraction(x: Fraction, bits: int) -> int:
    if bits < 1:
        raise ValueError("bits must be positive")
    m = 1 << bits
    q = Fraction(x)
    if q.denominator % 2 == 0:
        raise ValueError("fraction denominator is even, not in Z2")
    return (q.numerator * pow(q.denominator, -1, m)) % m


def v_mod(z: int, bits: int, r=source) -> int:
    """Exact value of convergent V(z)=sum_j>=0 16^j r(z-j) modulo 2^bits."""
    m = 1 << bits
    v = 0
    p = 1
    for j in range((bits+3)//4):
        v = (v + p*mod_fraction(r(z-j), bits)) % m
        p = (16*p) % m
    return v


def u_mod(n: int, bits: int, seed: Fraction = Fraction(0), r=source) -> int:
    """Direct forward recurrence, independent of v_mod expansion."""
    if n < 0: raise ValueError("n>=0 required")
    m = 1 << bits
    u = mod_fraction(Fraction(seed), bits)
    for j in range(1,n+1):
        u = (16*u + mod_fraction(r(j),bits))%m
    return u


def u_exact(n: int, seed: Fraction = Fraction(0), r=source) -> Fraction:
    """Exact rational forward recurrence; full unwrapped state."""
    if n < 0: raise ValueError("n>=0 required")
    u = Fraction(seed)
    for j in range(1,n+1):
        u = 16*u + r(j)
    return u


def valuation_two(q: Fraction) -> int:
    q = Fraction(q)
    if q == 0: raise ValueError("v2(0) is infinite")
    def v(x):
        x=abs(x)
        return (x & -x).bit_length()-1
    return v(q.numerator) - v(q.denominator)


def odd_branch(m: int, times: int) -> int:
    if m % 2 != 1 or times < 0:
        raise ValueError("odd m and nonnegative number of steps required")
    for _ in range(times):m=2*m+1
    return m
