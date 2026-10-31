# Validation, provenance and authority

Local campaign date: 2026-10-30. Exact parent PR400:
`2b0628f52e9d88993c2e3ffa30b9748adfb781f0`.
Branch: `research/gamma-twist-selected-phase-2026-10-30`.
Every change is additive under `research/2026-10-30/gamma_twist/`.

## Repository gates

| Gate | Result | Raw evidence |
|---|---|---|
| Full native unittest discovery | **10,008 PASS**,925.933s unittest time;934.273s wrapper time | [log](receipts/full-suite.log), [command metadata](receipts/full-suite.json) |
| Required provenance verifier | PASS,72 manifest entries | [log](receipts/provenance.log) |
| Observer foundations | PASS | [log](receipts/foundations.log) |
| Ordinal report | PASS | [log](receipts/ordinal.log) |
| Mathematics graph | PASS,51 nodes/60 edges | [log](receipts/math-graph.log) |
| Mathematics catalog | FAIL, stale catalog | [child](receipts/math-catalog.log), [untouched exact-parent baseline](receipts/baseline-catalog.log) |
| Inherited source byte audit | PASS,15+96+12=123 manifest files unchanged from exact parent;11 PR ancestry edges verified | [raw audit](receipts/source-audit.log) |

The catalog failure is baseline, not silently repaired or reported as passing.
No source, historical theorem, global catalog or workflow was changed.
The full suite used Python3.13.13, test extras in an isolated ignored `.venv`,
one BLAS thread,1024MiB address-space cap and2400s timeout. Exact argv,
timestamps, environment versions and output hashes are in the receipts.

## Focused and independent checks

New focused tests: **57 PASS** =12 identification +15 Gauss +16 signed
+14 geometry. Inherited focused tests: **51 PASS** =18 Gamma parent
+14 prime-power transport +19 Stoneham/transfer parent. These are separate
from the10,008-test repository discovery, which scans `tests/`.

- Identification: separate symbolic inverse/69-minor oracle; exact all-time
  polynomial proof; fresh k5/9/13/17, time2/7/31/97/257 and jets0..8.
  [tests](receipts/identification-tests.log), [oracle](receipts/identification-oracle.log).
- Gauss:17 full products and GK unit rows,119 separately reconstructed sums,
  13 cofiber comparisons,10 prime-power births; all four odd-prime classes.
  [final tests](gauss/focused_tests-final.log), [oracle](gauss/independent_receipt.json),
  [extra probe](gauss/extra_receiptcorrected.json).
- Signed:2,107 cofiber reconstructions,42 certified energy rows (36 fresh
  eligible),15 minimum-energy certificates,18 vacuous completion bounds,
  413 exact approximate-grid exclusions,18 typed controls.
  [final tests](signed/focused_tests-corrected.log),
  [separate oracle](signed/independent_oracle_receipt-with-grids.json).
- Geometry:14 tests,16 exact golden-root brackets, independent Beta oracle,
  four positive-integral root checks, Mellin/Oily audit, full16×16 Walsh/carry
  tensors. [Detailed validation](geometry/VALIDATION.md).
- Direct diagonal applicability:10 independent authentic first-birth
  rational witnesses. [Raw output](receipts/direct-diagonal.log).
- Complementary Gauss review also executed1,680 cofiber/order assertions,
  60 cyclotomic degree checks and11 exact Ramanujan traces.
  [Review receipt](signed/gauss_review_receipt.json).

Separate implementation is not independent mathematical authority. The agents
share model/context lineage. Universal claims rest on the written proofs;
high-precision comparison is calibration, not an interval proof. New research
theorems have not been formalized in Lean or externally refereed. GK unit
power checks do not independently fix the classical uniformizer root choice.

## Preserved failures and reviews

The first conductor2 grid assertion failed at j5; corrected dynamics retain
two transient steps1/32,1/2 before zero. Both failed executions and corrected
runs survive with an explicit filename relocation map in
[FAILED_CONTROLS](signed/FAILED_CONTROLS.md).
A separate Gauss probe failed JSON serialization after its assertions;
[failure and repair](gauss/INITIAL_FAILURE.md) preserve the raw traceback.

Complementary proof reviews: [root algebra](geometry/ROOT_IDENTIFICATION_REVIEW.md),
[Gauss multiplication/fiber](geometry/GAUSS_REVIEW.md),
[Gauss conductor/trace](signed/GAUSS_ADVERSARIAL_REVIEW.md),
[signed global minimum](gauss/SIGNED_ENERGY_REVIEW.md).
The geometry review's addendum says AT-04 when citing the birth theorem;
the correct identifier is **AT-03**, as in the actual DF proof. Its mathematical
birth formula is unchanged. The final J-fixed corollary was added after the
Gauss reviewed hash: root checked it directly from `A+4C=5t` on `c+t e`.
No claim of an external or blind review is made.

## Live refs and hosted CI

[Initial metadata](receipts/initial_remote.json) and
[refreshed metadata](receipts/refreshed_remote.json) pin actual heads/bases
for390–400. All remain open drafts. Parent400 still has the exact SHA above;
397's current head is992b3f9d..., not its stale c884... snapshot.
The refresh records all four workflows successful for390,391,395,396,398,399,400;
397 has three successful and full validation in progress. No runs were
returned for392–394, including initial all-event API checks: **not passed**.

This pre-delivery snapshot predates the new child commit. Its own exact-head
CI status is reported in the draft PR after push; parent CI is not child CI.
The inherited core Lean workflow does not formalize these new paper proofs.
All raw logs, source manifests and proof/oracle files are hash-indexed by
`SOURCE_MANIFEST.json`; `validate_artifacts.py` checks them and local links.
