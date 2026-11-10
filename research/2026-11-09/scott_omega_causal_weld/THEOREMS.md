# Source-faithful causal completion: theorems, proofs, and boundaries

All variables below are mathematical; no numerical π oracle is used.

## CW-01 — literal one-object CCC collapse (DISCLOSED, classical)

A one-object category `BM` is Cartesian closed only if its unique object is terminal. This forces `Hom(*,*)={id}`, hence `M` is the trivial monoid. The faithful repair is a **C-monoid** (a particular algebraic structure, not merely an affine monoid). Theorem 16.1 of Lambek–Scott, attributed to Dana Scott, says `Kar(M)` is a CCC when `M` is a genuine C-monoid: objects are idempotents `e²=e`; arrows `a:e→f` satisfy `fae=a`; composition is monoid multiplication. The original one-object category embeds fully faithfully as the object `1`.

**Set cardinality firewall:** A nontrivial ordinary set `U` cannot satisfy `U^U ≅ U`: for `|U|≥2`, Cantor gives `|U^U|≥2^|U|>|U|`. So do not pretend a finite transformation monoid, an affine monoid, or ordinary `End_Set(U)` is automatically a C-monoid. A semantic realization must be an appropriate reflexive/domain-theoretic or syntactic model, with its own proof of soundness and the required structure.

## CW-02 — Ω expansion is computational growth, not dimensionality (DISCLOSED)

Let `ω_k=λx. x x ... x` with `k` left-associated copies, `Ω_k=ω_kω_k`, and let `E_k(m)` be the left-associated chain of `m` copies. A leftmost β-contraction of `E_k(m)` (at its leftmost `ω_kω_k`) gives `E_k(m+k−2)`. Thus copy-count changes by exactly `k−2`; in particular, `Ω_3` is unit syntactic SUCC. For k≥3 these are nonterminating terms with **no finite β-normal form**. Do not confuse finite prefix tracing, finite strong normalization of a *separately typed compiler*, or Berarducci's infinitary β⊥ normal form. Conventional Scott `D∞` maps head-unsolvable Ωₖ to bottom, which is too coarse to preserve causal traces.

The ambitious `Ω_{d+2}→d independent directions` compiler is **UNVERIFIED**. A mere one-clock `m→m+d` map supplies one orbit, not `d` independent commuting successor operations.

## CW-03 — exact source functor and rational cone (DISCLOSED)

For every integer `j≥1`, the frozen BBP source is

`r(j)=4/(8j−7)−2/(8j−4)−1/(8j−3)−1/(8j−2)`.

Let `U_0=0`, `U_n=16U_{n−1}+r(n)`. Define `P_L=Σ_{j=1}^L16^{-j}r(j)` and `T_n^(L)=Σ_{j=n+1}^L16^{n-j}r(j)` for `0≤n≤L`. Direct unfolding gives

`U_n=Σ_{j=1}^n16^{n-j}r(j)` and `U_n+T_n^(L)=16^nP_L`.

For every fixed finite horizon L, the chronological source/Green-completed diagram **strictly commutes**:

~~~text
U_n + T_n^(L)      -- times 16 --> U_(n+1) + T_(n+1)^(L)
     ||                                       ||
  16^n P_L        -- times 16 -->           16^(n+1) P_L
~~~

The compatibility is an exact identity for all `0≤n<L` and does not require passing to infinity. The selected seed is the **marked natural section** `U_0=0`; a generic forcing-only functor does not select it.

## CW-04 — explicit nested rational compact intervals (DISCLOSED)

The rational simplification is

`r(j)=(120j²−89j+16)/[(2j−1)(4j−1)(8j−7)(8j−3)]`.

Setting `t=j−1≥0`, numerator, denominator and margin all have positive coefficients:

`A(t+1)=120t²+151t+47`,

`D(t+1)=512t⁴+1024t³+712t²+194t+15`,

`[4D(j)−j²A(j)]_(j=t+1)=1928t⁴+3705t³+2379t²+531t+13`.

Therefore `0<r(j)<4/j²` for all integer `j≥1`, and the geometric series implies for `L≥1`

`0<π/16−P_L = Σ_{j>L}16^{-j}r(j) < B_L := 4 / [15(L+1)²16^L]`.

The equality of the infinite source sum with π/16 is the standard BBP identity already authenticated in SUCC. The **new local derivation** is the explicit nested interval construction, not priority over BBP/Green-tail known identities.

Define `I_(n,L)=[16^n P_L,16^n(P_L+B_L)]`, with `0≤n≤L`. Then `I_(n,L+1)⊊I_(n,L)` for every fixed n and L≥max(1,n). Lower endpoints strictly increase because `r(L+1)>0`. Upper endpoints decrease, since

`B_L−B_(L+1) > (4/[(L+1)²16^(L+1)]) > 16^(-L-1)r(L+1)=P_(L+1)−P_L`.

Both chains are nested nonempty compact intervals and their widths `16^n B_L` tend to zero. Their intersections are the singleton `16^n π/16`.

For every `n<L`, **exact interval naturality** holds: `16 I_(n,L)=I_(n+1,L)`. It survives refinement and the limit. With `q:R→R/Z`, `q(16I)=T(q(I))` exactly for `T[x]=[16x]`.

### Scoped Scott completion

On each compact interval working chart `X` containing all the intervals at a fixed n, take nonempty compact subsets `K(X)` ordered by **reverse inclusion**. Directed joins are filtered intersections (nonempty by compactness). For a continuous map `q:X→S¹`, the direct-image map `q_*:K(X)→K(S¹)` preserves directed joins by compactness of filtered preimage fibers, hence is Scott-continuous. Thus

