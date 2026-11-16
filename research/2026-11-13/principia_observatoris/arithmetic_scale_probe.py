"""Exact PA-05 finite controls; universal authority is the manuscript proof.

Run from any directory:
  python research/2026-11-13/principia_observatoris/arithmetic_scale_probe.py

The closed Rodrigues/beta formula is independent of the native LDL computation.
No floating-point comparison, source alteration, or normality estimate is used.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
import json
from math import comb, factorial, prod
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))

from observational_succ.principia_observatoris import bbp_hankel_ldl


def beta_monic_norm(start: int, degree: int) -> Fraction:
    """Closed beta-weight monic norm, with alpha = start - 7/8."""
    if type(start) is not int or start < 1:
        raise ValueError("A positive integer starting index is required")
    if type(degree) is not int or degree < 1:
        raise ValueError("A positive integer degree is required")
    alpha = Fraction(8 * start - 7, 8)
    return Fraction(factorial(degree) * factorial(degree + 1)) / (
        (2 * degree + alpha + 1)
        * (degree + alpha)
        * prod((degree + alpha + j) ** 2 for j in range(1, degree + 1))
    )


def in_strict_bounds(error: Fraction, norm: Fraction) -> bool:
    return Fraction(15, 64) * norm < error < Fraction(1, 2) * norm


def rodrigues_check(start: int, degree: int) -> tuple[int, Fraction]:
    """Expand the derivative polynomial and integrate its coefficients exactly.

    This does not use the closed norm formula or native matrix factorization.
    """
    alpha = Fraction(8 * start - 7, 8)
    derivative = [
        (-1) ** j * comb(degree + 1, j)
        * prod(degree + alpha - 1 + j - k for k in range(degree))
        for j in range(degree + 2)
    ]
    # F^(d)/u^(alpha-1) is divisible by 1-u.
    if sum(derivative) != 0:
        raise AssertionError("Rodrigues polynomial failed division at u=1")
    quotient = [sum(derivative[:j + 1]) for j in range(degree + 1)]
    leading = quotient[-1]
    expected_leading = (-1) ** degree * prod(
        degree + alpha + j for j in range(1, degree + 1)
    )
    if leading != expected_leading:
        raise AssertionError("Rodrigues leading coefficient disagrees")
    coefficients = [x / leading for x in quotient]

    def beta_moment(k: int) -> Fraction:
        return 1 / ((alpha + k) * (alpha + k + 1))

    for k in range(degree):
        inner = sum(c * beta_moment(j + k) for j, c in enumerate(coefficients))
        if inner != 0:
            raise AssertionError(("Failed exact orthogonality", start, degree, k))
    direct_norm = sum(
        x * y * beta_moment(i + j)
        for i, x in enumerate(coefficients)
        for j, y in enumerate(coefficients)
    )
    return degree, direct_norm


def run() -> dict:
    rows = []
    rodrigues_cases = orthogonality_checks = 0
    rejected_mutations = {
        "zero_residual": 0,
        "swapped_lower_bound": 0,
        "swapped_upper_bound": 0,
        "omitted_degree_plus_one_factor": 0,
    }
    for start in (1, 2, 7, 31, 127, 509):
        for degree in range(1, 9):
            error = bbp_hankel_ldl(start, degree + 1)["diagonal"][-1]
            norm = beta_monic_norm(start, degree)
            if degree <= 5:
                count, direct_norm = rodrigues_check(start, degree)
                if direct_norm != norm:
                    raise AssertionError("Direct polynomial norm disagrees with formula")
                rodrigues_cases += 1
                orthogonality_checks += count
            if not in_strict_bounds(error, norm):
                raise AssertionError(("PA-05 failure", start, degree, error, norm))
            if in_strict_bounds(Fraction(0), norm):
                raise AssertionError("The checker accepted a zero-residual mutant")
            rejected_mutations["zero_residual"] += 1
            # The two true bounds are not interchangeable.
            if Fraction(1, 2) * norm < error:
                raise AssertionError("The false larger lower bound was accepted")
            rejected_mutations["swapped_lower_bound"] += 1
            if error < Fraction(15, 64) * norm:
                raise AssertionError("The false smaller upper bound was accepted")
            rejected_mutations["swapped_upper_bound"] += 1
            if degree >= 2:
                # Omitting this factor shrinks the upper bound below 15h/64.
                if in_strict_bounds(error, norm / (degree + 1)):
                    raise AssertionError("A factorial-coefficient mutant was accepted")
                rejected_mutations["omitted_degree_plus_one_factor"] += 1
            rows.append({
                "start": start,
                "degree": degree,
                "compulsory_error": str(error),
                "beta_monic_norm": str(norm),
                "error_to_norm_ratio": str(error / norm),
                "strict_lower": str(Fraction(15, 64) * norm),
                "strict_upper": str(Fraction(1, 2) * norm),
                "passes": True,
            })
    native = ROOT / "observational_succ/principia_observatoris.py"
    return {
        "claim": "PA-05",
        "authority": "finite exact arithmetic check; all-parameter theorem is paper proof",
        "status": "PASS",
        "grid": {"start": [1, 2, 7, 31, 127, 509], "degree": list(range(1, 9))},
        "cases": len(rows),
        "independent_rodrigues_cases": rodrigues_cases,
        "independent_orthogonality_checks": orthogonality_checks,
        "rejected_mutations": rejected_mutations,
        "source_and_probe_sha256": {
            str(native.relative_to(ROOT)): hashlib.sha256(native.read_bytes()).hexdigest(),
            str(Path(__file__).resolve().relative_to(ROOT)):
                hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        },
        "source_contract": "Original four-pole r(n), n>=1; no modified forcing",
        "limits": [
            "No empirical physical measurements",
            "No Lean or other formal-kernel verification",
            "No source-selected Fourier estimate or normality conclusion",
            "Same-family implementation triangulation, not external peer review",
        ],
        "rows": rows,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = run()
    if args.output is not None:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
        print(json.dumps({
            "status": result["status"],
            "cases": result["cases"],
            "independent_rodrigues_cases": result["independent_rodrigues_cases"],
            "independent_orthogonality_checks": result["independent_orthogonality_checks"],
            "rejected_mutations": result["rejected_mutations"],
            "output": str(args.output),
        }, sort_keys=True))
    else:
        print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
