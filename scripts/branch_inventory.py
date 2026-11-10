#!/usr/bin/env python3
"""Dependency-aware open-PR inventory for SUCC integration rounds.

Rebuilds the research-branch DAG from Git (not from PR titles or handoffs):
for every open PR it records head SHA, base, merge-base with ``main``,
ancestry among the open heads, own commits (head minus its base PR's head),
its own changed-file inventory with Git blob ids, the integration leaf that
carries it, cross-leaf path overlaps (with blob equality), and the hosted CI
conclusions on the exact head SHA.

Usage (read-only on the repository; needs ``git`` and an authenticated ``gh``):

    python scripts/branch_inventory.py --main <sha> --integration <ref> \
        --prs open_prs.json --repo owner/name --out inventory.json [--no-ci]

``open_prs.json`` is ``gh pr list --state open --json
number,title,headRefName,headRefOid,baseRefName,isDraft,url``.
No file in the repository is modified.
"""
from __future__ import annotations

import argparse
import itertools
import json
import subprocess
import sys
from collections import defaultdict


def git(*args: str, check: bool = True) -> str:
    out = subprocess.run(("git",) + args, capture_output=True, text=True)
    if check and out.returncode != 0:
        raise RuntimeError(f"git {' '.join(args)}: {out.stderr.strip()}")
    return out.stdout.strip()


def is_ancestor(a: str, b: str) -> bool:
    return subprocess.run(("git", "merge-base", "--is-ancestor", a, b)).returncode == 0


def changed_files(base: str, head: str) -> list[dict]:
    rows = []
    for line in git("diff", "--name-status", "--no-renames", base, head).splitlines():
        status, path = line.split("\t", 1)
        blob = git("rev-parse", f"{head}:{path}", check=False) if status != "D" else None
        rows.append({"status": status, "path": path, "blob": blob or None})
    return rows


def ci_conclusions(repo: str, sha: str) -> dict:
    out = subprocess.run(
        ("gh", "api", "--paginate", f"repos/{repo}/commits/{sha}/check-runs",
         "--jq", ".check_runs[] | [.name, .status, (.conclusion // \"\")] | @tsv"),
        capture_output=True, text=True)
    if out.returncode != 0:
        return {"error": out.stderr.strip()[:200]}
    tally: dict[str, int] = defaultdict(int)
    failing = []
    for line in out.stdout.splitlines():
        name, status, concl = (line.split("\t") + ["", ""])[:3]
        key = concl or status
        tally[key] += 1
        if concl in ("failure", "cancelled", "timed_out", "action_required"):
            failing.append(f"{name}: {concl}")
    return {"tally": dict(tally), "non_success": failing}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--main", required=True)
    ap.add_argument("--integration", required=True)
    ap.add_argument("--prs", required=True)
    ap.add_argument("--repo", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--no-ci", action="store_true")
    a = ap.parse_args()

    main_sha = git("rev-parse", a.main)
    integ_sha = git("rev-parse", a.integration)
    prs = sorted(json.load(open(a.prs)), key=lambda p: p["number"])
    by_branch = {p["headRefName"]: p for p in prs}
    open_heads = {p["number"]: p["headRefOid"] for p in prs}

    pending = [n for n, h in open_heads.items() if not is_ancestor(h, main_sha)]
    contains = {n: sorted(m for m in pending if is_ancestor(open_heads[m], open_heads[n])) for n in pending}
    leaves = [n for n in pending if not any(n != m and n in contains[m] for m in pending)]

    records = []
    for p in prs:
        n, head = p["number"], p["headRefOid"]
        rec = {
            "number": n, "title": p["title"], "branch": p["headRefName"], "head": head,
            "base_branch": p["baseRefName"], "url": p.get("url"),
            "merge_base_with_main": git("merge-base", head, main_sha),
            "ancestor_of_main": is_ancestor(head, main_sha),
            "ancestor_of_integration": is_ancestor(head, integ_sha),
        }
        if rec["ancestor_of_main"]:
            rec["disposition"] = "superseded-by-earlier-integration (head already in main)"
        else:
            parent = by_branch.get(p["baseRefName"])
            own_base = parent["headRefOid"] if parent else git("merge-base", main_sha, head)
            if parent and not is_ancestor(own_base, head):  # parent advanced after fork
                own_base = git("merge-base", own_base, head)
            rec["own_base"] = own_base
            rec["own_commits"] = git("rev-list", "--reverse", f"{own_base}..{head}").split()
            rec["commits_not_in_main"] = int(git("rev-list", "--count", f"{main_sha}..{head}"))
            rec["own_changed_files"] = changed_files(own_base, head)
            rec["contains_open_prs"] = [m for m in contains[n] if m != n]
            rec["carried_by_leaves"] = [L for L in leaves if n in contains[L]]
            rec["is_leaf"] = n in leaves
            rec["disposition"] = ("integrate (leaf)" if n in leaves else "integrate (by ancestry)") \
                if rec["ancestor_of_integration"] else "NOT INTEGRATED"
            if not a.no_ci:
                rec["ci_exact_head"] = ci_conclusions(a.repo, head)
        records.append(rec)

    added_by_leaf = {}
    for L in leaves:
        # diff from the merge-base, so a leaf forked from an older main is not
        # charged with main's own later edits (three-dot semantics)
        rows = changed_files(git("merge-base", main_sha, open_heads[L]), open_heads[L])
        added_by_leaf[L] = {r["path"]: r["blob"] for r in rows}
    overlaps = []
    for x, y in itertools.combinations(leaves, 2):
        for path in sorted(set(added_by_leaf[x]) & set(added_by_leaf[y])):
            overlaps.append({"leaves": [x, y], "path": path,
                             "identical_blob": added_by_leaf[x][path] == added_by_leaf[y][path]})

    out = {
        "main": main_sha, "integration": integ_sha,
        "open_pr_count": len(prs), "pending_count": len(pending),
        "leaves": leaves, "leaf_contains": {str(L): contains[L] for L in leaves},
        "cross_leaf_path_overlaps": overlaps,
        "integration_diff_vs_main": [
            {"status": s, "path": f} for s, f in
            (l.split("\t", 1) for l in git("diff", "--name-status", "--no-renames", main_sha, integ_sha).splitlines())],
        "prs": records,
    }
    json.dump(out, open(a.out, "w"), indent=1, sort_keys=True)
    print(f"main {main_sha[:8]} integration {integ_sha[:8]}: {len(prs)} open, "
          f"{len(pending)} pending, leaves {leaves}, {len(overlaps)} cross-leaf overlaps "
          f"({sum(not o['identical_blob'] for o in overlaps)} differing)")
    return 0 if all(r["ancestor_of_integration"] for r in records) else 1


if __name__ == "__main__":
    sys.exit(main())
