# Validation and authority record

The proof dossiers contain the mathematical arguments. The executions below
calibrate the finite implementations and replay the audited inputs. They
do not infer infinite-time cancellation from finite data, and they are not
Lean certificates or external peer review.

## Environment and frozen inputs

- Python 3.12.14; SymPy 1.14.0; mpmath 1.3.0; NumPy 2.5.4; SciPy 1.18.1.
- Exact parent: `1c6ce7d7ee83a0bd751bde8092e46ff798855fd3`, PR #417.
- Native main inspected: `e18ba565ca540adb7edf3292f5593929e76d91c5`.
- Every change in this round is additive below this research directory.
- SOURCE_INPUTS.json records the exact inspected heads, 40 parent input
  file hashes and 15 sibling file hashes. Parent files matched their local
  pinned git objects; sibling files matched the GitHub Contents API at the
  declared commits before replay.
- Executions were performed on 2026-10-31 UTC, in the continuation of the
  repository's 2026-10-30 research round. Raw command, start time, elapsed
  time, return code and output SHA-256 accompany each root receipt.

## Required native gates

| Required command | Observed result |
|---|---|
| `python scripts/verify_provenance.py` | PASS, 72 source items |
| `python -m unittest discover -s tests -p 'test_*.py'` | 10,008 tests executed in 1471.885 seconds: 10,006 passed, two environment/setup errors |
| `python scripts/observer_foundations_probe.py` | PASS |
| `python scripts/ordinal_succ_report_probe.py` | PASS |

The full native run is preserved with its original **exit code 1** in
`receipts/native_unittest.log` and `baseline_summary.json`. It is not
reported as an uninterrupted green full-suite run. Both errors were
diagnosed and their complete affected modules subsequently replayed:

1. `test_exact_probe_receipt_and_independent_count` invokes the script
   `scripts/meta_choice_descent_probe.py`. The isolated environment had
   dependencies installed but not the local package, so that subprocess
   raised `ModuleNotFoundError: observational_succ`. Installing the local
   package with `python -m pip install -e . --no-deps` resolved the import.
2. `test_real_graph_retains_history_and_checks_new_sources` requires pinned
   historical Git blobs. The partial clone lacked one such object, and its
   lazy fetch had no network access during the test. All nine unique
   commit/blob objects declared by the registry were materialized and
   checked with `git cat-file -t`, including the originally missing
   `f8f74e0eccb12e0d8aa127b3b5fa091f00367414`.

After these environment repairs, the complete meta-choice module passed
**11/11** and the complete registry module passed **6/6**, using unchanged
repository code under the original sandbox. The 17-method replay and both
command receipts are in `receipts/recovered_*.log` and
`receipts/native_recovery_summary.json`. All 10,008 discovered native
methods therefore have successful execution evidence across the original
run and this targeted replay. The entire 10,008-method command was **not
rerun** after setup repair; no such second result is claimed.

The source-provenance replay verifies 72 imported items: 17 byte-identical
research archives and 55 declared namespace migrations. This is an
integrity check, not mathematical truth certification. Both foundation
probes retain their own explicit boundaries on universal positivity and
finite versus universal authority.

## Final focused suite: 60 exact methods

`receipts/focused.log` records **60/60 PASS**, 18.826 seconds inside unittest
(19.690 seconds for the full captured process). All methods in this suite
use exact integer/rational or exact formal coefficient calculations. The
logarithmic readouts use rational interval bounds, not binary floats.

| Scope | Methods | Principal falsifiers |
|---|---:|---|
| Root all-order shadow | 13 | Wrong terminal indices, source sign, seed, prefix, relative defect, minimal carries |
| Rational jet and prime frames | 14 | Value/jet confusion, omitted local inverse, missing carry seam, wrong secant sign, aliased initial germ |
| Spectral source | 15 | Wrong residue, noncomposing Pascal shift, wrong four-pole recovery, unpaid truncation error |
| Rational summability and source controls | 13 | Missing higher pole orders, incorrect twisted inverse, false normality from rank or local data |
| Prime weighting | 4 | Missing prime powers, log(p^k) instead of log(p), missing dilation factor, false common-shift closure |
| Root moving rational-frame diagonal | 1 | Failure of the explicit summable rational phase-error budget |
| Total | 60 | Exact finite regression authority; analytic proofs remain in the dossiers |

## Separate implementations and adversarial checks

