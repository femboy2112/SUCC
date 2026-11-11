#!/usr/bin/env python3
"""IAD analytic probes: preregistered checks PR-1.1 .. PR-1.6, predictions PR-2.1 .. PR-2.5
and the PR-3 expectations that concern IAD-01 .. IAD-06 (see PREREGISTRATION.md).

Holdout shells B in {200, 360, 729, 1000}; calibration shells B in {64, 256} (already looked at
while the theorems were derived, so they are labelled ``calibration`` and never counted as holdout).
Modes h in {1, 3, 8}.

Rigor contract
--------------
* Exact ``Fraction`` arithmetic wherever a statement is exact (innovations, tails, steps,
  brackets, Kusmin-Landau hypotheses, seed constructions, alias identities).
* Every phase e(t) is evaluated from an argument that has first been reduced mod 1 *exactly*
  (integer numerator mod denominator); only then is it converted to a float.  Floats are used
  only for the final complex sums.
* Identities are checked to ``TOL_IDENTITY``; theorem-grade float inequalities pass when
  ``rhs - lhs >= -TOL_INEQUALITY``; IAD-02 uses the preregistered ``TOL_IAD02``.  For every
  inequality the number of *strict* failures (``rhs - lhs < 0`` with no tolerance) and the minimum
  margin are recorded too, so nothing passes silently because of the tolerance.
* All randomness is seeded from a SHA-256 of a descriptive string; output JSON has sorted keys
  and no timestamps.  ``mpmath`` is only used inside ``mp.workdps``.

Usage (from the repository root)::

    PYTHONPATH=. python research/2026-11-11/innovation_arithmetic_decoupling/probe_analytic.py
    PYTHONPATH=. python .../probe_analytic.py --quick            # B in {64, 200}; no file written
    PYTHONPATH=. python .../probe_analytic.py --quick --out X.json

Exit status is 1 iff some PR-1 check fails.  PR-2 outcomes never change the exit status.
"""
from __future__ import annotations

import argparse
import cmath
import hashlib
import json
import math
import random
import sys
import time
from fractions import Fraction
from pathlib import Path

import mpmath as mp
import numpy as np

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

import iad_core as core  # noqa: E402
from iad_core import CompletedOrbit, Source, neg_r_prime, r, r_real, tail_interval  # noqa: E402

# --------------------------------------------------------------------------------------------
# Preregistered design constants
# --------------------------------------------------------------------------------------------
HOLDOUT_SHELLS = (200, 360, 729, 1000)
CALIBRATION_SHELLS = (64, 256)
QUICK_SHELLS = (64, 200)
MODES = (1, 3, 8)
TOL_IDENTITY = 1e-12
TOL_IAD02 = 1e-12
TOL_INEQUALITY = 1e-9
N_SUBINTERVALS = 200
N_RANDOM_H = 50
N_RANDOM_PARTITIONS = 20          # per family (random 8-cell assignment, random contiguous blocks)
H_SET_MAX = 60                    # random H subset of [0, 60]
RESIDUE_FILTRATIONS = (1, 2, 5, 16)
PROGRESSION_MODULI = (2, 3, 7)
HIJACK_Q = 1000003
KL_CONSTANT = 4401
TWO_PI_J = 2j * math.pi
PI32 = math.pi / 32
SEEDS = ("1_true", "2_coherent", "3_shadow", "4_alias", "5_hijack")
SEQ_CONTROLS = SEEDS + ("6a_periodic_1_17", "6b_periodic_1_5", "7_factorial_sparse", "9_random")
DEFAULT_OUT = HERE / "RESULTS_analytic.json"
POLES = ((4, 7), (-2, 4), (-1, 3), (-1, 2))   # r(t) = sum c/(8t - a)


# --------------------------------------------------------------------------------------------
# Small exact helpers
# --------------------------------------------------------------------------------------------
def rng_for(*parts) -> random.Random:
    """Deterministic RNG from a descriptive key (independent of PYTHONHASHSEED)."""
    key = "iad-analytic|" + "|".join(str(p) for p in parts)
    return random.Random(int.from_bytes(hashlib.sha256(key.encode()).digest()[:8], "big"))


def lag_max(B: int) -> int:
    """floor(4.5 log_16 B), exactly: the largest l with 16^(2l) <= B^9."""
    l = 0
    while 16 ** (2 * (l + 1)) <= B ** 9:
        l += 1
    return l


def ell0(B: int) -> int:
    """ceil(2.25 log_16 B), exactly: the smallest l with 16^(4l) >= B^9."""
    l = 0
    while 16 ** (4 * l) < B ** 9:
        l += 1
    return l


def in_open_window(B: int, l: int) -> bool:
    """2 log_16 B < l < 3 log_16 B (the Kusmin-Landau mesoscopic window), exactly."""
    return B ** 2 < 16 ** l < B ** 3


def kl_admissible(B: int, h: int, l: int, q: int = 1) -> bool:
    """q h 16^l <= (15/8) B^3, exactly."""
    return 8 * q * h * 16 ** l <= 15 * B ** 3


def kl_lambda(B: int, h: int, l: int) -> Fraction:
    """lambda = h 16^(l-2) / (2B+1)^3 (exact)."""
    return Fraction(h * 16 ** l, 256 * (2 * B + 1) ** 3)


def kl_bound(lam) -> float:
    """cot(pi lambda / 2): the sharp discrete Kusmin-Landau constant (mpmath, 50 digits, from the
    exact rational lambda when given a Fraction)."""
    with mp.workdps(50):
        lm = mp.mpf(lam.numerator) / lam.denominator if isinstance(lam, Fraction) else mp.mpf(lam)
        return float(mp.cot(mp.pi * lm / 2))


def kl_constant_chain(B: int, h: int, l: int, q: int) -> tuple[float, float, float, list[float]]:
    """c1 = (q/(B-l-q)) cot(pi q lam/2), c2 = (q/(B-l-q)) 2/(pi q lam), c3 = 4401 B^2/((1-(l+q)/B) h 16^l),
    evaluated at 50 digits from the exact lambda; returns (c1, c2, c3, [c2-c1, c3-c2])."""
    lam = kl_lambda(B, h, l)
    with mp.workdps(50):
        lm = mp.mpf(lam.numerator) / lam.denominator
        f = mp.mpf(q) / (B - l - q)
        c1 = f * mp.cot(mp.pi * q * lm / 2)
        c2 = f * 2 / (mp.pi * q * lm)
        c3 = mp.mpf(KL_CONSTANT) * B ** 2 / ((1 - mp.mpf(l + q) / B) * h * mp.mpf(16) ** l)
        return float(c1), float(c2), float(c3), [float(c2 - c1), float(c3 - c2)]


