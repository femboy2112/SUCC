# Tate source objects to the complete signed Weil distribution

**Date:** 2026-10-15. **Status:** CLASSICAL IDENTIFICATION, reconstructed with explicit SUCC source interfaces; PROVED PAPER bounds and restricted positivity obstruction. **RH / GRH proved:** NO.

This note separates three operations: constructing a normalized completed arithmetic function from a Tate source, taking its logarithmic derivative, and pairing the resulting signed distribution with arbitrary compact smooth log tests. The second operation is nonlinear in the source. None is a claim that an arbitrary positive Hilbert norm equals the Weil form.

## 1. Scope, provenance, and conventions

The arithmetic objects considered here are exactly:

| Source | Character | Conductor q | Parity ε | Pole flag δ |
| --- | --- | ---: | ---: | ---: |
| Riemann zeta | χ(n)=1 | 1 | 0 | 1 |
| Dirichlet beta | χ₄(n)=0 for even n, 1 for n≡1 mod 4, −1 for n≡3 mod 4 | 4 | 1 | 0 |

Let

\[
\mathcal L_\chi(s)
 =\left(\frac q\pi\right)^{(s+\varepsilon)/2}
   \Gamma\!\left(\frac{s+\varepsilon}{2}\right)L(s,\chi).
\tag{1.1}
\]

The zeta version has simple poles at 0 and 1. The χ₄ version is entire. Both satisfy \(\mathcal L_\chi(s)=\mathcal L_\chi(1-s)\); χ₄ has root number 1 because its Gauss sum is \(2i\) and \(i^{-1}(2i)/\sqrt4=1\). These are conclusions of the upstream genuine theta/Tate source reconstruction, not assumptions about zeros. Any use of (1.1) must retain that upstream source receipt.

The additive Fourier convention on the real line is

\[
\widehat f(y)=\int_{\mathbb R}f(x)e^{2\pi ixy}\,dx,
\]

paired with the negative finite-place character. For log tests it is convenient to use the angular-frequency transform

\[
H_g(s)=\int_{\mathbb R}g(u)e^{(s-1/2)u}\,du,
\qquad g\in\mathcal D:=C_c^\infty(\mathbb R;\mathbb C).
\tag{1.2}
\]

Thus \(H_g(1/2+it)=\int g(u)e^{itu}du\), and inversion has factor \(1/(2\pi)\). The variable t in this convention is not the real-place Fourier variable y above.

The manifest `provenance/IMPORT_MANIFEST.json` identifies the frozen foundational import as `femboy2112/FuckingRH@ba075348b7bcc66d938b3e0ca96c26e95bba340a`. This note changes no imported or archival file. Existing comparison targets are `completed_weil_transport.py`, `certified_contour_weil.py`, `signed_weil_h1_tail.py`, and `tate_signed_weil_bridge.py` in `observational_succ/`. In particular, the contour and signed-tail modules already distinguish authentic-source certificates from synthetic models and preserve the unresolved sign gate.

Classical provenance is Tate's global functional equation and Weil's explicit formula. Burnol [B, §§B–C] gives the local Tate-to-explicit-formula derivation and contour organization; Suzuki [S, Eq. (3.3)] gives precisely the zeta real-space normalization used below. The bounds, source bookkeeping, and elementary obstructions are derived explicitly here. No academic novelty for the explicit formula is asserted.

## 2. A typed, surjective test interface

For each \(g\in\mathcal D\), define on the real additive carrier

\[
f_g(x)=\begin{cases}x^{-1/2}g(\log x),&x>0,\\0,&x\le0.\end{cases}
\tag{2.1}
\]

If \(\operatorname{supp}g\subset[-R,R]\), then \(f_g\) has support in \([e^{-R},e^R]\), so extension by zero is smooth at 0 and \(f_g\in C_c^\infty(\mathbb R)\subset\mathcal S(\mathbb R)\). Conversely, every \(C_c^\infty(0,\infty)\) function is of this form, uniquely. The interface is therefore onto the entire compact smooth log-test space, not just a Gaussian, tent, or autocorrelation family.

With real multiplicative measure \(dx/|x|\),

