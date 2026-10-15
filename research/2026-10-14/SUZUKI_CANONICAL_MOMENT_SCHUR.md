# Operation CANONICAL SCHUR — join the authentic Suzuki finite-source hierarchy and 30-moment sign theorem

**Date:** 2026-10-14. **RH PROVED: NO.** This is a source-specific exact mathematical reduction and research implementation, not a claim of academic priority, empirical physical observation, certified full Weil positivity, or a new Lean theorem.

**Parent checked at immutable Git SHA:** `femboy2112/SUCC@dc6b7e3adbfb67c2913c145a4efb95fe3d50b1bc` (PR #85, finite-source Weil hierarchy). File `observational_succ/source_weil_hierarchy.py` has **Git blob SHA** `0cc8510b71d178fc79e8d410a86d8b6014cf9178`, checked at runtime. **Sibling imported as a theorem with independently replayed rational inequalities, not as silently merged source code:** PR #86 `femboy2112/SUCC@205ffd020dd2a320eeac70a91a2a2700c969c048`, `research/2026-10-14/ARITHMETIC_META_WEIL_BOUNDARY.md` §6 (AMW-06B), including true prime-power/one-Gamma/contact/pole half-density. More recent live sibling branches #84 signed spectral tail, #88 solenoid no-flow-intertwiner, #89 horned observer and #93 Zeno Black Sun were inspected as context, **not merged ancestry**. `main` is unchanged. No nontrivial zeta zeros or black-box zero table are inputs.

**Original question:** Can the genuine infinite-dimensional moment-positive complement of #86 be paired with #85's source-authenticated finite signed compact operator to give a *real* 30-dimensional low/high Feshbach/Schur proof gate? *Answer: yes, at every strictly positive regularization λ, with explicit source error, canonical parity decomposition and one-sided Gamma tail order; no unshifted sign has yet been proved.*

## 1. The exact typed operator and natural Hilbert coordinate

At interval `(-a,a)`, let

- `H=L²_0(-a,a)` with the original, unweighted Lebesgue inner product and mean-zero subspace;
- `D:H_0¹(-a,a)→H`, `Dv=i v'`, a Hilbert isomorphism when its domain carries the derivative norm;
- `V:H→H_0¹(-a,a)` be the inverse integration map up to an irrelevant global phase: `Vu(x)=∫_{-a}^x u(t)dt`;
- `K=V*V=(-Δ_N)^-1>0` on `H`, a compact injective operator;
- `G_a` be **Suzuki's authentic** bounded, compact, signed continuous screw-kernel operator on `H` from (1.3), including the genuine von Mangoldt prime jets, one real Gamma completion, pole/contact, half density and correct original source.

The signed Weil form is `Q_W(v)=⟨G_a Dv,Dv⟩` (Suzuki, classical; #85 FSW-01). The L² norm of the *original* `v` is `||v||²=⟨K Dv,Dv⟩`. No replacement by an arbitrary positive covariance is made. The identification is not a statement about Suzuki's other unbounded L² Friedrichs operator.

### SM-01: precise conversion of the high-moment theorem (PROVED, conditional on the pinned original Weil/source identities)

The sibling AMW-06B theorem at a=1/2 establishes, on every smooth compact `v` satisfying `∫x^jv=0`, `j=0,...,29`, the **actual signed source inequality**

`Q_W(v) > κ||v||²`, with `κ=369/10000`.

Its rational heart is `L_75(21)>131/20`, `ε_29(1/2,21)<1/500`, and a rigorously retained complete signed negative budget `<13/2`:

`(131/20)(499/500)-13/2=369/10000`.

The new module recomputes these with Fraction, but their functional-analytic proof is credited to #86, rather than claimed from a finite unit test.

For `u=Dv=i v'`, integration by parts using v(±a)=0 gives

`∫_{-a}^a x^j v(x)dx = i/(j+1) ∫_{-a}^a x^(j+1)u(x)dx`.

Therefore exactly the same high sector is

`H_high={u in H: ∫x^ku=0, k=1,...,30}`.

Smooth compact moment-null functions are dense in its inverse image by correcting an arbitrary smooth approximant with fixed smooth moment-basis bumps. `Q_W` is continuous in derivative norm because G is bounded, and `||v||²` is also continuous. The inequality extends to **every** `u∈H_high`:

`⟨G_a u,u⟩ ≥ κ⟨K u,u⟩ >0` for `u≠0`.                  (SM1)

**Critical norm firewall:** this is a **relative** `G_high ⪰ κ K_high`, not `G_high ⪰κ I_H`. Since G_high is compact on infinite-dimensional H_high, no κ_I>0 is possible. In particular the raw inverse `D_high^-1` on the derivative-coordinate H is unbounded. A naive unregularized Schur complement is not justified by SM1.

### SM-02: source-specific finite nonpositive spectral index (PROVED)

The Riesz representers for `u↦∫x^ku` are `P_0x^k` for `k=1,...,30`. They span a 30-dimensional subspace, because nonconstant monomials are linearly independent mod constants. If the nonpositive spectral subspace of compact selfadjoint G_a had dimension ≥31, it would contain a nonzero vector orthogonal to all 30 representers; that u lies in H_high. But its Rayleigh is ≤0 by spectral calculus, contradicting SM1. Hence

`dim 1_(-∞,0](G_a)H ≤30` for authentic a=1/2.              (SM2)

This counts negative eigenvectors **and actual null eigenvectors**, with multiplicities; it does NOT assert there are any. Compactness still permits positive eigenvalues accumulating at 0. There is no RH proof or all-a statement.

## 2. A canonical computational low sector (CLASSICAL Legendre identity, PROVED LOCAL)

The best low coordinates are not arbitrary bumps. Let `L_k(x)=P_k(x/a)`, `k=1,...,30`, ordinary Legendre polynomials (exact rational when a rational). These have mean zero, parity `L_k(-x)=(-1)^k L_k(x)`, and diagonal L² Gram

`W_ij = (2a)/(2i+1) δ_ij`.

Their antiderivatives are exactly

`(V L_k)(x)= a (P_(k+1)(x/a)-P_(k-1)(x/a))/(2k+1)`,

vanishing at both endpoints. Thus **all these low probes really belong to H_0¹**, not a ghost sampling basis. High is exactly their L²-orthogonal complement.

### SM-03: the source relative metric has only two boundary channels (PROVED LOCAL)

Integration and orthogonality give

`K_ij = (2 a³)/[(2i+1)(2j+1)] * { δ_ij[1/(2i+3)+1/(2i-1)] - δ_(i+1,j-1)/(2i+3) - δ_(i-1,j+1)/(2i-1) }`.

Hence `K_ij=0` unless `i=j` or `|i-j|=2`. The canonical rank-30 low/high interface of **K**, therefore, has exactly two nonzero channels:

`K_(29,31) = -1/906948`, `K_(30,32)=-1/999180` at `a=1/2`.

The orthonormal-basis squared Frobenius norm of their 2-channel boundary matrix is exactly `3847/453102151320`. These are analytic identities, independently checked by exact Legendre recurrence, not empirically inferred coupling costs.

**Counter-warning:** the signed source G is generally not banded in this basis. The K boundary rank-two result is **not** a claim that the full completed Weil cross operator B has rank two.

### SM-04: actual reflection symmetry halves the low problem (PROVED)

For authentic Suzuki, `g(x-y)=g(|x-y|)` and the original interval is symmetric. Reflection R commutes with G, K and the source finite cell approximants. The Legendre low sector splits into the 15 odd indices `1,3,...,29` and 15 even indices `2,4,...,30`; both high and exact cross interaction respect parity. Any regularized Schur matrix is therefore **exactly block diagonal**:

`S_lambda = S_lambda^(odd) ⊕ S_lambda^(even)`, each size 15×15.

The implemented source-dependent rational finite matrices reject a wrong off-parity entry; a source geometry without reflection must not be passed into this symmetry gate.

## 3. The correct, safe Feshbach/Schur gate (PROVED GENERAL; SOURCE APPLICATION CONDITIONAL)

In derivative-coordinate `H=H_low⊕H_high`, write the **actual signed G** blocks

`G=[A  B; B*  D]`. From SM1, `D>=κK_high>=0`, but `D^-1` need not be bounded.

For **each λ>0**, `D+λI≥λI`, so the variational/Schur identity is valid:

`S(λ)=A+λ I_low - B(D+λI)^-1 B*`.                        (SM3)

The complete operator `G+λI` is PSD **iff** `S(λ)` is PSD. Its entire negative index below `-λ` equals the negative index of this finite 30-dimensional matrix, by Schur congruence/Sylvester inertia, with the two real parity sectors independent.

Thus

`G>=0  iff S(λ)>=0 for EVERY λ>0`.                         (SM4)

This is a finite-MODE reduction, **not a finite-DATA certificate**: S(λ) still involves the infinite high resolvent, and the all-λ quantifier is RH-equivalent. Any actual finite evaluation must pay a source-defined operator error and must not claim the unknown high inverse was computed.

### SM-05: genuine finite-source source-and-cell assembly (PROVED/IMPLEMENTED)

Import *only* the immutable PR #85 `source_weil_hierarchy.stage(a,J,N)` after verifying its Git blob `0cc8510b...`. The module returns the genuine signed `g_J` cell kernel with its original source, exact rational matrix and all-vector norm error. Let h=2a/N, and `c_i=1_(cell_i) - 1/N` (where 1/N is on the whole interval), so `C e_i=c_i`. Define the exact rational `N×N` matrix `R_ij=g_J(h|i-j|)` (the parent midpoint matrix divided by h), the real Legendre overlap `M_ki=∫_(cell_i)L_k`, and the low Gram W above.

The genuine source truncated/cell operator is **precisely** `G_N=C R C*` on mean-zero H. Set `Z=P_high C` and `H_cell=Z*Z=C*C - M*W^-1 M`. All these objects are exact fractions, including the true original prime, poles and Gamma contact embedded in R.

A finite-dimensional Woodbury identity eliminates the infinite complement for **the finite source model**:

`S_N(λ) = λ W + λ M (λ I_N+R H_cell)^-1 R M*`.            (SM5)

This is the unnormalized-Legendre bilinear Schur matrix on the full 30-dimensional low sector. N may be smaller than 30; the untouched directions then appear explicitly through `λW` and are **not** hallucinated as resolved source data. The parent stage's rigorous operator error controls that truncation.

### SM-06: symmetric source error (PROVED GENERAL)

Let `e=||G-G_N||` be bounded by parent #85 `stage.norm_error`, and `L=||G_N||` bounded by the maximum absolute row-sum of its normalized signed cell matrix. For `λ>e`, the exact resolvent identity and block difference estimate imply, on the orthonormal low coordinates,

`||S(λ)-S_N(λ)|| <= e[1+(2L+e)/λ+L²/{λ(λ-e)}] =: E_sym(λ)`.     (SM6)

This is not a guessed entrywise matrix tolerance: E_sym multiplies W in the *unnormalized* Legendre matrix inequality. Therefore strict rational LDL on `S_N(λ)-E_sym(λ) W` proves `G+λI⪰0` and consequently `d_-(G)≤λ` for this fixed interval. Failing the test means **UNRESOLVED**, not `G` negative.

### SM-07: source-positive Gamma monotonicity removes a SIGNED error tax (PROVED GENERAL + ORIGINAL SOURCE)

The sibling parent #85 proves the untruncated authentic Gamma rungs supply a positive operator `T_J` such that

`G=G_J+T_J`, `T_J⪰0`, `||T_J||<=τ_J^+ = 2/(4J+1)^2+16/(4J+1)^3`.

For the source cell approximation, `||G_J-G_N||<=e_sp` with `e_sp=2a(h L_J(a)+η)` from parent `honest_spatial_error`. The exact high positivity D>=0 implies high block of G_J bounded below by -τ_J^+. Whenever λ>τ_J^++e_sp, all relevant high resolvents exist. The Schur complement is the **variational infimum** over high states and hence is monotone under Loewner order:

`S(G+λI)⪰S(G_J+λI)`.

Comparing G_J and G_N by resolvent identity, with `μ=λ-τ_J^+`, gives the certified **ONE-SIDED** result

`S(G+λI)⪰S_N(λ)-E_one(λ)I_low`,

`E_one(λ)=e_sp[1+(2L+e_sp)/μ+L²/{μ(μ-e_sp)}]`.           (SM7)

**No Gamma-tail norm is subtracted in this LOWER Schur bound.** The Gamma tail enters only the invertibility threshold λ>τ_J^++e_sp. This is the rigorous interaction of the separate source-true proofs #85 and #86. It is classical Schur/shorted-operator monotonicity applied with exact authentic source data, not independent priority for shorting theory (Anderson–Trapp 1975).

Again, rational LDL of the **two 15×15 parity pieces** of `S_N(λ)-E_one(λ) W` suffices to prove original `G+λI⪰0`. No such sign certificate for arbitrarily small λ is claimed here.

## 4. The strongest adverse results (PROVED WITH CONCRETE RECEIPTS)

### SM-08a: AMW-07's full-output coupling bound may be structurally hopeless

The prior #86 sufficient condition uses `R_ij=<Af_i,Af_j>` (full operator action), rather than the **actual projected offdiagonal** `R^true_ij=<P_high Af_i,P_high Af_j>`. The prior condition is mathematically sufficient when its hypotheses hold, but is frequently much too strong. For any nonzero f and lower gap κ, if `q_f=<Af,f> >κ||f||²`, Cauchy gives

`q_f-κ^-1||Af||² <= q_f-q_f²/(κ||f||²)<0`.               (SM8)

Even the perfectly positive toy A=diag(10,1), high gap κ=1 and low f=e1 fails the full-output sufficient condition by -90. The **correct projected** offdiagonal vanishes and the exact Schur is +10. Thus a negative AMW-07 matrix need not signal an authentic negative Weil direction; project cross terms before charging their norm, or use the λ-regularized Schur of SM3.

### SM-08b: a hidden conditioning/resource floor in the CURRENT cell code

At `a=1/2`, the parent's declared source Lipschitz bound for **every J>=1** is `L_J=9+2Σ_(j<J)(4j+1)^-1 >=11`. Hence its spatial error bound satisfies

`e_sp >= L_J/N >=11/N`.

The current exact stage implementation supports `N<=24`, so the declared bound cannot even *attempt* a Schur regularization `λ<11/24`, let alone the first-window ~1e-4 scale observed in separate non-certifying PR #79 numerical experiments. For λ=1/10000, the inequality `λ>e_sp` **requires N>=110001** before the positive Gamma tail or other costs. This is a theorem about the declared instrument's error bound, **NOT a lower bound on the true operator approximation error** and NOT an arithmetic impossibility theorem.

The next numerical method should therefore integrate the authentic source *directly against the Legendre basis*, with signed interval bounds and a fast source low/high resolvent representation, instead of building an O(N²) brute-force cell kernel at 110k resolution.

### SM-08c: don't invert compact D at λ=0

The original compact G implies the high compression D is compact on infinite-dimensional H_high. SM1 makes it strictly positive there, but compact positive operators on infinite H have spectral infimum 0. The inverse on its range is unbounded. The toy `D e_n=(1/n)e_n`, `K e_n=(1/n)e_n` obeys `D>=K>0` and still has no bounded D^-1. Any unshifted Schur with an unexplained bounded inverse is REFUTED by this source-compatible operator-theory control.

### SM-08d: input mutations and independence

The source SHA gate rejects a modified genuine Weil interval evaluator; a fabricated `stage` dict with `float(0.0)==Fraction(0)` or `False==0` is explicitly rejected by recursive type-and-value replay, preventing #85's earlier `lru_cache` type-laundering bug from resurfacing. Reflection-breaking interval matrices fail the parity law. A fake independent Euler generator `6` and wrong χ₄ parity/conductor do not acquire permission from rational matrix algebra; all true source certification goes through the original source-tape gate of #85. A sampled finite matrix is never independently promoted to a full Weil theorem.

## 5. Verification / claims and next falsification

The exact standalone pure-math tests, original-source hash replay adapter, deterministic frozen rational receipt, an independent synthetic numerical Schur holdout, and a dedicated Python 3.10/3.13 workflow are in the branch. CI is required to exercise the **actual pinned parent source**; the isolated authored local overlay can test the pure matrix algebra but cannot substitute a fabricated Weil input. Do not claim integrated CI passed without checking the exact head.

The strongest exact result is the **real source-indexed 15+15 regularized reduction**, plus a quantitative *one-sided* true-Gamma Schur bound and a proved instrument-resolution wall. Full RH is not proved, because the source low matrix and its high resolvent have not been certified to yield nonnegativity as λ↓0, nor has positivity at all radii a>0 been established.

**Primary literature:** Suzuki, *Weil's quadratic form via the screw function* (arXiv:2606.09096v3); classical Anderson & Trapp, *Shorted Operators. II*, SIAM Journal on Applied Mathematics 28 (1975); Legendre/Galerkin standard polynomial identities. These imports are credited and distinguished from the source-specific combination.
