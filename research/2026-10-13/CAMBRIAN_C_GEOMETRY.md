# CAMBRIAN C — source histories, genuine probes, gluing, and minimal repairs

**Assignments actually executed:** 13–18. **Exact base:** `5eb09e7cba36ec01b8f9d6834b78b5766fd93935`.
**Worktree:** `c_geometry`. **Provisional claim namespace:** `CAMBRIAN-C`.
The six investigations were performed by one cluster worker, not six independent agents.
Initial theorem and countermodel conclusions were frozen with the coordinator before
cross-cluster synthesis. This report preserves that distinction.

**Principal result:** a source-changing, time-varying, nondeterministic history
realization theorem with compact closed constraints, and a genuinely kernel-checked
finitely branching specialization with no uniform state-size bound. Compactness,
closure, complete transition menus, and the original source-class specification
are separate premises. A stronger unrestricted inference is false.

**Additional sharp result:** obtaining one prescribed parallel section requires
`|Orb_H(x)|` sheets, whereas trivializing the whole transport requires `|H|`.
On a nonregular cover, deck invariance alone need not imply descent. The three-sheet
natural `S3` cover supplies an exact counterexample with a trivial deck group.
This does not contradict O569, whose cover is the regular holonomy-kernel cover.

All mathematics below is classical or a directly proved finite-model/interface
consequence. Independent academic priority, physical carrier authentication,
effective infinite execution, cognition claims, and RH consequences are not established.

## 0. State reconstruction and hole contract

Read before extending: `AGENTS.md`; foundations/method/architecture/roadmap;
O285–O295, O557–O571, O603–O619 and O638; the Voyager completion dossier;
the causal/Nerode dossier; existing formal trace, causal-descent and memory-debt
modules; `provenance/IMPORT_MANIFEST.json`; the actual Yoneda and cover code.
No imported or archival file was rewritten. Prior source-realization and
Weil/Gamma countermodels remain intact.

The precise dependency cut is:

`compatible finite actual histories → one global history in the declared source class`.

Voyager O619 gives compact-source realization for stationary deterministic trace
coordinates. The proposed extension allows different source types at each time,
relational instruments, and destructive readouts. Its weakest sufficient form
is compactness of the ambient history space plus closedness of every constraint;
determinism and stationarity are unnecessary. Its mathematical leverage is that
a global inconsistency then has a finite inconsistent history receipt. Its
novelty tax is substantial: this is Tychonoff/finite-intersection mathematics,
not a new general compactness theorem.

The cheapest falsifiers remove one premise at a time: a closed countdown on
noncompact naturals; a nonclosed countdown graph on a compact convergent-sequence
space; or a nonclosed original class of otherwise valid histories. A separate
finite-branching proof supplies kernel evidence without silently replacing a
topological proof with finite numerical testing.

## 13. Genuine restricted Yoneda observability

**Typed question.** For a small category `C` of source-backed contexts and a full
probe subcategory `D`, which source arrows are identified by

\[
N_D(X)=\operatorname{Hom}_C(-,X)|_{D^{op}}?
\]

Every arrow `f:X→Y` induces the actual natural transformation
`u↦f∘u`. Faithfulness means these transformations distinguish distinct arrows;
full faithfulness additionally says every natural transformation is induced by
one unique source arrow. Object identification requires the latter before
natural isomorphism can imply source-object isomorphism.

**Positive hypothesis versus rival.** Rich probe laws can suffice even with one
probe object. The rival says a few equal hom-set cardinalities already determine
objects or arbitrary arrows. Falsifier: retain literal precomposition maps and
enumerate natural transformations, then remove contexts or their laws.

**C13.1 — retract-probe sufficient theorem (CLASSICAL / PROVED LOCAL).** Suppose
every object `X∈C` is a retract of a probe `P_X∈D`: maps
`i_X:X→P_X`, `r_X:P_X→X` satisfy `r_X i_X=id_X`. Then `N_D` is fully faithful.

Proof: given `α:N_D(X)→N_D(Y)`, set
`f=α_{P_X}(r_X) i_X`. For any probe `P` and `u:P→X`, naturality for the
probe arrow `i_X u:P→P_X` gives
`α_P(u)=α_{P_X}(r_X)i_Xu=fu`. Uniqueness follows by evaluating at `r_X` and
composing with `i_X`. This requires the actual probe endomorphism/context laws.

