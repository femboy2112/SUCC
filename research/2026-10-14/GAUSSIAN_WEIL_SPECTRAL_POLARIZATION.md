# Spectral polarization of the genuine SUCC/Weil source: Gamma current, pole modes, and the finite-frequency moat

**2026-10-14; addendum to GWC-5/GWC-6**. Parent draft PR #76 branch \`research/gaussian-weil-conditional-certificates-2026-10-14\`. Input: Suzuki's genuine zeta screw \(g\), Eq. (1.3), https://arxiv.org/html/2606.09096v3. The existing completed-Weil source and its Gamma contact are inherited from SUCC PR #71. **No RH proof; no independently novel priority over Suzuki's high-frequency analysis.** This note isolates an explicit, zero-independent full-source spectral inequality and source-faithful signed-mode partition.

## GWC-7.1 — exact polar rank-two decomposition (PROVED LOCAL)

Write \(u=iv'\in L_0^2(-a,a)\) with \(\int u=0\). For the true pole term
\[
g_{\rm pole}(x-y)=-4(e^{(x-y)/2}+e^{-(x-y)/2}-2)
=-8[\cosh((x-y)/2)-1],
\]
the mean-zero compression is **exactly**
\[
 \boxed{Q_{\rm pole}(u)
 =8|\langle u,\sinh(x/2)\rangle|^2
 -8|\langle u,\cosh(x/2)\rangle|^2.}\tag{P1}
\]
No arbitrary auxiliary modes are inserted: the source polarity of both terms is forced by the completed zeta pole \(s(s-1)\). The constant \(+8\) vanishes because \(\int u=0\), and \(\cosh((x-y)/2)=\cosh(x/2)\cosh(y/2)-\sinh(x/2)\sinh(y/2)\).

**Exact rational source control:** Evaluate at three SUCC clock locations \(x_i=2(\log2)i\), \(i=-1,0,1\); for signed weights \(w=(1,-2,1)\), the positive odd moment vanishes, the even moment is \(1/2\), and \(Q_{\rm pole}=-2\). For weights \(w=(1,0,-1)\), the even moment vanishes, the odd moment has magnitude \(3/2\), and \(Q_{\rm pole}=18\). Thus genuine source poles carry both signs. These weights are **finite signed point-source controls**, not Hilbert \(L^2\) test vectors; smooth approximations are needed to construct actual compact-test witnesses for the *pole component alone*. In the full arithmetic Weil form other components can offset the negative pole.

## GWC-7.2 — the actual Gamma rungs are PSD (PROVED LOCAL)

Let \(d_j=4j+1\), \(\alpha_j=d_j/2\). The authentic Gamma part of Suzuki's screw potential is
\[
  g_\Gamma(t)=-4\sum_{j\ge0}(1-e^{-\alpha_j|t|})/d_j^2 .
\]
On the mean-zero space the constant parts vanish. Consequently the actual Gamma compression is the **positive** OU-resolvent bath
\[
 \boxed{Q_\Gamma(u)=
 \frac1{2\pi}\int_{\mathbb R} B_\Gamma(\xi)|\hat u(\xi)|^2d\xi\ge0,\quad
 B_\Gamma(\xi)=\sum_{j\ge0}\frac{4}{d_j(\xi^2+d_j^2/4)}>0.}\tag{P2}
\]
Proof: the angular Fourier transform of \(e^{-\alpha|t|}\) is \(2\alpha/(\alpha^2+\xi^2)\), and \(4d_j^{-2}(2\alpha_j)=4/d_j\). Absolute convergence follows from \(d_j^{-3}\) at fixed \(\xi\), and dominated convergence is valid for compact \(u\).

At source clock sites \(x_i=2(\log2)i\), each finite \(\Gamma\) matrix is EXACTLY rational:
\[
 (B_{\Gamma,J})_{ik}=\sum_{j=0}^{J-1}\frac4{(4j+1)^2}2^{-(4j+1)|i-k|}\succeq0.
\]
The \(j=0\) contribution for the negative-pole control \(w=(1,-2,1)\) is **+10**, against \(Q_{\rm pole}=-2\). For the odd pole-positive control \(w=(1,0,-1)\), the first Gamma contribution is **+6**. These are genuine arithmetic clock-aligned Gamma terms, not the auxiliary \(\chi_4\) companion bath of prime-sphere PR #68.

## GWC-7.3 — signed finite-prime band and exact high-frequency domination (PROVED LOCAL)

For fixed \(a>0\), put
\[
 c_\Gamma:=\psi(1/4)-\log\pi
 =-\gamma-\pi/2-3\log2-\log\pi<0,\quad
 w_n:=\Lambda(n)/\sqrt n,\quad
 \mathcal P_a:=\{n=p^k:n\le e^{2a}\}.
\]
There are only finitely many genuine source prime-power atoms in \(\mathcal P_a\). The even kernels \(|t|\) and \((|t|-b)_+\), tested on mean-zero compact \(u\), have Fourier multipliers \(-2/\xi^2\) and \(-2\cos(b\xi)/\xi^2\), respectively, modulo distributions concentrated at \(\xi=0\) that vanish in the mean-zero quadratic pairing. This follows by taking distributional second derivatives \(2\delta_0\) and \(\delta_b+\delta_{-b}\), then using the Fourier/derivative identity and mean-zero cancellation.

The exact genuine source form decomposes as
\[
 \boxed{Q_W(v)=
  \frac1{2\pi}\int_{\mathbb R}m_a(\xi)|\widehat{iv'}(\xi)|^2d\xi
  +8|\langle iv',\sinh(x/2)\rangle|^2
  -8|\langle iv',\cosh(x/2)\rangle|^2, }\tag{P3}
\]
where
\[
 \boxed{m_a(\xi)=\sum_{j\ge0}\frac4{d_j(\xi^2+d_j^2/4)}
 +\frac{c_\Gamma-2\sum_{n\in\mathcal P_a}w_n\cos(\xi\log n)}{\xi^2}.}\tag{P4}
\]
At \(\xi=0\), interpret this in the mean-zero quadratic pairing: \(\hat u(\xi)=O(\xi)\), so the apparently singular integral is finite. The identities use **the authentic** Gamma/prime/pole coefficients and no zeta-zero oracle. The dependence on a comes only from which prime atoms can occur within the diameter \(2a\) of the source's original compact test; it does not allow pretending the infinitely many other source primes do not exist globally.

Set \(D_a:= -c_\Gamma+2\sum_{n\in\mathcal P_a}w_n>0\). Let \(J\ge1\) be any integer for which
\[
 \boxed{2\sum_{j=0}^{J-1}\frac1{4j+1}\ge D_a.}\tag{P5}
\]
Such a finite J exists, since the harmonic sum diverges. If \(|\xi|\ge R_J:=(4J+1)/2\), then for every \(j<J\), \((d_j/2)^2\le\xi^2\), and hence
\[
  \sum_{j\ge0}\frac4{d_j(\xi^2+d_j^2/4)}
  \ge \sum_{j<J}\frac2{d_j\xi^2}
  \ge \frac{D_a}{\xi^2}.
\]
Since \(\cos(\xi\log n)\le1\) and \(c_\Gamma<0\), the signed second term of (P4) is at least \(-D_a/\xi^2\). Therefore
\[
 \boxed{ m_a(\xi)\ge0\quad\text{for ALL }|\xi|\ge R_J. }\tag{P6}
\]
This is **unconditional**, finite a, source-independent of unknown zero coordinates, and includes all prime powers within the actual compact support diameter. It is not RH: the band \(|\xi|<R_J\) can still contribute negatively; the pole contains a separate rank-one negative mode; and a nonzero compactly supported function cannot have its Fourier transform vanish on an open interval (Paley–Wiener/identity theorem), so this is NOT a finite-dimensional low-frequency reduction or an exact physical filtering shortcut.

### Numerical scale diagnostics, NOT certified interval thresholds

Using mpmath digamma/harmonic sums and the genuine prime tape, the *approximate* smallest integers J passing (P5), plus conservative \(R_J\), are:

| radius a | prime powers \(n\le e^{2a}\) | approximate J | \(R_J\) |
|---|---:|---:|---:|
| 0.15 | 0 | 677 | 1354.5 |
| 0.5 | 1 | 4806 | 9612.5 |
| 0.75 | 3 | 243011 | 486022.5 |
| 1 | 5 | 81968865 | 163937730.5 |
| 1.5 | 12 | 136619563732267 | 273239127464534.5 |
| 2 | 24 | 1021686551364604685482426 | 2043373102729209370964852.5 |

The exact theorem (P5)-(P6) holds regardless of any rounding; these displayed numbers are **numeric orientation only**, not a statement that outward-certified threshold inequalities were executed at these J. The very rapid growth quantifies why a conservative source-only cutoff is mathematically valid yet experimentally/instrumentally impractical. This is SUCC's IdealHard **resource/conditioning analogy**, not a proof of fundamental undecidability or a physical energy law.

## GWC-7.4 — how this changes the RH attack

The distribution is **not** one globally positive Gaussian, nor a free Gaussian regression interpolation. It is the source-fixed sum of: (1) an authentically PSD Gamma bath; (2) a source-fixed **positive** rank-one polar mode; (3) a source-fixed **negative** rank-one polar mode; (4) finite, frequency-oscillatory prime jets plus a signed contact Brownian term. Equations (P3)–(P6) say the potentially negative *nonpolar spectral density* is supported in an explicit bounded frequency band. This is significantly more structured than a raw finite Gram scan.

**Next verdict-changing instruments**: (a) replace the crude harmonic threshold with an adaptive source-certified lower envelope for \(m_a(\xi)\) on small real-frequency cells; (b) prove a joint inequality that trades the negative \(\cosh\) pole moment and band-limited spectral deficit against the genuine Gamma positive bath and positive odd pole, on **every** \(u=iv'\in L_0^2(-a,a)\); (c) build a rigorous *sinc/interval or Gaussian-Hermite Galerkin* source approximation with outward-rounded errors; (d) repeat against fake composite 6, wrong half-density, wrong Gamma normalization and a correctly completed non-Euler primitive character. If (b) holds for every a from original source laws, RH follows, but it remains **UNVERIFIED**.

**Audit of novelty:** Suzuki 2026 §2.4 already proves an equivalent Fourier-form representation with \(\log|\xi|\) leading behavior and finite-prime oscillations. Our exact OU/rank-two separation, harmonic dominating cutoff and SUCC clock rational regressions are source-specific assembly/quantification; **no claim of an independently new spectral theorem** is justified without comparing scope to that literature.


## GWC-7.5 — fully rational, zero-independent high-frequency certificates (PROVED LOCAL)

The approximate minimal J table above is useful to design instruments but cannot serve as a rigorous certificate by itself. The following deliberately conservative two examples **have no transcendental rounding at all** in the final harmonic inequality and are fully justified by elementary analytic inequalities:

**Claim A (no prime atom yet).** Fix any \(0<a\le1/4\). Then \(e^{2a}\le\sqrt{e}<2\), because the classical bound \(e<4\). Consequently \(\mathcal P_a=\emptyset\) and \(D_a=-c_\Gamma=\gamma+\pi/2+3\log2+\log\pi<8\), since \(0<\gamma<1\), \(\pi<4\), \(0<\log2<1\), and \(\log\pi<\log4<2\). Decompose the exactly rational harmonic sum at \(J=2^q\) into j=0 and q dyadic blocks \(2^m\le j<2^{m+1}\). Each block contributes more than \(1/4\):
\[
 2\sum_{j=2^m}^{2^{m+1}-1}\frac1{4j+1}
 \ge\frac{2^{m+1}}{2^{m+3}-3}>\frac14.
\]
Therefore \(\;2\sum_{j=0}^{2^q-1}(4j+1)^{-1}>2+q/4\).
Take \(q=24\), \(J=2^{24}\); the harmonic sum is strictly greater than 8, therefore strictly greater than the authentic defect \(D_a\). By (P6),
\[
 \boxed{m_a(\xi)\ge0 \;\;\text{for ALL }|\xi|\ge (4\cdot2^{24}+1)/2
 = 33554432.5,\qquad 0<a\le1/4.}\tag{P7}
\]
This exact certificate is *ridiculously conservative*, which is the point: real source truth and computationally useful conditioning are separate properties.

**Claim B (true first-prime interaction).** Fix \(0<a\le1/2\). The elementary \(e<3\) gives \(e^{2a}\le e<3\), hence at most the authentic prime-power atom \(n=2\) occurs. Its true coefficient \(w_2=\log2/\sqrt2<1\), so \(D_a<8+2=10\). Taking q=32 produces \(2\sum_{j<2^{32}}(4j+1)^{-1}>2+32/4=10>D_a\), hence
\[
 \boxed{m_a(\xi)\ge0\quad\text{for ALL }|\xi|\ge(4\cdot2^{32}+1)/2
 =8589934592.5,\qquad 0<a\le1/2.}\tag{P8}
\]
Both (P7) and (P8) retain the *true* source's pole and Gamma normalization and do not require zero coordinates, floating-point spectra, a probabilistic prior or millions/billions of explicitly enumerated rungs. Only the nonpolar multiplier is certified; the negative polar rank-one channel and arbitrary lower-frequency test contributions remain RH-hard.

The corresponding **O(log J) exact-rational proof checker** is \`harmonic_dyadic_lower(q)\` / \`source_spectral_moat(q,D_upper)\`, with targeted independent regression for q=24,D=8 and q=32,D=10. The API makes a genuine semantic distinction: the caller must establish a real upper bound \(D_a\le D_{\rm upper}\) from the original arithmetic/Gamma source; supplying an arbitrary small upper bound would be a source-justification failure, not a valid proof.
