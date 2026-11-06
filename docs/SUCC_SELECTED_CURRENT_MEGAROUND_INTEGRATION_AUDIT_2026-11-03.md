# Operation Selected-Current — integration audit (2026-11-03)

**Mandate.** Maintainer-authorized consolidation of the active SUCC research trunks, full
native validation, and merge of the *verified* integrated result into `main`. Research-only
new claims retain exact status. No tag, release, publication, license change, or force-push.
This document is the provenance record; it does **not** itself promote any mathematical status.

## 1. Baseline

- `main` at integration time: `81045770234a114247e43eb08ae5c6d446e9514a` (= the audit snapshot).
- `provenance/IMPORT_MANIFEST.json` git-blob: `a8805a8e4d64f35ff61937a36755d9b6d1ba3fae` (byte-identical before and after).
- Source contract (immutable, verified unchanged): `r(n)=4/(8n-7)-2/(8n-4)-1/(8n-3)-1/(8n-2)`, `U_0=0`, `U_n=16U_{n-1}+r(n)`, literal integer carries.
- Lean toolchain pin: `leanprover/lean4:v4.14.0`; mathlib bridge rev `4bbdccd9c5f862bf90ff12f0a9e2c8be032b9a84`.

## 2. The three trunks and merge topology

All three tips share merge-base exactly at `main 81045770`; the pre-main stack (#392–#455) is
already in main via Operation Main XIX.

| Trunk | Tip branch | Tip SHA | ahead | role |
|---|---|---|---:|---|
| A | `research/pi-selected-current-shift-coupling-2026-11-03` (#489) | `c0f9c3bb89c8cb473aa2c7edbd24b5ed20acf71d` | 117 | selected-current front + #465→#475→…→#488 current line |
| B | `research/figure-eight-pow2-hensel-2026-11-03` (#486) | `9eea9e3e89022b9a57716f21b31ffc3e69f0552f` | 156 | Möbius / E² / SU(2) / figure-eight sibling off #475 |
| C | `research/oily-hbar-moving-alias-vs-weyl-2026-11-02` (#472) | `85189e389ca1568636a7fedb7b2d6268b8eae447` | 161 | independent selected-prime / causal-response / oily-ħ off #459 |

Integration branch `integration/succ-selected-current-megaround-2026-11-03` built off fresh
`main`; merged A → B → C with `git merge --no-ff` (no cherry-pick, no rebase, no `-s ours`, no
force). Pre-doc-reorientation integrated head: `704e6847a8e747e38e44a014a6eb7b320f594769`.

**Result: purely additive — 412 added paths, 0 inherited files modified, 0 deleted** (`git diff
--name-status main HEAD` yields only `A` entries). Each merge was **conflict-free**.

**95-overlap resolution.** The audit flagged 95 path names shared between trunks A and B to
compare at the blob level. They are byte-identical, inherited from the shared `#475`
(`research/mesoscopic-spectral-army-2026-11-02`) ancestor — confirmed both structurally (both
trunks are add-only off a common ancestor; `git merge` reported 0 conflicts) and by spot-check
(`.../mesoscopic_spectral_army/PROOFS.md`, `.../line_sheet_gamma/PROOFS.md` identical across the
#486 and #489 tips). No historical theorem receipt was overwritten.

## 3. PR inventory and disposition

Ancestry of the integrated head covers the entire above-`main` π-frontier stack:

- **Included by ancestry (merged):** #459, #460, #461, #462, #463, #464, #465, #466, #467, #468,
  #469, #470, #471, #472, #473, #474, #475, #476, #477, #478, #479, #480, #481, #482, #483, #484,
  #485, #486, #487, #488, #489 (verified with `git merge-base --is-ancestor`).
- **Left open, NOT integrated:** #458 `research/selected-zero-boundary-signed-2026-11-01`
  (independent post-Main-XIX negative round off `main`; not an ancestor of any trunk). Correct per
  the mandate — unrelated experimental branches are not merged merely because open.
- Pre-main drafts #392–#455 are already content-merged via Main XIX (#456/#457).

Draft PRs are **not** auto-closed by this integration; disposition is annotated, not enforced.

## 4. Validation receipts (integrated head)

Native mandated checks, run with the compliant environment (`mpmath 1.3.0`, numpy 2.5.4,
sympy 1.14.0, scipy 1.18.1; `PYTHONPATH` = worktree; **not** `python -I`):

| Check | Result |
|---|---|
| `python scripts/verify_provenance.py` | `SOURCE_PROVENANCE_VERIFIED`, 72 items, exit 0 |
| `python -m unittest discover -s tests -p 'test_*.py'` | **Ran 11616 tests, OK, 0 failures / 0 errors / 0 skips**, exit 0 |
| `python scripts/observer_foundations_probe.py` | `OBSERVATIONAL_SUCC_FORMAL_FOUNDATIONS`, exit 0 (universal positivity `false`) |
| `python scripts/ordinal_succ_report_probe.py` | `FINITE_ORDINAL_SUCC_SECOND_ORDER_WEIL_PROBE`, exit 0 (definiteness `false`) |
| `scripts/check_selected_branch_lean.py` (representative) | `KERNEL_CHECKED` 10 theorems; 4 paired mutant controls reject; axiom export ⊆ {propext, Classical.choice, Quot.sound}; exit 0 |
| Lean diff `main`→integrated | **0 `.lean` / lakefile / toolchain files changed**; formal authority unchanged, no new Lean authority asserted |

Explicit hostile-control receipt (`tests.test_selected_current_front`, 15/15 OK): point-mass
cannot be made Haar by origin average (the `x=1/5` fixed-point firewall), immutable source,
`U_0=0` anchoring, forcing-crossing cap (SC-6), Gamma monotone-tail transport (SC-4), independent
odd-conductor source epochs (two blind evaluators).

## 5. Documentation reorientation (this commit)

- Regenerated `docs/math_memory/CLAIM_CATALOG.json` **last** (`build_math_memory.py --write`;
  `--check` now exit 0) — refreshed source-document index 1792 → 2003 entries from the new
  research. The 170 `NO EXACT NAMESPACE` warnings are **pre-existing on main** (byte-identical
  warning set and count) and out of scope for this integration; they are not errors and no
  check gates on them.
- `README.md`: added the active π current-front pointer; corrected pre-existing stale
  math-memory counts to the true values (48→51 nodes, 56→60 relations, 1876→1997 rows).
- `docs/PI_SELECTED_CATEGORICAL_FRONTIER.md`: cross-linked the parallel branch-current front,
  stating the band gate is a **strictly sufficient** estimate for the `J` route (`band⟹J`), sharing
  the same open high-frequency core — not a proven equivalence and not a second route (corrected
  2026-11-03; converse `J⟹band` is false, see `research/2026-11-03/renorm_transport/PROOFS.md` RT-00).
- `docs/ROADMAP.md`: added the dated operation entry.
- `docs/PI_BRANCH_CURRENT_FRONTIER_2026-11-03.md` (added by trunk A) is the active concise front.

No archival research proof was edited for editorial consolidation.

## 6. Research labels preserved (firewall intact)

**Proved/conditional (carried in):** arithmetic 2-adic isometry; quadratic Gaussian/real source
gluing; Gamma endpoint transport; exact split/inert prime denominators and nonrepeat; the
conditional log-mesh normality gate (#476); the exact source-selected current branch-square
decomposition (#488) and the new shifted-bin comparison (SC-1..SC-8).

**OPEN (not proved):** the actual source-selected real near-pair/carry/cofactor bound; the signed
second moment `Σ_{1≤|h|≤q_A²}|c_A(h)|²=o(K_A)`. **Correction (2026-11-03, see
`research/2026-11-03/renorm_transport/PROOFS.md` RT-00):** these are linked by a **one-directional
sufficiency chain** `band=o(K_A) ⟹ J_{A,m_A/2}=o(K_A) ⟹ E_{A,m_A}=o(log m_A) ⟹ π base-16 normal`,
**not** a ring of equivalences. The generic converse `J=o(K) ⟹ band=o(K)` is **false** (equally-spaced
cloud: `J=1`, unweighted band `=2q`). Only the Green-tail reduction is a biconditional:
`π base-16 normal ⟺ S_N(h)=o(N)` for every fixed nonzero `h`. **π base-16 normality** is OPEN; RH is a
separate OPEN program.

**False shortcuts (retained as corpses):** "Galois average implies the selected embedding";
"periodic branch inverse implies Haar"; "uniform current minimum is the actual source law";
"nonrepeat implies 1/log A real spacing"; "finite π-prefix shadow means infinite normality".

## 7. New sub-result this round (draft research, separate branch)

**RENORM-1** (source renormalization identity): `c_A(h)=c_A(16h)+ε_A(h)` with
`|ε_A(h)|≤2/A+(15π/32)|h|/A²`, where `c_A(h)=A^{-1}Σ_{n=A}^{2A-1}e(hU_n)`. Rigorous from
`hU_n=16hU_{n-1}+hr(n) (mod 1)` plus the SC-6 numerator bound `r(n)<15/((8n-7)(8n-6))`.
Verified on held-out epochs `A∈{40,64,128,256}`, `h∈{1,…,50}` (worst error/bound ≈ 0.94), with
the independent odd-conductor source agreeing to 0. **RENORM-2** (barrier corollary): since `h↦16h`
is injective on frequencies, iterating the identity transports the low band onto an
equal-cardinality high band, so single-frequency transport alone cannot drive the SC-8 band
second moment to `o(K_A)` — the needed cancellation is a genuine high-frequency equidistribution
input. This is an obstruction map, not progress on the estimate. Published only as a **draft
research PR** with its own receipts; **no status promotion**, π normality remains OPEN.
