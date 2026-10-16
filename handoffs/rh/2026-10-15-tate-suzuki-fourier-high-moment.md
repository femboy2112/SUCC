# RH handoff candidate — Tate's real Gamma Fourier source proves authentic Suzuki high sign at every radius

**Date:** October 15, 2026. **Origin:** \`research/tate-suzuki-fourier-high-moment-2026-10-15\`, stacked on DYSPON II PR #114 at \`9bcb7f4cc28128fa6171c1479d3d804b24e32bd3\`. Authentic source PR109 sibling \`6748cb8dd9d0eb186be18a75ed9ae1d94e9e898b\` is imported verbatim, original Suzuki blob \`0cc8510b71d178fc79e8d410a86d8b6014cf9178\`. **Draft, not exported to another repository, no main changes. RH OPEN.**

## Source-specific theorem

For all nonzero \(f\in C_c^\infty(-1/2,1/2)\) whose power moments \(\int f(t)t^kdt=0\) for \(k=0,\ldots,m-1\), the ORIGINAL completed zeta Weil quadratic form satisfies

\[
\boxed{
m=16:\quad Q_\zeta(f)>\frac1{20}\|f\|_2^2,\qquad
18\le m\le30:\quad Q_\zeta(f)>\frac1{16}\|f\|_2^2.
}
\]

Proven from the original Tate/Gamma Fourier multiplier

\[
m_{32}(12)=\sum_{j=0}^{31}\frac4{4j+1}
\frac{144}{144+(4j+1)^2/4}
\]

and the strict rational low Fourier mass upper

\[
\varepsilon_m(1/2,12)=\frac{12}{3(2m+1)}
\frac{6^{2m}}{(m!)^2},
\]

using first-prime \(\Lambda(2)/\sqrt2\), true two-cell shift norm <=1, **one real** \(4j+1\) Gamma ladder, correct negative contact/polar budget \(<95/16\), and **no nontrivial zero locations**. Exact \`Fraction\` inequalities verify \(m_{32}(12)(1-\varepsilon_m)-95/16\) strictly exceeds the stated margins for m=16 and m>=18. For m=15 this particular conservative certificate fails; no negative original Weil witness is inferred.

## Exact Suzuki/Neumann interface

On true Suzuki mean-zero derivative carrier \(H=L_0^2(-1/2,1/2)\), set \(f=Vu,\ (Vu)(t)=\int_{-a}^t u,\ K=V^*V=(-\Delta_N)^{-1}\). Legendre orthogonality of \(u\) to modes \(P_1,\ldots,P_r\) entails vanishing first r power moments of f, since the derivatives \(P'_1,\ldots,P'_r\) span polynomials of degree <r. Therefore

\[
Q_{16}GQ_{16}\succeq K/20,\qquad
Q_rGQ_r\succeq K/16 \ (18\le r\le30).
\]

These are source-proved **K-relative** high forms, NOT forbidden positive \(cI\) gaps for a compact operator. At rank30 this improves the previous \(369/10000\) relative high constant to \(1/16\). At rank18 the unknown low sign is only 18×18, split 9+9 by parity. The imported authentic PR109 source inequality \(||g'||_{L1(-1,1)}<11/40\) yields a finite actual zero-shift \(R_0\prec121/100I\) at rank18 or30, versus old rank30 \(3025/1476\approx2.04946\). The **true low short \(S_0=A-R_0\)** remains completely UNVERIFIED.

## All finite observation radii — constructive but extremely expensive

For every finite real a>0 and requested L>=0, a source-positive finite moment-rank exists such that \(Q_\zeta(f)>L||f||²\) on all tests annihilating its first r moments. The explicit rational-a **gross majorant** is

\[
N=2^{\lceil4a\rceil+1},\quad E=2^{\lceil2a\rceil+1},\quad
B(a)=43/8+N(N+1)-2+E.
\]

Every actual prime-power n with log n<2a lies below N and has w_n=Λ(n)/sqrt(n)<=n. The all-integer sum is an **upper bound only**, NEVER a fake composite Euler source. Set \(M=\lceil17(B+L+1)/4\rceil+1,\ J=2^M,\ \Omega=8J,\ r=\lceil4a\Omega\rceil+1\). Then the true real Gamma multiplier is \(>\frac{16}{17}(1+M/2)>2(B+L+1)\), the moment low-frequency fraction is \(<1/12\), and the full original Weil form is \(>L||f||²\). For real a, enlarge to a rational a' and transfer support/moment tests.

This is a proof of a finite-codimension original high sign at **every** a, NOT a feasible computational certificate at gigantic r and NOT RH. Generic a=1/2 already uses \(M=347\), and at a=2 \(M=1116448\), while source-tight first-prime \(m=18,J=32\) is efficient. No \(\omega\)-super-task, fake finite observer, global positive coupling or low-Schur sign is claimed.

## What to do next (verdict-changing, original source only)

1. Execute the **actual source** 18×18 low Legendre interval \(A_J\), including Gamma, prime2, contact and both poles, with source-positive omitted Gamma tail and explicit interval precision. The source-faithful \`scripts/tate_suzuki_authentic_low18_scan.py\` does this at J2; it is an input, not the full short.
2. Construct a true high trial \(U:P_{18}H\to Q_{18}H\) and its signed derivative residual Gram \(C_U\), directly from the unchanged source at every point. Prove or falsify a rigorous PSD source interval matrix \(A-L_U-16C_U\). Exact positivity would prove *first-window* Weil sign only.
3. Repeat at all radii with source-tight Gamma/prime-correlation estimates, maintaining the authentic Tate \(\Gamma_{\mathbb R}(s)\), pole/contact, prime-power, half-density, and complete test-function domain. Only universal sign implies RH.
4. Try independent Tate/Connes arithmetic polarizations and non-Euler mutation controls. No extra sign can be imported from Dedekind eta q^(1/24) alone.

**Proof:** \`research/2026-10-15/TATE_SUZUKI_FOURIER_HIGH_MOMENT.md\`. **Executable code:** \`observational_succ/tate_suzuki_fourier_schur.py\`, \`observational_succ/tate_suzuki_all_radii.py\`. **Tests:** \`tests/test_tate_suzuki_fourier_schur.py\`, \`tests/test_tate_suzuki_all_radii.py\`; full original source PR109 tests preserved verbatim. **Reproduction:** \`python scripts/tate_suzuki_fourier_high_probe.py --verify\`; \`research/2026-10-15/TATE_SUZUKI_FOURIER_HIGH_RECEIPT.json\`; isolated Python 3.10/3.13 CI \`.github/workflows/tate-suzuki-fourier-high.yml\`. Scientific priority not independently established; every finite computation is a certificate for only the stated analytic inequality or original source interval.

**Primary:** Tate's thesis (Fourier/Poisson), Masatoshi Suzuki arXiv:2606.09096v3 (2026) source signed Weil/screw, original SUCC PR #85, #109 source derivative bound, and independent classical Plancherel/Legendre theory. **RH PROVED: NO.**
