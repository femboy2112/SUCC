#!/usr/bin/env python3
"""Replay the predeclared synthetic RC calibration and held-out observation."""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from observational_succ.reality_pin_selection import synthetic_rc_receipt

if __name__ == "__main__":
    print(json.dumps(synthetic_rc_receipt(), indent=2, sort_keys=True))
