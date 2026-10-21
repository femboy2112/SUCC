#!/usr/bin/env python3
"""Finite exact receipt for the analytic dossier; never a normality verdict."""

import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from observational_succ.duck_bbp_fourier import (  # noqa: E402
    BBP_POLES, PoleTerm, arc_discrepancy_transport_budget, bbp_force,
    bbp_force_positive_form, bbp_shadow_budget, bbp_shadow_sum_budget,
    forced_orbit, fourier_sum_transport_budget, leading_matched_impostor,
    prefix_impostor, rational_coboundary, solve_rational_coboundary,
    weighted_pole_invariants,
)


def git(*arguments):
    return subprocess.check_output(["git", *arguments], cwd=ROOT, text=True).strip()


def receipt():
    source_paths = [
        "observational_succ/duck_bbp_fourier.py",
        "tests/test_duck_bbp_fourier.py",
        "scripts/duck_bbp_fourier_probe.py",
        "research/2026-10-21/DUCK_ANALYTIC_MOONSHOT.md",
    ]
    run = subprocess.run(
        [sys.executable, "-m", "unittest", "discover", "-s", "tests",
         "-p", "test_duck_bbp_fourier.py", "-v"],
        cwd=ROOT, text=True, capture_output=True, check=False,
    )
    prefixes = []
    for length in [0, 1, 3, 8, 12]:
        fake = prefix_impostor(bbp_force(n) for n in range(1, length+1))
        matches = all(fake.force(n) == bbp_force(n) for n in range(1, length+1))
        if not matches:
            raise ArithmeticError("finite-prefix counterfeit failed exact replay")
        prefixes.append({
            "length": length, "exact_prefix_match": matches,
            "denominator_power": fake.denominator_power,
            "newton_coefficients": [str(value) for value in fake.differences],
            "fresh_index": length+7,
            "fresh_correction": str(fake.correction(length+7)),
            "global_claim_status": "paper proof of rational shadow, not normality census",
        })
    fake_orbit = forced_orbit(leading_matched_impostor, 16, 12)
    correction = (PoleTerm(Fraction(-1), 2, Fraction(1, 64)),)
    forcing = rational_coboundary(correction, 16)
    if solve_rational_coboundary(forcing, 16) != correction:
        raise ArithmeticError("positive control failed exact certificate replay")
    if solve_rational_coboundary(BBP_POLES, 16) is not None:
        raise ArithmeticError("BBP negative control falsely accepted")
    return {
        "schema": "succ.duck_bbp_fourier.finite_probe.v1",
        "authority": "untrusted reproducible Python receipt, no formal kernel authority",
        "theorem_boundary": "transport differences and rational finite algebra; pi normality unproved",
        "git_head": git("rev-parse", "HEAD"),
        "git_branch": git("branch", "--show-current"),
        "git_working_tree_status": git("status", "--short"),
        "python_version": sys.version.split()[0],
        "source_sha256": {
            path: hashlib.sha256((ROOT/path).read_bytes()).hexdigest() for path in source_paths
        },
        "unit_tests": {
            "command": "python -m unittest discover -s tests -p test_duck_bbp_fourier.py -v",
            "returncode": run.returncode,
            "stdout": run.stdout,
            "stderr": run.stderr,
        },
        "source_positive_decomposition": [
            {"n": n, "four_fraction": str(bbp_force(n)),
             "positive_form": str(bbp_force_positive_form(n)),
             "tail_upper": str(bbp_shadow_budget(n))}
            for n in [1, 2, 17, 1000]
        ],
        "transport_budgets": [
            {"start": start, "length": length, "h": h,
             "sum_shadow_upper": str(bbp_shadow_sum_budget(start, length)),
             "fourier_difference_upper": str(fourier_sum_transport_budget(h, start, length))}
            for start, length, h in [(1, 0, 1), (1, 100, 1), (1000, 10, -7), (1, 10000, 100)]
        ],
        "arc_discrepancy_difference_budgets": [
            {"length": length, "upper": str(arc_discrepancy_transport_budget(length)[0]),
             "discarded_prefix": arc_discrepancy_transport_budget(length)[1]}
            for length in [1, 8, 64, 512, 4096]
        ],
        "actual_bbp_pole_obstruction": [
            {"pole_class": str(pole_class), "order": order, "invariant": str(value)}
            for (pole_class, order), value in sorted(weighted_pole_invariants(BBP_POLES, 16).items())
        ],
        "rational_coboundary_positive_control": {
            "correction": "q(z)=1/[64(z+1)^2]",
            "replay_passed": True,
            "orbit_at_12": str(fake_orbit[12]),
            "distance_from_zero_at_12": str(1-fake_orbit[12]),
        },
        "arbitrary_prefix_counterfeits": prefixes,
        "formal_verification": "not performed by this lane",
        "full_suite": "coordinator responsibility; not run by this probe",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = receipt()
    output = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(output)
        print(f"Saved finite receipt: {args.output}")
    else:
        print(output, end="")
    return int(result["unit_tests"]["returncode"] != 0)


if __name__ == "__main__":
    raise SystemExit(main())
