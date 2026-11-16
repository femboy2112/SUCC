# Provenance and novelty boundaries

## Exact source state

This additive research round starts from draft [#635](https://github.com/femboy2112/SUCC/pull/635), commit **`e14d46c17a65e1e5f231c619657b9332caa181c0`**, on local branch `research/bbp-volume-algebra-2026-11-15`. It inherits #633 through #635. The parallel [#634 Gamma Genesis](https://github.com/femboy2112/SUCC/pull/634) was read in the previous round and is acknowledged by #635; its code is not silently merged here. This round adds two production modules and two test modules. It does not change the original forcing, initial condition, imported archives, existing module contents, or main.

The source is always the literal four poles

`4/(8n-7) - 2/(8n-4) - 1/(8n-3) - 1/(8n-2)`, `n>=1`,

with `U_0=0` and `U_n=16U_(n-1)+r(n)`. Changed seeds, removed poles, all-positive residues and coherent prime-root sequences are explicitly labelled controls. They are not counterexamples to a theorem whose hypotheses fix the original source.

## Inherited mechanisms

| Existing source | What is inherited | What this round adds or clarifies |
|---|---|---|
| [Four-pole atomic substrate](../../2026-10-26/FOUR_POLE_ATOMIC_SUBSTRATE.md), especially §§2–4 | Exact reduced kernel, signed quadratic atoms, harmonic integration and source labels | The forcing-power inverse-Laplace compiler with 4j pole/order slots |
| [Oily source Mellin/Hilbert](../../2026-10-26/OILY_MACARONI_SOURCE_MELLIN_HILBERT.md) | Positive signed exponential source, q'(0)=15, q''(0)=-59, Gamma(2) endpoint | All integer convolution powers, exact cancellation of low jets, and a normalized Gamma(2j) envelope bound |
| [Universal N/Pascal/Gamma/Zeta](../../2026-10-30/universal_n_carrier/UNIVERSAL_N_PASCAL_GAMMA_ZETA.md), UN-06/09 | Rational potential, finite Gamma quotient, authentic multiplicative carrier and marked initial derivative seed | These are used as provenance; no claim to rediscover the Gamma product lift |
| [Summation snapshot arrows](../../2026-10-30/summation_snapshot_arrows/README.md), SA-04 | Inclusive ungraded Rota–Baxter rule of weight -1 | Retain the changing radix, source labels and seed terms in a finite word compiler |
| [Pascal/carry joint](../../2026-10-29/pascal_carry_joint/README.md), and earlier rational-filter carry obstructions | Literal original carries; difference between a declared probabilistic coupling and deterministic selection | Exact general affine carry composition and minimal coordinatewise moduli for Gamma-weighted lift phases |
| [Prime-birth strictness](../../2026-11-02/pisot_gamma_gluing/PRIME_BIRTH_STRICTNESS.md), PG-09 | At a fresh first-pole prime, no rational linear sum ending with a nonzero newborn phase can vanish | Extension to a fixed number field, then algebraic coefficient descent: no eventual recurrence over C(n) |
| [BBP graph resonance](../../2026-11-10/bbp_graph_resonance/RESEARCH_NOTE.md), R-02/03 | Finite holonomic source descriptions and infinite radix-decimation span | The distinct, stronger obstruction for the actual phase sequence; no rebranding of source holonomicity |
| [BBP Gamma matrix deformation](../../2026-11-09/bbp_gamma_matrix_deformation/THEOREMS.md), SGM-05 | Native q-Gamma radix blocking | Explicitly distinguished from continuous-lag Gamma convolution |
| [Gamma volume](../../2026-11-14/gamma_volume/THEOREMS.md), GV-02–06 | Gamma/Beta causal semigroup, bounded-operator filter, conditional source retention and projection defect | A raw-BBP domain test, exact tempering threshold 15, and the unique unstable-mode subtraction below that threshold |

The ordinary symmetric-power lift, partial fractions, convolution, Beta normalization, quasi-shuffle/Rota–Baxter framework, Mellin integration by parts, Ore shift relation and cyclotomic degree formula are classical. The new research product is a source-preserving assembly, explicit source consequences, and bounded executable certificates. Academic novelty of any mathematical corollary is **UNVERIFIED**.

## Pinned inherited Git blobs

All hashes below are read from the exact parent commit, not inferred from filenames.

| Path | Git blob SHA |
|---|---|
| `observational_succ/bbp_natural_carrier.py` | `74174890efe630ddccff430a371fd9bf0874fd31` |
| `observational_succ/bbp_dual_jets.py` | `c4709e11ac50ffe87dd98a458dddeea671a7cac9` |
| `research/2026-10-26/FOUR_POLE_ATOMIC_SUBSTRATE.md` | `d843637c6c0e7d58484508010aaa6faa1324b13e` |
| `research/2026-10-30/universal_n_carrier/UNIVERSAL_N_PASCAL_GAMMA_ZETA.md` | `07adce91a544ddccdfba14e8a3369b736cefa0a2` |
| `research/2026-11-02/pisot_gamma_gluing/PRIME_BIRTH_STRICTNESS.md` | `93fd3e88564970ece996e24f1e717a1984f671d2` |
| `research/2026-11-10/bbp_graph_resonance/RESEARCH_NOTE.md` | `a8b76d5b4cf7f07e936e05247e3c08587b6c04ff` |
| `research/2026-11-14/gamma_volume/THEOREMS.md` | `881436b8b3648e0bab271dadf9e4e16d2c3e199f` |
| `research/2026-10-29/pascal_carry_joint/README.md` | `c28f21b7313658cc18f142f30e77fcd4698b1c6f` |

## Primary external references consulted

1. Bailey, Borwein and Plouffe, [*On the rapid computation of various polylogarithmic constants*](https://www.davidhbailey.com/dhbpapers/digits.pdf), Mathematics of Computation 66 (1997), 903–913. Theorem 1 and the rational integral establish the original BBP source identity.
2. NIST DLMF [§5.2](https://dlmf.nist.gov/5.2), [§5.9](https://dlmf.nist.gov/5.9#E1), [§5.12](https://dlmf.nist.gov/5.12#E1), and [§1.14](https://dlmf.nist.gov/1.14). Euler Gamma, the scaled Laplace integral, Beta convolution and transform conventions; their convergence hypotheses are retained.
3. Wang, Zhang, Zhu and Chen, [*Free nonunitary Rota-Baxter family algebras and typed leaf-spaced decorated planar rooted forests*](https://www.degruyterbrill.com/document/doi/10.1515/math-2020-0059/html), Open Mathematics 18 (2020), 1173–1184, introduction equation (2). This is the established family identity instantiated by the graded Green operators.
4. Hoffman, [*Quasi-shuffle products*](https://arxiv.org/abs/math/9907173), Journal of Algebraic Combinatorics 11 (2000), 49–68; Hoffman and Ihara, [*Quasi-shuffle products revisited*](https://arxiv.org/abs/1610.05180), Journal of Algebra 481 (2017), 293–326. Context for iterated-sum product algebras. The specific radix-labelled recursion is proved explicitly in the local notes; no free universal property is inferred merely from the name.
5. Kauers, Jaroschek and Johansson, [*Ore Polynomials in Sage*](https://arxiv.org/pdf/1306.4263), §2. The noncommuting shift and multiplication rule is standard. This reference is mathematical provenance, not a claim about the current Sage package version.
6. Conrad, [*Cyclotomic Extensions*](https://kconrad.math.uconn.edu/blurbs/galoistheory/cyclotomic.pdf), Theorems 2.5 and 3.4; Sharifi, [*Algebraic Number Theory*, Chapter 3](https://math.ucla.edu/~sharifi/notes/algnum-ch03.html), Proposition 3.1.14. Cyclotomic irreducibility and field degree are the classical input to the fresh-prime proof.
7. Guo, Gustavson and Li, [*An algebraic study of Volterra integral equations and their operator linearity*](https://arxiv.org/pdf/2008.06756), Theorem 2.9 and Example 2.12. Context for continuous separable exponential integral kernels. The finite-interval product used here is also proved directly from its differential equation.

## Independence and source-map limits

The constructor, adversary and translator began with separate methods and then exchanged their identities and controls. Their mathematical source is shared, and the agents belong to the same model family. Their agreement is not independent empirical evidence or external peer review.

The independent finite scripts import neither new production module. The kernel tests compare local Laurent coefficients with a global polynomial identity, direct Beta-convolution jets, and a separately implemented SymPy partial-fraction calculation. The root reruns the scripts and selected suites and reviews the proof obligations; these routes check different implementation/decomposition errors on the same source.

No source/observer identification is asserted merely from matching Gamma marginals. No analytic bound for the selected temporal Weyl sum is asserted by any finite receipt. The same-forcing coherent counterseed remains a diagnostic for seed-blind reasoning, not a refutation of the canonical zero-seeded problem.

## Concurrent draft #636, inspected before this publication

During this round a separate continuation of #634 appeared as [draft #636](https://github.com/femboy2112/SUCC/pull/636), **`397eec34c3637c876ab4e4f71f7c9a5359f75535`**, based on `8b1673036fa624c3b2e9e43d67bddcbae7f44b86`. Its [theorem dossier](https://github.com/femboy2112/SUCC/blob/397eec34c3637c876ab4e4f71f7c9a5359f75535/research/2026-11-14/causal_volume_rewrite/THEOREMS.md), blob `b916ec3a447517a24d497d0be514b321d5ba3145`, was fetched and read at that exact commit. The remote file list and PR body were also inspected.

That draft gives a generic polynomial-Mellin/radix normal form, reconstructs the same Oily kernel, and develops the authentic finite-difference faces

`(-1)^k Delta^k T_n = integral x^(8n)(1-x^8)^k R(x) dx`,

whose fixed-k endpoint shape is Gamma(k+2). It also proves an explicit moving-Mellin character bound and retains source/phase countermodels. Those are complementary to the **convolution power** shape Gamma(2j) here: taking a finite difference and multiplying forcing values are different operations. A common Gamma shape does not identify their full kernels or clocks.

The elementary source-volume identity in VA-05 overlaps CV-01 and older Green work; it is not claimed as a separate discovery. This round's radix-graded word product, 4j-slot forcing-kernel compiler, C(n) phase nonrecurrence and exact tempering/lift-modulus rules provide a different operation-level extension. The #636 implementation is not in this branch's ancestry, was not run here, and its reported 29 tests and numerical comparisons are **not included** in this round's validation totals. No merge between the two research branches is performed.