**Flat-shadow coefficient oracle: 9/9 PASS.** The independent implementation
works with formal source-symbol coefficients and moving terminal supports,
with general radix controls 2, 3, 16 and 31. It does not import flat_shadow.py.
It separately checks finite telescoping, the V-shaped horizon, wrong-sign
and plateau controls, and the rational l1 budget. See
`receipts/flat_shadow_coefficient_oracle.log` and its command receipt.

**Prime-frame oracle: PASS.** A separate SymPy derivation differentiates the
original product expression, establishes explicit derivative-polynomial
positivity, and computes a rational enclosure for the sharp constant. Nine
90-digit mpmath holdouts separately calibrate the error asymptotic. Those
decimal holdouts are numerical observations; the rational interval and
symbolic calculations carry exact authority. See
`receipts/prime_frame_independent_oracle.log`.

**Adversarial source oracle: five exact symbolic identities PASS.** The
adversarial bearing separately used SymPy for the integer log potential,
four-pole telescope, leading coefficient and two source jets. Its original
receipt is retained as `receipts/adversary_symbolic_receipt.json`; the
root's 60-method suite independently reruns the associated 13 Fraction
methods. The symbolic receipt records agent execution, not a second root
execution or a blind external referee.

The final read-only reviews and their scope corrections are recorded in
FINAL_REVIEW.md. Successful independent derivations within one model system
are useful cross-checks, not independent human peer review.

## Fresh replay of incoming work

| Input | Result | Authority |
|---|---|---|
| #417 focused suite | 57/57 PASS | 35 exact-only methods; 22 include float/mpmath |
| #417 five separate oracles | All return code 0 | Mixture of exact symbolic checks, proved analytic bounds and numerical calibration |
| #418 committed probe | 14/14 PASS | 13 exact methods; one quadratic-family method uses floating square roots |
| #418 separate oracle | PASS | Exact polynomial/matrix identities plus numerical root moduli |
| #419 committed probe | 9/9 PASS | Exact Fraction arithmetic |
| #419 independent least-squares oracle | 6/6 controls PASS | Exact normal equations on independently expressed cases |

All commands and logs are under receipts/. The sibling folders were
materialized at their pinned heads outside the branch; no sibling merge is
implied. INCOMING_AUDIT.md explains the source and authority corrections,
including the stale #419 PR body and its newer same-field commutation no-go.

## Failures and corrections retained

The first prime-frame oracle incorrectly demanded strictly positive values
for every coefficient of a denominator polynomial. A factor a^k makes some
trailing coefficients zero while the polynomial remains positive on a>0.
The corrected test requires nonnegative coefficients and at least one
positive coefficient. ORACLE_CORRECTION.md retains this failed-attempt
history; it was not counted as a pass. The mathematical source sign theorem
did not fail.

Final paper review tightened the summary source class to distinct simple
poles with no polynomial part, explicitly included finite integral p-adic
precision in the alias theorem, and qualified the existence of general
asymptotic expansions. These changes affect theorem scope and prevent an
overbroad interpretation. They do not silently rewrite historical claims.

## Reproduction and integrity

Use a Python environment satisfying the repository's declared test extras.
Install the repository package itself (for example `python -m pip install
-e ".[test]"`) so subprocess scripts can import it. Use a complete clone or
materialize the exact historical objects pinned by the registry before an
offline replay. From the repository root:

```sh
python research/2026-10-30/carrier_adelic_transport/run_validation.py --scope baseline
python research/2026-10-30/carrier_adelic_transport/run_validation.py --scope focused
python research/2026-10-30/carrier_adelic_transport/run_validation.py --scope native_recovery
python research/2026-10-30/carrier_adelic_transport/flat_shadow_coefficient_oracle.py
python research/2026-10-30/carrier_adelic_transport/prime_frame_independent_oracle.py
python research/2026-10-30/carrier_adelic_transport/verify_manifest.py
```

The replay commands intentionally refresh receipts, so their timestamps and
elapsed times can differ from the frozen artifact manifest. Verify the
downloaded package before replaying if byte-level identity is the question.
Only use `verify_manifest.py --write` when deliberately freezing a revised
package. The manifest covers all package files except itself and Python
caches. The verifier also checks every pinned input file available in the
checkout; external sibling inputs remain separately pinned by commit and
blob hash.

Hosted checks are a separate observation made at the published commit. No
local receipt is a claim that GitHub Actions has completed successfully.
The selected macroscopic gap, all-frequency Weyl cancellation, pi normality
and RH remain OPEN.
