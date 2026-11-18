# Source-Null Section — exact algebra, implementation receipt, and unresolved boundary

**Date:** 2026-11-17. Companion to [SOURCE_NULL_SECTION_AND_PROJECTION_DYNAMICS.md](SOURCE_NULL_SECTION_AND_PROJECTION_DYNAMICS.md).

## Executed focused tests

A local, standard-library Python Fraction test file was executed:

~~~sh
python -m unittest -v /mnt/data/test_null_seed_source_anchor.py
~~~

**Result: 9 tests, 9 PASSED, zero errors, zero failures.** The exact 4,789-byte tested file was subsequently committed as [tests/test_null_seed_source_anchor.py](../../../tests/test_null_seed_source_anchor.py). The independently computed local Git blob SHA-1 matches GitHub's fetched blob SHA exactly:

~~~text
092bc59a34f81c2cf6fd77d941548cf8fc7c6537
~~~

Covered: direct original zero-seeded four-pole recurrence versus its rational partial sum; all scalar seed invariants preserved at every inspected clock; affine seed translation commuting with radix updates; chart shifts with nonzero b0 and a transformed forcing; source-transported null-reference excess remains zero while an honestly changed seed remains changed; dyadic changed seeds exactly alias original integer-time circle observations after a finite horizon; null seeds can be perfectly locked under *other* source laws; a deterministic classical two-coordinate carrier that yields incompatible one-step readouts under non-injective projection; and source-independent homogeneous first/second seed-variation controls.

## Independent symbolic derivation check

A separately written SymPy calculation at two successive clocks treated \(s,b_0,b_1,b_2,f_1,f_2\) as **independent symbolic indeterminates**.

Results: four expressions simplified to **exact zero**:
1. \((U_1-F_1)/16-s\);
2. \((U_2-F_2)/256-s\);
3. \((U'_2-F'_{{\rm numerical\ zero},2})/256-b_0-s\);
4. \(U'_2-(F_2+b_2)-256s\).

These are symbolic algebra checks on the full stated variable family for two clocks. The universal theorem follows from a separately included induction and chart-transport derivation; the finite checks are not substitutes for that proof.

## Evidence and nonclaims

- **EXACT/PAPER:** for the fixed authenticated forcing, the affine first integral \(\mathcal I_n=s\) and its source-reference-gauge-covariant null-excess version. They distinguish no injected homogeneous seed from an unknown seed, and from an observationally null seed.
- **EXACT CLASSICAL COUNTERMODEL:** zero initial seed with zero (or integral) forcing can produce an identically phase-locked trajectory. Thus source-nullity by itself is not a theorem of phase delocalization.
- **EXACT CLASSICAL OBSERVER COUNTERMODEL:** a deterministic carrier can be non-Markovian under a lossy selected readout; other full readouts (including BBP's completed circle law) can already be closed.
- **NOT CLAIMED:** reproducing quantum-mechanical Kochen–Specker contextuality, Bell nonlocality or general relativity; a physical temperature/entropy law; an independently measured BBP source; a new all-late-shell π Fourier bound or normality theorem.
- **NOT EXECUTED ON THIS HEAD:** the complete repository-wide unittest collection, provenance/observer/ordinal gates, Lean verification and final hosted CI completion. Earlier full-suite receipts belong to earlier exact commits and are not automatically transferred.
- **OPEN:** derive the actual source-forcing/null-section/selected-winding arithmetic property that forces the terminal rational \(\mathcal R_B\) to remain above a positive constant on every sufficiently late shell. The required conditional comparison and all previous wrong-seed/dyadic/gauge/finite-shadow hostile controls are retained in PR #657.

This validation is **a source/representation theorem**, not an arithmetic proof of base-16 normality.
