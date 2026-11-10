# Operation Main XXII — integration audit (2026-11-09)

**π base-16 normality: OPEN. Original-zero hexadecimal parity balance: OPEN. RH: OPEN.**
No mathematical status is promoted by integration. Main merge is conditional on complete
required validation and reviewed exact-head GitHub checks. This document records the integration and stable-candidate validation checkpoint.
The exact final-head decision and receipts are attached to [PR #575](https://github.com/femboy2112/SUCC/pull/575); incomplete gates remain incomplete until those receipts exist.

## Baseline, isolation and authorization

Fetched main is `43a607818907120d4cdab73d240f5b4d7700b63f`, matching Main XXI's certified
baseline. The active `/home/leah/SUCC` checkout remains on that main with its untracked
`.claude/` preserved. Work is isolated in `/home/leah/SUCC-main-xxii`, branch
`integration/succ-main-xxii-aphex-haar-parity`, draft PR #575. The maintainer explicitly authorized scoped
commits, pushes, draft integration PR and a main merge only after the stated strict gates.
No force-push, branch deletion, archive rewrite, tag, release, license or publication.

Frozen manifest blob: `a8805a8e4d64f35ff61937a36755d9b6d1ba3fae`.
The [manifest](SUCC_MAIN_XXII_INTEGRATION_MANIFEST_2026-11-09.json) records the before/after
formal/provenance tree SHA256 and every remote head. Source forcing and literal U0=0 are
unchanged; the frozen originating import commit is
`ba075348b7bcc66d938b3e0ca96c26e95bba340a`. Import provenance and research-head provenance
are distinct records.

## DAG and coverage

The freshly fetched inventory has **28 open PRs, 11 ancestry-minimal PR leaves**:
#544, #547, #549, #550, #551, #553, #555, #561, #569, #570, #574.
All 18 cross-leaf path overlaps have identical blobs. All leaves were merged with explicit
`--no-ff`; every second parent was checked against its audited head. All 28 heads are now
ancestors of research staging `4a09e0de933e884884e77bfd4285cd212470d481`.
The inventory tool had one real defect: for a research fork older than current main it
used current main as the own-diff base, falsely charging the branch with deletions of later
main files. It now uses the Git merge-base; an isolated divergent-history regression passes.
The raw pre-repair inventory is historical; the coverage manifest has corrected #544 ownership.
The complete manifest records head parents, own and inherited commits, own files/blobs,
exact-head historical CI, carrying merge, scope and disposition.

The full remote inventory contains **569 refs**. PR-less heads are recorded separately:
all changed blobs present elsewhere are DUPLICATE-CONTENT; unresolved historical differences
are DEFER, with their exact branches and files retained. The unique inverse-charge Laplace
preregistration at `fd5ef563148cf805da112c8b05aeabcb62f578b9` is integrated by a twelfth
explicit merge. It is an **unexecuted protocol**, not a new experimental result.
The prime-three-channel tomography sibling at `34403d5c` has eight byte-identical paths in
#554 and no unique file content. No historical branch is deleted or silently certified.

## Mathematical review

Read-only same-model proof and adversarial reviews cover every incoming cluster:
[parity](main_xxii_evidence/parity-audit.md), [Gamma/prime/Haar](main_xxii_evidence/gamma-audit.md),
[carry/geometry/entropy/RH](main_xxii_evidence/other-audit.md).
These methods and independent code oracles share sources and model lineage; they are not
external refereeing. The [claim supplement](CLAIM_SUPPLEMENT_MAIN_XXII.md) records repairs
without editing archived dossiers.

Strongest new imported finite conclusion: the calibrated two-fiber identity and sharp
source-relative certificate P=beta+m*t, |P-beta|<=|m|, plus sharp precision payment.
Its prime marginal input remains conditional on #554; the all-epoch complementary contrast
is OPEN. The complete rational p-integral wrong-seed control is epoch-dependent and has
contrast 2 and zero fitting loss. The exact refutation is of seed-blind descent/low-loss
inference, not of the original-zero conjecture. Local prime Haar, binary conditional Haar,
full future-conditioned sixteen-child Haar and real Haar have different domains.

Additional corrections: #554 fixed-Gram frequency qualification and averaged seed error;
#572 Fourier-series midpoint convention at jumps; finite-sample collision floor separated
from excess; #567 NONREPLICATION retained; source-only Gamma invariants separated in the
[typed definition table](MAIN_XXII_GAMMA_OBSERVABLES.md). RH #550/#553 remain a separate
program with completed source and unresolved signed positivity.

## README and history

Original README: **44,157 bytes / 543 lines**, Git blob
`96e71e9df1eb92d64c5d99b8a68520a3c4853094`, SHA256
`95e3f33f6ecf196748532246739d9292a11fdb6d8fe023abcbb20c7a4f9491a9`.
It is preserved byte-for-byte in [the dated archive](archive/README_PRE_MAIN_XXII_2026-11-09.md).
The #547-corrected intermediate README is also archived (blob `b2f609c7d4705e0e3f5271ad92c7ac490bf61274`).
The new landing page is approximately 8,900 characters, starting with theory and status, then objects, BBP, current frontier,
toolkit, executable quickstart and documentation. [History index](RESEARCH_HISTORY.md)
resolves all 145 original README link targets from the original repository root and adds
per-PR primary dossiers. Frozen archive-relative links are not modified inside original bytes.
The maintained frontier has a Main XXI snapshot and a new Main XXII hierarchy.

## Validation record and current gate

Evidence directory: `/home/leah/succ-main-xxii-evidence` (raw logs, commands, timings,
exit codes, dependency environments, CI job records and commit receipts). Selected durable
receipts are copied under `docs/main_xxii_evidence/` before final publication of this branch.
Thread limits are 1 for BLAS/OpenMP; heavy checks run serially on this 7 GiB machine.
Clean Python environments: 3.13.13 and 3.10.20 with editable package install and declared extras.
mpmath 1.3.0, sympy 1.14.0; numpy/scipy 2.5.4/1.18.1 (3.13), 2.2.6/1.15.3 (3.10).

Completed at research staging: **658 focused root tests, Python 3.13, PASS** (48.948s).
#544 focused subdirectories, artifact hashes, four Std Lean identities and #551 independent
SymPy oracle replay PASS. Separate parity review ran 55 canonical-source tests and 5,208
exhaustive small sign-pair streams. A512 is reused data, not a fresh holdout.
Historical branch-local validate.py asserts no shared changes since its START; individual
commands were replayed on integration rather than weakening that historical assertion.

**Stable candidate native PASS:** commit `9eafeaa85d9920a12e62ef2e8b755575ef4b6986`,
Python 3.13.13, 12,806 tests in 1176.982s, exit 0. Raw log and command receipt:
[`full-candidate313.log`](main_xxii_evidence/full-candidate313.log),
[`full-candidate313.json`](main_xxii_evidence/full-candidate313.json).

Both supported versions passed 658 focused root tests and 268 tests across 34 incoming
research directories. The inventory regression passes on Python 3.10 and is also included
in the full native run. Provenance, observer and ordinal gates pass on both versions.
The selected-branch Lean regression kernel-checked 10 declarations and rejected all four
paired false controls. The four new #544 Std identities also kernel-check; neither result
certifies an analytic normality theorem. Original-source 65,536 and 131,072 digit receipts
recompute with two guards; the #567 NONREPLICATION result is retained. Signed and retro
receipts replay identically. Catalog: 2055 rows, 179 namespaces, 1921 registered rows,
170 inherited warnings; typed graph 51 nodes / 60 relations.

**Final-head gate:** run the full Python 3.10 native suite after the documentation/evidence
commit, then inspect every hosted check on that exact head. To avoid changing a tested head
merely to record its own result, the final run logs and SHA receipts are committed to the
separate `evidence/succ-main-xxii-final-validation` branch and linked in PR #575. That evidence
branch is a receipt carrier, not another research integration or proof promotion. Never infer
a final-head pass from this checkpoint document alone.

Full final-head validation and hosted integration checks must be completed and
recorded before a main merge. Historical CI failures on #552/#553/#554 are retained:
setup-python failures and Lean toolchain-download failures occurred before mathematics.
Even a step named “Kernel” failed in `lean --version` downloading pinned 4.14.0; raw log
`lean-job-128699492273.log` records this. These are infrastructure failures, not proof passes.
Cancelled historical runs remain cancelled.

Raw GitHub logs retain their original trailing spaces/ANSI bytes; inherited research
Markdown/CSV whitespace is also preserved. The complete diff-check receipt names 84
whitespace lines. These are retained data bytes, not a claim of a clean aggregate whitespace
check. The newly authored source and maintained prose have no such defects.

GitHub Markdown API and actual Chromium inspection at desktop 1440px/mobile 390px verified
rendering and no document-width overflow. The final source/recurrence split improves mobile
readability. Final-page repeat receipts and screenshots accompany the final-validation branch.
An initial detached-DOM scroll and an incorrectly shadow-DOM-only math probe were instrument
failures, corrected before accepting the MathML check; see the rendering instrument note.

## Next round and closure policy

[Next-round protocol](MAIN_XXII_NEXT_ROUND.md): source-selected all-epoch conditional
contrast bound, then fresh zero-seed/control experiments at A=1024,2048,4096 under a frozen
selector. No new parity responses at those epochs were accessed here.
Only after a successful authorized merge and independent main verification may research
PRs close, and only when their **live heads** are proven ancestors of merged main. Each
comment must name the carrying merge. Branches stay. Failed/incomplete gates leave the
integration draft unmerged with exact blockers.
