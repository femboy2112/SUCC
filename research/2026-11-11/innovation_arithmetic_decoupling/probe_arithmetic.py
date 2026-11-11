#!/usr/bin/env python3
"""Arithmetic-side holdout probe of the IAD dossier.

Scope: PR-1.7 ... PR-1.11, PR-2.6 ... PR-2.8 and the arithmetic PR-3 items of
PREREGISTRATION.md (claims IAD-07, IAD-08, IAD-09 of THEOREMS.md and SWT-01 ... SWT-05
of SCOTT_TRANSPORT.md).

Run from the repository root::

    PYTHONPATH=. python research/2026-11-11/innovation_arithmetic_decoupling/probe_arithmetic.py
    PYTHONPATH=. python .../probe_arithmetic.py --quick --out /tmp/quick.json

Discipline
----------
* Exact ``Fraction``/integer arithmetic wherever the statement is exact.
* Every floor / threshold decision uses a rational enclosure, or rigorous mpmath interval
  arithmetic (``mp.iv``, outward rounding) when a transcendental constant enters; an
  instance that cannot be settled at the available width raises ``Undecidable`` (never
  guessed).  ``mp.mp.dps`` is never changed globally (``mp.workdps`` and a saved/restored
  ``mp.iv.prec`` only).
* The pi enclosure used for every comparison is computed here by Machin's formula in pure
  integer arithmetic (independent of BBP and of mpmath) and is cross-checked against the
  kernel's ``iad_core._x_scaled``; the hexadecimal digits for the seam law are additionally
  cross-checked against an mpmath route.
* PR-1 failures make the exit status 1.  PR-2 outcomes are recorded as
  ``predicted``/``observed``/``met`` and never change the exit status.  Additional theorem
  checks outside the preregistered PR-1 scope are recorded (with counterexamples) under
  ``additional_theorem_checks`` and do not change the exit status either.

Output: ``RESULTS_arithmetic.json`` (sorted keys, no timestamps, fixed seeds).
``--quick`` runs the smallest shell only with seam range n <= 400 and writes nothing unless
``--out`` is given.
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import random
import sys
from collections import Counter
from contextlib import contextmanager
from fractions import Fraction
from functools import lru_cache
from math import gcd, isqrt
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

import iad_core as ic  # noqa: E402

REPO = HERE.parents[2]
# AT-07 seven-pole null source (research/2026-10-30/arithmetic_barrier/arithmetic).
AT07_TRANSPORT = REPO / "research" / "2026-10-30" / "arithmetic_barrier" / "arithmetic" / "transport.py"
# Null vector Z on offsets 1..8: transcribed verbatim from test_transport.py lines 184 and 200
# (test_published_null_relation_and_signed_reflected_tail /
# test_zero_seed_coherent_null_has_all_odd_conductor_depths) and ARITHMETIC_THEOREMS.md AT-06
# (lines 345-378): z(n) = transport.source(n, Z, (1..8)) = w(n) - 2 r(n).
AT07_Z = (-8, 8, 4, 8, 2, 2, -1, 0)

HOLDOUT_SHELLS = (200, 360, 729, 1000)
MODES = (1, 3, 8)
Q_HIJACK = 1_000_003
SEAM_CALIBRATION_MAX = 1300
SEAM_MAX = 3200
QUICK_SEAM_MAX = 400
SEED = 20261111
FORCED_SEAM_N0 = 150
CONTROL_HORIZON = 400

FACTOR_LABELS = ("8m-7", "2m-1", "8m-3", "4m-1")
POLE_COEFF = {"8m-7": Fraction(4), "8m-3": Fraction(-1), "4m-1": Fraction(-1, 2)}
POLE_CLASSES = {"8m-7": (1,), "8m-3": (5,), "4m-1": (3, 7)}


class Undecidable(RuntimeError):
    """A floor/threshold decision that the available enclosure width cannot settle."""


# --------------------------------------------------------------------------- small helpers

def ffloor(q) -> int:
    return q.numerator // q.denominator


def ffrac(q: Fraction) -> Fraction:
    return q - ffloor(q)


def vp(q: Fraction, p: int) -> int:
    """p-adic valuation of a nonzero rational."""
    q = Fraction(q)
    if q == 0:
        raise ValueError("valuation of zero")
    v, num, den = 0, abs(q.numerator), q.denominator
    while num % p == 0:
        num //= p
        v += 1
    while den % p == 0:
        den //= p
        v -= 1
    return v


def log10_abs(q) -> float:
    q = Fraction(q)
    if q == 0:
        return float("-inf")
    with mp.workdps(30):
        return float(mp.log10(mp.mpf(abs(q.numerator))) - mp.log10(mp.mpf(q.denominator)))


def short(q) -> object:
    """JSON-safe rendering of a rational: exact string if small, else its log10."""
    q = Fraction(q)
    if max(abs(q.numerator).bit_length(), q.denominator.bit_length()) <= 128:
        return str(q)
    return {"log10_abs": log10_abs(q), "sign": (q > 0) - (q < 0)}


def chk(bad: list, n_checked: int) -> dict:
    return {"pass": not bad, "n_checked": n_checked, "n_failures": len(bad),
            "first_failures": [list(b) if isinstance(b, tuple) else b for b in bad[:10]]}


def primes_upto(n: int) -> list[int]:
    if n < 2:
        return []
    sieve = bytearray([1]) * (n + 1)
    sieve[0] = sieve[1] = 0
    for i in range(2, isqrt(n) + 1):
        if sieve[i]:
            sieve[i * i::i] = bytearray(len(range(i * i, n + 1, i)))
    return [i for i in range(n + 1) if sieve[i]]


def spf_table(n: int) -> list[int]:
    spf = list(range(n + 1))
    for i in range(2, isqrt(n) + 1):
        if spf[i] == i:
            for j in range(i * i, n + 1, i):
                if spf[j] == j:
                    spf[j] = i
    return spf


def prime_factors(n: int, spf: list[int]) -> set[int]:
    out = set()
    while n > 1:
        p = spf[n]
        out.add(p)
        while n % p == 0:
            n //= p
    return out


M_HIJACK_FACTORS = {2: 8, **{p: 2 for p in primes_upto(97) if p > 2}}
M_HIJACK = 1
for _p, _j in M_HIJACK_FACTORS.items():
    M_HIJACK *= _p ** _j


# --------------------------------------------------------------- independent pi (Machin)

def _arctan_inv(n: int, one: int) -> tuple[int, int]:
    """sum_k (-1)^k floor(floor(one/n^(2k+1))/(2k+1)) and the number of terms used.

    Each term is low by less than 2 and the omitted alternating tail is below 1, so the
    total error is below 2*terms + 1 in absolute value."""
    total, power, n2, k = 0, one // n, n * n, 0
    while power:
        term = power // (2 * k + 1)
        total = total - term if k & 1 else total + term
        power //= n2
        k += 1
    return total, k


@lru_cache(maxsize=None)
def pi_floor_bits(bits: int) -> int:
    """floor(pi * 2^bits) by Machin's formula, integer arithmetic only, error-certified."""
    guard = 64
    while True:
        one = 1 << (bits + guard)
        a5, t5 = _arctan_inv(5, one)
        a239, t239 = _arctan_inv(239, one)
        P = 16 * a5 - 4 * a239
        err = 16 * (2 * t5 + 1) + 4 * (2 * t239 + 1)
        lo, hi = (P - err) >> guard, (P + err) >> guard
        if lo == hi:
            return lo
        guard += 64


def x_scaled_machin(M: int) -> int:
    """floor(x 16^M) for x = pi/16, i.e. floor(pi 2^(4M-4)), M >= 1."""
    if M < 1:
        raise ValueError("M >= 1 required")
    return pi_floor_bits(4 * M - 4)


def x_interval(M: int) -> tuple[Fraction, Fraction, int]:
    """Strict rational enclosure X/16^M < x < (X+1)/16^M (x irrational), Machin route."""
    X = x_scaled_machin(M)
    return Fraction(X, 16 ** M), Fraction(X + 1, 16 ** M), X


def pi_floor_hex_mpmath(n_hex: int) -> int:
    """floor(pi 16^n_hex) by mpmath at ample working precision (second, library route)."""
    with mp.workdps(int(n_hex * 1.2042) + 80):
        return int(mp.floor(mp.pi * mp.mpf(16) ** n_hex))


# ---------------------------------------------------------------- rigorous intervals

@contextmanager
def iv_precision(bits: int):
    old = mp.iv.prec
    mp.iv.prec = bits
    try:
        yield mp.iv
    finally:
        mp.iv.prec = old


def fiv(iv, f) -> object:
    f = Fraction(f)
    return iv.mpf(f.numerator) / iv.mpf(f.denominator)


def hull(iv, lo: Fraction, hi: Fraction):
    a, b = fiv(iv, lo), fiv(iv, hi)
    return iv.mpf([a.a, b.b])


def iv_le(x, y) -> bool:
    """Decide x <= y for real intervals, or raise Undecidable."""
    if x.b <= y.a:
        return True
    if x.a > y.b:
        return False
    raise Undecidable("interval comparison overlaps")


def sq(iv, x):
    ax = abs(x)
    return ax * ax


