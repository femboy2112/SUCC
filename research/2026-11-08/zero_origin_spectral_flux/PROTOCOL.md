# Zero-origin spectral-flux experiment — frozen extension protocol

**2026-11-08. SUCC additive research; π base-16 normality OPEN.**

## Scope and chronology

The initial code, exact identities, hostile tests and **8,192-digit exploratory run** were developed first. They are **not** a blind or preregistered holdout. The next and only additional extension in this round is the first **16,384** zero-origin hexadecimal digits. No tuning based on its results is permitted. This protocol explicitly distinguishes mathematical identities, software validation, and descriptive data from the still-unproved all-epoch cancellation criterion.

### Fixed inputs for the extension

- Original four-pole BBP forcing, unchanged imported `observational_succ.duck_bbp.forcing` and exact `source_tail_budget`; literal `U0=0`, circle recurrence and certified tail enclosures for every digit.
- `N=16384`, checkpoints `16,32,...,16384`; chronological indexing starts at the first fractional digit of π. Independent rational Machin enclosure checks the first 128 digits.
- Full exact source-channel decomposition and phase reconstruction is required for the first **1024** steps; beyond that, the code retains the exact full BBP orbit, certified digits and carries but omits expensive exact three-channel histories. Channel histories beyond step 1024 are **not** claimed verified by this experiment.
- Cyclic window discrepancies at lengths `k=1,2,3`, exact rational chi-square energies `E_k` and exact `E_(k+1)-E_k` Fourier-sector flux. Linear-window signed arrival balances `D(M+1)-D(M)` separately, without confusing the two boundary conventions.
- Temporal FFT of `z_n=exp(2πi d_n/16)` at lengths powers of two, with all modes retained. Compare DC, largest nonzero line, period-16 mode and inverse participation. Parseval sum must be within `1e-9` numerically (the underlying theorem is exact).
- Digit-time residues `n mod 2,4,8,16`. Signed temporal work for `(h,q)=(1,2),(1,4),(1,8),(1,16),(2,16),(4,16),(8,16)` and mode `m=1`, with `|S_n|/√n` bins `1,2,3`. The bins can contain very few observations: never infer a drift sign from an undersampled bin.
- Original BBP unwrapped phase diagnostic and three-channel factorization are separate: three-channel data only for the 1024 certified channel steps.
- Controls: (a) a deterministic same-count shuffled permutation `seed=20261108`, (b) same-count sorted order, (c) balanced 16-cycle, (d) order-three de Bruijn 4096-cycle, (e) coherent zero sequence, (f) explicitly artificial, positive-probability periodic-mode-feedback generator at `beta=0.65, window=64`.
- 16 additional same-histogram shuffle replicates at seeds `20261109..20261124`; descriptive min/median/max only. No fitted significance thresholds, tail probability or confidence interval.
- No claim that feedback produces π, that an iid simulator is a mathematical null distribution for the original BBP orbit, or that concentration suppression is a conservation theorem.

## Exact pass/fail controls

1. Every digit must be uniquely determined by an exact rational two-sided BBP tail enclosure. Any failed digit is **FAIL**, not rounded away. The original source decomposition must match the four pole formula at each step, and all three channel fractional states reconstruct the full fractional state at every measured channel step.
2. Independent Machin rational intervals must certify and agree on the first 128 hexadecimal fractional digits.
3. On every prefix the cyclic marginalization and exact rational Fourier-depth flux law must hold with equality. The linear streaming surplus identity must hold with equality at every arrival. FFT Parseval error must be below `1e-9`.
4. Order-three de Bruijn cycle repeated an integer number of times must have exact energies `E1=E2=E3=0` and `E4=15`. Balanced repeated `0..F` must have `E1=0`, `E2=15`, and a single full temporal `h=1, q=16` Fourier line. Coherent zero must have DC energy one and no non-DC line. The same-histogram sorted control must have identical E1 to BBP while differing in higher-order temporal organization.
5. The source phase signed-lag energy must agree with the separate padded moving-sum calculation within floating tolerance; coherent phase control must not be reported as decaying.

## Verdict rule

No result from `N=16384`, however similar to shuffled controls, establishes π-normality, a true negative spectral drift, independence of digits, or the source-selected all-epoch `R_(A,h)(H_A)` bound. A useful finding is a reproducible temporal shape, an instrument failure, or a separating signature of a counterfeit. New conjectures must be labelled and given a next counterexample.

**Previous development snapshot:** 8,192 certified BBP digits; depth energies `(0.0015363693, 0.0303344727, 0.4964599609)`; spectral maximum `0.0011956`. This paragraph is disclosed to make clear which observations preceded the protocol.