# X01 independent adversarial review

Reviewer: separate second-generation agent `cross01_repair_completion`.
Reviewed source snapshot: `24c93bf0c2bdd4f3f84e9be6367bec15308270ce`.
This review independently read the formulas and proof scripts; it did not
promote claims by rerunning their original Python implementations.

## B09: survives with its stated scope

The arbitrary W quantifier is real: finite compatibility ranges over every
`Finset W`, not only sequential prefixes or a secretly countable index set.
The empty finite set correctly enforces source nonemptiness when compatibility
is inhabited. Discrete O is required for singleton cylinders and gives the
Hausdorff target needed by compact-source actualization. Finite O is used only
for compactness of the entire completed profile space.

`ThreadCondition` requires actual source admissibility for every finite row
and agreement on overlaps. This is equivalent to the ordinary restriction
inverse-system condition: coherence through the union of two finite sets
implies overlap agreement, and conversely overlap agreement implies every
restriction square. The singleton-row reconstruction is well typed; source
witnesses can vary with the finite row. Its inverse proofs do not identify
those separate witnesses with a single original source. Both map continuities
are actual dependent-product/subspace continuities. Thus the explicitly
packaged continuous inverse functions supply every homeomorphism obligation.

The independent compilation passed on pinned official Lean/mathlib. Only
unused-section-variable linter warnings occurred. No `sorry`, `admit`,
replacement topology, hidden finite W assumption, or source-realization axiom
appears. Existing-source actualization remains exactly closed trace image.

## A01/A06: source comparison survives, information direction matters

For total common-alphabet actions, word induction proves exact reindexing
of all-word stable equivalences, independently of source surjectivity. Under
relation inclusion the repair is an interior/right adjoint, not a closure
operator. The new report-code comparison must use `f* ker h_Y` when pulling
back target repair; replacing it with native `ker h_X` is incorrect unless
the code preserves the relevant report information. X01 explicitly records
this distinction and exhibits a carrier bijection with information loss.

## Root compact-policy theorem: survives, formal scope is narrower

The root formal file uses a total stop:S→Nat and openness of every bounded
halting set {s:stop(s)≤n}. Compactness of S and the directed open cover give
one N. This is a correct precise statement, independently compiled. It does
not formalize causal replay, policy nonanticipation, or cylinder continuity;
the root paper explicitly carries those separate obligations.

The paper proof is valid for a fixed deterministic nonanticipatory policy:
compatible terminal cylinders are open, they cover the original state space,
and membership in one forces the unique execution to end there. Finite
outcome alphabets additionally make the tree below a bounded depth finite;
the same source-independent finite node costs then give a finite cost bound.
Unbounded hidden source-dependent costs remain outside the theorem. Correct
Boolean truth is clopen because both output classes are unions of terminal
open cylinders. No all-word counterfactual data are treated as one execution.

X01 adds a stronger single-action discontinuity control: compact
{0}∪{1/n}, continuous binary-digit shift, discontinuous parity readout. It
simultaneously invalidates actualization and uniform stopping if continuity
is removed, without introducing infinitely many distinct test actions.

## New X01 formalization and independent controls

The new module imports B09 and proves the explicit trace-level transport and
actualization reflection gate. Its quantified map equality is a premise,
not a Boolean flag or a fictitious source certificate. T2/T3 remain paper
proofs; this boundary is marked beside the module and dossier claims.

The new Python oracle imports no existing repair implementation. It traverses
complete deterministic pair orbits to decide behavior, and separately
generates finite coded report rows for the recovery criterion. Every binary
source/report/map tuple is enumerated; failing action commutation is excluded
as an invalid strict map and tested explicitly as a theorem mutation.

Portable reproduction after building the pinned package's dependency:

```sh
lake build SwarmTopology
lake env lean SwarmX01CompletionTransport.lean
```

On this host, official Lean required the already-existing narrow procfs
executable-location shim. It does not alter the Lean kernel. Actual commands
used a temporary olean directory and the existing mathlib checkout:

```sh
# Working directory: /workspace/scratch/79b9e8091cb9/mathlib-root
PATH=/workspace/scratch/79b9e8091cb9/lean-root/lean-4.14.0-linux/bin:$PATH LD_PRELOAD=/workspace/scratch/79b9e8091cb9/compat/proc_exe_fallback.so lake env lean --root=/workspace/scratch/79b9e8091cb9/cross-X01/formal/swarm_topology -o /workspace/scratch/79b9e8091cb9/x01-lean/SwarmTopology.olean /workspace/scratch/79b9e8091cb9/cross-X01/formal/swarm_topology/SwarmTopology.lean
PATH=/workspace/scratch/79b9e8091cb9/lean-root/lean-4.14.0-linux/bin:$PATH LD_PRELOAD=/workspace/scratch/79b9e8091cb9/compat/proc_exe_fallback.so lake env bash -c 'export LEAN_PATH="/workspace/scratch/79b9e8091cb9/x01-lean:$LEAN_PATH"; lean /workspace/scratch/79b9e8091cb9/cross-X01/formal/swarm_topology/SwarmX01CompletionTransport.lean'
PATH=/workspace/scratch/79b9e8091cb9/lean-root/lean-4.14.0-linux/bin:$PATH LD_PRELOAD=/workspace/scratch/79b9e8091cb9/compat/proc_exe_fallback.so lake env lean /workspace/scratch/79b9e8091cb9/SUCC/formal/swarm_topology/SwarmPolicyCompactness.lean
```

All three compilation gates exited 0. An initial attempt to emit B09's olean
from outside the package root failed because `--root` was missing; it was
corrected before successful compilation and was never counted as validation.
Four new targeted unit tests passed. Aggregate full-suite and provenance
validation are assigned to root integration, not claimed as run by X01.

No source changes were needed to the audited B09 or policy proofs. The root
paper's bibliography at this snapshot still names the wrong authors for
arXiv:2507.18539; root already has its correction in flight. That citation is
explicitly non-load-bearing and does not affect the reviewed arguments.
