# Operation Main XXI — integration audit (2026-11-07)

**Mandate.** The maintainer authorized this research integration into `main` and the closing
of PRs whose content main already carries. Both were gated on full native validation and
on green hosted CI at the exact integration head. Nothing outside that was authorized or
done: no tag, release, publication, license change, history rewrite or force-push. This
document is the provenance record. It promotes no mathematical status.

**π base-16 normality: OPEN. Selected signed Weyl gate `S_N(h)=o(N)`: OPEN. RH: OPEN.**

## 1. Baseline and frozen invariants

- **Fresh `main`.** `d32342d375f44ddf62221ad6aff2f534abdc0a03`, the merge of PR #523. It
  was re-fetched before the integration branch was cut, and again before the merge.
- **`provenance/IMPORT_MANIFEST.json`.** Git blob `a8805a8e4d64f35ff61937a36755d9b6d1ba3fae`,
  byte-identical before and after. The `formal/`+`provenance/` tree listing hashes to
  `82c6cf9fb4e30a8c42e58716e661d4bec6151c86` before and after.
- **Source.** `r(n)=4/(8n-7)-2/(8n-4)-1/(8n-3)-1/(8n-2)`, `U_0=0`, `U_n=16U_{n-1}+r(n)`.
  No source file was touched.
- **Formal.** No `.lean`, lakefile or toolchain file changed, so no formal certificate is
  inherited for new content. Lean pin: `leanprover/lean4:v4.14.0`; mathlib `4bbdccd9`.
- **Environment.**
  - Python 3.13.13 and 3.10.20 venvs, both with mpmath 1.3.0 and sympy 1.14.0. numpy is
    2.5.4 on 3.13 and 2.2.6 on 3.10; scipy is 1.18.1 and 1.15.3. These are the same pins
    `pip install -e '.[test]'` resolves in CI.
  - Runs used `PYTHONPATH=<worktree>` and never `python -I`.
  - Commits in this round are authored as `femboy2112` with the account's GitHub noreply
    address.

## 2. The DAG, rebuilt from Git rather than from the planning schematic

There were 125 open PRs at reconnaissance (a paginated `gh pr list --limit 500`).
`scripts/branch_inventory.py` classified them:

- **106 are incorporated by ancestry.** Each head is already an ancestor of `main`. The
  integration merge that first carried each one was found by bisecting `main`'s
  first-parent chain:

  | Carrying merge | PRs carried |
  |---|---|
  | #425 `e8598cfa` | 26 |
  | #436 `4eb411e3` | 7 |
  | #456 `eb4f69b6` | 17 |
  | #490 `a673ec95` | 29 |
  | #523 `d32342d3` | 27 |

  The per-PR destination commits are in the manifest (§3).
- **19 were pending.** They reduce to **7 ancestry-minimal leaves**:

| Leaf | Head merged | Carries |
|---|---|---|
| #540 | `298f60d8` | #525, #526, #527, #528, #530, #531, #533, #536, #538, #540 |
| #532 | `f6560d93` | #525–#528, #530, #531, #532 (adds only #532's own commits) |
| #535 | `a265269a` | #525–#528, #529, #534, #535 |
| #537 | `5dad2bd4` | #537 |
| #539 | `c8c5cf04` | #539 |
| #543 | `92b98bc0` | #541, #543 |
| #542 | `a8f592b8` | #542 (an independent sibling of #541) |

**Corrections to the planning schematic.**

- The schematic listed the chain `#529→#530→#531→#533→#536→#538→#540`. In Git, #529 and
  #530 are **siblings**, both based on #528's branch.
- The real shape is
  `#525→#526→#527→#528→{#529→#534→#535, #530→#531→{#532, #533→#536→#538→#540}}`.
- #518 and #520–#524 were already in `main` through Main XX.

**Merge mechanics.**

- Branch `integration/succ-main-xxi-pinbed-reunification-2026-11-07` was cut from fresh
  `main`.
- Merge order: #540 → #532 → #535 → #537 → #539 → #543 → #542. Every merge was
  `--no-ff` and **conflict-free**. There was no rebase, cherry-pick, `-s ours` or force.
- Before each merge, the live PR head was compared with the inventory JSON, and every
  merged second parent was verified against it.
- The research-only staging tree, after the seven merges, is
  `987b002826afd3a725da7a95dcf9ab146f340757`.

**Overlaps.** Measured three-dot from each leaf's merge-base, there are 258 cross-leaf path
overlaps. **All 258 are byte-identical blobs** inherited from shared ancestors. The diff
against `main` is **332 added paths, 0 modified, 0 deleted**.

