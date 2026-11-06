# Front B — next falsifiable targets

CB-4 splits the open gate into two strictly weaker conjuncts:

\[
\text{normal}\iff\underbrace{(\mathrm{LS})}_{\text{log-scale stationarity}}\ \wedge\ \underbrace{(\mathrm{H2}^*)}_{\text{uniformity at the source lattice}}.
\]

The controls are each known to fail **exactly one** factor:

| Control | (LS) | (H2\*) |
|---|---|---|
| Coherent seed `s_*=−π/16` | holds (constant orbit) | fails (`b≡0`, CB-1c) |
| CB-3 calibrated non-stationary seed | fails | holds (CB-3) |
| Generic point of a non-uniform Bernoulli `β_p` | holds | fails (CB-2) |
| Haar seed (a.e.) | holds | holds |

## Target 1 — the stationarity discriminator (the next falsifiable inequality)

\[
Λ_A=\sup_{1\le a<b\le8,\ b-a\ge1/4}\ \sup_{t}\ \bigl|μ_{[aA,bA)}([0,t))-μ_{[A,2A)}([0,t))\bigr|.
\]

(LS) says `Λ_A\to0`.

**Predictions:**
- Haar seeds and the coherent seed: `Λ_A=O(\sqrt{\log A/A})` and `0` respectively.
- CB-3: `\liminf Λ_A>0`.
- Zero seed: unknown.

**What a result would mean:**
- A proof that `Λ_A\to0` for the zero seed would reduce π normality, by CB-2′, to (H2\*) alone. That is a single-factor uniformity statement at the source lattice.
- A proof of (H2\*) for the zero seed would reduce π normality to (LS).

Either half would be new. Neither is claimed. A finite trend in `Λ_A` is not evidence of either.

## Target 2 — second-order selected statistics and the hierarchy

CB-5 shows that `J2` separates CB-3 from Haar in exact expectation, while first-order `J` cannot.

**Next step:** build the `q=2` analogue of CB-3. That means a slowly-varying Markov (2-block) digit law calibrated so that every pair window `Leb(I_n∩T^{-ℓ}I_{n+ℓ})` is matched.

- If such a model exists: `J2` is also blind, which supports the CB-6 hierarchy conjecture. Every finite-order carry family then needs a stationarity input.
- If it cannot exist: write down the obstruction. It would be the first carry-observable family whose vanishing forces more than first-order calibration.

## Non-targets (refuted or proved insufficient here)

- **"`J→0` for one critical schedule ⟹ normality."** REFUTED by CB-3.
- **"Haar-seed carry moments (#521 CT-05/06) discriminate the zero seed."** Impossible by construction (CB-1e).
- **"Rational seed `1/5` is a nonnormal contrast."** No: it is a rotation. Its `J` differs from the zero seed's only because the window `I_n` is not rotation-invariant.
