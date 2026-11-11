# Probes — what was run and what came out

**Scope.** Finite, exact-arithmetic probes of the theorems in [THEOREMS](THEOREMS.md) and
[SCOTT_TRANSPORT](SCOTT_TRANSPORT.md), run after [PREREGISTRATION](PREREGISTRATION.md) was
committed (`e3f4111b`). They test theorem instances and instruments. **No outcome here changes the
status of any OPEN claim.** Raw data: `RESULTS_analytic.json`, `RESULTS_arithmetic.json`,
`RESULTS_band_lp.json` (deterministic; fixed seeds; no timestamps; byte-identical on rerun under
two Python environments, see [VALIDATION](VALIDATION.md)).

## Instruments and calibration

- `iad_core.py` — exact rational source states (frozen forcing reused from
  `observational_succ.selected_orbit`), rational tail enclosures, and certified fractional parts of
  `16^n(a + bx)` by integer arithmetic on `⌊x·16^M⌋` with 48 guard hexadecimal digits.
- Calibration on known answers before any unknown reading: hexadecimal digits of π reproduced by
  two independent routes (Machin-type integer arithmetic and mpmath) and matched against the seam
  law; `U_n + T_n` checked inside the `Y_n` enclosure; `Δ_ℓ(n)` by two exact routes; the alias seed
  `1/16` reproduces the true seed's phases exactly for `n ≥ 1`; the coherent seed returns
  correlation `(B-ℓ)/B`; `x' = 1/17` returns `cos(2πh/17)` to `10^-74` for even `B`.
- Every test file carries mutation controls (pole-mutated forcing, wrong normalization, wrong
  constant, flipped sign, hijack seed with a non-coprime modulus or too small a denominator, wrong
  birth formula): 23 analytic and 32 arithmetic tests, each mutation caught.
- Phases are reduced exactly modulo one as rationals before any float is formed.

## Design (as preregistered)

Holdout shells `B ∈ {200, 360, 729, 1000}`, modes `h ∈ {1, 3, 8}`, lags `1 ≤ ℓ ≤ ⌊4.5 log_16 B⌋`,
seam range `1301 ≤ n ≤ 3200`. Calibration shells `B ∈ {64, 256}` and seam range `n ≤ 1300` are
reported separately and not counted. Controls: true seed; coherent `s = -x`; shadow `s = -P_L`;
alias `1/16`; hijack `a/q^k` (`q = 1000003`); periodic `1/17`, `1/5`; factorial-sparse; AT-07;
seeded random unimodular.

## PR-1 — theorem-grade checks (any failure would refute the theorem)

| ID | Statement | Holdout checks | Failures |
|---|---|---:|---:|
| PR-1.1 | IAD-01 identity and (1.2), all controls and windows | 11 170 | 0 |
| PR-1.2 | IAD-02 window-energy monotonicity (2.1), (2.2) | 290 979 | 0 |
| PR-1.3 | IAD-03 innovation calculus and exact brackets (+168 993 grid checks) | 166 142 | 0 |
| PR-1.4 | IAD-04 Kusmin–Landau bound on 200 random subintervals per case, progressions `q ∈ {2,3,7}`, step facts, (4.3) | 603 559 | 0 |
| PR-1.5 | IAD-05 gauge identity, covariance bound, filtration inequality (5.2) | 714 658 | 0 |
| PR-1.6 | IAD-06 transport bound and sparse van der Corput (6.1), 50 random `H` | 16 017 | 0 |
| PR-1.7 | IAD-07 hijack seed: all primes `≤ 16B`, 42 times per shell, residues mod `M`, coherence bound | 4 shells | 0 |
| PR-1.8 | IAD-08 (8.1), 100 synthetic cases | 100 | 0 |
| PR-1.9 | IAD-09 (a), (b): every prime birth, exact `p`-components | all births | 0 |
| PR-1.10 | SWT-02/03 for `0 ≤ n ≤ 3200`; digits vs two independent π routes; coherent and forced-seam controls | 3 201 times | 0 |
| PR-1.11 | SWT-01(i) on 5 streams with 141 planted edits each | all blocks `k ≤ 3` | 0 |

No inequality failed even at zero tolerance. Tightness observed: (4.3) is nearly sharp (smallest
margin `9.9·10^-8` at `B = 1000`); (8.1) is sharp up to `1 - 16^-N`; the separation bound
`(p-5)/8` of IAD-09a is attained; (6.1) is attained with equality on some `H`; observed
Kusmin–Landau sums are at most `0.055` of the bound (the constant 4401 is safe, not sharp).

