# Operation Main XVIII — validation and integration receipt

**Date:** 2026-10-31 (New York) / 2026-11-01 UTC. **Status:** faithful integration of the ten open
research PRs #426–#435 into four ancestry-minimal leaves, with a three-cluster firewall audit, full
reconciliation of the known engineering/mathematical traps, and a compliant full validation, delivered
through a reviewed PR for an authorized merge to `main`. No publish, tag, release, force-push, archive
rewrite, frozen-source change, or workflow change. **No mathematical status promoted. π base-16/base-2/
base-3 normality, the signed Weyl gate `T_N(h)=o(N)` (`Sbar_N(h)=o(1)`), RH, Weil positivity, general
Collatz, and shifted Lonely Runner `n=18..94` remain OPEN.**

## 1. Before / after

| | SHA |
|---|---|
| `main` before | `e8598cfa5d32fd1de8e94a3e458a366a0850d59e` (Operation Main XVII) |
| Integration branch | `integration/succ-main-xviii-signed-frontier-2026-10-31` (from `origin/main`) |
| Leaf-merge head (pre-integration-commit) | `2f43c81a` |
| `main` after merge | _recorded on the PR after the authorized merge_ |

## 2. What was integrated

Four ancestry-minimal leaves, ancestry-preserving `--no-ff`, **zero conflicts**, subsuming all ten
open PRs #426–#435:

| leaf | role | subsumes |
|---|---|---|
| PR #426 | Cluster A — counterfactual triangle carrier | — |
| PR #430 | Cluster B tip | #427, #428, #429 (git ancestors) |
| PR #432 | Cluster C sibling — edge-seed tomography | — (own history preserved) |
| PR #435 | Cluster C tip | #431, #433, #434 (git ancestors; #432 byte-identical, reconciled) |

Overall diff vs `main`: **149 files, +14264 / −0** — purely additive. The content lives under
`research/2026-10-31/{counterfactual_triangle, two_three_joint_carrier, pascal_crossprime,
half_power_horizon, multiplace_bbp_difference, carrier_path_measure, edge_seed_tomography,
seed_superposition, selected_lag_tomography, signed_lag_fireworks}/`, this `main_xviii/` dossier, and
19 new test files. The **only canonical-file change** is an additive `## 7.` section in
`docs/PI_SELECTED_CATEGORICAL_FRONTIER.md`, plus the additive Main XVIII nav blocks in
`docs/CLAIM_INDEX.md`, `docs/ROADMAP.md`, `docs/math_memory/INDEX.md` and the regenerated
`docs/math_memory/CLAIM_CATALOG.json` (regenerated last). No change to `observational_succ/`,
`formal/`, `scripts/`, `provenance/`, `.github/`, `ci.yml`, the frozen BBP source, `IMPORT_MANIFEST`,
`U_0=0`, or the four signed poles.

## 3. DAG and byte-copy reconciliation

`#430` subsumes `#427–#429` (verified ancestors). `#435` subsumes `#431/#433/#434`, but **not** `#432`
(a sibling of `#433` off `#431`). PR #434/#435 carry byte-for-byte copies of PR #432's eleven files;
all eleven have identical git blob hashes in `#432`, `#434`, and `#435`. Merging `#432` first
(preserving its tomography commits) then `#435` yields an identical add/add that git resolves with no
conflict — no competing copy, no `-s ours`, no duplication. Full DAG: `MAIN_XVIII_PROVENANCE_DAG.md`.

## 4. Engineering/mathematical reconciliations (directive Phase 3)

- **Module-name collision:** every research oracle/module is loaded by a unique
  `spec_from_file_location` name; no bare `import independent_oracle` exists. All 228 new tests pass in
  a single process in both forward and reverse order.
- **Seed provenance vs normality (Wall):** PR #433's `RATIONAL_SEED_NORMALITY_ERRATUM.md` carries the
  classical Wall correction additively; the frozen Main XVI record
  `research/2026-10-29/triangle_genesis_repair/SEED_ALIAS_CLASSIFICATION.md` is **not** modified.
- **Phase-magnitude vs signed-real:** the inherited clipped-lag helper bounds `|D|`, not `Re D`; the
  counterexample `(N=2,k=1,h=4,s*=−π/16)` is reproduced at 60 digits, no consumer uses the clip as a
  signed bound, and `test_signed_lag_fireworks_audit.py` pins the behavior. The helper is preserved
  unmodified (history not rewritten); a docstring/rename is left to a later PR.
- **Source labels vs literal state:** `U_0=0` is the literal start in the code; `interval_oracle.py`'s
  combined rational was proved equal to the four poles symbolically; a source-label string does not
  authenticate the seed and a test shows the label is identical for `s=0` and `s=1/7`.
- **Finite tomography aliasing:** the 73-point detector is exact at nine time modes under its stated
  frequency conditions; explicit alias checks are preserved (`16^9≡1 mod 73`).
- **Paper proofs vs Lean:** `formal/` is byte-identical to `main`; no paper proof is claimed as Lean-
  certified.

## 5. Audit verdict

Three independent read-only reviewers (one per cluster) re-derived the load-bearing algebra, re-ran the
committed probes with the compliant interpreter, and checked the firewall wording; the principal
resolved the DAG, reconciliations, invariants, and catalog mechanics. **Firewall intact across all
three clusters; Cluster A INTEGRATE-SCOPED, Cluster B INTEGRATE-SCOPED, Cluster C INTEGRATE; no DEFER.**
Full registry + countermodel ledger + scoping caveats: `MAIN_XVIII_CLAIM_REGISTRY.md`. The caveats are
documentation-hygiene only (claim-ID prefix overlap/registration, two malformed ledger tables, two
stale test counts, one wording over-sell, one helper docstring), all confined to quarantined
`research/` dirs; none changes repo-wide status.

## 6. Validation (local, on the integration head)

All AGENTS.md gates rc=0; full suite **Ran 10253 tests — OK, rc=0** (zero failures/errors/artifacts);
228 focused tests in both orders OK; committed receipts reproduced exactly; invariants byte-identical.
Details: `MAIN_XVIII_VALIDATION.md`. The §1 `main`-after SHA and the hosted exact-head CI result are
filled from the authorized merge and the PR head run.

## 7. Mathematical status (unchanged; no promotion)

The new round sharpens the time-correlated gate: a certified source-transport error at
`K=⌊log_4 N⌋` and a proved gate **equivalence** (a criterion), with a sharp hostile barrier `(1−2/c)²`
and two nonnormal counterexample families — all negative or criterion results. The **selected
zero-boundary signed asymptotic estimate** for every fixed nonzero `h` is OPEN; a route must use the
exact `U_0=0` boundary and diagonal rationality, which no forcing-only argument supplies. π normality,
the signed Weyl gate, RH, Weil positivity, general Collatz, and shifted Lonely Runner `n=18..94` remain
**OPEN**. Main XVIII promotes no mathematical status and supplies no signed cancellation.
