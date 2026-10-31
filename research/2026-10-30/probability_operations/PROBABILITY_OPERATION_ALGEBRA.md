# SUCC — Probability-Operation Algebra on the Realized Carrier

**Research date:** 2026-10-30. **Status:** additive draft research, proposed child of [PR #409](https://github.com/femboy2112/SUCC/pull/409) at exact head `3857e70472cac7c572528cc6d4198246e57d36df` (parent chain #406/#404/#402/#397; Main XVI original baseline `e18ba565ca540adb7edf3292f5593929e76d91c5`). Original four signed BBP poles and selected `U_0=0` are unchanged. **Base-16 normality of π, RH, source-selected signed Weyl `o(N)` remain OPEN.**

## Objective: falsifiable generated probability operations, without introducing unearned randomness

**Author's hypothesis:** normal hexadecimal digits support a sufficiently rich algebra of probability-generated operations. Example: `sqrt(rand())` and `max(rand(),rand())` produce identical laws under independent uniform sampling. Could an observer build a probabilistic test model on the selected carrier such that failure proves π nonnormal?

**Answer with quantifiers:** Yes. For any fixed, declared transformation whose outcome is necessary for every base-16 normal digit stream, a *proved asymptotic* failure is a certificate of nonnormality. No **finite** prefix failure can certify nonnormality (any fixed prefix has normal and nonnormal extensions). Every success is conditional and cannot prove π normality by observation alone. We seek a **complete** operation identity with a unique uniform fixed point and a quantitative finite certificate; avoid a collection of generic tests with false positives.

## PO-01. The square-root / maximum law and two exact hostile witnesses

If `U,U1,U2` are independent `Uniform[0,1]`, then
\[
\boxed{\sqrt{U}\overset d=\max(U_1,U_2),\quad F(t)=t^2\ (0\le t\le1).}
\]
For **any** CDF of form `F_c(t)=t^c`, `c>0`, independent `X1,X2~F_c` obey `F_c(t²)=F_c(t)^2`, so the same square-root/maximum identity holds. Thus a `Beta(c,1)` input with `c=2` is a **specific nonuniform false positive**. The degenerate `δ_0` also passes. This ONE law cannot uniquely identify Haar.

**False negative caused by pairing overlapping deterministic tails:** Even if α is base-16 normal, its consecutive circle states `X_n={16^n α}` and `Y_n=X_(n+1)={16X_n}` converge in **joint empirical distribution** to graph-Haar `(id,T16)_*λ`, NOT independent `λ⊗λ`. At threshold `t=1/3`,
\[
\boxed{\lim_N N^{-1}\#\{n<N:\max(X_n,Y_n)\le1/3\}=\lambda\{x\le1/3,\{16x\}\le1/3\}=1/8,}
\]
while the independent maximum law would predict `1/9`. Exact derivation: 5 complete radix cells of length 1/16 each contribute (1/3)/16; the remaining partial cell also contributes (1/3)/16; sum 6/48=1/8. A naive observer could wrongly 'disprove' normality even for a genuinely normal sequence. **Independence and sample construction are load-bearing.**

For true normal digits, sample two disjoint non-overlapping k-digit blocks, `U^(k)`, `V^(k)` in an aligned 2k-word. At each **fixed k**, normality in base 16 implies base `16^(2k)` block-normality (Wall / power-base normality), so the limiting two-block grid law is product-uniform on `{0,...,16^k−1}²/16^k`. At fixed threshold t, its quantized laws `P(sqrt(U^(k))≤t)` and `P(max(U^(k),V^(k))≤t)` differ by at most `3/16^k`. To obtain the continuous identity, take the **sample horizon N→∞ first, then k→∞**. Normality alone supplies no convergence rate uniform over k growing with N.

## PO-02. A single operation identity that uniquely determines the correct raw-state measure

Set `b=16`, `D={0,...,15}`, `f_d(y)=(d+y)/16` for y∈[0,1]. Define the **fair inverse-branch probability operation** on probability measures:
\[
\boxed{\mathsf P\mu=\frac1{16}\sum_{d=0}^{15}(f_d)_*\mu.}
\]
It is the distribution of `(D+Y)/16` with D *independent uniform* on the digit alphabet and `Y~μ`. Lebesgue/Haar `λ` is fixed by P. The operation is 1/16-Lipschitz in ordinary interval Wasserstein-1:
\[
\boxed{W_1(\mathsf P\mu,\mathsf P\nu)\le\tfrac1{16}W_1(\mu,\nu).}
\]
Thus P has **exactly one** invariant probability, λ. Even without Wasserstein, Fourier gives `\hat{Pμ}(h)=0` when `16 ∤h`, and `\hat{Pμ}(h)=\hat μ(h/16)` otherwise; any P-fixed μ has every nonzero Fourier coefficient zero. This is classical transfer-operator/IFS uniqueness specialized to SUCC's radix-
16 inverse branches, not proof that π is such a fixed point.

**No-discard framing:** `x_n=(d_n+x_(n+1))/16` with `d_n=floor(16x_n)` is an exact left-invertible state rechart. It holds for EVERY radix orbit, normal or nonnormal. The **nontrivial** statistical hypothesis is that replacing the observed first digit by a *fair independent digit* still reconstructs the same state distribution. Merely rearranging exact state records gives no statistical constraint.

## PO-03. Quantitative finite-horizon model discrepancy — NEW SUCC specialization

For arbitrary α∈[0,1), define exact pure radix states and first digits
\[
x_n=\{16^n\alpha\},\quad d_n=\lfloor16x_n\rfloor,\quad x_{n+1}=16x_n-d_n.
\]
Let
\[
\mu_N=N^{-1}\sum_{n=0}^{N-1}\delta_{x_n},\quad
\mu_N^+=N^{-1}\sum_{n=0}^{N-1}\delta_{x_{n+1}},
\quad
\boxed{\varepsilon_N=W_1(\mu_N,\mathsf P\mu_N^+).}
\]
Here `P μ_N^+` is the observer's *generative test model*: pick one of the actually observed tail states uniformly and independently select one of 16 predecessor branches. Compare the generated predecessor distribution with the original realized states. **This uses all possible branches, not the actual correlated branch that generated each state.**

The exact telescoping difference `μ_N−μ_N^+=(δ_(x_0)−δ_(x_N))/N` implies
`W1(μ_N,μ_N^+)≤1/N`. Since P is a 1/16 contraction and fixes λ,
\[
W_1(\mu_N,\lambda)\le \varepsilon_N+\tfrac1{16}W_1(\mu_N^+,\lambda)
\le\varepsilon_N+\tfrac1{16}(W_1(\mu_N,\lambda)+N^{-1}).
\]
Rearrange. Conversely use triangle inequality to control ε_N by `W1(μ_N,λ)+1/16 W1(μ_N^+,λ)`. This yields the explicit TWO-SIDED stability bound
\[
\boxed{
\frac{16}{17}\varepsilon_N-\frac1{17N}
\ \le\ W_1(\mu_N,\lambda)\ \le\
\frac{16}{15}\varepsilon_N+\frac1{15N}.}
\]
Consequently, by Wall's criterion:
\[
\boxed{\alpha\text{ normal in base }16\iff\varepsilon_N\to0.}
\]
If the observer can prove `limsup_N ε_N>0` (or failure to converge to zero), then α is **not** normal; if it can prove ε_N→0, α **is** normal. A finite observed ε_N>0 alone certifies neither conclusion. The theorem holds for ANY α, and therefore does not yet provide source-selected proof of π.

**Coherent hostile control:** α=0 gives `μ_N=δ0`, `Pμ_N^+=(1/16)Σ_d δ_(d/16)`, exactly
\[
\varepsilon_N=\frac1{16}\sum_{d=0}^{15}\frac d{16}=\frac{15}{32},\qquad
W_1(\delta_0,\lambda)=\frac12.
\]
The upper stability inequality is asymptotically SHARP here: `(16/15)*(15/32)=1/2`. A periodic digit word `0123456789abcdef` also passes every single-digit frequency test, but has a nonzero operator discrepancy. The coherent same-forcing original BBP counterseed `s_*=-π/16` produces pure α=0, and hence exactly this control.

A mathematically equivalent **stronger joint test** compares the empirical pair `(d_n,x_(n+1))` to `Uniform(D)⊗μ_N^+` in a weak topology on `D×[0,1]`. Under normality the joint measure tends to that product, expressing asymptotic independence of *leading digit and residual tail*. Do NOT use total-variation against finite atomic point samples: with distinct residuals the empirical joint and product can have TV=15/16 even for normal α. Use weak/BL/Wasserstein tests or increasingly finer **fixed** finite cylinders with a correct order of limits.

## PO-04. Probability operations produce the whole harmonic/golden/Oily family

Under independent continuous `Uniform(0,1)` variables `U_1,...,U_r`, let
\[
G_r=-\log\prod_{i=1}^rU_i=\sum_i(-\log U_i)\sim\operatorname{Gamma}(r,1).
\]
Thus for integer r≥1,
\[
E[\log G_r]=\psi(r)=H_{r-1}-\gamma,
\quad E[e^{-\lambda G_r}]=(1+\lambda)^{-r}=\lambda^r,
\quad\lambda=\varphi^{-1},\ (1+\lambda)^{-1}=\lambda.
\]
This gives **the entire previously declared SUCC Oily–Macaroni grade family** by a universal probability-operation identity:
\[
\boxed{D_s=E[\log G_{s+2}-e^{-\lambda G_{s+2}}]
=H_{s+1}-\gamma-\lambda^{s+2}.}
\]
At s=0, D_0=λ−γ≈0.04081832384836. Separately implemented high-precision quadrature verifies r=2,3,4,6. This is an EXACT generic Gamma/Gibbs construction, not a π-specific discovery or a proof that SUCC's independently constructed Gamma boundary samples actual digits. For a single deterministic normal sequence, distributional convergence of fixed continuous bounded transforms follows from normality, but unbounded observables `log G_r` need truncation and a justified exchange of limit with expectation: normality alone doesn't give the requisite uniform integrability.

## PO-05. A second nonlinear operation and its own firewall

For independent `X,Y~μ` on the circle, the modular sum `(X+Y) mod 1` has distribution `μ*μ`. Uniform Haar is idempotent, `λ*λ=λ`. If μ is idempotent, then each Fourier coefficient obeys `μhat(h)^2=μhat(h)`, hence lies in `{0,1}`. If μ is **atomless**, the case `μhat(h)=1` for h≠0 is impossible, since it forces μ to be supported on finitely many h-th roots. Therefore
\[
\boxed{\mu*\mu=\mu\quad\text{and μ atomless}\implies\mu=\lambda.}
\]
Both assumptions are essential: δ0 and uniform measures on finite cyclic subgroups are idempotent but non-Haar. This offers a quadratic alternative, but establishing atomlessness of every authentic limit is a new arithmetic obligation. The inverse-branch operation of PO-02 needs no added atomlessness hypothesis.

## PO-06. Exact original-source π demonstration with a rigorous finite uncertainty budget

The authentic signed four-pole BBP source uses
\[
r_n=R(8n-7),\qquad R(a)=4/a-2/(a+3)-1/(a+4)-1/(a+5),\qquad\alpha=\pi/16=\sum_{n≥1}16^{-n}r_n.
\]
Since positive r_n decrease with n, the original rational M-term prefix bounds α within
\[
\boxed{S_M\le\pi/16<S_M+\frac{r_{M+1}}{15\,16^M}}.
\]
The standalone exact Fraction program certifies enough digits for every state in an N-window. Construct each x_n by taking **L=8** subsequent certified hex digits, obtaining a rational truncation \(\tilde x_n\) with error at most \(\delta=16^{-8}\). Then calculate the exact 1D Wasserstein ε for the two equal-mass finite point clouds with rational coordinates (the original state list replicated 16 times versus all 16 generated predecessor branches per next-tail state).

For any exact α tail state and its truncations, \(|\varepsilon_N-\tilde\varepsilon_N|\le(1+1/16)\delta\) by W1 stability. Thus the actual occupation measure is enclosed by
\[
\boxed{W_1(\mu_N,\lambda)\le\frac{16}{15}[\tilde\varepsilon_N+(17/16)\delta]+\frac1{15N}.}
\]
At N=32,128,256, the exact rational **truncated estimates** from the original BBP source are:

| N | Truncated inverse-branch W1 ε | Truncated raw-state W1 to Haar | Rigorous upper bound on actual-state W1 |
|---:|---:|---:|---:|
| 32 | 0.115532192 | 0.122901951 | 0.125317672 |
| 128 | 0.043046657 | 0.045715792 | 0.046437268 |
| 256 | 0.014679133 | 0.015136004 | 0.015918159 |

These are finite observations. No speed of convergence, eventual monotonicity, or uniform bound at untested N follows. The observer cannot promote finite comparisons to an infinite normality certificate. The original source's forced orbit \(\{U_n(0)\}\) differs from the pure radix reference by the exact Green tail T_n; converting interval-based branch tests across this difference requires separate seam controls. Source W1 for phase state alone does **not** automatically control the discontinuous digit-label map near radix boundaries.

## PO-07. How to avoid a test that only restates normality

The equivalence ε_N→0 iff normality is a **calibrated criterion**, not a solution. The open source-specific mathematical task is to derive a non-circular bound on the operator defect ε_N directly from original four-pole arithmetic, literal carries/prime CRT/Green-tail data, without assuming the unknown digit distribution or simply rewriting its Weyl sums.

Discriminating outcome categories:
- **PASS toward normality:** prove ε_N=o(1) with an independent original-source estimate valid for all large N, then the explicit W1 stability forces Haar and base-16 normality.
- **FALSIFY normality:** prove limsup ε_N>0 (not merely isolated finite failures), which forces non-Haar raw-state behavior.
- **AMBIGUOUS:** finite ε_N small or large; a few operation identities hold; conditional theorem with unverified arithmetic input; or a test fails because the observer mistakenly paired overlapping tail variables as independent.

**Hostile controls:** coherent same-forcing s*=−π/16 (operator defect 15/32); exact 15-torsion seed aliases (normality preserved under rational shift); periodic uniform one-digit controls; biased absolutely continuous Beta(2,1) fake satisfying sqrt=max; finite de Bruijn mimicry; normal Stoneham c=3/5 (classically known); Gamma-matched source and higher-jet controls; nontrivial mismatched digit/tail dependence; fixed versus growing block length; 2D/3D graph-Haar not product-Haar; p-primary vs entire CRT; finite precision near carry seams.

**Claim status:** PO-01/02/03/04/05 are classical laws or exact specialized proofs, not scholarly priority claims. PO-06 is verified original-source finite demonstration, not new infinity proof. PO-07 original-selected operator defect bound **UNVERIFIED**. Preserve exact tests, oracle, source hashes, and raw logs; no original recurrence or main changes.

## References (public mathematics, not new priority claims)

- Wall's normality criterion for base-b expanding orbits: https://digital.library.unt.edu/ark:/67531/metadc2178728/m1/2/ .
- Becher et al., *A zoo of computable binary normal sequences*, PNAS 2012: https://doi.org/10.1073/pnas.1215998109 .
- Hutchinson/IFS invariant measure uniqueness via contractions: https://link.springer.com/article/10.1007/s00009-024-02751-9 .
- Order statistics and probability integral transform: https://sadbhavnapublications.org/research-enrichment-material/2-Statistical-Books/Nonparametric-Statistics-Theory-and-Methods.pdf .
- SUCC PR #409 original source Green and raw-state quotient; #406 universal counting; #404 Ward/Noether; #395 Stoneham calibrated controls.
