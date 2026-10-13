# Genetic categorical model fusion: law-preserving crossover, newly generated bridges, and nonflat repair

**Research checkpoint:** 2026-10-12 (New York) / 2026-10-13 UTC. **Branch:** `research/genetic-categorical-model-fusion-2026-10-12`, stacked on contextual-heuristic PR #42 at `45597a5750971130e3399ed69c03e107bdc28c70`. **Source:** maintainer's proposal that independently understood models can be superimposed along their valid intersections, generating new combinations and a genetic-like search for mathematical structures. **Scope:** exact finite sets/relations; finite Z2 local systems; exact rational binary probability couplings; bounded evolutionary search. All classical underlying theorems, no scholarly priority or true external source attestation claimed.

## GF0. A precise typed distinction

An observer E may propose model combinations because they have matching shapes. Structural resemblance, a proposal score, posterior confidence, semantic correspondence, a mathematical proof, and authenticated evidence are **six different types**. In particular, two physical models can share a mathematical interface without sharing a physical source. A genetic mutation is a *conjectural change of representation*, not a permitted mutation of the measured original source.

The research engine works with a *declared finite source type* `(source_id, epoch, basis)`; finite named ports `(name, allowed values)`; independently specified mathematical relations; source-indexed paired observation tables; candidate translations; exact pullback witnesses; and a separate stochastic search that cannot grant proof status. Physically accessible/causal instruments, resetting original states, and empirical authenticity remain unverified in this synthetic laboratory.

## GF1. The compatibility theorem: genuine FinSet pullback (CLASSICAL / PROVED LOCAL)

For model row sets `A,B` with lawful maps `f:A->Y`, `g:B->Y` into a *certified shared interface*, define

\[
P=A\times_Y B=\{(a,b)\in A\times B:f(a)=g(b)\}.
\]

**Theorem.** `P` with projections to A and B is a pullback in `FinSet`. **Proof.** If any set W has maps a:W->A and b:W->B satisfying f∘a=g∘b, the only possible map W->P respecting both projections sends w to (a(w),b(w)). That ordered pair belongs to P by hypothesis, and the map is unique. The code enumerates every candidate pair, verifies the shared-interface equality, and reconstructs the *exact* allowed joined rows by a separate oracle. Source-ID, epoch, basis, port-domain, and forged-pair mutants fail before any proof transport.

**Falsifier:** joining by identical-looking port names with incompatible domains or different source epochs is prohibited. A cross-field alignment is an **additional proof obligation**, not a naming convention.

## GF2. Associativity, independent contexts, and higher-order reuse (CLASSICAL / PROVED LOCAL)

Given three source-compatible finite relations over globally coherent typed variable names, both iterated joins, `(A ⨝ B) ⨝ C` and `A ⨝ (B ⨝ C)`, consist of exactly the global assignments satisfying all three constraints. They are canonically isomorphic after a deterministic port reordering. Proof: logical conjunction is associative, and the projection to each original model is preserved. The code checks concrete equality of all states in a three-model example.

**Caution:** if a model is source-changing, a temporal intervention requires an explicit transformation of the original claim; ordinary static joins do not prove naturality under such interventions. Shared latent *physical* identity does not follow from the mathematical isomorphism.

## GF3. Genuine emergent cross-model theorem (PROVED LOCAL)

One model knows `x XOR y=1`; an independently named model knows `y XOR z=1`. The verified compatibility pullback permits exactly the states `(x,y,z)=(0,1,0),(1,0,1)`. Projecting out y produces the derived relation `x=z`. Neither parent even contains both x and z as ports. The new two-port relation is constructed as a *new theorem capsule* from the pullback, stored with its proof ancestry, and reusable in later joins. This is valid **for every state in the declared joined source class**, not merely for the observed examples.

**Proof:** XOR the parent equations and use `y XOR y=0`. An independent finite table enumerator verifies the exact row set, rather than repeating the symbolic argument as its only test. This is an example of cross-module theorem birth, not independent mathematical novelty.

## GF4. Discover a new arrow, not only select preinstalled adapters (PROVED LOCAL / DECLARED SOURCE)

