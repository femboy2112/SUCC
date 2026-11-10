# Validation scope and reproducibility

**29 focused tests PASS:** root5, observer8, arithmetic10, crucible6.
The root [runner](validate.py) executed11 commands successfully; all three
replayed oracle payloads match their retained receipts exactly. The mandated
provenance, observer-foundations and ordinal probes all pass. Command lines,
exit statuses, durations and log hashes are in [validation/SUMMARY.json](validation/SUMMARY.json).

The native12,147-test suite passed in the immediately preceding round at
`525d7c87dd1016aeeea4ac9cd1366cbb935a0441`. **It was not rerun this round.**
The runner verifies that tests, scripts, observational_succ, formal,
provenance, docs and AGENTS.md have no changes against that head. Its prior
receipt hash is retained in the new validation summary. This carries forward
the validation of unchanged native inputs; it is not a new full-suite or CI
claim. The optional `--native` flag performs a new full run if needed.

## New mathematical checks

- Full mixed-quadratic source scan:38,878,562 coefficients at h1,3. An
  independent full replay after input guards produces identical mathematical
  payloads; only the code hash changes. Both receipts and the exact guard
  diff remain under [arithmetic](arithmetic/VALIDATION.md). No float enters
  the budget certificate. Error radii and signed-int64 range bounds are proved.
- Separate70-digit interval implementation:14 coefficient probes including
  extrema and prespecified pairs,7,714 direct terms, all contained in the
  integer instrument's balls. This shares the source boxes but not the
  transform or transcendental evaluator.
- Separate-agent arbitrary-precision contractions match483 small-field
  NumPy matrix outputs. Arithmetic tests add155 direct full small spectra,
  165 weighted supports,606 off-diagonal tomography pairs,3,000 affine
  exponent checks and90 higher-moment collision fibers. The later MQ1b
  review independently checks10 additional collision cases/252 tuples.
- Observer source oracle:12 finite p/h cases,792 unwrapped recurrence/carry
  checks,396 actual principal parts,198 nonzero first-moment closures,
  186 chronology-radius certificates,372 exact phase cocycles and600 exact
  forcing-difference bounds. The small primes are clean clocks, not claimed
  to satisfy the stronger all-epoch selector.
- Clock quotient oracle:153 exact orbit-character identities,720 canonical
  rank-one identities,90 twisted-coboundary checks,408 equivariant matrix
  checks,11 asymmetric controls, and50 exact cycle potentials. Missing-twist
  and wrong-shift mutants are rejected. Four source replays certify26,324
  linear Fourier coefficients and the signed orbit sums, with explicit
  circularity warnings in every result.
- Root energy oracle:120 critical points in the preregistered multiplier
  list,4,093 strictly positive outward grid checks,8 existing source-energy
  cases,5,344 exact de Bruijn word counts and6,875 periodic digit matches.
  Separate-agent critical-point and all-prefix normality proof reviews
  accept RE1–4; independent finite Euler-circuit counts supplement the proof.

All new source measurements use existing/development finite windows.
**There is no fresh-source holdout in this round.** Prespecified coefficient
probes test the new instrument; they are not independent source data.
The paper's infinite results use proofs, not numerical extrapolation.

## Reproduce

From the repository root, with the existing environment:

```sh
/tmp/succ-learning-yoneda-venv/bin/python research/2026-11-08/frontier_connections/validate.py --output /tmp/succ-frontier-replay
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 /tmp/succ-learning-yoneda-venv/bin/python research/2026-11-08/frontier_connections/arithmetic/mixed_quadratic.py --source research/2026-11-08/complement_budget/results/source_1103.json --output /tmp/succ-mixed-quadratic.json
python research/2026-11-08/frontier_connections/manifest.py
```

The complete scan stays on one arithmetic worker and does not need a new
dependency installation. Source files and earlier receipts are immutable.
The [manifest](ARTIFACT_MANIFEST.json) checks every retained artifact except
itself and Python caches. No new Lean proof was attempted; existing formal
source is unchanged. Hosted CI status is reported separately on the PR.

## Review corrections and failure history

The observer one-bit claim was restricted to its declared two-assignment
fiber after root review. The normal control explicitly starts with digit0
to guarantee its same-forcing seed differs from zero. The arithmetic scanner
received additional integer-index and input-range guards; its complete
replay was unchanged. A crucible import-name collision was fixed before
source computation and is documented in its local validation note. No failed
mathematical source measurement was silently discarded.

Review receipts pin the exact version read. Later documented wording/guard
changes are not retroactively attributed to an earlier proof hash. Final
artifact hashes and the starting Git pin supply the durable final scope.
Internal agents share a model family and repository. These are cross-checks,
not external scholarly refereeing. Pi normality: OPEN. RH: OPEN.
