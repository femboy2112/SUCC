# OPERATION WILD ADELIC SUCC — ambient embeddings and arithmetic completion

**Checkpoint:** October 14, 2026. **Child:** `research/wild-adelic-embedding-solenoid-2026-10-14` of `research/arithmetic-meta-weil-boundary-2026-10-14@205ffd020dd2a320eeac70a91a2a2700c969c048` (draft PR #86), itself a child of Recursive Meta-SUCC PR #80. **RH PROVED: NO.** Do not merge. This is a mathematical exploration of *intrinsic model, source-indexed bonding law, and extrinsic embedding*; no real observer, knotting experiment, nontrivial zeta-zero list, or physical space-time energy measurement is constructed.

## 0. Hypothesis, repairs, and the three different senses of wildness

The user proposes: what globally presents as a sphere may, from a finite observer's local projection, be an infinitely intertwined embedding. This has a sharp mathematical counterpart in **J. W. Alexander's horned sphere**: a subset of `S^3` intrinsically homeomorphic to `S^2`, but whose exterior component has nontrivial fundamental group, unlike a standard tame sphere. Alexander, *An Example of a Simply Connected Surface Bounding a Region which is not Simply Connected*, PNAS 10 (1924), pp. 8–10. It is an **extrinsic** difference, not an intrinsic sphere genus or a new dimension. Nonlocal flatness lies at a Cantor set in the standard construction. The analytic source cannot be inferred from the picture.

Do **not** identify the following without a proof:

- **Alexander wild `S^2`:** intrinsically `S^2` and extrinsically wild; topology of the ambient complement distinguishes the embeddings.
- **Solenoid `Σ`:** intrinsically already unlike a circle (compact connected, not locally connected when infinitely many covering degrees exceed 1). Its inverse-system stages are circles; it is **not** a wild `S^2`, though standard embeddings into `S^3` are wild continua.
- **Analytic Weil/Suzuki data:** a particular *signed functional* assembled from genuine prime powers, one Archimedean Gamma, poles, half-density, and the contact term. Neither of the preceding topological objects is thereby identified with that signed form.

The mathematically productive higher recursion is:

`declared source -> stage model -> source-indexed bonding morphisms -> intrinsic limit + ambient embedding contract -> certified invariant -> optional transport into another source-matched theory`.

The new datum versus PR #80 is **ambient embedding / peripheral linking**, which is neither a model's abstract isomorphism class nor a mere pairwise relational join.

## 1. Source-typed arithmetic covering tower

Let `q_n >= 2` for every `n>=1`, let `D_0=1`, and `D_n=∏_{i=1}^n q_i`. Treat the whole infinite degree sequence as a **declared generative mathematical source law**, not as measurements of infinitely many stages.

Let

\[
\Sigma_q=\{(z_0,z_1,\ldots)\in (S^1)^{\mathbb N_0}: z_{n-1}=z_n^{q_n}\ \forall n\ge1\};
\quad G_q=\bigcup_{n\ge0}D_n^{-1}\mathbb Z\ \subset\mathbb Q.
\tag{WA-1}
\]

Stage circle `n` has fundamental group `Z`. Pullback on `H¹(S¹,Z)=Z` by `z↦z^{q_n}` multiplies by `q_n`. Under the standard continuity theorem for Čech cohomology of inverse limits of compact Hausdorff spaces with surjective maps,

\[
\boxed{\check H^1(\Sigma_q;\mathbb Z)\cong\operatorname{colim}(\mathbb Z,\times q_n)\cong G_q.}\tag{WA-2}
\]

**Proof of the second isomorphism:** represent an element of the direct limit by `[n,k]`; map it to `k/D_n`. An expansion to level `m>=n` replaces `k` by `(D_m/D_n)k`, leaving the rational invariant. Conversely equal fractions become identical at a common higher level. Thus this is an exact isomorphism. The first isomorphism imports a classical topological continuity theorem, not a finite Python claim. Dually, Pontryagin duality gives `Σ_q ≅ \hat G_q` as compact abelian groups. The code checks the first-to-last rational transport at each finite stage; it does NOT formalize Čech continuity or Pontryagin duality.

The finite observer's `D_n` is a genuine modular clock, including the fiber of `π_0:Σ_q→S¹`: at stage `n`, a point over `z_0=1` has the form `z_n=exp(2πi r_n/D_n)` with compatible `r_n mod D_n`. The fiber is the **profinite limit** `K_q=lim Z/D_n Z` and need not be the complete profinite integers unless the degrees are cofinal under divisibility. The dense real orbit

\[
\iota(t)=(e^{2\pi it/D_n})_{n\ge0}
\tag{WA-3}
\]

is source-defined and satisfies `π_0∘iota(t)=e^{2πit}`. It is injective when `D_n→∞`; its image is dense, by separating characters `k/D_n`.

## 2. Prime-by-prime globalization: invertibility theorem (WA-04)

For `m∈Z_{>0}`, define the coordinatewise finite-stage operation

\[
A_m:\Sigma_q\to\Sigma_q,\qquad(A_m z)_n=z_n^m.
\]

At **every individual circle stage**, this is a non-injective `m`-fold covering when `m>1`. Nevertheless,

\[
\boxed{A_m\text{ is a homeomorphism of }\Sigma_q
\iff \forall p\mid m:\lim_{n\to\infty}v_p(D_n)=\infty.}\tag{WA-4}
\]

**Proof:** Under Pontryagin duality, the dual map is multiplication `m:G_q→G_q`. The group `G_q` is torsion-free, so multiplication is injective; `A_m` is always surjective. It is an automorphism precisely when `mG_q=G_q`. If some `p|m` has bounded valuation in all `D_n`, `1/p^{r}` with sufficiently large `r` cannot lie in `G_q`, so `mG_q!=G_q`. Conversely unbounded `p`-valuation for each `p|m` means for every fixed `n`, a later `D_k/D_n` is divisible by `m`, so every `a/D_n` is `m` times an element of `G_q`. Compact-Hausdorff continuous bijection then yields a homeomorphism. In fact

\[
|\ker A_m|=[G_q:mG_q]
=\prod_{\substack{p\mid m\\\sup_n v_p(D_n)<\infty}}p^{v_p(m)}.
\tag{WA-5}
\]

The displayed finite index follows by factoring `m` and reducing the direct-limit cyclic presentations modulo `m`; primes occurring with unbounded valuation disappear from the quotient, while a bounded-valuation prime contributes its full `p^{v_p(m)}` factor. This is an arithmetic structure theorem, **not** authentication of primitive Euler place weights: degree 6 is allowed as a topological covering, but 6 cannot be used as a genuine primitive prime jet.

### A constructive inverse *from deeper finite-stage data*

When WA-4 holds, given the first `k` compatible phase coordinates `z_0,...,z_k` and any requested output level `n<=k`, choose `k>=n` such that `m | D_k/D_n`. Then the unique preimage `y=A_m^{-1}z` satisfies

\[
\boxed{y_n=z_k^{D_k/(mD_n)}.}\tag{WA-6}
\]

This exponent is an integer. It is compatible across different sufficiently deep `k` because the bonding maps say `z_j=z_k^{D_k/D_j}`; applying `A_m` returns `z_n`. **Uniqueness:** if `A_m(y)=z`, the same formula follows by substituting `z_k=y_k^m`, so an arbitrary choice of an `m`-th root at the original finite stage is NOT a legal global inverse.

The operation has a source-specific *inversion depth cost* `d(n,m)=min{k−n:m | D_k/D_n}`. The code calculates it and rejects forged coordinates, wrong source/epoch, and noninvertible attempts. For a `p`-solenoid (`q_i=p`), WA-6 simplifies to `y_n=z_{n+1}` for `m=p`. An entire finite stage has `p` possible roots, but the next stage selects the one compatible with the global source.

## 3. The factorial SUCC proto-ladder is the universal additive adelic solenoid

Choose `q_n=n+1`: its degree is the *ordinary additive SUCC counter advanced one rung*, and `D_n=(n+1)!`. Every positive integer divides some `D_n`, so

\[
\boxed{G_!=\bigcup_{n\ge0}\frac1{(n+1)!}\mathbb Z=\mathbb Q,\quad
\Sigma_!\cong\widehat{\mathbb Q},\quad
K_!\cong\widehat{\mathbb Z}.}\tag{WA-7}
\]

By the canonical additive-character form of Pontryagin duality for the adeles, `\hat Q` is abstractly the compact **additive** adele class group `\mathbb A_{\mathbb Q}/\mathbb Q`. One concrete model is

\[
\boxed{\Sigma_!\cong(\mathbb R\times\widehat{\mathbb Z})/
\{(n,-n):n\in\mathbb Z\}.}\tag{WA-8}
\]

Here `(x,a)` maps to the circle sequence `z_n=exp(2πi(x+a_n)/D_n)`, where `a_n` is the residue of the profinite integer `a` modulo `D_n`; the quotient relation `(x+n,a−n)~(x,a)` makes this well defined. One real coordinate plus every compatible finite clock share a single global source. **This is the additive place space, not the multiplicative idele class group and not the signed Weil form.** Analytic number theory requires additional Mellin/idele/trace, pole and Gamma identifications; PRs #71–#76 retain that debt.

The short exact sequence of topological groups

\[
0\longrightarrow\widehat{\mathbb Z}
\longrightarrow\Sigma_!\xrightarrow{\pi_0}S^1\longrightarrow0
\tag{WA-9}
\]

exhibits an exact compensating obstruction under multiplication by `m`.

### WA-10 — the Archimedean–profinite cancellation square (PROVED from WA-8)

For all `m>=2`, multiplication `m` on `\hat Z` is injective but has cokernel `\hat Z/m\hat Z ≅ Z/mZ`; multiplication `m` on `S¹` has kernel `μ_m`; and multiplication `m` on the full `Σ_!` is a homeomorphism by WA-4. The connecting homomorphism in the snake-lemma sequence is

\[
\boxed{\delta_m:\mu_m\xrightarrow{\sim}\widehat Z/m\widehat Z,
\qquad \delta_m(e^{2\pi i r/m})=r\bmod m.}\tag{WA-10}
\]

**Direct proof (fixing the sign convention):** lift `e^{2πir/m}` through `π_0` via `iota(r/m)=[(r/m,0)]`. Multiplication by `m` gives `iota(r)=[(r,0)]=[(0,r)]` using the specified *anti-diagonal* quotient, so the fiber residue is `r mod m`. This is bijective. It is a precise instance of one local model's apparent obstruction being canceled by a higher-order global interaction, not an undefined 'superconducting infinity'.

**Important warning:** Restricting multiplication `m` to the profinite fiber is generally *not* an automorphism, although `A_m` is an automorphism on the whole solenoid. Its inverse may change the `S¹` coordinate. This is why **the pair of models matters**: neither isolated quotient records the global inverse.

The affine SUCC/FUCC source relation also survives exactly: for `m>=1`, `t∈R`, and `\tau_t(z)=\iota(t)z`,

\[
A_m\tau_t=\tau_{mt}A_m.
\tag{WA-11}
\]

On the entire solenoid this is a lawful commutation-with-rescaling square, not a nontrivial unitarily frustrated holonomy. Composite `m=6` satisfies WA-11 as a generic covering action and is again NOT an Euler primitive.

## 4. Ambient embedding: where Alexander's warning becomes operational

The abstract space `Σ_q` does **not** include an embedding into 3-space. If an external source supplies a standard nested sequence of *unknotted* solid tori `T_0⊃T_1⊃...⊂S³`, where the core of `T_n` winds with positive degree `q_n` inside `T_{n-1}`, and `Σ=∩T_n`, the complements `Y_n=S³\T_n` form increasing open sets with `π_1(Y_n)≅Z`. The inclusions induce `Z --×q_n--> Z` on meridians. Consequently,

\[
\boxed{\pi_1(S³\setminus\Sigma)\cong\operatorname{colim}(\mathbb Z,\times q_n)
\cong G_q.}\tag{WA-12}
\]

The first-stage exterior facts and inclusion maps are classical geometric knot theory, specifically Conner–Meilstrup–Repovš, *The geometry and fundamental groups of solenoid complements*, J. Knot Theory Ramifications 24 (2015), 1550069, §3. The second equality is our exact rational direct-limit certificate. The first equality uses `S³\Σ=∪Y_n` and continuity of `π_1` under increasing **open** unions: any fixed loop or nullhomotopy has compact image and therefore lies inside some finite stage. No mathematical assertion about a genuine ambient embedded torus is inferred from integer code alone.

Combining WA-2, WA-4 and WA-12 yields the **source-and-embedding-conditioned global bridge**:

\[
\boxed{
A_p\text{ an automorphism of }\Sigma_q
\iff p\check H^1(\Sigma_q;Z)=\check H^1(\Sigma_q;Z)
\iff p\pi_1(S³\setminus\Sigma)=\pi_1(S³\setminus\Sigma)
\iff v_p(D_n)\to\infty.}
\tag{WA-13}
\]

The middle equivalence requires the **unknotted-stage embedding contract** and the identification of the (here abelian) exterior group. If the same abstract solenoid is embedded with knotted stage geometry, the complement may have a **nonabelian** group: Conner–Meilstrup–Repovš construct such embeddings, and even uncountably many inequivalent complements. Thus the intrinsic tower does not determine its ambient complement. This is the mathematically exact 'embedding is a new layer of model' obstruction.

**Controls:** `q_n=2` yields `G_q=Z[1/2]`: `A_2` invertible, `A_3` not; factorial `q_n=n+1` yields `G=Q` and every integer `A_m` invertible; enumerating each prime **once** yields a different `G` (squarefree denominator in reduced form) and no prime `A_p` invertible. A tail of 2s and a tail of 3s can share *any prescribed finite prefix*, yet only one makes `A_2` invertible. This property is not finite-stage continuous in the space of arbitrary covering-degree tapes; a symbolic generator law can prove it finitely.

## 5. Alexander's horned sphere forces an ambient-conditioning obstruction

### WA-14 — compact bi-equicontinuity implies tameness (GENERAL PROVED THEOREM)

Fix the round `S²⊂S³` and a compact metric `d` on `S³`. Let `H_n:S³→S³` be ambient homeomorphisms and let the compact sets `H_n(S²)` converge in Hausdorff distance to `K⊂S³`. Suppose both `(H_n)` and `(H_n^{-1})` are **uniformly equicontinuous**. Then `K=H(S²)` for some ambient homeomorphism `H:S³→S³`; consequently `K` is tame (ambiently equivalent to the round sphere).

**Proof.** Arzelà–Ascoli on compact `S³` supplies a subsequence `H_{n_j}` converging uniformly to a continuous `H`. Equicontinuity of the inverses supplies a further subsequence with `H_{n_j}^{-1}→G` uniformly. For every `x∈S³`,

`H(G(x))=lim H_{n_j}(H_{n_j}^{-1}(x))=x`, and similarly `G(H(x))=x`.

The limit compositions are justified by uniform convergence on compact spaces and continuity/uniform continuity of the limit maps. Hence `H` is an ambient homeomorphism with inverse `G`. Uniform convergence implies `H_{n_j}(S²)→H(S²)` in Hausdorff distance, which must equal `K` by uniqueness of metric-space limits. QED.

**Wild corollary (RIGOROUS, NO RATE CLAIM):** If `K` is a wild Alexander horned sphere and `H_n(S²)→K`, then the chart pairs `H_n,H_n^{-1}` cannot be uniformly bi-equicontinuous. In particular, for *any* sequence of bi-Lipschitz ambient charts with these images,

\[
\boxed{\max\{\operatorname{Lip}(H_n),\operatorname{Lip}(H_n^{-1})\}\longrightarrow\infty.}
\tag{WA-15}
\]

Indeed an infinite bounded-distortion subsequence would satisfy WA-14 and force tameness. The conclusion holds when the chosen finite charts are bi-Lipschitz; no physical energy law or specific distortion growth rate is inferred. A simple **tame polygonal U-arc** with endpoints separated by `2^{-n}` while their source parameters are unit-separated has inverse-Lipschitz lower bound `2^n`, checked with exact rational arithmetic in code. That toy is **not** an embedded horned sphere and provides no rate for Alexander's construction.

This supplies SUCC's mathematically meaningful `IdealHard` analogue: a global geometry can force **unbounded chart conditioning**, but only after an exact source-indexed ambient target and convergence mode have been specified. It does not establish that finite physical agents cannot prove a global theorem.

### WA-16 — no blanket no-finite-witness claim from wildness

For an increasing sequence of open connected sets `Y_0⊂Y_1⊂...` with common base point and `Y=∪Y_n`, the canonical map `colim π_1(Y_n)→π_1(Y)` is an isomorphism: any loop and any nullhomotopy have compact images and hence fit inside a sufficiently advanced stage. A fixed nontrivial loop can be present at finite depth and its nontriviality may be preserved by injective bonding homomorphisms. Thus the horned-sphere insight concerns **source-correct global embedding and scale-dependent control**, not an automatic proof of unobservable or undecidable global topology.

The intentionally noncompact toy `C_n={k∈N:k>=n}` has a witness at each finite stage but no common finite `k`: it demonstrates why claiming compatible global fillings from nonempty stagewise filler sets would be wrong. It is **not** a geometric realization of the horned sphere. Genuine topological noncontractibility relies on ambient inclusion maps, not this toy.

## 6. The RH-hard bridge remains missing; wildness is not a sign theorem

Existing PR #86 constructs source-correct real-place Carleman plus true prime-2 window translations, proves an explicit compression-commutator lower bound and an infinite-dimensional 30-moment subspace positivity certificate for the signed Weil form. This branch adds an **additive-adelic compact model** with exact arithmetic and extrinsic topology, *not* a second copy of that Weil certificate.

The **multiplicative** source-operator normalization needed for Weil includes:

\[
Q_W(v)=E_G(v)-C_G\|v\|_2^2
+2|\langle v,\cosh(x/2)\rangle|^2
-2|\langle v,\sinh(x/2)\rangle|^2
-2\sum_{n=p^k\le e^{2a}}\frac{\log p}{\sqrt{p^k}}\operatorname{Re}\langle\tau_{\log(p^k)}v,v\rangle.
\]

No operator has yet been built from WA-1–WA-15 and **proved unitarily or form-theoretically identified with this full signed form**. The compact additive adele-class group `A_Q/Q` is NOT the multiplicative idele-class quotient `A_Q^×/Q^×`. The latter has its own Haar modular structure, Mellin action and conductor/Gamma data; the former does not magically supply those. Topological covering degree 6 is lawful for a generic solenoid but **not** an authentic primitive prime source. Positive Laplacians from linked loops would also remain positive for many fake source mutations, and cannot certify the zeta-specific Weil sign by themselves.

The exact additional research object needed is a **signed source-compatible correspondence**, e.g. an embedding-/representation-indexed bilinear map `T` and a rigorously controlled correction form `R`, such that

\[
Q_W(v,w)=\langle Tv,\,\mathcal L_\mathrm{arithmetic}\,Tw\rangle+R(v,w)
\]

on a common dense test domain, where `R` retains and controls every authentic signed prime/pole/contact term; source mutations and `\chi_4`/non-Euler controls must fail appropriately. This identity is a GOAL, not a result. If it exists and its right-hand side is proved globally nonnegative, then Weil's criterion yields RH; **this branch establishes neither hypothesis**.

A useful new dependency cut is to identify the **Tate/Poisson additive-character pairing on the factorial solenoid** with the same one-Gamma normalization already established in PR #73, *before* attempting any sign theorem. The additive↔multiplicative interface should be an explicitly typed functor/correspondence, not a metaphorical wild-space warp.

## 7. Prior mathematics, controls and actual research status

**Classical imported topology/algebra:** Alexander (1924), horned sphere; continuity of Čech cohomology; Pontryagin duality of solenoids; Smith/normal subgroup calculations for circles; Arzelà–Ascoli; compactness of loop homotopies; Conner–Meilstrup–Repovš (2015), solenoid complement fundamental groups including embedding dependence. Exact type-specific formulations and computable source checks are **new-to-SUCC**, academic priority UNVERIFIED. WA-14/15 are elementary general mathematical consequences, not claimed new published results.

**Concrete negative controls:**

- Every single circle stage has `m` roots, yet global `A_m` may be invertible. The inverse rule must access a deeper, compatible phase.
- `q_n` all distinct primes does not yield `Q` and does not invert any individual prime; *frequency of occurrence*, not number of different primes, matters.
- Arbitrary shared finite prefixes cannot certify which tail primes repeat infinitely.
- The same intrinsic solenoid may have inequivalent ambient embeddings; trying to infer exterior π1 without the `unknotted_torus` contract fails closed.
- A fake `6` primitive Euler jet is rejected, though degree `6` itself is a perfectly legal topological covering.
- A strictly nonnegative Gram of translations on the rational localization cannot have a **uniform positive gap** merely because its common invariant kernel is zero. For any finite rational shifts `s_i` in `G_q`, weights `w_i>=0`, and `D` a common denominator, choose `f_N=(2N+1)^{-1/2}∑_{k=-N}^N δ_{k/D}` on `ℓ²(G_q)`. Then

\[
\sum_i w_i\|(I-U_{s_i})f_N\|²
=\frac{2}{2N+1}\sum_i w_i\min(|D s_i|,2N+1)\longrightarrow0.
\tag{WA-17}
\]

This is proved by exact support intersection counting and tested with `Fraction`. It is a **no-gap certificate for the specified rational-translation Gram**, not a statement that Suzuki's completed signed form is noncoercive. All shifts must lie in the source's actual `G_q`; a proposed dyadic `1/3` translation is rejected.
- Toy `C_n={k>=n}` records noncompact filling debt; it is not a horned-sphere topological proof.

**Source checks:** the new pure-stdlib module `observational_succ/wild_adelic_tower.py` and exact tests `tests/test_wild_adelic_tower.py`; `scripts/wild_adelic_tower_probe.py` emits a deterministic JSON receipt with no nontrivial zeta zero inputs, SHA of source files and no fictitious topology calculations. The module implements only rational stage maps, exact global inverse depths, factorial/profinite delta, prime-tail blindness, embedding contract guards, Čech-homology transport arithmetic and precise Følner energies. No symbolic call is mislabeled as a formally verified topological theorem.

**Next falsification / moonshots:** (i) build explicit ambient PL torus cable maps with a checker that computes meridian inclusion (not merely assumes it), (ii) separate any assumed topological Cech continuity from an actual formalized theorem using Lean/Mathlib, (iii) derive the adelic Poisson one-Gamma transport from WA-8 through the existing authentic PR #73 source (single Gamma, no duplicate places), (iv) investigate whether the 30-moment quotient/complement from PR #86 admits an authentic **signed** topology/holonomy pairing. If not, record a precise impossibility theorem for this class of topological representations.

**RH PROVED: NO. Formal topological Lean proof: NOT CLAIMED. The source/epoch/embedding contract is a mathematical declaration, NOT physically authenticated.**
