# OPERATION BESSEL-7 — Genuine Tate/Gamma Fourier polarization and a seven-dimensional original Suzuki low Schur frontier

**Research date:** 2026-10-15. **Base:** SUCC draft PR #126 exact head \`c0f35c6c7b9a6e81704e3ba1c10f4a7891580588\`. Source ancestry: Tate #103, APOLLO #110, true prime clocks #112, completed eta/Tate #114, original high Schur #116 and reflection #126; immutable original zeta Suzuki source Git blob \`0cc8510b71d178fc79e8d410a86d8b6014cf9178\`. **Main unchanged. No release, paper submission, or edits to femboy2112/FuckingRH.** This is original-source mathematics plus classical Fourier/Legendre harmonic analysis; scholarly priority UNVERIFIED. RH remains OPEN.

## A. The accepted proof-bearing target and source

The explicit request is to build a **source-derived arithmetic polarization** that might transport Tate's \(s\leftrightarrow1-s\) reflection, genuine prime-power current and the completed real Gamma into the *positive* Weil/Suzuki form. The previous original APOLLO K2 provides a POSITIVE-MINUS-POSITIVE Krein factorization of the authentic signed kernel, but no all-radius contraction. PR #126 identified the Brownian \(C_\infty\) as the central reflection derivative and separated a holomorphic high-prime-power reflection residual. None of these analytic identities gives Weil positivity.

A consequential smaller goal: prove a strong sign estimate for the ORIGINAL completed Weil form on an infinite-dimensional explicitly specified high source sector, and reduce the genuine zero-shift Suzuki low sign to a smaller finite moment carrier without fitting zeros or swapping the arithmetic source.

Fix \(a=1/2\). For any nonzero complex \(f\in C_c^\infty(-a,a)\), zero-extend to \(\mathbb R\) and write \(Q_\zeta(f)=W_\zeta(f*\widetilde f)\). The inherited ORIGINAL source identification (APOLLO/PR110, DYS-01) states

\[
\boxed{\begin{aligned}
Q_\zeta(f)
={}&
\sum_{j\ge0}\beta_j\langle f,(I-R_{\alpha_j})f\rangle
-C_\infty\|f\|_2^2\\
&+2|\langle f,\cosh(t/2)\rangle|^2
-2|\langle f,\sinh(t/2)\rangle|^2\\
&-w_2\langle f,(S_{\log2}+S_{-\log2})f\rangle,
\end{aligned}}\tag{B7-01}
\]
with
\[
\alpha_j=(4j+1)/2,\quad\beta_j=4/(4j+1),\quad
C_\infty=-\psi(1/4)+\log\pi,\quad
w_2=\log2/\sqrt2.
\]
Here \(R_\alpha\) is real convolution with \(\frac\alpha2e^{-\alpha|t|}\); \(\psi\) is digamma, \(S_b f(t)=f(t-b)\), and the scalar pairing uses original source pole signs. At a=1/2 the SHA-certified prime clock admits n=2 **only**; the genuine compressed two-direction shift has norm exactly 1 because \(a<\log2<2a\). The same SHA-checked source gives \(C_\infty<43/8,\ w_2<1/2\). Gamma rungs are source-positive by Plancherel and all omitted rungs are PSD. The positive cosh polar is dropped only as a correct lower bound.

## B. B7-02 — an EXACT Legendre–Bessel low-frequency projection theorem (CLASSICAL apparatus, PROVED analytic)

The earlier PR #116 Fourier certificate used the crude bound
\(|\widehat f(\omega)|\le\sqrt{2a}\|f\|(a|\omega|)^m/m!\), which loses almost all the beneficial orthogonality information of the Legendre moment nullspace. We recover the *actual* band-limited projection of the plane wave onto the true source moment complement.

Let
\[
\boxed{\int_{-a}^{a}t^k f(t)\,dt=0,\qquad k=0,\ldots,m-1.}\tag{B7-02}
\]

