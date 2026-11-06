# Operation Main XX — integration audit (2026-11-05)

**Mandate.** This was a maintainer-authorized, research-only integration into `main`, gated on full native validation and on hosted CI at the exact integration head. No tag, release, publication, license change or force-push was authorized or done. This document is the provenance record. It promotes no mathematical status.

**π base-16 normality: OPEN. Selected signed Weyl gate `S_N(h)=o(N)`: OPEN. RH: OPEN.**

## 1. Baseline and frozen invariants

- **Fresh `main`:** `a673ec95dfac4ef6a61c60222be8b615fd08535d` (merge of PR #490). It was re-fetched immediately before integration.
- **`provenance/IMPORT_MANIFEST.json`:** git-blob `a8805a8e4d64f35ff61937a36755d9b6d1ba3fae`, byte-identical before and after.
- **Source:** `r(n)=4/(8n-7)-2/(8n-4)-1/(8n-3)-1/(8n-2)`, `U_0=0`, `U_n=16U_{n-1}+r(n)`. Unchanged; no source file was modified.
- **Formal:** no file under `formal/` changed, and no lakefile or toolchain changed.
  - One research scratch file, `research/2026-11-04/europa_weyl/weyl/CocycleScratch.lean`, arrives with #500. It sits outside every lake project and carries no formal authority.
  - Lean pin: `leanprover/lean4:v4.14.0`; mathlib `4bbdccd9c5f862bf90ff12f0a9e2c8be032b9a84`.

## 2. P0 — the confirmed CI failure on #521, repaired

- **Symptom.** PR #521's exact-head workflow run `42141608952` failed on Python 3.10 and 3.13. Two tests in `tests/test_relative_zero_scale.py` failed, test_04 and test_05, with errors `3.16511540451680146402350332873227947171e-38` and `2.40741243048404481631997242823115914817e-35` against a `1e-43` tolerance. #522 failed identically (run `42149681980`).
- **Root cause, reproduced bit-exactly.**
  - The test set `mp.mp.dps=55` only at import time.
  - The helpers in `observational_succ/prime_form_heat.py` assign `mp.mp.dps=dps` globally.
  - `tests/test_prime_form_heat.py`, which sorts alphabetically earlier, last calls them with `dps=36`.
  - Running `python -m unittest tests.test_prime_form_heat tests.test_relative_zero_scale` reproduces the identical assertion strings. The reverse order passes. An ambient-dps sweep matches CI at exactly `dps=36`.
- **Repair.**
  - Commit `95490b46` on #521:
    - every mpmath evaluation now runs in `mp.workdps(55)`;
    - tolerances are **unchanged** and no test is skipped;
    - a regression class `AmbientPrecisionHostile` reruns the checks at ambient dps 15/36/40/120 (the original file fails it);
    - two tautological assertions (test_01 and test_03) were strengthened to evaluate the actual quantities. The originals are retained.
  - Merged forward into #522 as `cd672158`.
- **Leak left in place.** The global-state leak in `prime_form_heat.py` (on main since `53934b3a`) is documented, not modified.
- **Hosted CI after the repair:** #521 `95490b46` **19/19 pass**; #522 `cd672158` **19/19 pass**.

## 3. The DAG (rebuilt from Git, not from titles)

- **Open PRs at reconnaissance:** 112.
  - **79** (#392–#489 range) already have their head as an ancestor of `main`. Their disposition is *superseded by an earlier integration*. They are left open; closing them was not requested.
  - **33** were pending. They reduce to **10 ancestry-minimal leaves:**

| Leaf | Head merged | Carries open PRs |
|---|---|---|
| #491 | `e21ff757` | #491 (×16 renormalization; corrects the last integration's false `band⇔J` equivalence) |
| #522 (+#521 repair) | `cd672158` | #493, #496, #497, #499, #500, #502, #504, #506–#509, #511–#514, #518, #520, #521, #522 |
| #519 | `cac24927` | #515, #516, #517, #519 (RH/prime-jet track; shares #493…#513 with #522) |
| #505 | `00b6385b` | #501, #503, #505 (Gamma Prybar → critical chirp → source audit) |
| #510 | `f7060c81` | #510 (sibling off #508) |
| #492 | `a61a3968` | #492 |
| #494 | `d5b2fbbd` | #494 |
| #495 | `b96befcb` | #495 (forked from #494's first commit `ed195a1b`; its test fix is the **identical blob** `4b32cb63` as #494's `d5b2fbbd`, a convergent fix, not a conflict) |
| #498 | `24703021` | #498 |
| #458 | `4199edb0` | #458 (independent post-Main-XIX negative round) |

- **New this round:** #524 `8da6eefb`, the Main XX proof forge (§6), stacked on `cd672158`.

**Merge order and mechanics.** On a fresh-`main` branch `integration/succ-main-xx-history-first-2026-11-05`, the order was #491 → #522 → #519 → #505 → #510 → #492 → #494 → #495 → #498 → #458 → #524.
- All merges were `--no-ff` and **conflict-free**. There was no rebase, no cherry-pick, no `-s ours` and no force.
- Every merged second parent was verified against the live PR head SHA. One mistyped SHA during the operation was rejected by git ("not something we can merge"); nothing was merged from it, and it was corrected from the PR JSON.

**Cross-leaf overlaps.** There are 730 path overlaps, computed from each leaf's merge-base (three-dot). **All 730 are byte-identical blobs** inherited from shared ancestors: #510∩#519, #510∩#522 and #519∩#522 share #493…#508/#513, and #494∩#495 share 6 paths. No divergent re-add exists.

**Machine-readable inventory.** [`docs/SUCC_MAIN_XX_BRANCH_INVENTORY_2026-11-05.json`](SUCC_MAIN_XX_BRANCH_INVENTORY_2026-11-05.json), generated by `scripts/branch_inventory.py`. It records, for every open PR, the head, base, merge-base, own commits, own changed files with blob ids, containing leaves and exact-head CI conclusions.
- It covers 113 open PRs. The integration PR #523 is itself excluded, so that it does not swallow every leaf.
- 34 PRs are pending (the 33 above plus #524), reducing to the leaves #458, #491, #492, #494, #495, #498, #505, #510, #519 and #524. The latter carries #522.
- The CI fields are a snapshot taken at generation time. #524 was still running.
- Many intermediate stacked heads show `cancelled` full-suite runs: the workflow cancels a run when a descendant is pushed. Validation authority lies with the leaf heads (all green; #521/#522 green after the repair) and with this integration head.

## 4. Changes beyond pure additions

- `docs/PI_SELECTED_CATEGORICAL_FRONTIER.md` and `docs/SUCC_SELECTED_CURRENT_MEGAROUND_INTEGRATION_AUDIT_2026-11-03.md` — from #491. They correct the previous integration's unsupported `band⇔J⇔Weyl` equivalence to the proved one-directional chain.
- `README.md` — the "start here" pointer now goes to the single π entrypoint; earlier fronts are kept as history.
- `docs/ROADMAP.md` — the Main XX entry, prepended.
- `docs/PI_BRANCH_CURRENT_FRONTIER_2026-11-03.md` — a one-line navigation note only; content unchanged.
- `docs/CLAIM_NAMESPACE_REGISTRY.json` — registers `MAIN_XX_FORGE` (`MXX`).
- `docs/math_memory/CLAIM_CATALOG.json` — regenerated last with `build_math_memory.py --write`.

**No inherited file was deleted. No archival proof was edited for consolidation.**

**`git diff --check` vs `main`.**
- It reports 6 trailing-whitespace lines. All are inherited from original research commits:
  - `6ef791ee` gamma_pigeonhole/VALIDATION.md
  - `81fc24da` prime_character_primal/PROOFS.md
  - `117e70ef` critical_carry_jets/NEXT.md
  - `2e8f20f0` gamma_sphere_solenoid/NEXT.md
  - `8df33cf7` infinite_qubit_field/THEOREMS.md
  - `ff73b2d7` tests/test_source_sound_calculus.py
- They are **preserved byte-identically by design**. `prime_character_primal/PROOFS.md` is sha256-pinned in three receipts (europa_weyl/ARCHIVE_RECOVERY.json, prime_character_primal/TESTED_FILES.json, zero_frame_coupling/SOURCE_HASHES.json).
- CI does not gate on whitespace.
- All commits authored in this operation are `--check` clean.

## 5. Mathematical status audit (no promotion)

Every integrated leaf keeps its own labels. In particular:
- **#491 (RT-00):** `band⟹J⟹E⟹normal` is one-directional, and the converse `J⟹band` is false.
- **#519:** a local H¹/Volterra bound is **not** completed Weil positivity.
- **#513/#501:** microscopic collision bounds are not equidistribution.
- **#522 HS-08:** a low-predictive-error observer policy is not arithmetic typicality.

The single maintained π entrypoint, [`docs/PI_NORMALITY_FRONTIER.md`](PI_NORMALITY_FRONTIER.md), separates five things: the authenticated source; the proved exact theorems; the sufficient-but-open gates; the no-go theorems and countermodels; and the orthogonal tracks. It also states the precise next theorem.

## 6. This round's research (#524)

See [`research/2026-11-05/main_xx_forge/README.md`](../research/2026-11-05/main_xx_forge/README.md) and [`CLAIM_SUPPLEMENT_MAIN_XX_FORGE.md`](CLAIM_SUPPLEMENT_MAIN_XX_FORGE.md).
- The strongest rigorous results are the exact carry–interval identity (MXX-01) and the conditional stationary-rigidity transport (MXX-03/04).
- The same-forcing non-stationary countermodel (MXX-05) refutes "critical-carry J ⟹ normality" and "Clausen ≤ C·carries".
- #520's finite-cut Clausen inequality is identified exactly as the Weyl gate (MXX-09).
- Front C's de-sourcing and classification results are MXX-13 to MXX-15.
- A hostile same-model crucible is archived; these reviewers are not independent scholarly referees.
- **No unconditional source-selected estimate was obtained.**

## 7. Validation receipts at the integration head

**Validated content head:** `85b6a912d496307d7012c853062595b4720256de`. The final integration head equals this tree plus this section only. A document cannot carry the CI result of its own commit, so hosted CI on the final head is recorded on PR #523 and in the merge commit, and was required green before merge.

Local runs used the compliant venv (mpmath 1.3.0), `PYTHONPATH=<worktree>`, and no `python -I`. The tree was clean before and after every run.

| Gate | Command | Result at `85b6a912` |
|---|---|---|
| Provenance | `python scripts/verify_provenance.py` | `SOURCE_PROVENANCE_VERIFIED`; 72 items; source commit `ba075348b7bcc66d938b3e0ca96c26e95bba340a` |
| Full suite | `python -m unittest discover -s tests -p 'test_*.py'` | `Ran 12147 tests in 1371.489s` — **OK**, exit 0. HEAD was identical at start and end, with 0 dirty paths. |
| Observer probe | `python scripts/observer_foundations_probe.py` | exit 0 |
| Ordinal probe | `python scripts/ordinal_succ_report_probe.py` | exit 0 |
| Focused | `python -m unittest tests.test_relative_zero_scale tests.test_selected_orbit tests.test_main_xx_forge tests.test_prime_form_heat` | `Ran 117 tests` — OK |
| P0 hostile order | `python -m unittest tests.test_prime_form_heat tests.test_relative_zero_scale` | `Ran 69 tests` — OK. Before the repair, this order reproduced the CI failure. |
| Admissibility law | `research/2026-11-05/main_xx_forge/front_b/admissibility_law.py` | `CERTIFIED-FINITE`, `d∈[2,200]`, 0 exceptions |
| Front receipts | rerun byte-identically | A `b9df1aa66c4c50a3…dd37c4`; B `8e053b8a48dc9067…ae3f`; C `d32549df2ec9ad66…d73e` (sha256) |
| Lean | `python scripts/check_selected_branch_lean.py` | `KERNEL_CHECKED`: 10 theorems; 4 paired mutant controls, all exit 1 as required |
| Claim catalog | `python scripts/build_math_memory.py --check` | exit 0. Claim rows 2013, namespaces 177. Warnings stay at 170, unchanged from `main`. |
| Whitespace | `git diff --check a673ec95...HEAD` | 6 lines, all inherited and pinned (§4) |
| Frozen invariants | blob compare vs `main` | `IMPORT_MANIFEST.json` blob `a8805a8e…` unchanged; 0 `formal/` paths; 698 added and 7 modified paths (§4); 0 deleted |
| Hosted CI | PR #523 at `85b6a912` | Every job passed, including `Python 3.10 mathematical and epistemic checks` and `Python 3.13 mathematical and epistemic checks` (run `42164161293`) |

The suite's stderr contains `STALE/MISSING mathematics catalog: /tmp/…`. This is expected output from a negative test that runs on a temporary copy, and it appears identically in the earlier green runs.
