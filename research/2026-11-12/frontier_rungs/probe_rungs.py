#!/usr/bin/env python3
"""Probe for LIMIT_FACES.md (LMF-01..06), following PREREGISTRATION_RUNGS.md.

Order of work (fixed by the preregistration):
  1. authenticate the data path (three routes to the hexadecimal digits of x = pi/16);
  2. calibration shells {64, 128};
  3. fresh holdout shells {3301, 4099, 5003, 6007} (full run only).

Theorem-grade checks RC-1..RC-10 are decided by exact rational arithmetic, or by
floating evaluation of e(t) with tolerance TOL where a cosine is involved.
Predictions RP-1..RP-4 are evaluated without re-thresholding; a miss is recorded as
a miss.  The probe writes RESULTS_rungs.json and exits non-zero iff a
theorem-grade check or a mutation control fails.  It changes the status of no open
claim: pi normality and (CH) are OPEN whatever is printed here.

    python probe_rungs.py            full run (authentication, calibration, holdout)
    python probe_rungs.py --quick    authentication on a short overlap + calibration only
"""
from __future__ import annotations

import cmath
import json
import math
import random
import sys
from fractions import Fraction
from pathlib import Path

_HERE = Path(__file__).resolve().parent
if str(_HERE) not in sys.path:
    sys.path.insert(0, str(_HERE))

import faces_core as fc  # noqa: E402  (also puts the 2026-11-11 dossier on sys.path)
import iad_core as ic  # noqa: E402
import zsc_core as zc  # noqa: E402

F = Fraction
TOL = 1e-9
CAL, HOLD = (64, 128), (3301, 4099, 5003, 6007)
WITNESS_SHELLS = (64, 128, 700, 1500)
MODES = (1, 3, 15, 17)
THETAS = (F(0), F(1, 2), F(1, 7))
SEED = 2026111201
SCALE = fc.SCALE
PROVISIONAL = {"w_star": F(4, 225), "theta_star": F(1, 60)}
RP1_BOUND, RP2_BOUND, RP3_LO, RP3_HI = F(9, 1000), F(8, 1000), F(90, 100), F(97, 100)


class Tally:
    def __init__(self):
        self.n, self.bad = 0, []

    def ok(self, cond: bool, what) -> bool:
        self.n += 1
        if not cond:
            self.bad.append(str(what) if len(self.bad) < 5 else "...")
        return cond

    def out(self, **extra):
        return {"checked": self.n, "failures": len(self.bad), "first_failures": self.bad[:5], **extra}


def f9(x) -> str:
    return f"{float(x):.9f}"


# ---------------------------------------------------------------- shell data
class Shell:
    """Exact data of the shell [B, 2B) of a digit string (points truncated to 40 hex digits).
    The truncated points are NOT an exact orbit segment (T(trunc y_n) = trunc y_(n+1) only when
    d_(n+40) = 0); the inequalities checked here are those proved for arbitrary measures and for
    the shifted list actually used, and the computed D differs from the true one by at most
    16^(-40) (audit note, 2026-11-12)."""

    def __init__(self, d: list[int], B: int):
        self.d, self.B = d, B
        Y = fc.fracs_from_digits(d, B, 2 * B + 1)
        self.Y, self.Ynext = Y[:B], Y[1:]
        self.jump = F(abs(Y[B] - Y[0]), SCALE * B)                 # |y_2B - y_B| / B
        self.w1 = fc.seg_w1_lebesgue(self.Y)
        self.G = fc.seg_child_defect(self.Y)
        self.D = fc.seg_haar_defect(self.Y, self.Ynext)
        self.cB = F(fc.k_changes(d, B, 2 * B, 1), B)
        self._ph = {}

    def mean_e(self, h: int) -> complex:
        if h not in self._ph:
            self._ph[h] = sum(cmath.exp(2j * math.pi * ((h * y) % SCALE / SCALE)) for y in self.Y) / self.B
        return self._ph[h]


