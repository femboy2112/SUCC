# Periodic/mixed-lag continuation: validation and authority receipt

Parent #317: `848bad224fef455a9f87ed19e947c936d309c965`.
Published branch: `research/periodic-mixed-lag-source-2026-10-27`.
Execution worktree: `/media/leah/SPANKBANK/SUCCYBOI/SUCC-carry-defect`.
Publication worktree: `/media/leah/SPANKBANK/SUCCYBOI/SUCC-periodic-mixed`.
No main change, merge, release, sibling import or archival replacement.

## Native validation

| Check | Actual result |
| --- | --- |
| New focused tests | 38 passed in 3.908 seconds |
| New tests plus parent scalar core | 49 passed in 4.958 seconds; source-hash wrapper 5.157 seconds |
| Claim namespace checks | 15 passed in 0.082 seconds |
| Full native unittest discovery | 8982 passed in 1080.346 seconds; wrapper 1087.178 seconds; exit 0 |
| Provenance verification | Passed, 72 items; exit 0 |
| Observer foundations probe | Passed, exit 0 |
| Ordinal successor report probe | Passed, exit 0 |
| Exact receipt | Write and byte-for-byte replay passed |
| Receipt mutation controls | False normality, foreign source hash and false exponent margin rejected for their intended reasons |
| Lean | Four finite declarations and four paired positive/false controls; KERNEL_CHECKED |

The isolated Python 3.12 environment installs the complete native project
with `pip install -e '.[test]'`. All 1,295 production/test Python files were
frozen before full discovery. Each gate's reproducible harness records its
literal command, raw log, exit status, wall time, log hash, and before/after
source hashes. The full run also records every file hash. Paper and separate
proof/replay instruments were completed while that immutable suite ran.
The completed full suite verified every frozen hash. Its raw log SHA-256 is
`bca4882aaafe3cd5ca7dddc1b24e18073ac150d0b9f3433ce372c27a7a7601f5`.

```sh
python research/2026-10-27/carry_defect_validation/run_native.py focused
python research/2026-10-27/carry_defect_validation/run_native.py provenance
python research/2026-10-27/carry_defect_validation/run_native.py full_unittest
python research/2026-10-27/carry_defect_validation/run_native.py observer
python research/2026-10-27/carry_defect_validation/run_native.py ordinal
python scripts/carry_defect_probe.py --verify
python research/2026-10-27/carry_defect_validation/audit_receipt.py
python research/2026-10-27/carry_defect_validation/audit_final.py
```

The harness invokes the four required repository commands without source
interface shims. Results and raw output are in
[carry_defect_validation](carry_defect_validation/).
The receipt's budget at large $N$ is explicitly **conditional on a valid onset**;
none of its sample integers is advertised as a proved numerical π threshold.
The infinite mixed-tail holdouts include rational outward remainders.

## Kernel scope

The [kernel receipt](carry_defect_validation/lean/kernel-observation.json)
identifies Lean 4.14.0, compiler `410fab728470`, pinned mathlib
`4bbdccd9c5f862bf90ff12f0a9e2c8be032b9a84`, all dependency revisions,
checked source hashes, exported declaration types and axiom lists.
The existing compatible cache at `/home/leah/SUCC-rf/formal/mathlib_bridge`
was inspected and used read-only. Compilation was serial with a 2 GiB cap.
Only `propext`, `Classical.choice` and `Quot.sound` occur.

The four declarations are the signed finite endpoint identity, modal-pair
budget, scalar modal-loss implication, and periodic terminal identity.
The paired controls reject a wrong endpoint sign, missing pair factor,
false scalar coefficient and reversed terminal forcing sign.
The checker reports no unexpected failures.

The full Green inverse/cut sweep, integer branch construction, arbitrary
complex templates, BBP integrals, irrationality measure and analytic limits
are **not** formalized. The receipt's Git HEAD is the parent because the
new files were checked before their commit; their recorded source hashes
identify the actual checked input.

## Independent checks, provenance and limitations

The principal and three delegated research fronts share a model family;
their cross-review is not external peer review. Independent mathematical
and implementation bearings include literal four poles versus a collapsed
rational source, recurrence versus direct weighted source sums, subset
versus polynomial filter expansion, exact tridiagonal inversion versus
Gauss–Jordan, and certified Fourier intervals versus rational carry bounds.
See [the hostile review](MIXED_LAG_REVIEW.md).

An attempted read of the carry dossier preceded the worker's file creation
and returned file-not-found; the completed file was then read. This was a
tool timing error, not a mathematical failure. The full suite retains
inherited Python escape/deprecation warnings instead of suppressing them.
GitHub rendering audits found unrecognized inline math adjacent to prose
hyphens and Markdown emphasis interference with asterisk/subscript syntax.
Whitespace, named star symbols and a displayed operator equation repaired
the expressions. The strengthened audit rejects dollars outside rendered
math and code, and checks every claim-table column. The initial failures
were formatting failures, not passing evidence.
Failed mathematical shortcuts and their actual witnesses are retained in
the proof dossiers and mutation logs.

The [remote baseline](carry_defect_validation/remote_baseline.json) pins
the live heads of #306–#317 and the parent CI snapshot. Parent #317 had four
scoped workflows passed, full native validation running, and a cancelled
duplicate push run at the continuation's start. These are parent results,
not evidence for this child. Child exact-head CI is reported in its PR after
the coherent validated push, without promoting pending runs to passes.

A [final parent audit](carry_defect_validation/parent_ci_final.json) found
Python 3.13 passed, while Python 3.10 was cancelled after exceeding the
25-minute job limit. GitHub's check annotation explicitly identifies that
timeout. A patch proposes raising only the full-suite job timeout to 45
minutes; all test commands and both Python versions remain. The connector's direct
job-detail endpoint was unavailable, so job-list data and the `gh` check
annotation endpoint supplied this diagnosis. This correction addresses an
observed validation limit, not a claimed mathematical failure or pass.

**Publication permission boundary.** The first commit,
`e9b14db72a5c9d79b4dd37a204a206a31df549a3`, included that timeout fix.
GitHub rejected its push because the OAuth credential lacks `workflow`
scope. That commit is preserved locally on
`research/carry-defect-coercivity-2026-10-27`; no force push or history rewrite
was used. The publication branch was created afresh from the same verified
parent, with the exact research diff and unchanged workflow. The timeout
proposal is retained as a [reviewable patch](carry_defect_validation/ci_timeout_proposal.patch),
**not an applied hosted change**. Every production/test byte still matches
the completed full-suite snapshot, and the final audit checks this in the
publication worktree. The full suite is not spuriously attributed to a
second execution. Publication notes and rendered-document hashes were
updated and checked separately.

The handoff and source map were read before research. Main remained at
`6dd80730c3575d91f746546a25da5aedbd2e2737`. This child extends #317 directly;
no concurrent sibling was merged or impersonated. The reviewable state is
delivered as a stacked draft. **Normality, superlogarithmic absolute loss,
and a certified numerical onset remain OPEN.**
