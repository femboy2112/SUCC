# Validation and repair record

**Scope:** additive research code and proofs on Main XXV base
`db9fb4b84672050efa79b13377f1e73364598a14`. The saved exact arithmetic
receipts and source-code hashes are in
[VALIDATION_RESULTS.json](VALIDATION_RESULTS.json).
An arithmetic theorem is established by its stated proof and hypotheses;
passing these finite checks does not independently establish it.

## Repository baseline and integration

The complete pre-existing native suite was discovered before the new
boundary-filter loader was added. Its run completed successfully:

| Required command | Observed result |
|---|---|
| `python scripts/verify_provenance.py` | PASS, exit zero |
| `python -m unittest discover -s tests -p 'test_*.py'` | 13,050 tests, OK, exit zero |
| `python scripts/observer_foundations_probe.py` | PASS, exit zero |
| `python scripts/ordinal_succ_report_probe.py` | PASS, exit zero |

[Baseline metadata](receipts/baseline.json) and the original logs
([native suite](receipts/native_suite.log),
[provenance](receipts/provenance.log),
[observer](receipts/observer.log),
[ordinal](receipts/ordinal.log)) retain the actual results. Existing
invalid-escape `SyntaxWarning`s in three unrelated modules were emitted
by the baseline; no test failed. Those pre-existing modules were not edited.

The **71 new focused tests** passed separately, with warnings treated as
errors. They also passed through
`python -m unittest discover -s tests -p 'test_holographic_boundary_filters.py'`.
That new loader makes them part of future ordinary repository discovery.
This is a baseline plus a separately executed addition, not a claim that
a single final 13,121-test full-suite invocation was observed.

The deterministic mathematics catalog was regenerated for the added source
documents, then checked. Its 172 existing namespace warnings are identical
to the base catalog; this round adds none. The curated relationship-graph check is a syntax
and dependency lint, not a mathematical proof audit. Final command results
are saved in [final_checks.json](receipts/final_checks.json), with associated
logs in that directory.

## Focused suite

| Area | Named tests | Material risks checked |
|---|---:|---|
| Ordered realization | 14 | Positivity, Gram invertibility, basis-word consistency, exact closure, hidden directions, chronological phase, all 127 short words, contraction scope and metric conditioning |
| Phase and targets | 20 | Exact row-span witnesses, dual uncertainty, cyclotomic Fourier identities, equal-power and equal-triple aliases, finite torsion, near-Haar conditioning and strict rational input contracts |
| Goldbach moment filters | 14 | Valid grade cap, signed intervals, counterfeit moments, direct primality comparisons, ordinary/cyclic sum distinction and support-cap forgery |
| BBP interval filters | 9 | Source forcing, growing interval width, finite count integrity, seed/metadata mutations, tail payment and type-sensitive receipt validation |
| Damped grade filters | 10 | Expansion versus direct products, all-grade sign, distant grades, coefficient budget, odd/fractional-grade mutants, uncertainty, integer promises and two monotone ladders |
| Fixed-resolution indexing | 4 | Separate prime-power sieve, exact parity split, ordinary triangular reindexing, positive diagonal correction, first-coefficient sign and finite sum interchange |
| **Total** | **71** | Exact arithmetic; no asymptotic fit |

The reproduction command verifies both saved arithmetic reports against
their source reconstruction. Its receipt records all code hashes and the
integration loader hash, so changes to the implementation or tests require
an explicit receipt regeneration. The BBP schema comparison distinguishes
integers from Boolean and floating-point lookalikes.

```sh
python research/2026-11-12/holographic_boundary_filters/run_checks.py
```

Use `--write` only after reviewing an intended change. It regenerates
the verification receipt; it does not confer new theorem authority.

## Separate derivations and implementations

These audits were assigned to separate agents with different mathematical
or computational decompositions. They share a model family and portions
of context and source material. They are **not** external referees, blind
independent witnesses or proof-assistant checks.

- [PI_AUDIT.md](PI_AUDIT.md): an unwrapped exact Fraction recurrence using
  the four displayed poles, without importing the production interval
  module, replayed every one of the 18 frozen census vectors through index
  2181. It independently proved the all-index forcing bound and checked
  width-reset, counterseed and cell-refinement mutants.
