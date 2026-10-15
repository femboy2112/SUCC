# RH candidate handoff — source-real prime-clock UV positivity (DYSPON-SPHERE I)

**Date:** 2026-10-15. **Status:** PROVED ANALYTIC in restricted test domain (conditional on authenticated source normalization), new to SUCC; RH PROVED: NO. **Origin:** SUCC research branch \`research/tate-prime-clock-uv-transducer-2026-10-15\`, stacked on APOLLO PR #110 exact parent \`cb7b804d8624dcf5247eac34cf59e969577c6ccb\`. **Main is unchanged.** This handoff is a candidate only; it is NOT a publication or an update to the separate RH repository.

## What is actually provided

The original Suzuki/Weil test form on \(f\in C_c^\infty(-a,a)\), retaining one real Gamma, genuine von Mangoldt prime powers \(\Lambda(n)n^{-1/2}\), original contact, both polar terms and the correct half-density, has the following exact source representation:

\[
Q_\zeta(f)=
\sum_{j\ge0}\frac4{4j+1}\langle f,(I-R_{(4j+1)/2})f\rangle
-C_\infty\|f\|^2
+8|\langle f,s'\rangle|^2-8|\langle f,h'\rangle|^2
-\sum_{n=p^k:\log n<2a}\frac{\log p}{\sqrt n}
 \langle f,(S_{\log n}+S_{-\log n})f\rangle,
\]
where \(R_\alpha\) convolves with \(\frac\alpha2e^{-\alpha|t|}\), \(s'=\frac12\cosh(t/2)\), \(h'=\frac12\sinh(t/2)\), and \(C_\infty=-\psi(1/4)+\log\pi\). This is DYS-01, derived from the original APOLLO K2/K3 source decomposition and classical Weil/Suzuki identities, NOT new Tate continuation.

**Quantified theorem (DYS-04):** Every \(0<a\le1/2\) and every nonzero complex \(f\in C_c^\infty(-a,a)\) with Lebesgue measure of support \(\le1/16\) satisfies
\[
\boxed{Q_\zeta(f)>\frac1{24}\|f\|^2.}
\]
At a=1/2 the *true* first Euler place n=2 is active. The exact source certificate consists of:
- Source proof \(C_\infty<43/8\), \(2/3<\log2<7/10\), \(\log3>1\), true \(w_2=\log2/\sqrt2<1/2\); genuine source labels (2), fake n=6 forbidden.
- Sharp compressed source shift path bound \(\|P_I(S_b+S_{-b})P_I\|=2\cos[\pi/(\lceil2a/b\rceil+1)]\); on the first prime window it is <=1.
- Original negative polar bound \(2(\sinh a-a)<1/16\).
- **Exact 16-rung original real Gamma coercivity** from \(\|1_E R_\alpha1_E\|\le\alpha |E|/2\):
\[
Q_\Gamma(f)\ge \bigg[\sum_{j=0}^{15}\frac4{4j+1}-16\cdot\frac1{16}\bigg]\|f\|^2 .
\]
- Source-negative budget <95/16, leaving exact positive rational margin
\[
\frac{18140507408283703}{386282620694770800}>\frac1{24}.
\]

This is a **universal restricted-cone theorem**, not finite Gram sampling. It does NOT establish all-tests positivity, any enlarged all-a contraction, the conjectural global Suzuki spectral limit, or RH.

## Adversarial controls

- Original-shaped rational synthetic clock b=3/4, a=1/2, four anchored samples: signed prime-only energy -1/4, Brownian energy 1/4, exact relative negative -1. This REFUTES positive-per-prime and naive window-norm continuity.
- Fake composite 6 cannot be inserted into the original \(\Lambda\) source; true p=2 is required and checked against immutable source.
- Omitting real Gamma, changing contact, wrong pole sign, losing \(\sqrt n^{-1}\), or transporting the odd conductor-3 character without changing its Gamma/conductor/parity invalidates the authentic source passport.
- Tiny-support theorem is not dense in unrestricted test space. Any assertion of global positivity from it is rejected.

## How RH research can use it

1. Use DYS-01 as a reference operator/energy decomposition to reconstruct **true** first-prime low/high Suzuki source matrices in the existing PR #107/#109 residual Schur program. Preserve the original signed high-sector relative Neumann metric.
2. Derive a **coupled gamma-prime endpoint microlocal Schur bound** that quantifies cross-interactions between the small support channels (now certified positive) and the delocalized low-sector source. This is the natural candidate new transducer.
3. Attempt a source-compatible APOLLO positive/negative feature contraction across every genuine clock birth, with paired-neutral gluing; the all-tests all-a statement is exactly RH-strength and UNVERIFIED.
4. Independently develop the full Tate Schwartz–Bruhat to signed Weil distribution bridge; use chi(-3), wrong contact and non-Euler mutations as discrimination probes.

## Reproduce and source

Mathematics: \`research/2026-10-15/TATE_PRIME_CLOCK_UV_TRANSDUCER.md\`.
Source code: \`observational_succ/tate_prime_clock_uv.py\`.
Tests: \`tests/test_tate_prime_clock_uv.py\`.
Frozen receipt: \`research/2026-10-15/TATE_PRIME_CLOCK_UV_RECEIPT.json\`, run \`python scripts/tate_prime_clock_uv_probe.py --verify\`.
CI: \`.github/workflows/tate-prime-clock-uv.yml\`, inherited exact original source/provenance gate and Python 3.10/3.13.

**Primary imports:** Suzuki, arXiv:2606.09096v3, especially §1 Weil and §2 screw calculus; Tate's original thesis; Connes–Consani arXiv:2006.13771 only as a restricted comparator. Academic priority unverified. The scoped quantitative theorem is not a published independent peer-reviewed result.

**Missing theorem:** a truly original-source all-test positivity/contractive Hilbert realization for every finite observation window. **RH PROVED: NO.**
