#!/usr/bin/env python3
"""Exact kernel for LIMIT_FACES.md (LMF-01..06).

Everything that decides a theorem-grade check is exact rational or integer
arithmetic.  Measures are finitely supported rational measures on the closed
interval [0, 1] with the ordinary interval cost |u - v| (the convention of
docs/PI_NORMALITY_FRONTIER.md section 5); the endpoint 1 is a legal atom, because
shell measures of an orbit on [0, 1) can accumulate there (digits F F F ...).

The frozen four-pole forcing is reused through ``iad_core`` and never redefined.
No statistical claim is made by this module.
"""
from __future__ import annotations

import sys
from fractions import Fraction
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_ZSC = _HERE.parents[1] / "2026-11-11" / "innovation_arithmetic_decoupling"
for _p in (_HERE, _ZSC):
    if str(_p) not in sys.path:
        sys.path.insert(0, str(_p))

import iad_core as ic  # noqa: E402
import zsc_core as zc  # noqa: E402

F = Fraction
TRUNC = zc.TRUNC                       # 40 hexadecimal digits behind every fractional part
SCALE = 16 ** TRUNC

W1_FIX = F(1, 60)                      # min W_1(nu, Lebesgue) over nu on the sixteen points j/15
D_FIX = F(1, 60)                       # min W_1(nu, C nu)      over the same simplex
W1_FIX15 = F(4, 225)                   # the same minimum if the endpoint 1 is (wrongly) forbidden
G_MAX = F(15, 32)                      # max of W_1(nu, C nu); value at the coherent control delta_0
M_STAR = (F(1, 30),) + (F(1, 15),) * 14 + (F(1, 30),)   # the optimal masses on j/15, j = 0..15


# ---------------------------------------------------------------- finitely supported measures
def normalize(atoms) -> list[tuple[Fraction, Fraction]]:
    """Sorted list of (position, mass) with merged positions and zero masses removed."""
    acc: dict[Fraction, Fraction] = {}
    for p, m in atoms:
        p, m = F(p), F(m)
        if not 0 <= p <= 1:
            raise ValueError("atom outside [0, 1]")
        if m < 0:
            raise ValueError("negative mass")
        if m:
            acc[p] = acc.get(p, F(0)) + m
    return sorted(acc.items())


def total_mass(atoms) -> Fraction:
    return sum((m for _, m in atoms), F(0))


def fix16(masses) -> list[tuple[Fraction, Fraction]]:
    """The measure sum_j masses[j] delta_(j/15), j = 0..15 (j = 15 is the endpoint 1)."""
    if len(masses) != 16:
        raise ValueError("sixteen masses required")
    return normalize((F(j, 15), m) for j, m in enumerate(masses))


def mix(parts) -> list[tuple[Fraction, Fraction]]:
    """Convex combination: parts = [(weight, atoms), ...]."""
    return normalize((p, F(w) * m) for w, atoms in parts for p, m in atoms)


def child(atoms) -> list[tuple[Fraction, Fraction]]:
    """Sixteen-child operator C nu = (1/16) sum_a (B_a)_* nu, B_a(y) = (a + y)/16."""
    return normalize(((a + p) / 16, m / 16) for p, m in atoms for a in range(16))


def push_T(atoms) -> list[tuple[Fraction, Fraction]]:
    """T_* nu for T(y) = {16 y} on [0, 1), with the lift T(1) = 1 (the point 0.FFF...)."""
    return normalize((F(1) if p == 1 else 16 * p - (16 * p).__floor__(), m) for p, m in atoms)


def w1_between(a, b) -> Fraction:
    """Exact int_0^1 |F_a(t) - F_b(t)| dt (interval Wasserstein-1 for equal total masses)."""
    events: dict[Fraction, Fraction] = {}
    for p, m in a:
        events[p] = events.get(p, F(0)) + m
    for p, m in b:
        events[p] = events.get(p, F(0)) - m
    out, diff, last = F(0), F(0), F(0)
    for p in sorted(events):
        out += abs(diff) * (p - last)
        diff += events[p]
        last = p
    return out + abs(diff) * (1 - last)


