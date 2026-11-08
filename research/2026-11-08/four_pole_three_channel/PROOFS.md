# Four poles → three positive channels → a 3×3 Gram, and the sharp 1/9 Poisson boundary

**2026-11-08 research branch; original BBP poles, literal U0=0 and archives unchanged.** All new claims are elementary algebra/analysis within declared models; no independent scholarly review, novelty priority, or π-normality proof. The current signed covariance gate in #544 is OPEN.

## FP3-01: exact three-channel decomposition of the authentic four-pole source — PROVED

For a>0 let
\[
R(a)=4/a-2/(a+3)-1/(a+4)-1/(a+5),\quad
Q(x)=4-2e^{-3x}-e^{-4x}-e^{-5x}.
\]
Then **exactly**
\[
Q(x)=2(1-e^{-3x})+(1-e^{-4x})+(1-e^{-5x}),\qquad
R(a)=2\frac3{a(a+3)}+\frac4{a(a+4)}+\frac5{a(a+5)}.
\]
The 4-pole balanced coefficient vector has 3-dimensional linear freedom if coefficients are allowed to vary subject to sum zero. **The authentic coefficients are fixed**; this is not three freely variable BBP phase channels. The positive source has three explicitly marked components (d,w)=(3,2),(4,1),(5,1). Their mixture masses are \(\omega_d(a)=w_dd/[a(a+d)R(a)]\), positive and summing to one. As a→∞, \(\omega(a)\to(6,4,5)/15\). The first two source endpoint jets are \(Q'(0)=15\) and \(Q''(0)=-59\), with \(59=2\cdot3^2+4^2+5^2\). The **specific** 59 is a genuine four-pole fingerprint, unlike the universal 1/9.

## FP3-02: exact rational 3×3 source Gram and full rank — PROVED

On a common \(L^2((0,\infty),dx)\) carrier set \(v_d^{(a)}(x)=\sqrt{w_d}e^{-ax/2}(1-e^{-dx})\). Their 3×3 Gram is
\[
\mathcal G_{ij}(a)=\sqrt{w_iw_j}\left[\frac1a-\frac1{a+d_i}-\frac1{a+d_j}+\frac1{a+d_i+d_j}\right].
\]
The bracketed matrix \(G(a)\) is rational for every rational a>0. Both G and \(\mathcal G\) are strictly positive definite for all a>0: if \(\sum c_i(1-e^{-d_ix})=0\) on a positive-measure interval, analyticity and distinct exponential rates imply each \(c_i=0\). Hence all principal minors and the determinant are positive. **Nine entries exist, but symmetry reduces them to six independent real entries; no theorem identifies the number nine with the Poisson 1/9.**

**Asymptotic determinant:** expand \(1-e^{-d_ix}=d_ix-\frac12d_i^2x^2+\frac16d_i^3x^3+O(x^4)\). The coefficient matrix for monomials \(x,x^2,x^3\) has determinant \(-10\) for \(d=3,4,5\). The moment matrix \((\int_0^\infty e^{-ax}x^{i+j}dx)_{i,j=1}^3\) has determinant \(576/a^{15}\). By Gram–Cauchy–Binet / wedge expansion, the next independent monomial wedges have strictly higher inverse powers, so
\[
\boxed{\det G(a)=57600\,a^{-15}+O(a^{-16}),\quad
\det\mathcal G(a)=115200\,a^{-15}+O(a^{-16}).}
\]
The factor 2 in the second identity is the product of the three component weights. This is an exact source-specific rank hierarchy, not a cancellation estimate. The leading rank-one direction is proportional to \((\sqrt2\cdot3,4,5)\); the two transverse singular directions are suppressed at higher inverse-a orders. All three are present at every finite a.

**Caution:** The categorical covariance of the three exclusive channel labels is \(\mathrm{diag}(\omega)-\omega\omega^T\), which has rank exactly two, because the weights sum to one. This is a *different matrix* from the full-rank source Gram. “Three channels” does not mean three statistically independent fluctuations.

## FP3-03: 5 and 9 are exact disk geometry, but not four-pole multiplicity — PROVED

The native rank-two Pascal–Gamma observer in \`docs/OPERATIONAL_TRIANGLE.md\` has \(P(z)=(2-z)^{-2}\), from the original source endpoint zero \(Q(x)\sim15x\) and the declared native observation depth. For \(z=e^{i\theta}\):
\[
|P(e^{i\theta})|=\frac1{5-4\cos\theta}=\frac13\frac{1-(1/2)^2}{1-2(1/2)\cos\theta+(1/2)^2}.
\]
This is one-third the classical Poisson kernel at radius 1/2. Its sharp minimum is 1/9 at the antipode \(z=-1\), maximum 1 at \(z=1\). The fixed-point equation \(q=P(q)\) has roots \(q=1,\varphi^{-2},\varphi^2\); the attracting interior fixed point is \(\varphi^{-2}\), with \(2-q=\varphi\). The value 5 is the constant term in \(|2-z|^2\), **not a possible limit of \(z=e^{i\theta}\) to 5**.

**Decisive two-pole control:** \(Q_*(x)=1-e^{-x}\) has only two poles in its Laplace transform, but also a simple zero at 0. Under the same Gamma(2) native sensor scaling its limiting PGF is again \(P(z)=(2-z)^{-2}\). Thus 1/9, 5 and the interior golden fixed point cannot *by themselves* identify four-pole source structure. This kills the proposed literal implication “four poles → three channels → 3²=9 explains the Poisson bound.” It does NOT kill the source-specific full Gram.

## FP3-04: source-positive matrices alone are seed-blind — PROVED NEGATIVE

All \(R,Q,\omega,G,\mathcal G\) above depend on the four poles and the positive parameter a, but **not** the BBP initial seed s. With the same forcing, the coherent counterseed \(s_*=-\pi/16\) satisfies \(U_n(s_*)=-T_n\to0\), so its Weyl mean tends to one; the true zero seed has unknown Weyl limit. Hence no bound that uses only \(\mathcal G\), \(\omega\), or \(|P|\) can prove selected π normality. A genuine arithmetic observable must retain \(e(hU_n(s))\) or the equivalent original zero-seed chronology.

The exact signed covariance decomposition from #544 remains
\[
W_A(h)=\mathrm{Cov}_A(\chi,\beta)+\bar\chi_A\bar\beta_A,\qquad
\chi_n=e(h[U_n]_p),\quad\beta_n=e(h(U_n-[U_n]_p)).
\]
Our positive Gram does not bound the signed covariance. A potential next *new* instrument is the **marked, phase-bearing cross-time matrix**
\[
\mathcal K_{ij}^{(A,h)}=
\frac1A\sum_{n=A}^{2A-1}e(hU_n(0))
\int_0^\infty v_{d_i}^{(a_n)}(x)v_{d_j}^{(a_n)}(x)\,dx,
\quad a_n=8n-7.
\]
It is a well-defined exact-source signed complex matrix, not necessarily PSD. Its contraction with any bounded source-derived matrix functional must be compared against \(W_A(h)\) with an explicit uniform reconstruction error. The naive contraction can suppress coherent counterseeds as the unnormalized v norms shrink like \(a_n^{-3/2}\). **Normalize and calibrate against coherent controls before any normality inference.**

## FP3-05: falsifiable next theorem

Build a normalized, *historically labelled* three-channel Hilbert observer that (i) retains literal \(U_0=0\), the original four signed poles and carries, (ii) reconstructs the #544 prime/complement covariance up to o(1), (iii) exposes an **independently proved** all-A source-specific signed bound rather than merely restating Weyl, and (iv) fails on coherent same-forcing wrong seed, 2-pole matched-Gamma source, and 59-jet mutants. Check whether a four-pole-specific transverse channel can interact with chronological prime births; mere Gram positivity, finite rank and golden Poisson kernel cannot. **π base-16 normality OPEN.**