def e_minus_one_sum(iv, intervals):
    """Interval enclosures (Re, Im) of sum (e(t) - 1) over t in [lo, hi] (Fraction pairs)."""
    re, im = iv.mpf(0), iv.mpf(0)
    for lo, hi in intervals:
        k = ffloor(lo + Fraction(1, 2))
        T = hull(iv, lo - k, hi - k)
        s = iv.sin(iv.pi * T)
        re += -2 * sq(iv, s)
        im += iv.sin(2 * iv.pi * T)
    return re, im


def iv_float_upper(x) -> float:
    return float(mp.mpf(x.b))


# ============================================================ SWT-02/03/04 seam machinery

def kappa_swt02(frac_prev: Fraction, r_n: Fraction) -> int:
    """SWT-02: kappa_n = floor(16 frac(U_(n-1)) + r(n)) (carry 16 retained)."""
    return ffloor(16 * frac_prev + r_n)


def carry_and_seam(U, forcing, n_max, n_src, tail_fn, H=None, lookahead=True, kappa_fn=kappa_swt02):
    """Literal carries, carry formula, reconstruction, seam indicator and SWT-03 items.

    U[0..n_src]: exact states of one seed under ``forcing``.  ``tail_fn(n)`` returns (lo, hi)
    with lo <= T_n <= hi.  ``H[0..n_max+1]``: completed floors floor(Y_n(s)) from an
    independent route (None: source-side only, d derived from the seam law).  ``kappa_fn`` is
    an injection point for mutation controls only.
    """
    if len(U) < n_src + 1 or n_src < n_max + 2:
        raise ValueError("need U[0..n_src] with n_src >= n_max + 2")
    checks = {}
    C = [ffloor(u) for u in U[: n_src + 1]]
    kap = [None] * (n_src + 1)
    bad_range, bad_formula, bad_recon = [], [], []
    acc = C[0]
    for n in range(1, n_src + 1):
        k = kappa_fn(U[n - 1] - C[n - 1], forcing(n))  # kappa_n by the SWT-02 formula
        kap[n] = k
        if not 0 <= k <= 16:
            bad_range.append(n)
        if C[n] - 16 * C[n - 1] != k:  # the literal carry C_n - 16 C_(n-1)
            bad_formula.append(n)
        acc = 16 * acc + k  # C_n = 16^n C_0 + sum_j 16^(n-j) kappa_j (C_0 = 0 for the zero seed)
        if acc != C[n]:
            bad_recon.append(n)
    checks["kappa_in_0_16"] = chk(bad_range, n_src)
    checks["kappa_equals_floor_16frac_plus_r"] = chk(bad_formula, n_src)
    checks["C_equals_sum_16pow_kappa"] = chk(bad_recon, n_src)

    eps_src = []
    for n in range(n_max + 2):
        f = U[n] - C[n]
        lo, hi = tail_fn(n)
        if f >= 1 - lo:
            eps_src.append(1)
        elif f < 1 - hi:
            eps_src.append(0)
        else:
            raise Undecidable(f"eps_{n}: frac(U_n) lies inside the enclosure of 1 - T_n")
    out = {"C": C, "kappa": kap, "eps_src": eps_src, "checks": checks}

    if H is not None:
        eps = [H[n] - C[n] for n in range(n_max + 2)]
        checks["eps_in_0_1"] = chk([n for n, e in enumerate(eps) if e not in (0, 1)], n_max + 2)
        checks["eps_iff_fracU_ge_1_minus_T"] = chk(
            [n for n in range(n_max + 2) if eps[n] != eps_src[n]], n_max + 2)
        d = [H[n + 1] - 16 * H[n] for n in range(n_max + 1)]
        checks["d_in_0_15"] = chk([n for n, v in enumerate(d) if not 0 <= v <= 15], n_max + 1)
        # Left: digits from the independent completed route H.  Right: source-only data (kappa by
        # the SWT-02 formula, eps by the tail rule).  With eps := H - C the law would be an
        # algebraic identity, so the source-side eps is used here.
        checks["seam_law_d_eq_kappa_plus_eps_minus_16eps"] = chk(
            [n for n in range(n_max + 1) if d[n] != kap[n + 1] + eps_src[n + 1] - 16 * eps_src[n]], n_max + 1)
    else:
        eps = eps_src
        d = [kap[n + 1] + eps[n + 1] - 16 * eps[n] for n in range(n_max + 1)]

    bad3 = [n for n in range(1, n_max + 1)
            if eps[n] == 1 and not (d[n] == 0 and kap[n + 1] in (15, 16))]
    bad4 = [n for n in range(n_max + 1)
            if (kap[n + 1] == 16 and not (eps[n] == 1 and eps[n + 1] == 0))
            or (kap[n + 1] == 15 and eps[n + 1] == 1 and eps[n] != 1)]
    checks["item3_eps1_implies_d0_and_kappa_15_16"] = chk(bad3, n_max)
    checks["item4_carry16_and_15_back_propagation"] = chk(bad4, n_max + 1)
    checks["d_differs_from_kappa_only_at_seam"] = chk(
        [n for n in range(n_max + 1) if d[n] != kap[n + 1] and not (eps[n] or eps[n + 1])], n_max + 1)
    antecedents = {
        "item3_eps1": sum(1 for n in range(1, n_max + 1) if eps[n] == 1),
        "item4_kappa16": sum(1 for n in range(n_max + 1) if kap[n + 1] == 16),
        "item4_kappa15_eps1": sum(1 for n in range(n_max + 1) if kap[n + 1] == 15 and eps[n + 1] == 1),
    }
    if lookahead:
        bad5 = []
        for n in range(n_max + 1):
            j = n + 1
            while j <= n_src and kap[j] == 15:
                j += 1
            if j > n_src:
                raise Undecidable(f"look-ahead from n={n}: run of 15 reaches the source horizon")
            if (1 if kap[j] == 16 else 0) != eps[n]:
                bad5.append(n)
        checks["item5_eps1_iff_kappa_continues_15a_16"] = chk(bad5, n_max + 1)
    out.update(eps=eps, d=d, antecedents=antecedents)
    return out


def occurrences(seq, k, N) -> Counter:
    if N + k - 1 > len(seq):
        raise ValueError("sequence too short for occ_N")
    return Counter(tuple(seq[n:n + k]) for n in range(N))


def seam_density_bound(kap, N) -> int:
    """sum_{j<=N, kappa_j=16} (1 + a_j) + 1 + b_N (SWT-03 seam-density bound, source data only)."""
    total = 0
    for j in range(1, N + 1):
        if kap[j] == 16:
            a, i = 0, j - 1
            while i >= 1 and kap[i] == 15:
                a += 1
                i -= 1
            total += 1 + a
    b, i = 0, N
    while i >= 1 and kap[i] == 15:
        b += 1
        i -= 1
    return total + 1 + b


def true_seed_seam(S: ic.Source, n_max: int, n_src: int) -> dict:
    """PR-1.10 on the literal zero seed, the independent digit routes, counts and frequencies."""
    U = S.U[: n_src + 1]
    tails: dict[int, tuple[Fraction, Fraction]] = {}

    def tail(n):
        if n not in tails:
            tails[n] = ic.tail_interval(n)
        return tails[n]

    Mh = n_max + 2 + 64
    X = x_scaled_machin(Mh)
    H = [X >> (4 * (Mh - n)) for n in range(n_max + 2)]  # floor(16^n x), exact nested floors
    ev = carry_and_seam(U, ic.r, n_max, n_src, tail, H)
    checks = ev["checks"]
    C, kap, eps, d = ev["C"], ev["kappa"], ev["eps"], ev["d"]

    # Second pi route (mpmath) for the hexadecimal digits, and the kernel's pi oracle.
    Pm = pi_floor_hex_mpmath(n_max)  # floor(pi 16^n_max); H_n = floor(pi 16^(n-1))
    H_mp = [0] + [Pm >> (4 * (n_max - (n - 1))) for n in range(1, n_max + 2)]
    checks["digits_machin_eq_mpmath"] = chk([n for n in range(n_max + 2) if H[n] != H_mp[n]], n_max + 2)
    checks["kernel_x_scaled_eq_machin"] = {"pass": ic._x_scaled(Mh) == X, "M_hex": Mh}
    known = [3, 2, 4, 3, 15, 6, 10, 8, 8, 8, 5, 10, 3, 0, 8, 13, 3]  # 3.243F6A8885A308D3 (calibration)
    checks["digits_calibration_243F6A8885A308D3"] = {"pass": d[:len(known)] == known}

    # SWT-02 bracket 0 < x - C_n/16^n < (1 + T_n)/16^n with the Machin enclosure of x.
    bad_br = []
    for n in range(n_max + 1):
        scale = 16 ** (Mh - n)
        lower_ok = X >= C[n] * scale
        upper_ok = (X + 1) - C[n] * scale <= (1 + tail(n)[0]) * scale
        if not (lower_ok and upper_ok):
            bad_br.append(n)
    checks["x_minus_C_over_16n_in_0_1plusT"] = chk(bad_br, n_max + 1)

    def count(seq_idx):
        return len(seq_idx)

    eps_events = [n for n in range(n_max + 1) if eps[n] == 1]
    carries16 = [n for n in range(1, n_max + 1) if kap[n] == 16]
    counts = {
        "calibration_range": [0, min(SEAM_CALIBRATION_MAX, n_max)],
        "holdout_range": [SEAM_CALIBRATION_MAX + 1, n_max] if n_max > SEAM_CALIBRATION_MAX else None,
        "eps_events_calibration": count([n for n in eps_events if n <= SEAM_CALIBRATION_MAX]),
        "eps_events_holdout": count([n for n in eps_events if n > SEAM_CALIBRATION_MAX]),
        "carry16_calibration": count([n for n in carries16 if n <= SEAM_CALIBRATION_MAX]),
        "carry16_holdout": count([n for n in carries16 if n > SEAM_CALIBRATION_MAX]),
        "eps_event_positions": eps_events[:50],
        "carry16_positions": carries16[:50],
        "kappa_value_counts_1_to_nmax": {str(v): c for v, c in sorted(Counter(kap[1:n_max + 1]).items())},
    }

    # Frequencies (observation) and the SWT-04 inequality, N = n_max.
    N = n_max
    kplus = [kap[n + 1] for n in range(n_src)]
    freqs, swt04_bad, swt04_rows = {}, [], {}
    for k in (1, 2):
        od, ok_ = occurrences(d, k, N), occurrences(kplus, k, N)
        rho = sum(eps[n] for n in range(N + k))
        bound = 2 * k * rho
        worst = max((abs(od[w] - ok_[w]) for w in set(od) | set(ok_)), default=0)
        alphabet = range(17)
        words = [(a,) for a in alphabet] if k == 1 else [(a, b) for a in alphabet for b in alphabet]
        for w in words:
            if abs(od[w] - ok_[w]) > bound:
                swt04_bad.append((k, list(w)))
        swt04_rows[str(k)] = {"rho_N_plus_k": rho, "bound_2k_rho": bound, "max_abs_occ_difference": worst,
                              "n_words_checked": len(words)}
        freqs[f"d_block{k}"] = {",".join(map(str, w)): c for w, c in sorted(od.items())}
        freqs[f"kappa_plus_block{k}"] = {",".join(map(str, w)): c for w, c in sorted(ok_.items())}
    freqs["N"] = N
    swt04 = {"pass": not swt04_bad, "rows": swt04_rows, "first_failures": swt04_bad[:10]}
    rho_N = sum(eps[n] for n in range(N))
    density = {"N": N, "rho_N": rho_N, "source_side_bound": seam_density_bound(kap, N),
               "holds": rho_N <= seam_density_bound(kap, N)}
    return {"checks": checks, "counts": counts, "frequencies": freqs, "swt04": swt04,
            "seam_density": density, "antecedents_item3_item4": ev["antecedents"],
            "n_max": n_max, "n_src": n_src, "pi_enclosure_hex_digits": Mh}


