# Endpoint coercivity: validation, recovery and failed-attempt receipts

**Research round:** 2026-11-16, continuation of draft PR #657.
**Mathematical status:** the paper results and finite checks have the scopes
listed below. The eventual original-source lower bound, R0 and pi base-16
normality remain **OPEN**.

**Final complete root-suite replay: PASS.** A clean post-repair replay collected
and ran all **14,577** root-discovered tests: **14,575 passed, zero failures,
zero errors and two inherited Lean skips**. This was one complete eight-shard
run with exact test-ID coverage, not a mixture of successful earlier shards.
The [final receipt](endpoint_checks/full_suite_receipt.json) records the result.
The earlier complete run failed and is retained alongside the repairs.

## 1. Recovery and identity of the artifacts

The input was the exact draft head
`1f04b869182ad68deb764637034d72b19352ca48`, descending from Main XXVI main
`81be6b897ae980b801a3b9de9e22ef81e8360bfb`. The
[recovery manifest](ENDPOINT_RECOVERY_MANIFEST.json) inventories all 24 files
already present in that PR, with Git blob hashes, SHA-256 hashes and byte
counts. This establishes which committed artifacts were recovered; it does
not independently certify every claim those artifacts contain.

The [validation manifest](ENDPOINT_VALIDATION_MANIFEST.json) binds the proof
texts, finite instruments, certificate and replay by content hash. Hashes
establish byte identity, not mathematical truth. The manifest is refreshed
after final manuscript and script edits; its scope includes the executed
instruments, final receipts and the retained failed-attempt records.

The original four signed poles, literal zero seed, production source modules
and frozen provenance were retained. The work is on a non-main research
branch. A final push, hosted CI result or merge is not established by any
local receipt in this document.

## 2. The finite original-source certificate

The preregistered target was

\[
1-\Re W_B(\pi/16)>2/5
\quad\text{for every integer }16\le B\le4096.
\]

The [certificate](ENDPOINT_SHELL_CERTIFICATES.json) covers exactly **4,081**
integer shells, including all **3,840** shell starts beyond 256 through 4096.
The new norm-certificate interval is compared with the five VFM examples;
it is not represented as the largest finite source computation anywhere in
the SUCC repository.

The generator computes the literal zero-selected source endpoint at depth
8198, using exact rational arithmetic. Six hexadecimal guard digits give
`Q=16^6=16777216`. The endpoint's fractional remainder and the positive
source-tail allowance yield a rigorously enclosed phase interval of width
`2/Q` at each required clock. Integer lower and upper distance sums are
stored for every shell. No floating-point value of pi, sampled digit model
or random prime clock is a construction input.

The smallest certified phase-loss lower bound is exactly

\[
\frac{247384815345917}{439804651110400}
>\frac12,
\qquad B=25.
\]

Its decimal display is approximately `0.5624879471404642`. The rational
comparison proves that every tested shell exceeds 1/2. The stronger threshold
is a consequence of the executed certificate, not a retrospectively changed
preregistration. This result says nothing by itself about B > 4096.

The [independent replay](ENDPOINT_SHELL_REPLAY.json) reports **PASS**, with
all 4,081 lower and upper sums and the exact source endpoint digest matching.
The endpoint digest is
`e222179e8c24abdecde98c2192d73cb93d2744974312ced7a9e7fb007c24d91e`.

| Route | Source evaluation | Endpoint/digit path | Shell aggregation |
|---|---|---|---|
| Generator | Combined rational expression for the original four poles | Forward recurrence, integer digit extraction | Integer prefix sums |
| Independent replay | Literal four separate rational fractions | Reverse Horner summation, hexadecimal slicing | Moving-sum recurrence |

These routes differ in expression, summation direction, extraction and
aggregation. They share Python's Fraction library and the classical BBP
identity and source-tail premises. Their agreement is a useful implementation
cross-check, not two independent proofs of pi normality.

An additional [interval/extrema audit](endpoint_checks/check_endpoint_grid.py)
passed **1,612 exact assertions**; see
[its receipt](endpoint_checks/endpoint_grid_receipt.txt). It checks all extrema
of the piecewise linear torus-distance function on the tested grids, together
with strictly deeper rational source-prefix enclosures. This audits the
interval instrument, including wraparound and half-circle extrema.

## 3. Paper proofs and independent cross-audits

Three same-model bearings worked separately on construction, adversarial
review and translation before the parent synthesized their results. Later
cross-audits are disclosed rather than counted as blind independent witnesses.
No outside referee, proof assistant or formal kernel accepted these proofs.

