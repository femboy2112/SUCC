#!/usr/bin/env python3
"""Replay Main XXIV research gates serially at a clean, explicit Git head.

Research-local tests are outside native unittest discovery. This runner makes
their actual entrypoints reproducible without launching the native suite again.
Logs and the head/tree-bound receipt must be written outside the checkout.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[1]
RESEARCH = "research/2026-11-10/"


def commands(out):
    for folder in ("basel_crt_omega_phasebridge",
                   "basel_crt_omega_phasebridge/prime_archimedean",
                   "basel_crt_omega_phasebridge/ratio_fiber_joinings",
                   "cursed_categories_dedekind_yoneda",
                   "circle_line_lr_observer/height_shield",
                   "circle_line_lr_observer/zero_anchor_identity"):
        yield folder.replace("/", "-"), ["-W", "error", "-m", "unittest", "discover", "-s", RESEARCH+folder, "-p", "test_*.py", "-v"]
    for path in ("gaussian_circle_long_lag/gaussian_circle_probe.py",
                 "gaussian_circle_long_lag/viete_three_way_probe.py",
                 "gaussian_circle_long_lag/source_pair_probe.py",
                 "gaussian_circle_long_lag/long_lag_holdout.py",
                 "cursed_categorical_computation/round_ii_probe.py",
                 "cursed_categorical_computation/round_iii_dedekind/dedekind_order_probe.py",
                 "cursed_categorical_computation/round_iii_dedekind/computation_probe.py",
                 "cursed_categorical_computation/round_iii_dedekind/rational_compiler_probe.py",
                 "circle_line_lr_observer/observer_probe.py",
                 "aperiodic_circle_observer/aperiodic_probe.py",
                 "aperiodic_circle_observer/cycle_independent_probe.py",
                 "zero_anchored_lambda_haar/adversarial_probe.py",
                 "zero_seed_microscope/probe.py"):
        argv = ["-W", "error", RESEARCH+path]
        if path.startswith("aperiodic_circle_observer/"):
            target = out / path.replace("/", "-") / "receipt.json"
            target.parent.mkdir(parents=True, exist_ok=True)
            argv += ["--output", str(target)]
        yield path.replace("/", "-"), argv
    yield "lambda-haar-canonical-full-finite-protocol", [
        "-W", "error", "scripts/zero_anchored_lambda_haar_probe.py",
        "--output", str(out / "lambda_haar_canonical_finite_report.json")]
    yield "exact-archived-certificate-replay", [
        "-W", "error", "scripts/main_xxiv_certificate_replay.py", "--out", str(out / "exact-replay")]


def git(*args):
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    out = args.out.resolve()
    if out == ROOT or ROOT in out.parents:
        parser.error("write receipts outside the checkout to preserve candidate bytes")
    if git("status", "--porcelain", "--untracked-files=no"):
        parser.error("tracked candidate must be clean")
    out.mkdir(parents=True, exist_ok=True)
    head, tree = git("rev-parse", "HEAD"), git("rev-parse", "HEAD^{tree}")
    env = dict(os.environ, PYTHONPATH=str(ROOT), OPENBLAS_NUM_THREADS="1", OMP_NUM_THREADS="1")
    results = []
    entries = list(commands(out))
    for name, argv in entries:
        start = time.monotonic()
        log = out / (name+".log")
        with log.open("w") as stream:
            proc = subprocess.run([sys.executable, *argv], cwd=ROOT, env=env,
                                  stdout=stream, stderr=subprocess.STDOUT)
        results.append(dict(name=name, command=[sys.executable, *argv],
                            exit_code=proc.returncode, seconds=round(time.monotonic()-start, 3),
                            log=log.name, sha256=hashlib.sha256(log.read_bytes()).hexdigest()))
        print(name, proc.returncode, flush=True)
        if proc.returncode:
            break
    unchanged = head == git("rev-parse", "HEAD") and not git("status", "--porcelain", "--untracked-files=no")
    passed = unchanged and len(results) == len(entries) and all(r["exit_code"] == 0 for r in results)
    receipt = dict(head=head, tree=tree, python=sys.version, commands=results,
                   tracked_candidate_unchanged=unchanged, status="PASS" if passed else "FAIL",
                   authority="finite implementation/certificate replay; no universal proof promotion")
    (out/"receipt.json").write_text(json.dumps(receipt, indent=2)+"\n")
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