**Executed example.** In the full finite-set category on cardinalities 1 and 2,
the single two-element probe, with all four of its endomorphisms, gives exact
`Hom/Nat` counts `(1,1),(2,2),(1,1),(4,4)` for the four source-object pairs.
Both objects are retracts of that probe. Ignoring its endomorphism laws would
allow `4^4=256` raw endomaps of its four-element hom-set, versus four natural ones.
The adapter uses all literal functions and compositions, and the repository's
existing naturality checker; it is not a cardinality-only approximation.

**C13.2 — two distinct failures (REFUTED stronger inference).** In divisibility
`C={1,2,3,6}`, `D={1}` makes the nerves of 2 and 3 naturally isomorphic singletons,
although neither `2→3` nor `3→2` exists. In the actual multiplication path
category, `1→6` has distinct `(2,3)` and `(3,2)` histories. Restriction to `D={6}`
collapses both induced transformations because `Hom(6,1)=∅`; `D={1}` detects them
at the precursor identity. Full Yoneda yields two source arrows and two natural
transformations. These reproduce and sharpen the context-versus-law distinction
already present in the repository rather than claiming a new Yoneda lemma.

**Limit/next lamp.** Source IDs are declared, not authenticated. Retract density
is a sufficient condition, not necessary. Next: prove source-admissible density
for a practically restricted intervention category without assuming access to
all source objects or to an unavailable reset instrument.

## 14. Sheaves, proof witnesses, and omitted source constraints

**Typed question.** Let `V` be source coordinates, each with a value set, and
let constraints `c` have finite scopes `E_c⊂V`. Define `F(U)` as assignments on
`U⊂V` satisfying every original constraint whose entire scope lies in `U`.
Restrictions give a presheaf. For which covers does literal witness gluing hold?

**Positive hypothesis versus rival.** Literal overlap agreement plus coverage of
every constraint scope suffices. The rival says any variable cover, or matching
coarse observation images, suffices. Define the falsifier before gluing: put
`x=y` across two singleton charts with source witnesses `x=0`, `y=1`.

**C14.1 — constraint-adapted sheaf theorem (PROVED LOCAL / classical sheaf law).**
Cover `U` by `{U_i}` such that every original scope `E_c⊂U` is contained in some
`U_i`. Then compatible source sections have a unique global source section.
Literal overlap agreement defines one assignment. Every constraint is tested
inside a chart that contains its full scope, so the assignment satisfies all
constraints. Variable coverage gives uniqueness. Identity covers, pullbacks by
intersection, and composition of these covers preserve the condition, giving a
Grothendieck coverage on the subset poset. The empty assignment is the singleton
section on `∅` when no contradictory empty-scope constraint is present.

That last condition matters: constraints of empty scope with no allowed tuple
make the whole model inconsistent. One may exclude them or keep a nonempty chart
cover of `∅`; do not silently declare an empty cover valid in an inconsistent
constraint model. The executable cases all use nonempty scopes.

**C14.2 — coarse compatibility is insufficient (REFUTED).** The singleton-chart
example omits the scope `{x,y}` and is rejected. Independently, each edge of an
odd XOR triangle has local source witnesses. Map every witness to a constant
observation 0: all observation overlaps match, but no binary global source
assignment satisfies all three inequalities. A quotient does not automatically
preserve the equalizer specifying descent.

**Verification.** All 4096 binary triangle relation systems were checked: literal
matching chart families produce exactly the global assignments independently
enumerated on all eight source triples. The mismatch, missing-scope, and coarse
XOR mutants are retained. Source witness checking is distinct from checking a
proof string: combining proof certificates additionally requires matching
theories, source provenance, and inference rules.

**Limit/next lamp.** No logical soundness theorem for arbitrary proof systems is
claimed. Next: transport proof-support objects over this coverage and isolate
whether their restriction maps preserve the necessary source equalizers.

## 15. Nonabelian holonomy: one section, every section, and descent

**Typed question.** A connected graph has invertible transports on finite fiber
`X`. After a spanning-tree gauge, `ρ:π1(G)→H≤Sym(X)` is its holonomy image.
For prescribed root value `x`, what is the smallest connected cover admitting
a parallel section with that root value? Is deck invariance enough for descent?

**Positive hypothesis versus rival.** A stabilizer cover suffices for one section.
The rival conflates this with full transport trivialization and extends the
regular kernel-cover deck-descent test to arbitrary covers.

