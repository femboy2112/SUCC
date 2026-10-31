"""Run declared audit commands with raw, separately attributable receipts.

No result in this file is precomputed. Run with the repository test dependencies.
"""
from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
import hashlib
import importlib.metadata
import json
from pathlib import Path
import subprocess
import sys
import time

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
PARENT = ROOT / "research/2026-10-30/universal_nz_carrier"


def run_one(name, args):
    out = HERE / "receipts"
    out.mkdir(exist_ok=True)
    started = datetime.now(timezone.utc).isoformat()
    clock = time.monotonic()
    proc = subprocess.run([sys.executable, *args], cwd=ROOT,
                          stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    raw = proc.stdout
    (out / (name + ".log")).write_bytes(raw)
    receipt = {"name": name, "command": [sys.executable, *args],
               "cwd": str(ROOT), "started_utc": started,
               "elapsed_seconds": round(time.monotonic() - clock, 3),
               "returncode": proc.returncode,
               "log_sha256": hashlib.sha256(raw).hexdigest(),
               "log": name + ".log"}
    (out / (name + ".json")).write_text(json.dumps(receipt, indent=2) + "\n")
    return receipt


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--scope", choices=["baseline", "focused", "native_recovery"], default="baseline")
    scope = parser.parse_args().scope
    if scope == "baseline":
        commands = {
            "source_provenance": ["scripts/verify_provenance.py"],
            "native_unittest": ["-m", "unittest", "discover", "-s", "tests", "-p", "test_*.py"],
            "observer_foundations": ["scripts/observer_foundations_probe.py"],
            "ordinal_succ": ["scripts/ordinal_succ_report_probe.py"],
            "parent_focused": ["-m", "unittest", "discover", "-s", str(PARENT), "-p", "test_*.py", "-v"],
        }
        for stem in ["independent_oracle", "logjet_independent_oracle", "zeta_allgrade_oracle",
                     "zeta_tangent_independent_oracle", "bbp_twisted_zeta_independent_oracle"]:
            commands["parent_" + stem] = [str(PARENT / (stem + ".py"))]
    elif scope == "native_recovery":
        commands = {
            "recovered_meta_choice_descent": ["-m", "unittest", "discover", "-s", "tests",
                                              "-p", "test_eodcs_meta_choice_descent.py", "-v"],
            "recovered_round2_registry": ["-m", "unittest", "discover", "-s", "tests",
                                          "-p", "test_round2_registry.py", "-v"],
        }
    else:
        commands = {"focused": ["-m", "unittest", "discover", "-s", str(HERE), "-p", "test_*.py", "-v"]}
    results = []
    print(json.dumps({"scope": scope, "python": sys.version,
                      "versions": {k: importlib.metadata.version(k)
                                   for k in ["sympy", "mpmath", "numpy", "scipy"]}}), flush=True)
    with ThreadPoolExecutor(max_workers=3) as pool:
        futures = [pool.submit(run_one, name, args) for name, args in commands.items()]
        for future in as_completed(futures):
            result = future.result()
            results.append(result)
            print(json.dumps(result), flush=True)
    summary = {"scope": scope, "all_returncodes_zero": all(r["returncode"] == 0 for r in results),
               "results": sorted(results, key=lambda r: r["name"])}
    (HERE / "receipts" / (scope + "_summary.json")).write_text(json.dumps(summary, indent=2) + "\n")
    return 0 if summary["all_returncodes_zero"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
