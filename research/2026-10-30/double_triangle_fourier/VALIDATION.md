# Two-triangle Fourier validation and truth status

Base: merged SUCC Main XVI `e18ba565ca540adb7edf3292f5593929e76d91c5`; research complement to draft PR #390. All original source/seed formulas pinned in mathematical dossier.

## Executed evidence

- `python two_triangle_fourier_probe.py -v`: **18/18 standalone standard-library exact-Fraction tests passed** (original four-pole source, exact finite posterior joint, Vandermonde, hypergeometric split, nonzero source covariance, exact q6 primitive 36×36 ring inversion, mixed local stencil, first two-variable 59-jet and fake difference, clock conservation, even/odd opposing kernel, coherent constant phase, exact original zero-seed interior carry/phase register, rational seed variants and aliases). Tests are scoped, not universal proof certificates.
- Separate independently authored `independent_oracle.py`: SymPy exact verification of the two-variable polynomial/one-variable legacy slice/59 difference, separate exact 36×36 symbolic group-ring inverse, and 75-digit mpmath integrals at 3 generic `(z,w)` points and native `n=30,90,270`, including independent fake-source comparisons. All assertion checks passed.
- Initial research probe was computationally inefficient (`source_coeff` recomputed up to O(n^3) times); fixed via exact input memoization and bounded high-n Fraction workloads. Two **false TEST expectations** were corrected: the bilateral geometric tail missed a factor 2, and the doubled-clock golden-root difference has negative, not positive sign. Both did *not* change the mathematical source conclusions. Exact subsequent 18/18 passed.
- Native broad SUCC CI, Lean kernel, hosted PR checks, external peer review and publication-priority audit: **NOT EXECUTED** on this research head.

## Scope firewall

- The conditional shared-X observer is declared, although the source marginal and its finite rational moments are authentic BBP objects.
- `J,K` are auxiliary grades; neither their joint law nor 2D Fourier char function measures empirical frequencies of pi's digits.
- Source-specific 59 first jet, q6 covariance, clock-locus conservation and exact intermediate-carry labels are mathematically distinct; no selected unsigned/unnormalized Weyl saving is claimed.
- No physical entropic heat, gauge holonomy, or random BBP digit generation is inferred.
- The one remaining signed gate is `Σ_(n<=N) exp(2π i h U_n(0))=o(N)` (equivalent normalized average `o(1)`), for every fixed nonzero integer h; it is OPEN.
