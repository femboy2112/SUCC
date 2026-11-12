# Validation, counterexamples and publication scope

This continuation starts from published commit
`f4151c4ae877ee43c4b7d130174b6bec1dbab9d6`, on the same research branch
and draft PR #605. Its parent tree is the exact previously validated
boundary-filter snapshot. No archived source or prior mathematical code
was edited by this continuation.

## Required repository checks

The native run includes the entire existing test discovery and the new
42-test loader. Its actual command metadata and frozen core code hashes
are recorded in [native_validation.json](receipts/native_validation.json).
The four required checks run in sequence, with full untruncated logs:

| Command | Observed status |
|---|---|
| `python scripts/verify_provenance.py` | PASS, exit zero |
| `python -m unittest discover -s tests -p 'test_*.py'` | PASS, 13,163 tests, OK, exit zero |
| `python scripts/observer_foundations_probe.py` | PASS, exit zero |
| `python scripts/ordinal_succ_report_probe.py` | PASS, exit zero |

The logs are [provenance](receipts/provenance.log),
[native suite](receipts/native_suite.log),
[observer](receipts/observer.log), and [ordinal](receipts/ordinal.log).
Negative-control messages about intentionally stale temporary catalogs
are expected test output; the command exit and unittest result determine
whether the run passed.

The publication helper initially selected an embedded four-test subrun
instead of the final native summary and stopped its preflight. Inspection
showed embedded summaries for 4 and 7 tests followed by the actual
13,163-test `OK` summary. The parser was corrected to select the last
anchored summary. No repository test failed, no test result was changed,
and no full rerun was needed for this reporting-only correction.

The single complete native invocation ran **13,163 tests**: the 13,050-test
original suite, the earlier 71-test addition, and this round's 42 tests.
The frozen core code hashes were unchanged throughout that run. The
later standalone controls are separately bound by the final receipt.

The first-round 71-test exact receipt was separately replayed unchanged
and passed. It retains its own historical baseline-plus-addition record.
This continuation's full native run is distinct from that earlier run.

## Focused and standalone checks

The frozen suite has 42 tests:

| Area | Tests | Material contracts checked |
|---|---:|---|
| Integer information | 13 | Integer twins, exact mass, missing-channel discriminator, nonminimal product witness, rational rescaling, noisy packet overlap, channel bounds and moving-node escape. |
| Complex banks | 16 | Exact rational phases, conjugation, sieve/trial agreement, ordinary triangle, endpoint and unconjugated diagonal, false prefix and true-bank finite-prefix controls. |
| Pointwise certificates | 13 | Sharp mass/equality/noise budgets, clamped recovery, integral-target premise, masked-tail intervals, far grades, changing per-midpoint degree and false quantifier transfers. |

The tests passed with warnings treated as errors and through the native
integration loader. The deterministic reproduction command additionally
executes the independent root probe and the later phase-aperture controls:

```sh
python -W error research/2026-11-12/adaptive_boundary_resolution/run_checks.py
```

The code-bound receipt is [VALIDATION_RESULTS.json](VALIDATION_RESULTS.json).
It authenticates the precise saved reports and implementation hashes,
not physical acquisition or mathematical truth. `--write` records an
intended change after review; it cannot promote a conjecture into a proof.

### Exact finite outputs

- Eighteen product-twin packets across bases `2,3,5` and degrees `1..6`,
  plus the mass-14 improvement, are saved in
  [INTEGER_RESULTS.json](INTEGER_RESULTS.json).
- Four frozen arithmetic midpoints and degrees `2,4,6` give twelve
  damped certificates: ten positive, eight exact counts from their
  actual integer intervals, and seven meeting the stronger uniform
  mass-only completeness budget. All four moving-node intervals recover
  their counts `6,15,22,34`. These are in
  [AUDIT_RESULTS.json](AUDIT_RESULTS.json).
- The same probe independently reconstructs the integer annihilator by
  elementary symmetric sums, checks rational phase traps passing grades
  `1..8`, `1..32`, and `1..64` before first failing at `12,36,68`, and
  verifies 726 synthetic histogram/noise cases for one-channel intervals.