def coherent_seed_control(S: ic.Source, horizon: int = CONTROL_HORIZON) -> dict:
    """s = -x: U_n(s) = -T_n, C_n = -1, kappa = 15, eps = 1 (tail and x enclosures)."""
    Mh = horizon + 64
    lo, hi, _ = x_interval(Mh)
    orbit = ic.CompletedOrbit(horizon + 1, a=Fraction(0), b=Fraction(0))
    bad_C, bad_id, bad_kf, boundary_overlaps = [], [], [], 0
    prev = None
    for n in range(horizon + 2):
        u_lo, u_hi = S.U[n] - 16 ** n * hi, S.U[n] - 16 ** n * lo  # U_n(s) in (u_lo, u_hi)
        if not (-1 < u_lo and u_hi < 0):
            bad_C.append(n)
        t_lo, t_hi = ic.tail_interval(n)
        if not (u_lo < -t_lo and -t_hi < u_hi):  # identity U_n(s) = -T_n: enclosures must meet
            bad_id.append(n)
        if prev is not None:  # kappa_n = floor(16 frac(U_(n-1)(s)) + r(n)), frac = U + 1 (C = -1)
            k_lo = ffloor(16 * (prev[0] + 1) + ic.r(n))
            k_hi = ffloor(16 * (prev[1] + 1) + ic.r(n))
            if not (k_lo == k_hi == 15):
                bad_kf.append(n)
        # eps rule boundary: frac(U_n(s)) = 1 - T_n exactly; enclosures of both sides overlap.
        if (u_lo + 1) < 1 - t_lo and (u_hi + 1) > 1 - t_hi:
            boundary_overlaps += 1
        prev = (u_lo, u_hi)
    C = [-1] * (horizon + 2)
    kap = [None] + [C[n] - 16 * C[n - 1] for n in range(1, horizon + 2)]
    H = [orbit.floor(n) for n in range(horizon + 2)]
    exact_zero = all(orbit.frac(n) == 0 for n in range(horizon + 2)) and orbit.frac_error() == 0
    eps = [H[n] - C[n] for n in range(horizon + 2)]
    d = [H[n + 1] - 16 * H[n] for n in range(horizon + 1)]
    checks = {
        "C_n_eq_minus1": chk(bad_C, horizon + 2),
        "U_n_s_eq_minus_T_n_enclosures_meet": chk(bad_id, horizon + 2),
        "kappa_formula_eq_15": chk(bad_kf, horizon + 1),
        "kappa_eq_15": chk([n for n in range(1, horizon + 2) if kap[n] != 15], horizon + 1),
        "completed_orbit_identically_zero": {"pass": exact_zero},
        "eps_eq_1": chk([n for n in range(horizon + 2) if eps[n] != 1], horizon + 2),
        "seam_law": chk([n for n in range(horizon + 1) if d[n] != kap[n + 1] + eps[n + 1] - 16 * eps[n]],
                        horizon + 1),
        "item3": chk([n for n in range(1, horizon + 1)
                      if eps[n] == 1 and not (d[n] == 0 and kap[n + 1] in (15, 16))], horizon),
        "item4": chk([n for n in range(horizon + 1)
                      if (kap[n + 1] == 16 and not (eps[n] == 1 and eps[n + 1] == 0))
                      or (kap[n + 1] == 15 and eps[n + 1] == 1 and eps[n] != 1)], horizon + 1),
    }
    carries16 = sum(1 for n in range(1, horizon + 2) if kap[n] == 16)
    return {
        "horizon": horizon,
        "checks": checks,
        "pass": all(c["pass"] for c in checks.values()),
        "eps_rule_boundary_case": {
            "note": "frac(U_n(s)) = 1 - T_n exactly for s = -x; the rule sits on its boundary and "
                    "no finite enclosure decides it (eps taken from the exact completed point Y = 0)",
            "n_with_overlapping_enclosures": boundary_overlaps, "n_total": horizon + 2},
        "item5_expected_failure": {
            "expected": "infinite seam run (completed point x+s = 0 is rational): eps = 1 everywhere "
                        "but kappa contains no 16, so the finite look-ahead characterization fails",
            "eps_ones": sum(eps), "carries_16_in_kappa": carries16,
            "item5_fails_as_expected": sum(eps) == horizon + 2 and carries16 == 0},
    }


def forced_seam_seed(S: ic.Source, n0: int, a_run: int) -> Fraction:
    """Rational seed with frac(U_n0(s)) = 1 - eta forcing kappa_(n0+1..n0+a) = 15, kappa_(n0+a+1) = 16."""
    eta = sum((Fraction(ic.r(n0 + j), 16 ** j) for j in range(1, a_run + 1)), Fraction(0))
    eta += Fraction(ic.r(n0 + a_run + 1), 2 * 16 ** (a_run + 1))
    return (1 - eta - ffrac(S.U[n0])) / 16 ** n0


def forced_seam_control(S: ic.Source, n0: int, a_run: int, horizon: int = CONTROL_HORIZON) -> dict:
    s = forced_seam_seed(S, n0, a_run)
    n_src = horizon + 100
    U = [S.U[n] + 16 ** n * s for n in range(n_src + 1)]
    Mh = horizon + 2 + 64
    lo, hi, _ = x_interval(Mh)
    H = []
    for n in range(horizon + 2):
        a_, b_ = ffloor(16 ** n * (lo + s)), ffloor(16 ** n * (hi + s))
        if a_ != b_:
            raise Undecidable(f"forced seed: floor(Y_{n}(s)) not decided")
        H.append(a_)
    orbit = ic.CompletedOrbit(horizon + 1, a=s, b=Fraction(1))
    err = orbit.frac_error()
    kernel_bad = [n for n in range(horizon + 2)
                  if not (orbit.frac(n) + err < 1 and orbit.floor(n) == H[n])]
    ev = carry_and_seam(U, ic.r, horizon, n_src, ic.tail_interval, H)
    kap, eps = ev["kappa"], ev["eps"]
    planted = (eps[n0] == 1 and all(kap[n0 + i] == 15 for i in range(1, a_run + 1))
               and kap[n0 + a_run + 1] == 16 and eps[n0 + a_run + 1] == 0)
    checks = dict(ev["checks"])
    checks["completed_orbit_kernel_route_agrees"] = chk(kernel_bad, horizon + 2)
    checks["planted_pattern_present"] = {"pass": planted}
    return {
        "n0": n0, "a_run": a_run, "horizon": horizon,
        "seed": short(s),
        "checks": checks,
        "pass": all(c["pass"] for c in checks.values()),
        "eps_event_positions": [n for n in range(horizon + 1) if eps[n] == 1],
        "carry16_positions": [n for n in range(1, horizon + 1) if kap[n] == 16],
        "kappa_window": kap[n0 - 2:n0 + a_run + 4],
        "eps_window": eps[n0 - 2:n0 + a_run + 4],
        "antecedents_item3_item4": ev["antecedents"],
    }


# ========================================================================= SWT-01(i)

