# Source map and literature audit

## Immutable SUCC inputs

All reads below used parent commit `ad19e3794f1d8da4a81418d38a4fc731b7d355c7`, root tree `69b41162ba80a7004862c9b7d28b302157ed8043`. The verified main head was `b763ba8ef375fbac221e29e4396989a635a6ef36`. PRs #344 -> #346 -> #347 -> #348 -> #349 form the relevant inherited research chain. Other open work, including #350 and #351, is not modified or claimed as integrated by this branch.

| Input | Git blob | Used for |
|---|---|---|
| `AGENTS.md` | `2c04a24744366d5659f347caeb874a3613f893c9` | Governing source, theorem, and validation constraints |
| `CONTRIBUTING.md` | `dd8d49b347edaecd79fc52e11aee6325c0d712eb` | Evidence and draft-research discipline |
| `docs/METHOD.md` | `c3d90e9fe0cff7bc56b7a896a9efb87958849aa3` | Steelman, crucible, verdict |
| `research/2026-10-28/pisot_relativistic_geometry/RECONSTRUCTED_FIXED_POINT_PISOT_BRIDGE.md` | `ea67c71ee425a451368419f622838932ebb7975d` | Actual auxiliary Pisot machinery and its source boundary |
| `research/2026-10-28/ORIGIN_LOCKED_OILY_ZETA_FRAME_DOSSIER.md` | `f3676bc153c87743c9f6dbaa274f89420cb90fd3` | OLZF-04 source fibers, marked embedding, local overlap and character; lines 88-154 inspected |
| `research/2026-10-28/POLYA_COHERENCE_RIGIDITY.md` | `fbaa9a46f2112d28761298b7d339a6f03dab1d90` | PCR-01/02 accepted channel, leakage and spectrum; lines 1-122 inspected |

The last two inherited claims were additionally rederived at the finite-map level: factor-split counting versus valuation formulas, and channel Gram subtraction versus weighted path Laplacians. This is mathematical/implementation triangulation, not independent human review. No imported file is rewritten, and no historical proof ID is promoted.

## Primary external sources checked on 2026-10-28

**[S1] NIST Digital Library of Mathematical Functions, section 27.4, Euler Products and Dirichlet Series.**
https://dlmf.nist.gov/27.4
Used for the classical Euler-product/multiplicativity background and its absolute-convergence domain. The connected prime-power and Mobius primitive formulas are explicitly derived in RESEARCH.md, rather than claimed as new results.

**[S2] Frederik Broucke, Athanasios Kouroupis, Karl-Mikael Perfekt, A note on Bohr's theorem for Beurling integer systems.** Mathematische Annalen 389 (2024), 4319-4333; online 14 November 2023.
https://doi.org/10.1007/s00208-023-02756-x
Full HTML introduction and theorem context inspected. This is relevant prior art for generalized-prime perturbations, not a theorem being directly imported. Its definition assumes rational independence of the logarithms. Our exact 11/29 collision violates that hypothesis; our labeled multiplicity proof is therefore supplied independently. No priority claim for small Euler perturbations is made.

**[S3] Brad Rodgers and Terence Tao, The de Bruijn-Newman constant is non-negative, arXiv:1801.05914, version 5 (2021), originally 2018.**
https://arxiv.org/abs/1801.05914
https://terrytao.wordpress.com/2018/01/19/the-de-bruijn-newman-constant-is-non-negativ/
Primary paper abstract and author exposition inspected for heat deformation, interacting-zero dynamics, and the scope of the local-equilibrium argument. No claim that their theorem proves RH or identifies a one-prime/one-zero pairing. We use an independent two-zero polynomial calibration of the motion equation.

**[S4] Titus Hilberdink and Michel L. Lapidus, Beurling Zeta Functions, Generalised Primes, and Fractal Membranes, arXiv:math/0410270.**
https://arxiv.org/abs/math/0410270
Generalized-prime/zeta background only. No theorem requiring hypotheses unverified for our clock system is imported.

**[S5] GitHub Docs, Skipping workflow runs.**
https://docs.github.com/en/actions/how-tos/manage-workflow-runs/skip-workflow-runs
Official operational reference: `[skip ci]` skips push/pull_request-triggered workflows, not every possible event (not pull_request_target), and skipped required checks may remain pending. No global workflow setting is changed.

## Dependence and ablations

The SUCC dossiers are one ancestry family, not three independent sources of truth. The exact Fraction implementation and SymPy implementation differ in algebraic representation, but were written by the same reasoner. The mpmath probes share that reasoner and are not independent proofs. The literature is background and constraint evidence, not validation of the specific new synthesis.

Removing the numerical family leaves all paper proofs intact but removes computational corroboration. Removing the quadratic-Pisot assumption leaves the zero-divisor theorem true for rational `p+1/p`, exposing that the analytic mechanism is small logarithmic displacement. Removing original arithmetic labels breaks source reconstruction at the exact 11/29 collision. Removing source coefficient checks lets the fake-4 generator pass the zero-divisor comparison. These are distinct ablations, not a single truth score.

The earlier conversation's claims of specific prior computations are not reused as executed evidence. All reported local results in this folder come from the current scripts and preserved receipts. Neither the earlier conversation nor a previous PR's passing CI is counted as this branch's validation.
