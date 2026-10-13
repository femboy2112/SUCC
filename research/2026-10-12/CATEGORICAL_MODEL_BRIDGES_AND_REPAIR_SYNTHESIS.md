# Categorical model construction, cross-domain bridges and certified black-box abstraction

**SUCC research branch:** `research/categorical-repair-discovery-2026-10-12`  
**Date:** 2026-10-12/13 UTC. **Original maintainer insight:** After a model and its lawful context have been characterized, an observer should be able to reuse the model as a single composable object rather than reopening every internal derivation. The same categorical search should link models from apparently unrelated fields by discovering structure-preserving correspondences.  
**Base:** PR #40, `a085d754e037498a20cbb4d2330e3ce02d2f60c2` (Claude-consolidated main `52d2c02` before RC inverse).  
**Status:** Classical finite automata, categorical black-box semantics, resistor-network mathematics, Stieltjes/Hankel realization and Markov resolvents, implemented in an exact source-typed research prototype. No claim of independent priority, physical source authentication, completed Weil positivity, or RH.

## The precise abstraction goal

A **model capsule** packages `(interface ports, allowed contexts, mathematical law, original-source provenance, epoch, basis, abstract response, certified properties)`. It may retain one internal *witness* for auditing and future adaptation, but routine first-order inference is performed on the interface alone.

Define equivalence relative to a permitted class of contexts \(\mathscr K\):
\[
M\sim_{\mathscr K}N\iff \operatorname{Obs}(C[M])=\operatorname{Obs}(C[N])\quad\forall C\in\mathscr K.
\]
If a black-box semantics \(\mathcal B\) is **compositional** for these contexts—i.e. every \(C\) admits an appropriately typed operation \(\Phi_C\) with \(\mathcal B(C[M])=\Phi_C(\mathcal B(M))\)—then equality of \(\mathcal B(M)\) and \(\mathcal B(N)\) implies contextual equivalence. This is a theorem **conditional on proving compositionality**, not a license to declare arbitrary models equivalent from their appearance.

The implementation establishes this narrowly for *parallel open RC boundary wiring* and *well-posed scalar feedback* at zero initial storage. It does not implement the complete symmetric monoidal category of passive networks or arbitrary nonlinear/quantum context change. That richer theory already exists in Baez–Fong and Baez–Coya–Rebro; this is a source-relative interface and adversarial SUCC implementation.

## CR1 — Construct a categorical quotient of actual observational actions (CLASSICAL / PROVED LOCAL)

For a finite deterministic Mealy machine \(M=(S,A,o,\delta)\), define states \(x\equiv y\) iff **every** legal finite action word produces the same output trace. This is the greatest action-stable observation congruence, equivalently the coarsest valid quotient. Proof: any valid observation-preserving quotient equates only states with identical output and successor quotient on each generator; induction over words establishes behavior equality. Conversely, the behavioral relation itself is a congruence because prefixed words preserve output equality.

The partition-refinement implementation constructs the quotient and the universal map from any finer lawful quotient. For a four-state example, the minimal quotient has blocks `(0), (1), (2,3)`. A first `look` followed by `read` distinguishes states 0 and 1; no shorter word does. A guessed coarse partition merging 0 and 1 fails to commute with `look`, yielding explicit source states and the offending generator. Verified exhaustively on all 256 two-state/two-action binary Mealy tables and 220 additional randomized machines. **Meaning:** an observer can reason with the quotient's dynamics, not with all hidden states, provided it preserves *every permitted generator*.

## CR2 — Automatic representational upgrade from an independently measured boundary (CLASSICAL / CONDITIONAL)

`categorical_repair_synthesis.py` starts with four exact rational boundary receipts at \(s=0,1,2,3\), with no hidden graph or serial-pendant topology supplied to the inverse constructor. It tries four representations:

1. Static memoryless (contradicted by \(\Lambda(1)\ne\Lambda(0)\)).
2. Local-only port storage (contradicted by changing off-diagonal coupling).
3. Single relaxation mode (contradicted by \(q(2)-2q(1)+q(0)=-36/35\) for \(q=1/h\)).
4. A rational two-dimensional passive linear memory (fits all four observations and independently predicts \(s=4,11,17\) in the declared simulator).

