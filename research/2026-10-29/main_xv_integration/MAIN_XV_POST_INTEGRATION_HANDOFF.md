# Operation Main XV — post-integration research handoff (Triangle Genesis frontier)

**Date:** 2026-10-29. With Main XV the **operational triangle** (`docs/OPERATIONAL_TRIANGLE.md`)
is SUCC's primary research apparatus. The author's Harmonic / Golden-ratio / Euler–Mascheroni
triangle and Oily–Macaroni are preserved as its rank-two specialization. **π base-16/base-3
normality and RH remain OPEN**; nothing below changes that.

## The one target that would actually change the verdict

Derive an authentic **source-specific, zero-seed-sensitive signed intertime estimate** for

```
S_N(h) = (1/N) Σ_{n≤N} e(h · U_n(0)),   h ≠ 0,   e(x)=exp(2πix),
```

on the genuine BBP orbit `U_0 = 0`, `U_n = 16 U_{n-1} + r(n)`, with all four original signed poles
`R(a)=4/a−2/(a+3)−1/(a+4)−1/(a+5)`. "New" means a bona-fide asymptotic **signed inequality** that
does **not** follow by (i) applying an invertible positive filter, (ii) scalar `O(log N / N)`
reweighting, (iii) source-only phasors, or (iv) restating the Weyl criterion. The full Weyl gate
`∀ h≠0: S_N(h) = o(N)` **is** base-16 normality of π — so a decisive proof is OPEN by definition;
the realistic near-term goal is a strictly-better-than-trivial bound on a declared sub-band that
provably distinguishes the authentic seed from a coherent counterfeit.

## Why the easy routes are already closed (do not re-walk)

- **Seed-smearing is a universal zero (TG-06/08).** `∫_0^1 H(u;s) du = 0` for **every** seed `s`,
  including the coherent same-forcing `s* = −π/16` whose selected-phase mean → 1 while its orbit is
  nonnormal. The seed-displacement tomography recovers each `q_j e(h U_{n+j}(s))` exactly — that is
  observability, not cancellation.
- **The 59-jet discriminates the source, not the signed sum (TG-05).** `J_BBP − J_fake =
  59(1+t−z)/[120 d^3]` is a joint source/grade readout; it says nothing about `|S_N(h)|`.
- **Normality-equivalent observers only restate the problem (TG-10, #375/#382).** Fourier/entropy
  "normality-complete" observers give equivalences; `#376` signed nonzero limsup is a **seed
  discriminator**, not an all-N Weyl saving; `#384` shrinking-target sparsity and moving-grade
  bandwidth are resolution costs, not bulk mixing.
- **The transcendence→entropy bridge is refuted (#337).** Do not revive "π transcendental ⟹
  positive topological entropy ⟹ Haar": the Kempner number kills the general implication.

## Design of the next discriminating probe

Use the operational triangle's **joint** field/grade transform to choose observers, then test a
candidate signed estimate against a full control slate. A candidate passes only if it is
**positive on the authentic seed and fails on every counterfeit below**.

| Control | Must the candidate estimate hold? | Why |
| --- | --- | --- |
| Genuine zero seed `s=0`, four signed poles | **YES** (the claim) | the authentic orbit |
| Coherent same-forcing `s*=−π/16` (mean→1, nonnormal) | **NO** | the sharpest trap: same forcing, wrong seed |
| Gamma-matched fake `Q_fake=15x` (`15×` source) | **NO** | matches limiting `F`, differs at the jet |
| Cubic-jet-matched positive extra-pole `Q_ε=Q+ε(1−e^{−x})^3` | **NO** | matches the first jet; needs higher jets/poles |
| Wrong / sign-flipped pole set | **NO** | breaks the authentic signed structure |
| i.i.d.-reset sensor (posterior reset each trial) | **NO** | destroys `Var_{μ_a}(f)` covariance |
| Parity / totient-collapsed grade | **NO** | premature projection loses source info |
| Truncated fixed-grade observer (no moving grade) | **NO** | ignores Kepler III resolution |
| Independent two-geometric Oily packet (#368) | **NO** | same marginal, different latent coupling |
| de Bruijn / Kempner nonnormal digit control | **NO** | nonnormal holdouts |
| Rational changed seeds | **NO** | eventually periodic orbits |

Report predicted **yes / no / ambiguous** per control **before** running, with seeds, precision,
and exact outputs (the Instrument rule: calibrate the measuring code on known values first).
Validate on a **fresh** source family / seed holdout, not the fitted finite-`n` prefixes.

## Ingredients the apparatus now provides

- `research/2026-10-29/operational_triangle_frontier/` — `operational_triangle.py` (exact Fraction),
  `independent_oracle.py` (SymPy/mpmath), `THEOREMS.md` (TG-01–TG-07), `CLAIMS.md` (TG-01–TG-10).
- `research/2026-10-29/finite_field_superposition_triangle/` — parent #386 finite triangle and its
  independent first-jet oracle.
- Kepler III moving-grade / shrinking-target resolution (`#384`, `research/2026-10-29/…kepler…`).
- Complete 16-state unit + Walsh chart and the 255↔256 adversary (`#385`,
  `research/2026-10-29/…minimal pole…`); do not infer the whole alphabet from the mod15↔mod16 unit
  isomorphism.
- Literal carry `κ_n(s) = 16{U_{n-1}(s)} + r(n) − {U_n(s)} ∈ ℤ`, composition
  `κ_n^{(2)} = 16 κ_n + κ_{n+1}`: keep as integer-lift marks; do not exponentiate or parity-reduce
  before attaching them.

## Hard rules

Preserve every counterexample and failed proof obligation. Keep source-characterization strictly
separate from selected signed cancellation. Do not promote a positive source relation, Gamma
transform, entropy formula, phase rotation, or invertible filter into the missing cancellation
theorem. An equivalent restatement of Weyl is not an improvement. π base-16/base-3 normality and
RH remain **OPEN**; SUCC is a Σ₁ verifier, not a Π₂ prover.