def w1_lebesgue(atoms) -> Fraction:
    """Exact int_0^1 |F_nu(t) - t| dt for a probability measure nu on [0, 1]."""
    out, level, last = F(0), F(0), F(0)
    for p, m in list(normalize(atoms)) + [(F(1), F(0))]:
        out += _abs_linear(level, last, p)
        level += m
        last = p
    return out


def _abs_linear(c: Fraction, a: Fraction, b: Fraction) -> Fraction:
    """int_a^b |c - t| dt."""
    if b <= a:
        return F(0)
    if c <= a:
        return ((b - c) ** 2 - (a - c) ** 2) / 2
    if c >= b:
        return ((c - a) ** 2 - (c - b) ** 2) / 2
    return ((c - a) ** 2 + (b - c) ** 2) / 2


def child_defect(atoms) -> Fraction:
    """G(nu) = W_1(nu, C nu)."""
    return w1_between(atoms, child(atoms))


def haar_defect(atoms, t_atoms=None, q=None) -> Fraction:
    """D(nu) = W_1(nu, Q nu), Q = C T_*.  ``t_atoms`` overrides T_* nu (orbit segments: the
    shifted segment); ``q`` overrides the whole operator (mutation control RM-2)."""
    if q is not None:
        return w1_between(atoms, q(atoms))
    return w1_between(atoms, child(push_T(atoms) if t_atoms is None else t_atoms))


# ---------------------------------------------------------------- Kantorovich test functions
def dist_int(t: Fraction) -> Fraction:
    f = t - t.__floor__()
    return min(f, 1 - f)


def tri(h: int, theta: Fraction, y: Fraction) -> Fraction:
    """phi_(h,theta)(y) = ||h y - theta|| / h : 1-Lipschitz, integral over [0,1] equal to 1/(4h)."""
    return dist_int(h * F(y) - F(theta)) / h


def mean_tri(atoms, h: int, theta=F(0)) -> Fraction:
    return sum((m * tri(h, theta, p) for p, m in atoms), F(0))


def child_average_tri(h: int, theta: Fraction, y: Fraction) -> Fraction:
    """psi(y) = (1/16) sum_a phi_(h,theta)((a + y)/16); identically 1/(4h) when 16 does not divide h."""
    return sum((tri(h, theta, (a + F(y)) / 16) for a in range(16)), F(0)) / 16


def kantorovich_floor(atoms, h: int, theta=F(0)) -> Fraction:
    """(1/h)(1/4 - int ||h y - theta|| d nu): lower bound for W_1(nu, Lebesgue), and for
    W_1(nu, C nu) when 16 does not divide h (LMF-04)."""
    return F(1, 4 * h) - mean_tri(atoms, h, theta)


# ---------------------------------------------------------------- the Fix-mass lemma (LMF-05)
def psi_window(v: Fraction, half=F(1, 30)) -> Fraction:
    """psi(v) = int_0^half (v - s)^+ ds."""
    v = F(v)
    if v <= 0:
        return F(0)
    if v <= half:
        return v * v / 2
    return v * half - half * half / 2


def fix_mass_floor(jumps) -> Fraction:
    """Phi(J) = psi(J_0) + psi(J_15) + sum_(j=1..14) 2 psi(J_j / 2): lower bound for
    W_1(rho, Lebesgue) whenever rho({j/15}) >= J_j for all j."""
    return (psi_window(jumps[0]) + psi_window(jumps[15])
            + sum((2 * psi_window(F(jumps[j]) / 2) for j in range(1, 15)), F(0)))


