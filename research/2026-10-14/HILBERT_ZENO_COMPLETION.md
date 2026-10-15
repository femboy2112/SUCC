# HILBERT–ZENO: source-indexed space-filling observers and compact infinite-dimensional sign calculus

**Research date:** 2026-10-14 US Eastern. **Exact parent:** `femboy2112/SUCC main@03db44203147a7b28d445bb9f970fa71360e78c4`, after the completed Phoenix II merge of PRs #57–#99. **Research branch:** `research/hilbert-curve-cube-zeno-certificates-2026-10-14`. **RH PROVED: NO.** Every theorem has its mathematical premises; no claim of physical Hilbert apparatus, executed infinite history, certified Riemann zero locations, complete Weil sign, or scholarly theorem priority.

## 0. What the author's proposal actually says

The Hilbert **curve**, not an unspecified infinite-dimensional Hilbert-space basis, is a recursively defined finite-grid path whose limiting continuous image is the full square. The suggestion is to use its ordered *finite* approximations as observer SUCC steps so that global geometrical or analytical facts have a source-preserving finite-to-complete interface. It is mathematically productive when coupled to a **known regularity/continuity modulus** and a **named completion space**. A finite Peano path by itself never proves anything about unvisited cells. Even full finite meshes do not license an infinite-dimensional sign theorem without a uniform tail estimate.

We also use the **Hilbert cube** `K` in the Hilbert space `ell²`: unlike the curve, it has infinitely many genuine coordinate axes but is compact due to their summably shrinking sizes. The two constructions have related names but very different mathematical roles. They form a useful *two-axis* proof instrument: (coordinate horizon `d`, grid resolution `n`). Source-specific regularity supplies the error law; the Hilbert path supplies an exact traversal order for the first two finite coordinates. Neither is an RH sign axiom.

The Phoenix II `main` contains 3,350 full-suite tests recorded in `docs/PHOENIX_II_VALIDATION.md`, all 43 PRs #57–#99, `zeno_proof_debt.py`, `suzuki_moment_schur.py`, original signed Suzuki/Weil `source_weil_hierarchy.py`, and the zero-shift Douglas-range obstacle `research/2026-10-14/SUZUKI_SIGNED_TAIL_RESOLVENT_GATE.md`. The current main GitHub CI run `38671475263` is green; this is a software test fact, not proof of the RH-facing lemmas.

## 1. HZ-01 — a complete finite Hilbert traversal (CLASSICAL / PROVED HERE)

For `n>=0` write `N=2^n` and `h_n:{0,...,4^n-1}-> {0,...,N-1}²`. Begin with `h_0(0)=(0,0)`. For `n+1`, let `m=2^n`, and let `(x,y)` be the earlier coordinate. Concatenate four images, preserving the index order inside each block:

```
Q0: (x,y) -> (y,x)
Q1: (x,y) -> (x,y+m)
Q2: (x,y) -> (x+m,y+m)
Q3: (x,y) -> (2m-1-y,m-1-x)
```

**Theorem.** Each `h_n` is a bijection of its finite index set with the whole dyadic cell lattice, and successive indices have Manhattan distance exactly one. Its first point is `(0,0)`, its last `(N-1,0)`.

**Proof.** All four maps are integral isometries into pairwise disjoint `m×m` quadrants. Inductively they each visit their quadrant exactly once with internal unit Manhattan steps. Their block endpoints are `(0,m-1)` to `(0,m)`, `(m-1,m)` to `(m,m)`, and `(2m-1,m)` to `(2m-1,m-1)`, so the connectors also have unit length. Endpoint induction proves the stated orientation. The explicit quadrant inverse recovers each address and is the independently tested `hilbert_index`. QED.

### HZ-01B — actual source-preserving inverse-limit completion from a base-4 observer address (CLASSICAL / PROVED HERE)

