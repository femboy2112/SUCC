# Completed Weil transport from Pascal/prime heat: a source-identified signed approximation

**Checkpoint:** October 14, 2026, mathematical research branch `research/real-place-weil-identification-2026-10-14`; parent `research/prime-form-heat-mellin-2026-10-14@53934b3a5a980bb0f6e1001241822da5b6d928e5`, transitively stacked on Pascal/Gamma PR #67 and structural-coupling PR #65. `main` is not changed. **RH PROVED: NO.** These constructions do not prove the positivity of the completed Weil form, the conjectural Suzuki global-operator limit, or empirical physical source authentication. All uses of a *full Weil/spectral zero identity* are attributed to the established Weil explicit formula (Suzuki 2025, Eq. (3.3)), **not silently re-proved from finite code**. Zero positions are never inputs.

## 0. Intake, predecessors, boundary conditions and actual target

The user asked to continue the new Pascal/prime heat/Gamma program all the way to the *completed signed Weil/Suzuki form*, preserving half-density, prime powers, pole, Gamma, source and test-function domain before addressing the global sign. Initial repo inspection showed the target already existed in `main`: [`research/2026-10-13/SWM_E38_ARITHMETIC_POLARIZATION/DOSSIER.md`](../2026-10-13/SWM_E38_ARITHMETIC_POLARIZATION/DOSSIER.md) **E38** explicitly writes the full Weil distribution and its differentiated screw-kernel bridge. We **do not claim to have discovered that formula**. Main's signed structure is correct under Suzuki's official 2025 Eq. (3.3). E38's counterexamples kill sign-squared feature Gram identification and its signed `Q(v,w)=<S_av',w'>` bridge remains positive *only under an RH-hard additional hypothesis*.

Source precursor PH-01–PH-15 established: (i) authentic `p q+b` integer residue carriers that also exist for composites; (ii) IID Pascal random walk -> Gaussian heat, with correlated-step negative controls; (iii) Gaussian Fourier/Poisson rotation; (iv) `Gamma_R(s)=π^(-s/2)Γ(s/2)` with actual Mellin/Haar normalization; (v) genuine prime-power heat `J(t)=sum Λ(n)exp(-πtn²)`; (vi) one Gamma gate after assembling finite Euler chains; and (vii) the Re(s)>1 vs finite-prime Re(s)>0 domain obstruction. No earlier branch had supplied a *quantified finite signed Gamma ladder to the complete Weil distribution* or *a source-first executable double-integrated Suzuki screw potential with error bound*. This addition does both and stresses their positivity limits.

**External sources:**

- Masatoshi Suzuki, *On the Hilbert space derived from the Weil distribution*, Canadian Journal of Mathematics (published online 2025), §3, Eq. (3.3): https://www.cambridge.org/core/journals/canadian-journal-of-mathematics/article/on-the-hilbert-space-derived-from-the-weil-distribution/FD33EBD117A6B448053450DD8D62ADB6 . This gives the exact normalization and the distributional Weil identity. Several other key explicit maps appear in §§1 and 3.
- Masatoshi Suzuki, *Weil's quadratic form via the screw function*, arXiv:2606.09096v3 (Sept 25, 2026): https://arxiv.org/abs/2606.09096 . The finite interval realizations and continuity of the lowest eigenvalue do **not** prove the conjectural global limit or RH; see repo `SUZUKI_2606_09096_FRONTIER.md` on PR #62.
- NIST DLMF Gamma §§5.2,5.9 and zeta §§25.4–25.5: https://dlmf.nist.gov/5.9, https://dlmf.nist.gov/25.4, https://dlmf.nist.gov/25.5 . The Gamma logarithmic derivative, Gaussian integral, standard completion and theta identities are CLASSICAL IMPORTS.
- Connes–Consani (2023) and finite Galerkin Guinand–Weil techniques (including arXiv:2607.02828) are prior work; academic priority of the particular source-typed, corrected-ladder error bound is **UNVERIFIED**. No independent novel theorem claim.

All numerical work is explicit `mpmath` evaluation, with genuine **analytic** inequalities marked separately; high precision by itself is never advertised as certified interval arithmetic.

## 1. The fundamental correction: a Mellin product is not a completed logarithmic derivative

For actual primes and every `t>0`, define the source measure and heat observable