- [GOLDBACH_AUDIT.md](GOLDBACH_AUDIT.md): a separate smallest-prime-factor
  implementation checked midpoints 2 through 257 and exposed the limited
  positive range of the quadratic filter. It independently determined
  the real and integer relaxation minima for the midpoint-ten packet.
- [DAMPED_AUDIT.md](DAMPED_AUDIT.md): an SPF sieve through 8198, geometric
  Lagrange weights and direct-product grade evaluation reproduced all 18
  certificates with zero mathematical mismatches. All 72 added rational
  response coordinates matched independently. It checked signed asymmetric
  intervals, an upper mass budget and integer rounding.
- [DAMPED_DERIVATION_AUDIT.md](DAMPED_DERIVATION_AUDIT.md): a separate
  product/Lagrange derivation checked the tail cap, coefficient bound,
  parity and monotone brackets. The preserved reproduction block ran
  **4,716 exact assertions**, with zero failures. It distinguishes observed
  positivity from positivity guaranteed under every admissible noise error.
- [PHASE_AUDIT.md](PHASE_AUDIT.md): separate linear-duality and Fourier
  derivations checked the ambiguity constant, support-group criterion,
  Z/6 alias and cubic conditioning obstruction. A separate indexed-tuple
  implementation reproduced the correlation controls. Its extra finite
  torsion example became a regression.
- [FIXED_RESOLUTION_AUDIT.md](FIXED_RESOLUTION_AUDIT.md): independently
  verified the classical mean-value input, parity constants, finite-grid
  triangular limit, unordered diagonal term and dominant negative
  coefficient. This is a paper proof audit, with no fitted asymptotic data.

The root read the load-bearing arguments, checked the primary mean-value
and coefficient sources, executed the final test paths, and retained the
different source and method dependencies. Repeated agreement of the same
implementation is reproducibility, not added independence.

## Concrete issues found and repaired

### Fractional mass was accidentally assigned an integer-count promise

The initial convenience wrapper for damped histograms accepted nonintegral
masses but requested an integer conclusion. The concrete histogram
`(1/2,0,4)` at degree two exposed the error: its genuine ground mass is one
half, so an integer report is unsound. The wrapper now accepts only
nonnegative exact integers. General rational masses remain supported by
`response()` and `certificate(..., integral_counts=False)`. The auditor
replayed the original mutant after repair; it is rejected. The frozen
arithmetic packets were already integral and their values did not change.

### Python equality blurred receipt types

A dictionary comparison can treat `True` as equal to `1`, or `17.0` as
equal to `17`. The BBP receipt verifier now compares canonical JSON with
nonfinite numbers forbidden, after authentic source recomputation.
Regression mutations check the two type confusions. Exact arithmetic
results and source definitions are unchanged.

### Rational-input and phase-rank contracts needed explicit controls

The phase routines initially inherited `Fraction`'s permissive conversion
of floats, strings and Booleans. The audited mathematics was valid for the
resulting rational numbers, but the interface did not enforce the stated
exact-observation contract. It now rejects those implicit conversions.

A full-rank phase relation matrix was never a claimed completeness proof,
but the audit found a sharp torsion control: the q=21 support yields
`Z/63 -> Z/21`. The document and test now show explicitly why rational
rank cannot certify the absence of phase ambiguity.

### A frozen refinement expectation required a qualifier

Cellwise minorants improve under exact partition refinement. However,
the conservative rule “discard an interval crossing a cell boundary” can
lose a previously certified contribution at a finer resolution. The
preregistered expectation was therefore qualified after the audit.
The exact interval `[29/80,31/80]` has a positive q=4 contribution and an
ambiguous q=8 contribution. All frozen actual BBP packets had zero
ambiguous cells, so their reported comparisons remain valid. The limitation
and a safe repair strategy are recorded rather than erased.

## Authority and residual risks

The code assumes that supplied response intervals and source contracts are
genuine. Algebraic feasibility, a source string or a digest does not certify
physical acquisition or arithmetic provenance. The code does not solve a
general moment feasibility problem, a general minimax problem or a general
support-group isomorphism problem. Those implementation boundaries are
distinct from the narrower proved theorems.

The fixed-resolution arithmetic obstruction imports a classical
Selberg--Delange mean. Its hypotheses and constants were checked against
primary papers; the underlying analytic theorem is not newly proved or
formalized here. All finite empirical results have their exact listed
scope. The missing adaptive pointwise arithmetic estimates and the
uniform BBP R0 bound remain open.