**C15.1 — prescribed-section cover theorem (CLASSICAL / PROVED LOCAL).** Put
`H_x={h:hx=x}`. A connected pointed cover corresponding to `L≤π1(G)` admits the
desired section iff `ρ(L)⊂H_x`. Therefore `L⊂ρ^{-1}(H_x)` and

\[
[\pi_1(G):L]\ge [H:H_x]=|H x|.
\]

The subgroup `ρ^{-1}(H_x)` attains this degree. Construct its sheets as `H x`;
a gauged edge with based loop `g_e` sends sheet `y` to `g_e y`. The original
transport-compatible section is `q(v,y)=t_v(y)`, where `t_v` is the tree transport.
This establishes covering laws and section validity. The orbit is connected
because it is generated by the actual loop actions. To obtain any one section
without prescribing `x`, minimize `|H x|` over `X`.

Full transport trivialization instead requires `L⊂ker ρ`, of minimum degree
`|H|`, as correctly recorded by O567. These goals coincide for free transitive
actions but differ for nonfree actions. The natural `S3` action on three labels
requires three sheets for one chosen section and six for full trivialization.
A single transposition fixes the third label, giving degree one for that section
while its complete transport still requires degree two.

**C15.2 — nonregular deck-invariance inference (REFUTED).** Take the two-loop rose
with generators `(01)` and `(12)` on three sheets. Its monodromy is all `S3`.
The deck group is the centralizer of this natural action, which is trivial.
Its valid lifted section `q(sheet)=sheet` is therefore deck-invariant but varies
across each base fiber and cannot descend. Deck invariance characterizes descent
only when deck actions span the fibers, as on the regular kernel cover of O569.
On every cover the actual descent criterion remains constancy on each fiber.

**Verification.** 180 seeded connected permutation graphs, all three root values,
were compared with an independent raw-edge action-bundle BFS, without tree gauges
or group-generation algorithms. Centralizer enumeration independently verifies
the three-sheet counterexample. Cover minimality is the subgroup-index proof,
not inferred from the finite trials. Holonomy is mathematical transport; no
physical gauge field or quantum phase is asserted.

**Limit/next lamp.** The full cover-classification/minimality theorem remains
paper proof, not Lean. The next formal target is the subgroup-index lower bound
with an explicit action and connected-cover library.

## 16. Moonshot A: compact realization of changing relational histories

**Typed question.** For each `t∈N`, let `X_t` be a nonempty compact Hausdorff
original state type. The authorized instrument at time `t` has closed relation
`R_t⊂X_t×X_{t+1}`. Receipts specify closed state sets `C_t⊂X_t`; for example
`C_t=q_t^{-1}({z_t})` when `q_t` is continuous into a Hausdorff report space.
Relations may be nondeterministic, destructive, and time-dependent. Is one
original history realizable whenever every finite joint prefix is realizable?

**Positive hypothesis versus rival.** Closed compact histories suffice; mere
compatible finite reports do not. The rival drops graph closure, compactness,
or the complete original-class premise. All three deletions have explicit receipts.

**C16.1 — compact closed-constraint realization (CLASSICAL / PROVED PAPER).**
Suppose for every `n` there are `x_0,...,x_n` with `x_t∈C_t` and
`(x_t,x_{t+1})∈R_t` wherever those coordinates occur. Then there is one global
`x∈∏X_t` satisfying every receipt and transition. Conversely, a global history
supplies all prefixes. Thus global inconsistency implies some finite prefix is
already inconsistent.

Proof: the product `P=∏X_t` is compact by Tychonoff. Each coordinate receipt
and adjacent-coordinate relation pulls back to a closed subset of `P`.
A finite family of such constraints lies below a finite time bound and has
a source prefix witness; extend its unused coordinates arbitrarily using
nonemptiness and choice. The family has the finite-intersection property,
hence a common member. More generally the same argument permits any closed
finite-coordinate constraints, including declared finite-memory laws and
provenance consistency, provided finite families are jointly realizable.

The resulting history is in the **declared model of originals** exactly when
that original history class is precisely the set defined by the stated constraints,
or a further closed class constraint is included in the finite-intersection
premise. A locally defined Markov class is not automatically the actual physical
source class. This source-completeness gate survives the theorem.

**C16.2 — constructive-shaped kernel theorem (LEAN-KERNEL VERIFIED / classical choice).**
The standalone `formal/EODCS_CambrianRealization.lean` proves:

