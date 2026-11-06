# Critical source truncation: a second-order carry field, exact gauge and selected-orbit obstruction

**Research-only; additive descendant of PR #520 at dad940dc69ae02f71119e8fbb908cca98e6e0846.** Original signed four-pole BBP source and literal U0=0 are immutable. Claims here are paper derivations with exact-rational finite checks, not a π-normality theorem, external priority claim or Lean certificate.

## CT-01: a genuine, UNIFORM critical-resolution source law

Use the authenticated rational forcing
\[
r(n)=\frac{120n^2-89n+16}{(2n-1)(4n-1)(8n-7)(8n-3)}.
\]
For every integer n≥2,
\[
0<r(n)-\frac{15}{64n^2}<\frac1{n^3}.
\tag{CT1}
\]
**Proof:** the difference is \(P(n)/(64n^2D(n))\), with \(P=9664n^3-9656n^2+3090n-315\), \(0<P<9664n^3\) for n≥2. The denominator satisfies \(D(n)≥(2457/16)n^4\). Thus the difference is at most \(2416/(2457n^3)<1/n^3\).

Let \(B=16^m\), \(R_m(n)=\sum_{j=1}^m 16^{m-j}r(n+j)\). For all n≥2 and ALL m≥1,
\[
\boxed{
\left|R_m(n)-\frac{B-1}{64n^2}\right|<
\frac{B}{10n^3}.}\tag{CT2}
\]
This follows because \(|r(n+j)-\frac{15}{64n^2}|≤(1+\frac{15}{32}j)/n^3\), and
\(\sum_{j≥1}16^{-j}=1/15\), \(\sum_{j≥1}j16^{-j}=16/225\), producing \(1/15+1/30=1/10\).

**Consequences:** if \(B/n^2\to\lambda\in(0,\infty)\), then \(R_m(n)\to\lambda/64\). For n∈[A,2A) and a subsequence with B/A²→γ<64, this source window tends uniformly to γ/[64(n/A)²] (error O(1/A)). Fixed m misses it because R→0; the correct primitive truncation depth is \(m\approx2\log_{16}A\). All claims about growing integer m must pay the logarithmic rounding and can be stated along subsequences of B/A².

## CT-02: the carry is a moving boundary, not a smooth scalar derivative

For the authentic unwrapped U_n, set \(x_n=\{U_n\}\),
\[
K_m(n)=\lfloor Bx_n+R_m(n)\rfloor
=\lfloor U_{n+m}\rfloor-B\lfloor U_n\rfloor,
\quad W_m(n)=\lfloor Bx_n\rfloor.
\]
If \(0<R_m(n)<1\), then \(b_m=K_m-W_m\in\{0,1\}\) and
\[
\boxed{b_m(n)=\mathbf1_{\{\{Bx_n\}\ge1-R_m(n)\}}.}\tag{CT3}
\]
For R∈(0,1) define \(f_{R,B}(x)=\mathbf1_{\{\{Bx\}\in[1-R,1)\}}\). Its Fourier coefficients (convention \(\hat f(h)=\int f(x)e(-hx)dx\)) are
\[
\hat f(0)=R,\quad
\hat f(\ell B)=\frac{e(\ell R)-1}{2\pi i\ell}
\ (\ell\ne0),\qquad \hat f(h)=0\ (B\nmid h).
\tag{CT4}
\]
As a distribution on T,
\[
D_x f_{R,B}
=\sum_{k=0}^{B-1}
[\delta_{(k+1-R)/B}-\delta_{(k+1)/B}].\tag{CT5}
\]
The second and third derivatives are Dirac derivatives, NOT ordinary smooth Jacobians. After a declared Poisson smoothing \(0<\eta<1\), the qth derivative for q=1,2,3 multiplies the \(\ell B\) Fourier mode by \((2\pi i\ell B)^q\eta^{|\ell|}\). These jets amplify as B^q and do not themselves bound the selected high-frequency character.

The selected correction discrepancy
\[
J_{A,m}(0)=\frac1A\sum_{A\le n<2A}(b_m(n)-R_m(n))
\]
is a concrete source-dependent *boundary-correlation* probe. After smoothing, it is a weighted sum of **unproved** original signed characters \(e(\ell Bx_n)\); claiming its limit is zero would assume new arithmetic information.

## CT-03: exact same-source coherent control remains correction-free at the critical depth

With completed β=0 (seed s*=−π/16), the unchanged ORIGINAL forcing gives \(U_n=-T_n\), \(0<T_n≤1/[(8n+1)(8n+2)]\), and
\(R_m(n)=BT_n-T_{n+m}\). If \(BT_n<1\), then \(x_n=1-T_n\) and
\[
W_m=B-1,\quad K_m=\lfloor B-T_{n+m}\rfloor=B-1,
\quad \boxed{b_m(n)=0.}\tag{CT6}
\]
This holds throughout [A,2A) if \(B<(8A+1)(8A+2)\), even when \(B/A^2\) is a nonvanishing constant and R_m is order one. Thus the source-only forcing threshold cannot prove a correction-density lower bound, and a correction-density lower bound alone would not establish normality.

## CT-04: exact comoving source gauge at critical depth

