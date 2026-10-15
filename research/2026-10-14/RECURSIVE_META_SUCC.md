# RECURSIVE META-SUCC: Models of systems of interacting models

**Checkpoint:** 2026-10-14. **Research source:** `femboy2112/SUCC`, mathematical parent `research/global-model-sandwich-2026-10-14@8ce8ebbc4ea26d6a0f53f1f243a8b9a7932461c0` (PR #77); parent in turn includes the completed signed Weil branch. **Research branch:** `research/recursive-meta-interaction-coercivity-2026-10-14`. **RH PROVED: NO.** This is a standalone static finite source-contract and unitary-transport investigation. Nothing asserts physical joint measurement or realization of mathematical counterfactual histories. No Archimedean sign theorem is imported from the Euler data.

## 0. Steelman: what “one recursion farther” means

The maintainer's new direction is not just “Model A and Model B have an intersection.” It is to make **models of models**, **relationships among those models**, and then **models of the relationships themselves** into mathematics capable of enforcing a previously invisible restriction on the source.

A safe version has the levels:

- **Level 0:** a declared complete mathematical source relation `S` in a finite product carrier `Ω=∏_i D_i`, or a typed source law on a connected graph.
- **Level 1:** observational/model charts and permitted local relation constraints on their common original source, or unitary transports `U_e` along named interactions.
- **Level 2:** the model of model-interactions: exact joins/projections, or pathwise comparison/holonomy of transport operators.
- **Level 3:** the model of the system of *interactions*: recursing exact constraints; composing distinct loop obstructions; synthesizing a **proof-carrying universal invariant or inequality**.

**Key logical restriction:** A consequence of stipulated laws can be new to a bounded observer without being new information about the original source supplied by measurement. An internally generated consequence must not be relabeled as an independent source axiom. This campaign derives BOTH an exact no-free-source theorem and a constructive source-conditional inequality mechanism. Each source label/epoch/basis is a *mathematical assumption*, not a physical attestation.

The existing SUCC parents matter. GMS-01 source-chart factorization is classical and is not re-proved as new. F42 source-typed genetic repairs work inside supplied constructors. NO-GHOST/F48 require event-enabling, source, costs and complete causal interfaces for claims about executable histories. A03/A04 gain-graph holonomy and signed loop obstructions were already in the SUCC atlas. This work **does not claim discovery of relational joins, switching theory, graph connection Laplacians, holonomy, or classical spectral gaps**. The project-specific contribution is a typed, executable **recursive proof interface** and a finite exact **two noncoercive models → jointly coercive meta-model** source experiment.

## 1. Finite relational meta-model

Let `I={1,…,n}`, each `D_i` finite nonempty, and `Ω=∏_i D_i`. Let `S⊆Ω` be a **nonempty, fully declared source relation** (a mathematical specification). A local law is a pair `(J,R_J)` where `∅≠J⊆I` and `R_J⊆∏_{j∈J} D_j`. The law can be `SOURCE_PROJECTION` only when the entire declared source `S` is supplied and `R_J=π_JS`; alternatively it is a `DECLARED_THEORY` axiom. A `MODEL_DERIVED` law records its complete earlier source-indexed parents and its exact consequence. All laws must share source ID, epoch, basis and coordinate semantics, and any law in a source-backed system must contain the projections of every declared original state.

Define the joint **candidate relation** (logical CSP/join, **not** an executed joint experiment)

\[
C(\mathcal L)=\{x\in\Omega:\pi_Jx\in R_J\text{ for every }(J,R_J)\in\mathcal L\}.
\]

For any output scope `K`, define the strongest induced constraint

\[
R_K^{*}(\mathcal L)=\pi_K C(\mathcal L).
\]

### META-01 — strongest exact consequence, conservativity and constructive witnesses (CLASSICAL / PROVED LOCAL)

For every finite family `L` and nonempty output scope `K`:

1. Each candidate satisfies the derived relation `π_K x∈R_K*`.
2. `R_K*` is the **least** relation (under subset inclusion) containing all `K`-shadows of candidates. Thus every other sound `K`-scope consequence contains `R_K*`.
3. Adding `(K,R_K*)` to `L` does not change `C(L)`.
4. Every allowed tuple of `R_K*` has a *full joined witness* `x∈C(L)`. The original-source states survive whenever the parents contain their correct projections.

**Proof.** (1) is the definition of projection. For (2), if every `x∈C(L)` has `π_K x∈R'`, then `π_K C(L)⊆R'`. For (3), each old candidate satisfies the added law; adding constraints can never create new candidates. For (4) projection membership is existential and finite: the machine returns a complete tuple realizing each projected row. A source-backed law contains `S`, so the derived relation also contains `π_K S`. ∎

**Consequence**: The recursion **can** make a genuinely new theorem *visible* to the observer (a constraint absent from any single chart), but does **not** shrink the logically admitted source space unless **new independently justified source information** is introduced. An unexecuted joint Cartesian product is not a source. An empty candidate join is labeled `INCONSISTENT_THEORY`, never a positive empirical observation or proof from nature.

**Nested two-stage exact witness.** The original source is `S={(0,0,0,1),(1,1,1,0)}` with chart coordinates `(A,B,C,D)`. Its three independent binary projections supply models `A=B`, `B=C`, and `C≠D`. Level-2 joining `(AB,BC)` yields the new `AC` relation `A=C`, which neither binary input lists. Level-3 joining **the derived AC model** with `CD` yields `A≠D`. Both derivations return complete joined witnesses. The second constraint *requires* the CD law; omitting it permits all four `AD` pairs. All constraints remain conditional on the admitted mathematical source.

### META-02 — canonical fixed-arity recursion law (CLASSICAL / PROVED LOCAL)

For `1≤k≤n` define the `k`-local model-of-model closure

\[
\operatorname{Cl}_k(S)=\bigcap_{\substack{\varnothing\neq J\subseteq I\\ |J|\le k}}\pi_J^{-1}(\pi_JS),
\]

a subset of `Ω`. Then for all `1≤j,k≤n`:

\[
\boxed{S\subseteq \operatorname{Cl}_k(S),\qquad
 \operatorname{Cl}_k(\operatorname{Cl}_j(S))=\operatorname{Cl}_{\min(k,j)}(S).}
\]

In particular `Cl_k` is extensive, monotone, idempotent, and `Cl_n(S)=S`.

**Proof.** `S⊆Cl_k(S)` by its own projections. If `|J|≤j`, then `π_J Cl_j(S)=π_JS`: inclusion one way follows by the `J`-constraint, and the other from `S⊆Cl_j(S)`. If `k≤j`, replacing `S` by `Cl_j(S)` leaves every `≤k` shadow unchanged, yielding `Cl_k Cl_j(S)=Cl_k(S)`. If `k≥j`, the relation `Cl_j(S)` is already defined by `j`-ary constraints, so its `k`-closure cannot enlarge it; the converse inclusion is extensivity. Monotonicity follows from monotonicity of projection and inverse image. The unique full-coordinate constraint yields `Cl_n(S)=S`. ∎

This is a *precise limitation on repeating the same insight*: **adding arbitrarily many meta-layers that only recombine at arity ≤k cannot distinguish sources that have identical ≤k shadows**. It is not a theorem that arbitrary reasoners are bounded to arity `k`; the bound is a declared toolkit limitation. Higher-arity source laws, independent proof rules or nonlocal structure can escape it.

### META-03 — strict higher-order obstruction (CLASSICAL parity countermodel / EXACT)

For any `n≥2`, let

\[
S_n^{(0)}=\{x\in\{0,1\}^n:\textstyle\sum_i x_i\equiv0\pmod2\},\quad
S_n^{(1)}=\{x:\textstyle\sum_i x_i\equiv1\pmod2\}.
\]

Both nonempty disjoint relations have **identical full projections on every proper nonempty coordinate subset**, each equal to the full cube on that subset. Indeed, given any partial assignment omitting coordinate `i`, choose the missing bit to force the target parity. Therefore

\[
\boxed{\operatorname{Cl}_{n-1}(S_n^{(0)})=
\operatorname{Cl}_{n-1}(S_n^{(1)})=\{0,1\}^n,\quad
\operatorname{Cl}_{n}(S_n^{(\epsilon)})=S_n^{(\epsilon)}.}
\]

No computation restricted to the complete family of proper-coordinate shadows, no matter how deeply it recursively reorganizes them, can determine which of these two sources is actual. The minimal required interaction arity is **exactly `n`**. This is a source-map/observation-arity barrier, not an undecidability theorem about parity or an assertion that a symbolic observer cannot reason about the parity axiom if the axiom is supplied.

**Hostile crosscheck:** exhaustive testing of every one of the `2^8−1=255` nonempty sources on three binary coordinates confirms the closure identity for all 9 pairs `(j,k)`, against a separately written membership oracle. Parity source pairs with `n=3,…,6` check strictness; `n=5` exposes 16 ghosts at arity 2.

### META-04 — minimal justified repair of one ghost (CLASSICAL / PROVED LOCAL)

If `x∈Cl_k(S)\S`, there exists a separating scope `J` with `|J|>k`, since `J=I` is sufficient and no smaller scope can separate a valid `k`-shadow candidate. Pick a scope of least cardinality with `π_Jx∉π_JS`, append the **exact source** law `π_JS`, and the candidate relation shrinks strictly while containing `S`.

**Proof.** `x` fails the full constraint, so a separating scope exists; choose the minimum among finitely many. Its cardinality exceeds `k` by the definition of `Cl_k`. Addition excludes `x` and every original source survives. At most `|Ω\S|` strict counterexample-guided repairs can occur; a bound on search work or physical feasibility does not follow. ∎

The code refuses to "construct" that new source law without being supplied the *complete* original mathematical source relation. If the observer has only finite actual observations, the required higher-arity relation must be independently proved from a generative source law or obtained by a lawful source-preserving probe. Claiming to have measured it by logical recursion would be a NO-GHOST violation.

### META-05 — pairwise-consistent but globally impossible model system (CLASSICAL contextuality/CSP control)

On three bits, impose `A=B`, `B=C`, `A≠C`. Every pair of laws has at least one satisfying global assignment, and every individual local relation is nonempty. All three jointly have no solution. The exact engine reports `INCONSISTENT_THEORY` rather than declaring any proposition about the physical source. This refutes "pairwise matching model-interactions automatically glue into a lawful global source" and is the minimal parity triangle for the chosen binary language.

## 2. Recursive *transport* interactions: from compatibility to universal inequalities

Pure joins alone cannot manufacture stronger premises, but **lawful algebraic transport** may entail new restrictions on global objects. Here we independently declare transport *maps*, not merely relation shadows. This is a mathematically distinct instrument.

Let `G=(V,E)` be a finite connected graph of model charts. Fix a Hilbert space `H` and give each oriented edge `e:u→v` a unitary `U_e:H→H`, with reverse traversal `U_e^*`. Let each edge have weight `w_e>0`. A global assignment is `x=(x_v)_{v∈V}∈H^V`. Define its interaction energy

\[
\boxed{\mathcal E_G(x)=\sum_{e:u\to v}w_e\|x_v-U_e x_u\|_H^2.}\tag{M6}
\]

Every single local edge model admits exact zero energy (set `x_v=U_e x_u`). A *cycle* can obstruct all those local choices simultaneously. This is standard connection-Laplacian / synchronization mathematics, now equipped with SUCC's source-indexed proof and model-recursion interfaces. The word "phase" is licensed **only here**, because the unitary matrix/sign and edge orientation are explicitly declared common-basis transports. A generic collection of unrelated SUCC charts does not have a phase.

### META-06 — exact cycle-holonomy energy inequality (CLASSICAL / PROVED LOCAL, arbitrary Hilbert H)

For an oriented based simple cycle `C=(v_0→v_1→…→v_m=v_0)`, define its unitary holonomy `H_C=U_{e_m}…U_{e_1}` with reverse edges interpreted by adjoints, and resistance `R_C=Σ_{e∈C}w_e^{-1}`. Then for *every* global assignment:

\[
\boxed{\mathcal E_G(x)\ge
\frac{\|(I-H_C)x_{v_0}\|_H^2}{R_C}.}\tag{M7}
\]

**Proof.** Set the local error `d_j=x_{v_j}-U_{e_j}x_{v_{j-1}}`. Compose and telescope around the cycle:

\[
(I-H_C)x_{v_0}=\sum_{j=1}^{m}U_{e_m}\cdots U_{e_{j+1}}d_j
\]

(with the same absolute value if orientation is reversed). All operators multiplying `d_j` are unitary. Triangle inequality gives `||(I-H_C)x_root||≤Σ_j||d_j||`. Weighted Cauchy–Schwarz gives `(Σ_j||d_j||)^2 ≤ (Σ_jw_j^{-1})(Σ_jw_j||d_j||²)≤R_C E_G(x)`. ∎

**Sharpness with a fixed root and a single cycle:** for a cycle considered alone, any root vector `y` can attain equality by distributing the transported residual vector `(I-H_C)y` proportionally to the inverse weights along edges; solving the linear recurrence around the cycle imposes exactly this one residual sum. For a signed real cycle with product sign `−1` and `y=1`, the sharp minimum energy is `4/R_C`.

**Concrete exact certificate:** the triangle with signs `(+, +, −)` and unit weights has `H_C=−1`, `R_C=3`; fixing `x_A=1` forces `E≥4/3`. Equality is achieved at `(x_A,x_B,x_C)=(1,1/3,−1/3)`, where every edge contributes `4/9`. Its Boolean `±1` version must violate at least one edge, hence Boolean frustration cost is at least 1. An ordinary all-positive triangle has a nonzero zero-energy parallel section, confirming that the cycle sign matters.

### META-07 — source-indexed cycle packing creates global combinatorial lower bounds (CLASSICAL / PROVED LOCAL)

In a signed graph, a frustrated simple cycle `C` (sign product `−1`) must have at least one violated edge under every assignment `x:V→{−1,+1}`. Assign each such cycle an exact rational multiplier `λ_C≥0` satisfying the **edge capacities**

\[
\sum_{C\ni e}\lambda_C\le w_e \quad(\forall e).
\]

Then the total Boolean frustration energy `F(x)=Σ_e w_e 1[x_v≠s_e x_u]` obeys

\[
\boxed{F(x)\ge\sum_C\lambda_C\quad\text{for every Boolean assignment }x.}\tag{M8}
\]

**Proof:** `Σ_{e∈C} 1[violation at e]≥1` by parity frustration. Multiply by `λ_C`, sum cycles, interchange finite sums, and use the edge-capacity bound. ∎

This is a small exact certificate that emits a genuine global **inequality** from *relationships between lower-order interaction models*. Two disjoint frustrated triangles of unit weight yield `F≥2`, independently checked on all `2^6` assignments. It is classical fractional cycle packing, not a discovery of signed-graph optimization theory.

### META-08 — kernel as the common fixed vectors of the meta-holonomy family (CLASSICAL / PROVED LOCAL)

Choose a root `r` and a spanning tree `T`. Let `P_v` be tree-path unitary transport from `r` to `v`. For every non-tree edge `e:u→v`, define the **transported holonomy at one basis** `H_e=P_v^*U_eP_u`. Then:

\[
\boxed{\ker \mathcal E_G\cong\bigcap_{e\notin T}\ker(I-H_e),\qquad
 y\longmapsto(P_v y)_{v\in V}.}\tag{M9}
\]

**Proof.** Since `w_e>0`, zero energy means `x_v=U_ex_u` on every edge. Along the tree, it forces `x_v=P_v y` for one root vector `y`. On a non-tree edge it becomes `P_vy=U_eP_uy`, equivalent to `(I-H_e)y=0`. Conversely every common fixed vector defines a consistent parallel section. ∎

For a fixed finite graph and **finite-dimensional** Hilbert fiber `H`, the quadratic form has a strictly positive global spectral gap iff the common fixed-vector subspace is trivial. This uses finite-dimensional compactness of the unit sphere; in infinite-dimensional H, injectivity of the connection Laplacian does NOT imply coercivity.

**Exact infinite-dimensional negative control:** on `H=ℓ²(Z)`, bilateral shift `U` has no nonzero fixed vector, yet the normalized interval vector `y_N=(2N+1)^−1/2 1_{[-N,N]}` satisfies

\[
\|(I-U)y_N\|^2=\frac{2}{2N+1}\longrightarrow0.
\]

Therefore a meta-model cannot promote `no common fixed vector` to `uniform positive gap` unless it proves the missing spectral/compactness condition.

### META-09 — a *meta-meta* joint-holonomy coercivity theorem (CLASSICAL INGREDIENTS / PROVED LOCAL, general Hilbert H)

Now treat **entire cycle models as the objects** being combined. Choose `m` based cycles `C_j` at the *same declared root and basis*. For each let `H_j` be its unitary holonomy and `R_j=Σ_{e∈C_j}1/w_e`. Fix scalar weights `λ_j≥0` and suppose a **joint** operator inequality is independently proved:

\[
\boxed{G:=\sum_{j=1}^m \lambda_j (I-H_j)^*(I-H_j)\ \succeq\ \delta I_H,\quad\delta>0.}\tag{M10}
\]

Set `R=Σ_j λ_j R_j` and choose ANY spanning tree rooted at `r` with `T_v=Σ_{e \text{ on tree } r→v}w_e^{-1}`. Then for every global state `x∈H^V`:

\[
\boxed{
\mathcal E_G(x)\ \ge\
\frac{\delta}{2|V|R+2\delta\sum_{v\in V}T_v}\ \sum_{v\in V}\|x_v\|^2 .}\tag{M11}
\]

**Proof.** Apply (M7) on each based cycle, multiply by `λ_j` and sum. The cycle energies are each ≤ the full graph energy, so

`δ||x_r||² ≤ Σ λ_j ||(I-H_j)x_r||² ≤ Σ λ_j R_j E_G(x) = R E_G(x)`.

Along the spanning-tree path to `v`, transport errors telescope and the weighted Cauchy–Schwarz estimate gives `||x_v-P_v x_r||² ≤ T_v E_G(x)`. Thus `||x_v||²≤2||x_r||²+2T_vE_G(x)`. Summing over vertices, substituting `||x_r||²≤(R/δ)E_G(x)` and rearranging gives (M11). ∎

The theorem works on **arbitrary Hilbert fibers** assuming an actual operator gap (M10). In dimension two with exact rational orthogonal matrices, (M10) can be proved by checking three principal-minor inequalities, so the entire output is an exact finite *proof object*, not a floating positive spectrum.

### META-10 — decisive two-loop example: neither model coercive, their meta-model is (EXACT SOURCE-CONDITIONAL CERTIFICATE)

Consider a graph with vertices `(R,A,B,C,D)` consisting of **two triangles sharing only root R**. All weights are 1. The first two directed edges of each triangle are identity transports. The closing edges carry

\[
H_1=\begin{pmatrix}1&0\\0&-1\end{pmatrix},\quad
H_2=\begin{pmatrix}-1&0\\0&1\end{pmatrix}.
\]

Each loop separately has a one-dimensional nonzero fixed space and **cannot produce** any positive-definite `(I-H_j)^*(I-H_j)≥δI` with δ>0. At the next recursion level,

\[
\boxed{(I-H_1)^*(I-H_1)+(I-H_2)^*(I-H_2)=4I_2.}
\]

Now each cycle has `R_j=3`, `R=6`, `δ=4`, `|V|=5`. Choose a star spanning tree with four unit-weight edges from the root (two are reverse traversals of the non-identity closing edges), hence `Σ_v T_v=4`. The theorem produces the **exact rational global coercivity certificate**

\[
\boxed{\mathcal E_G(x)\ \ge\ \frac1{23}\sum_{v\in V}\|x_v\|_2^2.}\tag{M12}
\]

Every factor is printed and checked in Fractions, with 256 independent direct-energy assignments used as holdouts. Mutants replacing one reflection by identity, changing source ID/epoch/basis, using nonorthogonal matrices, claiming δ>4, or omitting a based cycle are rejected.

**Why this precisely realizes the maintainer's recursion:** Model 1 and Model 2 each support *some* perfectly compatible global states and are individually unable to force coercivity. Their *systems of interaction models* (cycles) carry **different** fixed directions. The meta-model of these two cycle-models sees the common fixed space collapse from a line to `{0}` and establishes a quantitative global energy law **not derivable from either individual loop premise alone**. This is a real mathematical consequence, NOT extra observational information. It is a source-conditional example, not an RH sign theorem.

An additional exact rational-rotation control uses `U=[[3/5,-4/5],[4/5,3/5]]`: `(I-U)^T(I-U)=4/5 I`, so one nontrivial rotation loop already suffices for a joint-root spectral gap without floating trigonometry.

## 3. The honest obstruction and what must happen next

**No-free-recursion boundary:** recursively regrouping finitely given shadows at unchanged interaction arity is an idempotent semantic closure. It cannot recover a missing `n`-ary parity law, no matter how clever its implementation. To move to new arithmetic truth, SUCC must acquire one of:

1. **New source-backed law** whose extension is independently proved from the actual underlying arithmetic (or physically observed through a certified source-preserving instrument).
2. **New theorem rule** with a soundness proof that transports existing true premises into a stronger *conditional mathematical conclusion* (this campaign's operator path and joint-gap theorems).
3. **New representation with a certified intertwiner** transporting relevant operators/quadratic forms into a space where a new inequality is provable on the *full original domain*.

The second option is **demonstrated here** for declared finite weighted unitary graphs: model-of-model holonomy conditions plus two noncoercive loop sources induce a strictly coercive graph energy. For authentic Weil positivity, it would additionally require a precisely defined diagram `genuine Euler/Gamma/pole source -> lawful unitary transport system -> quadratic form` and a **proved identity** between this graph energy (or a controlled signed difference) and `Q_ζ(v,v)` for all correct test functions, with gamma, half-density, contact, poles and all prime powers. We have *not* constructed that diagram. Fake primitive 6 and a non-Euler control must defeat any source-blind shortcut. No squaring away a signed negative channel.

**Why the operator version is worth keeping:** It creates a reusable, independent analytic lemma factory — provided future researchers can derive the edge transports and a joint holonomy gap from authentic mathematical source laws. The previous generic positive-semantic-covariance shortcut is blocked: the meta-operator does not claim to equal Weil's signed form.

## 4. Controls, reproducibility, provenance

Files on this branch:

- `observational_succ/recursive_meta_succ.py`: exact finite source/model law, strongest-consequence witnesses, exhaustive arity closure, minimal ghost scope, source-indexed signed graph and rational `2×2` orthogonal meta-meta cycle-gap certificates.
- `tests/test_recursive_meta_succ.py`: independent brute Cartesian-source oracle over all 255 nonempty 3-bit relations, strict parity arity controls, two-stage model fusion, inconsistent pairwise gluing, wrong-source/epoch/basis/transport, signed root inequality sharpness, Boolean edge-cycle packing, an ℓ²(Z) no-gap countermodel, and exact two-reflection joint coercivity.
- `scripts/recursive_meta_succ_probe.py` and `research/2026-10-14/RECURSIVE_META_SUCC_RECEIPT.json`: deterministic exact-rational public receipt and byte-exact replay.
- `docs/CLAIM_SUPPLEMENT_RECURSIVE_META_SUCC.md`: stable claim/status/negative-control inventory.
- `.github/workflows/recursive-meta-succ.yml`: 3.10/3.13 focused tests and source-provenance/receipt replay.

**Executed locally** on a separately authored overlay because direct `git clone` was blocked by DNS: `PYTHONPATH=. python -m unittest tests.test_recursive_meta_succ -v` passed all 18 tests on Python 3.13.5. No Lean compiler was installed locally and no Lean kernel proof is claimed. No actual source repo full-suite execution is claimed until CI at the pushed GitHub commit is checked. Math objects were compared against GMS/F48/A03/A04/SUZUKI context from the GitHub connector; imported sources and main were not edited.

### Prior mathematics and independence limits

- Relational projection/join and lossless-join dependencies are classical database / constraint-satisfaction theory; see Fagin's *Multivalued Dependencies and a New Normal Form for Relational Data Bases* and Kenig–Weinberger, [*Quantifying the Loss of Acyclic Join Dependencies*](https://arxiv.org/abs/2210.14572). Our arity closure and parity obstruction are elementary instances of established ideas, not priority claims.
- Signed cycle imbalance, frustration and signed Laplacian inequalities are established: [*Frustration and isoperimetric inequalities for signed graphs*](https://doi.org/10.1016/j.dam.2016.09.015).
- Orthogonal connection Laplacians and higher-order holonomy obstructions are established: Bandeira–Singer–Spielman, [*A Cheeger Inequality for the Graph Connection Laplacian*](https://doi.org/10.1137/120875338); Gao–Brodzki–Mukherjee, [*The Geometry of Synchronization Problems and Learning Group Actions*](https://arxiv.org/abs/1610.09051); and [*Cycle holonomy induces higher-order constraints*](https://arxiv.org/abs/2604.19682). The formulas and two-loop source-specific certificate here are **derived and exact-checked**, but academic novelty of the full abstract result is UNVERIFIED and not asserted.
- Independence is limited: the test oracle was written separately but runs under the same author/process/source specification; the Python script is not a Lean proof and source IDs are not empirical attestations. The full mathematical derivation, signed countermodels and algebraic proof objects carry the claims, not model-provider agreement.

## 5. Three verdict-changing next theorems

**RMS-N1 (algebraic):** Extend exact rational matrix certificates to arbitrary finite-dimensional unitary/orthogonal transports, with verified PSD via fraction-free LDL or exact sum-of-squares and explicit transport of common base. Prove independence of choice of spanning tree (gauge invariance) and discover minimal witnessing holonomy subfamilies / optimal packing weights; compare with literature on connection Laplacians.

**RMS-N2 (categorical causal):** Replace a static edge labeled by a declared map with a **lawfully executable intervention**. Require full source/current/outcome probability kernel, compatible action menus, retained public histories and conditional schedule exchanges. Prove which orthogonal transport diagrams survive NO-GHOST policy descent; destructive-order controls must invalidate false squares. Neither a gluing sheaf nor a unitary transport is automatic from marginal agreement.

**RMS-N3 (arithmetic RH-facing, speculative):** Derive a nontrivial source-specified family of basis-transport/holonomy defects from *authentic* prime jets and the single Archimedean Gamma/pole completion; prove a sign-preserving or quantitatively error-controlled **form identity** with Suzuki's full Weil form over every test in one nontrivial interval. Only after such a source-identified equality can (M11) be offered as an RH-facing inequality. A generic positive graph energy, even with many loops, has no Weil authority.

**Claim ledger:** see supplement. **RH PROVED: NO.**