`q_*(⋂_L I_(n,L))=⋂_L q_*(I_(n,L))={ [16^(n−1)π] }`.

**Important:** Scott continuity guarantees transport of the limit, *not* equality of unrelated limits. The equality above is supplied by the BBP source identity. In a full observation category one must additionally preserve provenance and rewrite operations.

## CW-05 — exact two-computation weld with no finite equality (DISCLOSED)

For every `n≥1`, set `A_n=[1−16^-n,1]`, `B_n=[0,16^-n]`, considered as reverse-inclusion increasing information. Their images in `R/Z` are **different** compact arcs for all finite n,m. The Hausdorff distance of `q(A_n)` and `q(B_m)` in the geodesic circular metric is `max(16^-n,16^-m)>0`. Nevertheless,

`sup_n A_n={1}`, `sup_m B_m={0}`, and `q({1})=q({0})`.

The pair of chains is jointly indexed by `N×N`; a cofinal synchronized schedule can approximate both, even though finite exact equality never occurs. They are identical **as completed circle observations** but distinct **as real lifts** with deck displacement one. A source/carry/winding-sensitive observer must retain this distinction.

## CW-06 — quantitative finite-path Fourier approximation, not cancellation (DISCLOSED)

Let `x_n=16^n π/16`, and `x_(n,L)=16^n P_L`, for `0≤n≤L`. Then

`0<x_n−x_(n,L)<16^nB_L`.

For each integer h, the elementary Lipschitz estimate gives

`| exp(2πihx_n)−exp(2πihx_(n,L))| ≤ 2π|h|16^nB_L`.

For an epoch `[A,2A)` and `L≥2A−1`, the **average** error is at most `2π|h|16^(2A−1) B_L`. Choosing `L=2A` makes this `O_h(A^-2)`.

This certifies a finite rational observation of the *actual* completed orbit at a declared precision. It says **nothing** about whether `A^-1 Σ exp(2πihx_(n,L))` tends to zero. Every source-selected signed cancellation, full hexadecimal normality and the weaker parity-contrast gate remain OPEN.

## CW-07 — higher-dimensional and source-gluing contracts (DISCLOSED / conditional)

- Currying is a genuine CCC law: `Hom(X×Y,H)≅Hom(X,H^Y)`; finite pinbed arrays and function-valued single-index observers encode the same data **if the index and evaluation maps survive**.
- `R²×_R R² ≅ R³` when the shared coordinate maps are the usual projections. This is *fiber-product dimensional gluing*, not the union of two planes and not a literal β-equivalence of `Ω_5`, `Ω_4×Ω_4`.
- `B³\{0} ≅ (0,R)×S²` for the punctured ball; the round sphere has a one-parameter **family of metrics** but is intrinsically 2-dimensional. Do not compress its pointwise two-coordinate data into radius.
- A single CRT clock is a full **group-theoretic** replacement for a product of pairwise coprime cyclic clocks. For `(16,16)` synchronous diagonal scanning covers only 16 of 256 states; an unlicensed one-clock collapse loses Fourier characters.
- `V_p∘S=S^p∘V_p` gives actual affine commuting squares and prime-pair cubes. Iterated arrow categories contain higher **diagrams**, not automatically new higher morphisms. Nontrivial 2/3-cell witnesses need a declared rewrite/polygraph calculus with coherence proofs.

## CW-08 — hostile controls (REFUTED shortcuts)

1. Any two Ωₖ have equal denotation in `D∞` bottom; such an equality contains **zero** information about carrier/source selected digits or geometric dimension.
2. In Set, ordinary self-power prevents a nontrivial `U≅U^U`; the finite transformation monoid proxy is NOT a complete C-monoid.
3. Seeds `0` and `1/16` produce identical later fractional BBP states because their unwrapped state difference is `16^(n-1)` for `n≥1`; the zero seed is not recovered by forgetting time zero.
4. Same-forcing coherent rational wrong seeds from SUCC Main XXII can have completely non-Haar real digits while retaining the same local prime data. Functorial source/quotient completion does not imply Haar equidistribution.
5. The limits `lim_k lim_N` and `lim_N lim_k` may differ; e.g. `1_{N≥k}`. Do not swap computational refinement and orbit-length limits without a **uniform quantitative** estimate.
6. The 16×16 equal-period diagonal CRT scan and de Bruijn(16,2) periodic word both refute finite low-order marginal → full Haar.

## References and verification boundaries

Classical: Lambek–Scott, *Introduction to Higher Order Categorical Logic*, §§15–18 (C-monoid and Karoubi theorem); Berarducci, *Infinite λ-calculus and non-sensible models*, introduction §§1–3 (non-sensible infinitary β⊥ semantics with Ω3); domain-theoretic compact-set filtered intersection; CRT; covering-space winding. Additional modern formal reference: van der Leer–Wullaert–Ahrens (ITP 2025), DOI 10.4230/LIPIcs.ITP.2025.33. These are published results, not SUCC discoveries.

Main XXII canonical π frontier and exact source: `docs/PI_NORMALITY_FRONTIER.md`, `observational_succ/duck_bbp.py`, `observational_succ/selected_orbit.py`, `observational_succ/prime_clock_yoneda.py`, `docs/CATEGORICAL_OBSERVER_ATLAS.md`.

The **scope of new code validation** is ten local exact Python unittest methods, plus the four archived standalone instrument probes. No actual physical experiment, complete higher compiler, proof of π normality, or independent theorem referee is claimed.
