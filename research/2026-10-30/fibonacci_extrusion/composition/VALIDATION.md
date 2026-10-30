# Validation actually executed

Worktree SUCC-fibonacci-extrusion, parent7b5a2b4534aa5e71865046ca8d3f723d8002b9fe.
All front changes are additive under composition/. Original source and seed
are untouched. Python3.12.3, mpmath1.2.1, SymPy1.12; no installs.

- Final focused unittest run: **12 PASS**,11.975s. Earlier11-test run also
  passed and is preserved; it is not counted again. Final extra test covers
  the source-clock theorem added after the initial pass.
- Exact logarithm-interval probe: **8 fresh (k,a) rows**, k13,21,34,55 and
  a19..705; all positive and inside the uniform error band. Parent partial
  fractions and range-reduced rational logarithm routines are explicitly
  reused with512 terms. This is not an independent implementation.
- Separate100-digit positive Frullani oracle: all8 intervals checked;
  **3 fresh joint-rank holdouts** k89,233,987; **4 native Jensen gaps**;
  exact symbolic Gamma Laplace identity and normalization;39 matrix-power
  Fibonacci identities. Numerical integrals are calibration, not rigorous
  quadrature or universal proof.
- Exact source-clock probe: **12 rational inequalities**; separate SymPy
  factored-transform derivative implementation checks all12 and also
  **12 Gamma controls**. The all-weight classification rests on the paper
  mgf-threshold proof, not this finite census.
- Root-clock complementary review: **3 fresh exact quadratic-field aggregate
  families** and **5 exact product identities**; separate160-digit finite
  aggregate residuals below1e-133. Reviewed hashes retained.
- A coarse but rigorous rational interval puts the Gamma memory Jensen gap
  between0.135 and0.137. The longer displayed decimal is separately numerical.
- Reciprocal Fibonacci constant enclosure uses80 exact terms and an explicit
  two-parity tail. This is a finite certificate of that constant, not a
  selected arithmetic distribution certificate.

No mathematical/test execution failed. Two exploratory reads used guessed
filenames absent from the parent directory, and the prior Fibonacci dossier
was absent from this checkout; it was read using its existing immutable Git
commit instead. These were read-only lookup errors, not concealed test failures.
Full native/provenance/foundations/ordinal/hosted checks are owned by the root
campaign and must not be inferred from these focused receipts.

Run focused tests from repo root:

    python3 -m unittest discover -s research/2026-10-30/fibonacci_extrusion/composition -p 'test_*.py' -v

The producer/oracle scripts refuse to overwrite existing result JSON. Use a
fresh copied directory or preserve existing receipts before rerunning to a
new output location. The manifest excludes itself and its own audit log to
avoid hash cycles. Every source input, script, dossier and raw output is pinned.
