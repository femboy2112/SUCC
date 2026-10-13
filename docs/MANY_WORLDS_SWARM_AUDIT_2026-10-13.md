# Many-worlds swarm consolidation audit (2026-10-13)

Canonical record of the 2026-10-13 "great consolidation": the VOYAGER-rooted
48+12 many-worlds swarm plus its carrier/no-ghost/positive-carrier/Cambrian/
evolutionary-obstruction/cegis lineages, audited and integrated into `main`.
Read this instead of the swarm's hundreds of per-mission dossiers or any prior
AI conversation. Status labels follow docs/METHOD.md (Disclosed / Corroborated /
Observed / Conjectured / Refuted). **This document establishes no mathematical
truth by itself; it records what was verified and how.**

## 1. What landed and how it was assembled

A Codex swarm produced ~60 local worktrees under `/home/leah/succ_lab/` on top of
`research/voyager-observational-profinite-completion-2026-10-13` (`5eb09e7`), the
common trunk. The lineages, by ancestry (not the stale external PR map):

- **Atlas trunk** (`research/many-worlds-atlas-2026-10-13`, local tip `80a53d2`,
  +239 commits on `main 52d2c02`): the 48 first-generation SWM missions (A01–F48,
  X01–X12) + 12 syntheses, assembled as per-mission dossiers/probes/receipts under
  `research/2026-10-13/SWARM_ATLAS/`, with VOYAGER, the three `eodcs-*` branches,
  and the 2026-10-12 categorical/source-driven spine already folded in. Carries the
  F48 principal acceptance (3 commits Codex made locally and never pushed; preserved).
