"""RENORM transport: the exact x16 Fourier renormalization of the original BBP source.

Add-only research instrument for the selected-current front. No pi digits, fitted
randomness, Galois average, or normality proof. The original four signed Mellin
terms and U_0 = 0 are immutable. Exponential-sum coefficients are measured at fixed
mpmath precision (an INSTRUMENT, calibrated on known cases) over exact rational phases.

RENORM-1 (proved; this instrument verifies it on held-out epochs):
    c_A(h) = c_A(16 h) + eps_A(h),        c_A(h) = A^{-1} sum_{n=A}^{2A-1} e(h U_n),
    |eps_A(h)| <= 2/A + 15 pi |h| / (4 A (8A - 15))          (rigorous, A >= 2)
               ~= 2/A + (15 pi / 32) |h| / A^2               (asymptotic).

RENORM-2 (barrier corollary, CORRECTED 2026-11-03): iterate RT-1 at a COMMON depth j
across the whole low band {1<=|h|<=H} (NOT a per-h depth). Then h -> 16^j h is
injective on Z (multiplication by a fixed nonzero integer), carrying the band
bijectively onto H distinct high frequencies {16^j h}. The accumulated error is

    |sum_{i=0}^{j-1} eps_A(16^i h)| <= 2j/A + pi|h|(16^j - 1)/(4A(8A-15))

(GEOMETRIC in j; the frequency-independent denominator 8A-15 does NOT carry a 16^i).
Choosing j = floor(log_16(A^{3/2}/H)) keeps 16^j|h| <= A^{3/2} for every |h|<=H, so the
error is 2j/A + O(A^{-1/2}) = o(1) UNIFORMLY over the band. Hence each low coefficient
equals a DISTINCT high coefficient up to o(1): mass is relocated up the frequency ladder
at equal cardinality, never annihilated. The recursion is information-preserving and
CANNOT, by itself, drive the SC-8 band second moment to o(K_A); a genuine high-frequency
equidistribution estimate (the OPEN input) is required. Obstruction map, not progress.

DEFECTS CORRECTED in this revision (were in the original PROOFS.md RT-03; regression-tested):
  D1  old per-h depth j*=floor(.5 log_16(A^{3/2}/|h|)) reaches 16^{j*}|h| ~ A^{3/4} sqrt|h|,
      NOT A^{3/2}: the leading 1/2 is wrong.  (reached_frequency_old / depth_old)
  D2  that per-h depth is NON-injective: at A=16^8, h=1 and h=16 both map to 16^6, so the
      "bijective band transport" fails.  Fix: a COMMON depth (common_depth) is injective.
  D3  the accumulated-error denominator was written 8*16^i*A-15 (frequency-dependent), which
      stays linear in j and masks the geometric 16^j growth.  Correct: acc_error_bound.
  D0  band<->J was written as an equivalence; only unweighted-band=o(K) ==> J=o(K) is proved
      (SC-8, sinc^2<=1). The converse is FALSE: the equally-spaced cloud x_j=j/q has J_q=1 but
      unweighted band = 2q (the sinc^2 weight is zero on the multiples of q where its mass
      sits).  band_vs_J_cloud exhibits it.
pi base-16 normality, the signed Weyl gate S_N(h)=o(N), and RH are OPEN.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from fractions import Fraction as F
from math import lcm
from pathlib import Path

import mpmath as mp

DPS = 50  # fixed instrument precision; deterministic at a pinned dps
# Preregistered held-out epochs and frequencies (NOT the selected_current_front A=40/80/160
# fit set alone; includes fresh 50/100/200/256). Declared before measurement.
HELDOUT_A = (40, 50, 64, 100, 128, 200, 256)
HELDOUT_H = (1, 2, 3, 5, 8, 13, 21, 50, 100, 200)


def source_force(n: int) -> F:
    """Exactly the original BBP four signed terms; n is source time (immutable)."""
    if type(n) is not int or n < 1:
        raise ValueError("original BBP source time n>=1 required")
    return F(4, 8 * n - 7) - F(2, 8 * n - 4) - F(1, 8 * n - 3) - F(1, 8 * n - 2)


def source_epoch(A: int) -> list[F]:
    """Literal zero-seeded original phases U_n mod 1 for n in [A, 2A)."""
    if type(A) is not int or A < 2:
        raise ValueError("A>=2 required")
    z = F(0)
    out = []
    for n in range(1, 2 * A):
        z = (16 * z + source_force(n)) % 1
        if n >= A:
            out.append(z)
    return out


def modular_epoch(A: int) -> list[F]:
    """Independent blind evaluator: one common ODD integer conductor, same source."""
    if type(A) is not int or A < 2:
        raise ValueError("A>=2 required")
    fs = [source_force(n) for n in range(1, 2 * A)]
    M = 1
    for f in fs:
        M = lcm(M, f.denominator)
    if M % 2 != 1:
        raise AssertionError("original BBP conductor must be odd")
    z = 0
    out = []
    for n, f in enumerate(fs, 1):
        z = (16 * z + f.numerator * (M // f.denominator)) % M
        if n >= A:
            out.append(F(z, M))
    return out


def _e(x: F):
    return mp.e ** (2j * mp.pi * mp.mpf(x.numerator) / mp.mpf(x.denominator))


def coeff(phases, h: int):
    """c_A(h) = A^{-1} sum e(h U_n), measured at fixed precision DPS."""
    return sum((_e(F(h) * x) for x in phases), mp.mpc(0)) / len(phases)


def renorm_residual(phases, h: int):
    """|c_A(h) - c_A(16 h)| for one epoch cloud."""
    return abs(coeff(phases, h) - coeff(phases, 16 * h))


def eps_bound_rigorous(A: int, h: int) -> float:
    return 2.0 / A + 15.0 * float(mp.pi) * abs(h) / (4 * A * (8 * A - 15))


def eps_bound_asymptotic(A: int, h: int) -> float:
    return 2.0 / A + (15.0 * float(mp.pi) / 32.0) * abs(h) / A ** 2


# --- RENORM-2 corrected barrier: common-depth injective transport ---------------

def depth_old(A: int, h: int) -> int:
    """DEFECTIVE per-h depth from the original RT-03 (kept to regression-test D1/D2)."""
    from math import floor, log
    return floor(0.5 * (log(A ** 1.5 / abs(h)) / log(16)))


def reached_frequency_old(A: int, h: int) -> int:
    """16^{j*}*|h| for the old per-h depth. Reaches ~A^{3/4} sqrt|h|, NOT A^{3/2} (D1)."""
    return 16 ** depth_old(A, h) * abs(h)


def common_depth(A: int, H: int) -> int:
    """Correct COMMON depth across the whole band {1<=|h|<=H}: keeps 16^j H <= A^{3/2}.

    Fixed j => h -> 16^j h is injective on Z (D2 fix)."""
    from math import floor, log
    if H < 1:
        raise ValueError("H>=1")
    return max(0, floor(log(A ** 1.5 / H) / log(16)))


def acc_error_bound(A: int, h: int, j: int) -> float:
    """CORRECT accumulated transport error over depth j (D3 fix):

        2j/A + pi|h|(16^j - 1)/(4A(8A-15)).

    The denominator 8A-15 is frequency-independent; the 16^j growth is geometric."""
    return 2.0 * j / A + float(mp.pi) * abs(h) * (16 ** j - 1) / (4 * A * (8 * A - 15))


def acc_error_true(phases, h: int, j: int):
    """Exact measured |sum_{i<j} eps_A(16^i h)| = |c_A(h) - c_A(16^j h)| (telescopes)."""
    return abs(coeff(phases, h) - coeff(phases, 16 ** j * h))


def band_vs_J_cloud(q: int):
    """D0 counterexample: equally-spaced cloud x_j=j/q, j=0..q-1.

    Returns (J_q, unweighted_band) with J_q computed from the tent kernel and the
    unweighted band = #{1<=|h|<=q^2 : q | h}. Exactly J_q=1 and band=2q, so
    'J=o(K) => unweighted-band=o(K)' is FALSE (only band => J is proved)."""
    xs = [F(j, q) for j in range(q)]

    def nn(d):
        d = d % 1
        return min(d, 1 - d)

    S = F(0)
    for a in range(q):
        for b in range(q):
            val = 1 - q * nn(xs[a] - xs[b])
            if val > 0:
                S += val
    J = (F(q) / F(q * q)) * S
    band = sum(1 for hh in list(range(1, q * q + 1)) + list(range(-q * q, 0)) if hh % q == 0)
    return J, band


def _phase_sha(phases) -> str:
    raw = ";".join(f"{x.numerator}/{x.denominator}" for x in phases).encode()
    return hashlib.sha256(raw).hexdigest()


def build_receipt() -> dict:
    mp.mp.dps = DPS
    rows = []
    worst_rig = 0.0
    worst_asy = 0.0
    violations = 0
    blind_max = mp.mpf(0)
    for A in HELDOUT_A:
        ph = source_epoch(A)
        phm = modular_epoch(A)
        # calibration 1: c_A(0) == 1 exactly
        c0 = coeff(ph, 0)
        assert abs(c0 - 1) < mp.mpf(10) ** (-DPS + 5), "c_A(0) must be 1"
        # calibration 2: two blind sources agree
        for h in (1, 3, 7, 50):
            blind_max = max(blind_max, abs(coeff(ph, h) - coeff(phm, h)))
        for h in HELDOUT_H:
            res = float(renorm_residual(ph, h))
            br = eps_bound_rigorous(A, h)
            ba = eps_bound_asymptotic(A, h)
            within = res <= br
            if not within:
                violations += 1
            worst_rig = max(worst_rig, res / br)
            worst_asy = max(worst_asy, res / ba)
            rows.append({"A": A, "h": h,
                         "residual_dps": mp.nstr(mp.mpf(res), 12),
                         "bound_rigorous": f"{br:.12e}",
                         "within_rigorous_bound": within})
        rows[-1]["source_phase_sha256"] = _phase_sha(ph)

    # --- defect regression (D0..D3): witnesses that the corrected claims hold ---
    # D0: equally-spaced cloud converse counterexample
    d0 = []
    for q in (4, 8, 16, 32):
        J, band = band_vs_J_cloud(q)
        d0.append({"q": q, "J_q": str(J), "unweighted_band": band, "band_eq_2q": band == 2 * q})
    # D1: old per-h depth reaches ~A^{3/4} sqrt|h|, not A^{3/2}
    d1 = []
    for A in (16 ** 4, 16 ** 8):
        for h in (1, 16, 100):
            reached = reached_frequency_old(A, h)
            d1.append({"A": A, "h": h, "reached_over_A32": f"{reached / A ** 1.5:.3e}",
                       "reached_over_A34_sqrth": f"{reached / (A ** 0.75 * h ** 0.5):.3f}"})
    # D2: non-injectivity of the old per-h depth at A=16^8
    A2 = 16 ** 8
    d2 = {"A": A2,
          "h1_depth": depth_old(A2, 1), "h1_target": reached_frequency_old(A2, 1),
          "h16_depth": depth_old(A2, 16), "h16_target": reached_frequency_old(A2, 16),
          "collision": reached_frequency_old(A2, 1) == reached_frequency_old(A2, 16)}
    # D3: true accumulated error <= correct bound; and worst ratio (non-vacuity)
    d3_viol = 0
    d3_worst = 0.0
    for A in (40, 64, 128, 256):
        ph = source_epoch(A)
        for h in (1, 3):
            for j in (1, 2, 3):
                if 16 ** j * h > A * A:
                    continue
                t = float(acc_error_true(ph, h, j))
                b = acc_error_bound(A, h, j)
                if t > b:
                    d3_viol += 1
                d3_worst = max(d3_worst, t / b)
    # corrected barrier: common depth is injective, reaches <= A^{3/2}, error o(1) at band edge
    barrier = []
    for A in (64, 256, 1024):
        H = max(2, int(round((mp.log(A) / mp.log(16)) ** 2)))  # ~ q_A^2 scale
        j = common_depth(A, H)
        top = 16 ** j * H
        barrier.append({"A": A, "H_band": H, "common_depth_j": j,
                        "top_frequency_16j_H": top, "top_le_A32": top <= A ** 1.5,
                        "edge_acc_error_bound": f"{acc_error_bound(A, H, j):.3e}"})
    return {
        "instrument": "renorm_transport",
        "dps": DPS,
        "immutable_source": "r(n)=4/(8n-7)-2/(8n-4)-1/(8n-3)-1/(8n-2), U0=0, U_n=16U_{n-1}+r(n)",
        "claim": "RENORM-1: c_A(h)=c_A(16h)+eps, |eps|<=2/A+15*pi*|h|/(4A(8A-15))",
        "heldout_A": list(HELDOUT_A),
        "heldout_h": list(HELDOUT_H),
        "blind_source_max_abs_diff": mp.nstr(blind_max, 4),
        "rigorous_bound_violations": violations,
        "worst_residual_over_rigorous_bound": f"{worst_rig:.6f}",
        "worst_residual_over_asymptotic_bound": f"{worst_asy:.6f}",
        "rows": rows,
        "barrier_RENORM2": ("common-depth x16 transport is injective; band relocated to a "
                            "distinct high band <= A^{3/2} at equal cardinality, mass preserved "
                            "up to o(1); information-preserving, not a size bound"),
        "renorm2_corrected_barrier": barrier,
        "defect_regression": {
            "D0_band_vs_J_cloud": d0,
            "D1_old_depth_reaches_A34_not_A32": d1,
            "D2_old_depth_noninjective_collision": d2,
            "D3_acc_error_true_le_correct_bound": {
                "violations": d3_viol, "worst_true_over_bound": f"{d3_worst:.6f}"},
        },
        "pi_base16_normality": "OPEN",
        "signed_weyl_gate_S_N_h_eq_o_N": "OPEN",
        "status": "RENORM1_VERIFIED_ON_HELDOUT; RENORM2_BARRIER_CORRECTED; NO_NORMALITY_PROOF",
    }


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", type=Path, default=None,
                        help="regenerate and compare against a committed FINITE_RECEIPT.json")
    parser.add_argument("--write", type=Path, default=None,
                        help="write a fresh FINITE_RECEIPT.json")
    args = parser.parse_args(argv)
    receipt = build_receipt()
    render = json.dumps(receipt, indent=2, sort_keys=True)
    if receipt["rigorous_bound_violations"] != 0:
        print("RENORM-1 RIGOROUS BOUND VIOLATED", file=sys.stderr)
        return 1
    if receipt["defect_regression"]["D3_acc_error_true_le_correct_bound"]["violations"] != 0:
        print("RENORM-2 CORRECTED ACCUMULATED-ERROR BOUND VIOLATED", file=sys.stderr)
        return 1
    if args.write:
        args.write.write_text(render + "\n", encoding="utf-8")
        print(f"wrote {args.write}")
        return 0
    if args.verify:
        committed = args.verify.read_text(encoding="utf-8").strip()
        if committed != render.strip():
            print(f"STALE/MISMATCHED receipt: {args.verify}", file=sys.stderr)
            return 1
        print("RECEIPT VERIFIED (deterministic)")
        return 0
    print(render)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
