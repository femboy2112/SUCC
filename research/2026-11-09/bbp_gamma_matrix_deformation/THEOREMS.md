# The authentic BBP Euler–Mascheroni deformation and its 16×16 Gamma-operator probe

**2026-11-09, research-only descendant of SUCC draft #567** (`40f2fca0d6101c3391fea9174399b0bf63c55e72`). Frozen authenticated source: the four signed poles, literal `U_0=0`, all-prime real carries, source provenance and original Lean contracts. **π's one-digit Haar, two-digit Haar, and base-16 normality: OPEN.** The analytic source identities below are proved on paper and exact rational checks; no new Lean kernel formalization or independent journal review is asserted.

## 1. The question and the three distinct gamma objects

The user's hypothesis: an arithmetic source with an exact Gamma-like 16→256 blocking recursion may possess its own Euler–Mascheroni boundary constant, expressible as a perturbation of the classical `γ = lim(H_N−log N)`. Distinguish:

1. **Classical γ:** `γ=−ψ(1)`, source-independent.
2. **Classical q-digamma γ_q:** `γ_q=−ψ_q(1)=log(1−q)−log(q) Σ_{n≥1} q^n/(1−q^n)`, `0<q<1`. The BBP block kernel has `q=u^8/16<=1/16`, not a `q→1` deformation. This is an exact reference family, not by itself a π normality theorem.
3. **Original BBP source finite part `γ_BBP`:** derived without curve-fitting from the weighted divergent sum `Σ n r(n)` and its authentic coefficient `a=15/64`. This is the new closed-form target below.

The empirical *real π* 16×16 transition matrix is yet another object, and is not itself the source's q-Gamma blocking kernel. A matrix Gamma observable must be **defined** with a declared source map and basis; ordinary eigenvalues cannot canonicalize its definition.

## SGM-01 — exact BBP harmonic Gamma recursion and unique source finite part (PROVED PAPER)

Let the authentic BBP forcing be

`r(n)=4/(8n−7)−2/(8n−4)−1/(8n−3)−1/(8n−2)`, n≥1,

with signed residues `(c_i,b_i)=(4,7),(-2,4),(-1,3),(-1,2)`. Set `a_i=1−b_i/8=(1/8,1/2,5/8,3/4)` and `w_i=c_i b_i/64=(28,-8,-3,-2)/64`, so `Σw_i=15/64=:a`. Then, EXACTLY, for every integer n≥1,

`n r(n)=Σ_i w_i/(n−1+a_i)`.                                (SGM1)

Proof: `n/(8n−b)=1/8+b/[64(n−b/8)]`, and `Σ c_i=0`. No asymptotics or numerical sampling.

Define for real z≥0 the gamma quotient (well-defined as a positive real function)

`G_BBP(z)=∏_i Γ(z+a_i)^(w_i)`.

Its logarithmic derivative `Ψ_BBP(z)=Σ_i w_i ψ(z+a_i)` obeys

`d/dz log[G_BBP(z+1)/G_BBP(z)] = Σ_i w_i/(z+a_i)`

by the classical Γ functional equation. At z=n−1 this derivative equals `n r(n)` **on the original frozen source**, not on a fitted substitute. Further,

`Ψ_BBP(N)−Ψ_BBP(0)=Σ_(n=1)^N n r(n)`;
`Ψ_BBP(N)=a log N+O(1/N)`.

Therefore the *source-specific Euler–Mascheroni type constant* is

`γ_BBP := lim_(N→∞)[Σ_(n=1)^N n r(n)−a log N] = −Ψ_BBP(0)`.

Using the inherited source jet `r(n)=a/n²+151/(512 n³)+O(n^-4)`, this is also the **absolutely convergent perturbation**

`γ_BBP = a γ + Σ_(n≥1)[n r(n)−a/n]`.                (SGM2)

For N≥2 the tail of the convergent correction is bounded by `151/(512N)+1/(2N²)` from #560's original source estimates. The classical harmonic difference gives a separately paid O(1/N) term for the finite log normalization. This is a *source finite part*, not automatically a new transcendence or digit-distribution theorem.

## SGM-02 — fully explicit γ_BBP in terms of classical γ (PROVED PAPER, Gauss digamma input)

Gauss's formula at the rational shifts 1/8,1/2,5/8,3/4 (DLMF §5.4.19) evaluates the digammas in SGM-01. The resulting exact expression is

```
γ_BBP = (15/64) γ
      + ((27+31√2)/128) π
      + (39/32) log 2
      + (31√2/64) log(1+√2).
```

Numerically `γ_BBP=3.32249791110640475659473238782379790945...`; the normalized leading-harmonic form is `(64/15)γ_BBP = 14.175991087387326961470858188...`. Both the independent four-pole partial fraction and the Gauss form were evaluated at ≥55 significant digits and agree at that scope. **The occurrence of π and γ on the right is an elementary digamma evaluation, not a π-normality inference.**

A matched-leading, genuinely different four-pole source

