# Floor-layercake source observer: continuous thresholds → signed Fourier carries

**2026-11-09, research child of draft #563. π normality: OPEN.** Original four-pole BBP source, `U_0=0`, original signed p-primary/Frobenius source and real carries remain intact. This is an additive research instrument with honest arithmetic and reference-measure boundaries, not a proof of normality.

The user's proposal is that integrals of floors are sums of integer-weighted continuous integrals. In the BBP carrier this becomes a literal 16-threshold description of every real and prime carry. The exact carry-character Fourier transform occupies one arithmetic progression `m≡h (mod16)`; each surviving Fourier coefficient is twisted by the **authentic forcing** `e(m r(n)/16)`. Thus the source is carried through to the Fourier observer rather than replaced by a uniform digit ensemble.

The crucial negative control is that the uniform-phase reference integral of every nontrivial carry character is **exactly zero for every source forcing**, while a p-integral rational changed seed such as `s=1/5` preserves all p-primary histories and changes *every* real carry modulo16. Therefore the source-integral zero cannot be transplanted to the realized zero-seed BBP path. The remaining signed boundary discrepancy and complementary slip are precisely identified in [THEOREMS.md](THEOREMS.md).

A new **quadratic resolution barrier** follows: under Fejér smoothing with bandwidth H, the original forcing changes the observable by at most `O(H/A²)` on epoch A. Thus H=o(A²) suppresses this source twist even before testing the real orbit; resolving the microscopic forcing requires A²-scale frequencies and a separately paid digit-boundary budget. This aligns structurally with the previous #555 relative-source spectral threshold, without proving normality.

The positive original four-pole Laplace source also admits a closed formula for `E[z^floor(LX)]`; its native-rank Gamma(2) limit is explicitly **non-Haar**, preventing another false short-circuit.

**Research files:** `observational_succ/bbp_floor_layercake.py`, `tests/test_bbp_floor_layercake.py`, `THEOREMS.md`, `CLAIM_LEDGER.md`, `VALIDATION.md`. No original files modified. Reproduce the 16 local focused tests with `python -m unittest discover -s tests -p 'test_bbp_floor_layercake.py' -v`. Full native suite/provenance/Lean and hosted CI on the exact pushed head are independent gates.
