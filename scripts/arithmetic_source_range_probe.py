#!/usr/bin/env python3
"""Source range audit: exact controls by default; optional serial experiment.

Without --output, print the receipt and write no files. --numerical adds
fresh-grid actual-source residual and fractional-moment diagnostics.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
from fractions import Fraction
from hashlib import sha256
import io
import json
import os
from pathlib import Path
import platform
import shlex
import subprocess
import sys
from time import monotonic
import unittest

sys.dont_write_bytecode = True
for key in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[key] = "1"
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from observational_succ import arithmetic_source_range as R

OWN = ("observational_succ/arithmetic_source_range.py",
       "tests/test_arithmetic_source_range.py",
       "scripts/arithmetic_source_range_probe.py",
       "research/2026-10-16/FRACTIONAL_SOURCE_RANGE_AUDIT.md")


def hashes():
    return {p: sha256((ROOT/p).read_bytes()).hexdigest() for p in OWN if (ROOT/p).exists()}


def git(*args):
    p = subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True)
    return {"exit_code": p.returncode, "stdout": p.stdout.strip(), "stderr": p.stderr.strip()}


def encode(value):
    if isinstance(value, Fraction):
        return str(value)
    raise TypeError(type(value).__name__)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--numerical", action="store_true")
    parser.add_argument("--rank", type=int, default=24)
    parser.add_argument("--fit-nodes", type=int, default=24)
    parser.add_argument("--holdout-nodes", type=int, default=48)
    args = parser.parse_args()
    start = monotonic()
    snapshot, before = R.source_snapshot(), hashes()
    receipt = {"schema": "ARITHMETIC_SOURCE_RANGE_V1", "status": "RUNNING",
               "time_utc": datetime.now(timezone.utc).isoformat(),
               "command": shlex.join([sys.executable, *sys.argv]), "cwd": str(Path.cwd()),
               "python": platform.python_version(), "git_head": git("rev-parse", "HEAD"),
               "git_branch": git("branch", "--show-current"),
               "origin_blob": git("rev-parse", R.SOURCE_COMMIT+":observational_succ/source_weil_hierarchy.py"),
               "source": snapshot, "source_git_blob": snapshot["source_git_blob"],
               "own_sha256": before, "claims": R.claim_boundaries(),
               "evidence": {}, "failures": [], "full_suite_run": False,
               "git_writes_performed": False, "nontrivial_zero_coordinates_used": False}
    try:
        evidence = receipt["evidence"]
        evidence["multiplier_enclosures"] = [R.gamma_multiplier_enclosure(xi, 64)
                                               for xi in (0, 1, 4, 16, 64, 256)]
        evidence["logarithmic_lower_bounds"] = [R.logarithmic_band_lower(j) for j in (1, 4, 16, 64, 256)]
        evidence["primitive_moment_controls"] = [R.primitive_control(n) for n in (5, 6, 9)]
        evidence["gamma_primitive_identity"] = [R.gamma_primitive_identity(n, j)
                                                for n in (5, 6) for j in (0, 1, 7)]
        evidence["retained_nonzero_boundary_mutant"] = R.gamma_primitive_identity(boundary_mutant=True)
        stream = io.StringIO()
        suite = unittest.defaultTestLoader.discover(str(ROOT/"tests"), pattern="test_arithmetic_source_range.py")
        result = unittest.TextTestRunner(stream=stream, verbosity=2).run(suite)
        evidence["focused_tests"] = {"count": result.testsRun, "success": result.wasSuccessful(),
                                      "failures": len(result.failures), "errors": len(result.errors),
                                      "skips": len(result.skipped), "log": stream.getvalue()}
        if not result.wasSuccessful():
            receipt["failures"].append("focused tests failed")
        if args.numerical:
            fit = R.numerical_source_grid(args.rank, args.fit_nodes)
            hold = R.numerical_source_grid(args.rank, args.holdout_nodes)
            ranks = sorted({n for n in (8, 12, 16, args.rank) if n <= args.rank})
            evidence["numerical"] = R.numerical_range_discriminator(fit, hold, ranks)
            # Predeclared instrument checks. Failure is retained, not masked
            # by replacing the operator by its positive part or changing gates.
            gates = {
                "fit_and_holdout_distinct": args.fit_nodes != args.holdout_nodes,
                "orthogonality_below_1e-10": max(fit["basis_orthogonality_defect"], hold["basis_orthogonality_defect"]) < 1e-10,
                "holdout_G_symmetry_below_2e-7": hold["G_symmetry_defect"] < 2e-7,
                "holdout_T_skew_below_2e-5": hold["T_skew_defect"] < 2e-5,
                "positive_high_spectrum_without_clipping": all(r["positive_eigenvalues_not_clipped"] for r in evidence["numerical"]["runs"]),
            }
            evidence["numerical_instrument_gates"] = gates
            receipt["failures"].extend(k for k, value in gates.items() if not value)
    except Exception as exc:
        import traceback
        receipt["failures"].append(type(exc).__name__+": "+str(exc))
        receipt["exception_traceback"] = traceback.format_exc()
    receipt["source_bytes_unchanged"] = snapshot == R.source_snapshot()
    receipt["own_bytes_unchanged"] = before == hashes()
    if not receipt["source_bytes_unchanged"] or not receipt["own_bytes_unchanged"]:
        receipt["failures"].append("input bytes changed during probe")
    receipt["elapsed_seconds"] = monotonic()-start
    receipt["status"] = "PASS_SCOPED_CHECKS" if not receipt["failures"] else "FAIL"
    receipt["exit_code"] = int(bool(receipt["failures"]))
    text = json.dumps(receipt, indent=2, default=encode, allow_nan=False)+"\n"
    if args.output is None:
        print(text, end="")
    else:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text)
        print(json.dumps({"status": receipt["status"], "output": str(args.output),
                          "elapsed_seconds": receipt["elapsed_seconds"],
                          "failures": receipt["failures"], "source_git_blob": R.SOURCE_BLOB}))
    return receipt["exit_code"]


if __name__ == "__main__":
    raise SystemExit(main())
