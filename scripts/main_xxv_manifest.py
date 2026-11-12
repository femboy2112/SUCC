#!/usr/bin/env python3
"""Record and replay Main XXV contribution provenance without a self-hash.

Main XXV integrates a short linear stack (research rounds on top of Main XXIV),
so the manifest is deliberately small: for every origin head it records the
files that head contributed relative to its own base, and it re-derives from
Git that

* every origin head is an ancestor of the integration ref,
* every contributed file still has the recorded bytes at the integration ref,
  unless a later origin of the same stack or a declared regeneration replaced it,
* every protected path (frozen sources and archives) has the baseline bytes.

    python scripts/main_xxv_manifest.py --generate origins.json --base <main-xxiv> \
        --integration HEAD --protected-from docs/SUCC_MAIN_XXIV_INTEGRATION_MANIFEST_2026-11-11.json \
        --out manifest.json
    python scripts/main_xxv_manifest.py --check manifest.json --integration HEAD

``origins.json`` is a list of ``{"id", "pr", "branch", "head", "own_base", "claim",
"claim_status"}`` rows in stack order.  ``regenerated`` paths (for example the
mathematics catalog, which pins hashes of research files and is rebuilt last) are
recorded but not byte-compared.  The manifest names no final commit or tree of
its own.  This tool checks bytes and ancestry; it is not a proof checker.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import sys

REGENERATED = ("docs/math_memory/CLAIM_CATALOG.json",)
SCOPE = "Main XXV contribution bytes and ancestry, not proof certification"


def git(*args: str) -> str:
    return subprocess.check_output(["git", *args], text=True, stderr=subprocess.DEVNULL).strip()


def blob(ref: str, path: str) -> str | None:
    try:
        return git("rev-parse", "--verify", "--quiet", f"{ref}:{path}")
    except subprocess.CalledProcessError:
        return None


def sha256(ref: str, path: str) -> str:
    data = subprocess.check_output(["git", "cat-file", "blob", f"{ref}:{path}"])
    return hashlib.sha256(data).hexdigest()


def is_ancestor(old: str, new: str) -> bool:
    return subprocess.run(["git", "merge-base", "--is-ancestor", old, new],
                          stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode == 0


def changed(base: str, head: str) -> list[tuple[str, str]]:
    out = git("diff", "--name-status", "--no-renames", base, head)
    rows = []
    for line in out.splitlines():
        status, path = line.split("\t", 1)
        rows.append((status, path))
    return rows


def generate(origins: list[dict], base: str, integration: str, protected: list[str],
             regenerated: tuple[str, ...] = REGENERATED) -> dict:
    base = git("rev-parse", base)
    rows = []
    for origin in origins:
        head, own_base = git("rev-parse", origin["head"]), git("rev-parse", origin["own_base"])
        files = []
        for status, path in changed(own_base, head):
            entry = {"path": path, "status": status}
            if status != "D":
                entry["blob"] = blob(head, path)
                entry["sha256"] = sha256(head, path)
            files.append(entry)
        rows.append(dict(origin, head=head, own_base=own_base,
                         head_tree=git("rev-parse", head + "^{tree}"), files=files))
    return {
        "schema_version": 1,
        "scope": SCOPE,
        "self_reference_policy": "No final commit/tree self-hash; check with an explicit --integration ref.",
        "baseline_main": {"commit": base, "tree": git("rev-parse", base + "^{tree}")},
        "integration_ref_at_generation": integration,
        "origins": rows,
        "regenerated": list(regenerated),
        "protected": [{"path": p, "blob": blob(base, p)} for p in protected],
    }


def check(data: dict, integration: str) -> list[str]:
    errors = []
    base = data["baseline_main"]["commit"]
    if not is_ancestor(base, integration):
        errors.append(f"Missing ancestry: baseline {base}")
    regenerated = set(data.get("regenerated", ()))
    origins = data["origins"]
    if not origins:
        errors.append("Contribution row coverage mismatch")
    later: list[set[str]] = []
    seen: set[str] = set()
    for origin in reversed(origins):          # paths rewritten by a later origin of the stack
        later.append(set(seen))
        seen |= {f["path"] for f in origin["files"]}
    later.reverse()
    for origin, superseded in zip(origins, later):
        if not is_ancestor(origin["head"], integration):
            errors.append(f"Missing ancestry: {origin['id']} {origin['head']}")
        if not origin["files"]:
            errors.append(f"Contribution row coverage mismatch: {origin['id']}")
        for entry in origin["files"]:
            path = entry["path"]
            if path in regenerated or path in superseded:
                continue
            now = blob(integration, path)
            if entry["status"] == "D":
                if now is not None:
                    errors.append(f"Deleted path reappeared: {path}")
            elif now != entry["blob"]:
                errors.append(f"Final bytes changed: {origin['id']}:{path}")
    for entry in data["protected"]:
        if blob(integration, entry["path"]) != entry["blob"]:
            errors.append(f"Protected bytes changed: {entry['path']}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--generate", help="origins JSON (stack order)")
    parser.add_argument("--base")
    parser.add_argument("--integration", required=True)
    parser.add_argument("--protected-from", help="earlier manifest whose protected path list is reused")
    parser.add_argument("--out")
    parser.add_argument("--check")
    args = parser.parse_args()
    if args.check:
        errors = check(json.loads(Path(args.check).read_text()), args.integration)
        for error in errors:
            print(error)
        print("MAIN_XXV_MANIFEST_OK" if not errors else "MAIN_XXV_MANIFEST_FAILED")
        return 1 if errors else 0
    if not (args.generate and args.base and args.out):
        parser.error("--generate needs --base and --out")
    protected = []
    if args.protected_from:
        protected = [row["path"] for row in json.loads(Path(args.protected_from).read_text())["protected"]]
    data = generate(json.loads(Path(args.generate).read_text()), args.base, args.integration, protected)
    Path(args.out).write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
