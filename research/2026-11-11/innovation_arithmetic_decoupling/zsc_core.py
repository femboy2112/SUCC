#!/usr/bin/env python3
"""Exact kernel for the zero-selected-carry continuation (CARRY_FLUX.md, ZSC-01..07).

Reuses the frozen forcing through ``iad_core`` (never redefined).  Everything that
decides a theorem-grade check is exact rational or integer arithmetic; floating
point is used only to evaluate e(t) after exact reduction modulo one, with a stated
tolerance in the probe.  No statistical claim is made by this module.
"""
from __future__ import annotations

import cmath
import math
import sys
from fractions import Fraction
from pathlib import Path

_HERE = Path(__file__).resolve().parent
if str(_HERE) not in sys.path:
    sys.path.insert(0, str(_HERE))

import iad_core as ic  # noqa: E402

F = Fraction
TRUNC = 40                      # hexadecimal digits kept behind every fractional part
G_PI = (4, 0, 0, -2, -1, -1)    # g_pi(z) = 4 - 2z^3 - z^4 - z^5
G_NULL = (8, -8, -4, -8, -2, -2, 1)                     # g_0 = K(z)(z^2 - 4z + 2)
G_HOSTILE = (56, -40, -4, -8, -2, -2, 1, 0, -3, 2)      # g_H = (16 - z^8)(3 - 2z) + g_0
A_PI = (4, 0, 0, -2, -1, -1, 0, 0)
A_NULL = (8, -8, -4, -8, -2, -2, 1, 0)


# ---------------------------------------------------------------- digit strings
def pi_digits(n_digits: int) -> list[int]:
    """d_0 .. d_(n_digits-1) of x = pi/16 (x = 0.d_0 d_1 ...), route (i): mpmath enclosure."""
    M = n_digits + ic.GUARD_HEX
    X = ic._x_scaled(M)
    return [(X >> (4 * (M - 1 - n))) & 15 for n in range(n_digits)]


def frac_from_digits(d: list[int], n: int) -> Fraction:
    """{16^n xi} truncated to TRUNC hexadecimal digits (error in [0, 16^-TRUNC))."""
    acc = 0
    for i in range(TRUNC):
        acc = 16 * acc + d[n + i]
    return F(acc, 16 ** TRUNC)