def fraction_sha256(x: Fraction) -> str:
    """SHA-256 of the signed big-endian bytes of numerator and denominator (no decimal strings)."""
    def b(n: int) -> bytes:
        return n.to_bytes(n.bit_length() // 8 + 1, "big", signed=True)
    return hashlib.sha256(b(x.numerator) + b"/" + b(x.denominator)).hexdigest()


def frac_pair(x: Fraction) -> tuple[int, int]:
    d = x.denominator
    return x.numerator % d, d


def phase(num: int, den: int) -> complex:
    """e(num/den) with the argument reduced mod 1 exactly (to (-1/2, 1/2]) before float."""
    num %= den
    if num + num > den:
        num -= den
    return cmath.exp(TWO_PI_J * (num / den))


def phase_fr(x: Fraction) -> complex:
    return phase(x.numerator, x.denominator)


def lag_key(l: int) -> str:
    """Zero-padded lag key so that sorted JSON keys follow numeric order."""
    return f"lag_{l:02d}"


def window_key(L: int) -> str:
    return f"L_{L:04d}"


def cjson(z: complex) -> list[float]:
    return [float(z.real), float(z.imag)]


def signed_derivative(t: Fraction, k: int) -> Fraction:
    """(-1)^k r^(k)(t) = k! 8^k sum_i c_i / (8t - a_i)^(k+1), exact."""
    t = Fraction(t)
    return math.factorial(k) * 8 ** k * sum((Fraction(c) / (8 * t - a) ** (k + 1) for c, a in POLES),
                                            Fraction(0))


# --------------------------------------------------------------------------------------------
# Ledger of theorem-grade checks
# --------------------------------------------------------------------------------------------
class Ledger:
    """Counts checks and failures per (PR id, sub-check), with margins and counterexamples."""

    MAX_EXAMPLES = 5

    def __init__(self):
        self.slots: dict[tuple[str, str], dict] = {}
        self.rollup: dict[tuple[str, str], list[int]] = {}

    def _slot(self, pr, sub, kind, tol):
        key = (pr, sub)
        s = self.slots.get(key)
        if s is None:
            s = self.slots[key] = {"kind": kind, "tolerance": tol, "checks": 0, "failures": 0,
                                   "counterexamples": []}
            if kind == "inequality":
                s.update(strict_failures=0, min_margin=None, worst=None)
            elif kind == "identity":
                s.update(max_abs_error=None, worst=None)
        return s

    def _roll(self, pr, ctrl, n, f):
        c = self.rollup.setdefault((pr, ctrl), [0, 0])
        c[0] += n
        c[1] += f

    def ineq(self, pr, sub, ctrl, lhs, rhs, *, ctx, tol=TOL_INEQUALITY, detail=None):
        """Batch of inequalities lhs <= rhs (pass iff rhs - lhs >= -tol; NaN fails)."""
        lhs = np.asarray(lhs, dtype=float).ravel()
        rhs = np.broadcast_to(np.asarray(rhs, dtype=float), lhs.shape).ravel()
        if lhs.size == 0:
            return
        m = rhs - lhs
        s = self._slot(pr, sub, "inequality", tol)
        bad = np.nonzero(~(m >= -tol))[0]
        s["checks"] += int(m.size)
        s["failures"] += int(bad.size)
        s["strict_failures"] += int(np.count_nonzero(~(m >= 0)))
        finite = np.where(np.isnan(m), -np.inf, m)
        i = int(np.argmin(finite))
        if s["min_margin"] is None or finite[i] < s["min_margin"]:
            s["min_margin"] = float(finite[i])
            s["worst"] = dict(ctx, control=ctrl, lhs=float(lhs[i]), rhs=float(rhs[i]),
                              **(detail(i) if detail else {}))
        for j in bad[: max(0, self.MAX_EXAMPLES - len(s["counterexamples"]))]:
            s["counterexamples"].append(dict(ctx, control=ctrl, lhs=float(lhs[j]), rhs=float(rhs[j]),
                                             **(detail(int(j)) if detail else {})))
        self._roll(pr, ctrl, int(m.size), int(bad.size))

    def ident(self, pr, sub, ctrl, errs, *, ctx, tol=TOL_IDENTITY, detail=None):
        """Batch of identities |err| <= tol."""
        e = np.abs(np.asarray(errs, dtype=float).ravel())
        if e.size == 0:
            return
        s = self._slot(pr, sub, "identity", tol)
        bad = np.nonzero(~(e <= tol))[0]
        s["checks"] += int(e.size)
        s["failures"] += int(bad.size)
        worst = np.where(np.isnan(e), np.inf, e)
        i = int(np.argmax(worst))
        if s["max_abs_error"] is None or worst[i] > s["max_abs_error"]:
            s["max_abs_error"] = float(worst[i])
            s["worst"] = dict(ctx, control=ctrl, error=float(worst[i]), **(detail(i) if detail else {}))
        for j in bad[: max(0, self.MAX_EXAMPLES - len(s["counterexamples"]))]:
            s["counterexamples"].append(dict(ctx, control=ctrl, error=float(e[j]),
                                             **(detail(int(j)) if detail else {})))
        self._roll(pr, ctrl, int(e.size), int(bad.size))

    def exact(self, pr, sub, ctrl, oks, *, ctx, detail=None):
        """Batch of exact (Fraction / integer) statements."""
        oks = [bool(o) for o in oks]
        if not oks:
            return
        s = self._slot(pr, sub, "exact", 0)
        bad = [i for i, o in enumerate(oks) if not o]
        s["checks"] += len(oks)
        s["failures"] += len(bad)
        for j in bad[: max(0, self.MAX_EXAMPLES - len(s["counterexamples"]))]:
            s["counterexamples"].append(dict(ctx, control=ctrl, index=j, **(detail(j) if detail else {})))
        self._roll(pr, ctrl, len(oks), len(bad))

    def failures(self, pr_prefix="PR-1") -> int:
        return sum(s["failures"] for (pr, _), s in self.slots.items() if pr.startswith(pr_prefix))

    def to_json(self) -> dict:
        out: dict = {}
        for (pr, sub), s in sorted(self.slots.items()):
            out.setdefault(pr, {})[sub] = s
        roll: dict = {}
        for (pr, ctrl), (n, f) in sorted(self.rollup.items()):
            roll.setdefault(pr, {})[ctrl] = {"checks": n, "failures": f}
        return {"checks": out, "by_control": roll}


def exit_code(ledgers) -> int:
    """1 iff any PR-1 check failed in any ledger (PR-2 never affects the exit status)."""
    return 1 if any(L.failures("PR-1") for L in ledgers) else 0


# --------------------------------------------------------------------------------------------
# Generic evaluators (also used, with deliberate mutations, by the tests)
# --------------------------------------------------------------------------------------------
def window_energy(v: np.ndarray, L: int) -> float:
    """E_L = sum_m |sum_{j<L} v_(m+j)|^2 over all m (zero-extended): direct convolution."""
    V = np.convolve(v, np.ones(L))
    return float(np.sum(V.real * V.real + V.imag * V.imag))


def lag_sums(v: np.ndarray, lmax: int) -> np.ndarray:
    """lag_sums[l] = sum_n v_(n+l) conj(v_n) for 0 <= l <= lmax."""
    out = np.zeros(lmax + 1, dtype=complex)
    for l in range(0, min(lmax, len(v) - 1) + 1):
        out[l] = np.vdot(v[: len(v) - l], v[l:])
    return out


def R_definition(lsums: np.ndarray, L: int, B: int, factor: float = 2.0) -> float:
    """R_(B,L,h) = (factor*B/L) sum_{l=1}^{L-1} (1 - l/L) Re lsums[l]  (true factor = 2)."""
    tot = math.fsum((1.0 - l / L) * float(lsums[l].real) for l in range(1, L))
    return factor * B / L * tot


def R_identity(E_L: float, S: float, L: int, B: int) -> float:
    """Right side of (1.1): (B/L)(E_L/L - S)."""
    return B / L * (E_L / L - S)


def bound_12(S: float, R: float, B: int, L: int, c_L: float = 4.0, c_R: float = 2.0):
    """(1.2): middle form and the stated majorant c_L/L + c_R max(R, 0)."""
    mid = (B + L - 1) / L * S + (B + L - 1) / B * R
    return mid, c_L / L + c_R * max(R, 0.0)


def iad02_margins(gam: dict[int, float], slack_scale: float = 1.0, divisibility_only: bool = True):
    """Margins of (2.1) over all pairs J < L in ``gam`` (J = L is trivial):
    sqrt(gam_J) + slack_scale*J/L - sqrt(gam_L) and, for J | L (or all J if not divisibility_only),
    gam_J - gam_L.  Returns (sqrt_list, div_list) of (J, L, margin)."""
    keys = sorted(gam)
    sq, dv = [], []
    for L in keys:
        for J in keys:
            if J >= L:
                break
            sq.append((J, L, math.sqrt(gam[J]) + slack_scale * J / L - math.sqrt(gam[L])))
            if (L % J == 0) or not divisibility_only:
                dv.append((J, L, gam[J] - gam[L]))
    return sq, dv


def cond_sums(x: np.ndarray, labels: np.ndarray, ncell: int):
    re = np.bincount(labels, weights=x.real, minlength=ncell)
    im = np.bincount(labels, weights=x.imag, minlength=ncell)
    return re + 1j * im, np.bincount(labels, minlength=ncell)


def l1_cond_mean(x: np.ndarray, labels: np.ndarray, ncell: int) -> float:
    """||E[x|F]||_1 for the uniform measure; F generated by the cells ``labels``."""
    sums, _ = cond_sums(x, labels, ncell)
    return float(np.abs(sums).sum() / x.size)


def l1_deviation(x: np.ndarray, labels: np.ndarray, ncell: int) -> float:
    """a_F = ||x - E[x|F]||_1 for the uniform measure."""
    sums, cnt = cond_sums(x, labels, ncell)
    means = np.where(cnt > 0, sums / np.maximum(cnt, 1), 0)
    return float(np.abs(x - means[labels]).mean())


def vdc_rhs(H, c: dict[int, complex], B: int, cross: float = 2.0, length_factor: bool = True) -> float:
    """Right side of (6.1): (1 + D/B)[1/k + (cross/k^2) sum_{a>b in H} Re c_(a-b)]."""
    H = sorted(H)
    k = len(H)
    D = H[-1]
    s = math.fsum(float(c[a - b].real) for i, a in enumerate(H) for b in H[:i])
    body = 1.0 / k + cross / (k * k) * s
    return (1.0 + D / B) * body if length_factor else body


def vdc_rhs_ap(k: int, l0: int, c: dict[int, complex], B: int) -> float:
    """Closed form (6.2) for H = {0, l0, ..., (k-1) l0}."""
    s = math.fsum((1.0 - j / k) * float(c[j * l0].real) for j in range(1, k))
    return (1.0 + (k - 1) * l0 / B) * (1.0 / k + 2.0 / k * s)


# --------------------------------------------------------------------------------------------
# Seeds and controls
# --------------------------------------------------------------------------------------------
def odd_primes_upto(n: int) -> list[int]:
    return [p for p in range(3, n + 1) if core.is_prime(p)]


def hijack_seed(B: int, X: int, Mhex: int):
    """IAD-07 seed s = a/q^k (q = 1000003, M = 2^8 prod_{odd p<=97} p^2, K = 2B).

    round(-x q^k / M) is certified from the integer enclosure X <= x 16^Mhex < X + 1."""
    q = HIJACK_Q
    M = 2 ** 8
    for p in odd_primes_upto(97):
        M *= p * p
    K = 2 * B
    target = M * 16 ** (K + 2)
    k, qk = 0, 1
    while qk < target:
        qk *= q
        k += 1
    den = M * 16 ** Mhex
    y_lo, y_hi = Fraction(-(X + 1) * qk, den), Fraction(-X * qk, den)
    half = Fraction(1, 2)
    rd_lo, rd_hi = math.floor(y_lo + half), math.floor(y_hi + half)
    a = M * rd_hi
    s = Fraction(a, qk)
    x_lo, x_hi = Fraction(X, 16 ** Mhex), Fraction(X + 1, 16 ** Mhex)
    dist_hi = max(abs(x_lo + s), abs(x_hi + s))
    meta = {
        "q": q, "q_is_prime": core.is_prime(q), "M": str(M), "M_bits": M.bit_length(), "K": K, "k": k,
        "q_pow_k_ge_M_16_pow_K_plus_2": qk >= target,
        "k_minimal": (qk // q) < target,
        "rounding_certified": rd_lo == rd_hi,
        "a_bits": abs(a).bit_length(),
        "abs_x_plus_s_le_M_over_2qk": dist_hi <= Fraction(M, 2 * qk),
        "M_over_2qk_le_half_16_pow_minus_K_minus_2": Fraction(M, 2 * qk) <= Fraction(1, 2 * 16 ** (K + 2)),
        "seed_sha256": fraction_sha256(s),
    }
    return s, meta


def factorial_sparse_point(jmax: int = 7) -> Fraction:
    """x' = sum_{j=2}^{jmax} 16^(-j!) (truncation error < 2*16^(-(jmax+1)!))."""
    return sum((Fraction(1, 16 ** math.factorial(j)) for j in range(2, jmax + 1)), Fraction(0))


# --------------------------------------------------------------------------------------------
# Global (shell-independent) forcing checks: PR-1.3 brackets and moment representation
# --------------------------------------------------------------------------------------------
def _poly_mul(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def _poly_trim(a):
    a = list(a)
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def forcing_global_checks(led: Ledger, t_max: int, m_max: int) -> dict:
    """IAD-03 (b), (c) exact brackets on a rational grid, polynomial identities, moment rep."""
    ctx = {"scope": "global"}
    pr = "PR-1.3"
    # ---- polynomial identities (coefficient lists, ascending powers)
    g = [4, 0, 0, -2, -1, -1]
    fact_g = _poly_mul(_poly_mul([1, -1], [2, 0, 1]), [2, 2, 1])
    sixteen_minus_z8 = [16, 0, 0, 0, 0, 0, 0, 0, -1]
    fact_16 = _poly_mul(_poly_mul([2, 0, -1], [2, 0, 1]), _poly_mul([2, 2, 1], [2, -2, 1]))
    # G = g/(16 - z^8) = (1-z)/((2-z^2)(z^2-2z+2))  <=>  g*(2-z^2)(z^2-2z+2) == (1-z)(16-z^8)
    lhs_G = _poly_mul(g, _poly_mul([2, 0, -1], [2, -2, 1]))
    rhs_G = _poly_mul([1, -1], sixteen_minus_z8)
    inc = _poly_mul([2, 0, 1], [2, 2, 1])   # (z^2+2)(z^2+2z+2)
    led.exact(pr, "moment_polynomial_identities", "forcing", [
        _poly_trim(g) == _poly_trim(fact_g),
        _poly_trim(sixteen_minus_z8) == _poly_trim(fact_16),
        _poly_trim(lhs_G) == _poly_trim(rhs_G),
        sum(inc) == 15 and inc[0] == 4 and all(c >= 0 for c in inc),  # 4 -> 15, increasing on [0,1]
    ], ctx=ctx)

    # ---- rational grid
    grid = sorted({Fraction(8 + j, 8) for j in range(0, 8 * (t_max - 1) + 1)}
                  | {Fraction(7 + j, 7) for j in range(0, 7 * 63 + 1)}
                  | {Fraction(10 ** e) for e in (4, 5, 6, 9)})
    cm_grid = [t for t in grid if t.denominator in (1, 2, 7) or t > 10 ** 3]
    ok_route, ok_r, ok_rp, ok_r2, ok_mis, ok_int = [], [], [], [], [], []
    worst_r_lo = worst_r_hi = worst_p_lo = worst_p_hi = None
    for t in grid:
        rt = r_real(t)
        s0 = signed_derivative(t, 0)
        s1 = signed_derivative(t, 1)
        nrp = neg_r_prime(t)
        ok_route.append(rt == s0 and nrp == s1)
        q2 = (8 * t - 7) * (8 * t - 6)
        lo_r, hi_r = Fraction(4) / q2, Fraction(15) / q2
        ok_r.append(lo_r <= rt <= hi_r)
        lo_p, hi_p = 32 * (16 * t - 13) / q2 ** 2, 120 * (16 * t - 13) / q2 ** 2
        ok_rp.append(lo_p <= nrp <= hi_p)
        ok_r2.append(signed_derivative(t, 2) > 0)
        if t >= 2:
            ok_mis.append(Fraction(1, 16) / t ** 3 <= nrp <= Fraction(4) / t ** 3)
        if t.denominator == 1:
            ok_int.append(r_real(t) == r(int(t)))
        # tightness of the constants (observation): ratios to the brackets
        rr = rt * q2
        pp = nrp * q2 ** 2 / (16 * t - 13)
        worst_r_lo = rr if worst_r_lo is None or rr < worst_r_lo else worst_r_lo
        worst_r_hi = rr if worst_r_hi is None or rr > worst_r_hi else worst_r_hi
        worst_p_lo = pp if worst_p_lo is None or pp < worst_p_lo else worst_p_lo
        worst_p_hi = pp if worst_p_hi is None or pp > worst_p_hi else worst_p_hi
    led.exact(pr, "r_real_and_neg_r_prime_match_partial_fractions", "forcing", ok_route, ctx=ctx)
    led.exact(pr, "r_real_at_integers_equals_frozen_forcing", "forcing", ok_int, ctx=ctx)
    led.exact(pr, "bracket_r_4_15", "forcing", ok_r, ctx=ctx, detail=lambda i: {"t": str(grid[i])})
    led.exact(pr, "bracket_neg_r_prime_32_120", "forcing", ok_rp, ctx=ctx, detail=lambda i: {"t": str(grid[i])})
    led.exact(pr, "r_second_derivative_positive", "forcing", ok_r2, ctx=ctx, detail=lambda i: {"t": str(grid[i])})
    led.exact(pr, "neg_r_prime_between_1_over_16t3_and_4_over_t3", "forcing", ok_mis, ctx=ctx)
    cm_ok = [signed_derivative(t, k) > 0 for t in cm_grid for k in range(0, 7)]
    led.exact(pr, "complete_monotonicity_orders_0_to_6", "forcing", cm_ok, ctx=ctx)

    # ---- delta(m) = r(m) - r(m+1)
    deltas = [None, None] + [r(m) - r(m + 1) for m in range(2, m_max + 2)]
    ok_pos, ok_dec, ok_br = [], [], []
    for m in range(2, m_max + 1):
        d = deltas[m]
        ok_pos.append(d > 0)
        ok_dec.append(deltas[m + 1] < d)
        ok_br.append(Fraction(1, 16 * (m + 1) ** 3) <= d <= Fraction(4, m ** 3))
    led.exact("PR-1.3", "delta_m_positive", "forcing", ok_pos, ctx=ctx)
    led.exact("PR-1.3", "delta_m_strictly_decreasing", "forcing", ok_dec, ctx=ctx)
    led.exact("PR-1.3", "delta_m_bracket_1_over_16(m+1)^3_to_4_over_m^3", "forcing", ok_br, ctx=ctx)

    # ---- moment representation (numeric, mpmath quad at 40 digits; tolerance 1e-25)
    num_tol = mp.mpf("1e-25")
    errs = []
    with mp.workdps(40):
        gz = lambda z: 4 - 2 * z ** 3 - z ** 4 - z ** 5          # noqa: E731
        Gz = lambda z: gz(z) / (16 - z ** 8)                      # noqa: E731
        rows = []
        for t in (Fraction(1), Fraction(3, 2), Fraction(2), Fraction(7, 3), Fraction(5), Fraction(10)):
            s = 8 * mp.mpf(t.numerator) / t.denominator - 8
            val = mp.quad(lambda z: z ** s * gz(z), [0, 1])
            ref = mp.mpf(r_real(t).numerator) / r_real(t).denominator
            errs.append(abs(val - ref))
            rows.append({"quantity": f"r({t})", "abs_error": float(abs(val - ref))})
        for n in (0, 1, 2, 5):
            val = mp.quad(lambda z: z ** (8 * n) * Gz(z), [0, 1])
            if n == 0:
                ref = mp.pi / 16
            else:
                lo, _ = tail_interval(n)
                ref = mp.mpf(lo.numerator) / lo.denominator
            errs.append(abs(val - ref))
            rows.append({"quantity": f"T_{n}", "abs_error": float(abs(val - ref))})
        src = Source(12)
        for n, l in ((1, 1), (2, 3), (5, 2)):
            val = mp.quad(lambda z: z ** (8 * n) * gz(z) * (16 ** l - z ** (8 * l)) / (16 - z ** 8), [0, 1])
            d = src.innovation(n, l)
            ref = mp.mpf(d.numerator) / d.denominator
            errs.append(abs(val - ref))
            rows.append({"quantity": f"Delta_{l}({n})", "abs_error": float(abs(val - ref))})
        for s in (0, 1, 8, 40):
            v1 = mp.quad(lambda z: z ** s * (1 - z), [0, 1])
            v2 = mp.quad(lambda z: z ** s * mp.log(1 / z) * (1 - z), [0, 1])
            errs.append(abs(v1 - mp.mpf(1) / ((s + 1) * (s + 2))))
            errs.append(abs(v2 - mp.mpf(2 * s + 3) / ((s + 1) ** 2 * (s + 2) ** 2)))
            rows.append({"quantity": f"beta_integrals_s={s}", "abs_error": float(max(errs[-2:]))})
        led.ident(pr, "moment_representation_numeric_quad", "forcing", [float(x) for x in errs],
                  ctx=ctx, tol=float(num_tol), detail=lambda i: {"row": i})
    return {
        "grid_points": len(grid), "grid_t_max": t_max, "complete_monotonicity_points": len(cm_grid),
        "delta_m_range": [2, m_max],
        "r_times_(8t-7)(8t-6)_range_on_grid": [float(worst_r_lo), float(worst_r_hi)],
        "neg_r_prime_times_(8t-7)^2(8t-6)^2_over_(16t-13)_range_on_grid": [float(worst_p_lo), float(worst_p_hi)],
        "moment_representation_rows": rows,
        "moment_representation_tolerance": "1e-25 (mpmath quad, workdps(40))",
    }


# --------------------------------------------------------------------------------------------
# One shell
# --------------------------------------------------------------------------------------------
def run_shell(B: int, role: str, modes=MODES, n_sub: int = N_SUBINTERVALS, log=None) -> tuple[dict, Ledger]:
    log = log or (lambda *a: None)
    led = Ledger()
    t_start = time.time()
    lmax, l0 = lag_max(B), ell0(B)
    lags = list(range(1, lmax + 1))
    rB = math.isqrt(B)
    windows = sorted({2, 3, 5, 8, rB, 2 * rB})
    Lgrid = 2 * rB
    extra_windows = sorted({B // 8, B // 4, B // 2, B} - set(range(1, Lgrid + 1)))
    dmax = max(H_SET_MAX, Lgrid - 1, lmax, 3 * l0)
    horizon = 2 * B + 64
    log2_16B = math.log(B) / math.log(16)
    window_lags = [l for l in lags if in_open_window(B, l)]
    out: dict = {
        "B": B, "role": role, "modes": list(modes), "log16_B": log2_16B,
        "lags": lags, "lag_max_floor_4.5_log16B": lmax, "ell0_ceil_2.25_log16B": l0,
        "ap_lags": [l0, 2 * l0, 3 * l0],
        "open_window_lags_2log16B_lt_l_lt_3log16B": window_lags,
        "fejer_windows_preregistered": windows, "fejer_extra_windows": extra_windows,
        "iad02_grid_L_max": Lgrid, "c_d_max_lag": dmax, "source_horizon": horizon,
        "n_random_subintervals": n_sub, "n_random_H": N_RANDOM_H,
        "n_random_partitions_per_family": N_RANDOM_PARTITIONS,
    }

    # ---------------- exact source objects
    src = Source(horizon)
    tails = {n: tail_interval(n) for n in range(B, 2 * B + lmax + 2)}
    lo = {n: tl[0] for n, tl in tails.items()}
    tail_width_max = max(tl[1] - tl[0] for tl in tails.values())
    delta = {l: [src.innovation_direct(n, l) for n in range(B, 2 * B)] for l in lags}
    out["tail_enclosure_width_max"] = float(tail_width_max)
    log(f"  B={B}: source/tails/innovations built ({time.time() - t_start:.1f}s)")

    # ---------------- Basel weights (exact normalization facts, PR-1.1)
    omega = sum((Fraction(1, n * n) for n in range(B, 2 * B)), Fraction(0))
    sum4 = sum((Fraction(1, n ** 4) for n in range(B, 2 * B)), Fraction(0))
    pB = Fraction(1, B * B) / omega
    S_exact = sum4 / (omega * omega)
    p = np.array([float(Fraction(1, n * n) / omega) for n in range(B, 2 * B)])
    ctxB = {"B": B}
    led.exact("PR-1.1", "normalization_omega_ge_1/(2B)_pB_le_2/B_S_le_pB_sigma_le_2", "weights", [
        omega >= Fraction(1, 2 * B), pB <= Fraction(2, B), S_exact <= pB, B * S_exact <= 2], ctx=ctxB)
    out["weights"] = {"omega_B": float(omega), "p_B": float(pB), "S_exact": float(S_exact),
                      "sigma_B_exact": float(B * S_exact)}

    # ---------------- seeds / controls
    co_true = CompletedOrbit(horizon)
    X, Mhex = co_true.X, co_true.M
    L_sh = 2 * B + 16
    P_L = sum((Fraction(r(j), 16 ** j) for j in range(1, L_sh + 1)), Fraction(0))
    s_shadow = -P_L
    s_alias = Fraction(1, 16)
    s_hijack, hijack_meta = hijack_seed(B, X, Mhex)
    led.exact("PR-1.5", "seed_construction_preconditions", "3_shadow",
              [P_L == Fraction(src.U[L_sh], 16 ** L_sh)], ctx=ctxB)
    led.exact("PR-1.5", "seed_construction_preconditions", "5_hijack",
              [hijack_meta[k] for k in ("q_is_prime", "q_pow_k_ge_M_16_pow_K_plus_2", "k_minimal",
                                        "rounding_certified", "abs_x_plus_s_le_M_over_2qk",
                                        "M_over_2qk_le_half_16_pow_minus_K_minus_2")], ctx=ctxB)
    x_fact = factorial_sparse_point(7)
    orbits = {
        "1_true": co_true,
        "2_coherent": CompletedOrbit(horizon, a=Fraction(0), b=Fraction(0)),
        "3_shadow": CompletedOrbit(horizon, a=s_shadow, b=Fraction(1)),
        "4_alias": CompletedOrbit(horizon, a=s_alias, b=Fraction(1)),
        "5_hijack": CompletedOrbit(horizon, a=s_hijack, b=Fraction(1)),
        "6a_periodic_1_17": CompletedOrbit(horizon, a=Fraction(1, 17), b=Fraction(0)),
        "6b_periodic_1_5": CompletedOrbit(horizon, a=Fraction(1, 5), b=Fraction(0)),
        "7_factorial_sparse": CompletedOrbit(horizon, a=x_fact, b=Fraction(0)),
    }
    out["controls"] = {
        "1_true": {"seed": "0", "U": "exact Source", "Y": "CompletedOrbit(a=0,b=1)"},
        "2_coherent": {"seed": "-x (irrational)", "U": "U_n(-x) = -T_n, T_n = tail_interval lower endpoint",
                       "Y": "CompletedOrbit(a=0,b=0) == 0", "U_error_bound": float(tail_width_max)},
        "3_shadow": {"seed": f"-P_L, L = 2B+16 = {L_sh}", "seed_den_bits": s_shadow.denominator.bit_length(),
                     "seed_sha256": fraction_sha256(s_shadow)},
        "4_alias": {"seed": "1/16"},
        "5_hijack": dict(hijack_meta, seed="a/q^k (IAD-07)"),
        "6a_periodic_1_17": {"x_prime": "1/17", "sequence_level_only": True},
        "6b_periodic_1_5": {"x_prime": "1/5", "sequence_level_only": True},
        "7_factorial_sparse": {"x_prime": "sum_{j=2}^{7} 16^(-j!)", "truncation_error_lt": "2*16^(-40320)",
                               "sequence_level_only": True},
        "9_random": {"sequence": "e(u_n), u_n = random.Random(sha256('iad-analytic|random-control|B|h')).random()",
                     "sequence_level_only": True},
        "8_AT07": "not in scope of this probe (arithmetic agent)",
        "Y_enclosure_error": "16^-48 per CompletedOrbit.frac (times |b|)",
    }
    shell_ns = range(B, 2 * B)
    Ypairs = {c: [frac_pair(o.frac(n)) for n in shell_ns] for c, o in orbits.items()}
    Upairs = {
        "1_true": [frac_pair(src.U[n]) for n in shell_ns],
        "2_coherent": [frac_pair(-lo[n]) for n in shell_ns],
        "3_shadow": [frac_pair(src.U_seed(n, s_shadow)) for n in shell_ns],
        "4_alias": [frac_pair(src.U_seed(n, s_alias)) for n in shell_ns],
        "5_hijack": [frac_pair(src.U_seed(n, s_hijack)) for n in shell_ns],
    }
    log(f"  B={B}: controls built ({time.time() - t_start:.1f}s)")

    # ---------------- PR-3 alias exactness (Fraction level)
    alias_Y_equal = [orbits["4_alias"].frac(n) == co_true.frac(n) for n in range(1, horizon + 1)]
    alias_Y_differs_at_0 = orbits["4_alias"].frac(0) != co_true.frac(0)
    alias_U_equal = [Upairs["4_alias"][i] == Upairs["1_true"][i] for i in range(B)]
    alias_unwrapped = []
    for n in (1, 2, B):
        Pn = sum((Fraction(r(j), 16 ** j) for j in range(1, n + 1)), Fraction(0))
        alias_unwrapped.append(Fraction(src.U_seed(n, s_alias), 16 ** n) - Pn == s_alias)
    pr3_alias = {
        "completed_phase_fraction_equal_for_1_le_n_le_horizon": all(alias_Y_equal),
        "n_checked": len(alias_Y_equal),
        "differs_at_n_0": alias_Y_differs_at_0,
        "U_fraction_mod_1_equal_on_shell": all(alias_U_equal),
        "unwrapped_seed_16^-n_U_n(s)_minus_P_n_equals_1/16_at_n_in_{1,2,B}": all(alias_unwrapped),
    }

    # ---------------- phase sequences
    w = {c: {} for c in SEQ_CONTROLS}
    for c in orbits:
        for h in modes:
            w[c][h] = np.array([phase(h * a, d) for a, d in Ypairs[c]])
    for h in modes:
        rg = rng_for("random-control", B, h)
        w["9_random"][h] = np.array([cmath.exp(TWO_PI_J * rg.random()) for _ in shell_ns])
    # exact completed lag phases e(h(16^d-1) Y_n), n in [B, 2B-1-d]  (orbit controls)
    cexact: dict = {c: {h: {} for h in modes} for c in orbits}
    c_d: dict = {c: {h: {} for h in modes} for c in SEQ_CONTROLS}
    for c in orbits:
        for h in modes:
            errs = []
            for d in range(1, dmax + 1):
                mult = h * (16 ** d - 1)
                arr = np.array([phase(mult * a, den) for a, den in Ypairs[c][: B - d]])
                if d <= lmax:
                    cexact[c][h][d] = arr
                c_d[c][h][d] = complex(arr.sum() / B)
                prod = complex(np.vdot(w[c][h][: B - d], w[c][h][d:]) / B)
                errs.append(abs(prod - c_d[c][h][d]))
                cexact[c][h].setdefault("lagsum_exact", {})[d] = complex(np.sum(p[: B - d] * p[d:] * arr))
            led.ident("PR-1.6", "c_d_exact_route_equals_product_route", c, errs, ctx={"B": B, "h": h},
                      detail=lambda i: {"d": i + 1})
    for h in modes:
        ww = w["9_random"][h]
        for d in range(1, dmax + 1):
            c_d["9_random"][h][d] = complex(np.vdot(ww[: B - d], ww[d:]) / B)
    log(f"  B={B}: completed phases and c_d built ({time.time() - t_start:.1f}s)")

    # ================= PR-1.1 (IAD-01) and PR-1.2 (IAD-02) =================
    iad01: dict = {}
    iad02: dict = {}
    for c in SEQ_CONTROLS:
        iad01[c], iad02[c] = {}, {}
        for h in modes:
            v = p * w[c][h]
            S = float(np.sum(np.abs(v) ** 2))
            sigma = B * S
            BB = complex(v.sum())
            B2 = abs(BB) ** 2
            Lall = sorted(set(range(1, Lgrid + 1)) | set(extra_windows))
            ls = lag_sums(v, max(Lall))
            E = {L: window_energy(v, L) for L in Lall}
            gam = {L: E[L] / (L * L * S) for L in Lall}
            rows = {}
            ctx = {"B": B, "h": h}
            for L in sorted(set(windows) | set(extra_windows)):
                Rd = R_definition(ls, L, B)
                Ri = R_identity(E[L], S, L, B)
                Rg = sigma * (gam[L] - 1.0 / L)
                row = {"S": S, "E_L": E[L], "gamma_L": gam[L], "L_gamma_L": L * gam[L], "R_definition": Rd,
                       "R_identity": Ri, "B_B_abs2": B2}
                led.ident("PR-1.1", "identity_1.1_R_def_eq_(B/L)(E_L/L-S)", c, [Rd - Ri], ctx=dict(ctx, L=L))
                led.ident("PR-1.1", "identity_1.1_R_eq_sigma(gamma-1/L)", c, [Rg - Ri], ctx=dict(ctx, L=L))
                if c in orbits and L - 1 <= dmax:
                    Re_ = 2 * B / L * math.fsum((1 - l / L) * cexact[c][h]["lagsum_exact"][l].real
                                                for l in range(1, L))
                    row["R_exact_phase_route"] = Re_
                    led.ident("PR-1.1", "identity_1.1_exact_phase_route_(16^l-1)Y_n", c, [Re_ - Ri],
                              ctx=dict(ctx, L=L))
                mid, maj = bound_12(S, Ri, B, L)
                row.update(bound_1_2_middle=mid, bound_1_2_majorant=maj)
                led.ineq("PR-1.1", "inequality_1.2_cauchy_schwarz_L2|B|2_le_(B+L-1)E_L", c, [L * L * B2],
                         [(B + L - 1) * E[L]], ctx=dict(ctx, L=L))
                led.ineq("PR-1.1", "inequality_1.2_|B|2_le_middle", c, [B2], [mid], ctx=dict(ctx, L=L))
                led.ineq("PR-1.1", "inequality_1.2_middle_le_4/L+2maxR", c, [mid], [maj], ctx=dict(ctx, L=L))
                led.ineq("PR-1.1", "inequality_1.2_|B|2_le_4/L+2maxR", c, [B2], [maj], ctx=dict(ctx, L=L))
                led.ineq("PR-1.1", "trivial_range_-sigma/L_le_R_le_sigma(1-1/L)", c, [-sigma / L, Ri],
                         [Ri, sigma * (1 - 1 / L)], ctx=dict(ctx, L=L))
                led.ineq("PR-1.1", "gamma_in_[0,1]", c, [0.0, gam[L]], [gam[L], 1.0], ctx=dict(ctx, L=L))
                rows[window_key(L)] = row
            iad01[c][str(h)] = {"S": S, "sigma_B": sigma, "B_B": cjson(BB), "windows": rows}
            # ---- IAD-02 grid
            sq, dv = iad02_margins(gam)
            led.ineq("PR-1.2", "2.1_sqrt_gamma_L_le_sqrt_gamma_J_plus_J/L", c, [0.0] * len(sq),
                     [m for _, _, m in sq], ctx=ctx, tol=TOL_IAD02,
                     detail=lambda i, sq=sq: {"J": sq[i][0], "L": sq[i][1]})
            led.ineq("PR-1.2", "2.1_gamma_L_le_gamma_J_if_J_divides_L", c, [0.0] * len(dv),
                     [m for _, _, m in dv], ctx=ctx, tol=TOL_IAD02,
                     detail=lambda i, dv=dv: {"J": dv[i][0], "L": dv[i][1]})
            # (2.2) quantitative R bound over the same grid
            Rof = {L: sigma * (gam[L] - 1.0 / L) for L in Lall}
            lhs22, rhs22, pairs22 = [], [], []
            for L in Lall:
                for J in Lall:
                    if J >= L:
                        break
                    rhs = sigma * ((math.sqrt(1.0 / J + max(Rof[J], 0.0) / sigma) + J / L) ** 2 - 1.0 / L)
                    lhs22.append(Rof[L])
                    rhs22.append(rhs)
                    pairs22.append((J, L))
            led.ineq("PR-1.2", "2.2_R_L_le_sigma[(sqrt(1/J+R+_J/sigma)+J/L)^2-1/L]", c, lhs22, rhs22, ctx=ctx,
                     tol=TOL_IAD02, detail=lambda i, pp=pairs22: {"J": pp[i][0], "L": pp[i][1]})
            led.ident("PR-1.2", "gamma_1_equals_1", c, [gam[1] - 1.0], ctx=ctx)
            iad02[c][str(h)] = {"gamma": [gam[L] for L in range(1, Lgrid + 1)],
                                "gamma_extra": {window_key(L): gam[L] for L in extra_windows}}
    out["iad01"] = iad01
    out["iad02"] = iad02
    log(f"  B={B}: PR-1.1/1.2 done ({time.time() - t_start:.1f}s)")

    # ================= PR-1.3 (IAD-03) shell part =================
    pr = "PR-1.3"
    ok_routes, ok_encl, enc_width = [], [], 0.0
    for l in lags:
        for i, n in enumerate(shell_ns):
            dd = delta[l][i]
            ok_routes.append(dd == src.innovation(n, l))
            lo_n, hi_n = tails[n]
            lo_m, hi_m = tails[n + l]
            ok_encl.append(16 ** l * lo_n - hi_m <= dd <= 16 ** l * hi_n - lo_m)
            enc_width = max(enc_width, float(16 ** l * (hi_n - lo_n) + (hi_m - lo_m)))
    led.exact(pr, "innovation_two_exact_routes_equal", "forcing", ok_routes, ctx=ctxB)
    led.exact(pr, "3a_Delta_eq_16^l_T_n_minus_T_(n+l)_inside_tail_enclosure", "forcing", ok_encl, ctx=ctxB)
    # completed-orbit cancellation Y_(n+l) = 16^l Y_n (at the enclosure level) and BBP completion
    ok_canc = []
    for l in lags:
        for i in range(B - l):
            a_n, d_n = Ypairs["1_true"][i]
            a_m, d_m = Ypairs["1_true"][i + l]
            ok_canc.append(((16 ** l * a_n) % d_n) * d_m == a_m * d_n)
    led.exact(pr, "3a_completed_cancellation_Y_(n+l)-16^l_Y_n_eq_0", "1_true", ok_canc, ctx=ctxB)
    ok_bbp = []
    err_Y = Fraction(1, 16 ** core.GUARD_HEX)
    for i, n in enumerate(shell_ns):
        fU = Fraction(*Upairs["1_true"][i])
        fY = Fraction(*Ypairs["1_true"][i])
        z = fU + lo[n] - fY
        z -= round(z)
        ok_bbp.append(-(tails[n][1] - tails[n][0]) < z < err_Y)
    led.exact(pr, "bbp_completion_U_n_plus_T_n_in_Y_n_enclosure_mod_1", "1_true", ok_bbp, ctx=ctxB)
    # tail bounds
    ok_T = []
    for n in sorted(tails):
        lo_n, hi_n = tails[n]
        ok_T.append(0 < lo_n and hi_n <= r(n + 1) / 15 <= Fraction(1, (8 * n + 1) * (8 * n + 2))
                    < Fraction(1, 64 * n * n))
    led.exact(pr, "tail_0_lt_T_le_r(n+1)/15_le_1/((8n+1)(8n+2))_lt_1/(64n^2)", "forcing", ok_T, ctx=ctxB)
    # (c) innovation steps
    ok_id, ok_pos, ok_dec, ok_br = [], [], [], []
    dm = {m: r(m) - r(m + 1) for m in range(B, 2 * B + lmax + 1)}
    steps = {}
    for l in lags:
        D = [delta[l][i] - delta[l][i + 1] for i in range(B - 1)]   # n in [B, 2B-2]
        steps[l] = D
        for i, Dn in enumerate(D):
            n = B + i
            ok_id.append(Dn == sum((16 ** (l - j) * dm[n + j] for j in range(1, l + 1)), Fraction(0)))
            ok_pos.append(Dn > 0)
            ok_br.append(16 ** (l - 1) * dm[n + 1] <= Dn <= Fraction(16, 15) * 16 ** (l - 1) * dm[n + 1])
            if i + 1 < len(D):
                ok_dec.append(D[i + 1] < Dn)
    led.exact(pr, "3c_step_identity_sum_16^(l-j)_delta(n+j)", "forcing", ok_id, ctx=ctxB)
    led.exact(pr, "3c_step_positive", "forcing", ok_pos, ctx=ctxB)
    led.exact(pr, "3c_step_strictly_decreasing_in_n", "forcing", ok_dec, ctx=ctxB)
    led.exact(pr, "3c_step_bracket_16^(l-1)delta(n+1)_to_(16/15)16^(l-1)delta(n+1)", "forcing", ok_br, ctx=ctxB)
    out["iad03"] = {"tail_enclosure_induced_width_max": enc_width, "n_innovations_checked": len(ok_routes)}
    log(f"  B={B}: PR-1.3 done ({time.time() - t_start:.1f}s)")

    # ================= PR-1.4 (IAD-04) =================
    pr = "PR-1.4"
    Zfull: dict = {h: {} for h in modes}
    dpairs = {l: [frac_pair(x) for x in delta[l]] for l in lags}
    iad04: dict = {str(h): {} for h in modes}
    age_ladder: dict = {str(h): {} for h in modes}
    pr21_42: list = []
    intervals = {}
    for l in lags:
        N = B - l
        rg = rng_for("kl-intervals", B, l)
        ivs = []
        for _ in range(n_sub):
            a_, b_ = sorted((rg.randint(B, 2 * B - 1 - l), rg.randint(B, 2 * B - 1 - l)))
            ivs.append((a_, b_))
        intervals[l] = ivs
        # exact size facts for (4.3)
        cap = Fraction(16 ** l, 64 * B * B)
        ok43 = [0 < delta[l][i] <= 16 ** l * r(B + i + 1) / 15 < cap for i in range(B)]
        led.exact(pr, "4.3_exact_0_lt_Delta_le_16^l_r(n+1)/15_lt_16^l/(64B^2)", "forcing", ok43,
                  ctx={"B": B, "lag": l})
        for h in modes:
            Zf = np.array([phase(h * a, d) for a, d in dpairs[l]])   # n in [B, 2B-1]
            Zfull[h][l] = Zf
            Z = Zf[:N]
            ctx = {"B": B, "h": h, "lag": l}
            rhs43 = PI32 * h * 16 ** l / B ** 2
            dev = np.abs(Zf - 1)
            led.ineq(pr, "4.3_|e(hDelta)-1|_le_(pi/32)h16^l/B^2", "forcing", dev, rhs43, ctx=ctx,
                     detail=lambda i: {"n": B + i})
            EZ = complex(Z.mean())
            regime = ("below_2log16B" if 16 ** l <= B ** 2 else
                      ("window_2_to_3_log16B" if 16 ** l < B ** 3 else "beyond_3log16B"))
            age_ladder[str(h)][lag_key(l)] = {"abs_E_Z_uniform": abs(EZ), "abs_sum_over_B": abs(complex(Z.sum())) / B,
                                         "l_over_log16B": l / log2_16B, "regime": regime,
                                         "max_dev_from_1": float(dev.max())}
            row = {"E_Z": cjson(EZ), "kl_admissible": kl_admissible(B, h, l)}
            P = np.concatenate([[0j], np.cumsum(Z)])
            if kl_admissible(B, h, l):
                lam = kl_lambda(B, h, l)
                lamf = float(lam)
                KB = kl_bound(lam)
                # exact Kusmin-Landau hypotheses: g(n) = h(Delta(n) - Delta(n+1)), n in [B, 2B-2-l]
                g = [h * steps[l][i] for i in range(N - 1)]
                led.exact(pr, "KL_step_strictly_decreasing", "forcing",
                          [g[i + 1] < g[i] for i in range(len(g) - 1)], ctx=ctx)
                led.exact(pr, "KL_step_in_[lambda,1/2]", "forcing", [lam <= gi <= Fraction(1, 2) for gi in g],
                          ctx=ctx, detail=lambda i: {"n": B + i})
                sums = np.array([abs(P[b_ - B + 1] - P[a_ - B]) for a_, b_ in ivs])
                led.ineq(pr, "4.1_random_subintervals_|sum_I|_le_cot(pi lambda/2)", "forcing", sums, KB,
                         ctx=ctx, detail=lambda i, ivs=ivs: {"interval": list(ivs[i])})
                full = abs(P[-1])
                allmax = max(float(np.abs(P[i + 1:] - P[i]).max()) for i in range(N))
                led.ineq(pr, "4.1_all_subintervals_max_|sum_I|_le_cot(pi lambda/2)", "forcing", [allmax], KB,
                         ctx=ctx)
                # monotone Basel weights corollary: |sum_I p_n Z_n| <= p_(min I) cot(pi lambda/2)
                Pw = np.concatenate([[0j], np.cumsum(p[:N] * Z)])
                wsums = [abs(Pw[b_ - B + 1] - Pw[a_ - B]) for a_, b_ in ivs] + [abs(Pw[-1])]
                wbounds = [p[a_ - B] * KB for a_, _ in ivs] + [p[0] * KB]
                led.ineq(pr, "4.1_corollary_monotone_weights", "forcing", wsums, wbounds, ctx=ctx)
                row.update({"lambda": lamf}, KL_bound=KB, max_random_I=float(sums.max()), full_interval=full,
                           max_all_I=allmax, ratio_all_I_to_bound=allmax / KB,
                           g_min=float(g[-1]), g_max=float(g[0]))
                prog = {}
                for q in PROGRESSION_MODULI:
                    if not kl_admissible(B, h, l, q):
                        continue
                    gq = [h * (delta[l][i] - delta[l][i + q]) for i in range(N - q)]
                    led.exact(pr, "KL_progression_step_in_[q lambda,1/2]", "forcing",
                              [q * lam <= x <= Fraction(1, 2) for x in gq], ctx=dict(ctx, q=q))
                    led.exact(pr, "KL_progression_step_strictly_decreasing", "forcing",
                              [gq[i + 1] < gq[i] for i in range(len(gq) - 1)], ctx=dict(ctx, q=q))
                    KBq = kl_bound(q * lam)
                    vals, maxcell = [], 0.0
                    for a in range(q):
                        first = B + ((a - B) % q)
                        idx = np.arange(first - B, N, q)
                        Pc = np.concatenate([[0j], np.cumsum(Z[idx])])
                        for a_, b_ in ivs:
                            klo = max(0, (a_ - first + q - 1) // q)
                            khi = (b_ - first) // q
                            vals.append(abs(Pc[khi + 1] - Pc[klo]) if khi >= klo else 0.0)
                        allq = max(float(np.abs(Pc[i + 1:] - Pc[i]).max()) for i in range(len(idx)))
                        vals.append(allq)
                        maxcell = max(maxcell, abs(Pc[-1]) / len(idx))
                    led.ineq(pr, "4.1_progression_|sum_(I, n=a mod q)|_le_cot(pi q lambda/2)", "forcing", vals,
                             KBq, ctx=dict(ctx, q=q))
                    c1, c2, c3, gaps = kl_constant_chain(B, h, l, q)
                    led.ineq(pr, "4.1_corollary_||E[Z|F_q]||_inf_le_(q/(B-l-q))cot(pi q lambda/2)", "forcing",
                             [maxcell], [c1], ctx=dict(ctx, q=q))
                    led.ineq(pr, "4.1_corollary_constant_chain_c1_le_c2_le_4401B^2/((1-(l+q)/B)h16^l)_mp50",
                             "forcing", [0.0, 0.0], gaps, ctx=dict(ctx, q=q), tol=0.0)
                    prog[str(q)] = {"bound": KBq, "max_abs_sum": max(vals), "cond_exp_sup": maxcell,
                                    "cond_exp_bound": c1}
                row["progressions"] = prog
            # (4.2) for PR-2.1: lags in the window with admissible delta
            if in_open_window(B, l):
                dmax_ = min(l / log2_16B - 2, 3 - l / log2_16B, 0.5)
                dmin_ = math.log(h) / math.log(B)
                if dmax_ > 0 and dmax_ > dmin_:
                    bound42 = KL_CONSTANT / (h * B ** dmax_)
                    obs = max([abs(P[b_ - B + 1] - P[a_ - B]) / B for a_, b_ in ivs] + [abs(P[-1]) / B])
                    pr21_42.append({"h": h, "lag": l, "delta_sup": dmax_, "observed_max_(1/B)|sum_I|": obs,
                                    "bound_4401/(h B^delta)": bound42, "met": obs <= bound42})
            iad04[str(h)][lag_key(l)] = row
    out["iad04"] = iad04
    out["age_ladder"] = age_ladder
    log(f"  B={B}: PR-1.4 done ({time.time() - t_start:.1f}s)")

    # ================= PR-1.5 (IAD-05) and PR-2.1 seed independence =================
    pr = "PR-1.5"
    partitions: dict = {}
    for l in lags:
        N = B - l
        parts = []
        ns = np.arange(B, 2 * B - l)
        for q in RESIDUE_FILTRATIONS:
            parts.append((f"residue_mod_{q}", ns % q, q))
        parts.append(("full_clock_each_n_own_cell", np.arange(N), N))
        for j in range(N_RANDOM_PARTITIONS):
            rg = rng_for("partition-assign", B, l, j)
            parts.append((f"random_assign_8cells_{j}", np.array([rg.randrange(8) for _ in range(N)]), 8))
        for j in range(N_RANDOM_PARTITIONS):
            rg = rng_for("partition-blocks", B, l, j)
            m = rg.randint(2, 16)
            cuts = sorted(rg.sample(range(1, N), m - 1))
            lab = np.zeros(N, dtype=np.int64)
            for c_ in cuts:
                lab[c_:] += 1
            parts.append((f"random_blocks_{j}", lab, m))
        partitions[l] = parts
    tau_pairs = {l: [frac_pair(lo[n + l] - lo[n]) for n in range(B, 2 * B - l)] for l in lags}
    iad05: dict = {s: {} for s in SEEDS}
    Eown: dict = {s: {} for s in SEEDS}
    cU: dict = {s: {} for s in SEEDS}
    Eseq: dict = {s: {} for s in SEEDS}
    pr21_bits: list = []
    # own-route innovations: exact rationals from each seed's own states (mod 1)
    own_innov: dict = {s: {} for s in SEEDS}
    for s in SEEDS:
        if s == "2_coherent":
            continue
        for l in lags:
            rows = []
            for i in range(B - l):
                a1, d1 = Upairs[s][i + l]
                a0, d0 = Upairs[s][i]
                rows.append((a1 * d0 - 16 ** l * a0 * d1, d0 * d1))
            own_innov[s][l] = rows
    for s in SEEDS:
        for h in modes:
            Eseq[s][h] = np.array([phase(h * a, d) for a, d in Upairs[s]])
            ww = Eseq[s][h]
            cU[s][h] = {d: complex(np.vdot(ww[: B - d], ww[d:]) / B) for d in range(1, dmax + 1)}
    for s in SEEDS:
        for h in modes:
            iad05[s][str(h)] = {}
            for l in lags:
                N = B - l
                ctx = {"B": B, "h": h, "lag": l}
                Z = Zfull[h][l][:N]
                mult = h * (16 ** l - 1)
                A = np.array([phase(mult * a, d) for a, d in Upairs[s][:N]])
                C = cexact[s][h][l]
                Tph = np.array([phase(-h * a, d) for a, d in tau_pairs[l]])
                err1 = np.abs(A * Z - C * Tph)
                err2 = np.abs(A - C * np.conj(Z) * Tph)
                led.ident(pr, "5.1_A_Z_eq_C_e(-h tau)", s, err1, ctx=ctx, detail=lambda i: {"n": B + i})
                led.ident(pr, "5.1_A_eq_C_conj(Z)_e(-h tau)", s, err2, ctx=ctx, detail=lambda i: {"n": B + i})
                sup_tau = float(np.abs(Tph - 1).max())
                tb = PI32 * h / B ** 2
                led.ineq(pr, "sup|e(-h tau)-1|_le_(pi/32)h/B^2", s, [sup_tau], tb, ctx=ctx)
                EA, EZ, EC = complex(A.mean()), complex(Z.mean()), complex(C.mean())
                cov = complex((A * Z).mean()) - EA * EZ
                led.ineq(pr, "corollary1_|Cov(A,Z)-E[C]|_le_|E[Z]|+(pi/32)h/B^2", s, [abs(cov - EC)],
                         [abs(EZ) + tb], ctx=ctx)
                lhs52, rhs52, names = [], [], []
                for name, lab, ncell in partitions[l]:
                    nz = l1_cond_mean(Z, lab, ncell)
                    nc = l1_cond_mean(C, lab, ncell)
                    aF = l1_deviation(A, lab, ncell)
                    lhs52.append(abs(nz - nc))
                    rhs52.append(2 * aF + tb)
                    names.append(name)
                led.ineq(pr, "5.2_| ||E[Z|F]||_1-||E[C|F]||_1 |_le_2a_F+(pi/32)h/B^2", s, lhs52, rhs52, ctx=ctx,
                         detail=lambda i, names=names: {"partition": names[i]})
                mAZ = complex((A * Z).sum() / B)
                led.ident("PR-1.6", "c^U_d_equals_shell_mean_of_A_Z", s, [abs(mAZ - cU[s][h][l])], ctx=ctx)
                # own-route innovation phase (PR-2.1 seed independence)
                if s == "2_coherent":
                    own = [frac_pair(16 ** l * lo[n] - lo[n + l]) for n in range(B, 2 * B - l)]
                    Zown = np.array([phase(h * a, d) for a, d in own])
                    exact_equal = None
                else:
                    own = own_innov[s][l]
                    Zown = np.array([phase(h * a, d) for a, d in own])
                    exact_equal = all(((h * a) % d) * dq == pq * d
                                      for (a, d), (pq, dq) in zip(own, (((h * x) % y, y) for x, y in dpairs[l][:N])))
                Eown[s].setdefault(h, {})[l] = complex(Zown.mean())
                pr21_bits.append({"seed": s, "h": h, "lag": l, "exact_rational_equal": exact_equal,
                                  "elementwise_bit_identical": bool(np.array_equal(Zown, Z)),
                                  "max_abs_diff": float(np.abs(Zown - Z).max())})
                iad05[s][str(h)][lag_key(l)] = {"E_A": cjson(EA), "E_Z": cjson(EZ), "E_C": cjson(EC), "Cov_AZ": cjson(cov),
                                            "abs_Cov": abs(cov), "max_err_5.1a": float(err1.max()),
                                            "max_err_5.1b": float(err2.max()),
                                            "corollary1_lhs": abs(cov - EC), "corollary1_rhs": abs(EZ) + tb,
                                            "min_margin_5.2": float(min(r_ - l_ for l_, r_ in zip(lhs52, rhs52)))}
    out["iad05"] = iad05
    log(f"  B={B}: PR-1.5 done ({time.time() - t_start:.1f}s)")

    # ================= PR-1.6 (IAD-06) =================
    pr = "PR-1.6"
    iad06: dict = {}
    Hs = []
    for j in range(N_RANDOM_H):
        rg = rng_for("vdc-H", B, j)
        k = rg.randint(2, 6)
        Hs.append(sorted(rg.sample(range(0, H_SET_MAX + 1), k)))
    for c in SEQ_CONTROLS:
        iad06[c] = {}
        for h in modes:
            ctx = {"B": B, "h": h}
            W = complex(w[c][h].mean())
            W2 = abs(W) ** 2
            row = {"W_B": cjson(W), "abs_W_B_sq": W2,
                   "c_d_for_d_1_to_dmax": [cjson(c_d[c][h][d]) for d in range(1, dmax + 1)]}
            if c in SEEDS:
                tb = PI32 * h / B ** 2
                diffs = [abs(c_d[c][h][d] - cU[c][h][d]) for d in range(1, dmax + 1)]
                led.ineq(pr, "6a_transport_|c_d-c^U_d|_le_(pi/32)h/B^2", c, diffs, tb, ctx=ctx,
                         detail=lambda i: {"d": i + 1})
                row["c_U_d_for_d_1_to_dmax"] = [cjson(cU[c][h][d]) for d in range(1, dmax + 1)]
                row["transport_max_ratio_to_bound"] = max(diffs) / tb
            rhs_r = [vdc_rhs(H, c_d[c][h], B) for H in Hs]
            led.ineq(pr, "6.1_random_H_|W|^2_le_rhs", c, [W2] * len(Hs), rhs_r, ctx=ctx,
                     detail=lambda i: {"H": Hs[i]})
            ap = {}
            for k in (2, 3, 4):
                H = [j * l0 for j in range(k)]
                r61 = vdc_rhs(H, c_d[c][h], B)
                r62 = vdc_rhs_ap(k, l0, c_d[c][h], B)
                led.ineq(pr, "6.1_AP_H_|W|^2_le_rhs", c, [W2], [r61], ctx=dict(ctx, k=k))
                led.ident(pr, "6.2_closed_form_equals_6.1_on_AP", c, [r61 - r62], ctx=dict(ctx, k=k))
                ap[str(k)] = {"H": H, "rhs_6.1": r61, "rhs_6.2": r62}
            row["AP"] = ap
            row["random_H_rhs"] = rhs_r
            iad06[c][str(h)] = row
    out["iad06"] = iad06
    out["random_H_sets"] = Hs
    log(f"  B={B}: PR-1.6 done ({time.time() - t_start:.1f}s)")

    # ================= PR-2 predictions =================
    pr2: dict = {}
    # PR-2.1
    bit_rows = []
    for h in modes:
        for l in lags:
            vals = [Eown[s][h][l] for s in SEEDS]
            bit_rows.append({"h": h, "lag": l, "E_Z_by_seed": {s: cjson(Eown[s][h][l]) for s in SEEDS},
                             "bit_identical_across_seeds_1_to_5": all(v == vals[0] for v in vals),
                             "bit_identical_across_rational_seeds_1_3_4_5":
                                 all(Eown[s][h][l] == Eown["1_true"][h][l] for s in ("3_shadow", "4_alias", "5_hijack"))})
    pr2["PR-2.1"] = {
        "predicted": "untwisted E[Z] bit-identical across seeds 1-5 (each from its own exact state route) "
                     "and obeys (4.2) on window lags with admissible delta",
        "observed": {"rows": bit_rows, "elementwise": pr21_bits, "eq_4.2": pr21_42},
        "met": all(rw["bit_identical_across_seeds_1_to_5"] for rw in bit_rows) and all(x["met"] for x in pr21_42),
        "met_bit_identity": all(rw["bit_identical_across_seeds_1_to_5"] for rw in bit_rows),
        "met_4.2": all(x["met"] for x in pr21_42),
        "note": "seed 2 (s=-x) has no rational state; its own route uses 16^l T_n - T_(n+l) from the tail "
                "enclosure (lower endpoints), so bit identity there is a float-rounding statement",
    }
    # PR-2.2
    rows = []
    for h in modes:
        for l in out["ap_lags"]:
            thr = 4 / math.sqrt(B - l)
            row = {"h": h, "lag": l, "true_abs_cU": abs(cU["1_true"][h][l]), "true_threshold_4/sqrt(B-l)": thr,
                   "true_met": abs(cU["1_true"][h][l]) <= thr}
            for s in ("2_coherent", "3_shadow", "5_hijack"):
                row[f"{s}_Re_cU"] = cU[s][h][l].real
                row[f"{s}_met_Re_ge_0.99"] = cU[s][h][l].real >= 0.99
                row[f"{s}_violates_true_seed_bound"] = abs(cU[s][h][l]) > thr
            dif = abs(cU["4_alias"][h][l] - cU["1_true"][h][l])
            row["4_alias_abs_diff_from_true"] = dif
            row["4_alias_met"] = dif <= 1e-12
            rows.append(row)
    pr2["PR-2.2"] = {"predicted": "true |c^U_l| <= 4/sqrt(B-l) at l in {l0,2l0,3l0}; controls 2,3,5 Re c^U_l >= 0.99; "
                                  "control 4 equals true to 1e-12",
                     "observed": rows,
                     "met_true": all(r_["true_met"] for r_ in rows),
                     "met_controls_2_3_5": all(r_[f"{s}_met_Re_ge_0.99"] for r_ in rows
                                               for s in ("2_coherent", "3_shadow", "5_hijack")),
                     "met_control_4": all(r_["4_alias_met"] for r_ in rows)}
    # PR-2.3
    rows = []
    for h in modes:
        for l in window_lags:
            row = {"h": h, "lag": l, "threshold_true_5/sqrt(B)": 5 / math.sqrt(B)}
            for s in SEEDS:
                row[f"{s}_abs_Cov"] = abs(complex(*iad05[s][str(h)][lag_key(l)]["Cov_AZ"]))
            row["true_met"] = row["1_true_abs_Cov"] <= 5 / math.sqrt(B)
            row["coherent_met_ge_0.9"] = row["2_coherent_abs_Cov"] >= 0.9
            rows.append(row)
    cor1 = led.slots.get(("PR-1.5", "corollary1_|Cov(A,Z)-E[C]|_le_|E[Z]|+(pi/32)h/B^2"), {})
    pr2["PR-2.3"] = {"predicted": "|Cov(A,Z)-E[C]| <= |E[Z]|+(pi/32)|h|B^-2 (PR-1 grade, see PR-1.5); true seed "
                                  "|Cov| <= 5/sqrt(B) on window lags; control 2 |Cov| >= 0.9",
                     "window_definition": "integer l with 2 log16 B < l < 3 log16 B (B^2 < 16^l < B^3)",
                     "observed": rows, "pr1_grade_part_failures": cor1.get("failures"),
                     "met_true": all(r_["true_met"] for r_ in rows),
                     "met_coherent": all(r_["coherent_met_ge_0.9"] for r_ in rows),
                     "met_pr1_grade_part": cor1.get("failures") == 0}
    # PR-2.4
    rows = []
    for h in modes:
        for k in (2, 3, 4):
            thr = 1 / k + 3 / math.sqrt(B)
            row = {"h": h, "k": k, "H": [j * l0 for j in range(k)], "true_threshold_1/k+3/sqrt(B)": thr}
            for c in SEQ_CONTROLS:
                row[f"{c}_rhs"] = iad06[c][str(h)]["AP"][str(k)]["rhs_6.1"]
            row["true_met"] = row["1_true_rhs"] <= thr
            row["coherent_met_ge_0.95"] = row["2_coherent_rhs"] >= 0.95
            for s in ("2_coherent", "3_shadow", "5_hijack"):
                row[f"{s}_violates_true_seed_bound"] = row[f"{s}_rhs"] > thr
            rows.append(row)
    pr2["PR-2.4"] = {"predicted": "rhs of (6.2), k=2,3,4: true <= 1/k + 3/sqrt(B); control 2 >= 0.95",
                     "observed": rows, "met_true": all(r_["true_met"] for r_ in rows),
                     "met_coherent": all(r_["coherent_met_ge_0.95"] for r_ in rows)}
    # PR-2.5
    rows = []
    for h in modes:
        row = {"h": h, "L": rB}
        for c in SEQ_CONTROLS:
            row[f"{c}_L_gamma_L"] = rB * iad02[c][str(h)]["gamma"][rB - 1]
        row["true_met"] = 0.4 <= row["1_true_L_gamma_L"] <= 1.6
        row["coherent_met_ge_0.8L"] = row["2_coherent_L_gamma_L"] >= 0.8 * rB
        for s in ("2_coherent", "3_shadow", "5_hijack"):
            row[f"{s}_outside_true_band"] = not (0.4 <= row[f"{s}_L_gamma_L"] <= 1.6)
        rows.append(row)
    pr2["PR-2.5"] = {"predicted": "Fejer at L=floor(sqrt B): true 0.4 <= L gamma_L <= 1.6; control 2 L gamma_L >= 0.8 L",
                     "observed": rows, "met_true": all(r_["true_met"] for r_ in rows),
                     "met_coherent": all(r_["coherent_met_ge_0.8L"] for r_ in rows)}
    out["PR-2"] = pr2

    # ================= PR-3 (in scope) =================
    roll = led.to_json()["by_control"]
    pr3: dict = {"hostile_seeds_pass_PR1": {}, "hostile_seeds_fail_true_seed_predictions": {}}
    for s in ("2_coherent", "3_shadow", "5_hijack"):
        pr3["hostile_seeds_pass_PR1"][s] = {
            prid: roll.get(prid, {}).get(s, {"checks": 0, "failures": 0}) for prid in
            ("PR-1.1", "PR-1.2", "PR-1.5", "PR-1.6")}
        pr3["hostile_seeds_fail_true_seed_predictions"][s] = {
            "PR-2.2_violates_true_bound_all": all(r_[f"{s}_violates_true_seed_bound"] for r_ in pr2["PR-2.2"]["observed"]),
            "PR-2.4_violates_true_bound_all": all(r_[f"{s}_violates_true_seed_bound"] for r_ in pr2["PR-2.4"]["observed"]),
            "PR-2.5_outside_true_band_all": all(r_[f"{s}_outside_true_band"] for r_ in pr2["PR-2.5"]["observed"]),
        }
    # alias: every phase statistic equal to the true seed
    alias_diffs = []
    for h in modes:
        alias_diffs.append(abs(complex(*iad06["4_alias"][str(h)]["W_B"]) - complex(*iad06["1_true"][str(h)]["W_B"])))
        alias_diffs += [abs(c_d["4_alias"][h][d] - c_d["1_true"][h][d]) for d in range(1, dmax + 1)]
        alias_diffs += [abs(cU["4_alias"][h][d] - cU["1_true"][h][d]) for d in range(1, dmax + 1)]
        alias_diffs += [abs(a_ - b_) for a_, b_ in zip(iad02["4_alias"][str(h)]["gamma"], iad02["1_true"][str(h)]["gamma"])]
        for l in lags:
            alias_diffs.append(abs(complex(*iad05["4_alias"][str(h)][lag_key(l)]["Cov_AZ"])
                                   - complex(*iad05["1_true"][str(h)][lag_key(l)]["Cov_AZ"])))
    pr3["alias_1_16"] = dict(pr3_alias, max_abs_diff_all_phase_statistics_vs_true=max(alias_diffs),
                             n_statistics_compared=len(alias_diffs))
    p17 = Fraction(16 ** B, 17)
    pr3["observation_periodic_1_17"] = {
        "dist_16^B_x'_to_Z_equals_1/17": core.dist_to_int(p17) == Fraction(1, 17),
        "W_B_vs_cos(2 pi h/17)": {str(h): {"W_B": iad06["6a_periodic_1_17"][str(h)]["W_B"],
                                           "cos": math.cos(2 * math.pi * h / 17)} for h in modes},
        "note": "IAD-08 item; recorded as an observation only (W_B = cos(2 pi h/17) exactly only for even B)",
    }
    out["PR-3"] = pr3
    log(f"  B={B}: done ({time.time() - t_start:.1f}s)")
    return out, led


# --------------------------------------------------------------------------------------------
# Driver
# --------------------------------------------------------------------------------------------
def summarize(shell_results: dict, ledgers: dict) -> dict:
    summ: dict = {"PR-1": {}, "PR-2": {}}
    for role in ("holdout", "calibration", "global"):
        agg: dict = {}
        for B, res in shell_results.items():
            if res["role"] != role:
                continue
            for (pr, sub), s in ledgers[B].slots.items():
                a = agg.setdefault(pr, {"checks": 0, "failures": 0, "strict_failures_inequalities": 0})
                a["checks"] += s["checks"]
                a["failures"] += s["failures"]
                a["strict_failures_inequalities"] += s.get("strict_failures", 0) or 0
        summ["PR-1"][role] = agg
    pr2: dict = {}
    for B, res in shell_results.items():
        if "PR-2" not in res:
            continue
        for pid, block in res["PR-2"].items():
            for key, val in block.items():
                if key.startswith("met"):
                    pr2.setdefault(pid, {}).setdefault(res["role"], {}).setdefault(key, {})[str(B)] = val
    for pid, roles in pr2.items():
        for role, keys in roles.items():
            for key, perB in keys.items():
                perB["all"] = all(v for k, v in perB.items() if k != "all")
    summ["PR-2"] = pr2
    return summ


def sanitize(obj):
    """Replace non-finite floats by strings so the JSON stays strict (nothing is dropped)."""
    if isinstance(obj, float) and not math.isfinite(obj):
        return repr(obj)
    if isinstance(obj, dict):
        return {str(k): sanitize(v) for k, v in obj.items()}
    if isinstance(obj, (list, tuple)):
        return [sanitize(v) for v in obj]
    if isinstance(obj, (np.floating,)):
        return sanitize(float(obj))
    if isinstance(obj, (np.integer,)):
        return int(obj)
    if isinstance(obj, (np.bool_,)):
        return bool(obj)
    return obj


def _is_leaf_array(x) -> bool:
    return isinstance(x, list) and all(
        isinstance(v, (int, float, str, bool)) or v is None
        or (isinstance(v, list) and all(isinstance(u, (int, float, str, bool)) or u is None for u in v))
        for v in x)


def dumps_compact(obj, indent: int = 0) -> str:
    """Deterministic JSON: sorted keys, one key per line, numeric leaf arrays on one line."""
    pad = " " * indent
    if isinstance(obj, dict):
        if not obj:
            return "{}"
        items = [f'{pad} {json.dumps(str(k))}: {dumps_compact(obj[k], indent + 1)}' for k in sorted(obj, key=str)]
        return "{\n" + ",\n".join(items) + "\n" + pad + "}"
    if isinstance(obj, list):
        if _is_leaf_array(obj):
            return json.dumps(obj, separators=(",", ":"), allow_nan=False)
        items = [f"{pad} {dumps_compact(v, indent + 1)}" for v in obj]
        return "[\n" + ",\n".join(items) + "\n" + pad + "]"
    return json.dumps(obj, allow_nan=False)


def run(shells, modes=MODES, n_sub=N_SUBINTERVALS, log=None):
    log = log or (lambda *a: None)
    ledgers: dict = {}
    shell_results: dict = {}
    gl = Ledger()
    tmax = 2 * max(B for B, _ in shells) + 64
    lmx = max(lag_max(B) for B, _ in shells)
    log("global forcing checks ...")
    glob = forcing_global_checks(gl, tmax, tmax + lmx + 2)
    ledgers["global"] = gl
    shell_results["global"] = {"role": "global", **glob, "PR-1": gl.to_json()}
    for B, role in shells:
        log(f"shell B={B} ({role}) ...")
        res, led = run_shell(B, role, modes=modes, n_sub=n_sub, log=log)
        res["PR-1"] = led.to_json()
        shell_results[str(B)] = res
        ledgers[str(B)] = led
    results = {
        "meta": {
            "dossier": "research/2026-11-11/innovation_arithmetic_decoupling",
            "script": "probe_analytic.py",
            "scope": "PR-1.1..PR-1.6, PR-2.1..PR-2.5 and the PR-3 items about IAD-01..IAD-06 "
                     "(PREREGISTRATION.md); AT-07 (control 8) and PR-1.7..PR-1.11 belong to the arithmetic probe",
            "baseline_commit_of_preregistration": "e3f4111b (PREREGISTRATION.md committed before this probe)",
            "holdout_shells": list(HOLDOUT_SHELLS), "calibration_shells": list(CALIBRATION_SHELLS),
            "shells_run": [[B, role] for B, role in shells], "modes_h": list(modes),
            "tolerances": {"identity": TOL_IDENTITY, "iad02_preregistered": TOL_IAD02,
                           "float_inequality": TOL_INEQUALITY,
                           "rule": "inequality passes iff rhs-lhs >= -tol; strict_failures counts rhs-lhs < 0; "
                                   "identities pass iff |err| <= tol; exact checks are Fraction/integer"},
            "phase_evaluation": "e(t) = cmath.exp(2 pi i t) after exact integer reduction of t mod 1 to (-1/2,1/2]",
            "random_seeds": "random.Random(int(sha256('iad-analytic|<purpose>|<params>')[:8]))",
            "n_random_subintervals": n_sub, "n_random_H": N_RANDOM_H,
            "n_random_partitions_per_family": N_RANDOM_PARTITIONS,
            "interpretations": [
                "PR-2.3 'in the window' = integer lags with 2 log16 B < l < 3 log16 B.",
                "PR-2.4 uses H = {0, l0, ..., (k-1) l0} (the preregistered l0 design), k = 2, 3, 4.",
                "PR-2.1 (4.2) is evaluated at the supremum of admissible delta (min(l/log16B-2, 3-l/log16B, 1/2), "
                "requiring it to exceed log_B h); window lags without admissible delta are skipped.",
                "(5.2) random partitions: 20 random 8-cell assignments AND 20 random contiguous-block partitions.",
                "PR-1.2 grid: all 1 <= J < L <= 2 floor(sqrt B) plus L in {B/8, B/4, B/2, B} (floors); J = L is trivial.",
                "PR-1.1 windows: preregistered {2,3,5,8,floor(sqrt B),2 floor(sqrt B)} plus the extra windows.",
            ],
        },
        "shells": shell_results,
    }
    results["summary"] = summarize(shell_results, ledgers)
    results["summary"]["any_PR1_failure"] = bool(exit_code(ledgers.values()))
    return results, ledgers


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--quick", action="store_true", help="only B in {64, 200}; no file unless --out")
    ap.add_argument("--out", type=Path, default=None, help="output JSON path")
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args(argv)
    log = (lambda *a: None) if args.quiet else (lambda *a: print(*a, file=sys.stderr, flush=True))
    if args.quick:
        shells = [(64, "calibration"), (200, "holdout")]
        out = args.out
    else:
        shells = [(B, "calibration") for B in CALIBRATION_SHELLS] + [(B, "holdout") for B in HOLDOUT_SHELLS]
        out = args.out or DEFAULT_OUT
    t0 = time.time()
    results, ledgers = run(shells, log=log)
    if out is not None:
        out.write_text(dumps_compact(sanitize(results)) + "\n")
        log(f"wrote {out}")
    code = exit_code(ledgers.values())
    s = results["summary"]["PR-1"]
    for role in ("global", "calibration", "holdout"):
        for prid, a in sorted(s[role].items()):
            log(f"{role:11s} {prid}: checks={a['checks']} failures={a['failures']} "
                f"strict_ineq_failures={a['strict_failures_inequalities']}")
    log(f"PR-1 exit code {code}; wall {time.time() - t0:.1f}s")
    return code


if __name__ == "__main__":
    sys.exit(main())
