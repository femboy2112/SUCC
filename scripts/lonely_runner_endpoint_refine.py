#!/usr/bin/env python3
"""Bounded endpoint-critical rule search, refined by exact tangent gaps.

Finite beta menu only. Every SAT model receives a full exact locality check;
endpoint coverage alone is never called a valid local rule.
"""
import argparse
from fractions import Fraction as F
import hashlib
import json
import os
from pathlib import Path
import resource
import sys
import time

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from observational_succ.lonely_runner_uniform import (
    AffineRunner, UniformRule, check_local_uniform, gap_counterexample,
    poliakova_rule, responsible_residues,
)
from observational_succ.lonely_runner_search import cover_certificate
from observational_succ.lonely_runner_verify import verify_cover


def family(limit):
    return tuple(sorted({d*2**a for d in (1, 3) for a in range(1, 9) if d*2**a <= limit}))


def candidates(affected, max_odd):
    """Retain actual velocity/alpha/beta labels, including endpoint duplicates."""
    velocities = affected+tuple(range(1, max_odd+1, 2))
    cells = [(q, k) for q in affected for k in responsible_residues(q)]
    records = []
    for v in velocities:
        by_alpha = {}
        for index, (q, k) in enumerate(cells):
            alpha = (-F(v*k, q)) % 1
            by_alpha.setdefault(alpha, []).append((index, q, k))
        for alpha, resonances in sorted(by_alpha.items()):
            resonant_q = {q for _, q, _ in resonances}
            betas = {F(0)} | {F(endpoint)-F(sign*v, q) for q in resonant_q
                              for endpoint in (-1, 1) for sign in (-1, 1)}
            for beta in sorted(betas):
                bits = 0
                for index, q, _ in resonances:
                    if abs(-F(v, q)+beta) <= 1:
                        bits |= 1 << (2*index)
                    if abs(F(v, q)+beta) <= 1:
                        bits |= 1 << (2*index+1)
                records.append((v, alpha, beta, bits))
    return cells, records


def calibration():
    affected = family(192)
    cells, records = candidates(affected, 31)
    menu = {(v, a, b) for v, a, b, _ in records}
    published = poliakova_rule()
    old = set(published.affected)
    padded = UniformRule(published.removed,
        published.rephased+tuple(AffineRunner(q, F(0), F(0)) for q in affected if q not in old),
        published.added)
    if not all((x.velocity, x.alpha, x.beta) in menu for x in padded.rescuers):
        raise ArithmeticError("finite menu lost the published 192 calibration")
    certificate = check_local_uniform(padded)
    if not certificate["local_uniform"] or padded.gain != 1:
        raise ArithmeticError("published positive calibration failed")
    return {"published_limit": 192, "gain": padded.gain,
            "padded_affected": affected, "full_locality_pass": True,
            "literal_coefficients_in_menu": True, "cells": len(cells)}


