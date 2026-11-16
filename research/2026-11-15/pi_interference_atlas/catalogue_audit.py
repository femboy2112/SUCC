#!/usr/bin/env python3
"""Audit the declared catalogue and pin its inherited source inventory.

This checks schema, links, source versions and frozen-code identity. It does
not turn the finite inventory into a proof of universal literature coverage,
or independently prove every inherited theorem mentioned by a catalogue row.
"""
from __future__ import annotations

import argparse
from collections import Counter
from hashlib import sha256
import json
from pathlib import Path
import subprocess


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
PARENT = "8097d9e802da1d83a615d8812e74279820f5ae7e"
RELATIONS = {"EQUIVALENT", "NECESSARY", "SUFFICIENT", "STRICTLY_STRONGER",
             "OBSERVER_ONLY", "AUXILIARY", "SEPARATE"}
REPRESENTATIONS = {"direct finite response", "conditional",
                   "limit with certified truncation", "outside grammar"}
CORE = ("AGENTS.md", "docs/METHOD.md", "docs/PI_NORMALITY_FRONTIER.md",
        "docs/PI_FRONTIER_CONTRACT.md", "docs/MAIN_XXV_HANDOFF.md",
        "research/2026-11-15/pi_carrier_collision/THEOREMS.md")


def git(*args: str) -> bytes:
    return subprocess.check_output(["git", *args], cwd=ROOT)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out-dir", type=Path, default=HERE / "receipts")
    args = parser.parse_args()
    raw = (HERE / "FRONTIER_TARGETS.json").read_bytes()
    data = json.loads(raw)
    assert data["schema_version"] == 1 and data["parent_commit"] == PARENT
    rows = data["targets"]
    assert [r["id"] for r in rows] == [f"F{i:02d}" for i in range(1, 75)]
    assert data["coverage_count"] == len(rows) == 74
    mapping = (HERE / "FRONTIER_MAP.md").read_bytes()
    assert sha256(mapping).hexdigest() == data["frontier_map_sha256"]
    mapping_text = mapping.decode("utf-8")
    fields = ("title", "exact_target", "response_construction", "quantifiers",
              "logical_relation_explanation", "unpaid_obligation")
    source_ids: dict[str, list[str]] = {}
    for row in rows:
        assert all(isinstance(row[f], str) and row[f].strip() for f in fields)
        assert row["logical_relation"] in RELATIONS
        assert row["implementation_scope"] in REPRESENTATIONS
        assert row["controls"] and all(isinstance(x, str) and x.strip() for x in row["controls"])
        assert isinstance(row["superseded_or_error_flags"], list)
        assert f"| {row['id']} |" in mapping_text
        assert row["source_paths"]
        for name in row["source_paths"]:
            path = Path(name)
            assert not path.is_absolute() and ".." not in path.parts
            source_ids.setdefault(name, []).append(row["id"])
    assert data["source_path_count"] == len(source_ids) == 42
    inherited = []
    for name in sorted(set(source_ids) | set(CORE)):
        content = git("show", f"{PARENT}:{name}")
        assert (ROOT / name).read_bytes() == content, f"Inherited source changed: {name}"
        inherited.append({"path": name,
                          "parent_git_blob": git("rev-parse", f"{PARENT}:{name}").decode().strip(),
                          "sha256": sha256(content).hexdigest(),
                          "catalogue_ids": source_ids.get(name, [])})
    snapshot = json.loads((HERE / "receipts" / "full_snapshot.json").read_text())
    assert snapshot["parent"] == PARENT
    for name, expected in snapshot["production_and_test_sha256"].items():
        assert sha256((ROOT / name).read_bytes()).hexdigest() == expected, name
    result = {"status": "PASS", "parent_commit": PARENT,
              "catalogue_sha256": sha256(raw).hexdigest(),
              "map_sha256": sha256(mapping).hexdigest(),
              "audit_script_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
              "coverage_count": len(rows), "mapped_source_paths": len(source_ids),
              "total_inherited_paths_pinned": len(inherited),
              "relation_counts": dict(sorted(Counter(r["logical_relation"] for r in rows).items())),
              "representation_counts": dict(sorted(Counter(r["implementation_scope"] for r in rows).items())),
              "source_version_checks": "All mapped and core inputs equal their parent Git blobs.",
              "frozen_code_checks": "All six production/test hashes match the integrated-suite snapshot.",
              "scope": "Finite declared catalogue integrity; representation is not implementation; relation counts include explicitly scoped weaker targets."}
    args.out_dir.mkdir(parents=True, exist_ok=True)
    (args.out_dir / "inherited_blobs.json").write_text(json.dumps({"parent_commit": PARENT, "files": inherited}, indent=2) + "\n")
    (args.out_dir / "catalogue.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
