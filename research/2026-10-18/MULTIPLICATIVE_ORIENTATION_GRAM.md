# Multiplicative orientation Gram: divisor vs interval completions of FUCC and the log-source obstruction

**Date:** 2026-10-18. **Base:** draft Connes PR #169, originally at 9924e7783a5ef3657a48c735b5a730f76a971973, itself based on research/direct-quotient-pontryagin-transfer-2026-10-17@c8ed4929cb4659de5dfbd8c8c11475e723ec2c2d. **Authority:** elementary mathematical proofs below; exact independent integer/Fraction probes. The GCD/Smith/Euler-totient positivity phenomenon, valuation-tree negative type, and interval covariance are classical mathematics. The comparison is new-to-SUCC research packaging, not claimed academic priority. **RH PROVED: NO.**

## Motivation: don't mistake an arbitrary positive matrix for one from multiplication on Z_{>0}

The previous local Connes bridge proved exact rational off-identity p-adic fixed-point coefficients and showed the *necessity* of distinguishing single-place idèle scaling from diagonal rational gauge. Its arbitrary-contact negative Gram mutation correctly refuted orientation **by itself** as a universal PSD theorem, but did not probe positivity arising from actual FUCC multiplication and unique factorization. The present note strengthens that test with two genuinely multiplication-covariant all-finite-set PSD Gram kernels and a nontrivial negative-type logarithmic generator.

## MOG-01. Two canonical normalized positive Gram kernels (CLASSICAL/PROVED)

For m,n≥1 let

\[
K_D(m,n)=\frac{\gcd(m,n)}{\sqrt{mn}},\qquad
K_A(m,n)=\frac{\min(m,n)}{\sqrt{mn}}.
\]

There are two independent **Gram factorizations**, both using canonical norm-one vectors:

\[
D_n(d)=\frac{\sqrt{\varphi(d)}}{\sqrt n}\,\mathbf1_{d\mid n}\in\ell^2(\mathbb N),\quad
A_n(x)=\frac{\mathbf1_{0<x\le n}}{\sqrt n}\in L^2(\mathbb R_{>0}).
\]

The classical identity \(\sum_{d\mid r}\varphi(d)=r\), applied to r=gcd(m,n), proves
\(\langle D_m,D_n\rangle=K_D(m,n)\); indicator overlap length proves
\(\langle A_m,A_n\rangle=K_A(m,n)\). Both vectors have norm one. Hence **for every finite set of labels, every complex coefficient vector**, both kernels are PSD without assuming RH or testing any zeros. Equivalently the unnormalized exact integer matrices have distinct incidence sums of squares:

\[
\sum_{i,j}\bar c_i\,\gcd(n_i,n_j)c_j
=\sum_{d\ge1}\varphi(d)\left|\sum_{i:d\mid n_i}c_i\right|^2,
\]

\[
\sum_{i,j}\bar c_i\,\min(n_i,n_j)c_j
=\int_0^\infty\left|\sum_{i:x\le n_i}c_i\right|^2dx.
\]

Both normalized matrices are positive diagonal congruences of the respective unnormalized ones.

### FUCC equivariance and agreement along every jet

For every integer a,m,n≥1,
\(K_D(am,an)=K_D(m,n)\) and \(K_A(am,an)=K_A(m,n)\). If \(m\mid n\) or \(n\mid m\), then gcd(m,n)=min(m,n), so **all comparable FUCC pairs** agree. In particular \(K_D(1,p^k)=K_A(1,p^k)=p^{-k/2}\), matching the squared half-density coefficient of the earlier independent local Connes C_p(p^k)=p^{-k/2} construction.

The normalization \(1/\sqrt n\) is forced if one demands that each original feature vector, with squared raw norm n, be of norm one; this is a true all-finite-set PSD mechanism. It does **not** uniquely choose a representation of the full arithmetic source.

## MOG-02. A real gluing defect, not merely an artificial negative toy (PROVED)

