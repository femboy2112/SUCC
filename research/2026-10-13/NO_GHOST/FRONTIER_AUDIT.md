# NO-GHOST: immutable frontier audit and integration boundary

Audit date: 2026-10-13. This is an inventory of inspected repository evidence,
not a new mathematical priority claim. Source reading and the fresh Python
checks below were performed by the NO-GHOST frontier auditor. Historical Lean
receipts are identified as historical receipts; they are not represented as
fresh compiles by this auditor. No archive, parent module, main branch, swarm
registry, or active sibling worktree was edited.

## 1. Frozen sources and namespace discipline

| Research line | Inspected immutable commit | Relationship to working base |
|---|---|---|
| PR49 rolling atlas | `bd0e0d6d2b507546bc73d0cc6da2272747d0829d` | Not an ancestor of PR53; read by `git show` |
| PR50 completed atlas | `759c30c72a2927212cdbfa41365800da96e5d515` | Ancestor of PR53 |
| PR51 Cambrian | `bdb1fcfce875ee6c51fc62f78fbb4111582caadc` | Not an ancestor of PR53; read by `git show` |
| PR53 carrier first | `9e7589e522aff990189aa8a14f6ee2fa5a28dd81` | NO-GHOST starting commit |

The shared founding frontier is `5eb09e7cba36ec01b8f9d6834b78b5766fd93935`.
The working branch is `research/no-ghost-causal-gluing-2026-10-13`. The audit
did not switch it. These are frozen research snapshots, not assertions about
the latest live PR heads or whether any draft has subsequently merged.

**Identical labels are not identical results.** In particular PR49's
`research/2026-10-13/F48/F48_LAWFUL_HISTORY_FIBRATION.md` and PR50's
`research/2026-10-13/SWARM_ATLAS/F48.md` are separate investigations. Likewise
PR49 and PR50 C22, A04, A06, X05, and B09 must be branch-qualified. Preserve
the old O1–O638 ledger, Cambrian O639–O679, CAR-01–CAR-21, and both SWM
namespaces. NO-GHOST should use its own identifiers.

`AGENTS.md`, `docs/FOUNDATIONS.md`, `docs/METHOD.md`, and the relevant
architecture, roadmap, historical ledger and carrier supplement were read.
They require actual maps, source-relative quantified statements, retained
countermodels, and an independent receipt for status promotion. Mathematical
source tags do not authenticate physical origins; unavailable sensors cannot
be introduced by notation. The import manifest remains a separate provenance
gate, not a theorem oracle.

## 2. Acceptance state at the frozen PR49 commit

The controlling source is
`bd0e0d6:research/2026-10-13/SWARM_ATLAS/registry.json`, not a stale author
dossier's last paragraph. It records **47 accepted first-generation slots**,
**F48 initial phase accepted / whole-swarm phase pending**, and **all twelve
X01–X12 bridges accepted**.

F48 has state `AWAITING FINAL REVIEW`, proof state `INITIAL PAPER/INTERFACE
KERNEL ACCEPTED; PHASE2 A03 REVIEW RUNNING`, initial commit
`6e751c0d996de3d27a91b09f44dc2d534db09c73`, and phase-two commit
`224d049964b02fc42ad4fcbaa078944ed91da0a7`. Thus its phase-two claims are
inspected paper derivations awaiting the stated gate; neither their presence
in Git nor the root's acceptance of the twelve bridges certifies the entire
F48 synthesis. Conversely the phase-two prose still calling X11/X12 pending
is stale relative to the registry: X11 and X12 are accepted in this snapshot.

PR49 C22, A04, A06, C17, F41, X03 and X05 are accepted paper results in the
registry. Several author dossiers still end with a generic review-pending
sentence. Acceptance is a repository review status; it does not establish
academic novelty, empirical truth, or a Lean proof.

## 3. Results that NO-GHOST must not rediscover as new

