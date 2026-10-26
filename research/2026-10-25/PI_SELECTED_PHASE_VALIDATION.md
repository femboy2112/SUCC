# Selected-phase forge: validation and reproducibility

This receipt belongs to `research/pi-selected-phase-forge-2026-10-25`,
descended from PR #301 at `b792caae40dfe777cf7e9d3301b61f1ac0adac41`.
The original source, initial condition, imported archives and main branch
were not changed. The [mathematical dossier](PI_SELECTED_PHASE_FORGE.md)
and [PSF ledger](../../docs/CLAIM_SUPPLEMENT_PI_SELECTED_PHASE.md) state
the exact authority of each claim. Base-16 normality remains **OPEN**.

## Environment and commands

Execution used Python 3.12 in a local `.venv` with the repository installed
editable using `pip install -e '.[test]'`. This also makes repository imports
available to subprocess probes. The venv is not a research artifact.
Run the following from the repository root in that environment:

```bash
python scripts/verify_provenance.py
python -m unittest discover -s tests -p 'test_*.py'
python scripts/observer_foundations_probe.py
python scripts/ordinal_succ_report_probe.py
python -m unittest tests.test_bbp_clock_transport tests.test_bbp_diophantine_coherence tests.test_bbp_positive_carry_control tests.test_bbp_sparse_carry_transport
python scripts/pi_selected_phase_probe.py --verify research/2026-10-25/selected_phase_validation/exact_receipt.json
```

The Lean replay command is below; the optional dependency project points
to an existing cache whose source revisions are checked before use.
Choose a fresh output directory to preserve this round's recorded logs.

```bash
python scripts/check_selected_phase_lean.py --output /tmp/succ-selected-phase-replay --dependency-project /home/leah/SUCC-rf/formal/mathlib_bridge
```

The exact probe regenerates its whole payload and compares current source
hashes, rational witnesses, counterexamples and authority flags. It does not
evaluate floating spectra or infer analytic truth from a finite trend.
Its small-conductor clock checks use the actual cyclotomic quotient;
formal group-algebra equality and evaluated root-of-unity equality are not
interchanged.

## Observed validation

| Check | Actual result | Evidence |
|---|---|---|
| Four new focused test modules | 54 tests passed | [log](selected_phase_validation/focused_new.log) |
| Claim namespace regression | 15 tests passed | [log](selected_phase_validation/namespace.log) |
| Source provenance | 72 items verified: 17 byte-identical archives, 55 mechanical namespace migrations | [log](selected_phase_validation/provenance.log) |
| Exact selected-phase receipt | Deterministic replay passed | [receipt](selected_phase_validation/exact_receipt.json), [log](selected_phase_validation/exact_replay.log) |
| Deliberately false normality receipt | Rejected with exit 1 | [log](selected_phase_validation/receipt_mutation.log) |
| Markdown and relative links | GitHub GFM render passed; PSF table has all 56 data cells | [audit](selected_phase_validation/markdown_audit.json) |
| Observer foundations | Exit 0 | [log](selected_phase_validation/observer_probe.log) |
| Ordinal successor report | Exit 0 | [log](selected_phase_validation/ordinal_probe.log) |
| Full Python suite | 8,474 tests passed in 945.167 seconds | [log](selected_phase_validation/full_unittest.log) |
| Pinned Lean finite kernel | 8 declarations checked; 3 positive controls passed and 3 false claims rejected | [receipt](selected_phase_validation/lean/kernel-observation.json) |

The baseline PR #301 modules were also exercised directly in the native
installed environment: 9 Möbius tests, 6 exceptional-pole tests, and 23
inherited internal-matrix tests passed. This is local execution evidence,
not a substitute for hosted checks at any sibling commit.

Focused controls include literal four-pole and independent integer-carrier
replays, fresh block endpoints and signed frequencies, odd prime and prime-2
state precisions, exact clock sharpness, altered source signs/initial states,
the previously negative naive counterfeit at time 14, all future carries
outside the observed horizon, and rejection of source-authenticity claims
for both counterfeit families. Dense edits and zero forcing remain biased.

## Lean authority

The checker is [check_selected_phase_lean.py](../../scripts/check_selected_phase_lean.py).
It used Lean **4.14.0** and the repository-pinned mathlib revision
`4bbdccd9c5f862bf90ff12f0a9e2c8be032b9a84`, with one job and a 2 GiB limit.
The receipt records the exact executable, commands, source hashes, exported
declaration types and hashes, logs, and permitted axioms. The declarations
depend only on the standard `propext`, `Classical.choice`, and `Quot.sound`
axioms as listed individually in the export. A separate read-only audit
matched all current source and declaration hashes to the receipt.

The formal statements cover integer branch uniqueness, backward recurrence
telescoping and endpoint bounds, summing assumed scalar block deficits, and
two rational margins. They do **not** formalize complex chord geometry,
the BBP integral identity, the published irrationality measure, the analytic
transport theorems, or pi normality. The initial elaboration needed the
ordered finite-sum import before the successful checked source was frozen.
The rejected mutant theorems reverse the forcing sign, overcount a block
deficit, and assert false integer equality; paired true controls compile.

## Remote and delivery scope

The [remote baseline](selected_phase_validation/remote_baseline.json)
preserves the reviewed heads and discussions of PRs #297–#302 and their
observed workflow states. A later fetch still found the same PR #301 head
and main at `1e3a453e869992961bc2d7f3bb6f2f1ddab38854`.
The [parent CI recheck](selected_phase_validation/parent_ci_recheck.json)
observed all four PR #301 workflows successful, including full validation;
duplicate push runs were cancelled. This is evidence for that parent head,
not for this new branch.
The stacked draft targets `research/mobius-refined-internal-matrix-2026-10-25`.
No merge, rebase, force push, release, or historical artifact rewrite is
part of this delivery. Hosted outcomes must be read at the exact delivered
head; local passing checks are not relabelled hosted CI success.

Mathematical review combined independently written derivations, exact
implementations, source mutations and held-out inputs. The workers share
a model family and source lineage, so this is not external peer review.
The published Diophantine input is classical; academic novelty of the new
repository results is not asserted.
