# Critical source Laplace scattering, Gamma(1/2) cusp and decisive controls

Additive paper-level proof dossier; parent #558 and preregistration pinned. **π normality remains OPEN.** No novel-priority or Lean claim.

## LCS-04 — Critical source-only response (PROVED PAPER)

Write e(x)=exp(2πix), and use original four-pole r(n+1)=(15/64)n⁻²+O(n⁻³). For t>0, integer h, put

\[
D_{h,t}=t\sum_{n\ge0}e^{-tn}\big(e(hr(n+1))-1\big).
\]

This is the SOURCE-ONLY transform; it is NOT the zero-selected Weyl mean. If integer h=h(t) obeys h(t)t²→λ, then

\[
D_{h(t),t}\longrightarrow
I(\lambda)=\int_0^\infty e^{-x}
\left[e\left(\frac{15\lambda}{64x^2}\right)-1\right]dx.
\]

Proof: set x=nt. On every compact interval δ≤x≤L, the original n⁻² source expansion gives uniform convergence of the phase and convergence of Riemann sums. On 0<x<δ, absolute contributions are ≤2δ+o(1); on x>L the geometric tail is ≤2e⁻ᴸ+o(1). Take t→0, δ→0 and L→∞. For λ≠0, Re I(λ)<0 because cos(2π(15/64)λ/x²)−1 is strictly negative on a set of positive measure. Thus the source-only critical response does NOT disappear at infinity.

As λ→0 through nonzero reals, rescale x=√|λ| y. The integrand is dominated by min(2,C/y²). The remaining integral has the standard Gamma(1/2) / Fresnel value (by v=y⁻² and integration by parts with Abel damping):

\[
I(\lambda)=-\frac{\pi\sqrt{30}}8
e^{-i\,\mathrm{sgn}(\lambda)\pi/4}
\sqrt{|\lambda|}+o(\sqrt{|\lambda|}).
\]

This is a source-derived square-root cusp, *not* a physical quantum claim.

**Source-fingerprint limitation.** The critical response depends only on the leading coefficient 15/64. The distinct four-pole source
r'(n)=r(n)+(1/10)[1/(8n−7)−2/(8n−4)−1/(8n−3)+2/(8n−2)]
has the SAME leading 15/64 coefficient but its n⁻³ coefficient shifts by 1/320. It produces the same I(λ). Therefore this critical source-only Laplace transform is not an injective observation of the complete original source.

## LCS-05 — Coherent counterseed and critical Laplace scaling (PROVED PAPER / REFUTED shortcut)

For the original forcing, the alternative real seed s*=−π/16 gives U_n(s*)=−T_n, T_n=(64n²)⁻¹+O(n⁻³). For every FIXED integer h,

\[
\lim_{z\uparrow1}(1-z)G_{h,s_*}(z)=1.
\]

Yet the source-side R(z), all source Ward coefficients, all source-defect cocycles and the source-only I(λ) are exactly the same. (The irrational wrong-seed state is NOT a rational p-adic state; do not attribute the zero-seeded finite-prime character product to it.)

At moving h(t)t²→λ, the wrong-seed normalized Laplace phase instead converges to

\[
\int_0^\infty e^{-x}e\left(-\frac{\lambda}{64x^2}\right)dx,
\]

by the same controlled Riemann-sum argument; the n=0 term costs O(t). Thus a nonzero critical source-Laplace effect can coexist with a maximally coherent fixed-h nonnormal seed. A valid π-normality proof must use an additional selected-zero signed interaction.

## Preregistered finite diagnostics

The first commit in this branch preregistered A in {160,320,640}, λ in {1/64,1/8,1}, integer h=λA², before the probes. The locally tested source-only finite truncated sums at N=18A were evaluated by two methods: exact original four signed-pole Fractions followed by 60-digit mpmath, and an independent double-precision source phase; all nine method differences were below 3.3e−15. The rigorously bounded omitted tail was less than 3.06e−8. These COMPLEX numerical values are not interval-certified; the asymptotic result is proved separately above, not extrapolated from them. A=160, λ=1/8 gave approximately −0.41814825+0.22774347i, while A=320, λ=1/8 gave −0.41848517+0.22797977i.

**Verdict:** the user's Laplace-domain intuition produces a genuine source-specific, critically scaled boundary response. But both source-only universality and the coherent wrong seed block an inference to selected π-normality. The actual remaining gate is a signed cross-prime/Laplace spectral-overlap estimate, not another positive source integral.