| Existing result | Exact source and proved scope | Verification boundary |
|---|---|---|
| Original/current joint event update | PR50 C17; `swarm_probability.py`; PR53 CAR1 | Classical finite stochastic composition; paper plus exact implementation |
| All-prior labelled-kernel descent iff full joint rows are constant on observation fibers | PR51 ST1–ST2; PR53 CAR2–CAR3 | Dirac necessity and finite-sum sufficiency already written; separate marginals and normalized posteriors insufficient |
| All finite deterministic history transport | PR50 F48 and PR53 `EODCS_CarrierIndexed.lean` | Same original labels, outcome/update squares; deterministic total-action Lean scope |
| Basic two-event diamond iff all outcome subkernels commute | PR50 `SWARM_ATLAS/C22.md` | Common-carrier instrument endomorphisms; all-prior necessity by source/current Dirac preparations |
| Weak fixed-schedule independence for finite event posets | PR50 C22; strengthened access contract in PR49 C22 | Adjacent incomparable swaps connect linear extensions; full report/endpoint law preserved; paper proof |
| Complete fixed-run incidence sheaf | PR49 F48 initial T1 | Root and every transition constraint covered; exact shared source/current/branch assignments; paper proof |
| Universal arbitrary-relation compressed join iff interface observation injective | PR49 F48 initial T2 | Predicate core Lean-checked; arbitrary relation instance by fixing external endpoints |
| Greatest surjective extendable-prefix subsystem | PR49 F48 phase-two T1 | Finite roots and finite branching, all locally legal infinite paths as admitted class; pending paper synthesis |
| Nonregular deck invariance does not imply descent | PR49 A04; PR51 geometry | Exact S3 three-sheet cover with trivial deck group and nonconstant section; paper proof/finite oracle |
| Nonabelian global sections are common holonomy fixed points | Native EC7/O566–O571; PR49 A04/F41 | Full permutation action; parity/scalar checks do not replace it |
| Exact one-step pair/signature repair | O574; PR51 ST6; PR53 CAR4 | Coarsest mathematical refinement; not an available instrument |
| Stationary action-stable coreflection | PR50 A06; PR53 CAR12 | Complete finite action family; exact refinement; finite termination |
| Positive-tolerance repair need not have a least element | PR49 F46-T4 | Three-state target `(0,1,2)`, tolerance `1/2`, incomparable partitions `01|2` and `0|12` |
| Finite compatible profiles need not have an original realizer | VOYAGER O615/O629; native Lean stream counterexamples | Eventually-zero sources versus all-one ideal profile |
| Compact continuous source image criterion | PR50 B09; PR49 B09 | Topology formalized in the separate pinned 4.14 mathlib lane; older roadmap statements saying paper-only are historical |

### 3.1 Two C22 statements and the remaining extension

PR50 C22 uses report-indexed matrices `A_r(x,y)` and `B_s(x,y)` on one common
carrier and proves

\[
\forall J,r,s\quad J A_rB_s=J B_sA_r
\quad\Longleftrightarrow\quad
\forall r,s\quad A_rB_s=B_sA_r.
\]

Its `swarm_probability.py::commutation_defect` returns exact outcome atom
defects. It already distinguishes joint report/terminal laws from summed
channels, and retains destructive-read counterexamples. Its schedule proof
is the standard first-desired-event bubbling induction on finite linear
extensions. It explicitly preserves event occurrence identities and retains
actual sequential records as distinct records.

PR49 C22 adds a forward-invariant domain and enabledness persistence. In the
stochastic variant every positive transition of either independent action
must preserve the other's enabledness; every outcome-specific square must
hold. It still concerns eligible fixed schedules. Neither result gives
unrestricted adaptive-policy invariance, canonical private-branch matching,
or a braid theorem for a selected family of matchings.

**Potential NO-GHOST extension:** changing typed stages and explicitly
history/source-indexed kernels; prefix/suffix stability after exchanged
events; selected private-history comparison maps; a precise distinction
between equality of laws and path-independent private transport. The common
carrier C22 theorem remains the baseline specialization.

### 3.2 Two F48 objects

PR50 F48 supplies deterministic `LawfulSource`, `Instrument`, `Event`, and
`HistoryFiber` in `swarm_lawful_history.py`. A history fiber retains surviving
originals and their current states; restrictions are inclusion of originals.
Under exact preparation, enabling, outcome, and update quotient squares,
all history fibers, original-target support and robust public policies
transport. Its destructive two-bit example shows intersecting counterfactual
original supports does not make a sequential one-carrier experiment.

PR49 F48 allows nondeterministic private lifts
`(sigma,c0,beta1,c1,...,betan,cn)` with genuine declared branch tokens. Its
prefix presheaf has literal truncations; endpoint beliefs do not determine
private truncations. Initial T1 uses the incidence complex of a **fixed run**:
edges bring both endpoint cells and their transition relation; root preparation
is also a constraint. Exact matching local assignments uniquely unite because
every constraint is contained in a cover member. Sheafness does not assert
existence of any matching family or section.

Initial T2 proves that a report `q:I→O` can substitute for full interface
equality uniformly over arbitrary left/right relations iff it is injective.
If `q(x)=q(y)` with `x!=y`, left `{(a,x)}` and right `{(y,b)}` have a spurious
reported join. The image of an assignment sheaf under existential projection
therefore need not be a sheaf. Sheafification's formal glue need not have a
source lift. NO-GHOST may strengthen or organize this no-go but must cite it.

