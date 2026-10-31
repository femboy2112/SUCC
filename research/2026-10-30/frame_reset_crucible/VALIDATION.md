# Validation and authority — Operation Frame-Reset Crucible

**Repository baseline:** `main@e18ba565ca540adb7edf3292f5593929e76d91c5` (Operation Main XVI). Research-only new branch, no main edits. Independent read-only contextual PRs #390–#393. Original four signed BBP poles and `U_0=0` unchanged. Published Stoneham/Champernowne normality is CLASSICAL; the elementary counting lemmas are locally re-derived paper theorems. No new normality claim for π.

## Exact local execution

Run from this folder:

```bash
python -m unittest discover -s . -p 'test_*.py' -v
python independent_oracle.py
python -m compileall -q frame_reset.py test_frame_reset.py independent_oracle.py
```

**Observed:** 20/20 standard-library `unittest` methods PASS (`focused_tests.log`), including:

- c=3 conductor p=1..5, c=5 conductor p=1..4: exact unit subgroup traversal with precisely 6/20 visits per residue;
- c=3 p=1..6, c=5 p=1..6: exact multiplicative orders via `pow(...,modulus)`;
- source-pulse recursion and positive remainder, four conductor stages, multiple clock points;
- certified *true orbit* interval upper bound from stage surrogates for every tested rational arc and horizon;
- exact certificate of first 300 Stoneham digits (lower/upper rational enclosures agree);
- exact de Bruijn order-2 cycle with all 256 ordered pairs but at most 256 of 4096 triples;
- biased full-support reset-invariant product, actual finite empirical frame bias on two normal systems, normal Champernowne choice-policy bias;
- exact sparse nonnormal conductor c=2 expansion (600 certified hexadecimal digits);
- original BBP rational forcing/selected recurrence and denominator variability; exact Haar cylinder frame reset;
- **hostile finite transfer failure**: original rational BBP phases on naive Stoneham c=3 stage p=2 equal bins `(9,7,2)` versus Stoneham's six each, and c=3 stage p=3 / c=5 p=2 also fail the Stoneham multiplicity.

**Independent oracle:** `independent_oracle.py` does **not** import `frame_reset.py`. It reconstructs rational conductor phases by direct pulse recurrence (rather than the primary modular-explicit formula) and checks c=3 p=1..6, c=5 p=1..4, each with **seven** Fourier modes. 75-digit complex sums confirm finite root-of-unity formulas, and independent exact future-tail holdouts p=1..4 verify source error. Raw `oracle_receipt.json` and `independent_oracle.log` retained. Independent implementation is *same reasoner*, not blind external peer review.

`compileall`: PASS. No source hash integrity mismatch claimed; see `SOURCE_MANIFEST.json` for source content hashes. **No full SUCC root suite, provenance scripts, new Lean formalization, hosted CI, or external proof review has been executed on this research branch.** The published base-16 normality result for coprime Stoneham constants is an external primary-source theorem; our special c=3,5 proof is an elementary derivation of that known theorem and not a priority claim.

## What finite tests cannot certify

The all-N, all-arcs uniform upper bound and the invariant-density implication are paper proofs in `RESEARCH.md`, **not** extrapolations from finite prefixes. The tested arcs/prefixes are mutation/regression checks. The c=2 nonnormality is a proof via explicit disjoint digit positions, not frequency sampling. No selected original π Weyl sum `o(N)` theorem, no authenticated odd conductor stage coverage for its rational prefixes, and no physical 'choice' measurement have been proved.

## Provenance, falsifiers and next gates

- Bailey–Crandall 2002 established normality of coprime Stoneham constants: https://www.tandfonline.com/doi/abs/10.1080/10586458.2002.10504704
- Bailey–Misiurewicz 2006 normality/hot-spots: https://escholarship.org/uc/item/2bp7q4b2
- SUCC `research/2026-10-29/OILY_STONEHAM_PATH_SHEET.md` previously examined the *base-2* Stoneham constant; this draft adds **base-16 c=3,5 and nonunit c=2** to align control radix with original BBP.
- Falsifiers: source-pulse schedule altered; nonunit c=2; de Bruijn local fairness; biased reset product; selected zero-seed vs nonnormal counterseed; initial digit/algorithm-dependent choice bias; exact finite naive modulus-grid BBP mismatch.
- Before any integration: rerun all commands in `AGENTS.md` against a clean branch checkout; check exact-head hosted CI and independent mathematical review; preserve main and frozen sources. No automatic merge authorization inferred from this research round.
