"""Unconditional Mellin-functional lower bound on the residue-clock L2 error.

The cell Mellin functional  L_s(f) = int_0^1 f(x) x^{s-1} dx  is bounded on
the weighted cell space ell^2(w), w_k = 1/(k(k+1)), iff Re(s) > 1/2 (classical;
the summands of ||L_s||^2 behave like k^{-2Re(s)}).  For INTEGER s >= 2 it is
therefore bounded, and Cauchy-Schwarz gives an UNCONDITIONAL lower bound on the
approximation error e = 1 - sum_n a_n r_n:

    ||e||  >=  |L_s(e)| / ||L_s||

with  L_s(1) = 1/s  and  L_s(r_n) = (zeta(s)/s)(1/n - n^{-s})  (ZCR-02),
and  ||L_s||^2 = (1/s^2) sum_k (k^{-s} - (k+1)^{-s})^2 k(k+1)  (rational series).

Unlike the ZCR-03 obstruction this needs NO nontrivial zero: it uses only the
bounded functional at s >= 2.  All quantities are certified by rational
interval arithmetic (zeta(s) enclosed by series truncation with a telescoping
tail bound).  It is a different, analytic mechanism from the combinatorial
periodicity/blackout enclosures, and it is weaker than the exact computation
(as a single functional sees only one direction) -- which is exactly the point:
it is rigorous and zero-independent, not a fit.

No zeta zero location, Gamma, pole or Weil kernel is used.
"""
from __future__ import annotations

from fractions import Fraction as Q

from .periodic_tail_enclosure import residue, PeriodicTailError


def _int(x, lo, hi):
    if type(x) is not int or not lo <= x <= hi:
        raise PeriodicTailError(f"expected integer in [{lo},{hi}]")
    return x


def zeta_enclosure(s: int, N: int = 256) -> tuple[Q, Q]:
    """[lo, hi] enclosing zeta(s) = sum_{k>=1} k^{-s} for integer s >= 2.

    Tail bound: sum_{k>N} k^{-s} < 1/((s-1) N^{s-1})  (integral comparison).
    """
    s = _int(s, 2, 64); N = _int(N, 2, 4096)  # N <= 4096: denominators stay < 4300 digits
    partial = sum((Q(1, k) ** s for k in range(1, N + 1)), Q())
    tail = Q(1, (s - 1) * (N ** (s - 1)))
    return partial, partial + tail


def functional_norm2_enclosure(s: int, N: int = 256) -> tuple[Q, Q]:
    """[lo, hi] enclosing ||L_s||^2 = (1/s^2) sum_k (k^{-s}-(k+1)^{-s})^2 k(k+1).

    Tail bound: (k^{-s}-(k+1)^{-s})^2 k(k+1) < 2 s^2 / k^{2s} for k >= 1, so
    the remainder is < 2 s^2 / ((2s-1) N^{2s-1}).
    """
    s = _int(s, 2, 64); N = _int(N, 2, 4096)
    partial = sum(
        ((Q(1, k) ** s - Q(1, k + 1) ** s) ** 2 * Q(k * (k + 1), 1)
         for k in range(1, N + 1)), Q())
    partial /= (s * s)
    tail = Q(2 * s * s, (2 * s - 1) * (N ** (2 * s - 1))) / (s * s)
    return partial, partial + tail


def _linear_abs_min(c0: Q, c1: Q, x_lo: Q, x_hi: Q) -> Q:
    """Rigorous lower bound on |c0 + c1*x| for x in [x_lo, x_hi] (c0,c1 rationals).

    The linear form c0 + c1*x is monotone in x; its |.| min over the interval
    is at an endpoint, or 0 if it crosses zero in between.
    """
    f_lo = c0 + c1 * x_lo
    f_hi = c0 + c1 * x_hi
    if (f_lo >= 0 and f_hi >= 0) or (f_lo <= 0 and f_hi <= 0):
        return min(abs(f_lo), abs(f_hi))
    return Q(0)  # crosses zero: no positive lower bound from this functional


def mellin_lower_bound(a: dict[int, Q], s: int = 2, N: int = 256) -> dict:
    """Rigorous rational lower bound on ||1 - sum a_n r_n||_2 via the L_s functional.

    L_s(e) = 1/s - (zeta(s)/s) * A_s  with  A_s = sum_n a_n (1/n - n^{-s}).
    Since this is linear in zeta(s) and zeta(s) is enclosed, |L_s(e)| is
    lower-bounded exactly, then divided by the upper bound on ||L_s||.
    """
    s = _int(s, 2, 64)
    if not a or any(type(c) not in (int, Q) for c in a.values()):
        raise PeriodicTailError("nonempty exact-rational coefficient family required")
    for n, c in a.items():
        _int(n, 2, 1_000_000)
    A = sum((Q(c) * (Q(1, n) - Q(1, n) ** s) for n, c in a.items()), Q())
    z_lo, z_hi = zeta_enclosure(s, N)
    n2_lo, n2_hi = functional_norm2_enclosure(s, N)
    # L_s(e) = 1/s - (zeta(s)/s) * A = (1/s) - (A/s) * zeta(s)
    c0 = Q(1, s)
    c1 = -A / s
    L_lo = _linear_abs_min(c0, c1, z_lo, z_hi)
    norm2_hi = n2_hi  # ||L_s|| <= sqrt(norm2_hi)
    if norm2_hi <= 0:
        raise ArithmeticError("nonpositive functional norm enclosure")
    # ||e|| >= |L_s(e)| / ||L_s|| >= L_lo / sqrt(norm2_hi).
    # sqrt(norm2_hi) = sqrt(p/q) = sqrt(p q)/q  <  M/q  with M = isqrt(p q)+1,
    # so 1/sqrt(norm2_hi) > q/M and the rigorous rational lower bound is L_lo * q / M.
    import math
    p, q = norm2_hi.numerator, norm2_hi.denominator
    M = math.isqrt(p * q) + 1               # M > sqrt(p q) strictly
    lower = Q(L_lo.numerator * q, L_lo.denominator * M)
    return {
        "s": s,
        "A_s": str(A),
        "zeta_s_interval": [str(z_lo), str(z_hi)],
        "norm2_Ls_interval": [str(n2_lo), str(n2_hi)],
        "|L_s(e)|_lower": str(L_lo),
        "lower_bound_on_norm_e": str(lower),
        "unconditional": True,
        "zero_independent": True,
        "RH_proved": False,
    }
