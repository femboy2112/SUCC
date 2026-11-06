# Operation PAULI × FEKETE: orbit exclusion that is actually sufficient for equidistribution

**2026-11-05, research-only**, strict additive child of [SUCC #512](https://github.com/femboy2112/SUCC/pull/512) at exact parent \`effbd923578a160ddbb792265a6a5ed311ff342f\`. Original four signed BBP forcing terms, literal U0=0, true integer/rational carries, historical source/Lean/proof contracts, archives, production, licenses, CI workflows and main are **immutable**. No merge, tag, publication or novel physical Pauli exclusion claim.

## Mission and known development derivations (NOT blind holdouts)

The user proposes an orbit analogue of Pauli exclusion: a nontrivial source-constrained mechanism preventing persistent phase alignment. Classify two mathematically exact candidates:

(A) Finite-dimensional Fourier frame: \(v_M(x)=M^{-1/2}(1,e(x),\dots,e((M-1)x))\). The empirical \(M\times M\) operator \(S_{N,M}=N^{-1}\sum_n v_M(x_n)v_M(x_n)^*\) is positive, trace 1. Its Hilbert–Schmidt purity is \(1/M+(2/M^2)\sum_{h=1}^{M-1}(M-h)|c_N(h)|^2\). Saturating the minimum \(1/M\) is **equivalent** to vanishing of those modes, not a new source-derived estimate.

(B) Antisymmetric/Fekete determinant: for \(z_n=e(x_n)\),
\(\Delta_N=\det(z_n^j)_{j=0}^{N-1}\), \(|\Delta_N|^2=\prod_{i<j}|z_j-z_i|^2\le N^N\).
Define \(\mathcal E_N=N^{-2}\log|\Delta_N|^2\), \(-\infty\) if phases repeat. For \(N\ge2\), \(r=1-1/N\),
\[
\boxed{\sum_{h\ge1}(r^h/h)|c_N(h)|^2\le-\mathcal E_N+
(1-1/N)\log(2/(1+r))+\log N/N.}
\]
These formulae were DERIVED INTERACTIVELY BEFORE preregistration and must not be labelled blind. The inequality is a direct, all-N comparison between the regularized positive Fourier logarithmic kernel and the actual pairwise Vandermonde energy. Consequently \(\mathcal E_N\to0\) implies Weyl equidistribution; it is a **strictly stronger sufficient condition**, not necessary (a normal sequence can contain sparse exact or exceptionally close repeats).

Classical Fekete potential theory is not novel: see E. Saff, *Logarithmic Potential Theory with Applications to Approximation Theory* https://www.math.vanderbilt.edu/saffeb/texts/230.pdf and Fekete/equidistribution work https://doi.org/10.1007/s00208-024-03088-0 .

**Development controls already explored:** uniform Nth roots \(\mathcal E_N=(\log N)/N\) and \(c_N(h)=0\) for 1≤h<N; N equally spaced points on a half-circle have distinct points separated by 1/(2N) but \(|c_N(1)|\to2/\pi\) and \(\mathcal E_N\to-7\zeta(3)/(2\pi^2)\). The quantitative positive-kernel inequality held at N=8,16,32,64,128 in an independent finite numpy calculation. These values are DEVELOPMENT, not fresh holdouts.

## Exact prospective tests not yet run

1. Use the original zero-seeded BBP recurrence from exact rational taps, and an independent collapsed four-pole rational numerator/denominator oracle. For source epochs \(A=9,17,33\), \(n=A,\ldots,2A-1\), preserve unwrapped Fractions, reduce phase differences exactly before any float trig.
2. Same-original-forcing coherent wrong seed \(s_*=-\pi/16\): compute the coherent orbit *without π digits* as \(-T_n=-\sum_{k\ge1}16^{-k}r_o(n+k)\) using a bounded rational future tail (at least 40 terms) and a rigorous analytic upper bound on omitted tail. It must cluster within O(A^-2), giving \(\mathcal E_A\le-2\log A+O(1)\) for ALL sufficiently large A, not just observed A.
3. For each source epoch, compare independently computed \(c_N(h)\) for h=1,2,3; the frame purity formula for M=3,5,9; and the regularized Fourier kernel bound with r=1-1/N. For the positive kernel, compute either the exact pairwise K_r sum or enough explicit Fourier terms with a geometric remainder bound; do NOT claim the truncated positive series equals the infinite sum without tail bound.
4. Fresh negative controls: 17/33-point half-circle grids and roots of unity; minimum spacing versus global half-circle nonuniformity; compare normalized log determinant and low-mode occupancies.
5. A possible *source-specific* sufficient theorem must prove \(\mathcal E_A^{\rm original}\ge-o(1)\) for the authentic selected sharp A-epoch, or an independently useful finite-mode source-frame inequality. The existing #501 microscopic collision count does not entail this multiscale energy lower bound; no such proof is claimed.

## Why the analogy is falsifiable

Pauli antisymmetry alone forbids identical occupied one-particle vectors, NOT nonuniform empirical distribution. Slater determinant under saturation over ALL N modes gives an actual equidistribution certificate, but this is far stronger than pairwise distinctness and not automatically tied to the original SUCC source. SUCC's actual arithmetic phases are rational roots of unity of growing, different conductors; invoking Galois norms or determinant integrality across conjugates cannot control the SINGLE SOURCE-SELECTED Archimedean embedding without a new inequality. A frame/Slater formulation that simply renames the open Weyl sum is category B, not a signed advance.

## Validation and claims

All mathematical statements require exact domains, proofs, source/seed controls and positive/negative finite checks; no global inference from finite computations. The first work action is this preregistration, before fresh A=9,17,33 tests. Keep full 11k+ CI from blocking research; run focused tests, preserve source, open draft PR. Base-16 normality of π, original selected fixed-h Weyl, and original critical maximal subinterval saving remain OPEN.
