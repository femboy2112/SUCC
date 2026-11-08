# Hostile controls — no illicit anti-clumping or hidden iid law

All statements are for base16 and the finite word-energy definitions in [THEOREMS.md](THEOREMS.md). Finite tests are not universal proofs. The original signed source is untouched in the comparisons.

## CM1. Normality does not imply a diffusive moving-resolution walk — PROVED

Start from a base16 Champernowne sequence (normal to its construction base by a classical theorem). After copying `M_j=2^(2^j)` base digits insert `L_j=M_j^(3/4)` additional zeros, for each j≥2. The insertions have density zero: their total up to any horizon N is o(N), so their effect on any *fixed* length-t word frequency is o(1) (including O(t) disturbed contexts per insertion). The new sequence is normal.

At the end `N_j~M_j` of one giant inserted block and k=`k_W(N_j)`, which is O(log N_j), at least `L_j−k+1` copies of `0^k` occur. Its expected uniform count `N_j/16^k` is O(log N_j). One summand in the count-discrepancy energy forces

`D_k(N_j)≥(L_j−k+1−N_j/16^k)^2=N_j^(3/2+o(1))`, hence `E_k(N_j)≥N_j^(1/2−o(1))`.

The sufficient Lambert entropy gate `log(1+E_k)=o(log N)` fails spectacularly at these sparse horizons, while normality survives. Thus our new criterion is **not necessary**; its negation does not imply nonnormality.

## CM2. Uniform one-digit counts do not give high-depth entropy

The repeated cycle `0123456789ABCDEF` has uniform single-digit counts but only 16 possible two-digit words. At cyclic depth k≥2, its collision energy is `16^k/16−1`, so the deficit is `(k−1)log16` and grows linearly in k. The entropy amplification theorem detects it as soon as t=2. A repeated order-3 de Bruijn cycle is balanced through depth 3 but becomes periodic and nonuniform at larger depths. Source-agnostic word conservation proves neither normality nor irrationality.

## CM3. Complete coverage does not imply low energy

For a finite prefix with each symbol observed once and hundreds of extra zeroes, **every single symbol has appeared** but one symbol dominates the collision energy. This refutes 'eventually every type appears ⇒ normality', even at one digit depth. The same construction applies to word types by inserting a covering de Bruijn cycle followed by repeated zeroes.

## CM4. The discrete Lambert depth creates a fake 'energy injection'

At N=32,768, the observed Lambert depth is 2 and original π data have `D_2/N≈1.0105`, `E_2≈0.00789`. At N=36,864, k_W jumps to 3, and data have `D_3/N≈0.9925`, `E_3≈0.11028`. The large increase in **raw E** is explained predominantly by the number of distinguishable word types jumping from 256 to 4096. The count-space displacement normalized by N stays near one. This is **not** a measured restoring force or new physical energy.

## CM5. The fixed π normality target needs real zero seed and chronological source

A same-forcing coherent counterseed `s_*=-π/16` satisfies `U_n(s_*)=-T_n` and has circle characters tending to one. The class of normal digital strings and its entropy bounds does not distinguish original and counterseed without source and initial-state provenance. A prime-local/source-only Gram is insufficient; earlier #544, #554, #555 and #559 controls remain relevant.

## CM6. No inference of independence from finite shuffle agreement

At N=40,960, the measured Lambert-depth D/N of π lies in the range of 16 fixed-seed same-count shuffles. This does not establish iid digits, a confidence interval, normality, or an emergent compensating physical mechanism. Under independent uniformly sampled *words* the coupon reference is classical; real digit blocks overlap and have correlated acquisition times even under an iid digit reference.
