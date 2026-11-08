# Source-critical Laplace response: π-normality frontier

2026-11-08. Research-only continuation of draft #558, pinned parent 46b96e61ea8a309546b399da328c9bfcc077ada2. Original four signed BBP poles and literal U0=0 unchanged. **π base-16 normality and signed zero-selected Weyl/Abel decay remain OPEN.**

The user's new hypothesis is that a Laplace-like source domain might expose signed chronological correlations among exact prime phases. Existing draft #496 already established the bounded Abel/Cesàro bridge and Gamma(2) observer; we do not claim that equivalence as new. Draft #558 gives the phase-preserving prime product, while #554 provides a conditional balanced-prime prefix estimate.

## LCS-01 — Exact source integral (paper proof)

Let Q(u)=4−2u³−u⁴−u⁵=2(1−u³)+(1−u⁴)+(1−u⁵), positive for 0≤u<1. Direct integration of the original poles gives

\[
r(n)=\int_0^1u^{8n-8}Q(u)\,du,\qquad
R(z)=\sum_{n\ge1}r(n)z^n
=z\int_0^1\frac{Q(u)}{1-zu^8}\,du.
\]

All exchanges hold for |z|<1 by absolute convergence, and for real 0≤z<1 by positivity. The authentic source has r(n)=a/n²+b/n³+O(n⁻⁴), a=15/64, b=151/512. Since the weighted error is absolutely summable, the classical dilogarithm expansion yields

\[
R(1)-R(z)=\frac{15}{64}(1-z)\log\frac1{1-z}+O(1-z)
\quad(z\uparrow1).
\]

This is a real source-side logarithmic singularity, NOT cancellation in the selected Fourier series.

## LCS-02 — Exactly paid Euler–Mascheroni seam (paper proof)

Put d_n=nr(n)−a/n and D=sum(n≥1)d_n. From the original pole bound |r(n)−a/n²−b/n³|≤1/n⁴ for n≥2, D converges and the rational cutoff D_N has tail

\[
|D-D_N|\le\frac{151}{512N}+\frac1{2N^2},\qquad N\ge2.
\]

Consequently

\[
\lim_{N\to\infty}\left(\sum_{n=1}^Nnr(n)-a\log N\right)
=D+a\gamma,
\qquad
\lim_{z\uparrow1}\left(R'(z)+a\log(1-z)\right)=D.
\]

This is an exact discrete/continuous finite-part difference equal to (15/64)γ. It is a source normalization, not evidence that the real zero-selected phase mean vanishes.

## LCS-03 — Source Ward bound at the critical scale (paper proof)

For the original recurrence U(n+1)=16U(n)+r(n+1), define f(n,h)=exp(2πihU(n)), G_h(z)=sum(n≥0)f(n,h)z^n. For any initial seed s,

\[
G_{h,s}(z)=e(hs)+zG_{16h,s}(z)+zE_{h,s}(z),
\]
\[
E_{h,s}(z)=\sum_{n\ge0}z^ne(16hU_n(s))(e(hr(n+1))-1).
\]

The Ward identity was already in #496; here we bound its correction uniformly as h moves with the Laplace scale t. Using the genuine positivity r(n+1)<15/(64n²), n≥1, and splitting sum min(2,15π|h|/(32n²)) at the square-root threshold gives

\[
|(1-e^{-t})E_{h,s}(e^{-t})|
\le\min\left\{2,(1-e^{-t})\left(4+3\sqrt{\frac{15\pi|h|}{32}}\right)\right\}.
\]

This vanishes as t→0 whenever |h|t²→0, uniformly over seeds. It does NOT furnish a vanishing bound when |h| is of order t⁻², and it does not bound the unknown G_(16h,s) ladder. **That is the critical double scaling to investigate.**

## Mathematical status

The displayed formulas are source-authentic paper derivations; previous Abel/Cesàro equivalence is classical/inherited, not new. The source remains fixed and main is untouched. Further critical scattering, finite-prime signed spectral overlap and hostile controls are documented in sibling notes on this research branch and in the locally tested downloadable research bundle.