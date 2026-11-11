# Validation of the circle/line observer

## Exact implementation and audit boundary

The final production source is `circle_line_observer.py`, SHA-256:

```text
a7b02e06e5e53a7a9d66b0b2d6fd8b4b0a8529b1fdecdfb995a01bc5cb9239fa
```

`observer_receipt.json` binds the production and probe hashes. The finite
512-arrow trace is stored in `observer_trace.json`; its L/R word has SHA-256
`3a6b7fe8c558ace21eac7f9f71b068fa6eea0bc70f4aa4312c6fecc6408b599d`.

| Check | Actual finite result |
|---|---|
| Two independently implemented geometric sources | Same 512 L/R arrows and 64 hexadecimal fractional digits. |
| Scalar reconstruction and independent BBP reference | All stored arrow and digit certificates passed; BBP 180 terms in root probe,192 terms in constructor's separate replay. |
| Circle incidence and metric | 87 rational parameters in root probe; exact circle, secant, inverse and speed identities. |
| Alternative coarse geometry | Seven Riemann brackets, subdivisions 2 through 128, exact width 2/N. |
| Conic action | 33 matrix maps and 1,089 composition pairs; quadratic-form scaling and parameter intertwining checked. |
| Metric cocycle | 256 root checks; exact non-isometry and rational-rotation controls. |
| Continued fractions | Completed L/R run lengths agree with a separate continued-fraction calculation from the BBP interval. |
| Precision transport | 18 exact rational majorants; the universal constant is proved separately. |
| Mutation suite | Eight rejected changes: branch, denominator, source precision, mediant, multiplication side, density, normalization and units. |
| Long imported API | 600 hexadecimal digits returned under Python integer display cap 640, without changing the process setting. |
| Adversarial final-source replay | 4,096 arrows and 129 digit certificates per source; see `HOSTILE_OBSERVER.md` §10 for full scope. |
| Streaming CLI | Each source emitted 64 JSON lines and exited cleanly when the finite consumer closed the pipe. |

The proof-relevant program and probes use integer and rational arithmetic.
The production file imports no external pi computation and evaluates no
trigonometric function. Its geometry is a fixed semantic model with a
supplied mathematical derivation, not an arbitrary geometry parser.

## Defects discovered and repaired before publication

The first audit caught integer geometry arguments falling back to floating
point; those methods now coerce to `Fraction`. Unknown imported API source
names are rejected instead of silently choosing a different implementation.
The digit helper explicitly distinguishes the units digit from the complete
integer part in small bases. A bounded-chunk rational formatter makes imported
long runs independent of Python's integer display cap. Both reviewers reran
their checks at the final source hash above.

The final receipts preserve earlier version boundaries. Reviewers are
same-model agents, with different derivations and implementations; this is
not external peer review or formal verification.

## Repository regression scope

The full existing unittest command was started on the frozen checkout at
`964768cd1fa5116f521625abfaaad8d8fab0f222`, after installing the package in
editable mode. The new round was assembled outside that checkout while the
suite ran. The fresh run passed all 12,806 tests in 1036.979 seconds,
with exit code 0. Its raw output and exact run receipt are preserved alongside this
file. This is a fresh run after the prior round's diagnosed environment error;
the earlier failure record is retained in the older dossier.

Only the new research dossier, the previous dossier's navigation, and the
generated mathematics catalog are changed in this round. No core module,
existing test, dependency, workflow or imported archive differs from that
frozen regression baseline. Final research scripts receive their own exact
probe; the completed catalog and its reader tests are checked after assembly.
`repository_validation.json` records the actual final commands and outcomes.

Final local results:

| Gate | Result |
|---|---|
| Full frozen-baseline suite | **PASS: 12,806 tests**, 1,036.979 seconds reported by unittest. |
| Import provenance | PASS: 72 items, including 17 byte-identical archives and 55 documented namespace migrations. |
| Observer foundations | PASS. |
| Ordinal successor report | PASS. |
| Final catalog reader tests | PASS: 10 tests. The logged stale-catalog message is an intentional negative fixture. |
| Final standalone observer/probe | PASS under `python -W error`; receipts bind the final source hash. |
| Catalog and staged patch | Freshness and whitespace receipts are in `repository_validation.json`; the 170 catalog warnings are identical to baseline. |

Required commands:

```sh
python -m unittest discover -s tests -p 'test_*.py'
python scripts/verify_provenance.py
python scripts/observer_foundations_probe.py
python scripts/ordinal_succ_report_probe.py
```

Additional final checks include the standalone observer probe, fresh trace
generation, mathematics-catalog freshness, catalog reader tests and staged
whitespace validation. Full-suite timing and count are taken from
`full_unittest_receipt.json` and its raw log, not inferred from a test list.

## Hosted CI and publication

The pre-round head `964768cd1fa5116f521625abfaaad8d8fab0f222` completed all
four observed GitHub workflows successfully. `baseline_ci.json` records their
names and run IDs. That success belongs to the earlier head, not a claim of
success for a commit that had not yet been pushed.

This round is published as one follow-up commit on the existing non-main
branch and draft PR #595. The final chat/PR status reports the new commit's
actual observed workflow state. No merge, release, tag or workflow edit is
part of the operation.

## Mathematical status

The finite-program recovery theorem, conic/cocycle correspondence and
precision-transfer inequalities have written proofs within the declared
classical domain. They have not been formalized in a theorem prover here.
Finite checks validate the implementations and countercontrols. Neither those
checks nor the proof of computability establishes the original-zero parity
contrast, pi normality, or RH. `CLAIM_LEDGER.md` preserves these distinctions.