**PR-less branches.** `research/final-pin-{carry,clausen,referee}-2026-11-05` are not
ancestors of `main`. However, all 34 of their files are **byte-identical** in `main` under
`research/2026-11-05/selected_orbit_final_pin/` (folded into #520). They are recorded as
content-preserved, and the branches are retained.

## 3. Coverage manifest

- **Coverage manifest.**
  [`SUCC_MAIN_XXI_INTEGRATION_MANIFEST_2026-11-07.json`](SUCC_MAIN_XXI_INTEGRATION_MANIFEST_2026-11-07.json)
  lists every reviewed PR with its disposition: INCORPORATED_BY_ANCESTRY, INTEGRATE or
  INTEGRATE-SCOPED. For each it gives the exact head, destination commit or staging
  commit, own commits and files, and the audit summary. It also covers the three PR-less
  branches.
  - Ancestry is **re-proved by `git merge-base --is-ancestor` at generation**, not copied
    from this text.
  - Its `staging` field is the development head at generation (`9d828c77`). The final
    head descends from it.
- **Raw inventory.**
  [`SUCC_MAIN_XXI_BRANCH_INVENTORY_2026-11-07.json`](SUCC_MAIN_XXI_BRANCH_INVENTORY_2026-11-07.json)
  is the `branch_inventory.py` output against the integration head. It reports all 125
  open PRs as ancestors (exit 0).

**Closure policy.** Closure happens after the merge of this integration and the green CI
on `main`.

- **Comments first.** Each closed PR receives a comment naming the exact commit in
  `main` that carries its head, and stating that no unique evidence is discarded.
- **Branches.** No branch is deleted.
- **No mass close.** Closure applies only to PRs whose head is proved to be an ancestor of
  `main`.

## 4. Mathematical audit (no promotion)

Bearings: every review was same-model and read-only.

- **Pin-bed cluster.** Two blind bearings: a proof audit (Lagrange) and an adversarial
  refutation (d'Alembert).
- **Every other cluster.** One proof auditor each: #525–#529/#534/#535, #530–#540, and
  #537/#539.
- **Receipt replay.** A separate receipt replay ran every research-directory test and
  receipt command (§6).

**Result: 19/19 integrate — 8 INTEGRATE (#525, #528, #531, #532, #533, #535, #536,
#541) and 11 INTEGRATE-SCOPED. Nothing was DEFERRED or BLOCKED.** Every scope correction is
a wording, label, identifier, provenance or test-coverage correction. **None is a
mathematical refutation of an incoming theorem.** The corrections are recorded as scope
notes in [`CLAIM_SUPPLEMENT_MAIN_XXI.md`](CLAIM_SUPPLEMENT_MAIN_XXI.md). The original
dossiers are byte-identical: they are research history, so this round did not rewrite them.

**Load-bearing checks that came out the same way independently.**

- **#538's "o(1)" is a transport error, not a gate estimate.** ET1 is
  `|√C^z−√C^x| ≤ (π/(15A²))√(H(H+1)(H+2)/6)`. It relates two quantities, neither of which
  is bounded. #540's `O(A⁻²)` is likewise a difference of fixed-aperture energies.
  **No PR proves an unconditional source-selected `o(1)` for the open gate.**
- **The ×16 constant is sharp.** `C₁₆(½)=341/√205` (real laws). The proof auditor found it
  by three routes, and the adversary found it again by an `h≤20000` scan. It is attained,
  hence sharp. On complex inputs the norm is `31`.
- **Learning does not imply normality.** With the forcing set to zero, a maximally
  non-normal source, the #542 learner behaves identically.
- **Provenance: #527 is a rederivation.** It independently rederives main's 2026-10-27
  2-adic zero boundary (`bbp_binwindow_conjugacy.py`, `bbp_two_adic.py`). Its new content
  is DB10 and the DB-06/DB-07 countermodels.
- **AGENTS.md rule 3: #534's "physically admissible" wording.** "Physically admissible
  plane" names the definitional seam `U=C+x`.
- **One headline denominator bound.** #532's `5≤liminf log d_n/n≤limsup≤8` supersedes
  #534's `≥2` on the same `d_n`. Neither is zero-seed selective.

## 5. Integration-time additions

| Commit | What | Why |
|---|---|---|
| `a3169835` | `research/2026-11-07/main_xxi_receipts/` receipt R1, plus `tests/test_main_xxi_ga09_receipt.py` | #540 labels GA-09 REFUTED with no countermodel. Under METHOD.md that label is otherwise not permitted. R1 is a uniform arc grid with `B_A(t)≤A+3A²t` for all `t`, yet `E_a→√5/9−1/6>0`. It is an elementary proof plus exact `ℚ(√5)` rows at `A=50,200,800`. |
| `02b211cc` | `tests/test_main_xxi_pinbed_hardening.py` (17 tests) | The adversary demonstrated five wrong implementations that passed all 84 original pin-bed tests. Each now fails at least one new test: M1 fails 3, M2 4, M3 3, M4 1, M5 3. The mutant table was re-run independently at integration. |
| `9d828c77` | `observational_succ/gram_mobius.py` scoped precision, plus `tests/test_precision_isolation_main_xxi.py` | The import-time `mp.mp.dps=50` raised every importing process's precision (measured 15→50). Values are bit-identical, and the new test fails on the old module. |

- **Withdrawn during integration (the record keeps it).** A precision-restoring decorator
  on `prime_form_heat` (23 functions) was tried and **reverted**. It made 7 of 60 tests
  fail. Six of those compute their reference values at leaked ambient precision. The
  seventh replays the pinned receipt `research/2026-10-14/PRIME_FORM_HEAT_RECEIPT.json`,
  whose stored numbers were produced at leaked precision. Repairing it needs those
  references rescoped and the receipt regenerated under provenance. It is deferred, with
  this exact blocker.
- **Withdrawn claim.** I first said `test_gram_mobius.test_T2` was order-dependent. A
  sweep of ambient dps 5..300 against the old module found **no** failing precision (the
  `log 2` scalings are exact in binary), so that claim is withdrawn.
- **Observed, not committed.** Run as documented with `--include-4096` (46.6 s on this
  machine), #540's `A=4096` golden interval gives
  `E∈[0.00015731538591, 0.00015731538592]` with pair count 12817828. The dossier's
  "TIMEOUT / NOT COMPUTED" is stale for this hardware. This is recorded as MXXI-25
  (OBSERVED-FINITE). The dossier is not edited.

## 6. Research-receipt replay

An isolated detached worktree at `987b0028` ran 26 targets: the 19 new research
directories plus the 7 new top-level test modules.

- **Overall result.** 0 test failures and no numeric result changed. A type-strict JSON
  comparison found zero mismatches on shared keys.
- **One genuine defect.** `research/2026-11-06/holographic_triangle/independent_run.sh`
  calls a `receipt.py` that has never existed in any commit. Under `set -eu`,
  `python receipt.py > FINITE_RECEIPT.json` truncates the tracked receipt. The committed
  receipt itself is consistent (17 sha256 pins match). **Do not run that script.** It is
  left unedited and flagged here and in the handoff.
- **Environmental differences.**
  - Two render scripts need matplotlib, which is not a declared dependency.
  - `joint_character_entropy/fresh_holdout_probe.py` opens a file relative to the cwd.
  - The `LOCAL_TEST_STDERR.txt` timing lines are hashed into two receipts, so those
    receipts drift with wall time by design.
- **Provenance weaknesses.**
  - Several tracked `FINITE_RESULTS`-style JSONs carry hand-written keys that no
    documented command emits (`spectral_exorcism`, the Galois selector,
    `critical_collision` `HOLDOUT_N4096`). The numbers agree on the shared keys.
  - The `joint_character_entropy` receipt pins a test log that records 29 tests; there
    are now 33.

## 8. Interface for parallel research

See [`CODEX_HANDOFF_MAIN_XXI.md`](CODEX_HANDOFF_MAIN_XXI.md). It covers:

- the canonical exact APIs to import;
- the pin-bed sign conventions, which do not compose verbatim;
- the precision hazards;
- the do-not-run script;
- test discipline;
- the three hostile controls a proof must survive.

## 10. Next integration round (Main XXI+)

1. **`prime_form_heat` precision repair.** Rescope the six leak-dependent tests, then
   regenerate `PRIME_FORM_HEAT_RECEIPT.json` with a provenance note. After that, the other
   14 modules with unrestored `mp.mp.dps` assignments, in order of test reach.
2. **Forcing and tail consolidation.** The census found 25 value-identical forcing copies
   and 5 identical tail enclosures in `observational_succ/`. They could delegate to
   `duck_bbp` behind thin wrappers that keep their exception types and domain guards.
   Excluded from consolidation:
   - the independent oracles: `pinbed_oscillator_bridge.four_pole` and the oracle
     scripts;
   - `gamma_bbp_signed_coherence`, whose tail enclosure is tighter than `duck_bbp`'s.
3. **Research-directory replay.** `research/**/test_*.py` is not part of
   `unittest discover -s tests`. A replay gate that runs from each directory would have
   caught the holographic script and the stale test count automatically.
4. **CI consolidation.** The repository has 141 workflow files. Measure per-workflow
   duplicate coverage before merging any of them. No CI file was changed in this round.
5. **The 872 remote branches.** Archive by manifest only, and never delete a branch whose
   commits are not reachable from `main`.
