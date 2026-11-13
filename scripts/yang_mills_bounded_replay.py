#!/usr/bin/env python3
"""Replay a bounded, explicitly non-endpoint slice of the pinned YM submission.

Requires an existing yang-mills-group/YM checkout and a local Lean 4.32.0
toolchain. Does not download, update dependencies, or build the full package.
The output directory contains logs/receipts and temporary Lean build products;
only text/JSON receipts should be committed.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile


UPSTREAM_HEAD = "55ba9fc36293b3f4d52c6b1f813169a0be76ee98"
SOURCE_SHA256 = "e3b65f4eb934fe60668bfe6642abe6314cfcc73a90efe22cc7cd3378e9c50912"
LEAN_VERSION = "version 4.32.0,"
LEAN_COMMIT = "8c9756b28d64dab099da31a4c09229a9e6a2ef35"
LEAN_ARCHIVE_SHA256 = "fca846f3588724a38ad19ee40292c67cb7438d7555903372e3308eef795ba516"
DOSSIER = Path("research/2026-11-13/yang_mills_succ/coupled_wilson")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--upstream", type=Path, required=True)
    parser.add_argument("--lean", type=Path, required=True)
    parser.add_argument("--toolchain-archive", type=Path,
                        help="Optionally verify the downloaded official Linux x86_64 release archive")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    upstream = args.upstream.resolve()
    lean = args.lean.resolve()
    output = (args.output or Path(tempfile.mkdtemp(prefix="ym-bounded-"))).resolve()
    output.mkdir(parents=True, exist_ok=True)
    build = output / "build"
    build.mkdir(exist_ok=True)
    package = upstream / "submissions/openai-20261028"
    source_root = package / "submission"
    source = source_root / "YM/UVExtension/Orchard/Barrel.lean"
    repo = Path(__file__).resolve().parents[1]
    fixtures = repo / DOSSIER / "formal"
    env = dict(os.environ)
    env["PATH"] = str(lean.parent) + os.pathsep + env.get("PATH", "")
    env["LEAN_PATH"] = str(build)
    receipt = {
        "scope": "Upstream integrity/text correspondence, one proof-transport generator, "
        "new positive/negative controls, and a finite rational Gram certificate. "
        "No Yang-Mills endpoint, Comparator, or full dependency graph is compiled.",
        "upstream_head_expected": UPSTREAM_HEAD,
        "lean_archive_sha256_expected": LEAN_ARCHIVE_SHA256,
        "lean_archive_url": "https://github.com/leanprover/lean4/releases/download/v4.32.0/lean-4.32.0-linux.tar.zst",
        "steps": [],
        "status": "running",
    }

    def run(label: str, command: list[str], cwd: Path, expected: int = 0,
            required_output: str | None = None) -> subprocess.CompletedProcess:
        result = subprocess.run(command, cwd=cwd, env=env, text=True,
                                capture_output=True, timeout=180)
        (output / f"{label}.stdout.txt").write_text(result.stdout)
        (output / f"{label}.stderr.txt").write_text(result.stderr)
        step = {
            "label": label, "command": command, "cwd": str(cwd),
            "exit_code": result.returncode, "expected_exit_code": expected,
            "stdout": result.stdout, "stderr": result.stderr,
        }
        receipt["steps"].append(step)
        if result.returncode != expected:
            raise RuntimeError(f"{label}: exit {result.returncode}, expected {expected}")
        if required_output and required_output not in result.stdout + result.stderr:
            raise RuntimeError(f"{label}: expected diagnostic absent: {required_output!r}")
        return result

    try:
        if args.toolchain_archive:
            receipt["lean_archive_sha256_actual"] = sha256(args.toolchain_archive.resolve())
            if receipt["lean_archive_sha256_actual"] != LEAN_ARCHIVE_SHA256:
                raise RuntimeError("Lean release archive hash mismatch")
        head = run("upstream_head", ["git", "rev-parse", "HEAD"], upstream).stdout.strip()
        receipt["upstream_head_actual"] = head
        if head != UPSTREAM_HEAD:
            raise RuntimeError("Upstream HEAD differs from pinned assessment")
        version = run("lean_version", [str(lean), "--version"], output).stdout.strip()
        if LEAN_VERSION not in version or LEAN_COMMIT not in version:
            raise RuntimeError("Lean version/commit differs from the pinned release")
        receipt["source_sha256"] = sha256(source)
        if receipt["source_sha256"] != SOURCE_SHA256:
            raise RuntimeError("Upstream proof-transport source hash mismatch")
        run("upstream_integrity", [sys.executable, str(package / "scripts/verify.py"),
            "integrity", "--run-dir", str(output / "integrity")], package)
        receipt["upstream_integrity"] = json.loads(
            (output / "integrity/result.json").read_text())
        if receipt["upstream_integrity"].get("status") != "passed":
            raise RuntimeError("Upstream integrity receipt did not report passed")

        object_file = build / "YM/UVExtension/Orchard/Barrel.olean"
        object_file.parent.mkdir(parents=True, exist_ok=True)
        run("upstream_generator", [str(lean), "-DwarningAsError=true", "-o",
            str(object_file), str(source)], source_root)

        receipt["fixtures_sha256"] = {}
        for name in ("ValidTransport.lean", "InvalidTransport.lean", "WilsonTaylorNegative.lean"):
            path = fixtures / name
            receipt["fixtures_sha256"][name] = sha256(path)
            shutil.copyfile(path, build / name)
        result = run("valid_transport", [str(lean), "-DwarningAsError=true", "-o",
            str(build / "ValidTransport.olean"), str(build / "ValidTransport.lean")],
            build, required_output="does not depend on any axioms")
        run("invalid_transport", [str(lean), "-DwarningAsError=true",
            str(build / "InvalidTransport.lean")], build, 1,
            "(kernel) declaration type mismatch")
        result = run("rational_gram_certificate", [str(lean), "-DwarningAsError=true", "-o",
            str(build / "WilsonTaylorNegative.olean"), str(build / "WilsonTaylorNegative.lean")],
            build, required_output="SUCC.WilsonTaylor.not_positive_semidefinite")
        dependencies = re.findall(r"depends on axioms: \[([^\]]*)\]", result.stdout)
        if len(dependencies) != 5:
            raise RuntimeError("Expected five explicit rational-certificate axiom reports")
        allowed = {"propext", "Classical.choice", "Quot.sound"}
        for dependency_list in dependencies:
            if set(filter(None, (name.strip() for name in dependency_list.split(",")))) - allowed:
                raise RuntimeError("Unapproved axiom in rational certificate")
        mutation = (build / "WilsonTaylorNegative.lean").read_text().replace(
            "quadratic witness = -71 / 512", "quadratic witness = 71 / 512")
        (build / "WrongSign.lean").write_text(mutation)
        run("wrong_sign_control", [str(lean), "-DwarningAsError=true", str(build / "WrongSign.lean")],
            build, 1, "Tactic `decide`")
        receipt["source_sha256_after"] = sha256(source)
        if receipt["source_sha256_after"] != SOURCE_SHA256:
            raise RuntimeError("Upstream source changed during replay")
        receipt["status"] = "passed"
    except (OSError, RuntimeError, subprocess.TimeoutExpired) as error:
        receipt["status"] = "failed"
        receipt["error"] = str(error)
    (output / "result.json").write_text(json.dumps(receipt, indent=2) + "\n")
    print(json.dumps({"status": receipt["status"], "receipt": str(output / "result.json")}, indent=2))
    return 0 if receipt["status"] == "passed" else 1


if __name__ == "__main__":
    raise SystemExit(main())