def check_shell(sh: Shell, t: dict) -> None:
    B, d = sh.B, sh.d
    # RC-2  Kantorovich lower bounds (LMF-04 (a), (b)) and the endpoint inequality (c)
    for h in MODES:
        for th in THETAS:
            m = fc.seg_mean_tri(sh.Y, h, th)
            floor = F(1, 4 * h) - m
            t["RC-2"].ok(sh.w1 >= floor, ("W1>=floor", B, h, th))
            t["RC-2"].ok(sh.G >= floor, ("G>=floor", B, h, th))
            # RC-3  Fourier form  mean||hy-theta|| <= sqrt((1 - Re e(-theta) nu^(h)) / 8)
            re = (sh.mean_e(h) * cmath.exp(-2j * math.pi * float(th))).real
            t["RC-3"].ok(float(m) <= math.sqrt(max(0.0, (1 - re) / 8)) + TOL, ("fourier", B, h, th))
        mod = abs(sh.mean_e(h))
        t["RC-3"].ok(float(sh.w1) >= (0.25 - math.sqrt(max(0.0, (1 - mod) / 8))) / h - TOL, ("W1 vs |nu^|", B, h))
        t["RC-3"].ok(float(sh.G) >= (0.25 - math.sqrt(max(0.0, (1 - mod) / 8))) / h - TOL, ("G vs |nu^|", B, h))
    t["RC-2"].ok(sh.D >= sh.G - sh.jump / 16, ("D>=G-jump/16", B))
    t["RC-2"].ok(sh.D <= sh.G + sh.jump / 16, ("D<=G+jump/16", B))
    # RC-5  Main XXIV reconstruction on a shell segment, both directions
    t["RC-5"].ok(sh.w1 <= F(16, 15) * sh.D + sh.jump / 15, ("W1<=16/15 D", B))
    t["RC-5"].ok(sh.D >= F(15, 16) * sh.w1 - sh.jump / 16, ("D>=15/16 W1", B))
    t["RC-5"].ok(sh.D <= F(17, 16) * sh.w1 + sh.jump / 16, ("D<=17/16 W1", B))
    # RC-4  digit forms (LMF-04 (d))
    m15 = fc.seg_mean_tri(sh.Y, 15) * 15                               # mean ||15 y_n||
    for k in (2, 3, 4, 5):
        beta = fc.bad_fraction(d, B, 2 * B, k)
        cap = (k - 1) * (sh.cB + F(k - 1, B))
        t["RC-4"].ok(beta <= cap, ("beta<=cap", B, k))
        t["RC-4"].ok(m15 <= beta / 2 + 15 * F(1, 16 ** k), ("mean15", B, k))
        low = F(1, 60) - cap / 30 - F(1, 16 ** k)
        t["RC-4"].ok(sh.w1 >= low, ("W1 digit form", B, k))
        t["RC-4"].ok(sh.D + F(1, 16 * B) >= low, ("D digit form", B, k))
    eps = F(1, 60) - sh.w1                                             # certified change density
    if eps > 0:
        k = max(2, math.ceil(math.log(2 / float(eps), 16) - 1e-12))
        while F(1, 16 ** k) > eps / 2:
            k += 1
        t["RC-4"].ok(sh.cB >= 15 * eps / (k - 1) - F(k - 1, B), ("certified c_B", B, k))
    # RC-6  the rung R0: binary changes and Re W_B(1)  (LMF-03 (a))
    bits = fc.bits_of_digits(d[B: 2 * B + fc.TRUNC])
    blocks = sum(1 for n in range(B) if any(bits[4 * n + i] != bits[4 * n + i + 1] for i in range(4)))
    cbin = F(sum(1 for m in range(4 * B) if bits[m] != bits[m + 1]), 4 * B)
    qB = F(blocks, B)
    re1 = sh.mean_e(1).real
    t["RC-6"].ok(cbin <= qB <= 4 * cbin, ("cbin<=q<=4cbin", B))
    t["RC-6"].ok(1 - re1 >= float(qB) / 53 - TOL, ("R0 lower", B))
    for n in range(B):
        if any(bits[4 * n + i] != bits[4 * n + i + 1] for i in range(4)):
            y = sh.Y[n]
            t["RC-6"].ok(32 * min(y, SCALE - y) >= SCALE, ("||y||>=1/32", B, n))
    for k in range(2, 9):
        up = (k + 2) * (2 * float(cbin) + (k - 2) / (2 * B)) + 2 * math.pi ** 2 * 4.0 ** (-k)
        t["RC-6"].ok(1 - re1 <= up + TOL, ("R0 upper", B, k))
    # RC-7  the period-k rungs (LMF-03 (c)): locality at N_k = 16^k - 1 and the two-sided bound
    for k in (1, 2, 3):
        Nk = 16 ** k - 1
        ck = F(fc.k_changes(d, B, 2 * B, k), B)
        rek = sh.mean_e(Nk).real
        for n in range(B):
            v = (Nk * sh.Y[n]) % SCALE
            dist = min(v, SCALE - v)                                    # ||N_k y_n|| * SCALE
            if d[B + n] != d[B + n + k]:
                t["RC-7"].ok(dist * 16 ** (k + 1) >= SCALE, ("k-change far", B, k, n))
            L = 0
            while L < 6 and d[B + n + L] == d[B + n + L + k]:
                L += 1
            if L:
                t["RC-7"].ok(dist * 16 ** (L + k) <= Nk * SCALE, ("k-periodic near", B, k, n))
        t["RC-7"].ok(1 - rek >= 8 * 16.0 ** (-2 * k - 2) * float(ck) - TOL, ("CH_k lower", B, k))
        for L in (1, 2, 3):
            up = 2 * L * (float(ck) + (L - 1) / B) + 2 * math.pi ** 2 * 16.0 ** (-2 * L)
            t["RC-7"].ok(1 - rek <= up + TOL, ("CH_k upper", B, k, L))
    # RC-8  Basel shell quantity (LMF-02 (e))
    w = fc.basel_weights(B)
    t["RC-8"].ok(all(F(1, 2 * B) <= p <= F(2, B) for p in w), ("weights", B))
    for h in (1, 15):
        ph = [cmath.exp(2j * math.pi * ((h * y) % SCALE / SCALE)) for y in sh.Y]
        Bq = sum(float(p) * z for p, z in zip(w, ph))
        gapW, gapB = 1 - sh.mean_e(h).real, 1 - Bq.real
        t["RC-8"].ok(gapW / 2 - TOL <= gapB <= 2 * gapW + TOL, ("Basel real sandwich", B, h))
        t["RC-8"].ok((1 - abs(sh.mean_e(h))) / 2 - TOL <= 1 - abs(Bq) <= 2 * (1 - abs(sh.mean_e(h))) + TOL,
                     ("Basel modulus sandwich", B, h))
    # RC-9  prefix form of the Fix-mass lemma (LMF-05 (b))
    if len(d) >= 2 * B + fc.TRUNC + 8:
        pre = fc.seg_w1_lebesgue(fc.fracs_from_digits(d, 0, 2 * B))
        for k in (2, 3, 4):
            a = (1 - fc.bad_fraction(d, B, 2 * B, k)) / 2
            t["RC-9"].ok(pre >= a * a / 60 - a * F(1, 16 ** k), ("prefix Fix-mass", B, k))


