#!/usr/bin/env python3
"""Bind Main XXVI donor ancestry, source bytes and declared integration repairs.

Generate only after committing all source/document changes; then commit the
manifest and regenerate the catalog. Neither file contains its own final hash.
This verifies provenance and assembly, not the truth of mathematical proofs.
"""
from __future__ import annotations

import argparse
from functools import lru_cache
import json
from pathlib import Path
import subprocess

BASE = "db9fb4b84672050efa79b13377f1e73364598a14"
DEFAULT_MANIFEST = "docs/SUCC_MAIN_XXVI_INTEGRATION_MANIFEST_2026-11-16.json"
CATALOG = "docs/math_memory/CLAIM_CATALOG.json"
EXPECTED_PRS = {600, 601, *range(604, 656)}


def git(*args: str) -> str:
    return subprocess.check_output(["git", *args], text=True).strip()


def ancestor(old: str, new: str) -> bool:
    return subprocess.run(["git", "merge-base", "--is-ancestor", old, new],
                          stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode == 0


@lru_cache(maxsize=None)
def tree(ref: str) -> dict[str, dict[str, str]]:
    raw = subprocess.check_output(["git", "ls-tree", "-rz", ref])
    result = {}
    for entry in raw.split(b"\0"):
        if not entry:
            continue
        meta, path = entry.split(b"\t", 1)
        mode, kind, sha = meta.decode().split()
        result[path.decode()] = {"mode": mode, "type": kind, "blob": sha}
    return result


def changed(a: dict, b: dict) -> dict:
    return {p: b.get(p) for p in sorted(a.keys() | b.keys()) if a.get(p) != b.get(p)}


def protected_paths(base: str) -> list[str]:
    original = tree(base)
    manifest = json.loads(git("show", f"{base}:provenance/IMPORT_MANIFEST.json"))
    paths = {row["destination_path"] for row in manifest["entries"]}
    paths.update(p for p in original if p.startswith(("provenance/", "docs/archive/")))
    historical = "docs/SUCC_MAIN_XXV_INTEGRATION_MANIFEST_2026-11-12.json"
    prior = json.loads(git("show", f"{base}:{historical}"))
    paths.update(row["path"] for row in prior.get("protected", []))
    paths.update(p for p in original if p.startswith("docs/SUCC_MAIN_XX") and "MANIFEST" in p)
    return sorted(paths)


def generate(rows: list[dict], integration: str, repairs: dict[str, str],
             manifest_path: str = DEFAULT_MANIFEST) -> dict:
    baseline, final = tree(BASE), tree(integration)
    donors, choices = [], {}
    for row in sorted(rows, key=lambda r: r["number"]):
        head = row["head"]
        if not ancestor(head, integration):
            raise ValueError(f"PR #{row['number']} head is not an integration ancestor")
        donor = tree(head)
        actual_tree = git("rev-parse", head + "^{tree}")
        if row.get("tree") != actual_tree:
            raise ValueError(f"PR #{row['number']} snapshot tree mismatch")
        inherited = [r for r in rows if r["number"] != row["number"] and ancestor(r["head"], head)]
        inherited_maximal = [r for r in inherited if not any(
            r != s and ancestor(r["head"], s["head"]) for s in inherited)]
        primary = min(inherited_maximal,
                      key=lambda r: int(git("rev-list", "--count", r["head"] + ".." + head)),
                      default=None)
        own_base = primary["head"] if primary else git("merge-base", BASE, head)
        delta = changed(tree(own_base), donor)
        own_files = []
        for path, value in delta.items():
            inherited_from = [r["number"] for r in inherited if tree(r["head"]).get(path) == value]
            own_files.append({"path": path, "entry": value,
                              "classification": "inherited" if inherited_from else "unique_or_merge_reconciliation",
                              "inherited_from": inherited_from})
        # Older independent donors may branch before Main XXV. Comparing their
        # entire trees directly with newer main would mistake later main work
        # absent from the donor for a donor deletion or contradictory rewrite.
        common_base = git("merge-base", BASE, head)
        contribution = changed(tree(common_base), donor)
        for path, value in contribution.items():
            choices.setdefault(path, []).append((row["number"], value))
        donors.append({"pr": row["number"], "url": row["url"], "title": row["title"],
                       "head": head, "tree": actual_tree,
                       "parents": git("show", "-s", "--format=%P", head).split(),
                       "nearest_active_ancestors": sorted(r["number"] for r in inherited_maximal),
                       "all_active_ancestors": sorted(r["number"] for r in inherited),
                       "comparison_base": own_base, "comparison_base_is_single_primary": True,
                       "baseline_merge_base": common_base,
                       "own_delta": own_files,
                       "disposition": "integrated by exact head ancestry; claims retain audited scopes"})
    overrides, missing_repairs = [], []
    for path, alternatives in sorted(choices.items()):
        if not any(value == final.get(path) for _, value in alternatives):
            if path == CATALOG:
                reason = "deterministic regeneration after combined claim/document changes"
            else:
                reason = repairs.get(path)
            if not reason:
                missing_repairs.append(path)
                continue
            overrides.append({"path": path, "reason": reason, "final_entry": final.get(path),
                              "donor_entries": [{"pr": n, "entry": value} for n, value in alternatives]})
    if missing_repairs:
        raise ValueError("Undeclared donor byte changes:\n" + "\n".join(missing_repairs))
    exclusions = [manifest_path, CATALOG]
    changes = {p: entry for p, entry in changed(baseline, final).items() if p not in exclusions}
    protected = {p: baseline.get(p) for p in protected_paths(BASE)}
    for path, expected in protected.items():
        if final.get(path) != expected:
            raise ValueError(f"Protected baseline bytes changed: {path}")
    return {"schema_version": 1, "baseline": {"commit": BASE, "tree": git("rev-parse", BASE + "^{tree}")},
            "scope": "Git ancestry, declared source reconciliation and bytes; no proof certification",
            "self_reference_policy": "Final SHA/tree belongs in external validation receipts; no self hash.",
            "comparison_policy": "Own delta uses nearest primary active ancestor; inherited blob matches are identified separately. Additional ancestral branch reconciliation is explicit, not independent proof.",
            "excluded_final_change_paths": exclusions,
            "excluded_path_checks": {CATALOG: "python scripts/build_math_memory.py --check",
                                     manifest_path: "this structural and byte/ancestry check"},
            "donors": donors, "declared_integration_overrides": overrides,
            "protected_baseline_entries": protected, "final_changes": changes}


def check(data: dict, integration: str) -> list[str]:
    errors = []
    final = tree(integration)
    base = data.get("baseline", {}).get("commit")
    if base != BASE or not ancestor(BASE, integration):
        errors.append("baseline identity/ancestry mismatch")
    donors = data.get("donors", [])
    numbers = [row.get("pr") for row in donors]
    if len(numbers) != 54 or set(numbers) != EXPECTED_PRS:
        errors.append("expected exactly 54 distinct recovery-snapshot PR donors")
    for row in donors:
        head = row["head"]
        if not ancestor(head, integration):
            errors.append(f"missing PR #{row['pr']} ancestry")
        if git("rev-parse", head + "^{tree}") != row["tree"]:
            errors.append(f"PR #{row['pr']} donor tree mismatch")
        if git("show", "-s", "--format=%P", head).split() != row["parents"]:
            errors.append(f"PR #{row['pr']} donor parent mismatch")
        for entry in row["own_delta"]:
            if tree(head).get(entry["path"]) != entry["entry"]:
                errors.append(f"donor delta entry mismatch: {entry['path']}")
    exclusions = set(data.get("excluded_final_change_paths", []))
    if exclusions != {DEFAULT_MANIFEST, CATALOG}:
        errors.append("unexpected final-byte exclusions")
    actual = {p: value for p, value in changed(tree(BASE), final).items() if p not in exclusions}
    expected = data.get("final_changes", {})
    for path in sorted(actual.keys() | expected.keys()):
        if actual.get(path) != expected.get(path) or (path in actual) != (path in expected):
            errors.append(f"final changed-file drift: {path}")
    protected = data.get("protected_baseline_entries", {})
    if set(protected) != set(protected_paths(BASE)):
        errors.append("protected path coverage mismatch")
    for path, entry in protected.items():
        if tree(BASE).get(path) != entry or final.get(path) != entry:
            errors.append(f"protected baseline drift: {path}")
    for row in data.get("declared_integration_overrides", []):
        if not row.get("reason") or final.get(row["path"]) != row["final_entry"]:
            errors.append(f"invalid integration override: {row['path']}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--generate", type=Path, help="recovery PR snapshot JSON")
    mode.add_argument("--check", type=Path)
    parser.add_argument("--integration", default="HEAD")
    parser.add_argument("--repairs", type=Path, help="JSON object mapping changed donor path to reason")
    parser.add_argument("--out", type=Path, default=Path(DEFAULT_MANIFEST))
    args = parser.parse_args()
    if args.generate:
        repairs = json.loads(args.repairs.read_text()) if args.repairs else {}
        data = generate(json.loads(args.generate.read_text()), args.integration, repairs, args.out.as_posix())
        args.out.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
        print(f"Generated {args.out}: {len(data['donors'])} donors, {len(data['final_changes'])} final changes")
    else:
        data = json.loads(args.check.read_text())
        errors = check(data, args.integration)
        for error in errors:
            print("FAIL:", error)
        print(f"{'FAIL' if errors else 'PASS'}: {len(data.get('donors', []))} donor ancestries and bound final bytes; no mathematical proof certification")
        return bool(errors)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
