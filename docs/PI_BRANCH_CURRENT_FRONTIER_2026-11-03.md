# SUCC's next π-normality front: original-source branch currents

**Status (2026-11-03): the original selected branch-current saving is OPEN; base-16 normality of π is OPEN; RH remains a separate OPEN program.** This document is a proposed concise main front door, not a retroactive change to existing theorem contracts.

## One objective

Preserve the original zero-seeded four-signed-pole BBP source `U_n=16U_(n-1)+r(n)`, with `U0=0` and literal integer carries. Let `mu_A` be the empirical distribution of `{U_n}` for dyadic epochs `[A,2A)`. At base-16 cylinder depth `K`, define exact energy

`E_K(A)=16^K sum_{|w|=K}mu_A(w)^2`.

Inherited PR #488 (and the elementary 16-ary martingale identity) proves

`E_K-1=sum_(l<K) 16^(l+1) sum_(w,j) (mu_A(wj)-mu_A(w)/16)^2`.

For `K_A=floor(log_16 log A)` and `m_A=16^K_A~log A`, inherited PR #476 proves CONDITIONALLY that `E_(K_A)(A)=o(K_A)` on all large dyadic epochs implies π normal in base 16. **No such original energy upper bound has been proved.** The single load-bearing problem is signed/near-pair nonconcentration of the actual Archimedean numerator and its original odd-prime cofactor/carry history.

## Boundary-stable target added in the current round

The same selected source gives an exact translation-averaged *observation* energy, without replacing its trajectory:

`J_(A,q)=(q/A²) sum_(n,t)(1-q||U_n-U_t||)_+`.

For every even `m>=4`, `E_(A,m)(canonical origin)<=4 J_(A,m/2)`. The original source Gamma tail also gives `|J_(A,q)(pi completion)-J_(A,q)(rational source)|<=q²(A-1)/(64A³)`—an error `o(1)` at q~log A without unproved boundary frequencies. Thus a new SUFFICIENT, **STILL OPEN** bound is `J_(A,m_A/2)=o(K_A)`.

The triangle Fourier representation supplies an explicit finite-band sufficient alternative, still unproved: for `q=m_A/2` show `sum_(1<=|h|<=ceil(q²))|A_A(h)|²=o(K_A)` for the original source; the tail of the sinc-square kernel is bounded by `2/π²`. These harmonics lie in the range where the source split/inert prime passports already prove exact nonalias, but that does **not** control real signed phases or source-selected cofactors.

## What to probe now

Construct an authenticated chronological cylinder-current equation from `x_(n+1)={16x_n+r(n+1)}`, carrying full original integer lifts, 2-primary/glued Gaussian structure, corrected split/inert p clocks, old p-free cofactor and positive Gamma flux. The source-forced translated-bin crossing rate satisfies `B_(A,q)<15q/[(8A+1)(8A+2)]`, but uniform stationarity is insufficient: `x=1/5` is fixed by ×16 and nonnormal. A real proof must derive an additional source-selected signed correlation/conditional-current saving, not average over all virtual inverse branches or apply a Galois average to one original real embedding.

## Review/merge structure

The live 2026-11-03 audit found three distinct active unmerged histories: PR #488 (main π/Gaussian/current line), PR #486 (E²/observer/figure-eight sibling) and PR #472 (causal/primes/oily-hbar sibling); their unique new path union is 394 at the observed parent heads, plus this research. See `research/2026-11-03/selected_current_front/INTEGRATION_AUDIT.md`, `PROOFS.md`, `VALIDATION.md`, and `CLAUDE_CONSOLIDATE_MEGAROUND.md`. Claude is requested to reconcile, run full native SUCC/Lean/CI validation, reorient the existing front pages, then merge verified research to main. Do not silently promote any draft mathematical status.
