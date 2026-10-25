# Euler--Mascheroni validation and proof-authority record

**Baseline:** main `e648df3e4fca73ab6b942232b5ca4b310e9cac08`.
The branch adds four independent finite interfaces and their tests on that
baseline. Siblings through #285 were inspected at pinned heads, not merged.
The execution environment was Python 3.12.14 with the existing research
dependencies; no dependency installation or runtime modification was needed.

## Observed local results

| Gate | Observed result | Evidence and scope |
|---|---|---|
| Full repository unittest discovery | **7,649 tests, PASS**, 716.396 seconds reported by unittest | [Result and frozen input hashes](euler_mascheroni_validation/full_suite_result.json); [complete compressed log](euler_mascheroni_validation/full_suite.log.gz). All eight new production/test files were byte-identical before and after, and checked again during packaging. |
| New focused test groups | **48 test methods**, all included in the full passing run | 18 successor/refinement; 10 BBP regulator; 7 character bridge; 13 completed Li. Exact tests and optional numerical calibration have distinct labels. |
| Source provenance | **PASS**, 72 manifest entries | [Receipt](euler_mascheroni_validation/provenance.json): 55 mechanical namespace migrations and 17 byte-identical historical research archives. |
| Observer foundations | **PASS** | [Receipt](euler_mascheroni_validation/observer_foundations.json). The inherited open analytic and foundational statements remain open. |
| Ordinal SUCC report | **PASS** | [Receipt](euler_mascheroni_validation/ordinal_succ.json). Finite report, no physically executed infinity or global positivity inference. |
| Combined new finite receipt | **Fresh construction and replay PASS** | [Replay log](euler_mascheroni_validation/probe_replay.log), [receipt](euler_mascheroni_validation/probe_receipt.json). Four rational actual-source character windows and three rational completed-Li coefficient enclosures. |
| Claim namespace checks after registration | **15 tests, PASS** | [Log](euler_mascheroni_validation/namespace_tests.log); EMS-01--28 registered without renaming history. |
| Academic Main VII and VIII metadata gates | **PASS** after namespace addition | [VII receipt](euler_mascheroni_validation/academic_main_vii.json), [VIII receipt](euler_mascheroni_validation/academic_main_viii.json). Existing admitted-source authority is unchanged; the new paper claims are not admitted Lean declarations. |

Subsequent changes after the full run were paper proofs, navigation, claim
registration and one CI receipt-replay step. Production and test hashes
remained unchanged. Namespace/metadata gates and the new receipt were
replayed for those integration changes. The new all-degree and centered Li
cutoff bounds are paper theorems, not assertions that the finite runtime
implements an unbounded-degree routine.

## Reproduction

From an environment with the repository's declared test dependencies:

```sh
python scripts/verify_provenance.py
python -m unittest discover -s tests -p 'test_*.py' -v
python scripts/observer_foundations_probe.py
python scripts/ordinal_succ_report_probe.py
python scripts/euler_mascheroni_probe.py --verify research/2026-10-24/euler_mascheroni_validation/probe_receipt.json
python -m unittest tests.test_claim_namespace_collisions -v
python scripts/academic_main_vii_gate.py
python scripts/academic_main_viii_gate.py
```

The full suite ran with the repository on `PYTHONPATH`, using an existing
research virtual environment. The exact executable and environment path
are recorded in the full-run JSON. On CI, the existing editable installation
provides that import path. A single step was added to the existing CI
workflow to replay the new receipt; no new parallel workflow was introduced.
Hosted CI is an additional observation and is not pre-declared passed by
this local record.

## What the new receipt certifies

The combined probe uses exact integers/Fractions. Rational logarithm
enclosures, monotone infinite-tail bounds, Machin bounds and Taylor
remainders determine its interval endpoints. Decimal endpoints are rounded
outward from rationals; they are not floating-point point estimates.

The four actual BBP windows use original zero-initial rational circle
states, 80-term Machin bounds, Taylor order 16, phase rounding to 64 binary
places and outward complex-box rounding to 60 binary places. Known zero,
quarter-turn and half-turn controls are enclosed. A separate rational
squared-modulus comparison establishes the finite nonmonotonicity.

The three Li certificates construct Stieltjes inputs from integer successor
sums at cutoff 512, rational logarithms and monotone tails. Integer-zeta and
pi/Gamma-completion channels have explicit enclosures. Supplying arbitrary
formal coefficient tuples to the lower-level recurrence does not
authenticate them as the actual Stieltjes source.

The receipt's 15-file manifest binds the named local implementation,
tests, source helpers and probe. It is not a full transitive dependency or
runtime attestation. The baseline commit, full-run metadata and original
provenance checker provide additional, separately scoped evidence.

## Failures and corrections retained

1. An initial baseline invocation used the default interpreter, which
   lacked `mpmath`. It failed to import the requested test modules. The
   existing research environment was then used; the relevant 40 inherited
   gamma/Tate tests and the full suite passed. No code claim was promoted
   from that environment failure.
2. The optional huge-cutoff Hurwitz diagnostic suffered cancellation at
   fixed precision: at $m=400,N=2^{400}$, 70 dps returned 0.0, while 220 dps
   returned approximately 0.948528108646579546014716. The
   [original receipt](euler_mascheroni_validation/bbp_precision_failure.json)
   is preserved. The code now rejects an insufficient digit budget before
   evaluating it. This guard is tested; the optional readout remains
   numerical-only and is not used to prove the cofinal theorem.
3. Internal review distinguished a fixed Archimedean Euler constant from
   a coupled mutation of both gamma appearances. The correct first-Li
   sensitivities are 1 and 1/2, respectively. Both are explicit and tested.
4. Paper review corrected the scope “any fixed finite list of jets” and
   made the cofinal hypotheses $s\downarrow0,N\to\infty$ explicit in the
   standalone claim row. These changes restrict the claims to what the
   proofs establish.
5. Final live reconciliation found sibling #285. Its source and completion
   normalizations are compared explicitly, and its centered observation
   prompted the sharper paper-only Li bound. A negative-even numerical
   endpoint failure in that sibling was reproduced separately and recorded
   in [its review receipt](euler_mascheroni_validation/pr285_review.json).
   The sibling is not included in this branch's full test count.

## Proof and review boundary

The finite tests catch source substitutions, omitted boundary terms,
incorrect refinement factors, wrong signed offsets, missing completion,
and finite-jet counterfeits. The analytic limits and all-degree error bounds
are justified by the proof notes, with primary classical references and
internal adversarial review. All agents share model provenance; they are
not independent external referees. No new Lean verification was attempted
or claimed. No nontrivial zero locations enter the construction.

**Established:** the explicitly scoped finite identities, paper transports,
error bounds and rational certificates in EMS-01--28. **Unproved:** actual
all-character harmonic cancellation, all-degree Li positivity, original
Weil positivity, Nyman closure, pi normality and RH.
