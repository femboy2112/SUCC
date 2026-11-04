"""RENORM transport: the exact x16 Fourier renormalization of the original BBP source.

Add-only research instrument for the selected-current front. No pi digits, fitted
randomness, Galois average, or normality proof. The original four signed Mellin
terms and U_0 = 0 are immutable. Exponential-sum coefficients are measured at fixed
mpmath precision (an INSTRUMENT, calibrated on known cases) over exact rational phases.

RENORM-1 (proved; this instrument verifies it on held-out epochs):
    c_A(h) = c_A(16 h) + eps_A(h),        c_A(h) = A^{-1} sum_{n=A}^{2A-1} e(h U_n),
    |eps_A(h)| <= 2/A + 15 pi |h| / (4 A (8A - 15))          (rigorous, A >= 2)
               ~= 2/A + (15 pi / 32) |h| / A^2               (asymptotic).

RENORM-2 (barrier corollary): h -> 16 h is injective on frequencies, so iterating
RENORM-1 transports the low band {|h| <= H} bijectively onto {16^j <= |.| <= 16^j H}
plus an O(j/A + 16^j|h|/A^2) error. Hence this single-frequency transport is
information-preserving and CANNOT, by itself, drive the SC-8 band second moment to
o(K_A); a genuine high-frequency equidistribution estimate (the OPEN input) is required.
This is an obstruction map, not progress on the estimate. pi base-16 normality is OPEN.
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
        "barrier_RENORM2": "x16 injective on frequencies; transport preserves band mass",
        "pi_base16_normality": "OPEN",
        "signed_weyl_gate_S_N_h_eq_o_N": "OPEN",
        "status": "RENORM1_VERIFIED_ON_HELDOUT; NO_NORMALITY_PROOF",
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
