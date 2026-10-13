# EODCS II: causal observation descent, finite Nerode horizons, autonomous probe-program genesis

**Research date:** 2026-10-13 (New York). **Base:** EODCS I draft PR #44 at commit 091b9e6ecb0f4bb1a162db2e97ef0f8d9a00f6ed. **Draft research branch:** research/eodcs-causal-nerode-moonshot-2026-10-13, PR #46. **No main merge, history rewrite, physical instrument, new license or release.**

**Steelman of the maintainer's moonshot:** E should not merely pick another fitting model. It should use an exact failure of previously legal model-composition/proof transport to *generate an observational language capable of expressing the missing distinctions*. Two environments may have separately correct models, yet their interaction generates a causal cross-model obstruction. Candidate synthesis must retain the original source, use permitted operations, and surrender when the closed toolkit cannot distinguish the remaining alternatives.

**Scope:** complete, finite, explicitly declared source tables; deterministically evolving carrier states and source-conditioned reports; finitely generated action words; exact rational weights when search cost is declared; finite graph-model prior results. These are mathematical simulators, not authenticated experimental data. General automata/Myhill–Nerode, kernel congruence, universal pair refinements and active-test set cover are CLASSICAL mathematical ingredients. The particular EODCS program integration is project work; independent scholarly originality is UNVERIFIED.

## CS1. The source-changing observational-square theorem (CLASSICAL / LEAN-KERNEL)

Let S and T be source state sets, U:S→T a specified causal update, q:S→O an observation whose image is all of O, and r:T→P a post-update observation. The desired observable update V:O→P must make a naturality square commute:

r(U(s))=V(q(s)) for every s∈S.

**Necessary and sufficient criterion, including quantifiers:**

There exists such a V iff

∀s,t∈S, q(s)=q(t) ⇒ r(U(s))=r(U(t)).

Necessity: apply V to equal original reports. Sufficiency: for each observed o∈O, choose s_o with q(s_o)=o and define V(o)=r(U(s_o)); the fiber implication proves choice independence. Uniqueness holds because q is surjective onto the chosen output support. **Important:** without surjectivity, extensions of V outside the actually observed image are arbitrary and uniqueness is false. The exact hypotheses are preserved in the standalone Lean proof and in Python source-image semantics.

**Original-source falsifier:** S={00,01,10,11}, q(s)=first bit, U exchanges bits. Then q(00)=q(01)=0, but q(U(00))=0 and q(U(01))=1. Therefore NO V exists at one step. This is a decisive mathematical counterexample to an unlicensed update of an internal observer's prior scalar model.

A source label, epoch, and basis are validated before attempting any transport. A false physical authentication assertion is rejected; the abstract existence of a commuting square is not experimental confirmation of a causal instrument.

## CS2. Universal least-information *mathematical* repair (CLASSICAL / LEAN-KERNEL)

Given the same q and target report F=r∘U, set

q*(s)=(q(s),F(s)).

Its fibers satisfy

q*(s)=q*(t) iff [q(s)=q(t) and F(s)=F(t)].

It is the **coarsest partition refining q's partition on which F is constant**. If any alternative observation a:S→A allows decoders d0:A→O and d1:A→P with d0(a(s))=q(s), d1(a(s))=F(s), then the unique coordinate-pair expression (d0,d1):A→O×P factors q* through a. There is no stronger statement that the new q* is an **available physical source instrument** or that it leaves its source unchanged.

**Exact extra fixed-width bits, conditional channel statement.** For a particular known q report o, let k_o be the number of distinct future reports attained among its preimage q⁻¹(o). If the observer already knows o, an additional fixed-width binary message can disambiguate the successor report iff it has at least

b_min = ceil(log2 max_o k_o)

bits (define ceil(log2 1)=0). The lower bound is pigeonhole within the largest fiber; achievability codes each possible future separately within that fiber and reuses the same codewords under different known o values. The code explicitly verifies its global bit width. This assumes a **hypothetical source-faithful supplemental channel**; it does not license creation of an instrument and does not conflate entropy with fixed-width worst-case coding.