def planted_stream(seed: int, length: int = 20000, alphabet: int = 16, target_letter=None):
    rng = random.Random(seed)
    v = [rng.randrange(alphabet) for _ in range(length)]
    n_edits = round(length ** 0.5)
    if target_letter is None:
        pos = sorted(rng.sample(range(length), n_edits))
    else:
        pos = sorted(rng.sample([i for i in range(length) if v[i] != target_letter], n_edits))
    w = list(v)
    for i in pos:
        w[i] = target_letter if target_letter is not None else (v[i] + rng.randrange(1, alphabet)) % alphabet
    return v, w, pos


def swt01_check(v, w, k_max: int = 3, N_list=None, bound_fn=None) -> dict:
    """|occ_N(u; v) - occ_N(u; w)| <= k #{n < N+k : v_n != w_n} for all words u, |u| = k <= k_max."""
    bound_fn = bound_fn or (lambda k, E: k * E)
    L = len(v)
    N_list = N_list or [1000, 5000, 10000, L - k_max + 1]
    pref = [0]
    for a, b in zip(v, w):
        pref.append(pref[-1] + (a != b))
    rows, bad = [], []
    for N in N_list:
        for k in range(1, k_max + 1):
            ov, ow = occurrences(v, k, N), occurrences(w, k, N)
            E = pref[min(N + k, L)]
            worst = max((abs(ov[u] - ow[u]) for u in set(ov) | set(ow)), default=0)
            bound = bound_fn(k, E)
            if worst > bound:
                bad.append((N, k, worst, bound))
            rows.append({"N": N, "k": k, "edits_before_N_plus_k": E, "bound": bound,
                         "max_abs_difference": worst})
    return {"pass": not bad, "rows": rows, "first_failures": bad[:10]}


# ========================================================================= SWT-05(B)

def near_pair_J(points: list[int], P: int, q: int, with_q_factor: bool = True) -> Fraction:
    """J_(A,q) = (q/A^2) sum_(n,m) (1 - q d_T(x_n, x_m))_+ with x_n = points[n]/2^P."""
    D = 1 << P
    tot = 0
    for x in points:
        for y in points:
            dd = x - y if x >= y else y - x
            if 2 * dd > D:
                dd = D - dd
            t = D - q * dd
            if t > 0:
                tot += t
    A = len(points)
    return Fraction(q * tot if with_q_factor else tot, A * A * D)


def swt05b_check(points: list[int], P: int, delta: Fraction, qs=(2, 4, 8, 16, 32),
                 with_q_factor: bool = True) -> dict:
    """Nondecreasing along the divisibility chain and J >= q/A, with the enclosure error
    |J - J_computed| <= 2 q^2 delta (each x_n known to within delta)."""
    A = len(points)
    J = {q: near_pair_J(points, P, q, with_q_factor) for q in qs}
    errs = {q: 2 * q * q * delta for q in qs}
    mono_bad, lower_bad = [], []
    for q1, q2 in zip(qs, qs[1:]):
        if q2 % q1:
            raise ValueError("qs must be a divisibility chain")
        diff = J[q2] - J[q1]
        if diff > errs[q1] + errs[q2]:
            continue
        if diff < -(errs[q1] + errs[q2]):
            mono_bad.append((q1, q2))
            continue
        raise Undecidable("J monotonicity within enclosure error")
    for q in qs:
        if J[q] - errs[q] < Fraction(q, A):
            if J[q] + errs[q] < Fraction(q, A):
                lower_bad.append(q)
            else:
                raise Undecidable("J >= q/A within enclosure error")
    return {"pass": not mono_bad and not lower_bad,
            "J": {str(q): float(J[q]) for q in qs},
            "q_over_A": {str(q): float(Fraction(q, A)) for q in qs},
            "monotone_failures": mono_bad, "lower_bound_failures": lower_bad,
            "enclosure_error_bound_2q2delta_log10": {str(q): log10_abs(errs[q]) for q in qs}}


def orbit_points(orbit: ic.CompletedOrbit, ns, P: int) -> tuple[list[int], Fraction]:
    pts = [ffloor(orbit.frac(n) * (1 << P)) for n in ns]
    return pts, orbit.frac_error() + Fraction(1, 1 << P)


def section_swt05(S: ic.Source, A: int = 200) -> dict:
    P = 256
    ns = range(A, 2 * A)
    true_orbit = ic.CompletedOrbit(2 * A, a=Fraction(0), b=Fraction(1))
    L = 2 * A + 16
    shadow_seed = -Fraction(S.U[L], 16 ** L)  # s_B = -P_L, P_L = 16^-L U_L(0)
    shadow_orbit = ic.CompletedOrbit(2 * A, a=shadow_seed, b=Fraction(1))
    # consistency of the shadow orbit with the source-only enclosure Y_n(s) = 16^(n-L) T_L
    tL_lo, tL_hi = ic.tail_interval(L)
    cons_bad = []
    for n in ns:
        f, err = shadow_orbit.frac(n), shadow_orbit.frac_error()
        y_lo, y_hi = Fraction(16 ** n, 16 ** L) * tL_lo, Fraction(16 ** n, 16 ** L) * tL_hi
        # frac in [f, f+err) mod 1 must meet [y_lo, y_hi] (allow wrap below 0)
        meets = (f <= y_hi and f + err >= y_lo) or (f - 1 <= y_hi and f - 1 + err >= y_lo)
        if not meets:
            cons_bad.append(n)
    out = {"A": A, "P_bits": P, "shadow_L": L,
           "shadow_orbit_consistent_with_source_tail": chk(cons_bad, A)}
    for name, orbit in (("true_seed", true_orbit), ("shadow_seed", shadow_orbit)):
        pts, delta = orbit_points(orbit, ns, P)
        out[name] = swt05b_check(pts, P, delta)
    out["pass"] = out["true_seed"]["pass"] and out["shadow_seed"]["pass"] and not cons_bad
    return out


# ============================================================ IAD-07 one-missing-place hijack

def hijack_construct(B: int, q: int = Q_HIJACK, M: int = M_HIJACK, k=None, K=None) -> dict:
    K = 2 * B if K is None else K
    need = M * 16 ** (K + 2)
    if k is None:
        k, Q = 1, q
        while Q < need:
            Q *= q
            k += 1
    Q = q ** k
    Mh = Q.bit_length() // 4 + 40
    while True:
        lo, hi, _ = x_interval(Mh)
        r_lo = ffloor(-hi * Q / M + Fraction(1, 2))
        r_hi = ffloor(-lo * Q / M + Fraction(1, 2))
        if r_lo == r_hi:
            break
        Mh += 64
    a = M * r_lo
    return {"B": B, "K": K, "q": q, "k": k, "Q": Q, "M": M, "a": a, "s": Fraction(a, Q), "Mh": Mh}


