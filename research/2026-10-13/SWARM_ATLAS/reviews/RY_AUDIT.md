# RY — Independent adversarial audit of six remaining synthesis bridges

Reviewer: `audit_remaining_bridges`, independent of the six synthesis authors
and their donor cohorts. This report audits mathematical scope, retains
counterexamples to stronger interpretations, and uses an independent exact
probe importing no repository modules. It does not run or claim the full suite,
re-prove analytic compactness in Lean, or authenticate any empirical source.

## Frozen sources

X02, X07, and X09 were read at
`ed102851f0566d3bc84fa140f2b6232d7c6f53ff`; X06 at
`1c9c415b26ced094813cd6ea68321c8869f66aef`; X03 at
`5e4be93cf41317f5c63f6652565ca1323551e7fc`; X11 at
`19fc6acf8db81d6361c6779d6aa06919e20d35fc`. The receipt records SHA-256 hashes
of each exact dossier retrieved from its frozen Git object. Associated probes
and implementations were inspected as supporting material. All six assigned
reviews are complete.

## Finding corrected during this audit: X03 cached cores

The pullback identity, surjective preservation of inclusion-minimal cores, and
finite rejection bound survive. The transition from a returned CEGIS core to
the proposed future-extension pruning certificate needs an explicit carrier
condition. `monotone_cegis` correctly returns `UNSAT_GRAMMAR` for an incomplete
grammar, but its returned `core` is minimized on the **projected grammar**
`p(Γ)`, not automatically on the full original source X.

The smallest nontrivial counterexample is X={0,1}, Γ={0}, and sole constraint
x=1. The implementation returns `UNSAT_GRAMMAR` and core {x=1}. Extending the
grammar to Γ′={0,1} yields `SAT_SOURCE` with witness 1. Therefore that returned
grammar-relative core cannot prune every future source-retaining extension.
Both outputs were executed directly and agree with this elementary argument.

The repair is to require `G_X(core)=∅` before source-wide caching. Verified
coverage `p(Γ)=X` suffices; a separate exact check on X can suffice even without
coverage. A grammar-only core is safe only when future projected candidates
stay within the carrier on which it was proved unsatisfiable. State this
condition in X03 §4(4) and the core-extraction paragraph in §5; expose or
document the returned core's carrier so `UNSAT_GRAMMAR` cannot be promoted
through the caching bridge. This is a scope correction to the caching claim,
not a refutation of conservative obstruction transport.

**RESOLVED.** The integrator amended §4(4) and §5 with the explicit original
source gate and added `core_scope` (`SOURCE`, `GRAMMAR_IMAGE`, or `None`) and
`core_source_verified` to returned results. The latter is certified through
checked projection coverage; no broader unperformed source check is claimed.
A new regression preserves the incomplete-grammar counterexample, its
satisfiable extension, and an actually contradictory full-source positive
control. I inspected those exact changes independently. The receipt separately
hashes the corrected working dossier, implementation, and regression file;
the original frozen hash remains to preserve the finding's provenance.

## Finding corrected during this audit: X07 deterministic recovery

X07 §3 allows an arbitrary initial original/current law. Its §4(4) and
deterministic-recovery proof additionally require an actual deterministic
preparation `i:O→X`, with `μ_empty(o,x)=π(o)1[x=i(o)]` and π fully supported.
Deterministic instruments alone do not provide that premise.

For the smallest counterexample, take one original o, two current states,
and `μ_empty(o,0)=μ_empty(o,1)=1/2`. The instrument that reports the current
bit and retains it is deterministic. Both read-0 and read-1 histories have
positive support {o}. No single fixed preparation i(o) in F48 can realize
both histories. Thus a full-support original prior plus deterministic
instruments is insufficient for the claimed exact F48 recovery. The proof's
sentence asserting one current evolution per original has silently used a
deterministic initial coupling. This does not affect the correctly defined
stochastic support presheaf or the first three parts of the weighted theorem.
The independent probe includes both the mixed-preparation negative control
and its two deterministic-preparation comparisons.

**RESOLVED.** I inspected the integrator's exact theorem and proof amendment:
both now state the deterministic preparation explicitly. The mixed-preparation
counterexample and its two pure-preparation comparisons are retained in the
probe and regression suite. Corrected working-file hashes are recorded
separately from the original frozen dossier, preserving both the defect and
its resolution. No general stochastic functor claim required modification.

## X02: invariant marginal laws and actual global sections