def shell_row(sh: Shell) -> dict:
    d, B = sh.d, sh.B
    bits = fc.bits_of_digits(d[B: 2 * B + 2])
    return {"W1": fc.dec(sh.w1), "D": fc.dec(sh.D), "G": fc.dec(sh.G),
            "changes": int(sh.cB * B), "c_B": fc.dec(sh.cB, 6),
            "c2_B": fc.dec(F(fc.k_changes(d, B, 2 * B, 2), B), 6),
            "binary_change_density": fc.dec(F(sum(1 for m in range(4 * B) if bits[m] != bits[m + 1]), 4 * B), 6),
            "mean_dist15": fc.dec(fc.seg_mean_tri(sh.Y, 15) * 15),
            "ReW1": f9(sh.mean_e(1).real), "absW1": f9(abs(sh.mean_e(1))), "ReW15": f9(sh.mean_e(15).real),
            "below_W1_threshold_1/60": sh.w1 < fc.W1_FIX, "below_D_threshold_1/60": sh.D < fc.D_FIX,
            "below_mode1_threshold_1/4": sh.w1 < F(1, 4)}


# ---------------------------------------------------------------- RC-1  authentication
def authenticate(quick: bool, t: Tally) -> tuple[list[int], dict]:
    top = max(CAL if quick else HOLD)
    n_digits = 2 * top + fc.TRUNC + 20
    M = n_digits + ic.GUARD_HEX
    XA = ic._x_scaled(M)                                   # route A: mpmath enclosure of pi
    XB = fc.x_scaled_from_source(M)                        # route B: frozen forcing, integer enclosure
    t.ok(XA == XB, "route A (pi oracle) == route B (source series) as integers")
    dA = fc.digits_from_scaled(XA, M, n_digits)
    dB = fc.digits_from_scaled(XB, M, n_digits)
    for n in range(n_digits):
        t.ok(dA[n] == dB[n], ("A==B digit", n))
    overlap = 300 if quick else 2600
    dC = fc.digits_from_carrier(overlap)                   # route C: exact carrier + seam bits
    for n in range(1, overlap + 1):
        t.ok(dA[n] == dC[n], ("A==C digit", n))
    t.ok(dA[:8] == [3, 2, 4, 3, 15, 6, 10, 8], "leading digits of pi = 3.243F6A8...")
    return dA, {"digits_compared_A_vs_B": n_digits, "guard_hex_digits": ic.GUARD_HEX,
                "overlap_A_vs_carrier": [1, overlap], "truncation_hex_digits": fc.TRUNC,
                "w1_truncation_error_bound": "16^-40", "defect_truncation_error_bound": "(17/16) 16^-40"}


