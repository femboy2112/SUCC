# F43: bounded action-law discovery with an identity obstruction

## 1. Original question

Can an observer recover an unspecified action invariant from opaque labels,
without consulting a named presentation, and preserve what remains unidentified?
The faithful target is bounded discovery, not automatic creation of mathematics.
The programmer chooses source constructors and the term grammar; only the
learner is ignorant of the equations. This distinction is load-bearing. The
experiment starts at clean parent `5eb09e7cba36ec01b8f9d6834b78b5766fd93935`
on `research/swm-f43-2026-10-13`. No pre-existing sealed holdout was consumed.

## 2. Existing mathematical context

[Brown, *Semigroups, rings, and Markov chains*](https://arxiv.org/pdf/math/0006145),
§§1.1, 1.3, and 2.1, defines left regular bands by idempotence and deletion of
repeated factors, constructs injective-word examples, and gives their support
map to subsets. The recovered equations reproduce this classical structure
under an explicitly declared execution convention. They are not academically
new. [Angluin, *Learning regular sets from queries and counterexamples*](https://homepages.math.uic.edu/~lreyzin/papers/angluin87.pdf),
§1.1, distinguishes membership observations from an equivalence teacher. This
experiment has complete declared finite tables, but no teacher certifying
equivalence to an unrestricted unknown physical source.

## 3. Proposed SUCC objects

A table supplies a finite carrier (S), finite primitive menu (A), and total
maps (U_a:S\to S). Labels have no semantic interpretation. A word executes
left to right: (U_{wv}=U_v\circ U_w); operational multiplication therefore uses

\(\operatorname{End}(S)^{op}\). Source version means the frozen file hash.
The supplied grammar contains identity and all words of length at most four
over three action variables: 121 terms and 7,260 unordered candidate equalities.
Variable assignments range over *primitive* actions. The learner groups terms
by exact endpoint signatures and selects every class's shortest lexicographic
representative. It never receives constructor names, a deletion algorithm,
expected equations, or holdout tables.

## 4. Candidate theorem

**CLASSICAL finite soundness.** For every finite collection of complete total
tables, every selected equality (u=v), every supplied table (T), every
assignment \(\theta:\{0,1,2\}\to A_T\), and every \(s\in S_T\),
\(U_{\theta(u)}(s)=U_{\theta(v)}(s)\).
Under any carrier bijection and action renaming, the selected abstract equality
classes are unchanged. Completeness, determinism, closed transitions, and exact
label equality are hypotheses. This theorem certifies the finite source models;
it makes no assertion about unauthenticated missing states or different versions.

## 5. Proof attempt

The signature includes every triple assignment and every starting state.
Equality of signatures is consequently equivalent to the quantified conclusion.
For a carrier bijection (h) and action renaming (g), define
\(U'_{g(a)}=hU_ah^{-1}\). Induction on word length gives conjugate endpoints;
renaming only permutes quantified coordinates. Thus neither names nor row order
affect the result. The separate checker composes whole endpoint maps by prefixes
instead of interpreting each word separately.

An independent constructor argument establishes an unbounded **CLASSICAL**
corollary: for every finite alphabet and every finite word, injective-word
extension ignores every occurrence after the first. A first-write coordinate
likewise either remains zero throughout or takes its earliest nonzero paint.
Repeating a paint later cannot change that coordinate. Subset union also ignores
repetition. These arguments establish deletion for the stated families, not a
family identification inferred from training.

## 6. Crucible

Training used independently relabelled two-letter words (five states) and
two-coordinate paints (nine states, three actions). The learner found 16 classes
and 105 canonical rewrites. Generic context/variable-renaming compression found
`xx=x`, `xyx=xy`, and `xyzx=xyz`. It permits no substitution by composite
actions. First-constructor-only fitting has 13 classes; paint-only fitting has
16. This ablation exposes spurious equalities from a restricted menu. Complete
state/action renaming and reversed row/menu order preserve the combined classes.
A malformed table is rejected.

The holdout was frozen before the learner existed. Its sole evaluation checks
all 105 rules on 65-state/four-action word extension and eight-state/four-action
subset union: 436,800 and 53,760 equation/state/assignment checks, zero failures.
The 16-state last-occurrence control fails 42 equations in 10,944 instances.
Its recorded witness starts empty: actions `1,0,1` yield `(0,1)`, while `1,0`
yield `(1,0)`. All failures remain in the receipt.

## 7. Verdict

**SURVIVES, TESTED MODEL:** generic discovery and fresh finite transfer within
the stated grammar. **CLASSICAL:** exhaustive-signature soundness, relabel
invariance, and family-conditional deletion. **REFUTED:** identical lawful
reported histories determine full hidden source identity; §9 supplies the
receipt. Recovery of a classical presentation is a useful implementation result,
not open-ended mathematical creativity. Source validity is conditional on the
declared constructors. Independent principal/crucible acceptance remains pending;
no Lean-kernel, physical, RH, or positivity claim is made.

## 8. Remaining obstruction

The two source-generation functions use separate seeds, labels, and row
construction; the larger word source also uses a different enumeration and
transition expression. Nevertheless, all share one programmer, Python, and
constructor selection. This is generation separation, not empirical provenance
independence. More than three primitive variables, longer terms, composite
substitutions, partial tables, noise, and source authentication remain outside
the learned certificate. The supplied families explain the short laws; training
does not identify that explanation. Next falsification: a separately authored
finite source outside these constructors, frozen before selection, with four
variables and a longer grammar. Changing the present holdout or replaying it
would provide development evidence only.

The Aletheia coordinates remain separate: κ is contact with serialized simulated
tables; φ is exact survival under this finite word closure; σ is the documented
constructor route, not a physically authenticated source; ρ includes the
programmer's choice of repeat-insensitive training families. That choice creates
selection coupling, even though no expected equation enters the learner. μ gives
every candidate and every legal assignment nonzero coverage inside the fixed
grammar; it supplies no coverage outside it. The family ablation measures source
menu dependence. It does not turn the two constructors into independent empirical
witnesses, and no operational phase or truth probability is introduced.

## 9. Cross-domain connection with actual maps

Let (F_2=\{\epsilon,0,1,01,10\}\) with append-if-absent actions, and let
\(B_2=\mathcal P\{0,1\}\) with union actions. The report
\(q:F_2\twoheadrightarrow B_2\), (q(w)=\{\text{letters in }w\}\), satisfies
\(qU_a=V_aq\) for every state and action; the witness checks all ten squares.
Induction yields \(qU_w=V_wq\) for every finite word. Hence paired starts

\((s,q(s))\) have identical complete reported histories. Yet (01\ne10),
the five-state source actions do not commute, the four-state quotient actions
do commute, and their different cardinalities forbid source isomorphism.
This actual action-equivariant quotient connects experiment histories to a
semilattice observer while proving that observational equivalence does not
recover hidden order. The exact lamp is an order-sensitive additional report.
This obstruction concerns report-only access, rather than the complete declared
tables supplied to the learner.

## 10. Deliverables

`freeze_sources.py`, `learn.py`, and `check_once.py` are standalone bounded
standard-library witnesses. `training.json` and `holdout.json` are newly frozen
opaque tables; `source_manifest.json` preserves constructors, seeds, raw-label
maps, and order. `freeze_receipt.json`, `selected_laws.json`, and
`holdout_execution_started.json` preserve stage order and guarded selection.
`witness.json` preserves the sole holdout execution, counterexamples, resource
counts, and the identity obstruction. `RECEIPTS.md` records actual commands,
exits, and SHA-256 values. Maximum holdout workspace is 7,865 integer map cells;
the checker completed in 0.118388 seconds. Only new F43 artifacts were written;
imported originals, runtime defaults, and shared registries were untouched.