- State types are arbitrary dependent `S:Nat→Type`, so source types may change.
- `R_t:S_t→S_{t+1}→Prop` is arbitrary, nondeterministic and time-varying.
- Each actual source state has a complete **finite successor menu**.
- The original initial class has a supplied finite menu.
- For every depth there is some initial menu state with a legal prefix of that
  depth, possibly a different initial witness at every depth.
- One initial state and one global compatible history then exist.

This is the finitely branching Kőnig specialization. It assumes no uniform
finite-state bound: branching menus and state types can grow with time.
The proof first establishes downward closure of legal prefix depth. For any
finite menu and downward-closed property surviving each depth, one menu member
survives every depth: remove a member that dies at depth `k`, choose a witness
at `max(k,d)`, and induct on the remaining menu. Apply this to successor menus,
then recursively choose an infinitely extendable successor. The dependent
recursion yields the history. Receipts can be included in the edge predicate.

The compiled theorem depends only on `propext`, `Classical.choice`, `Quot.sound`.
It supplies existence; classical branch selection can be noncomputable. It
does not prove the full compact topological theorem because no topology library
is imported. Treating the paper theorem as topology-kernel checked would be false.

**C16.3 — remove compactness / finite initial completeness (REFUTED stronger claim).**
Let `X=N` with discrete topology and closed relation `n→n−1` for `n>0`.
Every depth `d` has the original path `d,d−1,...,0`. No infinite path exists,
since `x_n+n=x_0` would fail at `n=x_0+1`. These all-depth existence and
no-infinite-history statements are also Lean-kernel checked. The finite-branching
premise holds, but an arbitrary unbounded initial state class is not finite.

**C16.4 — retain compactness, remove closed graph (REFUTED stronger claim).**
Let `X={0}∪{1/n:n≥1}` with its inherited real topology. This is compact. Give it
only the transitions `1/n→1/(n−1)` for `n≥2`, with no outgoing edge at 0 or 1.
Every finite depth has a path beginning at `1/(d+1)` and ending at 1, but every
original path terminates. The relation is not closed: its edge pairs tend to
`(0,0)`, which it omits. Taking graph closure adds an artificial stationary
zero history. That is an ideal enlarged relation, not an original transition.
No topological computation is claimed by the Fraction formula checks.

**C16.5 — retain locally closed dynamics, remove original-class closure.**
On compact binary sequence histories, identity/shift local laws can allow the
all-one history, while the declared original class of eventually-zero histories
excludes it. Every finite report is matched by an original. This is Voyager
O620/O621, preserved here as the independent source-class gate. Compact local
coordinate spaces cannot repair an omitted nonclosed global preparation law.

**Verification/limits.** 240 independently seeded changing finite-type relational
systems with receipt erasure/selection were compared with Cartesian path
enumeration. These finite tests verify the code's source-support and history
calculations, not compactness for arbitrary spaces. No cost bound on the finite
refuting prefix, uniform effective branch selector, stochastic distribution,
or infinitely executed observation process follows from the existence theorem.

**Next lamp.** Formalize the topology theorem in a reproducible pinned mathlib
environment, and derive effective conditions under which an extendable branch
can actually be selected. Those are distinct obligations.

## 17. Open black boxes and the shared-witness composition defect

**Typed question.** An open behavior is a relation `B⊂I×O`, with existential
internal-state elimination. Serial composition identifies one typed boundary
`M` and uses `(T∘R)(i,o)⇔∃m:R(i,m)∧T(m,o)`. Does quotienting that shared
boundary by an observation `q:M→Q` commute with wiring?

**Positive hypothesis versus rival.** Literal relational composition is
associative and source-consistent. The rival assumes equality of coarse labels
is enough to identify actual internal witnesses.

**C17.1 — compositional boundary behavior (CLASSICAL / PROVED LOCAL).**
Relational composition is associative because both parenthesizations quantify
the same internal pair `(m,n)`. Identity relations supply units; products
supply parallel composition. For independently specified black boxes whose
entire shared variables appear in the interface, this is an exact behavior
semantics in `Rel`. Structured-cospan descriptions need a separately justified
black-box functor; this finite relation implementation does not construct the
whole cospan category or prove every RC/thermal/Markov model sound.

**C17.2 — quotienting before wiring can invent behavior (REFUTED).** Let
`M={m0,m1}`, `q(m0)=q(m1)=0`, `R={(in,m0)}`, `T={(m1,out)}`. Original serial
behavior is empty. Coarse wiring admits `(in,out)` by using `m0` on the left
and `m1` on the right. The false composite is not a physically possible joint
history. Uniform equality for **all** choices of `R,T` requires `q` injective:
this two-point construction refutes every noninjective q; injection proves
equality by recovering the same middle witness.

