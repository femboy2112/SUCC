# Validation and provenance

Date: 2026-11-10. Base repository revision:
`50481e49592af00d87c602f671a28f3503709de0` (Main XXIII integration, PR #584).
Python runtime: **3.12.14**. New compiler and backend code use the standard
library. The broader inherited suite also uses the installed research dependencies.

## Final-code execution

| Gate | Actual result | Receipt |
|---|---|---|
| New compiler tests | 29 passed | `tests/test_zero_anchored_lambda.py`; focused log |
| New Haar/Pascal/backend tests | 20 passed | `tests/test_zero_anchored_haar.py`; focused log |
| Combined new and inherited focused suite | 90 passed in 1.182 seconds | `receipts/focused-tests.log` |
| Full native unittest discovery | **12,995 passed in 1065.317 seconds; exit 0** | `receipts/full-suite.log` |
| Imported source provenance | PASS; 72 imports verified | `receipts/provenance.log` |
| Observer foundations probe | PASS | `receipts/observer-foundations.log` |
| Ordinal report probe | PASS | `receipts/ordinal-report.log` |
| Typed mathematical graph | PASS | `receipts/math-graph.log` |
| Deterministic mathematics catalog | Regenerated; exact check PASS | `receipts/catalog-build.log`, `receipts/catalog-check.log` |
| Finite compiler/phase/Pascal/signed-overlap probe | PASS, exact rational receipt | `receipts/FINITE_REPORT.json`, `receipts/finite-probe.log` |
| Independent adversarial replay | PASS | `receipts/adversarial.json` |

The finite probe covers 15 state/seed cases, two actual evaluation strategies,
guarded-tail unfolding, explicit budget exhaustion, seven adjacent-block sizes
through 8,192 observations, and Pascal degrees 0, 1 and 4 on 257 starts.
Every claimed finite numerical verdict uses exact rational intervals.

The adversarial replay covers 200 altered-source values, 176 exact completion
identities, 448 rational-orbit quantization/floor cases, 61 certified shadow
windows, source-zero rejection, two equality-spoof attacks, and positive controls.
The general Wasserstein routine in that replay is inherited; it is not an
independent implementation. The separate new integer-CDF tests compare two
different implementations over 216 grid triples.

`receipts/FROZEN_CODE_HASHES.json` binds the final two package modules and two
new test files used by the native suite. `FINITE_REPORT.json` additionally
binds its executable probe, protocol, and the inherited source and reducer.
The canonical BBP source and import manifest remain byte-identical to the base.
`receipts/FINAL_VALIDATION.json` records the completed native run, frozen-code
verification and protected-file checks. Documentation delimiters were normalized
for GitHub after the code freeze; the mathematical text was unchanged.

## Retained failures and repairs

1. The first focused backend run had a one-character expected-prefix fixture
   error: a 12-phase request was compared with a 13-digit string. The generated
   source cells were correct; the fixture was corrected. The repaired test
   also compares shifted and independently refined windows.
2. The initial public `verify=False` observation path admitted a fake de Bruijn
   table that contradicted its claimed Wasserstein bound. That bypass was
   removed. Public upper bounds now rebuild all observations and derive N from
   the verified consecutive source window.
3. Duplicate character requests incorrectly doubled a degree-zero coefficient.
   Duplicate frequencies are now rejected. Negative error fields, detached
   coefficient arrays, floating integer aliases and inexact residual endpoints
   are rejected. See BACKEND_REVIEW.md for reproduced attacks and final hashes.
4. A custom Python string equality hook could initially substitute a wrong
   compiled literal or forged certificate status. Exact recursive type checks
   now run before structural equality; the independent replay confirms both
   attacks fail while positive controls pass. See ADVERSARIAL.md, Section 8.
5. A full native run was deliberately interrupted while these hardening changes
   were made. Its partial output is retained in
   `receipts/full-suite-prehardening-interrupted.log`; it is not counted as a
   full-suite pass. The final-code run was restarted after the code repairs and completed with
   12,995 passing tests.
6. An exploratory file-search command referenced a nonexistent catalog-builder
   name. The actual existing tool is `scripts/build_math_memory.py`; the
   failed lookup did not modify any repository file or establish a gate.

The protocol was locally committed before the signed-defect table was generated
at `41ad398`. This is not a claim of prior remote preregistration or new pi
digits. The measured original-source windows are finite diagnostics; their
statistics do not establish an all-N estimate.

## Review authority and mathematical boundary

Constructor, adversary, compiler author and root used different decompositions,
but the same model family. Root independently checked the source identities,
tail and quantization constants, signed-overlap scaling, and primary-source
discrepancy theorem. This is not external refereeing, Lean verification or a
worldwide novelty audit. No new formal proof authority is registered.

No test, certificate, or successful beta reduction in this round proves that
the original-zero statistical defect tends to zero. The actual contraction
with an independently justified vanishing remainder remains OPEN, as do
original-zero parity balance, pi normality and RH.

Hosted checks, if triggered by the new draft PR, have their own execution scope.
No hosted pass is inferred from a local pass. The branch is research work based
on an integration candidate; it does not authorize a main merge.