def half_prefix_extremal(step=3600) -> list[tuple[Fraction, Fraction]]:
    """A rational measure rho = (1/2) nu* + (1/2) mu' (nu* = fix16(M_STAR)) whose W_1 distance
    to Lebesgue is within 1/(2 step) of 1/240: mu' is twice Lebesgue on the complement of the
    flat windows, discretised on a grid of the given step (step must be a multiple of 60)."""
    if step % 60:
        raise ValueError("step must be a multiple of 60")
    flat = [(F(0), F(1, 60)), (F(59, 60), F(1))]
    flat += [(F(j, 15) - F(1, 60), F(j, 15) + F(1, 60)) for j in range(1, 15)]
    atoms = [(p, m / 2) for p, m in fix16(M_STAR)]
    for i in range(step):
        mid = F(2 * i + 1, 2 * step)
        if not any(a <= mid <= b for a, b in flat):
            atoms.append((mid, F(1, step)))
    return normalize(atoms)


# ---------------------------------------------------------------- exact certificates on Fix16
def fix16_dual_certificate() -> dict:
    """Exact LP-duality certificate that min over the simplex of measures on {j/15 : 0<=j<=15}
    of W_1(nu, Lebesgue) and of W_1(nu, C nu) is 1/60.

    Dual witness: s(t) = +1 on [j/15, j/15 + 1/30), -1 on [j/15 + 1/30, (j+1)/15).  For every
    vertex delta_(j/15):  int s (F_delta - t) dt = 1/60  and  int s (F_delta - F_(C delta)) dt
    = 1/60, so both objectives are >= 1/60 on the whole simplex (|s| <= 1); the primal point
    M_STAR attains 1/60 for both."""
    cells = 240                                           # s is constant on cells of width 1/240
    sign = [1 if (i % 16) < 8 else -1 for i in range(cells)]
    w_vals, g_vals = [], []
    for j in range(16):
        w = g = F(0)
        for i in range(cells):
            f_nu = 1 if 16 * j <= i else 0               # F_delta on the cell [i/240, (i+1)/240)
            f_c = F(sum(1 for a in range(16) if 15 * a + j <= i), 16)
            w += sign[i] * (F(f_nu, cells) - F(2 * i + 1, 2 * cells * cells))
            g += sign[i] * (f_nu - f_c) / cells
        w_vals.append(w)
        g_vals.append(g)
    nu = fix16(M_STAR)
    return {"dual_w1_vertex_values": w_vals, "dual_defect_vertex_values": g_vals,
            "primal_w1": w1_lebesgue(nu), "primal_defect": child_defect(nu)}


def min_w1_fix15() -> Fraction:
    """The minimum over measures on the fifteen points j/15, j = 0..14 (endpoint 1 forbidden):
    cells 0..13 at their midpoints, last cell forced to level 1."""
    masses = (F(1, 30),) + (F(1, 15),) * 13 + (F(1, 10),) + (F(0),)
    return w1_lebesgue(fix16(masses))


# ---------------------------------------------------------------- orbit segments (integer fast path)
def fracs_from_digits(d: list[int], lo: int, hi: int) -> list[int]:
    """Integers Y_n = floor({16^n xi} 16^TRUNC) for lo <= n < hi (needs d up to hi + TRUNC)."""
    acc = 0
    for i in range(TRUNC):
        acc = 16 * acc + d[lo + i]
    out = [acc]
    for n in range(lo + 1, hi):
        acc = (acc * 16 + d[n + TRUNC - 1]) % SCALE
        out.append(acc)
    return out


def seg_w1_lebesgue(Y: list[int], scale: int = SCALE) -> Fraction:
    """Exact W_1 to Lebesgue of the uniform measure on the points Y_i / scale."""
    n, total = len(Y), 0
    pts = sorted(Y) + [scale]
    last, level = 0, 0
    for p in pts:
        a, b, c = last * n, p * n, level * scale          # int_a^b |c - t'| dt', t' = n t
        if b > a:
            if c <= a:
                total += (b - c) ** 2 - (a - c) ** 2
            elif c >= b:
                total += (c - a) ** 2 - (c - b) ** 2
            else:
                total += (c - a) ** 2 + (b - c) ** 2
        last, level = p, level + 1
    return F(total, 2 * n * n * scale * scale)


