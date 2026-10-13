# Evolutionary obstruction-driven categorical synthesis

Date: 2026-10-13. Base: genetic fusion PR #43, `1cb30a3d92420f1197fc1615a68fb4309c0e036d`.
Research branch: `research/evolutionary-obstruction-synthesis-2026-10-13`.

## Mission, actual objects, and acceptance criteria

Leah proposed that contextual model intersections should generate new representations, not just rank an existing catalogue. This round implements bounded versions of all six requested directions: richer categorical objects; counterexamples inherited as constraints; source-dependent probabilistic combination; incomplete/noisy/delayed/changing sources; Lean verification; and a held-out source-structure discovery.

The deterministic source is a finite set X, a finite family of total lawful action maps U_a:X→X, and primitive readouts o_j:X→Y_j. An experiment is a typed word w of actions followed by one readout. All laws are declared mathematical simulators; source labels or a correct proof do not attest an actual physical instrument. The new objects are experiment programs, finite quotients with induced action functors, natural comparison maps, predicate adjunctions, transformation monoids, and finite probabilistic amalgamations.

**Architecture distinction.** The representation-repair kernel is deterministic. Its random candidate-mask audits measure how archived witnesses reject unsafe simplifications; they do not choose its next split and are not claimed as genetic improvement. A separate permutation-bridge engine performs actual crossover/mutation constrained by learned counterexamples. Neither engine claims to invent arbitrary categories outside its explicit computable metagrammar.

Acceptance criteria: a complete finite checker either constructs a minimal dynamic representation or returns a typed resource obstruction; every new experiment carries its separating witness; independently implemented pair-automaton checks agree; Bayesian crossover does not double-count separator evidence; delayed reports are processed in causal order; partial tables never receive universal certificates; core theorems compile in pinned Lean without sorry; the learner discovers an unprovided invariant on opaque-label holdouts and preserves old failures.

## EO1. The unique smallest adequate dynamical observer (CLASSICAL / proved)

For an action word w, let U_w execute the word left-to-right. Define

    x ≡* y  iff  o_j(U_w x) = o_j(U_w y) for every finite w and every j.

This is an equivalence relation, it refines equality of primitive readouts, and it is stable under every U_a. Indeed, action stability follows by prepending a to w.

**Maximality theorem.** If an equivalence R refines primitive observation equality and satisfies xRy ⇒ U_a(x) R U_a(y) for every a, then R⊆≡*.

**Proof.** Induction on word length preserves R through U_w; primitive observation compatibility then equates the terminal reports. Thus ≡* is the largest such equivalence and X/≡* is the smallest state representation preserving all permitted future observations. This is classical behavioural equivalence / deterministic automaton minimization, not a new general coalgebra theorem.

For a surjection q:X→Q, an induced update V:Q→Q with qU=Vq exists iff qx=qy implies qUx=qUy. Necessity is substitution. Conversely define V(qx)=qUx; the condition makes this well-defined and surjectivity makes it unique. This is the actual commuting square that E must repair.

## EO2. A failed square constructs a new experiment (CLASSICAL / constructive)

Suppose E represents x by the results of a finite test family F. If q_F(x)=q_F(y), but q_F(U_a x)≠q_F(U_a y), some test f∈F separates U_a x from U_a y. Construct

    f_new = f ∘ U_a.

Its syntax is obtained by prepending a to the action word of f. It separates x,y. Every dynamically adequate observer must separate x,y too, by EO1. Thus the witness is not merely a penalty against one candidate: it invalidates EVERY candidate that erases this necessary distinction.

**Finite progress theorem.** Start with all primitive readouts; retain previous tests and add one witnessed composite test per failure. If r=|X/≡*| and b0 is the number of primitive observation classes, at most r−b0 ≤ |X|−b0 failures occur before a complete finite check succeeds.

**Proof.** Each new test strictly increases the number of classes. Every generated test is a primitive readout after a lawful word, so it is constant on ≡* classes; no stage has more than r classes. Upon success the candidate equivalence is stable and observation-preserving, hence equals ≡* by EO1 and the preceding inclusion. This counts strict refinements, NOT CPU instructions, physical experiments, elapsed time or memory bits.

