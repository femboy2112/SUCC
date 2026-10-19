# The SUCC meta: generative choice, categorical construction, and source-certified global truth

**Date:** 2026-10-19  
**Status:** foundational research synthesis + exact finite theorem + formal strengthening. This is not a claim of an independently new topos theory, a physical theory, or a resolution of RH.  
**Research parent:** `main` at `4de865766d53ea448555386d98f3e88e3ec605b6`; non-main research branch `research/eodcs-choice-descent-meta-2026-10-19`.  
**Named hypothesis:** **Category-shaped set construction, set-theoretic rigor over categorical objects, and source-certified descent.**

## Abstract

SUCC asks how a finite, source-bound observer can construct mathematical objects, compare their representations, and justify assertions about the resulting global carrier. The proposed organizing principle is **not** to replace set theory with category theory. It is to use categorical construction and transport to assemble candidate worlds, set-theoretic/dependent-type-level quantification to check their laws, and source-indexed descent to distinguish local witness availability from global realization and proof.

Four logically different gates must not be collapsed:

1. **Local construction:** a source and a declared toolkit generate an admissible witness at a context.
2. **Compatibility/descent:** the witnesses respect restriction, quotient, overlap, transport, and holonomy.
3. **Source realization:** a descended mathematical section is actually realized by one original source under admissible maps.
4. **Proof authority:** a checked derivation establishes the *specified* global proposition within a stated logical foundation.

These gates yield the proposed meta-slogan:

> Construct categorically; verify relationally; certify globally, but only through lawful source interfaces.

In general, neither unrestricted classical AC nor excluded middle is declared an unexamined computational entitlement. A **witnessed, dependent-type form of choice** is immediate; the set-theoretic choice of representatives from arbitrarily inhabited fibers is not. Moreover, full internal choice in an elementary topos entails Boolean internal logic (Diaconescu). The difference is structural, not a contradiction to hand-wave away.

## 0. Relationship to the actual project

This manuscript extends, rather than overwrites:

- `docs/FOUNDATIONS.md`: physical record / semantic model / mathematical proof / global report are distinct.
- `docs/OBSERVER_PROOF_ACCESS.md`: `FieldClass(Source, Target, Tools)`, with Simple / IdealHard / Fucked / Unresolved classifications.
- `formal/EODCS_RelationalChoice.lean`: nondeterministic support, observation fibers, MayReport, CommonPossible.
- `formal/EODCS_CausalDescent.lean`: deterministic quotient descent and rooted holonomy fixed-point criterion.
- `docs/CLAIM_SUPPLEMENT_NO_GHOST.md`: source-supported compatibility, chosen comparison maps, formal gluing versus actual source realization; especially NG-Q0 and NG-INF.
- `formal/EODCS_CarrierIndexed.lean`: source identity does not change merely because the current carrier representation changes.
- `docs/ARCHITECTURE.md`: source-preserving typed arrows and the independent RH positivity firewall.

This round contributes an **unconditional choice-free strengthening of one relational descent statement**, a finite graph-cohomology oracle with falsifiable certificates, and a testable metatheory program. It does **not** supply a generic Grothendieck site compiler or new theorem of topos theory.

## 1. Recovering the intuition without inflating it

The analogy of a geometric warp drive is useful only as an architectural metaphor: the objective is not to violate a fixed law, but to seek a new lawful representation or path that carries the desired invariant without an unauthorized shortcut. Categories supply lawful compositional routes (limits, colimits, group completion, localization, gluing, quotients, duality); set-theoretic and type-theoretic disciplines enforce domains, quantifiers, concrete witnesses, and proof obligations on what those routes actually establish.

The proposal makes three claims, at different status levels:

- **Classical mathematical fact:** local sections can exist with no coherent global section; obstructions are described by overlap conditions, holonomy, and in favorable cases cohomology.
- **New-to-SUCC implementation target:** every construction, restriction, and descent map is recorded with source, basis, access, and evidence provenance; successful global comparison has an explicit replayable certificate.
- **Open research hypothesis:** this integration yields mathematically useful new preservation/failure theorems or genuinely new arithmetic results rather than simply repackaging known sheaf and obstruction theory.

