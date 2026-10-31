# Carrier first: certified transport and the selected-phase boundary

Research child of [PR417](https://github.com/femboy2112/SUCC/pull/417), pinned
at `1c6ce7d7ee83a0bd751bde8092e46ff798855fd3`. Work began on 2026-10-30
America/New_York; receipts use UTC and extend into 2026-10-31. Main was
`e18ba565ca540adb7edf3292f5593929e76d91c5`. Every change in this child is
inside this directory. No sibling branch was merged.

**The strongest results are two quantified source-to-selected-phase
transports and a countermodel that exactly matches any prescribed BBP
rational-state prefix yet fails the moving-band target. No new asymptotic
upper bound for authentic selected Weyl sums or collision energy is proved.
Pi normality and RH remain OPEN.**

## Surviving mathematics

* **Original source moments give a rational boundary enclosure.** If p_d is
  the monic orthogonal polynomial for the authentic positive BBP Hausdorff
  measure and R_d its Gaussian resolvent, then
  `0 < pi/16-R_d(16) < 188/(225*3600^d)`. A sharper fully rational interval
  uses the norm of p_d. The center needs 2d source values; the interval needs
  2d+1. At d=19 its width is about `1.22737e-71`. This is improved precision
  transport, with growing denominator cost, not cancellation.
* **All-horizon prime-frame transport.** A growing-order signed derivative
  stencil of genuine positive rational source frames gives explicit
  `A_n=sum_p beta_(p,n) log p` with `|U_n-A_n|<=1/(120n^3)` and total error
  below 1/315. Its square-root Fejer energy differs from the authentic one
  by at most `C H^(5/6)/N`, where `C^3=9pi/(80sqrt6)`. This vanishes even
  when H is proportional to N. Every sign, source factor and zero boundary
  is retained. No estimate for either energy follows without further work.
* **Finite-band indistinguishability has a sharp limit.** For every d a
  positive rational-valued Gaussian source with zero seed agrees with
  U_0,...,U_(2d), hence with every finite-band energy on that prefix. For
  each fixed such source, `log F_(H_N,N)/log H_N -> 1` whenever H_N tends
  to infinity and H_N=o(N). The source is changed after the prefix.
* **An embedded observer has a finite empirical certificate.** Actual
  digit/future-bin counts give an exact Wasserstein bound with explicit
  resolution and endpoint errors. It yields a certified finite h=1
  normalized Weyl upper bound `80707/286720` at N=1024. This is a finite
  calibration only. Sampling too few points in overly fine future bins
  produces a provable information-deficiency floor.
* **The carrier has explicit arrows and descent conditions.** Labeled
  paths, signed completion, colored multiplication recovery and matrix
  umbral calculus have exact APIs. Forgetting path order is valid precisely
  when every reachable diamond defect vanishes. The actual BBP source has
  a strict unwrapped chronological ordering inequality; it survives the
  coherent changed seed and therefore provides no circle cancellation.
* **Analytic continuation has paid errors and identifiable inputs.** Finite
  theta/Mellin completion has rational uniform derivative-tail bounds. The
  complete Archimedean-corrected zeta germ at -1 determines the positive
  prime-power measure; every finite jet admits explicit positive weighted
  countermodels. Those countermodels violate the exact divisor law and
  are not alternate authentic Euler products.

## Read and reproduce

| Purpose | Artifact |
|---|---|
| Typed maps, author's triangle and zeta interpretation | [CARRIER_ASSEMBLY.md](CARRIER_ASSEMBLY.md) |
| N/Z paths, noncommutative transport and Lean scope | [algebra/ALGEBRA_THEOREMS.md](algebra/ALGEBRA_THEOREMS.md) |
| Source resolvent, theta and prime germ | [analytic/ANALYTIC_TRANSPORT.md](analytic/ANALYTIC_TRANSPORT.md) |
| Selected prime frames, errors and Fibonacci counterexample | [selected/HIGH_ORDER_FRAMES.md](selected/HIGH_ORDER_FRAMES.md) |
| Embedded observer and actual finite counts | [OBSERVER_THEOREMS.md](OBSERVER_THEOREMS.md) |
| Prefix-exact countermodel and asymptotic band verdict | [FINITE_BAND_COUNTERMODEL.md](FINITE_BAND_COUNTERMODEL.md) |
| Routes, failures, source-selected missing lemma | [CLAIMS_AND_ROUTES.md](CLAIMS_AND_ROUTES.md) |
| Execution, proof authority and reproduction commands | [VALIDATION.md](VALIDATION.md) |
| Source heads, sibling boundaries and reviews | [PROVENANCE_AND_REVIEW.md](PROVENANCE_AND_REVIEW.md) |
| Next executable mathematical obligation | [NEXT_HANDOFF.md](NEXT_HANDOFF.md) |

All proofs are local paper arguments except the seven explicitly scoped
Lean declarations. Separate implementations and same-model cross-reviews
are not independent external mathematical authority. The DeepSeek sibling
was read and pinned; no live DeepSeek run or external referee is claimed.
The user-defined Harmonic/Golden/Euler--Mascheroni/Fibonacci roles and
Oily--Macaroni naming remain attributed to their preserved author records.
