# Global Signed validation and authority receipt

Parent #316: `239df54f5f56fdaba3bf4edfc282cdcabecea3c2`.
Branch: `research/global-signed-source-2026-10-27`.
Worktree: `/media/leah/SPANKBANK/SUCCYBOI/SUCC-global-signed`.
No main checkout, merge, release, sibling import, frozen archive change,
or historical authority-catalogue modification occurred.

## Native execution

The local Python 3.12 environment uses `pip install -e '.[test]'` in an
ignored worktree `.venv`. These results use the entire native repository,
not the source-interface shims used by the parent author's local tests.

| Check | Actual result |
|---|---|
| Focused new modules plus parent WTF tests | 42 passed, 3.729 seconds including source-hash wrapper |
| Full native unittest discovery | 8,944 tests passed in 1,149.370 seconds; wrapper 1,159.073 seconds; exit 0 |
| Provenance verification | Passed: 72 items, 17 byte-identical archives, 55 namespace migrations |
| Observer foundations probe | Passed, exit 0 |
| Ordinal successor report probe | Passed, exit 0 |
| Claim-namespace focused checks | 18 passed, 0.128 seconds |
| Exact receipt | Write and byte-for-byte replay passed |
| False receipt controls | Separate replay rejects false normality, foreign source hash and false loss constant |
| Lean | 13 finite declarations, seven paired positive/false controls, KERNEL_CHECKED |

The reproducible native harness records the actual command, raw combined
output, exit status, wall time, SHA-256 and before/after hashes of all
1,289 production/test Python files. Production and tests were frozen before
the full suite. Later work was restricted to research documents and separate
replay instruments. The final full-suite record verifies all frozen hashes.
Its raw log SHA-256 is
`edea4826f0937d9a916c3e324cad3c9cef080db6fb932f4304eb8d0c43d8f9dd`.
See [the completed result](global_signed_validation/full_unittest_result.json)
and [source snapshot](global_signed_validation/python_source_snapshot.json).
GitHub's actual GFM renderer accepted all eight research/handoff/ledger
documents; local links, math delimiters and the ten-row four-column claim
table passed. Production and tests were not modified after the successful suite.

```sh
python research/2026-10-27/global_signed_validation/run_native.py focused
python research/2026-10-27/global_signed_validation/run_native.py provenance
python research/2026-10-27/global_signed_validation/run_native.py full_unittest
python research/2026-10-27/global_signed_validation/run_native.py observer
python research/2026-10-27/global_signed_validation/run_native.py ordinal
python scripts/global_signed_probe.py --verify
python research/2026-10-27/global_signed_validation/audit_receipt.py
```

The harness invokes the required repository commands unchanged using its
Python interpreter. Finite replay uses exact integers/Fractions and native
Machin/Taylor outward intervals. Its receipt explicitly reports no certified
numerical onset, no new asymptotic order and no normality proof.
The Green countermodel's finite holdout bounds the complete infinite tail
by a rational remainder; it does not substitute a finite truncation for the
irrational seed. The prime-jet holdouts are labelled changed forcing.

## Kernel scope

Lean 4.14.0 and the pinned mathlib revision
`4bbdccd9c5f862bf90ff12f0a9e2c8be032b9a84` were checked, together with
every package revision and tracked dependency cleanliness. The compatible
cache was used read-only at `/home/leah/SUCC-rf/formal/mathlib_bridge`.
Compiler execution was serial (`-j 1`) with a 2048 MB memory cap.

The [receipt](global_signed_validation/lean/kernel-observation.json) exports
all 13 finite declaration types, hashes and axiom lists. Only `propext`,
`Classical.choice` and `Quot.sound` occur. Seven paired true/false controls
check missing hypotheses, endpoint and coefficient errors, and the quiet
scalar contradiction. The compiler checked the exact source identified by
hash before it was committed; the recorded Git HEAD is therefore the parent.
The source hashes, not an implication that the parent contained new files,
identify the checked declarations.

No kernel authority is claimed for the integer-branch construction, complex
norm comparison, Taylor inequality, BBP integrals, classical irrationality
measure, infinite prime family, Green limits or normality. The finite core
and the full analytic theorem have different authority.

## Independent checks and retained failures

The principal and three delegated fronts cross-reviewed the proofs and
constants. They share a model family and are not external peer review.
Independent implementation bearings include literal versus integer-carrier
source replay, generic finite inequalities versus outward trigonometric
intervals, and cyclotomic reduction versus rational Ramanujan counts.

The first Lean elaboration failed at an incorrectly targeted sum rewrite;
the final explicit rewrite checked successfully. Its initial log was
overwritten by the checker, so no reconstructed raw log is claimed. The
failure and cause are preserved in the formal dossier. Two read-only
`git show` calls used guessed sibling dossier filenames that did not exist;
the actual paths were discovered and read. A documentation patch initially
failed atomically on the case of `Claim Index`; it was corrected with no
partial edit. These were tooling failures, not passing evidence.

The successful full suite emitted inherited Python escape/deprecation warnings;
these remain in its raw log and were not suppressed to manufacture a pass.

A late targeted provenance search found the factor-289 forcing norm
argument already in PRK-02 (`eca4462e`). The final dossiers explicitly
credit that argument and its earlier quadratic-band consequence. The new
claim is narrowed to the unit-center refinement, stated moving-band
estimates and stronger counterexample; no duplicate identity is counted
as a second arithmetic constraint. The separate quiet-transition
improvement from $1/29$ to $1/14$ is unaffected.

## Remote state and communication

[Initial remote evidence](global_signed_validation/remote_baseline.json)
pins #306–#316 and the exact-head parent CI. At that snapshot, #316's
Institute, One Object and Collective workflows passed, while its two
native validation runs were in progress. A subsequent exact-head check
found #316 native run `40438884030` passed and duplicate `40438890349`
cancelled. Sibling #315's native run passed; both #311 native runs were
cancelled, while its scoped checks passed. These are parent/sibling
results, not validation of the child. Full records are in
[the updated CI snapshot](global_signed_validation/parent_sibling_ci.json).

Coordination was posted on #316 as authorized by the user, identifying this
isolated research lane and the updated #315 head. Claude's integration lane
was not impersonated or presumed complete. The reviewable state is pushed
once after local validation and opened as a stacked draft against #316.
Exact child CI is reported in the PR and final response after it exists;
no inherited or pending run is called passed.
