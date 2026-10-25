"""Independent finite exact audit of outward BBP intervals and pair sweeps.

Direct alternating Fractions check the integer binary-splitting instrument;
direct four-pole recurrence checks source intervals; exhaustive endpoint
assignments check every accepted small interval-pair certificate. No limit
or pi-normality assertion follows from this finite regression.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
import hashlib
from itertools import combinations, product
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from observational_succ.pi_collision_intervals import (
    SourceIntervals, atan_dyadic_bounds, certified_pair_count, source_intervals,
)


def receipt() -> dict:
    atan_checks = 0
    for q in (2, 3, 5, 7, 16, 239):
        for bits in range(1, 70):
            terms = bits+8
            a = sum((Q((-1)**k, (2*k+1)*q**(2*k+1))
                     for k in range(terms)), Q(0))
            b = a+Q((-1)**terms, (2*terms+1)*q**(2*terms+1))
            lo, hi = atan_dyadic_bounds(q, bits)
            assert Q(lo, 2**bits) < min(a,b)
            assert max(a,b) < Q(hi, 2**bits)
            atan_checks += 1

    source = [Q(0)]
    for n in range(1, 121):
        forcing = Q(4,8*n-7)-Q(2,8*n-4)-Q(1,8*n-3)-Q(1,8*n-2)
        source.append((16*source[-1]+forcing) % 1)
    source_checks = source_refusals = 0
    for bits in (12, 20, 40, 80):
        for start in (1, 3, 10, 25, 67):
            try:
                sample = source_intervals(start, 30, bits, 12)
            except ArithmeticError:
                source_refusals += 1
                continue
            for k, (a,b) in enumerate(sample.bounds):
                assert a <= 2**bits*source[start+k] <= b
                source_checks += 1

    pool = [(a,b) for a in range(0,16,3)
            for b in range(a,min(a+2,16))]
    accepted = rejected = vertex_checks = 0
    for n in (1,2,3):
        for intervals in combinations(pool,n):
            for cells in (3,4,5,7):
                sample = SourceIntervals(1,4,intervals,1,0)
                try:
                    count = certified_pair_count(sample,cells)
                except ArithmeticError:
                    rejected += 1
                    continue
                accepted += 1
                for values in product(*[[Q(a,16),Q(b,16)] for a,b in intervals]):
                    brute = sum(min((x-y)%1,(y-x)%1) <= Q(1,cells)
                                for x in values for y in values)
                    assert count == brute
                    vertex_checks += 1
    paths = ("observational_succ/pi_collision_intervals.py",
             "scripts/pi_lag_interval_independent_oracle.py")
    return {
        "schema": "SUCC-PI-LAG-INTERVAL-INDEPENDENT-1",
        "status": "VERIFIED_FINITE",
        "arithmetic": "integer and Fraction only",
        "atan_enclosures": atan_checks,
        "exact_BBP_source_enclosures": source_checks,
        "source_boundary_refusals": source_refusals,
        "pair_certificates_accepted": accepted,
        "pair_certificates_rejected": rejected,
        "independent_vertex_pair_checks": vertex_checks,
        "source_sha256": {p: hashlib.sha256((ROOT/p).read_bytes()).hexdigest()
                          for p in paths},
        "boundary": "Finite calibration; not an asymptotic collision or normality proof",
    }


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--output')
    args = parser.parse_args()
    result = json.dumps(receipt(), indent=2, sort_keys=True)+'\n'
    if args.output:
        Path(args.output).write_text(result)
    else:
        print(result, end='')
