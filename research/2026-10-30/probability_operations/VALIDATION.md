# Operation Probability Operations — exact validation and provenance receipt

Date: 2026-10-30. Draft additive continuation from exact PR #409 head `3857e70472cac7c572528cc6d4198246e57d36df`, itself stacked on #406/#404/#402/#397 and Main XVI `e18ba565ca540adb7edf3292f5593929e76d91c5`. Original signed BBP four poles, authentic U_0=0, historical source/proof contracts, CI, production and main untouched.

## Executed tests

`python probability_operations_probe.py`: **11/11 exact stdlib unittest methods PASS**. Includes original positive four-pole rational source and exact 64-digit hex prefix, Beta(c,1) sqrt-max false-positive, normal graph-Haar dependent-tail false-negative 1/8 vs1/9, quantized disjoint grid finite CDF bound ≤3/16^k, genuine fair digit branch identity, coherent δ0 model discrepancy exactly 15/32, periodic 16-digit first-order-uniform negative, exact two-sided finite W1 stability on periodic controls, finite BBP certified raw-state and generative-operation Wasserstein comparisons, and cyclic-subgroup convolution-idempotence negatives.

Separate `python independent_probability_oracle.py`: **PASS**. SymPy independently integrates the first seven inverse-branch Lebesgue moments; high-precision mpmath Gamma integrals agree with digamma/Oily readout at ranks r=2,3,4,6; an independent EXACT rational Machin arctangent interval agrees with original BBP first 80 hexadecimal digits; an independent CDF-area Wasserstein implementation agrees *exactly as rational numbers* with the test program's quantile algorithm for N=32,128,256.

Raw stdout/stderr are preserved in `RAW_TEST_LOGS.md`. Both locally tested `.py` files are byte-hashed with Git blob SHA-1 and SHA-256. The subsequent remote GitHub commit must match these exact source bytes; GitHub PR/CI after commit is separate from local execution.

## Finite BBP-certified demonstration

- N=32: quantized ε=0.115532192401..., quantized W1(raw,Haar)=0.122901951..., rigorous upper bound =0.125317672... .
- N=128: ε=0.043046656679..., raw W1=0.045715792..., rigorous upper=0.046437268... .
- N=256: ε=0.014679132558..., raw W1=0.015136004..., rigorous upper=0.015918159... .

These are rational data from original BBP source intervals with each state approximated to 8 subsequent hexadecimal digits. The exact state-vs-truncation error is ≤16^-8 and the operation defect error ≤(17/16)16^-8. The displayed upper is for actual (indeed a slightly looser bound that also adds one extra truncation error). No asymptotic rate, monotonicity or base-16 π normality theorem follows.

## Limit/independence firewalls

- `sqrt(U) =law max(U1,U2)` requires independent inputs. A Beta(2,1) and the coherent δ0 pass the identity too; it cannot alone identify Haar.
- Even under hypothetical base16 normality, `(x_n,x_(n+1))` tends graph-Haar, not independent Haar². Its maximum CDF at t=1/3 is 1/8, not 1/9. A falsely constructed observer can appear to refute a normal stream.
- Correct disjoint fixed-k digit blocks give asymptotically independent **discrete** grid uniform draws. Take horizon→∞ first, then k→∞; no uniform k-dependent convergence assumed.
- The fair inverse-branch operation has unique Haar fixed point with explicit two-sided Wasserstein stability. The criterion ε_N→0 iff normality is logically decisive **only when verified for infinite horizons**. Finite ε_N cannot prove nonnormality.
- The Gamma/Oily operation law is exact for ideal independent uniforms. Raw empirical log-Gamma expectations need tail control/uniform integrability beyond weak convergence; we do not claim direct untruncated averages from normality alone.
- Circle convolution μ*μ=μ characterizes Haar ONLY with additional nonatomic/full-support hypothesis. Finite cyclic subgroup Haar measures are idempotent and nonuniform on the full circle.
- The source's forced orbit and pure radix reference can be close in circle W1, but the digit-label readout is discontinuous at radix boundaries; seam controls are necessary.
- Complete AGENTS.md root suite, hosted exact-head CI, Lean, independent peer review **NOT RUN** in this standalone local round; no inference of physical randomness, π normality or RH.

## Remaining decisive mathematical obligation

Prove an original-source-selected asymptotic bound on ε_N from the exact four-pole recurrence, zero seed, full carry lifts and CRT interactions, *without* assuming its unknown digit distribution. A proven `limsup ε_N>0` would refute normality, or ε_N→0 prove it. Both remain unverified. Include coherent seed -π/16, source mutants, Stoneham 3/5 controls, de Bruijn finite mimics and disjoint-vs-overlapping blocks.
