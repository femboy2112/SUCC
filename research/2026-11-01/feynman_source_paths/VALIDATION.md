# Exact validation and authority boundary — Operation Feynman

**Source state**: `femboy2112/SUCC` Main XVIII `4eb411e3730a9e7b95480369a438b89d9a433a4b`, stacked on SUCC PR #443 exact SHA `00ba302898a8c81d3dbea0f4dd29f541a0f3d158`; original BBP four poles and U0=0 preserved. The literature supports general metaplectic/time-slicing instruments; proofs F-01–F-06 are derived for this exact solvable specialization.

## Executed in this current container

```sh
python -m unittest discover -s /mnt/data/succ_feynman_lab/tests -p 'test_*.py' -q
# Ran 48 tests in 0.047s — OK

python -m unittest discover -s /mnt/data/succ_feynman_integration/tests -p 'test_*.py' -q
# Ran 276 tests in 0.646s — OK
```

The **276-test local research proxy** combines actual unmodified released-in-chat ZIP snapshots for draft PRs #438, #439, #440, #441, #442, #443, and this new research package. It is **NOT** the complete >10k SUCC repository and cannot replace hosted CI or full provenance, observer and ordinal scripts. Each script is loaded under a unique file-based import identity to avoid cross-package oracle collisions.

**Source and algebra probes (exact Fraction)**: original four poles vs independent combined rational expression for 159 indices; source positivity and odd denominators; zero seed and rational seed covariance; ordered affine product checked against independent convolution; selected action increments; original noncommuting first two source steps; exact Fresnel covariance `C_N`, direct sum and independent recurrence; stationary `x,p` equations and quadratic action at multiple exact endpoints; distribution half-density Jacobian; fourth-root rational substep flow; bandlimited spectral error rational coefficients and uniform N-bound; Gaussian initial width / Gaussian-Wick point-regulator resolution; same-source rational-completed q=1/5 coherent counterfeit and tail; Gaussian two-order overlap attenuation and signed phase formula; bad-input cases fail closed.

**Independent symbolic check actually run**: SymPy source combination, original two-step affine commutator, N=1 stationary quadratic action, simple Fourier exponent identity. Output: `INDEPENDENT_SYMPY_AUDIT_PASS`, `r1=47/15`, `r2=106/819`, commutator `12301/273`. This is a different symbolic implementation of the same source, not blind scholarly refereeing.

**Independent numeric diagnosis actually run**: optional `finite_probe.py` integrates the complex Gaussian packet overlap with 60-decimal mpmath quadrature, comparing to analytic completion-of-square formula at sigma=1/8,p0=3,hbar*=2. Absolute discrepancy `8.01817165639e-62`. This is a finite numerical agreement, **not** a proof of the infinite-dimensional path integral; that is the analytic Fourier/operator derivation in PROOFS.

**Analytic proofs (paper only)**: (i) L2 unitarity via substitution and strongly continuous group, (ii) finite path distribution by Fourier delta, (iii) exact Gaussian Fresnel integration and source-order covariance, (iv) uniform spectral bound by Plancherel, (v) the wavepacket/point-source counterseed, (vi) Gaussian two-order interferometer overlap by completing the square. No new Lean kernel receipt or external independent referee is claimed.

## Explicitly unverified and forbidden promotion

- Full `python scripts/verify_provenance.py`, full root `unittest` suite, observer-foundations probe and ordinal probe on the latest complete Git checkout are **NOT RUN** here; local `git ls-remote` failed with container DNS unavailable, so the available GitHub connector is used for pinned source reads and additive research writes.
- No claim of a universal infinite-time Feynman path probability measure; our real-time object is a **tempered oscillatory distribution** and exact unitary operator. No claim of a physical implementation or that the BBP arithmetic has nontrivial quantum alternatives by itself.
- No kernel check of analytic results; no independent external peer review.
- **π normality and RH remain OPEN**. Source-specific all-horizon signed Weyl saving has NOT been proved.

## Recommended GitHub exact-head gates

```sh
python scripts/verify_provenance.py
python -m unittest discover -s tests -p 'test_*.py'
python scripts/observer_foundations_probe.py
python scripts/ordinal_succ_report_probe.py
```

Check actual PR-head CI before merging. Keep branch draft; no source archive/production or proof authority mutation.
