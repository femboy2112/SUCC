#!/usr/bin/env python3
"""Reproduce Swarm A's exact finite receipt; --verify also checks source hashes."""
from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from observational_succ.profinite_hilbert import profinite_hilbert_probe

RECEIPT = ROOT / "research/2026-10-15/PROFINITE_HILBERT_RECEIPT.json"
SOURCES = (
    "AGENTS.md", "docs/METHOD.md", "provenance/IMPORT_MANIFEST.json",
    "observational_succ/classical_haar_clock.py",
    "observational_succ/classical_unit_origin.py",
    "observational_succ/dynamic_fourier_tower.py",
    "observational_succ/pontryagin_source_duality.py",
    "observational_succ/finite_quotient_retract.py",
    "observational_succ/finite_fourier_carrier.py",
    "observational_succ/profinite_hilbert.py",
    "tests/test_profinite_hilbert.py",
    "scripts/profinite_hilbert_probe.py",
    "research/2026-10-15/CLASSICAL_HAAR_TOWER_AND_NONUNIT_BRIDGE.md",
    "research/2026-10-15/PONTRYAGIN_SOURCE_DUALITY_AND_ADELES.md",
    "research/2026-10-15/PROFINITE_HILBERT_RECONSTRUCTION.md",
)


def _json_exact(value):
    if isinstance(value, Fraction):
        return str(value)
    raise TypeError(f"Unsupported receipt type: {type(value).__name__}")


def build_receipt() -> dict:
    evidence = profinite_hilbert_probe()
    evidence["source_sha256"] = {
        path: hashlib.sha256((ROOT / path).read_bytes()).hexdigest() for path in SOURCES
    }
    evidence["reproduction_command"] = "python scripts/profinite_hilbert_probe.py --verify"
    evidence["baseline_commit"] = "0f86ba2478a72bf90cf33a4ee192cb2265d992dd"
    evidence["primary_reference"] = {
        "title": "Terence Tao, 254A Notes 3, Haar measure and the Peter-Weyl theorem, Exercise 22",
        "url": "https://terrytao.wordpress.com/2011/09/27/254a-notes-3-haar-measure-and-the-peter-weyl-theorem/",
        "use": "Classical attribution; self-contained profinite proofs are in the local dossier",
    }
    return json.loads(json.dumps(evidence, default=_json_exact))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true", help="Compare exact evidence and source hashes")
    args = parser.parse_args()
    actual = build_receipt()
    if args.verify:
        expected = json.loads(RECEIPT.read_text(encoding="utf-8"))
        if expected != actual:
            changed = sorted(k for k in set(expected) | set(actual) if expected.get(k) != actual.get(k))
            raise SystemExit(f"PROFINITE_HILBERT_RECEIPT_DRIFT: {changed}")
        print("PROFINITE_HILBERT: exact finite receipt and source hashes verified")
    else:
        print(json.dumps(actual, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