A failed diagram is not evidence that mathematics or physics is inconsistent. It is evidence that **at least one specified hypothesis, identification, or expected conclusion fails**. The correct response is to isolate the weakest premise and build a discriminating test.

## 2. Choice and excluded middle: the exact logical budget

### 2.1 Witnessed choice is immediate, global choice is not

In dependent type theory, the following map is definable by projections:

\[
\left(\prod_{x:X}\sum_{y:Y(x)}R(x,y)\right)
\longrightarrow
\left(\sum_{f:\prod_xY(x)}\prod_x R(x,f(x))\right).
\]

Given `h x : Σ y, R x y`, define `f x := (h x).1`, and obtain the proof `(h x).2`. **No selection oracle is needed**: the witnesses have already been provided as data. This is the *generative/witnessed* choice principle intended here.

In contrast, from a merely propositional assertion `∀ x, ∃ y, R x y` one cannot, in general, extract an executable selector in a constructive logic when existential witnesses are not data. Similarly, in an elementary topos the statement **every epimorphism splits** is a strong internal categorical choice principle, not the above lambda-calculus projection.

**Boundary:** a relation-valued witness `V : O → P → Prop` is different from a total deterministic `f : O → P`; existential direct images may define the first without choosing an element for the second.

### 2.2 The Diaconescu firewall

Classical result: in an elementary topos, if **every epimorphism splits**, the internal logic is Boolean (excluded middle holds). Thus:

\[
\text{internal full choice}\implies\text{internal LEM}.
\]

Therefore do not simultaneously assert unrestricted internal AC as a standing axiom and treat unrestricted LEM as an unsettled independent obligation in that same internal logic. The defensible SUCC reading is:

- freely build witnesses **when the source and toolkit furnish them**;
- leave arbitrary global selectors and internal Booleanity as explicit, separately typed assumptions or theorems;
- preserve the distinction between an external classical metatheory and an internal intuitionistic logic.

