# PREREGISTRATION — ZERO OBJECT × CASIMIR CONSTRAINTS × SELECTED BBP EXCLUSION PRESSURE

**2026-11-05; research only.** Strict additive child of [SUCC #513](https://github.com/femboy2112/SUCC/pull/513) exact pinned parent \`727a97a006e929243e0fee1ab44cf52dc68e2c8f\`. No original BBP source modifications, no change to literal U0=0, frozen proof/Lean/provenance/production/workflow/main, no merge/tag/release. π-normality, original selected Weyl decay and critical determinant bound remain OPEN.

## User hypothesis and scope

The primal neutral zero object enables relational constructions; finite causally marked forms select histories and change their *conditional field of available continuations*. The proposed analogy is a mathematical "Casimir" pressure: baseline virtual forms outside a constraint and source-conditioned reduced fluctuations inside. Do NOT assert physical quantum vacuum energy, genuine Casimir physics, a canonical probability measure on all of mathematics, or that causal generation necessarily breaks time-reversal symmetry.

**Categorical type correction:** In pointed sets \(\mathbf{Set}_*\) the singleton pointed set \(0_*\) is both initial and terminal; it is the coproduct/wedge unit *and* the Cartesian-product unit. That is not the numerical identity 0=1 in a ring and NOT the smash-product unit (which is the pointed two-point set). There is only one endomorphism of \(0_*\), so dynamic content must be supplied in richer objects and source-labelled arrows.

## Analytic leads, derived BEFORE preregistration (development, not blind)

1. Gaussian centered bridge with stationary covariance \(C_{ij}=\rho^{|i-j|}\), \(0<\rho<1\). Conditioning \(X_0=X_d=0\) gives
\[
\operatorname{Var}(X_k|X_0=X_d=0)
=\frac{(1-\rho^{2k})(1-\rho^{2(d-k)})}{1-\rho^{2d}},\quad 0<k<d.
\]
The two-endpoint constraint interaction (joint zero density ratio) is \(p_{both}(0,0)/[p_0(0)p_d(0)]=(1-\rho^{2d})^{-1/2}\). Free-energy-like interaction \(F_{\rm int}(d)=\frac12\log(1-\rho^{2d})<0\) tends to zero as d grows; the covariance correction is the classical Schur complement. This is an engineered centered Gaussian mathematical model, NOT a derivation of a physical Casimir effect or actual BBP digit probabilities.
2. The process with \(C_{ij}=\rho^{|i-j|}\) is time-reversal invariant as a joint Gaussian law **despite having a valid forward Markov construction**. Causal GENERATION alone is insufficient to prove symmetry breaking. Source forcing/observation/conditioning can introduce a distinct arrow.
3. Original BBP seed family \(U_n(s)=U_n(0)+16^ns\) and #513 normalized Fekete energy
\[
E_A(s)=A^{-2}\sum_{A\le i<j<2A}\log|e(U_j(s))-e(U_i(s))|^2.
\]
The exact Haar-seed baseline is \(\int_0^1E_A(s)ds=0\) for every finite A>=2: the nonzero integer difference frequencies \(q_{ij}=16^j-16^i\) uniformly average the integrable logarithmic chord kernel.
4. A more powerful source-*uniform* variance theorem has been derived in development, not yet independently checked on new holds. With \(B_2(x)=\{x\}^2-\{x\}+1/6\), \(\alpha_{ij}=U_j(0)-U_i(0)\), \(q_{ij}=16^j-16^i\), \(g_{pq}=\gcd(q_p,q_q)\), then
\[
\operatorname{Var}_{s\in[0,1]}E_A(s)
=\frac{2\pi^2}{A^4}\sum_{p,q}
\frac{g_{pq}^2}{q_pq_q}
B_2\left(\left\{\frac{q_q}{g_{pq}}\alpha_p-\frac{q_p}{g_{pq}}\alpha_q\right\}\right).
\]
At the original rational source this is \(\pi^2\) times an EXACT rational! A source-independent bound is
\[
\operatorname{Var}E_A(s)\le \frac{\pi^2}{3}\left(\frac{16}{15}\frac{17}{15}\right)^2\frac{A-1}{A^3} < 4.808/A^2.
\]
Proof uses Fourier modes of \(\log|1-e(t)|^2\), gcd resonance, \(\gcd(16^a-1,16^b-1)=16^{\gcd(a,b)}-1\), and geometric sum bounds. No independence assumption.
5. Chebyshev + first Borel–Cantelli imply for Lebesgue almost every seed, \(E_A(s)\to0\) on ALL integer epochs A, which by #513 gives base-16 normality for almost every completion. It says nothing about the single authentic zero seed. The same-forcing coherent seed \(s_*=-\pi/16\) violates exclusion strongly, so an ensemble theorem cannot be promoted to selected normality.
6. To connect "field pressure" with the determinant: source-seed derivative (away from collision seeds)
\[
\frac d{ds}E_A(s)=\frac{2\pi}{A^2}\sum_{i<j}
(16^j-16^i)\cot\big(\pi[U_j(s)-U_i(s)]\big).
\]
Its exponentially large clock factors and singularities explain why seed-average concentration lacks a uniform Lipschitz transfer to s=0.

## Prospectively declared NEW independent probes

- Fresh original-source rational variance coefficients at A=**9 and 11** (A=2,...,8 were used during development), computed by an independently coded exact Fraction route; check the coefficient of π² is rational, nonnegative, obeys the explicit all-A bound.
- At A=9,11 exact integer gcd resonances for EVERY pair of distinct orbit-pair labels, and independent off-diagonal covariance Bernoulli identities; compare with formula using explicit q_p.
- Gaussian boundary-pressure holds: (rho,d,k)=(2/5,4,1),(3/7,7,3),(1/2,5,2), checking exact rational Schur complement and inside vs one-boundary variance, plus interaction log sign. No fake quantum-energy meaning.
- Independent tiny-radix b=2, A=3 seed-averaged quadrature against Bernoulli covariance with arbitrary rational phase offsets, using adequate high resolution (finite numeric calibration only), to check the Fourier sign/normalizations.
- Test source-selection obstruction at all A symbolically: for \(s_*=-\pi/16\), the coherent tail is \(-T_n=O(A^{-2})\), so \(E_A(s_*)\le-2(1-1/A)\log A+O(1)\). Even an exponentially small neighborhood around s* can inherit this bound at finite A; do not infer a pointwise zero-seed estimate.

**Positive criterion:** an actual NEW source-specific deterministic bound \(E_A(0)\ge-o(1)\), or another valid original fixed-h Weyl estimate, with complete carry/Archimedean selection. A variance theorem over ALL seeds is useful mathematics but not that criterion.

**Failure criteria:** equating a categorical zero object to numerical 0=1; treating stationary reversible Gaussian sampling as spontaneous causal asymmetry; claiming physical Casimir forces; treating almost-everywhere seed ensemble estimates as the selected s=0; hiding any source-provenance dependence. Use 11k+ CI only at later integration gate.
