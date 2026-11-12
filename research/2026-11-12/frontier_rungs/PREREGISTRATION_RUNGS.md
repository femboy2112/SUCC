# Preregistration — frontier rungs round (2026-11-12)

Written and committed before any code of this round reads π data on the shells named below.
Parent: `8de33430fb35dc0360dacff92c4ee1e4364ad458` (draft PR #599 head), itself a descendant of
Main XXIV `071ce1e0ee6ab8f8c07113e901131aa646d6b95d`.

**π base-16 normality, the source-selected signed estimate and (CH) are OPEN and stay OPEN
whatever the outcome of anything below.** Finite numerics are instance checks of proved
inequalities or observations; none is evidence for an asymptotic claim.

## Frozen source

`r(n) = 4/(8n-7) - 2/(8n-4) - 1/(8n-3) - 1/(8n-2)`, `U_0 = 0`, `U_n = 16 U_(n-1) + r(n)`,
`C_n = floor(U_n)`, `κ_n = C_n - 16 C_(n-1)`, completed point `x = π/16`, `y_n = {16^n x}`.

## Shells

- Calibration (may be used while debugging): `B ∈ {64, 128}`.
- Fresh holdout (first computed by the full run of this round's probe): `B ∈ {331, 577, 947, 1291}`.
  None of these was used in the IAD or ZSC rounds (their shells were `{64,128}`, `{97,…}` of IAD and
  `{243, 420, 811, 1210}` of ZSC).
- Shell measure: `ν_B = B^(-1) Σ_(n=B)^(2B-1) δ_(y_n)` on `[0,1)`, interval cost `|u-v|`.

## Quantities

- `W1(ν_B) = ∫_0^1 |F_(ν_B)(t) - t| dt` (interval Wasserstein distance to Lebesgue).
- `D(ν_B) = ∫_0^1 |F_(ν_B)(t) - F_(Qν_B)(t)| dt` with the sixteen-child operator `Q = C T_*` of
  `docs/PI_NORMALITY_FRONTIER.md` §5 (Main XXIV).
- change density `c_B = B^(-1) #{n ∈ [B,2B) : d_n ≠ d_(n+1)}` (ZSC-02).

## Predictions (stated before computation)

Provisional thresholds, derived on paper before any code and still to be proved and audited in
this round: `w* = 4/225` for `W1`, `θ* = 1/60` for `D`.

- RP-1. On every holdout shell `W1(ν_B) < 0.009` (about half of the provisional `w*`).
- RP-2. On every holdout shell `D(ν_B) < 0.008` (about half of the provisional `θ*`).
- RP-3. On every holdout shell `0.90 < c_B < 0.97`.
- RP-4. Every inequality of this round's theorem files that is stated for all real points holds on
  every tested instance (theorem-grade checks; a failure refutes the statement, not the data).

A miss of RP-1…3 is recorded as a miss. Thresholds are not changed after the run. If the proved
thresholds differ from the provisional ones, both are reported.

## Mutation controls (must be rejected by the checks)

- RM-1. A point whose digits on the shell are constant must give `W1 ≥ 4/225` and `c_B = 0`.
- RM-2. Replacing `Q` by the identity must give `D = 0` identically (so a `D`-based check that
  still passes is vacuous and must be flagged).
- RM-3. A measure equal to Lebesgue restricted to a 256-adic grid of step `1/256` must give
  `W1 ≤ 1/512`.

## Not preregistered

Exact symbolic computations with no π shell data (linear programs over measures on the fifteen
fixed points, 2-adic valuations of coefficients of Padé-type linear forms, continued-fraction
identities) are exploratory algebra and are reported as such.
