# Unique-vacuum gapless Haar coherence: a sharper hostile control

**Date:** 2026-11-13. **Status:** elementary explicit operator-theoretic proof, not a 4D Yang–Mills construction.

This countermodel strengthens the finite 2×2 coherent eigenvalue-1 mutant in MG3: the **full** infinite-dimensional model has exactly one vacuum and no other zero-energy eigenvector, yet its excitation spectrum has no positive lower bound. In each Haar coarse/detail channel separately, the transfer has a uniform spectral margin strictly below one. The singular obstruction lies only in their coherent cross-coupling as observer resolution increases.

## Construction and proof

Take

\[
\mathcal H=\mathbb C\Omega\oplus\bigoplus_{n=2}^{\infty}\mathbb C^2.
\]

On the vacuum set TΩ=Ω; on the nth excitation pair set

\[
T_n=\begin{pmatrix}
3/5 & (2/5)(1-1/n)\\
(2/5)(1-1/n)&3/5
\end{pmatrix}.
\]

The pair eigenvalues are, **exactly**,

\[
\lambda_n^+=1-\frac{2}{5n},\qquad
\lambda_n^-=\frac15+\frac{2}{5n}.
\]

For n≥2, 0<λ_n^-≤λ_n^+<1. Hence 0<T≤I on the non-vacuum summands and T is a bounded positive self-adjoint contraction. Define \(H=-\log T\) by functional calculus, setting HΩ=0 (the spectrum of T is contained in [1/5,1]). Each excited eigenvalue has strictly positive energy \(E_n^\pm=-\log\lambda_n^\pm\); no excited eigenvalue equals zero. Since the operator is a countable direct sum with all \(\lambda_n^\pm<1\), \(\ker H=\mathbb C\Omega\): the vacuum is unique. However \(\lambda_n^+\uparrow1\), so \(E_n^+\downarrow0\), and

\[
\boxed{\inf\sigma(H|_{\Omega^\perp})=0.}
\]

Thus a unique vacuum and strictly positive energies for every individual excitation do **not** establish a mass gap.

Let C be the orthogonal span of first-coordinate basis vectors of every pair, D the orthogonal span of second-coordinate basis vectors. Then

\[
\|P_CTP_C\|=\|P_DTP_D\|=3/5
\]

uniformly in the bank horizon. Nevertheless

\[
\|P_CTP_D\|=\sup_{n\ge2}(2/5)(1-1/n)=2/5
\]

(with supremum not attained on any finite pair), so the strict MG3 margin sits **exactly on its boundary**:

\[
\gamma^2=4/25=(1-\alpha)(1-\beta).
\]

Each fixed finite-horizon bank up to N has \(\lambda_N^+=1-2/(5N)<1\) and therefore a positive finite certificate. But its best q_N approaches 1. No fixed q<1 works across all horizons; this is the exact distinction between finite observations and a certified uniform physical mass gap.

The entire construction is rational at finite horizons, and its continuum operator conclusion follows by spectral functional calculus; no numerical extrapolation or guessed eigenvectors are involved. It is an abstract semigroup, **not** a Wilson-lattice measure, an OS-reconstructed 4D QFT or a mass measurement.

## Why it matters for SUCC

A naïve Haar projection sees 3/5 contraction in each separate channel and declares the system massive. The full, source-coupled SUCC observer retains the nonzero off-diagonal transport and discovers increasingly long-lived coherent modes. **These slow modes do not require a second vacuum**: they can accumulate at zero energy as resolution increases.

Discriminating test: for N=2,4,8,32,128, the exact largest excited transfer eigenvalues are 4/5,9/10,19/20,79/80,319/320. A claimed bank-uniform q must reject every q<1 once N is sufficiently large. If an implementation reports one q for all N, check missing detail channels, re-orthogonalization, stale finite horizon or cutoff-specific choice of q.

**Verdict:** the MG3 **strict** margin must be uniform across channel depth and the physical source, not merely positive at each finite truncation. No independently sourced continuum YM estimate has been provided.