# ---------------------------------------------------------------- RC-10 exact constants
def constants(t: Tally) -> dict:
    cert = fc.fix16_dual_certificate()
    t.ok(all(v == F(1, 60) for v in cert["dual_w1_vertex_values"]), "dual W1 certificate")
    t.ok(all(v == F(1, 60) for v in cert["dual_defect_vertex_values"]), "dual defect certificate")
    t.ok(cert["primal_w1"] == F(1, 60) and cert["primal_defect"] == F(1, 60), "primal M_STAR")
    t.ok(fc.min_w1_fix15() == F(4, 225), "fifteen-point minimum")
    zero, one = [(F(0), F(1))], [(F(1), F(1))]
    t.ok(fc.haar_defect(zero) == F(15, 32) and fc.child_defect(one) == F(15, 32), "coherent control 15/32")
    half = [(F(0), F(1, 2)), (F(1), F(1, 2))]
    t.ok(fc.w1_lebesgue(half) == F(1, 4) and fc.child_defect(half) == F(1, 4), "mode-1 extremal 1/4")
    for i in range(0, 241):
        y = F(i, 240)
        t.ok(fc.child_defect([(y, F(1))]) <= fc.G_MAX, ("G<=15/32", i))
        t.ok(fc.child_defect([(y, F(1))]) >= F(1, 4), ("G(delta)>=1/4", i))
    rng = random.Random(SEED)
    for h in (1, 2, 3, 5, 8, 15, 17, 24, 255):
        for _ in range(12):
            th, y = F(rng.randrange(360), 360), F(rng.randrange(10 ** 6), 10 ** 6)
            t.ok(fc.child_average_tri(h, th, y) == F(1, 4 * h), ("psi constant", h))
    t.ok(fc.child_average_tri(16, F(0), F(1, 3)) != F(1, 64), "psi not constant when 16 | h")
    rho = fc.half_prefix_extremal(3600)
    w = fc.w1_lebesgue(rho)
    t.ok(F(1, 240) <= w <= F(1, 240) + F(1, 7200) < F(1, 120), "half-prefix extremal")
    # Fix-mass lemma on random rational measures
    for _ in range(200):
        a = F(rng.randrange(1, 41), 40)
        raw = [rng.randrange(0, 9) for _ in range(16)]
        if not sum(raw):
            raw[rng.randrange(16)] = 1
        masses = [a * F(x, sum(raw)) for x in raw]
        rest = [(F(rng.randrange(0, 721), 720), F(1)) for _ in range(rng.randrange(1, 9))]
        atoms = [(F(j, 15), m) for j, m in enumerate(masses)]
        if a < 1:
            atoms += [(p, (1 - a) / len(rest)) for p, _ in rest]
        rho = fc.normalize(atoms)
        w1 = fc.w1_lebesgue(rho)
        floor = fc.fix_mass_floor(masses)
        t.ok(w1 >= floor >= a * a / 60, ("Fix-mass", a))
        # Kantorovich bounds on arbitrary rational measures (also atoms at 1)
        for h in (1, 15):
            th = F(rng.randrange(60), 60)
            t.ok(w1 >= fc.kantorovich_floor(rho, h, th), ("K W1", h))
            t.ok(fc.child_defect(rho) >= fc.kantorovich_floor(rho, h, th), ("K G", h))
        t.ok(F(15, 16) * w1 <= fc.child_defect(rho) <= F(17, 16) * w1, ("15/16 <= G/W1 <= 17/16", a))
    # the provisional threshold 4/225 is refuted by an explicit shell (not pi data)
    refute = {}
    for k in (40, 100):
        d, B = fc.superblock_shell_digits(k)
        Y = fc.fracs_from_digits(d, B, 2 * B)
        w1k, ck = fc.seg_w1_lebesgue(Y), F(fc.k_changes(d, B, 2 * B, 1), B)
        t.ok(ck == F(1, 2 * k) and F(1, 60) - F(1, 30 * 2 * k) - F(1, 256) <= w1k < F(4, 225),
             ("provisional 4/225 refuted", k))
        t.ok(w1k <= F(1, 60) + F(16, 450 * k), ("superblock upper bound", k))
        refute[f"k={k}"] = {"B": B, "c_B": fc.dec(ck, 6), "W1": fc.dec(w1k)}
    return {"min_W1_on_sixteen_fixed_points": "1/60", "min_defect_on_sixteen_fixed_points": "1/60",
            "provisional_threshold_4/225_refuted_by": refute,
            "min_W1_on_fifteen_fixed_points_endpoint_forbidden": "4/225",
            "optimal_masses": "1/30, 1/15 (x14), 1/30", "coherent_control_defect": "15/32",
            "mode_1_threshold": "1/4", "half_prefix_floor": "1/240",
            "half_prefix_extremal_W1": fc.dec(w)}