A second capsule uses values `cold,warm` where the first uses `0,1`. A source-indexed observation table at two distinct source states reports `(0,cold)` and `(1,warm)`. E does **not** receive the map. It enumerates all finite bijections from the first domain to the second and rejects ones inconsistent with source pairs. Here the unique surviving map is `0->cold, 1->warm`. Source-indexed finite-table completeness is explicitly *assumed*, not authenticated by the mere fact that the simulator supplied two rows.

**Uniqueness theorem.** Suppose a total bijection `f:A->B` is required and the paired law is known for every `a∈A`. If compatible, it is unique because each f(a) is fixed. If some `a` is unobserved, multiple total bijections may remain: for example, a 3-value domain with one observed pair has two bijective extensions. E correctly preserves both and cannot silently label one certified.

**Falsifier:** wrong source version, a false value flip, an incomplete observation table, or an attempted identification of two already distinct target ports prevents a legitimate certified bridge.

## GF5. The negative theorem: pairwise compatibility does not glue (CLASSICAL / EXACT)

Three models assert `x XOR y=1`, `y XOR z=1`, `x XOR z=1`. Each pair of models admits legitimate states; their full intersection is empty. The sum of these three equations modulo 2 asserts `0=1`.

**Minimal unsatisfiable core:** all three equations are needed; every proper subfamily is satisfiable. The engine enumerates source-compatible subsets, returning the triple as an exact *minimal inconsistency witness*. No empty intersection is upgraded to a unique or vacuous physical source.

This is a concrete counterexample to an overly optimistic model fusion engine that independently checks pairwise compatibility only. In graph terms it is a nontrivial Z2 cycle holonomy.

## GF6. Obstruction-driven language birth: from global potentials to connections (CLASSICAL / PROVED LOCAL)

Each binary edge e from u to v carries the invertible transport `T_e(x)=x XOR b_e`. Transport along a path `e1,...,ek` is `T_path(x)=x XOR (Σ b_e mod 2)`. Path composition and inverse reversal are lawful: these data define a functor from the free path groupoid into one-point group of automorphisms Z2. The data are meaningful **even when no global scalar potential exists**.

**Theorem (binary integrability).** A single-valued vertex potential `q:V->Z2` with `q(v)-q(u)=b_e` on every edge exists iff the XOR sum around **every** closed walk is zero. **Proof:** If q exists, each closed loop sum telescopes. Conversely choose a spanning forest root in each component, define q(v) by the parity sum along the tree path; vanishing cycle sums force each non-tree edge to satisfy its equation. The code constructs an explicit nonzero witness loop when it fails; an independent exhaustive assignment oracle validates 240 seeded graphs including loops and disconnected carriers.

**Language repair:** the nonzero-holonomy graph can still be represented correctly by a **nonflat path-indexed connection**, whose loop transports flip the fiber. This does NOT repair the impossible claim that the three source observations are equalities of one scalar vertex field, and does NOT claim an external physical gauge field. It identifies the missing *kind of representation* without deleting inconvenient evidence.

## GF7. A typed, bounded evolutionary search (PROVED LOCAL; HEURISTIC fitness)

A genome stores `(candidate bijection, left-parent included?, right-parent included?)`. Mutation can swap two bijection values or add/remove a parent; crossover inherits a whole typed permutation from one parent and separately inherits parent-inclusion genes. No operation can form a non-bijection or edit the source table. The population is finite, seeded and reproducible. A declared score rewards verified source-pair matches and newly **expressible** cross-family relations and penalizes mismatches/complexity; the score carries no semantic proof authority.

For source table with 2 symbols there are `2!·2²=8` possible genomes. In ten deterministic tested seeds, the genetic process discovers the correct bridge and combined theorem. A separate **exhaustive search of all eight genomes**, not the genetic algorithm, proves that the returned score is optimal *within this restricted grammar*. Any proposal's proof is separately checked against the full declared source table and FinSet pullback semantics. The new inferred x-z relation is absent from the parent modules and is inserted into the extended model library as a derived capsule.

