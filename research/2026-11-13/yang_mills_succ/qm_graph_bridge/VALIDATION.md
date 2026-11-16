# Validation: existing SUCC quantum structures and the Wilson source

Date: 2026-11-13. Parent: `3929e30930438881bebcb371646389d9e66bfbde`.
Base main: `db9fb4b84672050efa79b13377f1e73364598a14`.

The additions use standard-library Python and exact rational or
Gaussian-rational arithmetic. Universal mathematical claims have paper proofs;
the finite checks verify implementations and deliberately broken alternatives.

## 1. Executed focused checks and required gates

| Command | Observed result | Raw evidence |
|---|---|---|
| `PYTHONPATH=. python -m unittest discover -s tests -p 'test_ym_*.py' -v` | PASS: 76 tests in 1.378 seconds, exit 0 | [Focused log](validation/focused_tests.log) |
| `python scripts/verify_provenance.py` | PASS: 72 provenance items, 17 byte-identical archives, exit 0 | [Provenance log](validation/provenance.log) |
| `python scripts/observer_foundations_probe.py` | PASS, exit 0 | [Foundations log](validation/foundations.log) |
| `python scripts/ordinal_succ_report_probe.py` | PASS, exit 0 | [Ordinal log](validation/ordinal.log) |
| `python scripts/yang_mills_qm_bridge_probe.py` | PASS: exact Wilson, graph, weighted Haar, native measurement and multiplier controls, exit 0 | [Probe log](validation/finite_probe.log), [JSON receipt](probe_receipt.json) |

The 76 focused tests comprise the previous 36 plus **40 new tests**:
13 graph-semantics tests, 10 weighted-Haar tests, 14 successor/character tests,
and three integration tests joining the new modules to existing quantum code.
The standalone multiplier probe additionally checks 56 polynomial identities
and 56 exact Haar norms; those checks are not counted as extra unit tests.

[targeted_validation.json](validation/targeted_validation.json) binds commands,
exit codes, raw-log hashes and all eight new implementation/test/script files.
The final standalone probe output and committed receipt are byte-identical.
The probe was extended and rerun while the full repository suite was executing;
no production module or test changed during that full-suite run.

## 2. Full repository gate

```sh
PYTHONPATH=. python -m unittest discover -s tests -p 'test_*.py'
```

**PASS: 13,126 tests in 1,033.194 seconds, exit 0.** The wrapper's elapsed
wall time was 1,038.976 seconds. See the unmodified [full-suite log](validation/full_suite.log)
and [command/environment/exit receipt](validation/full_suite_result.json).
The receipt's SHA-256 matches the complete log.

The full invocation supplies the repository root through `PYTHONPATH`, including
to child processes. This is the import precondition isolated in the first
round's [baseline diagnosis](../LOCAL_VALIDATION.md). The original uninstalled
checkout run and its one-error result remain recorded without alteration.
No historical test or module was changed to resolve that environment issue.

## 3. What the checks distinguish

The character suite compares half-line walk counts with the Catalan formula
and a separate integration-by-parts Haar recurrence through degree 100. It
checks every first cutoff deficit for cutoffs 0 through 14, character Gram
identities through index 12, fusion identities through index 8, the generated
character basis, positive Wilson approximants, and their agreement with the
previous round's independently implemented positive-density intervals.

The graph suite compares explicit path enumeration with matrix multiplication,
then checks composition, tensor and dagger semantics. It compiles the actual
finite `source_lambda` residue tables and `quantum_records` instruments. The
controls retain the difference between coherent path alternatives, orthogonal
outcome records and duplicate descriptions of a single map. Many-to-one
arithmetic maps fail the isometry test and have a source-retaining reversible
oracle construction instead.

The Haar suite checks weighted norms, exact inversion, transported multiplication
operators, existing polyphase boundary slots, complete detail retention and
source-sensitive finite Wilson controls. The integration tests establish that
the rational Wilson ray yields the same expectation through the graph matrix
calculus and complete Haar coordinates, while native Z-dephasing changes the
two-vertex example from 4/17 to 0.

The standalone receipt gives a 15-vertex graph for beta=3/2 and f(x)=x, with
an exact expectation and proved error budget below 1.227e-13. It also records
the existing multiplier as weighted Chebyshev composition, including composite
multipliers, and rejects the bare-pullback norm claim. The universal L2-domain
and isometry statements are proved in [SUCC_CHARACTER_PROOF.md](SUCC_CHARACTER_PROOF.md).

## 4. Source binding and limits of authority

[SOURCE_MANIFEST.json](SOURCE_MANIFEST.json) binds 21 existing repository source
files to the parent commit, four native Yang–Mills files to upstream commit
`55ba9fc36293b3f4d52c6b1f813169a0be76ee98`, the new code, and primary references.
The native `Gauge.price` definition was checked to match 1−Tr(U)/2 in the
defining SU(2) representation. Shared plaquettes in a full lattice are not
declared independent.

Parallel reviews checked the representation formulas, graph semantics,
source-weighted metric, Fock identification, generator domains and finite
boundaries. Those reviewers share a model family. Their agreement is not
counted as blind peer review, and uncommitted exploratory checks are not
promoted into the reproduction receipt.

This continuation did not execute Lean, the upstream kernel replay or
Comparator. The earlier upstream integrity result has its own unchanged
receipt. No new full 4d reconstruction, physical mass gap, arithmetic-source
identification, normality/RH theorem or quantum speedup follows from these
finite adapters. Remote CI is a separate result and is not claimed here.
