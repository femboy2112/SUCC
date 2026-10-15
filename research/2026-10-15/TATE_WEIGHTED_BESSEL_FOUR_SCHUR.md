# OPERATION WEIGHTED BESSEL-4 — A source-derived original Weil polarization with only four test moments

**Date:** October 15, 2026. **Parent:** completed source, source-neutral APOLLO and seven-moment SUCC draft PR #128, exact parent head \`21a1d6854df56b99e9846b311a1035455a6d6d88\`; transitive Tate #103, APOLLO #110, DYSPON #112/#114, original Suzuki #109/#116, reflection #126. **New isolated research branch only:** \`research/tate-weighted-bessel-four-low-2026-10-15\`. Main, source archive and the separate RH repo unchanged. **RH PROVED: NO.** Academic priority relative to existing analytic-number-theory literature not established. Fourier–Legendre and spherical Bessel formulas classical.

## 0. Target / why this advances the real RH program

The maintainer's moonshot is a source-derived positive polarization of the actual completed Weil distribution, not a standalone positive covariance, sampled Gram, or formal s↔1−s identity. We already have source-identical true arithmetic/Gamma/pole and finite-window Krein positive-minus-positive operators, but the **full** contraction remains exactly RH-hard.

One genuinely useful theorem is to establish positivity for the true completed distribution on an **infinite-dimensional codimension-four** source test subspace (previous branch needed seven power moments), using the positive Gamma spectral density with its complete frequency dependence.

This reduces the real first-prime Suzuki zero-shift low Schur from 7×7 to **4×4**. It does NOT prove the 4×4 sign, all first-window positivity, or RH.

## 1. Honest source law and test quantifiers (WB4-01)