In the normalized Legendre basis \(P_\ell(t/a)\), the classical Jacobi–Anger/plane-wave expansion gives the **exact Parseval projection identity**
\[
\boxed{
\|\mathsf P_{\ge m}e^{-i\omega t}\|_{L^2(-a,a)}^2
=2a\sum_{\ell=m}^\infty (2\ell+1)\,j_\ell(a\omega)^2,
}\tag{B7-03}
\]
where \(j_\ell\) is the real spherical Bessel function. Since f annihilates the first m polynomials, Cauchy–Schwarz and Plancherel on a finite Fourier band yield, for every \(\Omega>0\),
\[
\boxed{
\frac1{2\pi}\int_{-\Omega}^{\Omega}|\widehat f(\omega)|^2d\omega
\le\varepsilon_m(a,\Omega)\|f\|_2^2,
\quad
\varepsilon_m(a,\Omega)
=\frac2\pi\int_0^{a\Omega}
\sum_{\ell=m}^\infty(2\ell+1)j_\ell(z)^2\,dz.
}\tag{B7-04}
\]
This is an **all-f infinite-dimensional inequality** and is not an assumed f-specific Fourier zero.

### Entirely rational upper bound, not finite Bessel numerical sampling

The original spherical Bessel integral can be derived by Rodrigues/integration by parts:
\[
j_\ell(z)=\frac{z^\ell}{2^{\ell+1}\ell!}\int_{-1}^1e^{izu}(1-u^2)^\ell\,du.
\]
For real z≥0, the weight is nonnegative, giving the crucial exact global pointwise upper
\[
\boxed{|j_\ell(z)|\le \frac{z^\ell}{(2\ell+1)!!}.}\tag{B7-05}
\]

The true convergent power series is
\[
j_\ell(z)=\frac{z^\ell}{(2\ell+1)!!}
\sum_{k\ge0}(-1)^k c_{\ell,k}z^{2k},
\quad c_{\ell,0}=1,\quad
c_{\ell,k+1}=\frac{c_{\ell,k}}{2(k+1)(2\ell+2k+3)}.
\]
Let \(P_{\ell,K}(z)\) be the rational polynomial through k=K. On 0≤z≤A, the omitted terms are bounded absolutely by
\[
\boxed{
\delta_{\ell,K}(A)=
\frac{
 A^\ell/(2\ell+1)!!\;
 c_{\ell,K+1}A^{2(K+1)}
}{
 1-A^2/[2(K+2)(2\ell+2K+5)]
}}
\tag{B7-06}
\]
whenever that final ratio is less than 1. This is a genuine geometric remainder, **not** an unproved alternating-series monotonicity assertion. Each finite polynomial square
\[
I_{\ell,K}(A)=\int_0^A P_{\ell,K}(z)^2\,dz
\]
is exactly integrated coefficient-by-coefficient in \(\mathbb Q\). For any rational η>0, Young's inequality
\[
j_\ell(z)^2\le(1+\eta)P_{\ell,K}(z)^2+
(1+\eta^{-1})\delta_{\ell,K}(A)^2
\]
bounds the entire finite mode sector \(\ell=m,\ldots,L-1\).

The infinite genuine spherical-Bessel mode tail is independently bounded by B7-05:
\[
\boxed{
\sum_{\ell=L}^\infty (2\ell+1)\int_0^A j_\ell(z)^2dz
\le\frac{A^{2L+1}}{((2L+1)!!)^2}
\frac1{1-[A/(2L+3)]^2}.
}\tag{B7-07}
\]
No zeros, hidden floating-point estimates, or unperformed ω observations enter these universal source upper bounds.

