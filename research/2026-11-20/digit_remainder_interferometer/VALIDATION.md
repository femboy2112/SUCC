# Validation — reflected-digit / transmitted-remainder seam

**2026-11-20 · isolated additive research.** Executed in `/mnt/data/digit_remainder_interferometer` against the exact files committed. All commands are local, no hosted GitHub CI or inherited SUCC root suite claimed.

## Focused tests

Command: `python -m unittest discover -v -p 'test_digit_remainder.py'`

Result: **16/16 passed**, `OK`, exit 0; raw stdout/stderr preserved in [focused_unittest.log](focused_unittest.log). Tests cover exact rational digit/remainder inverse on hundreds of states; four binary routing stages; original four BBP pole rational reductions; strictly positive and decreasing original forcing on tested indices; exact tail enclosure and first 12 hexadecimal π/16 digits; zero-seed versus locked source-independent warning; exact prefix-plus-remainder conservation; exact Walsh transform isometry on rational amplitude vectors; pure-branch and uniform-input hostile measures; phasor identity sign calibration; two-cycle mirror no-go; four H roots on digit thresholds; and input guards.

## Independent oracle

Command: `python independent_audit.py` (separate SymPy implementation, does **not** import `digit_remainder.py`).

Result: **PASS, 833 exact checks**: 183 rational inverse routes; 183 four-stage factorizations; 256 Walsh Gram entries; 4 independent exact branch-norm comparisons; 96 original four-pole arithmetic identities; 95 strict source decrease comparisons; 12 exact prefix-branch checks; 4 algebraic H-root threshold checks. Raw receipt preserved in [independent_audit_receipt.json](independent_audit_receipt.json). The scripts share the same theorem statements but not implementation; not a blind external mathematical referee.

Compile command: `python -m compileall -q digit_remainder.py test_digit_remainder.py independent_audit.py` — exit 0.

## What remains untested or unsupported

- Full inherited SUCC root tests (>14k), `scripts/verify_provenance.py`, observer foundations and ordinal gate, hosted CI, Lean and independent refereeing **NOT RUN**; this scope is not a root-suite pass.
- No physical mirror/slit experiment, no genuine quantum state/preparation or Born probabilities, no root-sector-to-real-BBP-digit intertwiner, no π-normality/R0 proof, no RH or source-derived Gauss/energy law.
- Finite BBP digits are certified under the standard imported identity `π/16=Σ16^(-j)r(j)` and an exact monotone-source tail bound; not an independent π identity proof.
- Root threshold positions depend on explicitly declared left-semicircle chart; the fourth root at x=1 is a boundary outside `[0,1)`.

The remaining decisive proof is an authenticated map from the *original source filter H root parity* to the *actual four bit decisions* of the π-digit seam, with a new signed all-shell prediction independent of the target phases. The universal algebraic digit recursion alone cannot provide it.