- [COMPLEX_RESULTS.json](COMPLEX_RESULTS.json) preserves the designed
  genuine phase bank with cumulative values `1,2,3/2,1/2,-3/2` and the
  separate invalid-prefix bank.
- [PHASE_APERTURE_RESULTS.json](PHASE_APERTURE_RESULTS.json) records
  19 standalone exact controls. The phase addendum was developed after
  the 42-test freeze; its tests are assertions inside `report()`, run
  by the final reproduction command, not extra native unittest cases.
  At midpoint 263 the actual four-phase average is `2227/128`, whose
  floor is 17 while the genuine count is 15. The sound mass-corrected
  lower bound is `131/120`.

The arithmetic source is computed by finite factorization, with separate
trial primality and algebraic decompositions for comparison. These runs
verify wiring, conventions and finite inequalities. No asymptotic curve
was fitted, and no finite sample is used as proof of an infinite statement.
In particular, all four larger frozen midpoints are prime: their diagonal
pairs make target positivity known in advance. The numerical counts and
false-negative filters remain substantive integration checks, but these
points are not hostile Goldbach-existence tests. The shorter unit-suite
ranges include composite midpoints as well.

## Separate proof audits and exact replays

[INTEGER_APERTURE_AUDIT.md](INTEGER_APERTURE_AUDIT.md) independently
checks integer divisibility over arbitrary finite support, the positive
root argument, exact mass, channel gaps, noise and aperture scope. Its
displayed checker was replayed by the root and returned `[72,108,1620]`:
72 polynomial-multiple checks, 108 channel-boundary checks and 1,620
authentic aperture intervals. The log is
[integer_audit_replay.log](receipts/integer_audit_replay.log).
The audit also supplies five explicit contract mutations.

[COMPLEX_POINTWISE_AUDIT.md](COMPLEX_POINTWISE_AUDIT.md) checks the
complex analytic import at the gamma-zero endpoint, strict outer-mode
dominance, the triangular endpoint and diagonal, the sharp integer/noise
threshold, the true individual degree schedule, and the classical
density-one transfer. It makes no claim to have run a new broad scan.

The root checked the audited note/code hashes against the final reviewed
files. Every recorded hash matched; the exact record is
[audited_snapshot_check.json](receipts/audited_snapshot_check.json).
The root also independently derived the load-bearing elementary
arguments, inspected the primary Selberg--Delange statements and
rendered Vaughan's original page 315 to check the precise imported
mean-square theorem. The angular addendum came from a disclosed root
derivation, then an assigned implementation/proof check; it is not
counted as a blind independent discovery.

All authors and auditors are instances of the same model family, with
shared sources and prior context. Different implementations and proof
decompositions provide useful adversarial checks. They are not external
referees, statistically independent witnesses, or proof-assistant runs.

## A concrete scope error found and repaired

The first aperture paragraph allowed only a known mass upper bound but
then discussed normalization by the actual total mass without explicitly
supplying it. That loses absolute-count information: histograms `(1)`
and `(2)` have identical normalized responses at every node and both
have mass at most two, but their zero counts differ.

The auditor reported this exact counterexample. The text now normalizes
by the known bound `M`, or requires the actual normalization mass as an
additional supplied value. The root added the counterexample to its
executable controls, and the auditor reread the correction. The
unnormalized proof and frozen source values did not change. The repaired
hash is retained in the audit and the snapshot check.

## Limits and publication verification

The imported classical arithmetic theorems are not reproved or formally
verified here. The new elementary and analytic deductions have explicit
paper proofs and their stated domains. No arithmetic-source realization
is asserted for the integer ambiguity twins. No response acquisition,
support certificate, normalization scale or uncertainty guarantee is
created by a source string or digest.

The mathematical catalog and curated relationship-graph lint are checked
after the final documents are written; they discover references and
syntax/dependency issues rather than certify proofs. The publication
step compares the connector-created repository tree to the locally
validated tree before advancing the research branch. The draft PR
remains a review surface, with the universal arithmetic claims still open.
