# SUCC integration audit — three distinct research trunks, not one linear PR queue

**Observed on 2026-11-03 (live GitHub connector).** **NOT a merge authorization by this dossier**; the user has separately asked Claude to consolidate and merge, after validating. All values must be re-fetched at integration time. Repository `femboy2112/SUCC`, main at `81045770234a114247e43eb08ae5c6d446e9514a`. All named PRs below were **OPEN DRAFT**, not already integrated into main.

## Live branch diffs relative to main

| Tip | Exact SHA | Ahead of main | Added paths | Modified / removed inherited paths | Hosted workflow snapshot |
|---|---|---:|---:|---|---|
| [#488](https://github.com/femboy2112/SUCC/pull/488) current circle-path backbone | `f47e3768631cd1628c1390d529811c911e0f6443` | 115 commits | 240 | 0 / 0 | 3 completed success, 1 in progress |
| [#486](https://github.com/femboy2112/SUCC/pull/486) figure-eight / observer sibling | `9eea9e3e89022b9a57716f21b31ffc3e69f0552f` | 156 commits | 145 | 0 / 0 | 4 completed success |
| [#472](https://github.com/femboy2112/SUCC/pull/472) selected-prime / causal-response sibling | `85189e389ca1568636a7fedb7b2d6268b8eae447` | 161 commits | 104 | 0 / 0 | 4 completed success |

**Set comparison by exact added paths (not a source correctness proof):** #488 and #486 overlap in 95 newly added paths, leaving #488-only 145 and #486-only 50. #472's 104 added paths are disjoint from both. Union of the three trunks: **394 distinct added paths**, 0 inherited-file modifications/deletions in each main-relative comparison. The 95 shared-path file BLOB contents were NOT exhaustively compared; before merging inspect their bytes/diffs for sibling divergence. These 394 files are not 394 separate theorem certifications.

**Direct sibling compare:** #486 -> #488 is `diverged`, merge base `20acb35a42b6ae5fb9260c041ed3a1aa47429484` (parent #475); neither tip subsumes the other. Merging #488 alone leaves #486 content out. #472 is another independent research history from main; merging the first two still leaves its results out.

## High-level dependency DAG (verify exact Git ancestry before merge)

```text
main @ 81045770234a...
  |
  +-- shared analytic/spectral line ... #465 -> #468 -> #470 -> #471
  |     -> #473 -> #474 -> #475
  |        |-- #476 -> #479 -> #481 -> #483 -> #484 -> #485
  |        |      -> #487 -> #488 -> NEW selected-current research
  |        |
  |        `-- #477 -> #478 -> #480 -> #482 -> #486
  |
  `-- independent source/causal line ... #462 -> #463 -> #464
         -> #466 -> #467 -> #469 -> #472
```

**Note:** the diagram is a human-readable dependency map from PR metadata. It is NOT a substitute for `git merge-base`, `git rev-list`, and release branch comparison. It deliberately does not claim that *all* open PRs in the repository are relevant to this π-normality front; Claude must inventory and classify any other active unmerged research before announcing “everything”.

## Suggested secure integration workflow for Claude

1. Snapshot live refs, main commit, branch heads, `AGENTS.md`, `provenance/IMPORT_MANIFEST.json`, frozen archive, original source and formal theorem contracts. Use a new **integration worktree**. Do not rewrite or force-push any original research branch.
2. Build one integration branch off the **fresh** main, preserve the whole add-only ancestry, merge the latest NEW current-front tip (includes #488 and its dependencies) first with `--no-ff`, then reconcile and merge #486's full sibling history, then reconcile #472's independent history. Alternative topology allowed if independently verified. Don't cherry-pick every ancestor twice.
3. For all 95 overlapping path names between #488 and #486, compare Git blobs before asserting conflict-free. When divergent, record both raw versions and justify resolution; never silently replace a historical theorem receipt. Source contracts, Lean proof imports, test file names and original signed forcing must be checked for cross-branch incompatible assumptions.
4. Validate original zero seed `U0=0` and **all four signed Mellin poles** bytewise against main and frozen provenance. Ensure π-normality, selected signed Weyl, and original `E=o(log m)` are still tagged OPEN after docs integration. Preserve no-go and failed holdouts.
5. Run impacted focused tests/receipt replay once after each logically coherent trunk, then **full native mandatory** `verify_provenance.py`, all `test_*.py`, `observer_foundations_probe.py`, `ordinal_succ_report_probe.py` at the *final integrated head*. Check Lean and workflows separately; do not infer child CI from parent CI. Existing packages may need `PYTHONPATH` installed.
6. Refresh `README.md`, `docs/PI_SELECTED_CATEGORICAL_FRONTIER.md`, `docs/ROADMAP.md`, claim/architecture/source-map catalogs and mathematical-memory index in a small well-attributed integration commit. Make `docs/PI_BRANCH_CURRENT_FRONTIER_2026-11-03.md` the active concise operational front. Avoid editing archival research proofs solely for editorial consolidation.
7. Only after full tests and integration PR CI pass: merge integration into main as authorized by user's explicit request to Claude. No force push, no merge of contradictory claims without reconciliation, no release/tag unless separately authorized. Report exact main SHA, test receipts, PR dispositions and unresolved research obligations. On a blocking failure, leave a draft integration PR rather than claiming a completed merge.

## Research labels to preserve

**Proved/conditional:** arithmetic 2-adic isometry, quadratic Gaussian/real source gluing, Gamma endpoint transport, exact split/inert p denominators and nonrepeat, conditional log-mesh normality gate, exact source-selected current branch-square decomposition and the NEW shifted-bin comparison. **Not proved:** actual original source-selected real near-pair/carry/cofactor bound, all-prefix Weyl `S_N(h)=o(N)` and π base-16 normality; RH is an unrelated open program. **False shortcuts:** “Galois average implies selected embedding”, “periodic branch inverse implies Haar”, “uniform current minimum is the actual source law”, “nonrepeat implies 1/logA real spacing”, “finite pi-prefix shadow means infinite normality”.
