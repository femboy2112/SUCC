#!/usr/bin/env python3
"""Replay the Main XXV research gates serially at a clean, explicit Git head.

Research-local tests are outside native unittest discovery. This runner replays
the entrypoints of the dossiers integrated by Main XXV: innovation × arithmetic
decoupling / zero-selected carry and the frontier rungs, including their full
preregistered probes. Historical ``RESULTS_*.json`` remain immutable: probes run
in a disposable copy and must reproduce exact decisions and explicitly bounded
floating diagnostics (see ``main_xxv_numeric_replay.py``); and the unit
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
import platform
import shutil
import tempfile
import importlib.metadata
from pathlib import Path
import subprocess
import sys
import time

from main_xxv_numeric_replay import compare

ROOT = Path(__file__).resolve().parents[1]
IAD = "research/2026-11-11/innovation_arithmetic_decoupling/"
RUNGS = "research/2026-11-12/frontier_rungs/"
PRIME = "research/2026-11-12/"


RESULTS = {
    "iad-probe-arithmetic": IAD + "RESULTS_arithmetic.json",
    "iad-probe-analytic": IAD + "RESULTS_analytic.json",
    "iad-band-lp-probe": IAD + "RESULTS_band_lp.json",
    "zsc-probe": IAD + "RESULTS_zsc.json",
    "rungs-probe": RUNGS + "RESULTS_rungs.json",
}


def commands(out: Path, lean_project: Path | None, replay_root: Path | None = None):
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
        yield name, ["-W", "error", str(replay_root / path) if replay_root else path]
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
    replay_root = Path(tempfile.mkdtemp(prefix="replay-source-", dir=out))
    for folder in (IAD, RUNGS):
        shutil.copytree(ROOT / folder, replay_root / folder,
                        ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
    transport = Path("research/2026-10-30/arithmetic_barrier/arithmetic/transport.py")
    (replay_root / transport).parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(ROOT / transport, replay_root / transport)
    for path in RESULTS.values():
        (replay_root / path).unlink(missing_ok=True)
    results = []
    replays = []
    entries = list(commands(out, args.lean_dependency_project, replay_root))
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
        if name in RESULTS:
            path = RESULTS[name]
            if not (replay_root / path).is_file():
                replays.append(dict(path=path, status="FAIL", error="probe did not produce its receipt"))
                print(name, "missing generated receipt", flush=True)
                break
            archived = (ROOT / path).read_bytes()
            replay = (replay_root / path).read_bytes()
            comparison = compare(json.loads(archived), json.loads(replay), Path(path).name)
            comparison.update(path=path,
                              archived_sha256=hashlib.sha256(archived).hexdigest(),
                              replay_sha256=hashlib.sha256(replay).hexdigest(),
                              replay_path=str(replay_root / path))
            (out / (name + "-comparison.json")).write_text(json.dumps(comparison, indent=2) + "\n")
            replays.append(comparison)
            if comparison["status"] != "PASS":
                print(name, "receipt mismatch", flush=True)
                break
    unchanged = head == git("rev-parse", "HEAD") and not git("status", "--porcelain", "--untracked-files=no")
    passed = (unchanged and len(results) == len(entries)
              and all(r["exit_code"] == 0 for r in results)
              and len(replays) == len(RESULTS)
              and all(r["status"] == "PASS" for r in replays))
    receipt = dict(head=head, tree=tree, python=sys.version, executable=sys.executable,
                   platform=platform.platform(),
                   dependencies={p: importlib.metadata.version(p) for p in ("numpy", "scipy", "mpmath", "sympy")},
                   commands=results, numeric_replays=replays, replay_source=str(replay_root),
                   lean_replayed=args.lean_dependency_project is not None,
                   tracked_candidate_unchanged=unchanged, status="PASS" if passed else "FAIL",
                   authority="finite implementation/certificate replay; no universal proof promotion")
    (out / "receipt.json").write_text(json.dumps(receipt, indent=2) + "\n")
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