| Result | Proof authority | What the computation can check |
|---|---|---|
| Original VFM sandwich and R0 equivalence | Existing elementary proof, reread and re-audited | Source evaluation, finite tail margins and finite norm identities |
| Cold-shell dimension `dim_H E_lambda=1/lambda` and dense G-delta | Self-contained finite cover, entropy upper bound, Frostman lower bound and Baire argument; parent audit | Finite branch alphabet, exact quadratic slack, endpoint coding and examples |
| Two-sided terminal-tail norm comparison | Reverse triangle inequality for the declared residual vectors | Rational surrogate tails and exact square-root comparison by squaring |
| Coherent quintic baseline `1/(16711680 B^5)` | Source asymptotics and exact geometric tail sum | Partial-tail diagnostics and rational upper envelopes |
| Critical pointwise floor implies `E_B>1/(679173120 B^7)` and `v_16<=1` | Exact subleading bound and contradiction with exponentially small restricted approximations | Constants, finite source inequalities and square-marker locations |
| Nearby-seed winding erasure | Exact dyadic shift and source recurrence | Nonzero seed, preserved odd-primary data, terminal fraction, erasure and later reunion |

The translator independently checked the critical constants and quantifiers.
In particular, `(16B+1)(16B+2)<=306B^2` and the gap between its reciprocal
and `1/(256B^2)` give the stated `1632` and `679173120` constants. The
restricted-exponent convention matches the existing RDT definition; shifting
from pi/16 to pi does not change it. The square-marker endpoint satisfies the
critical intermediate while failing R0. The equality-permitting condition
`liminf B^5 R_B>=1/16711680` is correctly rejected by the coherent control;
it is different from the eventual pointwise inequality.

The report distinguishes the exact R0 failure set of dimension 1/2 from the
earlier failed sufficient carry-gate set of dimension 7/8. Neither dimension
theorem determines membership of pi/16. The balanced-carry dictionary and
bulk constants 225 and 289 are credited to earlier SUCC work rather than
counted as discoveries of this round.

## 4. Focused regressions and calibrated hostile controls

The session's focused runs were observed passing **11 new endpoint-coercivity
tests** and **55 existing focused tests** in the immediate VFM/interferometry chain.
The latter comprise VFM (10), adaptive Gamma (10), shadow interferometry
(13), moving-frame horizon (11), and boundary order lift (11). These are
focused executions, not a substitute for the complete root-suite replay.
Their outputs were observed in the session transcript; no separate durable
focused-run log is asserted here. All these modules are also included in the
complete root-discovery coverage map.

The new [test module](../../../tests/test_endpoint_coercivity.py) includes
zero-crossing grid intervals, reconstruction against direct rational probes,
an independent small replay, a mutated certificate that must be rejected,
the checked-in 4,081-shell witness, balanced-branch sharpness, winding erasure,
fine erasure, tail calibration and invalid-domain rejection.

Standalone controls have retained receipts:

| Instrument | Executed finite scope | Receipt and discriminating controls |
|---|---|---|
| Cold-shell coding | 836 rational cases, four forced-zero windows | [Receipt](endpoint_checks/check_cold_shell_cover_receipt.json); `x=8/17` attains the 289 bulk constant and rejects replacement by 288; `x=1/15` has energy exactly 1/225 |
| Tail calibration | 196 generic norm cases; 28 zero-error mutants rejected; eight source-bound shells; 128 source-polynomial checks; 9,991 square-marker location checks | [Receipt](endpoint_checks/check_tail_calibration_receipt.json); no polynomial raw floor is silently promoted to completed-phase escape |
| Winding erasure | 581 exact assertions on ten declared shells | [Receipt](endpoint_checks/check_winding_erasure_receipt.json); wrong-shift mutation rejected, seed nonzero, odd-primary class and terminal fraction preserved |
| Phase interval instrument | 1,612 exact extrema/enclosure assertions | [Receipt](endpoint_checks/endpoint_grid_receipt.txt); includes wrapped intervals and deeper rational source bounds |

`finite_cover_receipt.json` and `check_cold_shell_cover_receipt.json` preserve
the same cold-cover execution result; they are duplicate records, not
independent runs. Decimal values in the tail and winding receipts are display
diagnostics. Their asserted comparisons are exact Fraction calculations.
The coherent asymptotic limit itself is proved on paper, not by those decimal
values approaching a constant.

## 5. Environment setup and the incomplete serial attempt

The environment is Python 3.12.14, with mpmath 1.3.0, NumPy 2.3.5,
SymPy 1.14.0 and SciPy 1.17.0. The
[setup receipt](endpoint_checks/execution_setup_receipt.json) records an initial
subprocess failure caused by the omitted repository import path:
`ModuleNotFoundError: No module named 'observational_succ'`. The documented
Main XXVI setup requires `PYTHONPATH=.`. Correcting that environment reran
the affected 11-test module successfully; no repository code was changed to
hide the import failure.

The initial literal serial command

```sh
python -m unittest discover -s tests -p 'test_*.py'
```

was incomplete at its 900-second limit, with exit code 124. It also began
without the documented import-path setup. The preserved
[receipt](endpoint_checks/unittest_receipt.json) explicitly says
`INCOMPLETE_TIMEOUT`; the normalized partial output is
[unittest_initial_serial.txt](endpoint_checks/unittest_initial_serial.txt).
Neither an incomplete test count nor the partial progress output is a pass.

