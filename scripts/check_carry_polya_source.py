"""Replay the source-locked research gates without rewriting inherited receipts."""
from __future__ import annotations

import argparse
import hashlib
from importlib.metadata import version
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[1]
DATE = ROOT / "research/2026-10-28"
FOCUSED = (
    "test_bbp_dirichlet_resolvent.py", "test_divisor_observer_spectrum.py",
    "test_polya_coherent_observer.py", "test_oily_prime_growth_compiler.py",
    "test_origin_fiber_arithmetic_observer.py", "test_original_bbp_carry_origin_bridge.py",
    "test_origin_locked_oily_zeta.py", "test_bbp_virtual_seed_prior.py",
    "test_math_memory.py",
)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--full", action="store_true", help="also run all native tests")
    args = parser.parse_args()
    destination = args.output.resolve()
    destination.mkdir(parents=True, exist_ok=True)
    env = {**os.environ, "PYTHONPATH": str(ROOT), "OPENBLAS_NUM_THREADS": "1",
           "OMP_NUM_THREADS": "1", "MKL_NUM_THREADS": "1"}
    commands, failures = [], []
    manifest = json.loads((DATE / "CARRY_POLYA_SOURCE_MANIFEST.json").read_text())
    for path, expected in manifest["source_hashes"].items():
        actual = hashlib.sha256((ROOT / path).read_bytes()).hexdigest()
        if actual != expected:
            raise RuntimeError(f"Source/proof receipt mismatch: {path}")
    print(f"source/proof manifest: {len(manifest['source_hashes'])} hashes verified", flush=True)

    def run(label, argv, cwd=ROOT):
        start = time.monotonic()
        log_path = destination / f"{label}.log"
        with log_path.open("w") as log:
            result = subprocess.run(argv, cwd=cwd, env=env, stdout=log,
                                    stderr=subprocess.STDOUT, timeout=2400)
        commands.append({"label": label, "command": argv, "cwd": str(cwd),
                         "exit_code": result.returncode,
                         "seconds": round(time.monotonic() - start, 3),
                         "log": log_path.name,
                         "log_sha256": hashlib.sha256(log_path.read_bytes()).hexdigest()})
        if result.returncode:
            failures.append(label)
        print(f"{label}: exit {result.returncode}", flush=True)
        return result.returncode

    py = sys.executable
    for name, command in (
        ("provenance", ["scripts/verify_provenance.py"]),
        ("observer-foundations", ["scripts/observer_foundations_probe.py"]),
        ("ordinal", ["scripts/ordinal_succ_report_probe.py"]),
        ("native-demo", ["-m", "observational_succ", "demo"]),
        ("math-memory-graph", ["scripts/verify_math_memory_graph.py"]),
        ("property-graph", ["scripts/verify_succ_property_graph.py"]),
        ("academic-vii", ["scripts/academic_main_vii_gate.py"]),
        ("academic-viii", ["scripts/academic_main_viii_gate.py"]),
        ("duck-dependencies", ["scripts/verify_duck_pi_dependencies.py"]),
        ("hostile-registry", ["scripts/main_vii_hostile_replay.py", "--target-repo", ".", "--require-fixed"]),
        ("original-source-genesis", ["scripts/pi_source_genesis_oracle.py"]),
    ):
        run(name, [py, *command])
    for pattern in FOCUSED:
        # Ensure a misspelled pattern cannot report a successful zero-test run.
        if not (ROOT / "tests" / pattern).is_file():
            raise FileNotFoundError(pattern)
        run(pattern.removesuffix(".py"),
            [py, "-m", "unittest", "discover", "-s", "tests", "-p", pattern, "-v"])
    # These parent scripts choose output by __file__. Copy their exact bytes into
    # an isolated layout so inherited research receipts are never rewritten.
    replay_root = destination / "parent-oracles"
    (replay_root / "scripts").mkdir(parents=True, exist_ok=True)
    (replay_root / "research/2026-10-28").mkdir(parents=True, exist_ok=True)
    for script, receipt in (
        ("oily_prime_growth_independent_oracle.py", "OILY_GROWTH_SYMPY_ORACLE.json"),
        ("bbp_dirichlet_finite_part_oracle.py", "ORIGINAL_BBP_DIRICHLET_FINITE_PART_RECEIPT.json"),
    ):
        copied = replay_root / "scripts" / script
        shutil.copyfile(ROOT / "scripts" / script, copied)
        label = script.removesuffix(".py")
        if not run(label, [py, str(copied)]):
            actual = json.loads((replay_root / "research/2026-10-28" / receipt).read_text())
            if actual != json.loads((DATE / receipt).read_text()):
                failures.append(label + "-receipt-drift")
    for script, receipt in (
        ("bbp_dirichlet_resolvent_oracle.py", "BBP_DIRICHLET_RESOLVENT_RECEIPT.json"),
        ("divisor_observer_spectrum_probe.py", "BBP_SIGNED_OBSERVER_RECEIPT.json"),
        ("polya_coherence_oracle.py", "POLYA_COHERENCE_ORACLE.json"),
    ):
        target = destination / receipt
        label = script.removesuffix(".py")
        if not run(label, [py, str(ROOT / "scripts" / script), "--output", str(target)]):
            if json.loads(target.read_text()) != json.loads((DATE / receipt).read_text()):
                failures.append(label + "-receipt-drift")
    if args.full:
        run("full-unittest", [py, "-m", "unittest", "discover", "-s", "tests", "-p", "test_*.py"])
    record = {"schema": "succ.carry-polya.local-validation.v1",
              "python": sys.version, "commands": commands, "failures": failures,
              "dependency_versions": {name: version(name) for name in
                                      ("sympy", "mpmath", "numpy", "scipy")},
              "source_manifest_sha256": hashlib.sha256(
                  (DATE / "CARRY_POLYA_SOURCE_MANIFEST.json").read_bytes()).hexdigest(),
              "full_suite_included": args.full, "status": "PASS" if not failures else "FAIL",
              "scope": "Local execution only; no hosted CI, analytic proof or normality authority"}
    (destination / "validation.json").write_text(json.dumps(record, indent=2, sort_keys=True) + "\n")
    print(record["status"], len(commands), "commands", failures)
    return bool(failures)


if __name__ == "__main__":
    raise SystemExit(main())
