# Scoped parallel audit: PR49, PR50 and PR51

**Verdict: SURVIVES WITH EXPLICIT GATES.** No contradiction between the selected,
properly quantified statements was found. Several stronger integration readings
fail exact counterexamples. This is a theorem/map comparison of the named subset,
not an audit of every campaign proof or permission for a wholesale merge.

## Authority and reproducibility

Frozen sources, read through Git objects:

| Line | Exact snapshot | Role |
|---|---|---|
| PR49 | `9bcb93965239c395653ad14e7c7afe65fa7faec0` | Accepted local atlas snapshot; audit parent |
| PR50 | `759c30c72a2927212cdbfa41365800da96e5d515` | Completed many-worlds sibling |
| PR51 | `bdb1fcfce875ee6c51fc62f78fbb4111582caadc` | Cambrian sibling after scanner correction |

All three descend from `5eb09e7cba36ec01b8f9d6834b78b5766fd93935`.
The audit branch is `research/swm-parallel-audit-2026-10-13`, in its own clean
worktree. AGENTS, METHOD, PROTOCOL, the import manifest and frozen founding dossier
were inspected. The manifest identifies archival origin
`ba075348b7bcc66d938b3e0ca96c26e95bba340a`; that original commit object is absent
locally. No archival/imported theorem or implementation was changed.

`PARALLEL_AUDIT.json` binds selected dossiers, formal sources and review records
to exact Git blob IDs and SHA-256 hashes. Its independent standard-library probe
imports no repository mathematics. Commands executed from this worktree:

```sh
git status --short
git merge-base 9bcb93965239c395653ad14e7c7afe65fa7faec0 759c30c72a2927212cdbfa41365800da96e5d515
git merge-base 9bcb93965239c395653ad14e7c7afe65fa7faec0 bdb1fcfce875ee6c51fc62f78fbb4111582caadc
python research/2026-10-13/SWARM_ATLAS/comparisons/PARALLEL_AUDIT_probe.py --output research/2026-10-13/SWARM_ATLAS/comparisons/PARALLEL_AUDIT.json
git diff --check
```

The probe exits zero. It verifies nine exact controls, 27 changed-path collisions,
the common base, frozen accounting, and all seven PR50 formal receipt/source hash
correspondences. No compiler, full suite, child spawning, push, merge, or shared
ledger write was run. Existing kernel verdicts remain source-bound recorded
evidence; this audit does not independently rerun those kernels or current CI.

## Theorem and file comparison

`A/` below abbreviates `research/2026-10-13/SWARM_ATLAS/`. Every SWM identifier is
**branch-qualified**; identical labels are not automatically identical statements.

