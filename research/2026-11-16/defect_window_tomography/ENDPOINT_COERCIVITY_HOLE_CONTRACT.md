# Endpoint coercivity: live hole contract

**Research round:** 2026-11-16 (America/New_York). **Starting head:**
`1f04b869182ad68deb764637034d72b19352ca48`, draft PR #657.
**Canonical main:** `81be6b897ae980b801a3b9de9e22ef81e8360bfb` (Main XXVI).

## Source and exact target

Keep the literal zero seed and original four poles:

\[
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},
\qquad U_0=0,\qquad U_n=16U_{n-1}+r(n).
\]

For every integer B >= 1, let

\[
R_B=\frac1B\sum_{k=1}^B\|U_{2B}/16^k\|_{\mathbb T}^2.
\]

**OPEN target:** there exist delta > 0 and an integer B0 such that R_B >= delta
for every integer B >= B0. The existing VFM sandwich makes this equivalent to
R0: an eventual positive lower bound on
`1 - Re (B^(-1) sum_{n=B}^{2B-1} exp(2 pi i 16^n pi/16))`.
The equivalence is a reformulation, not a proved statistical saving.

## Dependency cut and novelty tax

Authenticated source -> exact terminal rational form -> quantitative shadow
comparison -> **missing arithmetic coercivity** -> R0 -> further still-open
signed rungs -> all-mode Weyl cancellation -> base-16 normality.

The weakest sufficient obligation in this round is the target itself. A useful
intermediate result must additionally exclude a class of low-energy source
histories, give a new source-derived estimate, or prove a sharp limitation of an
attempted inference. Renaming R_B, assuming a digit density, or decoding its
phase through Gamma does not close the missing edge.

## Live obstruction and controls

- Irrationality and perpetual nonstationarity allow arbitrarily cold shells.
- A changed seed -pi/16 retains the forcing but cancels the completed orbit.
- Rational seed shifts can alias late observations while failing authentication.
- Unrestricted positive/Gamma/Hilbert energy need not bound the selected orbit.
- Original finite data B = 16,32,64,128,256 have already been used. Fresh integer
  shells, including nonpowers of two and endpoints beyond 256, are holdouts.
- Global irrationality measures and odd-denominator inventories require explicit
  real-circle transfer; neither may be substituted for that transfer.

## Preregistered probes and proof languages

1. **Construction:** exploit nearest-integer backward branches, exact carries,
   pole residues and selected numerator/cofactor constraints. Pass: a proved
   quantitative statement not using the desired density as a premise. Fail:
   a valid source-class counterexample or a circular use of R0. Ambiguous:
   finite improvements without an all-shell lift.
2. **Adversary:** audit VFM constants and quantifiers; attack any proposed
   denominator-only, irrationality-only, generic-force or energy-only argument.
   Preserve counterexamples and distinguish them from the authentic zero seed.
3. **Translation:** compare with the existing restricted-exponent, signed carry,
   finite recurrence and Diophantine results; check primary sources before any
   imported theorem becomes load-bearing.

Exact rational computations are finite certificates only. Parent verification
of delegated claims, calibrated mutation/negative controls, explicit error
budgets and the repository's mandatory gates are required before publication.

## Completion criterion

Publish audited proofs, finite witnesses, failed routes and an updated next
dependency cut on the existing draft branch. Do not promote R0 or normality
unless every infinite quantifier has been proved. The next lamp, if this remains
open, must name the arithmetic property missing from the surviving probe.

## Final state of this round

The target remains OPEN. The round proved the fixed-aspect cold-set dimension
1/lambda, a finite sparse-form cover, the precise coherent tail baseline, and
near-zero dyadic winding erasure. The inherited endpoint bridge survived audit.
The preregistered finite claim A_B>2/5 passed for every 16<=B<=4096; its
executed exact minimum exceeds 1/2. This is finite evidence only.

A strictly weaker next arithmetic contract is the eventual pointwise bound
R_B>=1/(16711680 B^5). If proved for the literal zero seed, the established
subleading tail comparison forces E_B>1/(679173120 B^7), hence v_16(pi)<=1.
The square-marker changed-seed control satisfies this intermediate while
failing R0, so it is not an equivalent reformulation. Its original-source
premise is unproved. See ENDPOINT_COERCIVITY_REPORT.md for the proof products,
failed routes, dominance boundary, complete ledger and execution handoff.
