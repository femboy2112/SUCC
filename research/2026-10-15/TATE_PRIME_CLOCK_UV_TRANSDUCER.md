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

## 3. DYS-03: positive real Gamma UV transducer, with a SHARP finite-mode refinement (PROVED ANALYTIC)

Let E be any measurable subset of R with Lebesgue measure \(\mu\), and suppose f is supported in E. The elementary Schur estimate for the original \(\alpha/2\,e^{-\alpha|x-y|}\) source is

\[
0\le\langle f,R_\alpha f\rangle
\le \frac{\alpha\mu}{2}\|f\|_2^2.
\tag{DYS-03a}
\]

**General logarithmic source gate.** For any integer J>=1 with \((4J-3)\mu\le2\), each original Gamma rung j<J has positive energy at least \(\frac{2}{4j+1}\|f\|^2\). If J=2^k, the integral estimate and log2>2/3 yield

\[
Q_\Gamma(f)>
\frac12\log(4J+1)\|f\|^2
>\frac{k+2}{3}\|f\|^2.
\tag{DYS-03b}
\]

This is a genuinely nonzero small-support positivity budget at EVERY finite observation radius. It proves that some UV-controlled cone always exists, but is not optimally calibrated.

**Sharper transducer — retain each rung's exact Schur loss.** From the SAME source kernel,

\[
\beta_j(1-\alpha_j\mu/2)
=\frac4{4j+1}-\mu.
\]

Thus whenever \((4J-3)\mu\le4\), the first J source Gamma rungs are each nonnegative and

\[
\boxed{\quad Q_\Gamma(f)\ge
\left(\sum_{j=0}^{J-1}\frac4{4j+1}-J\mu\right)\|f\|_2^2.\quad}\tag{DYS-03c}
\]

The omitted infinitely many original Gamma modes are PSD. This is a complete continuum **all-f restricted-support** theorem, not an approximation in finite-dimensional feature coefficient space. Importantly, the crucial first-prime certificate now needs only **16 actual real Gamma rungs**, not 65,536. Its exact rational sum can be audited directly.

For J=16 and \(\mu=1/16\), the largest retained Schur ratio is \(61/64<1\); every kept Gamma term is positive. The exact sum is

\[
S_{16}:=\sum_{j=0}^{15}\frac4{4j+1}
=\frac{168623511779891008}{24142663793423175},
\qquad
Q_\Gamma(f)\ge(S_{16}-1)\|f\|^2.
\tag{DYS-03d}
\]

No directed floating-point Γ/zeta approximations, empirical eigenvalue fits or imaginary zero positions enter this bound. The full original Gamma tail is left in place as a nonnegative remainder.

**Observation geometry:** A prime clock can pair narrowly localized cells across a translation, but its source companion pays original Gamma energy. The UV protection depends on *total source support measure*, allowing disconnected multi-cell configurations. It does NOT establish control over delocalized superpositions.

## 4. DYS-04: THE ORIGINAL FIRST-PRIME SPARSE-WEIL THEOREM (PROVED ANALYTIC, SOURCE-CONDITIONAL)

**Sharpened theorem.** For every \(0<a\le1/2\) and every nonzero complex \(f\in C_c^\infty(-a,a)\) whose support has Lebesgue measure at most **1/16**,

\[
\boxed{W_\zeta(f*\widetilde f)>\frac1{24}\|f\|_2^2.}\tag{DYS-04}
\]

This is a universal exact restricted-support theorem inside the original **prime-active** window a=1/2. It is NOT the unconditional all-test Weil positivity that would imply RH. This revision makes the permissible support **8192 times larger** than the preliminary 2^-17 certificate, and drops the analytical Gamma cutoff from 65,536 to only 16 source modes.

**Exact original-source proof:**

1. The pinned original Suzuki zeta source certifies \(C_\infty<43/8\). Since \(2/3<\log2<7/10<1<\log3\), for \(0<a\le1/2\) the only genuine prime-power that can activate is n=2 (at a=1/2 it really activates). Original weight \(w_2=\log2/\sqrt2<1/2\); from the positive rational series for log2 one gets \(\log2<25/36<7/10\), while \(\sqrt2>7/5\).
2. \(2a\le1<2\log2\), so the true prime-2 compressed clock has at most two vertices, and DYS-02 bounds its entire negative effect below by \(-\frac12\|f\|^2\). No composite-6 or wrong-conductor feature is admitted.
3. The original negative polar channel costs at most \(2(\sinh a-a)\|f\|^2\). For \(a\le1/2\), the positive power series and \(\sinh a-a\le a^3/[6(1-a^2)]\) give \(2(\sinh a-a)<1/16\). The original positive polar term is simply omitted from a valid lower bound.
4. With \(J=16\), \(\mu=1/16\), (DYS-03c) gives the **exact Fraction** positive real Gamma lower \(S_{16}-1\). The total source-negative budget is strictly below
\[
\frac{43}8+\frac12+\frac1{16}=\frac{95}{16}.
\]
Thus
\[
Q_\zeta(f)>
\left(S_{16}-1-\frac{95}{16}\right)\|f\|^2
=\frac{18140507408283703}{386282620694770800}\|f\|^2
>\frac1{24}\|f\|^2.
\]
5. This is exact rational arithmetic from the first 16 actual Gamma coefficients and SHA-pinned source contact. No hidden limits or samples substitute for the quantified smooth-function theorem. All omitted Gamma and the positive polar channel remain bona fide positive.

