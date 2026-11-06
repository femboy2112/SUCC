# The reciprocal-square observer clock: source-derived radial linearization and exact Fourier zeros

**2026-11-04, additive mathematical continuation of two-clock PR #506.** Parent #504 pinned \`f3327bdce023fe3f68d4c5431b5a7c2b53dac2ed\`. This result was developed interactively after the initial PR #506 preregistration; it is explicitly **post-prereg exploration**, not a blind holdout. All four original signed BBP poles, zero seed, and historical source/proof contracts remain unchanged. Not an original π signed Weyl theorem, a physical relativity claim, or a global novelty assertion.

Define the authentic radial zero-seeded source \(Z_n\), its smooth rational-tail extension \(z(x)\), and fixed signed delay \(\ell\ne0\), as in [TWO_CLOCK_THEOREMS.md](TWO_CLOCK_THEOREMS.md). Put \(e(t)=\exp(2\pi i t)\), \(H\in\mathbb N\), \(q=H/A^2\), \(A\le n<2A\). The proven source expansion is
\[
z(n+\ell)-z(n)=-\frac{\ell}{32n^2}+O_\ell(n^{-3}).
\]

## RC-01: a source-induced reciprocal-square observation clock

Set \(x=n/A\in[1,2]\) and \(\tau=1/x^2\in[1/4,1]\). Then the *leading* actual relative source phase is
\[
H(z(Ax+\ell)-z(Ax))=-\frac{\ell q}{32}\tau+O_\ell(q/A).
\]
The differential is \(d\tau=-2x^{-3}dx\). Uniform sampling in \(\tau\) corresponds to the positive, **normalized** observer density
\[
\boxed{w(x)=\frac8{3x^3},\qquad \int_1^2w(x)dx=1.}
\]
This weighting is an explicit CHOICE OF OBSERVER, not inherited sample-time Haar measure. The original source's \(\{U_n\}\) trajectory is not reweighted by this proof. The time transformation is a deterministic nonuniform reparametrization, not a Lorentz boost.

## RC-02: exact Fourier/sinc form of the retimed radial observer

Define the positive weighted source-relative phase response
\[
C^{\mathrm{rec}}_{A,\ell}(H)
=\frac1A\sum_{n=A}^{2A-1}\frac8{3(n/A)^3}
 e(H(Z_{n+\ell}-Z_n)).
\]
The source expansion and uniform Riemann variation estimate give
\[
C^{\mathrm{rec}}_{A,\ell}(H)
=\frac43\int_{1/4}^1e\left(-\frac{\ell q}{32}\tau\right)d\tau
+O_\ell((1+q)/A).
\]
The continuum integral is elementary and **EXACT**:
\[
\boxed{C^{\mathrm{rec}}_{A,\ell}(H)
=e(-5\ell q/256)\,
 \frac{\sin(3\pi\ell q/128)}{3\pi\ell q/128}
+O_\ell((1+q)/A),}
\]
with sinc(0)=1, used only if \(\ell q=0\); we take \(\ell\ne0,\ q>0\).

For every fixed nonzero integer \(\ell\), every nonzero integer \(k\), and every integer \(A\ge1\) with \(H=128kA^2>0\) (so \(k>0\)), \(\sin(3\pi\ell k)=0\), hence
\[
\boxed{C^{\mathrm{rec}}_{A,\ell}(128k A^2)=O_\ell((1+k)/A).}
\]
The continuum Fourier zero is **exact** and follows from first-principles character orthogonality on an interval of \(\tau\)-length \(3/4\). The discrete BBP radial response need not be literally zero. Finite errors include the exact \(O_\ell(n^{-3})\) source curvature and sampling quadrature.

In particular choose \(k(A)=\lfloor(\log A)/128\rfloor\ge1\) for sufficiently large A and \(H_A^{\rm rec}=128 k(A)A^2\). Then \(H_A^{\rm rec}/A^2\asymp\log A\) but **THIS frequency is not generally #501's prescribed \(H_A(h)=|h|16^j\)**. We obtain the genuinely source-specific weighted observer saving
\[
\boxed{C^{\mathrm{rec}}_{A,\ell}(H_A^{\rm rec})=O_\ell(\log A/A)
=o_\ell(1/\log A).}
\]
This is a real clean reparametrized cancellation theorem. It does **not** prove the original untapered selected π Weyl estimate or replace the maximal-subinterval criterion.

