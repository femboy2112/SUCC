#!/usr/bin/env python3
"""Exact controls for arbitrary-phase existence; not a compactness proof."""

import argparse
from fractions import Fraction as F
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from observational_succ.lonely_runner_uniform import (
    AffineRunner, UniformRule, check_local_uniform, circle_distance,
    responsible_residues,
)


def oscillatory_rule(d, n):
    """Return the affine component selected by this size's parity."""
    if type(d) is not int or d < 1 or d % 2 == 0:
        raise ValueError("positive odd d required")
    if type(n) is not int or n < 2*d:
        raise ValueError("integer N>=2d required for admissibility")
    alpha, beta = (F(3, 4), F(1, 8)) if n % 2 == 0 else (F(1, 4), F(-1, 8))
    return UniformRule((4*d,), (), (
        AffineRunner(d, alpha, beta), AffineRunner(3*d, alpha, beta),
    ))


def divergent_residual_control(m):
    """Unused odd v=5: delta=1/m², epsilon=1/m, epsilon/delta=m."""
    if type(m) is not int or m < 3:
        raise ValueError("integer m>=3 required")
    delta = F(1, m*m)
    alpha, epsilon = F(3, 4), F(1, m)
    distances = []
    for z in (-1, 0, 1):
        time = (F(1) + delta*z) / 4
        distance = circle_distance(5*time + alpha + epsilon)
        if not distance > delta:
            raise ArithmeticError("divergent residual unexpectedly rescued a tangent cell")
        distances.append(str(distance))
    return {"m": m, "N": m*m-1, "delta": str(delta),
            "alpha": str(alpha), "epsilon": str(epsilon),
            "scaled_residual": str(epsilon/delta),
            "unused_velocity": 5, "q": 4, "k": 1,
            "z": [-1, 0, 1], "distances": distances}


def receipt():
    schedules = []
    for d in (1, 3, 15):
        for n in (2*d, 2*d+1, 4*d, 4*d+1):
            rule = oscillatory_rule(d, n)
            checked = check_local_uniform(rule)
            if not checked["local_uniform"]:
                raise ArithmeticError("oscillating schedule component is not local")
            delta = F(1, n+1)
            worst = F(0)
            for k in responsible_residues(4*d):
                for z in (-1, 0, 1):
                    time = (F(k) + delta*z)/(4*d)
                    margin = min(circle_distance(v.velocity*time + v.alpha + v.beta*delta)
                                 for v in rule.added)
                    if margin > F(7, 8)*delta:
                        raise ArithmeticError("direct source rescue exceeded proved slack")
                    worst = max(worst, margin/delta)
            schedules.append({"d": d, "N": n, "alpha": str(rule.added[0].alpha),
                              "beta": str(rule.added[0].beta),
                              "all_tangent_cells_covered": True,
                              "direct_probe_max_normalized_distance": str(worst)})
    return {
        "schema": "SUCC-arbitrary-phase-affinization-v1",
        "authority": "exact finite controls; compactness theorem is a paper proof",
        "oscillatory_schedules": schedules,
        "infinite_scaled_residual_controls": [divergent_residual_control(m)
                                               for m in (3, 4, 7, 20, 1000)],
        "input_schedule_identity_preserved": False,
        "supports_and_gain_preserved_by_theorem": True,
        "no_convergence_rate_or_full_lean_proof": True,
        "academic_priority": "unverified",
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
            raise SystemExit("Phase schedule receipt differs from exact replay")
        print("Phase schedule receipt matches exact replay")
    elif args.output:
        args.output.write_text(rendered)
    else:
        print(rendered, end="")


if __name__ == "__main__":
    main()
