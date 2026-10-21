# Academic Main VIII integration audit

This is a live integration record for [PR #219](https://github.com/femboy2112/SUCC/pull/219).
The starting main is `b5f9591033db2022bda6a2f16a935c06466f9eff`.
Final merge and validation receipts are recorded separately; this document
does not turn a historical branch test into a combined-head test.

## Incoming graph and independent review

All five heads independently descend Main VII; none is an ancestor of another.
Each is retained as an original merge parent, with no cherry-picking or
squashing of its source history. Only README and CLAIM_INDEX overlap, between
#212 and #218; both mathematical domains and warnings were retained.
The [machine-readable baseline](live_dag_and_coverage.json) records exact
heads, trees, ancestry, file coverage and intersections.

| PR | Exact reviewed head | Verdict and evidence |
| --- | --- | --- |
| #211 | e8c12ca0eac57dcffce59747ad160330f6225756 | Nine exact-type kernel observations; rebuild and installed authority admission required |
| #212 | 04dc97022d4b75e8d229128de50509c413d86b8b | Effective mean and t>=1 obstruction survive [independent reconstruction](../../research/2026-10-21/MAIN_VIII_ARITHMETIC_AUDIT.md) |
| #214 | 9372c669892a2a29fb8c16f0fa20c11815f650df | Cofactor/exterior/simplex claims survive [geometry](../../research/2026-10-21/MAIN_VIII_GEOMETRY_AUDIT.md) and [hostile](../../research/2026-10-21/MAIN_VIII_HOSTILE_AUDIT.md) reviews |
| #213 | d3e0ccf671b2ddc2a9e94549db77f60955ee7580 | Original-source moment-Gram theorem and fixed-budget ceiling reviewed; signed S4 sign remains open |
| #218 | 8f9444c3984e4b981422d400c4c3ebde7a0a6715 | Retained subject to exact input guards and separation of ideal polygon width from computed interval width |

These are separate same-model reviews with independent derivations and exact
oracles, not external academic refereeing. Original archived sources remain
byte-identical. Existing reports preserve their original evaluated heads.

## Repairs and authority boundary

The repaired pi transport API rejects floating inputs that can underflow a positive
error budget to zero. A rounded polygon enclosure must use its actual rational
width: at depth 1, precision 1, the returned [2,4] has width 2 while the ideal
polygon bound 64/8^2 is 1. The enclosure itself is valid; substituting the ideal
bound into its computational transport budget is not.

The formal pipeline serially rebuilds three pinned projects and exports 19
actual theorem types, with axiom checks and negative elaboration controls.
Changing this generator invalidates the old record's current-source hashes.
The first candidate therefore intentionally fails closed until the coordinator
reviews real hosted output and installs the new record digest. A JSON success
flag or a theorem name cannot admit itself. Historical records remain archived.

## Combined gates

Merge requires exact combined-head Python 3.10 and 3.13 suites, genuine pinned
Lean builds, actual catalogue admission, all hostile controls, namespace
uniqueness, packaging/import checks, source provenance, source-specific checks,
and the new Main VIII metadata gate. Failed and incomplete intermediate runs
must be included in the final receipt. A finite test suite does not prove
universal software correctness.

The maintainer authorized history-preserving mainline integration after these
gates. New speculative research is separately reviewable; no publication,
release, licensing change or archive rewrite is authorized by this integration.

## Observed formal admission

The actual 19-export build and five negative controls passed in hosted run `39546972269`; its overall admission step initially failed against the old environment. After inspecting the real output and matching all 21 source hashes and all 19 prior theorem exports, the coordinator admitted the new record. See [full admission review](../../formal/kernel_audit/MAIN_VIII_ADMISSION_REVIEW.md). Combined-head rerun remains a separate required gate.
