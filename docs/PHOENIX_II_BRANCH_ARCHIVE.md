# Phoenix II — branch archive review (2026-10-14)

Human-readable companion to `docs/BRANCH_ARCHIVE_MANIFEST_2026-10-14.json`. **162 remote branches** classified against the integration head `8d77c73` and `main` `6e0d88f`.

## Policy (non-negotiable)

- **No branch is deleted by this campaign without explicit maintainer go.** This document + the manifest are the *plan*; execution of archive-refs and deletions is a separate, gated step.
- Archive mechanism: immutable refs `archive/2026-10-14/<branch-name>` at each branch's exact tip SHA, created and pushed **only on explicit go**. Nothing is a release or version tag.
- `git branch --merged` is **not** used as a content oracle — some `research/swm-*` refs have diverged git histories despite their mathematics being in the Oct-13 atlas. Classification uses ancestry **and** patch-id content containment.

## Categories

| Category | Count | Meaning | Disposition |
|---|---|---|---|
| `INTEGRATED_ANCESTOR` | 99 | tip reachable from the integrated tree (43 with open PRs #57–99 + 56 already in `main`) | 43: **RETIRE_AFTER_MERGE** (PR auto-closes on integration→main merge); 56: **ARCHIVE_AND_DELETE_ELIGIBLE** |
| `INTEGRATED_BY_CONTENT` | 61 | commits patch-equivalent-present though git history diverged (old `swm-*`, prior integration/audit branches) | **ARCHIVE_AND_DELETE_ELIGIBLE** |
| `ACTIVE_RESEARCH` | 1 | `research/suzuki-weil-finite-to-global-2026-10-13` — a separate pending frontier, **not** integrated here | **KEEP_ACTIVE** |
| `PRESERVED_EXPERIMENT` | 1 | `research/swm-f48-2026-10-13` — a later "freeze" commit diverged from the atlas history (unique F48 phase-2 receipt churn) | **PRESERVE_EXPERIMENT_ARCHIVE_ONLY** (archive, do not delete) |

## Special cases

- **Hazard C duplicate:** `research/signed-weiI-h1-spectral-tail-2026-10-14` (capital `I`) — byte-identical tip to #82's head (`bb5b6f96`). `DUPLICATE_REF`, zero unique content. Archive ref only; safe to delete after archiving (no open PR points at the capital-I name; PR #82 uses the correct lowercase `signed-weil`/`xi-complex-contour` head).
- **The 43 open-PR branches (#57–99):** their content is now ancestral to the integration branch. They are **not** retired until the integration→main merge lands and auto-closes their PRs. Deleting them earlier would close active PRs — disallowed.
- **`research/suzuki-weil-finite-to-global-2026-10-13`:** pending integration with a separate track; left fully intact and active.

## Pre-retirement checklist (applied before any deletion)

For each `ARCHIVE_AND_DELETE_ELIGIBLE` / `RETIRE_AFTER_MERGE` branch, confirm: (1) exact tip preserved at `archive/2026-10-14/<name>` and reachable; (2) no unique patch lost (manifest records `unique_patches_vs_integ`); (3) no open PR depends on it as head/base; (4) no descendant integration branch needs the name. Only then delete the remote branch.
