# Validation and audit record

**Observed date:** 2026-11-19. **Base:**
`81be6b897ae980b801a3b9de9e22ef81e8360bfb` (Main XXVI).

All reported commands below were actually executed. The full inherited test
suite completed successfully, the new focused suite passed, and independent
source implementations agree exactly on the held-out matrices and inverses.
Universal mathematical statements rest on the written proofs, not on these
finite passes.

## Environment and change scope

| Component | Version or scope |
|---|---|
| Python | 3.12.14 |
| SymPy | 1.14.0 |
| NumPy | 2.3.5 |
| SciPy | 1.17.0 |
| mpmath | 1.3.0 |
| New implementation arithmetic | Fraction integers/rationals; separate exact SymPy symbolic audit; inherited exact rational complex matrices for graph controls |
| Changed repository area | Additions only under this dossier directory |
| Runtime and frozen sources | No edits |

The root regression run was started while this additive dossier was being
written. Its discovery directory was `tests/`, and the inherited runtime and
tests remained byte-for-byte unchanged. The dossier's own tests were run
separately after the four implementation lanes were complete. Later changes
were proof wording, GitHub math delimiters, synthesis, provenance, and the
receipt bridge; its independent command is recorded below.

## Required repository gates

Commands ran from the repository root. `PYTHONPATH=.` makes the checkout's
runtime package available to the standalone scripts.

| Command | Observed result | Raw receipt |
|---|---|---|
| `python scripts/verify_provenance.py` | Exit 0; `SOURCE_PROVENANCE_VERIFIED`; 72 items, 17 byte-identical archives and 55 mechanical namespace migrations | [provenance.log](receipts/provenance.log) |
| `PYTHONPATH=. python -m unittest discover -s tests -p 'test_*.py'` | Exit 0; **14,476 tests run in 1233.960 seconds; OK, skipped=2** | [root_unittest.log](receipts/root_unittest.log) |
| `PYTHONPATH=. python scripts/observer_foundations_probe.py` | Exit 0; complete JSON report with `OBSERVATIONAL_SUCC_FORMAL_FOUNDATIONS` | [observer_foundations.log](receipts/observer_foundations.log) |
| `PYTHONPATH=. python scripts/ordinal_succ_report_probe.py` | Exit 0; complete JSON report with `FINITE_ORDINAL_SUCC_SECOND_ORDER_WEIL_PROBE` | [ordinal_succ.log](receipts/ordinal_succ.log) |

The root log includes output from negative-control child runs, including a
temporary `STALE/MISSING mathematics catalog` diagnostic. The final parent
unittest result is `OK (skipped=2)`. No failure in that parent run was suppressed
or converted into a pass. The provenance verifier explicitly states that source
provenance does not establish mathematical truth.

## Focused exact tests

```sh
PYTHONPATH=. python -m unittest discover \
  -s research/2026-11-19/causal_generator_reconstruction -p 'test_*.py' -v
```

**Observed:** exit 0; **53 tests in 0.438 seconds, OK**.
The full named-test receipt is [focused_unittest.log](receipts/focused_unittest.log).

| Lane | Test methods | What the checks distinguish |
|---|---:|---|
| Source acquisition | 12 | All 126 five-tuples from clocks 0 through 8; later/Fibonacci schedules; exact inverse and determinant; precision signs; four-reading kernel; source/seed/lift/weight mutations; delayed source; tail bound |
| Minimal realization | 15 | Fibonacci reconstruction; noncommuting action order; minimal rank and similarity; unavailable response queries; global functional closure; derivative anchors; delayed chain; graph support and hidden zeta |
| Forward path geometry | 12 | Rooted forward diamond; gauge normal form; missing/inaccessible phase data; traversal costs; moving frames; intensity ambiguity; nonlinear-jet failure; near-pole conditioning; trace/response separation |
| Signed completion | 14 | Product and resolvent defects; spectral stationary components; signed telescope and moving-frame mutation; rational periodic controls; exact finite Gram calibration and compression bound |

The initial source-only run also passed 12 tests; its original receipt is
[source_acquisition_tests.log](receipts/source_acquisition_tests.log). These are
not counted as 12 additional distinct tests beyond the 53-method suite.

