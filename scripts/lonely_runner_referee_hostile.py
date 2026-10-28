#!/usr/bin/env python3
"""Independent exact replay of 7,992 quadratic-growth hostile source cases.

This standard-library-only probe imports no SUCC bound, witness, interval,
or certificate implementation. It checks finite source metrics and the
common-multiple gap lower bound directly with integer/Fraction arithmetic.
The universal proof and academic priority are separate claims.
"""

import argparse
from fractions import Fraction as F
import json
from math import gcd, lcm
from pathlib import Path


def circle_distance(value):
    residue = value % 1
    return min(residue, 1-residue)


def check_common_multiple_source(n, r, s, scale):
    """Check the actual source and its quantitative open escape interval.

    Both endpoints are derived from this source, including the upper cap
    before the next inserted-speed bad band. No precomputed bound routine
    or assumption that an entire baseline-safe interval stays uncovered
    enters the check.
    """
    inserted = lcm(r, s) * scale
    radius = F(n-r, n*r*(n-1))
    lower = F(1, n*inserted)
    upper = min(radius, F(n-1, n*inserted))
    width_lower_bound = min(F(1, n*r*(n-1)), F(n-2, n*inserted))
    if not upper-lower >= width_lower_bound > 0:
        raise ArithmeticError(f"gap-width failure: {(n, r, s, scale)}")
    time = F(1, r) + (lower+upper)/2
    actual_source = tuple(v for v in range(1, n) if v not in (r, s)) + (inserted,)
    if not 0 < time < 1:
        raise ArithmeticError(f"time left the unit interval: {(n, r, s, scale)}")
    if min(circle_distance(v*time) for v in actual_source) <= F(1, n):
        raise ArithmeticError(f"actual source has no claimed strict hole: {(n, r, s, scale)}")


def receipt():
    unit_cases = 0
    minimum = F(1)
    # Exhaust all nonzero residue classes a and all units p independently;
    # do not construct p using the proof's CRT or near-half recipe.
    for modulus in range(2, 101):
        units = [p for p in range(1, modulus) if gcd(p, modulus) == 1]
        for residue in range(1, modulus):
            best = max(circle_distance(F(residue*p, modulus)) for p in units)
            if best < F(1, 6):
                raise ArithmeticError(f"unit-center failure: {(modulus, residue, best)}")
            minimum = min(minimum, best)
            unit_cases += 1
    common_cases = 0
    scales = (1, 3, 10**40)
    for n in range(5, 31):
        for r in range((n-1)//2+1, n-1):
            for s in range(r+1, n):
                for scale in scales:
                    check_common_multiple_source(n, r, s, scale)
                    common_cases += 1
    if (unit_cases, common_cases) != (4950, 3042):
        raise ArithmeticError("incomplete or changed finite source domain")
    if minimum != F(1, 6):
        raise ArithmeticError("the sharp finite unit-phase control changed")
    return {
        "authority": "fresh finite exact hostile checks; universal proof reviewed separately",
        "common_multiple_source_cases": common_cases,
        "minimum_observed_max_unit_phase": [minimum.numerator, minimum.denominator],
        "scales": [1, 3, str(10**40)],
        "status": "pass",
        "unit_source_cases": unit_cases,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--output", type=Path)
    group.add_argument("--verify", type=Path)
    args = parser.parse_args()
    rendered = json.dumps(receipt(), sort_keys=True, indent=2) + "\n"
    if args.verify:
        if args.verify.read_text() != rendered:
            raise SystemExit("independent quadratic receipt differs from exact source replay")
        print("7,992 independent exact source checks match the saved receipt")
    elif args.output:
        args.output.write_text(rendered)
    else:
        print(rendered, end="")


if __name__ == "__main__":
    main()
