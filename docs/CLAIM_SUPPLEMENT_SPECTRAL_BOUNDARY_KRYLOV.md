# SBK — source-conditioned spectral boundary/Krylov rigidity

**2026-10-22 research-only stacked draft** research/spectral-boundary-source-rigidity-2026-10-22 based on observation-anchored total boundary PR #242 at 146ddf514f05928158b38f0d8216b45df13dc92b, with earlier observer/factorial, SUCC/FUCC and EPR bridges upstream. Main, preserved imports and authentic RH/Weil sources unchanged.

Full [paper](../research/2026-10-22/SPECTRAL_BOUNDARY_SOURCE_RIGIDITY.md). Exact [source](../observational_succ/spectral_boundary_rigidity.py), [tests](../tests/test_spectral_boundary_rigidity.py), and [frozen receipt](../research/2026-10-22/SPECTRAL_BOUNDARY_RIGIDITY_RECEIPT.json).

| ID | Statement | Verdict and missing authority |
|---|---|---|
| SBK-01 | Positive finite path RC source with known unit internal capacitances and source-ordered boundary/ground terminals: full rational response Y(s) uniquely recovers all g_0..g_n and n by Jacobi/Weyl continued-fraction inverse | CLASSICAL / PAPER PROVED, independently exact full-Schur-calibrated. NOT arbitrary network/inverse-Einstein uniqueness |
| SBK-02 | A predeclared bound d on rational response degree, plus 2d+1 distinct exact nonpole boundary samples, uniquely identifies whole response and hence path model in SBK-01 class | CLASSICAL / PAPER PROVED + exact rational interpolation. NO uniform-noise guarantee, no missing pole/higher-degree source allowed |
| SBK-03 | Replacing grounded terminal edge at depth r with one more hidden node leaves boundary moments mu_k identical for k<2r; first difference is prod_(j=1)^r g_j² at moment 2r | CLASSICAL WALK EXPANSION / PAPER PROVED + exact finite tests. Source-relative round trip, NOT gravitational curvature or physical backward causality |
| SBK-04 | Boundary Weyl function of a self-adjoint finite source pair (A,b) determines canonical minimal observable Krylov/Jacobi chain up to standard gauge, not necessarily complete physical graph | CLASSICAL KALMAN/JACOBI / PAPER PROVED. Connected 3-mode star with dark antisymmetric eigenvector has only 2 boundary-visible modes, exact negative control |
| SBK-07 | The source-boundary moment Hankel matrices H_r=(mu_(i+j)) have exact determinants `prod_(j=1)^(r-1) g_j^(2(r-j))` for r≤n and det H_(n+1)=0. Rank measures minimal observable depth; a connected dark graph can have smaller visible Krylov rank | CLASSICAL GRAM/KRYLOV / PAPER PROVED + exact finite independent tests. Arbitrarily small positive minors defeat uncalibrated noisy-rank claims |
| SBK-N1 | Exact/noiseless injectivity implies uniform topology reconstruction from arbitrarily noisy finite boundary samples on all positive conductance chains | REFUTED. Weak but positive extra coupling eps gives response difference below eps² across every s≥0 while depth differs |
| SBK-N2 | Full boundary response or sum of glued DtN maps uniquely identifies independent hidden subsystems | REFUTED. Dark modes, gauge/similarity and arbitrary parallel splitting of a positive constant remain |
| SBK-05 | SUCC's own prime-source operators and authenticated histories determine a physical boundary cyclic vector and a canonical measured transfer function | UNVERIFIED — construct real source-relative observable, not definition by desired answer |
| SBK-06 | Global Archimedean/p-adic SUCC/FUCC/QEC spectral response derives Einstein spacetime, EPR=ER gravity, fine-structure alpha or signed Weil positivity | UNVERIFIED, RH OPEN |

**Validation boundary:** 28 focused independent exact Fraction tests, source module independently checked against the previous finite graph Schur module. CI on 3.10/3.13 has a frozen Git blob-source receipt; report actual exact-head status, not inferred success. No Lean kernel result or physical experiment claimed.

**Next gate:** derive a genuine source-preserving boundary functor on the affine/prime SUCC operator category, show passive transfer response and canonical minimal operational geometry, quantify measurement stability, and preregister independent physical dimensionless branch predictions. Require held-out scales, dark-mode controls, fake prime sources and no physical alpha/Weil inference from positive classical energy.
