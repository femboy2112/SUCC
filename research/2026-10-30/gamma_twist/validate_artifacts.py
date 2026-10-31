"""Verify scoped bytes and retained receipts; never certify mathematical truth."""
from __future__ import annotations

import argparse
import ast
import hashlib
import json
from pathlib import Path
import re
import subprocess

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
PARENT = "2b0628f52e9d88993c2e3ffa30b9748adfb781f0"
MANIFEST = HERE / "SOURCE_MANIFEST.json"
EXCLUDED = {"SOURCE_MANIFEST.json", "receipts/artifact-validation.json",
            "receipts/artifact-validation.log"}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def files() -> dict[str, Path]:
    return {str(p.relative_to(HERE)): p for p in sorted(HERE.rglob("*"))
            if p.is_file() and "__pycache__" not in p.parts
            and str(p.relative_to(HERE)) not in EXCLUDED}


def check_hash(path: Path, expected: str) -> None:
    assert path.is_file(), f"missing {path}"
    assert digest(path) == expected, f"hash mismatch {path}"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write-manifest", action="store_true")
    args = parser.parse_args()
    current = files()
    if args.write_manifest:
        manifest = {
            "parent_commit": PARENT,
            "branch": "research/gamma-twist-selected-phase-2026-10-30",
            "authority": "paper proofs and finite checks; shared-model review; no new Lean proof",
            "scope": "additions under research/2026-10-30/gamma_twist only",
            "exclusions": sorted(EXCLUDED) + ["__pycache__"],
            "input_audit": "receipts/source-audit.log",
            "related_live_refs": "receipts/refreshed_remote.json",
            "files": {name: {"sha256": digest(p), "bytes": p.stat().st_size}
                      for name, p in current.items()},
        }
        MANIFEST.write_text(json.dumps(manifest, indent=2) + "\n")
    manifest = json.loads(MANIFEST.read_text())
    assert set(manifest["files"]) == set(current), "artifact inventory changed"
    for name, item in manifest["files"].items():
        check_hash(current[name], item["sha256"])
        assert current[name].stat().st_size == item["bytes"]

    counts = {"artifact_files": len(current), "python_asts": 0,
              "json_files": 1, "local_links": 0, "receipt_hashes": 0,
              "source_input_hashes": 0, "nested_artifact_hashes": 0}
    failures = []
    for name, p in current.items():
        if p.suffix == ".py":
            ast.parse(p.read_text(), filename=name)
            counts["python_asts"] += 1
        if p.suffix == ".md":
            for link in re.findall(r"\[[^\]]+\]\(([^\s)]+)\)", p.read_text()):
                if "://" in link or link.startswith(("#", "mailto:")):
                    continue
                target = link.split("#", 1)[0]
                assert (p.parent / target).exists(), f"broken link {name}: {link}"
                counts["local_links"] += 1
        if p.suffix != ".json":
            continue
        data = json.loads(p.read_text())
        counts["json_files"] += 1
        rows = data if isinstance(data, list) else [data]
        for row in rows:
            if not isinstance(row, dict) or "exit_code" not in row:
                continue
            if "log_sha256" in row:
                target = p.with_suffix(".log")
                expected = row["log_sha256"]
            elif "output" in row and "sha256" in row:
                target = p.parent / row["output"]
                if not target.exists() and target.name == "approximate_grid_receipt.json":
                    target = p.parent / "approximate_grid_failed.log"
                expected = row["sha256"]
            else:
                continue
            check_hash(target, expected)
            counts["receipt_hashes"] += 1
            if row["exit_code"] != 0:
                failures.append(name)

    expected_failures = {"receipts/math-catalog.json", "receipts/baseline-catalog.json",
        "gauss/extra_command_receipts.json", "signed/command_receipts.grids.json",
        "signed/command_receipts-with-grids.tests.json"}
    assert set(failures) == expected_failures, f"unexpected failed receipts: {failures}"

    for scope in ("gauss", "signed", "geometry"):
        data = json.loads((HERE / scope / "SOURCE_MANIFEST.json").read_text())
        for name, item in data.get("files", data.get("artifact_files", {})).items():
            check_hash(HERE / scope / name, item["sha256"])
            counts["nested_artifact_hashes"] += 1
        inputs = data.get("source_inputs", data.get("source_inputs_actually_read", []))
        if isinstance(inputs, dict):
            inputs = [{"path": name, "sha256": sha} for name, sha in inputs.items()]
        for item in inputs:
            commit = item.get("commit", PARENT)
            raw = subprocess.check_output(["git", "show", f"{commit}:{item['path']}"], cwd=ROOT)
            assert hashlib.sha256(raw).hexdigest() == item["sha256"], item["path"]
            if "git_blob" in item:
                blob = hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()
                assert blob == item["git_blob"], item["path"]
            counts["source_input_hashes"] += 1
        for item in data.get("current_campaign_review_inputs", []):
            check_hash(ROOT / item["path"], item["sha256"])

    subprocess.run(["git", "diff", "--check"], cwd=ROOT, check=True)
    print(json.dumps({"status": "PASS", "counts": counts,
          "preserved_expected_failed_receipts": sorted(failures),
          "authority": "byte/structure/provenance validation only"}, indent=2))


if __name__ == "__main__":
    main()