Phase-two T1 defines `E_n` as prefixes extendable to every larger finite depth.
Finite allowed roots and finite branching imply: every `E_n` finite; adjacent
restrictions onto; greatestness among surjective subsystems; equality with
the actual infinite-path prefix image; compact inverse-limit realization;
functoriality under depth-preserving lawful tree maps. Its admitted paths are
**all locally legal branches**. Fairness/liveness or a stricter nonclosed
original class requires another admission theorem. In particular requiring
infinitely many ones admits every finite binary prefix but not `0^infinity`.
Aggregate depth restrictions being onto does not make a chosen outcome's
conditional restriction onto. Infinite paths are mathematical objects, not
performed infinite experiments or necessarily positive-probability events.

Phase-two T2 separately rejects a CP-channel-invariant private-path assignment
that is bijective to every Kraus representation's branch labels: one Kraus
identity versus two scaled identities give unequal private-fiber cardinality.
Classical process tokens must therefore not be silently assigned to unobserved
quantum Kraus indices.

### 3.3 Source-aware repair and policy gates

Native O572/O574/O579 already prove causal report descent, universal pair
repair, and composition of lawful deterministic squares. O575's extra-memory
formula is the fixed-width `ceil(log2(maximum future-report fiber split))`,
conditional on availability of that supplemental message. `field_probe_repair`
already has an exact finite hitting-set optimizer, independently checked
certificates, impossible-pair witnesses, and a distinct budget-exhausted result.
Its plans are static probe choices, not destructive execution policies.

PR50 A06 proves action-stable refinement is a coreflection under relation
inclusion. Separate one-pass repairs need not equal the combined-action
repair: the preserved four-state mixed-word counterexample is minimal.
`Swarm_Repair.lean` later formalizes named coreflection/base-change/equivalence
claims even though the early A06 author dossier says it added no Lean file.

PR53 `repair_one_step` incorporates enabledness and complete next joint rows;
`minimal_stationary_repair` repeatedly closes the whole declared action menu.
These mathematical refinements do not create sensors. PR49 F46 already kills
universal least tolerant repair. A new legal-cost menu solver is useful only
if its candidates carry lawful implementation contracts; enumerating hidden
source functions is not an operational repair algorithm.

PR50 X05 is stronger than a quotient-only simulation: stochastic carrier
intertwiner `T`, report-only garbling `G`, one-way availability lifting, and
joint transition squares transport finite robust original-target policies
with controlled cost. The controller does **not** sample `T(y|x)` using hidden
`x`; `T` is a proof object. This prevents accidental invention of a private
state oracle. Its sufficient square is not a necessary characterization of
all possible policy comparisons.

## 4. Formal verification inventory relevant to NO-GHOST

### PR53 deterministic carrier lane

`formal/EODCS_CarrierIndexed.lean` has no imports, no mathlib, and is written
for Lean 4.14. Its six theorem names are:

- `ObservationalSUCC.CarrierIndexed.carrier_original_is_invariant`
- `ObservationalSUCC.CarrierIndexed.all_finite_carrier_reports_transport`
- `ObservationalSUCC.CarrierIndexed.all_finite_carrier_endpoints_transport`
- `ObservationalSUCC.CarrierIndexed.original_support_survives_carrier_pushforward`
- `ObservationalSUCC.CarrierIndexed.original_claim_transport`
- `ObservationalSUCC.CarrierIndexed.carrier_comparison_composes`

These concern total deterministic actions on one carrier per representation,
finite action words and predicate support. They do not mechanize stochastic
CAR3 finite sums, partial-action menus, adaptive planners, incidence sheaves,
or concurrency coherence. Do not promote the whole Python module to a Lean
refinement claim because these six statements compiled historically.

### PR49 interface kernel

`bd0e0d6:formal/SWM_F48_InterfaceJoin.lean` imports `Std`. Its named results
`SWM.F48.exact_compressed_join_iff_injective` and
`SWM.F48.constant_bool_join_fails` are recorded as kernel-checked in
`research/2026-10-13/SWARM_ATLAS/receipts/F48_interface_join_kernel.json` and
`reviews/F48_KERNEL_REVIEW.md`. The receipt reports Lean 4.14.0,
compiler commit `410fab728470`, exit zero and **no axioms** for those two
declarations. The incidence sheaf and phase-two pruning remain paper.
The receipt's top-level assignment field is a reused `SWM-B09` label; the
per-file source hash, command and theorem output identify the actual F48
check. Preserve that provenance detail instead of treating the label as proof.

### PR51 changing-type realization

`bdb1fcf:formal/EODCS_CambrianRealization.lean` imports `Std.Tactic` and
uses Lean 4.14. It formalizes changing state types and arbitrary time-varying
nondeterministic relations with complete finite successor menus. Named
theorems include `cambrian_finite_coherent_choice`,
`cambrian_extendable_successor`,
`cambrian_nondeterministic_history_realization`, and
`cambrian_finite_prefixes_realize_one_history`. The last requires a finite
initial menu and arbitrarily long compatible prefixes. It uses classical
choice; it is not an effective branch selector. The file also proves
`cambrian_countdown_all_finite_depths` and
`cambrian_countdown_no_infinite_history`. The general compact closed-graph
topological theorem in Cambrian remains paper, while this finite-branching
specialization has historical kernel evidence.

