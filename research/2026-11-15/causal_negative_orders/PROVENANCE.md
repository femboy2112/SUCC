# Provenance and distinct analytic objects

## Pinned repository state

- Repository: `femboy2112/SUCC`.
- Parent draft: [#637](https://github.com/femboy2112/SUCC/pull/637).
- Exact parent commit: `55bcde3d0c5ceb47d50cb499bd39f4a97c96bfc5`.
- Parent tree: `4989f6e4e6a0357ea881d49c2c6abb117032f8d7`.
- New work branch: `research/causal-negative-orders-2026-11-15`.
- The working tree was clean before creating this branch. Only additive
  files are intended; existing source, archives, tests and defaults are
  preserved. Required provenance validation is reported separately.

The initial fresh GitHub frontier check found #637 and parallel #636
unchanged. A final check discovered concurrent #638, which was read and
reviewed as recorded below. No result is based solely on a prior
conversational summary.

## Inherited objects inspected

All blob hashes below refer to the pinned parent.

| File | Git blob | Actual inherited content |
|---|---|---|
| `research/2026-10-24/EULER_MASCHERONI_BBP_REGULATOR.md` | `7c71ff98012f8becc93768b0cb3d54c18961f8a2` | Entire four-ray Lerch family for `|z|<1`; original pi at `s=1,z=1/16`; three-positive-difference representation; regulator-one boundary defect |
| `observational_succ/euler_bbp_regulator.py` | `22b5fe976dc16a8945c2b72f5acaa77f0970fd44` | Exact finite source/refinement and positive exponent instruments; the family is not introduced anew here |
| `research/2026-10-29/recursive_carrier_triangle/ATOMIC_SOURCE_AND_INTERACTIONS.md` | `3d946c186b07a14d352912a6b18bfef48c0e8027` | Literal source factorization over `Q(sqrt(241))`, positive Levy density, Gamma/compound-Poisson convolution roots and coherent subdivisions |
| `research/2026-10-30/universal_nz_carrier/ZETA_NEGATIVE_INTEGER_TANGENT_FAMILY.md` | `b4665e5700cab6d80e3cff6229ba0bc913478693` | Universal Pascal/Hasse faces, finite negative-integer value truncation, surviving analytic tangents, and the classical reflected prime-product tangent |
| `observational_succ/bbp_dirichlet_resolvent.py` | `37621406adae7853455621e70289d50bf78ab57c` | A *different* chronology Dirichlet response `sum r(n)n^-s`, source shifts, Bernoulli values and pole data |
| `observational_succ/bbp_gamma_kernel_algebra.py` | `9ce17c3b3d9b471fe5fc6c56ca527bcc68028035` | Complete signed kernel for integer convolution powers, endpoint jet cancellations |
| `research/2026-11-15/bbp_volume_algebra/THEOREMS.md` | `359cd4b7002c30090417b6958add138cfc59c315` | VA-01--09: original Laplace source, Gamma(2j) kernels, graded causal products, polynomial/phase distinction, carry and convergence domains |
| `research/2026-11-14/gamma_volume/THEOREMS.md` | `881436b8b3648e0bab271dadf9e4e16d2c3e199f` | Ordered volume and tempered conjugacy; retained-source depth laws and report-descent conditions |

Also inspected: the universal-N carrier's UN-05--07, the existing
`zeta_minus_one_transport.py`, `gamma_dirac_continuum.py`, and
`origin_locked_oily_zeta.py`. Their finite carrier, regulator and
two-sided Gamma-clock results are retained as provenance, not counted
as new theorems or evidence for an actual physical clock.

## Concurrent #636

Read-only draft [#636](https://github.com/femboy2112/SUCC/pull/636),
head `397eec34c3637c876ab4e4f71f7c9a5359f75535`, supplies the original
finite-difference faces and their `Gamma(k+2)/(64 n^(k+2))` asymptotic.
Its source path is `research/2026-11-14/causal_volume_rewrite/THEOREMS.md`,
blob `b916ec3a447517a24d497d0be514b321d5ba3145`. CN-06 derives the exact
map to those faces, while CN-08 takes a different limit in `k`.
That branch's code and test counts are not imported or included here.

## Concurrent #638 discovered before publication

[Draft #638](https://github.com/femboy2112/SUCC/pull/638), head
`582e6bea90268b58262ac0f32e6ab23bfaae1951`, is a child of #636.
The root retrieved and read
`research/2026-11-14/causal_suspension_gamma_zeta/THEOREMS.md`, blob
`2e91d846250c55fb62b462a80ae814cd36ba1d23`. Its declared odometer
suspension supplies a literal continuous forward path to embedded
negative arithmetic coordinates and a positive Gamma concentration
law. It shares the classical signed negative-Gamma and Pascal/Hasse
ingredients, and compares the Gamma face coefficient with the zeta
trivial-zero slope. Our [review appendix](CONCURRENT_SUSPENSION.md)
preserves those types and credits the companion. No source or test is
silently imported; its 19 reported tests are excluded from our counts.

## Classical primary references checked

1. Epstein and Morava, *Tempering the Polylogarithm*,
   [author paper](https://arxiv.org/pdf/math/0611240), p.2 and the
   distributional continuation construction. The divided-power family
   is entire in its order and realizes fractional differentiation.
2. Li and Liu, *A Generalized Definition of Caputo Derivatives and Its
   Application to Fractional ODEs*, SIAM J. Math. Anal. 50 (2018),
   2867--2900, [author PDF](https://sites.math.duke.edu/~jliu/pdf/Li_Liu_SIMA_2018.pdf),
   Lemmas 2.2--2.4 and Proposition 2.5: causal real-order convolution group.
3. Hilfer and Kleiner, *Fractional calculus for distributions* (2024),
   [author PDF](https://www2.icp.uni-stuttgart.de/~hilfer/publications/fractional-calculus-for-distributions-Hilfer.pdf),
   equations (5.2)--(5.3), defines the same distributions and negative
   integer derivatives. No uninspected regularization formula from the
   review is used; the proof is written out in CN-01 and CN-04.
4. Flajolet, Gourdon and Dumas, *Mellin transforms and asymptotics:
   Harmonic sums*, [author PDF](https://algo.inria.fr/flajolet/Publications/FlGoDu95.pdf),
   Theorem 3, and [corrigenda](https://algo.inria.fr/flajolet/Publications/mellin-harm-corr.pdf).
   CN-04 uses only the elementary endpoint-power case, with explicit
   subtractions and no inverse-mapping theorem assumed.
5. NIST DLMF [5.2](https://dlmf.nist.gov/5.2),
   [5.9.2](https://dlmf.nist.gov/5.9#E2),
   [2.6](https://dlmf.nist.gov/2.6): Gamma poles/reciprocal zeros,
   Hankel contour, distributional derivative and fractional integrals.
6. NIST DLMF [25.5.1](https://dlmf.nist.gov/25.5#E1),
   [24.2](https://dlmf.nist.gov/24.2),
   [25.6](https://dlmf.nist.gov/25.6): positive zeta Mellin kernel,
   Bernoulli generating function/parity, negative integer values.
7. NIST DLMF [20.7.32](https://dlmf.nist.gov/20.7#E32),
   [25.5.13--14](https://dlmf.nist.gov/25.5#E13),
   [25.4](https://dlmf.nist.gov/25.4): Gaussian theta inversion and the
   completed zeta reflection law. This is a specified lattice source,
   not a consequence of the BBP Gamma endpoint.
8. NIST DLMF [25.14](https://dlmf.nist.gov/25.14): Lerch family and its
   regulator domains; [25.11](https://dlmf.nist.gov/25.11): distinct
   Hurwitz boundary at regulator one.

## Novelty and independence accounting

The generalized functions, Gamma/Beta algebra, zeta parity and positive
BBP convolution semigroup are classical or already in SUCC. The new
source interface includes explicit negative-depth inverses and endpoint
atoms, the full real-zero classification of causal faces and convolution
powers, and the normalized growing-face reciprocal-Gamma limit.
Some are transparent corollaries of the inherited formulas; none is
presented as a new special function or academic priority claim.
The late search also recovered the universal Pascal/Hasse negative-order
ladder. CN-09 explicitly reuses it and adds a comparison with the same
grade averaging on the authentic BBP faces, whose value at -2 is 8.
It does not claim to introduce causal-face zeta continuation into SUCC.

The constructor, adversary, translator and root used different
decompositions and code paths. They are same-model agents with shared
source provenance, so their agreement is not four independent empirical
witnesses. The independent audit avoids production imports; separate
symbolic checks and mutation controls constrain implementation errors.
All universal assertions rest on the stated paper proofs. Numerical
quadrature is diagnostic unless a separate rigorous bound is given.
