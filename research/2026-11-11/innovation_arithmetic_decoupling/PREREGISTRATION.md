# Preregistration — written and committed before any holdout probe is run

**Baseline:** Main XXIV `071ce1e0ee6ab8f8c07113e901131aa646d6b95d`. This file is committed in the
same commit as `THEOREMS.md`, `SCOTT_TRANSPORT.md` and `iad_core.py`, and before
`probe_*.py`, `RESULTS*.json` or `PROBES.md` exist. The commit order is the receipt.

## Disclosure: what was already looked at (calibration, not holdout)

While deriving the theorems, two scratch scripts (not in the repository) were run on the true
zero-seed source:

- shells `B ∈ {64, 256, 1024}`, `h ∈ {1, 3}`, lags `1 ≤ ℓ ≤ 4.2 log_16 B`: untwisted innovation
  means, the Kusmin–Landau bound, the low-lag deviation bound, exact derivative brackets on a
  rational grid `t ∈ [2, 288]`;
- shell `B = 512`, `h ∈ {1, 3}`: the Fejér identity and window-energy monotonicity for the true
  seed, a constant sequence and one pseudo-random sequence; the seam law `d_n = κ_(n+1) +
  ε_(n+1) - 16ε_n` for `n ≤ 1300` (result: no seam event, no carry 16).

Those shells and that seam range are **calibration**. They may be rerun as regression checks but
are not counted as holdouts.

## Holdout design (fresh, non-dyadic)

- Shells: `B ∈ {200, 360, 729, 1000}`; modes `h ∈ {1, 3, 8}`.
- Lags: every `1 ≤ ℓ ≤ ⌊4.5 log_16 B⌋`; the mesoscopic lag `ℓ_0(B) = ⌈2.25 log_16 B⌉` and its
  multiples `2ℓ_0, 3ℓ_0` for the sparse van der Corput budget.
- Fejér windows: `L ∈ {2, 3, 5, 8, ⌊√B⌋, 2⌊√B⌋}`.
- Seam range: `1301 ≤ n ≤ 3200`.
- Seeds / controls run through the same evaluators:
  1. true source, `U_0 = 0`;
  2. coherent wrong seed `s = -x` (completed orbit identically 0);
  3. rational zero-prefix shadow `s_B = -P_L`, `L = 2B + 16`;
  4. rational alias `s = 1/16` (later circle phases must coincide with the true seed — a
     discriminator is mathematically impossible and is *not* demanded; only the unwrapped seed
     differs);
  5. one-missing-place hijack `s = a/q^k` of IAD-07 with `q = 1000003`, `M = ∏_{p ≤ 97} p^2` (odd
     primes) `· 2^8`, `K = 2B`;
  6. periodic completed points `x' = 1/17` and `x' = 1/5`;
  7. factorial-sparse irrational `x' = Σ_{j ≥ 2} 16^{-j!}`;
  8. AT-07 seven-pole null source with its own zero seed (different forcing);
  9. a seeded pseudo-random unimodular sequence (generic-sequence calibration of the
     all-sequence inequalities).

Controls not run, and why: PPP-08 itself (IAD-07's seed is its strict generalization and is run
instead); matched-prime-marginal/incorrect-winding and the nonproduct Haar joinings (they test
parity/CRT joint laws, which no claim of this dossier asserts; IAD-07 is the applicable hostile
for prime-to-real transfer here).

## Class PR-1 — theorem checks (must hold exactly; one failure refutes the stated theorem)

