# Preregistration — zero-selected carry continuation (ZSC)

Written and committed **before** `probe_zsc.py`, `test_zsc.py` or any holdout computation for the
ZSC statements existed. Exact symbolic checks of ZSC-06 (rank 7, null vector, the partial-fraction
identity) and the proofs in [CARRY_FLUX](CARRY_FLUX.md) were done first; they involve no π data.
Thresholds below are fixed here and are **not** to be re-tuned after the run; a missed prediction
is reported as a miss.

## Data split

- **Calibration shells** (free to inspect while writing the probe): `B ∈ {64, 128}`.
- **Fresh holdout shells** (first touched by the final probe run; disjoint from the earlier
  holdout `{200, 360, 729, 1000}`): `B ∈ {243, 420, 811, 1210}`.
- Modes `h ∈ {1, 3, 15, 17}`. Source horizon `n ≤ 2600` for the zero seed.
- Pseudo-random controls use `random.Random(2026111102)`.
- Two routes to the digits: (i) integer arithmetic on an mpmath enclosure of π
  (`iad_core.CompletedOrbit`), (ii) the literal carries of exact rationals `U_n` through the
  cocycle `d_n = κ_(n+1) + ε_(n+1) - 16ε_n`. They must agree on the whole horizon.

## Theorem-grade checks (any failure is a defect in a proof or in the code; exit non-zero)

| ID | Statement tested | Inputs |
|---|---|---|
| ZC-1 | Stretch lemma (1.1) for every admissible `(m, N)` on a grid | π on all six shells; `K = Σ16^(-2^k)`; `ξ_λ`, `λ ∈ {1/4, 1/2, 3/4}`; 40 synthetic near-dyadic points |
| ZC-2 | Theorem (1.2) on synthetic points whose saving and `‖16^m ξ‖` are both computable (`ξ_λ`, random digit strings) | shells `B ≤ 2048` |
| ZC-3 | Locality lemma 1–2 of ZSC-02 at every position | π, `n ≤ 2600`; W1–W3; `1/17`, `7/15`; 2 random strings of length 5000 |
| ZC-4 | ZSC-02 (a), (b) for `k ∈ {2,3,4}`, (c) on every shell | same strings; all six shells for π |
| ZC-5 | Renewal lemma and Corollary 1 of ZSC-03 | zero seed `n ≤ 2600`; coherent seed; 6 forced-seam rational seeds; hostile source `g_H`; null source |
| ZC-6 | Corollary 2 of ZSC-03: `|c^κ_B - c_B|` bound, and the case table for `(ε_n, ε_(n+1), ε_(n+2))` | zero seed; forced-seam seeds |
| ZC-7 | ZSC-04: runs `≤ 41n`; look-ahead `⌊16^(n-1)π⌋ = ⌊C_(42n-41)/16^(41(n-1))⌋` for `2 ≤ n ≤ 40` (π from route (i)) | zero seed |
| ZC-8 | ZSC-05: stated properties of W1–W3 on prefixes of length 20000 (inequalities proved in the file, with their explicit constants) | — |
| ZC-9 | ZSC-06: gauge identity `U'_n = U_n + a(n)` exactly for three `h`; proper reduction; `baker_rank = 7`, kernel `= Q·A_0`; partial-fraction identity; `0 < U^0_n < 1/(8n+1)`; `U^H_n = 2·16^n - T^H_n` with `0 < T^H_n < 1`, carries 15, `ε ≡ 1`; `g_H > 0` on a rational grid of `[0,1)`; `U^ρ_n - U_n = ρU^0_n` | `n ≤ 400` |
| ZC-10 | Repaired IAD-04 progression corollary on occupied cells; the retired display is violated at `(B, ℓ, h, q) = (100, 1, 1, 1000)` | cells with `q ≤ B-ℓ`, `B ∈ {64, 128, 243}` |
| ZC-11 | Transport `|D_(B,h) - W_B(h)| ≤ (π/32)|h|B^(-2)` between route (ii) and route (i) | all six shells, four modes |

## Predictions (empirical; a miss is a finding, not a defect)

| ID | Prediction for the zero seed on the four holdout shells | Basis |
|---|---|---|
| ZP-1 | `|c_B - 15/16| ≤ 4·sqrt(15/(256B))` | changes of i.i.d. uniform digits are uncorrelated Bernoulli(15/16) |
| ZP-2 | `|W_B(h)| ≤ 4/√B` for `h ∈ {1, 3, 15, 17}` | random-phase scale `1/√B` |
| ZP-3 | no letter 16 and no seam (`ε_n = 0`) for `n ≤ 2600`; hence `c^κ_B = c_B` exactly on every shell | SEAM-FREE (already observed to 3200; not fresh) |
| ZP-4 | longest run of equal digits starting in `[B, 2B)` is `≤ 6` | `P(run ≥ 7 somewhere) ≈ B·15·16^(-7) < 10^(-4)` |
| ZP-5 | carries of the sources `A_π` and `A_π + A_0` differ at `≤ 12` of the times `n ≤ 2600`, and `|D^(ρ=1)_(B,h) - D_(B,h)| ≤ 2π|h|/(8B+1)` (the latter is theorem-grade) | `Σ_(n≤2600) 2/(8n) ≈ 2.1` expected differences |

## Hostile and null controls (expected outcomes stated in advance)

| Control | Expected |
|---|---|
| coherent seed `s = -x` (as `U_n = -T_n` by enclosure) | carries 15, `c^κ = 0`, `ε ≡ 1`, `|D - 1| ≤ (π/32)|h|B^(-2)` |
| null source `A_0`, zero seed | `|D_(B,h) - 1| ≤ 2π|h|/(8B+1)`; all carries 0 |
| hostile source `g_H`, zero seed | carries 15 from some `n_0 ≤ 3` on; `Re D_(B,h) ≥ 1 - 2π|h| max T^H`; seam density 1 |
| rational shadows `1/17`, `7/15` | `1/17`: `c_B = 1`, `|W_B(17)| = 1`, `|W_B(1)| = |cos(2π/17)| + O(1/B)`; `7/15`: `c_B = 0`, `W_B(15) = 1` |
| Shallit point `K` | `Re W_(2^k)(1; K) ≥ 1 - 2⌈log_16 2^k⌉/2^k - 10^(-3)` for `k = 8, 9, 10` |
| IAD-07 hijack seed for the shell `B = 243` (`q = 1009`) | `|W_B(1) - 1| ≤ π/(3840B)`; `c_B = 0` on the shell |
| random digit strings | ZP-1, ZP-2 bands hold (positive control for the bands) |

## Mutation controls (the test must reject each mutated statement on at least one input)

| ID | Mutation | Must fail on |
|---|---|---|
| ZM-1 | locality threshold `1/256 → 1/128` in ZSC-02 Lemma 2 | an explicit `y = 1/15 + 3/(2·15·256)` |
| ZM-2 | stretch lemma with `2N - B` replaced by `2N - B + 1` | the coherent point `ξ = 0` shifted by `16^(-m-N)`, anti-aligned tail |
| ZM-3 | renewal length `J(n) → J(n) + 3` | a forced-seam seed |
| ZM-4 | the retired IAD-04 display | `(100, 1, 1, 1000)` |
| ZM-5 | wrong null vector `A_0 + e_8` | `L(A) ≠ 0` to 40 digits, and rank test |

## What no outcome can establish

Every item above tests an instrument or an instance of a proved statement. No outcome changes the
status of (CH), of the seam density, of any signed estimate, or of π normality: all remain OPEN.