**Critical limitations.** The theorem assumes a total support measure <=1/16, not diameter <=1/16: two far-separated small regions are allowed. Arbitrary compact smooth tests can occupy far more of (-1/2,1/2); a fixed bounded-support-measure cone is not dense in full L², so density cannot extend this result to all tests. A global RH conclusion would require one independent domination theorem covering **every** f and every finite a.

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

The proof is DYS-03b plus the genuine finite-clock and polar budgets. This establishes a **nonempty infinite-dimensional positive restricted cone for every finite a**, even far into prime-active windows, while preserving all source couplings. The bound may be extraordinarily small and says NOTHING about delocalized tests.

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

## 7. DYS-07: an ACTUAL prime-2 maximal negative direction protected by genuine completed positivity

The earlier four-anchor path witness uses a synthetic rational clock b=3/4 solely to test exact operator geometry. The following source-faithful direction activates true arithmetic, not a stand-in.

Take \(a=1/2\), \(b=\log2\) and the rational open cell
\[
J=(-31/64,-29/64), \qquad |J|=1/32.
\]
The independently SHA-pinned outward-rational log2 interval proves \(J+\log2\subset(-1/2,1/2)\) and \(J\cap(J+\log2)=\varnothing\). For **every nonzero** complex \(\phi\in C_c^\infty(J)\), form
\[
f(t)=\phi(t)+\phi(t-\log2).
\]
Then \(f\in C_c^\infty(-1/2,1/2)\) and \(|\operatorname{supp}f|\le1/16\). Since the two bumps are disjoint, \( \|f\|_2^2=2\|\phi\|_2^2\); also \(\langle f,S_{\log2}f\rangle=\|\phi\|_2^2\) because exactly one translated copy overlaps. Thus the GENUINE arithmetic prime-2 form saturates its maximally negative two-chain bound:

\[
\boxed{
Q_{\text{prime }2}(f)
=-2\frac{\log2}{\sqrt2}\,\|\phi\|_2^2
=-\frac{\log2}{\sqrt2}\,\|f\|_2^2<0.
}\tag{DYS-07a}
\]

However the exact ORIGINAL full Weil form, containing the independent real Gamma, polar terms and completed contact, satisfies DYS-04 for **every such \(\phi\)**:

\[
\boxed{Q_\zeta(f)>\frac1{24}\|f\|_2^2>0.}\tag{DYS-07b}
\]

**Meaning:** This first-prime positivity result does *not* evade arithmetic by choosing support that cannot interact with a prime. On the contrary, it contains an infinite-dimensional family of tests whose authentic prime clock extracts the sharpest possible negative relative energy, while the genuinely coupled completed source remains positive. That is a valid, sharply discriminating arithmetic positivity transducer.

**Boundary:** The result does not control all f with large/delocalized support and cannot be extrapolated from the restricted 1/16 cone to RH. It is not a proof that every newly activated prime is harmless. It does establish a nontrivial actual-prime positive family beyond the older prime-free local window, rather than merely comparing toy operators.

## 8. Reproduction / provenance / independence

- \`observational_succ/tate_prime_clock_uv.py\`: exact rational clock geometry; original-source and contact pinned sparse theorem; never inserts nontrivial-zero data.
- \`tests/test_tate_prime_clock_uv.py\`: path-boundaries, exact negative 4-anchor witness, original source labels at a=1/2, exact 16-rung Gamma support-Schur gate, contact/pole/prime budget and intentionally broken source cases.
- \`scripts/tate_prime_clock_uv_probe.py\`: printable deterministic receipt (no random fit).
- \`.github/workflows/tate-prime-clock-uv.yml\`: required original source and regression checks on Python 3.10 and 3.13.
- The crucial constant \(C_\infty<43/8\) and source SHA validation are inherited from APOLLO PR #110 K6, not rediscovered.
- Primary: Tate thesis (1950; adeles, Fourier, Poisson); Masatoshi Suzuki, *Weil's quadratic form via the screw function*, arXiv:2606.09096v3 (2026), §§1–2 and §8; Alain Connes and Caterina Consani, *Weil positivity and Trace formula, the archimedean place*, arXiv:2006.13771 (restricted real-place scope).

**Claim ledger:** DYS-01 DERIVED from specified source identities, DYS-02 PROVED CLASSICAL OPERATOR, DYS-03 PROVED ANALYTIC, DYS-04 PROVED ANALYTIC conditional on pinned original-source interval constant, DYS-05 PROVED ABSTRACT, DYS-06 REFUTED shortcuts; full Weil global source-positive contraction UNVERIFIED. **RH PROVED: NO.**