**SURVIVES as a paper theorem.** Tree transport forces every local law from its
root law. The remaining equations are exactly holonomy invariance; finite
permutation invariance means equal mass on every orbit. Thus the law-section
simplex has one extreme point per orbit. A point section has a root in the
common fixed-point set, so a global joint law satisfying every edge equation
can have root mass only there. Conversely each fixed root determines exactly
one section, proving both the lift criterion and uniqueness for a supplied
law. A connected graph and invertible transport are essential here.

The original-index version is rowwise invariance, not a free replacement of
the original/current coupling by marginal laws. In a transitive nontrivial
orbit, invariant conditional rows are uniform and the current state conveys
no original distinction beyond the retained prior. The target criterion is
precisely constancy of the target on each positive conditional support. Null
original rows do not certify any original proposition.

The independent probe uses relation closure and exhaustive actual three-vertex
assignments, rather than the synthesis author's generated-group algorithm.
It checks 617 permutation-generator pairs on fibers of sizes 1–4, 20,721
denominator-four laws, and 963 invariant-law global-lift cases. A law on a
nontrivial orbit can satisfy every local marginal equation while having no
global supported coupling. No probabilistic averaging repairs that distinction.

## X07: weighted histories, normalization, and opposite variance

**SURVIVES as a paper theorem, with the deterministic-recovery premise above.**
Finite nonnegative sum interchange proves the
forward subprobability functor. The unique outgoing lift above a fixed kernel
is exactly the discrete opfibration condition. Conversely original supports
can only shrink under extension, giving the opposite-variance presheaf and
discrete fibration. Neither categorical construction alone supplies an actual
physical history or latent-variable completeness.

Partial normalization composes with equality of domains: if the prefix mass
is zero then every extension remains zero; if it is positive, the intermediate
normalizer cancels and the remaining domain condition is positive total
composite mass. The trace quotient needs equality of **unnormalized** products
for every original/current preparation. Point preparations recover every
matrix entry, making that universal quantifier sufficient and necessary.

The independent probe checks a fixed catalogue of 20 three-state kernels in
400 ordered pairs against direct path sums on eight original/current laws:
3,200 cases, including 2,210 positive normalizations and 990 null cases.
It also reconstructs `DN=2ND≠ND`: all corresponding positive posteriors agree
while likelihoods differ. Hence posterior-only equality cannot authorize the
weighted quotient. Fixed named event DAGs retain outcome identities and
adaptive dependencies; this theorem does not authorize arbitrary reordering
of a feedback policy. Positive finite prefixes still need not yield a positive
probability infinite event.

## X09: analytic actualization needs both bound and closedness

**SURVIVES as a paper theorem.** The uniform coefficient bound supplies a
geometric tail on each smaller disk and makes evaluation continuous in the
product topology. The coefficient product is compact; a closed source subset
is therefore compact. Its report image in the Hausdorff product of complex
values is closed. Finite simultaneous approximate compatibility is exactly
membership in the closure and therefore gives an actual source. Empty source
sets and M=0 cause no exception to the quantifiers.

Neither the hypothesis nor the proof is a certificate that arithmetic data
possess the needed common bound and closed source law. Arbitrary polynomial
interpolation lacks a common bound. Bounded-coefficient polynomials form a
nonclosed source class, so their geometric-series limit is a separate
closedness counterexample. Separate coordinate witnesses do not constitute
the common finite witness required by the theorem.

An independent Vandermonde solver, not the author's Lagrange helper, verifies
11 alternating prefixes of lengths 2–12 and the necessary coefficient bound
`M≥2n(n−1)`. Another 3,888 exact checks cover the sharp pairwise inequality
for five-term coefficient choices in {−1,0,1}. These finite checks supplement
the analytic derivation; they do not computationally prove infinite
actualization or Gamma uniqueness. Separately from the frozen X09 source, I
inspected E37's actual working-tree correction: it now treats the meromorphic
functional equation as classical input and explicitly infers neither a
zero-free region nor global nonvanishing. This resolves the wording issue
reported in X09_REVIEW; it supplies no new analytic or positivity theorem.

## X06: reusable memory and already-erased preparation

**SURVIVES as a paper theorem with the revised access boundary.** Deterministic
composition coarsens the partition of the same original set. Coloring each
final fiber injectively makes every earlier encoded stage injective with the
same memory label. The maximal final fiber is both necessary and sufficient.
The resulting stage maps are bijections between reachable encoded images;
they are not automatically permutations of unequal ambient product registers.

The independent probe exhausts simultaneous colorings on 4,764 small
composable map pairs, verifying that the final maximum fiber is the least
common-buffer alphabet and that the product bound holds. It separately
verifies that initialization of the form `m=k∘e₀` cannot separate originals
already identified by noninjective e₀. The frozen dossier now states original
access or initially injective preparation, the reachable-image restriction,
and dependence on the known finite program. These qualifications prevent the
existence theorem from promising an online physical recovery procedure.