**No unjustified moonshot:** no stochastic finite genetic strategy is complete for arbitrary grammars. Genome search is not a proof procedure for unconstrained general mathematics; the current solver invents finite value bijections, finite relation compositions, and derived projection capsules, **not** arbitrary new kinds of categories, functors, or analytic tests.

## GF7a. An honest genetic *failure* creates a stronger source-proof architecture (TESTED MODEL / EXACT FALLBACK)

The binary example has only `2!·4=8` genotypes, so it is a trivial case for evolutionary search. A more demanding independently typed example starts from a cyclic modulo-three model `y=x+1 (mod 3)` and a differently named three-temperature-state model encoding `z=y+2 (mod 3)`. The simulator provides three source-paired reports `0↔cold`, `1↔warm`, `2↔hot`, but **no bridge arrow**. This is a 3!-bijection × four-parent-selection = **24-genome** search grammar. E's exact pullback, once the correct bridge is proposed, derives the genuinely new cross-context law `z=x (mod 3)` by `(x+1)+2=x`.

**Adversarial observation:** the genetic population is neither exhaustive nor globally convergent. With the fixed declared seeds 0 through 19, it independently discovers the optimal verified bridge on **17** seeds but misses it on seeds **0, 11 and 13**, despite finite, complete source data. The `ternary_fusion_demo` labels those failures `genetic_succeeded=False` and `bounded_optimum_verified=False`. Because there are only 24 genotypes, a separate exact enumeration supplies a **bounded-grammar rescue**: it independently finds and source-certifies the bridge and projected theorem even on failed evolutionary seeds. The rescue is never counted as a genetic success.

**Theorem:** a finite enumerator deciding a finite explicit grammar can establish exact bounded optimality; an elitist finite-population heuristic need not sample the global optimum, even when a perfect score is source-attainable. This rules out promoting heuristic search success into mathematical completeness, and supplies actionable failure measurements: add mutation diversity, counterexample-driven candidate generation, or exact fallback when feasible. Increasing mutation or population size is not a universal completeness proof over unrestricted representations.

## GF8. Probabilistic superposition has a missing joint-law parameter (CLASSICAL / EXACT)

Let two independently understood binary heuristics assign `P(A)=p`, `P(B)=q`. Writing `t=P(A∩B)`, the 2x2 joint table is

\[
\begin{pmatrix}
 t & p-t \\
 q-t & 1-p-q+t
\end{pmatrix}.
\]

Nonnegativity is equivalent to the *sharp* Fréchet bounds

\[
\boxed{\max(0,p+q-1)\le t\le\min(p,q).}
\]

**Proof:** each table entry is nonnegative precisely on this interval, and every t in the interval constructs a normalized exact rational joint distribution. For p=2/3, q=3/4, overlap may lie anywhere in `[5/12,2/3]`. The independent product t=pq=1/2 is merely one possibility. Identical marginals may produce positive, negative, or zero covariance depending on the actual coupling.

**Failure control:** treating two separately scored heuristic reports as independent without a source-justified conditional law will invent certainty. This experiment makes *joint source coupling* a first-class unobserved quantity. It is probabilistic correlation, not quantum superposition or entanglement.

## GF9. Hidden coupling imposes an observable lower bound (CLASSICAL / EXACT)

Suppose a binary joint probability matrix `P(X,Y)` admits a latent conditional-independent representation

\[
P(X,Y)=\sum_{z=1}^rP(Z=z)P(X\mid Z=z)P(Y\mid Z=z).
\]

Each z contributes one rank-one outer product, so `rank(P) ≤ r`. A diagonal positive 2x2 law with entries 1/2 has ordinary matrix rank 2: **no one-state conditional-independent latent representation suffices**. A two-state construction exists by taking Z=X. Thus the bound is sharp for this exact binary case. This proves a minimum *mathematical latent dimension*, not the existence or ontology of a physical hidden agent.

## GF10. Source change, inference transport, and the proof firewall (DEFINITION / OPEN)

A pullback certificate in a static source category does not automatically survive an intervention `U:C->C'`. To transport evidence and decoded claims one needs the actual causal/context square and target preservation (as established in the prior CV/F5 program), then a valid Beck–Chevalley/pullback correspondence where appropriate. Failed generators can break a previously valid emergent relation. A genetic search over **syntax** cannot silently solve original-source destructive backaction or causal reset resources.

