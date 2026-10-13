# RA — Independent adversarial category audit

Audited immutable source: `34904661c721ea9140c5994be5ca964f4a806268`
in `/workspace/scratch/79b9e8091cb9/swarm-A`.
Scope: AGENTS.md, A01/A06/A07/A08 dossiers, swarm_categories.py and its tests.
No source worktree or shared research document was modified.

## Verdict

**SCOPED PASS, with one LOW API boundary finding.** No counterexample was
found to the stated deterministic all-word repair, coreflection, base-change,
mixed-action criterion/minimality, origin/current filtered-image identity, or
strict report 2-category laws. The general all-word base-change, relation
coreflection, equivalence preservation and idempotence were independently
formalized and actually compiled in Lean 4.14 without mathlib or placeholders.

This is one same-model audit with an independently written lattice oracle;
it is method diversity, not independent reasoner provenance. Finite enumeration
is bounded evidence; the universal base-change/coreflection claims additionally
have kernel-checked proofs under their explicit hypotheses.

## LOW RA-01 — unavailable action is not always rejected

`belief_update` checks action availability only by calling `source.step` inside
the loop after report filtering. Consequently both calls below silently return
an empty belief:

```python
belief_update(source, frozenset(), 'missing', 0)
belief_update(source, frozenset({(0, 0)}), 'missing', 9)
```

Here source is the complete three-state source with reports `(0,0,1)` and
declared actions `a0,a1`. `missing` is outside its declared alphabet. An empty
belief is the smallest witness; a one-pair filtered-out belief is the nonempty
control. This does not refute the mathematical theorem quantified over a∈A.
It weakens the module's complete-source/availability rejection boundary.

Suggested fix: check `action in source.actions` at function entry and raise
CategoryError before filtering. Add both regression cases plus a legal action
on an empty belief as the positive control. The principal has been notified.

## Surviving claims and their quantifiers

**A01 — kernel checked.** For arbitrary types X,Y,A, total maps
TX:A→X→X and TY:A→Y→Y, any f:X→Y satisfying
f(TX(a,x))=TY(a,f(x)) for EVERY a,x, and ANY binary relation R on Y,
the two repaired relations agree pointwise for every x,y and ALL finite words.
Neither surjectivity nor injectivity nor report preservation is needed for
this equality. Restriction to equivalences supplies the Eq(X) coreflection.
The proof also works for infinite sets and empty action alphabets; the finite
Python implementation's nonempty action requirement is narrower.

**A06 — independent bounded exhaustive check plus local derivation.** The
independent oracle enumerates the entire equivalence lattice and selects the
greatest action-stable equivalence contained in R. It does not enumerate words
or use candidate partition refinement for its oracle. Candidate unary repairs
agree with that oracle for all maps on 1,2,3,4 states and every equivalence.
For all 66,282 ordered unary-action pairs and 986,718 pair/relation cells,
one-pass exactness holds iff IA preserves every B-stable equivalence;
commutation is sufficient in every case. There are no failed cells below
four states. At four states there are 23,040 failed relation cells among
983,040, and the smallest encountered witness is recorded in RA_receipt.json.
Among four-state action pairs 44,584 satisfy universal one-pass exactness and
33,784 commute, confirming that the sufficient condition is strictly stronger
than the exact criterion. Universal minimality still rests on the elementary
three-state equivalence-lattice proof, not on bounded enumeration alone.

**A01 origin/current transport — independent exact finite check.** All 512
subsets of the 3×3 origin/current carrier were checked for two destructive or
swapping actions and two reports: 2,048 cells. The independently written set
comprehensions agree before and after the nontrivial lawful quotient `(0,0,1)`;
no saturation assumption was introduced. Reading reports BEFORE the action is
essential to this particular formula. A before/after semantic convention swap
would require changing both sides.

**A07 — independent bounded check plus pointwise coherence derivation.** 500
seeded generated cases use nonsquare carrier changes 2→3→1→2, report widths
0,1,2, unused declared report labels, and potentially noninjective garblings.
Full object equality verifies strict 1-arrow and horizontal 2-cell
associativity, both 1-arrow units, and interchange. Flattened word alphabets
make regrouping strictly equal; fixed widths make all pair decompositions
unique. The model is deterministic total carrier maps with total report maps
that preserve the actual carrier transition. No larger stochastic/quantum or
carrier-changing 2-cell bicategory follows.

**A08 — local proof inspection and baseline reproduction.** The inverse
first-separation-depth pseudoultrametric and exact shortest-path resource
geometry survive their stated domains. Raw separation debt remains refuted as
a metric. This audit did not perform an additional exhaustive metric search.

## Hidden-target and availability attacks

The two-state source with identical reports, reset transition and constant
quotient has original targets `(0,1)`. No quotient decoder exists. Thus report
coherence alone cannot preserve original target homogeneity; A01 explicitly
requires target factorization and A07 explicitly disclaims the stronger claim.
This negative control is outside that hypothesis, not a counterexample to it.

Likewise costs `(0,1)` on states identified by a constant behavioral quotient
do not factor through the quotient. State-dependent partial availability could
also distinguish the same states. The finite-source objects here use the same
total action menu at every state; optimal policy transport is only licensed
when available actions and common costs are preserved. A08 states this gate.
These assumptions must be retained in any cross-domain theorem.

## Actual executed validation and artifacts

1. `python /workspace/scratch/79b9e8091cb9/reviews/RA_probe.py` completed exit 0;
   complete machine-readable counts and source/probe hash: RA_receipt.json.
2. `python -m unittest discover -s tests -p test_swarm_categories.py -v` in
   swarm-A completed exit 0: 20 tests passed.
3. `/workspace/scratch/79b9e8091cb9/lean-root/lean-4.14.0-linux/bin/lean
   /workspace/scratch/79b9e8091cb9/reviews/RA_Repair.lean` completed exit 0.
   `#print axioms` reports no axioms for repair_base_change,
   repair_coreflection, and repair_preserves_equivalence.

The first compilation attempt caught an incorrectly instantiated idempotence
helper proof in this audit file. It was corrected, then the entire final file
was successfully recompiled; the final successful result is the claimed run.
No full repository validation or external literature retrieval is claimed by
this independent audit. The principal's broader validation remains separate.

Next verdict-changing probe: extend origin/current transport to partial or
stochastic actions with explicit availability/coupling gates; the current
deterministic identity should not be silently generalized.

## Integration resolution

RA-01 fixed by validating the declared action before support filtering. Both
rejected calls and the legal-empty-belief control are in the integrated tests.
Root independently ran all 21 category tests successfully. The formal proof
is integrated as `formal/Swarm_Repair.lean`; historical audit paths above record
the original execution and are not claims of a portable runner.

The retained probe now takes `--source <checkout-of-3490466>` and prints JSON
without overwriting its historical receipt. Its historical digest predates
this portability-only wrapper change. It intentionally tests the pre-fix API.

Integrated A_CATEGORIES_RECEIPT test count is refreshed from 20 to 21 after
the new availability regression; all mathematical witness fields are unchanged.