For incomparable m,n, gcd(m,n)<min(m,n). Thus \(K_A(m,n)-K_D(m,n)>0\), although the two kernels share identical diagonal entries. Already on labels (2,3),

\[
(K_A-K_D)|_{\{2,3\}}
=\frac1{\sqrt6}\begin{pmatrix}0&1\\1&0\end{pmatrix}
\]

with one positive and one negative eigenvalue. Both input matrices are PSD; their difference is indefinite. Consequently they are **not** related by an isometry preserving their labeled feature vectors, nor by an everywhere-positive correction. More generally any nonzero Hermitian matrix with zero diagonal cannot be PSD (Cauchy–Schwarz or the 2×2 principal minor). The convex continuum
\(K_\theta=(1-\theta)K_D+\theta K_A\), \(0\le\theta\le1\), is PSD, normalized, multiplication-invariant, and agrees on every comparable pair—yet its cross-prime pair (2,3) varies with θ. This is an exact *non-uniqueness under prime-jet-only observations* countermodel.

Hence the SUCC/FUCC source must specify cross-prime data, topology, and the correct trace/test transport. One-dimensional prime-jet covariance and positivity are not enough to identify the global arithmetic form.

## MOG-03. Natural logarithmic prime energy and conditional positivity (CLASSICAL/PROVED)

Write \(v_p(n)\) for the exponent of p dividing n and set
\[
d_D(m,n)=\sum_p|v_p(m)-v_p(n)|\log p
=\log\frac{mn}{\gcd(m,n)^2}.
\]
This is the weighted \(\ell^1\) valuation metric, nonnegative and multiplication invariant. Then \(K_D(m,n)=e^{-d_D(m,n)/2}\).

The *unrestricted* PSD kernel
\[
G(m,n)=\log\gcd(m,n)
=\sum_{p,k\ge1}(\log p)\,\mathbf1_{p^k\mid m}\mathbf1_{p^k\mid n}
\]
has the exact positive quadratic
\[
\sum_{i,j}\bar c_i\,G(n_i,n_j)c_j
=\sum_{p,k\ge1}(\log p)\left|\sum_{i:p^k\mid n_i}c_i\right|^2\ge0.
\]
Each finite test contains only finitely many contributing primes and powers, so there are no convergence assumptions.

Since \(\log K_D(m,n)=G(m,n)-(\log m+\log n)/2=-d_D(m,n)/2\), for every **zero-sum** finitely supported vector \(c\) the row/column terms vanish, and
\[
\boxed{
-\frac12\sum_{i,j}\bar c_i c_j\,d_D(n_i,n_j)
=\sum_{p,k\ge1}(\log p)\left|\sum_{i:p^k\mid n_i}c_i\right|^2\ge0.
}
\]
Thus d_D is conditionally negative definite and **log K_D is conditionally positive definite**: its off-diagonal entries are negative, yet its quadratic is nonnegative on the natural zero-sum difference subspace. This is a source-derived sum of squares, not a tautological GNS factorization of the completed Weil form. The zero-sum condition here is not asserted to equal the Mellin/pole-vanishing test conditions in Weil's criterion.

### Exact prime-power amplitude

Along a genuine p-ladder,
\(K_D(1,p^k)=p^{-k/2}\) and \(d_D(p^k,p^{k+1})=\log p\). Consequently
\[
d_D(p^k,p^{k+1})K_D(1,p^k)
=\frac{\log p}{\sqrt{p^k}}
=\frac{\Lambda(p^k)}{\sqrt{p^k}}.
\]
This recovers the **magnitude** of the correct von Mangoldt weight from one prime-FUCC step and the normalized carrier overlap. At n=6, the single-prime-stratum projection excludes an illegitimate log(6) prime jet. The required signed Weil distribution, the Gamma/poles/contact, and the measure of its complete test space are **not** reconstructed by this product identity.

## MOG-04. The real-log-topology discontinuity (PROVED)