There is an even sharper result than having a Hamiltonian ordering. **Every parent Hilbert cell with order-n index `i` has its four geometric dyadic children at EXACTLY the order-(n+1) indices `4i,4i+1,4i+2,4i+3`, in some orientation.** The proof is by induction on the four quadrant isometries above: the level-(n+1) order groups the four refinements of each previously visited cell into one contiguous block, preserving the parent visitation order. We independently test all dyadic parents through order 4 and compare inverse indexes.

Let the mathematical original source be an **infinite base-4 digit stream** `a=(a_1,a_2,...)∈{0,1,2,3}^N`. Its first `n` digits specify integer index `i_n=sum_(j=1)^n a_j 4^(n-j)`, hence one actual dyadic square cell `C_n(a)` of side `2^-n`. By the exact index-block law, `C_(n+1)(a)⊆C_n(a)`. These are nonempty compact sets with diameters shrinking to zero, so the intersection contains **exactly one** point `h(a)` in `[0,1]^2`. If `p_n` is the center of the source-licensed cell, then

`boxed: ||p_n-h(a)||_infinity <= 2^(-n-1)`.

For two addresses with common first `n` digits, `||h(a)-h(b)||_infinity<=2^-n`. Using the usual prefix ultrametric `d_4(a,b)=4^(-n)` (for the maximal length-n common prefix), this makes `h` **1/2-Hölder as a map from the 4-ary Cantor address space onto the square**. Surjectivity: each point in the square lies in at least one finite dyadic cell at every level; choose a nested dyadic chain of such cells and read their Hilbert indexes, which by the index-block law have compatible base-4 prefixes. The unique intersection is the chosen point. Dyadic boundary points may have several valid addresses; no injective inverse is claimed.

This is an authentic and quantified **finite source prefix -> every mathematically possible completed endpoint** theorem: a length-n address certifies a whole closed cell and an exact Zeno remainder relative to its center, not a physically performed omega-step or an independently observed endpoint. A finite **walk** of 4^n cells and a finite **prefix** of n base-4 digits are different objects; the latter is actually compatible across depths even though the list of cell-center probes is not a literal prefix of the refined list. This is the rigorous version of "origin -> complete at infinity" available to SUCC.

The cell center is `c_(x,y)=((2x+1)/(2N),(2y+1)/(2N))`. A complete grid tour has mathematical `L¹` length

`ell_n=(4^n-1)/2^n=2^n-2^(-n)`.

**Optimality in this finite model:** distinct dyadic cell centers are separated by at least `1/N` in Manhattan distance, so ANY Hamiltonian tour through the `N²` centers has length `>= (N²-1)/N`. The Hilbert path attains this. This is not a universal optimization theorem for arbitrary geometry or an argument that the infinite physical path has finite length; in fact `ell_n -> infinity`. Nor is the query sequence at depth `n` literally a prefix of the sequence at depth `n+1`: finite approximations refine their source cells and must be treated as different mathematical schedules.

## 2. HZ-02 — finite Hilbert-Zeno Lipschitz certificate (CLASSICAL / PROVED HERE)

Let `f:[0,1]² -> R` satisfy the **source-proved all-pairs law**

`|f(x)-f(y)| <= L(|x1-y1|+|x2-y2|)` with `L>=0`.

For the complete order-`n` Hilbert samples `v_i=f(c_(h_n(i)))`, every `x` lies in one dyadic cell whose center `c` satisfies `||x-c||_1 <=1/N`. Consequently

`min_i v_i - L/N <= inf_[0,1]² f <= min_i v_i`,

`max_i v_i <= sup_[0,1]² f <= max_i v_i + L/N`.                         (HZ-2)

For rational polynomial `f(x,y)=sum_(i,j) c_ij x^i y^j`, the implementation *derives* a valid `L` from its exact coefficients: `L=max(sum |c_ij|i,sum |c_ij|j)` on `[0,1]²` by the fundamental theorem of calculus. For a smaller subcell, derivative bounds use powers of its **upper right corner**; monomials are nonnegative on the stated domain. Thus the finite engine does not turn fitted finite samples into an unproved Lipschitz assumption.