`r_mut(n)=r(n)+(1/10)[1/(8n−7)−2/(8n−4)−1/(8n−3)+2/(8n−2)]`

has the same coefficient `a/n²` because both its zero- and first-pole moments vanish, but its finite-part constant changes by EXACTLY

`γ_BBP(mut)−γ_BBP = (3/160)log2+(√2/64)log(1+√2)+(√2 π/128)`
`                      = 0.0671823213442434143999478000...`.

This is a source-fingerprint **finite-part difference**. Neither matched leading order nor matched Gamma(1/2) source-critical limit of #560 fixes it. It does not assert the mutated source has the same π constant.

## SGM-03 — source gamma's exact recurrence and a 16×16 matrix generalization (PROVED / DEFINED)

Define the scalar **source Gamma coordinate**

`C_BBP(z):=−Σ_i w_i ψ(z+a_i)`, real `z>−1/8`, with `C_BBP(0)=γ_BBP`.

Then the ψ recurrence gives

`C_BBP(z+1)−C_BBP(z)=−Σ_i w_i/(z+a_i)`.

In particular, for integer n≥1,

`C_BBP(n)−C_BBP(n−1)=−n r(n)` exactly.

This is the precise Gamma recursion associated with the frozen source, and all observation origins use one common function.

Now for any 16×16 **row-stochastic** matrix P define H=J/16 and `X=P−H`. For `||X||₂<1/8` define the analytic functional calculus

`𝓒_BBP(X) := −Σ_i w_i ψ(a_i I+X)`.                   (SGM3)

The closest digamma pole is at `−a_min=−1/8`. In this norm domain the following convergent matrix Taylor series is valid:

`𝓒_BBP(X) = γ_BBP I + Σ_(m≥1)(−1)^m c_m X^m`,
`c_m = Σ_i w_i ζ(m+1,a_i)`,                         (SGM4)

with Hurwitz zeta ζ(s,a). Here `c_1=27.7515939068881733175...`.

The **mathematical** tail after order M obeys the explicit (not rounded-arithmetic) bound for `x=||X||₂<1/8`:

`||remainder||₂ ≤ (41/64)[8(8x)^(M+1)/(1−8x) + 2x^(M+1)/(1−x)]`. (SGM5)

Proof: `Σ|w_i|=41/64`, `a_i≥1/8`, and `ζ(s,a_i)≤8^s+ζ(s)≤8^s+2` for s≥2; use a geometric series and submultiplicativity. Implemented float/MP values have additional ordinary rounding errors; the bound is **not a certified interval bound on the floating output**.

This construction is a **chosen source-labelled observer**, not a mathematically forced unique physical 16×16 transfer. P is the finite *empirical* two-digit Markov surrogate from #567. A fixed P is not claimed to generate the actual deterministic digit process. Convergence of 𝓒(X_A) to γ_BBP I is equivalent to vanishing of the centered transition defect only in a local invertibility neighborhood; absent a source-derived bound this is not a shortcut to real π digit normality. One-digit marginal Haar remains separately necessary.

## SGM-04 — Gamma operator detects the non-Haar nilpotent eigenblind mode (PROVED EXACT ALGEBRA)

Recover #567's exact, positive, doubly stochastic hostile matrix:

`P_* = H+X`, `X=u vᵀ/64`,
`u=(1,−1,0,..,0)`, `v=(1,1,−2,0,..,0)`.

Here `X²=0`, X≠0, `P_*²=H` and `spec(P_*)={1,0×15}` *identical* to H. Nevertheless, SGM4 terminates exactly:

`𝓒_BBP(X) = γ_BBP I − c_1 X ≠ γ_BBP I`.

Its operator deviation is

`||𝓒_BBP(X)−γ_BBP I||₂ = c_1 ||X||₂ = c_1 √3/32`
`                                   = 1.502099082429662...`.

This produces a precise **non-Haar matrix Gamma response invisible to eigenvalue-only or trace-only analysis**: because X is nilpotent, `tr 𝓒_BBP(X)=16γ_BBP` also equals Haar's trace. The full operator, generalized eigenvectors or singular values detect it; a scalar trace does not. This is a detector of known non-Haar data, not a mechanism that makes the data Haar.

**Second hostile control:** P=H can coexist with a non-Haar one-digit marginal. In that case all observed conditional transitions are Haar but the two-digit joint law is not. Thus a Gamma operator on X alone **cannot** prove full two-digit Haar without a separate actual one-digit source estimate.

### SGM-04B — a quantitative local Gamma/Haar equivalence (PROVED PAPER)

In fact the chosen Gamma diagnostic is *locally coercive*, although this creates no new source-selected decay. For every 16×16 row-stochastic P with `X=P−H` and `||X||₂≤1/32`, the exact source coefficients and Hurwitz tail give

`13 ||X||₂ ≤ ||𝓒_BBP(X)−γ_BBP I||₂ ≤ 43 ||X||₂`.    (SGM6)