def run(limit, max_odd, seconds, max_models, destination):
    import z3
    z3.set_param("parallel.enable", False)
    z3.set_param("smt.threads", 1)
    z3.set_param("memory_max_size", 768)
    positive = calibration()
    affected = family(limit)
    cells, records = candidates(affected, max_odd)
    selected = [z3.Bool(f"use_{i}") for i in range(len(records))]
    solver = z3.Solver()
    for v in sorted({r[0] for r in records}):
        solver.add(z3.PbLe([(selected[i], 1) for i, r in enumerate(records) if r[0] == v], 1))
    solver.add(z3.PbLe([(x, 1) for x in selected], len(affected)-1))
    for bit in range(2*len(cells)):
        solver.add(z3.Or([selected[i] for i, r in enumerate(records) if (r[3] >> bit) & 1]))
    report = {"schema": "SUCC-endpoint-critical-refinement-v1", "limit": limit,
              "affected": affected, "odd_limit": max_odd, "required_gain": 1,
              "phase_scope": "complete resonance alpha; finite beta zero and every endpoint-critical value",
              "candidate_count": len(records), "endpoint_cells": 2*len(cells),
              "velocity_labels_preserved": True, "continuous_beta_infeasibility_claim": False,
              "published_calibration": positive, "seconds_limit": seconds,
              "model_limit": max_models, "solver_version": z3.get_version_string(),
              "models": [], "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    destination.mkdir(parents=True, exist_ok=True)
    (destination/"started.json").write_text(json.dumps(report, indent=2)+"\n")
    print(f"calibration passed; candidates={len(records)} endpoint_cells={2*len(cells)}", flush=True)
    start = time.monotonic()
    for attempt in range(max_models):
        remaining = seconds-(time.monotonic()-start)
        if remaining <= 0:
            report["status"] = "overall_timeout"; break
        solver.set(timeout=max(1, int(1000*remaining)))
        status = solver.check()
        if status != z3.sat:
            report["status"] = str(status)
            if status == z3.unknown:
                report["reason"] = solver.reason_unknown()
            break
        model = solver.model()
        chosen = [AffineRunner(v, a, b) for i, (v, a, b, _) in enumerate(records)
                  if z3.is_true(model.eval(selected[i]))]
        kept = {x.velocity for x in chosen if x.velocity % 2 == 0}
        rule = UniformRule(tuple(q for q in affected if q not in kept),
                           tuple(x for x in chosen if x.velocity % 2 == 0),
                           tuple(x for x in chosen if x.velocity % 2))
        certificate = check_local_uniform(rule)
        row = {"attempt": attempt, "removed": rule.removed,
               "rephased": [(x.velocity, str(x.alpha), str(x.beta)) for x in rule.rephased],
               "added": [(x.velocity, str(x.alpha), str(x.beta)) for x in rule.added],
               "gain": rule.gain, "all_endpoints_covered": True,
               "exact_local_uniform": certificate["local_uniform"]}
        if certificate["local_uniform"]:
            n0 = max(affected)//2
            delta = F(1, n0+1)
            phases = {x.velocity: (x.alpha+x.beta*delta) % 1 for x in rule.rescuers}
            speeds = tuple(v for v in range(2, 2*n0+1, 2) if v not in rule.removed)+tuple(x.velocity for x in rule.added)
            finite = cover_certificate(speeds, [phases.get(v, F(0)) for v in speeds], delta,
                                       source={"campaign": "endpoint-critical exact refinement", "N": n0})
            row["independent_finite_cover"] = verify_cover(finite)
            (destination/"verified-finite-cover.json").write_text(json.dumps(finite, indent=2)+"\n")
            report["models"].append(row); report["status"] = "verified_local_rule"
            print("VERIFIED_LOCAL_RULE "+json.dumps(row), flush=True)
            break
        gap = certificate["gap"]
        q, k, z = gap["q"], gap["k"], F(gap["z"])
        row["gap"] = gap
        row["actual_locality_counterexample"] = gap_counterexample(rule, q, k, z)
        report["models"].append(row)
        covering = [selected[i] for i, (v, a, b, _) in enumerate(records)
                    if (F(v*k, q)+a).denominator == 1 and abs(F(v, q)*z+b) <= 1]
        solver.add(z3.Or(covering))
        print(f"model={attempt} gain={rule.gain} endpoint-only; exact gap q={q} k={k} z={z}; refinement_options={len(covering)}", flush=True)
    else:
        report["status"] = "model_limit"
    report["solver_and_refinement_seconds"] = time.monotonic()-start
    report["peak_rss_kib"] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    report["solver_statistics"] = str(solver.statistics())
    report["claim_boundary"] = "Only exact full-locality and finite-cover checks certify positive results; other outcomes apply to this finite beta menu, with no general nonexistence claim."
    (destination/"result.json").write_text(json.dumps(report, indent=2)+"\n")
    print(f"FINAL {report['status']} models={len(report['models'])} seconds={report['solver_and_refinement_seconds']:.3f}", flush=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit", type=int, default=190)
    parser.add_argument("--max-odd", type=int, default=31)
    parser.add_argument("--seconds", type=float, default=120)
    parser.add_argument("--max-models", type=int, default=20)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if not 4 <= args.limit <= 192 or not 1 <= args.max_odd <= 383 or not 0 < args.seconds <= 120 or not 1 <= args.max_models <= 20:
        parser.error("bounded search domain exceeded")
    if hasattr(os, "sched_getaffinity"):
        os.sched_setaffinity(0, {min(os.sched_getaffinity(0))})
    resource.setrlimit(resource.RLIMIT_AS, (1024**3, 1024**3))
    run(args.limit, args.max_odd, args.seconds, args.max_models, args.output)


if __name__ == "__main__":
    main()