## A statement the probes refuted (retained)

**IAD-09(d), as first written, is false.** The first draft claimed that every fresh pole term
`c·16^k/p` with `|c|·16^k < p` has `Q_p/Z_p`-class equal to its real value modulo one. The
arithmetic probe found 1119 counterexamples on the holdout shells, all of one kind: the pole
`4m-1` at age 0, term `-1/(2p)`, whose real value is `(2p-1)/(2p)` and whose `p`-class is
`(p-1)/(2p)` (first instance `p = 823`, `n = 201`, `ℓ = 5`). The independent audit found the same
defect (`p = 7`). The corrected statement (integral `c·16^k`; equivalently `{t}_p + {t}_2 ≡ t`)
has 0 failures. The probe still reports the literal form as failing, on purpose.

## PR-2 — finite discrimination predictions

| ID | Prediction | Outcome |
|---|---|---|
| PR-2.1 | `E[Z]` bit-identical across seeds 1–5 and within (4.2) | **met**; observed means are at most `0.011` of the bound |
| PR-2.2 (true seed) | `|c^U_ℓ| ≤ 4/√(B-ℓ)` at `ℓ_0, 2ℓ_0, 3ℓ_0` | **met**; largest value is `0.49` of the threshold |
| PR-2.2 (alias) | equals the true seed | **met**; difference exactly 0 |
| PR-2.2 (controls 2, 3, 5) | `Re c^U_ℓ ≥ 0.99` | **NOT MET — the threshold was mis-specified.** Observed `Re c^U_ℓ = 1 - ℓ/B` to `10^-12` (range `0.925–0.994`); only 6 of 36 cases reach `0.99`. The `1/B` normalization over `B-ℓ` terms makes `0.99` unreachable once `ℓ > B/100`. The controls are fully coherent (every summand is 1 to `10^-10`); the miss is the preregistration's arithmetic, the same normalization slip the audit found in IAD-07. Not re-thresholded. |
| PR-2.3 (inequality) | `|Cov(A,Z) - E[C]| ≤ |E[Z]| + (π/32)|h|B^-2` | **met**, 0 failures |
| PR-2.3 (true seed) | `|Cov| ≤ 5/√B` in the window | **met**; largest `0.112` against smallest threshold `0.158` |
| PR-2.3 (control 2) | `|Cov| ≥ 0.9` in the window | **NOT MET at the low end of the window** (12 of 30 cases reach `0.9`). Where `|E[Z]|` is still near 1 the covariance is small for every seed (e.g. `B = 1000`, `h = 1`: `0.0004` at `ℓ = 5`, `0.107` at `ℓ = 6`, `0.98` at `ℓ = 7`). The prediction should have been restricted to lags with `|E[Z]|` small; IAD-05 Corollary 1 now says so. |
| PR-2.4 | sparse vdC right side: true `≤ 1/k + 3/√B`; control 2 `≥ 0.95` | **met** (true seed at least `0.077` below threshold; control 2 at least `1.003`) |
| PR-2.5 | Fejér `L·γ_L ∈ [0.4, 1.6]` (true), `≥ 0.8L` (control 2) at `L = ⌊√B⌋` | **met** on holdouts (`0.628–1.529`); one calibration case misses (`B = 256`, `h = 3`: `1.821`) |
| PR-2.6 | no seam event and no carry 16 for `1301 ≤ n ≤ 3200` | **met**; also none for `n ≤ 1300` |
| PR-2.7 | mean births per window within 20% of prediction | **met**; ratios `0.979–1.017` |
| PR-2.8 | `max_(B ≤ 3200) [-log_16‖16^B x‖ - log_16 B] ≤ 2` | **met**; maximum `0.855` at `B = 2949` |

Two preregistered control thresholds were wrong and are reported as misses, not repaired after the
fact. Neither bears on a theorem.

## PR-3 — hostile rejections

- Coherent, shadow and hijack seeds pass every PR-1 check (the theorems hold for all seeds) and
  violate the true-seed bounds of PR-2.2/2.4/2.5 in every case.
- Alias `1/16`: completed phases equal the true seed's exactly for `n ≥ 1`, differ at `n = 0`; it
  is separated only by the unwrapped seed.
- AT-07 (imported from `arithmetic_barrier/arithmetic/transport.py`): `-1/(8n+1) < E_n < 0` for
  `n ≤ 400`; `|W_200(h) - 1| = 0.0027, 0.0082, 0.0218` for `h = 1, 3, 8`; all 478 tested odd
  prime-power conductor depths present. Its forcing is negative at `n = 1` and positive,
  decreasing and convex for `2 ≤ n ≤ 400`; IAD-04 is not asserted for it.
