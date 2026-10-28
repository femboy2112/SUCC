#!/usr/bin/env python3
"""Replay exact source certificates and repository gates with durable raw logs."""
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
PACKAGE = ROOT / "research/2026-10-28/lonely_runner"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--full", action="store_true")
    args = parser.parse_args()
    destination = args.output.resolve()
    destination.mkdir(parents=True, exist_ok=True)
    env = {**os.environ, "PYTHONPATH": str(ROOT), "OPENBLAS_NUM_THREADS": "1",
           "OMP_NUM_THREADS": "1", "MKL_NUM_THREADS": "1"}
    records, failures = [], []
    manifest = json.loads((PACKAGE / "SOURCE_MANIFEST.json").read_text())
    for path, expected in manifest["source_hashes"].items():
        if hashlib.sha256((ROOT / path).read_bytes()).hexdigest() != expected:
            raise RuntimeError(f"source hash mismatch: {path}")
    print("source hashes:", len(manifest["source_hashes"]), flush=True)

    def run(label, command):
        started = time.monotonic()
        path = destination / f"{label}.log"
        with path.open("w") as log:
            try:
                result = subprocess.run(command, cwd=ROOT, env=env, stdout=log,
                                        stderr=subprocess.STDOUT, timeout=2700)
                code = result.returncode
            except subprocess.TimeoutExpired:
                log.write("\nSOURCE GATE TIMEOUT: 2700 seconds; not a passing result.\n")
                code = 124
        records.append({"label": label, "command": command, "exit_code": code,
                        "seconds": round(time.monotonic()-started, 3), "log": path.name,
                        "log_sha256": hashlib.sha256(path.read_bytes()).hexdigest()})
        if code:
            failures.append(label)
        print(label, "exit", code, flush=True)

    py = sys.executable
    for label, argv in (
        ("provenance", ["scripts/verify_provenance.py"]),
        ("observer", ["scripts/observer_foundations_probe.py"]),
        ("ordinal", ["scripts/ordinal_succ_report_probe.py"]),
        ("native-demo", ["-m", "observational_succ", "demo"]),
        ("math-graph", ["scripts/verify_math_memory_graph.py"]),
        ("property-graph", ["scripts/verify_succ_property_graph.py"]),
        ("academic-vii", ["scripts/academic_main_vii_gate.py"]),
        ("academic-viii", ["scripts/academic_main_viii_gate.py"]),
        ("duck-dependencies", ["scripts/verify_duck_pi_dependencies.py"]),
        ("hostile-registry", ["scripts/main_vii_hostile_replay.py", "--target-repo", ".", "--require-fixed"]),
        ("original-source", ["scripts/pi_source_genesis_oracle.py"]),
        ("math-catalog", ["scripts/build_math_memory.py", "--check"]),
        ("lonely-tests", ["-m", "unittest", "discover", "-s", "tests", "-p", "test_lonely_runner_*.py", "-v"]),
        ("inherited-exact", ["-m", "unittest", "tests.test_farey_gauss_defect", "tests.test_coverage_sieve_crt",
                             "tests.test_circle_transport", "tests.test_source_proof_certificate",
                             "tests.test_math_memory_graph", "tests.test_math_memory"]),
        ("published-controls", ["scripts/lonely_runner_certificates.py", "--output", str(destination / "certificates")]),
        ("uniform-rule", ["scripts/lonely_runner_uniform_probe.py", "--output", str(destination / "uniform.json")]),
        ("two-entry", ["scripts/lonely_runner_two_entry_probe.py", "--verify", str(PACKAGE / "receipts/gamma.json")]),
        ("dyadic-obstruction", ["scripts/lonely_runner_dyadic_probe.py", "--verify", str(PACKAGE / "receipts/dyadic-obstruction.json")]),
        ("arbitrary-phase", ["scripts/lonely_runner_phase_schedule_probe.py", "--verify", str(PACKAGE / "receipts/affinization.json")]),
    ):
        run(label, [py, *argv])
    for n in range(5, 21):
        run(f"census-{n}", [py, "scripts/lonely_runner_census.py", "--n", str(n),
                           "--max-domain-candidates", "25000000", "--verify",
                           str(PACKAGE / f"receipts/census-n{n}.json"),
                           "--certificate-dir", str(PACKAGE / "certificates")])
    run("independent-census", [py, "scripts/lonely_runner_census_independent.py",
                              "--max-n", "8", "--output", str(destination / "independent-census.json")])
    independent = destination / "independent-census.json"
    if not independent.exists() or independent.read_bytes() != (PACKAGE / "receipts/census-independent-5-8.json").read_bytes():
        failures.append("independent-census-drift")
    for name in ("bcs-five.json", "bcs-thirteen.json", "poliakova-n95.json", "verification.json"):
        actual = destination / "certificates" / name
        if not actual.exists() or actual.read_bytes() != (PACKAGE / "certificates" / name).read_bytes():
            failures.append("certificate-drift-" + name)
    uniform = destination / "uniform.json"
    if not uniform.exists() or uniform.read_bytes() != (PACKAGE / "BETA_UNIFORM_EXACT_RECEIPT.json").read_bytes():
        failures.append("uniform-receipt-drift")
    if args.full:
        run("full-native", [py, "-m", "unittest", "discover", "-s", "tests", "-p", "test_*.py"])
    for path, expected in manifest["source_hashes"].items():
        if hashlib.sha256((ROOT / path).read_bytes()).hexdigest() != expected:
            failures.append("source-changed-" + path)
    receipt = {"schema": "succ.lonely-runner.validation.v1", "python": sys.version,
               "commit_at_observation": subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip(),
               "source_manifest": manifest, "commands": records, "failures": failures,
               "status": "PASS" if not failures else "FAILED",
               "authority": "local executed gates; hosted and kernel observations are separate"}
    (destination / "validation.json").write_text(json.dumps(receipt, indent=2) + "\n")
    print(receipt["status"], len(records), "commands", flush=True)
    return bool(failures)


if __name__ == "__main__":
    raise SystemExit(main())