**Explicit constants (no numerical fitting):** Let `c1=Σ_i w_i ζ(2,a_i)`. Since `ζ(2,a)≤a^(−2)+2` and the negative weights are only at shifts `1/2,5/8,3/4`,

`c1 ≥28−3/4−171/800−17/144 =193811/7200 >26`, while
`c1 ≤(28/64)(64+2)=231/8<29`.

For `x≤1/32` the exact higher-order matrix power-series tail after the linear term is bounded by `T(x)≤(40795/2976)x<14x` using (SGM5) with M=1. Hence `||𝓒_BBP(X)−γ_BBP I||₂ ≥(c1−14)x>13x`, and the upper bound is `<(29+14)x=43x`. QED. The inequality applies to the **ideal exact analytic function** in the declared spectral-norm radius; a floating approximation also has rounding error.

**Scope:** If a source argument independently proved `||X_A||₂→0`, then its Gamma observable would converge, and vice versa when the norms enter this radius. The transformation supplies a quantitative **detector** of non-Haar transition structure, not an estimate that transition structure actually decays. Real one-digit marginals still need their own authentic source bound.

## SGM-05 — BBP q-Gamma blocking is related but a different normalization (PROVED SOURCE ALGEBRA)

The already-used source integral is `r(n)=∫_0^1 u^(8n−8) Q(u)du` with `Q(u)=4−2u³−u⁴−u⁵`. Group g chronological steps with exact kernel

`K_g(u)=Σ_(j=0)^(g−1)16^(g−1−j)u^(8j)`, `q=u^8/16`.

Therefore

`K_g(u)=16^(g−1)(1−q^g)/(1−q)=16^(g−1) Γ_q(g+1)/Γ_q(g)`;
`K_(g+h)(u)=16^h K_g(u)+u^(8g) K_h(u)`.

At u=0 the Γ_q ratio is interpreted by continuity. This is exact source chronology. However, `q∈[0,1/16]`, so *no q→1 asymptotic happens within the authentic source integral*. Classical `γ_q=−ψ_q(1)` at q=1/16 is approximately `0.131895818222398...`; it is NOT the `γ_BBP≈3.322498` of SGM-01. Equating them is a typed error. Classical sources: DLMF §5.18 and Salem's q-digamma exposition.

## SGM-06 — original 131,072-digit π transition matrices, calibrated only (FINITE NUMERICS)

Reuse #567's 131,072 **source-certified** hexadecimal digits; do not call this a new blind holdout. Each 65,536-digit half is analyzed using its 65,535 actual linear adjacent pairs, NOT an invented cyclic end→start pair. Define P(a,b)=count(a,b)/row_total and X=P−H. At 24 terms with 70-digit source coefficient evaluation, local numeric matrix calculations give:

| Existing block | `||X||₂` | `||𝓒_BBP(X)−γ_BBP I||₂` | Status |
| --- | ---: | ---: | --- |
| First 65,536 | 0.03307051955 | 0.81819890558 | finite diagnostic |
| Second 65,536 | 0.02832584039 | 0.81940907795 | finite diagnostic |
| Entire 131,072, 131,071 linear pairs | 0.01910466230 | 0.49556199337 | finite diagnostic |

These are values of a **chosen analytic transformation** of known empirical P, not an independent arithmetic proof of normality. The P-H norm improves across the combined sample by ordinary averaging; the Gamma response is nonlinear and nonmonotonic between the halves. No constant above is alleged to be the true γ eigenvalue of the empirical P.

## Prior art, hypotheses, next falsifier

- #560 LCS-02 already proves `D+aγ` as a source finite part; SGM-02 adds its **closed elementary formula**, exact Gamma quotient recursion, and matrix functional calculus. The global π signed Weyl gate is unchanged.
- #565 gives a conditional Haar future-tail projector, which would prove real normality if its original-zero discrepancy vanished. No such arithmetic vanishing is imported here.
- #566 gives 2-adic **spatial** Haar, not real π digit-pair Haar; #567 gave the nilpotent eigenvalue no-go and certified finite pairs. This round provides a Gamma operator that **detects**, but does not eliminate, that nilpotent.
- Matched-leading source mutation changes γ_BBP; coherent seed `s*=−π/16` retains the source finite part but fails real Haar. Thus no seed-blind source Gamma constant forces π normality.
- **Decisive next theorem:** an all-epoch, original-zero, source-dependent estimate on `||P_A−H||` (plus actual one-digit marginals), or an exact signed 225-mode/full-prime-carry conditional current that enforces it. Any growing-depth Gamma-regularized operator must include all chronological source/tail/prime residues and show an *independent signed contraction*, rather than merely recoding `P−H` analytically.

**Claim ledger:** SGM1/2 source/closed form PROVED PAPER; SGM3/4 matrix formula PROVED finite analytic algebra conditional on chosen P; SGM5 q-Gamma source identity classical/algebra; SGM6 finite observed numeric; real π normality OPEN.