**Hostile controls:** all 1,728 three-state/binary-report original and post source tables are compared with a separate exhaustive V-function existence oracle; four-state repairs are compared with all partitions; 130 seeded four-state instances are compared against brute-force shorter-alphabet encodings. One observed failed CI instance exposed a genuine implementation flaw: local-fiber codewords had differing widths although the claim was global fixed-width. The repair zero-pads to the maximal width; the mutant and regression remain in history.

## CS3. A useful composition paradox (CLASSICAL / EXACT COUNTERMODEL)

Two successive updates can each fail observational descent while their composite descends. Let U be the involution exchanging the two bits. With q reporting only the first bit, the individual q∘U cannot factor through q. But U²=id, so q∘U²=q does descend.

This is **not** retrospective proof that the earlier step was safe. Its prior obstruction pair remains valid at the intermediate time. General composition of two actually commuting causal squares is sound and separately Lean checked: if r∘U=V∘q and p∘W=Z∘r, then p∘W∘U=Z∘V∘q. The converse, that a composite commuting square forces its components to commute, is REFUTED by the bit-swap example.

**Original-claim firewall:** a commuting observation square alone does not certify a source predicate. A Boolean original-source claim must itself be reportable on licensed fibers and satisfy claim_before(s)=claim_after(U(s)) for every source state. An identity observation square with an intentionally flipped after-claim refutes unconditional proof transport. The implemented original-claim audit is a sufficient gate, not a general proof system.

## CS4. Stationary finite observer completion: relative Nerode stabilization (CLASSICAL / EXACT)

Fix a complete stationary finite source S of cardinal n, a total deterministic U:S→S, and an observation q:S→O. Define the finite observation word W_h(s)=(q(s),q(U(s)),...,q(U^h(s))). Let P_h be the partition by equal W_h.

1. P_(h+1) is always a refinement of P_h.
2. If P_h=P_(h+1), it is an action congruence: s≈_h t implies U(s)≈_h U(t), because agreement through h+1 after the same q word contains all length-h suffix information. By induction every future W_k partition coincides with P_h for k≥h.
3. Each strict refinement increases the number of partition blocks by ≥1. If the original report has b_0 nonempty output classes, the first stable horizon is at most n−b_0. For all n≥2, b_0≥1, hence at most n−1. This is a **source-relative** finite theorem, not a statement about unknown/infinite physical world completion.
4. Equality under the stable partition is precisely equality of all future q∘U^t reports, yielding a quotient transition map well-defined on classes. A different complete observable law may still share this quotient and have a distinct hidden ontology.

**Sharp adversarial long debt:** the n-state delayed-signal chain U(i)=min(i+1,n−1), q(i)=1 iff i=n−1, otherwise q(i)=0. At horizons h=0,...,n−2 its class counts are 2,3,...,n. Thus its first stable horizon is h=n−2, and each of the n−1 candidate time-offset probes q∘U^t for t=0,...,n−2 is required to distinguish all n source states in a nonadaptive individually re-prepared source-probe basis. The bounded cost model price(t)=t+1 yields exact minimum sum_{t=0}^{n−2}(t+1)=n(n−1)/2. Over the family of finite n, the necessary horizon is unbounded; no claim of a single infinite source exhausting time or unbounded-physical Zeno execution follows.

**Independent oracle:** 180 independently seeded complete multi-state source tables are compared against separately simulated future raw trajectories up to 4n+17, not just the same dynamic-programming partition routine; the first differing clock, final aliases and quotient successors must match. A perceived plateau under **partial/unverified** source rules is not the complete-table theorem.

## CS5. Automatic typed probe syntax + a genuine search-counterexample (BOUNDED ALGORITHM)

A source-typed grammar begins with the report q and legal composition by the source action U, producing strings q∘U^t. For the stable finite quotient, a set of offsets is sufficient iff every pair that *can* be distinguished eventually differs on at least one chosen offset.

