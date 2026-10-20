#!/usr/bin/env python3
"""Exact finite arithmetic holdout; prints JSON and does not grant authority."""
from __future__ import annotations

from dataclasses import asdict
from fractions import Fraction
from hashlib import sha256
from itertools import product
import json
from math import gcd
from pathlib import Path
import platform
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from observational_succ.abc_effective_mean import (  # noqa: E402
    dyadic_first_moment_lower, effective_constant_budget, primitive_divisor_budget,
    primitive_divisor_count_mobius, raw_discrepancy_bound, raw_divisor_count,
)


def direct(X, d, e, f, primitive):
    return sum(
        a % d == b % e == (a+b) % f == 0
        and (not primitive or gcd(a,b) == 1)
        for a in range(1, int(X)+1)
        for b in range(1, int(X)+1)
        if a+b <= X
    )


def main():
    cases = 0
    max_raw_ratio = Fraction()
    max_center_ratio = Fraction()
    moduli = [(d,e,f) for d,e,f in product(range(1,10), repeat=3)
              if gcd(d,e) == gcd(d,f) == gcd(e,f) == 1]
    cutoffs = (2, Fraction(7,2), 5, 11, 23, Fraction(101,4), 41)
    for X in cutoffs:
        for d,e,f in moduli:
            raw = raw_divisor_count(X,d,e,f)
            primitive = primitive_divisor_count_mobius(X,d,e,f)
            if raw != direct(X,d,e,f,False):
                raise AssertionError(("raw census",X,d,e,f))
            if primitive != direct(X,d,e,f,True):
                raise AssertionError(("primitive census",X,d,e,f))
            error = abs(raw - Fraction(X)**2/(2*d*e*f))
            raw_bound = raw_discrepancy_bound(X,d,e,f)
            if error > raw_bound:
                raise AssertionError(("raw discrepancy",X,d,e,f))
            budget = primitive_divisor_budget(X,d,e,f)
            center_error = abs(primitive-budget.finite_center)
            if center_error > budget.lattice_error:
                raise AssertionError(("Mobius center",X,d,e,f))
            max_raw_ratio = max(max_raw_ratio,error/raw_bound)
            max_center_ratio = max(max_center_ratio,center_error/budget.lattice_error)
            cases += 1
    source_paths = (
        "observational_succ/abc_effective_mean.py",
        "observational_succ/cloud_abc_correlations.py",
        "observational_succ/abc_triple_moment.py",
        "tests/test_abc_effective_mean.py",
        "scripts/abc_effective_mean_probe.py",
        "research/2026-10-20/ABC_EFFECTIVE_MEAN.md",
    )
    receipt = {
        "schema": "succ.abc_effective_mean.exact_finite_probe.v1",
        "proof_status": "paper proof; finite probe is supporting evidence only",
        "formal_status": "entire effective mean theorem not Lean-formalized",
        "checkout": subprocess.check_output(
            ["git","rev-parse","HEAD"],cwd=ROOT,text=True).strip(),
        "working_tree_dirty": bool(subprocess.check_output(
            ["git","status","--porcelain"],cwd=ROOT,text=True).strip()),
        "python": platform.python_version(),
        "cutoffs": cutoffs,
        "modulus_range": "1 <= d,e,f <= 9, pairwise coprime",
        "case_count": cases,
        "checks": ["raw CRT rows against direct a,b census",
                   "full Mobius primitive count against direct gcd census",
                   "exact uniform raw discrepancy",
                   "exact finite Mobius center discrepancy"],
        "failures": 0,
        "max_raw_error_over_bound": max_raw_ratio,
        "max_center_error_over_bound": max_center_ratio,
        "coprime_k_shortcut_counterexample": {
            "X":4, "d":2, "e":1, "f":1, "wrong_count":2,
            "actual_count":primitive_divisor_count_mobius(4,2,1,1),
        },
        "endpoint_finite_subexpansion": {
            "X":32, "K":5, "lower_S_1":dyadic_first_moment_lower(32,5),
            "scope":"finite exact lower bound; divergence uses Appendix A proof",
        },
        "encoded_constants": {
            str(t): asdict(effective_constant_budget(t))
            for t in (Fraction(0),Fraction(1,2),Fraction(3,5))
        },
        "source_sha256": {
            name:sha256((ROOT/name).read_bytes()).hexdigest() for name in source_paths
        },
        "scope": "No full suite, external referee, kernel proof, or academic priority claim.",
    }
    print(json.dumps(receipt,indent=2,default=str,sort_keys=True))


if __name__ == "__main__":
    main()
