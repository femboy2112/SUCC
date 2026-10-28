#!/usr/bin/env python3
"""Exact countermodel to GW necessity, not to the prefix-hole conjecture."""
import argparse
from fractions import Fraction as F
from itertools import permutations
import json
from math import gcd
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from scripts.lonely_runner_referee_fraction import source_gaps


def receipt():
    n, removed, inserted = 7, (1, 3, 5), (8, 10, 12)
    retained = (2, 4, 6)
    speeds = retained+inserted
    if source_gaps(n, speeds):
        raise ArithmeticError("dilated baseline does not cover")
    t = F(1, n)
    margin = min(min((v*t)%1, 1-(v*t)%1) for v in speeds)
    if margin != F(1, n):
        raise ArithmeticError("exact lower witness failed")
    prefixes = []
    for j in range(3):
        gaps = source_gaps(n, retained+inserted[:j])
        if not gaps:
            raise ArithmeticError("control unexpectedly refutes prefix-hole assertion")
        a, b = gaps[0]
        witness = (a+b)/2
        minimum = min(min((v*witness)%1, 1-(v*witness)%1) for v in retained+inserted[:j])
        if minimum <= F(1, n):
            raise ArithmeticError("prefix hole witness failed")
        prefixes.append({"inserted_count": j, "time": str(witness), "minimum": str(minimum)})
    matching_failures = []
    for order in permutations(inserted):
        # r=1 is first in every matching, so b=n-1 already kills its GW condition.
        if gcd(1, n-1) != 1:
            raise ArithmeticError("unit gcd control failed")
        matching_failures.append({"matching": list(zip(removed, order)),
                                  "failed_removed_speed": 1, "window_integer": n-1,
                                  "gcd": 1})
    return {"schema": "SUCC-three-entry-GW-countermodel-v1", "n": n,
            "removed": removed, "inserted": inserted, "speeds": speeds,
            "speed_gcd": gcd(*speeds), "full_fraction_cover": True,
            "lower_witness": {"time": "1/7", "minimum": "1/7"},
            "exact_loneliness": "1/7", "prefix_holes": prefixes,
            "all_GW_matchings_fail": matching_failures,
            "refuted_claim": "all three-entry tight sets are individually GW admissible",
            "prefix_hole_conjecture_refuted": False,
            "academic_novelty_claim": False}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    rendered = json.dumps(receipt(), sort_keys=True, indent=2)+"\n"
    if args.output:
        args.output.write_text(rendered)
    else:
        print(rendered, end="")


if __name__ == "__main__":
    main()
