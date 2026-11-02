# GS-02C — exact Gamma seam mass: π, eighth-root geometry and the silver ratio

**2026-11-02, research-only paper proof.** This evaluates the *infinite positive source mass* used in GS-02's absolute cutoff-sewing bound. It is a real arithmetic connection to SUCC's algebraic-unit work, **not** a signed Weyl cancellation estimate. The proof uses two independent analytic descriptions of the exact ORIGINAL four-pole source.

Let

\[
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},
\quad
P(u)=4-2u^3-u^4-u^5.
\]

By the exact positive Beta/Mellin representation and monotone convergence,

\[
S_\Gamma:=\sum_{n=1}^\infty r(n)
=\int_0^1\frac{P(u)}{1-u^8}\,du
=\int_0^1\frac{(u^2+2)(u^2+2u+2)}
{(1+u)(1+u^2)(1+u^4)}\,du.
\]

A direct **exact rational-function partial fraction identity** is

\[
\frac{P(u)}{1-u^8}
=\frac{u+3}{4(1+u^2)}
-\frac{u^3}{1+u^4}
+\frac{u}{2(1+u^4)}
+\frac{5}{2(1+u^4)}
+\frac{3}{4(1+u)}.
\]

Integrating the elementary first, second, third and last terms gives

\[
S_\Gamma=\frac\pi4+\frac58\log2
+\frac52\int_0^1\frac{du}{1+u^4}.
\]

Factor \(1+u^4=(u^2+\sqrt2u+1)(u^2-\sqrt2u+1)\). Its two real quadratic partial fractions produce an exact log term and two arctangents:

\[
\int_0^1\frac{du}{1+u^4}
=\frac{\sqrt2\pi}{8}
+\frac{\sqrt2}{4}\log(1+\sqrt2).
\]

To verify the branch, at u=1 the arctangents \(\arctan(1+\sqrt2)+\arctan(\sqrt2-1)=\pi/2\) (both arguments positive, product 1). The log ratio is \((2+\sqrt2)/(2-\sqrt2)=(1+\sqrt2)^2\). Thus

\[
\boxed{S_\Gamma=
\frac{(4+5\sqrt2)\pi}{16}
+\frac58\log2+\frac{5\sqrt2}{8}\log(1+\sqrt2).}
\]

A completely separate derivation uses the original Gamma ratio
\(G(t)=\Gamma(t+1/8)^4/[\Gamma(t+1/2)^2\Gamma(t+5/8)\Gamma(t+3/4)]\).
Since \(r(n)=(1/8)\partial_t\log[G(t+1)/G(t)]_{t=n-1}\) and
\((\log G)'(t)\to0\) at infinity,

\[
S_\Gamma=-\frac18\left[
4\psi(1/8)-2\psi(1/2)-\psi(5/8)-\psi(3/4)
\right].
\]

The standard rational-argument digamma identities yield the same displayed elementary formula. The common Euler–Mascheroni constant cancels, since the source pole weights sum to zero.

The **total earlier-phase cutoff correction** of GS-02 therefore has the explicit fully source-attested upper bound

\[
\boxed{
\frac{2\pi|h|}{15}
\left[
\frac{(4+5\sqrt2)\pi}{16}
+\frac58\log2+\frac{5\sqrt2}{8}\log(1+\sqrt2)
-\frac{47}{15}
\right]
\approx0.1058567126911634\,|h|.}
\]

The algebraic unit \(1+\sqrt2\) (silver ratio, root of \(x^2-2x-1=0\)) appears because the ORIGINAL source's \(1-u^8\) denominator contains \(1+u^4\). This **does not derive π normality from Pisot units**; the scalar source mass and the signed real-circle cross-block correlations are separate observables. A same-four-pole coherent altered real seed has this *identical* mass and fails all positive Haar-loss claims.

**Validation:** independent exact algebraic partial fractions and real-branch arctangent evaluation as above; arbitrary-precision numerical cross-check of the infinite original rational source sum, the Beta integral, the elementary formula and the digamma boundary all agree near 3.38604761959719172. Numeric agreement is not a substitute for the exact derivations. Do not infer an independent source randomization law.