A negative sampled value is a finite exact source counterexample. If `min v_i - L/N>=0`, the **global** scalar target is nonnegative on the full square; if the interval crosses zero, the verdict is `UNRESOLVED`, not a claimed proof. The adaptive quadtree recursively subdivides exactly the unresolved cells, visiting each set of children in its actual Hilbert order. Its final leaves cover the source square; a `GLOBAL_NONNEGATIVE` outcome requires nonnegative lower bounds on **all** leaves. Resource exhaustion is a separate result.

### Sharp failure when the source modulus is absent (HZ-03)

If strictly fewer than `N²` distinct Hilbert cells are sampled, some cell is unvisited. For its center `c` and radius `r=1/(2N)`, define

`g_c(x)=-max(0,r-||x-c||_infinity)`.

This function is 1-Lipschitz for the `L∞` and `L¹` metrics, zero at all OTHER cell centers, and `g_c(c)=-r<0`. An observer lacking the remaining cell cannot certify nonnegativity even with that global Lipschitz law at depth `n`. Moreover, for ANY finite point sample set `{p_i}`, the finite polynomial `-prod_i ||x-p_i||²` is zero at all samples and negative elsewhere; with no uniform degree/Lipschitz law there is no finite-sampling global sign inference at all. This is the classical information lower bound specialized to the actual SUCC scan.

## 3. HZ-04 — the weighted Hilbert cube is a genuinely compact infinite-dimensional carrier

Let `H` be a separable real Hilbert space with an **actual chosen orthonormal basis** `e_j`, `j>=1`, and define

`K = {sum_(j>=1) 2^(-j) t_j e_j : -1<=t_j<=1}`.

The sum converges absolutely in norm, since `sum_j 4^(-j)=1/3`. Every `x∈K` has `||x||<=1/sqrt3`, and its tail satisfies

`||x-P_d x||² <= sum_(j>d)4^(-j)=4^(-d)/3`.                  (HZ-4)

**Compactness.** Every finite head is contained in a compact Euclidean cube. The uniform tail bound makes `K` totally bounded: approximate every point by finitely many head-grid points within any fixed epsilon. `K` is closed by coordinatewise bounds and dominated convergence for its tails, hence complete. Thus `K` is compact in the Hilbert norm (not just abstract product topology). This is a standard weighted Hilbert-cube construction. It has empty interior in infinite-dimensional H but spans a dense subspace.

**Global sign equivalence (HZ-05).** For bounded self-adjoint `A:H->H`, put `q_A(x)=<Ax,x>`. Then

`A>=0 on H  <=>  q_A(x)>=0 for every x∈K  <=>  inf_K q_A=0`.      (HZ-5)

Proof: the forward implications and `0∈K` are immediate. If `q_A>=0` on `K`, take any finite-support vector `v` in the chosen basis. There exists a positive scalar `c` with `cv∈K` (choose `c<=min_(j in supp v)2^(-j)/|v_j|`). Homogeneity gives `q_A(v)=q_A(cv)/c²>=0`. Finite-support vectors are norm-dense and the quadratic form is norm-continuous because `A` is bounded, so `q_A>=0` on all H. QED.

This is a compact sign-*equivalence*, NOT a finite positivity certificate: deciding whether the attained compact minimum is **exactly zero**, as opposed to a very small negative number, is generally still hard/undecidable over arbitrary computable sources. The true `K` has infinite Hausdorff dimension in the Hilbert metric because it contains a fixed nondegenerate Euclidean `d`-cube for every `d`.

### HZ-06 — a valid interval fills the Hilbert cube, but never with uniform positive Hölder exponent