- **Carrier chain** (a strict chain, not independent siblings):
  `many-worlds-swarm` (#50, `759c30c`) ⊆ `carrier-indexed-unification` (#53,
  `9e7589e`) ⊆ `no-ghost-causal-gluing` (#54, `c13b614`); and `carrier-indexed` ⊆
  `positive-carrier-realization` (#55, `619f075`). `many-worlds-swarm` is a parallel
  "completed atlas" assembly (consolidated `observational_succ/swarm_*.py` library +
  `formal/swarm_topology/` Lean project); it is a *subset* of the carrier tips, so it
  entered `main` transitively.
- **Twigs off the trunk**: `cambrian-observational-realization` (`bdb1fcf`, off
  VOYAGER), `evolutionary-obstruction-synthesis` (`b2774ca`, off genetic-fusion,
  own Lean 4.19 package), `cegis-categorical-discovery` (`34f2806`).

**Canonical-assembly decision (maintainer):** the atlas assembly (#49) is canonical.
On merge, the ~47 divergent `SWARM_ATLAS/*.md` dossier `add/add` conflicts were
resolved to the atlas; mw-swarm's `swarm_*` library + `swarm_topology` Lean proof
entered transitively via the carrier chain (they are load-bearing imports for the
carrier/no-ghost code, not redundant decoration). The `many-worlds-swarm` branch is
preserved for provenance, not deleted.

Integration branch `integration/succ-carrier-complete-2026-10-13`, off `main`,
audited `--no-ff` merges in order: atlas trunk → no-ghost (carrier chain + mw-swarm)
→ positive-carrier → cambrian → evolutionary-obstruction → cegis. Union-resolved the
4 additive cambrian conflicts (two CI branch-trigger globs; ARCHITECTURE and ROADMAP
each keep both the carrier/swarm section and the Cambrian section). Zero conflict
markers tree-wide.

## 2. Objective gates (reproduced locally; Python 3.12.3, mpmath 1.2.1; Lean 4.14.0 via elan)

- `scripts/verify_provenance.py`: **SOURCE_PROVENANCE_VERIFIED**, 72 items, exit 0,
  on every lineage and on the final merged tree. It self-reports
  `establishes_mathematical_truth: false`.
- Full `unittest` suites, all `OK`: atlas trunk **1602**, carrier-indexed **1839**,
  no-ghost **1901**, positive-carrier **1897**, cambrian **1716**, evolutionary **1528**,
  cegis **1469**; **final merged union tree 2132 tests OK**.
- Probes exit 0 (run with the repo root importable).
- Lean: toolchain `v4.14.0` matches the pin. The standalone kernels compile and are
  axiom-clean (`#print axioms` shows only `propext`/`Classical.choice`/`Quot.sound`,
  no `sorry`/`admit`/custom axioms): `SWM_A01_BaseChange`, `SWM_F48_InterfaceJoin`,
  `SWM_C19_FiniteHeight`, `SWM_X07_DirectedHeight`, the `EODCS_*` set, `NoGhost.lean`
  (12 decls), `EODCS_PositiveCarrier{,II,Cone}.lean`, `EODCS_CarrierIndexed.lean`.
  Three independent Lean packages are kept separately pinned: root (4.14),
  `formal/swarm_topology` (4.14), `formal/obstruction_synthesis` (**4.19**).
  The Mathlib-dependent `SWM_B09_TopologicalCompletion.lean` and the swarm_topology /
  obstruction_synthesis (4.19) packages were NOT recompiled in-session; their Lean
  status rests on their own CI lanes (UNVERIFIED here, not re-checked).

## 3. Four-bearing adversarial crucible (read-only; each number independently re-derived)

All four lineage audits: **PASS-WITH-NITS, firewall intact, zero false theorems,
zero fatal overclaims.** Every nit is documentation / test-coverage / labeling.

- **Atlas trunk (SWM + F48).** RH firewall clean — probes emit `RH_proved:false`,
  `completed_source_identified:false`, `nontrivial_zeta_zero_inputs:false`,
  `floating_point_used:false`; no dossier uses nontrivial-zero positions as inputs.
  E37/E38/E39/E40/E34/E35 EARNED (E38 `W_b` matches a `zetazero` *verification* oracle
  to ~22 digits; E38 is an honest no-go + conditional "missing object ⇒ RH", not a
  bridge). The four Lean kernels are scoped to exactly what they prove (A01's witness
  bijectivity is PAPER-ONLY; F48's `constant_bool_join_fails` is non-injectivity —
  trivial but honest). **F48 acceptance survives** (König/compact path space confirmed
  on 2000 random digraphs; Kraus representation no-go confirmed) and is honestly scoped,
  not a rubber stamp. **The "independent A03 review" is common-mode provenance (same
  model/provider/source family) — it counts as one bearing, which the registry's
  `review_independence_note` already discloses.**
- **positive-carrier.** Fibonacci cat system CONFIRMED-EARNED by rebuild: `r=2`,
  `d⁺_ℝ=2`, `d⁺_ℚ=∞`, 2-state over ℚ(√5); 21844 words (len 1–7) all nonnegative;
  `d⁺_ℚ=∞` *derived* (R̄=P=cone(e,e'), irrational extreme rays `s²+s−1=0`). Firewall:
  only the named algebraic/number-theoretic cores are Lean-formalized; the frozen
  flags `cone_theorem_lean_formalized_over_Q=false` and
  `bottom_completion_is_weakest_repair=false` are real; PCR-19 is `[amended II]`,
  realization clause REFUTED (PCR-31/32).
- **no-ghost.** Farkas certificates CONFIRMED (3000 systems vs HiGHS, 0 mismatches).
  The support-vs-fixed-kernel-vs-public-policy firewall holds at three layers; NG-P
  polytope equals the deterministic-policy hull (verified vs brute force). The braid
  holonomy is an explicitly *chosen* family and does **not** claim real independent
  experiments fail to commute.
- **carrier-indexed.** Central identity `J_{h·(a,z)}=Σ_c J_h·K_a` CONFIRMED atom-exact
  (brute path-sum vs matrix product); descent laws agreed 400/400 with an independent
  oracle; the matched-marginal-but-invalid-quotient counterexample reproduced with real
  downstream consequences. Lean covers only the trivial half (disclosed).

## 4. Honesty corrections applied on the integration branch

All non-mathematical; every touched file re-verified (full suite stays green):

- positive-carrier II dossier: "all entries positive" → "nonnegative" (the diagonal
  tick/tock realization matrices have zero off-diagonal entries).
- `docs/CLAIM_SUPPLEMENT_CARRIER.md` CAR-16: "embedded losslessly" → lossless only on
  the uniformly/safely-enabled subset (F48 `replay_fiber` drops disabled configs).
- `docs/ARCHITECTURE.md` compatibility layers: F48 + C17 are code-adapted; EODCS/A06/
  VOYAGER are prose-only intended layers, status UNVERIFIED (were listed as if wired).
- `docs/ROADMAP.md`: note Part II's fourth (irrational-contact) mechanism beside the
  Part-I "three mechanisms"; PCR link range `PCR-25–PCR-40` → `PCR-25–PCR-41`.
- `SWARM_ATLAS/A01.md`: reconcile "No Lean kernel check" (the BC/surjectivity/descent
  core IS kernel-checked in `SWM_A01_BaseChange.lean`, row SWM-A01-K).
- `tests/test_eodcs_carrier_indexed.py`: the 180-table oracle test was vacuous on its
  sufficiency branch (0/180 valid with random weights). Planted lawful q-fiber-constant
  kernels for `j%3==0` → now **60/180 valid**, so the `verdict.valid` assertions
  actually execute (and pass).

## 5. Deferred / documented (not promoted, not silently fixed)

- no-ghost overloaded status strings (`LAWFUL_GLUING`, `PROBABILITY_COUPLING_FAILURE`
  reused for support-only vs operational results) — docstrings disclose scope; a
  distinct-enum refactor is deferred (would churn sibling receipts/tests).
- no-ghost dossier claim-ID crosswalk (NG-P1/NG-P0 named differently across
  MANUSCRIPT/GLUING_REPAIR/supplement) and the NG-P "all deterministic policies"
  empty-menu wording — research-dossier labeling, not main-facing.
- no-ghost Lean gate `verify_no_ghost_lean.sh` asserts Lean 4.14.0; under elan a
  directory without a `lean-toolchain` can resolve a newer default — set
  `NO_GHOST_LEAN` / ensure the pin in CI. The file compiles identically on 4.14 and 4.29.
- `F48_PHASE2_PROBE.py` hard-codes a worktree-absolute `ATLAS_ROOT` (reproducibility nit).
- Mathlib B09 and the 4.19 obstruction_synthesis Lean packages: verified only by their
  own CI lanes, not re-run here.

## 6. What the consolidated repository proves / models / leaves open

- **Proves (classical, Lean-kernel or exact-arithmetic):** finite source-indexed base
  change / Beck–Chevalley predicate cores; the carrier reindexing identity and its
  lawful-quotient descent criterion; the positive-realization field-sensitivity results
  incl. the Fibonacci ℚ/ℝ gap; no-ghost Farkas obstruction certificates and the
  policy-polytope = deterministic-hull theorem; finite-branching König/compact
  path-space and the Kraus representation no-go.
- **Models (finite, exact, scoped):** the SWM missions, the carrier/no-ghost/
  positive-carrier/Cambrian campaigns — finite observational models with explicit
  hypotheses and negative controls.
- **Open / Conjectured / firewalled:** RH, completed-Weil positivity, any physical
  source authentication, the A06/VOYAGER code bridges, a necessary-and-sufficient
  `d⁺_ℚ<∞` criterion, general history-site gluing. SUCC remains a **Σ₁ verifier, not a
  Π₂ prover**; no RH/Navier–Stokes/cognition claim is made.

## 7. Next research frontier (three most valuable precise targets)

1. A necessary-and-sufficient criterion for `d⁺_ℚ<∞` (irrational contact is only
   sufficient for ∞; test the slack conjecture).
2. Mechanize the carrier reindexing descent (`audit_descent`) and no-ghost's
   policy-polytope LP in Lean, lifting them from Python+paper to kernel-checked.
3. A lawful concurrent history site with an actual gluing theorem and a
   destructive-order negative control (the standing F48/no-ghost open obligation).
