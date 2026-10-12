# A shared fundamental carrier, circle E-towers, and genuine boundary reconstruction

**Checkpoint:** 2026-10-12, a continuation of the maintainer's circle/sphere family of E-towers, and a refinement of the independent local-to-global Čech/Yoneda gluing in SUCC PR #27. The maintainer's decisive additional premise is **all SUCC nodes inhabit the same fundamental carrier, which is the actual global interior field**, not separate independent interiors. All results are elementary/classical with local finite proof and exact-code oracles. No claim of new mathematical priority, physical observation authentication, AdS/CFT, adelic completion, completed Weil positivity or RH.

## Carrier/source distinction: existence versus epistemic recovery

Let **C** be the set of admissible states of ONE declared carrier (interior field). Every boundary tower E_{θ,n} is associated with a lawful observation map **q_{θ,n}:C→Y_{θ,n}**. Vertical successor/refinement and horizontal communication are comparisons between outputs of maps on the *same* C. They must respect source identity, basis and, for interventions, actual source transitions; a matching source-id string alone authenticates nothing.

The entire boundary observation interface is the map

\[
\mathcal O:C\longrightarrow\prod_{(\theta,n)}Y_{\theta,n},\qquad
x\mapsto\bigl(q_{\theta,n}(x)\bigr)_{\theta,n}.
\]

With cross-node consistency relations, the codomain is narrowed to a compatible inverse-limit/equalizer object **B**. There is a canonical source-to-boundary map **O:C→B**. **The ontic global interior is C**; an element of B represents only observational data. Equating B with C requires proving that O is sufficiently faithful or providing a source-derived extension law.

### SC1. Source-relative target factorization criterion (classical, PROVED LOCAL)

For sets C, B and target Z, with O:C→B and T:C→Z, there exists a decoder \(\widehat T:O(C)→Z\) such that \(T=\widehat T\circ O\) **iff**

\[
\boxed{O(x)=O(y)\Rightarrow T(x)=T(y)\quad\forall x,y\in C.}
\]

Proof: necessity by substituting into the factorization; sufficiency by defining \(\widehat T(O(x))=T(x)\), well-defined exactly when T is constant on each observational fiber. Decoder uniqueness holds **on O(C)**, not on all arbitrary formally compatible boundary reports. In particular reconstructing *all* carrier states requires O injective (or injective modulo a declared gauge equivalence). Reconstructing a *claim* may be possible even when states are not uniquely distinguishable. This cleanly separates operational sufficiency from underlying ontology. Implemented by `SharedSource.factorization` and `SharedSource.conclude`.

### SC2. A common carrier does NOT make pairwise source-compatible records globally compatible (PROVED LOCAL negative control)

Let C be the four 3-bit strings of **even parity**: C={000,011,101,110}. Each of three boundary observers reports one bit. The reports (1,1,1) are **pairwise** realizable by valid states 110,101,011, respectively. But their joint fiber in C is empty. Thus pairwise horizontal agreement does not imply a common global source; all available observations must admit a joint witness, or there must be a proven descent/sheaf condition that supplies one.

An actual source state x∈C makes its true reports globally realizable by construction. What fails is the converse inference from formally compatible, unauthenticated local records. This is a finite constraint/gluing obstruction, not a physical contextuality theorem.

### SC3. Horizontal communication cannot create source distinctions for free (CLASSICAL, PROVED LOCAL)

Suppose x,y∈C give the same outcome to every tower's admissible boundary measurement. Any purely **deterministic**, source-blind communication/aggregation protocol between those towers yields identical transcripts under x and y. Proof is an induction over the message events: initial transcripts agree; deterministic next messages are functions of already equal data. With additional independent source-blind randomness, the *transcript laws* are identical by conditioning on its seeds. Hence cross-communication may **combine information from different genuine probes** but cannot recover a target T that separates an O-fiber without an additional source-sensitive measurement or justified source law. A horizontal ring that simply repeats the same sensor cannot become faithful by taking its network size to infinity.

### SC4. Compact separating-boundary theorem (CLASSICAL)

If C is compact Hausdorff, the observation codomains Y_i are Hausdorff, each q_i:C→Y_i is continuous, and the family of all accessible tower maps **separates points**, then O:C→∏_i Y_i is a **topological embedding** onto O(C). Proof: continuous injective map from compact to Hausdorff is a homeomorphism onto its image. Every continuous target T on C therefore has a unique continuous decoder on O(C). This is a genuine mathematical *holographic observability* sufficient condition. It says nothing about whether separation is physically available, efficient, computable in finite time or guaranteed for finite tower levels.

Finite-level no-go: boundary samples of the holomorphic disk functions 0 and z^{2^n}−1 agree at all 2^n-th roots of unity but have different centers; a finite ring does not determine the interior without a further degree/regularity bound. An increasing tower can have a faithful limit without any fixed finite level attaining full faithfulness.

## An exact finite holographic law from the shared carrier

