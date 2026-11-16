# Validation and authority boundary

## Source and environment

The continuation starts at founding draft #618, commit
`ab31057590a59b2bfbd5dbcd7126b2aefc7a2b55`, with main
`db9fb4b84672050efa79b13377f1e73364598a14`. Both refs were checked again during
the round and remained unchanged. The new work uses a separate non-main branch,
`research/principia-observatoris-kernel-2026-11-13`, stacked on the founding
branch. No main merge, tag, release, frozen-source edit or historical runtime
behavior change is part of this milestone.

Local runtime: **Python 3.12.14**. New native mathematics uses the standard
library and exact integers/Fractions. This is not a Python 3.10/3.13 hosted-CI
result. No Lean executable was available on the active path; no new formal
kernel check is claimed. Existing Lean theorems keep their existing provenance.

## Actual validation history

| Check | Actual outcome | Receipt |
|---|---|---|
| `python -m unittest discover -s tests -p 'test_principia_observatoris.py' -v` | PASS: 15 tests | [Focused log](receipts/focused_tests.log) |
| First required full native command, without installed-package/PYTHONPATH setup | Ran 13,065 tests in 1,072.269 s; FAILED with one subprocess import error | [Unaltered first-run log](receipts/full_suite.log) |
| Import diagnosis | `scripts/meta_choice_descent_probe.py` could not import `observational_succ` when executed as a subprocess from this fresh checkout | Existing source is unchanged; environment defect, not a false mathematical assertion |
| `PYTHONPATH=. python -m unittest discover -s tests -p 'test_eodcs_meta_choice_descent.py' -v` | PASS: all 11 affected-suite tests, 0.138 s | [Import repair replay](receipts/import_repair_tests.log) |
| `PYTHONPATH=. python -m unittest discover -s tests -p 'test_*.py'` | PASS: **13,065 tests in 1,037.662 s**, exit 0 | [Full corrected-environment log](receipts/full_suite_with_import_path.log) |
| `python scripts/verify_provenance.py` | PASS: 72 imported items, including 17 byte-identical archives and 55 mechanical namespace migrations | [Final provenance](receipts/final_provenance.log) |
| `python scripts/observer_foundations_probe.py` | PASS, exit 0; scoped model outputs retained | [Final observer probe](receipts/final_observer.log) |
| `python scripts/ordinal_succ_report_probe.py` | PASS, exit 0; scope and open positivity status retained | [Final ordinal probe](receipts/final_ordinal.log) |
| `python scripts/principia_ancestral_probe.py` | PASS, exit 0; existing selected-root adapter exercised | [Ancestral receipt](receipts/ancestral_probe.json) |
| `python scripts/principia_observatoris_probe.py` | PASS: rational closure/defect/separation controls, 131 native forcing comparisons, 15 fitted-forcing certificates | [Exact probe](receipts/exact_probe.json) |
| `python research/2026-11-13/principia_observatoris/independent_audit.py` | PASS: separate implementation and native differential audit | [Audit JSON](receipts/independent_audit.json) |
| Finite-horizon review's retained Python block, replayed by root | PASS: 20,736 switched cases; 5,152 zero-through-length-one cases remain zero on held-out words through length five; sharp dimensions 2–12 | [Root horizon replay](receipts/horizon_replay.json) |
| Arithmetic audit's retained determinant/cofactor block, replayed by root | PASS: 16 exact cases, 80 prefix checks, 48 rival comparisons | [Root arithmetic replay](receipts/arithmetic_independent.log) |
| `quantum_certificate_probe.py --output .../quantum_certificate.json` | PASS: 64 signed matrices, 3 positive certificates; false ε=1/3 and 3 malformed contracts rejected | [Quantum certificate](receipts/quantum_certificate.json), [command log](receipts/quantum_probe.log) |
| `arithmetic_scale_probe.py` | PASS; root replay byte-data matches retained JSON: 48 bounds, 30 independent Rodrigues norms, 90 orthogonality checks, 186 rejected mutations | [Scale certificate](receipts/arithmetic_scale.json) |
| `adaptive_linear_probe.py`, replayed by root | PASS: all 13 fixed schedules on a symmetric seven-state prior; nonlinear-action, state-dependent-cost and randomized-loss controls | [Adaptive certificate](receipts/adaptive_linear.json) |
| `sharp_rival_probe.py`, replayed by root | PASS: 32 source/order pairs, 796 PSD principal minors, 32 attaining recurrences, 32 open-interval root certificates and 96 rejected perturbations | [Sharp uniform rival radius](receipts/sharp_rival.json) |
| `python scripts/verify_math_memory_graph.py` | PASS; syntax/dependency lint, not a proof checker | [Graph lint](receipts/relation_graph.log) |

The native source and its 15 tests were held fixed throughout both complete
test runs. Later research additions are isolated manuscript material and
standalone exact probes, each checked separately. The first failed command is
retained; no log was edited to manufacture a green history. CI installs the
package, while the successful local replay supplies the repository on the
subprocess import path explicitly.

## Independent implementation and adversarial findings

The separate implementation exhausts 6,561 two-action linear families with
19,683 output cases, checks 1,944 quotient/action pairs and 9,720 candidate-model
comparisons, 250 ordered defect words, all 729 three-state/two-action tables,
and 10,140 quantum branch vectors. Its native differential layer additionally
checks all 19,683 ternary 3-by-3 single-action matrices, 400 switched
multi-preparation cases, 400 predictive completions, 150 model comparisons,
30 Hankel blocks and nine malformed contracts. These counts overlap in
mathematical content and are not independent votes for truth.

Review found and repaired a Boolean BBP-start input bypass; the production
function now validates the starting index before adding offsets. Paper review
also repaired a missing nonempty source-label hypothesis in PO-Q3, distinguished
one-state immediate output from retained memory, and corrected coordinate/domain
and mathematical-delimiter issues. The false stronger conjectures remain as
countermodels. See [the crucible](crucible_audit.md).

The universal theorems have explicit paper proofs. Separate agents used the
same model family, so their agreement is not external peer review or a blind
independent reasoner certificate. No physical experiment, empirical source
authentication, scholarly-priority determination, π-normality proof, RH proof,
or quantum-gravity result is asserted.

## Integration receipt

The [entrypoint reading receipt](foundation_entrypoints_audit.md) lists exact
hashes and coverage for all twelve requested foundation files; root verified
those hashes. The [live-head snapshot](receipts/live_heads.json) and
[provenance audit](provenance_audit.md) distinguish current inspected drafts
from their older integrated snapshots. The generated mathematics catalog is
refreshed after the final manuscript. Its 172 pre-existing warning strings
are unchanged from the founding parent. The catalog and graph checks establish
index consistency, not mathematical correctness. The [artifact manifest](artifact_manifest.json)
pins all paths added or changed by this continuation other than itself.

Publication uses one validated tree and one draft PR. The PR description supplies
the exact published commit/tree; the local artifact manifest records the file
hashes independently. Hosted CI status must be read at the published head and
must not be inferred from local validation.
