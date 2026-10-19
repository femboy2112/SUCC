# Academic novelty comparison: exact forgetting and adjacent lanes

**Date:** 2026-10-18. **Inspected source base:**
`f309d9104ba480c1999c962af1df7c50f19e1bfe`.
**Working branch:** `research/academic-transmutation-2026-10-18`.
**Scope:** bounded primary-source comparison and independent mathematical
criticism; no exhaustive priority search or claim of scholarly originality.
This supplement does not change historical claim statuses.

## 1. Main verdict

An exact future-preserving quotient of a deterministic source, including partial
actions, changing source/history states, state-dependent costs and designated
task outputs, is an instance of classical coalgebraic behavioral equivalence.
The explicit contract, implementation, obstruction examples and verification
can be useful SUCC contributions. Those additions do not by themselves make the
underlying quotient theorem a new theorem in the literature.

For state set X, actions A, outputs O and nonnegative costs C, the relevant
type is

\[
F(X)=O\times(1+C\times X)^A.
\]

The option value records unavailable actions. Complete source/history states
belong to X; declared proof answers can be components of O. Source identity is
preserved only if it is an output or a separate morphism constraint. Merely
adding semantic names to X or O does not escape this classical formulation.

## 2. Theorem-by-theorem comparison

| Candidate or claim | Closest inspected result | Defensible SUCC contribution | Status and boundary |
|---|---|---|---|
| Greatest exact future equivalence and its universal quotient | Rutten [R], Theorems 7.2, 7.4, 9.3 and Proposition 8.2; partial-machine instances in [S] | One explicit source/history/cost/task contract; exact checker and countermodels | **CLASSICAL / PROVED LOCAL**, independently reviewed; academic novelty **UNVERIFIED** |
| Partial actions or structured output values as a strict extension | [S], section 3.1.1 and structured Moore examples | Explicit lawful/undefined semantics instead of silently totalizing actions | The claimed novelty from these features alone is **REFUTED** by the classical encoding |
| Preserve all bounded experiments by a fixed-budget quotient on bare source states | Residual-language reasoning; state augmentation with remaining resources | Exact residual-budget theorem and countermodel to replenishing the budget after every action | Counterclaim **REFUTED** below; new priority **UNVERIFIED** |
| Exact minimum budget that distinguishes two states | Classical synchronized pair search and nonnegative shortest paths; no exact prior weighted-testing theorem was established in this bounded audit | Under the specified rejection/price interface, finite rational threshold d satisfies inequivalence at budget B iff d <= B | Theorem D in [future-safe forgetting](FUTURE_SAFE_FORGETTING.md) **PROVED LOCAL**; priority **UNVERIFIED** |
| All future answers factor through a representation, therefore its updates are well-defined | Quotient descent [R]; existing SUCC CS1 | Separate predictive sufficiency from update closure | Implication **REFUTED** below |
| General stochastic analogue | [G], stochastic bisimulation and quotient-policy preservation; [P], predictive sufficient states | A future separately proved history/resource/provenance contract | **UNVERIFIED** as a new SUCC theorem; deterministic proof does not establish it |
| Source-indexed causal path lifting and finite obstruction | Automata subset construction; acyclic private network-flow decomposition and duality [F] | Complete all-projected-path audit; source/report-sensitive finite obstruction bound; checked private paths, cuts and invariants | LH1/LH2 **PROVED LOCAL / CLASSICAL** after independent proof review; novelty **UNVERIFIED** |
| Arbitrarily late rational Beurling-source camouflage | Generalized-prime source class [B]; #162's fixed paired mutant; finite-transcript nonidentifiability | ASM-01 supplies one family matching every prescribed finite horizon, density one with effective O(log^2 X) error, residue one and the critical-strip zero divisor, while exhibiting an explicit braid defect | **PROVED LOCAL**; new-to-project constructive obstruction; scholarly priority **UNVERIFIED**; full completed source/functional equation is not preserved |
| Original Gamma tail with retained Laplacian and paid endpoint layers | Classical exponential-kernel resolvent integration and Schur bounds; inherited original Gamma adapter; official Gamma context [D] | GTR-1--3 retain -16 S_3(J) h'' with explicit endpoint and bulk remainder; exact whole-source certificate comparison | **PROVED LOCAL** source-specific bound; scholarly priority **UNVERIFIED**; smaller tail uncertainty did not certify or improve the complete tested Schur lower |