A high Bayesian posterior, a zero error on sampled data, a low MDL code cost, a valid functor on one selected interface, or a finite generated source ID does not prove physical authenticity, model-class exhaustiveness, an unrestricted analytic theorem, or RH. The `scope` receipt explicitly records these firewalls.

## GF11. Adversarial validation and independent oracles

Files:
- `observational_succ/relational_model_genetics.py`: typed finite relation capsules, exact row-fiber product, source-table bridge synthesis, emergent functional dependency, minimal unsat family.
- `observational_succ/evolutionary_bridge_search.py`: typed genetic crossover/mutation, heuristic score, independently exhaustive bounded grammar optimum, exact derived theorem capsule.
- `observational_succ/genetic_obstruction_holonomy.py`: graph-path connection, nonzero cycle proof, complete binary potential criterion, independent truth-table oracle.
- `observational_succ/source_coupling_bounds.py`: exact Fréchet interval, joint law, conditional latent decomposition and matrix-rank lower bound.
- `tests/test_*.py` (new four files): named tests, 100 random independent Cartesian-product row oracles, 169 marginal pairs at three extremal couplings each, 240 seeded holonomy graphs checked by independent exhaustive vertex assignments, ten binary seeded genetic runs, and a distinct 20-seed ternary test with 17 successes / 3 genuine failures rescued by exhaustive 24-genome search.
- `scripts/genetic_model_fusion_probe.py` produces stable `research/2026-10-12/GENETIC_MODEL_FUSION_RECEIPT.json`. Deterministic local tests are separate from the cited classical infinite/general proofs. Two Python versions must be checked in CI on the exact pushed SHA.

**Prior art** (the new architecture does NOT claim priority):
1. Hitzler, Krötzsch, Ehrig, Sure, *What Is Ontology Merging?—A Category-Theoretical Perspective Using Pushouts* (2005), https://corescholar.libraries.wright.edu/cse/26/ .
2. Zimmermann, Krötzsch, Euzenat, Hitzler, *Formalizing Ontology Alignment and its Operations with Category Theory* (2006), https://corescholar.libraries.wright.edu/cse/201/ .
3. Durán & Meseguer, *Structured theories and institutions* (2003), https://www.sciencedirect.com/science/article/pii/S0304397503003128 .
4. Krawiec & Swan, *Counterexample-Driven Genetic Programming: Heuristic Program Synthesis from Formal Specifications* (2018), https://direct.mit.edu/evco/article/26/3/441/1070/Counterexample-Driven-Genetic-Programming .
5. Braithwaite, Hedges & St Clere Smithe, *The Compositional Structure of Bayesian Inference* (2023), https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.MFCS.2023.24 .
6. Classical graph potentials, groupoid representations, signed graphs, nonnegative matrix factorizations, Fréchet–Hoeffding inequalities, pullbacks in `FinSet`.

## GF12. What genuinely changes the research program?

**Achieved (conditional exact):** E synthesizes a new context translation absent from the supplied adapters, proves a cross-model emergent invariant, records its ancestry as a reusable capsule, diagnoses incompatible global intersections with a minimal source/loop witness, and proposes a lawful higher model type (nonflat path-indexed connection). It scores candidate recombinations heuristically but accepts proofs only from a separate finite exact verifier. It explicitly preserves uncertainty about joint probabilities and hidden source ontology.

**Missing:** source authentication outside a declared simulator; general alignments involving quotient/noninvertible maps and base change; richer typed multicategory/institution-theoretic pushout schemas; automatic invention of **new probe types**, real experiments and causal reset costs; scalable genetic search with independently calibrated fitness and guaranteed diversity; nonstationary/unknown-source model-class growth and rigorous generalization; true theorem novelty audit; proof-assistant formalization; arithmetic Euler/Gamma/Weil identification and positive global theorem. The next moonshot is an actual CEGIS (counterexample-guided inductive synthesis) engine in which E learns novel functors/observations in an enlarging grammar, proves every candidate naturality equation, and grows the grammar specifically in response to exact failures rather than merely adding convenient genes.
