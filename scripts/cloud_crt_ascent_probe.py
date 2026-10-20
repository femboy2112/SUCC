#!/usr/bin/env python3
"""Reproducible exact holdout; run from repository root with PYTHONPATH=."""
from collections import Counter
from fractions import Fraction as F
from hashlib import sha256
from math import gcd
from pathlib import Path
import json
import random

from observational_succ.cloud_crt_ascent import (
    cell_enclosure, primitive_triangle_budget, primitive_triangle_count,
    triangle_count, triangle_enclosure, valuation_pattern,
)


def main():
    rng = random.Random(7719021)
    checks = 0
    for _ in range(48):
        W = rng.randrange(1, 43)
        X = F(rng.randrange(2, 380), 3)
        R = {(rng.randrange(W), rng.randrange(W)) for _ in range(rng.randrange(1, 25))}
        all_counts, primitive_counts = Counter(), Counter()
        for a in range(1, int(X)+1):
            for b in range(1, int(X-a)+1):
                key = (a % W, b % W)
                all_counts[key] += 1
                if gcd(a,b) == 1:
                    primitive_counts[key] += 1
        actual = sum(all_counts[pair] for pair in R)
        primitive = sum(primitive_counts[pair] for pair in R)
        assert triangle_count(X, W, R) == actual
        assert triangle_enclosure(X, W, R).contains(actual)
        assert cell_enclosure(X, W, R).contains(actual)
        assert primitive_triangle_count(X, W, R) == primitive
        M = max(1, int(X // 2))
        for D in {1, max(1, M//3), M}:
            assert primitive_triangle_budget(X, W, R, D).enclosure.contains(primitive)
        checks += 1
    W, R = valuation_pattern(2, 12, 0, 0)
    X = 4097
    deep = {'X': X, 'W': W, 'r': len(R), 'count': triangle_count(X,W,R),
            'naive_main_term': str(F(len(R)*X*X,2*W*W))}
    # Geometrically opposite sharpness control: a real cutoff just below an integer.
    Y = F(10**12-1, 10**6)
    negative_discrepancy = (Y*Y/2 - triangle_count(Y,1,{(0,0)}))/Y
    assert negative_discrepancy > F(149999,100000)
    paths = ['observational_succ/cloud_crt_ascent.py', 'tests/test_cloud_crt_ascent.py',
             'scripts/cloud_crt_ascent_probe.py', 'research/2026-10-20/CLOUD_CRT_ASCENT.md']
    receipt = {
        'status': 'PASS', 'scope': 'finite exact independent holdout; universal proofs are in dossier',
        'base_sha': '0e56e0ae26f3d52a2ea34c0a4288478139fcb634',
        'command': 'PYTHONPATH=. python scripts/cloud_crt_ascent_probe.py',
        'seed': 7719021, 'fresh_direct_census_cases': checks,
        'deep_prime_power_counterexample': deep,
        'negative_sharpness_ratio': str(negative_discrepancy),
        'sha256': {p:sha256(Path(p).read_bytes()).hexdigest() for p in paths},
        'formal_kernel_status': 'UNVERIFIED',
        'novelty': 'CLASSICAL mechanisms; new-to-project explicit budget; academic novelty UNVERIFIED',
    }
    print(json.dumps(receipt, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