- `x' = 1/17`: `‖16^B/17‖ = 1/17` exactly for `B ≤ 200` while the shell mean is `cos(2πh/17)`.
- Seam controls: the coherent seed has `κ ≡ 15`, `ε ≡ 1` (402 times, no carry 16); a rational seed
  constructed to force a carry 16 satisfies the look-ahead characterization of SWT-03.

## Selected readings

**Age ladder, `B = 1000`, `h = 1` (untwisted `|E[Z]|`, identical for every seed).**

| `ℓ` | 1–3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 |
|---|---|---|---|---|---|---|---|---|---|
| `ℓ / log_16 B` | – | 1.61 | 2.01 | 2.41 | 2.81 | 3.21 | 3.61 | 4.01 | 4.42 |
| `|E[Z]|` | 1 | 0.999999 | 0.99978 | 0.9449 | 0.1353 | 0.0092 | 0.0187 | 0.0318 | 0.0375 |

No saving below `2 log_16 B`, decay through the window, and continued smallness beyond
`3 log_16 B` (the regime covered only by the imported higher-derivative test).

**Hijack against the true seed.**

| `B` | hijack `|W_B - 1|` (`h = 1, 3, 8`) | allowed `π|h|/(3840B)` | true `|W_B|` |
|---|---|---|---|
| 200 | `1.3e-11, 4.0e-11, 1.1e-10` | `4.1e-6, 1.2e-5, 3.3e-5` | 0.042, 0.049, 0.038 |
| 360 | `1.1e-10, 3.4e-10, 9.1e-10` | `2.3e-6, 6.8e-6, 1.8e-5` | 0.061, 0.018, 0.031 |
| 729 | `2.1e-10, 6.2e-10, 1.7e-9` | `1.1e-6, 3.4e-6, 9.0e-6` | 0.020, 0.081, 0.008 |
| 1000 | `1.1e-11, 3.2e-11, 8.6e-11` | `8.2e-7, 2.5e-6, 6.5e-6` | 0.059, 0.040, 0.045 |

At every prime `p ≤ 16B` and all 42 sampled times the two seeds have identical `Q_p/Z_p` classes.

**Birth mass (mean prime births per innovation window).**

| `B` | `ℓ` | observed | predicted | windows with no birth |
|---|---|---|---|---|
| 200 | 5 / 8 | 4.06 / 6.50 | 3.99 / 6.39 | 0 / 0 |
| 360 | 5 / 9 | 3.64 / 6.53 | 3.70 / 6.67 | 0 / 0 |
| 729 | 6 / 10 | 4.04 / 6.74 | 4.09 / 6.81 | 0.14% / 0 |
| 1000 | 6 / 11 | 3.88 / 7.11 | 3.95 / 7.23 | 0.6% / 0 |

**Seam.** For `0 ≤ n ≤ 3200` the literal carries take values `0…15` only, `ε_n = 0` throughout,
and `d_n = κ_(n+1)` at every time: on this range the hexadecimal digits of π are exactly the
shifted literal carries of the rational source.

**Band extremal constant (`band_lp_probe.py`, floating-point LP).** Largest atom at frequency 0
of a positive measure with vanishing coefficients on the lag band: `0.5` (one lag), `0.4972`
(ratio 1.1), `0.4472` (ratio 1.5, four scales), `0.376`/`0.366` (ratio 1.95/1.975).

## Deviations from the preregistration

- PR-1.9 windows cover `n ∈ [B-1, 2B]`, a superset of the preregistered range; nothing was
  sampled.
- Extra checks were added (all subintervals for (4.1) on small shells, singleton-cell partitions,
  windows `L ∈ {B/8, B/4, B/2, B}`, derivative signs to order 6); trivial `J = L` pairs dropped.
- Readings of ambiguous wording: "in the window" in PR-2.3 was taken as
  `2 log_16 B < ℓ < 3 log_16 B`.
- IAD-09(c)/(d), SWT-04, SWT-05(B) and the seam-density bound are recorded as additional theorem
  checks outside the preregistered PR-1 list; all pass except the literal IAD-09(d) above.
- One float artefact (`cot y ≤ 1/y` at `y ≈ 10^-9`) was removed by evaluating at 50 digits; it was
  rounding, not a theorem failure.
- `CompletedOrbit.floor()` in `iad_core.py` is not certified when the fractional part is within
  the guard error of 1; the probes guard for it and it was never triggered.

