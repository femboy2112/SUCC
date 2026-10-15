# DYSPON-SPHERE I — Tate-normalized prime clock transducers and source-derived sparse Weil positivity

**Status (2026-10-15):** source-identified analytical theorem with exact rational/source control, restricted-domain only; operator path theorem classical, source application new to this SUCC branch. **RH PROVED: NO.** Scholarly priority UNVERIFIED. No new globally positive Hilbert carrier, no nontrivial-zero inputs, no empirical carrier access. Isolated draft stacked on APOLLO PR #110 at \`cb7b804d8624dcf5247eac34cf59e969577c6ccb\`, transitively on ONE OBJECT PR #106, Tate PR #103, Phoenix-II main.

## 0. Origin and exact target

The user's proposed DYSPON-SPHERE uses Tate's adelic/Fourier normalization as a source reference, then seeks genuinely source-justified positive transducers, not an abstract positive covariance. This document changes APOLLO K2 from a positive-minus-negative *anchored point* representation into an exact **form on the original Weil test f**, in which primes become translations of the source carrier. It then proves a nontrivial quantitative positive *restricted cone of tests* for the actual completed zeta Weil form, including the first genuine prime.

The original Weil functional is Suzuki, arXiv:2606.09096v3, equation (1.1)/§2, and its compact smooth positivity is RH-equivalent (classical Weil/Yoshida). The screw potential, original true-prime weights, and Gamma/pole/contact decomposition come from the immutable \`source_weil_hierarchy.py\` blob identified upstream by APOLLO, not from synthetic operators. Tate's Poisson/Mellin/character conventions are imported from PR #103 and classical Tate theory; we have NOT constructed a new adelic trace.

**The obstruction:** Positive separate Hilbert features cannot prove positivity of their difference. Even the first prime hinge has a negative direction. We need a valid domination theorem at the level of the original source.

## 1. DYS-01: exact original Weil form in prime-translation coordinates (DERIVED from classical Weil/Suzuki + APOLLO)

Work with any finite real \`a>0\` and \`f in C_c^infinity(-a,a)\`, complex-valued. Regard f as zero-extended to all of R. Define

\[
b_n=\log n,\quad w_n=\Lambda(n)n^{-1/2},\quad
\mathcal P_a=\{n=p^k:\log n<2a\},\quad C_\infty=-\psi(1/4)+\log\pi .
\]

Each n in P_a is an ACTUAL prime power, never a primitive composite 6. For \(\alpha_j=(4j+1)/2,\;\beta_j=4/(4j+1)\), let \(R_\alpha\) on \(L^2(\mathbb R)\) be convolution by \(r_\alpha(t)=\frac\alpha2e^{-\alpha|t|}\), and \((S_bf)(t)=f(t-b)\). Let \(s(t)=\sinh(t/2)\), \(h(t)=\cosh(t/2)-1\).

\[
\boxed{\begin{aligned}
Q_\zeta(f)=W_\zeta(f*\widetilde f)
={}&\sum_{j=0}^{\infty}\beta_j
       \bigl(\|f\|_2^2-\langle f,R_{\alpha_j}f\rangle\bigr)
-C_\infty\|f\|_2^2\\
&+8|\langle f,s'\rangle|^2-8|\langle f,h'\rangle|^2\\
&-\sum_{n\in\mathcal P_a}w_n
   \langle f,(S_{b_n}+S_{-b_n})f\rangle .
\end{aligned}}\tag{DYS-01}
\]

Inner products are taken over R, with f zero-extended. In particular, \(8|\langle f,s'\rangle|^2=2|\int f(t)\cosh(t/2)\,dt|^2\) and the negative pole is \(2|\int f(t)\sinh(t/2)\,dt|^2\).

**Proof/normalization:** APOLLO K2 gives the exact original anchored kernel \(K_g=K_+-K_-\); APOLLO K3 gives \(\partial_x\partial_yK_g=W_\zeta(x-y)\). Pair K_g with \(f'(x)\overline{f'(y)}\) twice by parts. The cumulative signed Brownian indicator is \(-f(t)\), since \(\int f'(x)I_x(t)dx=-f(t)\). A single Gamma mode \(c_jE_j\), \(c_j=4/(4j+1)^2\), contributes \(2c_j\alpha_j\delta_0-c_j\alpha_j^2e^{-\alpha_j|t|}=\beta_j(\delta_0-r_{\alpha_j})\). Each real prime hinge contributes \(-w_n(\delta_{b_n}+\delta_{-b_n})\) and **no spurious contact**. The original contact contributes \(-C_\infty\delta_0\), and the two original polar channels have the signs displayed. For f smooth compact, the Gamma series converges absolutely, because \(0\le 1-\alpha_j^2/(\alpha_j^2+\omega^2)\le \omega^2/\alpha_j^2\), and \(\sum_j\beta_j/\alpha_j^2<\infty\). This is not independent Tate completion: the exact original completed Weil distribution is a pinned inherited fact.

**Falsification conditions:** omit Gamma, change contact, flip a pole, use fake \(\Lambda(6)>0\), remove the half-density, or exchange the twisted chi(-3) conductor/parity; then (DYS-01) is NOT the original zeta form.

## 2. DYS-02: sharp finite-path theorem for one clock (CLASSICAL operator theorem / exact source geometry)

For \(I=(-a,a)\), restrict \(H_b=P_I(S_b+S_{-b})P_I\) to \(L^2(I)\), \(b>0\), and put \(m=\lceil 2a/b\rceil\). Then

\[
\boxed{\quad \|H_b\|_{\mathrm{op}}=2\cos\frac{\pi}{m+1},
\qquad -wH_b\succeq-2w\cos\frac{\pi}{m+1}\,I .\quad}\tag{DYS-02}
\]

The m=1 case is zero, and for \(b<2a\le2b\), m=2 and the sharp lower bound is \(-wI\), not the crude \(-2wI\).

**Proof:** Disintegrate \(L^2(I)\) by position modulo b: \(x=r+kb\), \(0\le r<b\), with finitely many admissible k for almost every r. Translation by b connects consecutive k. Thus H_b is a direct integral of adjacency matrices of ordinary finite path graphs. The longest path has exactly m vertices on a set of positive r-measure, except harmless measure-zero threshold fibers; the path adjacency eigenvalues are \(2\cos(\pi j/(m+1))\). For m=2, +/-1 occur on the active two-cell subspace. This is a theorem about the full continuum \(L^2\), NOT sampled matrices or a positive-definite prime.

**Exactly attained negative control:** let \(a=1/2,b=3/4,w=1\), \(\ell=(2a-b)/2=1/8\), \(J=[-1/2,-3/8]\), \(J+b=[1/4,3/8]\), \(v=\mathbf1_J+\mathbf1_{J+b}\). Four anchored point coefficients generate v. Then \(\|v\|^2=1/4\) and the original-shaped prime hinge is exactly \(-1/4\), so the sharp relative Rayleigh quotient is -1. All entries are Fractions. This b is a SYNTHETIC RATIONAL CLOCK and is not substituted for true log 2.

**Prime birth obstruction:** as \(a\downarrow b/2\) from above, the unweighted point kernel tends uniformly to zero on the shrinking interval, while its Brownian-energy-relative negative operator norm remains 1. At \(2a=b\), the compressed translation is zero. This is a loss of uniform coercivity under naive observer-window comparison, not a physical supertask or a proof that the full Weil source is negative. The endpoint-localized maximizing vectors vary with a.

## 3. DYS-03: positive real Gamma UV transducer on sparse support (PROVED ANALYTIC)

Let E be any measurable subset of the line, with Lebesgue measure \(\mu\), and suppose f is supported in E. The elementary Schur estimate is

\[
0\le\langle f,R_\alpha f\rangle
\le (\alpha\mu/2)\|f\|_2^2.
\tag{DYS-03a}
\]

For any integer J>=1 with \((4J-3)\mu\le2\), every original real Gamma mode j=0,...,J-1 obeys
\[
\beta_j\langle f,(I-R_{\alpha_j})f\rangle
\ge \frac{2}{4j+1}\|f\|_2^2.
\]

The omitted Gamma modes remain PSD, so for J=2^k,

\[
\boxed{
Q_{\Gamma}(f)\ge \left(\sum_{j=0}^{J-1}\frac2{4j+1}\right)\|f\|_2^2
>\frac12\log(4J+1)\|f\|_2^2
>\frac{k+2}{3}\|f\|_2^2.
}\tag{DYS-03b}
\]

Proof of the final fully rational bound: the summand is decreasing, so the sum dominates its integral; \(4J+1>2^{k+2}\) and the exact positive expansion \(\log2=2(1/3+1/(3\cdot3^3)+\cdots)>2/3\). No numerical eigenvalues, empirical smallness or imaginary zero positions are inputs.

**Geometric interpretation (not physical claim):** a negative prime shift can act on narrow translation-paired cells, but such cells must pay growing original Gamma energy in their own \(L^2\)-localized observation carrier. The UV positive budget grows at least like \((1/2)\log(1/\mu)\) as total support measure tends to zero. This applies to arbitrarily disconnected support, not only single bumps.

## 4. DYS-04: THE ORIGINAL FIRST-PRIME SPARSE-WEIL THEOREM (PROVED ANALYTIC, SOURCE-CONDITIONAL)

**Theorem.** For every \(0<a\le1/2\) and every nonzero complex \(f\in C_c^\infty(-a,a)\) whose support has Lebesgue measure at most \(2^{-17}\),

\[
\boxed{W_\zeta(f*\widetilde f)>\frac1{16}\|f\|_2^2.}\tag{DYS-04}
\]

In particular, this is a complete all-tests-in-the-restricted-cone positivity theorem **inside the original first prime-active observation window \(a=1/2\)**; it is NOT all-tests positivity at a=1/2. Smooth compact functions with very small support exist there in infinite-dimensional families.

**Exact source proof:**

1. The pinned original Suzuki real source verifies \(C_\infty<43/8\). Genuine log 2 is between 2/3 and 7/10, and log 3>1, so in every window \(0<a\le1/2\) the only possible active prime-power is the authentic n=2 (active at a=1/2). The true weight \(w_2=\log2/\sqrt2<1/2\), since \(\log2<7/10\) and \(\sqrt2>7/5\). To prove the log upper using rationals, bound the tail of \(2\sum_{k\ge0}3^{-(2k+1)}/(2k+1)\) by 1/36 after the first term: \(\log2<25/36<7/10\).
2. Since \(2a\le1<2\log2\), the true prime-shift chain has at most two vertices. DYS-02 bounds its entire negative energy from below by \(-\frac12\|f\|_2^2\). Missing/inactive primes contribute zero. The fake n=6 clock is not a source term.
3. The original negative polar channel is at most \(2(\sinh a-a)\|f\|_2^2\). For \(a\le1/2\), the elementary series bound \(\sinh a-a\le a^3/[6(1-a^2)]\) gives \(2(\sinh a-a)\le1/18<1/16\). The positive polar channel is dropped only as a valid LOWER bound.
4. Take J=2^16 and \(\mu=2^{-17}=1/(2J)\). Then \((4J-3)\mu<2\), and DYS-03b gives \(Q_\Gamma(f)>6\|f\|_2^2\). This is a finite-source lower inequality with a valid positive omitted infinite tail, not a 65,536-mode numerical sample.
5. Hence the exact original completed form obeys
\[
Q_\zeta(f)>
\left[6-\frac{43}8-\frac12-\frac1{16}\right]\|f\|_2^2
=\frac1{16}\|f\|_2^2.
\]

This proof uses original true-prime and one real-place source data, one Gamma ladder, **both** polar channels, the actual negative contact, half-density \(\sqrt n^{-1}\), the genuine Weil test domain, and no zero lookup. The only numerical-looking constant in the argument, 43/8, is a preexisting source-backed outward-rational special-function interval certificate inherited from APOLLO. Source pin verification is executed through the original source adapter.

**Domain warning:** Support measure \(\le2^{-17}\) is a substantial restriction. An arbitrary compactly supported test can occupy nearly all of (-1/2,1/2); the theorem cannot be extended by density because the sparse-support *class* is not norm-dense in all L² tests with a fixed support measure cap.

## 5. DYS-05: positive sparse-support cones exist for every finite interval (PROVED ABSTRACT from DYS-01)

For any fixed finite a, the genuine set P_a of prime powers is finite. DYS-02 yields the finite negative prime budget

\[
M_a=C_\infty+2(\sinh a-a)+
\sum_{n\in\mathcal P_a}w_n\,2\cos\frac{\pi}{\lceil2a/b_n\rceil+1}.
\]

All numbers in M_a are defined from the original source. Pick k so large that \((k+2)/3>M_a\), and set \(\mu_a=2^{-(k+1)}\). Every nonzero \(f\in C_c^\infty(-a,a)\) supported on a set of measure at most \(\mu_a\) then satisfies

\[
Q_\zeta(f)>\left((k+2)/3-M_a\right)\|f\|_2^2>0.
\tag{DYS-05}
\]

The proof is DYS-03 plus the genuine finite-clock and polar budgets. This establishes a **nonempty infinite-dimensional positive restricted cone for every finite a**, even far into prime-active windows, while preserving all source couplings. The bound may be extraordinarily small and says NOTHING about delocalized tests.

This is a derived local positivity theorem, NOT a globally positive Weil form. The contextually relevant prior literature includes Bombieri's finite-union-of-intervals localization questions and Connes–Consani localized lower-bounded forms, both discussed in Suzuki §1.1. Novel academic priority remains unverified.

## 6. DYS-06: exact obstruction and next decisive probes

The naive inequality "each prime activation is an additional PSD Gram" is REFUTED by DYS-02's exact four-anchor witness. Likewise an argument which assumes uniform operator-norm continuity in the Brownian relative metric at the threshold is REFUTED: the relative prime norm jumps from 0 to 1. Neither counterexample is an RH disproof.

The Gamma protection is **UV/localized**, and is insufficient for the *delocalized*, low-frequency, many-clock correlations in the all-test Weil form. That is the actual source-positive proof debt.

**Next research contracts:**

- (R1) Prove a source-specific microlocal Schur estimate separating newly activated endpoint shift channels from the complement, with Gamma cross-terms and a residual that decays in the activation width. The split must preserve original contact and polar terms. Test both a synthetic clock and true log2 with certified interval arithmetic.
- (R2) Feed DYS-01 directly into the **authentic** 30-low/high Suzuki zero-shift residual algorithm of PRs #107/#109. Compare energy bounds for sparse high vectors against computed low-mode couplings; certify the full 30x30 source matrices, not handpicked samples.
- (R3) Attempt a transport/extension theorem for the APOLLO positive/negative features which absorbs the paired-neutral new prime birth. A scalar jump budget alone is too pessimistic; retention of source-correlated gamma-prime interactions is essential.
- (R4) Transport from the exact Tate Schwarz–Bruhat/Fourier/conductor chart to this very Weil quadratic form with a commuting test-domain square. As an orthogonal family, use primitive chi(-3) (signed p=2) and an intentionally non-Euler functional-equation mutant. Neither may silently borrow zeta's even Gamma/contact.
- (R5) Seek a *global* original-source domination invariant that controls tests with large or delocalized supports. Only the all-test all-a version can prove RH.

**Pass/fail/ambiguous:** A proof of DYS-04 is genuine restricted positivity; any exact original negative Weil witness in its domain would refute the implementation/derivation. A synthetic negative *prime-only* witness is expected and is not such a contradiction. A positive sampled Gram outside the restricted cone is ambiguous. The global RH theorem remains UNVERIFIED.

## 7. Reproduction / provenance / independence

- \`observational_succ/tate_prime_clock_uv.py\`: exact rational clock geometry; original-source and contact pinned sparse theorem; never inserts nontrivial-zero data.
- \`tests/test_tate_prime_clock_uv.py\`: path-boundaries, exact negative 4-anchor witness, original source labels at a=1/2, gamma support-Schur gate, contact/pole/prime budget and intentionally broken source cases.
- \`scripts/tate_prime_clock_uv_probe.py\`: printable deterministic receipt (no random fit).
- \`.github/workflows/tate-prime-clock-uv.yml\`: required original source and regression checks on Python 3.10 and 3.13.
- The crucial constant \(C_\infty<43/8\) and source SHA validation are inherited from APOLLO PR #110 K6, not rediscovered.
- Primary: Tate thesis (1950; adeles, Fourier, Poisson); Masatoshi Suzuki, *Weil's quadratic form via the screw function*, arXiv:2606.09096v3 (2026), §§1–2 and §8; Alain Connes and Caterina Consani, *Weil positivity and Trace formula, the archimedean place*, arXiv:2006.13771 (restricted real-place scope).

**Claim ledger:** DYS-01 DERIVED from specified source identities, DYS-02 PROVED CLASSICAL OPERATOR, DYS-03 PROVED ANALYTIC, DYS-04 PROVED ANALYTIC conditional on pinned original-source interval constant, DYS-05 PROVED ABSTRACT, DYS-06 REFUTED shortcuts; full Weil global source-positive contraction UNVERIFIED. **RH PROVED: NO.**
