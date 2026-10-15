# Read-only local SUCC Git push audit

**Date:** 2026-10-15. **Objective:** distinguish commits already pushed to GitHub from commits/files existing only in a research agent's local checkout. This is a read-only procedure; there is NO automatic push, merge, force push, rebase, branch delete or source mutation.

## Usage on the user's own workstation

Run in the actual cloned SUCC repository:

    git fetch --all --prune
    python scripts/audit_local_push_state.py --json

The first command is an OPTIONAL **explicit user choice** to refresh remote tracking refs; it does not push or change working files, but it updates local remote-tracking metadata. The second command runs completely without network or mutating the repository.

Output includes the exact HEAD, current branch, changed/untracked files, local branch upstream names and ahead/behind counts, and commits on local branches which are not reachable from any FETCHED remote ref. A branch without an upstream is labelled UNKNOWN, not incorrectly called unpushed.

If an interactive review wants to fail on possible unpushed work, use:

    python scripts/audit_local_push_state.py --strict

It returns exit code 2 when changed/untracked files, commits absent from fetched refs, or ahead-of-upstream branches are reported. It does NOT perform a push. Have the maintainer review branch histories and mathematical/source validation before pushing. Inspect also git reflog and optional git fsck --no-reflogs --unreachable when looking for dropped/dangling commits; the lightweight audit does not traverse reflog-only objects.

## Why ChatGPT GitHub API cannot inspect local-only work

The GitHub connector can enumerate pushed branch heads, commits, pull requests and CI. It cannot read a user's unpushed workstation commits, in-memory agent edits, untracked files or local stashes. Claims that all work is pushed require either a local audit or complete control of the local checkout. A remote commit is not proof that an unpublished local branch has no extra commits.

## Live remote snapshot, not a statement about the user's local work

At this round GitHub showed 181 pushed branches and 22 then-open PRs. Four non-archived remote research branch names lacked a PR head association; these were already PUSHED branches, not hidden laptop commits:

- research/suzuki-30mode-neumann-dual-gauge-2026-10-15 at 256cb681, 50 commits ahead of main; original head's CI failed. A separate recovery branch and draft PR #123 now preserve this work and fix the exact log2 interval and polynomial-test adapter errors, leaving the original head unchanged.
- research/suzuki-full30-residual-swarm-2026-10-15 at 44d7f699, which is the exact same commit SHA as existing PR #107 (branch alias, not lost work).
- research/suzuki-weil-finite-to-global-2026-10-13, an older diverged historical research head, not silently merged or deleted.
- research/swm-f48-2026-10-13, another diverged historical head, not silently merged or deleted.

This snapshot is not proof that no further local/unpushed data exist. Avoid auto-opening dozens of obsolete historical PRs or force-pushing over concurrent branches; review sources and provenance first.

**Current code:** scripts/audit_local_push_state.py. The synthetic Git integration suite tests/test_audit_local_push_state.py constructs a temporary bare remote and clone, creates a pushed initial commit, an UNPUSHED local commit, a no-upstream branch and an untracked file, then proves the audit detects them **without changing remote HEAD or local status**.

**Original mathematical source status:** the ordinal authenticated Suzuki margin work is independent of the local audit. Its finite interval certificates are not RH proofs; only source-derived all-test positivity could solve RH.
