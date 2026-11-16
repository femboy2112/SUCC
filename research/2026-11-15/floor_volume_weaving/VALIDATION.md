# Validation receipt

**Result:** all required local repository gates passed. These are software
and finite arithmetic checks; the original source's asymptotic carry-density
estimate and pi normality remain open.

## Required repository gates

Run from the repository root, with the project root explicitly on the Python
import path for subprocesses:

```sh
PYTHONPATH=. python -m unittest discover -s tests -p 'test_*.py'
PYTHONPATH=. python scripts/verify_provenance.py
PYTHONPATH=. python scripts/observer_foundations_probe.py
PYTHONPATH=. python scripts/ordinal_succ_report_probe.py
```

| Gate | Observed result | Raw receipt |
|---|---|---|
| Full unittest discovery | **13,545 tests passed**, 1043.803 seconds, exit0 | [full_unittest.log](receipts/full_unittest.log) |
| Frozen provenance | 72 items verified: 17 byte-identical archives, 55 mechanical namespace migrations, exit0 | [provenance.log](receipts/provenance.log) |
| Observer foundations probe | Completed, exit0; its open mathematical obligations remain reported | [observer_foundations.log](receipts/observer_foundations.log) |
| Ordinal SUCC report probe | Completed, exit0; no infinite execution or universal positivity claimed | [ordinal_report.log](receipts/ordinal_report.log) |

The full suite ran while research notes were assembled. No existing production
or test source changed during the run. The new standalone audit was executed
after its final substantive edit. Existing SyntaxWarnings in imported modules
are retained in the raw log; the suite's final result is `OK`.

## Exact research audit

```sh
python research/2026-11-15/floor_volume_weaving/independent_audit.py
```

**19,014 exact assertions passed**, using only Python integers and
`fractions.Fraction`; no production imports. The machine-readable output is
[independent_audit.json](receipts/independent_audit.json).

The audit covers period-four identities (including negative integer indices),
the source slope residue, the original four poles versus the five Beta
branches, dyadic branch valuations and reassembly, product/Beta moments,
rational forms of floor Laplace transforms, root/floor layer-cake formulas,
the signed boundary-count identity, and declared mutations.

For the sharp continuous controls it independently integrates the entered
cell polynomials. Every row, column, and diagonal-CDF formula is compared
as a polynomial identity on its whole quarter interval. The two uniform
extremizers have gate probabilities `1/16` and `7/8`; the missing-cofactor
control has probability zero with the full maximum law intact. Nonnegativity
is proved by the displayed factored cell formulas and was separately checked
at all corners in the final symbolic review (each cell is multiaffine).

The exact finite-state Haar model is checked through lag24 at five signed
parameters. These finite checks calibrate the general operator proof. The
initial wedge that misses the target projection is retained as an orientation
control. Nonpositive densities, changed pole coefficients, wrong floor shifts,
and a dropped negative threshold term are rejected by explicit controls.

## Authentic source checks and provenance

The inherited 32,768-residue certificate is SHA-256 checked against its parent
receipt. An independent direct rational recurrence reproduces the first512
carry residues, source/cofactor transport, and aligned selected gate. The
remaining shell statistics reanalyze those inherited certified inputs; they
are not newly generated digits or a fresh statistical holdout.

At `B=16384`, the source counts are `(1008,4146,4130)` for `(F1,c1,F2)*B`,
giving the exact three-mass lower certificate `1/16`; the actual selected
fraction is `4089/8192`. These finite observations do not supply a uniform
eventual estimate.

Five distant integer inputs additionally test the rational source/Beta
implementation beyond its initial range. They are implementation holdouts,
not asymptotic orbit evidence. Full inputs and source Git blob identities are
recorded in [source_provenance.json](receipts/source_provenance.json).

## Review and publication scope

Separate mathematical passes and a final separately entered SymPy audit
verified the high-risk continuous constructions. They share model/source
provenance, as disclosed in [PROVENANCE.md](PROVENANCE.md), and are not an
external referee or kernel-checked proof. The derivations are ordinary
mathematical proofs with exact executable checks.

JSON and local document links were checked, and the staged diff passed
`git diff --cached --check`. The GitHub tree is matched to the local staged
tree before publishing the draft. No hosted CI or external review result is
claimed here.