The Hilbert cube is a compact, connected, locally connected metric space, hence a continuous image of `[0,1]` by the classical Hahn–Mazurkiewicz theorem. However, if `F:[0,1]->K` were surjective and `alpha`-Hölder for any `alpha>0`, its image would have Hausdorff dimension at most `1/alpha`, contradicting the previous infinite-dimensional subcubes. Equivalently, take any integer `d>1/alpha` and project the supposed image onto the first `d` axes: this would be an `alpha`-Hölder surjection from an interval to a Euclidean `d`-box, whose `d`-volume must be zero by a `k`-interval covering argument (`k` balls of radius `O(k^-alpha)` cover volume `O(k^(1-alpha*d)) -> 0`). Contradiction.

The executable helper `holder_no_go_dimension(alpha)` produces that finite `d` from an exact positive rational exponent. The theorem refutes an **all-dimensional Hölder-uniform** Zeno-time shortcut; it does NOT rule out continuous space-filling maps with weaker moduli of continuity, and it does NOT assert any actual infinite physical traversal.

## 4. HZ-07 — a quantitative *two-axis* Hilbert–Zeno theorem for bounded quadratic forms

Let `A=A*` on H be bounded with a **source-certified** `||A||<=M`. For `d>=1`, `n>=0`, `N=2^n`, define the exact dyadic-center grid

`G_(d,n)={sum_(j=1)^d 2^(-j) [-1+(2k_j+1)/N] e_j : 0<=k_j<N}`.

The grid has `N^d=2^(n*d)` points. For `d>=2`, the first two index coordinates are visited by the actual finite Hilbert order; the other coordinates form a Cartesian product. No unproved `d`-dimensional Hilbert adjacency is claimed.

For any `x∈K`, round the first `d` coordinates to the nearest grid midpoint and set the tail to 0, obtaining `g∈G_(d,n)`. The head error satisfies `||P_d x-g||²<=N^-2/3`; the tail satisfies `||(I-P_d)x||²<=4^-d/3`. Therefore, using triangle inequality,

`||x-g|| <= (N^-1+2^-d)/sqrt3`.

Since `||x||,||g||<=1/sqrt3`, boundedness of A and polarization give

`|q_A(x)-q_A(g)| <= ||A|| (||x||+||g||)||x-g||`

`<= delta_(d,n) := (2M/3)(2^-d+2^-n)`.                    (HZ-7)

Define `m_(d,n)=min_(g∈G_(d,n)) q_A(g)` and `m_K=min_(x∈K)q_A(x)`. Then

`boxed: m_(d,n)-delta_(d,n) <= m_K <= m_(d,n)`.

As both `d,n -> infinity`, `delta_(d,n)->0`; this is an **effective two-axis approximation of a compact infinite-dimensional minimum**, provided the matrix values and M are themselves source-certified. Finite dyadic CENTER grids at successive resolutions are not literally nested; monotonicity of `m_(d,n)` is NOT assumed. A path visits each finite stage, not an executed omega-stage.

### HZ-08 — rigorous independent debt for inexact matrix coefficients

Suppose we know only a rational symmetric `d×d` matrix `Ahat` with a justified entrywise error bound `|<Ae_i,e_j>-Ahat_ij|<=eta`. Every grid `g` has `sum_(i<=d)|g_i|<=sum_(i<=d)2^-i=1-2^-d`; hence

`|q_A(g)-g^T Ahat g| <= eta (1-2^-d)^2 =: E_(d,eta)`.

With `mhat=min_(g∈G)g^T Ahat g`, the complete conditional interval is

`boxed: mhat - E_(d,eta) - delta_(d,n) <= m_K <= mhat + E_(d,eta)`.

A certified negative *upper* endpoint proves an authentic negative Rayleigh witness once the source identification and errors are independently established. A positive finite scan, even a very dense one, **does not** prove global PSD: `0∈K` forces `m_K<=0`. The engine refuses to promote `PARTIAL_SOURCE` into `FULL_FINITE_RANK`; the latter is a separate global source law with an exact rational operator-norm bound. In the full-finite-rank case row-sum domination establishes `||A||<=max_i sum_j|A_ij|` without numerical eigensolvers.

### HZ-09 — a sharp source-blind counterexample to positivity promotion