## What these probes do not show

They do not show that the twisted correlations of the true seed tend to 0, that any bound holds
on all large shells, or anything about normality. The true seed looks random-scale on four
shells; so would any generic point. The decisive content of this dossier is in the theorems and
the obstructions, not in these tables.

---

# Continuation probe (ZSC)

**Scope.** `probe_zsc.py` tests instances of ZSC-01…06 of [CARRY_FLUX](CARRY_FLUX.md) and the
repaired IAD-04 corollary, after [PREREGISTRATION_ZSC](PREREGISTRATION_ZSC.md) was committed
(`d6bdb2bd`). **No outcome changes the status of any OPEN claim.** Raw data: `RESULTS_zsc.json`
(19 kB; deterministic; fixed seed; no timestamps). Run time ≈ 15 s.

## Instruments and calibration

- Two routes to the digits of `x`: integer arithmetic on an mpmath enclosure, and the literal
  carries of exact rationals through the cocycle `d_n = κ_(n+1) + ε_(n+1) - 16ε_n` with rational
  tail enclosures; they agree for `2 ≤ n ≤ 2600`. The look-ahead identity of ZSC-04 compares
  `⌊16^(n-1)π⌋` from the first route with `⌊C_(42n-41)/16^(41(n-1))⌋` from the second for
  `2 ≤ n ≤ 40`.
- Fractional parts are kept to 40 hexadecimal digits and phases are reduced exactly modulo one
  before a float is formed; inequalities are checked with tolerance `10^-9`.
- Known answers first: `g_π` through the general source class reproduces the frozen forcing
  exactly; `L(A_π)` encloses `π/16` and `L(A_0)` encloses 0 to 60 digits; the shadow `1/17` returns
  `|cos(2π/17)|` at mode 1 and modulus 1 at mode 17.

## Design

Calibration shells `B ∈ {64, 128}`; fresh holdout shells `B ∈ {243, 420, 811, 1210}`; modes
`h ∈ {1, 3, 15, 17}`; zero-seed horizon `n ≤ 2600`.

## Theorem-grade checks: 247 588, 0 failures

| ID | Checks | Content |
|---|---|---|
| ZC-1 | 10 243 (all non-trivial) | stretch lemma (1.1) on π, the witnesses, the Shallit point, shadows, random strings and 40 near-dyadic points |
| ZC-2 | 9 925 | law (1.2) for `ξ_λ` (`λ = 1/4, 1/2, 3/4`), a random string and W3, hypothesis verified on `32 ≤ B ≤ 2048` |
| ZC-3 | 177 165 | locality lemma at every position of twelve digit strings |
| ZC-4 | 360 | ZSC-02 (a), (b) for `k = 2, 3, 4`, (c), on every shell of every string |
| ZC-5 | 2 872 | renewal lemma from 260 admissible states and on six forced-seam seeds; `J(n) ≥ ⌊log_4 2n⌋` for `n ≤ 2600`; RIO-09 window |
| ZC-6 | 6 715 | cocycle and the `(ε_n, ε_(n+1), ε_(n+2))` case table: zero seed to 2600, six forced-seam seeds |
| ZC-7 | 2 737 | runs `≤ 41n`; exact look-ahead for `2 ≤ n ≤ 40` |
| ZC-8 | 37 360 | W1–W3 on prefixes of length 20 000 |
| ZC-9 | 90 | gauge identity for three `h`; proper form; rank 7 and kernel `Q·A_0`; partial fractions; null, hostile and `ρ`-family sources for `n ≤ 400` |
| ZC-10 | 13 | repaired IAD-04 corollary on occupied cells; the retired display is violated at `(100, 1, 1, 1000)` (left side 1, right side negative) |
| ZC-11 | 24 | `|D_(B,h) - W_B(h)| ≤ (π/32)|h|B^(-2)` between the two routes |
| controls | 84 | below |

## Zero seed on the shells (π; `c_B` = change density)

| `B` | `c_B` | `|W_B(1)|` | `|W_B(3)|` | `|W_B(15)|` | `|W_B(17)|` | longest run |
|---|---|---|---|---|---|---|
| 64 (cal.) | 0.9375 | 0.0629 | 0.0807 | 0.0946 | 0.0427 | 2 |
| 128 (cal.) | 0.9688 | 0.0654 | 0.0803 | 0.0465 | 0.0630 | 2 |
| 243 | 0.9424 | 0.0908 | 0.0703 | 0.0289 | 0.0221 | 2 |
| 420 | 0.9310 | 0.0732 | 0.0260 | 0.0620 | 0.0502 | 2 |
| 811 | 0.9383 | 0.0454 | 0.0603 | 0.0205 | 0.0270 | 3 |
| 1210 | 0.9306 | 0.0178 | 0.0385 | 0.0316 | 0.0312 | 4 |