\[
\nu=\sum_{p\text{ prime}}\sum_{k\ge1}(\log p)\,\delta_{k\log p},\qquad
J(t)=\int_0^\infty e^{-\pi t e^{2x}}\,d\nu(x)
=\sum_{n\ge2}\Lambda(n)e^{-\pi t n^2}.
\]

The Gaussian guarantees convergence of `J(t)` for `t>0`. For `Re(s)>1`, absolute convergence and Tonelli/Fubini give

\[
\boxed{\mathcal M_tJ(s)=\Gamma_{\mathbb R}(s)\int e^{-sx}\,d\nu(x)
=\Gamma_{\mathbb R}(s)\left(-\frac{\zeta'(s)}{\zeta(s)}\right),\qquad
\Gamma_{\mathbb R}(s)=\pi^{-s/2}\Gamma(s/2).}\tag{CW-01}
\]

**Source uniqueness scope (CW-02, CLASSICAL/DERIVED).** Fix `σ>1`; `e^{-σx}\nu(dx)` is a finite positive measure. Values of `Γ_R(σ+iu)^(-1) M_tJ(σ+iu)` for **all real u**, not finitely many selected frequencies, form its Fourier transform. By uniqueness of the Fourier transform of finite Borel measures, these data determine the true-prime atomic source *uniquely* within the stated class. This does **not** mean an embedded finite observer can execute the entire vertical line or that the sensor/source law is externally authenticated. A finite list of Mellin samples is NOT an all-source certificate.

For `σ>1` and integer `N>=3`, exact prime powers up to N give an analytical remainder

\[
\boxed{\left|\sum_{n>N}\Lambda(n)n^{-s}\right|
\le N^{1-\sigma}\left(\frac{\log N}{\sigma-1}+\frac1{(\sigma-1)^2}\right),\quad \sigma=\Re(s)>1.}\tag{CW-03}
\]

Proof: `Λ(n)≤log n` and `log x/x^σ` decreases on `x>=N>=3`; bound the discrete tail by its elementary integral. This is NOT a uniform bound as σ↓1.

The previous PH Mellin **product** is not Weil positivity and not even the target *logarithmic derivative*. To build the completed symmetric resolvent, use the separate operations

\[
\xi(s)=\tfrac12s(s-1)\Gamma_{\mathbb R}(s)\zeta(s),\qquad
\boxed{2\frac{\xi'(s)}{\xi(s)}=
\frac{2}{s}+\frac{2}{s-1}
+\psi(s/2)-\log\pi
-2\frac{\mathcal M_tJ(s)}{\Gamma_{\mathbb R}(s)}.}\tag{CW-04}
\]

There are **four signed and separately sourced terms**: two completed-pole terms, Gamma log derivative, and **negative** normalized heat prime current. This is a classical equality on `Re(s)>1`, no zeros read. The experimentally false shortcut `Gamma_R * (-ζ'/ζ)` -> `2ξ'/ξ` is a *type error*: multiplication versus logarithmic differentiation; mutant tests reject it.

## 2. Half-density and the exact compact Weil test domain

Take `\mathcal D=C_c^\infty(\mathbb R)`. For functions `F` on `\mathbb R_+`, choose `\mathcal M F(s)=\int_0^\infty F(x)x^{s-1}\,dx` and

\[
(UF)(u)=e^{u/2}F(e^u),\quad
F^\sharp(x)=x^{-1}\overline{F(1/x)},\quad
U(F^\sharp)(u)=\overline{UF(-u)}.
\]

Then `U:L²(dx)->L²(du)` is unitary and `\mathcal M F(1/2+it)=\int (UF)(u)e^{itu}du`. This is E38's source-preserving half-density chart, *not a zero observer*. An independent numerical oracle integrates an explicit multiplicative tent source against `x^{s-1}dx`, recovering the additive tent Fourier transform. Replacing exponent `-1/2` visibly fails the chart.

For `h\in\mathcal D`, Weil's **arithmetic-side** distribution is

\[
\boxed{\begin{aligned}
W_\zeta(h)={}&\underbrace{\int_{\mathbb R}h(x)(e^{x/2}+e^{-x/2})\,dx}_{P(h)}\\
&-\underbrace{\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}[h(\log n)+h(-\log n)]}_{R_\mathrm{prime}(h)}\\
&-\underbrace{(\gamma+\log4\pi)h(0)
+\int_0^\infty\frac{e^{-x/2}[h(x)+h(-x)-2e^{-x/2}h(0)]}{1-e^{-2x}}\,dx}_{\text{signed Archimedean deduction}}.
\end{aligned}}\tag{CW-05}
\]

The final bracket must be read as one Archimedean contribution with the displayed minus signs; its `h(0)` contact cannot be dropped. The prime sum is **locally finite** for compact `h`. For `v,w\in\mathcal D_a=C_c^\infty(-a,a)`, `h=v*\widetilde w` has support in `[-2a,2a]`; therefore only true prime powers `n≤e^{2a}` can contribute (equality at a smooth support endpoint is zero). `Q_\zeta(v,w)=W_\zeta(v*\widetilde w)` is the *actual completed* signed Weil form under the external Weil explicit formula. A linearly transported covariance or generic positive Hilbert Gram is not enough to identify it.

**Arch test-domain regularization (CW-06, CLASSICAL/DERIVED).** For `h\in C_c^2(\mathbb R)`, define

\[
D_h(x)=h(x)+h(-x)-2e^{-x/2}h(0).
\]

Symmetric first-derivative cancellation yields `D_h(x)=O(x)` near zero, so the singular factor `e^{-x/2}/(1-e^{-2x})\sim1/(2x)` is removable. The distribution is well defined on this class, and `W(h)` on `h=v*\widetilde v` with `v\in H^1_0(-a,a)` extends through the existing E38 signed quadratic representation. The 2025 Eq. (3.3) equality on smooth compact tests remains the **imported global Weil identity**; the C² extension uses approximation/continuity and the standard zero-counting bound, not a finite test.

## 3. Crucial new transport derivation: Gamma digamma -> exact Weil contact term

With the Fourier convention `\widehat h(u)=\int h(x)e^{-iux}dx`, let

\[
\Omega(u)=\operatorname{Re}\psi\left(\tfrac14+\tfrac{iu}{2}\right)-\log\pi,
\quad
\mathcal A(h)=\frac1{2\pi}\int_{\mathbb R}\widehat h(u)\Omega(u)\,du.
\]

Euler's integral for `ψ(z)` on `Re(z)>0` gives, after combining the conjugate terms,

\[
\Omega(u)=-\gamma-\log\pi+
\int_0^\infty\frac{e^{-y}-e^{-y/4}\cos(uy/2)}{1-e^{-y}}\,dy.
\]

Truncate the y-integral near zero **before** interchanging Fourier operations, combine the `h(0)` terms, and let the truncation vanish. With `y=2x` the resulting real-space distribution is

\[
\mathcal A(h)=(-\gamma-\log\pi)h(0)
+\int_0^\infty\frac{2e^{-2x}h(0)-e^{-x/2}[h(x)+h(-x)]}{1-e^{-2x}}\,dx.
\]

To express it with the cancellation built directly into `D_h`, use the **exact contact identity**

\[
2\int_0^\infty\frac{e^{-2x}-e^{-x}}{1-e^{-2x}}\,dx=-2\log2.
\]

Consequently

\[
\boxed{\mathcal A(h)=-(\gamma+\log4\pi)h(0)
-\int_0^\infty\frac{e^{-x/2}}{1-e^{-2x}}D_h(x)\,dx.}\tag{CW-07}
\]

This **recovers E38/Suzuki's precise Gamma component**, including the missing `2log2` if one naively retains only `log π`. The derivation uses only the stated real Gaussian/Gamma source and classical digamma analysis. At **one** prime one cannot place a separate Gamma term: the same `\Omega` acts once on the fully assembled source.

**Conductor/parity mutation (CW-08, CLASSICAL).** A primitive Dirichlet completion with conductor q and parity `ε\in{0,1}` has log-Gamma spectral symbol
`Ω_(q,ε)(u)=log(q/π)+Re ψ(1/4+ε/2+iu/2)`.
Its change from zeta is the conductor contact `log(q)h(0)` plus the regular parity kernel

\[
\int_0^\infty[h(x)+h(-x)]
\frac{e^{-x/2}(1-e^{-\epsilon x})}{1-e^{-2x}}dx.
\]

This is only the **Archimedean adapter**; it is not a full primitive-character L-function or a certified root number. The test checks both the spectral and exponential-resolvent sides. Conductor and parity cannot be guessed from the shape of the Pascal triangle.

## 4. Exact finite Gamma-mode ladder and the signed C² remainder theorem

For every x>0,

\[
\frac{e^{-x/2}}{1-e^{-2x}}=\sum_{j=0}^\infty e^{-(2j+1/2)x}.
\]

These positive scalar terms are a **real Gamma spectral ladder**, but the full signed Weil form contains the subtracted `D_h(x)`. Let `\mathcal A_J` keep its contact term and its first J rungs. Define `a_J=2J+1/2`, `H=\|h\|_\infty`, `M_2=\|h''\|_\infty`, and `h_0=|h(0)|`.

**CW-09 (PROVED LOCAL / SIGNED BOUND):** for `h\in C_c^2`,

\[
\boxed{|\mathcal A(h)-\mathcal A_J(h)|
\le C_h\left(\frac1{2a_J}+\frac1{a_J^2}\right),
\quad C_h=\max(h_0+M_2,2(H+h_0)).}\tag{CW-09}
\]

*Proof.* On `0<x≤1`, symmetric Taylor gives `|D_h(x)|≤(h_0+M_2)x`; on `x≥1`, direct supremum gives `|D_h(x)|≤2(H+h_0)x`. The omitted geometric ladder is `e^{-a_Jx}/(1-e^{-2x})`. The elementary `1-e^{-2x}≥2x/(1+2x)` bounds `x/(1-e^{-2x})≤x+1/2`. Integrate the resulting exponential moment: `\int_0^\infty (x+1/2)e^{-a_Jx}dx=a_J^{-2}+(2a_J)^{-1}`. QED. All rational inputs to the implementation yield exact rational bounds, distinct from numerical quadrature values.

The leading error at x≈0 is a **boundary term**. Since

\[
D_h(x)=h(0)x+E_h(x),\qquad
|E_h(x)|\le\left(M_2+\tfrac14 h_0\right)x^2,
\]

we can subtract it analytically, not fit a numeric constant. Set

\[
\widetilde{\mathcal A}_J(h)=\mathcal A_J(h)-\frac{h(0)}{2a_J}
=\mathcal A_J(h)-\frac{h(0)}{4J+1}.
\]

**CW-10 (PROVED LOCAL / ACCELERATED `O(J^-2)`):**

\[
\boxed{|\mathcal A(h)-\widetilde{\mathcal A}_J(h)|
\le\frac{h_0}{a_J^2}+
\left(M_2+\frac{h_0}{4}\right)
\left(\frac1{2a_J^2}+\frac2{a_J^3}\right).}\tag{CW-10}
\]

*Proof.* Since `1-e^{-2x}≤2x`, `0≤x/(1-e^{-2x})-1/2≤x`; likewise `x²/(1-e^{-2x})≤x²+x/2`. Substitute `D_h=h(0)x+E_h`, integrate `\int x^k e^{-a_Jx}dx=k!/a_J^{k+1}` and use the preceding C² bound. This is uniform for all compact C² h with the stated seminorms. No sign assumption enters.

**CW-11 (PROVED LOCAL / UNIFORM H¹ FORM NORM).** Let `v,w\in C_c^\infty(-a,a)`, extend them by 0, and `h=v*\widetilde w`. Then

\[
|h(0)|\le\|v\|_2\|w\|_2,\quad
\|h\|_\infty\le\|v\|_2\|w\|_2,\quad
\|h''\|_\infty\le\|v'\|_2\|w'\|_2.
\]

The last inequality follows from `h''=-v'*\widetilde{w'}` in distributions, followed by Cauchy–Schwarz. The prime term is finite on each fixed interval and has no J-truncation. Denote the full Weil form by Q and its Gamma-only corrected J-rung form by `\widetilde Q_J`. Then

\[
\boxed{|Q(v,w)-\widetilde Q_J(v,w)|
\le\varepsilon_J\|v\|_{H^1}\|w\|_{H^1},}\tag{CW-11}
\]

with the *explicit* rational coefficient

\[
\varepsilon_J=\max\left\{
\frac9{8a_J^2}+\frac1{2a_J^3},
\frac1{2a_J^2}+\frac2{a_J^3}
\right\}=O(J^{-2}).
\]

The result extends to each fixed `H^1_0(-a,a)` by density; the canonical form remains **signed**. This is a quantified whole-test-space limit statement in a stated Sobolev topology, not finite Gram sampling, a positivity factorization or a claim about the maximal spectral operator domain.

For calibration, use the real tent `v_a(x)=(1-|x|/a)_+` on `[-a,a]`, `v_a\in H^1_0`. Its autocorrelation is a compact C² cubic B-spline with exact `h(0)=2a/3`, `\|h\|∞=2a/3` and `\|h''\|∞=2/a`. The tests independently integrate the complete Archimedean expression and evaluate the corrected J-level ladder at `a=1/4,2/5,4/5`; every observed error is below the exact rational bound. Independent Fourier/digamma quadrature is also tested, but **its finite-frequency cutoff itself is not a certified interval tail**.

## 5. A resolvent calibration that reads no nontrivial zero locations

Let `h_a(x)=e^{-a|x|}` with a>1/2, set `s=a+1/2>1`. This is positive definite, with `\widehat h_a(u)=2a/(a^2+u^2)`. It is **not** compact smooth, so it is not used to assert an unrestricted Weil form domain; rather the standard explicit-formula regularization and absolute convergence under `s>1` justify this separate test family.

The Poisson integral for the digamma spectral symbol, independent real-space Gamma renormalization, and the explicit resolvent series all yield

\[
\boxed{\mathcal A(h_a)=\psi(s/2)-\log\pi.}\tag{CW-12a}
\]

The two pole terms give `2/s+2/(s-1)`, and the prime impulse contributes `-2\sum_{n\ge2}\Lambda(n)n^{-s}`. Thus

\[
\boxed{W_\zeta(h_a)=
\frac2{s} +\frac2{s-1}+\psi(s/2)-\log\pi-2\sum_{n\ge2}\Lambda(n)n^{-s}
=2\frac{\xi'(s)}{\xi(s)},\quad s>1.}\tag{CW-12b}
\]

This identity is **zero-independent as a construction and evaluation**: `ξ'/ξ(s)` on `Re(s)>1` is evaluated from Gamma and ζ, never a zero list. It does not extend by pointwise limit to the critical strip; the prime series loses its absolute convergence at σ=1. A second route integrates the Cauchy Fourier transform against `Ω` directly. `CW-03` makes finite source truncation errors explicit. Numerical agreement is corroboration of the classical identity, not a proof of RH or of the full test-function formula.

## 6. Direct source-first Suzuki screw potential, no zeros needed

For R≥0 define the *wedge* `\ell_R(x)=(R-|x|)_+`. It is Lipschitz compact, and the regularized E38/Suzuki arithmetic expression `W_\zeta(\ell_R)` is finite. Define the even function

\[
\boxed{\Psi(R)=\tfrac12 W_\zeta(\ell_R),\qquad \Psi(-R)=\Psi(R),\ \Psi(0)=0.}\tag{CW-13}
\]

No zeros enter this definition. Formally, the distributional second derivative of `\ell_R(x)` in the R variable is `\delta(R-|x|)+\delta(R+|x|)` (including the appropriate doubled atom at 0). By evenness of `W_\zeta`, **`\Psi''=W_\zeta` in distributions**. This is the classical signed double integration underpinning the Suzuki screw kernel, now given a direct finite arithmetic implementation.

The completed expression is

\[
\begin{aligned}
\Psi(R)={}&8(\cosh(R/2)-1)
-\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}(R-\log n)_+
-\tfrac12(\gamma+\log4\pi)R\\
&-\int_0^\infty\left[(R-x)_+-Re^{-x/2}\right]
\frac{e^{-x/2}}{1-e^{-2x}}\,dx.
\end{aligned}\tag{CW-14}
\]

The sum over prime powers is finite for each finite R. For `\alpha_j=2j+1/2`, each Archimedean rung is **explicitly integrable**:

\[
I_j(R)=\int_0^\infty\left[(R-x)_+-Re^{-x/2}\right]e^{-\alpha_jx}\,dx
=\frac{R}{\alpha_j}-\frac{1-e^{-\alpha_jR}}{\alpha_j^2}-\frac{R}{\alpha_j+1/2}.
\]

Define the finite, source-first screw potential `\Psi_J(R)` by replacing the Gamma integral in (CW-14) with `\sum_{j=0}^{J-1}I_j(R)`. For R≥0, since `|(R-x)_+-Re^{-x/2}|≤(1+R/2)x`, its exact error is bounded by

\[
\boxed{|\Psi(R)-\Psi_J(R)|\le
\left(1+\frac R2\right)
\left(\frac1{2a_J}+\frac1{a_J^2}\right).}\tag{CW-15}
\]

Away from 0 and genuine prime atoms `R=\log n`, ordinary differentiation gives

\[
\boxed{\Psi_J''(R)=2\cosh(R/2)
-\sum_{j=0}^{J-1}e^{-(2j+1/2)R},}\tag{CW-16}
\]

converging on every compact subset of `(0,∞)` away from prime atoms to the **regular density** `2cosh(R/2)-e^{-R/2}/(1-e^{-2R})`. The missing negative atoms at `R=\log p^k` and the origin contact **must be retained distributionally**. The code explicitly refuses to identify an atom with an ordinary pointwise second derivative.

Finally set `g=-\Psi` and `K(t,u)=g(t-u)-g(t)-g(-u)+g(0)=\Psi(t)+\Psi(u)-\Psi(t-u)` (evenness and Ψ(0)=0). The required distributional relation `∂_t∂_uK=W_\zeta(t-u)` follows from (CW-13) and recovers E38/Suzuki's differentiated kernel, **without postulating its sign**. `K_J` is explicitly executable, with the finite-rung error above. This is not a new theorem about an infinite self-adjoint Suzuki operator.

## 7. Decisive positive-source / negative-global-kernel countermodel

Use the positive connected fake source `b_\delta=\log_*\zeta+\delta\delta_6`, with δ≥0. Its Dirichlet exponential has exact nonnegative coefficients

\[
a_\delta(n)=\sum_{0\le j\le\min(v_2(n),v_3(n))}\frac{\delta^j}{j!}\ge1.
\]

But `a(2)=a(3)=1` whereas `a(6)=1+δ`: it fails Euler multiplicativity. Its completed **arithmetic-side signed form** uses the ordinary Γ/pole source plus the extra composite impulse `-δ(log6)/sqrt6` at each of `±log6`. In the screw potential the addition is

\[
\boxed{\Psi_\delta(R)-\Psi_0(R)
=-\delta\frac{\log6}{\sqrt6}(R-\log6)_+.}\tag{CW-17}
\]

**CW-18 (PROVED LOCAL / RATIONAL NEGATIVE CERTIFICATE).** At R=2, the *genuine* baseline source potential obeys `\Psi_0(2)<17`: its pole term is `<8` because `cosh1<2`; its contact and authentic-prime contributions are nonpositive; the absolute Gamma-rung sum is `< 2[4+\pi^2/24]<9`, using `|E_2(x)|≤2x`. Elementary Taylor bounds give `1<log6<19/10` (`exp(19/10)>6` already by its fourth positive Taylor partial sum), and `sqrt6<3`. Therefore

\[
\boxed{\Psi_\delta(2)<17-\delta/30.}\tag{CW-18}
\]

Choosing the **positive rational** impulse `δ=1000` yields `\Psi_{1000}(2)<-49/3`. Consequently `K_{1000}(2,2)=2\Psi_{1000}(2)<0`. A continuous kernel with a negative diagonal has a negative quadratic witness; compact smooth approximations to the indicator-step derivative supply signed Weil-form witnesses as well. This is a theorem using basic inequalities, not a numerical eigenvalue, and it refutes any general attempt to infer *completed Weil positivity* merely from **nonnegative arithmetic coefficients and positive Gaussian heat**. It does **not** refute genuine ζ or RH; the fake input is not Euler-multiplicative.

An especially revealing source-map defect: `\xi_\delta(s)=\xi(s)\exp(\delta6^{-s})` has the **same zero divisor** as genuine ξ, since the multiplier has no zeros, but it loses the functional equation/growth contract: its reflection ratio is `\exp(\delta[6^{-s}-6^{s-1}])`, nonconstant in s, and the entire multiplier has infinite order. The fake signed distribution is *not a Weil zero-side formula for this altered completed function*. Source-specific growth, Euler multiplicativity, functional equation and analytic normalization are separate gates. A matching zero divisor alone does not authorize one to replace its Weil distribution.

## 8. Positivity is still open; quantified next verdict-changing problem

**Already established here, under stated boundaries:** true-prime heat determines its source measure under a full Mellin vertical line (CW-02); half-density and Gamma/pole normalization transport to **the completed signed Weil arithmetic distribution** (CW-04–07) using the classical external Weil explicit formula; compact-test source impulses are finite; corrected Gamma rungs converge in uniform `H¹_0(-a,a)` form norm `O(J^-2)` (CW-11); a zero-independent double-integrated Suzuki-type kernel has a finite closed form and explicit remainder (CW-13–16); and positive fake non-Euler coefficients do not force Weil sign (CW-18).

**Not established:** positivity of `Q_ζ` for every compact test (RH equivalent); a positive source-constructed map `T` whose Gram converges to `Q_ζ` without circularly taking a square root of Q; actual self-adjoint global limit, uniformly convergent Suzuki characteristic functions, physical source experiments or independently new math priority. This work is a signed approximation theorem, not a hidden proof of the sign.

**No-coercivity caution.** E38's `Q(v,w)=<S_av',w'>` uses a continuous bounded-interval screw kernel `K`. Thus `S_a` is Hilbert–Schmidt/compact on L² for fixed a. On the infinite-dimensional mean-zero derivative range of `H¹_0(-a,a)`, normalized weakly-null orthonormal sequences give `Q(v_n,v_n)->0` with nonvanishing `H¹` norms. Consequently one cannot seek a strictly positive **uniform** `H¹` coercivity gap `Q(v,v)≥c||v||_{H¹}²` with c>0, even if RH is true. The correct numerical/analytic target is a form lower bound whose negative part tends to zero at the certified arch-remainder scale, or an independent positive realization with source-identified equality.

**Concrete next gate:** on each a, derive a source-first estimate uniform for *all* `v\in H¹_0(-a,a)` of the form `\widetilde Q_J(v,v)≥-o(1)\|v\|²_{H¹}`, where the `o(1)` is proved from arithmetic and Gamma laws rather than a finite set of Gram evaluations. Combining it with (CW-11) would imply signed-form positivity for that a. An alternative is an independently positive operator factorization with error controlled in the same norm. Either would have to withstand the fake-6 source, an honest non-Euler L-function completed to its own source law, wrong half-density/conductor and a new high-resolution holdout. The full Weil–Suzuki sign obstruction is **still real**.

A source-typed downstream RH handoff is justified for (CW-11)/(CW-15)/(CW-18) as finite signed evaluation, a limit theorem and a no-go; *not* as a proof of positivity.

## 9. Exact implementation and validation boundaries

- `observational_succ/completed_weil_transport.py`: exact prime tape, signed Gamma source, contact/spectral/resolvent routes, rational ladder bounds, accelerated Sobolev form bound, source-first elementary Suzuki screw functions, positive fake source and rational negative certificate.
- `tests/test_completed_weil_transport.py`: independent trial factorization, true-prime and fake composite, exact Gaussian Mellin quadrature, digamma spectral/real-space/resolvent equality, tiny-x counterterms, conductor/parity controls, H¹ acceleration, finite-screw second derivative, non-Euler source, source-domain guard, and byte-identical independent receipt replay.
- `scripts/completed_weil_transport_probe.py`: deterministic no-zero-input high-precision diagnostic. Its **rational** bounds are theorem-backed, while reported mpmath readings are not interval arithmetic. `--verify research/2026-10-14/COMPLETED_WEIL_RECEIPT.json` checks byte-for-byte output.
- `docs/CLAIM_SUPPLEMENT_COMPLETED_WEIL.md` and `.github/workflows/completed-weil-source.yml`: scoped ledger and exact-head automated tests.

**Reproduction:** Python 3.10+ and optional `mpmath`; `PYTHONPATH=. python -m unittest discover -s tests -p 'test_completed_weil_transport.py' -v`; run `PYTHONPATH=. python scripts/completed_weil_transport_probe.py --verify research/2026-10-14/COMPLETED_WEIL_RECEIPT.json`. No new Lean proof was compiled. The inherited 121-test research overlay provides regressions; a full repository CI can be claimed **only once the pushed GitHub SHA has actually passed**. Academic novelty is not established by many tests on one implementation family.
