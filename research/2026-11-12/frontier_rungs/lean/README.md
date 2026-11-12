# ZSC carry-flux lemmas: kernel checks (Lean 4.14.0, pinned mathlib)

Source dossier: `research/2026-11-11/innovation_arithmetic_decoupling/CARRY_FLUX.md`
(its sha256 is pinned in `RECEIPT.json`). This directory gives **kernel authority** to a few
small exact lemmas of that dossier. It does not touch any existing file, and no statistical,
Diophantine or asymptotic claim of the dossier is checked here. π base-16 normality, (CH) and RH
remain OPEN.

| File | Role |
|---|---|
| `ZSCCarryFlux.lean` | Lean source: namespace `ObservationalSUCC.ZSCCarryFlux` |
| `check_zsc_carry_flux_lean.py` | Self-contained serial check: pins, compile, axiom export, mutant controls |
| `RECEIPT.json` | Compact receipt: file hashes, toolchain, mathlib pin, axioms per theorem, control outcomes |

## Reproduce

```sh
cd <repository root>
python3 research/2026-11-12/frontier_rungs/lean/check_zsc_carry_flux_lean.py \
  --dependency-project <prebuilt formal/mathlib_bridge> \
  --output <directory outside the checkout> \
  --receipt research/2026-11-12/frontier_rungs/lean/RECEIPT.json
```

