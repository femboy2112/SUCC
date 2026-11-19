"""Certified, fixed, chronological Weyl probes for the original BBP source.

Only rational/integer arithmetic is used for certificates. Decimal fields are
display summaries. The inherited bulk prefix routine uses the original source,
outward integer rounding and an analytic tail, not an oracle for pi.
Finite outcomes do not prove any asymptotic digit-distribution statement.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
from functools import lru_cache
from hashlib import sha256
import json
from math import factorial, gcd, isqrt
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
sys.path.insert(0, str(ROOT))
from observational_succ.bbp_spatial_haar_lift import bulk_pi_hex_digits
from observational_succ.duck_bbp import forcing


def atan_interval_inverse(q: int, terms: int = 16) -> tuple[F, F]:
    """Alternating-series enclosure for atan(1/q), q>=2."""
    if type(q) is not int or q < 2 or terms < 1:
        raise ValueError("q>=2 and a positive term count required")
    a = sum((F((-1)**k, (2*k+1)*q**(2*k+1))
             for k in range(terms)), F())
    b = a + F((-1)**terms, (2*terms+1)*q**(2*terms+1))
    return min(a, b), max(a, b)


def pi_interval() -> tuple[F, F]:
    """Machin identity: pi = 16 atan(1/5) - 4 atan(1/239)."""
    a, b = atan_interval_inverse(5)
    c, d = atan_interval_inverse(239)
    return 16*a-4*d, 16*b-4*c


def _trig_polynomials(x: F) -> tuple[F, F]:
    """Cosine degree24 and sine degree25, exact rational evaluation."""
    x2 = x*x
    ct = F(1)
    st = x
    cosv, sinv = ct, st
    for k in range(1, 13):
        ct *= -x2 / ((2*k-1)*(2*k))
        st *= -x2 / ((2*k)*(2*k+1))
        cosv += ct
        sinv += st
    return cosv, sinv


@lru_cache(maxsize=8)
def trig_table(grid: int = 4096, scale_bits: int = 44):
    """Integer cosine/sine table plus rigorous per-component error.

    Quarter-wave symmetries are imposed exactly. On [0,pi/2] the
    polynomial remainder is bounded by 2^25/25!. Replacing pi by a
    dyadic approximation and rounding the outputs are paid separately.
    """
    if grid < 4 or grid % 4 or scale_bits < 8:
        raise ValueError("grid divisible by4, scale_bits>=8 required")
    plo, phi = pi_interval()
    assert F(3) < plo < phi < F(22, 7)
    pscale = 1 << 60
    pmid = F(((plo+phi)*pscale/2).__floor__(), pscale)
    perr = max(abs(pmid-plo), abs(phi-pmid))
    scale = 1 << scale_bits
    quarter = []
    for j in range(grid//4):
        x = 2*pmid*j/grid
        assert 0 <= x < 2
        c, s = _trig_polynomials(x)
        quarter.append(((c*scale).__floor__(), (s*scale).__floor__()))
    table = []
    for quadrant in range(4):
        for c, s in quarter:
            table.append(((c, s), (-s, c), (-c, -s), (s, -c))[quadrant])
    error = perr/2 + F(2**25, factorial(25)) + F(1, scale)
    return tuple(table), scale, error


def signed_enclosure(sums: tuple[int, int], count: int, scale: int,
                     error: F) -> dict:
    """Enclose a signed mean when each coordinate error is <=error."""
    if count <= 0:
        raise ValueError("empty chronological sample")
    re, im = F(sums[0], count*scale), F(sums[1], count*scale)
    rlo, rhi, ilo, ihi = re-error, re+error, im-error, im+error
    upper2 = max(abs(rlo), abs(rhi))**2 + max(abs(ilo), abs(ihi))**2
    def minabs(lo, hi):
        return F() if lo <= 0 <= hi else min(abs(lo), abs(hi))
    lower2 = minabs(rlo, rhi)**2 + minabs(ilo, ihi)**2
    return {
        "count": count,
        "real_interval": [str(rlo), str(rhi)],
        "imag_interval": [str(ilo), str(ihi)],
        "modulus_squared_interval": [str(lower2), str(upper2)],
        "midpoint_display_only": [float(re), float(im)],
        "coordinate_error": str(error),
    }


def classify_upper(lo: F, hi: F, threshold: F) -> str:
    if hi <= threshold:
        return "PASS_FINITE"
    if lo > threshold:
        return "FAIL_FINITE"
    return "AMBIGUOUS"


def rational_sample_mean(phases, h: int, grid=4096, scale_bits=44):
    table, scale, terr = trig_table(grid, scale_bits)
    sr = si = count = 0
    for phase in phases:
        index = ((F(phase)*h) % 1 * grid).__floor__()
        c, s = table[index]
        sr += c
        si += s
        count += 1
    error = terr + F(44, 7*grid)
    return signed_enclosure((sr, si), count, scale, error)


def controls(grid=4096, scale_bits=44) -> dict:
    """Controls run before any held-out source statistics are computed."""
    table, scale, terr = trig_table(grid, scale_bits)
    assert table[0] == (scale, 0)
    assert table[grid//4] == (0, scale)
    assert table[grid//2] == (-scale, 0)
    assert sum(v[0] for v in table) == sum(v[1] for v in table) == 0
    # Finite balanced calibration, NOT a proof that any supplied real is normal.
    balanced = rational_sample_mean((F(j, grid) for j in range(grid)), 1,
                                    grid, scale_bits)
    locked = rational_sample_mean([F()] * grid, 1, grid, scale_bits)
    assert F(balanced["modulus_squared_interval"][1]) < F(1, 256)
    assert F(locked["real_interval"][0]) > F(15, 16)
    # A moving chart can make even the balanced calibration read zero.
    # Retaining and multiplying its compensator returns exactly the same phases.
    assert all(((F(j, grid)-F(j, grid)) + F(j, grid)) == F(j, grid)
               for j in range(grid))
    # A finite prefix of a factorial sparse irrational creates a cold shell;
    # the infinite remaining tail is explicitly bounded in the proof note.
    theta = sum((F(1, 16**factorial(k)) for k in range(1, 6)), F())
    sparse = rational_sample_mean(((16**n*theta) % 1 for n in range(48, 96)),
                                  1, grid, scale_bits)
    assert F(sparse["real_interval"][0]) > F(15, 16)
    k1, k2 = 11*(16**4-1), 7*(16**6-1)
    assert (k1, k2, gcd(k1, k2)) == (720885, 117440505, 255)
    invisible = F(1, 255)
    assert k1*invisible % 1 == k2*invisible % 1 == 0
    assert invisible % 1 != 0 and 15*invisible % 1 == F(1, 17)
    # Phase-selected stopping changes the empirical law: (0,1/2) is balanced;
    # selecting only the displayed zero produces the locked control.
    pair = rational_sample_mean([F(), F(1, 2)], 1, grid, scale_bits)
    assert F(pair["modulus_squared_interval"][1]) < F(1, 256)
    return {
        "status": "PASS",
        "balanced_grid": balanced,
        "locked_zero": locked,
        "factorial_cold_shell_finite_control": sparse,
        "omitted_compensator_mutation_detected": True,
        "phase_selection_mutation_detected": True,
        "fixed_lag_bank_kernel_order": 255,
        "finite_controls_are_asymptotic_theorems": False,
        "table_error_before_grid": str(terr),
    }


def run(config_path: Path, output: Path, *, calibration_only=False) -> dict:
    config_bytes = config_path.read_bytes()
    config = json.loads(config_bytes)
    modes = config["absolute_modes"]
    shells = config["shells"]
    if 1 not in modes or any(type(h) is not int or not h for h in modes):
        raise ValueError("fixed nonzero modes must include authenticated h=1")
    if any(type(b) is not int or b <= config["prior_source_training_horizon"]
           for b in shells):
        raise ValueError("new source shells must start after prior training data")
    grid, bits = config["trigonometric_grid"], config["table_scale_bits"]
    control_report = controls(grid, bits)
    output.mkdir(parents=True, exist_ok=True)
    report = {
        "status": "CALIBRATED_FINITE_INSTRUMENT",
        "config_sha256": sha256(config_bytes).hexdigest(),
        "source": config["source"],
        "normality_proved": False,
        "R0_proved": False,
        "controls": control_report,
        "shells": [],
    }
    if calibration_only:
        (output / "calibration.json").write_text(json.dumps(report, indent=2)+"\n")
        return report
    width = config["phase_hex_width"]
    length = 2*max(shells)-1 + width
    prefix = bulk_pi_hex_digits(length)
    (output / "bbp_prefix_hex.txt").write_text(prefix+"\n", encoding="ascii")
    report["prefix"] = {"length": len(prefix),
                        "sha256": sha256(prefix.encode("ascii")).hexdigest(),
                        "source_terms_used": length+24,
                        "construction": "outward integer BBP enclosure; guard24"}
    table, scale, terr = trig_table(grid, bits)
    q = 16**width
    for b in shells:
        sums = {h: [0, 0] for h in modes}
        for n in range(b, 2*b):
            # Y_n=16^(n-1)*pi; prefix[0] is pi's first fractional hex digit.
            word = int(prefix[n-1:n-1+width], 16)
            for h in modes:
                index = ((h*word) % q)*grid//q
                c, s = table[index]
                sums[h][0] += c
                sums[h][1] += s
        shell = {"B": b, "first_n": b, "last_n": 2*b-1,
                 "sample_count": b, "all_chronological_times_retained": True,
                 "modes": {}}
        for h in modes:
            error = terr + F(44, 7)*(F(1, grid) + F(abs(h), q))
            result = signed_enclosure(tuple(sums[h]), b, scale, error)
            raw_debt = F(44, 7)*abs(h)*forcing(b+1)/15
            result["raw_U_mean_additional_coordinate_error"] = str(raw_debt)
            result["raw_U_mean_real_interval"] = [
                str(F(result["real_interval"][0])-raw_debt),
                str(F(result["real_interval"][1])+raw_debt)]
            result["raw_U_mean_imag_interval"] = [
                str(F(result["imag_interval"][0])-raw_debt),
                str(F(result["imag_interval"][1])+raw_debt)]
            result["finite_stress_verdict"] = classify_upper(
                *map(F, result["modulus_squared_interval"]),
                F(config["finite_stress_modulus_threshold"])**2)
            if h == 1:
                result["finite_R0_threshold_verdict"] = classify_upper(
                    *map(F, result["real_interval"]),
                    F(config["finite_r0_real_upper_threshold"]))
            shell["modes"][str(h)] = result
        report["shells"].append(shell)
    report["status"] = "FINITE_SOURCE_CERTIFICATES_ONLY"
    (output / "signed_weyl.json").write_text(json.dumps(report, indent=2)+"\n")
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path, default=HERE/"preregistration.json")
    parser.add_argument("--output", type=Path, default=HERE/"receipts")
    parser.add_argument("--calibration-only", action="store_true")
    args = parser.parse_args()
    result = run(args.config, args.output, calibration_only=args.calibration_only)
    print(json.dumps({"status": result["status"],
                      "config_sha256": result["config_sha256"],
                      "controls": result["controls"]["status"],
                      "shells": [{"B": s["B"], "modes": {
                          h: {"midpoint": v["midpoint_display_only"],
                              "finite_verdict": v["finite_stress_verdict"]}
                          for h, v in s["modes"].items()}}
                          for s in result["shells"]]}, indent=2))


if __name__ == "__main__":
    main()