Reusable buffer size, generator state count, retained record storage, and a
postulated debt recurrence remain different quantities. No thermodynamic or
general synthesis-termination conclusion follows from the fiber theorem.

## X03: remaining claims and independent finite checks

**SURVIVES after the caching scope is corrected.** Preimages commute with
intersections, so the gluing identity has no hidden completeness hypothesis.
Surjectivity is required only for the converse image equality and exact
preservation of all minimal cores. In finite CEGIS, each failed candidate
adds a previously absent constraint and removes at least that candidate, so
the rejection bound is `min(|I|,|Γ|)`. This is finite mathematical verification,
not empirical source completeness or fairness of an infinite syntax search.

The independent probe checks 110,592 pullback/subset cases and 4,096 finite
CEGIS problems on a three-element source. It includes the grammar-only core
counterexample above. Static sections still do not authorize a destructive
sequential experiment: causal replay is a separate map.

## X11: finite support and partial Boolean reports

**SURVIVES as a paper theorem.** Every ideal is a directed union of its
principal ideals. A principal ideal is compact because its generator must
occur in one stage of any covering directed union. Combining one finite
evidence support with finitely many required licenses therefore reaches one
common stage. Conversely an open set is the union of cylinders above its
compact pairs. This supplies an abstract support presentation, not an r.e.
presentation or the soundness of an existing formula.

For the Boolean representation, directedness and source-admissibility prevent
one ideal from containing finite cylinders certifying opposite values. A
clopen property has a finite cylinder around each original source on its own
side, producing the correct partial answer. Conversely the source embedding
pulls basic Scott opens back to relative product cylinders, and pulling back
the two open truth values proves both sides of the property open. No
compactness of the original source is used. Nonempty fibers are essential:
allowing an impossible support would incorrectly certify both values by
vacuity.

The eventual-zero first-zero-parity example correctly distinguishes a clopen
property on actual originals from a required answer at the phantom all-one
ideal. Every finite scattered all-one support has opposite-parity original
extensions. Scott continuity forbids either discrete answer at their supremum,
while a partial answer remains lawful. Kripke negation and arbitrary persistent
global properties are consequently outside the finite positive-proof theorem.
The non-r.e. support example correctly separates topological openness from
effective recognition.

The independent probe enumerates all 15 nonempty source subsets of two-bit
worlds. Its 95 admissible ideals are independently checked principal; 584
partial Boolean reports respect all 1,520 comparable pairs and agree with
every original point. Thirty-two scattered supports, including widely spaced
addresses, each retain two actual eventual-zero extensions of opposite parity.
These bounded models corroborate the written theorem, not an execution of an
infinite ideal or an analytic completion. No X11 correction is requested.

## Execution and limits

Run `python research/2026-10-13/SWARM_ATLAS/reviews/RY_probe.py` from the
published checkout. `RY_RECEIPT.json` records
the probe hash, exact source hashes and control counts. This audit claims
independence of derivation and finite probe from the reviewed implementations,
not independence from the shared task statement or donor mathematics. None
of these reviewed X02/X03/X06/X07/X09/X11 results is marked Lean-kernel-checked.
No new priority or RH-facing conclusion is established.

## Published-snapshot portability

The original independently executed probe had SHA-256
`6c78de814b86f1c7fc4d3865f50c5f3e273e8f50018682365fd6bf86e2eaa039`.
For publication, **only the `frozen_hash` provenance-loading wrapper changed**;
all mathematical probe functions, cases, and assertions are unchanged.
The wrapper now prefers the six bundled `frozen/RY_X*.md` files and checks
each file against its original commit, path, and SHA-256 recorded in
`RY_FROZEN_SOURCES.json`. The original Git objects were used to create these
byte-identical copies. Replaying this published audit therefore does not
require those local commit objects. Git retrieval remains only a fallback
when a bundled file is absent; the same expected hash is still enforced.

The finite probe was rerun after this wrapper-only change, and every reported
case count and mathematical control result was compared with the original
receipt and found unchanged. The refreshed receipt records the portable
probe's new hash, while the original hash above preserves the audit history.
Replay also passed with `PATH` set to an unavailable directory, so no `git`
executable could be called. An AST comparison verified that `frozen_hash` was
the sole changed function and that all other code was unchanged. The portable
probe SHA-256 is
`d5f5283c36b7d77a42324f1395160aa7e5f64bc9042c3da3492885756785aaf3`.