def seg_w1_between(P: list[int], Q: list[int], scale: int) -> Fraction:
    """Exact int |F_P - F_Q| for uniform measures on P/scale and on Q/scale."""
    nP, nQ = len(P), len(Q)
    ev = sorted([(p, nQ) for p in P] + [(q, -nP) for q in Q])
    total, diff, last = 0, 0, 0
    for p, w in ev:
        total += abs(diff) * (p - last)
        diff += w
        last = p
    return F(total, nP * nQ * scale)


def seg_child_defect(Y: list[int]) -> Fraction:
    """G(nu) = W_1(nu, C nu) for the uniform measure nu on Y / SCALE."""
    big = 16 * SCALE
    return seg_w1_between([16 * y for y in Y], [a * SCALE + y for y in Y for a in range(16)], big)


def seg_haar_defect(Y: list[int], Ynext: list[int]) -> Fraction:
    """D(nu) = W_1(nu, C T_* nu) for an orbit segment: Ynext is the segment shifted by one step."""
    big = 16 * SCALE
    return seg_w1_between([16 * y for y in Y], [a * SCALE + y for y in Ynext for a in range(16)], big)


def seg_mean_tri(Y: list[int], h: int, theta=F(0)) -> Fraction:
    return sum((tri(h, theta, F(y, SCALE)) for y in Y), F(0)) / len(Y)


# ---------------------------------------------------------------- digits, bits, change counts
def bits_of_digits(d: list[int]) -> list[int]:
    """Binary digits b_(4n+i) = bit (3 - i) of d_n, so xi = 0.b_0 b_1 b_2 ... in base 2."""
    return [(x >> (3 - i)) & 1 for x in d for i in range(4)]


def k_changes(d: list[int], lo: int, hi: int, k: int = 1) -> int:
    return sum(1 for n in range(lo, hi) if d[n] != d[n + k])


def bad_fraction(d: list[int], lo: int, hi: int, k: int) -> Fraction:
    """Fraction of n in [lo, hi) for which d_n, ..., d_(n+k-1) are not all equal."""
    return F(sum(1 for n in range(lo, hi) if any(d[n + i] != d[n] for i in range(1, k))), hi - lo)


# ---------------------------------------------------------------- witnesses (LMF-03, LMF-06)
def ladder_digits(length: int) -> list[int]:
    """S*: superblock k is 0^k 1^(2k) 2^(2k) ... E^(2k) F^k.  Shell measures tend to fix16(M_STAR):
    change density -> 0 while W_1 and D tend to the thresholds 1/60."""
    d, k = [], 1
    while len(d) < length:
        for j in range(16):
            d += [j] * (k if j in (0, 15) else 2 * k)
        k += 1
    return d[:length]


def superblock_shell_digits(k: int) -> tuple[list[int], int]:
    """A digit string whose shell [B, 2B), B = 30k, is exactly one superblock
    0^k 1^(2k) ... E^(2k) F^k (followed by F's).  Change density 15/B = 1/(2k), and
    W_1(nu_B, Lebesgue) <= 1/60 + 16/(450 k), which is below 4/225 for k >= 33."""
    B = 30 * k
    d = [n % 2 for n in range(B)]
    for j in range(16):
        d += [j] * (k if j in (0, 15) else 2 * k)
    return d + [15] * (TRUNC + 8), B


def two_runs_digits(a: int, b: int, length: int) -> list[int]:
    """Runs a^k b^k, k = 1, 2, ...: shell measures tend to (delta_(a/15) + delta_(b/15))/2."""
    d, k = [], 1
    while len(d) < length:
        d += [a] * k + [b] * k
        k += 1
    return d[:length]


def sparse_excursion_digits(a: int, b: int, length: int) -> list[int]:
    """Digit a everywhere except digit b at the squares n = m^2 >= 4."""
    d = [a] * length
    m = 2
    while m * m < length:
        d[m * m] = b
        m += 1
    return d


