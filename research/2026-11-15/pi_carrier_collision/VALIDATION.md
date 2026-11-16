# Validation record

All results below are actual executions or explicitly bounded paper
reviews. The environment is Python 3.12.14. The final proof snapshot is
SHA-256 `03938f2d19125d214ad2e517982365d4f73f33fe8a264a6ef3278741d3021e1b`.

## Executed checks

| Check | Actual result | Scope and receipt |
|---|---|---|
| Full inherited discovery | **13,404 tests PASS**, exit 0; unittest reports 1084.019 s, wrapper 1092.902 s | Immutable parent `85a14bb6`, isolated at `/tmp/succ_pi_baseline_85a14bb6`; excludes this round's files. [Receipt](receipts/full_baseline.json), [raw log](receipts/full_baseline.log) |
| Final focused suite | **211 tests PASS**, 0 failures/errors, exit 0; 2.715 s | 60 new tests plus 151 related inherited tests, at the six final file hashes. [Receipt](receipts/focused.json), [raw log](receipts/focused.log) |
| Provenance gate | **PASS**, exit 0 | `scripts/verify_provenance.py`. [Receipt](receipts/provenance.json), [raw log](receipts/provenance.log) |
| Observer foundations gate | **PASS**, exit 0 | `scripts/observer_foundations_probe.py`. [Receipt](receipts/foundations.json), [raw log](receipts/foundations.log) |
| Ordinal successor report gate | **PASS**, exit 0 | `scripts/ordinal_succ_report_probe.py`. [Receipt](receipts/ordinal.json), [raw log](receipts/ordinal.log) |
| Standalone exact audit | **6,622 exact checks PASS**, replay exit 0 | No SUCC production imports; root replay 0.190 s. [Original receipt](receipts/translator_independent.json), [root output](receipts/root_independent_audit.stdout.log), [run receipt](receipts/root_independent_audit_run.json) |
| Numerical frame/control diagnostic | **PASS within its declared finite checks**, exit 0; 0.708 s | Exploration B=4,8, holdout B=13,29. [Prior plan](receipts/numerical_probe_plan.json), [output](receipts/numerical_probe.json), [run receipt](receipts/numerical_probe_run.json) |

The full inherited run and the focused suite overlap on old tests. They
are not two independent evidence families and are not reported as one
combined all-current-file discovery run. The separate parent worktree
prevented concurrent new files from contaminating the baseline. The
parent discovery command set `PYTHONPATH=.` before execution; this round
did not reproduce the previous round's missing-path import failure.

The full raw discovery log contains child test-run summaries and expected
mutation diagnostics. The final top-level summary is `Ran 13404 tests`
followed by `OK`; the wrapper exit status is zero. The log's SHA-256 is
`d815db7eaca2822716a3df573c9c0d49ca5beb6f2f81d6f0c406541674b9d665`.

## New test coverage

| Module | New tests | Concrete risks exercised |
|---|---:|---|
| `bbp_collision_frame.py` | 21 | Exact source echo and gap constants; erased seed; deleted source channel; clock laws and tails; Gram bounds and complex orientation; locked-reference residual; frequency-center versus spread; error gains and domain budgets |
| `phase_detection.py` | 29 | Exact Gaussian-rational Gamma response; clock recovery and variance; finite-circle forgetting; propensity mutation; fresh-trial versus copied-trial behavior; exact counterseed tail enclosures and dose |
| `random_probe_frames.py` | 10 | Rational conservative Chernoff budgets; exact binomial census controls; copied-row rank failure; correct whitening, Gram/matrix distinction and normalized noise factors; invalid domains |

The 151 inherited focused tests cover source authentication, original
BBP/Fourier behavior, bin-window conjugacy, echo transport, GB coercivity,
selected-orbit invariants, adaptive Haar, Gamma source volume and the
Haar/Gamma bridge. Exact per-file counts are in the focused receipt.

## Independent implementation scope

