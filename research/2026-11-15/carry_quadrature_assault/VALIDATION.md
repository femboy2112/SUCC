# Validation and limits

The universal mathematical statements are justified in the proof notes.
Finite arithmetic checks calibrate implementation, signs, chronology and
countermodels. They do not establish an asymptotic density or normality.

## Focused source and control checks

| Check | Observed result | Receipt |
|---|---|---|
| New focused unit tests | 10 passed | `receipts/focused_tests.log` |
| Original-source finite carry probe | 32,768 certified indices; no unresolved boundary and no borrow in that finite range | `receipts/finite_probe.json` |
| Direct rational recurrence comparison | 2,048 exact cross-checks through index 512; 484 nonzero winding packet inequalities | Same JSON |
| Standalone four-pole/control audit | 55,022 exact assertions passed | `receipts/independent_audit.json` |
| Historical source preservation | 72 frozen items verified | `receipts/provenance.log` |
| Observer-foundations probe | Exit 0 | `receipts/observer_foundations.log` |
| Ordinal report probe | Exit 0 | `receipts/ordinal_report.log` |
| Full repository unittest discovery | 13,545 tests executed; 13,544 passed and one inherited subprocess import-path error | `receipts/full_tests.log` |
| Affected module with the repository import path | All 11 tests passed on this revision and the parent | `receipts/import_path_rerun.log`, `receipts/import_path_triage.json` |

### Full-run environment qualification

The full command `python -m unittest discover -s tests -p 'test_*.py'`
completed in 1048.533 seconds with one error in
`test_eodcs_meta_choice_descent.TestMetaChoiceDescent.test_exact_probe_receipt_and_independent_count`.
Its child process invokes the unchanged `scripts/meta_choice_descent_probe.py`,
which imports the repository package without inserting the repository root
into its script search path. Without `PYTHONPATH=.`, that child raises
`ModuleNotFoundError: No module named 'observational_succ'`.

The identical child failure was reproduced on the unchanged parent commit.
With `PYTHONPATH=.`, the entire affected 11-test module passes on both
revisions. Neither the inherited script nor its test was changed. The
parent's earlier full-suite receipt also explicitly used `PYTHONPATH=.`.
The original failed log is retained; this record does not claim that a
second full green run occurred. The isolated environment cause and its
corrected module rerun resolve the observed failure without an unrelated
source edit or another full-suite repetition.

The direct production paths use different algorithms but share
`duck_bbp.forcing`. The 2,048 cross-checks also include same-path identities;
they are not 2,048 independent experiments. The standalone audit imports no
production module and expands all four signed rational fractions, while
still sharing the mathematical source and Python rational arithmetic.

## Certificate construction

The inherited bulk BBP routine bounds a scaled pi prefix by outward integer
rounding of the original series and a proved remainder. Matching prefix
cells certify the hexadecimal string. For each n, the new code encloses the
completed circle phase using that string, compares it against a rigorous
interval for T_n, and certifies the exact borrow

\[
\beta_n=1_{\{\{16^n\pi/16\}<T_n\}},\qquad
C_n\bmod4=(d_n-\beta_n)\bmod4.
\]

Ambiguous boundaries raise an error after the declared maximum refinement;
they are never rounded to a desired outcome. In the recorded horizon, the
analytic n^-2 bound decided all 32,768 comparisons at the initial precision.
Raw hexadecimal and carry-residue strings are preserved alongside hashes.

The standalone audit represents complex character identities in an exact
finite group algebra of Q/Z. It checks the decoder after multiplying by the
nonzero reference norm, avoiding floating-point trigonometric comparisons.
The proof establishes the nonzero and uniform conditioning constants.
Those constants concern reference division with the correct fractional
representative supplied. No uniform infinite-time margin from integer carry
boundaries, or general noisy floor-classification guarantee, is asserted.

## Hostile controls and what was actually checked

The standalone run constructs all four combinations L=2 or8 and endpoint
1 or1/5 in the fixed-precision Mahler control, through index48. Each has
1,176 checked state-pair isometries and1,128 source-pair isometries, positive
odd-denominator forcing, matched low source bits and carry residue3.
Infinite analyticity and the exact limiting endpoint follow from the proof,
not extrapolation from these finite coefficients.

The Thue-Morse control has124 floor certificates,124 nearest-integer
certificates and123 winding identities over indices5..128. There are62
positive nonzero packets and zero selected events in that range. Its
all-index exclusion after time4 and asymptotic packet density1/2 are proved
separately, using the no-three-zeros fact and exact binary block balance.

## Review and reproducibility

Proof reviews checked the source inequalities, inverse reference phase,
fixed-depth/time limit order, half-open bin boundaries, signed packet ties,
global analytic zero pin, changed-source quantifiers and all control scopes.
The root additionally reviewed the standalone audit source and reran it.
Agent audit notes disclose their shared model/source provenance.

The commands and current code hashes are recorded in `receipts/validation.json`.
Existing Python syntax warnings in unrelated inherited modules may
appear in full discovery; they are not changes made in this dossier.

No Lean verification of the new statements, source-selected positive
carry-density estimate, new asymptotic real-phase saving, or pi normality
proof is claimed.
