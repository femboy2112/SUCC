#!/usr/bin/env python3
"""Exact endpoint-capacity controls; universal proof is in OBSTRUCTION.md."""

import argparse
from fractions import Fraction as F
import json
from math import gcd
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from observational_succ.lonely_runner_uniform import (
    AffineRunner, UniformRule, check_local_uniform, poliakova_rule,
)


def _support(affected):
    values = tuple(affected)
    if (not values or len(set(values)) != len(values)
            or any(type(q) is not int or q < 2 or q % 2 for q in values)):
        raise ValueError("distinct positive even affected velocities required")
    return tuple(sorted(values))


def endpoint_capacity(affected, runner):
    """Compute the manuscript's weighted endpoint count using exact arithmetic."""
    total = F(0)
    for q in _support(affected):
        residues = tuple(k for k in range(q) if gcd(k, q // 2) == 1)
        resonant = sum((F(runner.velocity * k, q) + runner.alpha).denominator == 1
                       for k in residues)
        ends = sum(abs(F(sign * runner.velocity, q) + runner.beta) <= 1
                   for sign in (-1, 1))
        total += F(resonant * ends, 2 * len(residues))
    return total


def fixed_support_capacity_maximum(affected, velocity):
    """Exact maximum over all real alpha,beta for this finite support and v.

    Useful alpha values are the finitely many exact resonances. Endpoint
    coverage changes only at beta=+-1+-v/q. Since all constraints are closed,
    every value on an open segment is also achieved or improved at its
    boundary. This finite maximization does not replace the universal proof.
    """
    affected = _support(affected)
    if type(velocity) is not int or velocity < 1:
        raise ValueError("positive integer velocity required")
    residues = {q: tuple(k for k in range(q) if gcd(k, q // 2) == 1)
                for q in affected}
    alphas = sorted({(-F(velocity * k, q)) % 1
                     for q in affected for k in residues[q]})
    betas = sorted({F(endpoint) - F(sign * velocity, q)
                    for q in affected for endpoint in (-1, 1) for sign in (-1, 1)})
    maximum, witness = F(-1), None
    for alpha in alphas:
        fractions = {
            q: F(sum((F(velocity * k, q) + alpha).denominator == 1
                     for k in residues[q]), len(residues[q]))
            for q in affected
        }
        for beta in betas:
            capacity = sum((fractions[q] * sum(
                abs(F(sign * velocity, q) + beta) <= 1 for sign in (-1, 1)) / 2
                for q in affected), F(0))
            if capacity > maximum:
                maximum = capacity
                witness = AffineRunner(velocity, alpha, beta)
    if endpoint_capacity(affected, witness) != maximum:
        raise ArithmeticError("capacity maximizer failed direct recomputation")
    return maximum, witness


def sharp_rule(d):
    if type(d) is not int or d < 1 or d % 2 == 0:
        raise ValueError("positive odd d required")
    return UniformRule((4 * d,), (), (
        AffineRunner(d, F(3, 4), F(0)),
        AffineRunner(3 * d, F(3, 4), F(0)),
    ))


def receipt():
    sharp = []
    for d in (1, 3, 5, 15, 45):
        rule = sharp_rule(d)
        checked = check_local_uniform(rule)
        capacities = [endpoint_capacity(rule.affected, v) for v in rule.added]
        if not checked["local_uniform"] or capacities != [F(1, 2), F(1, 2)]:
            raise ArithmeticError("sharp dyadic construction failed")
        sharp.append({"d": d, "removed": [4*d], "added": [d, 3*d],
                      "alpha": "3/4", "beta": "0", "gain": rule.gain,
                      "checked_cells": checked["checked_cells"],
                      "capacities": list(map(str, capacities))})
    maxima = []
    for d in (1, 3, 15):
        affected = tuple(d * 2**a for a in range(1, 5))
        velocities = sorted(set(affected) | {1, 3, 5, 7, 9, d, 3*d, 5*d})
        for v in velocities:
            maximum, witness = fixed_support_capacity_maximum(affected, v)
            bound = F(1) if v % 2 == 0 else F(1, 2)
            if maximum > bound:
                raise ArithmeticError("exact capacity maximum exceeds theorem")
            maxima.append({"d": d, "affected": affected, "velocity": v,
                           "maximum": str(maximum), "bound": str(bound),
                           "alpha": str(witness.alpha), "beta": str(witness.beta)})
    published = poliakova_rule()
    rescuer = next(v for v in published.rephased if v.velocity == 12)
    hostile_capacity = endpoint_capacity(published.affected, rescuer)
    if hostile_capacity != F(3, 2) or not check_local_uniform(published)["local_uniform"]:
        raise ArithmeticError("published two-odd-part scope control failed")
    return {
        "schema": "SUCC-dyadic-obstruction-v1",
        "claim": "same affected odd part implies added_count >= 2*removed_count",
        "authority": "exact finite controls; universal theorem is a paper proof",
        "sharp_examples": sharp,
        "complete_fixed_support_endpoint_maxima": maxima,
        "hostile_two_odd_parts": {"published_gain": published.gain,
                                  "rescuer_velocity": 12,
                                  "endpoint_capacity": str(hostile_capacity)},
        "no_full_lean_proof": True,
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
            raise SystemExit("Dyadic endpoint receipt differs from exact replay")
        print("Dyadic endpoint receipt matches exact replay")
    elif args.output:
        args.output.write_text(rendered)
    else:
        print(rendered, end="")


if __name__ == "__main__":
    main()
