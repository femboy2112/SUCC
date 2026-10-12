#!/usr/bin/env python3
"""Reproduce finite structure controls; entropy numbers are diagnostics."""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from observational_succ.entropy_transport import entropy_transport_probe


if __name__ == "__main__":
    print(json.dumps(entropy_transport_probe(), indent=2, sort_keys=True))
