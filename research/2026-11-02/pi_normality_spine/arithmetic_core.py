"""π-normality arithmetic core — single source of truth for the SUCC π-frontier primitives.

This module consolidates, in ONE place, the exact arithmetic objects that the entire
base-16 π-normality reduction depends on. Every function returns an exact `Fraction`
(or integer); no floating point enters the arithmetic. The purpose is tractability:
future proof-fronts import these primitives instead of re-deriving and re-verifying them.

Objects (all exact):
  r(n)         — the four-pole BBP forcing.
  U(n)         — the finite rational prefix orbit U_0=0, U_n=16 U_{n-1}+r(n).
  T(n, R)      — the positive Green tail T_n = sum_{j>=1} 16^{-j} r(n+j) (R-truncated).
  a_pj(p, j)   — primary residue a_{p,j} = c_p 16^{j-b_p} mod p.
  W_pj(p, j)   — prime-cofiber W_{p,j} = U_j - a_{p,j}/p (p-integral in the window).
  kappa(p, j)  — hexadecimal carry digit kappa_{p,j} = floor(16 a_{p,j}/p).
  Q_mN(digits, N, m) — collision energy Q_{m,N} (base 16).
  order16(p)   — ord_p(16).

Each is cross-checked against an independent representation in the test suite
(test_arithmetic_core.py), following the repo's dual-certification discipline.

No normality claim. This is scaffolding, not a theorem.
"""
from __future__ import annotations

from fractions import Fraction
from math import gcd


# ---------------------------------------------------------------------------
# Four-pole BBP forcing and orbit
# ---------------------------------------------------------------------------

def r(n: int) -> Fraction:
    """The authentic four-pole BBP forcing r(n) = 4/(8n-7) - 2/(8n-4) - 1/(8n-3) - 1/(8n-2)."""
    assert n >= 1
    return (Fraction(4, 8*n - 7) - Fraction(2, 8*n - 4)
            - Fraction(1, 8*n - 3) - Fraction(1, 8*n - 2))


def r_as_fm(n: int) -> Fraction:
    """Independent representation: r(n) = 2 f_3 + f_4 + f_5, f_m = 1/(8n-7) - 1/(8n-7+m)."""
    f = lambda m: Fraction(1, 8*n - 7) - Fraction(1, 8*n - 7 + m)
    return 2 * f(3) + f(4) + f(5)


def U(n: int) -> Fraction:
    """Finite rational prefix orbit U_n = sum_{j<=n} 16^{n-j} r(j), via the recurrence."""
    u = Fraction(0)
    for j in range(1, n + 1):
        u = 16 * u + r(j)
    return u


def U_direct(n: int) -> Fraction:
    """Independent representation: U_n = sum_{j<=n} 16^{n-j} r(j) (explicit sum)."""
    return sum(Fraction(16 ** (n - j)) * r(j) for j in range(1, n + 1))


def T(n: int, R: int = 64) -> Fraction:
    """Green tail T_n = sum_{j>=1} 16^{-j} r(n+j), truncated at R (upper bound for R<infty)."""
    assert n >= 1
    return sum(Fraction(16 ** (-j)) * r(n + j) for j in range(1, R + 1))


def T_upper_bound(n: int) -> Fraction:
    """Proved upper bound 0 < T_n < 1/(64 n^2) (a fortiori < (8n+1)^-2)."""
    return Fraction(1, 64 * n * n)


# ---------------------------------------------------------------------------
# Prime-cofiber primitives (p = 1 or 5 mod 8, p > 5)
# ---------------------------------------------------------------------------

def birth_index(p: int) -> int:
    """b_p = (p+7)/8 for p=1 mod 8; (p+3)/8 for p=5 mod 8."""
    assert p > 5 and p % 8 in (1, 5)
    return (p + 7) // 8 if p % 8 == 1 else (p + 3) // 8


def primary_coeff(p: int) -> int:
    """c_p = +4 for p=1 mod 8; -1 for p=5 mod 8."""
    return 4 if p % 8 == 1 else -1


def a_pj(p: int, j: int) -> int:
    """Primary residue a_{p,j} = c_p * 16^{j-b_p} mod p (integer in [0,p))."""
    c = primary_coeff(p)
    b = birth_index(p)
    return (c * pow(16, j - b, p)) % p


def kappa(p: int, j: int) -> int:
    """Hexadecimal carry digit kappa_{p,j} = floor(16 a_{p,j}/p) in {0,...,15}."""
    return (16 * a_pj(p, j)) // p


def W_pj(p: int, j: int) -> Fraction:
    """Prime-cofiber W_{p,j} = U_j - a_{p,j}/p (p-integral within the persistence window)."""
    return U(j) - Fraction(a_pj(p, j), p)


def order16(p: int) -> int:
    """Multiplicative order ord_p(16)."""
    assert p > 2
    x = 16 % p
    o = 1
    while x != 1:
        x = (x * 16) % p
        o += 1
        assert o <= p, "order must divide p-1"
    return o


# ---------------------------------------------------------------------------
# Collision energy (the normality certificate)
# ---------------------------------------------------------------------------

def Q_mN(words: list[int], m: int, base: int = 16) -> Fraction:
    """Q_{m,N} = base^m * sum_w p_{m,N}(w)^2, words = list of length-m word values."""
    from collections import Counter
    N = len(words)
    c = Counter(words)
    return Fraction(base ** m * sum(v * v for v in c.values()), N * N)


# ---------------------------------------------------------------------------
# Self-check (run directly)
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    # r = 2 f_3 + f_4 + f_5
    assert all(r(n) == r_as_fm(n) for n in range(1, 200))
    # U recurrence == direct sum
    assert all(U(n) == U_direct(n) for n in range(1, 40))
    # r(n) > 0, decreasing
    assert all(r(n) > 0 for n in range(1, 500))
    assert all(r(n) > r(n + 1) for n in range(1, 200))
    # T_n bound
    assert all(0 < T(n) < T_upper_bound(n) for n in range(1, 100))
    # cofiber p-integrality (p=5 mod 8)
    for p in (13, 29, 37, 53, 61, 101):
        b = birth_index(p)
        for j in range(b, (p + 1) // 2):
            assert W_pj(p, j).denominator % p != 0, (p, j)
    print("arithmetic_core self-check: ALL PASS")
