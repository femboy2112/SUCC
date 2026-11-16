"""Reproduce this dossier's exact tests and saved arithmetic receipts.

Run without arguments to check, or --write to deliberately regenerate the
verification receipt. This checks implementation consistency and finite
controls; universal mathematical claims require the accompanying proofs.
"""
from __future__ import annotations

import argparse
from hashlib import sha256
import json
from pathlib import Path
import sys
import unittest

import boundary_realization
import damped_filters
import goldbach_filters
import phase_filters
import pi_filters

HERE = Path(__file__).resolve().parent
RECEIPT = HERE / "VALIDATION_RESULTS.json"


def canonical(value):
    return json.dumps(value, indent=2, sort_keys=True, allow_nan=False) + "\n"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    suite = unittest.TestLoader().discover(str(HERE), pattern="test_*.py")
    result = unittest.TextTestRunner(verbosity=1).run(suite)
    if not result.wasSuccessful():
        return 1
    pi = json.loads((HERE / "PI_RESULTS.json").read_text())
    damped = json.loads((HERE / "DAMPED_RESULTS.json").read_text())
    if not pi_filters.verify_receipt(pi):
        raise ValueError("BBP receipt disagrees with its source reconstruction")
    if canonical(damped) != canonical(damped_filters.report()):
        raise ValueError("damped receipt disagrees with its source reconstruction")
    paths = sorted(HERE.glob("*.py")) + [HERE / "PI_RESULTS.json", HERE / "DAMPED_RESULTS.json"]
    wrapper = HERE.parents[2] / "tests" / "test_holographic_boundary_filters.py"
    files = {p.name: sha256(p.read_bytes()).hexdigest() for p in paths}
    files["tests/" + wrapper.name] = sha256(wrapper.read_bytes()).hexdigest()
    receipt = {
        "scope": "finite exact tests and reproducibility; no automatic proof authority",
        "base_commit": pi_filters.PARENT,
        "tests_run": result.testsRun,
        "failures": len(result.failures),
        "errors": len(result.errors),
        "skipped": len(result.skipped),
        "file_sha256": files,
        "ordered": boundary_realization.demo_receipt(),
        "phase": phase_filters.control_report(),
        "goldbach_moments": goldbach_filters.report(),
        "pi": {"certificates": len(pi["entries"]),
               "ambiguous_cells": sum(e["ambiguous"] for e in pi["entries"]),
               "receipt_reproduced": True, "uniform_R0_proved": False},
        "damped": {"certificates": len(damped["entries"]),
                   "positive": sum(e["positive"] for e in damped["entries"]),
                   "exact_count_recovered": sum(e["count_recovered"] for e in damped["entries"]),
                   "receipt_reproduced": True, "Goldbach_proved": False},
    }
    rendered = canonical(receipt)
    if args.write:
        RECEIPT.write_text(rendered)
    elif not RECEIPT.exists() or RECEIPT.read_text() != rendered:
        raise ValueError("saved verification receipt is stale; review before using --write")
    print(canonical({"status": "PASS", "tests_run": result.testsRun,
                     "pi_certificates": len(pi["entries"]),
                     "damped_certificates": len(damped["entries"]),
                     "receipt": RECEIPT.name}), end="")
    return 0


if __name__ == "__main__":
    sys.exit(main())
