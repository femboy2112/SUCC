# Operation Oily Logarithm — reproducible validation and proof authority

**Date:** 2026-10-29. **Research-only branch intended:** `research/oily-logarithm-levy-carry-2026-10-29`, stacked on the **exact** #381 parent `3d7f8d1a2dd4d3145c899daddd15377c4b0b632e`, in turn stacked on #379/#373/#367. Historical source, main, and canonical theorem registry unchanged. The source's `a_n=8n-7` and genuine zero seed are maintained in all original-path observations. No physical or academic-priority claim.

## Reproducible execution in the isolated standalone research package

```sh
python oily_logarithm.py
python test_oily_logarithm.py -v
python independent_oracle.py
python numerical_oracle.py
python -m compileall -q oily_logarithm.py test_oily_logarithm.py independent_oracle.py numerical_oracle.py
```

- **13/13 focused `unittest` methods PASS**, with exact `Fraction` recurrences, source rational moments, conjugate phasors, true q3 branch probabilities, 16-registered carry identities, source and seed midpoint algebra, phase aliases, and bad-input mutation rejections.
- **1966 independent exact checks PASS** in a separately reauthored SymPy/Fraction oracle (it does not import the new model): original numerator root algebra, first Fourier and Mellin corrections, reciprocal source inversion/hyperbolic slope, 210 exact seed transports, 210 independent integer carry checks, 32×32 exact rational Haar-cell branch witnesses, and source-overlap holds.
- **27 high-precision mpmath holdouts PASS** at 70 working decimal places: original Lévy exponent integral against the rational source log, original positive source Mellin/Laplace integral, special-function seed logarithm and explicit remainder, 59 first-correction, finite Oily scalar. These are numerical holdouts, **not** interval certificates of all real parameters.
- Original staged code compileall PASS. Full mathematical statements use **explicit paper proofs** in RESEARCH.md, not finite extrapolation. The numerical probe first failed with a source syntax typo, then an accidental native Python float in numerical reference formulas; these were corrected by matching parentheses and forcing mpmath high-precision constants before generating the passing log. No failed mathematical theorem was silently promoted.

## Source and proof type guards

- **Positive source:** original signed four-pole rational coefficients, positive regrouping `Q(x)>0`, and inherited exact source convolution `mu_(a,τ)`. The analytic characteristic logarithm is a theorem about that positive law, not about deterministic digits.
- **Actual path:** `U_0=0`, `U_n=16U_(n-1)+r(n)` with r(n)=R(8n-7). Counterseeds are labelled and never substituted for the authentic path without notation.
- **Mirror-seed probe:** two preparations `c±delta` are deliberately coupled, **not** independent samples. The exact q3 character is conditional on Haar-uniform delta; it is not claimed that an actual observer randomly selects these seeds.
- **Logarithmic inversion:** `a↔16/a` is a true symmetry of the reciprocal source numerator and a controlled odd defect of full R. It is not a symmetry of the discrete native clock.
- **Gamma/Oily:** the Mellin derivative supplies `1-gamma`, and a *separately declared* Oily golden Laplace parameter supplies `lambda²`; their contrast recovers `lambda-gamma`. The source numerator root hyperbolic parameter is a different algebraic number and not automatically golden.
- **Root-free signed logarithm:** its linear derivative recovers the still-unproved signed selected readout. An analytically well-defined log does not prove its derivative vanishes over arithmetic time.

## Exact-head integration status

The locally staged probes and documents are preserved. The full 9k+ SUCC root suite, root provenance/observer/ordinal commands, historical claim catalog regeneration, and Lean exports have **NOT** been executed against this new candidate head in the local research environment. They must be run before merging. Previous parent's hosted result is not used as a success claim for this new commit. The GitHub PR must remain **DRAFT**.

See `CLAIMS.md`, `NEGATIVE_CONTROLS.md`, and `NEXT.md`. The unresolved objective is a new source-dependent signed carry-bias inequality on the **actual** zero-seeded orbit, not an invertible change of coordinates or a source-independent seed average.