# ---------------------------------------------------------------- strings
def build_strings(quick: bool) -> dict:
    L = (2 * max(WITNESS_SHELLS[:2] if quick else WITNESS_SHELLS)) + fc.TRUNC + 20
    rng = random.Random(SEED)
    return {"coherent_zero": [0] * L, "constant_7": [7] * L,
            "W1": zc.w1_digits(L), "W2": zc.w2_digits(L), "W3": zc.w3_digits(L),
            "shallit_K": zc.shallit_digits(L), "1/17": zc.periodic_digits([0, 15], L),
            "ladder_S*": fc.ladder_digits(L), "runs_0_F": fc.two_runs_digits(0, 15, L),
            "runs_1_2": fc.two_runs_digits(1, 2, L), "sparse_1_with_2": fc.sparse_excursion_digits(1, 2, L),
            "period_mix": fc.period_mix_digits(L), "basel_converse": fc.basel_converse_digits(L),
            "random_a": [rng.randrange(16) for _ in range(L)],
            "random_b": [rng.randrange(16) for _ in range(L)]}


ABOVE_ALL = ("coherent_zero", "constant_7", "W1", "W2", "shallit_K", "runs_0_F")


def section_witnesses(strings: dict, shells, t: dict) -> dict:
    out = {}
    for name, d in strings.items():
        rows = {}
        for B in shells:
            sh = Shell(d, B)
            check_shell(sh, t)
            rows[str(B)] = shell_row(sh)
            if name in ABOVE_ALL and B >= 64:
                t["RC-11"].ok(sh.w1 >= fc.W1_FIX and sh.D >= fc.D_FIX, ("hostile above thresholds", name, B))
        out[name] = rows[str(shells[-1])]
    # exact hostile values
    sh = Shell(strings["coherent_zero"], shells[0])
    t["RC-11"].ok(sh.D == F(15, 32) and sh.w1 == F(1, 2) and sh.cB == 0, "coherent control: D = 15/32, W1 = 1/2")
    return out


