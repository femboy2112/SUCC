# Signed finite-prime / Laplace complement spectrum

**π base-16 normality remains OPEN.** This note turns the authentic #558 prime product into an exact signed time-frequency overlap. The finite Fourier transformation itself is classical; the new-to-SUCC element is its source-faithful combination with #554's balanced p-local prefix estimate and the Laplace critical source analysis.

## LCS-06 — Exact source-labelled Cauchy/DFT overlap

Fix a genuine original-zero BBP epoch n=A,...,2A−1, and an admissible p as in #554. For j=0,...,A−1 let

\[
a_j=e\big(h[U_{A+j}]_p\big),\qquad
b_j=\prod_{q\ne p}e\big(h[U_{A+j}]_q\big).
\]

The p and q parts are the canonical rational additive-adelic fractional parts from #558, including every active odd prime and its unit residue. **Exactly** \(a_jb_j=e(hU_{A+j})\). For τ≥0 set \(b^\tau_j=e^{-\tau j/A}b_j\). With normalized temporal DFTs

\[
\hat a(k)=A^{-1}\sum_{j=0}^{A-1}a_j e(-kj/A),\qquad
\hat b_\tau(k)=A^{-1}\sum_{j=0}^{A-1}b^\tau_j e(-kj/A),
\]

orthogonality yields the exact signed overlap

\[
L_{A,h}(\tau)=A^{-1}\sum_{j=0}^{A-1}e^{-\tau j/A}e(hU_{A+j})
=\sum_{k\bmod A}\hat a(k)\hat b_\tau(-k).
\]

Equivalently \(L_{A,h}(\tau)=A^{-1}[w^0]A_p(w)B_\tau(w^{-1})\) for the finite phase polynomials, with full chronological labels intact. This is a Cauchy/Hadamard pairing, NOT a product of marginal Laplace transforms and NOT a probabilistic independence statement.

### An exact conditional low/high spectrum gate

Assume the actual four-stage p-local prefix estimate imported from #554, \(\max_{m\le A}|\sum_{j<m}a_j|\le A E_A\), \(E_A\to0\), under its exact prime-order, frequency and stage hypotheses. Summation by parts gives for representative \(|k|\le A/2\),

\[
|\hat a(k)|\le E_A(1+2\pi|k|).
\]

For \(0\le K<(A-1)/2\), decompose the signed overlap into \(|k|\le K\) and \(|k|>K\). Parseval plus Cauchy–Schwarz gives

\[
|L_{A,h}(\tau)|
\le \sqrt{2K+1}\,E_A(1+2\pi K)
+\left(\sum_{|k|>K}|\hat b_\tau(k)|^2\right)^{1/2}.
\]

Thus, for a fixed nonzero h, a **NEW** all-epoch, original-zero complement estimate with some K_A→∞, \(E_AK_A^{3/2}\to0\), and complementary high-time-frequency energy o(1), would imply \(L_{A,h}(\tau)\to0\). This sufficient condition is stronger than necessary and is **UNVERIFIED**.

More generally, the desired theorem would directly force the SIGNED high-high cross sum
\(\sum_{|k|>K}\hat a(k)\hat b_\tau(-k)\to0\), which allows large high-frequency power in each factor. This is the spectral form of the same outstanding forcing-corrected prime/complement covariance from #544/#554. Exact reconstruction and positive Parseval energies do not establish it.

For every sequence of unit phases and every τ≥0,

\[
|W_A(h)-L_{A,h}(\tau)|\le\tau/2.
\]

Hence proving the signed Laplace overlap tends to zero for every fixed h≠0 at a sequence of positive τ_j↓0, **each with its own all-A bound**, would force the original fixed-frame Weyl limit. This is a conditional bridge, not a proof of its premise.

### Decisive controls

Choose \(a_j=e(j/A)\) and \(b_j=\overline{a_j}\): each unweighted marginal can have zero mean, but their pointwise product is 1 and the τ-weighted product mean is positive. Factorized marginal Laplace analysis therefore fails decisively.

The genuine zero-seed complement is also not demonstrably low-frequency. Exploratory PRESEEN double-precision exact-rational-source data with τ=0, h=1, K=8 give the complementary high-mode power:

| A, p | high complement power | |W_A(1)| |
|---|---:|---:|
| 32, 73 | 0.34023 | 0.06239 |
| 80, 193 | 0.79427 | 0.14211 |
| 192, 457 | 0.92733 | 0.06927 |
| 320, 769 | 0.93762 | 0.05868 |

The high-mode energy gate is numerically unfavorable at these finite clocks, but this does NOT refute the all-A asymptotic. The SIGNED overlap, not absolute high energy, remains the more credible research target.

## Verdict and next decisive proof

The finite-place data authentically reconstruct *each individual* real phase. The Laplace transform reorganizes the time-domain multi-prime nonconspiracy question into a signed spectral matching question; it does not solve that matching.

Prove a genuine zero-selected bound for the high-high cross spectrum using exact stage births, the old odd-prime cofactor, and #544's integer carry observer. Must fail for coherent irrational wrong-seed and epoch-dependent rational dyadic shadow controls. No all-epoch source-selected signed decay established in this branch; **π NORMALITY OPEN**.