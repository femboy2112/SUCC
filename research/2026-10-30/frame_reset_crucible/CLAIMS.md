# Scoped claims FR-01…FR-12 — frame-reset / normal-digit calibration

This research branch uses classical theorems in a source-faithful SUCC implementation, not a claim of new mathematical priority. All finite programs are exact unless expressly identified as numerical witnesses. **The π base-16 normality and RH targets remain OPEN.**

| Claim | Domain / conclusion | Status | Calibrated falsifier or missing proof |
|---|---|---|---|
| FR-01 | For `T(x)={16x}` and fixed finite word w, `R_w(mu)=(T^|w|)_*(mu|C_w/mu(C_w))`; inverse branch `g_u o g_v=g_uv` | DEFINED / elementary exact | Conditioning undefined for zero-mass cylinder, cannot call it a physical path change |
| FR-02 | For Haar, all fixed-word resets Haar; empirical fixed-word resets of a normal point converge to Haar | CLASSICAL / elementary | Finite prefixes nonuniform; rapidly moving observation words unlicensed |
| FR-03 | Full-support all-word reset fixed points are exactly Bernoulli product digit measures; biased products need not be Haar | PROVED LOCAL elementary cylinder proof | `p0=1/2, others=1/30` is reset-fixed but nonuniform |
| FR-04 | Stoneham `alpha_(16,c)` c=3,5 rational stages traverse the `1 mod c` conductor class exactly `c(c-1)` times per residue | PROVED LOCAL (LTE + congruences), exact recurrence enumeration | Changed c not dividing 16−1; c=2 nonunit |
| FR-05 | True Stoneham orbit vs rational-stage surrogate error ≤`1/[16(c−1)c^p]` on c^p≤n<c^(p+1) | PROVED LOCAL positive tail inequality, exact rational checks | Pulse schedule mutation / wrong c birth |
| FR-06 | All-horizon `A_N(I)≤cN|I|+3c(c−1)floor(log_c(N−1))+c` for c=3,5, all arcs, N>c | PROVED LOCAL paper counting; independent finite tests; recovers classical result | Must cover **partial** final stages and true-orbit error, not only complete stage Fourier |
| FR-07 | Bounded interval occupancy with uniform finite density constant plus radix-shift invariance forces Haar via Riemann–Lebesgue | CLASSICAL / elementary proof | Nonnormal periodic orbit violates uniform bound for small intervals |
| FR-08 | Complete rational conductor-stage Fourier sum exactly zero if `c^(p−1) ∤h`; true-orbit full-stage bound `≤π|h|/8` | PROVED LOCAL, discrete character orthogonality + tail inequality; high precision oracle | Does NOT bound incomplete-stage Fourier sums or automatically imply all N Weyl |
| FR-09 | `alpha_(16,2)` has isolated digits `2^(4ceil(p/4)−p)` at `2^p+ceil(p/4)`; nonzero-digit density zero | PROVED LOCAL digit expansion identity, exact prefix control | The same sparse-series template does not imply normality |
| FR-10 | Repeated hexadecimal de Bruijn order-2 sequence has exact uniform one-step transitions but is nonnormal; computable normal Champernowne admits biasing choice policy | CLASSICAL + local exact controls | One-step reset, computability or chosen subsequences do not certify global uniformity |
| FR-11 | Portable finite-grid occupancy lemma: rational surrogates + uniformly budgeted grid visits and approximation errors imply normality | PROVED LOCAL sufficient lemma, independent of Stoneham grammar | Need actual source-authenticated grid/visit budgets; not automatic from precision |
| FR-12 | Original four-pole BBP selected rational carrier satisfies an accurate phase-approximation leg; an arithmetically certified bounded-occupancy leg is missing | OBSERVED exact source/tail from merged SUCC; OPEN/UNVERIFIED normality bridge | Same-forcing coherent counterseed, source mutants, imperfect rational-stage matching; no π signed saving obtained |

**Independence/coupling:** attaching the same auxiliary positive BBP posterior to two unrelated digit sequences gives identical positive-source observables irrespective of whether one is normal. Any claimed normality transfer requires a genuine source-to-selected-arithmetic coupling. Matching exceptional primes `2,3,5` is a source-passport analogy until such a coupling is derived. This branch changes no frozen source, claim namespace, workflow, or main.

**FR-06b / finite hostile control:** the naive Stoneham `c=3,5` equal-bin stage histograms do not coincide with exact BBP rational-prefix histograms (e.g. `3,p=2` has `(9,7,2)` rather than six each). **REFUTED as a literal finite transfer only**; general selected π normality remains OPEN. Exact Fraction receipt: `NaiveSourceTransferFalsifier` in `test_frame_reset.py`.