**Primary reference:** R. Diaconescu, *Axiom of choice and complementation*, Proc. Amer. Math. Soc. **51** (1975), 176–178, DOI [10.1090/S0002-9939-1975-0373893-X](https://doi.org/10.1090/S0002-9939-1975-0373893-X). Also see the [Lean tutorial treatment of choice and excluded middle](https://github.com/leanprover/tutorial/blob/master/12_Axioms.org).

### 2.3 LEM as internal geometry, not a quantum analogy

Take the Heyting algebra of opens of the usual real line, where negation is interior of the complement. For `U=(0,∞)`,

\[
\neg U=(-\infty,0),\quad U\vee\neg U=\mathbb R\setminus\{0\}\neq\mathbb R.
\]

This exhibits an internal proposition that is not decidable *globally* in the sheaf logic. It does not disprove classical excluded middle in the external metatheory. It does not involve a physical quantum system.

**Source:** [nLab, internal logic](https://ncatlab.org/nlab/show/internal%2Blogic), and the general sheaf semantics described in standard topos texts.

**Operational budget proposal** for each new SUCC claim:

| Question | Required authority |
|---|---|
| May I construct a successor? | source-typed inhabited witness or verified algorithm |
| May I choose one from *each* fiber? | witnessed function, explicit chooser, or declared choice axiom |
| May I decide a proposition? | decidability witness, classical assumption, or checked proof |
| May I glue local data? | an actual cover contract and overlap/cocycle compatibility |
| Does the result come from my original source? | a realization map and source-adequacy certificate |
| May I report a global theorem? | proof object in an explicitly specified theory |

## 3. The first exact improvement: relational transport without choosing representatives

Let `S` be source states, `O` present reports, `T` successor states, and `P` successor reports. Let

\[
q:S\to O,\qquad N:S\times T\to\mathrm{Prop},\qquad r:T\to P.
\]

Define the relational future support:

\[
F(s,p)\;:\iff\;\exists t:T,\;N(s,t)\wedge r(t)=p.
\]

Define observation-fiber compatibility:

\[
\operatorname{Inv}(q,F)\;:\iff\;
\forall s,t,p,\;q(s)=q(t)\Rightarrow(F(s,p)\leftrightarrow F(t,p)).
\]

**Proposition MC-1 (choice-free relational descent; elementary).** For *any* `q`, including nonsurjective `q`, the following are equivalent:

\[
\operatorname{Inv}(q,F)
\quad\Longleftrightarrow\quad
\exists V:O\times P\to\mathrm{Prop},\;
\forall s,p,\;V(q(s),p)\leftrightarrow F(s,p).
\]

No law of excluded middle, choice of representatives, or surjectivity is required for this **relation-valued** statement.

**Proof.** If `V` exists, equal `q` reports yield identical `V` values, hence invariant `F`. Conversely define the existential pushforward:

\[
V(o,p):=\exists s:S,\;q(s)=o\wedge F(s,p).
\]

Then `F(s,p)⇒V(q(s),p)` with witness `s`. If `V(q(s),p)`, choose the **already furnished existential proof witness** `t` in the proof, with `q(t)=q(s)` and `F(t,p)`; compatibility gives `F(s,p)`. No globally computed `pick:O→S` has been constructed. □

**Lean location:** the new `support_transition_exists_choice_free` and `support_transport_iff_fiber_invariance_choice_free` declarations in `formal/MetaChoiceRelationalDescent.lean`, imported from the byte-frozen `formal/EODCS_RelationalChoice.lean` via the dedicated pinned compilation workflow. The original EODCS III source is unchanged.

Existing `support_transition_exists_of_fiber_invariance` is preserved for backwards compatibility, although its `surj` and `Classical.choose` inputs were unnecessary to get this weaker *relation-valued* objective.

### 3.1 Why the image boundary matters

SUCC already has

\[
\begin{aligned}
\mathrm{May}(o,p)&:=\exists s,\;q(s)=o\land F(s,p),\\
\mathrm{Common}(o,p)&:=\forall s,\;q(s)=o\Rightarrow F(s,p).
\end{aligned}
\]

If `o∈im(q)` and support is fiber-invariant, the relations agree. But at `o∉im(q)`:

\[
\mathrm{May}(o,p)=\bot,\qquad\mathrm{Common}(o,p)=\top
\]

for *every* `p` (including if no successor of any actual source state exists). Thus global equality of the two over all `O` needs a surjectivity/inhabited-fiber condition.

The new `exact_envelopes_on_image_choice_free` proves equality on the image. `empty_observation_fiber_separates_envelopes` gives an exact negative boundary. This is a clean, nonpsychological example of SUCC's prohibition on promoting image-relative observation into global model truth.

### 3.2 Source and constructive boundaries

- A `Prop`-valued existential pushforward is not a computational selector.
- The above proof uses existential elimination to prove a proposition, not to extract arbitrary data across fibers.
- Two source states may share a report but have different *probabilities* while having the same support; neither `V` nor equality of supports transports their stochastic kernels. Retain existing EODCS III mutant controls.
- An abstract `q`, `N`, and `r` do not attest that an actual observer can perform `N`; source access remains a separate gate.

### 3.3 A categorical universal property obtained without categorical overreach

For `q:S→O`, define the existential direct image `(∃_q F)(o,p) := ∃s, q(s)=o ∧ F(s,p)`. For any report predicate `G:O×P→Prop`, order predicates by pointwise implication. Then:

\[
\boxed{\quad (\exists_q F\leq G)\ \Longleftrightarrow\ (F\leq q^*G)\quad}
\]

where `(q*G)(s,p)=G(q(s),p)`. **Proof:** forward, apply the left inequality to the witness `s` at report `q(s)`; backward, destruct the explicit witness of `∃_q F(o,p)`, and apply the right inequality. This is the classical adjunction `∃_q ⊣ q^*` between predicate preorders, proved constructively. It is an exact realization of **category-shaped set reasoning**: the map's universal property packages all source witnesses without choosing a representative.

The new Lean declaration `may_report_left_adjunction` formalizes this property using the repository's exact `FutureSupport`/`MayReport` types. The standalone `EODCS_MetaChoiceParity.lean` additionally proves the direct-image **identity and composition** laws, again without classical choice:

\[
\exists_{\mathrm{id}}F\equiv F,\qquad
\exists_h(\exists_qF)\equiv\exists_{h\circ q}F.
\]

These equivalences concern proposition-valued relations and do not supply computational witness selection. Their novelty is an explicit, source-aware SUCC use and Lean encoding, not the underlying adjunction.

## 4. Exact finite obstruction: an odd-loop cannot descend

Let `G=(V,E)` be a finite undirected multigraph viewed as a one-dimensional CW complex, and let every edge `e=(u,v)` carry a parity `t_e∈F_2`. An assignment of local states `x_v∈F_2` is a global section of this transport problem if

\[
x_v-x_u=t_e\quad(\mathrm{mod}\ 2)
\]

on **every** edge. With `C^0(G;F_2)` the vertex functions and `C^1(G;F_2)` the edge functions, define `(\delta x)(e)=x_v-x_u`. As the graph has no 2-cells, `H^1(G;F_2)=C^1/\operatorname{im}\delta`.

**Proposition MC-2 (graph transport descent; classical elementary).**

\[
\exists x:\delta x=t
\quad\Longleftrightarrow\quad
[t]=0\in H^1(G;F_2)
\quad\Longleftrightarrow\quad
\bigoplus_{e\in\gamma}t_e=0
\text{ for every closed walk }\gamma.
\]

If the conditions hold and the graph has `c` connected components, there are exactly `2^c` global sections. If a closed walk has odd transport, it is a finite negative certificate of global compatibility.

**Proof.** A global assignment telescopes around each closed walk. Conversely fix a root in each connected component; assign root value 0 and propagate `x` along a spanning tree. Any non-tree edge closes a fundamental walk. When all walk transports vanish, every edge law holds. Choosing each root bit independently gives `2^c` sections. An odd walk cannot telescope to zero, proving obstruction. □

For a three-vertex triangle with three flips, each ordinary edge is locally satisfiable, yet

\[
x_B=x_A+1,\quad x_C=x_B+1,\quad x_A=x_C+1
\]

forces `0=1` in `F_2`. This **refutes** the false meta-principle `every local edge has a witness ⇒ global section exists`. With two flips and a zero edge, the triangle has exactly two global sections.

**Finite implementation:** `observational_succ/meta_choice_descent.py` supplies:

- a declared original `source_id` and `basis_id`, rejected when edge contracts disagree;
- spanning-forest potential reconstruction without enumerating all assignments;
- a replayable `LoopObstruction` listing the vertices and original edge IDs of a closed walk;
- a separate exact `verify_loop` checker and `brute_force_sections` oracle for small graphs;
- a guard against confusing `F_2`-symmetric transport with arbitrary nonabelian/oriented transport;
- explicit `physical_source_authenticated=False` and `RH_proved=False` results.

**Hostile test domain:** all `3^6=729` simple undirected edge-labeled graphs on four named vertices (edge absent, parity 0, or parity 1), each compared against all `2^4=16` vertex assignments. Triangle parity masks, parallel-edge contradictions, self-loops, disconnected graphs, proof-witness mutations, and source/basis mismatch are extra controls. These are exhaustive **within that finite grammar**, not for all graphs.

Command: `python -m unittest tests.test_eodcs_meta_choice_descent -v` (or `python -m unittest discover -s tests -p 'test_eodcs_meta_choice_descent.py'`), `python scripts/meta_choice_descent_probe.py`.

### 4.0a Independent combinatorial count of the four-vertex grammar

The `729=3^6` graph contracts have `393` flat transport assignments and `336` obstructed ones. This count can be derived without consulting either the spanning-forest solver or the vertex-assignment oracle. For a fixed subgraph `H⊆K_4` with `c(H)` connected components, the coboundary map `F_2^4→F_2^{E(H)}` has kernel of size `2^{c(H)}`, so its image contains exactly `2^{4-c(H)}` flat edge assignments. Sum over the `64` unlabeled-by-parity edge subsets:

\[
N_{\mathrm{flat}}
=\sum_{H\subseteq K_4}2^{4-c(H)}
=1+12+60+144+120+48+8=\boxed{393}.
\]

The terms are grouped by the number of edges `m=0,1,2,3,4,5,6`; for `m=3`, four triangles plus isolated vertices give `4×4` and sixteen spanning trees give `16×8`. All other edge-count classes have constant component count. The remaining `729-393=336` have an odd closed-walk obstruction. The standalone probe hard-asserts these exact totals; they are independent paper-level acceptance targets, not outputs to be invented if runtime tests fail.

### 4.1 Why a cover does not magically solve the original task

Pulling the odd triangle's parity local system to a suitable double cover can trivialize the lifted holonomy. That does not provide a descended section on the original triangle: deck invariance remains an independent condition. A new carrier can make a hard interface accessible while failing to transport the original target. This is the correct mathematical version of the warp metaphor.

The repository's existing `formal/EODCS_CausalDescent.lean` proves an abstract based-loop fixed-point and cover-invariance characterization; the finite `F_2` implementation is a calibration, not a new universal nonabelian descent theorem.

## 5. Candidate architecture: source-indexed categorical construction

Define a **candidate**, not-yet-implemented, observational context `U` as a tuple:

\[
U=(\text{original source},\text{current carrier},\text{basis},\text{probe domain},
\text{lawful actions},\text{record},\text{proof context}).
\]

A proposed category `C_S` has such contexts as objects and source-compatible, compositionally witnessed access/restriction arrows as morphisms. If a Grothendieck pretopology `J_S` is supplied and checked (identity cover, pullback stability in the required sense, transitivity), then `(C_S,J_S)` is a site. Until those axioms are supplied it is a **proto-site**, not an established topos.

A proposed presheaf of lawful reports/witnesses is

\[
\mathcal F_S:C_S^{op}\to\mathbf{Set}.
\]

A sheaf condition is an explicitly proved equalizer/compatibility property:

\[
\mathcal F(U)\longrightarrow\prod_i\mathcal F(U_i)
\rightrightarrows\prod_{i,j}\mathcal F(U_i\times_U U_j).
\]

Whenever pullbacks or products have not been constructed, replace this display with the actual indexed matching-family definition for the concrete coverage. Do not assert a universal sheaf from suggestive diagrams.

**Distinct semantic questions:**

1. **Mathematical descent:** do compatible local elements glue uniquely in `F`?
2. **Source-adequate descent:** does the glued element have a lawful realizing point of the *original* source carrier?
3. **Effective descent:** does the declared computational toolkit produce a useful finite symbolic interface or witness?
4. **Proof-theoretic authority:** does the global claim have a checked derivation under precisely declared logical rules?
5. **Stability under base change:** are compatibility and source certificates preserved when observers refine probes, bases, or time indices?

Only the first question is the ordinary sheaf axiom. Sheafification of a presheaf can create formal sections that do not lift to global elements of the original presheaf; this must not be silently relabeled 'physical source completed'. Earlier SUCC NG-Q0/NG-N/NG-INF are explicit warnings.

Source reference for the classical sheaf condition: [Stacks Project, Section 6.7 (006S)](https://stacks.math.columbia.edu/tag/006S).

## 6. The SUCC transport certificate

For each requested source-target comparison, require a structured certificate with:

| Field | Meaning | Typical failure |
|---|---|---|
| `source` | immutable original carrier/source law and provenance | synthetic duplicate substituted for original |
| `target` | exact global predicate or object | metric/observable silently changed |
| `context` | accessible probe, basis, action closure, and cost | forbidden counterfactual action |
| `construction` | witness/program/category arrow | no lawful constructor |
| `logical_budget` | constructive fragment; any AC/LEM assumptions | classical choice hidden in quotient |
| `local_laws` | verified equations, support, and domains | same fiber with different support |
| `overlap` | cocycle/holonomy/matching-family certificate | nontrivial loop |
| `realization` | source-side lift or independent source adequacy proof | phantom glue |
| `proof` | kernel/proof checker, arithmetic certificate, or cited theorem | numerical fit promoted to proof |
| `countermodel` | explicit hostile negative control | source mutation falsely passes |

This schema extends `docs/CARRIER_ATLAS.md`, not a replacement for it. A proven abstract isomorphism is not a free physical instrument or a certified arithmetic original-source comparison.

## 7. Steelman → crucible → verdict

| ID | Strong claim to test | Receipt / obstruction | Verdict |
|---|---|---|---|
| MC-0 | “Choice is trivial” = witnessed dependent-type choice | projections construct a choice function from supplied dependent pairs | **CLASSICAL/CONSTRUCTIVE**, with *witnessed* domain only |
| MC-FALSE-AC | Full internal choice may be assumed while LEM need not hold | Diaconescu's theorem in an elementary topos | **REFUTED in that joint interpretation** |
| MC-1 | Support-compatible relation factors over observation quotient without AC or surjectivity | explicit existential pushforward; Lean strengthening added | **PROVED PAPER / LEAN KERNEL VERIFIED on dedicated imported gate** |
| MC-1E | May and common-possible coincide at every report without surjectivity | unreachable report gives `May=⊥`, `Common=⊤` | **REFUTED; repaired on image(q)** |
| MC-2 | Every locally satisfiable edge transport glues globally | odd triangle; verified parity obstruction | **REFUTED** |
| MC-3 | Finite `F_2` graph transport descends iff all closed-walk parity vanishes | spanning-forest proof and exact finite oracle | **CLASSICAL PROVED PAPER; finite tests pending CI** |
| MC-4 | Formal sheafification automatically supplies original-source realizer | existing NG-Q0/NG-INF countermodels | **REFUTED** |
| MC-5 | An accessible source-indexed site and all structural stability axioms exist for general SUCC | not implemented; needs base-change and actual source-map probes | **UNVERIFIED** |
| MC-6 | This categorical/set-theoretic synthesis proves a novel arithmetic statement | no fresh arithmetic proof, holdout or publication-priority audit | **UNVERIFIED** |
| MC-RH | This source/descent architecture proves completed Weil positivity or RH | signed source→Weil morphism and original low-Schur sign remain missing | **NOT ESTABLISHED; RH OPEN** |

No proof-status promotion from a finite test, a user-level analogy, or a shared-model crosscheck is authorized.

## 8. Research campaigns with explicit verdict-changing probes

**A. Relational choice removal (verified base; further probes open).** Preserve the byte-frozen `formal/EODCS_RelationalChoice.lean`, compile it to an importable `.olean`, compile `formal/MetaChoiceRelationalDescent.lean`, and inspect axioms of the new theorems. Verify that the choice-free declarations do not invoke the `Classical.choose` path. Preserve the older theorem and compare normal forms under surjective and nonsurjective observations.

**B. Fiber/counterfactual transport.** Add typed refinements of `MayReport` and `CommonPossible` for reachable-image contexts; independently mutate support versus probability distributions, and verify that support descent does not imply statistical descent.

**C. Obstruction atlas.** Generalize the graph oracle from `F_2` to (i) finite abelian group actions; (ii) nonabelian finite permutation fibers with a rooted holonomy fixed-point theorem; (iii) partial relations where a comparison is undefined. Require orientation bookkeeping, source-permitted actions, and exact witness replay. Existing EODCS cover modules are mandatory baselines, not blank slate.

**D. Site/compiler existence.** Formulate `C_S` as a small category or specify a universe bound, implement composition and identity proofs, and check a pretopology's stability and transitivity. Construct presheaves of legal observations; build an explicit right-to-left matching-family test. Counterexample control: charts that appear pairwise coherent but lack an accessible common comparison chart (existing NG-Q0).

**E. Source realization versus formal glue.** Demand a separate realization relation `Realizes(source, global_section)`; distinguish `∀ finite cover ∃ source` from `∃ source ∀ cover`. Calibrate compact finite sources against noncompact decreasing-naturals towers, profinite ghosts, and observationally aliased sources already in SUCC.

**F. Arithmetic transport stress test.** Take genuine `Z/p^n`, CRT charts, finite Haar/Fourier, and Euler prime jets. Make every isomorphism, basis, conductor, and source change explicit. See which global statements admit finite certificates and which require external completeness; do *not* use arbitrary analytic continuation as a choice selector. Preserve fake-prime/non-Euler and wrong-conductor controls.

**G. RH adversarial firewall.** The completed signed Weil form (Gamma, pole, conductor, half-density, source-derived original primes) remains a separate typed object. A positive covariance or formal local system is not its positivity proof. Any claimed bridge must prove equality on a valid test domain with source provenance and independent hostile controls. No nontrivial zero locations as construction input.

**H. Academic novelty audit.** Compare with canonical constructions in categorical logic, Lawvere–Tierney topology, constructive type theory, étale descent, graph local systems, operational sheaf contextuality, and computable sheaf theory. Isolate the first theorem whose hypotheses or conclusion are materially different; formally prove it, then seek independent holdouts.

## 9. Acceptance criteria

A metatheory milestone is accepted **only if**:

1. At least one source-sensitive preservation/failure theorem is stated with complete quantifiers and a correct proof (not solely an example).
2. Its formalization passes the pinned kernel (if advertised as Lean-certified).
3. Exact finite witnesses/counterexamples replay without solver trust, including hostile mutations.
4. Source authenticity, computability, internal logic, and mathematical global existence have separate report coordinates.
5. Every new arrow has valid naturality/composition/base-change obligations and a stated failure mode.
6. Nothing reclassifies RH as unprovable, solved, or intrinsically inaccessible without an independent proof.

## 10. What this could genuinely change

An important research direction is to compute **minimum repair costs** to make an obstructed local system globally representable while preserving the original carrier laws. For finite graphs, the obstruction class `[t]∈H^1` is a crisp benchmark. A proposed probe or cover repair must expose an actual new distinction, rather than insert a fictitious transport that erases the contradiction.

A valuable next conjectural step is a theorem describing when a source-indexed refinement functor preserves observational identities *and* kills precisely a designated class of descent obstructions. Require a concrete counterexample to falsify it: two originally indistinguishable sources with different global target truth, whose images remain observationally identical under the refinement.

The long-term point is not that global truth becomes optional; it is that **the inferential path from local construction to global truth becomes an explicit mathematical object with checkable structure and cost**.

> Freedom to construct is not freedom to globally certify; an equivalent interface is useful only when the original source can lawfully use it.

## Bibliography and provenance

- R. Diaconescu (1975), *Axiom of choice and complementation*, Proc. AMS 51, 176–178, DOI 10.1090/S0002-9939-1975-0373893-X.
- The Stacks Project, [Sheaves §6.7](https://stacks.math.columbia.edu/tag/006S) and the matching-family/equalizer definitions.
- [nLab: internal logic](https://ncatlab.org/nlab/show/internal%2Blogic) for the opens/Heyting interpretation.
- S. Mac Lane and I. Moerdijk, *Sheaves in Geometry and Logic* (1992), established categorical logical framework (not claimed new here).
- This repository: `formal/EODCS_RelationalChoice.lean` (frozen), `formal/MetaChoiceRelationalDescent.lean` (new imported module), `formal/EODCS_MetaChoiceParity.lean`, `formal/EODCS_CausalDescent.lean`, `formal/EODCS_CarrierIndexed.lean`, `docs/CLAIM_SUPPLEMENT_NO_GHOST.md`, `docs/OBSERVER_PROOF_ACCESS.md` and `research/2026-10-15/SOURCE_FIELD_INVERSE_LIMIT_CALCULUS.md`.

**Attribution boundary:** the philosophy and specific SUCC research priorities originate in the author's program. Diaconescu, sheaf logic, graph cohomology, and the local-to-global descent theorems are classical. The choice-free Lean strengthening and exact finite program are *new to this repository round*, not an assertion of academic priority. Only successful compilation, test receipts, and later independent mathematical review can raise their formal or novelty statuses.