Fix any examined depth `d` and choose `N>d`. Let `A+=0`, `A-=-|e_N><e_N|`. Their entire first `d×d` source matrix, all Hilbert grid reports at that depth and even their norms' coarse certified upper bounds can agree. Yet `A+>=0` while `q_A-(2^-N e_N)=-4^-N<0`. The negative direction is found at sufficiently deep `N` with a finite rational witness, but no bounded finite `d` can guarantee the absence of all higher negative coordinates. This is exactly SUCC's source-typed sign-debt obstruction, not a fabricated nontrivial zero of zeta.

**Effective horizon & resource law:** choosing `d=n=k` yields mathematical residual `delta<=(4M/3)2^-k` with `2^(k²)` grid evaluations. The exact rational scheduler `hilbert_cube_horizon(M,epsilon)` finds the first symmetric k with certified error <= epsilon, reports `2^(k²)` evaluations, and explicitly refuses a resource cap without declaring the mathematical theorem false. For `M=1, epsilon=1/3`, k=2 costs 16 evaluations. For `M=1, epsilon=1/8`, the first k=4 already costs 2^16=65,536; a 1,000-sample budget must fail, though mathematical convergence is proved. The Hilbert curve minimizes the walk length of the *first two axes at one finite resolution*, not the number of independent infinite-dimensional coordinates or the exponential sample count. With `n` fixed and `d->infinity`, the spatial debt remains; with `d` fixed and `n->infinity`, the coordinate-tail debt remains. The two limits must BOTH be controlled.

## 5. HZ-10 — an actual SUCC source anchor and the missing signed identification

