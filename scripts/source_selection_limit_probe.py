#!/usr/bin/env python3
"""Exact selector-depth and source-enclosure controls; no normality inference."""
from __future__ import annotations

import argparse
from dataclasses import asdict
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from observational_succ.pi_source_genesis import machin_pi_interval
from observational_succ.source_selection_limits import (
    RationalInterval, bbp_selection_budget, bbp_selector_interval,
    cylinder_mixture_report, orbit_observable_enclosure,
    signed_product_variation,
)


def encode(value):
    if isinstance(value, Q):
        return str(value)
    if isinstance(value, RationalInterval):
        return {k: encode(v) for k, v in asdict(value).items()}
    if isinstance(value, dict):
        return {k: encode(v) for k, v in value.items()}
    if isinstance(value, (tuple, list)):
        return [encode(v) for v in value]
    return value


def main():
    cylinder_checks = 0
    for base in (2, 3, 16, 5):
        for depth in (0, 1, 2, 4, 8):
            for horizon in (1, 4, 16, 32):
                for point in (Q(), Q(1, 7), Q(4, 13)):
                    r = cylinder_mixture_report(base, depth, point, horizon)
                    assert r['absolute_error'] <= r['wasserstein_budget']
                    cylinder_checks += 1
    constant_rows = [cylinder_mixture_report(16, k, 0, 64)
                     for k in (0, 2, 16, 32, 64, 96)]
    assert constant_rows[1]['interval_mean'] > Q(3, 20)
    assert constant_rows[4]['interval_mean'] < Q(1, 100)
    pi_lo, pi_hi = machin_pi_interval(96)
    alpha = RationalInterval(pi_lo/16, pi_hi/16)
    source_rows = []
    for depth, horizon in ((0, 32), (1, 32), (7, 32), (17, 32),
                           (29, 32), (47, 64), (64, 64)):
        r = bbp_selection_budget(depth, horizon)
        selected = r['selected_steps']
        low, high = orbit_observable_enclosure(alpha, 16, selected)
        weight = r['selected_fraction']
        mixture_low = weight*low+(1-weight)/6
        mixture_high = weight*high+(1-weight)/6
        assert mixture_low-r['total_budget'] <= r['interval_mean']
        assert r['interval_mean'] <= mixture_high+r['total_budget']
        assert r['exact_late_tv_budget'] <= r['geometric_late_budget']
        assert r['total_budget'] <= r['uniform_budget']
        r['independent_machin_mixture_interval'] = [mixture_low, mixture_high]
        source_rows.append(r)
    nesting_checks = 0
    for depth in range(65):
        a, b = bbp_selector_interval(depth), bbp_selector_interval(depth+1)
        assert a.left < b.left < b.right < a.right
        assert a.left < alpha.left < alpha.right < a.right
        nesting_checks += 1
    files = ['observational_succ/source_selection_limits.py',
             'tests/test_source_selection_limits.py',
             'scripts/source_selection_limit_probe.py',
             'observational_succ/pi_source_collision.py',
             'observational_succ/pi_source_genesis.py',
             'research/2026-10-24/PI_PATH_SELECTION_HOLE_CONTRACT.md']
    result = dict(
        status='VERIFIED_EXACT_FINITE', pi_normality='OPEN',
        source_law_preservation_proved=False,
        cylinder_mixture_checks=cylinder_checks,
        strict_source_nesting_checks=nesting_checks,
        held_out_base=5,
        observable='periodic x(1-x), Haar mean 1/6, circle Lipschitz constant 1',
        constant_selected_orbit_mean='0',
        constant_selector_rows=constant_rows,
        authentic_source_rows=source_rows,
        signed_product_control={str(k): signed_product_variation((2, -1), k)
                                for k in range(9)},
        source_sha256={p: hashlib.sha256((ROOT/p).read_bytes()).hexdigest()
                       for p in files})
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    text = json.dumps(encode(result), indent=2, sort_keys=True)+'\n'
    if args.output:
        args.output.write_text(text)
    else:
        print(text, end='')


if __name__ == '__main__':
    main()