### Topology and the separate EOS lane

The PR50 topology package's pin is
`formal/swarm_topology/lean-toolchain = leanprover/lean4:v4.14.0`; its
`lakefile.lean` pins mathlib to
`4bbdccd9c5f862bf90ff12f0a9e2c8be032b9a84`. Its final kernel receipt records
`SwarmTopology`, `SwarmPolicyCompactness`, and
`SwarmX01CompletionTransport`. Standard mathlib axioms are disclosed in its
own formal audit. The independent EOS PR45 lane uses 4.19 and is not merged
or imported here. A NO-GHOST compile under another version would not certify
this pinned environment.

## 5. Integration map: add obligations over the existing carrier

| Existing attachment | Safe NO-GHOST extension | Necessary guard |
|---|---|---|
| `carrier_indexed.CarrierStage`, `CarrierInstrument`, `ActualHistory` | Finite source/history-indexed contract and exact event paths | Immutable original label; positive receipt evidence; safe public action choice |
| `carrier_indexed.CarrierStep`, `transport_actual_history` | Compare sequential realizations and transport through valid quotients | Occurrence/stage/epoch identity; never a name-only registry |
| `swarm_probability.commutation_defect` / C22 | Typed diamond witness and law-level schedule certificates | Full outcome/next-state atoms, future-law context compatibility |
| PR49 private-history presheaf | Selected adjacent private-path isomorphisms and coherence tests | Actual branch tokens; source/report/endpoint preservation; braid/square laws stated separately |
| PR49 incidence sheaf | Constraint-complete event/ancestry covers, possibly with coherent schedule presentations | Every global constraint covered; quotient comparisons commute with restrictions |
| Native holonomy / `voltage_cover_synthesis` | Schedule-path holonomy as an explicit permutation action on private fibers | Full nonabelian maps, regularity or full kernel-pair descent; fixed law is weaker than fixed atoms |
| Native exact static repair / CAR4 | Finite legal repair menu with costs and explicit execution realization | Never infer access from a mathematical refined statistic |
| VOYAGER / Cambrian / F48 pruning | Infinite-horizon boundary appendix | Original class, closedness, finite branching and effectiveness kept distinct |
| Probability coupling bounds and C18 | Finite polytope with atoms enumerated from actual contract | Nonnegative coupling alone is insufficient if its atoms are unlicensed experiments |

Current `carrier_indexed` instruments have tables indexed by current state;
explicit source/history dependence needs a declared extension or inclusion
of the necessary latent memory in the complete state. It must not become
an observer input. Its latest inherited regression specifically fixes
repeated action names across changing stage/epoch charts. Reusing action
labels is legal; identifying event occurrences merely by their label is not.

## 6. Fresh baseline checks performed by this audit

On the PR53 working base, before this audit file was added:

| Command | Observed result |
|---|---|
| `python scripts/verify_provenance.py` | Exit 0; 72 entries, 17 byte-identical archives, 55 namespace migrations |
| `python -m unittest tests.test_eodcs_carrier_indexed tests.test_eodcs_holonomy tests.test_field_probe_repair -v` | Exit 0; 58 tests pass |
| `python scripts/observer_foundations_probe.py` | Exit 0; exact foundation controls pass; no RH or source-authentication promotion |
| `python scripts/ordinal_succ_report_probe.py` | Exit 0; retained ordinal/source/positivity countermodels reproduce |

The required full-suite and final-head formal gates belong to the integrating
principal. Historical source receipts are not substituted for those gates.
Python finite tests do not establish universal theorems; the proofs above
retain their stated mathematical hypotheses.

## 7. Frontier verdict

The available frontier is substantially beyond a proposal for a history
fibration. Basic all-prior stochastic diamonds, fixed-schedule law invariance,
exact interface sheaf gluing, canonical exact refinements, nonregular-cover
descent failure and finite/infinite source-realization distinctions already
exist in distinct scopes. NO-GHOST should make them composable without
flattening those scopes.

The useful new cut is the separation of **law-level schedule equality** from
**coherence of selected private-history identifications**, followed by an
operationally supported gluing/coupling/repair interface. A theorem based only
on local diamonds still needs complete global constraints and admissible
atoms. A finite Farkas characterization is classical linear feasibility;
its SUCC contribution is correct construction and verification of the lawful
atom universe. Academic originality of any stronger structural theorem
requires separate primary-literature comparison.