\[
\int_{\mathbb R^\times} f_g(x)\operatorname{sgn}(x)^\varepsilon
 |x|^s\frac{dx}{|x|}=H_g(s)
\tag{2.2}
\]

for every complex s. There is no convergence restriction because the support avoids 0 and infinity. The half-density in (2.1) is forced by the chosen central line: replacing it by \(x^{-b}\) changes the exponent in (1.2) to \(s-b\), hence introduces real drift on \(\Re s=1/2\) unless \(b=1/2\).

This real Haar convention gives the usual \(\Gamma_{\mathbb R}(s)\) from \(e^{-\pi x^2}\) integrated over both signs. Burnol [B] instead normalizes real multiplicative Haar to push forward under \(|x|\) to \(dt/t\), hence uses \(dx/(2|x|)\). His real Tate integrals have an extra factor 1/2 for the same test; one must rescale the test to compare them. This constant does not affect a logarithmic derivative, but it does affect the unnormalized source integral and (2.3).

Normalize finite multiplicative Haar measure by \(\operatorname{vol}(\mathbb Z_p^\times)=1\). For zeta, take \(\Phi_g=f_g\otimes\prod_p1_{\mathbb Z_p}\). For χ₄ use the unramified character with \(\chi_p(p)=\chi_4(p)\) at odd p, and at p=2 use

\[
\Phi_{g,2}(x)=\chi_2(x)^{-1}1_{\mathbb Z_2^\times}(x),
\quad \chi_2(2)=1,\quad \chi_2(u)=\chi_4(u\bmod4).
\]

The real character is \(\operatorname{sgn}(x)\). These local characters multiply to 1 on diagonal \(\mathbb Q^\times\). The local ramified integral is 1 and every odd local integral is the genuine signed Euler factor. Consequently,

\[
Z(\Phi_g,\chi,s)=H_g(s)L(s,\chi),\qquad \Re s>1.
\tag{2.3}
\]

Both the compact-test embedding and the idelic integral are linear in g. The normalized arithmetic source \(\mathcal L_\chi\) is obtained separately from the canonical Gaussian/odd Gaussian tensor and its ramified local factor. One must **not** take the logarithmic derivative of (2.3) and mistake it for \(L'/L\): it would additionally contain \(H_g'/H_g\), including test-dependent poles. The honest construction is