For particular systems, less is required. If right boundary behavior is
constant on `q` fibers (or if a suitably saturated left relation allows the
matching representative), coarse wiring is exact. Equal observation labels
without that behavior/source law are insufficient.

**Verification.** All 4096 triples of binary finite relations satisfy serial
associativity by independently compared compositions. The explicit false
middle-witness composite and its repaired version are in the frozen receipt.

**Limit/next lamp.** Shared environmental correlations must be included in the
interface or retained in joint source state. A black-box relation of a subsystem
alone does not authenticate independence from another subsystem. Next: check
the black-box functor on the existing dynamic RC bridge with complete temporal
interfaces, including storage modes rather than static voltages alone.

## 18. An obstruction-forced representation constructor and memory repair

**Typed question.** Given finite source interface `M`, baseline report `q`, and
right boundary relation `T⊂M×O`, construct the smallest sufficient refinement
from the source obstruction rather than choose a named prewritten template.

**Positive hypothesis versus rival.** The failed composition forces distinct
future behaviors to remain distinct. The rival adds arbitrary hidden labels or
hard-codes the particular two-state answer. Falsifier: enumerate unrelated
three-state output relations and all competing partitions.

**C18.1 — coarsest sufficient interface constructor (PROVED LOCAL / classical factorization).**
Define `B(m)={o:T(m,o)}` and

\[
q^*(m)=(q(m),B(m)).
\]

Its kernel is exactly `ker(q)∩ker(B)`. If a representation `r:M→Z` admits
decoders for both `q` and `B`, then `q*` factors through `r` by pairing those
decoders. Conversely a factorization through `r` supplies both decoders on its
realized image. Therefore `q*` is the coarsest sufficient refinement, unique
up to source-image isomorphism. No arbitrary classes are needed: the code
constructs signatures directly from the input relation. Under this refinement,
coarse serial composition equals the original for **every** left relation,
because two matched representatives have exactly the same right outputs.

**Verification.** All 512 relations from three middle states to three outputs,
and all eight left relations, preserve composition after generated repair.
All 64 three-state/two-output relations, all eight binary baseline reports,
and all 27 competing three-label maps were checked against an independent
fiber-constancy criterion: 13,824 universal-property partition cases. The
constructor operates on arbitrary supplied finite relations, not an answer
enumeration or fitted model template menu.

**C18.2 — exact history-support memory (PROVED LOCAL).** For a relational source
and matched receipt sets, let

\[
B_0=C_0,\qquad B_{t+1}=\{y\in C_{t+1}:\exists x\in B_t,(x,y)\in R_t\}.
\]

Induction says `B_t` is precisely the endpoints of realized matching finite
histories. Thus the current support, indexed by actual causal receipt history,
is a lawful powerset state and predicts possible continuations. Forgetting past
receipts can merge supports with different next behavior; retaining this state
repairs that representational defect. The destructive example ends in the same
erased physical state while its immutable past records still distinguish the
original bit. Endpoint support alone does not reconstruct every past witness
or original-source claim; store source/current pairs or complete histories
when those claims are required.

**Limit/next lamp.** This is one-step behavior sufficiency. Repeated actions
require right-language/continuation closure, as in the prior causal Nerode work.
Support equality is not stochastic-law equality (O607). The higher-order
constructor grammar is declared: products and exact powersets over a supplied
finite relation. It supplies principled model repair, not unrestricted invention
of new mathematics beyond that metagrammar. Next: prove a canonical constructor
for temporal interfaces whose minimal memory is unbounded but whose finite
prefix languages remain source-realizable.

## 19. Cross-cluster interface, independence, and dominance boundary

The verified bridge is:

`literal source witnesses → constraint-adapted gluing → exact relational wiring`
`→ closed compact history realization`.

Quotienting a witness before gluing/wiring can create a false equality. The
coarsest behavioral refinement repairs that finite compositional obstruction.
History-support memory makes receipt dependence explicit. None of these repairs
alone proves source-class closure: compact realization still needs the stated
closedness/completeness gate. Conversely compactness does not restore an
incorrectly glued witness diagram.