Using only the elementary \(\pi>3\), evaluate in EXACT rational arithmetic:
\[
\boxed{
a=1/2,\quad m=7,\quad\Omega=49/4,\quad
A=49/8,\quad L=20,\quad K=10,\quad\eta=1/10000
\ \Longrightarrow\ 
\varepsilon_7(1/2,49/4)<\frac1{61}.
}\tag{B7-08}
\]
\`observational_succ.tate_bessel_seven_schur.exact_legendre_low_frequency_enclosure\` recomputes the whole finite rational integral and all omitted mode/series corrections and FAILS CLOSED if any parameter invalid. Independent mpmath Bessel evaluations are calibration only.

## C. B7-03 — the completed original negative polar term is ALSO suppressed by the SAME seven moments

A subtle source repair is necessary. An earlier 18-moment certificate simply threw away the genuine negative sinh-polar using the coarse bound \(2(\sinh a-a)\|f\|^2\). With seven moments it must be controlled **more sharply**, not silently deleted.

Since f annihilates degree≤6, integrate it against the degree-six Taylor polynomial of \(\sinh(t/2)\) and use the real Taylor remainder. For |t|≤a=1/2, \(|\partial_t^7\sinh(t/2)|\le2/2^7\) (because \(e^{1/4}<2\)). By Cauchy–Schwarz, \(\|f\|_1\le\sqrt{2a}\|f\|_2=\|f\|_2\), so
\[
|\langle f,\sinh(t/2)\rangle|
\le 2\frac{(a/2)^7}{7!}\|f\|_2.
\]
The authentic negative pole therefore obeys
\[
\boxed{
2|\langle f,\sinh(t/2)\rangle|^2
\le
\frac{8(a/2)^{14}}{(7!)^2}\|f\|^2
<\frac1{10000}\|f\|^2.
}\tag{B7-09}
\]
The full original pole channels and all signs have remained present.

## D. B7-04 — FIRST-PRIME ORIGINAL WEIL POSITIVITY FROM JUST SEVEN MOMENTS (PROVED analytic)

Use the first 128 **TRUE** Gamma rungs:
\[
m_{128}(\Omega)=\sum_{j=0}^{127}\frac4{4j+1}
\frac{\Omega^2}{\Omega^2+(4j+1)^2/4}.
\]
At the exact source-independent rational Fourier clock \(\Omega=49/4\),
\[
\boxed{m_{128}(49/4)>\frac{3019}{500}.}\tag{B7-10}
\]
The independent mathematical proof and executable Fraction loop evaluate this finite true real-Gamma sum, not a fake positive surrogate.

The genuine negative contact and prime budgets are
\[
C_\infty+w_2<\frac{43}8+\frac12=\frac{47}{8};
\]
the negative sinh term is bounded by B7-09, and the positive cosh rank-one channel is retained but discarded only under lower order. Combine exact source Gamma multiplier, B7-04, B7-08 and B7-09:
\[
\begin{aligned}
Q_\zeta(f)
&>
\left[m_{128}(49/4)(1-\varepsilon_7)
-\frac{47}{8}
-\frac{8(a/2)^{14}}{(7!)^2}\right]\|f\|^2\\
&>
\left[\frac{3019}{500}\left(1-\frac1{61}\right)
-\frac{47}{8}-\frac1{10000}\right]\|f\|^2.
\end{aligned}
\]
The last number is the exact rational \(\frac{38989}{610000}\), which is **strictly greater** than \(1/16\). Thus:

\[
\boxed{
\begin{gathered}
\forall f\in C_c^\infty(-1/2,1/2;\mathbb C)\setminus\{0\},\\
\left(\forall\,0\le k\le6,\ \int t^k f(t)\,dt=0\right)
\Longrightarrow\quad
W_\zeta(f*\widetilde f)>\frac1{16}\|f\|_2^2.
\end{gathered}}
\tag{B7-11}
\]

This is **source-true**, not conditional on RH. The entire proof is a deterministic finite-rational inequality on universal Fourier projection bounds plus classical original Weil/Suzuki source equality. It does NOT certify the remaining low seven-dimensional source or all tests on the interval.

A hostile rank-six test of the same source cutoff yields \(\varepsilon_6>1/20\) and a negative *conservative method lower bound*; this is evidence ONLY that this particular proof technique is insufficient at rank six, not a genuine negative completed Weil witness.

## E. B7-05 — RIGOROUS ORIGINAL 7×7 ZERO-SHIFT SUZUKI LOW FRONTIER (PROVED high theorem, low sign UNKNOWN)

Work in the real original Suzuki mean-zero derivative carrier \(H=L^2_0(I)\), \(I=(-1/2,1/2)\), and set
\[
(Vu)(t)=\int_{-a}^t u(s)ds,\qquad K=V^*V=(-\Delta_N)^{-1}.
\]
The source identity is \(\langle u,Gu\rangle=Q_\zeta(Vu)\), and \(\langle u,Ku\rangle=\|Vu\|^2\). Let P project onto the **FIRST SEVEN** genuine Legendre derivative modes \(P_1(t/a),\ldots,P_7(t/a)\) and Q=1−P.

For EVERY \(u\in QH\), integration by parts gives
\[
0=\langle u,P_j(t/a)\rangle
=-\langle Vu,P_j'(t/a)\rangle,\qquad j=1,\dots,7.
\]
The derivatives of the first seven Legendre modes span the polynomial space of degrees 0,...,6. Therefore f=Vu satisfies *every* moment hypothesis of B7-11; the estimate extends from compact smooth tests to \(H_0^1\) by finite-dimensional moment-preserving density and the source's continuous signed quadratic form.

The **actual compact signed Suzuki operator** satisfies
\[
\boxed{
D_7:=QGQ\succeq\frac1{16}QKQ.
}\tag{B7-12}
\]

This is the same K-relative high positivity constant as our older 18- and 15-/30-mode programs but with only **seven** remaining genuine low modes, separated as 4 odd +3 even. It is NOT a forbidden \(D_7\succeq cI\) spectral gap: K is positive compact on the infinite high sector.

Now invoke the independently sourced PR #109 genuine \(\|g'\|_{L^1(-1,1)}<11/40\). With the real P/Q blocks
\[
A=PGP,\quad B=PGQ,\quad D=QGQ,
\]
the genuine increasing zero-shift positive resolvent exists as a bounded low-space quadratic form
\[
R_0=\lim_{\lambda\downarrow0}B(D+\lambda I)^{-1}B^*,
\qquad
0\preceq R_0\prec\frac{(11/40)^2}{1/16}I_7
=\boxed{\frac{121}{100}I_7}.
\tag{B7-13}
\]

The REAL source low Schur is \(S_0=A-R_0\). We have **NOT** constructed/verified its 7×7 original-source sign, so this does not solve first-window Weil positivity or RH. A zero-shift source-valid high trial \(U\) still must certify
\[
\boxed{
A-L_U-16C_U\succeq0,\quad
L_U=BU+U^*B^*-U^*DU,
\quad
C_U(i,j)=\langle [G(e_i-Ue_i)]',[G(e_j-Ue_j)]'\rangle.
}\tag{B7-14}
\]
This inequality would imply complete sign on that *single* first-prime interval; all radii remain RH-hard.

The source K low/high cross-boundary rank two and reflection parity \((4,3)\) are computed in original exact Legendre coordinate formulas. **No all-a K4 positive-feature contraction is inferred**; source low Schur and all-radii signed gluing remain UNVERIFIED.

## F. Hostile controls, epistemic / source debts and next moonshot

- **Genuine source:** SHA-pinned \(\log2\), \(p^{-1/2}\), C∞, exactly one real 4j+1 Gamma ladder, correct 8s²−8h² polar channels, true prime shift norm one. Fake primitive 6, mutated conductor/parity/half-density or Gamma-contact mismatch are forbidden by original repo parent source checks.
- **Actual infinite-dimensional tests:** m7 moments on C_c∞ and their legitimate H_0^1 dense extension; spherical Bessel plane-wave projection is mathematical for all ω in the band. A finite matrix of seven sample vectors would not prove B7-11.
- **No numerical eigenvalue fitting:** all finite gamma, spherical power-series polynomial, Bessel high-mode and error bounds are exact \(\mathbb Q\) computations; mpmath is a separate sanity holdout.
- **Method no-go:** repeating the same rational cutoff with rank m6 does not certify the sign; record INCONCLUSIVE, never call it a counterexample. Similarly a *negative finite-J original low matrix* can be rescued by omitted positive Gamma modes, so a truncated negative diagonal is no RH witness.
- **Original source 7×7 scan:** run \`scripts/tate_bessel_source_low7_scan.py\` at J finite, preserve both polar channels and the original positive remainder with rigorous tail; keep truncated diagnostic separate from the actual \(S_0\) sign.
- **Next proof step:** source-defined trial high U for 4+3 low parity modes, fully computed signed continuum \(C_U\), genuine \(A-L_U-16C_U\) interval PSD or an independently authenticated negative witness. Compare the PR #109 source derivative estimate, authentic original Legendre direct matrix, and Fourier–Bessel all-test coercivity. At every new prime birth use paired-source contact gluing, never independently nest Krein positive and negative channels.

**Artifact/provenance:** \`observational_succ/tate_bessel_seven_schur.py\`, \`tests/test_tate_bessel_seven_schur.py\`, \`research/2026-10-15/TATE_BESSEL_SEVEN_SCHUR_RECEIPT.json\`, \`scripts/tate_bessel_seven_probe.py --verify\`, \`.github/workflows/tate-bessel-seven.yml\`; sibling first-prime original signed kernel from PR #126 and #109 unchanged. Scholarly priority unverified.

**Primary mathematical references:** Tate's thesis, real Gaussian Fourier; Suzuki, *Weil's quadratic form via the screw function*, arXiv:2606.09096v3 (2026), and classical spherical Bessel/Legendre plane-wave formulas (NIST DLMF §§10.47, 10.54). **RH PROVED: NO.**