A finite budget stopping early is `UNRESOLVED_REFINEMENT_BUDGET`, not a proof that no adequate model exists. The checker assumes a complete finite mathematical transition oracle. Its answers are not justified by finite samples from an unbounded or unknown carrier.

## EO3. Universal property and genuine categorical reuse (CLASSICAL / proved)

If r:X→R is any adequate surjective observer, there is a unique f:R→X/≡* such that f∘r=q*. Define f(r(x))=[x]. EO1 ensures well-definedness. Moreover f intertwines every induced action: checking on x gives f(r(U_a x))=[U_a x]. Surjectivity extends this to all R.

Thus the quotient is terminal among adequate surjective source observers with commuting factor maps. Action words form a free monoid/one-object category; sending each word to its induced transformation is a functor. Generator squares imply every finite composite square by induction. Factor maps between successive sufficient representations compose normally.

The implementation additionally constructs the actual powerset adjunction

    ∃_q(P) ⊆ Q  iff  P ⊆ q^{-1}(Q).

The two sides say the same thing pointwise: every source satisfying P maps to a state satisfying Q. No general adjunction-invention or arbitrary higher-category synthesis is claimed; this is one checked constructor in the new metagrammar.

## EO4. Repair commutes with deterministic shared-source fusion (CLASSICAL / proved)

Let two observers on the SAME source and SAME action family have primitive readouts o1,o2, with behavioural equivalences E1,E2. The joint observer o=(o1,o2) has

    E_joint = E1 ∩ E2.

**Proof.** Equality of every paired future observation is equivalent to equality of each component's future observation. Therefore the jointly repaired representation is canonically isomorphic to the reachable shared-source image

    {[x]_{E1},[x]_{E2}: x∈X} ⊆ X/E1 × X/E2.

The full Cartesian product may contain impossible combinations. The code uses the source image, not arbitrary independently paired states. Repair is monotone under adding readouts or lawful actions, and idempotent as a behavioural quotient. Re-running the learning algorithm from only the primitive readout can still perform work; idempotence is not a free computational cache.

**Important failure beyond the hypotheses.** Marginal stochastic models do not determine their coupling. A hidden bit selects either the joint law P(0,0)=P(1,1)=1/2 or P(0,1)=P(1,0)=1/2. Each individual observer sees exactly a fair bit, but their joint parity identifies the hidden bit. Thus marginal statistical equivalence cannot substitute for complete joint behavioural equivalence. Cross-model dependence is part of the context.

## EO5. Counterexamples become inherited genes (CLASSICAL CEGIS / finite specialization)

The parent genetic implementation had three failed seeds (0,11,13) out of twenty on its ternary task, followed by a separately disclosed exhaustive rescue. The new bridge search keeps a persistent archive of pairs `left value ↦ required right value`. A rejected candidate exposes one previously unfixed value. All future permutation crossovers and mutations preserve these fixed alleles.

**Finite bridge theorem.** For a consistent, completely specified bijection on d values, this counterexample-guided search needs at most d−1 rejected candidates and one accepted candidate. It uses no enumeration of the d! maps.

**Proof.** A failure cannot occur at an already fixed value; every failure fixes a new one. After d−1 values the final value is forced by bijectivity. The uniform guarantee comes from the informative exact verifier and sound constraint inheritance, NOT from evolutionary fitness. A weaker oracle or inconsistent source invalidates the guarantee.

On partial reports fixing k distinct inputs, there are (d−k)! source-report-compatible bijections, assuming no further laws. A chosen candidate remains a proposal unless the relevant source class and proof obligations are closed. The code rejects a `complete_source_class=True` flag when even interface coverage is missing; complete interface coverage still does not physically authenticate the source.

A generic archive pruning theorem says: if a witness obligation is necessary for all valid candidates, failing it soundly excludes a candidate. The meaningful part is deriving that obligation from EO2 or a genuine source report. Merely labelling an arbitrary constraint as necessary would be circular.

## EO6. Source-aware probabilistic crossover (CLASSICAL / exact)

Suppose two law capsules provide p(a,y) and p(y,b), with identical common marginal p(y). Under the EXTRA conditional-independence assumption A independent B given Y, their unique joint law is

    q(a,y,b)=p(a,y)p(y,b)/p(y)   when p(y)>0,