E's heuristic chooses offsets by exact rational newly split pair mass divided by a declared cost(t)=1+λt. A separate exhaustive hitting-set enumerator checks **all subsets** of the complete finite grammar within a declared horizon. Its optimum is proved only inside this finite cost model; there is no physical reset budget or instrument attestation.

**Hard negative control:** a seven-state deterministic source with U indices (5,6,0,6,2,4,3) and reports (2,2,0,2,1,2,0) has stabilized horizon h=2. Heuristic selection chooses t=(0,1,2), cost 6; exhaustive optimum chooses (0,2), cost 4. This falsifies any claim that greedy fitness is proof of globally minimum instrument cost and remains a permanent regression. The exact proof of optimality is exhaustive finite search, not stochastic success.

## CS6. Two-action observation can create an expressible relation neither one-step action reveals

For a complete finite source with two available actions A,B, start at states x,y with q(x)=q(y)=0. Choose source transitions where q(Ax)=q(Ay)=q(Bx)=q(By)=0, but q(B(Ax))=0 and q(B(Ay))=1. Each single-action observation fails to distinguish x from y. The automatically enumerated minimum distinguishing action word is (A,B), whose output difference is a **new composite report expression** absent from the seed probe vocabulary.

The deterministic multi-action quotient is constructed by repeatedly refining present output classes using the destination classes under every available action. When a partition is stable, it is an output-preserving action congruence. The direct product-state BFS independently constructs shortest discriminating words, or certifies there is no such finite word for that state pair.

**Proof of toolkit-relative darkness (LEAN-KERNEL).** Suppose E(s,t) is any relation satisfying:
(a) E(s,t) ⇒ q(s)=q(t);
(b) E(s,t) ⇒ E(U_a(s),U_a(t)) for every available primitive action a.
By induction on any finite word w in the action alphabet, E(s,t) implies q(U_w(s))=q(U_w(t)). Thus no mutation, repetition or composition of these actions separates the pair. This is a theorem **relative to the stated closure of available actions**, not an assertion of fundamental logical or physical undecidability.

**Darkness control:** a four-state source has two different states a,b with identical reports. Both available actions preserve the reporting equivalence; no finite word can split them, independently confirmed by complete finite state-pair reachability. An *unavailable* additional probe p with p(a)≠p(b) would split the class; E cannot claim to have materialized it.

## CS7. Causal commutator tomography and delayed versus dark curvature (SOURCE-CONDITIONAL)

For two authorized primitive actions A and B, compare the two source endpoints U_B(U_A(s)) and U_A(U_B(s)). If unequal, the source update paths do not commute at s. If their current reports differ, the *observed* two-step square is noncommuting. An observationally noncommuting square implies source noncommutation, but not conversely: a coarse q can erase differences between noncommuting hidden endpoints. This logical implication is Lean checked in EODCS_ActionClosure.lean. The term "curvature" here names a precise two-path categorical defect, **not a physical gauge curvature**.

An independent minimum pair-word oracle classifies source-model noncommutations by how they appear to the observer:
- **Immediate:** q distinguishes the endpoints with no further actions.
- **Delayed:** some shortest legal word w separates their reports later.
- **Dark:** no word in the present action closure separates endpoints.

**Nontrivial probe mutation:** In the six-state A/B source, state y has immediately observable noncommutation, while state x has a source-level noncommutation permanently invisible to the original A/B instruments. Add a new *declared* action C satisfying C(u)=d and C(c)=c, with q(c)=0,q(d)=1: x becomes delayed-visible after C. The model records this as source-relative rotation of the observation basis, NOT a physical intervention being obtained. A separate 110-source independent word enumerator validates all three categories on seeded 2–5-state action systems.

## CS8. Genetic programming actually generates a probe word (BOUNDED / HEURISTIC)

The typed genetic genome is a finite tuple of available action names (initial grammar length 0 and 1). Mutation adds/deletes/replaces/swaps actions, crossover recombines prefixes/suffixes; the decoder checks every action against the source menu and checks the full causal report only after proposal. The score is an exact rational combination of source-matched separation, global report diversity and code length. **Fitness cannot prove mathematical truth.**