The standalone audit checks 800 rational sampling-budget cases, five
complete binomial censuses, copied-row rank failure, four Hadamard
normalizations, 198 Gamma multiplier comparisons, 594 semigroup fixtures,
312 negative-binomial tail/character enclosures, four rational Hermitian
population Grams, 480 literal-source echo identities, source-channel
mutations and GB-12 dose accounting. It counts 6,622 exact checks under
its declared case bounds. It imports no production implementation and
uses no floating comparison to certify those checks.

The audit does not re-prove matrix Chernoff, the irrationality measure of
pi, inherited GB-12, the source identity or a universal normality theorem.
Its example scale m=4096 is a budget fixture conditional on m>=m_2, not
a computation of the inherited unknown onset.

## Numerical holdout: what it demonstrates

The fixed seed is 20261115. The bounded triangular tap law and conservative
sampling budget were chosen before the diagnostic. On the largest held-out
block B=29, 5,568 rows gave Gram eigenvalues approximately
0.8605430906 and 1.1265132297 at the extremes; every tested coefficient
vector was recovered to maximum component error below 2.7e-15.

| B=29 carrier | Original absolute mean | B times raw detector energy | B times coherent locked-reference residual |
|---|---:|---:|---:|
| Authentic zero-seeded source | 0.154141 | 0.989682 | 1.821499 |
| Locked phase vector | 1 | 0.989203 | 0 |
| Same-forcing counterseed control | 0.9999999997 | 0.989203 | 3.98188e-9 |
| Zero-mean roots control | approximately 4.67e-17 | 1.006485 | 1.996439 |

These values illustrate the proved distinction: raw energy is nearly
universal, while labelled complex recovery and the coherent reference
residual retain the phase information. They provide no inference about
the distribution of pi digits, an asymptotic trend, or an all-scale
arithmetic bound. Source phases were reduced exactly modulo one before
conversion to floating complex values. The counterseed uses certified
tail midpoints; the resulting table itself is not an interval certificate.

## Bounded paper review

| Reviewer | Final scope | Verdict |
|---|---|---|
| Constructor | PC-01 through PC-06 and PC-09 | Bounded PASS at the final proof hash |
| Adversary | PC-01 through PC-10 | Bounded PASS at the final proof hash |
| Translator | PC-03, PC-04, PC-06 and PC-09, plus static random-frame implementation | Bounded PASS at the final proof hash |

The reviews found and resolved explicit inverse-domain assumptions,
sample normalization, confidence domains, the distinction between a
random clock and the source tail, and the uniform stability margin
needed for the across-scale R0 equivalence. The final hash-bound record
is [proof_review.json](receipts/proof_review.json). Notes preserve the
review sequence instead of presenting initial drafts as final approvals.
These are human-readable mathematical reviews, not proof-assistant
certificates or statistically independent sources.

## Reproduction

From the repository root, the new tests alone are:

```sh
PYTHONPATH=. python -m unittest tests.test_bbp_collision_frame tests.test_phase_detection tests.test_random_probe_frames
```

The standalone audit and numerical diagnostic are:

```sh
python research/2026-11-15/pi_carrier_collision/independent_audit.py
PYTHONPATH=. OPENBLAS_NUM_THREADS=1 python research/2026-11-15/pi_carrier_collision/numerical_probe.py
```

The inherited baseline was executed in the separate, detached parent
worktree with:

```sh
PYTHONPATH=. python -m unittest discover -s tests -p 'test_*.py'
```

Executing that command on the new branch also discovers the new tests;
the historical 13,404 count belongs specifically to the pinned parent.
The final artifact check compiles the five new Python implementation/probe
files and three test files, parses JSON receipts, checks local document
links and verifies frozen hashes. Its result is
[artifact_check.json](receipts/artifact_check.json). The final payload is
bound by [FILE_HASHES.json](FILE_HASHES.json).

## Remaining limitations

The formal probability-one result certifies eventual detector conditioning.
The source-specific hit theorem imports a previously proved weak signed
loss and its unextracted onset. No executed test or finite frame theorem
supplies the missing uniform original-source residual estimate, establishes
R0, proves pi normality, or demonstrates a physical quantum BBP carrier.