We now adopt a **positive** example in which the carrier dictates the interior field through a justified mathematics, not through a metaphor.

Let (V,E,w) be a finite undirected graph with conductances w_{uv}>0∈Q, a nonempty designated boundary B⊂V, and interior I=V\B. Require **each connected component of the carrier graph to meet B**. The Laplacian is

\[
(Lu)_v=\sum_{z:\{v,z\}\in E}w_{vz}(u_v-u_z),\quad
L=\begin{pmatrix}L_{BB}&L_{BI}\\L_{IB}&L_{II}\end{pmatrix}.
\]

Every E-tower at boundary vertex b knows the genuine prescribed boundary value f_b. Assume the admissible interior fields obey the **discrete harmonic law** (Lu)_i=0 at every i∈I. This is an additional source-dynamics contract, not inferred from the shared carrier label.

### SC5. Unique harmonic reconstruction and exact boundary action (CLASSICAL / PROVED LOCAL)

The interior Dirichlet Laplacian L_{II} is positive definite and invertible. Indeed, for any vector v supported on interior nodes with boundary value 0,

\[
 v_I^TL_{II}v_I=\sum_{\{a,b\}\in E}w_{ab}(v_a-v_b)^2.
\]

Vanishing implies v is constant on every connected component, hence zero on every component meeting the zero boundary. Thus **E can construct the unique interior** by

\[
\boxed{u_I=-L_{II}^{-1}L_{IB}f_B.}\tag{SC5a}
\]

If all conductances and f_B are rational, every interior value is rational and is computable by finite exact elimination. This is a **genuine source-law-dependent holographic reconstruction**, not merely a consensus among boundary observers.

Define the Dirichlet-to-Neumann/Kron reduced boundary operator

\[
\boxed{\Lambda=L_{BB}-L_{BI}L_{II}^{-1}L_{IB}.}\tag{SC5b}
\]

It is symmetric, positive semidefinite and annihilates the constant vector (on each connected component). The source energy of the unique harmonic interior is **exactly** the boundary action

\[
\boxed{\frac12\sum_{\{a,b\}\in E}w_{ab}(u_a-u_b)^2
=\frac12 f_B^T\Lambda f_B.}\tag{SC5c}
\]

Proof: block substitution from L_{II}u_I=-L_{IB}f_B, then u^T L u=f_B^T\Lambda f_B. Positive semidefiniteness follows from the positive sum of squares. This is the classical Schur-complement reduction of an electrical network, made into an exact SUCC/E boundary certificate.

**Variational uniqueness:** for any other field v with the same boundary data, write e=v-u, e_B=0. The harmonic cross term vanishes; hence

\[
\boxed{\mathcal E(v)-\mathcal E(u)=\tfrac12 e_I^TL_{II}e_I\ge0,}\tag{SC5d}
\]

with equality iff v=u. Therefore the shared carrier's **harmonic law** selects the global interior uniquely. Without the law, the same carrier graph and the same boundary measurements permit infinitely many nonharmonic interiors.

**Exact calibration A (four-node boundary ring plus center):** unit conductance on every ring edge and every spoke, boundary values (1,0,0,0). The reconstructed center is 1/4, all interior fluxes vanish, the boundary operator has diagonal 11/4 and neighboring off-diagonal −5/4; the full interior and boundary-only energies agree as exact fractions.

**Exact calibration B (one-dimensional path):** boundary endpoints 0 and 1 joined through two interior points by three unit edges. The interior field is 1/3 and 2/3; energy is 1/6. The effective boundary operator is (1/3)[[1,−1],[−1,1]].

**Independent controls:** 110 deterministic seeded connected weighted graphs with rational conductances and random boundary conditions, checked for exact interior harmonicity, energy equality, positive variational gap, and common-gauge invariance. Other controls reject unanchored hidden components, wrong source/basis, forged/contradictory reports, improper weights and fabricated proof from an empty source fiber. These software tests do not constitute independent Lean verification.

### SC6. Continuum circle/sphere version (CLASSICAL, under explicit regularity)

For the *real or complex harmonic* fields on D continuous to the closed disk, the boundary trace T:u↦u|_{S^1} is injective by the maximum principle. Every continuous boundary f has a unique harmonic extension given by the Poisson integral. Our prior ring implementation checks finite dyadic consistency and a uniform Lipschitz bound; **assuming the genuine trace is L-Lipschitz**, stage n interpolation has uniform boundary error ≤L/(2·2^n), and harmonic Poisson extension contracts sup-norm error. This supplies an effective *conditional* approximation scheme, not a source-free infinite computation.

In contrast the unrestricted continuous interior fields u≡0 and v(r,θ)=1−r² have identical zero boundary trace but different interiors. They share the **same fundamental disk carrier**. The source law is what excludes v from the admissible harmonic class. The analogous sphere theorem uses the corresponding Poisson kernel on the ball and the maximum principle; it does not imply physical holography or AdS/CFT.

