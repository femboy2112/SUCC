#!/usr/bin/env python3
"""Replay the preregistered source experiment; output contains exact intervals."""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from observational_succ.pi_source_collision import prime_window, small_ball_pairs
from observational_succ.twisted_source_energy import source_energy_report


def json_exact(value):
    if isinstance(value, Q):
        return {"numerator": str(value.numerator), "denominator": str(value.denominator)}
    raise TypeError(type(value).__name__)


def compact_interval(low, high, digits=10):
    scale = 10**digits
    return {"scale": scale, "lower_integer": (low*scale).__floor__(),
            "upper_integer": (high*scale).__ceil__()}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    reports = []
    for prime in (41, 97, 257, 1009):
        for frequency in (1, 3):
            report = source_energy_report(prime, frequency)
            report["display_mean_squared_interval"] = compact_interval(
                report["direct_mean_squared_low"], report["direct_mean_squared_high"])
            for row in report["rows"]:
                row["display_energy_interval"] = compact_interval(
                    row["energy_low"], row["energy_high"])
                assert report["direct_mean_squared_low"] <= row["mean_squared_upper"]
            reports.append(report)
    # Independent lower-scale replay of the pinned PR266 receipt, using the
    # merged exact Fraction implementation rather than its large interval sweep.
    window = prime_window(2081)
    pairs = small_ball_pairs(window.states, Q(1, 16))
    assert pairs == 76544
    replay = {"prime": 2081, "length": window.length, "cells": 16,
              "ordered_close_pairs": pairs,
              "scaled_collision": Q(16*pairs, window.length**2),
              "pinned_pr": 266,
              "pinned_head": "e821a90d615aa5f78a61ad08c9d7a44709ad6189"}
    paths = (
        "observational_succ/twisted_source_energy.py",
        "observational_succ/pi_source_collision.py",
        "observational_succ/pi_source_genesis.py",
        "scripts/twisted_source_energy_probe.py",
        "research/2026-10-24/PI_TWISTED_OBSERVER_PREREGISTRATION.md",
    )
    result = {"status": "VERIFIED_FINITE", "pi_normality": "OPEN",
              "base_commit": "e648df3e4fca73ab6b942232b5ca4b310e9cac08",
              "preregistered_reports": reports, "pr266_replay": replay,
              "source_sha256": {p: hashlib.sha256((ROOT/p).read_bytes()).hexdigest()
                                for p in paths}}
    text = json.dumps(result, default=json_exact, indent=2, sort_keys=True)+"\n"
    if args.output:
        args.output.write_text(text, encoding="utf-8")
        print(json.dumps({"status": result["status"], "rows": len(reports),
                          "source_windows": [41, 97, 257, 1009],
                          "pr266_pairs_replayed": pairs}, sort_keys=True))
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
