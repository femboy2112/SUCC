#!/usr/bin/env python3
"""Probe for CARRY_FLUX.md (ZSC-01..07), following PREREGISTRATION_ZSC.md.

Theorem-grade checks ZC-1..ZC-11 are decided by exact rational arithmetic, or by
floating evaluation of e(t) after exact reduction modulo one with tolerance TOL.
Predictions ZP-1..ZP-5 are empirical and are reported as met or missed.  The
probe writes a compact RESULTS_zsc.json and exits non-zero iff a theorem-grade
check or a mutation control fails.  It changes the status of no open claim.

    python probe_zsc.py            full run (calibration + holdout shells)
    python probe_zsc.py --quick    calibration shells only (used by the unit tests)
"""
from __future__ import annotations

import json
import math
import random
import sys
from fractions import Fraction
from pathlib import Path

_HERE = Path(__file__).resolve().parent
if str(_HERE) not in sys.path:
    sys.path.insert(0, str(_HERE))

import iad_core as ic  # noqa: E402
import zsc_core as zc  # noqa: E402

F = Fraction
TOL = 1e-9
CAL, HOLD = (64, 128), (243, 420, 811, 1210)
MODES = (1, 3, 15, 17)
SEED = 2026111102
PI = math.pi
TRUNC_ERR = F(1, 16 ** zc.TRUNC)


class Tally:
    def __init__(self):
        self.n, self.bad = 0, []

    def ok(self, cond: bool, what):
        self.n += 1
        if not cond and len(self.bad) < 5:
            self.bad.append(str(what))
        elif not cond:
            self.bad.append("...")
        return cond

    def out(self, **extra):
        return {"checked": self.n, "failures": len(self.bad), "first_failures": self.bad[:5], **extra}


def fracs_of(d: list[int], n_max: int) -> list[Fraction]:
    return [zc.frac_from_digits(d, n) for n in range(n_max)]


def phases(fr: list[Fraction], h: int) -> list[complex]:
    return [zc.e_of(h * f) for f in fr]


def prefix(ph: list[complex]) -> list[complex]:
    out, s = [0j], 0j
    for z in ph:
        s += z
        out.append(s)
    return out


def shell(pre: list[complex], B: int) -> complex:
    return (pre[2 * B] - pre[B]) / B


def cB(d: list[int], B: int) -> Fraction:
    return F(zc.changes(d, B, 2 * B), B)


