# Signed spectral-tail calculus — source-pinned research round (2026-10-14)

Parent: PR #96 `f6539057daaf7c98df1c069c98d90d6be2e5d0ca`; source: authentic signed Suzuki compact operator on mean-zero `L²(-a,a)`, inherited from PR #85. **RH OPEN.** This note gives conditional and unconditional operator facts, not a sign certificate for the true low Schur.

## ST-1: Exact finite spectral extraction does not bound the residual sign

Let `G=G*=G_a` be compact and let `P` be a finite-rank *exact spectral projection* commuting with G. Then `G=PGP ⊕ (I-P)G(I-P)`, so
`d_-(G)=max(d_-(PGP),d_-((I-P)G(I-P)))`,
where `d_-(A)=max(0,-inf σ(A))`. In particular, certifying that a selected finite spectral pair is positive says **nothing** about the sign of the complementary block. A contour projector obtained from a zero of ξ is not automatically a spectral projection of Suzuki's finite-interval G; an explicit source-identified intertwiner is required. Thus a local theta zero certificate cannot be subtracted from G as a positive summand without this extra proof.

## ST-2: Finite Galerkin negative depth is monotone, and its convergence has an effective two-sided bound

For nested finite-dimensional `H_N` dense in H, put `m_N=inf_{v∈H_N,||v||=1}<Gv,v>`. Then `m_{N+1}≤m_N` and `m_N↓inf σ(G)` (Rayleigh variational principle). This **does not** imply `m_N≥0` from finitely many positive stages.

For a self-adjoint finite source approximation `G_N` with certified `||G-G_N||≤ε_N`, `|d_-(G)-d_-(G_N)|≤ε_N`. A single strict negative margin `d_-(G_N)>ε_N` proves a genuine negative witness. The reverse (small negative depth at finite N) cannot prove `d_-(G)=0` without a universal decay bound on the *source-derived* signed part.

## ST-3: Positive-tail one-sided transfer (Suzuki's actual Gamma source)

Write `G=G_J+T_J`, where the omitted authentic Gamma OU tail is PSD and `0≤T_J≤τ_J I` on H. Then
`G_J≤G≤G_J+τ_J I`,
and for every finite P,
`P G_J P≤P G P≤P G_J P+τ_J P`.
Hence
`inf σ(G_J)≤inf σ(G)≤inf σ(G_J)+τ_J`.
For a **lower** sign certificate, the positive tail may be omitted; charging it as a symmetric negative error wastes source information. Conversely, positivity of the full G cannot be deduced from an indefinite G_J.

## ST-4: Shifted low/high Feshbach sign and its unavoidable singular limit

Let `H=H_L⊕H_H` and `G=[[A,B],[B*,D]]`, with `D≥0` (in PR #96, this is the source-true 30-moment-null high-space result at a=1/2). For λ>0 define
`S_λ=A+λI-B(D+λI)^(-1)B*`.
Then `G+λI≥0 ⇔ S_λ≥0`, since `D+λI>0`. This is the **exact** infinite-dimensional Schur complement, with finite low dimension.

The family is operator-monotone increasing in λ:
`S_μ-S_λ=(μ-λ)[I+B(D+μI)^(-1)(D+λI)^(-1)B*]≥(μ-λ)I`
for μ>λ>0. Thus the difficult direction is λ↓0. A single positive shift is not RH-strength evidence.

## ST-5: A necessary-and-sufficient range/shorting criterion at λ=0

Suppose D≥0 and low dimension is finite. Define the possibly infinite quadratic expression
`R_0(x)=lim_{λ↓0}<B*x,(D+λI)^(-1)B*x>`.
By the spectral theorem,
`R_0(x)=||D^(-1/2)B*x||²` if `B*x∈Ran(D^(1/2))`, and `+∞` otherwise (interpret the inverse on the orthogonal complement of ker D). Then

`G≥0 ⇔ (i) B*(H_L)⊂Ran(D^(1/2)), and (ii) A≥B D^† B*`,

where the right-hand quadratic matrix is the Gram form of `D^(-1/2)B*x`. This is the classical positive block-operator/Douglas range condition, **not** a new proof of RH. For compact D, its inverse can be unbounded and the range condition is a genuine obstruction. In particular, finite positive shifted Schur certificates do not supply a uniform zero-shift bound unless the range/cross control is established.

Proof: complete the square with `D^(1/2)y` in `<Ax,x>+2Re<B*y,x>+<Dy,y>`; the infimum over y is finite exactly when the linear functional on Ran(D^(1/2)) is bounded in its induced norm. The Riesz representation theorem then gives the range condition and shorted matrix. The resolvent limit follows by monotone convergence of spectral integrals.

## ST-6: The finite-zero / finite-shadow trap

For any finite-rank P and any δ>0, choose unit `e∈P^⊥`. The compact self-adjoint pair `G_+=0`, `G_-=-δ|e><e|` agrees on P's entire compression, but `d_-(G_-)=δ`. Both can be approximated in operator norm. This is a generic operator countermodel, **not** a source-lawful modification of zeta. To exclude such hidden directions for authentic G, one needs an all-test source-derived bound or an exact range/shorting identification.

## ST-7: What the theta contour observer actually gives

The theta-contour certificate (PR #82, sibling branch, not merged) isolates one authentic simple critical-line zero. By the explicit formula it contributes a positive rank-one spectral functional on test functions. But no source-identified operator map from that functional to the finite-interval Suzuki G's low/high splitting is currently proved. The absence of that map is a **probe/identification gap**, not a demonstrated physical or logical impossibility.

## Next falsifiable source experiment

On the true PR #96 Legendre 30→15+15 split, construct certified **cross-resolvent Gram** entries
`R_λ(i,j)=<B*e_i,(D+λI)^(-1)B*e_j>`
with rigorous source errors, and attempt a uniform λ↓0 upper bound. Compare (a) direct source-integral Legendre entries, (b) positive Gamma one-sided tail, (c) independent Schur resolvent enclosure. A true bounded limit plus `A-R_0≥0` would prove the authentic localized Weil form positive at a=1/2. A diverging direction would refute positivity there and hence RH, but only after the original-source identification and operator-domain checks survive. The current finite-cell error method has a λ-dependent blow-up; a direct moment/Legendre source integration is the next instrument.

**Claim ledger:** ST-1 through ST-6 are classical operator deductions under stated hypotheses; ST-7 is a source/provenance gap; the λ→0 sign and all-a positivity are UNVERIFIED. No zero-location or numerical-fit input to the deductions.