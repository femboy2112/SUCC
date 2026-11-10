# Spectral front: audit, finite-memory bandwidth theorem, and cancellation boundary

Read `THEOREMS.md` for the complete proof and `SOURCE_READ_AUDIT.json` for
the exact source heads and file hashes. All input branches were read-only.

**Surviving result.** #543's `341/sqrt(205)` sharp half-aperture ×16
constant is correct on real law differences with full translated coherent
profiles. The two-tone first-order inverse and cross-channel realization
criterion reconcile with #541's B2 instrument and #542's positive moments.

**New local theorem, SP-3.** For the continuum of initial probability laws,
exact Fourier observations of bandwidth H at every time through N leave
worst-case future two-tone prediction error
`Theta(sqrt(min(b^k/H,1)))` after k further ×b steps, uniformly in the
finite memory depth N and in the known common forcing. Positive Fejer-law
pairs give explicit indistinguishable histories; the upper estimator is
explicit Fourier truncation. Unlimited retained finite history cannot
remove this precision cost. A restricted finite source family or a known
singleton initial state is a different inference problem.

**Original-source boundary.** No new source-selected signed decay bound
was obtained. Same-forcing wrong seeds satisfy the operator, naturality,
and transport theorems while failing Haar. History-refinement positivity
controls conditional energy, not the needed global signed cancellation.

Validation performed in this run:

* 15,495 exact rational checks in the standalone independent oracle;
* six explicitly rejected shortcuts/mutations;
* seven new local regression tests;
* exact-head focused source replays: #541 31 tests, #542 21 tests,
  #543 32 tests, all exit 0.

The source replays use `git archive` extractions into `/tmp`, not cached
binaries. They are focused suites only. Their test algorithms were written
by the prior same-model research stack; passing them is not independent
scholarly verification. The new oracle imports none of those implementations
and independently counts squared Fourier-amplitude pairs. Its checks are
finite and do not certify the general theorem or any asymptotic statement.

Reproduce the new checks from this directory:

```sh
python independent_oracle.py
python -m unittest -v test_spectral
```

Paper proof, exact finite checks, source implementation replays, and open
π-normality debt are separate outputs. No kernel theorem is claimed here.
