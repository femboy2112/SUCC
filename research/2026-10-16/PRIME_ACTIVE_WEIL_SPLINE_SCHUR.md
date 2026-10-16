# Operation MOONSHOT — source-certified prime-active Weil splines and the low-Schur frontier

**Date:** 2026-10-16. **Branch:** `research/prime-active-source-weil-spline-schur-2026-10-16`.
**Parent:** `research/tate-mellin-prime-fucc-escape-2026-10-16` at `d7545a1c5fe7b16d12af877513283f802f3d151d` (draft PR #146, stacked on #145/#142/#141).
**Status:** classical Suzuki/Weil distribution and Fourier/Sobolev theorems imported with exact stated assumptions; PWS-01–11 below are **PROVED PAPER / exact rational computer-aided finite certificates** *inside specified domains*, independently numerically calibrated; no priority claim. **Independent cross-checks of already proved low-mode facts are not new mathematical milestones.**
**RH PROVED: NO. The original low Schur sign remains UNVERIFIED.**

## 0. Why this step is not another positive probability Gram

Previous source charts reconstruct \(\Gamma_{\mathbb R}(s)\zeta(s)\) using positive Beta/exponential/Dirac and prime-valuation laws in \(\Re s>1\) (TMF, PR #146). A positive probability Gram on that half-plane does **not** equal the completed signed Weil form. The independently established classical bridge is

\[
(\mathcal L_\zeta,H_g)\ \longrightarrow\
\mathcal L_\zeta'/\mathcal L_\zeta\ \overset{\text{contour}}\longrightarrow\
W_\zeta(g),\quad g\in C_c^\infty(\mathbb R),
\]

with normalized \(\mathcal L_\zeta=\pi^{-s/2}\Gamma(s/2)\zeta(s)\), poles at 0,1 and the correctly regularized Archimedean identity distribution. This is the existing CTW-08 theorem in `research/2026-10-15/TATE_TO_WEIL_DISTRIBUTION.md`, not a new discovery. Its source-to-test contract also explains why differentiating a test-dependent product \(H_g(s)\mathcal L(s)\) produces spurious \(H'_g/H_g\) terms. **We instead evaluate the actual original signed distribution on explicit test functions.**

Write \(\widetilde f(u)=\overline{f(-u)}\). The genuine zeta source is

\[
\begin{aligned}
W(g)&=P(g)+A(g)-E(g),\\
P(g)&=\int_{\mathbb R} (e^{u/2}+e^{-u/2})g(u)\,du,\\
E(g)&=\sum_{n=p^k\ge2}\frac{\log p}{\sqrt{n}}
       [g(\log n)+g(-\log n)],\\
A(g)&=c_\zeta g(0)-\int_0^\infty
\frac{e^{-x/2}}{1-e^{-2x}}
[g(x)+g(-x)-2e^{-x/2}g(0)]\,dx,\\
c_\zeta&=-\gamma_E-\log(4\pi).
\end{aligned}\tag{0.1}
\]

The sum is finite for compactly supported \(g\); the contact compensation is essential. Parameters: **conductor 1, even parity, half-density \(1/2\), root number 1, both polar residues, authentic \(\Lambda(p^k)=\log p\), \(\Lambda(6)=0\)**. This is the exact source interface used throughout. Test values need not be a priori positive. Numerically sampled Gamma integrals or approximate zero positions are not certificates.

## PWS-01. A finite, genuinely prime-active Schwartz–Tate test interface (CLASSICAL / exact)

Let \(B_3\) be the centered cardinal cubic B-spline, a fourfold convolution of the uniform density on \([-1/2,1/2]\), and \(B_7=B_3*B_3\). In exact rational truncated-power coordinates,

\[
B_3(x)=\frac1{3!}\sum_{j=0}^{4}(-1)^j{4\choose j}(x+2-j)_+^3,\quad
B_7(x)=\frac1{7!}\sum_{j=0}^{8}(-1)^j{8\choose j}(x+4-j)_+^7.
\tag{1.1}
\]

Choose the **same** fixed width \(h=1/5\) and centers \(t_0=0,t_1=1/10\):

\[
f_i(u)=h^{-1}B_3((u-t_i)/h),\quad
\operatorname{supp}f_0=[-2/5,2/5],\quad
\operatorname{supp}f_1=[-3/10,1/2].
\tag{1.2}
\]

These are nonzero real \(C^2\) compactly supported functions supported in the **closed** original Suzuki interval \([-a,a]\), \(a=1/2\). The second test touches the right endpoint, so it is **not literally** an element of \(C_c^\infty(-a,a)\); boundary vanishing to third order and smooth inner cutoff/mollification put both in the \(H_0^1\) closure. The Weil pairing extends by the existing fixed-support \(C^1\) continuity estimate to their autocorrelations. The Tate lift \(x^{-1/2} f_i(\log x)\) is \(C_c^2\) away from \(x=0\) (not necessarily Schwartz-smooth until mollified), with exact Mellin \(H_{f_i}(s)\). No global smoothness is inferred from finite-polynomial formulae. Importantly, their autocorrelations are **exact piecewise rational splines**:

\[
g_{ij}(u)=f_i*\widetilde f_j(u)
  =h^{-1}B_7((u-t_i+t_j)/h).
\tag{1.3}
\]

The widest support is \([-9/10,9/10]\), containing \(\pm\log2\) but not \(\pm\log3\). The genuine prime tape for **every** entry is exactly \(((n,p)=(2,2))\), certified by rational atanh enclosures of \(\log2,\log3\) and a conservative \(e^R<3^{\lceil R\rceil}\) integer bound. In particular there is *one genuine half-density prime impulse* and no fake composite 6.

## PWS-02. Entirely rational, outward-certified Archimedean transport (PROVED PAPER)

For \(g_d(u)=h^{-1}B_7((u-d)/h)\), its exact moment generating function gives the whole polar term without quadrature:

\[
P(g_d)=2\cosh(d/2)\left[\frac{\sinh(h/4)}{h/4}\right]^8.\tag{2.1}
\]

This is because \(B_7\) is an eightfold convolution of centered uniform densities. The complete Gamma ladder with \(\alpha_j=2j+1/2\) is

\[
\begin{aligned}
A_J(g_d)={}&c_\zeta g_d(0)-\sum_{j<J}
\Bigg[\int_0^\infty e^{-\alpha_jx}(g_d(x)+g_d(-x))\,dx
 -\frac{2g_d(0)}{\alpha_j+1/2}\Bigg].
\end{aligned}\tag{2.2}
\]

Do not discard the all-\(x\) contact compensator. Every truncated integral in (2.2) is the Laplace transform of a **finite rational piecewise polynomial**. On each cell, calculate \(\int_L^R x^m e^{-\alpha_j x}\,dx\) by the exact recurrence

\[
M_0=\frac{e^{-\alpha_j L}-e^{-\alpha_j R}}{\alpha_j},\quad
M_m=\frac{L^m e^{-\alpha_j L}-R^m e^{-\alpha_j R}}{\alpha_j}
 +\frac{m}{\alpha_j}M_{m-1}.\tag{2.3}
\]

All exponentials at **rational** arguments are enclosed with alternating Taylor polynomials after dyadic scaling and rigorously outward-quantized integer interval arithmetic (grid \(10^{-55}\)). \(\pi\) is bounded using Machin's alternating arctangent identity; \(\log\) uses the positive atanh series with a proved geometric remainder; \(\gamma_E\) uses the elementary bracketing

\[
H_N-\log N-\frac1{2N}<\gamma_E<
H_N-\log N-\frac1{2(N+1)},\quad N=1024.\tag{2.4}
\]

These enclosures are **mathematical rational bounds**, not mpmath interval claims. For the omitted real-Gamma modes, import and apply the proved accelerated CTW-09 estimate at \(a_J=2J+1/2\):

\[
\left|A(g_d)-\left(A_J(g_d)-\frac{g_d(0)}{2a_J}\right)\right|
\le\frac{M_0}{a_J^2}
 +(M_2+M_0/4)\left(\frac1{2a_J^2}+\frac2{a_J^3}\right).\tag{2.5}
\]

The bounds \(\|B_3\|_\infty=2/3\), \(\|B_3''\|_\infty=2\), positivity and mass-one of \(B_3\) imply for \(g_d=h^{-1}(B_3*B_3)((\cdot-d)/h)\) the valid global norm caps \(M_0=2/(3h)\), \(M_2=2/h^3\). Nothing depends on an unverified compact high-sector inverse. The prime term is enclosed separately by exact source authentication \(n=p^k\), rational log enclosures and rational square-root bounds from integer `isqrt`. All arithmetic is finite.

## PWS-03. Explicit strictly positive original signed Weil Gram (PROVED, conditional only on classical Weil identity)

Let \(M_{ij}:=W(f_i*\widetilde f_j)\). The even real source gives the exact Toeplitz form
\[
M=\begin{pmatrix}a&b\\b&a\end{pmatrix},
\quad a=W(g_0),\quad b=W(g_{1/10}).\tag{3.1}
\]

**Outward-rational result at J=64** (decimal representations merely show the certified rational interval endpoints):

| Entry / eigenvalue | Certified interval (rounded outward for display) |
|---|---|
| a | [0.1047590, 0.1208275] |
| b | [0.0075407, 0.0236091] |
| a+b | [0.1122997, 0.1444366] |
| a−b | [0.0811499, 0.1132868] |

The actual machine asserts the **exact rational comparisons** \(a\pm b>1/16\). Consequently, for every coefficient vector \(c\in\mathbb C^2\),

\[
\boxed{\quad W((c_0f_0+c_1f_1)*\widetilde{(c_0f_0+c_1f_1)})
  >\frac1{16}(|c_0|^2+|c_1|^2)\quad}\tag{3.2}
\]

for nonzero \(c\). This is **original source**, genuinely prime-active, completed gamma/contact/**both** poles, no nontrivial zeros, valid compact tests. It is a finite-dimensional theorem; **not the RH-equivalent all-test Weil positivity**. A separate 50-digit `mpmath` direct integral calculation falls within the rigorous intervals, but is not their justification.

## PWS-04. Same physical contact coordinates as the genuine Neumann metric (PROVED)

Let \(u_i=i f_i'\), a mean-zero source vector in \(H=L_0^2(-1/2,1/2)\). Suzuki's imported identity [S, Eq. (1.8), §8.2] gives
\[
\langle G_{1/2}u_i,u_j\rangle=M_{ij},\qquad
K_{1/2}=(-\Delta_N)^{-1},\qquad
\langle K_{1/2}u_i,u_j\rangle=\int f_i(x)f_j(x)\,dx.\tag{4.1}
\]

Because \(f_i\) vanish at both boundaries, \(D^{-1}(if_i')=f_i\), with \(D=i\partial\). The metric/contact matrix is exactly

\[
C=\begin{pmatrix}151/63&259723/129024\\259723/129024&151/63\end{pmatrix},\qquad
\operatorname{eig}(C)=\left\{\frac{63219}{14336},\frac{7075}{18432}\right\}.\tag{4.2}
\]

Source entry bounds and these **exact fractions** imply, as forms restricted to \(U=\operatorname{span}\{u_0,u_1\}\),

\[
\boxed{\quad G_{1/2}|_U\ \succ\ \frac1{50}K_{1/2}|_U.\quad}\tag{4.3}
\]

The exact checker obtains a relative lower ratio greater than `0.0254659`, so \(1/50\) is conservative. This is now a **positive slice of the original Suzuki operator in the correct K metric**, not a physically motivated positive probability Gram substituted for the signed Weil source.

## PWS-05. Exact Legendre P30 geometry: small does not mean absent (PROVED, exact rational)

One existing residual/Schur construction uses the **30-dimensional Legendre subspace** \(F_{30}=\operatorname{span}\{P_k(2x):1\le k\le30\}\), as distinct from our spline plane U. The derivatives \(f_i'\) are piecewise quadratic with rational breakpoints. The normalized Legendre projection can be integrated **exactly as fractions**:

\[
\|P_{30}u_i\|_2^2=\sum_{k=1}^{30}(2k+1)
\left|\int_{-1/2}^{1/2}f_i'(x)P_k(2x)\,dx\right|^2,\quad
\|u_i\|_2^2=\frac{250}{3}.\tag{5.1}
\]

Both instances obey the exact inequalities

\[
\boxed{\quad0<\|(I-P_{30})u_i\|_2^2<\frac1{60000}\|u_i\|_2^2.\quad}\tag{5.2}
\]

Approximate residual square-norms, for orientation only: `0.0013526152564` (\(t_0\)) and `0.0012941211623` (\(t_1\)), against full square-norm \(83.3333333\). Since the high leakage is **strictly nonzero**, the positive spline Gram is *not* a certified positive part of the exact **low Schur block** \(S_0=A-R_0\). One needs the genuine source high-response and cross-coupling certification (ORS-02/ORS-03), not projection-based wishful thinking.

## PWS-06. Two decisive source-normalization falsifiers (PROVED, exact rational)

1. **Contact spoof**: replace \(W\) by \(W_c=W+c\delta_0\). From (4.1), the metric change on U is exactly \(M_c=M+cC\), matching the existing whole-operator identity \(G_{a,c}=G_a+cK_a\). Setting the deliberately incorrect contact \(c=-1/8\) produces an eigenvalue with certified upper bound below `−0.4067`; the positive vector \((1,1)\) now has negative signed energy. This refutes the shortcut “off-origin prime and Gamma data alone determine the sign”, **not RH**.
2. **Fake composite at 6**: an early unauthenticated prototype prime-power recognizer mistakenly stopped after finding a first divisor, thereby accepting 6 as a power of 2. Its bogus negative numerical signature disappeared when the source defect was repaired. The integrated test rejects every extra `(6,6)` and does not credit it as a genuine von Mangoldt coefficient. For the narrow \(h=1/5\) spline, \(\log6>9/10\), so its **signed impulse is genuinely invisible to this finite support**, despite being source-invalid. For the wider \(h=1/2\) spline, \(\operatorname{supp}(f*\widetilde f)=[-2,2]\) and the exact signed fake-six change \(-\log6/\sqrt6\,[g(\log6)+g(-\log6)]\) is rigorously **strictly negative** by rational enclosures. Source provenance and observational detectability are separate gates.

Every certificate insists that the source tape contains the *full set* of authentic prime powers in the compact window, with correct prime labels, no omissions, no duplicates, and no forged composite. Wrong half density, Gamma scale/parity or poles are not silently tolerated as authentic source metadata.

## PWS-07. A complete rational finite-spline witness grammar (PROVED PAPER, classical ingredients)

Let \(\mathcal B_\mathbb Q\) be the set of **finite rational linear combinations of translates/dilates of centered cubic B-splines** with rational positive mesh and rational centers. These are \(C_c^2\). The family is countable, and is dense in \(C_c^1\) in the local fixed-support \(C^1\) norm:

- For smooth compact \(f\), use cardinal quasi-interpolation \(I_hf(x)=\sum_{k\in\mathbb Z}f(kh)B_3(x/h-k)\). The B-spline integer translates form a partition of unity. Compactness makes the sum finite. \(I_hf\to f\) uniformly as \(h\to0\), and \(\frac{d}{dx}I_h f\to f'\) follows by writing the derivative as a convex combination of first divided differences weighted by the positive quadratic \(B_2\); uniform continuity of \(f'\) proves convergence.
- Approximate the finitely many real coefficients \(f(kh)\) by rationals with error \(o(h)\); this preserves the uniform derivative limit. Supports grow by at most \(2h\), so a fixed slightly larger compact interval suffices.
- For \(f,v\) supported in \([-a,a]\), elementary convolution bounds give \(\|f*\widetilde f-v*\widetilde v\|_\infty\le 2a(\|f\|_\infty+\|v\|_\infty)\|f-v\|_\infty\) and the analogous first derivative bound with \(\|f'-v'\|_\infty\). CTW-09's \(C^1\) source-distribution continuity therefore preserves any **strict negative** Weil quadratic witness under sufficiently fine approximation.

Thus the classical Weil criterion yields

\[
\boxed{\quad\neg\mathrm{RH}\ \Longrightarrow\
\exists v\in\mathcal B_\mathbb Q:\ W(v*\widetilde v)<0.\quad}\tag{7.1}
\]

Conversely, a rigorously **negative** original-source certificate for one such \(v\) disproves RH. The strict sign can be witnessed by rational interval evaluation of a **finite** source tape and finite Gamma ladders with convergent error bounds, because the compactly supported spline autocorrelations are rational piecewise polynomials; the numerical/code prototype handles a bounded subfamily at \(a=1/2\). This gives a **complete, computably enumerable falsifier grammar**, not a uniform first-witness search horizon, an RH decision algorithm, or a new RH equivalence. All analytic ingredients and one-sided decidability are classical.

For complex candidates, because \(W\) is real and even, writing \(v=v_R+iv_I\) gives \(Q(v)=Q(v_R)+Q(v_I)\), so real rational spline coefficients suffice to find a strict negative direction if one exists.

## PWS-08. A positive Mellin source can hide entirely artificial off-critical zeros (PROVED countermodel)

For each integer \(m\ge1\), set \(N=6^{4m}\), \(A=6^{3m}\) and form the **positive but non-Euler** Dirichlet multiplier

\[
F_m(s)=1+A N^{-s}.\tag{8.1}
\]

On every half-plane \(\Re s\ge5/4\), \(|F_m(s)-1|\le6^{-2m}\), uniformly in all imaginary heights. For the normalized positive Bernoulli source at a base \(\sigma>1\), \(F_m(\sigma+it)/F_m(\sigma)\) is a characteristic function. Yet **by exact algebra**

\[
F_m\!\left(\frac34+\frac{(2k+1)\pi i}{4m\log6}\right)=0,
\qquad k\in\mathbb Z.\tag{8.2}
\]

Multiplying the genuine \(\zeta(s)\) by this factor creates new off-critical zeros of a **different** meromorphic function, without changing its positive-source convergence in the safe right half-plane by more than an arbitrarily small amount. It does **not** preserve the authentic Euler product or completed functional equation and hence is deliberately NOT an RH counterexample. This is a sharp falsifier of the unsupported inference “positive Mellin closeness on \(\Re s>1\) forces global zero or Weil-sign control.” The coefficient \(A\) is an integer (we chose fourth powers deliberately); no nontrivial zeta-zero coordinates were read.

## PWS-09. What transport requires next (PROVED conditional stability; Schur still OPEN)

Let \(K\) be a compact subset of the half-plane \(\Re s>1\) possessing a complex \(r\)-collar; \(F\) be nonvanishing and \(|F|\ge m_0>0\) on that collar. If a holomorphic source approximation \(F_N\) satisfies \(\sup|F_N-F|\le\epsilon<m_0\), then Cauchy's estimate and division give

\[
\left|\frac{F_N'}{F_N}-\frac{F'}{F}\right|
\le\frac{\epsilon}{m_0-\epsilon}
\left(\frac1r+\frac{\sup|F'|}{m_0}\right),\quad s\in K.\tag{9.1}
\]

This is a classical **conditional** error transport: no normalization matching, positivity, or finite precision can replace the nonvanishing lower bound. The off-critical mutant (8.2) shows why right-half-plane control does not transport through an unrestricted continuation region. Fortunately the authentic Weil distribution can be computed directly by (0.1) on compact tests without ever dividing near unknown zeros; that is the channel used in this branch.

**Schur-falsification outcome defined in advance:**
- `POSITIVE_FINITE`: strict outward rational sign on the source-authenticated spline plane, plus verified true prime tape and norm; observed here.
- `NEGATIVE_FINITE`: a rigorous original-source negative spline autocorrelation; would refute RH. **Not observed**.
- `AMBIGUOUS`: interval straddles zero, support/source mismatch, Gamma tail too large, or unproved high-response sign. Do not infer global positivity/negativity.

The next verdict-changing step is not “find another positive test.” **Use the stronger, already proved WB4-13 four-mode high coercivity** \(D_4=Q_4G_{1/2}Q_4\succeq Q_4KQ_4/50\), and the already certified genuine four-low block \(A_4=P_4GP_4\succ0\). Compute the original \(B_4=Q_4GP_4\), an actual source-compatible high response \(Y_4\), and a rigorously bounded derivative residual \(T_{r_J}\), including **all** authentic prime, real-Gamma, contact and pole terms. Then the established source-relative shorting theorem ORS-02 gives
\[
A_4-L_Y-50T_r\preceq S_4\preceq A_4-L_Y,
\]
with the appropriate inequalities as in `research/2026-10-15/ONE_OBJECT_RESIDUAL_SCHUR.md`. The tiny but nonzero spline-to-P30 leakage is a useful *probe*, not a positivity theorem for the whole low sector. **A sharper, previously established four-moment result (WB4-12/13) reduces the first-prime obstruction to four low Legendre modes; the new spline vectors actually have much larger leakage into that rank-four high complement (PWS-11).** The high coercivity \(\kappa\) is inherited conditionally from the earlier exact source proof, not reproduced here. No source-derived \(S_0\succeq0\), all-radius positivity, source-positive Hilbert factorization, or RH proof is delivered.

## PWS-10. The original low Legendre A11/A22 source is strictly positive (PROVED LOCAL, not the Schur sign)

The spline experiment PWS-03 belongs to a plane *near* the low 30-mode subspace. To obtain two **actual original low-sector entries** with no projection substitution, choose unnormalized meanzero Legendre generators

\[
u_1(x)=P_1(2x)=2x,\qquad u_2(x)=P_2(2x)=6x^2-\tfrac12,\quad x\in[-\tfrac12,\tfrac12].
\]

Their authentic inverse-derivative Dirichlet primitives are

\[
v_1(x)=x^2-\tfrac14,\qquad v_2(x)=2x^3-\tfrac{x}{2}\quad(|x|\le1/2),
\]

extended by zero. These lie in \(H_0^1\), and the Suzuki integral-operator pairing is the extension of the signed Weil form to the stated energy domain. Their even autocorrelations \(g_k=v_k*\widetilde v_k\) are compact *rational polynomials* for \(0\le r\le1\):

\[
\boxed{g_1(r)=\frac1{30}-\frac{r^2}{6}+\frac{r^3}{6}-\frac{r^5}{30}},
\quad
\boxed{g_2(r)=\frac1{210}-\frac{r^2}{10}+\frac{r^3}{6}-\frac{r^5}{10}+\frac{r^7}{35}}.\tag{10.1}
\]

Both vanish outside \([-1,1]\) and have a genuine active \(p=2\) impulse. The exact forms of \(g_k\) follow by integrating \(v_k(x)v_k(x-r)\) over \([r-1/2,1/2]\), not by fitting a Fourier spectrum. The complete signed Weil formula (0.1), the polynomial exponential integral recurrence (2.3), and the **same** original Gamma/contact/pole source produce rigorous rational enclosures at \(J=64\):

| True low matrix entry | Outward-rational interval (decimal shown outward) | Result |
|---|---|---|
| \(A_{11}=\langle G_{1/2}u_1,u_1\rangle\) | [0.00010035, 0.00012575] | \(A_{11}>1/10000\) |
| \(A_{22}=\langle G_{1/2}u_2,u_2\rangle\) | [0.00022875, 0.00024190] | \(A_{22}>1/5000\) |
| \(A_{12}=\langle G_{1/2}u_1,u_2\rangle\) | exactly 0 | even/odd source parity |

The Gamma tail is enclosed by (2.5) with \(M_0=\|v_k\|_2^2=1/30,1/210\) and \(M_2=\|v_k'\|_2^2=1/3,1/5\) using Cauchy–Schwarz on the correlation and its second derivative. Thus the **first two original low A principal modes are strictly positive**. Their baseline Neumann metric entries \(1/30,1/210\) independently match existing SUCC source/Neumann code.

**Existing stronger theorem and provenance:** `docs/CLAIM_SUPPLEMENT_TATE_WEIGHTED_BESSEL_FOUR.md` (WB4-LOW) and `research/2026-10-15/TATE_WEIGHTED_BESSEL_FOUR_SCHUR.md` already prove strict positivity of the entire *four-dimensional* original low Galerkin block \(A_4\) using authenticated J64 Gamma-source intervals and parity blocks. The present P1/P2 direct polynomial-autocorrelation route is an **independent implementation/holdout of two entries**, NOT a novel first proof that low \(A\) is positive, and it never computes the original zero-shift response. The more appropriate frontier is \(S_4=A_4-R_4\), not requiring all 30 low modes. The 30-mode construction remains a useful complementary representation.

**The decisive missing distinction:** the RH-hard source Schur matrix is \(S_4=A_4-R_4\), where \(R_4\ge0\) is the original four-low/high zero-shift short. Establishing \(A_{11},A_{22}>0\) (or the entire positive \(A_4\)) does not bound \(R_4\). In fact the first entry is only around \(1.22\times10^{-4}\); even a tiny legitimate high-sector response could determine its eventual Schur sign. Two exact toy responses in the first diagonal coordinate, \(R_4=0\) and \(R_4=1/5000\), are both nonnegative and give opposite signs for the first scalar \(A_{11}-R_4\). They are **not** claims about the genuine Riemann source. The prior WB4 result establishes \(A_4\succ0\) but not \(S_4\succeq0\); no all-test first-window or global positivity has been proved.

This directly narrows the next computational theorem: obtain source-certified \(R_4\) upper bounds **at precision substantially better than \(10^{-4}\)** for the first original Legendre mode using the established Neumann/Douglas variational range theorem. The current coarse global high response bound is not enough. The original \(A_{11},A_{22}\) computations are exact independent cross-checks of WB4-LOW and useful input data, rather than the previous spline proxies.

## PWS-11. The rank-four frontier is not an accidental rank-thirty projection (PROVED, exact rational)

The stronger **previously proved** first-prime result WB4-12/13 gives a positive infinite-dimensional high sector after removing only the four Legendre modes \(P_1,\ldots,P_4\). Accordingly, recompute the **same exact** spline-derivative projections with rank \(r=4\), rather than \(r=30\). The source vectors have not changed, and exact rational integration gives

\[
\begin{aligned}
\frac{\|(I-P_4)u_0\|_2^2}{\|u_0\|_2^2}&=\frac{2809}{6250}=0.44944,\\
\frac{\|(I-P_4)u_1\|_2^2}{\|u_1\|_2^2}&=\frac{869}{3125}=0.27808.
\end{aligned}\tag{11.1}
\]

In comparison, rank-thirty residual ratios were about \(1.6\times10^{-5}\). **A spline plane close to the 30-low space is not close to the four-low space.** Its genuine positive sign cannot be smuggled into the sharper \(P_4\) Schur problem using a projection-smallness argument.

This is a source-geometry falsifier of one tempting shortcut, while preserving the sharper next step: apply source-relative ORS-02/03 shorting to the already proven WB4 rank-four original low block \(A_4\), and seek \(A_4-L_Y-50T_r\succeq0\) or a rigorous original-source negative trial direction. WB4 already proves \(A_4\succ0\); it does **not** bound the actual high response tightly enough to decide \(S_4\). No finite positive subspace determines that response.

## How to reproduce and audit

Code: `observational_succ/prime_active_weil_splines.py` (pure Python standard library exact rational interval engine). Tests: `tests/test_prime_active_weil_splines.py` (hostile, exact, independent mpmath numerical holdouts, including true P1/P2 low A). Receipt: `scripts/prime_active_weil_spline_probe.py` and `research/2026-10-16/PRIME_ACTIVE_WEIL_SPLINE_RECEIPT.json`.

```bash
python -m unittest discover -s tests -p 'test_prime_active_weil_splines.py' -v
python scripts/prime_active_weil_spline_probe.py --verify
```

Local inherited TMF/FGF focused tests also run independently; the full GitHub CI takes 10+ minutes and is NOT claimed as passed without observing completion.

**Primary classical source:** Masatoshi Suzuki, *Weil's quadratic form via the screw function* (arXiv:2606.09096v3, Sept 23 2026), §8 (https://arxiv.org/html/2606.09096v3). The local Weil distribution is derived independently in existing SUCC `TATE_TO_WEIL_DISTRIBUTION.md` using Tate/Weil contour methods. Finite inequality certificates are new-to-project calculations, not claimed original RH results.