def basel_converse_check(d: list[int], t: Tally) -> dict:
    """Instance check of LMF-02 (f): on the converse witness, Re(A F_15(A)) stays below
    1 - 1/9963 on a truncated tail while shells B = 16^i have (almost) no change."""
    top = len(d) - fc.TRUNC - 2
    Y = fc.fracs_from_digits(d, 1, top)
    gap = [1 - math.cos(2 * math.pi * ((15 * y) % SCALE / SCALE)) for y in Y]     # index n - 1
    rows = {}
    for A in (16, 17, 24, 31, 32, 100, 256, 300, 511, 512, 700):
        if 4 * A > top:
            continue
        # Omega_A - Re F_15(A) >= truncated sum; compare with the lower bound of the proof
        part = sum(gap[n - 1] / (n * n) for n in range(A, top))
        chg = sum(1.0 / (n * n) for n in range(A, top) if d[n] != d[n + 1])
        t.ok(part >= chg / 3321 - TOL, ("pointwise 1/3321", A))
        t.ok(part * A >= 1 / 9963 * (1 - A / top) - TOL, ("Basel converse saving", A))
        rows[str(A)] = f9(part * A)
    c16 = F(fc.k_changes(d, 256, 512, 1), 256)
    t.ok(c16 <= F(1, 256), "shell 256 of the converse witness has at most one change")
    return {"A_times_truncated_gap": rows, "c_B_at_256": fc.dec(c16, 6)}


# ---------------------------------------------------------------- mutation controls
def mutations(dpi: list[int]) -> dict:
    out = {}
    # RM-1: constant digits on the shell
    rm1 = []
    for j in (0, 7, 15):
        sh = Shell([j] * (2 * 64 + fc.TRUNC + 8), 64)
        rm1.append(sh.w1 >= PROVISIONAL["w_star"] and sh.cB == 0 and not sh.w1 < RP1_BOUND)
    out["RM-1"] = all(rm1)
    # RM-2: Q replaced by the identity: D == 0 identically; the checks must notice
    ident = lambda atoms: atoms                                                   # noqa: E731
    zero = [(F(0), F(1))]
    sh = Shell(dpi, 64)
    nu = fc.normalize((F(y, SCALE), F(1, sh.B)) for y in sh.Y)
    d_mut_pi, d_mut_zero = fc.haar_defect(nu, q=ident), fc.haar_defect(zero, q=ident)
    identically_zero = d_mut_pi == 0 and d_mut_zero == 0
    coherent_check_fails = d_mut_zero != F(15, 32)
    floor_check_fails = not (d_mut_zero >= fc.kantorovich_floor(zero, 15))        # 0 >= 1/60 is false
    out["RM-2"] = identically_zero and coherent_check_fails and floor_check_fails
    out["RM-2_vacuous_pass_flagged"] = d_mut_pi < RP2_BOUND                       # RP-2 would pass vacuously
    # RM-3: uniform measure on the 256-adic grid
    grid = [(F(i, 256), F(1, 256)) for i in range(256)]
    out["RM-3"] = fc.w1_lebesgue(grid) <= F(1, 512)
    out["RM-3_value"] = str(fc.w1_lebesgue(grid))
    return out


