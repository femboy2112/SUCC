# Operation Main XIX — provenance DAG and blob reconciliation

All SHAs verified against live GitHub and recomputed from the actual fetched heads on
2026-11-01. `main` before = `4eb411e3730a9e7b95480369a438b89d9a433a4b` (Main XVIII, PR #436).

## Source PRs and the three ancestry-minimal leaves

Nineteen open research PRs are subsumed by three leaves whose union is complete and whose
pairwise unique content is disjoint:

| leaf | head | cluster | subsumes (git ancestors) |
|---|---|---|---|
| #437 | `f6abb3a91426c7a23efab100ed9d002b60a082bc` | A — four-pole path interference | — (based directly on `main`) |
| #452 | `2ec2a406399277af361ca4da8f257e1ce726b8b9` | B — arctan/chiral solenoid + finite-history | shared trunk #438–#447 and the finite-history fork **#448** |
| #455 | `a5752c3d3403c1b01b0a3b71a3241d77fdc87a59` | C — categorical/Fourier/entropy/Laurent | shared trunk #438–#447 and **#449, #450, #451, #453, #454** |

### The DAG (forks at #447)

```
main (4eb411e3)
 ├─ #437  four_pole_path_interference                         ← LEAF A (independent)
 └─ #438 → #439 → #440 → #441 → #442 → #443 → #444 → #445 → #446 → #447 (6fedcbe4)   ← shared trunk
                                                                     ├─ #448 → #452   ← LEAF B
                                                                     └─ #449 → #450 → #451 → #453 → #454 → #455  ← LEAF C
```

Verified: `merge-base(main, #437)=merge-base(main, #452)=merge-base(main, #455)=main`;
`merge-base(#452, #455)=6fedcbe4` (the #447 head); #437 is an ancestor of neither #452 nor #455.
Each of #438–#447 is an ancestor of **both** #452 and #455; #448 is an ancestor of **#452 only**;
#449/#450/#451/#453/#454 are ancestors of **#455 only**.

### Correction to the pre-integration prose

An earlier description grouped #455 as going "through PRs #438–#451." Git disagrees: **#448 is
NOT an ancestor of #455** — it is the finite-history fork that lives only on the #452 leaf. The
recomputed-from-heads ancestry above governs. The three leaves still subsume the full #437–#455
range with no orphan parent result.

## File-path accounting (recomputed from actual heads)

- Added by #437: **11** files. Added by #452: **135**. Added by #455: **217**.
- Shared trunk (added on `main..#447`, present in both #452 and #455): **108** files.
- #452-unique: **27**. #455-unique: **109** (= 94 at #454 + 15 for `laurent_clock_sharpness`).
- Pairwise intersections of the three leaves' unique sets: **empty** (#452-unique ∩ #455-unique = ∅;
  #437 disjoint from all). Shared content is only the 108-file trunk.
- **Distinct added file paths across all three leaves: 255** (= 11 + 27 + 109 + 108).

These reproduce the directive's expected 108 / 255 counts exactly.

## Merge reconciliation (no duplicate sibling import)

The shared trunk #438–#447 is carried once: merging #452 first brings the trunk (plus #448 and
#452); the subsequent `--no-ff` merge of #455 has `merge-base = 6fedcbe4` (#447), so it applies
only the #449/#450/#451/#453/#454 deltas. Because every leaf's unique file set is disjoint, the
#455 merge is a conflict-free add/add — **no `-s ours`, no silent overwrite, no duplicated
theorem identity, no discarded test.** Trunk blobs are byte-identical in both #452 and #455 by
construction (same commits), so there is no competing copy to reconcile.

## First-parent integration chain

```
main 4eb411e3
  └─(--no-ff)→ 163bfe4a  Main XIX: integrate PR #437 (four-pole path interference)
      └─(--no-ff)→ 710b33c2  Main XIX: integrate PR #452 (arctan/finite-history)
          └─(--no-ff)→ 92c58f4f  Main XIX: integrate PR #455 (categorical/entropy/Laurent)
              └→ <integration commit: dossier + nav + regenerated catalog>
```

## Frozen invariants (byte-identical to `main`, verified)

`observational_succ/`, `formal/`, `scripts/`, `provenance/IMPORT_MANIFEST.json`, `.github/`,
`ci.yml`, `pyproject.toml`, the frozen BBP source dossier, `U_0=0`, and the four signed poles
`r(n)=4/(8n−7)−2/(8n−4)−1/(8n−3)−1/(8n−2)` are unchanged. `git diff main..HEAD` touches only
`research/` and `tests/` (plus the integration commit's additive nav blocks and the regenerated
catalog).