# ---------------------------------------------------------------- ZC-1 / ZC-2  (ZSC-01)
def check_stretch(fr, pre, B, h, tally, const_shift: int = 0) -> int:
    """(1.1) on a grid of (m, N).  Returns the number of non-trivial instances.
    ``const_shift`` = 1 is the mutation ZM-2."""
    reW = shell(pre, B).real
    nontrivial = 0
    for m in sorted({B + j * max(1, B // 8) for j in range(8)} | {B}):
        if m >= 2 * B:
            continue
        eps = ic.dist_to_int(fr[m]) + TRUNC_ERR          # upper bound for ||16^m xi||
        Ns = sorted({1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, B // 2, B - 3,
                     B - 1, B, 2 * B - m})
        for N in Ns:
            if N < 1 or m + N > 2 * B:
                continue
            log_err = math.log(2 * PI * abs(h) / (15 * B)) + N * math.log(16) \
                + (math.log(eps.numerator) - math.log(eps.denominator))
            if log_err > 3:                               # right side below -1: trivially true
                continue
            rhs = (2 * N - B + const_shift) / B - math.exp(log_err)
            nontrivial += 1
            tally.ok(reW >= rhs - TOL, ("stretch", B, h, m, N, reW, rhs))
    return nontrivial


def check_law(fr, pre, h, B0, Bmax, tally) -> dict:
    """Theorem (1.2) with the hypothesis verified on B0 <= B <= Bmax."""
    savings = {B: 1 - shell(pre, B).real for B in range(B0, Bmax + 1)}
    eta = min(savings.values())
    out = {"eta_min": eta, "argmin_B": min(savings, key=savings.get), "m_checked": 0}
    if eta <= 1e-6:
        return out
    expo = (2 - eta) / (2 + eta)
    m_lo = max(2 * B0, math.ceil((2 + eta) / eta))
    for m in range(m_lo, Bmax + 1):
        dist = ic.dist_to_int(fr[m]) + TRUNC_ERR
        lhs = (math.log(dist.numerator) - math.log(dist.denominator)) / math.log(16)
        rhs = math.log(15 * eta / (512 * PI * abs(h))) / math.log(16) - expo * m
        out["m_checked"] += 1
        tally.ok(lhs >= rhs - 1e-9, ("law", h, m, lhs, rhs))
    return out


def synthetic_near_dyadic(rng, count=40):
    cases = []
    for _ in range(count):
        B = rng.choice((16, 24, 32, 48, 64))
        m = rng.randrange(B, 2 * B - 1)
        N0 = rng.randrange(1, 2 * B - m + 6)
        d = [rng.randrange(16) for _ in range(2 * B + 8 + zc.TRUNC)]
        fill = rng.choice((0, 15))
        for n in range(m, min(len(d), m + N0)):
            d[n] = fill
        cases.append((B, d))
    return cases


def section_zsc01(strings: dict, shells, quick: bool) -> dict:
    t1, t2, nontriv = Tally(), Tally(), 0
    for name, (d, fr) in strings.items():
        for h in (1, 3, 15):
            pre = prefix(phases(fr, h))
            for B in shells:
                if 2 * B <= len(fr):
                    nontriv += check_stretch(fr, pre, B, h, t1)
    rng = random.Random(SEED + 1)
    for B, d in synthetic_near_dyadic(rng):
        fr = fracs_of(d, 2 * B + 2)
        for h in (1, 2):
            nontriv += check_stretch(fr, prefix(phases(fr, h)), B, h, t1)
    law, Bmax = {}, (256 if quick else 2048)
    for name in ("xi_1/4", "xi_1/2", "xi_3/4", "random_a", "W3"):
        d, fr = strings[name]
        for h in (1,):
            pre = prefix(phases(fr, h))
            law[name] = check_law(fr, pre, h, 32, min(Bmax, len(fr) // 2), t2)
    sharp = {}
    for lam in (F(1, 4), F(1, 2), F(3, 4)):
        key = f"xi_{lam}"
        sharp[key] = {"observed_min_saving": law[key]["eta_min"],
                      "limit_formula_1.978(1-l)/(1+l)": (1 - math.cos(14 * PI / 15)) * float((1 - lam) / (1 + lam)),
                      "theorem_ceiling_2(1-l)/(1+l)": 2 * float((1 - lam) / (1 + lam))}
    return {"ZC-1_stretch_lemma": t1.out(nontrivial_instances=nontriv),
            "ZC-2_law": t2.out(per_string=law), "remark4_near_sharpness_OBSERVED": sharp}


# ---------------------------------------------------------------- ZC-3 / ZC-4  (ZSC-02)
def check_locality(d, fr, tally, threshold=F(1, 256)) -> None:
    for n in range(len(fr) - 6):
        t = zc.dist15(fr[n])
        for k in range(1, 5):
            if all(d[n + i] == d[n] for i in range(k)):
                tally.ok(t <= F(15, 16 ** k) + 15 * TRUNC_ERR, ("loc1", n, k))
        if t + 15 * TRUNC_ERR < threshold:
            tally.ok(d[n] == d[n + 1], ("loc2", n))


def check_rung(d, fr, B, tally) -> dict:
    c = cB(d, B)
    w15 = shell(prefix(phases(fr[:2 * B], 15)), B)
    w1 = shell(prefix(phases(fr[:2 * B], 1)), B)
    s15 = 1 - w15.real
    tally.ok(s15 >= float(c) / 3321 - TOL, ("a", B))
    for k in (2, 3, 4):
        tally.ok(s15 <= 2 * (k - 1) * (float(c) + (k - 1) / B) + 450 * PI ** 2 * 16.0 ** (-2 * k) + TOL,
                 ("b", B, k))
    tally.ok(abs(w1) <= 1 - (float(c) - 1 / B) / 65793 + TOL, ("c", B))
    return {"c_B": float(c), "1-ReW15": s15, "absW1": abs(w1)}


def section_zsc02(strings: dict, shells) -> dict:
    t3, t4, table = Tally(), Tally(), {}
    for name, (d, fr) in strings.items():
        check_locality(d, fr, t3)
        table[name] = {str(B): check_rung(d, fr, B, t4) for B in shells if 2 * B + 6 <= len(fr)}
    return {"ZC-3_locality": t3.out(), "ZC-4_rung_inequalities": t4.out(), "table": table}


# ---------------------------------------------------------------- ZC-5 / ZC-6  (ZSC-03)
def renewal_direct(tally, n_values, extra: int = 0) -> None:
    """Start from every state x_n in [1 - r(n+1)/16, 1) on a grid; the next J(n)+extra carries
    after the 16 must be 0.  extra = 3 is the mutation ZM-3."""
    for n in n_values:
        rn1 = ic.r(n + 1)
        for th in (F(1, 1000), F(1, 2), F(999, 1000), F(1)):
            x = 1 - th * rn1 / 16
            v = 16 * x + rn1
            k = v.numerator // v.denominator
            assert k == 16
            x = v - 16
            J = zc.renewal_J(n) + extra
            good, b = True, 0
            for j in range(1, J + 6):
                v = 16 * x + ic.r(n + 1 + j)
                k = v.numerator // v.denominator
                if k != 0:
                    break
                b += 1
                x = v
            good = b >= J
            upper = 16 ** (b - 1) * 15 < (8 * n + 9) * (8 * n + 14) if b >= 1 else True
            tally.ok(good and upper, ("renewal", n, str(th), b, J))


def seeded_streams(S, seed, n_max):
    """Carries, seam bits and digits of the seeded carrier (authentic forcing, rational seed)."""
    U = [S.U[n] + 16 ** n * seed for n in range(n_max + 3)]
    C = [u.numerator // u.denominator for u in U]
    kap = [None] + [C[n] - 16 * C[n - 1] for n in range(1, n_max + 3)]
    eps = zc.seam_bits(U, n_max + 2)
    orbit = ic.CompletedOrbit(n_max + 3, a=seed, b=F(1))
    fl = []
    for n in range(n_max + 3):
        f = orbit.frac(n)
        if not (2 * orbit.frac_error() < f < 1 - 2 * orbit.frac_error()):
            raise RuntimeError(f"floor undecidable at n={n}")
        fl.append(orbit.floor(n))
    dig = [fl[n + 1] - 16 * fl[n] for n in range(n_max + 2)]
    return kap, eps, dig


AGREE = {(0, 0, 0), (1, 1, 1), (0, 1, 1), (0, 1, 0)}
DISCREPANT = {(0, 0, 1), (1, 1, 0), (1, 0, 0)}


def check_case_table(kap, eps, dig, n_lo, n_hi, tally) -> dict:
    disc, runs = 0, sum(1 for n in range(n_lo, n_hi + 3) if kap[n] == 16)
    for n in range(n_lo, n_hi):
        tally.ok(dig[n] == kap[n + 1] + eps[n + 1] - 16 * eps[n], ("cocycle", n))
        pat = (eps[n], eps[n + 1], eps[n + 2])
        dch, kch = dig[n] != dig[n + 1], kap[n + 1] != kap[n + 2]
        if pat in AGREE:
            tally.ok(dch == kch, ("agree", n, pat))
        else:
            tally.ok(pat in DISCREPANT, ("pattern", n, pat))
            disc += dch != kch
    tally.ok(disc <= 3 * max(runs, 0), ("disc<=3runs", disc, runs))
    return {"discrepancies": disc, "sixteen_events": runs}


def section_zsc03(S, dpi, quick: bool) -> dict:
    t5, t6 = Tally(), Tally()
    n_dir = list(range(1, 60)) + [100, 200, 400, 800, 1600, 2500]
    renewal_direct(t5, n_dir)
    for n in range(1, 2601):
        t5.ok(4 ** (zc.renewal_J(n) + 1) > 2 * n, ("J>=floor(log4 2n)", n))
    n_zero = 300 if quick else 2600
    kap0 = [None] + [(S.U[n].numerator // S.U[n].denominator) - 16 * (S.U[n - 1].numerator // S.U[n - 1].denominator)
                     for n in range(1, n_zero + 3)]
    eps0 = zc.seam_bits(S.U, n_zero + 2)
    zero = check_case_table(kap0, eps0, dpi, 2, n_zero, t6)
    zero["seam_positions"] = sum(eps0)
    zero["max_carry"] = max(kap0[1:])
    seeds = {}
    for k, a in ((20, 0), (35, 1), (50, 3), (80, 6), (120, 10), (200, 15))[: 3 if quick else 6]:
        s = zc.forced_seam_seed(S, k, a)
        kap, eps, dig = seeded_streams(S, s, k + a + 40)
        res = check_case_table(kap, eps, dig, 2, k + a + 38, t6)
        p = next(n for n in range(2, k + a + 40) if kap[n] == 16)
        J = zc.renewal_J(p - 1)
        t5.ok(all(kap[p + j] == 0 for j in range(1, J + 1)), ("renewal-seed", k, a))
        b = 0
        while kap[p + 1 + b] == 0:
            b += 1
        t5.ok(16 ** (b - 1) * 15 < (8 * (p - 1) + 9) * (8 * (p - 1) + 14), ("RIO-09 window", k, a))
        res.update(seam_run=sum(eps), sixteen_at=p, zeros_after=b, J=J)
        seeds[f"k={k},a={a}"] = res
    return {"ZC-5_renewal": t5.out(), "ZC-6_case_table": t6.out(zero_seed=zero, forced_seam_seeds=seeds)}


# ---------------------------------------------------------------- ZC-7  (ZSC-04)
def section_zsc04(S, dpi, quick: bool) -> dict:
    t = Tally()
    longest = (0, 0)
    for n in range(2, len(dpi) - 60):
        L = zc.run_length(dpi, n, 50)
        t.ok(L <= 41 * n, ("run", n, L))
        longest = max(longest, (L, n))
    top = 12 if quick else 40
    for n in range(2, top + 1):
        J = 41 * (n - 1)
        floor_pi = sum(dpi[i] * 16 ** (n - 1 - i) for i in range(n))          # floor(16^(n-1) pi), route (i)
        C = S.U[n + J].numerator // S.U[n + J].denominator                     # route (ii)
        t.ok(C // 16 ** J == floor_pi, ("lookahead", n))
    return {"ZC-7": t.out(longest_run_len_pos=list(longest), lookahead_checked_to_n=top)}


# ---------------------------------------------------------------- ZC-8  (ZSC-05)
def seam_fraction(d, fr, lo, hi) -> tuple[int, int, int]:
    """(#seam, #non-seam, #undecided) using r(n+1)/16 <= T_n < 1/(64 n^2)."""
    yes = no = und = 0
    for n in range(lo, hi):
        f = fr[n]
        if f + TRUNC_ERR < ic.r(n + 1) / 16:
            yes += 1
        elif f >= F(1, 64 * n * n):
            no += 1
        else:
            und += 1
    return yes, no, und


def section_zsc05(quick: bool) -> dict:
    t = Tally()
    L = 3000 if quick else 20000
    out = {}
    d = zc.w1_digits(L + 80)
    fr = fracs_of(d, L)
    for m in range(16, L - 200):
        gap = next(i for i in range(0, 400) if d[m + i] == 1)
        t.ok(gap <= math.isqrt(m) + 2 and not (d[m] == 1 and d[m + 1] == 1), ("W1 gap", m))
    for n in range(16, L - 200):
        z = next(i for i in range(0, 400) if d[n + i] != 0)
        if 4 ** z >= 16 * n + 4:                                   # z >= log_4(16n+4)
            t.ok(fr[n] + TRUNC_ERR < ic.r(n + 1) / 16, ("W1 seam", n))
    shells = (243, 1210) if quick else (243, 1210, 4096, 8192)
    w1 = {}
    for B in shells:
        ch = zc.changes(d, B, 2 * B)
        t.ok(ch <= 2 * math.isqrt(B) + 6, ("W1 changes", B, ch))
        y, n_, u = seam_fraction(d, fr, B, 2 * B)
        w1[str(B)] = {"changes": ch, "seam_density_lower": y / B, "undecided": u,
                      "ReW_1": shell(prefix(phases(fr[:2 * B], 1)), B).real}
    out["W1"] = w1
    d = zc.w2_digits(L + 80)
    fr = fracs_of(d, L)
    t.ok(0 not in d, "W2 has no digit 0")
    t.ok(all(ic.dist_to_int(fr[m]) <= F(1, 16 ** min(nxt - m - 1, zc.TRUNC))
             for m, nxt in ((3, 4), (5, 16), (17, 256), (257, 65536))), "W2 near-integers")
    out["W2"] = {str(B): {"changes": zc.changes(d, B, 2 * B),
                          "ReW_1": shell(prefix(phases(fr[:2 * B], 1)), B).real} for B in shells}
    d = zc.w3_digits(L + 80)
    fr = fracs_of(d, L)
    w3 = {}
    for B in shells:
        c = float(cB(d, B))
        y, n_, u = seam_fraction(d, fr, B, 2 * B)
        w3[str(B)] = {"c_B": c, "seam_density_lower": y / B, "undecided": u,
                      "absW_1": abs(shell(prefix(phases(fr[:2 * B], 1)), B))}
        t.ok(abs(c - 0.5) <= 0.06 and y / B >= 0.25, ("W3", B, c, y / B))
    out["W3"] = w3
    return {"ZC-8": t.out(**out)}


# ---------------------------------------------------------------- ZC-9  (ZSC-06)
def poly_eval(g, z):
    return sum(F(c) * z ** i for i, c in enumerate(g))


def section_zsc06(S, quick: bool) -> dict:
    t = Tally()
    n_max = 120 if quick else 400
    for hpoly in ((1,), (1, -2, 0, 5), (0, 0, F(3, 7), 0, 0, 0, 0, 0, 0, -1)):
        g2 = zc.gauge_transform(zc.G_PI, hpoly)
        S2 = zc.GSource(g2, n_max, seed=sum(F(c, i + 1) for i, c in enumerate(hpoly)))
        t.ok(all(S2.U[n] == S.U[n] + zc.gauge_a(hpoly, n) for n in range(n_max + 1)), ("gauge", hpoly))
        t.ok(all(abs(zc.gauge_a(hpoly, n)) <= F(sum(abs(F(c)) for c in hpoly), 8 * n + 1)
                 for n in range(n_max + 1)), ("gauge size", hpoly))
        gp, sp = zc.proper_form(g2, sum(F(c, i + 1) for i, c in enumerate(hpoly)))
        t.ok(gp == tuple(F(c) for c in zc.A_PI) and sp == 0, ("proper form returns (A_pi, 0)", hpoly))
    rank, ker = zc.baker_rank()
    t.ok(rank == 7 and len(ker) == 1, ("rank", rank))
    t.ok([c * 8 / ker[0][0] for c in ker[0]] == [F(c) for c in zc.A_NULL], "kernel = Q A_0")
    for zq in (F(i, 13) for i in range(1, 12)):                    # partial-fraction identity
        m = (2 - zq * zq) * (zq * zq - 2 * zq + 2)
        t.ok((zq * zq - 4 * zq + 2) / m == zq / (zq * zq - 2) - (zq - 1) / (zq * zq - 2 * zq + 2), ("pf", zq))
    K = (4, 4, 4, 2, 1)                                            # (z^2+2)(z^2+2z+2)
    for zq in (F(i, 7) for i in range(-9, 10)):
        t.ok(poly_eval(zc.G_PI, zq) == poly_eval(K, zq) * (1 - zq), ("g_pi = K(1-z)", zq))
        t.ok(poly_eval(zc.G_NULL, zq) == poly_eval(K, zq) * (zq * zq - 4 * zq + 2), ("g_0 = K q_0", zq))
        t.ok(poly_eval(zc.G_HOSTILE, zq) == (16 - zq ** 8) * (3 - 2 * zq) + poly_eval(zc.G_NULL, zq), ("g_H", zq))
    lo, hi = zc.L_enclosure(zc.A_NULL)
    t.ok(lo < 0 < hi and hi - lo < F(1, 10 ** 60), "L(A_0) = 0 to 60 digits")
    lo, hi = zc.L_enclosure(zc.A_PI)
    xlo = F(ic._x_scaled(60), 16 ** 60)
    t.ok(lo - F(1, 16 ** 55) < xlo < hi + F(1, 16 ** 55), "L(A_pi) = pi/16")
    t.ok(all(poly_eval(zc.G_HOSTILE, F(i, 1000)) > 0 for i in range(1000)) and poly_eval(zc.G_HOSTILE, F(1)) == 0,
         "g_H > 0 on grid of [0,1), g_H(1) = 0")
    t.ok(sum(zc.G_HOSTILE) == 0 and sum(zc.G_PI) == 0 and sum(zc.G_NULL) == -15, "residue sums")
    N0 = zc.GSource(zc.G_NULL, n_max)
    t.ok(all(0 < N0.U[n] < F(1, 8 * n + 1) for n in range(1, n_max + 1)), "0 < U^0_n < 1/(8n+1)")
    H = zc.GSource(zc.G_HOSTILE, n_max)
    TH = [2 * 16 ** n - H.U[n] for n in range(n_max + 1)]
    t.ok(all(H.U[n] == N0.U[n] + 2 * 16 ** n - F(3, 8 * n + 1) + F(1, 4 * n + 1) for n in range(n_max + 1)),
         "U^H identity")
    t.ok(all(0 < TH[n] < 1 for n in range(1, n_max + 1)), "0 < T^H_n < 1")
    kH = H.carries()
    t.ok(all(kH[n] == 15 for n in range(2, n_max + 1)), "hostile carries are 15")
    t.ok(all(2 * 16 ** n - (H.U[n].numerator // H.U[n].denominator) == 1 for n in range(1, n_max + 1)),
         "hostile seam bit is 1")
    g_rho = tuple(a + b for a, b in zip(zc.G_PI + (0,), zc.G_NULL))
    R = zc.GSource(g_rho, n_max)
    t.ok(all(R.U[n] == S.U[n] + N0.U[n] for n in range(n_max + 1)), "U^rho = U + rho U^0")
    lo, hi = zc.L_enclosure(tuple(a + b for a, b in zip(zc.A_PI, zc.A_NULL)))
    t.ok(lo - F(1, 16 ** 55) < xlo < hi + F(1, 16 ** 55), "L(A_pi + A_0) = pi/16")
    return {"ZC-9": t.out(rank=rank, kernel=[str(c * 8 / ker[0][0]) for c in ker[0]],
                          T_H_at_100=float(TH[100]) if n_max >= 100 else None)}


# ---------------------------------------------------------------- ZC-10 (IAD-04 repair)
def progression_cells(S, B, ell, h, q):
    cells = {}
    for n in range(B, 2 * B - ell):
        cells.setdefault(n % q, []).append(zc.e_of(h * S.innovation(n, ell)))
    return cells


def iad04_repaired_holds(S, B, ell, h, q) -> tuple[bool, float, float]:
    assert 1 <= q <= B - ell and q * h * 16 ** ell * 8 <= 15 * B ** 3
    lam = h * 16 ** (ell - 2) / (2 * B + 1) ** 3
    cells = progression_cells(S, B, ell, h, q)
    lhs = max(abs(sum(v)) / len(v) for v in cells.values())
    occ = (B - ell) // q
    rhs1 = (1 / math.tan(PI * q * lam / 2)) / occ
    rhs2 = 8802 * B * B / ((1 - ell / B) * h * 16 ** ell)
    return (len(cells) == q and min(len(v) for v in cells.values()) >= occ
            and lhs <= rhs1 + TOL and rhs1 <= 4 / (PI * lam * (B - ell)) + TOL <= rhs2 + 2 * TOL), lhs, rhs1


def iad04_retired_display(S, B, ell, h, q) -> tuple[float, float]:
    """Left and right side of the retired display (q/(B-l-q)) * 2/(pi q lam)."""
    lam = h * 16 ** (ell - 2) / (2 * B + 1) ** 3
    cells = progression_cells(S, B, ell, h, q)
    lhs = max(abs(sum(v)) / len(v) for v in cells.values())
    return lhs, (q / (B - ell - q)) * 2 / (PI * q * lam)


def section_iad04(S, quick: bool) -> dict:
    t, rows = Tally(), []
    grid = [(64, 2, 1, 62), (64, 3, 1, 1), (64, 3, 1, 7), (64, 4, 1, 3), (64, 4, 1, 7), (128, 4, 1, 5),
            (128, 5, 1, 3), (128, 5, 1, 1)]
    if not quick:
        grid += [(243, 5, 1, 11), (243, 5, 2, 6), (243, 5, 1, 25), (243, 2, 3, 241)]
    for B, ell, h, q in grid:
        ok, lhs, rhs = iad04_repaired_holds(S, B, ell, h, q)
        t.ok(ok, ("iad04", B, ell, h, q, lhs, rhs))
        rows.append({"B": B, "l": ell, "h": h, "q": q, "max_cell_mean": lhs, "bound": rhs})
    lhs, rhs = iad04_retired_display(S, 100, 1, 1, 1000)
    t.ok(lhs > rhs and rhs < 0 and abs(lhs - 1) < 1e-12, ("retired display must be violated", lhs, rhs))
    return {"ZC-10": t.out(rows=rows, retired_display_at_100_1_1_1000={"lhs": lhs, "rhs": rhs})}


# ---------------------------------------------------------------- ZC-11, predictions, controls
def section_pi(S, dpi, frpi, shells) -> dict:
    t, pred, rows = Tally(), {"ZP-1": [], "ZP-2": [], "ZP-4": []}, {}
    frU = [S.U[n] - (S.U[n].numerator // S.U[n].denominator) for n in range(2 * max(shells) + 1)]
    for B in shells:
        row = {"c_B": float(cB(dpi, B))}
        for h in MODES:
            W = shell(prefix(phases(frpi[:2 * B], h)), B)
            D = shell(prefix(phases(frU[:2 * B], h)), B)
            t.ok(abs(D - W) <= (PI / 32) * h / B ** 2 + TOL, ("transport", B, h))
            row[f"absW_{h}"] = abs(W)
            row[f"absD_{h}"] = abs(D)
            if B in HOLD:
                pred["ZP-2"].append(abs(W) <= 4 / math.sqrt(B))
        longest = max(zc.run_length(dpi, n, 60) for n in range(B, 2 * B))
        row["longest_run"] = longest
        if B in HOLD:
            pred["ZP-1"].append(abs(row["c_B"] - 15 / 16) <= 4 * math.sqrt(15 / (256 * B)))
            pred["ZP-4"].append(longest <= 6)
        rows[str(B)] = row
    return {"ZC-11_transport": t.out(), "shells": rows,
            "predictions": {k: {"met": all(v), "instances": len(v), "misses": v.count(False)}
                            for k, v in pred.items()}}


def hijack_fracs(B: int, q: int = 1009):
    K = 2 * B
    k = 1
    while q ** k < 16 ** (K + 2):
        k += 1
    M = K + ic.GUARD_HEX + 8
    X = ic._x_scaled(M)
    a = -((2 * q ** k * X + 16 ** M) // (2 * 16 ** M))             # -round(x q^k)
    base = F(X, 16 ** M) + F(a, q ** k)
    out = {}
    for n in range(B, 2 * B + 2):
        y = 16 ** n * base
        out[n] = y - (y.numerator // y.denominator)
    return out


def section_controls(S, strings, shells, quick: bool) -> dict:
    t, out = Tally(), {}
    Bs = [B for B in shells]
    n_top = 2 * max(Bs) + 2
    # coherent seed: U_n = -T_n
    for B in Bs:
        fr = {n: 1 - ic.tail_interval(n, 12)[0] for n in range(B, 2 * B)}
        for h in (1, 15):
            D = sum(zc.e_of(h * fr[n]) for n in range(B, 2 * B)) / B
            t.ok(abs(D - 1) <= (PI / 32) * h / B ** 2 + TOL, ("coherent", B, h))
    N0 = zc.GSource(zc.G_NULL, n_top)
    H = zc.GSource(zc.G_HOSTILE, n_top)
    t.ok(all(k == 0 for k in N0.carries()[2:]), "null source carries are 0")
    kH = H.carries()
    t.ok(all(k == 15 for k in kH[2:]), "hostile carries are 15")
    host = {}
    for B in Bs:
        for h in (1, 15):
            D0 = sum(zc.e_of(h * N0.frac(n)) for n in range(B, 2 * B)) / B
            t.ok(abs(D0 - 1) <= 2 * PI * h / (8 * B + 1) + TOL, ("null D", B, h))
            DH = sum(zc.e_of(h * H.frac(n)) for n in range(B, 2 * B)) / B
            TH = float(1 - H.frac(B))
            t.ok(DH.real >= 1 - 2 * PI * h * TH - TOL, ("hostile D", B, h))
            host[f"B={B},h={h}"] = {"ReD_hostile": DH.real, "ReD_null": D0.real}
    out["null_and_hostile"] = host
    # rho-family (ZP-5)
    kpi = [None] + [(S.U[n].numerator // S.U[n].denominator) - 16 * (S.U[n - 1].numerator // S.U[n - 1].denominator)
                    for n in range(1, n_top + 1)]
    Urho = [S.U[n] + N0.U[n] for n in range(n_top + 1)]
    Crho = [u.numerator // u.denominator for u in Urho]
    krho = [None] + [Crho[n] - 16 * Crho[n - 1] for n in range(1, n_top + 1)]
    diff = [n for n in range(1, n_top + 1) if kpi[n] != krho[n]]
    for B in Bs:
        for h in MODES:
            D = sum(zc.e_of(h * (S.U[n])) for n in range(B, 2 * B)) / B
            Dr = sum(zc.e_of(h * Urho[n]) for n in range(B, 2 * B)) / B
            t.ok(abs(D - Dr) <= 2 * PI * h / (8 * B + 1) + TOL, ("rho transport", B, h))
    out["rho_family"] = {"horizon": n_top, "carry_differences": len(diff), "positions": diff[:20],
                         "ZP-5_met": len(diff) <= 12}
    # shadows
    d17, fr17 = strings["1/17"]
    d715, fr715 = strings["7/15"]
    for B in Bs:
        t.ok(cB(d17, B) == 1 and abs(abs(shell(prefix(phases(fr17[:2 * B], 17)), B)) - 1) < 1e-9, ("1/17", B))
        w = abs(shell(prefix(phases(fr17[:2 * B], 1)), B))
        t.ok(abs(w - abs(math.cos(2 * PI / 17))) <= 2 / B, ("1/17 mode 1", B, w))
        t.ok(cB(d715, B) == 0 and abs(shell(prefix(phases(fr715[:2 * B], 15)), B) - 1) < 1e-9, ("7/15", B))
    # Shallit point
    dK, frK = strings["shallit_K"]
    sh = {}
    for k in (8, 9, 10):
        B = 2 ** k
        if 2 * B <= len(frK):
            w = shell(prefix(phases(frK[:2 * B], 1)), B).real
            t.ok(w >= 1 - 2 * math.ceil(k / 4) / B - 1e-3, ("Shallit", k, w))
            sh[str(B)] = w
    out["shallit_ReW_1"] = sh
    # hijack seed of IAD-07 on the first holdout shell (or calibration when quick)
    B = Bs[0] if quick else 243
    fh = hijack_fracs(B)
    Wh = sum(zc.e_of(fh[n]) for n in range(B, 2 * B)) / B
    dh = [int(16 * fh[n]) for n in range(B, 2 * B + 1)]
    t.ok(abs(Wh - 1) <= PI / (3840 * B) + TOL and all(a == b for a, b in zip(dh, dh[1:])), ("hijack", B))
    out["hijack"] = {"B": B, "abs(W-1)": abs(Wh - 1), "digit_on_shell": dh[0]}
    # random strings: positive control for the prediction bands
    bands = []
    for name in ("random_a", "random_b"):
        d, fr = strings[name]
        for B in Bs:
            if 2 * B + 6 <= len(fr):
                bands.append(abs(float(cB(d, B)) - 15 / 16) <= 4 * math.sqrt(15 / (256 * B)))
                bands += [abs(shell(prefix(phases(fr[:2 * B], h)), B)) <= 4 / math.sqrt(B) for h in MODES]
    out["random_band_control"] = {"instances": len(bands), "misses": bands.count(False)}
    return {"controls": t.out(**out)}


# ---------------------------------------------------------------- mutation controls
def mutations(S) -> dict:
    res = {}
    def zm1(y):                                                        # ZM-1
        return zc.dist15(y) < F(1, 128) and int(16 * y) != int(16 * (16 * y - int(16 * y)))
    # The preregistered input 1/15 + 3/(2*15*256) does NOT exhibit a change (the upward margin
    # at j = 1 is 14/(15*256)); it is kept and reported.  The corrected input is its mirror image.
    res["ZM-1_preregistered_input"] = zm1(F(1, 15) + F(3, 2 * 15 * 256))
    res["ZM-1"] = zm1(F(1, 15) - F(3, 2 * 15 * 256))
    t = Tally()                                                        # ZM-2
    B, N = 64, 34
    d = [3] * B + [0] * N + [7] * (2 * B + zc.TRUNC)
    fr = fracs_of(d, 2 * B + 2)
    check_stretch(fr, prefix(phases(fr, 1)), B, 1, t, const_shift=1)
    t0 = Tally()
    check_stretch(fr, prefix(phases(fr, 1)), B, 1, t0)
    res["ZM-2"] = len(t.bad) > 0 and len(t0.bad) == 0
    t = Tally()                                                        # ZM-3
    renewal_direct(t, [5, 50, 500], extra=3)
    res["ZM-3"] = len(t.bad) > 0
    lhs, rhs = iad04_retired_display(S, 100, 1, 1, 1000)               # ZM-4
    res["ZM-4"] = lhs > rhs
    A_bad = tuple(a + (1 if j == 7 else 0) for j, a in enumerate(zc.A_NULL))   # ZM-5
    lo, hi = zc.L_enclosure(A_bad)
    rows = zc.baker_matrix()
    dot = [sum(c * F(a) for c, a in zip(row, A_bad)) for row in rows]
    res["ZM-5"] = not (lo < 0 < hi) and any(v != 0 for v in dot)
    return res


# ---------------------------------------------------------------- driver
def build_strings(quick: bool, dpi) -> dict:
    L = 700 if quick else 4300
    rng = random.Random(SEED)
    raw = {"pi": dpi, "W1": zc.w1_digits(L + 60), "W2": zc.w2_digits(L + 60), "W3": zc.w3_digits(L + 60),
           "xi_1/4": zc.xi_lambda_digits(F(1, 4), L + 60), "xi_1/2": zc.xi_lambda_digits(F(1, 2), L + 60),
           "xi_3/4": zc.xi_lambda_digits(F(3, 4), L + 60), "shallit_K": zc.shallit_digits(L + 60),
           "1/17": zc.periodic_digits([0, 15], L + 60), "7/15": zc.periodic_digits([7], L + 60),
           "random_a": [rng.randrange(16) for _ in range(L + 60)],
           "random_b": [rng.randrange(16) for _ in range(L + 60)]}
    return {k: (d, fracs_of(d, min(len(d) - zc.TRUNC - 1, L))) for k, d in raw.items()}


def run(quick: bool = False) -> tuple[dict, bool]:
    shells = CAL if quick else CAL + HOLD
    n_src = 700 if quick else 2602
    S = ic.Source(n_src)
    dpi = zc.pi_digits((700 if quick else 2700) + 60)
    strings = build_strings(quick, dpi)
    frpi = strings["pi"][1]
    res = {"meta": {"quick": quick, "calibration_shells": list(CAL), "holdout_shells": list(HOLD),
                    "shells_run": list(shells), "modes": list(MODES), "tolerance": TOL, "seed": SEED,
                    "status_note": "no outcome changes the status of any open claim"}}
    res.update(section_zsc01(strings, shells, quick))
    res.update(section_zsc02(strings, shells))
    res.update(section_zsc03(S, dpi, quick))
    res.update(section_zsc04(S, dpi, quick))
    res.update(section_zsc05(quick))
    res.update(section_zsc06(S, quick))
    res.update(section_iad04(S, quick))
    res.update(section_pi(S, dpi, frpi, shells))
    res.update(section_controls(S, strings, shells, quick))
    res["mutation_controls_rejected"] = mutations(S)
    z3 = res["ZC-6_case_table"]["zero_seed"]
    res["predictions"]["ZP-3"] = {"met": z3["seam_positions"] == 0 and z3["max_carry"] <= 15,
                                  "seam_positions": z3["seam_positions"], "max_carry": z3["max_carry"]}
    res["predictions"]["ZP-5"] = {"met": res["controls"]["rho_family"]["ZP-5_met"],
                                  "carry_differences": res["controls"]["rho_family"]["carry_differences"]}
    grade = [v for k, v in res.items() if isinstance(v, dict) and "failures" in v]
    ok = all(v["failures"] == 0 for v in grade) and all(
        v for k, v in res["mutation_controls_rejected"].items() if k != "ZM-1_preregistered_input")
    res["meta"]["theorem_grade_checks"] = sum(v["checked"] for v in grade)
    res["meta"]["theorem_grade_failures"] = sum(v["failures"] for v in grade)
    res["meta"]["all_theorem_grade_pass"] = ok
    return res, ok


def main(argv=None) -> int:
    argv = sys.argv[1:] if argv is None else argv
    quick = "--quick" in argv
    res, ok = run(quick)
    if not quick:
        (_HERE / "RESULTS_zsc.json").write_text(json.dumps(res, indent=1, sort_keys=True) + "\n")
    m = res["meta"]
    print(f"theorem-grade checks: {m['theorem_grade_checks']}, failures: {m['theorem_grade_failures']}")
    print("predictions:", {k: v["met"] for k, v in res["predictions"].items()})
    print("mutations rejected:", res["mutation_controls_rejected"])
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