The construction gives \(g=(2,3,5)\), \(q(s)=G+\frac{\alpha s+\beta s^2}{1+\gamma s}\) with \(G=10\), \((\alpha,\beta,\gamma)=(5,3/2,3/4)\), and a minimal-rank two-state realization from Hankel moments. This detects a missing *kind* of law (causal memory), not a uniquely existing literal circuit topology. **Source caveat:** a polynomial/rational law class and a two-mode cap remain external hypotheses; E has not generated arbitrary mathematical languages.

## CR3 — Finite observations cannot justify arbitrary complexity bounds (EXACT NO-GO)

For arbitrary prescribed distinct nonnegative rationals \(s_1,\dots,s_m\), choose sufficiently many distinct positive rational poles \(\lambda_j\) and construct
\[
R(s)=\frac{\prod_i(s-s_i)}{\prod_j(s+\lambda_j)}.
\]
The residues in the partial fraction expansion alternate in sign. Separating its positive and negative residues constructs two **strictly positive rational Stieltjes functions** with different modal degrees that agree at every prescribed \(s_i\), yet differ at a held-out frequency. Optional extra interpolation points enforce a common DC value and even residue count. At \(s=0,1,2,3\) the implementation produces a two-mode and three-mode pair with a nonzero held-out difference \(|\Delta(4)|=1/283500\). Therefore `four reports => globally two modes` is **false without an independently justified modal cap**. Each test is exact rational, including 240 randomized finite-observation rivals.

## MB1 — Four samples CAN prove infinitely many equalities when the degree bounds are sourced (CLASSICAL / PROVED)

For a passive finite RC network, with \(n\) interior nodes and boundary zero-storage convention, let \(A(s)=L_{II}+sC_I\). The boundary Dirichlet-to-Neumann map is
\[
\Lambda(s)=L_{BB}-L_{BI}A(s)^{-1}L_{IB}.
\]
Each entry is a rational function with denominator \(\det A(s)\) and numerator \(\le n\) in degree, because the adjugate of \(A(s)\) has degree at most \(n-1\). Two networks with declared maximum hidden sizes \(n,m\) and equal ordered ports are equal at *every* \(s\ge0\) **if their responses agree at \(n+m+1\) distinct nonnegative rational frequencies**: cross multiplication yields a polynomial of degree \(\le n+m\) with too many roots. Positive anchored conductances make the determinants nonzero on this domain.

For a star with one hub and an equivalent split-hub model with two hubs, the exact certificate needs four points. It succeeds. For star versus memoryless triangle, it fails at \(s=1\) although they agree at DC. This proof requires both models' **known mathematical order bounds**, not estimates from the measured table alone. It does not identify which physical topology is true.

## MB2 — Black-box congruence through lawful contexts (CLASSICAL / PROVED)

Two verified equal full boundary maps remain equal after connecting either in parallel to any independent compatible linear network \(K\):
\[
\Lambda_{M\parallel K}(s)=\Lambda_M(s)+\Lambda_K(s).
\]
Disjoint interiors cause the joint Dirichlet block to be block diagonal; Schur elimination gives this identity. For a well-posed scalar boundary feedback law,
\[
F_k(\Lambda)=(I+k\Lambda)^{-1}\Lambda,\qquad k\ge0,
\]
transfer equality likewise implies feedback equality. Passive response \(\Lambda(s)\succeq0\) ensures \(I+k\Lambda(s)\) invertible for \(s\ge0\). Explicit graph gluing, parallel Schur, exact feedback and reassociation are tested. **Not included:** hidden-node interventions, unknown nonzero initial hidden state, incompatible units or temporal coupling beyond the admitted law. Changing one of the split hub's hidden capacitors destroys its equality with the original star.

## MB3 — Electrical circuits, thermal diffusion and absorbing random walks share an exact mathematical adapter (CLASSICAL / PROVED)

For positive weighted edges \(g_{ij}\) and strictly positive interior storage \(c_i\), the heat flow equation
\[
C_I\dot T_I+L_{II}T_I=-L_{IB}T_B
\]
has the same **mathematical** state and transfer matrices as the corresponding RC voltage equation. The bridge must explicitly translate voltage to temperature, current to heat-flow, electrical conductance to thermal conductance and capacitance to heat capacity; it never equates real measurements or source identity between physical domains.

