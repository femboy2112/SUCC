# Cambrian publication verification and concurrent siblings

## Publication identity

Draft PR51 was first published as010dcdd14d519a533d285e4ed3fee736e5991175,
with tree4549f54fc4f3fa7c64f88a0ce52c920dca209443 exactly matching local
08b73af1b5d98bfbc3fae58e2f22f4a03eed26d7. Native git push stopped for lack
of command-line credentials before changing any remote reference. The connected
GitHub API published the identical tree. The Git bundle in provenance/cambrian
preserves the actual original worker/audit/integration objects and was verified.

## First remote CI correction

At initial head010dcdd, the official unmodified Lean runtime accepted all nine
production modules, all65 printed theorem dependencies, the independent positive
appendix and all four intended false-proof rejections. The final inherited
substring scanner nevertheless failed: it found `admit` inside the English
comment `countdown admits depth d` in EODCS_CambrianRealization.lean.

Run38364586119, job115186550112, records that exact separation: kernel checks
and the portable audit passed, then the text scanner failed. The publication
fix scans uncommented Lean tokens using the already-audited nested-comment
stripper and token boundaries. It still rejects sorry, admit, axiom, unsafe and
native_decide tokens. Positive comment/identifier and negative nested-comment,
placeholder and custom-axiom controls pass locally. No theorem statement, proof
source, frozen mathematical receipt or source hash was changed for this repair.
The initial failure is retained; final-head workflow results belong to the PR.

## Concurrent sibling snapshots

PR49 and PR50 were created during this campaign from the same PR48 base. They
were discovered during the final publication refresh, not used as unacknowledged
inputs to the already frozen six-worker derivations. Both remain independent
draft lines; none of their branches, files or defaults was modified.

| Draft | Inspected head | Relationship |
|---|---|---|
| [49](https://github.com/femboy2112/SUCC/pull/49) |42d97e4f7abe778b2fa9852560f4fd25afbeb797| Source-pinned atlas; witness-aware base change and faithful quotient actions |
| [50](https://github.com/femboy2112/SUCC/pull/50) |2e1bda55799e1e1f2c516e472c4fa169fc9692f8| Executable histories, source repair, stochastic descent and completion |

At these snapshots both preserve the exact original O1–O638 ledger blob
f0dc83d9e2d37874e35932db72570ddeba044684; neither allocates our O639–O679.
Their supplementary SWM namespaces must be reconciled before any future merge.
PR50 also reports its own B09 product-topology completion and compact-source
formalization in an isolated mathlib4.14 lane. That contribution is separate
from our finite-branching theorem and was neither imported nor recompiled by
this campaign. Its exact source/toolchain/CI correspondence must be checked
before reuse; the next topology task is reconciliation and extension, not
claiming that no sibling formalization exists.

In particular, PR50 C17 independently covers the same classical joint-law
fiber criterion, paired-law repair and finite sequential conditioning as much
of ST1–ST6. Its quantum and filtered-fluid work also overlaps campaign themes.
This is duplicate classical/project-level mathematics, not evidence of priority
or an additional independent external referee. PR49 A01 distinguishes Boolean
weak-pullback surjectivity from witness-family bijectivity; our subset-relation
presentation does not absorb that distinction by renaming it.

A future integration should compare theorem hypotheses and exact maps before
combining implementations or allocating a unified supplementary claim namespace.
This draft retains its pinned PR48 base and all sibling source provenance.