**Predictions (holdout).** ZP-1 (`|c_B - 15/16| ≤ 4·sqrt(15/(256B))`): met, 4 of 4. ZP-2
(`|W_B(h)| ≤ 4/√B`): met, 16 of 16. ZP-3 (no letter 16, no seam for `n ≤ 2600`): met, not fresh.
ZP-4 (longest equal-digit run in a shell `≤ 6`): met. ZP-5 (carries of `A_π` and `A_π + A_0`
differ at `≤ 12` times): met — they differ at exactly two times, `n = 162, 163`, of 2422. These
readings are what any generic point would give; they are not evidence for (CH) beyond the four
shells.

## Witnesses and controls (all outcomes as stated in advance)

| Object | Reading |
|---|---|
| `ξ_λ` (ZSC-01, Remark 4), least saving `1 - Re W_B(1)` over `32 ≤ B ≤ 2048` | `λ = 1/4`: 1.1859 (formula 1.1869, ceiling 1.2); `1/2`: 0.6585 (0.6594, 0.6667); `3/4`: 0.2819 (0.2826, 0.2857) |
| Shallit point `K` | `Re W_B(1) = 0.99970, 0.99985, 0.99993` at `B = 256, 512, 1024` |
| W1 | changes per shell 24, 56, 104, 148 at `B = 243, 1210, 4096, 8192`; seam density `≥ 0.75, 0.85, 0.91, 0.93`; `Re W_B(1) ≥ 0.996` |
| W2 | no digit 0; at most 2 changes per shell; `Re W_B(1) ≥ 0.9996` |
| W3 | `c_B = 0.494 … 0.514`; seam density `0.42 … 0.48`; `|W_B(1)| ≈ 0.943 … 0.945` |
| forced-seam seeds (six) | one letter 16 each, followed by `J(n)+1` zeros; 2–3 carry/digit discrepancies per seam run, never more than 3 |
| null source `A_0`, zero seed | all carries 0; `|D - 1| ≤ 2π|h|/(8B+1)` |
| hostile source `g_H`, zero seed | carries 15 from `n = 2`; seam bit 1; `Re D_(B,h) ≥ 1 - 2π|h|T^H_B` |
| IAD-07 hijack seed, `B = 243`, `q = 1009` | `|W_B(1) - 1| = 1.3·10^-7`; digits constant on the shell |
| shadows `1/17`, `7/15` | `c_B = 1`, `|W_B(17)| = 1`; `c_B = 0`, `W_B(15) = 1` |
| two random strings | 60 band instances, 0 misses (positive control for ZP-1, ZP-2) |

## Mutation controls

ZM-2 (stretch lemma with `2N - B + 1`), ZM-3 (renewal length `J + 3`), ZM-4 (the retired IAD-04
display) and ZM-5 (null vector `A_0 + e_8`) are each rejected.

**ZM-1 was mis-specified in the preregistration and is reported as such.** The registered input
`y = 1/15 + 3/(2·15·256)` satisfies `‖15y‖ < 1/128` but has **no** digit change (at `j = 1` the
upward margin is `14/(15·256)`), so it does not exhibit the failure of the mutated threshold. The
mirror input `y = 1/15 - 3/(2·15·256)` does (`0.10…` in base 16) and rejects the mutation. Both
are recorded in `RESULTS_zsc.json`; the unit test additionally checks the equality case
`y = 239/256` and an exhaustive grid of 30 720 points.

## Deviations from the preregistration

- ZC-3/ZC-4 digit strings have length 4300, not 5000.
- ZC-5: the zero seed, the coherent seed, the null source and the hostile source contain no
  letter 16 on the horizon, so the renewal lemma is vacuous there (and the last two have a
  different forcing). It was tested instead from 260 admissible states `{U_n} ∈ [1 - r(n+1)/16, 1)`
  and on the six forced-seam seeds.
- Coherent-seed control: only the phase bound was run; its carries were verified in the first
  round's probe and follow algebraically (`⌊16 - T_n⌋ = 15`).
- ZC-1 was run on all twelve strings, a superset of the registered inputs.

## What this probe does not show

Nothing about (CH), the seam density, any saving for the zero seed on all large shells, or
normality. Four holdout shells with `c_B ≈ 15/16` are four shells.