## Independent symbolic source audit

```sh
python research/2026-11-19/causal_generator_reconstruction/source_independent_audit.py \
  --output research/2026-11-19/causal_generator_reconstruction/receipts/source_independent_audit.json

python research/2026-11-19/causal_generator_reconstruction/verify_source_audit.py
```

**Observed:** both exit 0. The SymPy audit passed **116 exact assertions**.
It derives raw state coefficients directly from the symbolic recurrence and
inverts the resulting five-by-five matrix. It imports no acquisition functions.
The independent polynomial/Vandermonde sign derivation and proof audit appear in
[SOURCE_AUDIT.md](SOURCE_AUDIT.md).

The held-out schedules are `(4,9,21,44,67)`, `(8,13,21,34,55)`,
`(7,8,9,10,11)` and `(3,5,8,10,13)`. Symbolic `s=-x`, rational `s=1/16`,
four-reading kernel perturbations, discontinuous adaptive policies and every
term of one 36-term positive expansion are checked exactly. Consecutive-clock
determinant and inverse leading coefficients are calculated symbolically.

The Fraction bridge then matched **eight matrices/inverses and eight
determinants** by canonical rational SHA-256 digests. Both implementation hashes
match those recorded by the audit. This is an implementation-independence check,
not independent physical authentication of their shared source formula.

- [source_independent_audit.json](receipts/source_independent_audit.json): exact
  outcomes, audit/implementation hashes and canonical matrix digests.
- [source_independent_audit.log](receipts/source_independent_audit.log): captured
  output of the root rerun of that audit.
- [source_cross_implementation.json](receipts/source_cross_implementation.json):
  Fraction-versus-SymPy agreement.

## Finite signed-compression calibration

```sh
python research/2026-11-19/causal_generator_reconstruction/signed_completion.py
```

**Observed:** exit 0; **84 exact compression cases**.
[signed_compression.json](receipts/signed_compression.json) records the cases'
canonical payload hash:

`9b8abe704255a5b8c2d0312fbd7bdf97c3ded2cdcd8c2ba7b915c8742c31a17c`.

The controls are finite rational sign records and explicit complete character
grids. A grid average is not treated as the history of the selected seed. No
pi data is used to validate the normality-conditional asymptotic theorem.

## Adversarial paper audit and corrections

Three delegated mathematical lanes reviewed disjoint constructions, followed by
cross-lane proof criticism and root verification. They share a model family and
research context, so this is not external independent peer review.

The review led to concrete corrections rather than an unqualified consensus:

- An initial noncommuting-word test expected different scalar outputs from
  `aab` and `baa`; the chosen sensor made them equal. The discriminating pair
  was corrected to `aba` and `baa`. Noncommutation alone does not force every
  scalar sensor to distinguish every word pair.
- The endpoint identity `U_n+T_n=16^n*pi/16` was explicitly tied to the authentic
  zero seed. The general seed contributes `16^n*s`.
- The derivative-defect bound was clarified: finite intrinsic radius makes
  that bound uniform; it is not a necessary condition for every possible global
  defect estimate.
- Forward phase comparison now explicitly requires both coherently referenced
  reports, even when the histories meet at the same spacetime vertex. The
  parallel-edge ambiguity remains inside the unit-phase model.
- The general completion discussion now says equality at **every truncation**,
  rather than the ambiguous phrase “the same finite sequence.” The radix rank
  statement explicitly requires integer base at least two and nonzero integer
  frequency. The finite compression range is `0 <= d < m <= L`.

No remaining load-bearing proof defect was found by these audits. That statement
records the scope of the review; it is not a guarantee against future errors.

## Static integrity and limits

The package was compiled with `python -m compileall -q`, all JSON artifacts were
parsed, relative Markdown file links were checked, and staged whitespace was
checked with `git diff --cached --check`. The committed receipt manifest records
artifact hashes so subsequent edits cannot silently inherit these exact results.

No hosted-CI result, proof-assistant kernel verification, external peer review,
physical quantum implementation, new pi normality evidence, R0 proof, or RH proof
is asserted. The draft is ready for mathematical and repository review within
the stated source and observation contracts.