| Focus | PR49 exact content | PR50 / PR51 exact content | Compatibility and boundary |
|---|---|---|---|
| A01 | `A/A01.md`; `formal/SWM_A01_BaseChange.lean`: for a commuting square, predicate existential/universal BC iff comparison to the pullback is surjective. Witness-family BC requires bijectivity; that part remains paper proved. | PR50 `A/A01.md` instead proves all-word repair naturality and filtered origin/current belief-image transport. Its repair proof is in `formal/Swarm_Repair.lean`. | Different theorems sharing a label. Predicate truth truncation does not preserve receipt multiplicity. A01's Std kernel file covers its named predicate/surjectivity/target-descent claims, not every dossier claim. |
| A06 | Greatest action-stable equivalence below a seed; inclusion-order coreflection; source-system reflector and lawful pullback naturality. | Same all-word relation operator; PR50 adds the exact one-pass criterion for separate action repairs and a four-state mixed-action counterexample. | Same order convention and total common action grammar. Report preservation alone fails naturality. PR50's core kernel theorem allows arbitrary relations/infinite carriers; it does not prove every finite implementation or action-family criterion. |
| B09 | `formal/SWM_B09_InverseFamilies.lean` uses finite Lists with membership-indexed coordinates; `SWM_B09_TopologicalCompletion.lean` gives a native Homeomorph, limit universal property, closed-image criterion, and intrinsic profinite properties. | PR50 `formal/swarm_topology/SwarmTopology.lean` uses Finsets, source-admissible rows and overlap coherence; explicit continuous mutually inverse maps identify threads with literal trace closure. | Equivalent completion representations through singleton evaluation and finite restriction. Lists do not count repeated probes twice. Neither construction executes counterfactual words jointly or manufactures an original realizer. |
| B10 | Hausdorff source, continuous finite reports, finite-valued compact-sublevel cost: global minimum cost equals the supremum of finite-fiber infima; finite profile-specific cap iff realization. | PR50: for countably enumerated probes, the observational trace quotient is complete iff trace image is closed iff every compatible profile is realized. | Complementary sufficient/exact criteria. An unrelated complete/Polish/Baire source metric is insufficient. PR49 allows arbitrary probe index sets; PR50's stream metric needs complete countable enumeration. |
| C17 | History/source-dependent joint kernels, original/current prior, surjective source/carrier maps satisfying the joint-row square; all-prior unnormalized law, evidence and positive posterior transport. | PR50 current-state-sufficient instruments, retained original index, joint-law statistic repair. PR51 ST1–ST6: changing-carrier joint receipt/report lumpability and Bayesian descent. | Same finite reindexing mechanism under explicit encoding. PR49 permits kernel dependence on the original; PR50 must include that persistent latent information in its current carrier. Support/marginals/posterior equality alone is weaker. |
| C18 | Conditional-product reconstruction commutes with Bayes iff supported likelihood minors vanish; null fibers allowed; sharp complete-coupling Fréchet range. | PR50 factorized evidence gives the corrected common separator `p A B/Z`; posterior CI iff active supported likelihood matrix has rank one. | Same nonzero-fiber criterion. PR49's rank-at-most-one wording also includes all-zero eliminated fibers. Reusing one receipt gives 3/4; fresh CI draws can give 9/10. |
| C21 | Frozen registry says RUNNING/UNVERIFIED; no accepted C21 dossier at this snapshot. | PR50 finite-horizon, finite-menu expected-cost Bellman theorem, certifying all positive branches; no-reset obstruction. PR51 discusses public-history policy and access boundaries. | Sibling theorem can inform a future independent mission, not retroactively complete PR49. Source-universal certification additionally requires full admitted-original support. Almost-sure unbounded stopping is another claim. |
| F48 | Frozen registry says QUEUED/UNVERIFIED; no accepted F48 dossier. | PR50 deterministic preparation, enabling/report/update-descending quotient, unchanged originals: identical support presheaves and discrete fibrations; finite-original realization. PR51 supplies changing-type nondeterministic finite-branching realization. | Forward measure opfibration and backward support fibration have opposite variance. Quotienting current states must preserve enabling and original-target support. A stochastic support tower need not have positive infinite-event probability. |

Both B09 lines use Lean 4.14 and exact mathlib commit
`4bbdccd9c5f862bf90ff12f0a9e2c8be032b9a84`: PR49's bootstrap pin and PR50's
isolated lakefile agree. PR51's Cambrian realization uses core/Std 4.14, not
mathlib topology. EOS at `b2774ca485db4b5b4f7ce92e535220352fb3af2f` has
`formal/obstruction_synthesis/lean-toolchain` pinned to **4.19.0**. It remains
an isolated source/toolchain family. Equal mathlib pins permit comparison;
they do not prove interchangeable namespace instances or authorize a pin change.

## Corrected synthesis claims and crucible receipts

**PR50 X03 survives its corrected scope.** The exact implementation
`observational_succ/swarm_gluing_cegis.py` returns `core_scope` and
`core_source_verified`; the latter is established by checked projection coverage.
On original carrier `{0,1}`, grammar `{0}`, constraint `x=1`, the grammar is
unsatisfiable but the source witness `1` exists. Enlarging the grammar admits it.
Thus a grammar-image core cannot prune arbitrary future source-retaining
extensions. Source-wide caching needs unsatisfiability checked on the original
carrier; coverage is sufficient, not logically necessary. The amended X03
theorem and RY audit preserve this distinction. PR49's different `A/X03.md`
must retain its own statement identity.

**PR50 X07 survives with deterministic preparation.** Its corrected theorem
requires `mu(o,x)=pi(o) 1[x=i(o)]` and full-support `pi` to recover F48 exactly.
One original with a fair mixture of two current states, followed by deterministic
bit readout, gives both outcomes positive original support `{o}`. Either pure
preparation produces only one outcome. Deterministic instruments alone cannot
recover that mixed preparation as F48's fixed `i`. The exact two-current-state
control retains the missing premise; unnormalized forward composition itself
does not require this restriction.

