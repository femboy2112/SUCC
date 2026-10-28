#!/usr/bin/env python3
"""Deterministic exact Gamma receipt; default stdout, optional --output/--verify."""

import argparse
from dataclasses import asdict
from fractions import Fraction
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from observational_succ.lonely_runner_two_entry import (
    all_retained, general_effective_bounds, general_single_insert_hole,
    occupancy_upper_bound, periodic_occupancy, single_insert_hole,
    uncovered_intervals,
)


def encode_exact(value):
    if isinstance(value, Fraction):
        return [value.numerator, value.denominator]
    if isinstance(value, dict):
        return {k: encode_exact(v) for k, v in value.items()}
    if isinstance(value, (tuple, list)):
        return [encode_exact(v) for v in value]
    return value


def receipt():
    hole_cases = [(5, 2, 4, 7), (6, 2, 3, 9), (8, 2, 3, 11)]
    holes = [general_single_insert_hole(*case) for case in hole_cases]
    holes.append(single_insert_hole(74, 70, 72, 2520))
    if not all(hole.verify() for hole in holes):
        raise RuntimeError("a rational one-insertion hole failed exact verification")
    positives = []
    for n, r1, r2, w1, w2 in ((5, 1, 3, 6, 8), (8, 2, 3, 11, 13),
                               (74, 70, 72, 140, 144), (284, 280, 282, 560, 564)):
        speeds = all_retained(n, r1, r2) + (w1, w2)
        gaps = uncovered_intervals(n, speeds)
        bounds = general_effective_bounds(n, r1, r2)
        if gaps or not w1 < bounds["first_strict_bound"] or not w2 <= 2 * (n - 1) * w1:
            raise RuntimeError("a known cover or necessary bound failed")
        positives.append({"n": n, "removed": [r1, r2], "inserted": [w1, w2],
                          "all_time_cover": True, "bounds": bounds})
    a, b = Fraction(-1, 35), Fraction(1, 35)
    occupied = periodic_occupancy(5, 7, a, b)
    sharp = occupancy_upper_bound(5, 7, b - a)
    if occupied != sharp or occupied != b - a:
        raise RuntimeError("sharp discrepancy calibration failed")
    return encode_exact({
        "schema": "SUCC-lonely-runner-gamma-v1",
        "authority": "exact finite source replay; universal theorem is a paper proof",
        "theorem": "GAMMA-05; every two-entry 1/n cover has w2<4*n^3 for n>=5",
        "one_insertion_holes": [asdict(hole) for hole in holes],
        "known_covers": positives,
        "sharp_occupancy_control": {"n": 5, "velocity": 7, "left": a, "right": b,
                                    "occupied": occupied, "upper_bound": sharp},
        "no_general_lonely_runner_claim": True,
        "no_full_gamma_kernel_claim": True,
        "academic_priority": "unverified for unrestricted bound; upper-half classification prior art",
    })


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--output", type=Path)
    group.add_argument("--verify", type=Path)
    args = parser.parse_args()
    rendered = json.dumps(receipt(), sort_keys=True, indent=2) + "\n"
    if args.verify:
        if args.verify.read_text() != rendered:
            raise SystemExit("Gamma receipt differs from exact replay")
        print("Gamma receipt matches exact replay")
    elif args.output:
        args.output.write_text(rendered)
    else:
        print(rendered, end="")


if __name__ == "__main__":
    main()