Under the restricted one-generation test the genetic population cannot create the valid two-action word (A,B); it records genetic failure, while an independent exhaustive shortest pair-state search identifies (A,B). Under a sufficiently large population/generation budget, successful genes are independently checked against actual declared outputs. Seeds retain true misses and the exact verifier is reported separately. The original action-congruence-dark pair yields NO exact valid word: the evolutionary algorithm cannot legally invent an unavailable physical probe to rescue it.

This is a real executable generation of *new action-word syntax from old constructors*, more capable than a fixed list of predeclared probes. It is **not** spontaneous invention of arbitrary new functors, categories, physics, measurement devices, or scholarly mathematical theorems.

## CS9. Formal Lean instrument status and proof boundaries

New proof modules:
- formal/EODCS_CausalDescent.lean: fiber criterion necessary/sufficient and unique with declared surjectivity, pair-refinement factorization, actual causal square composition, based holonomy fixedpoint ↔ tree-parallelness, abstract deck invariance ↔ root fixedpoints.
- formal/EODCS_ActionClosure.lean: action congruence implies equality under ALL finite legal action words, observable commutator implies genuine source noncommutation, and injective reports expose source inequality.
- formal/EODCS_OrderAdjunction.lean: retained from parent, composition, adjunction unit/counit, uniqueness and order quotient universal factorization.

The pinned Lean 4.14.0 workflow compiles all formal/EODCS_*.lean, and explicitly forbids sorry/admit/axiom/unsafe after the module namespace. **These exact statements** are machine verified when CI is green; the finite Nerode stabilization/cover-minimality/source-cost bounds remain paper proofs + executable finite oracles, NOT Lean theorems. A classical choice of source preimage in the quotient theorem is stated explicitly, not hidden as computational source access.

Mandatory reproducibility:
- python scripts/verify_provenance.py
- python -m unittest discover -s tests -p 'test_eodcs_*.py' -v
- python scripts/eodcs_causal_probe.py
- python -m unittest discover -s tests -p 'test_*.py'
- python scripts/observer_foundations_probe.py
- python scripts/ordinal_succ_report_probe.py
- pinned Lean CI kernel suite; verify exact pushed SHA and claim only completed jobs.

## CS10. The open moonshot and next falsifiers

1. **Multi-action full source-changing fibration.** Current result is deterministic typed q/U with stationary finite or one declared intervention; asynchronous/noisy state changes require conditional distributions, actual history-dependent backaction, and explicit functorial source transitions. A diagrammatic shape is not enough.
2. **Unbounded grammar birth.** The search creates finite action-word expressions and post-observation pairs under programmer-supplied constructors. It does not discover new sensors or categories outside its closure; a crucial hostile task is to furnish an instrument that genuinely changes its closure and verify first-source provenance.
3. **Resource-faithful information budget.** Costs are declared models, not measured energy, reset counts or causal accessibility. The full finite simulator queries hypothetical counterfactual source states; a single nonresettable physical specimen might prohibit them. Encode availability and adaptive policy in a future version.
4. **Independent formalizer.** Lean formalizes finite source transport and tool-relative darkness, not the full Nerode partition bound or cover minimality. Formalize these with actual finite cardinalities and nonabelian group-action covering maps.
5. **Independent scientific novelty.** Before claiming new mathematics or experimental physics, compare primary scholarly literature on automata minimization, partition refinement, counterexample-guided program synthesis, behavioral equivalence, universal property of quotients, and covering theory. An internal tool's exact examples are not independent academic novelty.
6. **RH / Weil** stays explicitly downstream; no authentic prime-power/Arch Gamma/Weil form identification, no global positivity proof, no zero-reading construction, and no RH claim.

**Verdict:** The bounded engine turns concrete source-changing failures into new *finite observational expressions* with exact certification and no-go results. Its high-value claim is compositional and epistemic architecture, not generalized automatic theorem invention. Keep κ (contact), φ (within-tool distinguishability), σ (source adequacy), μ (probe availability), plus coherence and independence distinct; none is a truth probability.