The corrected runs use `PYTHONPATH=.` and one thread each for OpenBLAS, OMP
and MKL. Execution-root paths in published logs are normalized to `<repo>`;
mathematical results and failure messages are retained.

## 6. First complete root-suite run: failures retained and repaired

The first complete module-sharded run executed the entire collection of
**14,577** tests, with **three failures, zero errors and two skips**.
The [complete failed receipt](endpoint_checks/first_full_suite_attempt/full_suite_receipt.json),
coverage map and all eight shard logs remain under
`endpoint_checks/first_full_suite_attempt/`.

The failures were:

1. `test_inherited_seed_and_analytic_path_compose`: reassociated binary-float
   products differed by `7.275957614183426e-12`, failing an absolute
   decimal-place comparison at a large magnitude. The exact rational
   transport already passed. The repair retains that assertion and computes
   the logarithmic comparison at 70 decimal digits with a `1e-60` bound.
2. `test_native_gamma2_bound_does_not_resolve_moving_phase`: finite binary
   precision rounded `1+q^2` to `q^2`, turning a mathematically strict
   inequality into equality. The repair preserves the strict comparison
   while evaluating its unit correction at 70 decimal digits.
3. `test_p1_oracle_agrees`: another test's process-global mpmath precision
   left a 45-digit comparison running with insufficient precision. The
   repair declares a local 60-digit `workdps` context and restores the
   caller's precision when it exits; the existing `1e-45` threshold remains.

No failed test was skipped, converted to expected failure, removed from
collection or given a weaker threshold. The fixes are confined to the two
test files and do not modify the mathematical source implementations.

Targeted post-repair checks passed all **13 Gamma dilation tests** and the
triangle comparison under an intentionally reduced **35-digit ambient
precision**; the latter also checked restoration to 35 digits afterward.
The [precision-repair receipt](endpoint_checks/precision_repair_receipt.json)
records their commands, exit codes and durable log hashes.
These targeted results diagnose the repairs. They do not erase the failed
complete run or establish the final complete-suite status.

## 7. Mandatory repository gates

| Gate | Observed local status | Receipt |
|---|---|---|
| `python scripts/verify_provenance.py` | PASS, exit 0 | [Provenance](endpoint_checks/provenance_receipt.json) |
| Root `test_*.py` discovery, complete final replay | PASS: 14,575 passed, two inherited skips, zero failures/errors | [Final suite](endpoint_checks/full_suite_receipt.json) |
| `python scripts/observer_foundations_probe.py` | PASS, exit 0 | [Observer foundations](endpoint_checks/observer_receipt.json) |
| `python scripts/ordinal_succ_report_probe.py` | PASS, exit 0 | [Ordinal report](endpoint_checks/ordinal_receipt.json) |

The [shard runner](endpoint_checks/run_full_suite_shards.py) collects the
same root-discovered test IDs, checks uniqueness and exact once-only
partition coverage, and keeps every module together. Its coverage manifest
records each shard's test-ID hash and compares their union with the complete
collection. All 14,577 IDs are unique; the coverage hash is
`fe8ec45a7eadeacf0dffa47ef093257dd27c2d2a17814ba96d5b9033ec004315`.
This is a complete module-sharded replay, not the literal serial
execution order; shared-process order independence is not established merely
by matching test IDs. The final result comes from one complete post-fix
run, not a mixture of successful shards from different attempts.

The two inherited skips belong to `LeanEncodingReceipts`; both require the
unavailable pinned Lean 4.14.0 executable. Their exact IDs and reasons are
recorded in the [skip audit](endpoint_checks/lean_skip_receipt.json). No skip
was introduced for this research round.

Root discovery may invoke research tests through existing wrappers. No
separate claim is made that every research-local test was collected. Lean,
formal proof checking, external referee review and final-head hosted CI are
not established by these local gates.

## 8. Reproduction and final boundary

From the repository root with the documented dependencies available:

```sh
export PYTHONPATH=.
export OPENBLAS_NUM_THREADS=1
export OMP_NUM_THREADS=1
export MKL_NUM_THREADS=1
python scripts/endpoint_shell_certificate.py --output research/2026-11-16/defect_window_tomography/ENDPOINT_SHELL_CERTIFICATES.json
python scripts/verify_endpoint_shell_certificate.py research/2026-11-16/defect_window_tomography/ENDPOINT_SHELL_CERTIFICATES.json
python -m unittest discover -s tests -p 'test_endpoint_coercivity.py' -v
python research/2026-11-16/defect_window_tomography/endpoint_checks/run_full_suite_shards.py --workers 8
```

The geometric and calibration theorems are paper proofs with scoped audits.
The endpoint certificate is a rigorous finite arithmetic observation with a
paid source-tail budget. The code regressions and repository gates test their
declared implementations and integration. None performs the missing infinite
lift to an eventual original-source lower bound. R0 and pi normality remain
open regardless of the final test count.
