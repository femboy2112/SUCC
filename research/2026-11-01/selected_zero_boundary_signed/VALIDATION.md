# Validation — selected zero-boundary signed-lag attack

All runs on the compliant environment (Python 3.12, mpmath 1.4.1, numpy 2.5.0), **without**
`python -I`. Self-contained: `probe.py` and `test_selected_zero_boundary.py` import nothing from the
repo tree.

| Check | How | Result |
|---|---|---|
| SZB-01 exact reduction | `test` recurrence `U_n(0)−U_n(s_*)=16^{n−1}π` to 1e-45, n=1..24 | PASS |
| SZB-02 positivity refuted | `probe.py` grid `d∈{2,3}`, `h∈{1,3,5,7}`, `N∈{16384,65536}`; `test` at `N=8192` | 16/16 configs negative per-lag corr; aggregate sign-oscillates → REFUTED |
| SZB-03 angular period | `mp.quad` of `P/(16−t^8)` on `[0,1]` vs `π/16` to 1e-38 | PASS (match) |
| SZB-03 seed-blindness | `q=1/5` orbit `|S_N(h)|/N` at `N∈{2000,4000}`, `h∈{1,2,3}` | `=1.0000` (nonnormal) → representation identity |
| SZB-04 within-cell = shifted gate | digit-shift of `|S_N(h·16^k)|/N`, `k=1,2,3` | small (~0.007/0.002) and equal up to the finite-window/boundary shift → OBSTRUCTION |
| regression suite | `python -m unittest test_selected_zero_boundary` | **Ran 5 tests, OK** |

Receipts: `COMBINED_LOG.txt` (full probe output). Finite N only; no claim is made about any
all-horizon limit. The firewall is unchanged: base-16/base-3 π normality, the signed Weyl gate
`∀h≠0: S_N(h)=o(N)`, RH, Weil positivity, general Collatz, and shifted Lonely Runner n=18..94 remain
**OPEN**.