**The naive B09-to-Cambrian stage identification fails.** B09 stages are finite
restrictions of already supplied *complete source traces*. Their restriction
maps are surjective because the same original source extends each row. Raw
causal prefixes need not have that property. With states `l,d`, start `l`,
transitions `l->{l,d}`, `d->{}`, length-one stage includes `(l,d)`; no length-two
path extends it. Arbitrarily long all-live paths nevertheless exist. The probe
computes the two stages and missing truncation preimage exactly. Therefore raw
prefix stages cannot simply be renamed B09 source-image stages. This refutes
that extension, not either realization theorem.

PR51's exact `formal/EODCS_CambrianRealization.lean` states arbitrary
time-indexed state types and nondeterministic relations. Each state has a finite
list **covering every legal successor**; the list may also contain extraneous
entries, since candidate edges are checked. A fixed arbitrarily extendable start
gives a classical infinite history. A finite initial list plus arbitrarily long
prefixes selects such a start. No uniform state-size cap is assumed. The same
file proves natural countdowns have every finite depth using different starts
but no infinite history, so deleting the finite-initial-menu gate is false.
Its general compact-product/closed-constraint theorem remains paper proved.

## Strongest compatible representation and next lemmas

A useful joint representation retains `(original,current,public history)` and
the complete outcome/poststate law. Deterministic sources embed as Dirac rows;
general finite rows push forward unnormalized, preserving evidence mass; positive
mass permits partial normalization. Taking support then yields the backward
original-support presheaf, with no probability-preserving inverse. A current
quotient is lawful only after enabling, outcome, update, law and specified target
maps descend. All-word repair addresses representation; realization and actual
access remain separate obligations.

Four precise next lemmas follow:

1. **Completion representation adapter.** Construct the PR49 List-stage/PR50
   Finset-thread equivalence by restriction and singleton decoding; prove inverse
   identities, stage-cone naturality and continuity in the pinned common lane.
   Include empty source/probe stages and duplicate/permuted lists.
2. **Causal realization bridge.** Construct finite path stages from changing
   types, track initial constraints and dead ends, then isolate arbitrarily
   extendable paths. Prove the required inverse-limit/closed-constraint map before
   applying trace actualization. Never use already-existing infinite histories
   to prove their existence circularly. Countdown and `(l,d)` remain controls.
3. **Weighted original-history quotient.** Extend the deterministic F48 square
   to history-indexed, changing-carrier joint kernels and partial action menus.
   Check original-target factorization and availability separately. Keep the
   mixed-preparation and rare-event controls; PR51's ST7 bounds conditional TV by
   joint TV divided by the larger positive evidence mass, not uniformly alone.
4. **Policy preservation.** Prove a lawful joint-history quotient transports
   feasible public-history policy trees and descending costs. Distinguish finite
   horizon, bounded stopping and almost-sure stopping; full-support noisy rows
   preserve both targets after every finite word and obstruct zero-error reports.

## Provenance and integration verdict

PR49's frozen spawn registry contains **29 unique recorded native agents**,
including the nested C17 crucible. This is a frozen snapshot count, explicitly
not the current live total. PR50 reports **21 child processes**: six cohorts,
twelve synthesis workers and three audits. Their spawning was not independently
witnessed by this audit. PR51 reports six research workers and eight audit
assignments; 36+8 assignments do not establish 44 independently spawned agents.
Sibling counts are never aggregated as owned execution.

The snapshots share ancestral mathematics, provider/reasoner lineage and several
classical constructions. κ here is direct immutable-source contact; φ is scoped
derivation inspection and exact controls; σ remains conditional on declared
source laws; ρ supplies no evidence. This is provenance comparison without
operational phase, phasor ranking or independent physical observations.

The JSON enumerates **27 PR49/PR50 changed-path collisions**, including dossiers,
atlas and X02 receipt. Case-sensitive `registry.json` versus `REGISTRY.json` is
also an integration hazard on other filesystems. Preserve branch-qualified
SWM names and complete receipts; select or rename contributions only after
principal review. No shared historical claim status, default, archive, license,
or source branch was rewritten. Principal remains the sole integration authority.