The positive future Green tail obeys \(16T_n-T_{n+1}=r(n+1)\). Therefore
\[
\boxed{U_{n+1}+T_{n+1}=16(U_n+T_n),\qquad
U_n(s)+T_n=16^n(s+\pi/16).}\tag{CT7}
\]
Multiplying by B and reducing mod1 gives \(z_n=\{B(U_n+T_n)\}\) with **exactly** \(z_{n+1}=\{16z_n\}\). At the critical depth \(BT_n\sim B/(64n²)=O(1)\), the needed gauge translation is order one, even though its time variation is O(1/n). This is the same already-known Bailey–Crandall/Lagarias perturbed-orbit equivalence, now expressed in source-critical coordinates. In the enlarged space of future-tail sequences the forcing is an exact time coboundary, whereas SUCC's smaller **rational-time function** category retains a genuine nonzero weighted-residue obstruction. Do NOT conflate the two categories.

The comoving gauge identifies the completed orbit parameter \(s+\pi/16\); it does not establish that the literal zero-seeded parameter is normal.

## CT-05: new-to-SUCC SECOND-ORDER randomized-seed covariance

Let S be Haar-uniform on the initial seed circle, and fix an observer order m with 0<R_m(n)<1 for times being observed. Write \(b_n(S)=f_{R_m(n),B}(\{U_n(S)\})\). Since \(U_n(S)=U_n(0)+16^nS\), every one-time marginal is exactly \(E_S b_n=R_m(n)\), regardless of forcing. For n<k, d=k−n, and \(S_d(n)=\sum_{j=1}^d16^{d-j}r(n+j)\), Fourier resonance gives the **exact signed covariance**
\[
\boxed{
\operatorname{Cov}_S(b_n,b_k)
=\sum_{\ell\in\mathbb Z\setminus\{0\}}
c_{16^d\ell}(R_m(n))
\overline{c_\ell(R_m(k))}
\,e(-\ell B S_d(n)),}\tag{CT8}
\]
where \(c_\ell(R)=(e(\ell R)-1)/(2\pi i\ell)\). The series is absolutely convergent (coefficients O(\ell^-2)). All homogeneous seed terms cancel on resonance. Thus this is a TRUE source-labelled **second-order** observer statistic, not an independence assumption.

Since \(|c_\ell(R)|≤1/(\pi|\ell|)\) and \(\sum_{\ell\ne0}\ell^{-2}=\pi^2/3\),
\[
\boxed{|\operatorname{Cov}_S(b_n,b_k)|≤\frac1{3\cdot16^{|n-k|}}.}\tag{CT9}
\]
Hence for ANY deterministic source, ANY sequence m=m(A) obeying the binary-window condition on the epoch, and ANY A≥1,
\[
\boxed{
\operatorname{Var}_S\left[
\frac1A\sum_{n=A}^{2A-1}(b_n(S)-R_m(n))
\right]
≤\frac{53}{180A}.}\tag{CT10}
\]
Proof: diagonal Bernoulli variances ≤1/4, offdiagonal pair sum ≤(2A/3)\sum_{d≥1}16^{-d}=(2A/45). This bound is **even valid at critical growing m**. Along dyadic A, first Borel–Cantelli gives mean-centered correction decay for Haar-almost every initial seed (when all corresponding binary windows are valid). It does NOT hold pointwise at the selected exact seed without an independent source arithmetic estimate. The coherent counterseed from CT-03 violates mean-centering while the ensemble still concentrates.

## CT-06: exact THIRD-ORDER randomized-seed source response

For n0<n1<n2, d_j=n_j−n0 (d0=0), write \(R_j=R_m(n_j)\), \(\beta_j=B S_{d_j}(n_0)\), and let \(y=\{BU_{n_0}(S)\}\), uniform in [0,1). Then the entire joint source-conditioned distribution has the exact representation
\[
(b_{n_0}(S),b_{n_1}(S),b_{n_2}(S))
\overset{\rm law}{=}
\left(f_{R_j,1}(\{16^{d_j}y+\beta_j\})\right)_{j=0,1,2}.
\tag{CT11}
\]
Consequently the centered **third moment** is an integral of a finite product of piecewise-constant functions, with R_j and β_j genuine rational source values. Every discontinuity has a rational endpoint; the integral is an **EXACT RATIONAL NUMBER** computable by a finite endpoint partition, without any π digit inputs or unproved approximation.

Equivalently, use Fourier coefficients \(c_{\ell_j}(R_j)\) and the exact character-resonance lattice
\(\ell_0+16^{d_1}\ell_1+16^{d_2}\ell_2=0\). A Poisson factor \(\eta^{\sum|\ell_j|}\) makes termwise calculations absolutely convergent, and letting η→1 in bounded L¹ recovers the exact step-function integral. Surviving phases reduce to the source fingerprint \(e(B[\ell_1S_{d_1}+\ell_2 S_{d_2}])\). This is a genuinely third-order *source-ensemble* correlation, not the time average along the selected zero seed.

Fresh exact Fraction holdouts selected BEFORE calculation:
| n | m | Cov lag1 | Cov lag2 | Third centered moment lags 0,1,2 |
|---:|---:|---:|---:|---:|
| 13 | 2 | +0.000711537214 | −0.0000433533583 | −0.0000330381468 |
| 29 | 3 | +0.003518958778 | +0.00000821995515 | +0.000170847554 |
| 61 | 3 | +0.000744087645 | +0.0000372456290 | +0.0000291303759 |

The signs are EXACT signs of rational moments, not rounded-float guesses. Their mixed signs refute any unproved universal positivity of a third-order "gluing pressure". They are finite randomized-seed observations, not selected-source normality evidence.

**True barrier:** this exact higher-order joint law is an ensemble/source-covariant diagram. The actual seed s=0 chooses ONE y at every time. No source-selected time occupancy or signed Weyl estimate has been proved from these ensemble covariance/cumulant identities.
