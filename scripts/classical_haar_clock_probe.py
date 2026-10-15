#!/usr/bin/env python3
"""Deterministic real-Haar finite-clock exact source receipt."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from observational_succ.classical_haar_clock import classical_haar_clock_probe

RECEIPT = ROOT / "research/2026-10-15/CLASSICAL_HAAR_CLOCK_RECEIPT.json"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    actual = classical_haar_clock_probe()
    if args.verify:
        if actual != json.loads(RECEIPT.read_text(encoding="utf-8")):
            raise SystemExit("HAAR CLOCK RECEIPT DRIFT")
        print("CLASSICAL_HAAR_CLOCK: exact receipt verified")
    else:
        print(json.dumps(actual, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
