# SUCC — Fibonacci information time × the epicycle-demon observer
Research date: 2026-10-30. DRAFT RESEARCH ONLY. This is an additive standalone note from Main XVI, commit e18ba565ca540adb7edf3292f5593929e76d91c5. No change to authentic four-pole BBP, zero-seeded orbit, histories, theorem contracts, workflows, production code, or main. Base-16 normality of π and RH remain OPEN. No physical Maxwell demon or gravitational model is asserted.

## Provenance and the author's hypothesis

The author proposes that a static Harmonic / Golden Ratio / Euler–Mascheroni triangle, once extruded in time, could select Fibonacci temporal transport; further, an observer committed to an incorrect theory might preserve the appearance of order by expending ever more information on exceptions and frame resets. This is the **epicycles-versus-ellipses / Maxwell-demon** analogy. We formalize the strongest conditional version and preserve decisive negative controls.

Read-only ancestors: SUCC [#379](https://github.com/femboy2112/SUCC/pull/379) (Gamma/Fibonacci), [#390](https://github.com/femboy2112/SUCC/pull/390) (time extrusion), [#391](https://github.com/femboy2112/SUCC/pull/391) (zero spine), [#392](https://github.com/femboy2112/SUCC/pull/392) (two-panel Gamma/Mellin), [#393](https://github.com/femboy2112/SUCC/pull/393) (Lorentz clocks), [#394](https://github.com/femboy2112/SUCC/pull/394) (arithmetic mass shell), [#395](https://github.com/femboy2112/SUCC/pull/395) (Stoneham normal controls), and [#396](https://github.com/femboy2112/SUCC/pull/396) (T-action/frame resets). These branches are references, not imported premises.

## FEO-01: the Golden fixed point is a Fibonacci contraction factor (EXACT)

At the authentic rank-two, unit-clock Gamma–Poisson boundary, the endpoint PGF is

\[
G(z)=(2-z)^{-2},\qquad
q=\varphi^{-2}=(3-\sqrt5)/2,\quad G(q)=q.
\]

The nontrivial fixed-point polynomial is \(q^2-3q+1=0\). Independently, the Fibonacci transfer

\[
S=\begin{pmatrix}0&1\\1&1\end{pmatrix},
\qquad
B=S^2=\begin{pmatrix}1&1\\1&2\end{pmatrix}
\]

has precisely the characteristic polynomial \(t^2-3t+1\), hence eigenvalues \(\varphi^{\pm2}\); its contracting eigenvalue is q. Moreover, \(B^n=\left(\begin{smallmatrix}F_{2n-1}&F_{2n}\\F_{2n}&F_{2n+1}\end{smallmatrix}\right)\). The integer quadratic form \(Q(u,v)=u^2+uv-v^2\) obeys \(Q(Bx)=Q(x)\) and \(Q(Sx)=-Q(x)\). The primitive S step is anti-isometric; B is a proper orthochronous Lorentz boost of rapidity \(\eta_F=2\log\varphi\) in a suitable linear basis.

**Firewall:** equality of characteristic polynomials does NOT derive an operational clock, physical proper time, or a covariance law of selected π carries. The golden fixed point belongs to a separately declared auxiliary offspring iteration.

## FEO-02–04: exact original-source Fibonacci information geometry

Keep the original four-pole **positive** carrier:

\[
Q_B(x)=4-2e^{-3x}-e^{-4x}-e^{-5x},\quad
R(a)=4/a-2/(a+3)-1/(a+4)-1/(a+5)
=\frac{15a^2+121a+240}{a(a+3)(a+4)(a+5)}.
\]

For \(a>0\), \(\mu_a(dx)=e^{-ax}Q_B(x)\,dx/R(a)\), with \(Q_B(x)=15x-\frac{59}{2}x^2+O(x^3)\), \(R(a)=15a^{-2}-59a^{-3}+O(a^{-4})\), \(E_a X=-R'(a)/R(a)=2/a-59/(15a^2)+O(a^{-3})\), and Fisher information \(I(a)=\partial_a^2\log R(a)=2/a^2+O(a^{-3})\).

**Declared** Fibonacci sample schedule (NOT selected by BBP): \(n_k=F_{2k}\), \(a_k=8F_{2k}-7\), \(k\ge1\). Then \(a_{k+1}/a_k\to\varphi^2\) and the Fisher path increment tends to \(2\sqrt2\log\varphi\).

The exact Jeffreys divergence between these specified posteriors is
\[
\mathcal J(a,b)=D_{\rm KL}(\mu_a\Vert\mu_b)+D_{\rm KL}(\mu_b\Vert\mu_a)
=(b-a)\big(E_aX-E_bX\big).
\]
Consequently
\[
\mathcal J(a_k,a_{k+1})\longrightarrow
2(\varphi^2+\varphi^{-2}-2)=2.
\]
Let \(q=\varphi^{-2}\). Using the exact Binet formula \(F_{2k}=(q^{-k}-q^k)/\sqrt5\) and the source expansion, for the authentic carrier and a Gamma-matched fake \(R_f(a)=15/a^2\):
\[
\begin{aligned}
\mathcal J_B(k)&=2+\frac{151(\sqrt5-1)}{48}q^k+O(q^{2k}),\\
\mathcal J_f(k)&=2+\frac{35(\sqrt5-1)}{8}q^k+O(q^{2k}),\\
\mathcal J_B(k)-\mathcal J_f(k)&=-\frac{59(\sqrt5-1)}{48}q^k+O(q^{2k}).
\end{aligned}
\]
The asymptotic limit 2 is universal for this rank and sampling ratio, while the first defect distinguishes the original Q''(0)=-59 from the Gamma-matched fake. A higher-jet-matched mutant can preserve the same first defect: it is not a unique source identifier. The divergence is coordinate-independent for the specified posterior pair, but the Fibonacci **sampling protocol** is freely declared.

Binet + \(H_N=\log N+\gamma+o(1)\) gives an exact harmonic offset:
\[
\lim_{k\to\infty}\big(H_{F_{2k}}-k\eta_F\big)
=\gamma-\tfrac12\log5.
\]
The two-panel tiling of #392 has \(D_{j,l}=H_{j+l+1}-\gamma-\lambda^{j+l+2}\), \(\lambda=\varphi^{-1}\). On the **chosen** diagonal \(j+l=F_{2k}-1\),
\[
\lim_{k\to\infty}\big(D_{j,l}-k\eta_F\big)=-\tfrac12\log5.
\]
Finally \(r(F_{2k})=R(8F_{2k}-7)\sim(75/64)e^{-2k\eta_F}\) and
\[
R(a_k)/R_f(a_k)=1-\frac{59\sqrt5}{120}e^{-k\eta_F}+O(e^{-2k\eta_F}).
\]
These results use no signed zero-seeded π phases or carries.

**Negative control:** the native weighted Pascal recurrence has characteristic roots 1 and -g (with f+g=1), NOT Fibonacci roots. Unweighted diagonal path counting is insufficient to derive Fibonacci as a native time law.

## FEO-05: quantitative wrong-observer evidence theorem (CLASSICAL consequence, PROVED conditionally)

Let x be an arbitrary **normal base-b** digit sequence. Fix integer memory \(m\ge0\), and a **fixed before observation** full-support Markov predictor \(p(d\mid w)>0\) for every length-m word w and next digit d. Uniform reference \(U(d\mid w)=1/b\). Define the prequential Bayes/likelihood factor
\[
B_N(p:U)=\prod_{t=m+1}^{N}
b\,p(x_t\mid x_{t-m}\dots x_{t-1}).
\]
Normality of all \(m+1\)-digit blocks implies
\[
\boxed{\lim_{N\to\infty}\frac{\log B_N}{N}
=-b^{-m}\sum_{w\in A^m}D_{\rm KL}(U_b\Vert p(\cdot\mid w))
=:-C(p).}
\]
Proof: group the logarithm into the finitely many context/next-digit cells, use each limiting frequency \(b^{-(m+1)}\), and apply Gibbs' inequality. If at least one conditional forecast differs from uniform, \(C(p)>0\); for any \(0<\epsilon<C(p)\) there is a finite (generally ineffective) \(N_0(x,p,\epsilon)\) with \(B_N\le e^{-(C(p)-\epsilon)N}\) for all \(N\ge N_0\). Any **fixed finite collection** of wrong predictors has an eventual common horizon by taking the maximum. This is the precise restricted sense in which a degenerate observer's model faces insurmountable evidence.

Strict positivity can be relaxed carefully: a fixed zero-probability context transition is eventually observed on a normal stream, ending that predictor's likelihood. No convergence *rate*, horizon algorithm, or universal bound follows from normality itself.

The stronger equivalence of normality with finite-state dimension 1 and incompressibility by lossless finite-state encoders is classical; it is **not** a new SUCC theorem: Schnorr–Stimm and later KL divergence work, e.g. [STACS 2020](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.STACS.2020.51), [TCS 2013](https://doi.org/10.1016/j.tcs.2013.01.019), [MFCS 2023](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.MFCS.2023.65).

## FEO-06: exact relative limit on ordered corridors, and no absolute cutoff

Fix word w of length \(\ell\). Normality yields \(C_w(N)=b^{-\ell}N+o(N)\), where \(C_w\) counts starting positions <N. If [a,a+L) avoids w, then \(0=C_w(a+L)-C_w(a)=b^{-\ell}L+o(a+L)+o(a)\). Hence every word-avoiding interval ending at n=a+L has \(L=o(n)\); equivalently the longest such interval before N is o(N).

For any **fixed** periodic target of period p, pick a length-(p+1) word absent from its p distinct windows. Every exact matching corridor must avoid this word except for a bounded edge, so its maximal length is also o(N), **conditional on normality**. The statement is per fixed pattern/period, not uniform for p growing with N. It is necessary but not sufficient for normality: weaker models can avoid macroscopic periodic corridors yet be nonnormal.

**Refuted absolute cutoff:** every normal sequence contains every fixed finite word infinitely often, including \(0^\ell\) for arbitrarily large \(\ell\) and arbitrarily late positions. Prepending any finite prescribed prefix to a normal sequence preserves normality. Therefore no universal last ordered patch, bounded run length, or computable finite observer horizon follows.

**Refuted algorithmic-randomness leap:** computable normal numbers exist (e.g. Champernowne); a sufficiently capable algorithm-informed observer can predict all their digits. Normality constrains finite-state asymptotic frequencies, not arbitrary computational prediction. See [PNAS 2012](https://pmc.ncbi.nlm.nih.gov/articles/PMC3511067/) for computable normal sequences and arbitrarily slow convergence.

## FEO-07: the epicycle/demon ledger (DECLARED operational model, not physical law)

To make model-repair testable, predeclare a prefix-free encoding of model M, exceptions E, selection/resets S, and any side-channel. For observations scored **before** seeing the next digit define the proposed ledger
\[
L_N(M,E,S)={\rm codebits}(M,E,S)-\sum_{t\le N\,{\rm actually\ scored}}\log_2 p_t(x_t).
\]
Charge all unscored positions, policy descriptions, reference-frame recentering information and held-out data exposure appropriately before comparing with uniform \(N\log_2 b\). Without such rules, hindsight exception-fitting is cheap by definition and proves nothing. This is an **observer-relative** measurement, not a universal Kolmogorov lower bound.

In a declared probabilistic ensemble with selection record S, \(H(X)=H(X\mid S)+I(X;S)\) accounts for apparent conditional entropy reduction. A deterministic arithmetic digit stream has no thermodynamic heat/temperature. Maxwell's demon has physical information/erasure requirements only after a physical apparatus is specified; see [Mandal–Jarzynski PNAS 2012](https://pmc.ncbi.nlm.nih.gov/articles/PMC3406850/) and [Landauer experimental test, Nature 2012](https://doi.org/10.1038/nature10872). No heat/entropy law for π is claimed.

Countermodels:
- A normal stream with an arbitrarily long biased prefix refutes universal finite cutoff.
- A normal computable stream refutes 'all observers require ever-growing outside information'.
- A periodic de Bruijn sequence has uniform statistics through a given finite word length but is nonnormal at higher lengths.
- Selection/frame-reset without recording costs can fabricate apparent order.
- The authentic four-pole positive source is also present with coherent same-forcing counterseed \(s_*=-\pi/16\), so no source-only normality implication survives.

## Claim boundary, next proof gate

**DISCLOSED**: Fibonacci/Gamma algebra, four-pole Jeffreys asymptotics for the **declared clock**, conditional normality evidence and corridor theorems (classical analysis). **PROPOSED**: complexity-accounted epicycle ledger. **REFUTED**: absolute universal cutoff, normality implies algorithmic unpredictability, Maxwell demon implies arithmetic heat, source-only clock implies selected normality. **UNVERIFIED/OPEN**: native Fibonacci clock selection; actual base-16/base-3 π normality; RH; physical Lorentzian dynamics.

A useful SUCC advance would be a **zero-seed-sensitive, original-source, all-horizon** selected Fourier or grid-occupancy theorem for \(U_0=0\), including full literal radix-16 carries and two-time phase tensor. Predeclare comparisons against coherent \(s_*=-\pi/16\), Gamma-matched and higher-jet-matched sources, prior resets, finite-period de Bruijn controls, and normal Stoneham c=3/5 controls from #395. A conditional theorem that merely says what normality would imply must not be promoted into a proof of π normality.

Validation is scoped to the accompanying standalone Python probe; full SUCC root AGENTS gates, hosted CI, Lean and external peer review have NOT run. Do not merge blindly.
