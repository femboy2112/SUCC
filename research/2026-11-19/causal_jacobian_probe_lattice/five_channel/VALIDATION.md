# Executed validation and claim boundary

**Date:** 19 November 2026. **Source baseline:** Main XXVI
`81be6b897ae980b801a3b9de9e22ef81e8360bfb`. **Parent draft head:**
`966f789b6523a4918b24e96fac7bc22cd791fb79`. The only remote write before the
fresh signed experiment was its preregistration commit
`099e36d0c7fd3e53f4fb35ccfbceb5066b357e2b`.

## Required repository gates

All four AGENTS.md commands were executed in the full-history local checkout:

| Command | Observed result | Receipt |
|---|---|---|
| `python scripts/verify_provenance.py` | PASS:72 source items,17 byte-identical archives,55 mechanical namespace migrations | receipts/provenance.log |
| `PYTHONPATH="$PWD" python -m unittest discover -s tests -p 'test_*.py'` | 14,476 tests; no failures or errors;2 skipped; exit0 | receipts/full_unittest.log |
| `python scripts/observer_foundations_probe.py` | exit0; stated open mathematical obligations retained | receipts/foundations.log |
| `python scripts/ordinal_succ_report_probe.py` | exit0; finite/ordinal and open-positivity boundaries retained | receipts/ordinal.log |

The full root suite ran while the new isolated research files were being
developed. No imported source, production module, root test, or workflow was
modified by this follow-up. The new research tests below were rerun after their
final code changes. The suite result is not mislabeled as hosted CI on the final
Git commit. The two skips remain skips. No new Lean or external-referee result
is claimed.

## Final focused and independent checks

- `five_channel/test_observer.py`: **30 test methods passed**, exit0. Includes
  source-family and seed recovery, preserved history, future-clock rejection,
  source/seed mutations, determinant and Smith oracles, sharp precision controls,
  universal odd-prime repair, the bounded common clock schedule, bad-start
  congruences, and real measurement-unit accounting.
- `five_channel/independent_audit.py`: **2,313 exact finite checks passed**,
  exit0. Uses independent combined-source, cofactor/adjugate, minor-GCD,
  finite-field, full-angle Taylor, and source-prefix calculations. It verifies
  the all-clock lattice examples and the explicit binary ambiguity. Detailed
  case data are in receipts/independent_audit.json and its execution log.
- `five_channel/observer_receipt.py`: exact original coefficients
  `(4,-2,-1,-1)` and seed0 recovered; history retained; common future clocks
  `(236,237,238,239)` produce integer determinant524288. Full finite input and
  precision receipts are in receipts/observer.json.
- `five_channel/*.py`: `py_compile` passed.
- Inherited `probe.py` and `sheet_probe.py`: both replayed successfully. The
  first now explicitly asserts the already computed order pair at29.
- `git diff --check`: passed before publication.

The independent audit is another implementation and decomposition within the
same model family. It is not an independent external academic referee. Universal
claims rely on the displayed algebraic proofs, not on the number of tested cases.

## Preregistered signed finite experiment

The six-mode configuration was committed before the fresh source run. It fixes
every index in `[131073,262146)`, all signs and frequencies, precision, and
finite thresholds. The source run used262185 original source terms to certify
a262161-digit hexadecimal prefix by outward integer arithmetic. The exact prefix,
its SHA-256, signed rational intervals, and config hash are preserved.

Every tested mode passed its declared **finite** modulus threshold1/16; the
mode1 finite real threshold15/16 also passed. The results appear in
receipts/signed_weyl.json, with a separate raw-source tail payment. They are
observations on this one shell only. The earlier source horizon through131072
was treated as consumed data. The new shell is now consumed as well.

The source run was not tuned by changing the thresholds or rejecting samples.
Later algebraic improvements to the repair planner do not change the frozen
signed configuration. The prefix and report do not establish any estimate on
an untested shell, any positive liminf, R0, or normality.

## Repairs and rejected interpretations retained

The audit corrected the previous233-to147 modulo11 repair, the two-lag bank's
255-point blind subgroup, squared-energy reflection loss, the unsupported
out-of-source description of29, and the distinction between a spatial pulse
resolvent and chronological BBP dynamics. It also replaced the requirement that
all faithful local observers must unlock: an exact causal stationary frame is
now a required positive control.

Prior conversational execution claims are not needed as evidence. The present
logs and hashes provide the replay receipts. The characteristic polynomial and
terminal-observer identities retain their inherited credit. A missing Claude
artifact is not treated as proof provenance.

## Remaining limits

The complete source-observation lattice is now proved, including its fixed-
precision binary plateau. This is a source-channel result; the fifth terminal
channel and stronger priors can refine those fibers. Row clearing rescales real
errors, and seed authentication has its own precision cost.

The missing arithmetic statement is a uniform signed estimate on the actual
zero-seeded chronological source. **R0 and base-16 pi normality remain OPEN.**
Finite source reconstruction, exact Jacobians, coherent frames, and all passing
finite checks do not replace that estimate.
