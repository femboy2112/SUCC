# CLAUDE MAIN INTEGRATION HANDOFF — SUCC, carrier-first and all swarms

**Prepared:** 2026-10-13.
**Carrier integration:** draft PR #53, branch \`research/carrier-indexed-unification-2026-10-13\`,
based on COMPLETE #50 at \`759c30c72a2927212cdbfa41365800da96e5d515\`.
**This file is an executable plan for a future maintainer-authorized Claude session,
NOT an executed main merge.** All live branch SHAs are a snapshot only.
Refresh \`research/2026-10-13/CARRIER_SWARM_BRANCH_SNAPSHOT.json\` from remote
immediately before choosing integration inputs.

## A. The new unification principle

The historical carrier is not another peripheral mathematical object; it is
the **source-indexed base** for every observer, report, quotient, proof-support
judgment and causal-history update. Use a common typed interface:

\[
(S,\ C_h,\ h,\ A_h,\ K_a,\ J_h,\ \mathrm{source/basis/epoch})
\]

Here \`S\` is the immutable original-source label set, \`C_h\` is current
carrier after actual history h, \`A_h\` is the lawful menu of executable
instruments, \`K_a(c;z,c')\` is the full joint receipt/next-state law, and
\`J_h(s,c)\` is the UNNORMALIZED original/current law.

**Mandatory law:** \`J_(h,a,z)(s,c')=Σ_c J_h(s,c) K_a(c;z,c')\`.
A carrier quotient \`q:C→D\` is lawful iff action availability descends and
the complete joint (receipt,next q'-state) law is constant on every enabled
q-fiber. This is the source-conditional Markov/kernal square. A deterministic
specialization is kernel-checked in \`formal/EODCS_CarrierIndexed.lean\`.
Finite stochastic reindexing and full history transport are proved on paper
and tested with independent rational source oracles, but **not** fully
machine-refined in Lean.

Do not erase or replace established \`Engine\`, \`ControlledCarrier\`,
\`LawfulSource/HistoryFiber\`, \`StochasticHistory\` or \`swarm_categories\`
with a newly invented god object. Integrate the carrier as an explicit
common vocabulary and source-preserving compatibility layer.

## B. Actual branch dependency DAG

The verified snapshot, including 43 observed \`research/swm-*\` child branches,
is in \`research/2026-10-13/CARRIER_SWARM_BRANCH_SNAPSHOT.json\`.
The dependency shape, not the floating SHA, is:

\`\`\`text
origin/main (historically 52d2c02...)
  └─ #40 source-driven inverse
      └─ #41 categorical repair
          └─ #42 contextual heuristics
              └─ #43 genetic categorical fusion
                  ├─ #45 EOS evolutionary synthesis (sibling, Lean 4.19)
                  └─ #44 EODCS posets/holonomy
                      └─ #46 causal/Nerode
                          └─ #47 relational/modal source
                              └─ #48 VOYAGER
                                  ├─ #49 ROLLING WIP atlas — active child worktrees
                                  ├─ #50 COMPLETED 48+12 atlas
                                  │    └─ #53 carrier-first research (THIS BRANCH)
                                  ├─ #51 COMPLETED Cambrian 36+8 audit campaign
                                  └─ #52 scoped EOS/VOYAGER F41 comparison
\`\`\`

This DAG is not a claim that \`main\` already includes these PRs. Verified
at the handoff snapshot: \`main\` was \`52d2c02b85b246aec67160260ac06bb1da33645e\`.
The floating PR #49 moved more than once WHILE the carrier work was underway.
Its original child branches are NOT automatically integrated or accepted.

Stable heads at the freeze:
- #45 EOS \`b2774ca485db4b5b4f7ce92e535220352fb3af2f\`.
- #48 VOYAGER \`5eb09e7cba36ec01b8f9d6834b78b5766fd93935\`.
- #50 completed Atlas \`759c30c72a2927212cdbfa41365800da96e5d515\`.
- #51 Cambrian \`bdb1fcfce875ee6c51fc62f78fbb4111582caadc\`.
- #52 F41 \`aeefd7ec2a7f50e45a1446e1995c7f6289c158a9\`.
- #49 rolling WIP: see SNAPSHOT, refresh and identify its TRUE final head.
- #53 carrier: refresh draft PR head after last proof receipt and CI gates.

## C. The two-phase MERGE policy

**Phase I: completed and independently reviewed research.**
Start a new integration branch from freshly fetched \`origin/main\`; never
modify active worker worktrees. Verify direct ancestry and commit DAG using
\`git merge-base\` before merging. Integrate the dependent lineage
#40→#41→#42→#43→#44→#46→#47→#48 in causal order, preserving exact source and
history test regressions. Incorporate complete #50, then carrier-first #53.

Integrate #51 Cambrian as a sibling, reviewing conflicts theorem-by-theorem:
its \`EODCS_CambrianRealization.lean\` covers finite-branching, changing-type
history actualization, and \`cambrian_stochastic_transport.py\` gives full
joint-law Bayesian source descent and sharp rare-event bound.
Compare with carrier \`CarrierInstrument\` and atlas C17 BEFORE choosing an
implementation. Preserve both if their semantics or type scopes differ.
Protect its actual source/git-bundle provenance in \`provenance/cambrian/\`.

Audit and selectively integrate #45 EOS and #52 F41 after source/claim and
formal-toolchain comparisons. #45's Lean 4.19 formal lane must remain pinned
in its **own package**; do not silently switch root Lean 4.14 or mathlib.
#52's mathematics may duplicate F41 already present in #50/#49; one exact
source-checked canonical result with cross-references is better than
copying a duplicate claim as a second independent theorem.

**Phase II: unfinished rolling swarm #49.** Verify every outstanding
assignment against the LATEST actual \`registry.json\`, freeze the parent
only when the running principal/agents have finished committing, and inspect
each accepted original child SHA against the frozen integration tree.
Do NOT merge 43 individual child branches merely because they exist.
An unresolved child is a future research item, not a main integration source.

If the rolling swarm is STILL ACTIVE:
- do not interrupt, reset, checkout, force-push, delete or change its worktree;
- merge only the completed audited material that is separately admissible;
- preserve a deferred-input manifest containing exact child heads and owners;
- document what is excluded and why, so the maintainer can complete it later.

\`Research finished\`, \`agent finished\`, \`PR open\`, \`CI green\`, and
\`mathematical theorem proved\` are separate claims. Mark all five explicitly.

## D. Cross-branch mathematical reconciliation

For each potentially duplicate theorem, build a reconciliation table:

\`{source_branch, original SHA, module, mathematical statement, hypotheses,
status, Lean version/axioms, independent oracle, countermodel, source identity,
chosen canonical home, disposition: MERGED | REFERENCED | WIP | REFUTED}\`.

Pay special attention to:

1. **Carrier source/history:** \`ControlledCarrier\`, \`Engine\`, F48
   \`swarm_lawful_history\`, C17 \`swarm_probability\`, Cambrian ST1–ST7, #53.
2. **Causal transport:** full joint report/poststate, partial enabledness,
   destructive actions, original-source label retention, conditional evidence.
3. **Finite repair:** A06 coreflection, EODCS Nerode, EOS CEGIS, the new
   full stochastic stationary refinement; preserve strongest valid hypotheses.
4. **Completion:** VOYAGER ideal profiles, #50 mathlib inverse-limit topology,
   #51 changing-type finite-branching Kőnig result, actual-source closedness.
   Do not interpret completion as physically performed infinite history.
5. **Geometry:** regular-kernel holonomy cover vs nonregular stabilizer
   cover; deck invariance NOT sufficient on arbitrary covers; F41 Heisenberg
   normal forms and source/observer group-order distinctions.
6. **Statistical source:** Fréchet couplings, conditional independence,
   duplicate event evidence, per-history available actions, rare receipt
   conditioning, support-vs-law non-invertibility.
7. **Arithmetic/RH:** genuine Euler/multiplicative, conductor/phase, Gamma
   completion, test-function topology, matched non-Euler mutations. A
   phase-blind covariance is NOT an authenticated Weil form.

Do not revise a theorem statement silently to make CI pass. Record
original obstruction and repaired theorem with an independent test receipt.

## E. Claim namespace and archive law

- Historical O1–O638 belong to the inherited core/VOYAGER lineage.
- Cambrian O639–O679 are already owned by PR #51.
- \`SWM-*\` belongs to completed/rolling swarm supplements.
- \`EOS-*\` belongs to #45.
- \`CAR-01..CAR-21\` belongs to this branch.

Never independently renumber those namespaces or paste parallel O-claims
into one ledger. Preserve hash/provenance histories and \`AGENTS.md\` rules.
Build a consolidated cross-reference index with sources and status labels.
Archived original files are immutable. Do not add a license.

## F. Mandatory validation and reproducibility

Run on one immutable integration SHA AFTER reconciliation, not by
combining prior PR test counts.

\`\`\`sh
git status --porcelain=v1
python scripts/verify_provenance.py
python -m unittest discover -s tests -p 'test_*.py'
python -m unittest discover -s tests -p 'test_eodcs_*.py'
python scripts/observer_foundations_probe.py
python scripts/ordinal_succ_report_probe.py
python scripts/carrier_indexed_probe.py
python scripts/verify_swarm_receipts.py
\`\`\`

Also run the branch's Cambrian verification, the independently pinned Mathlib
topology \`formal/swarm_topology\` package, every \`formal/EODCS_*.lean\`
module using the pinned Lean 4.14 root toolchain, and EOS Lean 4.19 in its
OWN isolated package. Check complete Lean axiom dependencies and real
negative controls (sorry/admit/axiom and false theorem rejection).
Do not run huge concurrent compiler jobs on memory-constrained hardware.

Reproduce every frozen JSON scientific receipt byte-identically when its
contract says byte-identical; never edit receipts to fit changed code
without declaring a NEW source experiment version.

Validate Python 3.10 and 3.13 on the actual final integration SHA via remote
CI. PR51 and #50 individual CI are useful provenance, but do not replace
post-merge CI.

Check source-laden demos and determinism under exact Fraction arithmetic;
no floats masquerading as mathematical proof certificates.

## G. What to do with main

The maintainer requested a Claude prompt for the later integration. On THAT
explicitly authorized run, once the integration candidate's original
commits, source provenance, full suite, both Lean lanes, hostile controls,
and exact-head GitHub CI are all green:

- refresh \`origin/main\` and verify no intervening third-party changes;
- merge the validated integration branch into main with a non-forced,
  auditable history-preserving commit;
- push main only if the accepted gate passes;
- preserve original research branches and draft PR review history;
- open an integration summary showing included, deferred, duplicated,
  failed and superseded work, with exact SHAs and theorem status.

If any gate fails, DO NOT push main. Keep a draft integration PR and give the
maintainer a concrete blocker with minimal countermodel or failed command.
If any swarm is still moving, do not falsify \`everything integrated\`:
include completed work and explicitly defer unfinished branches.

## H. Highest-value future theorem after reconciliation

A lawful carrier/history **gluing theorem** should be derived, not
announced. Specify a site of actual admissible histories, stable
concurrency diamonds for enabling/outcomes/current updates, common
original source and event identity, and unnormalized joint-law
Beck–Chevalley/base-change. Require compatible original-support
presheaf sections and independent probability densities when necessary.
The destructive two-bit read is the mandatory exact counterexample to
unqualified gluing.

Under compactness/finite-branching, compare compatible finite actual
histories with projective mathematical completion and original-source
realization. Do not conflate these with an instrument executing infinite
time, a general cognitive mechanism, or a source-derived Weil/RH sign proof.

**Final handoff standard:** source-first mathematics, not a new god object;
every arrow typed; every claim provenance-backed; all accepted proofs intact;
WIP sources preserved; and a transparent, actually verified main history.