\[
(\text{normalized Tate source},g)
\longmapsto (\mathcal L_\chi,H_g)
\longmapsto (\mathcal L_\chi'/\mathcal L_\chi,H_g)
\longmapsto W_\chi(g).
\tag{2.4}
\]

This is a typed operation on a fixed normalized arithmetic object and a linear test space. It is not a linear functor from arbitrary Schwartz functions to logarithmic derivatives.

## 3. The arithmetic tape comes from genuine Euler places

For \(\Re s>1\), absolute and locally uniform convergence permits logarithmic differentiation of the Euler product:

\[
-\frac{L'}L(s,\chi)
=\sum_p\sum_{k\ge1}(\log p)\chi(p)^k p^{-ks}
=\sum_{n\ge2}\Lambda(n)\chi(n)n^{-s}.
\tag{3.1}
\]

Here \(\Lambda(p^k)=\log p\) and \(\Lambda(n)=0\) otherwise. In particular the coefficient at 6 is zero. For χ₄, every even coefficient is zero, the coefficient at 3 is \(-\log3\), and the coefficient at 9 is \(+\log3\). The sign of a prime cannot be copied unchanged to all its powers.

The completed logarithmic derivative is

\[
\frac{\mathcal L_\chi'}{\mathcal L_\chi}(s)
=\frac12\log(q/\pi)
 +\frac12\psi((s+\varepsilon)/2)
 -\sum_{n\ge2}\Lambda(n)\chi(n)n^{-s}.
\tag{3.2}
\]

For \(\xi(s)=s(s-1)\mathcal L_\zeta(s)/2\), add \(1/s+1/(s-1)\). The extra factor 2 in `complete_logderivative_from_heat` is deliberate: that routine returns \(2\xi'/\xi\), not (3.2).

For \(\sigma>1\) and integer \(N\ge3\),

\[
\sum_{n>N}|\Lambda(n)\chi(n)n^{-s}|
\le N^{1-\sigma}\left(\frac{\log N}{\sigma-1}
                     +\frac1{(\sigma-1)^2}\right).
\tag{3.3}
\]

Indeed \(|\chi(n)|\le1\), \(\Lambda(n)\le\log n\), and \(\log x\,x^{-\sigma}\) is decreasing for \(x\ge3\). Integrate this majorant from N to infinity. Formula (3.1) is not asserted to converge on the critical line.

## 4. Definition of the source-built signed distribution

Put

\[
\alpha=\varepsilon+\tfrac12,\qquad
K_\varepsilon(x)=\frac{e^{-\alpha x}}{1-e^{-2x}}\quad(x>0),
\]

\[
D_g(x)=g(x)+g(-x)-2e^{-x/2}g(0),\qquad
c_{q,\varepsilon}=\log(q/\pi)+\psi((\varepsilon+1)/2).
\]

Define

\[
\begin{split}
P_\chi(g)&=\delta\int_{\mathbb R}2\cosh(u/2)g(u)\,du,\\
E_\chi(g)&=\sum_{n\ge2}\frac{\Lambda(n)\chi(n)}{\sqrt n}
                              [g(\log n)+g(-\log n)],\\
A_\chi(g)&=c_{q,\varepsilon}g(0)
                  -\int_0^\infty K_\varepsilon(x)D_g(x)\,dx,\\
W_\chi(g)&=P_\chi(g)+A_\chi(g)-E_\chi(g).
\end{split}
\tag{4.1}
\]

The prime sum is finite for every compactly supported g. Near zero, \(D_g(x)=g(0)x+O(x^2)\), so the apparent \(1/(2x)\) kernel singularity is integrable. At infinity, the compact g terms vanish and the remaining compensation decays exponentially. This constructs \(W_\chi\) without any nontrivial-zero coordinate.

The two complete Archimedean formulas are

\[
A_\zeta(g)=-(\gamma+\log(4\pi))g(0)
-\int_0^\infty\frac{e^{-x/2}D_g(x)}{1-e^{-2x}}\,dx,
\tag{4.2}
\]

\[
A_{\chi_4}(g)=(\log(4/\pi)-\gamma)g(0)
-\int_0^\infty\frac{e^{-3x/2}D_g(x)}{1-e^{-2x}}\,dx.
\tag{4.3}
\]

Changing only the conductor cannot turn the even kernel (4.2) into the odd kernel (4.3). The χ₄ form has no zeta pole contribution.

**Proposition 4.1 (spectral Gamma identification).** For all \(g\in\mathcal D\),

\[
A_\chi(g)=\frac1{2\pi}\int_{\mathbb R}H_g(1/2+it)
\left\{\log(q/\pi)+\Re\psi(1/4+\varepsilon/2+it/2)\right\}\,dt.
\tag{4.4}
\]

**Proof.** Apply the convergent digamma difference identity

\[
\psi(z)+\gamma=\int_0^\infty\frac{e^{-v}-e^{-zv}}{1-e^{-v}}\,dv
\qquad(\Re z>0)
\]

with a common positive lower cutoff, Fourier invert against \(H_g\), and set \(v=2x\). Before rearranging, the integrand is

\[
\frac{2e^{-2x}g(0)-e^{-\alpha x}[g(x)+g(-x)]}{1-e^{-2x}}.
\]

Extract \(-K_\varepsilon D_g\). The remaining contact integral is

\[
2g(0)\int_0^\infty
\frac{e^{-2x}-e^{-(\varepsilon+1)x}}{1-e^{-2x}}\,dx
=[\psi((\varepsilon+1)/2)+\gamma]g(0).
\]

The \(-\gamma\) contact in the first digamma identity cancels this \(+\gamma\). Letting the cutoff tend to zero is justified by the cancellation above and the rapid decay of \(H_g\). This proves (4.4). \(\square\)

## 5. Identification with the complete Weil distribution

**Theorem 5.1 (Tate-to-Weil identification; classical).** Assume the authentic Tate source reconstruction of (1.1), its meromorphic continuation and functional equation, and the standard finite-order/vertical-strip estimates for these completed Dirichlet functions. Then for every \(g\in\mathcal D\),

\[
W_\chi(g)=\sum_{\rho:\,\mathcal L_\chi(\rho)=0}m_\rho H_g(\rho).
\tag{5.1}
\]

The sum is absolutely convergent. Zeros in (5.1) are the zeros of the completed source, with multiplicity; they lie in the closed strip \(0\le\Re\rho\le1\) by Euler nonvanishing and the functional equation. No zero coordinate is a construction input to (4.1). The trivial zeros have already been canceled by Gamma poles and are not to be added again. The familiar stronger fact excluding boundary zeros is not needed for the contour argument or the bounds below.

**Proof.** Write \(F=\mathcal L_\chi\), choose \(c>1\), and integrate \((F'/F)(s)H_g(s)\) counterclockwise around the rectangle with vertical sides \(c\) and \(1-c\). The standard contour lemma for completed Dirichlet L-functions supplies heights \(T_j\to\infty\), avoiding zeros, such that \(F'/F(\sigma\pm iT_j)\) is polynomially bounded in \(T_j\), uniformly for \(1-c\le\sigma\le c\). This logarithmic-derivative estimate away from zeros, and the count bound used below, are explicitly imported classical analytic estimates. Rapid decay of \(H_g\) then makes both horizontal integrals vanish. Their inputs are Euler nonvanishing for \(\Re s>1\), continuation and completed-function growth; neither estimate assumes critical-line zeros. This is the classical analytic contour step in [B, §C; W], not a consequence of finite matrix tests.

The residue theorem gives

\[
\sum_\rho m_\rho H_g(\rho)-\delta[H_g(0)+H_g(1)]
=\frac1{2\pi i}\int_{(c)}\frac{F'}F(s)[H_g(s)+H_g(1-s)]\,ds.
\tag{5.2}
\]

Here the functional equation gives \((F'/F)(s)=-(F'/F)(1-s)\), turning the left vertical line into the second term on the right. The constant root number differentiates to zero; its value was checked upstream.

Insert (3.2) **only on the absolutely convergent line \(\Re s=c>1\)**. Mellin inversion gives

\[
\frac1{2\pi i}\int_{(c)}n^{-s}H_g(s)\,ds
=n^{-1/2}g(\log n),
\]

and the same expression with \(H_g(1-s)\) gives \(n^{-1/2}g(-\log n)\). The two half-Gamma terms can each be shifted to \(\Re s=1/2\), because their own Gamma poles lie at \(-\varepsilon-2k\), outside the intervening strip. This shifts the Gamma terms, not the zero-bearing full logarithmic derivative. After \(t\mapsto-t\) in one term they give (4.4). The constant yields \(\log(q/\pi)g(0)\), and the residues at 0,1 yield \(P_\chi\). Thus (5.2) is exactly (4.1).

For convergence, repeated integration by parts gives arbitrarily rapid \(|\Im s|^{-m}\) decay of \(H_g\), uniformly for \(0\le\Re s\le1\). The classical zero-count bound \(N_\chi(T)=O_\chi(T\log(T+2))\) then makes the sum absolutely convergent. Hence no ordering ambiguity remains for this test class. \(\square\)

The proof exposes its classical analytic dependencies instead of relabeling them new SUCC results. It closes the full-test **signed identification** interface once the upstream Tate analytic package is available. It does not close the positivity interface.

## 6. Continuity and explicit approximation errors

For \(R>0\), write \(\mathcal D_R=\{g\in\mathcal D:\operatorname{supp}g\subset[-R,R]\}\), \(M_j=\|g^{(j)}\|_\infty\), and

\[
B_\chi(R)=\sum_{2\le n\le e^R}\frac{\Lambda(n)|\chi(n)|}{\sqrt n},
\qquad I_\alpha=\frac1{\alpha^2}+\frac1{2\alpha}.
\]

**Proposition 6.1 (fixed-support continuity).**

\[
|W_\chi(g)|\le C_0(R,\chi)M_0+C_1(\chi)M_1,
\tag{6.1}
\]

where

\[
C_0=8\delta\sinh(R/2)+2B_\chi(R)+|c_{q,\varepsilon}|+I_\alpha,
\qquad C_1=2I_\alpha.
\tag{6.2}
\]

**Proof.** The pole integral has absolute value at most \(8\delta\sinh(R/2)M_0\); the prime sum is bounded by \(2B_\chi(R)M_0\). The mean-value bound and \(1-e^{-x/2}\le x/2\) imply

\[
|D_g(x)|\le(2M_1+M_0)x.
\]

Since \((1-e^{-2x})^{-1}\le1+(2x)^{-1}\),

\[
\int_0^\infty xK_\varepsilon(x)\,dx
\le\int_0^\infty e^{-\alpha x}(x+1/2)\,dx=I_\alpha.
\]

Combine the bounds. \(\square\)

Thus \(W_\chi\) is a continuous distribution, and for \(g,h\in\mathcal D_R\),

\[
|W_\chi(g)-W_\chi(h)|\le
C_0\|g-h\|_\infty+C_1\|g'-h'\|_\infty.
\tag{6.3}
\]

This is an explicit error guarantee for an adequately rich fixed-support approximation scheme. Density must be in at least this topology, not merely pointwise sample agreement. The union over all R is the full test space; one fixed R does not establish arbitrary-support positivity.

The implementation `tate_weil_distribution.py` uses a deliberately coarse **rational** majorant. For its finite source-label set \(\mathscr A_R\), which includes every genuine atom in the window and may include extra atoms outside it,

\[
\begin{split}
|W_\chi(g)-W_\chi(h)|\le{}
&\left[4\delta R3^{\lceil R/2\rceil}
 +2\sum_{(n,p,\chi(n))\in\mathscr A_R}p
 +C_{\rm contact}+I_\alpha\right]\Delta_0
 +2I_\alpha\Delta_1,
\end{split}
\tag{6.3a}
\]

where \(\Delta_j\) are rational upper bounds on the two supremum errors, \(C_{\rm contact}=4\) for zeta and 2 for χ₄. Indeed \(2\cosh(u/2)\le2e^{R/2}\le2\cdot3^{\lceil R/2\rceil}\), \(\log p/\sqrt n<p\), and the contact bounds follow from \(0<\gamma<1\), \(2<\pi<4\), \(\log2<1\), and \(\log16<3\). For the latter inequality, the exponential series gives \(e^3>16\). All coefficients of (6.3a) are rational when R is rational. The norm bounds remain mathematical premises: a few sampled test values do not certify them.

**Proposition 6.2 (Gamma ladder).** Replace \(K_\varepsilon\) by

\[
K_{\varepsilon,J}(x)=\sum_{j=0}^{J-1}e^{-(2j+\alpha)x},\qquad J\ge1,
\]

and denote the resulting Archimedean term by \(A_{\chi,J}\). With \(a=2J+\alpha\),

\[
|A_\chi(g)-A_{\chi,J}(g)|
\le(2M_1+M_0)\left(\frac1{2a}+\frac1{a^2}\right).
\tag{6.4}
\]

For C² tests, the accelerated approximation

\[
\widetilde A_{\chi,J}(g)=A_{\chi,J}(g)-\frac{g(0)}{2a}
\]

satisfies

\[
|A_\chi(g)-\widetilde A_{\chi,J}(g)|
\le\frac{M_0}{a^2}
 +(M_2+M_0/4)\left(\frac1{2a^2}+\frac2{a^3}\right).
\tag{6.5}
\]

**Proof.** The omitted kernel is \(e^{-ax}/(1-e^{-2x})\), giving (6.4). Taylor's theorem gives \(|D_g(x)-g(0)x|\le(M_2+M_0/4)x^2\). Use \(0\le x/(1-e^{-2x})-1/2\le x\) for the linear term and \(x^2/(1-e^{-2x})\le x^2+x/2\) for the remainder, then integrate against \(e^{-ax}\). \(\square\)

For \(L\ge R\), truncating the Gamma integral at L has the separate bound

\[
\left|\int_L^\infty K_\varepsilon(x)D_g(x)\,dx\right|
\le\frac{2M_0e^{-(\alpha+1/2)L}}
{(\alpha+1/2)(1-e^{-2L})}.
\tag{6.6}
\]

The arithmetic truncation is exactly zero once the cutoff N satisfies \(N\ge e^R\); one may use the rationally verifiable sufficient cutoff \(N\ge3^{\lceil R\rceil}\) because \(e<3\). Finite ladder quadrature still needs a separate rigorous integration error bound: (6.4)–(6.6) do not turn floating-point quadrature into interval certification.

For completeness, a zero-side tail can also be bounded without reading zero coordinates. Define the **two-sided** count \(N_\chi(t)=\sum_{|\Im\rho|\le t}m_\rho\). If an independently justified estimate is \(N_\chi(t)\le C_\chi t\log(B_\chi t)\) for \(t\ge T_0\), let

\[
J_m(g,R)=2Re^{R/2}\sum_{j=0}^{m}\binom mj2^{-(m-j)}M_j,
\qquad r=2^{1-m},\quad m\ge2.
\]

Integration by parts and dyadic shells give, for \(T\ge T_0\),

\[
\sum_{|\Im\rho|>T}m_\rho|H_g(\rho)|
\le2C_\chi J_m(g,R)T^{1-m}
\left[\frac{\log(B_\chi T)}{1-r}
     +\frac{\log2}{(1-r)^2}\right].
\tag{6.7}
\]

This conditional numerical envelope is useful only after the constants and domain of the count theorem have been authenticated. The existing `signed_weil_h1_tail.py` supplies a separate zeta source-count route; this note does not silently certify a new χ₄ count constant.

## 7. What the distribution remembers and forgets

Away from zero, (4.1) is locally a signed Radon measure:

\[
W_\chi\big|_{\mathbb R\setminus\{0\}}
=\big[2\delta\cosh(u/2)-K_\varepsilon(|u|)\big]du
-\sum_{n\ge2}\frac{\Lambda(n)\chi(n)}{\sqrt n}
 (\delta_{\log n}+\delta_{-\log n}).
\tag{7.1}
\]

The atoms are locally finite. By uniqueness of the Lebesgue decomposition, the full distribution recovers every arithmetic coefficient from its atomic masses. A smooth Gamma or pole adjustment cannot hide a fake standalone impulse at 6, a missing prime, or a wrong half-density. On a fixed compact log window it recovers only the atoms lying in that window.

Concrete mutation interfaces follow.

| Mutation | Witness and scope |
| --- | --- |
| Add coefficient b at n=6 | Exact difference \(-b/\sqrt6\,[g(\log6)+g(-\log6)]\); a smooth bump there detects it. The genuine source rejects it already as a prime-power label. |
| Remove odd prime p from χ₄ | Exact missing atomic coefficient \(\chi_4(p)\log p/\sqrt p\), and its lawful power coefficients; a window around \(\log p\) suffices. Omitting the Euler factor at p=2 is instead correct for conductor 4. |
| Replace half-density 1/2 by b | Atomic amplitudes become \(\Lambda(n)\chi(n)n^{-b}\); any nonzero source coefficient distinguishes \(b\ne1/2\), assuming the same log locations. |
| Change conductor q to q′, keep parity fixed | Difference \(\log(q'/q)\delta_0\), detected by any test with \(g(0)\ne0\). |
| Change parity | Changes the smooth density \(-K_\varepsilon\) away from zero and the contact; a bump avoiding all atomic locations detects it. |
| Insert/delete zeta poles | Changes the smooth density \(2\cosh(u/2)\); this cannot be repaired by a finite source tape. |
| Wrong local Fourier/Gauss phase | Requires the upstream finite-character/Fourier witness. A real self-dual downstream form, which factors through the even part of g, can conceal orientation information. |
| Incorrect constant root-number metadata or overall nonzero scalar | The logarithmic derivative is blind to the scalar, and its differentiated functional equation contains no explicit root-number constant. The current downstream evaluator does not validate supplied root metadata: use the upstream Fourier/Gauss-sum witness. See the qualification below. |
| Matched non-Euler tail beyond the support window | No test in that window distinguishes it. The full authentic arithmetic law rejects it, or a larger window observes it. |

The tail ambiguity on a bounded window and the absolute-scalar ambiguity are exact kernels of those observations, not accidental numerical insensitivity. In particular equality of all logarithmic derivatives determines an analytic nonzero source locally only up to a constant. Calling this map source-faithful requires retaining the upstream normalization receipt alongside the downstream distribution.

There is an important qualification for root numbers: no blanket theorem says the root number is irrecoverable from the **full** logarithmic derivative together with additional global analytic structure. For a self-dual meromorphic function satisfying \(F(s)=wF(1-s)\), if its order at \(s=1/2\) is m, then comparison of leading Taylor/Laurent terms gives \(w=(-1)^m\), and m is the residue of \(F'/F\) there. Thus simply changing the root-number label while holding the genuine source function fixed does not produce a second lawful source. The concrete audit boundary here is narrower: checking (3.2), (4.1), or the differentiated functional equation alone does not execute this extra reconstruction, and a normalization contract is not itself a Gauss-sum proof. The upstream receipt supplies the actual phase check.

## 8. An unconditional authentic-source positivity obstruction

**Theorem 8.1 (pointwise positivity is the wrong cone).** Neither \(W_\zeta\) nor \(W_{\chi_4}\) is a positive distribution on pointwise nonnegative compact smooth tests. Consequently neither can be the pushforward of a positive measure by a positivity-preserving linear map on that test cone.

**Zeta proof with rational margin.** Set \(\eta=1/100\). Let \(b(t)=\exp(1-1/(1-t^2))\) for \(|t|<1\), and b(t)=0 otherwise. Then \(0\le b\le1\), b(0)=1, and b is smooth. Choose

\[
g(u)=b((u-\log2)/\eta).
\]

Its support lies in (0,1), it has g(0)=0, and g(log 2)=1. The only integer n≥2 with \(\log n\) in its support is 2: indeed \(\log(3/2)>1/3>\eta\), using \(\log(1+x)\ge x/(1+x)\). Thus the single arithmetic atom contributes \(-\log2/\sqrt2<-1/3\), from \(\log2>1/2\) and \(\sqrt2<3/2\). Every Gamma contribution is nonpositive, because the kernel and g are nonnegative and the contact vanishes. On (0,1), \(e^{u/2}+e^{-u/2}<4\), so the pole integral is less than \(4\cdot2\eta=2/25\). Therefore

\[
W_\zeta(g)<\frac2{25}-\frac13=-\frac{19}{75}<0.
\tag{8.1}
\]

The elementary bounds \(\log2<7/10\) and \(e^{1/2}<2\) used to locate the support and bound the pole density follow directly from the exponential series, or rational exponential enclosures. No zero data or floating quadrature is used.

**χ₄ proof.** Use the same bump centered at \(\log5\). The neighboring integer log gaps satisfy \(\log(5/4)>1/5\) and \(\log(6/5)>1/6\), both greater than η; hence only n=5 lies in the window. There is no pole term, the contact vanishes, the Gamma integral is strictly negative, and \(\chi_4(5)=1\). Thus

\[
W_{\chi_4}(g)<-\frac{\log5}{\sqrt5}<0.
\tag{8.2}
\]

A positive measure paired with the image of every pointwise nonnegative test under a positivity-preserving map cannot have these negative evaluations. This proves the stated obstruction. \(\square\)

This theorem does **not** refute Weil positivity. The relevant cone there consists of additive convolution autocorrelations

\[
g=f*\widetilde f,\qquad \widetilde f(u)=\overline{f(-u)}.
\]

Such tests need not be pointwise nonnegative; conversely, the nonnegative bumps above are not nonzero autocorrelations, because they have g(0)=0 while every nonzero autocorrelation has \(g(0)=\|f\|_2^2>0\). Their centered Mellin transform is

\[
H_{f*\widetilde f}(s)=H_f(s)\overline{H_f(1-\overline s)}.
\tag{8.3}
\]

On the critical line this is \(|H_f(s)|^2\). Off the line it is not a squared modulus. Identifying (4.1) with (5.1) therefore does not make its quadratic form positive. For zeta the all-test positivity criterion is RH; for χ₄ it is the corresponding GRH statement. No such theorem is established here.

## 9. Observer-relative boundary and next discriminating probe

The completed carrier makes the source distribution mathematically well-defined and permits finite symbolic proofs of identities on an infinite test space. A particular compact-support evaluation needs only finitely many exact prime-power labels, plus certified integration or series error control for its real-place term. It does not require enumerating all primes or knowing nontrivial zeros. A physically observed finite tape supplies less information than the declared exact arithmetic source law.

The compact test embedding (2.1), source coefficient identity (3.1), complete signed identification (5.1), and estimates (6.1)–(6.6) close a defined classical interface. They do not authenticate physical events from a model-generated label, establish universal executable precision without an input representation, recover an absolute scalar normalization from a logarithmic derivative, or classify RH as IdealHardField/FuckedField. Such labels require a declared carrier, target, proof theory, experiment class and execution model, together with an actual result about that tuple.

The next consequential probe is a source-specific **convolution-cone** comparison: construct one candidate positive source mechanism, state its map to arbitrary \(f*\widetilde f\), and prove or falsify equality with the complete form using (6.3)–(6.5) uniformly on a declared support/Sobolev window. It must survive χ₄ parity and signs, preserve the root-phase receipt upstream, and expose where support-dependent estimates cease to be uniform. Testing ordinary nonnegative functions or quoting Parseval cannot replace this gate; Theorem 8.1 decisively rules out that particular shortcut.

## 10. Claim summary and references

| Claim | Status | Boundary / next falsification |
| --- | --- | --- |
| Compact Tate test embedding reaches every \(C_c^\infty\) log test | PROVED PAPER, classical Mellin substitution | Check positive-axis support and multiplicative Haar factor; do not differentiate the varying test factor |
| Complete ζ and χ₄ signed Weil formulas | CLASSICAL IDENTIFICATION, independently reconstructed | Uses upstream Tate continuation/FE and classical contour estimates; no RH input |
| Explicit C¹ continuity and Gamma ladder errors | PROVED PAPER | Quadrature errors require their own certificates; support must be declared |
| Atomic source coefficients are identifiable away from 0 | PROVED PAPER, elementary distribution theory | Fixed windows do not recover unobserved tails |
| Absolute scalar normalization is recoverable from the logarithmic derivative | REFUTED | Retain the normalized upstream source receipt; constant root-number metadata separately requires a genuine phase check |
| Authentic Weil distributions are pointwise-positive | REFUTED | Exact source bump witness, ζ margin \(-19/75\) |
| Full convolution-autocorrelation positivity | UNVERIFIED / RH or χ₄-GRH HARD | The next missing theorem, not supplied by any claim above |

Primary sources consulted during this reconstruction:

- **[T]** J. Tate, *Fourier Analysis in Number Fields and Hecke's Zeta-Functions*, Princeton thesis (1950), reprinted in Cassels–Fröhlich, *Algebraic Number Theory* (1967), pp. 305–347. Historical source attribution; the present online verification of the Tate-to-Weil interface used the author's derivation [B].
- **[W]** A. Weil, *Sur les « formules explicites » de la théorie des nombres*, Comm. Sém. Math. Univ. Lund (1952), pp. 252–265. Classical source attribution; not independently digitized or reproduced here.
- **[B]** J.-F. Burnol, [*The Explicit Formula and the conductor operator*](https://arxiv.org/pdf/math/9902080), 1999, §§B–C, especially pp. 5–8. Directly inspected author manuscript. Its zero/pole sign convention is opposite to (5.1), and its real multiplicative Haar normalization pushes forward to \(du/u\), whereas (2.2) uses \(dx/|x|\); these differences have been resolved explicitly rather than copied across.
- **[S]** M. Suzuki, [*On the Hilbert space derived from the Weil distribution*](https://www.cambridge.org/core/journals/canadian-journal-of-mathematics/article/on-the-hilbert-space-derived-from-the-weil-distribution/FD33EBD117A6B448053450DD8D62ADB6), Eq. (3.3). Directly inspected published formula; it agrees with (4.2) after its spectral coordinate \(\rho=1/2-i\gamma\) is converted to (1.2). Suzuki's Hilbert norm identifications with the full Weil structure have explicit RH hypotheses.
- **[D]** NIST DLMF, [§5.9, Eq. (5.9.16)](https://dlmf.nist.gov/5.9.E16), verified digamma integral used in Proposition 4.1.

The rigorous derivations in this note are mathematical proofs under their stated classical inputs. Numerical comparisons and repository CI validate implementation consistency, not those imported infinite theorems or RH.

RH PROVED: NO.
