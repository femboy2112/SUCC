# Operation Main XVIII — provenance DAG and integration reconciliation

**Research-status.** This records the exact pull-request ancestry, the ancestry-minimal
integration order, the blob-level reconciliation of the duplicated sibling content, and the
invariants preserved. It promotes no mathematical status.

## 1. Starting point

`main` before integration: `e8598cfa5d32fd1de8e94a3e458a366a0850d59e` (Operation Main XVII).
All four cluster tips branch directly off this commit — each tip's merge-base with `e8598cfa`
is `e8598cfa` itself, so every leaf is a pure addition on top of Main XVII with no hidden rebase.

## 2. The three content clusters and their git ancestry

```
  main e8598cfa
    │
    ├── Cluster A ── PR #426  counterfactual-triangle-carrier-rigidity   (def05a7c)      [base: main]
    │
    ├── Cluster B ── PR #427 → #428 → #429 → #430                                         [chain off main]
    │                 #427 pi-two-three-adic-joint-clock-rigidity        (8558a95b)
    │                 #428 pascal-2-3-conjugacy-pisot-probe              (91e06fd2)
    │                 #429 half-power-two-three-horizon                  (33d53f57)
    │                 #430 multiplace-bbp-difference-resolvent  (TIP)    (ba8bc0d3)
    │
    └── Cluster C ── PR #431 (base: main)  carrier-relative-path-measure (cf23b8cf)
                      ├── PR #432 edge-seed-tomography-selected-pi       (d3907a79)  [SIBLING off #431]
                      └── PR #433 → #434 → #435
                          #433 selected-seed-superposition-horizon       (5721c048)  [off #431]
                          #434 selected-pi-signed-lag-forge-astra         (030ee84b)  [off #433]
                          #435 selected-pi-lag-fireworks         (TIP)    (f8b588b1)  [off #434]
```

**Verified by `git merge-base --is-ancestor`:**
- `#427`, `#428`, `#429` are each **ancestors of `#430`** → one leaf (`#430`) carries Cluster B.
- `#431`, `#433`, `#434` are each **ancestors of `#435`** → `#435` carries that chain.
- `#432` is **NOT an ancestor of `#435`**. It is a sibling of `#433` off `#431`. PR #434 re-created
  PR #432's eleven files inside its own history without taking `#432`'s commits.

## 3. Minimal ancestry-preserving integration set — four leaves

`#426`, `#430`, `#432`, `#435`. The 22 interior PRs (`#427–#429`, `#431`, `#433`, `#434`) land
transitively as ancestors. `#432` is carried as its own leaf so that its tomography commit history
is preserved rather than discarded in favour of `#434`'s byte-copy.

## 4. The #432 ↔ #434/#435 byte-copy reconciliation

PR #434 (hence #435) carries byte-for-byte copies of PR #432's eleven files:

```
research/2026-10-31/edge_seed_tomography/{CLAIMS,NEXT,PROOFS,README,SOURCE_MAP,VALIDATION}.md
research/2026-10-31/edge_seed_tomography/{edge_seed_tomography.py,finite_receipt.json,independent_oracle.py,probe.py}
tests/test_edge_seed_tomography.py
```

Every one of these eleven paths has an **identical git blob hash** in `#432`, `#434`, and `#435`
(checked individually). Because the files are byte-identical and share the common ancestor `#431`,
merging `#432` first and `#435` afterward produces an **identical add/add that git resolves with no
conflict** — the files enter history through `#432`'s commits, and `#435`'s copies reconcile as a
no-op. No competing copy is created, no `-s ours` or forced resolution is used, and no separate
implementation is written to make the two siblings coexist.

## 5. Integration order and merge commits (all `--no-ff`, zero conflicts)

First-parent chain `main → A → B → C(#432) → C(#435)`:

| order | merge commit | parents (base, leaf) | leaf |
|---|---|---|---|
| 1 | `0c40933d` | `e8598cfa`, `def05a7c` | PR #426 (Cluster A) |
| 2 | `2150589c` | `0c40933d`, `ba8bc0d3` | PR #430 (Cluster B tip) |
| 3 | `ef62211a` | `2150589c`, `d3907a79` | PR #432 (Cluster C sibling, brings #431) |
| 4 | `2f43c81a` | `ef62211a`, `f8b588b1` | PR #435 (Cluster C tip) |

Integration-branch head (pre-squash-PR): `2f43c81a`. Overall diff vs `main`:
**149 files, +14264 / −0** (purely additive; no deletions).

## 6. Where the content lands

- `#426` → `research/2026-10-31/counterfactual_triangle/` + `tests/test_counterfactual_triangle_carrier.py`
- `#430` → `research/2026-10-31/{half_power_horizon,multiplace_bbp_difference,pascal_crossprime,two_three_joint_carrier}/` + 4 tests
- `#432` → `research/2026-10-31/edge_seed_tomography/` + `tests/test_edge_seed_tomography.py`
- `#435` → `research/2026-10-31/{carrier_path_measure,seed_superposition,selected_lag_tomography,signed_lag_fireworks}/` + 9 tests, plus the single canonical touch below

## 7. The only canonical-file change in the whole integration

`docs/PI_SELECTED_CATEGORICAL_FRONTIER.md` — PR #435 appends an **additive** `## 7.` section
("October 31 signed-lag continuation"). It states that π normality remains OPEN and that the work
"settles gate equivalence, not the selected bound." Nothing else under `docs/`, `observational_succ/`,
`formal/`, `scripts/`, `provenance/`, `.github/`, or `ci.yml` is modified.

The additive Main XVIII navigation blocks (`docs/CLAIM_INDEX.md`, `docs/ROADMAP.md`,
`docs/math_memory/INDEX.md`), this dossier, and the regenerated `docs/math_memory/CLAIM_CATALOG.json`
are added by the integration commit itself (not by any leaf), with the catalog regenerated **last**.

## 8. Invariants preserved (byte-identical to `main e8598cfa`)

`observational_succ/`, `formal/`, `scripts/`, `provenance/` (including the frozen BBP source dossier
and `IMPORT_MANIFEST.json`, `source_commit ba075348`), `.github/`, and `ci.yml` are all byte-identical
to `main`. The authentic BBP source `r(n)=4/(8n-7)-2/(8n-4)-1/(8n-3)-1/(8n-2)`, `U_0=0`,
`U_{n+1}=16 U_n + r(n+1)`, and the four signed poles are unchanged. The frozen Main XVI seed-alias
record `research/2026-10-29/triangle_genesis_repair/SEED_ALIAS_CLASSIFICATION.md` is **not modified**;
PR #433's Wall's-theorem correction is carried as an additive erratum
(`research/2026-10-31/seed_superposition/RATIONAL_SEED_NORMALITY_ERRATUM.md`).
