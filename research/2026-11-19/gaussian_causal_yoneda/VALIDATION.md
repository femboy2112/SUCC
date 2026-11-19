# Validation receipts — Gaussian causal Yoneda

Date: 2026-11-19. Base main: `81be6b897ae980b801a3b9de9e22ef81e8360bfb`.

## Actually executed in isolated local working directory

```
python -m unittest -v test_gaussian_causal
Ran 22 tests in 0.024s
OK
```

Additional focused controls: exact mean/variance energy split; one-sided
polarity run-length bound; complete late-phase alias; stationary-delta versus
uncertainty-heat distinction; phase-only magnitude blindness; high-harmonic
blindness of a fixed finite probe set.

Test groups: exact canonical four-pole recurrence; exact rational BBP finite tail;
strict rational tail polynomials; exact five-parameter affine Jacobian;
exact five-clock determinant `32768/17039726835256125`; exact covariance
identities; Gaussian constants and 501-grid R0 inequalities; independent
2048-bin circle quadrature of spectral V; mean-vs-mean-energy distinction;
mode-by-mode Gaussian discrepancy; four finite source-prefix transfer checks;
source-pulse n^-4 asymptotic; s=-x locked control; s+1/16 phase alias;
co-moving Gaussian seed-width compensation; exact circle heat Fourier
transport; high-frequency inverse-instability control.

The scripts use only Python stdlib. The finite spectral functions evaluate
ordinary floating-point exponentials/trigonometric functions: their displayed
finite values are **calibration, not rigorously outward-rounded intervals**.
All universal inequalities in PROOFS.md are justified by the paper derivations,
not by sampling the tests. A future adversarial interval implementation should
certify truncation and rounding bounds before claiming numerical shell certificates.

## Not run or not claimed

- Repository-wide `python scripts/verify_provenance.py`, root 14k+ tests,
  `scripts/observer_foundations_probe.py`, `scripts/ordinal_succ_report_probe.py`:
  not available in the isolated sandbox and **not claimed**.
- Hosted GitHub CI on the final draft branch: status pending/unverified.
- Independent proof assistant/Lean verification, external mathematical referee:
  NOT done.
- All-late-shell original source-specific signed Gaussian cross-correlation
  lower bound, R0, full pi normality, RH: NOT proved.

## Independent symbolic arithmetic audit (executed)

A second SymPy implementation, independent of the stdlib source functions,
verified the exact rational reduction of r(n), both strict tail-bound
polynomials, the five-clock determinant, and full source-Jacobian rank for
clocks 1 through 5, 6 and 7. All assertions passed. This validates symbolic
algebra against a second implementation; it is not external peer review.

Changes remain research-only and additive; no original/source/provenance
mutation is implied. Independent symbolic arithmetic cross-checks, when
executed, should be recorded separately and not conflated with the base suite.
