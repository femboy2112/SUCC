# SUCC Main XXVI — recovery and integration audit

This audit describes the assembled candidate. Completed final-candidate command receipts,
immutable commit/tree, hosted checks and final main verification are attached to the integration
PR and preserved on [`integration/succ-main-xxvi-validation-evidence`](https://github.com/femboy2112/SUCC/tree/integration/succ-main-xxvi-validation-evidence).
This separate evidence ref avoids adding a self-referential receipt to the tree being tested.
The existence or success of a planned receipt is not asserted by this document: read its actual
status, command exits and exact commit. Merge is authorized only after the required gates pass.

## Recovery and reused artifacts

The live initial main and remote integration branch were both
`db9fb4b84672050efa79b13377f1e73364598a14`, tree
`4b0dc4572a1f971d83e23125ee14cfb06cbb0b8b`. GitHub returned 54 open PRs, highest #655.
The earlier unpublished six-layer tree and original 178-line failure receipt were unavailable
in accessible scratch/tmp/home. Ten existing SUCC worktrees were clean and left in place;
no reset, deletion or shared history rewrite was performed. Locally divergent historical
prime-observer head `599c55ef8b656976a1bb375bb94dd711b5aa9faa` was recorded, not substituted
for the published donor.

Reused: exact published commits, trees and parents; source dossiers, proofs, controls and
historical receipts; Main XXIV/XXV manifests and frontier; frozen import provenance.
Reconstructed: the combined six logical layers, manifests, canonical atlas and final validation.
The earlier candidate was not silently assumed recovered or independently validated.

## Ancestry, conflict resolution and dispositions

All 54 heads are ancestry inputs, carried by 20 maximal tips:
#600, #601, #604, #605, #606, #607, #609, #610, #611, #612, #615, #616, #617,
#621, #622, #644, #652, #653, #654 and #655. Intermediate stack heads are included
once through ancestry. Matching statements and shared proofs are one provenance family.
Exact per-head commit/tree/parents, nearest ancestor, unique/inherited blobs and final bytes
are machine-recorded in the [manifest](SUCC_MAIN_XXVI_INTEGRATION_MANIFEST_2026-11-16.json).
The [disposition map](MAIN_XXVI_PR_DISPOSITIONS.md) enumerates every active PR.

Mechanical catalog conflicts were resolved by deterministic regeneration from the complete
tree. Independent additive entries in the canonical ledger were both retained. #605 and
#606 independently used `holographic_boundary_filters/CLAIM_LEDGER.md` and `NEXT.md`;
both contributions and distinct claim namespaces are retained with an explicit continuation
boundary. The manifest declares these repairs, the source corrections below and canonical
frontier updates. Frozen archival originals are unchanged.

## Mathematical reconciliation

1. **Gauge:** #648's assertion that `g(n)=2n²` changes π is refuted by exact telescoping.
   #651's correction is adopted: `U'=U+g`, `T'=T−g`, same completion, different arithmetic
   presentation. Source passport rejection and real-target separation are distinct.
2. **Gamma:** original-source attenuation, complex phase transport and moving-frequency
   cancellation retain their scoped proofs. The coherent wrong seed has the same source
   windows and no fixed-frequency cancellation; a forcing-only Weyl inference is refuted.
3. **Observation order:** expectation, exponential, norm, floor, extraction and conditioning
   remain distinct maps. Original BBP coin counterexamples, source sharing and independent
   references are preserved; no nonlinear interchange is authorized.
4. **Detectors:** all-mode/Haar/lag equivalences are instruments. Their required asymptotic
   estimates remain unpaid. Positive marginals and full inverse maps do not imply normality.
5. **Carry:** #652's matching-mask tail transfer, exact 7/8 exceptional dimension, entropy
   quantifiers and source holdouts survive the proof audit. Small exceptional dimension
   does not establish π's avoidance. The 32768-shell integration recount is a shared-data
   replay, not a fresh holdout.
6. **Boundary case:** #651's strictly positive lag statement is restricted to positive lag;
   zero lag has zero difference. The old overstatement and correction remain documented.

The [claim supplement](CLAIM_SUPPLEMENT_MAIN_XXVI.md), [atlas](MAIN_XXVI_CONSTRUCTIVE_INTERFERENCE_ATLAS.md),
[source audit](main_xxvi_evidence/source_audit.md), [foundations audit](main_xxvi_evidence/foundations_audit.md)
and [earlier-family audit](main_xxvi_evidence/earlier_families_audit.md) give provenance,
proof scopes, countermodels and exact retests. These are same-model reviews plus different
implementations; they are not external peer review.

## Reproduced floating-point blocker and minimum repair

Fresh untouched Main XXV replay reproduced the reported diff signature: 178 inserted and
178 deleted lines in `RESULTS_analytic.json`, containing 1186 changed floating leaves and
two near-tied argmax labels. All 11 probe/test commands returned zero, but the strict wrapper
failed because it had regenerated tracked historical diagnostic JSON in place. The original
interrupted receipt was unavailable; this is a labelled fresh reproduction.

The differences are downstream of NumPy complex `vdot`: lag inner products, accumulated
diagnostics, small residual/bound ratios and residual argmax selection. The primary runtime
is Python 3.12.14 / Clang / glibc 2.41, NumPy 2.3.5, SciPy 1.17.0, mpmath 1.3.0 and
SymPy 1.14.0. A second system Python 3.13/GCC runtime also preserved decisions but changed
additional diagnostics; it is retained as a rejected, unreviewed replay configuration.
No exact arithmetic defect or changed mathematical threshold was observed.

The repaired XXV runner executes numerical generators in a disposable source copy, deletes
stale generated outputs first, and compares every produced receipt. All keys, shapes,
types, exact source decisions, thresholds, counts and statuses remain exact. Only listed
analytic diagnostic paths admit absolute drift ≤1e−14 (small residual/bound ratio ≤1e−10);
the two witness labels can differ only in the validated sub-1e−14 roundoff argmax class.
NaN/Inf, new paths, altered thresholds, invalid controls and structural mutations fail.
Historical RESULTS bytes remain untouched. Raw strict failure, regenerated JSON, exhaustive
path differences, environment and preservation hashes are under
[`main_xxvi_evidence/baseline`](main_xxvi_evidence/baseline).
This is a scoped finite reproducibility policy, not a theorem error bound or unrestricted
cross-runtime portability claim. Successful subcommands alone are insufficient.

## Composite deductions and frontier

The [source-phase interface](MAIN_XXVI_SOURCE_PHASE_INTERFACE.md) derives a calibrated
Gamma-weighted carry decoder with error ≤`7√2/(8|a|B)`, a finite seed-shadow obstruction
retaining all source windows, and an exact fourfold CRT carrier retaining winding.
The [observer transport theorem](MAIN_XXVI_OBSERVER_TRANSPORT.md) gives sharp Gamma
resolvent defect bounds under explicit contraction/source hypotheses.

These improve interfaces and delimit the missing source information. No new all-shell
source-selected saving is proved. The weakest maintained rung remains
`∃η>0,B0 ∀B≥B0: Re W_B(1)≤1−η`; full π normality is stronger.
The next offensive is a zero-seed/height-sensitive signed count or potential on the actual
growing-CRT numerator history, with rational-shadow falsifiers before a new source holdout.

## Exact-candidate validation contract

Use declared `.[test]` dependencies, `PYTHONPATH=.` and recorded BLAS thread limits.
Required command receipts are separate from donor historical passes:

```sh
python scripts/verify_provenance.py
python -m unittest discover -s tests -p 'test_*.py'
python scripts/observer_foundations_probe.py
python scripts/ordinal_succ_report_probe.py
python scripts/main_xxiv_research_gate.py --out ../final_xxiv_receipts
python scripts/main_xxv_research_gate.py --out ../final_xxv_receipts
python scripts/main_xxvi_research_gate.py --out ../final_xxvi_receipts
python scripts/main_xxvi_manifest.py --check docs/SUCC_MAIN_XXVI_INTEGRATION_MANIFEST_2026-11-16.json --integration HEAD
python scripts/build_math_memory.py --check
python scripts/verify_math_memory_graph.py
```

Also replay applicable pinned Lean verifiers and mutation controls. A missing toolchain or
failed check is disclosed as such; historical Lean receipts do not become fresh certification.
XXVI's runner covers every changed research-local test directory plus explicitly selected
standalone audits and inventories other unrun Python candidates. It does not claim that native
test discovery executes every research script. Exact final commit/tree and unchanged tracked
bytes are checked, and hosted Actions are inspected at the published candidate before merge.

The validated tree is published with every maximal donor as an ancestor, preserving exact
source history without rewriting a shared ref. Any publication commit identifier change
retains the same tree but requires exact-commit receipts. No release, tag, history deletion,
force push or failed-check bypass is authorized.
