# OPERATION TERMINAL WALLS — exact virtual zero-field domain-wall norm

**Anchor:** literal original four-pole BBP source, U₀=0, and one exact rational endpoint U_(2B) per shell. **Target:** a source-derived all-shell lower bound for R0, with periodic-shadow, Γ and CRT controls.

> **One original source. One finite rational endpoint for each shell. A family of backward computational probes. A precise distance from the zero-phase reference. Prove the norm cannot collapse on arbitrarily late shells, and R0 follows.**

**Read first:** [THEOREMS](THEOREMS.md) (mathematics), [NEXT](NEXT.md) (unpaid arithmetic), [VALIDATION](VALIDATION.md) (executed receipts), [SOURCE_MAP](SOURCE_MAP.md) (provenance), [CLAIM_LEDGER](CLAIM_LEDGER.json) (statuses), [exact tests](../../../tests/test_terminal_wall_crucible.py).

## Result and claim status

Existing SUCC [virtual-field form metric, draft PR #657](https://github.com/femboy2112/SUCC/pull/657), proves R0 for x=π/16 **equivalent** to positive liminf of the exact source terminal norm
\[
\mathcal R_B=B^{-1}\sum_{k=1}^B\|U_{2B}/16^k\|_{\mathbb T}^2.
\]

This operation derives exact two-sided *symbolic coercivity* for one terminal rational integer C_(2B). Let D_B count trailing B hexadecimal digits **not equal to 0 or F**, and J_B count direct 0↔F transitions:
\[
\boxed{
\frac{D_B/256+225J_B/65536}{B}\le\mathcal R_B
\le\frac{D_B/4+(D_B+J_B+1)/255}{B}.
}
\]
Consequently, on the authentic original zero-seeded source,
\[
\boxed{\text{R0}\iff\liminf_{B\to\infty}(D_B+J_B)/B>0.}
\]
The *completed* π digit block differs from the rational terminal integer's corresponding block by at most one carry, changing the event budget by at most three. This is an **equivalent target**, not a proof that the positive liminf exists.

## The two strongest hostile receipts

1. **Terminal phase/cofactor clone:** change the low B integer digits to all 0 while retaining the exact terminal fractional phase, reduced denominator, numerator residue modulo that denominator and every prime-cofactor residue. The cloned norm collapses to u²(1−16^(−2B))/(255B). Therefore scalar phase and cofactor alone cannot reconstruct the integer-winding path.
2. **Gamma-matched all-prefix counterfeit:** for **any** integer M, construct strictly positive, decreasing rational forcing with literal zero seed, exact agreement with the first M original signed four-pole forcing values, and the same leading 15/(64n²) asymptotic. Its completed endpoint has radix-16 rational denominator and is eventually exactly locked, with terminal norm O(B^(−5)). Thus no proof using only a finite source prefix, generic positivity, monotonicity and the first Γ asymptotic term can establish R0.

Both are deliberately **different from the complete authentic source**. The surviving proof pathway must use the infinite exact four-pole source law and its signed chronology, not just its generic shape.

## Where the ice-climb stopped

**OPEN:** a zero-seed, full-four-pole arithmetic proof that D_B+J_B stays at positive density on **every** sufficiently late shell; R0; and all-mode π normality. Irrationality, finite rational shadow agreement, source-blind Gamma smoothing, finite odd CRT congruences and a single fresh terminal prime do **not** pay that obligation.

The focused test module exhausts all 4,096 three-digit words against three fractional controls (12,288 exact inequality checks), plus original source and hostile source variants. **13/13 focused tests PASS locally**; full repository integration gates were not run in this round. See the validation file for exact hashes and proof scope.

**Repository discipline:** standalone additive research-only draft against pinned Main XXVI, while previous #657 remains a separate draft. No frozen provenance, original sources, historical files, workflows, main, release or tag changes.