def spread_times(B: int, count: int = 40) -> list[int]:
    return sorted({(i * 2 * B) // count for i in range(count + 1)} | {B, 2 * B - 1})


def hijack_checks(S: ic.Source, hj: dict, primes: list[int], times: list[int], M_factors: dict,
                  modes=MODES, with_W: bool = True, ell_list=(1,), exclude_q: bool = True) -> dict:
    """IAD-07 items 1-3 for the seed in ``hj``.  ``exclude_q=False`` (mutation controls only)
    also compares the classes at the place q itself."""
    B, K, q, Q, M, a, s = hj["B"], hj["K"], hj["q"], hj["Q"], hj["M"], hj["a"], hj["s"]
    lo, hi, X = x_interval(hj["Mh"])
    pre = {
        "q_is_prime": ic.is_prime(q),
        "gcd_q_M_eq_1": gcd(q, M) == 1,
        "a_multiple_of_M": a % M == 0,
        "Qk_ge_M_16pow_K_plus_2": Q >= M * 16 ** (K + 2),
        "kernel_x_scaled_eq_machin": ic._x_scaled(hj["Mh"]) == X,
    }
    e_lo, e_hi = lo + s, hi + s  # x + s in (e_lo, e_hi)
    abs_up = max(abs(e_lo), abs(e_hi))
    item_abs = abs_up <= Fraction(M, 2 * Q)
    item_budget = Fraction(M, 2 * Q) <= Fraction(1, 2 * 16 ** (K + 2))
    bad3 = [n for n in range(K + 1) if 16 ** n * abs_up > Fraction(16 ** n, 2 * 16 ** (K + 2))]

    bad_i, bad_ii, bad_ii_class, bad_div, bad_census0, bad_census_s, bad_auth, bad_innov = ([] for _ in range(8))
    v_q_a = vp(Fraction(a), q) if a else None
    for n in times:
        U0 = S.U[n]
        diff = Fraction(16 ** n * a, Q)
        Us = U0 + diff
        for p in primes:
            if p == q and exclude_q:
                continue
            if ic.p_adic_component(Us, p) != ic.p_adic_component(U0, p):
                bad_i.append((n, p))
        if (16 ** n * a) % M:
            bad_div.append(n)
        for p, j in M_factors.items():
            if diff != 0 and vp(diff, p) < j:
                bad_ii.append((n, p))
            pj = p ** j
            if ic.p_adic_component(Us / pj, p) != ic.p_adic_component(U0 / pj, p):
                bad_ii_class.append((n, p))
        # census: den U_n(0) supported on primes <= 8n - 2; den U_n(s) = den U_n(0) * q^(k - v_q(a))
        d0 = U0.denominator
        for p in primes:
            if p > max(8 * n - 2, 1):
                break
            while d0 % p == 0:
                d0 //= p
        if d0 != 1:
            bad_census0.append(n)
        if a and Us.denominator != U0.denominator * Q // q ** min(v_q_a, hj["k"]):
            bad_census_s.append(n)
        Z = (Us - U0) / 16 ** n  # unwrapped authentication Z_n = 16^-n U_n(s) - P_n
        if not (Z == s and Z != 0):
            bad_auth.append(n)
        for ell in ell_list:
            if n + ell <= S.N:
                Us_l = S.U[n + ell] + 16 ** (n + ell) * s
                if not (Us_l - 16 ** ell * Us == S.U[n + ell] - 16 ** ell * U0 == S.innovation_direct(n, ell)):
                    bad_innov.append((n, ell))
    checks = {
        "preconditions": {"pass": all(pre.values()), **pre},
        "abs_x_plus_s_le_M_over_2Qk": {"pass": item_abs, "log10_abs_x_plus_s_upper": log10_abs(abs_up),
                                       "ratio_to_budget_half_16pow_minus_K_minus_2":
                                           float(abs_up * 2 * 16 ** (K + 2))},
        "M_over_2Qk_le_half_16pow_minus_K_minus_2": {"pass": item_budget},
        "item1_innovations_unchanged": chk(bad_innov, len(times) * len(ell_list)),
        "item2_i_QpZp_classes_equal_all_p_le_16B": chk(bad_i, len(times) * len(primes)),
        "item2_ii_16n_a_divisible_by_M": chk(bad_div, len(times)),
        "item2_ii_vp_difference_ge_j_for_pj_exactly_dividing_M": chk(bad_ii, len(times) * len(M_factors)),
        "item2_ii_class_mod_pj_equal": chk(bad_ii_class, len(times) * len(M_factors)),
        "item3_abs_Y_n_le_half_16pow_n_minus_K_minus_2_all_n_le_K": chk(bad3, K + 1),
        "census_den_U_n0_supported_on_p_le_8n_minus_2": chk(bad_census0, len(times)),
        "census_den_U_ns_eq_den_U_n0_times_q_power": chk(bad_census_s, len(times)),
        "authentication_Z_n_eq_s_ne_0": chk(bad_auth, len(times)),
    }
    W = {}
    if with_W:
        bad_w = []
        true_orbit = ic.CompletedOrbit(2 * B, a=Fraction(0), b=Fraction(1))
        for h in modes:
            ivs = []
            for n in range(B, 2 * B):
                t1, t2 = h * 16 ** n * e_lo, h * 16 ** n * e_hi
                ivs.append((min(t1, t2), max(t1, t2)))
            decided = None
            for prec in (320, 1024, 4096):
                with iv_precision(prec) as iv:
                    re, im = e_minus_one_sum(iv, ivs)
                    dev2 = (sq(iv, re) + sq(iv, im)) / (B * B)
                    bound = iv.pi * abs(h) / (3840 * B)
                    try:
                        decided = iv_le(dev2, bound * bound)
                    except Undecidable:
                        continue
                    dev_up = float(mp.mpf(iv.sqrt(dev2).b))
                    bound_lo = float(mp.mpf(bound.a))
                    re_mid, im_mid = float(mp.mpf(re.mid)), float(mp.mpf(im.mid))
                    break
            if decided is None:
                raise Undecidable(f"|W_B - 1| bound, B={B}, h={h}")
            if not decided:
                bad_w.append(h)
            with mp.workdps(30):
                acc = mp.mpc(0)
                for n in range(B, 2 * B):
                    f = true_orbit.frac(n)
                    acc += mp.expjpi(2 * h * (mp.mpf(f.numerator) / f.denominator))
                Wt = acc / B
            W[str(h)] = {
                "hijack_abs_W_minus_1_upper": dev_up,
                "hijack_W_minus_1_mid": [re_mid / B, im_mid / B],
                "bound_pi_h_over_3840B": bound_lo,
                "hijack_bound_holds": decided,
                "true_seed_W": [float(Wt.real), float(Wt.imag)],
                "true_seed_abs_W": float(abs(Wt)),
            }
        checks["item3_abs_W_B_minus_1_le_pi_h_over_3840B"] = chk(bad_w, len(modes))
    return {
        "B": B, "K": K, "q": q, "k": hj["k"], "v_q_a": v_q_a,
        "log10_Qk": log10_abs(Fraction(Q)), "log10_M": log10_abs(Fraction(M)),
        "n_times": len(times), "times_first_last": [times[0], times[-1]], "n_primes": len(primes),
        "checks": checks,
        "pass": all(c["pass"] for c in checks.values()),
        "W": W,
    }


def section_hijack(S: ic.Source, shells) -> dict:
    out = {}
    for B in shells:
        hj = hijack_construct(B)
        primes = [p for p in primes_upto(16 * B) if p != Q_HIJACK]
        ell0 = ell_pair(B)[0]
        out[str(B)] = hijack_checks(S, hj, primes, spread_times(B), M_HIJACK_FACTORS,
                                    ell_list=(1, ell0))
    return out


# ============================================================ IAD-08 Liouville wall

def check_81(y: Fraction, m: int, N: int, theta: int, h: int, eps=None) -> dict:
    """(8.1): |(1/N) sum_{n=m}^{m+N-1} e(h theta 16^n y) - 1| <= 2 pi |h| eps 16^N/(15N)."""
    if eps is None:
        eps = ic.dist_to_int(theta * 16 ** m * y)
    phases = [h * theta * 16 ** n * y for n in range(m, m + N)]
    if all(t.denominator == 1 for t in phases):  # left side exactly 0 <= right side
        return {"holds": True, "lhs_exactly_zero": True, "eps": short(eps),
                "rhs_lt_1": True if eps == 0 else None}
    for prec in (256, 1024, 4096):
        with iv_precision(prec) as iv:
            re, im = e_minus_one_sum(iv, [(t, t) for t in phases])
            lhs2 = (sq(iv, re) + sq(iv, im)) / (N * N)
            rhs = 2 * iv.pi * abs(h) * fiv(iv, eps) * 16 ** N / (15 * N)
            try:
                holds = iv_le(lhs2, rhs * rhs)
            except Undecidable:
                continue
            return {"holds": holds, "lhs_exactly_zero": False, "eps": short(eps),
                    "lhs_upper": float(mp.mpf(iv.sqrt(lhs2).b)), "rhs_lower": float(mp.mpf(rhs.a)),
                    "rhs_lt_1": bool(rhs.b < 1)}
    raise Undecidable("(8.1) comparison")


def synthetic_81_cases(n_cases: int = 100, seed: int = SEED + 8) -> list[dict]:
    rng = random.Random(seed)
    cases = []
    for i in range(n_cases):
        kind = i % 4
        ell = rng.randint(1, 4)
        theta = 1 if i % 2 == 0 else 16 ** ell - 1
        h = rng.choice((1, 2, 3, 5, 8, -1, -3))
        N = rng.randint(1, 24)
        mprime = rng.randint(0, 20)
        a = rng.randrange(16 ** mprime) if mprime else 0
        if kind == 0:  # informative: 16-adic part absorbed, tiny perturbation (right side < 1)
            m = rng.randint(mprime, mprime + 12)
            epsp = Fraction(rng.choice((-1, 1)) * rng.randint(1, 15), 16 ** (m + N + ell + rng.randint(2, 6)))
        elif kind == 1:  # pure 16-adic rational (eps may vanish exactly)
            m = rng.randint(0, mprime + 4)
            epsp = Fraction(0)
        elif kind == 2:  # generic rational: right side huge
            m = rng.randint(0, 30)
            epsp = Fraction(rng.randint(1, 10 ** 6), rng.randint(10 ** 6 + 1, 2 * 10 ** 6))
        else:  # periodic points (1/17-type, 1/5-type)
            m = rng.randint(0, 30)
            epsp = Fraction(rng.randint(1, 16), 17) if rng.random() < 0.5 else Fraction(rng.randint(1, 4), 5)
        cases.append({"y": Fraction(a, 16 ** mprime) + epsp, "m": m, "N": N, "theta": theta, "h": h,
                      "kind": kind})
    return cases


def section_iad08(wall_max: int, shells) -> tuple[dict, dict, dict]:
    cases = synthetic_81_cases()
    rows, bad = [], []
    for i, c in enumerate(cases):
        res = check_81(c["y"], c["m"], c["N"], c["theta"], c["h"])
        if not res["holds"]:
            bad.append(i)
        rows.append({"case": i, "kind": c["kind"], "m": c["m"], "N": c["N"], "h": c["h"],
                     "theta_is_1": c["theta"] == 1, **res})
    pr18 = {"pass": not bad, "n_cases": len(cases), "failures": bad,
            "n_rhs_lt_1": sum(1 for r in rows if r.get("rhs_lt_1")),
            "n_lhs_exactly_zero": sum(1 for r in rows if r["lhs_exactly_zero"]),
            "cases": rows}

    # Liouville-wall observable for the true pi, B = 1..wall_max (PR-2.8).
    orbit = ic.CompletedOrbit(wall_max)
    kernel_ok = ic._x_scaled(orbit.M) == x_scaled_machin(orbit.M)
    err = orbit.frac_error()
    best, arg, viol = None, None, []
    with mp.workdps(30):
        for B in range(1, wall_max + 1):
            f = orbit.frac(B)
            dist_lo, dist_hi = min(f, 1 - f - err), min(f + err, 1 - f)
            thr = Fraction(1, 256 * B)  # g(B) <= 2  <=>  ||16^B x|| >= 16^-2 / B
            if dist_lo >= thr:
                pass
            elif dist_hi < thr:
                viol.append(B)
            else:
                raise Undecidable(f"wall threshold at B={B}")
            dist = min(f, 1 - f)  # lower enclosure endpoint (relative error < 1e-50 here)
            g = -mp.log(mp.mpf(dist.numerator) / dist.denominator, 16) - mp.log(B, 16)
            if best is None or g > best:
                best, arg = g, B
    pr28 = {"predicted": "max_{1<=B<=%d} g(B) <= 2" % wall_max, "observed_max_g": float(best),
            "observed_argmax_B": arg, "n_B_with_g_gt_2": len(viol), "B_with_g_gt_2": viol[:20],
            "met": not viol, "kernel_x_scaled_eq_machin": kernel_ok,
            "g_definition": "g(B) = -log_16 ||16^B x|| - log_16 B (lower enclosure endpoint, 1e-57 relative)"}

    # PR-3: x' = 1/17.
    xp = Fraction(1, 17)
    norm_bad = [B for B in range(0, 201) if ic.dist_to_int(16 ** B * xp) != Fraction(1, 17)]
    means = {}
    mean_bad = []
    for B in shells:
        for h in MODES:
            ivs = [(h * 16 ** n * xp, h * 16 ** n * xp) for n in range(B, 2 * B)]
            with iv_precision(256) as iv:
                re, im = e_minus_one_sum(iv, ivs)
                mean_re, mean_im = 1 + re / B, im / B
                target = iv.cos(2 * iv.pi * h / 17)
                dev = abs(mean_re - target) + abs(mean_im)
                ok = iv_le(dev, fiv(iv, Fraction(1, 10 ** 12))) if B % 2 == 0 else None
                means[f"B{B}_h{h}"] = {"B_even": B % 2 == 0, "mean": [float(mp.mpf(mean_re.mid)),
                                                                     float(mp.mpf(mean_im.mid))],
                                       "cos_2pi_h_over_17": float(mp.mpf(target.mid)),
                                       "abs_deviation_upper": float(mp.mpf(dev.b)), "asserted": ok}
                if B % 2 == 0 and not ok:
                    mean_bad.append((B, h))
    pr3_17 = {"norm_eq_1_over_17_all_B_le_200": chk(norm_bad, 201),
              "shell_mean_eq_cos_even_B": chk(mean_bad, sum(1 for B in shells if B % 2 == 0) * len(MODES)),
              "means": means,
              "pass": not norm_bad and not mean_bad}
    return pr18, pr28, pr3_17


# ============================================================ IAD-09 fresh primes

def birth_formula(p: int) -> tuple[int, str]:
    c = p % 8
    if c == 1:
        return (p + 7) // 8, "8m-7"
    if c == 5:
        return (p + 3) // 8, "8m-3"
    if c in (3, 7):
        return (p + 1) // 4, "4m-1"
    raise ValueError("odd prime >= 7 required")


def factor_values(m: int) -> tuple[int, int, int, int]:
    return 8 * m - 7, 2 * m - 1, 8 * m - 3, 4 * m - 1


def first_events_direct(p_list) -> dict[int, tuple[int, tuple[str, ...]]]:
    """Brute force: first m >= 1 with p | (8m-7)(2m-1)(8m-3)(4m-1), and which factors vanish."""
    out = {}
    for p in p_list:
        m = 1
        while (8 * m - 7) * (2 * m - 1) * (8 * m - 3) * (4 * m - 1) % p:
            m += 1
        out[p] = (m, tuple(lbl for lbl, f in zip(FACTOR_LABELS, factor_values(m)) if f % p == 0))
    return out


def event_table(m_max: int, p_max: int) -> dict[int, list[tuple[int, tuple[str, ...]]]]:
    """Second route: all events m <= m_max of primes 7 <= p <= p_max by factorization."""
    spf = spf_table(8 * m_max)
    ev: dict[int, list] = {}
    for m in range(1, m_max + 1):
        hits: dict[int, list[str]] = {}
        for lbl, f in zip(FACTOR_LABELS, factor_values(m)):
            for p in prime_factors(f, spf):
                if 7 <= p <= p_max:
                    hits.setdefault(p, []).append(lbl)
        for p, lbls in hits.items():
            ev.setdefault(p, []).append((m, tuple(lbls)))
    return ev


def births_check(B: int, direct: dict, ev: dict, formula=birth_formula) -> dict:
    p_max, horizon = 16 * B + 200, 3 * B
    primes = sorted(p for p in direct if p <= p_max)
    bad_birth, bad_route, bad_one, bad_sep = [], [], [], []
    n_events, min_slack = 0, None
    for p in primes:
        m_f, pole = formula(p)
        m_d, lbls = direct[p]
        if m_d != m_f or lbls != (pole,):
            bad_birth.append((p, m_d, m_f))
        evs = [(m, l) for (m, l) in ev.get(p, []) if m <= horizon]
        if (m_d <= horizon and (not evs or evs[0][0] != m_d)) or (m_d > horizon and evs):
            bad_route.append(p)
        for m, l in evs:
            n_events += 1
            if len(l) != 1:
                bad_one.append((p, m))
        for (m1, _), (m2, _) in zip(evs, evs[1:]):
            slack = 8 * (m2 - m1) - (p - 5)
            min_slack = slack if min_slack is None else min(min_slack, slack)
            if slack < 0:
                bad_sep.append((p, m1, m2))
    return {
        "p_range": [7, p_max], "event_horizon": horizon, "n_primes": len(primes), "n_events": n_events,
        "birth_formula": chk(bad_birth, len(primes)),
        "direct_vs_factorization_route": chk(bad_route, len(primes)),
        "exactly_one_factor_per_event": chk(bad_one, n_events),
        "separation_ge_(p-5)/8": chk(bad_sep, n_events),
        "min_separation_slack_8dm_minus_p_plus_5": min_slack,
        "pass": not (bad_birth or bad_route or bad_one or bad_sep),
    }


def rho_expected(pole: str, k: int, p: int) -> int:
    if pole == "8m-7":
        return 4 * pow(16, k, p) % p
    if pole == "8m-3":
        return -pow(16, k, p) % p
    if pole == "4m-1":
        return -pow(16, k, p) * pow(2, -1, p) % p
    raise ValueError(pole)


def fresh_window(S: ic.Source, n: int, ell: int, births_fn=ic.births_at, rho_fn=rho_expected,
                 events=None) -> dict | None:
    """IAD-09(b)-(d) on the window (n, n+ell]; None if no prime is born in it."""
    births = [(j, p, pole, c) for j in range(1, ell + 1) for (p, pole, c) in births_fn(n + j)]
    if not births:
        return None
    D = S.U[n + ell] - S.U[n]
    rows = []
    for j, p, pole, c in births:
        k = ell - j
        comp = ic.p_adic_component(D, p)
        row = {
            "n": n, "ell": ell, "j": j, "p": p, "pole": pole,
            "U_n_p_integral": S.U[n].denominator % p != 0,
            "v_p_eq_minus_1": vp(D, p) == -1,
            "component_eq_rho_over_p": comp.denominator == p and comp.numerator % p == rho_fn(pole, k, p) % p,
            "pole_matches_class_mod_8": p % 8 in POLE_CLASSES.get(pole, ()),
            "coefficient_matches_pole": c == POLE_COEFF.get(pole),
            "no_other_event_in_window": True if events is None else
            [m for (m, _) in events.get(p, []) if n < m <= n + ell] == [n + j],
        }
        # (d) weld: fresh pole term t = c 16^k / p with |c| 16^k < p.
        cc = POLE_COEFF[pole] if pole in POLE_COEFF else c
        t = cc * 16 ** k / p
        if abs(cc) * 16 ** k < p:
            comp_t = ic.p_adic_component(t, p)
            row["weld_applicable"] = True
            row["weld_literal_p_component_eq_real_mod_1"] = comp_t == ffrac(t)
            row["weld_product_formula_p_plus_2_component"] = ffrac(comp_t + ic.p_adic_component(t, 2)) == ffrac(t)
            row["weld_integral_coefficient"] = (cc * 16 ** k).denominator == 1
        else:
            row["weld_applicable"] = False
        rows.append(row)
    return {"D": D, "rows": rows, "birth_primes": [b[1] for b in births]}


def ell_pair(B: int) -> tuple[int, int]:
    """(ceil(2.25 log16 B), floor(4.5 log16 B)) by exact integer comparisons."""
    l0 = 0
    while 16 ** (4 * l0) < B ** 9:
        l0 += 1
    l1 = 0
    while 16 ** (2 * (l1 + 1)) <= B ** 9:
        l1 += 1
    return l0, l1


ROW_CHECKS = ("U_n_p_integral", "v_p_eq_minus_1", "component_eq_rho_over_p", "pole_matches_class_mod_8",
              "coefficient_matches_pole", "no_other_event_in_window")


def section_fresh_primes(S: ic.Source, shells) -> dict:
    Bmax = max(shells)
    p_cap = 16 * Bmax + 200
    p_list = [p for p in primes_upto(p_cap) if p >= 7]
    direct = first_events_direct(p_list)
    ev = event_table(3 * Bmax, p_cap)
    born_brute: dict[int, list[int]] = {}
    for p, (m, _) in direct.items():
        born_brute.setdefault(m, []).append(p)
    out = {"p_cap": p_cap, "event_table_m_max": 3 * Bmax, "shells": {}}
    weld_literal_failures, weld_rows_all = [], 0
    for B in shells:
        shell = {"a_births": births_check(B, direct, ev)}
        ells = ell_pair(B)
        shell["ells"] = list(ells)
        # births_at agrees with brute force on the whole range used
        m_lo, m_hi = B, 2 * B + max(ells)
        bad_ba = [m for m in range(m_lo, m_hi + 1)
                  if sorted(p for p, _, _ in ic.births_at(m)) != sorted(born_brute.get(m, []))]
        shell["births_at_eq_brute_force"] = chk(bad_ba, m_hi - m_lo + 1)
        pr2_rows, b_ok, c_ok = {}, True, True
        for ell in ells:
            bad_b, bad_c, n_births, n_windows_with_births = [], [], 0, 0
            weld = {"applicable": 0, "literal_fail": 0, "literal_fail_examples": [],
                    "product_formula_fail": 0, "integral_coeff_literal_fail": 0,
                    "fail_pole_age_counts": {}}
            min_norm, min_info = None, None
            for n in range(B - 1, 2 * B + 1):
                res = fresh_window(S, n, ell, events=ev)
                if res is None:
                    continue
                n_windows_with_births += 1
                for row in res["rows"]:
                    n_births += 1
                    if not all(row[c] for c in ROW_CHECKS):
                        bad_b.append((n, row["p"], [c for c in ROW_CHECKS if not row[c]]))
                    if row["weld_applicable"]:
                        weld["applicable"] += 1
                        if not row["weld_literal_p_component_eq_real_mod_1"]:
                            weld["literal_fail"] += 1
                            key = f"{row['pole']}_age{ell - row['j']}"
                            weld["fail_pole_age_counts"][key] = weld["fail_pole_age_counts"].get(key, 0) + 1
                            if len(weld["literal_fail_examples"]) < 5:
                                weld["literal_fail_examples"].append(
                                    {"n": n, "ell": ell, "j": row["j"], "p": row["p"], "pole": row["pole"]})
                            if row["weld_integral_coefficient"]:
                                weld["integral_coeff_literal_fail"] += 1
                        if not row["weld_product_formula_p_plus_2_component"]:
                            weld["product_formula_fail"] += 1
                D = res["D"]
                for h in MODES:
                    hD = h * D
                    if any(h % p for p in res["birth_primes"]):
                        if hD.denominator == 1:
                            bad_c.append((n, h))
                            continue
                        nrm = ic.dist_to_int(hD)
                        if min_norm is None or nrm < min_norm:
                            min_norm, min_info = nrm, (n, h, hD.denominator)
            weld_rows_all += weld["applicable"]
            weld_literal_failures.extend(weld["literal_fail_examples"])
            # (e) birth mass over n in [B, 2B)
            counts = [sum(len(ic.births_at(n + j)) for j in range(1, ell + 1)) for n in range(B, 2 * B)]
            obs = Fraction(sum(counts), B)
            zero_frac = Fraction(sum(1 for c in counts if c == 0), B)
            with iv_precision(96) as iv:
                acc = iv.mpf(0)
                for m in range(B, 2 * B):
                    acc += 4 / iv.log(8 * m) + 2 / iv.log(4 * m)
                pred = ell * acc / B
                lo_ok = iv_le(fiv(iv, Fraction(4, 5)) * pred, fiv(iv, obs))
                hi_ok = iv_le(fiv(iv, obs), fiv(iv, Fraction(6, 5)) * pred)
                pred_f = float(mp.mpf(pred.mid))
            pr2_rows[str(ell)] = {"predicted_mean_births": pred_f, "observed_mean_births": float(obs),
                                  "ratio": float(obs) / pred_f, "met_within_20pct": lo_ok and hi_ok,
                                  "fraction_windows_zero_births": float(zero_frac)}
            shell[f"ell_{ell}"] = {
                "n_range": [B - 1, 2 * B], "n_windows_with_births": n_windows_with_births,
                "n_births_checked": n_births,
                "b_exact_component": chk(bad_b, n_births),
                "c_inequation_hD_not_integer": chk(bad_c, n_windows_with_births * len(MODES)),
                "c_min_norm_hD": None if min_norm is None else {
                    "log10_min_norm": log10_abs(min_norm), "at_n": min_info[0], "at_h": min_info[1],
                    "log10_den_hD_at_min": log10_abs(Fraction(min_info[2])),
                    "log10_one_over_den": -log10_abs(Fraction(min_info[2]))},
                "d_weld": weld,
            }
            b_ok &= not bad_b
            c_ok &= not bad_c
        shell["PR-2.7"] = pr2_rows
        shell["pr19_pass"] = shell["a_births"]["pass"] and shell["births_at_eq_brute_force"]["pass"] and b_ok
        shell["c_pass"] = c_ok
        out["shells"][str(B)] = shell
    out["sampling"] = "full: every n in [B-1, 2B] (births in [B, 2B+ell]) for both ells; no sampling"
    out["weld_literal_failure_examples"] = weld_literal_failures[:10]
    return out


# ============================================================ AT-07 seven-pole null control

def load_at07_transport():
    spec = importlib.util.spec_from_file_location("at07_transport", AT07_TRANSPORT)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def at07_section(n_max: int = 400, B: int = 200, Z=AT07_Z) -> dict:
    t = load_at07_transport()
    offsets = tuple(range(1, 9))

    def z(n):
        return t.source(n, Z, offsets)

    cross = [n for n in range(1, n_max + 3)
             if Z == AT07_Z and z(n) != t.source(n, (8, 4, 4, -1), t.REFLECTED) - 2 * ic.r(n)]
    cross_r = [n for n in range(1, n_max + 3) if t.source(n) != ic.r(n)]
    E = [Fraction(0)]
    for n in range(1, n_max + 1):
        E.append(16 * E[-1] + z(n))
    bad_bounds = [n for n in range(1, n_max + 1) if not (-Fraction(1, 8 * n + 1) < E[n] < 0)]
    depth_bad, depth_n = [], 0
    for p in primes_upto(8 * n_max):
        if p == 2:
            continue
        a = 1
        while (p ** a + 7) // 8 <= n_max:
            Q = p ** a
            n = (Q + 7) // 8
            depth_n += 1
            if E[n] == 0 or vp(E[n], p) != -a:
                depth_bad.append((p, a))
            a += 1
    zs = [None] + [z(n) for n in range(1, n_max + 3)]
    pos_fail = [n for n in range(1, n_max + 1) if zs[n] <= 0]
    mono_fail = [n for n in range(1, n_max + 1) if not zs[n] > zs[n + 1]]
    conv_fail = [n for n in range(1, n_max + 1) if not zs[n] - 2 * zs[n + 1] + zs[n + 2] > 0]
    W = {}
    if B and 2 * B - 1 <= n_max:
        with mp.workdps(30):
            for h in MODES:
                acc = mp.mpc(0)
                for n in range(B, 2 * B):
                    acc += mp.expjpi(2 * h * (mp.mpf(E[n].numerator) / E[n].denominator))
                w = acc / B
                W[str(h)] = {"W": [float(w.real), float(w.imag)], "abs_W_minus_1": float(abs(w - 1)),
                             "rigorous_majorant_2pi_h_over_8B_plus_1": float(2 * mp.pi * h / (8 * B + 1))}
    return {
        "source": "research/2026-10-30/arithmetic_barrier/arithmetic/transport.py (imported); "
                  "Z transcribed from test_transport.py:184,200",
        "Z": list(Z), "n_max": n_max,
        "z_eq_w_minus_2r": chk(cross, n_max + 2),
        "transport_bbp_source_eq_iad_core_r": chk(cross_r, n_max + 2),
        "bounds_minus_1_over_8n_plus_1_lt_E_n_lt_0": chk(bad_bounds, n_max),
        "conductor_depth_v_p_E_ceil_Q_over_8_eq_minus_a": chk(depth_bad, depth_n),
        "z_positive_failures": pos_fail[:20], "z_positive_on_all": not pos_fail,
        "z_strictly_decreasing_failures": mono_fail[:20], "z_monotone_on_all": not mono_fail,
        "z_strictly_convex_failures": conv_fail[:20], "z_convex_on_all": not conv_fail,
        "z_1": str(zs[1]),
        "shell_mean_e_hE_n_B": B, "W": W,
        "note": "IAD-04 is not asserted for this forcing",
    }


# ===================================================================================== main

def run(quick: bool) -> tuple[dict, bool]:
    shells = (HOLDOUT_SHELLS[0],) if quick else HOLDOUT_SHELLS
    seam_max = QUICK_SEAM_MAX if quick else SEAM_MAX
    wall_max = QUICK_SEAM_MAX if quick else SEAM_MAX
    n_src = seam_max + 100
    S = ic.Source(max(n_src, 2 * max(shells) + 32, 2 * CONTROL_HORIZON + 120))

    R: dict = {"meta": {
        "probe": "probe_arithmetic.py", "mode": "quick" if quick else "full",
        "baseline": "Main XXIV 071ce1e0 + IAD pre-probe commit e3f4111b",
        "mpmath_version": mp.__version__, "guard_hex": ic.GUARD_HEX, "source_horizon": S.N,
        "holdout_shells": list(shells), "modes_h": list(MODES), "seed_base": SEED,
        "pi_routes": "Machin integer arithmetic (decisions) + mpmath (digit cross-check) + "
                     "iad_core._x_scaled (kernel cross-check)",
    }}

    # ---- PR-1.10 / PR-2.6 / SWT-04 / seam controls
    seam = true_seed_seam(S, seam_max, n_src)
    coherent = coherent_seed_control(S)
    forced = {f"a{a}": forced_seam_control(S, FORCED_SEAM_N0, a) for a in (0, 3)}
    pr110_pass = (all(c["pass"] for c in seam["checks"].values()) and coherent["pass"]
                  and all(f["pass"] for f in forced.values()))
    # ---- PR-1.11
    streams = {str(SEED + 11 + i): swt01_check(*planted_stream(SEED + 11 + i)[:2]) for i in range(5)}
    pr111_pass = all(s["pass"] for s in streams.values())
    # ---- PR-1.7
    hijack = section_hijack(S, shells)
    pr17_pass = all(h["pass"] for h in hijack.values())
    # ---- PR-1.8, PR-2.8, PR-3 (1/17)
    pr18, pr28, pr3_17 = section_iad08(wall_max, shells)
    # ---- PR-1.9 / PR-2.7 / IAD-09 (c), (d)
    fresh = section_fresh_primes(S, shells)
    pr19_pass = all(sh["pr19_pass"] for sh in fresh["shells"].values())
    # ---- SWT-05(B)
    swt05 = section_swt05(S, 200)
    # ---- AT-07
    at07 = at07_section()

    R["PR-1"] = {
        "PR-1.7": {"pass": pr17_pass, "shells": hijack,
                   "scope": "IAD-07 items 1-3 exactly; spread of >= 41 times in [0, 2B]; all primes p <= 16B"},
        "PR-1.8": pr18,
        "PR-1.9": {"pass": pr19_pass,
                   "shells": {B: {"a_births": sh["a_births"], "births_at_eq_brute_force": sh["births_at_eq_brute_force"],
                                  **{k: {"b_exact_component": v["b_exact_component"], "n_range": v["n_range"],
                                         "n_births_checked": v["n_births_checked"]}
                                     for k, v in sh.items() if k.startswith("ell_")},
                                  "ells": sh["ells"]}
                              for B, sh in fresh["shells"].items()},
                   "sampling": fresh["sampling"], "p_cap": fresh["p_cap"]},
        "PR-1.10": {"pass": pr110_pass, "true_seed": {k: v for k, v in seam.items() if k not in ("frequencies",)},
                    "control_coherent_seed": coherent, "control_forced_seam": forced},
        "PR-1.11": {"pass": pr111_pass, "streams": streams,
                    "design": "length 20000 over 16 letters, round(N^(1/2)) = 141 planted edits, k <= 3, "
                              "N in {1000, 5000, 10000, 19998}"},
    }
    holdout_run = seam_max > SEAM_CALIBRATION_MAX
    cts = seam["counts"]
    R["PR-2"] = {
        "PR-2.6": {"predicted": "zero eps_n = 1 and zero kappa_n = 16 for 1301 <= n <= 3200",
                   "observed": {"eps_events_holdout": cts["eps_events_holdout"],
                                "carry16_holdout": cts["carry16_holdout"],
                                "eps_events_calibration": cts["eps_events_calibration"],
                                "carry16_calibration": cts["carry16_calibration"]} if holdout_run else
                   "holdout range not run in quick mode",
                   "met": (cts["eps_events_holdout"] == 0 and cts["carry16_holdout"] == 0) if holdout_run else None},
        "PR-2.7": {"predicted": "mean births in (n, n+ell] within 20% of ell * mean_m[4/ln(8m) + 2/ln(4m)]",
                   "observed": {B: sh["PR-2.7"] for B, sh in fresh["shells"].items()},
                   "met": all(r["met_within_20pct"] for sh in fresh["shells"].values()
                              for r in sh["PR-2.7"].values())},
        "PR-2.8": {"predicted": pr28["predicted"], "observed": {k: v for k, v in pr28.items() if k not in
                                                                ("predicted", "met")}, "met": pr28["met"]},
    }
    R["PR-3"] = {
        "x_prime_1_over_17": pr3_17,
        "AT-07_seven_pole_null": at07,
        "hijack_seed_passes_PR-1.7": pr17_pass,
        "coherent_seed_seam_item5_expected_failure": coherent["item5_expected_failure"],
    }
    weld_fail = sum(v["d_weld"]["literal_fail"] for sh in fresh["shells"].values()
                    for k, v in sh.items() if k.startswith("ell_"))
    weld_pf_fail = sum(v["d_weld"]["product_formula_fail"] for sh in fresh["shells"].values()
                       for k, v in sh.items() if k.startswith("ell_"))
    weld_int_fail = sum(v["d_weld"]["integral_coeff_literal_fail"] for sh in fresh["shells"].values()
                        for k, v in sh.items() if k.startswith("ell_"))
    R["additional_theorem_checks"] = {
        "note": "theorem-grade checks outside the preregistered PR-1 scope; recorded, not exit-gating",
        "IAD-09c_inequation": {"pass": all(sh["c_pass"] for sh in fresh["shells"].values()),
                               "per_shell": {B: {k: {"c_inequation_hD_not_integer": v["c_inequation_hD_not_integer"],
                                                     "c_min_norm_hD": v["c_min_norm_hD"]}
                                                 for k, v in sh.items() if k.startswith("ell_")}
                                             for B, sh in fresh["shells"].items()}},
        "IAD-09d_weld_literal": {"pass": weld_fail == 0, "n_literal_failures": weld_fail,
                                 "per_shell": {B: {k: v["d_weld"] for k, v in sh.items() if k.startswith("ell_")}
                                               for B, sh in fresh["shells"].items()},
                                 "examples": fresh["weld_literal_failure_examples"]},
        "IAD-09d_weld_integral_coefficient_cases": {"pass": weld_int_fail == 0,
                                                    "n_failures": weld_int_fail},
        "IAD-09d_weld_product_formula_p_plus_2": {"pass": weld_pf_fail == 0, "n_failures": weld_pf_fail},
        "SWT-04_inequality": seam["swt04"],
        "SWT-03_seam_density_bound": seam["seam_density"],
        "SWT-05B_near_pair_energy": swt05,
    }
    findings = []
    if weld_fail:
        findings.append({
            "claim": "IAD-09(d)",
            "statement_tested": "for a fresh pole term c 16^k/p with |c| 16^k < p, the class in Q_p/Z_p equals "
                                "the real term reduced mod 1",
            "result": "FAILS literally",
            "counterexample_class": "pole 4m-1 (c = -1/2) at age k = 0: term -1/(2p); Q_p/Z_p class (p-1)/(2p), "
                                    "real value mod 1 (2p-1)/(2p); they differ by the 2-adic component 1/2",
            "n_failures": weld_fail, "examples": fresh["weld_literal_failure_examples"][:5],
            "holds_when": "c 16^k is an integer (all poles at age k >= 1; poles 8m-7, 8m-3 at all ages); "
                          "the product-formula form {t}_p + {t}_2 = t mod 1 holds in every instance"})
    R["theorem_statement_findings"] = findings
    R["observations"] = {
        "seam_frequencies": seam["frequencies"],
        "hijack_vs_true_W": {B: h["W"] for B, h in hijack.items()},
    }
    R["scope_notes"] = [
        "PR-1.7: (i)/(ii) at a spread of 41-43 times in [0, 2B] (every multiple of 2B/40 plus B, 2B-1), "
        "all primes p <= 16B; (iii) at every n <= K; W bound by rigorous interval arithmetic.",
        "PR-1.9: births with beta(p) in [B, 2B+ell] (n in [B-1, 2B]) - a superset of the brief's n in [B, 2B); "
        "birth mass (PR-2.7) uses n in [B, 2B) only.",
        "PR-1.10: n <= %d; eps decided from tail enclosures and from the Machin enclosure of x (must agree)."
        % seam_max,
        "IAD-09(c)/(d), SWT-04, SWT-05(B) and the seam-density bound are outside the preregistered PR-1 table.",
    ]
    pr1_pass = all(v["pass"] for v in R["PR-1"].values())
    R["PR-1_all_pass"] = pr1_pass
    return R, pr1_pass


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--quick", action="store_true", help="smallest shell only, seam range n <= 400")
    ap.add_argument("--out", default=None, help="output JSON (default: RESULTS_arithmetic.json in full mode, "
                                                "nothing in quick mode)")
    args = ap.parse_args(argv)
    R, ok = run(args.quick)
    out = args.out or (None if args.quick else str(HERE / "RESULTS_arithmetic.json"))
    if out:
        Path(out).write_text(json.dumps(R, sort_keys=True, indent=1) + "\n")
    for key, val in R["PR-1"].items():
        print(f"{key}: {'PASS' if val['pass'] else 'FAIL'}")
    for key, val in R["PR-2"].items():
        print(f"{key}: met={val['met']}")
    for f in R["theorem_statement_findings"]:
        print(f"FINDING {f['claim']}: {f['result']} ({f['n_failures']} instances)")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
