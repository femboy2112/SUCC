#!/usr/bin/env python3
"""Exact reproducible classical SUCC receipt; independent of RH zero data."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from observational_succ.classical_unit_origin import classical_unit_origin_probe

RECEIPT = ROOT / "research/2026-10-15/CLASSICAL_UNIT_ORIGIN_RECEIPT.json"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true", help="Compare fresh calculation with pinned receipt")
    options = parser.parse_args()
    actual = classical_unit_origin_probe()
    if options.verify:
        expected = json.loads(RECEIPT.read_text(encoding="utf-8"))
        if actual != expected:
            raise SystemExit("Classical source/receipt mismatch")
        print("CLASSICAL_UNIT_ORIGIN: exact receipt verified")
    else:
        print(json.dumps(actual, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
