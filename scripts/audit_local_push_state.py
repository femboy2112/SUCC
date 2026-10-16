#!/usr/bin/env python3
"""Read-only local unpushed Git audit.

Usage: python scripts/audit_local_push_state.py --json
       python scripts/audit_local_push_state.py --repo /path/to/SUCC
       python scripts/audit_local_push_state.py --strict

NEVER commits, pushes, fetches, rebases, prunes, or edits files.
For fresh remote refs, the USER may choose to run git fetch --all --prune
before auditing. GitHub cannot inspect unpushed changes on a laptop.
"""
from __future__ import annotations
import argparse
import json
import subprocess
from pathlib import Path


def _git(repo: Path, *args: str) -> str:
    p = subprocess.run(["git", "-C", str(repo), *args],
                       capture_output=True, text=True, check=False)
    if p.returncode:
        raise RuntimeError(
            f"Read-only git command failed ({' '.join(args)}): {p.stderr.strip()}"
        )
    return p.stdout.strip()


def audit(repo: Path) -> dict:
    root = Path(_git(repo, "rev-parse", "--show-toplevel"))
    branches = []
    fmt = "%(refname:short)%00%(upstream:short)"
    refs = _git(root, "for-each-ref", f"--format={fmt}", "refs/heads")
    for line in refs.splitlines():
        branch, upstream = line.split("\0", 1)
        entry = {"branch": branch, "upstream": upstream or None}
        if upstream:
            # For upstream...local, left count is behind, right count ahead.
            counts = _git(root, "rev-list", "--left-right", "--count",
                          f"{upstream}...{branch}").split()
            if len(counts) != 2:
                raise RuntimeError("Git ahead/behind counter malformed")
            entry["behind"] = int(counts[0])
            entry["ahead"] = int(counts[1])
            entry["classification"] = ("AHEAD_OF_FETCHED_UPSTREAM"
                                        if int(counts[1])
                                        else "NOT_AHEAD_OF_FETCHED_UPSTREAM")
        else:
            entry["classification"] = "NO_UPSTREAM_UNKNOWN_REMOTE_RELATION"
        branches.append(entry)
    local_only = _git(root, "log", "--branches", "--not", "--remotes",
                      "--format=%h %s", "--max-count=100")
    dirty = _git(root, "status", "--porcelain=v1", "-uall")
    return {
        "operation": "READ_ONLY_LOCAL_GIT_COMMIT_PUSH_AUDIT",
        "repository": str(root),
        "head": _git(root, "rev-parse", "HEAD"),
        "current_branch": _git(root, "branch", "--show-current") or "(detached HEAD)",
        "worktree_changes": dirty.splitlines() if dirty else [],
        "branches": branches,
        "commits_not_on_fetched_remote_refs": local_only.splitlines() if local_only else [],
        "limitations": [
            "Fetched remote tracking refs can be stale until human-initiated git fetch",
            "NO_UPSTREAM does not prove a commit has never been pushed",
            "Reflog-only/dangling commits are not scanned by this lightweight audit",
            "No network or working-tree/branch modifications are performed",
            "GitHub Actions cannot inspect a separate user's laptop",
        ],
        "may_have_local_unpushed_work": bool(
            dirty or local_only or any(b.get("ahead", 0) > 0 for b in branches)
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=Path("."))
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--strict", action="store_true",
                        help="Exit 2 on local changes, local-only commits or ahead branches")
    args = parser.parse_args()
    result = audit(args.repo)
    if args.json:
        print(json.dumps(result, sort_keys=True, indent=2))
    else:
        print("Local Git head:", result["head"], result["current_branch"])
        print("Changed/untracked files:", len(result["worktree_changes"]))
        for line in result["worktree_changes"]:
            print("  ", line)
        print("Local branch tracking:")
        for b in result["branches"]:
            if b["upstream"]:
                print(f"  {b['branch']} -> {b['upstream']}: "
                      f"ahead {b['ahead']}, behind {b['behind']}")
            else:
                print(f"  {b['branch']}: NO UPSTREAM / REMOTE RELATION UNKNOWN")
        print("Commits not reachable from FETCHED remote refs:",
              len(result["commits_not_on_fetched_remote_refs"]))
        for line in result["commits_not_on_fetched_remote_refs"]:
            print("  ", line)
        print("READ-ONLY. Freshness requires a separate git fetch when desired.")
    if args.strict and result["may_have_local_unpushed_work"]:
        raise SystemExit(2)


if __name__ == "__main__":
    main()
