# TATE → WEIL → SUZUKI: ORIGINAL-SOURCE FOURIER HIGH-MOMENT COERCIVITY AND ZERO-SHIFT SCHUR

**Research checkpoint:** October 15, 2026. **Status:** NEW-TO-SUCC original-source analytic theorem and exact-rational source certificates, subject to independent mathematical review; RH **NOT** proved. Classical Tate/Suzuki/Weil, Fourier/Plancherel, Legendre and Schur facts credited; original scholarly priority UNVERIFIED.

**Branch:** \`research/tate-suzuki-fourier-high-moment-2026-10-15\`, parent DYSPON II PR #114 exact \`9bcb7f4cc28128fa6171c1479d3d804b24e32bd3\`, transitively source PR #112, APOLLO #110, ONE OBJECT #106, Tate #103, Phoenix-II main \`03db44203147a7b28d445bb9f970fa71360e78c4\`. **Sibling PR #109** at \`6748cb8dd9d0eb186be18a75ed9ae1d94e9e898b\` is imported VERBATIM as **ten immutable, Git-blob referenced existing files** (source codes/tests/receipts/workflow). No alteration of source archive, no main update, no cross-repo export.

The user's objective is to build a genuine *arithmetic positivity transducer* from Tate's correctly normalized source, not a generic positive Gram or fictional physical observer. The hard target remains full original Weil positivity on all smooth compact test functions, equivalent to RH. Our meaningful bounded mission is **a new proof of the genuine first-prime high-sector sign**, coupled rigorously to the original Suzuki 30-low/high zero-shift Schur problem.

## 1. EXACT target, original arithmetic source and functional-analytic carrier

Fix the **real first-prime interval** \(I=(-a,a)\) with \(a=1/2\). For an admissible complex \(f\in C_c^\infty(I)\), let

\[
Q_\zeta(f):=W_\zeta(f*\widetilde f)
=\iint_{I^2}K_g(x,y) f'(x)\overline{f'(y)}\,dx\,dy.
\]

This equality is the classical Weil/Suzuki distributional mixed-derivative identification, source-verified by APOLLO and ONE OBJECT. \(K_g(x,y)=g(x-y)-g(x)-g(y)+g(0)\) is the **original** signed screw potential. \(\Lambda(n)/\sqrt n\) is the authentic half-density prime-power source; on \(|x-y|<1\) the ONLY active jet is \(n=2\), with \(b=\log2\) and \(w_2=\log2/\sqrt2\). The real Gamma source occurs **once**, and both polar terms plus the original \(C_\infty=-\psi(1/4)+\log\pi\) contact are mandatory.

From the previously established DYSPON-SPHERE I original-source identity (DYS-01), set

\[
\alpha_j=\frac{4j+1}{2},\qquad \beta_j=\frac4{4j+1},
\qquad R_\alpha f=\frac{\alpha}{2}e^{-\alpha|\cdot|}*f.
\]

The actual signed completed Weil quadratic form is

\[
\boxed{\begin{aligned}
Q_\zeta(f)
={}&
\sum_{j\ge0}\beta_j\langle f,(I-R_{\alpha_j})f\rangle
-C_\infty\|f\|_2^2\\
&\quad+2\left|\int_I f(t)\cosh(t/2)\,dt\right|^2
-2\left|\int_I f(t)\sinh(t/2)\,dt\right|^2\\
&\quad-w_2\langle f,(S_b+S_{-b})f\rangle .
\end{aligned}}\tag{TSF-01}
\]

Here f is zero-extended to the real line, \((S_bf)(t)=f(t-b)\). The finite real-place Gamma terms are genuinely PSD because the Fourier multiplier is \(1-\alpha^2/(\alpha^2+\omega^2)\ge0\), but the full sum is signed. On the first-prime interval, the **compressed two-direction prime translation** has norm \(\le1\), a classical finite-path result rigorously source-checked in DYSPON I. Thus (original outward-rational source bounds)

\[
C_\infty<43/8,\quad 0<w_2<1/2,\quad
2(\sinh(1/2)-1/2)<1/16,
\]

give a NEGATIVE source budget **strictly smaller** than

\[
\boxed{\mathcal N=43/8+1/2+1/16=95/16.}\tag{TSF-02}
\]

The positive cosh-polar channel and any omitted Gamma rungs are discarded only as valid lower bounds. An authentic mutant source with a wrong \(\Gamma\), contact, half-density, extra composite 6, prime omission, or pole sign is NOT allowed to inherit this budget.

## 2. The real Tate Gamma Fourier multiplier (PROVED ANALYTIC)

Use the declared additive Fourier transport \(\widehat f(\omega)=\int f(t)e^{-i\omega t}\,dt\), with Plancherel factor \(d\omega/(2\pi)\). This is an additive log chart for compact multiplicative Tate tests; it is NOT an independent adelic trace.

The Fourier transform of the source OU kernel is

\[
\widehat{\left(\frac\alpha2e^{-\alpha|t|}\right)}(\omega)
=\frac{\alpha^2}{\alpha^2+\omega^2}.
\]

Therefore each TRUE Gamma mode has multiplier

\[
\beta_j\frac{\omega^2}{\alpha_j^2+\omega^2}.
\]

For any integer \(J\ge1\) define the exact (monotonically increasing in \(|\omega|\)) rational finite-Gamma multiplier

\[
\boxed{
m_J(\Omega)=
\sum_{j=0}^{J-1}\frac4{4j+1}
\frac{\Omega^2}{\Omega^2+(4j+1)^2/4}.
}\tag{TSF-03}
\]

Then \(\Gamma\) source positivity yields, **for every** smooth compact test f,

\[
Q_\Gamma(f)\ge
m_J(\Omega)\frac1{2\pi}
\int_{|\omega|\ge\Omega}|\widehat f(\omega)|^2\,d\omega.
\tag{TSF-04}
\]

No location of a nontrivial zeta zero enters this construction or inequality.

## 3. SUCC observer transducer: 30 Legendre observations annihilate dangerous low Fourier mass

Let \(m\) be an integer with \(1\le m\le30\). Suppose f is supported in \(I=(-1/2,1/2)\) and satisfies

\[
\boxed{
\int_I t^k f(t)\,dt=0,\qquad k=0,\ldots,m-1.
}\tag{TSF-05}
\]

These are source-independent polynomial moment observations, not spectrally fitted eigenvectors. Crucially, the remainder after subtracting the first m terms of the OSCILLATORY Taylor expansion of \(e^{-i\omega t}\) satisfies

\[
\left|e^{-i\omega t}
-\sum_{k=0}^{m-1}\frac{(-i\omega t)^k}{k!}\right|
\le \frac{(|\omega t|)^m}{m!}.
\]

Unlike a generic complex exponential error, the source phase is purely imaginary and its integral Taylor remainder has absolute value at most \(1\); inserting the crude factor \(e^{|\omega t|}\) would greatly weaken this proof. Moment cancellation thus gives

\[
|\widehat f(\omega)|\le\sqrt{2a}\|f\|_2\frac{(a|\omega|)^m}{m!}.
\]

Integrating exactly over the low Fourier window, using \(\pi>3\), produces a **completely rational and universal** Plancherel mass bound

\[
\boxed{\begin{aligned}
\frac{1}{2\pi}\int_{|\omega|\le\Omega}
|\widehat f(\omega)|^2\,d\omega
&\le \varepsilon_m(a,\Omega)\|f\|_2^2,\\
\varepsilon_m(a,\Omega)
&=\frac{2a\Omega}{3(2m+1)}
\frac{(a\Omega)^{2m}}{(m!)^2}.
\end{aligned}}\tag{TSF-06}
\]

The bound is strict whenever \(\widehat f\not\equiv0\), since \(\pi>3\). For \(\Omega=12,a=1/2\), the expression is a Fraction; no floating precision is being mistaken for a proof.

Combine (TSF-01) through (TSF-06):

\[
\boxed{
Q_\zeta(f)>
\underbrace{\left(
m_J(\Omega)[1-\varepsilon_m(1/2,\Omega)]
-\frac{95}{16}\right)}_{\mathfrak c_{m,J,\Omega}}
\|f\|_2^2
}\tag{TSF-07}
\]

for all nonzero smooth compact f satisfying the m moment constraints. The original source was used in both the positive and negative terms. This is a bona fide **Weil form inequality over infinite-dimensional classes**, not a sampled matrix.

### Exact-rational positive results (original zeta, not surrogates)

Take \(J=32,\ \Omega=12,\ a=1/2\).

\[
m_{32}(12)=
\sum_{j=0}^{31}\frac4{4j+1}
\frac{144}{144+(4j+1)^2/4}
>6,
\]
an independently computed, stored exact Fraction (the full numerator/denominator are in the immutable proof receipt).

The Python \`Fraction\` proof evaluates \(\mathfrak c_{m,32,12}\) without machine floats and certifies:

| Vanishing power moments | Source-positive lower | Status |
|---|---|---|
| \(m=15\) | current conservative \(\mathfrak c_{15,32,12}<0\) | **INCONCLUSIVE**, not a negative original Weil witness |
| \(m=16\) | \(\mathfrak c_{16,32,12}>1/20\) | **PROVED source-analytic** |
| \(m=18\) | \(\mathfrak c_{18,32,12}>1/16\) | **PROVED source-analytic** |
| \(m=30\) | \(\mathfrak c_{30,32,12}>1/16\) | **PROVED source-analytic** |

For m≥18 the rational \(\varepsilon_m\) strictly decreases because \(\varepsilon_{m+1}/\varepsilon_m=(6/(m+1))^2(2m+1)/(2m+3)<1\). Hence the \(1/16\) lower holds uniformly for every m≥18 within this source proof's declared finite-rank range.

**The missing all-tests low moments are not removed by this theorem. RH OPEN.**

## 4. THE SOURCE-PRESERVING BRIDGE INTO SUZUKI/PR109'S EXACT NEUMANN METRIC

This step is the core mathematical interface, not an analogy.

Let \(H=L^2_0(I)\) be the mean-zero **derivative-coordinate Hilbert carrier**, and for \(u\in H\) define

\[
(Vu)(t)=\int_{-a}^t u(s)\,ds,\qquad a=1/2.
\]

Since \(\int_Iu=0\), \(f=Vu\) has zero trace at BOTH endpoints and belongs to \(H_0^1(I)\). Let \(G\) be the original compact Suzuki integral operator, with convolution kernel \(g(x-y)\), and \(K=V^*V=(-\Delta_N)^{-1}\) on mean-zero \(H\). The classical/PR109 source identities give

\[
\boxed{
\langle u,Gu\rangle=Q_\zeta(Vu),
\qquad
\langle u,Ku\rangle=\|Vu\|_2^2.
}\tag{TSF-08}
\]

Both are **actual original** sourced quadratic forms. There is NO compact-operator \(\kappa I\) gap.

Let \(P_r\) be the \(L^2(I)\) orthogonal projection onto the genuine unnormalized Legendre modes \(P_1(t/a),...,P_r(t/a)\) and let \(Q_r=1-P_r\) on H. For every \(u\in Q_rH\),

\[
\int_I u(t)P_j(t/a)\,dt=0,\quad j=1,\ldots,r.
\]

Integrating by parts in the **same source chart**,

\[
0=\int_I f'(t)P_j(t/a)\,dt
=-\int_I f(t)\frac d{dt}P_j(t/a)\,dt.
\]

The Legendre derivatives for j=1..r span the real polynomial space of degrees 0..r−1. Therefore f satisfies **ALL** TSF-05 moment constraints with m=r. The proof initially established on compact smooth f extends to the full \(H_0^1\) domain by density and finite-dimensional moment corrections (choose r compact smooth bumps with invertible moment matrix to correct any approximating sequence). No finite-grid support assumption enters.

Consequently:

\[
\boxed{
D_{16}:=Q_{16}GQ_{16}
\succeq\frac1{20}Q_{16}KQ_{16},
}\tag{TSF-09a}
\]

and for **all integer \(18\le r\le30\)**,

\[
\boxed{
D_r:=Q_rGQ_r
\succeq\frac1{16}Q_rKQ_r.
}\tag{TSF-09b}
\]

This is an independently derived original-source high sector relative positivity theorem; the inherited PR #86/PR #109 30-moment constant was only \(\kappa_{\rm old}=369/10000\). On the **same r=30** carrier, \(1/16>369/10000\). Both constants are in the **inverse-Neumann \(K\) metric**, not a forbidden \(L^2\) spectral-gap replacement. More strikingly, (TSF-09b) works at **r=18**, reducing the remaining low-dimensional sign gate to **18×18**, split as 9 even / 9 odd modes by reflection (and r=16 is a 8+8 alternative with a smaller \(\kappa=1/20\)).

**Dependency and novelty ledger:** Fourier/Legendre/Sobolev proofs are classical apparatus; their numerical source-specific quantitative combination is new-to-repository, not claimed new academic mathematics. The original Weil identification and PR109 \(g'\) estimate are imported on authenticated SHAs. PR109's premise \(D\ge369/10000\,K\) is no longer necessary for this high theorem.

## 5. The zero-shift Feshbach/Douglas theorem is sharpened — BUT THE LOW SIGN IS STILL OPEN

Source sibling PR #109 proves by outward-rational genuine Gamma/contact/prime/pole cancellation, with a separate analytic treatment of the origin log singularity,

\[
g\in W^{1,1}(-1,1),\qquad
\|g'\|_{L^1(-1,1)}<11/40.
\tag{TSF-10}
\]

Young's inequality for the actual truncated convolution gives

\[
\|(Gx)'\|_2\le\frac{11}{40}\|x\|_2.
\]

In the Feshbach split \(H=P_rH\oplus Q_rH\), write

\[
A=P_rGP_r,\quad B=P_rGQ_r,\quad D=Q_rGQ_r.
\]

The true high/low resolvent (not a fictitious positive covariance) has zero-shift limit

\[
R_0=\lim_{\lambda\downarrow0}B(D+\lambda I)^{-1}B^*.
\]

One can use the variational formula, integration by parts \(\langle Gx,h\rangle=-\langle(Gx)',Vh\rangle\), and (TSF-09) directly, without a compact \(D^{-1}\), obtaining the **rigorous original-source improvements**

\[
\boxed{\begin{array}{ll}
r=16:&0\preceq R_0\prec (121/80)\,I_{16},\\
r=18:&0\preceq R_0\prec (121/100)\,I_{18},\\
r=30:&0\preceq R_0\prec (121/100)\,I_{30}.
\end{array}}\tag{TSF-11}
\]

PR109's older same-rank \(r=30\) bound was \(3025/1476\approx2.04946\); the new bound is exactly \(121/100=1.21\). The true zero-shift Douglas range inclusion follows on each chosen finite low carrier, and the *unshifted* finite-dimensional short

\[
S_0=A-R_0
\tag{TSF-12}
\]

exists and controls the original entire first-prime sign. We have **NOT** certified \(S_0\succeq0\). In fact, the crude \(R_0\) norm bound CANNOT suffice:

Because \(g(0)=0\), \(\|g\|_{L^1[-1,1]}\le\|g'\|_{L^1[-1,1]}<11/40\), so \(\|A\|\le\|G\|<11/40\). Thus even with our improved \(\kappa\), the norm-only sufficient matrix

\[
A-(121/100)I\preceq
\left(\frac{11}{40}-\frac{121}{100}\right)I
=-\frac{187}{200}\,I
\]

is *strictly negative*. This proves the **specific norm-only sufficient test is hopeless**; it does NOT prove \(S_0\) negative. We must resolve the source-specific low/high cross correlations via an actual trial/residual map \(U\), as in imported PR109:

\[
\boxed{
A-L_U-\kappa^{-1}C_U
\preceq S_0
\preceq A-L_U,
}\tag{TSF-13}
\]

with \(L_U=BU+U^*B^*-U^*DU\), \(C_U(i,j)=\langle[G(e_i-Ue_i)]',[G(e_j-Ue_j)]'\rangle\), \(U:P_rH\to Q_rH\), and **the same original signed source throughout**. Certifying the **actual** lower matrix PSD would prove full first-prime-window Weil positivity, not RH at all radii.

The ordinary \(\eta\)/Eisenstein/Möbius/Poisson source transducer from parent #114 matters here as a **source passport and reconstruction/normalization channel**; it does NOT make \(C_U\) vanish or identify an independent positive Hilbert source by itself.

## 6. Hostile tests, source/observer boundaries, and next new transducers

**Controls discharged / exact receipt:**
- Native \(j\mapsto4j+1\) Tate real Gamma spectrum; wrong \(4j+3\) parity loses the 30-high proof margin.
- Exact no-zero rational Fourier multiplier \(m_{32}(12)\); first-prime source at 2 only; original contact/polar normalization.
- Moment rank 15 gives a negative **conservative bound only**, NOT an authentic negative source witness. Rank 16 and 18 positive with explicitly different \(\kappa\). Exact Legendre mode \(P_{r+1}\) has primitive \(V P_{r+1}\) annihilating first r power moments, verified for r=16,18,30 using exact rational polynomial algebra.
- Sibling PR109 source \(g'\) interval proof rerun; source \(\Gamma\)/prime/contact and **origin primitive** compared to immutable PR85 original source; trace/conductor Gamma_R/pole passport from Tate #103/DYSPON II.
- Wrong contact +1/10 exhausts the rank16 published \(1/20\) budget; it is intentionally **NOT** the authentic zeta source. Fake primitive composite 6 rejected by eta/Euler source even if its clock lies outside the first interval.
- Full high-sector \(D\ge\kappa K\) and true zero-shift bound are paper proofs, not finite sampled matrix certificates. Synthetic exact finite-block experiments exercise both positive and negative low Schur outcomes; neither is zeta.
- Genuine \`authentic_full_low_entry(1,1,J=2)\` and its parity-cross-zero entry use actual original signed source intervals; they are **NOT** the unresolved entire 18×18/30×30 Schur, nor a global sign certificate.

**Next verdict-changing execution program:**
1. Compute **all** original low Legendre signed matrix intervals \(A_J\) at ranks 18 and 30 using the existing analytic \`suzuki_legendre_source.authentic_full_low_entry\`, with the source-positive omitted Gamma tail. Build a certified, source-matched approximate high trial \(U\) and the continuum derivative residual matrix \(C_U\) with analytic quadrature/error.
2. Evaluate the 9+9 (or 8+8) true source Schur sufficient matrix (TSF-13) rigorously at \(a=1/2\). A positive eigenvalue **of each bound** is irrelevant; need full matrix PSD by rational interval LDL/Schur with all high correlations. A negative upper-short genuine source witness would falsify RH after independent audit; a failed sufficient bound is ambiguous.
3. Develop a **radius-dependent** Fourier-moment cutoff \(r(a)\), prime path norm budget \(\sum_{\log n<2a}2 w_n\cos(\pi/(\lceil2a/\log n\rceil+1))\), and Gamma threshold \(\Omega(a)\). Prove which positive high sectors transport across all source births. This supplies a finite-codimension positive carrier for every fixed a, not a proof that the *low shorted signs* remain positive for all a.
4. Orthogonally attempt a truly signed Tate/Connes trace/Arakelov polarization that directly manufactures the low short without assuming RH. Require fake six, changed half density, wrong \(4j+3\) real parity, altered polar/contact and primitive twisted-character controls.

**Claim ledger:** TSF-01 original Weil/Suzuki imported, TSF-02 original source bounds imported, TSF-03 Fourier Gamma classical derivation PROVED, TSF-05–07 source original high-moment inequality PROVED analytic with exact rational, TSF-08–09 classical/source transport plus NEW-TO-SUCC stronger high Neumann bound PROVED analytic, TSF-10 sibling PR109 source theorem imported/independently run, TSF-11 zero-shift improvement PROVED given source statements, TSF-12–13 correct sign contract still UNVERIFIED. All-radii positivity **UNVERIFIED**; RH **OPEN**.

**Files and reproduction:** \`observational_succ/tate_suzuki_fourier_schur.py\`, \`tests/test_tate_suzuki_fourier_schur.py\`, \`scripts/tate_suzuki_fourier_high_probe.py --verify\`, \`research/2026-10-15/TATE_SUZUKI_FOURIER_HIGH_RECEIPT.json\`, \`.github/workflows/tate-suzuki-fourier-high.yml\`. PR109 original-code SHA has been imported intact and is part of mandatory CI regressions; independent academic peer-review not performed.

**Literature:** Tate, *Fourier Analysis in Number Fields and Hecke's Zeta-Functions* (1950), SUCC PR #103 source chart; Suzuki, *Weil's quadratic form via the screw function*, arXiv:2606.09096v3 (2026); Connes–Consani, *Weil positivity and Trace formula, the archimedean place*, arXiv:2006.13771 (restricted comparator). **RH PROVED: NO.**