Fix \(a=1/2\), \(I=(-a,a)\). The original, separately authenticated (APOLLO #110 / DYSPON #112) completed Weil quadratic form, with zero-extension of \(f\in C_c^\infty(I;\mathbb C)\), is

\[
\boxed{\begin{aligned}
Q_\zeta(f)=W_\zeta(f*\widetilde f)
={}&\sum_{j\ge0}\frac4{4j+1}
\langle f,(I-R_{(4j+1)/2})f\rangle\\
&-C_\infty\|f\|_2^2
+2|\langle f,\cosh(t/2)\rangle|^2
-2|\langle f,\sinh(t/2)\rangle|^2\\
&-\frac{\log2}{\sqrt2}
\langle f,(S_{\log2}+S_{-\log2})f\rangle.
\end{aligned}}\tag{WB4-01}
\]

Here \(R_\alpha f=\frac\alpha2e^{-\alpha|\cdot|}*f\) on \(\mathbb R\), \(S_bf(t)=f(t-b)\), \(C_\infty=-\psi(1/4)+\log\pi<43/8\) is the genuine original real-Archimedean Brownian contact, and the **only** active first-window Euler atom is n=2 with actual weight \(w_2=\log2/\sqrt2<1/2\). The authentic compressed symmetric shifted-prime source has sharp operator norm 1. Real source pole signs are retained. This is the signed original Weil test object; no numerical zeta-zero lookup or non-Euler factor is allowed.

The target universal test class is

\[
\boxed{
\mathcal V_4
=\left\{f\in C_c^\infty(-1/2,1/2;\mathbb C):
\int_{-1/2}^{1/2}t^k f(t)dt=0,\ k=0,1,2,3\right\}.
}\tag{WB4-02}
\]

These FOUR polynomial test moments are **NOT** the arithmetic prime-power orders \(p^k\). A true all-f statement about \(\mathcal V_4\) is stronger than testing four vectors, but still weaker than all-test Weil/RH positivity.

## 2. WB4-03 — the exact spectral Gamma-weighted low-frequency inequality

Write \(\widehat f(\omega)=\int_{\mathbb R}f(t)e^{-i\omega t}dt\). The first J true real Gamma rungs have monotonically increasing nonnegative spectral multiplier

\[
\boxed{
m_J(\omega)=
\sum_{j=0}^{J-1}\frac4{4j+1}
\frac{\omega^2}{\omega^2+(4j+1)^2/4}.
}\tag{WB4-03}
\]

For any finite \(\Omega>0\), monotonicity gives the *exact source-inequality without approximation*:

\[
\boxed{
Q_{\Gamma,J}(f)\ge
m_J(\Omega)\|f\|^2
-
\frac1{2\pi}\int_{|\omega|\le\Omega}
\bigl[m_J(\Omega)-m_J(|\omega|)\bigr]
|\widehat f(\omega)|^2d\omega.
}\tag{WB4-04}
\]

**Proof:** for \(|\omega|\ge\Omega\), \(m_J(|\omega|)\ge m_J(\Omega)\); for smaller \(|\omega|\), the difference is by definition \(m_J(\Omega)-m_J(|\omega|)\). Integrate with Plancherel. The infinite omitted genuine Gamma rungs are PSD and may only increase the original quadratic form.

This repairs the earlier Bessel-7 method, which replaced the true positive low-band spectral shape by a uniform maximum and lost essential frequency information.

## 3. WB4-05 — Legendre projection and all-source finite exact rational weighted integration

The classical plane-wave Legendre expansion is an all-\(\omega\) identity:
\[
\|P_{\ge m}e^{-i\omega t}\|_{L^2(-a,a)}^2
=2a\sum_{\ell\ge m}(2\ell+1)j_\ell(a\omega)^2.
\]
For every f annihilating moments 0..m−1, Cauchy–Schwarz gives a pointwise Fourier mass upper. Thus the low-band loss in WB4-04 is universally at most

\[
\boxed{\begin{aligned}
W_{m,J,\Omega}(a)\|f\|^2,\quad
W_{m,J,\Omega}(a)
&=\frac2\pi\int_0^{a\Omega}
[m_J(\Omega)-m_J(z/a)]\\
&\hspace{8pt}\times\sum_{\ell\ge m}(2\ell+1)j_\ell(z)^2\,dz.
\end{aligned}}\tag{WB4-05}
\]

This is the **correct source-driven polarization** of real Gamma against the unobserved low Fourier mass: it uses the actual spectral source in the compensating weight, not a fictitious covariance or arbitrary cutoff.

### A rigorous rational upper, finite computation but all-f validity

Choose exact rational parameters
\[
\boxed{
a=1/2,\quad m=4,\quad J=128,\quad
\Omega=13,\quad
L=16,\quad K=12,\quad
\eta=1/1000,\quad T=96.
}\tag{WB4-06}
\]

Use the spherical Bessel power series from NIST DLMF §10.53.1. Let \(P_{\ell,K}(z)=\sum_{k=0}^K c_{\ell,k}z^{\ell+2k}\), with rational recurrence \(c_{\ell,0}=1/(2\ell+1)!!\) and
\[
c_{\ell,k+1}=-c_{\ell,k}/[2(k+1)(2\ell+2k+3)].
\]

On any 0≤z≤A, the omitted terms are bounded by a **positive geometric error**
\[
\delta_{\ell,K}(A)
=\frac{|c_{\ell,K+1}|A^{\ell+2K+2}}
{1-A^2/[2(K+2)(2\ell+2K+5)]}.
\tag{WB4-07}
\]

For angular modes \(\ell=4,\ldots,15\) compile the exact rational antiderivative of the NONNEGATIVE polynomial
\[
P(z):=\sum_{\ell=4}^{15}(2\ell+1)P_{\ell,12}(z)^2.
\]

Partition \([0,\Omega]\) into \(T=96\) equal rational cells. On cell \(i\), \(m_J(\Omega)-m_J(\omega)\) decreases as \(\omega\) increases. Its **source-correct upper** is therefore the value at the LEFT endpoint \(\omega_i=i\Omega/T\). The cell's Bessel integral is bounded, **not sampled**, using

\[
j_\ell(z)^2\le(1+\eta)P_{\ell,K}(z)^2+
(1+1/\eta)\delta_{\ell,K}(a\omega_{i+1})^2
\]
for every real z in the cell. The polynomial-square integral is the EXACT difference of rational antiderivative values, and the remainder is its real cell width times the rigorous pointwise error. No rounding or floating-point zero spectrum enters this computation.

For all omitted angular modes \(\ell\ge L\), the classical integral representation gives \(|j_\ell(z)|\le z^\ell/(2\ell+1)!!\) on real z≥0. Hence their entire spectral contribution is bounded, using \([m_J(\Omega)-m_J(z/a)]\le m_J(\Omega)\), by

\[
\boxed{
\frac{2m_J(\Omega)}3\,
\frac{A^{2L+1}}{((2L+1)!!)^2}\,
\frac1{1-[A/(2L+3)]^2},\quad A=a\Omega.
}\tag{WB4-08}
\]

The first factor \(2/3\) comes from the rigorous elementary \(\pi>3\), not numerical integration.

Combining all 96 finite rational upper rectangles, their **real** spherical Bessel Taylor remainders, and the infinite angular tail gives the exact-rational machine-verifiable result

\[
\boxed{W_{4,128,13}(1/2)<\frac{2013}{10000}.}\tag{WB4-09}
\]

The exact rational numerator/denominator are very large (hundreds of thousands of bits). The program retains Fraction-exact arithmetic; a SHA256 of their sign-length-delimited BIG-ENDIAN integer bytes is frozen in a receipt, avoiding float lossy conversions and Python's large-decimal text limit. A few mpmath/scipy preliminary calculations are **NOT** part of the proof.

## 4. WB4-10 — all original Gamma/contact/polar/true p2 contributions survive

The original **true** first 128 \(\alpha_j=(4j+1)/2\) Gamma modes obey the independent exact-rational bound

\[
\boxed{m_{128}(13)>\frac{6097}{1000}.}\tag{WB4-10}
\]

From the authentic original Suzuki source, \(C_\infty<43/8\), true prime \(w_2<1/2\), compressed symmetric prime-shift norm one. Positive cosh-polar and omitted Gamma are source-positive and can only HELP a lower bound. Their negative contact+prime budget is \(<47/8\).

The negative sinh-polar is **not dropped**. Four vanished polynomial moments annihilate the cubic Taylor polynomial of \(\sinh(t/2)\). On |t|≤a=1/2, its fourth derivative is bounded by \(2/2^4\), and \(\|f\|_1\le\sqrt{2a}\|f\|_2=\|f\|_2\). Therefore

\[
2|\langle f,\sinh(t/2)\rangle|^2
\le\frac{8(a/2)^8}{(4!)^2}\|f\|^2
=\frac1{4718592}\|f\|^2
<10^{-6}\|f\|^2.
\tag{WB4-11}
\]

The real Gamma and polar source therefore give for EVERY f∈\(\mathcal V_4\)\setminus\{0\}:

\[
\begin{aligned}
Q_\zeta(f)&>
\left[m_{128}(13)-W_{4,128,13}(1/2)
-\frac{47}{8}-\frac1{4718592}\right]\|f\|^2\\
&>
\left[\frac{6097}{1000}-\frac{2013}{10000}
-\frac{47}{8}-\frac1{1000000}\right]\|f\|^2\\
&=\boxed{\frac{20699}{1000000}\|f\|^2>
\frac1{50}\|f\|^2}.
\end{aligned}\tag{WB4-12}
\]

**THIS IS THE NEW SOURCE-TYPED FOUR-MOMENT POSITIVITY THEOREM.**

All source atoms are authentic; true \(\log2/\sqrt2\) and the original C∞ are SHA pinned; a fake primitive composite 6 has never been added; Gamma is exactly one real archimedean completion; no nontrivial zeta-zero coordinate was read. The proof is an analytic universal bound, not an empirically certified four-test Gram.

## 5. WB4-13 — the authentic Suzuki low sign is now only FOUR-dimensional (still RH-hard)

Let \(H=L^2_0(I)\) be the original Suzuki derivative-coordinate carrier, \(f=Vu=\int_{-a}^t u(x)dx\), \(K=V^*V=(-\Delta_N)^{-1}\). For u orthogonal to the genuine unnormalized Legendre \(P_1(t/a),\ldots,P_4(t/a)\), integration by parts against the derivatives \(P_j'(t/a)\) forces \(f\in H_0^1\) to annihilate the degree 0,1,2,3 polynomial moments.

Thus the signed original Suzuki G, which corresponds to the SAME completed Weil form by the authentic mixed-derivative identity, satisfies

\[
\boxed{D_4:=Q_4GQ_4\succeq\frac1{50}Q_4KQ_4.}\tag{WB4-13}
\]

The unresolved low sector is only four-dimensional, with parity **2 odd+2 even**. This is a source-true infinite-dimensional high coercivity, NOT a positive \(cI\) gap on a compact G operator.

PR #109's separately certified signed original \(g\in W^{1,1}\) estimate, \(\|g'\|_{L^1(-1,1)}<11/40\), gives the true zero-shift Douglas/Feshbach high/low resolvent

\[
\boxed{0\preceq R_0=
\lim_{\lambda\downarrow0}B(D_4+\lambda I)^{-1}B^*
\prec \frac{(11/40)^2}{1/50}I_4
=\frac{121}{32}I_4.}
\tag{WB4-14}
\]

This quantitative bound is weaker than the old rank7 \(121/100 I\), since we are now controlling a larger high sector. But a **4×4 source-authentic** low residual/short might be much more tractable analytically or by original source interval inequalities. The low sign \(S_0=A-R_0\) remains COMPLETELY UNVERIFIED; proving it at a=1/2 would establish only local completed Weil positivity, not RH at all radii.

The decisive next source calculation is **actual original low 4×4** signed matrix \(A\) with both polar channels and true p2, a continuum-source high trial \(U:P_4H\to Q_4H\), and rigorous derivative residual matrix \(C_U\) on the whole high carrier, to check

\[
\boxed{A-L_U-50C_U\succeq0}
\]
with \(L_U=BU+U^*B^*-U^*DU\), where \(Q_4KQ_4\) controls the correct Sobolev remainder. Independent sign on a finite sampled Gram is NOT this theorem.

## 6. Falsification, comparison to previous research, resource barrier

- **The premise is the original completed source**: one \(\Gamma_{\mathbb R}\), correct original contact and both polar signs, true n=2 \(\Lambda(n)/\sqrt n\) impulse with exact shift norm 1, and every omitted Gamma mode PSD.
- **Spherical Bessel source:** Derive the exact plane-wave projection and power series analytically; finite rational integration includes every real frequency interval, every omitted power-series term and every angular mode tail; no numerically fitted quadrature or RH-zero hypothesis.
- **Failure mode m=3:** same method yields a negative CONSERVATIVE lower bound. This means the proposed sufficient method fails for 3 moments, NOT that original zeta Weil has a negative test.
- **Wrong real Gamma parity:** the mutational 4j+3 ladder does not reach the authentic >6097/1000 lower, so cannot forge this certificate.
- **Low signed source:** the original 7×7 J32 interval stage from parent PR128 has all seven truncated diagonal intervals positive but does NOT prove its matrix PSD or source Schur sign; a complete 4×4 source calculation must preserve and extend the whole signed low/high coupling.
- **Not a physical source model:** polynomial moment constraints are source-functional observations, not four elementary particles or Euler jet orders. Gamma frequency monotonicity is mathematical, not an empirical time-arrow.
- **All-a RH remains open:** This is one radius and a moment-null test family. A new source-derived all-radius low-Schur positivity transport is mandatory.

**Artifacts:** \`observational_succ/tate_weighted_bessel_four_schur.py\`, \`tests/test_tate_weighted_bessel_four_schur.py\`, exact byte-serialized rational receipt \`scripts/tate_weighted_bessel_four_probe.py --verify\` with \`research/2026-10-15/TATE_WEIGHTED_BESSEL_FOUR_RECEIPT.json\`, \`.github/workflows/tate-weighted-bessel-four.yml\`, original low 4×4 source scan, scoped claim supplement and RH handoff.

**Classical references:** NIST DLMF [10.53.1](https://dlmf.nist.gov/10.53.E1), [10.54.1–2](https://dlmf.nist.gov/10.54), and Suzuki's 2026 screw/Weil primary preprint [arXiv:2606.09096v3](https://arxiv.org/abs/2606.09096). Imported original arithmetic source belongs to SUCC predecessor PR #110/#116/#126, unmodified. Academic novelty not verified, independent peer review not performed.

**RH PROVED: NO.**
