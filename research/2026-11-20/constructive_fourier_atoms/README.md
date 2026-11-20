# Operation Constructive Fourier Atoms — source-labelled causal spectral bookkeeping

**20 November 2026.** Research-only, additive SUCC dossier. Based on open draft [#674](https://github.com/femboy2112/SUCC/pull/674) at `ec4f99bbd9ec34461ba7393c15833b966284cc05` (stacked above #673 and #672); original Main XXVI at `81be6b897ae980b801a3b9de9e22ef81e8360bfb`. Nothing modifies the original BBP forcing, literal `U_0=0`, import manifest, frozen history, application code, defaults, or CI.

## Research question

Can source-labelled finite causal succession *construct* the compatible Fourier probes of its observer rather than have Fourier structure assumed externally? Can those probes be glued across the real and prime-adic frames without manufacturing a false π-normality argument?

**Yes, for precisely declared additive and affine causal laws.** We derive an explicit 3/5-adic odometer clock, its complete finite Fourier eigenbasis and a unitary change of basis from ordinary state characters; the 2-adic completion has a different attracting role. The **original** four-signed-pole BBP source also generates a separate analytic event-time Fourier transform, and we derive a strict constructive-interference gap with the exact coefficient `2491/12579840`. The authenticated affine source path admits an exact covariant product of phase atoms with a terminal-tail error bound. None establishes a cross-place semiconjugacy into the real phase, a signed all-shell Weyl estimate, R0, base-16 normality or RH.

## Entry points

| Resource | What it contains |
|---|---|
| [THEOREMS.md](THEOREMS.md) | CFA-01–10, full paper derivations, source typing, spectral dichotomy, proved counterexamples |
| [causal_fourier.py](causal_fourier.py) | Pure stdlib original-BBP source, finite odometer labels, additive and causal Fourier atoms, rational terminals |
| [test_causal_fourier.py](test_causal_fourier.py) | 25 targeted tests covering all claimed finite identities, negative controls and unitarity |
| [independent_audit.py](independent_audit.py) | Independent SymPy/ms precision construction of BBP Mellin Fourier and 3/5 clock, without importing the stdlib code |
| [independent_audit_receipt.json](independent_audit_receipt.json) | Raw audit summary for replay (no external expert review) |
| [CLAIM_LEDGER.md](CLAIM_LEDGER.md) | Scoped statuses, receipts, falsifiers, φ/σ/μ boundaries |
| [NEXT.md](NEXT.md) | Preregistered source-faithful signed joining probe and reject/accept gates |
| [PROVENANCE.md](PROVENANCE.md) | Main/PR ancestry and exact classical vs source-specific vs novel-to-dossier distinctions |
| [VALIDATION.md](VALIDATION.md) | Executed commands, exact results, unrun gates, limits |

## Results most worth reading

1. **Frequency transport instead of magical Fourier emergence.** Additive causal composition has circle characters. Affine `u↦16u+r(n)` transports the dual frequency: `e(h(16a+b))=e(16ha)e(hb)`. The original phase is an exact source-labelled chronological atom product with no erased integer lifts.
2. **Causal-clock diagonalization.** The geometric clock `J_n=(16^n−1)/15` is a 3- and 5-adic isometric odometer. Its clock-coordinate Fourier characters are Koopman eigenfunctions; ordinary additive characters of the state `J` mix frequencies. A finite explicit **unitary change of basis** connects the two. Both the frequency mixing and its repair are exact, and the compatible finite quotients lead to the standard p-adic harmonic hierarchy.
3. **The 2-adic observer is different.** The same integer `J_n` tends chronologically to `−1/15` in `Z_2` but admits no continuous 2-adic clock-time extension `n↦J_n`. The rational product formula relates the real, 2-, 3-, and 5-adic sizes of the same source displacement without asserting physical energy conservation.
4. **An original-source constructive interference gap.** The positive finite measure on event time with weights `16^-n r(n)` has Fourier transform `F(e^(iω))=∫_0^1 Q(t)e^(iω)/(16−e^(iω)t^8)dt`, with `F(1)=π/16`. The first two source atoms give `|F(1)|²−|F(e^(iω))|² ≥ (2491/12579840)(1−cosω)`. This is **not** the orbital Weyl sum.
5. **Spectral contrast and boundary.** The real circle Koopman `f(θ)↦f(16θ)` has no nonconstant eigenfunctions on `L²(T,Haar)`, unlike the 3/5 clock odometers. This is not a contradiction: they are distinct dynamical compactifications and the Haar statement says nothing by itself about the distinguished π trajectory.

## Reproducibility

From this directory:

```sh
python -m unittest -v test_causal_fourier
python independent_audit.py   # optional SymPy and mpmath
python -m compileall -q causal_fourier.py test_causal_fourier.py independent_audit.py
```

The test suite was executed locally: **25/25 PASS**. Independently written SymPy/mpmath audit: **PASS**, with 5,303 exact clock/valuation assertions, 244 exact source/mutant prime residue assertions, and four 75-digit analytic integral comparisons. The full inherited 14k+ SUCC tests and four `AGENTS.md` root gates were **not** run on this isolated artifact; hosted CI, Lean and external review are **not claimed**.

## The actual unsolved arrow

The 3/5 odometer clock, event-time source spectrum, and real-circle Weyl spectrum all have authenticated finite *connections through the same rational source labels*, but there is **no proved finite-to-infinite, signed, uniformly conditioned joining** that transfers clock/source spectral activity into a positive all-late-shell displacement of the authentic zero-seeded π phase. The same forcing with seed `−π/16` and a constant-forcing locked model kill source-blind inference. The matched-jet mutant `Q+(1−t)^2` kills generic source-positivity inference. See [NEXT.md](NEXT.md).

**Status:** exact constructive spectral architecture and useful controls; π normality, R0 and a source-specific signed all-shell inequality remain **OPEN**.