#!/usr/bin/env python3
"""Reproduce finite source-bridge checks; never certify RH/ABC or normality."""
from __future__ import annotations

import argparse
from dataclasses import asdict
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import platform
import subprocess
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

import sympy as sp

from observational_succ.duck_source_bridge import (
    conditional_fourier_budget, prime_power_terms,
    residual_square_consequence, thue_morse_prefix_interval,
)


def encode(value):
    if isinstance(value, Fraction):
        return f"{value.numerator}/{value.denominator}"
    raise TypeError(type(value).__name__)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, help="also save the JSON receipt")
    args = parser.parse_args()

    suite = unittest.defaultTestLoader.discover(
        str(ROOT / "tests"), pattern="test_duck_source_bridge.py"
    )
    result = unittest.TextTestRunner(verbosity=1).run(suite)
    if not result.wasSuccessful():
        return 1

    x = sp.Symbol("x", positive=True)
    integral_tail = x**(-sp.Rational(3, 2)) * (
        sp.Rational(4, 3) * sp.log(x) + sp.Rational(14, 9)
    )
    derivative_residual = sp.simplify(
        sp.diff(integral_tail, x) + x**(-sp.Rational(5, 2)) * (2*sp.log(x)+1)
    )
    if derivative_residual != 0:
        raise AssertionError("independent symbolic tail derivative failed")

    files = [
        "observational_succ/duck_source_bridge.py",
        "tests/test_duck_source_bridge.py",
        "scripts/duck_source_bridge_probe.py",
        "research/2026-10-21/DUCK_RH_ABC_GAMMA_CONTINGENCY.md",
    ]
    record = {
        "schema": "duck-source-bridge-finite-receipt-v1",
        "status": "EXACT_FINITE_CHECKS_PAPER_ANALYSIS_NOT_LEAN_VERIFIED",
        "does_not_certify": ["RH", "universal ABC", "pi normality", "Fourier cancellation"],
        "git_parent_at_execution": subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=ROOT, text=True
        ).strip(),
        "file_sha256": {name: hashlib.sha256((ROOT/name).read_bytes()).hexdigest()
                        for name in files},
        "python": platform.python_version(),
        "sympy": sp.__version__,
        "focused_tests": {"run": result.testsRun, "failures": len(result.failures),
                          "errors": len(result.errors), "skipped": len(result.skipped)},
        "independent_symbolic_integral_derivative_residual": str(derivative_residual),
        "prime_power_atoms_through_6": prime_power_terms(6),
        "conditional_rh_budget": asdict(conditional_fourier_budget(16**8, 8, 3)),
        "exact_abc_normalized_example": asdict(
            residual_square_consequence(22, 7, 314, 10, 2, 1)
        ),
        "thue_morse_base16_prefix_interval_32": thue_morse_prefix_interval(16, 32),
        "external_premises": {
            "RH_instance": "Lee--Nosal arXiv:2312.05628v4 Theorem 1.2; RH assumed",
            "ABC": "only a supplied finite exponent-two premise is checked by code",
            "irrationality_exponent_countermodel": "Bugeaud 2011 DOI:10.5802/aif.2666 imported",
        },
    }
    payload = json.dumps(record, indent=2, sort_keys=True, default=encode) + "\n"
    if args.output:
        args.output.write_text(payload)
    print(payload, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