Two verification routes differ in mechanism but have different scopes: the
paper compact-product proof permits compact continuum state types; the kernel
proof permits arbitrary dependent state types with finite branching and finite
initial class. Cartesian histories, raw-edge action BFS, complete finite-source
assignment enumeration, and literal naturality checks fail differently. All
were written by this one cluster worker; they are not independent human or
different-model referees. A separate adversarial campaign audit is still required.

The framework survives with stronger conditional source-realization and repair
maps, and with the nonregular deck-descent overgeneralization explicitly killed.
It has no new source-exclusive arithmetic sign mechanism and carries no RH status
promotion. The context is not globally saturated: effective branch selection,
complete source attestation, full topology mechanization, and temporal black-box
interfaces can still change the verdict.

## 20. Reproduction and provenance

Additive artifacts:

- `observational_succ/cambrian_c_geometry.py`
- `scripts/cambrian_c_geometry_probe.py`
- `tests/test_cambrian_c_geometry.py`
- `formal/EODCS_CambrianRealization.lean`
- this report, `CAMBRIAN_C_ASSIGNMENTS.json`, and `CAMBRIAN_C_RECEIPT.json`

Targeted Python command actually passed: `python -m unittest discover -s tests
-p 'test_cambrian_c_geometry.py'` — **14 tests**. Exact receipt replay is one of
those checks; `python scripts/cambrian_c_geometry_probe.py` prints the source
controls. The three indexed counts above describe bounded cases, not the number
of independently commissioned agents or universally verified physical sources.

Standalone Lean command actually passed at this artifact state:

```sh
LD_PRELOAD=/workspace/scratch/6d134115e8ca/lean-runtime/self_exe_locator.so \
  /workspace/scratch/6d134115e8ca/lean-runtime/lean-4.14.0-linux/bin/lean \
  formal/EODCS_CambrianRealization.lean
```

The official Lean runtime's own-executable locator uses `/proc/<pid>/exe`,
which is unavailable in this host. The coordinator's small runtime shim reroutes
only that locator to `/proc/self/exe`, leaving kernel/proof logic unchanged.
Exact Lean version: **4.14.0**, commit `410fab728470` as reported by the runtime.
The final positive theorem prints standard axioms only; the countdown
nonrealization theorem prints `[propext, Quot.sound]`. No admitted assertions or
custom axioms are introduced. Independent CI without this host shim remains a
distinct verification route.

The required full suite actually passed **1616 tests**; source provenance
passed all **72 items**; both required foundation/ordinal probes exited zero.
Those outcomes are recorded in the companion assignment receipt. GitHub CI at this new head
has not been asserted by the cluster worker; publication is the coordinator's
responsibility. The artifact hashes identify source content rather than circularly
embedding the SHA of the commit that contains the receipt.

## 21. Primary literature retrieved in this run

- [Stacks Project, Yoneda lemma, tag 001P](https://stacks.math.columbia.edu/tag/001P):
  full representables and actual natural transformations. C13.1 is derived above
  directly by retract naturality; no restricted-density priority is claimed.
- [Stacks Project, sheaves, tag 006S](https://stacks.math.columbia.edu/tag/006S):
  literal matching-family gluing and its uniqueness requirement.
- [Stacks Project, quasi-compact spaces, tag 0059](https://stacks.math.columbia.edu/tag/0059),
  Lemma 5.12.6, and [limits of spaces, tag 08ZS](https://stacks.math.columbia.edu/tag/08ZS),
  Theorem 5.14.4: finite-intersection and product-compactness ingredients.
- Allen Hatcher, *Algebraic Topology*, §1.3, Propositions 1.32, 1.33, 1.39,
  retrieved as [the author's textbook on a university course mirror](https://math.uchicago.edu/~farb/algtop2023/Hatcher.pdf):
  subgroup indices, lifts, and regular/deck-cover classification. Official
  Cornell PDF endpoints timed out in this tool; the mirror contains Hatcher's
  actual textbook, not a third-party reinterpretation. No textbook file is
  redistributed in this repository.
- John C. Baez and Kenny Courser, [Structured Cospans](https://arxiv.org/abs/1911.04630),
  *Theory and Applications of Categories* 35 (2020), 1771–1822: prior art for
  open-network/cospan structure. C17's exact finite relation implementation
  verifies only the explicitly stated behavior laws.

Literature retrieval, source proof, kernel checks, and finite tests remain
different provenance families. This report does not compress them into a truth
probability or mistake shared-model agreement for independent referee evidence.
