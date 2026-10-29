# Validation and verification limits

**Parent pin:** PR #354 at 6adf1a74e3d85355ee94f0087b27e2c3b7f125d8. Inherited original PCR-02 and OLZF-04 unchanged.

- Local standard-library unittest: 10/10 methods pass, covering exact Fraction native and controlled transitions (40 depths), source martingale, bounded tilted occupation, rational Hellinger identity, both KL asymptotics, complex character zero-line residuals and static biased two-path hostile control.
- Independent SymPy oracle (does not import primary library): 35 symbolic identity checks pass, 12 native and 12 controlled transport checks plus 11 Pólya geometric boundary-defect checks.
- Standard compileall passed.
- Initial oracle assertion compared algebraically equal expressions using structural equality and failed; replaced by simplify(lhs-rhs)==0. The repaired oracle passed. It was a test-structure issue, not a theorem failure.
- Mathematical global claims rely on the explicit proofs and classical Pólya/data processing results, not extrapolation of finite tests.

**Not run/claimed:** complete GitHub checkout/full root AGENTS provenance+native+observer+ordinal gates, hosted CI, Lean, rigorous float intervals, independent external reviewers. Local complex residuals are observations, while Fourier zero roots are derived algebraically. One reasoner produced the implementations. Commit is [skip ci] to avoid CI fan-out, **not** a CI pass. Main untouched; no workflow changes. RH and pi normality OPEN.