## SC7. The E-ring elimination tower REALLY commutes (CLASSICAL / PROVED LOCAL)

Let **B₀ ⊆ B₁ ⊆ V** be nested boundaries of one positive-conductance carrier, with B₀ meeting every connected component. Denote by **Λ_B(L)** the Schur-complement effective boundary Laplacian obtained by eliminating V\B. Because its off-diagonal entries are nonpositive and each row sums to zero, Λ_B₁(L) itself represents a (possibly dense) positive-conductance graph on B₁. Then the exact tower identity holds:

\[
\boxed{\Lambda_{B_0}(L)=\Lambda_{B_0}(\Lambda_{B_1}(L)).}\tag{SC7}
\]

**Proof 1 (variational):** for any prescribed values on B₀, unique harmonic completion minimizes the positive quadratic energy over all unobserved vertices. Splitting V\B₀ into (V\B₁) followed by (B₁\B₀), the iterated minimization is equal to the joint minimization:

\[
\min_{u_{V\setminus B_0}} \mathcal E_L(u)=
\min_{u_{B_1\setminus B_0}}
  \min_{u_{V\setminus B_1}}\mathcal E_L(u).
\]

Both sides are boundary quadratic forms; equality for all boundary values implies equality of the symmetric boundary operators by polarization. **Proof 2:** associativity of Schur-complement block elimination / Gaussian elimination.

This is precisely the *commuting square* required by a ladder of E-rings: it does not matter whether observers transmit the original carrier or an exact effective model through many intermediary rings. As long as every stage retains the law, gauge and boundary interface, E receives exactly the same boundary action at the base. **No independent global reconstruction or physically zero-cost compression** is inferred: every reduction uses exact source topology and conductances, and eliminating nodes can make the effective graph dense.

**Exact positive witness:** the three-edge unit path (a,u,v,b) reduces directly to conductance 1/3 on a—b. Eliminating v first creates u—b conductance 1/2, then eliminating u gives the same 1/3. 90 independent seeded rational weighted graphs and multiple intermediate-ring choices pass direct-versus-staged equality checks. Mutated nested boundaries that omit required probes, invent unknown nodes or repeat a node are rejected.

## What this does and does not say about the Archimedean place

A circle boundary, a Dirichlet-to-Neumann operator and a complete archimedean absolute value are **different mathematical structures**. If the fundamental carrier is the rational source, the classical normalized product formula for q≠0 gives

\[
\boxed{|q|_\infty=\prod_p p^{v_p(q)},}
\]

but the finite valuations cannot distinguish q from −q, nor produce the real topology, test-function completion, Gamma factor or Weil positivity. The existing `boundary_tower.py` includes this exact sign-alias negative control. An identification of a ring of E-towers with the actual archimedean local factor requires a **concrete morphism preserving topology, source identity, spectral/analytic structure, valuation/product formula and the appropriate test-function action**. None is yet constructed.

## Connection to the previous SUCC descent work

The previous SUCC PR #27 glues independently produced **local potentials** on a prescribed graph if the overlap-graph cocycle vanishes; false gluing yields an actual closed source walk. The shared-carrier model adds a logically distinct gate:

1. **Source realizability:** do all proposed observations really admit an element of the same C?
2. **Observational sufficiency:** does the desired interior/claim factor through the joint boundary map O?
3. **Local-to-global compatibility:** do the patch transition data glue under the exact, full overlap cocycle?
4. **Interior dynamics:** does the shared carrier have a certified extension operator, e.g. the positive definite Dirichlet L_{II}?
5. **Operational sourcing:** could actual devices produce and authenticate the claimed reports without prohibited destructive mutation?

The first four are mathematical questions; the fifth is a separate empirical/source-provenance obligation. Crucially, compatible boundary evidence from a common carrier need not determine the source until the joint observation family is separating **on the admissible law-governed source class**.

## Next genuinely discriminating theorem candidate

Develop a **source-changing, law-preserving base-change theorem** for the boundary operator. Let h:C'→C be an intervention or refinement and K a boundary probe change. Find precise commuting relations under which the reconstructed interior field and the effective boundary action descend naturally:

\[
 \mathrm{Ext}_{C'}\circ K = h^*\circ\mathrm{Ext}_{C},
 \quad \Lambda_{C'} \text{ appropriately related to }\Lambda_C.
\]

The naive equalities fail for arbitrary changes of conductance or hidden interior geometry, even when all boundary values remain unchanged. A positive theorem requires a source-certified carrier map, harmonic law compatibility, and a precise boundary energy pairing. Test gauge freedoms and noncommuting interventions. For actual RH applications, also enforce independent Euler/Gamma/half-density/test-domain source gates and no zero-reading input.

**Status:** Classical algebra, topology, and PDE results; source-relative finite implementation new to SUCC. No source-free holographic theorem, physical infinity, uniquely reconstructed unrestricted interior, analytic archimedean realization, physics or RH proof.
