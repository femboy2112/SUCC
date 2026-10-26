# Signed pushforward / Skeleton-Key Main XII obstruction supplement

Round **Skeleton Key (Main XII)**, staged on `research/pi-signed-pushforward-obstruction-2026-10-26`
(branched from `origin/main` `6dd80730c3575d91f746546a25da5aedbd2e2737`, Main XI / PR #305).
**pi base-16 normality: OPEN. Logical independence: OPEN. RH: OPEN (separate program).**
No zero lookup, no physical-source claim, no academic-priority or Lean result. The authentic
source `r(n)=4/(8n-7)-2/(8n-4)-1/(8n-3)-1/(8n-2)`, `U_0=0`, `U_{n+1}=16U_n+r(n+1)` is byte-unchanged.

This supplement records a **convergent negative result**: eight independent research fronts plus
the categorical apparatus located the *same* wall from different directions, and every load-bearing
claim survived adversarial verification (each adversary rebuilt the orbit from scratch and
reproduced the receipts; every OVERCLAIM was trimmed to the corrected statement carried below).
**No cancellation, signed saving, or sub-frontier bound was established anywhere; the DC-1 modulus
frontier `N - O(log N)` is unchanged.** The round's value is a sharper obstruction map, one new
(classical) firewall product, and tested source-faithful instruments.

This doc mints **no** new claim-namespace prefix (per `docs/CATEGORICAL_OBSERVER_ATLAS.md`
collision discipline). Labels `SK2-*` below are **doc-local** finding tags, not registry claim IDs;
each cross-references the existing registered claims it bounds or sharpens. Authoritative gate:
`tests/test_claim_namespace_collisions`.

## The gate, restated (proved reductions, not re-derived here)

- **#293 / SGO-09 (proved).** `|sum_{n<=N} e(h 16^{n-1} pi) - sum_{n<=N} e(hU_n)| < (119/648)|h|`, so
  pi is base-16 normal **iff** `Shat_N(h)=sum_{n<=N} e(hU_n)=o(N)` for every fixed `h != 0`.
- **DC-1 / #304 (paper-proved).** `|sum_{n<=N} e(hU_n)| <= N - (1/1250) max(0, floor(log_8 N) - max(J_0, ceil(log_64 |h|)))`.
  A **modulus** bound; normalized it tends to 1; **not** `o(N)`; `J_0` not numerically effective.

## Findings (all exact over Q[Q/Z] unless marked OBSERVED)

| Tag | Statement | Status | Boundary |
|---|---|---|---|
| SK2-A1 | **(accumulation barrier, M3 anchor)** For every fixed `c in (0,1)` and every positive-density set of geometric width-8 blocks, `|S_B(h)| <= (1-c)|B|` for all `B` implies, by the triangle inequality alone, only `|S_N(h)| <= (1-c')N` (linear, never `o(N)`); and the extremal-consistent configuration feeds the section-2 gate as `R^2_{N,H} = (1-c)^2 (H-1) = Theta(H)`, which diverges. So **any fixed positive-proportion relative block loss is insufficient** for normality; sufficiency needs `c = c_N -> 1`. | **PROVED** (elementary structural no-go) | pi normality OPEN; sharpens the target, does not reach it. Bounds **PSF-14**, the stated moderate-coherence route. |
| SK2-A2 | **(coherence-width ceiling)** The single-step x16 inverse lemma (**DC-5**) certifies a block loss only while `34a + |h| range(r) < 1` (i.e. `a < 1/34`, constant `34 = 2(1+16)`), giving an **absolute** loss `<= 8a^2 < 2/289`, length-independent. For `a >= 1/32` the x16 image of a width-`2a` arc covers the circle, so the integer-collapse is non-unique and the lemma yields nothing. Escape requires the **joint** phase across `>= 2` consecutive x16 steps. | **PROVED** (geometric obstruction) | the wrap at `32a >= 1` is a hard geometric fact, not DC-5-specific. Confirmed by **Front H FACT 1** below. |
| SK2-B | **(signed pushforward: gate-conservative, positivity-blind)** With `K_{a,b}=z_a conj(z_b)`, `z_n=e(hU_n)`, the identity `|S_N(h)|^2 = sum_A |S_A|^2 + sum_{A != B} S_A conj(S_B)` is a **partition-coarsening invariant**: refinement only moves mass between the within-cell diagonal and the signed cross term. The authentic cross term is **sign-indefinite** across `h=1..5` (OBSERVED), so carries no provable negative bias. **Corrected positivity statement:** positive within-cell/ANOVA/PSD data does **not** determine `|S_N(h)|^2` and cannot bound it below the sharp trivial `(sum_A |S_A|)^2`; it yields **no saving**. | **PROVED** (no-go) | A saving must come from a source-derived within-cell coherent-energy bound, which is not supplied. `observational_succ/signed_pushforward.py`. |
| SK2-C | **(CRT occupancy phase-blind)** The occupancy observable class `O` (hit-classes, combined-sieve survivors, conductor tower `Q_n`, birth pattern) is seed-blind and exactly CRT-multiplicative (joint `{3,5,7}` density `64/225 = 8/9 * 14/25 * 4/7`). A coherent-seed twin shares the entire `O`-fingerprint yet is `>= (1-eps)N` coherent, so any upper bound on `|S_N(h)|` that is a function only of `O` is `>= (1-eps)N`, never `o(N)`. The only live seed-dependent phase datum is the integer carry `c_t`. | **PROVED** (obstruction) | all-N reach rests on an uncertified seed-radius bound; the sound coherence bound is `1 - 20 h^2 radius^2` (not the receipt's `2pi < 315/100`, which is false). Bounds any pure CRT/prime-clock route. |
| SK2-D | **(signed base change iff cartesian — the one new categorical product)** On finite carriers with exact `Q[Q/Z]` amplitudes, amplitude base change `g^*(q_! z) = q'_!(g'^* z)` holds for **every** `z` **iff** the square is cartesian (classical finite-set / Mackey base change). Realization/ghost-faithfulness is **necessary but not sufficient**: the redundant-realizer square passes the ghost firewall **and** Prop-base-change-for-all yet breaks signed transport (defect `-e(1/3)`). The correct signed firewall is `is_cartesian`, not `realization_firewall_breaks`. The Prop/ghost report is amplitude-independent (signed-blind: energies 48 vs 0). | **PROVED LOCAL / CLASSICAL** + firewall sharpening (keeper) | **WITHDRAWN:** "pushforward low-frequency energy IS the section-2 gate" is false — the computed `coefficient(0) = (H-1)/N` is the phase-blind occupancy baseline (identical for the authentic orbit and the non-normal counterfeit `xi = sum 16^{-2^k}`), not the complex Weyl gate. See SK2-TRAP. |
| SK2-TRAP | **(occupancy-baseline trap)** `occupancy_baseline(states,H,h) = (purity.coefficient(0) - H)/H = (H-1)/N` **exactly** and is phase-**blind**: identical for authentic, changed-seed, and changed-forcing orbits (verified `(8,3,1),(20,4,1),(40,5,3)`). The real section-2 statistic is the **evaluated** `2 sum_{d<H}(1-d/H)|(1/N) sum_n e(dhU_n)|^2`: OBSERVED authentic `0.154/0.203/0.151` vs counterfeits `~H-1` at the same points. | **PROVED** (exact) + OBSERVED separation | exposed only to certify the distinction; `occupancy_baseline_is_the_gate = False`. |
| SK2-E | **(path coherence adds rank 0)** Among **forcing-universal** source-labelled structural relations (coefficients independent of the numeric `U_n, r_n`), path coherence — k-step macros, the telescope syzygy, opposite-directed odd-torsion backward steps, the circulation of the selected-phase node-potential around any labelled null 1-cycle — adds rank 0 (`= span(E_1..E_N)`); adjoining the anchor `U_0=0` adds exactly one structural dimension. | **PROVED** (no-go), transport_to_gate = NONE | **Corrected:** the full `ev_authentic=0` module is strictly larger (contains value-coincidence tautologies), so "rank exactly N+1 / unique rank-adder" is restricted to the forcing-universal class. The non-gradient carry cochain (holonomy `-2`, NOT-transportable) is the only open micro-direction. |
| SK2-F | **(0,1,inf / cross-ratio / elliptic degree-16 coincidence trap)** Every observable the four-point / moduli / elliptic geometry offers either (i) **is** the target and its conjugate (the only two charts regular on `R/Z`), or (ii) is singular at the punctures `{0,1}` the orbit provably visits (`min{U_n}=1.99e-3` at `n=48`), or (iii) is the phase-blind `S_3`-invariant Legendre-j (`j(2/15)=504358336/38025 != 2048`), or (iv) a cardinality-16 coincidence refuted by `C_16 != C_4 x C_4 != (C_2)^4` and `z^16` (Julia=circle) `!=` Lattes (Julia=sphere). No time-independent intertwiner exists (dense forcing-difference subgroup). | **PROVED** (no-go), build_spec NONE | the nonexistence **is** the result; transport_to_gate = NONE. Both adversary axes survived. |
| SK2-G | **(unimodular transfer kernel; odd/even top-bit split)** The gate equals `2 sum_{h<H}(1-h/H)|A_N(h)|^2` with `A_N(h) = <flat-carry word-measure, kappa_h>` and `kappa_h` **unimodular**, so any **first-moment** modulus/triangle bound is the trivial `|A_N(h)| <= 1`. The order-4 Walsh component `ghat_h(15) = prod_{i<4}(1 - zeta^{h 2^i})` is **zero iff `h` even** (exact, `h=0..40`): odd-`h` gate modes couple to the marginal-invisible order-4 carry interaction; even-`h` modes are order-`<=3` marginal-reachable. | **PROVED** (scoped no-go) + exact decomposition | **Corrected scope:** kills only the phase-blind, bounded-order **occupation-count** route; positivity / `L^2` / van der Corput (second-moment) methods remain live. "Irreducibly signed" is struck. |
| SK2-H | **(literature: no classical theorem beats the frontier)** Across Weyl, Bailey-Crandall Hypothesis A, Erdos-Turan/Koksma/LeVeque, van der Corput, Gowers/GTZ, Furstenberg x2x3, Weil-Deligne `F_p`, and Diophantine + Zeilberger-Zudilin `mu(pi)<15/2`, **no** theorem has source-satisfiable hypotheses (without assuming normality) yielding a signed `o(N)` saving stronger than `N - O(log N)`. **FACT 1** (exact to `1e-896`): van der Corput lag-`k` autocorrelation `=` the Weyl sum at frequency `h -> h(16^k-1)` — **no degree drop**, differencing never leaves the x16 family (the analytic mechanism behind SK2-A2). | **PROVED** (obstruction map) | the one independent lever (Weil/Deligne `F_p`, Route A/B) has **unverified** real-circle transport; its naive relative-trace transport is **REFUTED** (**OSP-12**, keep as mandatory negative control). |

## Did category theory earn its place?

**Yes, but only negatively.** It discovered no construction and produced no signed saving. Its one
earned product is the **sharpened firewall** (SK2-D): the correct signed-transport condition is
`is_cartesian`; ghost/realization-faithfulness is necessary but not sufficient. Everything else was
reorganization (the pushforward is an exact coarsening-invariant base change that moves energy
faithfully without creating cancellation, and is amplitude-blind) or obstruction (SK2-F, the
multiplier-16 non-jet). It correctly handed the problem **back to the arithmetic gate**.

## Effect on the PI Frontier Contract

The frontier did **not** move; every route remains OPEN and the DC-1/DC-5 ceiling is re-confirmed.
What changed: (1) the moderate-coherence target is **sharpened** — it must deliver relative loss
`c_N -> 1` (SK2-A1), not a fixed positive-proportion relative loss; (2) the atlas `K->PKP*`
obligation is **discharged as a negative theorem** with the `is_cartesian` sharpening (SK2-D);
(3) routes closed as dead for a *saving*: four-point/elliptic geometry (SK2-F), occupancy/CRT
independence (SK2-C), path-coherence/null-boundary (SK2-E), categorical universal-property
(SK2-D), bounded-order occupation-count tomography (SK2-G, first-moment); van der Corput confirmed
circular (SK2-H FACT 1). The only **live but unproven** transfer mechanisms remain: the
multiplicative x16 frequency-ladder contraction, signed `L^2` cross-block cancellation, and the
Weil/Deligne `F_p` real-circle transport (OSP-12 as negative control).

## Single next discriminating probe

Prove the **even-`h` sub-band** fragment — the one genuinely weaker, marginal-reachable target the
round exposed: `2 sum_{h even, h<H_N}(1-h/H_N)|A_N(h)|^2 = o(1)` using only the `<=3`-order
Walsh/Lucas marginals of the flat-carry word (legitimate there because `ghat_h(15)=0` for even `h`).
A proof isolates the odd-`h` order-4 signed band as the sole irreducible obstruction and routes the
rest to the x16 ladder contraction test: whether `limsup_h |A_N(16h)|/|A_N(h)| < 1` for the
authentic orbit while **failing** on the counterfeits that must be excluded (SS-08, positive-carry
#304, `xi`), driven by the `15/64` four-pole resonance — not by `U_0=0` or the carries, which the
controls share. Falsification routes to signed `L^2` cross-block cancellation or the Weil/Deligne
`F_p` transport. See `handoffs/SKELETON_KEY_MAIN_XII_NEXT_2026-10-26.md`.

## Instruments committed this round

- `observational_succ/signed_pushforward.py` + `tests/test_signed_pushforward.py` (9 tests): the
  unified signed `K->PKP*` adapter as a negative theorem + the `is_cartesian` firewall, with the
  four negative controls (ghost / redundant-realizer / signed-blindness / positive-Gram rotation),
  the coarsening-conservation identity, and the occupancy-baseline trap. Grep-able hard flags
  `signed_saving_proved = pi_normality_proved = occupancy_baseline_is_the_gate = introduces_new_theorem = False`.