## RC-03: why the equalized boundary flux is exactly the issue

For a smooth observer weight \(w\), the leading nonstationary-phase endpoint term is
\[
\int_1^2w(x)e(-\ell q/(32x^2))dx
=\frac8{\pi i\ell q}
 \left[x^3w(x)e(-\ell q/(32x^2))\right]_{x=1}^{x=2}
+O_{w,\ell}(q^{-2}).
\]
In the original sharp uniform-source-time frame \(w(x)=1\), the two endpoint amplitudes are 1 and 8; they CAN NEVER cancel, yielding OR-03's \(\Theta(1/\log A)\) obstruction. With the reciprocal-clock Jacobian \(w(x)=8/(3x^3)\), **both boundary amplitudes are exactly \(8/3\)**. At \(q=128k\) their phases also coincide, so the leading term cancels—and the entire continuum integral is exactly zero by its linear-in-\(\tau\) Fourier form. This is an exact operational demonstration of observer-dependent cancellation timing/weight, with no physical energy transport.

A completely different route to faster cancellation is a compact smooth taper \(w\in C_c^\infty((1,2))\), as proved in OR-04; there both boundary amplitudes are zero. The reciprocal clock instead pays the boundary by **matching** nonzero endpoint amplitudes and phases.

## RC-04: the radix-16 observer needs a frequency-transported link

The previous ordinary Wilson link \(W_{n,m}(h)=e(h(Z_m-Z_n))\) compares simultaneous characters at *the same frequency*. But the authentic source dynamics includes a radix-16 expansion. For \(n<m\), define the actual dynamically covariant source-relative link
\[
\boxed{D_{n,m}(h)=e\!\left(h(Z_m-16^{m-n}Z_n)\right)
=e\left(h\sum_{j=n+1}^m16^{m-j}r_r(j)\right).}
\]
It obeys the source-correct twisted cocycle
\[
\boxed{D_{n,k}(h)=D_{m,k}(h)\,D_{n,m}(16^{k-m}h),\qquad n<m<k.}
\]
The transported frequency factor \(16^{k-m}\) is **essential**; omitting it changes the mathematical observable and typically breaks the equality. The ordinary W cocycle and the radix-covariant D cocycle answer different observer questions. Both are exact without a π oracle, and neither forces a Haar time orbit.

## Controls, status and next step

1. This weighted radial source is the same real-circle nonnormal source of #500: \(Z_n\to0\), so at every **fixed h**, \(A^{-1}\sum e(hZ_n)\to1\). Thus cancellation at the tuned moving high frequency, even with a natural positive Jacobian and a root-of-unity clock, **does not imply normality**.
2. \(\tau=1/x^2\) is the leading radial-lag phase clock; source error \(O_\ell(q/A)\) is paid. Retiming a different process with unrelated phase curvature may fail.
3. This proof requires tuned frequency \(H=128kA^2\) and a **different observer measure**. Neither is supplied by the actual unweighted high-depth maximal-subinterval Weyl target. Source-original angular/radial correlations remain unbounded. A coherent source compensated by a frame-dependent multiplier still produces false cancellation if incorrectly interpreted as selected mixing.
4. The exact source rank-two/Frobenius and clock cochain are inherited, not independent scholarly witnesses. All mathematical novelty priority is **UNVERIFIED**. A stdlib regression test checks the independent continuum sinc integral, finite exact reciprocity/Fraction link and tuned finite source observer response.
5. **Verdict-changing probe:** find a source-authenticated way of transferring the reciprocal clock's Fourier orthogonality into a bound for the **original equal-time, uniform-source-time** \(\ell=0\) angular–radial product, paying both the Jacobian inverse and the original signed centered numerators without invoking Haar or assuming independence. Without that transport, base-16 π normality remains OPEN.
