# Validation and failure record — UNIT-TO-UNIT, 2026-10-31

**Repo baseline:** `femboy2112/SUCC`, Main XVIII `4eb411e3730a9e7b95480369a438b89d9a433a4b` as checked live. Read-only precursors PR #437 original 4-pole/Poisson alias, #438 periodic analytic interpolation, #439 Zak–Jackson signed trace; integrated `proto_succ_variable_unit.py`, `clock_mahler_interpolation.py`, `operational_yoneda_descent.py`. No original source, production code, proof authority, CI or frozen history modified.

**Source/independence:** The module uses the original exact signed four-pole and combined numerator formulations; the oracle independently computes source via combined rational polynomial and finite-difference recursion, and the Beta formula uses factorial products. All share a single underlying mathematical source: these are distinct algorithms, not blind mathematical referees.

**Actually executed:**

```sh
cd /mnt/data/succ_unit_seam_round
python -m unittest discover -s tests -p 'test_*.py' -v
```

Final state: **31/31 PASS**, Python 3.13, pure stdlib, 0.16 s. Every new test is root-discoverable when copied to the existing SUCC `tests/` directory. Coverage: 64 original source samples, 17 separate positive unit coefficients, 16 finite source inversions, 14 extrusion recurrences, 13 rational zero-seeded state reconstructions, determinant law, bounded Green telescope, positive rational pi enclosures and independent 20-term Machin arctan certificates, nonlinear rational phase exponent factor, 7 symbolic dilation operators on 5 depths, BBP-source exact moment diamond, positive two-measure indistinguishability for m=2..8, same-endpoint different-history path cochain, irrational Pisot colored-unit integer diamond, fail-closed invalid types, and all-prefix rational shadow bounds through M=11.

**Observed correction retained:** Initial independent recursion `path_count` indexed one element beyond the previous Pascal row and two tests ERRORED with `IndexError`. The independent oracle was corrected to treat absent previous-row coordinates as zero. Rerun **25/25 PASS**, then four additional rational circle shadow and two quadratic Pisot tests were added; final **31/31 PASS**. This is an ordinary oracle indexing defect, not a mathematical counterexample.

**Separate exact SymPy audit executed:** original P(t) positive factor, full four-pole combined source, eight rational Gamma/Beta jet identities, 30 polynomial dilation/shift diamonds, the Z[phi] characteristic X²−X−1 — PASS. The first audit incorrectly compared algebraically equal SymPy expressions by syntactic `==` rather than zero simplification; fixed and rerun. This is a CAS normalization error, not mathematical falsification.

**Exact finite diagnostic:** rational intervals derived from the unit-jet geometric remainder:

| J | certified pi interval approximate endpoints | interval width |
|---|---|---|
| 2 | 3.1286110432777101–3.1424383693769316 | 0.013827... |
| 5 | 3.1415924149135255–3.1415962837487954 | 3.8688e-6 |
| 8 | 3.1415926525534426–3.1415926536581953 | 1.1048e-9 |
| 12 | 3.1415926535897736–3.1415926535897944 | 2.1065e-14 |
| 16 | endpoints numerically round to 3.1415926535897931 | 4.0513e-19 EXACT rational interval |

The exact Fraction interval itself, not rounded display, is the certificate. These values do not measure normality or digits beyond the stated interval.

`M=1,2,3,5,9`, `J=2M`, `h=1` real-circle Weyl shadow error exact rational bounds respectively `<0.086914621`, `<0.0063001789`, `<0.00043653981`, `<2.1167093e-6`, `<5.1268262e-11`. Those are phase **transport error** certificates only, not observed signed cancellation. The optional `FINITE_RECEIPT.json` gives machine-readable small exact rationals.

**Not run/claimed:** full ~10k SUCC suite and repo provenance/foundations/ordinal scripts (no complete source tree in the working container), hosted exact-head CI, Lean kernel for the present paper theorems, external review, RH, pi normality, unconditional signed Weyl bound.