def e_of(t: Fraction) -> complex:
    t = t - (t.numerator // t.denominator)
    return cmath.exp(2j * math.pi * (t.numerator / t.denominator))


def shell_mean(fracs, B: int, h: int) -> complex:
    """(1/B) sum_{n=B}^{2B-1} e(h * fracs(n)); ``fracs`` maps n to a Fraction."""
    return sum(e_of(h * fracs(n)) for n in range(B, 2 * B)) / B


def dist15(t: Fraction) -> Fraction:
    return ic.dist_to_int(15 * t)


def changes(d: list[int], lo: int, hi: int) -> int:
    return sum(1 for n in range(lo, hi) if d[n] != d[n + 1])


def run_length(d: list[int], n: int, cap: int) -> int:
    L = 1
    while L < cap and d[n + L] == d[n]:
        L += 1
    return L


# ---------------------------------------------------------------- witnesses (ZSC-01, ZSC-05)
def w1_digits(length: int) -> list[int]:
    d = [0] * length
    a = 16
    while a < length:
        d[a] = 1
        a = a + math.isqrt(a - 1) + 1 + 1          # ceil(sqrt(a)) = isqrt(a-1)+1
    return d


def w2_digits(length: int) -> list[int]:
    d = [15] * length
    b = 2
    while b < length:
        d[b] = 14
        b = b * b
    return d


def w3_digits(length: int) -> list[int]:
    d, k = [], 1
    while len(d) < length:
        d += [0] * k + [1 + (i % 2) for i in range(k)]
        k += 1
    return d[:length]


def xi_lambda_digits(lam: Fraction, length: int) -> list[int]:
    d = [7] * length
    k = 1
    while 2 ** k < length:
        for n in range(2 ** k, min(length, 2 ** k + (lam * 2 ** k).__floor__())):
            d[n] = 0
        k += 1
    return d


def shallit_digits(length: int) -> list[int]:
    """K = sum_{k>=0} 16^(-2^k) = 0.d_0 d_1 ... with d_n = 1 iff n+1 is a power of two."""
    d = [0] * length
    p = 1
    while p - 1 < length:
        d[p - 1] = 1
        p *= 2
    return d


def periodic_digits(block: list[int], length: int) -> list[int]:
    return [block[i % len(block)] for i in range(length)]


# ---------------------------------------------------------------- sources (ZSC-03, ZSC-06)
def forcing(g: tuple, n: int) -> Fraction:
    """r_g(n) = sum_i g_i / (8n - 7 + i)."""
    return sum((F(c, 8 * n - 7 + i) for i, c in enumerate(g) if c), F(0))


class GSource:
    """Exact states of the source (g, seed): U_0 = seed, U_n = 16 U_(n-1) + r_g(n)."""

    def __init__(self, g: tuple, horizon: int, seed=F(0)):
        self.g, self.N = tuple(g), horizon
        U = [F(seed)]
        for n in range(1, horizon + 1):
            U.append(16 * U[-1] + forcing(self.g, n))
        self.U = U

    def carries(self) -> list:
        """kappa_1 .. kappa_N as a list indexed by n (entry 0 is None)."""
        C = [u.numerator // u.denominator for u in self.U]
        return [None] + [C[n] - 16 * C[n - 1] for n in range(1, self.N + 1)]

    def frac(self, n: int) -> Fraction:
        u = self.U[n]
        return u - (u.numerator // u.denominator)


def gauge_a(h: tuple, n: int) -> Fraction:
    """a(n) = int_0^1 z^(8n) h(z) dz for h = sum h_i z^i."""
    return sum((F(c, 8 * n + 1 + i) for i, c in enumerate(h) if c), F(0))


def gauge_transform(g: tuple, h: tuple) -> tuple:
    """Coefficients of g - (16 - z^8) h."""
    out = [F(0)] * max(len(g), len(h) + 8)
    for i, c in enumerate(g):
        out[i] += c
    for i, c in enumerate(h):
        out[i] -= 16 * F(c)
        out[i + 8] += F(c)
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return tuple(out)


def proper_form(g: tuple, seed=F(0)) -> tuple:
    """Reduce (g, seed) to the unique gauge-equivalent pair with deg g <= 7."""
    g = [F(c) for c in g]
    seed = F(seed)
    while len(g) > 8:
        c, i = g[-1], len(g) - 1 - 8       # leading term c z^(i+8): use h = -c z^i
        # g - (16 - z^8) h with h = -c z^i  ->  g + 16 c z^i - c z^(i+8); seed += int h = -c/(i+1)
        g[i] += 16 * c
        g.pop()
        seed -= c / (i + 1)
        while len(g) > 1 and g[-1] == 0:
            g.pop()
    return tuple(g) + (F(0),) * (8 - len(g)), seed


def renewal_J(n: int, r=ic.r) -> int:
    """J(n) = floor(log_16(15 / (16 r(n+1)))): largest j >= 0 with (16/15) 16^j r(n+1) <= 1."""
    j, v = 0, F(16, 15) * r(n + 1)
    if v > 1:
        return -1
    while 16 * v <= 1:
        v *= 16
        j += 1
    return j


def seam_bits(S_U: list, n_max: int, seed_shift=None, depth: int = 60) -> list[int]:
    """eps_n = 1 iff {U_n} >= 1 - T_n, decided by a rational enclosure of T_n (authentic tail)."""
    out = []
    for n in range(n_max + 1):
        u = S_U[n]
        gap = 1 - (u - (u.numerator // u.denominator))       # 1 - {U_n} in (0, 1]
        lo, hi = ic.tail_interval(n, depth)
        if gap <= lo:
            out.append(1)
        elif gap > hi:
            out.append(0)
        else:
            raise RuntimeError(f"seam undecidable at n={n}")
    return out


def forced_seam_seed(S: "ic.Source", k: int, a: int) -> Fraction:
    """Rational seed whose completed orbit has {Y_k} in (theta, theta + 16^-40): a seam run of
    length about a starting at k (theta = 16^-(a+3) / (8(k+a)+2)^2)."""
    lo, _ = ic.tail_interval(k, 60)
    theta = F(1, 16 ** (a + 3) * (8 * (k + a) + 2) ** 2)
    target_gap = lo - theta                                   # want 1 - {U_k(s)} = target_gap
    u = S.U[k]
    return (-(u - (u.numerator // u.denominator)) + 1 - target_gap) / 16 ** k


# ---------------------------------------------------------------- Baker conditions (ZSC-06e)
def _mul(a, b):
    a0, a1, a2, a3 = a
    b0, b1, b2, b3 = b
    return (a0 * b0 + 2 * a1 * b1 - a2 * b2 - 2 * a3 * b3, a0 * b1 + a1 * b0 - a2 * b3 - a3 * b2,
            a0 * b2 + a2 * b0 + 2 * a1 * b3 + 2 * a3 * b1, a0 * b3 + a3 * b0 + a1 * b2 + a2 * b1)


_ROOTS = {  # the eight roots of z^8 = 16 in the basis (1, sqrt2, i, i*sqrt2) of Q(sqrt2, i)
    "s": (0, 1, 0, 0), "-s": (0, -1, 0, 0), "is": (0, 0, 0, 1), "-is": (0, 0, 0, -1),
    "1+i": (1, 0, 1, 0), "1-i": (1, 0, -1, 0), "-1+i": (-1, 0, 1, 0), "-1-i": (-1, 0, -1, 0)}
_CONDITIONS = (  # coefficients of l_4, l_6, l_5, l_7, l_2, l_3, l_1 in -128 L(A)
    ((1, "-s"), (-1, "s")), ((1, "is"), (-1, "-is")), ((1, "1+i"), (-1, "1-i")),
    ((1, "-1+i"), (-1, "-1-i")), ((1, "is"), (1, "-is")), ((1, "-1+i"), (1, "-1-i")),
    tuple((1, k) for k in _ROOTS))


def baker_matrix() -> list[list[Fraction]]:
    pw = {}
    for k, a in _ROOTS.items():
        a = tuple(F(c) for c in a)
        p, lst = (F(1), F(0), F(0), F(0)), []
        for _ in range(8):
            p = _mul(p, a)
            lst.append(p)
        assert lst[7] == (16, 0, 0, 0), k
        pw[k] = lst
    rows = []
    for cond in _CONDITIONS:
        block = [[F(0)] * 8 for _ in range(4)]
        for c, k in cond:
            for j in range(8):
                for comp in range(4):
                    block[comp][j] += c * pw[k][j][comp]
        rows += block
    return rows


def rank_and_kernel(rows: list[list[Fraction]]) -> tuple[int, list[list[Fraction]]]:
    M = [list(r) for r in rows]
    ncol, piv, r = len(M[0]), [], 0
    for c in range(ncol):
        p = next((i for i in range(r, len(M)) if M[i][c] != 0), None)
        if p is None:
            continue
        M[r], M[p] = M[p], M[r]
        M[r] = [v / M[r][c] for v in M[r]]
        for i in range(len(M)):
            if i != r and M[i][c] != 0:
                M[i] = [v - M[i][c] * w for v, w in zip(M[i], M[r])]
        piv.append(c)
        r += 1
    kernel = []
    for free in (c for c in range(ncol) if c not in piv):
        v = [F(0)] * ncol
        v[free] = F(1)
        for i, c in enumerate(piv):
            v[c] = -M[i][free]
        kernel.append(v)
    return r, kernel


def baker_rank() -> tuple[int, list[list[Fraction]]]:
    return rank_and_kernel(baker_matrix())


def L_enclosure(A: tuple, terms: int = 60) -> tuple[Fraction, Fraction]:
    """Rational enclosure of L(A) = sum_j A_j sum_{k>=0} 16^(-k-1)/(8k+j)."""
    s = sum((F(A[j - 1], 16 ** (k + 1) * (8 * k + j)) for k in range(terms) for j in range(1, 9)),
            F(0))
    err = F(sum(abs(c) for c in A), 15 * 16 ** terms * (8 * terms + 1))
    return s - err, s + err
