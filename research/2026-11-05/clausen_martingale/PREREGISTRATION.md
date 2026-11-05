# Operation CLAUSEN CUT × CAUSAL ZERO-SEED MARTINGALE — preregistration

**Research-only, 2026-11-05.** Additive child of [SUCC PR #514](https://github.com/femboy2112/SUCC/pull/514), exactly pinned parent \`4243b6c5dda90d49969c62f99b3f3aae73300ebe\`. Preserve genuine four signed BBP poles, literal U0=0, exact rational carries, all source/Lean/archive/production/workflow contracts, and main. Do not merge, tag, release or claim π normality.

## User's research intent

Transport the **exact seed-ensemble** anti-clustering/Fekete energy and "randomized arrows" into the **one chosen zero-seed** BBP orbit. Clarify why Gaussian Markov arrows are both normal-distribution-coded and (after probability integral transform, under ergodicity) sample-path uniform almost surely, without equating Gaussian normality to π's hexadecimal normality. Find a provable seed-conditioning bridge with a falsifiable deterministic arithmetic criterion.

## Mathematical leads developed BEFORE this preregistration (development, not blinded discovery)

- Use authentic source \(u_n=U_n(0)\in\mathbb Q\), and seed \(U_n(s)=u_n+16^n s\). For N=A epoch points \(i=A,\dots,2A-1\), define \(g(t)=\log|1-e^{2\pi it}|^2\) (mean zero and logarithmic singularity), \(Q_{ij}=16^j-16^i\), \(\alpha_{ij}=u_j-u_i\), \(E_A(s)=A^{-2}\sum_{i<j}g(\alpha_{ij}+Q_{ij}s)\). For cylinder \(\mu_K=\mathrm{Uniform}[0,16^{-K})\) set \(M_{ij,K}=\mathbb E_{\mu_K}g(\alpha_{ij}+Q_{ij}s)\).
- Define \(L(t)=\int_0^tg(v)\,dv=-\operatorname{Cl}_2(2\pi t)/\pi=-\Im\operatorname{Li}_2(e^{2\pi it})/\pi\). It is continuous 1-periodic, \(L(0)=0\), and \(\int g=0\). **Exact source/cylinder formula:** \(M_{ij,K}=[L(\alpha_{ij}+Q_{ij}16^{-K})-L(\alpha_{ij})]/(Q_{ij}16^{-K})\). Because \(\alpha_{ij}\in\mathbb Q\), all endpoints are rational phases: root-of-unity Clausen/Bloch-Wigner evaluations. This is classical special-function calculus, not arithmetic signed Weyl decay.
- Three **causal cut classes** for A≤K≤2A: (a) i≥K: M=0 exactly; (b) i<K≤j: \(q_{ij}16^{-K}=16^{j-K}-\delta_i\), \(\delta_i=16^{i-K}\). Thus \(M=-[q16^{-K}]^{-1}\int_{\alpha_{ij}-\delta_i}^{\alpha_{ij}}g\). A universal \(|\int_J g|\le2\delta(1+\log(1/\delta))\) for any arc length \(\delta≤1/16\) leads to a SOURCE-INDEPENDENT summed cross-cut bound
\[
\left|A^{-2}\sum_{A≤i<K≤j<2A}M_{ij,K}\right|
\le\frac{C_\times}{A^2},\quad
C_\times=\frac{512}{225}\left(\frac1{15}+\frac{16\log16}{225}\right)\approx0.60035648.
\]
(c) i<j<K: the 'actualized past' contribution contains the genuine source \(\alpha_{ij}\), regularized over an arc of length q16^-K∈(0,1/16). Bounding its absolute average using the same local log integral gives a universal magnitude \(\le [(1+\log(16/15))t(t-1)+(\log16/3)t(t-1)(t+1)]/A^2\), t=K-A. Hence uniform seed-ensemble neutrality holds for t=o(A^(2/3)).
- **Sharp hostile control:** for unforced dynamics r=0, \(\alpha_{ij}=0\) and the past contribution has explicit expansion
\[
\mathbb E_{\mu_{A+t}}E_A(s)=
-\frac{\log16}{3}\frac{t(t-1)(t+1)}{A^2}
+O(t^2/A^2+A^{-2})
\]
uniformly 1≤t≤A. Consequently t~cA^(2/3) yields limit \(-(\log16/3)c^3\). This means the \(A^{2/3}\) neutrality window cannot be universally improved in exponent without source-specific arithmetic input. **This is a baseline zero-forcing countermodel, not a BBP original lower bound.**
- Exact conditional martingale: under Haar seed s, the conditional expectation of E_A given its first K radix-16 digits is a martingale. Full ensemble \(\mathbb EE_A=0\), Var≤4.808/A² from #514, but a specific zero-prefix path may be exceptional; source-independent conditional concentration and half-arc hard-core cannot prove pointwise zero-seed Fekete.
- Wall's rational-addition theorem means normality of \(\pi/16+s\) for ANY rational s is equivalent to normality of \(\pi/16\). It permits alternate rational seeds in a proof without *solving* source-selected distribution. For terminating hex s, the circle orbit is literally identical to zero for n beyond its denominator's radix depth.
- Gaussian arrow model \(\mathsf K(x,dy)=\mathcal N(\rho x,1-\rho^2)\) fits Markov category theory (Fritz, Advances in Mathematics 2020). Stationary Gaussian \(X_n\), probability-integral transform \(V_n=\Phi(X_n)\) has uniform marginals and almost-sure temporal equidistribution via ergodicity, while covariance \(\rho^d\) gives \(I(X_0;X_d)=-\tfrac12\log(1-\rho^{2d})=-F_{\mathrm{int}}(d)\). The stationary process is reversible even if sampled with forward arrows. This is stochastic MODEL FACT, not a theorem that the original deterministic U0=0 BBP orbit is normal.

## Prospectively declared independent checks, not yet run

1. Genuine original four-pole BBP rational source holds: **A=7,11,13** (these A not used for this new conditional-pressure calculation), K=A, A+1, A+2, floor(3A/2), 2A, 2A+3; evaluate exact source \(\alpha_{ij}\) and the explicit Clausen formula at high mpmath precision. Check zero below K=A, cross-cut O(C/A²), and full pressure decomposition at every K. Numeric Clausen tests are CALIBRATION, not exact interval authority.
2. Independently derive conditional mean via direct high-precision numerical integration of g over a *noninteger phase arc* for some small-epoch cross pairs; compare with Clausen primitive including correct sign. Use at least 4 source-labeled pair examples and one collision-near-cusp.
3. Unforced baseline pressure onset at **(A,t)=(64,8),(125,20),(216,36)**, chosen *before running*. Check predicted scale and sign; do not fit constants to these data. This independently falsifies a universal stronger neutrality window.
4. Source-Fraction exact identity \(U_n(s)-u_n=16^ns\), branch periodicity and rational-seed character relation for n up to 60. A new low-level test must preserve unwrapped rational source first.
5. Gaussian Markov kernel: exact Fraction Schur complement/MI covariance identity for \(\rho=2/5,3/7\), test stationary covariance/detailed balance and deterministic all-zero innovations counterseed.
6. Root-style standalone tests, exact tracked source blobs and reproducible receipts. Full 11k+ native suite only at integration gate. CI status tied to exact final SHA.

## Claim firewall and verdict-changing probe

A genuine bound \(E_A^{\rm BBP}(0)\ge-o(1)\) or original fixed-h Weyl estimate is still OPEN. The new cut bound and a.e. seed concentration are source-UNIFORM, hence cannot prove selected normality; r=0 and coherent wrong seed explicitly falsify that inference. A selected proof must estimate the *already causally resolved* (i<j<K) logarithmic source-phase interactions, rather than only neutral future-crossing pairs. If the 'randomized arrow' merely makes typical trajectories, classify that as a different theorem; no quantum vacuum or causal symmetry breaking is assumed.

**Next verdict-changing mathematical lamp:** the signed digit-resolution/carry-conditioned drift of the past-past Clausen regulator at K≈A+t, including source-specific complex/Gaussian angular orientation and all-scale π orbit pair collisions. Prove a nonnegative integrated drift or construct an exact zero-seed obstruction. Never manufacture a claimed π-normality theorem.