and zero when p(y)=0. Summing over a or b verifies the parent marginals. Conversely conditional independence factors every joint law this way. Different context/source/basis/epoch signatures are not silently identified.

This is finite conditional-product/Markov-category mathematics. Without the conditional-independence hypothesis, the system preserves an explicit family of compatible couplings. A target probability is reported as an interval over the DECLARED finite convex hull, not as a uniquely inferred number and not as an automatic enumeration of all couplings.

**Bayes/gluing naturality.** For shared evidence with likelihood L(y), let Z=Σ_y p(y)L(y). Updating both parents and the separator, then gluing, yields

    [(p(a,y)L/Z)(p(y,b)L/Z)]/[p(y)L/Z] = q(a,y,b)L/Z.

This equals updating the joint law directly. Keeping the OLD separator instead produces a factor L²: evidence duplication. In the exact fair-separator calibration, likelihoods 1/4 and 3/4 yield correct posterior 3/4, while the squared-evidence shortcut yields 9/10.

The Bayesian bridge-population adapter converts candidate bijections into explicit finite likelihood models. One declared noisy query gives posterior (4/5,1/10,1/10) from three equal-prior candidates. It ranks hypotheses without promoting them to physical truth. Repeated noisy observations leave every positive-likelihood rival alive at every finite stage.

## EO7. Noisy interventions preserve ORIGINAL-source bookkeeping (CLASSICAL / exact)

