# Operation Main XVI — post-integration handoff (Triangle Genesis, next round)

**Date:** 2026-10-29. Main XVI repaired three Main XV inconsistencies and added one obstruction, all
on `main`. **π base-16/base-3 normality and RH remain OPEN.** The next round continues in ChatGPT;
this file is the durable, reproducible state.

## What is now settled (do not re-litigate)

- **Weyl normalization (P0).** The gate is `T_N(h) = Σ_{n≤N} e(hU_n(0)) = o(N)`, equivalently the
  normalized `Sbar_N(h) = T_N(h)/N = o(1)`, `h ≠ 0`. The normalized `Sbar_N = o(N)` is vacuous
  (`|Sbar_N| ≤ 1`). Repo's historical `S_N` = unnormalized `T_N`; its `o(N)` entries are correct.
  (`WEYL_NORMALIZATION_CONVENTION.md`.)
- **Golden locus (P1 / TG-11, PROVED).** `q_{r,θ} = λ^r ⇔ θ = λ/(1−λ^r)`, `r>0`, supercritical;
  calibration `(1,φ,λ),(2,1,λ²),(3,φ/2,λ³)`; constant Laplace rate `θ(1−q)=λ`; restricted
  uniqueness `θ=1 ⇒ r=2`. The BBP point `(2,1)` is the unique intersection of its authentic clock
  `{θ=1}` with the locus; it is **not** the only coincidence of `λ^r` with `q_{r,θ}`.
  (`GOLDEN_LOCUS_THEOREM.md`.)
- **Seed-alias dichotomy (P2 / TG-12, PROVED).** `U_n(s) = U_n(0) + 16^n s`. Seven classes;
  magnitude `|T_N(h)|` is blind to exact aliases `s∈(1/16)ℤ`, eventual aliases `s∈ℤ[1/16]`, and
  constant twists `q|15`; it separates periodic twists `q∤15`. Corrected control slate demands
  failure only on seeds the readout can separate (`s*=−π/16`, periodic twists, source mutants).
  (`SEED_ALIAS_CLASSIFICATION.md`.)
- **Carry obstruction (P3 / TG-13, PROVED negative).** The literal carry `κ_n(s)` distinguishes
  circle-aliased seeds but gives no bound on `|T_N(h)|`; no noncentral/carry enrichment is at once a
  magnitude bound and an alias separator.

## The one target that still moves the verdict (unchanged, sharper framing)

A source-authenticated, zero-seed-sensitive **signed** estimate improving the trivial
`|Sbar_N(h)| ≤ 1` on a declared growing sub-band `H_N → ∞`, `H_N = o(N)`, for the authentic orbit
`U_0 = 0` with the four signed poles — a bona-fide asymptotic signed inequality that is **not**
(i) an invertible positive filter, (ii) scalar `O(log N/N)` reweighting, (iii) source-only phasors,
or (iv) a restatement of Weyl. By SK2-A1 a uniform relative block bound `(1−c)` is insufficient
unless `H_N(1−c_N)² → 0`; merely `c_N → 1` fails. The estimate must pass the **corrected** slate:

| Must FAIL on | Reason |
|---|---|
| coherent counterseed `s* = −π/16` | nonnormal, same forcing (class 7) |
| periodic twist `q∤15` (e.g. `1/7`) | magnitude-separable eventually-periodic orbit |
| `Q_fake=15x`, cubic-jet mutant `Q+ε(1−e^{−x})³`, wrong/sign-flipped poles | source-structure mutants |
| parity/totient projection, i.i.d.-reset sensor | premature projection / lost covariance |
| Kempner / de Bruijn nonnormal digit controls; independent source holdout | nonnormal / overfit guards |

| Must NOT be required to fail on | Reason |
|---|---|
| exact/eventual circle alias `s∈ℤ[1/16]` | circle-identical to authentic for `n≥N₀` |
| constant twist `q|15` (e.g. `1/3, 2/5`) | `|T_N(h)|` exactly seed-invariant |

Report predicted yes/no/ambiguous per control **before** running (Instrument rule), with seeds,
precision, exact outputs; validate on a fresh holdout, not the fitted finite-`n` prefixes.

## Promising but unproven directions

- **Growing-band on the golden locus.** The locus gives a rate-locked (`λ`) one-parameter family of
  declared observers. Whether a *moving-rank* observer along the locus yields a sub-band coherence
  bound with `H_N(1−c_N)²→0` for the authentic clock `(2,1)` is open; must survive SK2-A1.
- **Carry-resolved noncentral statistic.** TG-13 forbids a pure carry/absolute-phase separator from
  being a magnitude bound. Any proposal must state, up front, how it evades being (a) invertible,
  (b) source-only, or (c) a constant-twist-invariant functional — else it is already refuted.
- **Four-bit Walsh × q=3/q=6 orientation.** Still a candidate source-coupling basis; equal endpoint
  marginals ≠ equal latent couplings (#368 vs #370 vs Gamma–Poisson), so any saving must come from a
  source-derived within-cell coherent-energy bound (SK2-B), which remains unsupplied.

## Hard rules (unchanged)

Preserve the four signed poles, `U_0 = 0`, the frozen BBP sources, Lean proof contracts, and all
historical claim statuses and counterexamples. Keep source characterization strictly separate from
selected signed cancellation. An equivalent restatement of Weyl is not an improvement. SUCC is a
Σ₁ verifier, not a Π₂ prover. **π base-16/base-3 normality and RH remain OPEN.**

**Primary principle:** the goal is not more equivalent descriptions of π's digits, but a
source-authenticated, selected-history-sensitive constraint that actually improves the signed
cancellation problem.
