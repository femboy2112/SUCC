# Source-selected signed lag finite receipts — exact rational enclosures

**2026-10-31. OBSERVED FINITE / independently reproducible finite arithmetic.** All selected cases use exact original signed four-pole BBP, U0=0, h=1, K=4. Source-scoped mathematical LAG-01..04 proofs are in PROOFS.md. The signed phase interval computation is deterministic, rational and outward-rounded; **no limit, π normality, RH or new arithmetic upper saving is claimed**.

## Certified finite data

Each raw score interval is a pair of exact rational bounds [lo,hi] enclosing the SINGLE source-selected signed real cosine observable L_(N,4)(1). The coherent nonnormal same-forcing counterseed has an independently derived rigorous lower bound. The VdC column is a rigorous rational UPPER bound on the selected |S_N(1)/N|², not an observation of actual |S_N|².

| N | Selected L lower | Selected L upper | Coherent altered-seed L lower | Selected normalized |S_N|² upper |
|---:|---|---|---|---|
| 512 | -620250446467/163840000000000 | -7753130579303/2048000000000000 | 60161/114688 | 692840117852322537/1468006400000000000 |
| 1024 | -37498145618503/4096000000000000 | -14999258246173/1638400000000000 | 146177/229376 | 4150060982468262303/11744051200000000000 |
| 1536 | -1446341069911/192000000000000 | -92565828465091/12288000000000000 | 232193/344064 | 4659713953327286073/14680064000000000000 |

Decimal views of EXACT intervals: N512 L in (-0.003785708292,-0.003785708290), bound square <=0.471959875552; N1024 L in (-0.009154820709,-0.009154820707), square <=0.353375586653; N1536 L in (-0.007533026407,-0.007533026405), square <=0.317417822793. These decimal inequalities are deliberately rounded outward and are not the proof certificates; the raw fractions above are.

## Error policy and independent checks

- Original r(n) is computed as exact Fraction arithmetic, source zero-seed recurrence is never seeded from known π digits.
- Phase x = h(16^k−1)U_n modulo 1 is computed **exactly** as a rational; first it is rounded to a decimal rational midpoint of width 10^-20. Its phase-error is bounded by one-half that cell width.
- π is bracketed by the classical Machin identity 16 arctan(1/5)−4 arctan(1/239), with alternating rational arctan series and explicit first-omitted-term errors. There is no high-precision float oracle.
- cos(2πx) is enclosed using a finite exact rational Taylor polynomial (default 17 terms), Taylor's global bounded-derivative remainder and the π/phase-rounding Lipschitz costs. Outputs are rounded OUTWARD to multiples of 10^-12 before adding weighted signed lags.
- The all-horizon source error uses only the original four-pole positivity bound and π<22/7; the coherent counterseed lower bound is an independent analytic source-tail calculation.
- All rational finite results use the same code implementation, so the three measured horizons are time holdouts, **not independent mathematical source families**. Other modes h and lags K require fresh separately certified results.

## Reproduction commands on the combined research branch

    python -m unittest discover -s tests -p 'test_selected_lag_tomography.py' -v
    python research/2026-10-31/selected_lag_tomography/run_receipt.py 512 4
    python research/2026-10-31/selected_lag_tomography/run_receipt.py 1024 4
    python research/2026-10-31/selected_lag_tomography/run_receipt.py 1536 4

The three full-horizon receipt runs were **actually executed locally** against the exact file content uploaded to GitHub, before this handoff. Exact source code blob SHA-1 59d0351484865ab919317ae1a34f6e9ec1b12da3; independent source oracle d4c5a4a815fe3d8beb29b075972e2de03eb63fdf; receipt runner f294eb5ae0c6b77fe300623591755c27e0037304; exact root test 55a5857cc8e1b13606dac4edb9fd479775d82ca4. Those blobs were verified byte-for-byte against local tested copies before the atomic Git tree commit. The exact SUCC full-root suite and Lean/hosted CI are separate and must not be claimed from these receipts.

## Required holdout interpretations

- At N=512, K=4, selected signed lag L is certainly negative, while the *fixed* coherent same-forcing irrational altered seed has L>0.52456. At fresh N=1024 and 1536, the same fixed K=4,h=1 comparison also holds.
- The *distinct* irrational near-zero nonnormal shadow seeds from PR #433 can reproduce these selected finite L scores arbitrarily closely for any preassigned finite horizon while having exactly rational completed trajectories. Therefore no finite signed certificate can prove the infinite selected normality statement.
- A valid unconditional proof needs an ALL-HORIZON source-selected signed estimate, with time/frequency coverage and exact original U0=0. The finite intervals only validate the measurement and identify discriminating hypotheses.