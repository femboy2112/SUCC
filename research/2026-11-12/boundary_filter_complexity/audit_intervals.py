"""Independent hostile numerical checks of the rational Gram backend.

This tests selected interior points of rational intervals. It is not a proof
of interval soundness. All deliberate undersampling cases must remain
INCONCLUSIVE regardless of the numerical sample checks.
"""
from __future__ import annotations

import json
import random
import sys
from fractions import Fraction as Q
from pathlib import Path

import mpmath as mp

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))

from observational_succ.boundary_filter_complexity import (  # noqa: E402
    certify_bbp_boundary_rank,
    gram_from_phase_intervals,
)


def as_mp(value):
    return mp.mpf(value.numerator) / value.denominator


def main():
    rng = random.Random(20261112)
    mp.mp.dps = 100
    cases = []
    checked_entries = 0
    for case in range(16):
        size = 1 + case % 4
        degree = 1 + case % 4
        harmonic = (-1 if case % 2 else 1) * (1 + case % 3)
        phases = []
        samples = []
        for _ in range(size):
            center = Q(rng.randrange(-1000, 1001), rng.randrange(2, 100))
            radius = Q(1, 10 ** (2 + case % 4)) if case % 3 else Q(3, 2)
            phases.append((center - radius, center + radius))
            samples.append(center + radius * Q(rng.randrange(-10, 11), 10))
        boxes, lower = gram_from_phase_intervals(phases, degree, harmonic, bits=24)
        # H has size rows and degree+1 columns, so it has a column kernel.
        assert size < degree + 1
        assert lower == 0
        for j in range(degree + 1):
            for k in range(degree + 1):
                frequency = harmonic * (16 ** k - 16 ** j)
                value = mp.fsum(mp.exp(2j * mp.pi * as_mp((frequency * q) % 1))
                                for q in samples) / size
                box = boxes[j][k]
                slack = mp.mpf("1e-90")
                assert as_mp(box.real_low) - slack <= value.real <= as_mp(box.real_high) + slack
                assert as_mp(box.imag_low) - slack <= value.imag <= as_mp(box.imag_high) + slack
                checked_entries += 1
        cases.append({
            "case": case,
            "rows": size,
            "columns": degree + 1,
            "harmonic": harmonic,
            "phase_intervals": [[str(lo), str(hi)] for lo, hi in phases],
            "sample_phases": [str(q) for q in samples],
            "lower_bound": str(lower),
            "verdict": "INCONCLUSIVE",
        })

    # The actual-horizon resource guard must run before constructing a source.
    guard_passed = False
    try:
        certify_bbp_boundary_rank(0, 1, 1, lookahead=8192)
    except ValueError as error:
        guard_passed = "horizon budget" in str(error)
    assert guard_passed

    receipt = {
        "status": "PASS",
        "scope": "Finite hostile numerical checks; not a universal interval theorem",
        "provenance": "Separate implementation and audit within the same model family; no external-referee claim",
        "random_seed": 20261112,
        "mpmath_decimal_precision": 100,
        "numerical_comparison_slack": "1e-90",
        "interval_bits": 24,
        "cases_count": len(cases),
        "matrix_entry_checks": checked_entries,
        "undersampled_false_positive_count": 0,
        "actual_horizon_guard_passed": guard_passed,
        "cases": cases,
    }
    target = Path(__file__).with_name("receipts") / "interval_oracle.json"
    target.write_text(json.dumps(receipt, indent=2) + "\n")
    print(f"PASS: {len(cases)} undersampled/wide/seam/negative-harmonic cases; "
          f"{checked_entries} matrix-entry numerical containment checks; actual-horizon guard")
    print("Wrote", target)


if __name__ == "__main__":
    main()