A more surprising connection is probabilistic. Define a continuous-time Markov chain on the interior nodes, with jumps \(i\to j\) at rates \(g_{ij}/c_i\), absorbing transitions \(i\to b\) at rates \(g_{ib}/c_i\), and no other transitions. Its transient generator and exit-rate matrices are
\[
Q=-C_I^{-1}L_{II},\qquad R=-C_I^{-1}L_{IB}.
\]
The discounted absorption kernel \(H(s)\), whose \((i,b)\)-entry equals \(\mathbb E_i[e^{-s\tau}\mathbf1_{\{X_\tau=b\}}]\), satisfies the *first-jump* (or Feynman–Kac) equation
\[
(sI-Q)H(s)=R\quad\Longrightarrow\quad
H(s)=-(L_{II}+sC_I)^{-1}L_{IB}.
\]
Hence
\[
\boxed{\Lambda(s)=L_{BB}+L_{BI}H(s).}
\]
This is an exact, source-derived, **cross-disciplinary commuting square**. A theorem about boundary voltage can be interpreted in terms of discounted hitting probabilities, and vice versa, within the declared law class. In the one-hub example \(g=(2,3,5),c=2\), the exit probabilities are \((1/5,3/10,1/2)\), the expected absorption time is \(1/5\), and the discounted probability of leaving at terminal A at \(s=1\) is \(1/6\). For the two-hub example, the exact transient generator is
\[
Q=\begin{pmatrix}-7&2\\4/3&-4/3\end{pmatrix};
\]
all absorption-probability rows sum exactly to one. The implementation verifies \(\Lambda_{\rm Markov}(s)=\Lambda_{\rm RC}(s)\) on 150 randomized positive serial sources and several independent test frequencies.

## MB4 — A transferable spectral invariant (CLASSICAL / PROVED)