There is a sharp distinction between the two otherwise compatible PSD completions. The real-log chart sends n+1 over n to
\(t_n=\log((n+1)/n)\to0\). But because gcd(n,n+1)=1,

\[
K_D(n,n+1)=\frac1{\sqrt{n(n+1)}}\to0,
\qquad
K_A(n,n+1)=\sqrt{\frac n{n+1}}\to1.
\]

On \(\mathbb Q_{>0}^\times\), the multiplication-invariant divisor kernel is a positive-definite function \(F_D(a/b)=1/\sqrt{ab}\) for coprime positive a,b. The sequence \((n+1)/n\to1\) in the **ordinary real** topology, but \(F_D((n+1)/n)\to0\ne F_D(1)=1\). Therefore **there is no continuous positive-definite function on the real additive log-line whose restriction to log Q_{>0} equals F_D**. Conversely \(K_A(m,n)=e^{-|\log(m/n)|/2}\) has this real-log continuity.

This does NOT preclude an adelic or other topology retaining prime valuations; it refutes an unqualified one-dimensional Archimedean-continuity identification of the bare divisor kernel. SUCC's unit-successor \(n\mapsto n+1\) supplies a decisive source-differentiating probe: near-neighbors are close in real-log chart but arithmetically coprime.

## MOG-05. Weil/Suzuki/Connes transfer remains a separate, falsifiable obligation (UNVERIFIED)

The positive source kernels act on finitely supported coefficient sequences indexed by integers, not automatically on the full Schwartz–Bruhat/Weil test space. The already-authenticated full completed Weil source contains **signed prime-power impulses plus the one real Gamma, pole/contact**, and the claimed equality
\[
B_{\rm source}(f,g)=W(f*\widetilde g)
\stackrel{?}{=}\langle Jf,Jg\rangle_{\mathcal H_{\rm mult}}
\]
for one declared source-built map J on ALL admissible tests is unproved. If J is defined only by declaring the Gram of W positive, the construction is circular; if J discards cross-prime or identity/contact information, the equality can fail while both auxiliary kernels stay PSD. The 2/3 contrast, successor near-neighbor discontinuity, and 6 false-prime mutation are mandatory probes.

This package sharpens the earlier draft Connes interface. The next serious gate is a **source-typed all-place test-transport map** between SUCC/FUCC (with both successor and prime actions) and the canonical Connes scaling trace, preserving exact contact and the original Weil functional. A bridge that matches only p^k amplitudes but not the (2,3), (n,n+1), Gamma or pole terms fails. A full source-equal noncircular positive factorization would be RH-level progress, not an implication from the elementary lemmas here.

### Exact executable receipts / independence

- observ​ational_succ/multiplicative_orientation_gram.py: separate integer factorization, totient divisor sums, interval indicator quadratics, explicit signed valuation energies and zero-sum mutation, symbolic log-prime weights without floating transcendental tests.
- tests/test_multiplicative_orientation_gram.py: independent exact source/feature evaluations, cross-prime indefinite difference, chain invariance, discontinuous near-neighbors, fake p=6 projection and wrong-domain mutants; independent cross-oracle to observational_succ/connes_oriented_scaling.py.
- Python tests are finite calibration of stated proved identities, not their proof. An isolated local run passed ten purely arithmetic groups; an additional integration cross-oracle needs the authentic previous branch module, so only CI on the **exact final GitHub head** can certify integrated execution. Record its actual status rather than assuming success.

**Citations / provenance:** Smith's classical GCD matrix determinant (1876) and later GCD Gram theory; Connes–Consani *Weil positivity and Trace formula: the archimedean place*, arXiv:2006.13771 (restricted Sonin-compressed scaling positivity); prior SUCC O1–O8 dossier research/2026-10-15/ONE_OBJECT_TATE_WEIL_SUZUKI_CONNES.md and COT-01–08. **New academic priority NOT asserted. RH PROVED: NO.**
