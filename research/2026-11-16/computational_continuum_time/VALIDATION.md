# Validation and proof authority

- Exact source algebra, solenoid-prefix compatibility, integer deck-shift equivalence and all winding formulas have elementary paper proofs in THEOREMS.md. The degree obstruction and mapping-torus suspension use standard topological constructions, not a finite computation.
- The path-metric integer-shift enclosure is derived by exact integration by parts. Simpson quadrature in the probe is labelled numerical calibration, not a sound interval certificate.
- Gamma alpha=1 high-time attenuation is derived by integration by parts, and general alpha by the Riemann–Lebesgue lemma; it is a decisive nonnormal control, not a statement about π.
- Independent source consistency uses exact fractions and a Machin alternating-series enclosure of geometric π, rather than comparing double-precision endpoints at near-machine tolerance.
- One **initial local test failed** solely because `float(lo)<float(pi)` compared two distinct exact numbers rounded to the same binary64 value. We preserved `INITIAL_TEST_LOG.txt`. The corrected test uses independent *exact rational* Machin enclosures and passed in the subsequent run. No analytic statement or source input was adjusted to make the test pass.
- `python -m unittest -v test_continuum_probe.py` and `python continuum_probe.py` are the focused research runs. These are not the full SUCC repository gates.
- No Lean proof, GitHub Actions result, independent external referee or source-specific all-shell Fourier bound is claimed by this dossier.

## Local test execution record

- `python -m unittest -v test_continuum_probe.py` — **19 tests, PASS, zero failures** on the corrected source. `TEST_LOG.txt` retained.
- `python continuum_probe.py` — deterministic exact rational source and numerical metric diagnostics. `PROBE_OUTPUT.txt` retained.
- `python independent_audit.py` — **95 exact arithmetic/symbolic checks and 11 high-precision diagnostics**, PASS. No imports from `continuum_probe.py`. `INDEPENDENT_AUDIT_LOG.txt` retained.
- `python -m compileall -q continuum_probe.py test_continuum_probe.py independent_audit.py` — PASS.
- Independent SciPy weighted oscillatory quadrature versus mpmath incomplete Gamma — absolute differences <4e-13 for t=0,1 in the explicit alpha=1 control, not interval-certified.
- Original failed local probe and first algebra-audit expression-tree mismatch retained in `INITIAL_TEST_LOG.txt`, `INITIAL_INDEPENDENT_AUDIT_LOG.txt`, `CALIBRATION_HISTORY.md`.