def period_mix_digits(length: int) -> list[int]:
    """Superblock s: for k = 1 .. floor(log2 s) + 1, the word 0^(k-1) 1 repeated ceil(s / 2^k)
    times.  Every (CH_k) holds, yet the only shell limit is purely atomic on periodic points."""
    d, s = [], 1
    while len(d) < length:
        for k in range(1, s.bit_length() + 1):
            d += ([0] * (k - 1) + [1]) * (-(-s // 2 ** k))
        s += 1
    return d[:length]


def basel_converse_digits(length: int) -> list[int]:
    """d_n = n mod 2 except d_n = 0 on [16^i, 2*16^i], i >= 1: (CH) fails along B = 16^i, yet
    limsup_A Re(A F_15(A)) < 1."""
    d = [n % 2 for n in range(length)]
    L = 16
    while L < length:
        for n in range(L, min(length, 2 * L + 1)):
            d[n] = 0
        L *= 16
    return d


# ---------------------------------------------------------------- Basel weights (LMF-02 (e))
def omega(A: int) -> Fraction:
    return sum((F(1, n * n) for n in range(A, 2 * A)), F(0))


def basel_weights(A: int) -> list[Fraction]:
    w = omega(A)
    return [F(1, n * n) / w for n in range(A, 2 * A)]


# ---------------------------------------------------------------- data paths for the digits of x
def x_scaled_from_source(M: int, guard: int = 16) -> int:
    """floor(x 16^M), x = pi/16 = sum_(j>=1) 16^(-j) r(j), from the frozen forcing alone by
    integer arithmetic with a rigorous enclosure (route B; no pi oracle, no floating point).

    With M' = M + guard and L = M' + 2:  S = sum_(j<=L) floor(16^(M'-j) r(j)) satisfies
    S <= x 16^M' < S + L + 1 (each floor loses < 1; the tail is < 1).  The result is certified
    when floor(S / 16^guard) = floor((S + L + 1) / 16^guard)."""
    Mp = M + guard
    L = Mp + 2
    S = 0
    power = 16 ** (Mp - 1)
    for j in range(1, Mp + 1):
        rj = ic.r(j)
        S += (power * rj.numerator) // rj.denominator
        power //= 16
    # j = Mp + 1, Mp + 2 contribute floor(r(j) / 16^(j - Mp)) = 0; their true value is in the slack
    lo, hi = S >> (4 * guard), (S + L + 1) >> (4 * guard)
    if lo != hi:
        raise RuntimeError("route B undecided: increase guard")
    return lo


def digits_from_scaled(X: int, M: int, n_digits: int) -> list[int]:
    """d_0 .. d_(n_digits-1) from X = floor(x 16^M)."""
    return [(X >> (4 * (M - 1 - n))) & 15 for n in range(n_digits)]


def digits_from_carrier(n_max: int, S=None) -> list:
    """d_1 .. d_(n_max) from the exact zero-seed carrier alone (route C): the cocycle
    d_n = kappa_(n+1) + eps_(n+1) - 16 eps_n with exact carries and source-certified seam bits.
    Entry 0 is None."""
    S = S or ic.Source(n_max + 2)
    C = [u.numerator // u.denominator for u in S.U[: n_max + 2]]
    eps = zc.seam_bits(S.U, n_max + 1)
    return [None] + [C[n + 1] - 16 * C[n] + eps[n + 1] - 16 * eps[n] for n in range(1, n_max + 1)]


def dec(x: Fraction, places: int = 15) -> str:
    """Deterministic decimal string: floor(x 10^places) / 10^places (sign-aware truncation)."""
    x = F(x)
    sgn = "-" if x < 0 else ""
    q = (abs(x) * 10 ** places).__floor__()
    s = str(q).rjust(places + 1, "0")
    return f"{sgn}{s[:-places]}.{s[-places:]}"
