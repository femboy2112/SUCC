# Fixed probes before selected-epoch output inspection

**2026-11-06, research-local preregistration.** This file is written and SHA256-recorded before running `holdout_probe.py`. It is NOT an independent blind preregistration service; all probes are designed and run by the same researcher.

## Input and unmodified source
- Original four signed BBP poles, literal `U_0=0`, exact `Fraction` recurrence; no π digit tables.
- Independent arithmetic: exact combined `A(n)/D(n)` and Machin `π/16 = atan(1/5) - atan(1/239)/4`, with alternating-series rational remainders.
- Certified zero-seed digits for lengths `N=384,768,1536`; 16-state reversible observer `c_n=d_n+q_n+σ_n mod16`, `q_next=q+3d+2σ mod16`, `σ_n=(8(n+1)-7) mod7`, initial `q_0=0`.
- Report empirical entropy deficits `Δ_X(k;N)` and `Δ_Y(k;N)` for `k=1,2`; output/input ratio for `k=1` if well-defined. No fitted parameter or alternate machine selection.

## Signed joint-character finite bound (new, fully rational verification)
- Epochs `A=223,457`, characters `h=1,2` of original selected completed circle orbit `z_n={U_n+T_n}` for `n∈[A,2A)`.
- Approximate each phase by a binary rational 2^-40 grid; bound phase and Machin-π errors rigorously. Use rational cosine/sine Taylor polynomials of degree 24/25 (M=12) with Lagrange error and `π<22/7` to obtain a **rigorous rational interval** for `|W_A(h)|`. The bound must not rely on raw cmath floating values or unverified π digits.
- Calibration: exact uniform 16th-root grid, `h=1,2` should have near-zero certified upper bounds. Exact constant completed `β=1/5` for all n has `|W_A(h)|=1`, and certified lower bound must exceed `0.99`. The two genuine selected epochs are **OBSERVED-FINITE**, no claimed trend or universal estimate.

## Negative / mutation probes
- Deliberately change the first source pole value by +1/37 at the first step: the finite source-digit comparison against independently certified Machin digits must reject the mutant.
- Constant input + 7-period source gives a periodic output, not normal, regardless of apparent short-word uniformity.
- Constant input + a separate normal external digit tape (base-b Champernowne) can output normal: shows why positive source entropy is a real loophole.
- Finite order-5 de Bruijn periodic tape detects the **finite** omission of source entropy in the debt inequality, but is explicitly not an asymptotically normal tape.

## Verdict thresholds, fixed beforehand
- All zero-seed signed reported bounds must contain the actual character mathematically by their error proof, whether small or large. A nontrivial (<1) upper bound is a valid *finite certificate only*.
- If control lower/upper interval fails or Machin/source digits diverge, record failure; do not post-hoc change epochs/thresholds.
- If the source-coded entropy deficit is larger than the raw deficit, record it. There is **no predeclared improvement claim**.
- π normality, selected signed Weyl `o(1)`, log-scale stationarity and Haar transfer all remain OPEN without an infinite-time source-selective argument.
