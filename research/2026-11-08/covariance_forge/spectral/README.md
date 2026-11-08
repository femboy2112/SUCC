# Spectral covariance forge

The complete derivations are in `THEOREMS.md`.

**New unconditional supporting bound.** For the original zero-seeded source,
choose the deterministic prime p_A from the previous PE theorem. Its local
character cancels uniformly against every linear temporal tone and, for each
fixed degree d, every real polynomial temporal chirp. This follows from
source-exact finite differences and the already imported BK subgroup bound;
no new exponential-sum import is hidden.

**What this can certify.** If the complementary factor admits a sufficiently
accurate temporal Fourier/chirp model whose coefficient variation grows slowly
enough, then the actual real Weyl mean tends to zero. A cycle-folded sparse
model has a more economical certificate: replica-orthogonal history components
contribute exactly zero. Shift-invariant learned predictor spaces are Fourier
subspaces and receive the same bound. Arbitrary learned subspaces do not.

**Hostile result.** PE14's shadows have the same cancelled prime signal and
maximal real coherence. For every sparse support with s_A beta_A^2 tending to
zero, their best folded-complement approximation error tends to one. Thus the
strong local theorem cannot manufacture the missing complement regularity.

Validation completed:

* exact unwrapped four-pole source and local-prime checks;
* formal root-of-unity multiset equality for the cyclic autocorrelation
  rearrangement, independently implemented from rational source states;
* exact polynomial-difference phase checks through degree four;
* exact Gaussian-rational Hilbert projections, covariance decomposition,
  cycle folding and sharp sparse-error controls;
* seven explicit negative controls and six regression tests, all passing.

`EXACT_RECEIPT.json` counts 42,371 algebra terms/instances, including 39,648
terms included in the formal autocorrelation comparisons. These are finite
validation counts, not 42,371 independent mathematical assertions or a kernel
certificate. The cases are fixed implementation checks, not preregistered
asymptotic holdouts. No floating arithmetic enters this oracle.

Reproduce from this directory:

```sh
python oracle.py
python -m unittest -v test_spectral
```

The root's separate interval sparse-spectrum probe was reviewed in
`ROOT_PROBE_REVIEW.md`; this agent did not rerun its larger computations.
Source and local-input hashes are in `PROVENANCE.json`.

Original complement approximation/covariance: **OPEN**.
π base-16 normality: **OPEN**. RH: **OPEN**.
