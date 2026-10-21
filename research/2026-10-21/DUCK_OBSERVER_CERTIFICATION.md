# Duck observers: closed certificates, minimal quotients and separating probes

Date: 2026-10-21. Parent research head:
`9894d39250021bbbc2615c33dee0d286ddf0950f` (PR #232).
This lane owns `formal/DuckObserver.lean`,
`observational_succ/duck_observer.py`, and `tests/test_duck_observer.py`.
It preserves `formal/DuckPrinciple.lean` and all imported archives.

**Initial status:** the mathematical statements below are **PAPER_PROVED**;
the finite implementation is **EXACT_FINITE_CHECK**. The seventeen new Lean
declarations require the coordinator's actual hosted compiler and axiom receipt
before any **LEAN_KERNEL_PROVED** promotion. The local toolchain was downloaded,
but execution returned `error: failed to locate application`; no local kernel
success is claimed. The coordinator's final receipt supersedes this explicitly
historical pre-build status without changing what was observed here.

These are classical deterministic-observer/automata constructions, newly
connected to the SUCC Duck and causal interfaces. Academic novelty is not
claimed. They do not prove discovery completeness, physical-source identity,
normality of pi, RH or ABC.

## 1. Hole contract

The exact missing bridge was:

> Turn a proposed map and a declared finite observation model into either a
> complete structural certificate, a finite distinguishing experiment, or an
> explicitly unresolved resource-exhaustion outcome.

The weakest sufficient infinite-word certificate is a relation containing the
initial pair, agreeing on current reports, and closed under every declared
action. The universal implication is induction on finite words; it does not
require executing infinitely many experiments. A complete finite table can
discharge its hypotheses. A fixed finite sample without closure cannot.

This closes the Duck existence-to-executable-probe gap for total stationary
finite models. It is not the pi-normality problem restated: finite observer
equivalence is decidable under an independently declared state bound, whereas
the source-specific unbounded pi orbit has no such finite model supplied.

Cheapest falsifiers: remove one transition-closure pair, change a current
readout, change the bound model's epoch, erase a separating report, or stop BFS
before its reachable pair set closes. All are permanent negative controls.

## 2. Exact universal objects and laws

Fix arbitrary types `Act`, `X`, `Y`, `Out`, transitions
`stepX : Act -> X -> X`, `stepY : Act -> Y -> Y`, and readouts into the same
declared output type. The state and action types need not be finite for the
Lean laws. Reuse `ObservationalSUCC.Duck.runWord`: the head action executes
first, then the tail. Define an **observed morphism** `f:X->Y` by

\[
f(\operatorname{step}_X(a,x))=\operatorname{step}_Y(a,f(x)),\qquad
o_X(x)=o_Y(f(x)).
\]

Surjectivity is not part of this morphism definition; an onto dynamical factor
requires it separately. The executable common-factor routine checks onto maps
on both sides. Identity and composition preserve both laws, and every word
preserves the readout. Composition is ordinary function composition; this file
does not claim a separately elaborated mathlib `Category` instance.

For a single source, put

\[
x\sim y\iff\forall w\in\mathrm{List}(\mathrm{Act}),\quad
o(\operatorname{run}(w,x))=o(\operatorname{run}(w,y)).
\]

The empty word gives current-report equality; prepending an action gives
forward congruence. This relation is an equivalence. Its Lean `Setoid`
quotient has well-defined action and readout, and projection is an observed
morphism. Quotient equality is exactly behavioral equality. The quotient
is behaviorally separated: all-word agreement of quotient states forces
their equality.

Every observed morphism has fibers contained in `~`, because equal images
have equal word readouts. Hence this is the **coarsest observation-preserving
action quotient**, not a reconstruction of all hidden states. If the target
is itself behaviorally separated, the morphism is constant on `~` and factors
uniquely through the quotient. The induced lift is again an observed morphism.
No source identity, physical intervention, or unseen experiment is supplied
by this universal property.

The relation-certificate theorem is slightly more general. For
`R : X -> Y -> Prop`, assume

\[
R(x,y)\Longrightarrow o_X(x)=o_Y(y),\qquad
R(x,y)\Longrightarrow R(\operatorname{step}_X(a,x),\operatorname{step}_Y(a,y))
\]

for all states and actions. If `R(x0,y0)`, induction on `w` gives equal word
readouts from `x0,y0`. Both hypotheses are essential, and their exact types
are retained by `closed_relation_all_words`.

## 3. Lean declaration-to-meaning map

All names have prefix `ObservationalSUCC.Duck.Observer`.

| Declaration | Exact role |
| --- | --- |
| `identity_morphism` | The identity preserves actions and current readouts. |
| `compose_morphism` | Two observed morphisms compose with the same action/output types. |
| `morphism_word_readout` | Their finite-word final readouts agree universally. |
| `behavior_step` | Behavioral equality is closed under every action. |
| `closed_relation_all_words` | Report agreement plus action closure proves all-word agreement. |
| `validated_table_all_words` | A checked finite Boolean relation table supplies both complete hypotheses. |
| `finite_table_positive_control` | An exact erased flip/idle relation is accepted. |
| `finite_table_closure_negative_control` | Dropping a necessary successor pair is rejected. |
| `finite_table_readout_negative_control` | A related pair with different readout is rejected. |
| `quotient_is_morphism` | The actual behavioral quotient has the declared structure. |
| `quotient_equality_iff_behavior` | Quotient equality has exactly the proposed meaning. |
| `quotient_is_behaviorally_separated` | No distinct quotient states have identical all-word behavior. |
| `factor_fibers_refine_behavior` | An observed morphism cannot merge distinguishable source states. |
| `separated_factor_respects_behavior` | A separated target does not retain behaviorally redundant distinctions. |
| `quotient_universal` | Unique pointwise lift for maps constant on behavioral classes. |
| `separated_target_factorization` | The lift into a separated target is an observed morphism. |
| `morphism_iff_existing_descent` | Exact compatibility with the prior partial/cost interface on the total unit-cost slice. |

The declarations contain no self-declared axioms, admitted placeholders or
native evaluation standing in for proof. Quotient reasoning may use Lean's
standard quotient/extensionality dependencies; the actual dependency list
must come from `#print axioms`, not this expectation. Finite BFS termination,
shortestness and the Python refinement algorithm are **paper proofs below**,
not additional Lean declarations or a Lean-to-Python compiler theorem.

## 4. Finite probe synthesis and its proof

Let `n=|X|`, `m=|Y|`, with chosen valid initial states. BFS explores the product
transition graph. Each pair is enqueued only on first discovery, with its
action word. Thus at most `nm` pairs enter the queue. A dequeued pair with
different readouts supplies a genuine distinguishing word. FIFO order ensures
minimum length; deterministic action ordering resolves ties. The shortest
path has no repeated vertex, so its word length is at most `nm-1`.

An independent refinement argument gives the **sharp linear bound `n+m-2`**
whenever a distinguishing word exists. Form the disjoint union of the two
observers with their common action and output interface; it has `N=n+m`
states. Let `P_r` identify states agreeing on every word of length at most `r`.
`P_0` is the current-readout partition, and `P_{r+1}` refines by successor
`P_r` classes. If `P_{r+1}=P_r`, action congruence makes every later partition
equal too. Thus if a pair first separates at depth `r`, all `r` preceding
refinements must be strict. The initial partition has at least two classes
(otherwise all states report one common value forever), so `P_r` has at least
`r+2` classes. Hence `r+2 <= N`. This argument independently bounds an exhaustive
word-search horizon without relying on product-path counting. For two states
of a single `n`-state observer the same proof improves the bound to `n-2`.

Both linear bounds are attained. Take the unary `n`-state chain with transition
`i -> min(i+1,n-1)` and readout one only at its terminal state. Against the
one-state constant-zero observer, initial state zero first differs after
`n-1=n+1-2` actions. Internally, states zero and one first differ after `n-2`
actions for `n>=2`. Exact tests cover this family through `n=24`. The general
linear-bound proof is a paper proof, not an added Lean declaration.

If BFS empties without a difference, its complete reached-pair relation
contains the initial pair, every pair has equal current reports, and every
successor pair was inserted. The universal closed-relation theorem therefore
proves all-word equality. This conclusion uses known total transition tables;
it is not generalized from a long trace. If a caller's smaller pair budget is
exhausted, the implementation raises `ProbeBudgetExceeded`, with **no verdict**.

The independent final checker does not rerun BFS. For a `DistinguishingWord`
it replays the exact word and checks the unequal terminal reports. It certifies
that word, not its shortestness. For a `ClosedRelation` it checks root inclusion,
no repeated pairs, report equality and all action-closure cells. Both variants
are immutably bound to both complete finite models, including source tags,
epoch, interface, transition arrays and readout arrays. A valid certificate
for a different model is rejected. Arbitrary hostile Python code in the same
interpreter is outside this threat model; these objects are not installed
formal proof authority.

## 5. Minimal observable model and the common-factor calculation

Start with the partition by current reports. Refine each class using the tuple
of previous class and all successor classes. Every strict refinement increases
class count. Consequently there are at most `n-k0` strict refinements, where
`k0` is the number of initial report classes. A stable partition is an
observation-preserving action congruence and therefore has all-word agreement
inside every class by the closure theorem. Conversely all-word-equivalent
states survive every refinement, by induction on refinement depth. The final
partition is exactly `~`, and representatives define its finite quotient.
Empty carriers and empty action alphabets retain their literal meanings.

For two sources, reduce both to this separated quotient. Compare quotient
states by complete BFS certificates. When the sets of realized behaviors
coincide, matching is unique, is a bijection, and commutes with each action;
the two onto quotient maps give a common separated observed factor. Otherwise
there is no common **onto separated observed factor for this fixed interface**:
such a factor would have exactly the behavior set of both sources. This is
not a claim about arbitrary hidden common factors, different probes or source
ontology.

The default nontriviality requirement means at least two *behaviorally
distinguishable* states. For two erased flip clocks a nontrivial hidden common
clock certainly exists, but their minimal observable quotient has one state;
the routine correctly returns `None` under its declared stronger criterion.
An erased flip and erased idle model likewise agree on all readouts even though
the identity candidate fails its structural square. A four-state duplicated
flip and a faithful two-state flip instead produce a genuine common observable
two-state factor; their hidden carriers are not isomorphic.

## 6. Compatibility with existing SUCC machinery

* `DuckPrinciple.lean`: imports and reuses the original `runWord`, `IsFactor`
  and all-word theorem; no renamed competing word convention.
* `FutureSafeForgetting.lean`: `asPartial` uses `some (step a x, ())` and the
  same current readout. `morphism_iff_existing_descent` proves the exact iff
  with its `Descends` law. Partial enabledness and variable costs are not
  silently erased by a general claim.
* `causal_nerode_succ.py`: `from_causal_endo` consumes actual `SourceChart`
  and `CausalInstrument` objects, requiring one fixed chart and unit costs.
  Changing epochs/charts or variable costs is rejected. Reset availability
  is not inferred. The new quotient extends the one-step fiber repair to all
  finite words for these stationary finite models.
* `operational_yoneda_descent.py`: `as_eos_morphism` constructs the existing
  `CertifiedSourceMorphism`, with post-state readouts encoded in one shared
  alphabet and current readouts preserved as the target table. It respects
  EOS's nonempty-menu, 1..128-state domain and retains epoch in source tags.
  Its existing verifier is actually run. No new physical-source flag is set.
* `categorical_model_bridges.py` and `heuristic_bridge_discovery.py`: candidate
  similarity remains a search prior. This package supplies a separate exact
  finite-state acceptance boundary, not a replacement for their rational
  all-frequency identities or source-specific continuous models.
* `EODCS_NerodePlateau.lean`: the prior stationary one-update plateau theorem
  remains intact. The new closure theorem handles arbitrary action alphabets
  and two different state carriers; neither file falsely formalizes the
  finite-cardinality stopping bound by merely naming it.

## 7. Controls and observed validation

Command run on this lane:

```sh
python -m unittest discover -s tests -p 'test_duck_observer.py' -v
```

**13 tests passed.** Independent word enumeration checked 2,010 within-model
comparisons across every unary binary-output model with 1..3 states. Another
16,384 comparisons cover all pairs of two-state/two-action/binary-output
models and all initial pairs. The oracle enumerates words and applies raw
transition arrays; it imports neither the production BFS nor its partition
routine. An additional 4,096 common-factor decisions match a separate
exhaustive two-bijection oracle.

Negative controls cover missing closure, mismatching reports, a shortened
false witness, stale source/epoch/transition/readout binding, duplicate or
missing relation entries, immutable evidence, budget exhaustion, type-confused
indices, erasure, mismatched alphabets/bases, empty boundaries, changed causal
epoch and variable-cost adapters. The exporter additionally rejects stale or
nonclosed input and escapes hostile model labels in its complete JSON comment.
Finite census supports implementation
fidelity, not the universal proof by itself.

Proposed kernel mutations for the coordinator's genuine compiler:

1. Assert erased flip-to-idle identity is an `IsFactor`; the false Boolean
   action square must prevent elaboration.
2. Delete the relation closure premise from `closed_relation_all_words` while
   retaining its claimed conclusion. A pair with equal current output but
   differing first successor is the minimal semantic countermodel.
3. Assert quotient projection is always injective. Constant readout on two
   hidden states makes the quotient one point; the corresponding proof must
   fail. The correct theorem is equality iff *behavioral* equality.

Actual mutation outcomes and axiom/type exports belong in the coordinator's
hosted receipt; this dossier does not invent them.

## 8. Prior art, truth states and next discriminating probe

Finite observer minimization and behavioral congruence are classical
Myhill–Nerode/Moore machinery. BFS on the product is deliberately simple,
not an efficiency or originality claim. The original institutional record for
Hopcroft and Karp, *A Linear Algorithm for Testing Equivalence of Finite
Automata* (Cornell technical report TR71-114, December 1971), explicitly gives
a faster state/alphabet complexity bound:
<https://hdl.handle.net/1813/5958>. We inspected that primary archive record;
we do not claim this implementation is their algorithm or matches its bound.

The useful new-to-project result is the exact connection between the Duck
heuristic, a typed observed quotient, a finite closed witness and the existing
causal/EOS interfaces. The mathematical source is a declared finite simulator;
external-source authenticity remains a separate obligation.

Next verdict-changing proof debt: formalize the concrete BFS program and its
shortest-word bound. The finite-table exporter below instead provides a small
independent kernel-checking route for individual equivalence certificates;
it does not formally prove the Python search correct or shortest.
For pi, first supply an actual source-preserving finite quotient with an
independently proved global observation scope; mere similarity to a finite
clock cannot manufacture such a quotient.

## 9. A proof-producing finite certificate route

`RelationTableLaws` fixes the exact state types `Fin n` and `Fin m`, action
type `Fin k`, two total transition tables, natural-valued readouts and a Boolean
relation table. Its hypotheses are precisely report agreement at every related
pair and closure under every action. `relationTableValid` decides this entire
finite proposition. The theorem `validated_table_all_words` takes a proof that
this decision is `true`, recovers both hypotheses by `of_decide_eq_true`, and
applies the general induction theorem. There is no new axiom, native evaluation
shortcut, callback registration or presumed trust in the table producer.

Three separate declarations are exact controls: `finite_table_positive_control`
accepts the total relation between an erased two-state flip and a one-state
idle observer; `finite_table_closure_negative_control` rejects the singleton
nonclosed relation; `finite_table_readout_negative_control` rejects the same
total relation when the two-state readout distinguishes its states. These
are intended kernel computations using `by decide`, not finite experimental
substitutes for `validated_table_all_words`.

`lean_closed_relation_certificate` emits literal Lean tables from a supplied
closed relation, a shared injective natural-number encoding of the two models'
string readouts, and three declarations: complete table validation, initial
membership, and the resulting universally quantified `all_words` proposition.
The exact model and certificate are serialized as single-line ASCII JSON with
a SHA256 comment. Source labels cannot inject declarations. Empty action sets
are encoded with `Fin.elim0`; initial states ensure both carriers are nonempty.
The table producer first runs the Python checker, but this success is not used
as an axiom: Lean independently recomputes the finite laws. A complete source
hash and successful build of this generated file are still necessary before
calling any particular generated theorem kernel checked.

This is proof-producing translation for individual certificates, not a proof
that the Python exporter always preserves semantics. The exported literals,
shared readout encoding and original-model JSON must be compared independently
when binding a formal theorem back to a consumer claim. The hash authenticates
content against an externally pinned receipt; it does not authenticate the
physical source named in that content. A false generated table must fail
`checked`, irrespective of Python's prior verdict. No defense against arbitrary
hostile code running inside the same Python interpreter is advertised.