## 3. Existing repository work must be credited

[B15](../2026-10-13/SWARM_ATLAS/B15.md), sections 3--6, already proves total
deterministic Moore finality, the greatest report/action congruence, the quotient
as the image of final semantics, and the correct map from any finer quotient.
It also supplies nondeterministic and probabilistic trace-versus-bisimulation
countermodels and a remembered-history obstruction.

[EODCS causal Nerode](../2026-10-13/EODCS_CAUSAL_NERODE_PROBE_GENESIS.md),
CS1--6, already develops the fiber criterion for causal descent, least pair
refinement, stationary finite plateau and multi-action refinement. CS10 explicitly
leaves resource-faithful and broader changing-history interfaces open. These
are predecessors, not fresh discoveries in this round. The manuscript should
state the actual delta from them.

## 4. Sharp guards and countermodels

**Predictive sufficiency versus an executable quotient.** Let beta(x) be the
complete declared future behavior. For any representation q, every behavior
factors through q exactly when ker(q) is contained in ker(beta). A deterministic
induced update additionally requires ker(q) itself to be transition-stable.
Refining a stable equivalence need not preserve stability.

For a four-state unary unit-cost system, take p->u, q->v, u->u and v->v, with
all reports equal. Every state has identical behavior. The representation
e(p)=e(q)=0, e(u)=1, e(v)=2 preserves every future answer but has no induced
deterministic update at 0. An abstract decoder is also not automatically a
computable decoder.

**Universal-arrow direction.** For a surjective exact system morphism e:X->Y,
the canonical behavioral quotient pi satisfies pi=f composed with e for a
unique f:Y->X/~. In general e does not factor through pi: e may retain extra
irrelevant distinctions. This is the direction already used in B15.

