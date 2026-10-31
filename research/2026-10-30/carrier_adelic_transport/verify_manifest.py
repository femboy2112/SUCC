"""Verify frozen research artifacts and available pinned input files.

Use --write only when intentionally freezing a revised research package.
The manifest excludes itself and interpreter caches, and covers all other
files below this directory, including the receipts and this verifier.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
MANIFEST = HERE / "MANIFEST.json"


def files():
    return sorted(p for p in HERE.rglob("*")
                  if p.is_file() and p != MANIFEST
                  and "__pycache__" not in p.parts and p.suffix != ".pyc")


def record(path):
    raw = path.read_bytes()
    return {"path": str(path.relative_to(HERE)), "bytes": len(raw),
            "sha256": hashlib.sha256(raw).hexdigest()}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    current = [record(p) for p in files()]
    if args.write:
        MANIFEST.write_text(json.dumps({
            "schema": "succ.research.artifact-manifest.v1",
            "parent_commit": "1c6ce7d7ee83a0bd751bde8092e46ff798855fd3",
            "scope": "All package files except this manifest and Python caches.",
            "files": current,
        }, indent=2) + "\n")
    frozen = json.loads(MANIFEST.read_text())
    expected = {r["path"]: r for r in frozen["files"]}
    actual = {r["path"]: r for r in current}
    problems = []
    for name in sorted(set(expected) | set(actual)):
        if expected.get(name) != actual.get(name):
            problems.append("artifact mismatch: " + name)
    inputs = json.loads((HERE / "SOURCE_INPUTS.json").read_text())
    present = 0
    external = 0
    for entry in inputs["files"]:
        candidate = ROOT / entry["path"]
        if not candidate.is_file():
            external += 1
            continue
        digest = hashlib.sha256(candidate.read_bytes()).hexdigest()
        if digest != entry["sha256"]:
            problems.append("input mismatch: " + entry["path"])
        present += 1
    print(json.dumps({"status": "FAIL" if problems else "PASS",
                      "artifact_files": len(current),
                      "available_input_files_checked": present,
                      "external_input_files_pinned_not_materialized": external,
                      "problems": problems}, indent=2))
    return int(bool(problems))


if __name__ == "__main__":
    raise SystemExit(main())
