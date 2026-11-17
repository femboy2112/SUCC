# Two-BBP-Form Locked Source — full rational certificate and validation

**Date:** 2026-11-17. This is a deliberately **changed-source** control, not an alternate original BBP history or a normality proof. Accompanies [the complete matched countermodel](BBP_TWO_FORMULA_LOCKED_COUNTERMODEL.md).

## Executed exact focused regression

Locally executed:

~~~sh
python -m unittest -v /mnt/data/test_matched_nontele_locked_source.py
~~~

**8 tests PASSED, 0 failures/errors.** The exact locally executed 3,690-byte standard-library file matches the GitHub blob at [tests/test_matched_nontele_locked_source.py](../../../tests/test_matched_nontele_locked_source.py), SHA-1:

~~~text
01025ffff495e99798d44b3cea2fda72485a2cf5
~~~

Exact Fraction tests verify the source’s rational partial-fraction form, positivity and strict finite monotonicity, telescoping correction, rational locked endpoint 13/128, an uncancelled pole orbit inherited at 7/8, the same 15/(64n²) leading coefficient in exact rational asymptotic calibrations, and source-basis differentiation polynomial with entirely positive coefficients.

## Independently checked symbolic polynomial identities

A separate SymPy script, not reusing the finite Fraction code, calculated the exact rational function

\[
r_\flat(n)=r_{\rm BBP1}(n)-r_{\rm BBP2}(n)+16b(n)-b(n+1),
\quad b(n)=1/(16n)+5/(128n^2).
\]

It independently produced

\[
P(n)=3932160n^9-8077312n^8-1591296n^7+17061120n^6
-13293600n^5-1264320n^4+5583978n^3
-2495921n^2+432000n-25200,
\]

\[
Q(n)=128n^2(n+1)^2(2n-1)(4n-3)(4n-1)
(8n-7)(8n-5)(8n-3)(8n-1),
\]

and the **exact** equality \(r_\flat=P/Q\). Replacing \(n=t+1\) yields a P polynomial with **10 strictly positive integer coefficients**, a factored strictly positive Q, and the numerator \(P Q'-P' Q\) of \(-r'_\flat\) with **20 strictly positive integer coefficients**. The full independent coefficient arrays are preserved in [the theorem manuscript](BBP_TWO_FORMULA_LOCKED_COUNTERMODEL.md) and regenerated from its formula by the regression test.

The exact asymptotic result is
\[
r_\flat(n)=15/(64n^2)-133/(1024n^3)+O(n^{-4}),
\]
so its leading term matches the real BBP source, while its pole at 7/8 has the same nonzero residue 1/2 and no other pole in that integer-shift class.

## Imported infinite BBP evaluation boundary

The two rational source sequences \(r_1,r_2\) each sum to π/16 under base-16 weighting. That is not proved by a finite numerical test; it is an **imported published identity**: https://mathworld.wolfram.com/BBP-TypeFormula.html , formulas (2) and (3). An 80-digit mpmath check independently computed 180 terms of each series, agreeing with π/16 to working precision; this is **not a rigorous interval proof** and cannot replace the reference identity.

The countermodel's **infinite** completed endpoint follows by subtracting those two imported exact identities and applying the rigorously telescoping rational correction: \(x_\flat=b(1)=13/128\). Its completed radix-16 orbit is phase 1 from n=2 onward, despite its source’s positive monotone asymptotics and nonzero weighted shift-orbit residues.

## Claim boundary and next source-specific obligation

- **PROVED PAPER, conditional on established BBP identities:** null-seeded positive monotone rational locked source with the same leading asymptotics as BBP, and with a nonzero orbit-weighted pole-residue obstruction against rational telescoping.
- **EXACT SYMBOLIC/FINITE CHECKED:** rational identity, positivity, strict decreasing profile, locked endpoint and isolated residue.
- **REFUTED GENERAL INFERENCE:** nonzero weighted pole residue + null seed + positivity + decreasing n^-2 profile would imply R0.
- **UNVERIFIED/OPEN:** an actual original-zero BBP four-pole **quantitative winding-density** inequality on all sufficiently late shells. No full pi normality proof.
- **NOT RUN ON THIS NEW HEAD:** full root AGENTS gates, full repository unittest suite, Lean proof kernel, final hosted CI completion, external peer review of SUCC’s new composite argument.

**Next test that could change the verdict:** find and prove an arithmetic inequality using the *complete original four-pole coefficient/pole vector* and its actual zero-seeded chronological winding, not only generic source-nullity or nonzero shift-orbit residues. It must exclude this matched alternative, the rationally telescoping locked alternative, the badly approximable Kempner cold-shell model, and the original-forcing changed-seed lock without incorporating the desired result into the assumptions.