`--dependency-project` may be any prebuilt copy of `formal/mathlib_bridge` (in this checkout,
`formal/mathlib_bridge` itself also has a built `.lake`). The script verifies that each package
there is at the revision pinned in `formal/mathlib_bridge/lake-manifest.json` and has a clean
worktree, and that `lean --version` (resolved by elan from the repository's `lean-toolchain`) is
4.14.0. It rebuilds nothing. The full observation (every command, log, exported type expression)
goes to `--output`; only the compact receipt is kept here.

## Result of the recorded run

Recorded run: at commit `9d6f2e56` of branch `research/frontier-rungs-restricted-exponent-2026-11-12`,
after the re-audit repairs to `CARRY_FLUX.md` (whose current sha256 is the one pinned). The files
of this directory were untracked at that commit, so the sha256 pins in `RECEIPT.json` identify
them, not the commit. The check was written and first run by a helper instance (at `9b4b71b2`,
114.5 s) and re-run twice by the integrator with the same outcome.

- Status `KERNEL_CHECKED`: 33 theorems exported, 9 of 9 mutant controls passed, 117.3 s wall
  (module compile, axiom export, and 27 control compiles).
- Every theorem depends on exactly `propext`, `Classical.choice`, `Quot.sound`: the standard
  mathlib axioms for real analysis and `Int.floor` on `ℝ`. There is no `sorry`, `axiom`,
  `native_decide`, `unsafe`, `implemented_by` or `extern` in the source. The script scans the
  source with comments removed and stops if it finds one.
- Toolchain `leanprover/lean4:v4.14.0` (`lean` 4.14.0, commit `410fab728470`). mathlib pin is
  `4bbdccd9c5f862bf90ff12f0a9e2c8be032b9a84`, and all 9 manifest packages were verified at their
  pinned revisions.

## What is KERNEL_CHECKED (namespace `ObservationalSUCC.ZSCCarryFlux`)

Definitions used in the statements are as follows.
- `hexDigit y i := ⌊16 * Int.fract (16 ^ i * y)⌋` is the file's `d_i`, with `y_n = 16^n ξ`.
- The file's `‖t‖` is written `|t - round t|`. By mathlib's `round_le`, this distance is at most
  `|t - m|` for every integer `m`, so it is the distance to the nearest integer.
- `A0 : ℕ → ℚ` is `8, -8, -4, -8, -2, -2, 1, 0` at indices 0 to 7 and `0` at every later index.
- `rPi m := 4/(8m-7) - 2/(8m-4) - 1/(8m-3) - 1/(8m-2)` is the four-pole forcing of
  `A_π = (4,0,0,-2,-1,-1,0,0)`.
- `Jn n := ⌊Real.logb 16 (15 / (16 * rPi (n + 1)))⌋` is the file's `J(n)`.

**L1, ZSC-06(a)/(d)/(f)3, the null relation**
- `zsc06_null_partial_fraction`: in any field, if `z²-2 ≠ 0` and `z²-2z+2 ≠ 0`, then
  `(z²-4z+2)/((2-z²)(z²-2z+2)) = z/(z²-2) - (z-1)/(z²-2z+2)`.
- `zsc06_sixteen_factorisation`, as an identity in `ℚ[X]`: `16 - X⁸ = (X²+2)(X²+2X+2)·((2-X²)(X²-2X+2))`.
- `zsc06_authentic_numerator`: `K·(1-X) = 4 - 2X³ - X⁴ - X⁵`.
- `zsc06_null_numerator`: `K·(X²-4X+2) = 8 - 8X - 4X² - 8X³ - 2X⁴ - 2X⁵ + X⁶`.
- `zsc06_null_coefficient_vector` and `zsc06_null_coeff`: for every `i`,
  `(K·(X²-4X+2)).coeff i = A0 i`. This is the vector `A_0`.
- `zsc06_hostile_numerator`: `(16-X⁸)(3-2X) + g_0 = 2X⁹ - 3X⁸ + X⁶ - 2X⁵ - 2X⁴ - 8X³ - 4X² - 40X + 56`.
- `zsc06_null_integral`: `∫ z in 0..1, (z²-4z+2)/((2-z²)(z²-2z+2)) = 0`. The proof uses the
  fundamental theorem of calculus with the file's antiderivative.
- `zsc06_null_period_integral`: `∫ z in 0..1, g_0(z)/(16-z⁸) = 0`.
- `zsc06_L_A0_eq_zero`: `Σ_{i<8} A0 i · ∫ z in 0..1, z^i/(16-z⁸) = 0`. This is `L(A_0) = 0`
  with `v_j` in the file's integral form.

**L2, ZSC-02 locality lemma** (every real `ξ`)
- `zsc02_locality_run (ξ) (n k : ℕ)`: if `∀ i < k, d_{n+i} = d_n`, then
  `|15·y_n - round(15·y_n)| ≤ 15/16^k`. This is Lemma 1 for every `k`, including `k = 0`.
- `zsc02_locality_change (ξ) (n : ℕ)`: if `|15·y_n - round(15·y_n)| < 1/256`, then
  `d_n = d_(n+1)`. This is Lemma 2.
- `zsc02_locality_run_zero` and `zsc02_locality_change_zero` are the same two statements at
  position 0.
- `zsc02_two_digit_form`: for `0 ≤ y < 1`,
  - `⌊16y⌋ = ⌊16(16y - ⌊16y⌋)⌋ → ‖15y‖ ≤ 15/256`, and
  - `‖15y‖ < 1/256 → ⌊16y⌋ = ⌊16(16y - ⌊16y⌋)⌋`.

**L3, ZSC-03 renewal lemma** (every real seed). The carry is
`κ_m = ⌊U_m⌋ - 16⌊U_(m-1)⌋` and the recurrence is `U(m+1) = 16·U m + r(m+1)`.
- `zsc03_renewal_kernel`: let `r` be any forcing with `0 ≤ r(n+1+i) ≤ r(n+1)` for all `i`.
  If `κ_(n+1) = 16` and `(16/15)·16^J·r(n+1) ≤ 1`, then `κ_(n+1+j) = 0` for `1 ≤ j ≤ J`.
- Bounds on the four-pole forcing:
  - `rPi_succ_pos`: `0 < r(n+1)`.
  - `rPi_succ_antitone`: `r(n+2) ≤ r(n+1)`.
  - `rPi_succ_le`: `r(n+1) ≤ 15/((8n+1)(8n+2))`.
- `Jn_le_iff`: `(j:ℤ) ≤ J(n) ↔ (16/15)·16^j·r(n+1) ≤ 1`.
- `zsc03_J_ge`: if `n ≥ 1`, then `⌊logb 4 (2n)⌋ ≤ J(n)`.
- `zsc03_window`: if `n ≥ 1` and `4^L ≤ 2n`, then `(16/15)·16^L·r(n+1) ≤ 1`. This is the integer
  form behind `test_zsc.py::Renewal` (`4^(J+1) > 2n`).
- `zsc03_renewal_lemma`: under the recurrence with `rPi`, if `κ_(n+1) = 16`, then
  `κ_(n+1+j) = 0` for every natural `j` with `1 ≤ j` and `(j:ℤ) ≤ J(n)`. This is the file's
  statement, for every `n` (the file assumes `n ≥ 1`).
- `zsc03_renewal_authentic`: the same conclusion with `J(n)` replaced by any `L` such that
  `4^L ≤ 2n`.

## Mutant controls (each with a kernel-checked refutation)

Each control takes the exact closed statement `P` of a theorem and changes one substring to get
`P'`. It passes only if all three of these hold:
1. `P` compiles from the theorem.
2. `P'` does **not** compile from the theorem, and fails with `type mismatch`. This is the
   repository's usual paired control.
3. `¬ P'` compiles from a `refute_*` theorem, so `P'` is proved false.

| Control | Mutation | Refutation witness |
|---|---|---|
| partial-fraction-sign | `- (z-1)/…` → `+ (z-1)/…` | `z = 0` in `ℚ` |
| null-numerator-coefficient | `- 8X³` → `+ 8X³` | evaluate at `1` (`-15` vs `1`) |
| sixteen-factorisation | `(2 - X²)` → `(2 + X²)` | evaluate at `1` (`15` vs `45`) |
| null-integral-numerator | numerator `…+2` → `…+3` | integral = `0 + ∫ 1/m > 0` |
| locality-change-threshold | `< 1/256` → `< 1/200` | `ξ = 249/3750`: `‖15ξ‖ = 1/250`, digits `1, 0` |
| locality-run-constant | `15/16^k` → `14/16^k` | `ξ = 255/256`, `k = 2`: digits `F, F`, `‖15ξ‖ = 15/256` |
| window-two-n | `4^L ≤ 2n` → `4^L ≤ 4n` | `n = L = 1` |
| renewal-kernel-overrun | `j ≤ J` → `j ≤ J+1` | `r ≡ 15/256`, `J = 1`, seed `65535/65536`: carries `16, 0, 15` |
| renewal-lemma-overrun | `j ≤ J(n)` → `j ≤ J(n)+1` | real forcing, `n = 1` (`J(1) = 0`), `U_1 = 999/1000`: `κ_2 = 16`, `κ_3 = 1` |

Leg 3 is needed. In a self-test, a mutant that is still true (`2 * n` → `n * 2`), paired with an
unrelated refutation, passed legs 1 and 2 with `type mismatch`. Only leg 3 marked the control as
failed. So a `type mismatch` failure alone does not show that a mutant is false.

The two ZSC-02 controls show that both constants are reached exactly or cannot be improved.
- Lemma 1 holds with equality at `ξ = 255/256`, `k = 2`. Only this case is kernel-checked. A
  Python check finds equality at `ξ = 1 - 16^(-k)` for `k = 2..6`.
- Lemma 2 fails at the threshold `1/200`. Only that one case is kernel-checked. Exact
  arithmetic in Python also finds counterexamples with `‖15y‖` slightly above `1/256`.

## What is NOT kernel-checked

- The BBP series form `v_j = Σ_k 16^(-k-1)/(8k+j)`, the identity `ξ = π/16`, and any claim
  about π.
- The identity `rPi(n) = ∫_0^1 z^(8n-8) g_π(z) dz`. The forcing is taken in closed form.
- ZSC-06(e), Baker rigidity, which is an imported theorem that has not been re-read, and the
  rest of ZSC-06(f).
- ZSC-03: the RIO-09 upper window `b < 1 + log_16((8n+9)(8n+14)/15)`, and Corollaries 1 and 2.
- ZSC-01, ZSC-02 Theorem (a) to (d), ZSC-04 (Mahler), ZSC-05, (CH), seam density, and every
  asymptotic or statistical statement.

## Comparison with CARRY_FLUX.md

**No disagreement was found.** Every statement listed above was proved exactly as the file
states it. Two statements were proved slightly more generally:
- Lemma 1 also holds for `k = 0`, where it is trivial.
- The renewal lemma does not need `n ≥ 1`. That hypothesis is used only in `J(n) ≥ ⌊log_4 2n⌋`.