| ID | Check | Refutation condition |
|---|---|---|
| PR-1.1 | IAD-01 identity (1.1) and inequality (1.2), every control, every `L` | mismatch `> 1e-12` or (1.2) violated |
| PR-1.2 | IAD-02 (2.1): `√γ_L ≤ √γ_J + J/L` all `J ≤ L`; `γ_L ≤ γ_J` for `J | L`; every control | any violation beyond `1e-12` |
| PR-1.3 | IAD-03: `Δ_ℓ(n) = 16^ℓ T_n - T_(n+ℓ)` inside the rational tail enclosure; two exact routes for `Δ`; exact brackets for `r`, `-r'`, `δ(m)` on a rational grid | any exact inequality false |
| PR-1.4 | IAD-04 (4.1): `|Σ_{n∈I}| ≤ cot(πλ/2)` for 200 seeded random subintervals per `(B, h, ℓ)` with `h16^ℓ ≤ (15/8)B³`; progression version for `q ∈ {2, 3, 7}`; (4.3) for all `ℓ` | any violation |
| PR-1.5 | IAD-05 (5.1) for seeds 1–5; (5.2) for `F_q`, `q ∈ {1, 2, 5, 16}`, and 20 seeded random partitions | mismatch `> 1e-12` or (5.2) violated |
| PR-1.6 | IAD-06 transport bound and (6.1) for 50 seeded random `H`, every control | any violation |
| PR-1.7 | IAD-07 items 1–3 exactly, for the hijack seed on each holdout shell: `Q_p/Z_p` classes equal for all primes `p ≤ 16B`, residues mod `M` equal, `|W_B - 1| ≤ π|h|/(3840B)` | any inequality false |
| PR-1.8 | IAD-08 (8.1) on synthetic `x' = a/16^B + ε'`, 100 seeded cases | any violation |
| PR-1.9 | IAD-09 (a), (b): every prime birth with `β(p) ∈ [B, 2B + ℓ]`; exact `p`-component of `U_(n+ℓ) - U_n` | any mismatch |
| PR-1.10 | SWT-02/03: `κ_n ∈ {0..16}`, `C_n = Σ16^{n-j}κ_j`, seam law, look-ahead characterization of `ε`, for `0 ≤ n ≤ 3200`; digits equal an independent π hex expansion | any mismatch |
| PR-1.11 | SWT-01(i) on seeded synthetic streams with planted density-zero edits | inequality violated |

## Class PR-2 — finite discrimination predictions (failure is informative, not theorem-refuting)

| ID | Prediction on the holdout shells | Why |
|---|---|---|
| PR-2.1 | Untwisted `E[Z]` is bit-identical across seeds 1–5 (seed independence) and obeys (4.2) | IAD-04 scope |
| PR-2.2 | True seed: twisted means `|c^U_ℓ(B)| ≤ 4/√(B-ℓ)` at `ℓ ∈ {ℓ_0, 2ℓ_0, 3ℓ_0}`; controls 2, 3, 5: `Re c^U_ℓ ≥ 0.99`; control 4 equals the true value to `1e-12` | random-scale expectation vs coherence |
| PR-2.3 | `|Cov(A, Z) - E[C]| ≤ |E[Z]| + (π/32)|h|B^{-2}` (this is PR-1-grade), and for the true seed `|Cov(A,Z)| ≤ 5/√B` in the window while control 2 has `|Cov| ≥ 0.9` | IAD-05 |
| PR-2.4 | Sparse van der Corput right side for `k = 2, 3, 4`: true seed `≤ 1/k + 3/√B`; control 2 `≥ 0.95` | IAD-06 |
| PR-2.5 | Fejér: true seed `0.4 ≤ L·γ_L ≤ 1.6` at `L = ⌊√B⌋`; control 2 has `L·γ_L ≥ 0.8·L` | IAD-02 |
| PR-2.6 | Seam: zero events `ε_n = 1` and zero carries `κ_n = 16` for `1301 ≤ n ≤ 3200` | `Σ_{n>1300} T_n < 1.3·10^{-5}` |
| PR-2.7 | Birth mass: mean number of prime births in `(n, n+ℓ]` over the shell is within 20% of `ℓ·mean_m[4/ln(8m) + 2/ln(4m)]` | PNT in progressions |
| PR-2.8 | Liouville-wall observable: `max_{B ≤ 3200} [ -log_16 ‖16^B x‖ - log_16 B ] ≤ 2` (zero/F runs at position `B` no longer than `log_16 B + 2`) | random-scale expectation; the wall only requires `≤ B - log_16 B + O(1)` |

## Class PR-3 — expected failures (hostile rejections that must occur)

- The coherent seed, the shadow seed and the hijack seed must **pass** every PR-1 check (they are
  theorems for all seeds) and must **fail** PR-2.2/2.4/2.5 in the stated direction.
- The `1/16` alias must be indistinguishable from the true seed in every phase statistic at
  `n ≥ 1` and distinguishable only by the unwrapped seed `Z_n = 16^{-n}U_n(s) - P_n = 1/16`.
- AT-07 must show `W → 1` with zero seed and full conductor growth; the innovation theorem is not
  asserted for it (its forcing is not completely monotone).
- `x' = 1/17` must satisfy the conclusion of IAD-08(a) (`‖16^B x'‖ = 1/17`) while
  `W_B(h) = cos(2πh/17)`: the wall is necessary, not sufficient.

## What no outcome of these probes can do

Finite favourable data cannot establish any asymptotic statement. No PR-2 success changes the
status of any OPEN claim. A PR-1 failure retracts the corresponding theorem.