For \(C_I\succ0\) set \(K=C_I^{-1/2}L_{II}C_I^{-1/2}\succ0\) and \(W=C_I^{-1/2}L_{IB}\). Then
\[
\Lambda(s)=L_{BB}-W^\mathsf T(K+sI)^{-1}W.
\]
For every integer \(k\ge1\) and \(s\ge0\),
\[
\boxed{(-1)^{k-1}\Lambda^{(k)}(s)
      =k!\,W^\mathsf T(K+sI)^{-(k+1)}W\succeq0.}
\]
This follows by differentiating the resolvent (diagonalize positive symmetric \(K\)); each term is a Gram matrix with nonnegative weights. In particular \(\Lambda'\succeq0\) and \(\Lambda''\preceq0\). Exact rational Gram tests implement the first two signs. Finite samples \(s=0,1,2\) additionally supply necessary Loewner monotonicity/concavity inequalities, rejecting forged data with negative slopes or convex acceleration. Passing finitely many tests does **not** prove the full passive class.

E can transfer this invariant across **electrical, thermal, and random-walk** interpretations because it is a property of their common *mathematical resolvent*, without rereading each model's physical internals. No relation to completed Weil/Suzuki positivity is established.

## MB5 — Graded observer contexts: first order may forget internals; higher order may not (CLASSICAL / PROVED)

Near \(s_0\ge0\), define the degree-\(k\) observable jet \(J_k\Lambda=(\Lambda(s_0),\Lambda'(s_0),\dots,\Lambda^{(k)}(s_0)/k!)\). If two models have equal k-jets, then **any analytic boundary-only operation with a well-defined local expansion** has equal resulting k-jets (for example, parallel addition or well-posed feedback). This follows by passing to the quotient algebra \(\mathbb Q[[s-s_0]]/((s-s_0)^{k+1})\): polynomial operations and inversion of elements with invertible constant coefficient are well defined and respect equality.

The code computes exact jets of the Schur inverse without numerical derivatives, and computes feedback jets by a recursive formal inverse. It finds star vs triangle equal at grade 0 (static), unequal at grade 1 (first dynamical derivative), and star vs twin equal through grades 0–6 and globally for the admitted LTI context. **Do not infer** hidden-intervention equivalence from even perfect all-frequency boundary equivalence.

## MB6 — Automatic model-link discovery, not accidental analogy (CLASSICAL / TESTED)

`discover_model_connections` attempts all pairwise source-typed connections in a finite model library, first checking port order and basis, then same-source identity (or an explicit electrical↔thermal mathematical adapter), then the exact degree-bound all-frequency theorem. It returns a connection graph with successful law-preserving links and *source-based counterexamples* to proposed links. For the four-item library `(star, twin hubs, thermal star, resistive triangle)`, E finds three mathematical links joining the first three, and correctly isolates the static-only triangle after a dynamical check. The graph's connected components classify **declared mathematical behavior**, not a shared empirical carrier across domains. For genuinely cross-domain links, physical-source identity is explicitly false.

## What we actually learned (not a claim of academic novelty)

1. Once verified, an interface allows safe reasoning with an entire class of internal source implementations; no need to revisit their derivations for every ordinary context. That is an exact *categorical equivalence class relative to the context*.
2. Source-finite measurements and **model-known degree bounds** are separate warrants. The first alone cannot justify the second; constructive higher-degree Stieltjes aliases falsify it.
3. The missing repair type can be a **memory operator** rather than a uniquely inferred object hidden behind the boundary. The category change is measurable by exact failed interface equations.
4. A common operator may link genuinely different sciences (RC ↔ heat ↔ absorbing walk) and transport theorems, but cannot by itself transport physical provenance or identities.
5. Graded contexts formalize the maintainer's observation about first-order versus second-order attention: compress a proven model until the next context requires higher derivatives, interventions, or new interfaces.
6. The current repair engine searches a supplied finite category ladder; it does not generate arbitrary new categories, learn unknown experimental menus, mechanize a general proof fibration, or prove RH.

## Next falsification targets

- **Algorithmic adapter invention:** Search for candidate interpretations (e.g., Laplacians, Markov generators, mass/dashpot systems) using typed signatures/invariants, rather than prelisting each adapter. Prove strict soundness/completeness statements relative to the search grammar and emit counterexamples for invalid adapters.
- **Composition beyond parallel:** Implement general typed open-network pushout gluing with multiport external wires, Schur elimination, algebraic feedback and source-relative Beck–Chevalley tests. The full abstract categorical result should reuse Baez–Fong rather than reinvent established machinery.
- **LTI to nonlinear or non-Markovian fields:** Check how much memory/order data must be added to preserve the certificate when observation changes the state, contexts communicate asynchronously or source noise is introduced.
- **Robust approximate black boxes:** Replace exact transfer identity with operator-norm error bounds under passive feedback (small-gain/invertibility margins). Ensure errors cannot silently amplify across long E-tower loops.
- **Formal priority and source:** Mechanize the rational degree bound, Mealy congruence, and Markov absorption identity in Lean; make empirical source/units/data attestation an independent gate.
- **RH moonshot firewall:** A real arithmetic bridge must arise from authentic finite Euler factors, the true real Gamma/test-function normalization, half-density and the full analytic Weil/Suzuki form, with independent global positivity. Laplacian Gram PSD does not provide that bridge.

## Classical prior art

- John C. Baez and Brendan Fong, *A Compositional Framework for Passive Linear Networks*, **Theory and Applications of Categories** 33 (2018), 1158–1222, <https://www.tac.mta.ca/tac/volumes/33/38/33-38abs.html> (open circuits, external behavior, black-box symmetric monoidal/hypergraph functor).
- John C. Baez, Brandon Coya and Franciscus Rebro, *Props in Network Theory*, **Theory and Applications of Categories** 33 (2018), 727–783, <https://www.tac.mta.ca/tac/volumes/33/25/33-25abs.html> (connections across network types via props).
- Classical random-walk/electrical-network harmonic correspondence and absorption: <https://link.springer.com/chapter/10.1007/978-3-030-27968-4_2>.
- Classical Stieltjes rational functions, spectral resolvents, Schur complements, realization theory; this manuscript proves the finite identities directly under declared hypotheses. These sources must not be construed as independent review or novelty certification of SUCC.
