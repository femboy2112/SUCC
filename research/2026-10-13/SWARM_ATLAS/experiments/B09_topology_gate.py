#!/usr/bin/env python3
"""Replay B09's pinned topology gate without downloading or building dependencies."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import resource
import re
import signal
import subprocess
import tempfile
import time


MATHLIB_COMMIT = "4bbdccd9c5f862bf90ff12f0a9e2c8be032b9a84"
RSS_LIMIT_MIB = 1280
MIN_SYSTEM_AVAILABLE_MIB = 768
FORMAL_FILES = (
    "formal/SWM_A01_BaseChange.lean",
    "formal/SWM_C19_FiniteHeight.lean",
    "formal/SWM_X07_DirectedHeight.lean",
    "formal/SWM_B09_InverseFamilies.lean",
    "formal/SWM_B09_TopologicalCompletion.lean",
)
TOPOLOGY_MODULES = (
    "Mathlib.Topology.Constructions",
    "Mathlib.Topology.Separation.Basic",
    "Mathlib.Topology.Homeomorph",
)


def run_readonly(command: list[str], cwd: Path | None = None) -> str:
    return subprocess.run(command, cwd=cwd, capture_output=True, text=True,
                          check=True, timeout=30).stdout.strip()


def cap_compiler() -> None:
    resource.setrlimit(resource.RLIMIT_AS, (4 * 1024**3, 4 * 1024**3))


def process_tree_rss_kib(pid: int) -> int:
    pending = [pid]
    total = 0
    while pending:
        current = pending.pop()
        try:
            status = Path(f"/proc/{current}/status").read_text()
            for line in status.splitlines():
                if line.startswith("VmRSS:"):
                    total += int(line.split()[1])
            children = Path(f"/proc/{current}/task/{current}/children").read_text()
            pending.extend(int(child) for child in children.split())
        except FileNotFoundError:
            pass
    return total


def bounded_compile(command: list[str], root: Path, environment: dict[str, str],
                    scratch: Path, timeout_seconds: float = 120) -> dict:
    started = time.monotonic()
    peak = 0
    minimum_available = None
    reason = None
    with tempfile.TemporaryFile(mode="w+", dir=scratch) as stdout, \
            tempfile.TemporaryFile(mode="w+", dir=scratch) as stderr:
        process = subprocess.Popen(command, cwd=root, env=environment,
                                   stdout=stdout, stderr=stderr,
                                   preexec_fn=cap_compiler, start_new_session=True)
        while process.poll() is None:
            peak = max(peak, process_tree_rss_kib(process.pid))
            available = next(int(line.split()[1]) for line in Path("/proc/meminfo").read_text()
                             .splitlines() if line.startswith("MemAvailable:"))
            minimum_available = available if minimum_available is None else min(
                minimum_available, available)
            if peak > RSS_LIMIT_MIB * 1024:
                reason = "RESIDENT MEMORY CAP"
            elif available < MIN_SYSTEM_AVAILABLE_MIB * 1024:
                reason = "SYSTEM MEMORY HEADROOM CAP"
            elif time.monotonic() - started > timeout_seconds:
                reason = "TIMEOUT"
            if reason:
                os.killpg(process.pid, signal.SIGTERM)
                try:
                    process.wait(timeout=2)
                except subprocess.TimeoutExpired:
                    os.killpg(process.pid, signal.SIGKILL)
                    process.wait()
                break
            time.sleep(0.1)
        stdout.seek(0)
        stderr.seek(0)
        return {
            "command": command, "exit_code": reason or process.returncode,
            "stdout": stdout.read(), "stderr": stderr.read(),
            "elapsed_seconds": round(time.monotonic() - started, 4),
            "observed_process_tree_peak_rss_kib": peak,
            "minimum_system_available_memory_kib": minimum_available,
        }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--lean", type=Path, required=True)
    parser.add_argument("--mathlib-dir", type=Path, required=True)
    parser.add_argument("--receipt", type=Path, default=Path(
        "research/2026-10-13/SWARM_ATLAS/receipts/B09_topology.json"))
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[4]
    lean = args.lean.absolute()
    mathlib = args.mathlib_dir.resolve()
    if (root / "lean-toolchain").read_text().strip() != "leanprover/lean4:v4.14.0":
        raise SystemExit("Integration pin differs from Lean 4.14.0")
    if run_readonly(["git", "rev-parse", "HEAD"], mathlib) != MATHLIB_COMMIT:
        raise SystemExit("Mathlib checkout differs from the verified v4.14.0 commit")
    run_readonly(["git", "diff", "--exit-code", "--", "Mathlib", "lakefile.lean",
                  "lake-manifest.json", "lean-toolchain"], mathlib)
    version = run_readonly([str(lean), "--version"])
    if "version 4.14.0," not in version:
        raise SystemExit("Compiler differs from Lean 4.14.0")

    local_lib = root / ".swm-tools" / "proofs"
    local_lib.mkdir(parents=True, exist_ok=True)
    search_roots = [local_lib, mathlib / ".lake/build/lib", mathlib / ".lake/build/lib/lean"]
    manifest = json.loads((mathlib / "lake-manifest.json").read_text())
    package_versions = {}
    for package in manifest["packages"]:
        directory = mathlib / manifest["packagesDir"] / package["name"]
        actual = run_readonly(["git", "rev-parse", "HEAD"], directory)
        if actual != package["rev"]:
            raise SystemExit(f"Unpinned dependency: {package['name']}")
        package_versions[package["name"]] = actual
        run_readonly(["git", "diff", "--exit-code"], directory)
        search_roots.extend([directory / ".lake/build/lib", directory / ".lake/build/lib/lean"])
    environment = os.environ.copy()
    environment["LEAN_PATH"] = ":".join(str(path) for path in search_roots if path.is_dir())
    current_sources = {
        path: hashlib.sha256((root / path).read_bytes()).hexdigest() for path in FORMAL_FILES
    }
    for path in FORMAL_FILES:
        code = (root / path).read_text().split("\nnamespace ", 1)[1]
        for forbidden in ("sorry", "admit", "axiom ", "unsafe "):
            if forbidden in code:
                raise SystemExit(f"Forbidden proof placeholder/declaration in {path}: {forbidden}")

    receipt_path = args.receipt if args.receipt.is_absolute() else root / args.receipt
    receipt = json.loads(receipt_path.read_text()) if receipt_path.exists() else {
        "assignment": "SWM-B09", "attempts": []}
    attempt = {
        "compiler": version,
        "mathlib_commit": MATHLIB_COMMIT,
        "dependency_commits": package_versions,
        "mathlib_manifest_sha256": hashlib.sha256(
            (mathlib / "lake-manifest.json").read_bytes()).hexdigest(),
        "direct_topology_import_sha256": {
            module: {
                "source": hashlib.sha256(
                    (mathlib / (module.replace(".", "/") + ".lean")).read_bytes()).hexdigest(),
                "compiled_olean": hashlib.sha256(
                    (mathlib / ".lake/build/lib" /
                     (module.replace(".", "/") + ".olean")).read_bytes()).hexdigest(),
            } for module in TOPOLOGY_MODULES
        },
        "source_sha256": current_sources,
        "lean_path": environment["LEAN_PATH"],
        "compiler_virtual_limit_bytes": 4 * 1024**3,
        "compiler_resident_limit_bytes": RSS_LIMIT_MIB * 1024**2,
        "minimum_system_available_bytes": MIN_SYSTEM_AVAILABLE_MIB * 1024**2,
        "lean_allocation_limit_mib": 2048,
        "watchdog_poll_seconds": 0.1,
        "compiler_timeout_seconds": 120,
        "checks": [],
        "status": "RUNNING",
    }
    receipt["attempts"].append(attempt)
    failed = False
    calibration = local_lib / "B09_ImportCalibration.lean"
    calibration.write_text("import Mathlib.Topology.Constructions\n"
                           "import Mathlib.Topology.Separation.Basic\n"
                           "import Mathlib.Topology.Homeomorph\n"
                           "#check closure\n#check Homeomorph\n#check IsCompact.isClosed\n")
    inputs = (str(calibration),) + FORMAL_FILES
    for path in inputs:
        target = local_lib / (Path(path).stem + ".olean")
        command = [str(lean), "-j1", "-M2048", "-o", str(target), path]
        record = bounded_compile(command, root, environment, local_lib)
        if record["exit_code"] == 0:
            declared_axioms = {
                name.strip() for axioms in re.findall(r"axioms:\s*\[([^]]*)\]",
                                                      record["stdout"])
                for name in axioms.split(",")
            }
            record["printed_axiom_dependencies"] = sorted(declared_axioms)
            if not declared_axioms <= {"propext", "Quot.sound", "Classical.choice"}:
                record["exit_code"] = "UNEXPECTED AXIOM"
        attempt["checks"].append(record)
        if record["exit_code"] != 0:
            failed = True
            break
    attempt["maximum_child_rss_kib"] = resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss
    attempt["status"] = "COMPILE FAILED" if failed else "LEAN-KERNEL PROVED"
    receipt["latest_status"] = attempt["status"]
    receipt_path.parent.mkdir(parents=True, exist_ok=True)
    receipt_path.write_text(json.dumps(receipt, indent=2) + "\n")
    print(f"{attempt['status']}; maximum child RSS {attempt['maximum_child_rss_kib']} KiB")
    print(f"Receipt: {receipt_path}")
    if failed:
        print(attempt["checks"][-1]["stdout"])
        print(attempt["checks"][-1]["stderr"])
        raise SystemExit(1)


if __name__ == "__main__":
    main()
