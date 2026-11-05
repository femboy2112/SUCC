# The BBP virtual gauge is an exact nonautonomous conjugacy with a Fourier resolution threshold

**2026-11-04, research draft.** This is an analytical extension of [RETURN_LAW.md](RETURN_LAW.md) on the additive child [#504](https://github.com/femboy2112/SUCC/pull/504). Discovery arose interactively, before this commit; no pretense of blind preregistration or worldwide priority. Source \`P\`, initial \`U_0=0\`, #499 angular/radial split, and all historic contracts stay unchanged.

## VG-06: exact source-labelled gauge conjugacy (paper algebra)

Let \(r_o=r_a+r_r\) be the authentic original, angular, and radial source injections, and set \(Y_0=Z_0=U_0=0\), \(Y_n=16Y_{n-1}+r_a(n)\), \(Z_n=16Z_{n-1}+r_r(n)\), \(U_n=Y_n+Z_n\). For any time \(n\ge1\), on the line or circle \(\mathbb R/\mathbb Z\), define
\[
T^a_n(x)=16x+r_a(n),\qquad T^o_n(x)=16x+r_o(n),\qquad
{\cal G}_n(x)=x+Z_n.
\]
The diagram COMMUTES **exactly at every time**
\[
\boxed{{\cal G}_n\circ T^a_n=T^o_n\circ{\cal G}_{n-1}.}
\]
Proof: the left side is \(16x+r_a(n)+Z_n\), the right side \(16x+16Z_{n-1}+r_a(n)+r_r(n)\), equal by the actual source recurrence. \({\cal G}_0=\mathrm{id}\), and \(\sup_x\|{\cal G}_n(x)-x\|_{\mathbb R/\mathbb Z}\to0\) by inherited/source-derived \(Z_n=1/(32n)+O(n^{-2})\). This is a conjugacy between **nonautonomous source sequences** using invertible translations, NOT a conjugacy of a single autonomous expanding map and not a Haar mixing assertion. For the affine family, \({\cal G}_n^{(\lambda)}(x)=x+\lambda Z_n\) gives the identical commutative diagram between the Gaussian angular source and \(w_\lambda=w_a+\lambda w_r\).

For \(e(x)=\exp(2\pi ix)\) and integer harmonic \(h\),
\[
\boxed{e(hU_n)=e(hY_n)e(hZ_n).}
\]
At the SOURCE-INJECTION level the gauge is a multiplicative radix-16 coboundary:
\[
\boxed{e(h r_r(n))=\frac{e(hZ_n)}{e(hZ_{n-1})^{16}}.}
\]
The scalar exact period-zero theorem does not force the original mixed time-average of these products to cancel.

## VG-07: the Fourier identity–crossover–oscillation regimes (paper proof)

The inherited radial tail expansion (source only; #504 VG-05) is
\[
z(x)=\frac1{32x}-\frac5{256x^2}+O(x^{-3}),\quad
z'(x)=-\frac1{32x^2}+O(x^{-3}),\quad
z''(x)=\frac1{16x^3}+O(x^{-4}),
\]
with differentiated errors justified by the absolutely convergent sum of rational-in-\(x\) source injections. \(Z_n=z(n)\).

For integer epochs \(A\to\infty\) and positive INTEGER observation frequencies \(H_A\), let
\[
R_A(H_A)=\frac1A\sum_{n=A}^{2A-1} e(H_A Z_n).
\]

**Regime I, identity: \(H_A=o(A)\).** The uniform bound \(Z_n=O(A^{-1})\) on the epoch implies
\[
\boxed{R_A(H_A)=1+O(H_A/A)\to1.}
\]
For the **coupled** original vs angular Weyl means, the same bound gives
\[
\left|A^{-1}\sum e(H_AU_n)-A^{-1}\sum e(H_AY_n)\right|=O(H_A/A).
\]
This is an **observer-resolution statement**, not the unknown base-16 normality limit.

**Regime II, crossover: \(H_A/A\to\tau\in(0,\infty)\).** The expansion gives \(H_AZ_{\lfloor Ax\rfloor}=\tau/(32x)+o(1)\) uniformly for \(x\in[1,2]\), hence a Riemann sum:
\[
\boxed{R_A(H_A)\to \int_1^2\exp\!\left(\frac{2\pi i\tau}{32x}\right)\,dx.}
\]
This is nontrivial for generic \(\tau\) and is NOT an assumed phase distribution of π; it is a deterministic radial source-only profile.

**Regime III, radial cancellation: \(A\ll H_A\le A^2\).** On \([A,2A]\), for all sufficiently large A the differentiable real phase \(f(x)=H_A z(x)\) has monotone \(f'\) (because \(z''>0\)), and
\[
0<cH_A/A^2\le |f'(x)|\le CH_A/A^2<1/2.
\]
The classical Kusmin–Landau first derivative exponential-sum estimate (monotone derivative and separation from integers) implies
\[
\boxed{\left|\sum_{n=A}^{2A-1}e(H_A Z_n)\right|\ll A^2/H_A,\qquad
|R_A(H_A)|\ll A/H_A\to0.}
\]
There is no contradiction with Regime II, where \(H_A\asymp A\) and only an \(O(1)\) normalized bound is obtained. At the superquadratic \(\#501\) scale \(H_A\asymp A^2\log A\), VG-05's *separate* classical second-derivative estimate gives \(|R_A(H_A)|\ll\sqrt{\log A/A}\to0\) despite \(f'\) passing through integer resonances.

**Boundary of these theorems:** none of the source-only radial estimates bounds \(A^{-1}\sum e(H_A Y_n)e(H_A Z_n)\) for \(H_A\gtrsim A\). Indeed the original accelerated source satisfies \(r_a(n)=+15/(32n)+O(n^{-2})\), \(r_r(n)=-15/(32n)+O(n^{-2})\), so the two sources are strongly anti-aligned in their leading injections, not statistically independent.

## A source-coupled verdict-changing probe

For integer frequency \(H\) from the authentic \(\#501\) Weyl schedule, define
\[
C_{A,H}^{(k)}=A^{-1}\sum_{n=A}^{2A-1} e(HY_n)e(HZ_{n+k})
\]
for fixed labelled lags \(k\) with \(n+k\ge1\). Compare \(k=0\) (authentic original source) to \(k=\pm1,\pm2\) and a fully source-authentic wrong-seed control, while keeping exact integer/rational carries. Predict what bound genuinely discriminates the aligned original from shifts AND the radial-only nonmixing control. Numerical differences are **hypothesis-generating diagnostics**, not an all-time theorem. A proof of \(C_{A,H}^{(0)}=o(1/\log A)\) at \(\#501\)'s specified high depth would constitute an actual sufficient source-selected signed estimate. But it remains **UNVERIFIED**.

The mathematical “virtual” terminology is an analogy for transient radial signed/coboundary structure; no physical energy borrowing, quantum vacuum dynamics, or uncertainty-principle implication is asserted. Existing normality conjecture, selected signed original Weyl gate, and RH stay OPEN.