# ---------------------------------------------------------------- driver
def run(quick: bool = False) -> tuple[dict, bool]:
    names = ["RC-1", "RC-2", "RC-3", "RC-4", "RC-5", "RC-6", "RC-7", "RC-8", "RC-9", "RC-10", "RC-11", "RC-12"]
    t = {k: Tally() for k in names}
    res = {"meta": {"quick": quick, "calibration_shells": list(CAL), "holdout_shells": list(HOLD),
                    "witness_shells": list(WITNESS_SHELLS[:2] if quick else WITNESS_SHELLS),
                    "modes": list(MODES), "tolerance": TOL, "seed": SEED,
                    "status_note": "no outcome changes the status of any open claim; (CH) and pi "
                                   "normality are OPEN"}}
    # 1. authentication, before any shell of pi is touched
    dpi, auth = authenticate(quick, t["RC-1"])
    res["authentication"] = auth
    res["constants"] = constants(t["RC-10"])
    # 2. witnesses and controls (not pi data)
    strings = build_strings(quick)
    res["witnesses_largest_shell"] = section_witnesses(strings, WITNESS_SHELLS[:2] if quick else WITNESS_SHELLS, t)
    if not quick:
        res["basel_converse"] = basel_converse_check(strings["basel_converse"], t["RC-12"])
    # 3. pi: calibration, then holdout
    pi_rows, shells = {}, (CAL if quick else CAL + HOLD)
    for B in shells:
        sh = Shell(dpi, B)
        check_shell(sh, t)
        row = shell_row(sh)
        eps = fc.W1_FIX - sh.w1
        row["role"] = "calibration" if B in CAL else "holdout"
        row["W1_margin_below_1/60"] = fc.dec(eps)
        pi_rows[str(B)] = row
    res["pi_shells"] = pi_rows
    for k in names:
        res[k] = t[k].out()
    res["mutation_controls"] = mutations(dpi)
    grade_ok = all(t[k].bad == [] for k in names)
    preds = {}
    if not quick:
        hold = [pi_rows[str(B)] for B in HOLD]
        preds["RP-1"] = {"met": all(F(r["W1"]) < RP1_BOUND for r in hold), "bound": "0.009",
                         "values": [r["W1"] for r in hold]}
        preds["RP-2"] = {"met": all(F(r["D"]) < RP2_BOUND for r in hold), "bound": "0.008",
                         "values": [r["D"] for r in hold]}
        preds["RP-3"] = {"met": all(RP3_LO < F(r["c_B"]) < RP3_HI for r in hold), "window": "(0.90, 0.97)",
                         "values": [r["c_B"] for r in hold]}
        preds["RP-4"] = {"met": grade_ok}
    res["predictions"] = preds
    res["thresholds"] = {"provisional_w_star": "4/225", "proved_w_star": "1/60",
                         "provisional_theta_star": "1/60", "proved_theta_star": "1/60",
                         "note": "4/225 is the minimum over the fifteen points j/15 < 1; shell measures can "
                                 "accumulate at the endpoint 1, and the correct threshold is 1/60"}
    m = res["mutation_controls"]
    ok = grade_ok and m["RM-1"] and m["RM-2"] and m["RM-3"]
    res["meta"]["theorem_grade_checks"] = sum(t[k].n for k in names)
    res["meta"]["theorem_grade_failures"] = sum(len(t[k].bad) for k in names)
    res["meta"]["all_theorem_grade_pass"] = ok
    return res, ok


def main(argv=None) -> int:
    argv = sys.argv[1:] if argv is None else argv
    quick = "--quick" in argv
    res, ok = run(quick)
    if not quick:
        (_HERE / "RESULTS_rungs.json").write_text(json.dumps(res, indent=1, sort_keys=True) + "\n")
    m = res["meta"]
    print(f"theorem-grade checks: {m['theorem_grade_checks']}, failures: {m['theorem_grade_failures']}")
    print("predictions:", {k: v["met"] for k, v in res["predictions"].items()})
    print("mutation controls:", res["mutation_controls"])
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