**Budget depletion.** Take unary unit-cost transitions p->u, q->v, u->u,
v->z, z->z. All reports are 0 except the report at z, which is 1. With budget
1, p and q have identical available traces, while u and v are distinguished.
Thus fixed-budget equivalence on X is not an unbudgeted transition congruence.
Use resource states (x,b) with updates (x,b)->(x',b-c). State whether unavailable
and unaffordable actions have distinct reports; do not silently introduce one.

**Availability is not a free sensor.** A difference in enabled actions is a
legality difference. It is an executable observational distinction only under
an explicit menu/refusal instrument or other permitted protocol. In particular,
a source-aware evaluator is not automatically an observer policy. The existing
architecture already distinguishes these models.

**Semantic quotient versus effective construction.** A computable countable
unary system can have states (M,n), successor (M,n+1), unit cost, and output 1
exactly when Turing machine M halts within n steps. Add an always-zero self-loop
z. Then (M,0) and z are behaviorally equivalent exactly when M never halts.
All one-step data are computable, but no uniform equivalence decision algorithm
exists for this class. Finite complete tables are a different domain. This
obstruction supplies no claim about RH undecidability.

**Proof authority.** Putting a proof-task answer in O preserves the specified
answer function. It does not establish its soundness, decide all mathematical
truths, or provide a lawful finite procedure to obtain it. Each of those is an
additional mathematical or operational obligation.

**Branching boundary.** For nondeterminism or probability, equality of output
traces need not equal branching bisimulation. B15 already gives exact examples.
An extension must declare which equivalence it preserves, its policy class,
observations, probability conditioning and zero-probability conventions.

## 5. Sources and inspected scope

- **[R]** J. J. M. M. Rutten, *Universal coalgebra: a theory of systems*,
  Theoretical Computer Science 249 (2000), 3--80.
  [Primary paper, hosted PDF](https://fldit-www.cs.tu-dortmund.de/~peter/Rutten/UniversalCoalgebra.pdf).
  Inspected: Theorems 7.2 and 7.4 give quotient factorization; Proposition 8.2
  characterizes the simple quotient; Theorem 9.3 identifies bisimilarity with
  equality of final behaviors. Their generality makes the displayed deterministic
  encoding a specialization, not evidence of independent priority.
- **[S]** A. Silva, F. Bonchi, M. Bonsangue and J. Rutten, *Generalizing
  determinization from automata to coalgebras*.
  [Author paper](https://arxiv.org/pdf/1302.1046).
  Inspected: section 3.1.1 treats partial Mealy machines; section 3.1 gives
  structured Moore examples; Theorem 4.1 compares original and determinized
  behavioral equivalences under lifting hypotheses.
- **[G]** R. Givan, T. Dean and M. Greig, *Equivalence notions and model
  minimization in Markov decision processes*, Artificial Intelligence 147
  (2003), 163--223.
  [Primary paper, hosted PDF](https://ics.uci.edu/~dechter/courses/ics-295/fall-2019/papers/givan-dean-greig.pdf).
  Inspected: section 3.3 requires equal rewards and class-transition
  probabilities; Theorems 5 and 7 establish value/sequence preservation and
  lifting of optimal quotient policies. This is an MDP result, not a claim that
  arbitrary hidden-state POMDP compression is solved by the same condition.
- **[P]** M. L. Littman, R. S. Sutton and S. Singh, *Predictive Representations
  of State*, NIPS 2001.
  [Original proceedings PDF](https://proceedings.neurips.cc/paper/2001/file/1e4d36177d71bbb3558e43af9577d70e-Paper.pdf).
  Inspected: the sufficient-statistic definition preceding Theorem 1 and the
  theorem giving a linear PSR with no more tests than the number of states in
  a minimal finite POMDP model. No literal finite-state quotient is thereby
  asserted for every belief process.
- **[F]** L. R. Ford Jr. and D. R. Fulkerson, *Maximal flow through a network*,
  Canadian Journal of Mathematics 8 (1956), 399--404.
  [Publisher record](https://doi.org/10.4153/CJM-1956-045-5);
  [primary scanned PDF](https://www.cs.yale.edu/homes/lans/readings/routing/ford-max_flow-1956.pdf).
  Bibliography and scan located. Exact matching to the new causal theorem is
  supplied by the explicit acyclic flow proof in LH1; an arbitrary causal
  constraint system is not automatically an integral network-flow problem.
- **[B]** A. Beurling, *Analyse de la loi asymptotique de la distribution des
  nombres premiers generalises. I*, Acta Mathematica 68 (1937), 255--291.
  [DOI](https://doi.org/10.1007/BF02546666).
  Bibliographic lead; the original article was not fetched successfully in
  this bounded audit. No particular theorem from it is used as a proof here.
- **[D]** NIST Digital Library of Mathematical Functions,
  [section 5.9](https://dlmf.nist.gov/5.9), especially the Gamma/psi integral
  representations and their stated domains. Official reference inspected;
  the particular tail bound is proved directly from the inherited original
  exponential-kernel series in GTR-1--3. DLMF is contextual authority, not a
  source for that particular bound or for positivity of the Weil form.

## 6. Verdict-changing work

To establish a strict mathematical advance, identify a conclusion unavailable
from the displayed classical encoding under equivalent hypotheses, or establish
a new sharp source-specific bound/obstruction whose proof uses additional
structure. Until then, report the reusable contract and checked counterexamples
as local synthesis. Formal verification can increase confidence in a statement;
it does not establish academic priority or authenticate a physical source.

## 7. Independent causal proof review

[Lawful history gluing](LAWFUL_HISTORY_GLUING.md), LH1 and LH2, was subsequently
read in full. The unit-flow argument uses the complete private layered network;
positive-flow path subtraction terminates because an edge vanishes at every
step and no circulation survives in a directed acyclic graph. Its binary dual
has the correct sign for the declared head-minus-tail incidence convention.
For LH2, deleting a repeated nonempty (report,support) configuration shortens
any failed path. This proves the stated upper bound
sum_y(2^|fiber_y|-1), not a claim that every source attains that bound.

No soundness defect was found in those arguments. A separate Cartesian-path
oracle checked all 988 three-state/two-action graphs with at most three edges,
fixed reports (0,0,1), and the first state initial: 724 had spurious projected
paths, and every shortest length agreed with the implementation and its
certificates. This bounded run is a code check, not the universal proof.
The cut checker proves non-liftability; local admissibility must additionally
be checked when the desired verdict is that a path is *spurious*.

Section 5.4's three-state example further separates one lift for every whole
word from a single online resolver for every future request. This is an exact
quantifier obstruction, not a defect in LH2's explicitly pathwise contract.

## 8. Independent future-safe proof review

[Future-safe forgetting](FUTURE_SAFE_FORGETTING.md), Theorems A--D, was read
in full. The quotient arrows, finite refinement bound, residual-budget
monotonicity and intersection statement are correct for the declared interface.
In Theorem D a cost mismatch is exposed when the cheaper action first becomes
affordable, so the terminal edge must use the minimum cost, not the maximum.
Equal-cost common prefixes then give exactly a nonnegative shortest-path
problem. No novelty follows from this reduction alone.

A separate algebraic oracle enumerated all 52 partitions for each of 160 fresh
five-state/two-action models, checked the local laws directly, and matched the
unique minimal valid congruence. A separate bounded-transcript interpreter
checked the threshold code on 100 fresh four-state/two-action models with
costs 0, 1/3, 1/2, 2/3, using all words through six actions and the budget grid
0, 1/6, ..., 4: all agreed (98 finite thresholds, two infinite), and all 98
returned words distinguished at the exact returned threshold. These are
bounded implementation checks, not replacements for the proofs.

One wording guard was reported: for arbitrary sets, autonomous updates are
*determined by* the retained state; computability additionally needs effective
presentations and algorithms. This does not affect the finite-table code.

## 9. Final arithmetic and Gamma comparison

[Arithmetic source minimality](ARITHMETIC_SOURCE_MINIMALITY.md), ASM-01,
was read and its elementary derivation checked. Deleted-prime valuations
separate source words; the paired replacement identity normalizes density and
residue; the omitted p atom gives the exact next braid defect. The analytic
factor has no zeros or poles on Re(s)>0. This simultaneous arbitrary-horizon
construction is a concrete advance over the project's fixed mutant. It
neither proves a new general Beurling theorem nor authenticates the complete
Weil source. The adaptive corollary uses only the stated bounded-query language.
Academic priority of the assembled construction remains **UNVERIFIED**.

[Gamma tail refinement](GAMMA_TAIL_RESOLVENT_REFINEMENT.md), GTR-1--3,
was read and the integration-by-parts constants, endpoint signs and summable
norm estimates checked. For real clamped H^4 functions the bound follows from
the exact exponential resolvent and Cauchy--Schwarz; complex functions require
replacing uv by Re(u conjugate(v)) and squares by squared moduli in the endpoint
norm, or explicitly restricting the theorem to real functions.
The project advance is this original-source remainder with endpoint costs and
the exact signed comparison. It is not a new general resolvent method. The
retained leading action increases the projected residual enough that smaller
tail uncertainty does not yield a successful first-window certificate. The
Schur conclusion remains conditional on inherited coercivity and the source
adapter; tested negative conservative lowers are **AMBIGUOUS**, not negative
original-source witnesses. Priority is **UNVERIFIED** and first-window
positivity remains **OPEN**.
