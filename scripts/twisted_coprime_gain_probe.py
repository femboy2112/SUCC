#!/usr/bin/env python3
"""Fresh actual-source check of whether the stable-probe budget is useful."""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
from hashlib import sha256
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from observational_succ.pi_source_collision import prime_window
from observational_succ.twisted_source_energy import phase_boxes


def outward(low, high, digits=10):
    scale = 10**digits
    return {"scale": scale, "lower_integer": (low*scale).__floor__(),
            "upper_integer": (high*scale).__ceil__()}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    rows = []
    for prime in (193, 353, 577):
        window = prime_window(prime)
        intervals = []
        for gain in (2, 3):
            boxes = phase_boxes(window.complement, gain)
            low = 2-2*sum((box.real_high for box in boxes), Q())/window.length
            high = 2-2*sum((box.real_low for box in boxes), Q())/window.length
            intervals.append((low, high))
        total_lo, total_hi = (sum((x[i] for x in intervals), Q()) for i in (0, 1))
        rows.append({"prime": prime, "length": window.length, "frequency": 1,
                     "gain2_squared": outward(*intervals[0]),
                     "gain3_squared": outward(*intervals[1]),
                     "sum_squared_mismatches": outward(total_lo, total_hi),
                     "squared_coercivity_error": outward(Q(4, 3)*total_lo,
                                                          Q(4, 3)*total_hi),
                     "cancellation_bound_vacuous_certified": Q(4, 3)*total_lo > 1})
    paths = ("scripts/twisted_coprime_gain_probe.py",
             "observational_succ/pi_source_collision.py",
             "observational_succ/twisted_source_energy.py",
             "observational_succ/pi_source_genesis.py",
             "research/2026-10-24/PI_TWISTED_OBSERVER_PREREGISTRATION.md")
    result = {"status": "VERIFIED_FINITE", "pi_normality": "OPEN",
              "sampling_scope": "fresh finite holdout; no asymptotic inference",
              "rows": rows,
              "source_sha256": {p: sha256((ROOT/p).read_bytes()).hexdigest()
                                for p in paths}}
    rendered = json.dumps(result, indent=2, sort_keys=True)+"\n"
    if args.output:
        args.output.write_text(rendered)
    print(rendered, end="")


if __name__ == "__main__":
    main()
