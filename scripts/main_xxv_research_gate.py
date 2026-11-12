#!/usr/bin/env python3
"""Replay the Main XXV research gates serially at a clean, explicit Git head.

Research-local tests are outside native unittest discovery. This runner replays
the entrypoints of the dossiers integrated by Main XXV: innovation × arithmetic
decoupling / zero-selected carry and the frontier rungs, including their full
preregistered probes, whose committed ``RESULTS_*.json`` must be reproduced byte
for byte (the tracked candidate must be unchanged afterwards); and the unit
tests of the prime fixed-point dossiers integrated at their audited snapshots.
``--lean-dependency-project`` additionally replays the Lean kernel check of the
exact ZSC lemmas against a prebuilt pinned mathlib bridge. Logs and the
head/tree-bound receipt are written outside the checkout.
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
IAD = "research/2026-11-11/innovation_arithmetic_decoupling/"
RUNGS = "research/2026-11-12/frontier_rungs/"
PRIME = "research/2026-11-12/"


def commands(out: Path, lean_project: Path | None):
    for name, folder in (("iad-zsc-unit-tests", IAD), ("rungs-unit-tests", RUNGS),
                         ("prime-fixed-point-observer-unit-tests", PRIME + "prime_fixed_point_observer"),
                         ("prime-fixedpoint-cylinder-unit-tests", PRIME + "prime_fixedpoint_cylinder"),
                         ("scott-relative-defect-unit-tests", PRIME + "scott_relative_defect"),
                         ("carrier-first-goldbach-unit-tests", PRIME + "carrier_first_goldbach")):
        yield name, ["-W", "error", "-m", "unittest", "discover", "-s", folder, "-p", "test_*.py", "-v"]
    for name, path in (("iad-probe-arithmetic", IAD + "probe_arithmetic.py"),
                       ("iad-probe-analytic", IAD + "probe_analytic.py"),
                       ("iad-band-lp-probe", IAD + "band_lp_probe.py"),
                       ("zsc-probe", IAD + "probe_zsc.py"),
                       ("rungs-probe", RUNGS + "probe_rungs.py")):
        yield name, ["-W", "error", path]
    if lean_project is not None:
        yield "zsc-carry-flux-lean", [
            RUNGS + "lean/check_zsc_carry_flux_lean.py",
            "--dependency-project", str(lean_project),
            "--output", str(out / "lean"),
            "--receipt", str(out / "lean-receipt.json")]


def git(*args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--lean-dependency-project", type=Path, default=None)
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
    entries = list(commands(out, args.lean_dependency_project))
    for name, argv in entries:
        start = time.monotonic()
        log = out / (name + ".log")
        with log.open("w") as stream:
            proc = subprocess.run([sys.executable, *argv], cwd=ROOT, env=env,
                                  stdout=stream, stderr=subprocess.STDOUT)
        results.append(dict(name=name, command=[sys.executable, *argv],
                            exit_code=proc.returncode, seconds=round(time.monotonic() - start, 3),
                            log=log.name, sha256=hashlib.sha256(log.read_bytes()).hexdigest()))
        print(name, proc.returncode, flush=True)
        if proc.returncode:
            break
    unchanged = head == git("rev-parse", "HEAD") and not git("status", "--porcelain", "--untracked-files=no")
    passed = unchanged and len(results) == len(entries) and all(r["exit_code"] == 0 for r in results)
    receipt = dict(head=head, tree=tree, python=sys.version, commands=results,
                   lean_replayed=args.lean_dependency_project is not None,
                   tracked_candidate_unchanged=unchanged, status="PASS" if passed else "FAIL",
                   authority="finite implementation/certificate replay; no universal proof promotion")
    (out / "receipt.json").write_text(json.dumps(receipt, indent=2) + "\n")
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