## CS11. A stronger Lean theorem: finite complete plateau iff ALL future observational equivalence

The initially verified forward theorem is now strengthened in \`formal/EODCS_NerodePlateau.lean\` to an exact biconditional under explicit stationary-source assumptions. For any source set S (not assumed finite in the theorem itself), deterministic U:S→S, q:S→O, and a fixed finite horizon h, define
\[
  s\equiv_h t \iff \forall i\le h,\;q(U^i(s))=q(U^i(t)).
\]
Assume the **global plateau condition**
\[
  \forall s,t\in S,\quad s\equiv_h t\Longrightarrow s\equiv_{h+1}t.
\]
Then, for *each* source pair s,t,
\[
  \boxed{s\equiv_h t\quad\Longleftrightarrow\quad
    \forall n\in\mathbb N,\;q(U^n(s))=q(U^n(t)).}
\]
**Proof:** the plateau implies that h-equivalence is U-stable, since the length-(h+1) successor words already contain all length-h shifted reports. Induction on n yields h-equivalence after n source updates; taking the zeroth observation gives equality for every n. The reverse implication is immediate by restriction to i≤h. This is a proof about a universally quantified *declared* stationary mathematical source, not a physically infinite experiment. The theorem's core induction and biconditional were kernel-checked using pinned Lean 4.14.0 at GitHub Actions [run 38350713441](https://github.com/femboy2112/SUCC/actions/runs/38350713441), commit \`72148563f240fb6f15dc35aff2d3c107df1cafcf\`.

**Important separation:** the Lean theorem takes the **global plateau** as a hypothesis; the existence of some sufficiently early plateau for every *finite* S is a separate block-count argument CS4, which remains non-kernel-formalized. A partial/noisy apparent plateau is not a global antecedent. The source action must remain stationary; arbitrary event-dependent source backaction can invalidate the time-shift step. This distinguishes a rigorous finite logical certificate from physical execution of ω steps.

## CS12. Partial source windows and dangerous false global transport

New \`PartialSourceAudit\` takes only the explicitly exposed source addresses and their paired receipts. A sample can consistently support a mathematical observation successor while the full source does not. For the exact bit-swap source CS1, the incomplete sample of states (00,10) contains no conflicting original report fiber and therefore appears compatible; however the omitted state 01 has the same initial report as 00 and a different post-update report. Opening that omitted state gives a finite, decisive falsifier. The engine records \`sample_consistent=True\`, \`globally_certified_from_sample=False\` and a proposed (not executed) next source address, rather than inventing a total map V.

Only when all addresses of the **declared finite complete source class** are observed, and no fiber obstruction remains, is the source-relative claim certified. This is NOT empirical authentication: a declared simulator could still omit physically existing states. Hostile mutants include repeated addresses, forged unseen states, wrong input types, changed epochs and false original-claim preservation. Remaining task: partial probabilistic source laws with simultaneous source-changing interventions, nonstationary history and empirical probe access.

## CS13. Exact reproducibility receipt and honest genetic failure

The reproducible receipt \`research/2026-10-13/EODCS_CAUSAL_PROBE_RECEIPT.json\` was derived from real GitHub workflow logs on both Python 3.10 and 3.13, which produced identical complete JSON objects (CI run 38350367922). A fixed exact seed schedule (0 through 19) recovers a valid genetic separating action word on **6** seeds and misses on **14**; every success is source-verified and every miss remains a genetic miss even when the separate complete pair-BFS oracle recovers the valid shortest word. One constrained one-generation test fails by construction and supplies an explicit budget-negative control. A truly action-congruence-dark source has no separation witness in the finite grammar, with no forged sensor. The bound is not a population-wide statistical success estimate, because these source tasks and heuristic rules are declared rather than independent empirical data.

Two separate Python versions now replay the frozen receipt byte-for-byte in \`.github/workflows/eodcs-tests.yml\`; an additional test compares parsed saved JSON against freshly generated source output. Tests and full CI must still be checked at the **final** branch head before counting them as passing. No open-world proof completeness, academic novelty or RH inference follows.