The current main file `observational_succ/suzuki_moment_schur.py` (integrated from PR #96) constructs the **authentic original source's Neumann integration metric** `K=V*V`, not the signed Suzuki operator G. In the first two unnormalized mean-zero Legendre modes `P1,P2`, `a=1/2`, its exact matrix is

`K_raw = [[1/30, 0],[0, 1/210]]`.

In the **normalized L² Legendre basis**, it is

`K_normalized = [[1/10, 0],[0, 1/42]]`.

The new module derives both independently from the classical Legendre primitive formula and the existing module's exact block (`low_inverse_neumann(a,2)`), and the dedicated CI compares them to the real integrated code. Importantly, the source's full K has low/high cross terms (rank two at the 30-mode cutoff), and these two rows are **not** an identification of its whole operator. In particular, positive K is not the original completed Weil signed G, and it cannot be promoted into a proof of RH or a positivity witness for G.

For the actual first-prime Suzuki/Weil H¹ form, choose a complete *real orthonormal basis* of its **form Hilbert space**, e.g. the normalized mean-zero Legendre coordinates under the SUCC `D:v->iv'` isometry. Source-identify the real signed Riesz operator `G_a` and establish the full operator-norm budget M (Suzuki's compact signed screw operator and its H¹ analogue are already present in the merged repo). Then HZ-05 implies

`Q_W>=0 on whole H¹_0(-a,a) <=> inf_(x∈K_a) <G_a x,x>=0`.

**Exact RH-equivalent reformulation, not a proof (HZ-10B).** Assuming the already-imported classical completed-Weil criterion and SUCC's verified signed source operator identification, for each positive *rational* radius `a` choose a complete real Hilbert basis of `L²_0(-a,a)` and its compact weighted cube `K_a`. Define `m_a=min_(u∈K_a)<G_a u,u>`. The operator form is real symmetric, and its complex extension has the usual compatible Hermitian reality condition. By HZ-05, `m_a=0` iff `G_a>=0` on the entire real mean-zero Hilbert carrier. Any compact real or complex test lies in a rationally wider interval; for a real-symmetric source form complex positivity follows by splitting real and imaginary parts. Therefore the mathematical equivalence is

`boxed: RH <=> for EVERY rational a>0, m_a = 0.`

For every such a, the two-index mesh gives `mhat_(a,d,n)-eta_(d)-delta_(a,d,n) <= m_a <= mhat_(a,d,n)+eta_(d)`, provided a real source-norm budget and certified signed matrix values exist. This converts the criterion into a compact *zero-minimum* problem; **it does not supply the sign**, nor does it provide a uniform finite stage at which equality to 0 is decidable. A false RH world would admit a finite strict negative source witness after sufficient approximation; the true positive case remains an all-scales claim. The original 30-mode zero-shift source Schur criterion may give a more economical structural proof route than an exhaustive Hilbert cube grid.

An exact source-authenticated matrix + rigorously justified δ,η gives a useful two-axis *negative-witness semidecision* and quantitative finite shadow. It is an **equivalent reformulation**, not an RH proof: no finite collection of zero-adjacent interval enclosures proves that the true compact minimum equals 0. The legitimate remaining gate is PR #99's **zero-shift Douglas-range / shorted finite matrix** (and the source-specific signed coupling), NOT source-blind space filling or ad hoc scalar covariance. One must also independently verify extension from real to complex tests via the genuine real-symmetric source kernel; never assume it for an unrelated complex form.

## 6. Honest evaluation and next falsification

**What this round genuinely adds to SUCC:** nested exact base-4 Hilbert-address completion with a quantitative 1/2-Hölder Zeno modulus; exact finite Hilbert coding with reversible coordinates; full-source polynomial certificates with actual rational Lipschitz modulus; an adaptive finite mathematical observer with sound local-to-global pruning; a quantitative two-axis compact Hilbert-cube extrema theorem; a source-type hierarchy and hostile invisible-rank-one tests; an actual connection to the integrated Legendre K source. The underlying math is classical or elementary derived, and academic originality is **UNVERIFIED**.

**What is still missing:** original signed `G_a` matrix entries (with rigorous enclosures), a provably global M for the chosen Hilbert form topology, certified zero-shift cross-resolvent bounds in the true 30-moment split, and uniform sign. Space-filling alone never supplies these. The attached `docs/HILBERT_ZENO_ROADMAP.md` prioritizes that work.

**Falsification menu:** wrong prime source/epoch/basis; all-grid versus partially visited; false regularity from samples; hidden negative cell and hidden e_N direction; non-Hilbert domain/incorrect K normalization; inexact matrix entry laundering; half-density/Gamma/pole/contact mutation if constructing the actual signed source. No zeta zeros are used in any current test.

### Source and prior mathematics

- SUCC `main@03db442`, `docs/PHOENIX_II_INTEGRATION_AUDIT_2026-10-14.md`, `docs/PHOENIX_II_VALIDATION.md`, `research/2026-10-14/ZENO_PROOF_DEBT_MACHINE.md`, `research/2026-10-14/SUZUKI_SIGNED_TAIL_RESOLVENT_GATE.md`, `research/2026-10-14/SUZUKI_CANONICAL_MOMENT_SCHUR.md`.
- David Hilbert, *Ueber die stetige Abbildung einer Linie auf ein Flächenstück* (1891). Classical finite Hilbert curve and inverse indexing explained independently by J. Burkardt: https://people.math.sc.edu/burkardt/m_src/hilbert_curve/hilbert_curve.html (the code here is an independently written quadrant recursion, not copied implementation).
- Hahn–Mazurkiewicz theorem; survey in *Continuous images of linearly ordered continua and compacta*, Topology and its Applications 195 (2015), https://doi.org/10.1016/j.topol.2015.09.029 .
- Hilbert cube as a compact convex subset of Hilbert space: standard infinite-dimensional topology; the basis-tower and sign arguments are elementary.
- Existing finite-to-global Zeno and compact negative-depth proofs within SUCC; do not claim the same result twice with a new name.

**Proof-authority summary:** HZ-01 (including HZ-01B)–09 paper-proved within stated mathematical assumptions; HZ-10 source-metric finite algebra proved and software-crosschecked, all-signed-Weil mapping remains conditional. All executable tests are finite checks of formulas and guards, not proofs of an infinitely quantified analytic theorem. **RH PROVED: NO.**
