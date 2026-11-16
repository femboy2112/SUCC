#!/usr/bin/env python3
"""Replay XXVI research-local tests and selected load-bearing standalone audits.

Native tests and Main XXIV/XXV have separate mandatory runners. Research test
directories run in separate processes to avoid same-named module collisions.
Auditors which write historical receipt filenames run in an exported copy of
the exact candidate. Raw outputs stay outside the checkout.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.metadata
import json
import os
from pathlib import Path
import platform
import re
import subprocess
import sys
import tarfile
import time

ROOT = Path(__file__).resolve().parents[1]
BASE = "db9fb4b84672050efa79b13377f1e73364598a14"
DIRECT = (
    "research/2026-11-15/compiled_knowledge_probe/exact_probe.py",
    "scripts/main_xxvi_source_phase_probe.py",
    "scripts/main_xxvi_observer_transport_probe.py",
)
EXPORTED = (
    "research/2026-11-15/three_count_hail_mary/independent_audit.py",
    "research/2026-11-15/bbp_gamma_mellin_phase_bridge/independent_audit.py",
)


def git(*args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()


def changed_paths(head: str) -> list[str]:
    return git("diff", "--name-only", "--diff-filter=ACMR", BASE, head).splitlines()


def research_test_dirs(paths: list[str]) -> list[str]:
    return sorted({str(Path(p).parent) for p in paths
                   if p.startswith("research/") and Path(p).name.startswith("test_")
                   and p.endswith(".py")})


def export_candidate(head: str, out: Path) -> Path:
    destination = out / "auditor_candidate"
    destination.mkdir()
    archive = out / "candidate.tar"
    with archive.open("wb") as stream:
        subprocess.run(["git", "archive", head], cwd=ROOT, stdout=stream, check=True)
    with tarfile.open(archive) as bundle:
        for member in bundle.getmembers():
            target = (destination / member.name).resolve()
            if not target.is_relative_to(destination):
                raise ValueError("unsafe archive member")
            # The authenticated candidate has no links. Reject rather than
            # materialize a future unreviewed link; works on Python 3.10 too.
            if member.issym() or member.islnk() or member.isdev():
                raise ValueError("unexpected link or device in candidate export")
        bundle.extractall(destination)
    archive.unlink()
    return destination


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", required=True, type=Path)
    parser.add_argument("--timeout", type=int, default=1800, help="per invocation seconds")
    args = parser.parse_args()
    out = args.out.resolve()
    if out == ROOT or ROOT in out.parents:
        parser.error("receipts must be outside the checkout")
    if args.timeout <= 0:
        parser.error("timeout must be positive")
    if git("status", "--porcelain", "--untracked-files=no"):
        parser.error("tracked candidate must be clean")
    out.mkdir(parents=True, exist_ok=True)
    if (out / "receipt.json").exists() or (out / "auditor_candidate").exists():
        parser.error("use a new output directory to preserve previous receipts")
    head, tree = git("rev-parse", "HEAD"), git("rev-parse", "HEAD^{tree}")
    paths = changed_paths(head)
    dirs = research_test_dirs(paths)
    entries = [("research-tests-" + str(i + 1),
                ["-W", "error", "-m", "unittest", "discover", "-s", folder,
                 "-p", "test_*.py", "-v"], ROOT)
               for i, folder in enumerate(dirs)]
    for path in DIRECT:
        if not (ROOT / path).is_file():
            parser.error(f"missing explicit entrypoint: {path}")
        try:
            expected = git("rev-parse", f"{head}:{path}")
        except subprocess.CalledProcessError:
            parser.error(f"explicit entrypoint not present in committed candidate: {path}")
        if git("hash-object", path) != expected:
            parser.error(f"explicit entrypoint differs from committed candidate: {path}")
        entries.append((Path(path).stem, [path], ROOT))
    mirror = export_candidate(head, out)
    for path in EXPORTED:
        if not (mirror / path).is_file():
            parser.error(f"missing exported entrypoint: {path}")
        entries.append((Path(path).parent.name + "-independent-audit", [path], mirror))
    env = dict(os.environ, PYTHONPATH=str(ROOT), OPENBLAS_NUM_THREADS="1", OMP_NUM_THREADS="1")
    results = []
    for name, argv, cwd in entries:
        start = time.monotonic()
        log = out / (name + ".log")
        command = [sys.executable, *argv]
        actual_env = dict(env, PYTHONPATH=str(cwd))
        timed_out = False
        with log.open("w") as stream:
            try:
                proc = subprocess.run(command, cwd=cwd, env=actual_env,
                                      stdout=stream, stderr=subprocess.STDOUT,
                                      timeout=args.timeout, check=False)
                code = proc.returncode
            except subprocess.TimeoutExpired:
                code, timed_out = 124, True
                stream.write(f"\nRUNNER TIMEOUT after {args.timeout} seconds\n")
        text = log.read_text(errors="replace")
        counts = re.findall(r"Ran (\d+) tests? in", text)
        results.append({"name": name, "command": command,
                        "cwd_kind": "exact_candidate" if cwd == ROOT else "exported_exact_candidate",
                        "exit_code": code, "timed_out": timed_out,
                        "seconds": round(time.monotonic() - start, 3),
                        "unittest_count": int(counts[-1]) if counts else None,
                        "log": log.name, "sha256": hashlib.sha256(log.read_bytes()).hexdigest()})
        print(name, code, flush=True)
    unchanged = head == git("rev-parse", "HEAD") and not git("status", "--porcelain", "--untracked-files=no")
    invoked = set(DIRECT) | set(EXPORTED)
    candidates = sorted(p for p in paths if p.startswith("research/") and p.endswith(".py")
                        and not Path(p).name.startswith(("test_", "__init__")) and p not in invoked)
    versions = {}
    for package in ("mpmath", "numpy", "scipy", "sympy"):
        try:
            versions[package] = importlib.metadata.version(package)
        except importlib.metadata.PackageNotFoundError:
            versions[package] = None
    passed = unchanged and all(row["exit_code"] == 0 for row in results)
    receipt = {"head": head, "tree": tree, "baseline": BASE,
               "environment": {"python": sys.version, "platform": platform.platform(),
                               "libc": platform.libc_ver(), "dependencies": versions,
                               "PYTHONPATH": "candidate root", "OPENBLAS_NUM_THREADS": "1", "OMP_NUM_THREADS": "1"},
               "commands": results, "research_test_directories": dirs,
               "unittest_executions": sum(r["unittest_count"] or 0 for r in results),
               "other_changed_research_python_candidates_not_invoked": candidates,
               "coverage_boundary": "All changed research-local test directories and five explicit standalone entrypoints; inventory candidates may be libraries, CLI generators, historical wrappers or additional unrun probes. Native, XXIV/XXV and Lean are separate gates.",
               "exported_auditor_writes_preserved": "auditor_candidate/",
               "tracked_candidate_unchanged": unchanged,
               "authority": "finite implementation and certificate replay; no universal proof promotion",
               "status": "PASS" if passed else "FAIL"}
    (out / "receipt.json").write_text(json.dumps(receipt, indent=2) + "\n")
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
