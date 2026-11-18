# PR #663 refresh: wavelet, Pascal and Gamma audit

**Source-time pins:** earlier inspected #663 `16d04ab58e213e75ab47e61a170138196dbcd292`; refreshed head `814cfe06999f9083b5c2eee479d21bfb951d724f`. Main remains `81be6b897ae980b801a3b9de9e22ef81e8360bfb`. This read-only audit covers only the new six-file delta between those #663 commits. No donor branch was modified, merged or executed.

Read at the refreshed SHA:

- `research/2026-11-17/causal_clock_scrambling/BORWEIN_WAVELET_PASCAL_GAMMA.md`
- its `_VALIDATION.md` companion;
- `observational_succ/bbp_tail_impulse.py`;
- `observational_succ/borwein_scale_renormalization.py`;
- `tests/test_bbp_tail_impulse.py`;
- `tests/test_borwein_scale_renormalization.py`.

**Verdict:** no load-bearing mathematical error found in the new stated bounds. They add source-independent observer inequalities, exact source-tail identities and convergence to the analytic source carrier. They do not establish any original-source winding or phase cancellation estimate. All four original-source verdicts remain OPEN: terminal coercivity, R0, swept convergence, and full normality. This is a same-model read-only derivation audit, not external review or a replay of the donor's tests.

## New mathematical claims and scope

1. **Finite atomic floor:** for every N-point empirical circle measure, `V_N>=c_*^2/(16N^4)` with `c_*=2205/139876`. The Fejer diagonal contributes at least 2, forcing at least 1/2 of unweighted positive-frequency mass below 2N. The inherited h^-2 transfer floor then proves the constant. Equally spaced grids have `V_N<968/(250563N^4)`, so exponent 4 has the correct order. This is a universal instrument floor; it supplies no upper decay for pi.

2. **Exact block and wavelet identities:** `E_(A union B)=(E_A+E_B)/2-D`, `D=||F_A-F_B||^2/4`. For an actual radix orbit the second block's h mode equals the first block's `16^N h` mode. A shared rational terminal obeys the same exact rational-angle identity. The source-tail comparison for sqrt(D) is valid with `16r(a+2N+1)/(7225N)`. The arbitrary binary-tree budget is exactly `C_atom-V_N`, where `C_atom=335872/304434045`; the node mass normalization is correct for unequal children. Saturation of this budget is explicitly another normality-equivalent target, not a proved limit.

3. **Dense-horizon interpolation:** the prefix-feature bound `64(N-M)/(289N)` is valid (conservative). Decay on horizons with successive ratio tending to one therefore extends to all horizons. The text correctly declines to obtain that extension from dyadic endpoints alone.

4. **Actual chronological Pascal hierarchy:** `T_N=int t^(8N)K(t)dt` and `S_(N,k)=int t^(8N)(1-t^8)^k K(t)dt` are exact. Positivity, Pascal recursion and binomial mass conservation hold for both full and fixed-M truncated source measures. The rational remainder bound uses the positive decreasing k-th source difference, with the correct factor `16^-M/15`.

5. **Gamma asymptotics:** the fixed-k coefficient `Gamma(k+2)/64`, fixed-N coefficient `Gamma(N+1/8)/32`, and joint proportional-order rate `lambda log lambda-(1+lambda)log(1+lambda)` agree with direct endpoint/Beta/Laplace calculations. The locked kernel's order-axis coefficient is exactly ten times the original. This discriminates kernels; it is not a winding bound.

6. **Source-carrier convergence:** the binomial observer coupling gives `W1<=1/(2sqrt(m))+16^-M r(M+1)/(15P_M)` for M,m>=1. The normalization/tail mixture argument is correct. Its limit is the normalized pushforward of K(t)dt under y=t^8, explicitly not the pi phase empirical measure.

The locked Mellin countermodel and near-invariance identity remain valid and show why none of these positive constructions selects Haar on the actual circle orbit.

## Minor qualifications, not theorem failures

- The interpretation says each successor exposes an **independent** block contrast. Nonzero or linearly independent contrasts in the feature Hilbert space are not guaranteed; a locked list makes every contrast zero. Read this as an additional tree-index contrast, or qualify orthogonality in the index-space wavelet decomposition. The actual nonnegative ANOVA formulas are correct.
- State `M>=1` explicitly wherever `P_M` divides the observer weights or the W1 bound. The implementation already enforces this; M=0 would have P_0=0.
- Both new test files place `if __name__=='__main__': unittest.main()` before a second test class. Direct file execution omits that later class (8 rather than 13 tail tests, and 12 rather than 16 scale tests). The **reported** `python -m unittest module...` command imports both files and does discover all 29 new methods, so this does not invalidate the reported 53-method suite. Reproduction should use that module/discovery route or move the main guard later in a future donor change.
- The suite includes asymptotic floating diagnostics, including an optional mpmath test. Its statement of 53 passes is an inspected donor receipt, not a local replay here; do not label all 53 as exact-arithmetic checks. The exact rational assertions have their own scope.

## Novelty accounting after refresh

The new N^-4 finite floor, block/tree budget, and Pascal-carrier convergence should now be credited to #663 at the refreshed SHA. They do not overlap away this operation's exact measure inverse, sharp supremum-to-interval exponent 1/2, or sharp energy-to-interval exponent 1/5. The six-file delta does not change #663's earlier V^(1/6) all-word estimate; the root's V^(1/5) refinement remains a refinement of that inspected statement. No new arithmetic category-D/E result for the normality gap appears.

## Blob and execution provenance

The four source/test Git blobs at the refreshed commit exactly match the hashes printed in its validation document:

- scale module: `a406f4877c1614f434194c43cb06e8956caf3de9`;
- tail module: `54399f281f60ebb01c1d6e461e69242e65460c6a`;
- scale tests: `3ed7ef3a67f78d15de5ed89db0e784358fd5ac3d`;
- tail tests: `3e1cf1e56301d4e9cf4f02ba2fe07c03c008625c`.

No new tests, broad runs, numerical quadratures, Lean checks, hosted-CI checks or source edits were performed by this refresh audit. Donor claims of 53/53 scoped passes and unavailable full-head gates retain the donor's stated authority and exact commit boundary.
