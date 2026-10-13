# SWM-X03 — Obstruction-preserving gluing and finite counterexample-guided repair

## 1. Original question

Can a failed local-to-global observational model guide an expanding constructor
search without losing its counterexample or inventing a new source? This is the
cross-domain cut A03 × F42/F44, checked against F48's history boundary.

## 2. Existing mathematical context

Assignment restriction and global-section obstructions are classical; see
[Abramsky–Brandenburger, 2011](https://arxiv.org/abs/1102.0264). Finite
counterexample-guided synthesis is also classical; see
[Solar-Lezama et al., 2006](https://people.csail.mit.edu/asolar/papers/asplos06-final.pdf).
Both primary sources were inspected. The local result below couples exact
pullback maps and inherited unsatisfiable cores with a bounded grammar search;
it is not a new general sheaf theorem. Scholarly priority is **UNVERIFIED**.

## 3. Proposed SUCC objects

Let V be finite typed coordinates, D_v finite nonempty sets, and
X ⊆ ∏_(v∈V) D_v a fixed, completely declared original source carrier. X may be
empty, in which case that fact is recorded as inconsistency, never empirical
certainty. Each provenance-named constraint i has scope C_i ⊆ V and relation
R_i ⊆ ∏_(v∈C_i) D_v. Let π_i:X→∏_(v∈C_i) D_v be restriction and

G_X(I) = ⋂_(i∈I) π_i⁻¹(R_i) ⊆ X.

A constructor extension supplies a carrier Y and an explicit original-retaining
map p:Y→X. Its inherited constraint is (π_i ∘ p)⁻¹(R_i). Extra coordinates may
be hidden variables or deterministic probes. The implementation takes p to be
typed coordinate projection and rejects a candidate whose projection invents
an original outside X. The theorem holds for arbitrary functions p.

A bounded typed grammar has a finite semantic candidate set Γ ⊆ Y. Its source
coverage is p(Γ), independently checked against X. Constructor syntax is not
assumed to authenticate the denotation or to implement an empirical sensor.
Constraints are fixed throughout one run; old source reports are not mutable
fitness weights. A minimal unsatisfiable core means **inclusion-minimal**, not
minimum cardinality, relative to the stated carrier.

## 4. Candidate theorem

**Obstruction transport and sound finite synthesis.** For every such X, Y, p,
finite constraint index set I, and J ⊆ I:

1. G_Y(J) = p⁻¹(G_X(J)). Hence G_X(J)=∅ implies G_Y(J)=∅ for every extension.
2. If p is surjective, p(G_Y(J))=G_X(J). Thus satisfiability of **every** subset
   of inherited constraints, and consequently all inclusion-minimal
   unsatisfiable cores, is preserved exactly.
3. For finite Γ and exact verification, the following monotone loop terminates.
   Choose any candidate satisfying every retained constraint. Verify it against
   every original constraint; either return its witnessed global section or
   retain one violated constraint. If no candidate remains, report
   `UNSAT_GRAMMAR`; promotion to `UNSAT_SOURCE` requires p(Γ)=X. There are at
   most min(|I|,|Γ|) failed verifications and at most one final successful check.
4. An unsatisfiable inherited core is a sound pruning certificate for **every
   future** source-retaining grammar extension, even if the new grammar is
   larger. The certificate ceases to apply if a core constraint or its
   interpretation is weakened. Such a change is a new observational contract.

This establishes a limited repair operation: remove unsound proposed models by
adding inherited obligations to their verifier. It cannot repair an actually
inconsistent full original contract by adding syntax or variables.

## 5. Proof attempt — full bounded derivation

For any y∈Y, membership in G_Y(J) means (π_i∘p)(y)∈R_i for every i∈J. This
is precisely p(y)∈G_X(J), proving assertion 1. The forward image is always
contained in G_X(J). If p is onto, every x∈G_X(J) has y with p(y)=x; that y
satisfies every pulled-back constraint, giving equality. Applying this to each
J and each J\{j} proves exact transport of minimal cores. No probability,
compactness, sensor availability, or physical gluing is hidden in this step.

For the search, let L_t ⊆ I be retained indices and
H_t={γ∈Γ : pγ∈G_X(L_t)}. Initially L_0=∅. If a chosen γ_t fails constraint j,
then j∉L_t, because γ_t satisfies all of L_t. Set L_(t+1)=L_t∪{j}. Thus
L_t grows strictly and H_(t+1)⊊H_t: γ_t is permanently excluded. Both |I| and
|Γ| bound the number of failures. A successfully verified candidate satisfies
all constraints and its projection is an actual mathematical section in X.
If H_t=∅, no Γ candidate satisfies all constraints. Only the checked coverage
p(Γ)=X turns this into G_X(I)=∅; otherwise a section may simply be missing
from the grammar. Finite exhaustion therefore has a scoped verdict.

To extract a core, start from an unsatisfiable retained set L and successively
delete a constraint only when the remaining set stays unsatisfiable. The
result stays unsatisfiable. Whenever deletion of j was refused, the then
remaining set without j had a witness. Later deletions cannot invalidate that
witness, so deleting j from the final core is satisfiable. This proves
inclusion-minimality. Apply assertion 1 to cache this core across future
source-retaining extensions. Proof obligations depend on the full constraint
semantics, not merely their human-readable names.

The algorithm is exact finite enumeration; a fair unbounded syntax generator,
an incomplete verifier, or an unknown empirical source does not satisfy these
termination/completeness hypotheses.

## 6. Crucible

**Overlap agreement does not glue.** On three bits use xy equality, yz equality,
and xz inequality. Every overlap projects onto both bits; all three relations
are nonempty. The three constraints form a minimal unsatisfiable core.
Deleting any one supplies witnesses. Adding an arbitrary hidden bit duplicates
the eight original states but retains exactly the same core. Adding the
deterministic parity probe gives a graph bijective with X and also cannot fix
the inconsistency.

**Grammar failure is not source failure.** X={0,1}, constraint x=1, and grammar
Γ={0} yields `UNSAT_GRAMMAR`; the original section 1 exists. A grammar proposing
an undeclared original is rejected rather than accepted as a source extension.

**Surjectivity is necessary for minimality.** On X={0,1}, the pair of constraints
x=0 and x=1 is a minimal core. Restrict Y to original 0; the lifted constraint
x=1 alone is now an unsatisfiable core. Inconsistency still transports, but
minimality does not. No claim that arbitrary observation-induced restriction
preserves minimality survives this control.

**Forgotten counterexamples cycle.** For the same contradictory one-bit pair,
a learner retaining only its most recent violated constraint proposes
0,1,0,1,… indefinitely. Retaining both terminates after two rejections. A
stochastic/genetic proposer has the same issue unless exact inherited
verification is enforced; this experiment tests a concrete forgetful proposer,
not every possible genetic algorithm.

**Changing the problem can create sections.** Relaxing the triangle's xz
inequality to the full binary relation produces 000 and 111. Those fail the old
constraint. This is an explicit source-report-model change, not a conservative
resolution of the original obstruction.

**Static sections do not authorize causal amalgamation.** For original bits
(a,b), constraints a=1 and b=1 have section 11. If reading a erases b, the
actual sequential report (a=1, then b=1) has no original realizer. A projection
on original assignments is not the changed-carrier replay map. F48's availability,
outcome and update obligations remain necessary.

All 4,096 binary triangle relation families are checked against an independently
written direct join oracle. Every unsatisfiable CEGIS result has its returned
core checked for unsatisfiability and every one-constraint deletion checked for
a witness. Typed-domain, forgotten-coordinate, duplicate-provenance, empty-
grammar and undeclared-original mutations are also exercised.

## 7. Verdict

**PROVED LOCAL** for the stated projection/obstruction and finite-search bridge,
with a full paper proof and exact finite controls. The pullback identity, minimal
core deletion argument and finite CEGIS principle are **CLASSICAL** ingredients.
**REFUTED**: adding hidden variables or deterministic probes while retaining the
original constraints can repair a genuinely inconsistent original contract.
**REFUTED**: exhaustion of an incomplete typed grammar certifies no original
source section. No Lean proof or empirical-source authentication is claimed.

## 8. Remaining obstruction

The declared source table may itself be a wrong empirical model. This procedure
can locate an inconsistent contract and show which assumptions a change would
affect; it cannot decide which real sensor or causal interpretation is wrong.
Unbounded grammars need separate fair enumeration and semidecision statements.
The smallest next formal lemma is an inductive constructor interpretation that
produces an original projection plus kernel-checkable constraint pullback
proofs; every stored core would then be reusable as a checked pruning lemma.

## 9. Cross-domain connection

A03's relation-valued local reports become original-coordinate constraint sets.
F42's typed constructors contribute p:Y→X, so their soundness obligations can
transport the very obstruction that defeated the previous model. F44's no-go
is reflected in the deterministic-probe graph: recomputation of existing
coordinates leaves the possible original sections unchanged. A new physical
sensor may improve target identification on a **consistent** source; that does
not make inconsistent old equations jointly true. F48 marks the limit of this
bridge: original-section compatibility is semantic, while lawful joint history
requires its own causal replay. No arrow to an RH positivity statement appears.

## 10. Deliverables

Frozen baseline: `71eaf11e48ca3ccb349858bba64abf36b59ee6f5`; independent worktree
`cross-X03`, branch `research/swarm-x03-2026-10-13`. Additive files only, without
modifying provenance archives or shared ledgers. Implementations:
`observational_succ/swarm_gluing_cegis.py`,
`tests/test_swarm_gluing_cegis.py`, and `scripts/swarm_x03_probe.py`.

Executed validation is recorded in `X03_RECEIPT.json` and `X03_REVIEW.md`:

```sh
python -m unittest discover -s tests -p 'test_swarm_gluing_cegis.py' -v
python scripts/swarm_x03_probe.py --output research/2026-10-13/SWARM_ATLAS/X03_RECEIPT.json
```

This synthesis owns 11 targeted tests. Full integration validation belongs to
the coordinating branch; it is not asserted by this isolated assignment.