For hypothesis m, original state x, current state z, maintain π_t(m,x,z). A declared action first changes z by transition K_a(z,z') and then emits y by L_a(y|z'). The update is

    π_{t+1}(m,x,z') ∝ Σ_z π_t(m,x,z) K^m_a(z,z') L^m_a(y|z').

The original x coordinate is not overwritten. This is finite hidden-state filtering on an augmented original/current carrier, with exact rational laws. It correctly handles repeated reports of the same latent variable, fresh conditional noise, and destructive interventions.

**Delayed delivery theorem.** For one declared causally ordered stream, buffering out-of-order arrivals until a contiguous prefix is available produces exactly the same posterior as receiving that prefix in causal order. Induction on the processed sequence proves this. Interventions can be noncommutative; arrival order must not replace causal order.

In the exact test, an erase action followed by a flip yields current state 1, while the original bit remains fair. Receiving the flip receipt first does not prematurely update anything. Duplicate event IDs do not count twice; conflicting IDs, source changes and impossible observations are rejected transactionally.

This does not solve a general partially ordered distributed source: independent concurrent updates need separately proved commutation/base-change laws. A syntactic `FreshEvidenceContract` blocks literal training/holdout reuse but does NOT prove independence or valid calibration; appropriate source-conditioned laws remain necessary.

## EO8. Partial tables must remain open (CLASSICAL / finite scope)

For an assumed N-state source with a actions and k observed distinct transition entries, there are N^(aN−k) total deterministic completions if no other structure is imposed. Every missing entry is open, not an automatic self-loop. The `PartialTransitionTable` filters candidates against actual recorded rows, requests an unobserved query, and refuses to produce a complete dynamic certificate until the declared finite domain has been covered.

A two-state calibration leaves identity and erase dynamics both possible after observing only U(0)=0. Observing U(1)=1 eliminates erase. Before that observation the engine must return `UNRESOLVED_PARTIAL_SOURCE`. Unknown carrier cardinality, unknown physical action types and genuinely open-world laws remain harder obligations.

## EO9. Precommitted unknown-to-E law discovery (exact finite experiment + general proof)

`DISCOVERY_PRECOMMIT.json` was committed at `93d67f25b1552f0aa78aff0589ca1a59baa32f7a` before evaluating the holdouts. Calibration uses p=3, seed 271828; heldouts use (5,314159) and (7,161803). The simulator keeps coordinates private and permutes all state indices. The learner receives only finite action tables and a readout, not p, latent coordinate formulas, or the desired invariant.

For the independent mathematical audit, the source is F_p³ with

    A(x,y,z)=(x+1,y,z+y),    B(x,y,z)=(x,y+1,z),    o(x,y,z)=z.

E begins with p observable classes. A failed update square constructs `read after A`, giving the pair (z,z+y). E then constructs a p²-state quotient and a transformation monoid by closing the learned action tables under composition. A generic law miner tests inverses, the center, element orders, and candidate normal forms. It has no special Heisenberg-group target rule.

**Exact recovered results.**

| p | Hidden states | Initial observer states | Repaired states | Generated action group | Center | Ord(A), Ord(B), Ord(H) |
|---|---:|---:|---:|---:|---:|---|
| 3 | 27 | 3 | 9 | 27 | 3 | 3,3,3 |
| 5 | 125 | 5 | 25 | 125 | 5 | 5,5,5 |
| 7 | 343 | 7 | 49 | 343 | 7 | 7,7,7 |

Every row has one strict experiment-invention step. Thirty-six fresh longer action words per case validate predictions independently of the short words used to generate the basis. The full finite pair-automaton oracle independently checks minimality; this is a different implementation, not an independent human/agent witness.

**Universal source-family proof.** Equality of (z,z+y) means equality of y,z. All future y,z updates are independent of x, so this pair is exactly the minimal behavioural quotient. In execution order A,B,A^{-1},B^{-1}, the commutator H maps (y,z) to (y,z−1). It is central, nonidentity and has order p. Every generated transformation has a unique form

    (y,z) ↦ (y+j, z+i y+k),    i,j,k∈F_p.

Closure follows by composing affine expressions. A,B,H generate every triple; distinct triples act differently, proving p³ transformations. Commuting with A forces j=0 and commuting with B forces i=0, so the center has p elements. This is classical finite Heisenberg-type structure, NOT a theorem previously unknown to humanity.

**Information lower bound.** Distinguishing p² behavioural states using p-valued readouts needs at least two readout results in the worst case. The two constructed observations attain this bound, in the ideal nondestructive-read simulator. This is a cardinality bound, not a claim of cheap physical experiments or fresh-state preparation.

**A useful repair boundary.** The lost x coordinate is not reconstructible from ANY original action/readout word. Add a genuinely new action W(x,y,z)=(z,y,x). Then o∘W=x becomes available and the minimal quotient expands to all p³ states. Old certificates remain valid in their original toolkit but are rejected for the new digest. The change is epistemic reach, not a retroactive change to the original theorem.

## EO10. What is and is not synthesized

New experiment words, quotient state objects, induced actions, comparison maps, conditional products and finite action-algebra relations are constructed from source constraints. The final invariant is not preinstalled as a target expression. The meta-constructors, finite source signatures and candidate law-mining operators ARE engineered inputs. This is object-language growth within a fixed typed metagrammar, not unbounded invention of arbitrary categories, adjunctions, physics or mathematical truth.

The old ternary genetic failure seeds remain regression cases. The new constrained search succeeds on all 20 runs at each of d=3,5,7 without the factorial fallback, with maxima 3,5,7 verifier calls respectively. It is misleading to call this a miraculous genetic breakthrough: exact counterexamples supply stronger supervision and persistent logical constraints.

The source-family experiments are held out from calibration and unknown to E's learner, but selected by the researcher. They do not establish an open-problem result, unbiased generalization, independent scientific novelty, or natural-world source discovery. New examples plus a derivation are evidence for a scoped theorem; fitted examples are not a universal proof.

## EO11. Machine verification, exact scope

`formal/obstruction_synthesis/RepairKernel.lean` contains 15 proved universal declarations: action-word composition; equivalence/stability/maximality of behavioural equality; necessity of separating experiments; deterministic repair-fusion; all-word naturality; quotient-update existence/uniqueness; the predicate adjunction; and sound archive pruning. Lean 4.19.0 has checked this kernel. The printed axiom inventory has no `sorryAx`; the quotient selection proof uses standard `Classical.choice`, and function extensionality uses standard `Quot.sound`. Other printed core lemmas need no axioms.

`DiscoveredInstance.lean` encodes the ACTUALLY learned p=3 action and quotient tables, then checks nine finite claims with kernel-reduced `decide` and explicit existential witnesses: generator/readout naturality, the discovered separator, non-recovery of full source, noncommutation, the commutator word, centrality and period three. Its verification status belongs to CI; no generated numerical output alone is called a formal proof. The workflow also tests rejection of a deliberately false theorem. An initial elaboration failure on three finite existential statements was fixed by supplying their actual witnesses; no statement or assumption was weakened.

The Python algorithms have not been formally refined to these Lean specifications. The finite progress bound, stochastic filtering, general p-family arithmetic proof, and wall-clock resource costs have written proofs/tests rather than a complete Lean mechanization. Whole-program formal verification is still outstanding.

## Provenance, implementation audits, and controls

New implementation: `evolving_observer_categories.py`, `evolving_bridge_search.py`, `source_aware_amalgamation.py`, `obstruction_discovery_lab.py`. The bridge and probability support adapters invoke the previous PR #43 capsule/pullback machinery. All new probabilities and certificates use exact integer/Fraction operations. The independent verifier uses backward pair-automaton reachability rather than the forward generated-test algorithm; complete small partitions test the universal minimality claim. Existing source archives remain unchanged.

The local environment could not clone GitHub due network/DNS restrictions. Local testing therefore used the mounted predecessor package with confirmed Git blob identity for the dependency interface, plus the new sources. The 56 predecessor subset tests passed before modification. The final local subset has 115 passing tests (56 parent and 59 new); it is not a full repository checkout. Full-repository and pinned-Lean verification run in GitHub Actions on the exact committed tree.

Positive/negative controls include 160 generated finite systems; all partitions of 40 four-state systems; 70 shared-source fusion systems; exhaustive finite predicate adjunctions; 150 nonuniform stochastic gluing instances; old 3/20 genetic failures; malformed source, wrong toolkit, forged witness, fake completeness, latent erasure, event replay, delayed noncommuting receipts, inconsistent marginals, duplicated evidence, coupling ambiguity, and training/holdout reuse. No claim of independent reasoner triangulation is made.

## Next verdict-changing questions

1. **Abandon the complete-model oracle.** Learn or bound the state space itself from source-accessible membership/experiment interfaces. Prove what finite data and counterexample access actually suffice; distinguish falsification from equivalence certification.
2. **Grow the metagrammar.** Synthesize new representation constructors with proofs, rather than only apply the supplied word/quotient/group/coupling constructors. Grammar-search fairness and soundness must survive those updates.
3. **Stochastic minimality.** Deterministic congruence minimization does not capture arbitrary probabilistic or quantum observational equivalence. Derive suitable source-conditional minimal representations including dependence, memory, and allowed intervention context.
4. **Resource optimality.** Minimize experiments, preparation/reset cost and memory while preserving the minimal behavioural target. State minimality does not imply a shortest experiment basis or fastest learner.
5. **Mechanize the program.** Link executable representations and witness verifiers to the Lean semantics; formalize finite termination and stochastic gluing/filtering, not only their abstract logical core.
6. **Independent mathematical advance.** Seek a source family not selected to fit these constructors, precommit rivals and holdouts, and derive a genuinely new invariant or theorem. The present result does not identify the completed Weil/Suzuki form or prove RH; no unknown zeta zeros enter any construction.

## Primary mathematical references

- Armando Solar-Lezama, *Program Synthesis by Sketching* (2008), Berkeley technical report EECS-2008-177: https://www2.eecs.berkeley.edu/Pubs/TechRpts/2008/EECS-2008-177.html
- Solar-Lezama, *Counterexample Guided Inductive Synthesis*, MIT lecture notes: https://people.csail.mit.edu/asolar/SynthesisCourse2020/Lecture10.htm
- Dana Angluin, *Learning regular sets from queries and counterexamples*, Information and Computation 75 (1987), 87–106: https://doi.org/10.1016/0890-5401(87)90052-6
- Dorsch, Milius, Schröder, Wißmann, *Efficient Coalgebraic Partition Refinement*, CONCUR 2017: https://doi.org/10.4230/LIPIcs.CONCUR.2017.32
- Tobias Fritz, *A synthetic approach to Markov kernels, conditional independence and theorems on sufficient statistics*, Advances in Mathematics 370 (2020): https://arxiv.org/abs/1908.07021
- Official Lean toolchain documentation: https://lean-lang.org/doc/reference/latest/Build-Tools-and-Distribution/Managing-Toolchains-with-Elan/

These sources establish prior art and standard framework choices. The particular new code, proof kernel, witness protocol and benchmark derivations need their own verification. Scholarly priority is UNVERIFIED; physical source authenticity and unrestricted ontology are not claimed.
