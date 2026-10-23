#!/usr/bin/env python3
"""Reproduce exact geometry/dimension witnesses and focused validation.

The JSON output is an unauthenticated reproducibility record, not proof
authority. It hashes the exact sources tested; its Git HEAD may predate a
commit containing those sources. No network or formal prover is invoked.
"""
import argparse
from dataclasses import asdict
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import platform
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

import sympy
from observational_succ.viii_exterior_geometry import section_lattice, section_cell_budget
from observational_succ.viii_simplex_asymptotics import (
    binomial_log_correction, binomial_entropy_enclosure, residue_log_correction,
)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    sources = [
        "observational_succ/viii_exterior_geometry.py",
        "observational_succ/viii_simplex_asymptotics.py",
        "tests/test_viii_exterior_geometry.py",
        "tests/test_viii_simplex_asymptotics.py",
        "research/2026-10-21/VIII_SECTION_LATTICES_AND_SIMPLEX_LAWS.md",
        "scripts/viii_geometry_probe.py",
    ]
    tests = []
    for pattern in ("test_viii_exterior_geometry.py", "test_viii_simplex_asymptotics.py"):
        command = [sys.executable, "-m", "unittest", "discover", "-s", "tests", "-p", pattern, "-v"]
        result = subprocess.run(command, cwd=ROOT, text=True, capture_output=True)
        transcript = result.stdout + result.stderr
        match = re.search(r"Ran (\d+) tests?", transcript)
        tests.append({"command": command, "exit_code": result.returncode,
                      "test_count": int(match.group(1)) if match else None,
                      "transcript": transcript})
    M = 17
    section = section_lattice(((1, 0), (M - 1, -1), (0, 1)), (1, 1, 1), M)
    center = (Fraction(1, 2 * M), Fraction(M - 1, 4 * M), Fraction(M - 1, 4 * M))
    record = {
        "schema": "viii-geometry-reproduction-v1",
        "authority": "unauthenticated exact-computation record; paper proofs separate; no Lean claim",
        "git_head_at_run": subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip(),
        "python": platform.python_version(), "sympy": sympy.__version__,
        "source_sha256": {name: hashlib.sha256((ROOT / name).read_bytes()).hexdigest() for name in sources},
        "tests": tests,
        "positive_section_counterexample": {
            "M": M, "section": asdict(section), "center": center,
            "beta": section_cell_budget(section.lattice_basis, center),
            "cutoff": M, "primitive_point_count": M - 2,
            "counting_coefficient": Fraction(M - 1, 2 * M ** 2),
        },
        "log_correction": asdict(binomial_log_correction(1000, 100, 2)),
        "entropy_linear_dimension": asdict(binomial_entropy_enclosure(60, 30)),
        "empty_dimension": asdict(binomial_entropy_enclosure(60, 61)),
        "residue_shift_control": {
            "W": 2, "X": 200, "m": 10,
            "all_positive_representatives_one": asdict(residue_log_correction(2, 200, (1,) * 10)),
            "all_positive_representatives_two": asdict(residue_log_correction(2, 200, (0,) * 10)),
        },
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(record, indent=2, default=str) + "\n")
    print(json.dumps({"output": str(args.output), "tests": [
        {key: row[key] for key in ("test_count", "exit_code")} for row in tests]}))
    return int(any(row["exit_code"] for row in tests))


if __name__ == "__main__":
    raise SystemExit(main())
