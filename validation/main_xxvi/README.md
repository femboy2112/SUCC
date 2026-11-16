# Main XXVI exact-candidate validation evidence

Validated commit: `554de88c17a09fc24777fbe5101730dbd6b44ebf`.
Validated tree: `ae89bcfb3d912098f0a27143ec3f411ca868e309`.
Integration PR: [#656](https://github.com/femboy2112/SUCC/pull/656).

Local validation PASS: native 14476 tests run / 2 skipped / zero failures; XXIV 21 commands and 148 research tests; XXV 12 commands, 249 research tests, five probes plus pinned Lean; XXVI 20 commands, 566 research tests and five explicit probes. Counts overlap in subject matter and are not independent proof votes.

`summary.json` gives the compact status. `receipts.tar.gz` preserves raw logs, command exits, exact-head/tree receipts, actual environments, regenerated numeric outputs, Lean source/axiom/mutation receipts, and the retained historical XXV snapshot failure with all eight paths reconciled to exact later donor601. Large individual JSON outputs are additionally losslessly gzipped. `archive_manifest.json` authenticates stored archive members. Source-copy mirrors and downloaded toolchains are not duplicated; their pinned source hashes and recipe are in the receipts.

Hosted CI is tracked separately in `hosted_ci.json` when the completed snapshot is available. This evidence branch is separate from main so that recording results does not change the validated source tree. Passing finite tests and scoped Lean encodings do not establish pi normality, R0, Goldbach, RH or a continuum Yang–Mills result. Paper proofs retain their declared authority.


## Completed integration

PR #656 merged to main `81be6b897ae980b801a3b9de9e22ef81e8360bfb`; main tree is byte-identical to the validated candidate. All54 source heads and92 protected paths passed postmerge verification. See `postmerge.json` and its raw logs.

Hosted CI passed all12 expected workflows and all30 jobs/checks at the exact candidate. Both Python3.10 and3.13 native suites ran14476 tests with2 default-PATH skips and passed. `hosted_ci.json` identifies every run/job and the actual synthetic merge tree; `hosted_ci_receipts.tar.gz` preserves metadata and both raw native logs. The two skipped local Lean cases were separately executed:2 passed/0 skipped, verified Lean4.14.0; see `skipped_lean_receipt.json` and `skipped_lean_logs.tar.gz`.

The original local receipt archive is immutable and contains its contemporaneous pending-CI status. Current completion is recorded in the adjacent `summary.json` and hosted/postmerge receipts. No mathematical all-shell saving was established; R0 and pi normality remain open. The new main push starts its own CI repetition, which is distinct from the completed exact-candidate gate.
