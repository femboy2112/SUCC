# Claim supplement — Operation Main XXI integration (2026-11-07)

Namespace `MAIN_XXI` (bare prefix `MXXI`). Each row points into the research dossiers of
PRs #525–#543. Those dossiers merged into `main` unchanged in this round.

- **Status vocabulary.** Statuses use the [`docs/METHOD.md`](METHOD.md) labels; the finer
  label is in parentheses.
- **Scope notes.** A *scope note* records a wording or label correction found by the
  integration audit. The original files are left byte-identical; where a note applies,
  read the original statement through the note.
- **Who reviewed.** All reviews were same-model, read-only bearings (proof auditors and an
  adversary). None was an independent scholarly referee.
- **π base-16 normality, the selected signed Weyl gate `S_N(h)=o(N)`, and RH remain
  OPEN.** No row promotes any of them.

Audit and receipts: [SUCC_MAIN_XXI_INTEGRATION_AUDIT_2026-11-07](SUCC_MAIN_XXI_INTEGRATION_AUDIT_2026-11-07.md).

## A. Fourier–Yoneda pin beds (#541, #543 stacked on #541; #542 independent)

The three PRs use **different spaces, kernels and conventions**. They do not form one
universal theorem:

- #541 uses Bernoulli `B₂` continuous surfaces.
- #543 uses forward-window oscillator channels and a half-aperture two-channel metric.
- #542 uses finite two-tone windows and **backward** continuous convolutions `g*μ` with
  conjugated multipliers.

| ID | Claim | Status | Source / receipt |
|---|---|---|---|
| MXXI-01 | Bernoulli pin bed: `μ=λ−½D²F` inverts the `B₂` surface (from `D²B₂=2λ−2δ₀`). The affine transport has sharp norm `‖L_{b,a}‖=b²`. The discounted completion has threshold `ρb²=1`. BBP surface-norm transport is `1/(30√3A²)`. | PROVED LOCAL | #541 `research/2026-11-07/fourier_yoneda_pinbed/THEOREMS.md:93–409, 505–516` |
| MXXI-02 | Driven pin bed: the first-order continuous inverse, and the realization characterization (coherence + mass + positivity, with a ghost counterexample). The half-aperture frame `4‖η‖_{H⁻¹} ≤ D ≤ √(16+2π²)‖η‖_{H⁻¹}` is sharp at both ends. | PROVED LOCAL | #543 `driven_pinbed_observability/CONTINUOUS_THEOREMS.md:47–259` |
| MXXI-03 | One-step ×16 constant in the half-aperture metric on **real** probability-law differences: `C₁₆(½)=341/√205≈23.8164730857` (so `C²=116281/205`), attained at `h=2` (densities `1±ε cos(2π·32x)`). The `h=1` value, `(π²+8)/8·255²/257≈565.161`, falls short of `116281/205` by about 0.36%. **Boundary:** on complex inputs the ×16 operator norm is exactly `31`. "`h=2` wins" is specific to `b=16`; at `b=32`, `h=1` is larger (2280.617 vs 2273.889), though the `max{·}` formula itself is correct. | PROVED LOCAL (sharp; Verified by two blind bearings: analytic + physical-space quadrature + attaining witness, and an independent scan to `h≤20000`) | #543 `CONTINUOUS_THEOREMS.md:324–367` |
| MXXI-04 | Phase cycle, demodulation and gain calibration `g=∫Y₁/c(−1)`. Lock-in unbiasedness, variance `[S+2Re(āb c)]/(αS²)` and the Hoeffding constant. | PROVED LOCAL | #543 `LOCKIN_AND_CONTROLS.md:49–152`, `COHERENT_SCAN.md:33–66, 117–135` |
| MXXI-05 | Two-tone stable arc STP-1…STP-4. Realization RY-1…RY-3. Learning observer LO-02…LO-05: `4N` bits = `log₂16^N` are necessary and sufficient for lossless distinction of all `16^N` seeds under circle-only access, with noise margin `1/(2·16^{N−t})`. | PROVED LOCAL | #542 `pinbed_yoneda_oscillators/TWO_TONE_STABLE_ARC.md:45–189`, `REALIZATION_AND_DYNAMIC_YONEDA.md:88–183`, `LEARNING_OBSERVER.md:34–63` |
| MXXI-06 | Every pin-bed normality statement is an **equivalent reformulation** of the open gate. None says a learning observer forces π's digits to be normal. Sources: #541 `THEOREMS.md:518–537`; #542 STP-5 and PBFO-10; #543 `CONTINUOUS_THEOREMS.md:543–546`. | PROVED LOCAL (EQUIVALENT-REFORMULATION; premise OPEN; not progress) | as cited |
| MXXI-07 | Refuted strategies, each with a receipt: seed-blind holonomy (APH-01, receipt `s_*=−π/16`); erased-clock uniformity; raw DC-scan uniformity; positivity without coherence; "one missing quadrature is always fatal" (as an inference). | REFUTED | #542 `ANCHORED_PATHS_VS_HOLONOMY.md`; #543 `LOCKIN_AND_CONTROLS.md:173–216`, `COHERENT_SCAN.md:79–101`, `CONTINUOUS_THEOREMS.md:116–125` |

**Scope notes for A.**

- **#543 `CONTINUOUS_THEOREMS.md:43`.** It says the forward window "matches #542's sign
  convention". That holds for #542's *finite* `R_{L,k}` windows only. #542's continuous
  surfaces (`TWO_TONE_STABLE_ARC.md:85`, `REALIZATION_AND_DYNAMIC_YONEDA.md:93`) are
  backward convolutions with `G_a(r)=conj(a_r)`. The inverse `𝒜_α` and the coherence
  relation `a_h f̂₁=a_{h−1}f̂₀` transfer only after conjugation.
- **#543 symbol collisions.** `A_α` means two things (`CONTINUOUS:198` vs `LOCKIN:222`).
  So does `C_b(α)` vs `C_α(d)`. `a_h` is a scalar in CONTINUOUS and a vector in LOCKIN.
- **#542 `RESEARCH_NOTE.md:197`.** "at fixed nonzero h" should read "for every fixed
  nonzero h".
- **#542 `ANCHORED_PATHS_VS_HOLONOMY.md:55`.** The constant `2√d/a` needs Minkowski on
  the two-channel pair; a plain triangle inequality gives `2√2·√d/a`. The bound is true.
- **#542 tests.**
  - `tests/test_pinbed_oscillator_bridge.py:169` (`assertEqual(1*1-2*2,-3)`) runs no
    module code. It is a **paper-only control**, not the executed countermodel that
    `VALIDATION_FOLLOWUP.md:21` describes.
  - `tests/test_learning_pinbed.py:91` echoes arithmetic. The real witness is the 256
    distinct transcripts at line 89.
- **#542 validation counts.** The counts "26", "49/49" and "59/59" include an external
  bundle that is not in this repository. Only 10+11 of those tests are in main.
- **#541 `tests/test_fourier_yoneda_pinbed.py:171`.** It re-asserts the paper constant
  `1/(2700A⁴)`.
- **Coverage gaps (killed mutants).** The adversary demonstrated five wrong
  implementations that all pass the 84 original pin-bed tests:
  - the translation-bound tail term deleted;
  - the learner noise margin inflated 1.9×, under which `guarded_pin(5,1,0,3/64)` returns
    `6`;
  - the alias bound `6h²/M²` replaced by a linear one, because it was tested only at
    `(4,1)`;
  - the bridge energy bound divided by 1000;
  - `choose_mode` replaced by "take the first entry".

  `tests/test_main_xxi_pinbed_hardening.py` was added at integration. Each new test
  compares a bound against an independently computed true quantity at its tightest point,
  so each of these mutants now fails. **No mathematical claim was refuted.**
- **Learning does not imply normality.** Replacing the forcing with zero, a maximally
  non-normal source, leaves the learner's behaviour unchanged. The docstring phrase "for
  SUCC's unchanged four-pole BBP" therefore describes the test fixture, not a
  dependency.

## B. Adelic, return and Fejér/golden chain (#525→#528, then #529→#534→#535 and #530→#531→{#532, #533→#536→#538→#540})

| ID | Claim | Status | Source / receipt |
|---|---|---|---|
| MXXI-08 | Completion identity (`T₀=π/16`). `0<r(n)<1/n²` for `n≥2`. Base 16 ⇔ base 2 (classical). Staircase and `β=1/5` countermodels. | PROVED LOCAL / CLASSICAL | #525 `realization_gyroscope/` |
| MXXI-09 | J9: a finite entropy-deficit → joint-Weyl inequality, with exact TV `ε=(L−k)/(N−k+1)`. J15 and J18/J19. Six certified `\|J_A(h)\|` intervals, reproduced at 1400 digits. The J20 premise is OPEN. | PROVED LOCAL (criterion) / CERTIFIED FINITE | #526 `joint_character_entropy/THEOREMS.md:100–119, 201–210`. **Scope note:** `σ_n` at `:140,:144` and `CLAIM_LEDGER.md:10` is the *index-only* period-7 clock `(n+1) mod 7`, not a source-derived pole clock (its own `SOURCE_CLOCK_AUDIT.md:7`). |
| MXXI-10 | The original BBP 2-adic zero `V(0)=0`, the isometry, and DB10. DB-06/DB-07: the 2-adic zero plus 2-adic Haar do not force real Haar, and do not fingerprint the source. | PROVED LOCAL (independent **rederivation** of main's 2026-10-27 binwindow zero boundary) / countermodels | #527 `padic_boundary/`. **Scope note (provenance):** prior art is `research/2026-10-27/BBP_BINWINDOW_ZERO_BOUNDARY.md:90ff`, `observational_succ/bbp_binwindow_conjugacy.py` and `bbp_two_adic.py`. New here: DB10 packaging and DB-06/DB-07. |
| MXXI-11 | RS8: the state-only 2-adic decoder has a floor of `1/34`. RS-06: no odometer→×16 Haar factor exists. RS6–RS8 use only irrationality, so they hold for **every** irrational `β`. | PROVED LOCAL / CLASSICAL | #528 `adelic_return_bridge/THEOREMS.md:103–125` |
| MXXI-12 | Adelic CRT (AT1/AT2). Birth table (AT3; already present as `observational_succ/bbp_cyclotomic_birth.py:21–26`). Subgroup Gauss bound (AT5). AT6/AT7. AT10. AT9: closed form of `Σr(n)` by digamma. | PROVED LOCAL / CLASSICAL | #529 `odd_place_triangle/THEOREMS.md`. **Scope note:** ledger AT-04…AT-06 ≠ THEOREMS AT-04/AT-05. Read by THEOREMS ids. |
| MXXI-13 | **log of the reduced denominator is linear:** `5 ≤ liminf log d_n/n ≤ limsup log d_n/n ≤ 8`, where `d_n` is the odd reduced denominator of `U_n` (PF7 / ledger PF-04; unconditional PNT and PNT in progressions). The exact sweep `n=8..300` violates the prime band only at the declared exception `p=19, n=10..16`. PF9: Galois-orbit Haar. | PROVED LOCAL (classical inputs; **not zero-seed selective**: persists for any fixed rational seed) | #532 `prime_frobenius_spectral/THEOREMS.md:13–154`. Its `FAILED_SCRATCH.md:5` refutes "denominator growth + Galois Haar ⇒ real Haar". |
| MXXI-14 | HT14: `max_{n<N} d_n > N` for `N≥6`. HT18: `v_p(U_n)=−1` iff `p≡1 (mod 4)` for `4n<p≤8n−7`. HT20: `liminf log d_n/n ≥ 2`. **HT20 is superseded by MXXI-13's `≥5` on the same `d_n`.** | PROVED LOCAL (+Bertrand, PNT-AP) | #534 `holographic_triangle/THEOREMS.md:167–239`. **Scope notes:** AGENTS.md rule 3 — "physically admissible plane" (`:45`, `:66`, `CLAIM_LEDGER.md:15`) is the *definitional* seam `U=C+x`, and HT4 reads `R=A`. "Gamma/harmonic source functor" (`:262`) is the exact digamma partial-sum identity. `independent_run.sh` calls a `receipt.py` that never existed and, under `set -eu`, truncates the tracked receipt. **Do not run it.** The committed receipt is internally consistent (17 sha256 pins match). |
| MXXI-15 | FG10/FG11: at fixed `N`, return energy is monotone nondecreasing under dyadic refinement (`1 = global + between + within`). This refutes contraction-by-refinement. FG2–FG17 hold. | PROVED LOCAL / REFUTED strategy | #535 `fejer_gamma_split/THEOREMS.md:133–147`. **Scope note:** `:136` "Q from 1 to N" should read "Q from 1 to 2^K". |
| MXXI-16 | TS5/TS10 closed forms (agree to 40 digits; exact numerator identity). TS-09 signs certified. | PROVED LOCAL / CERTIFIED FINITE | #530 `triangle_signed_return/`. **Scope note:** TS-09…TS-11 are used twice in `CLAIM_LEDGER.md` (`:14–16` vs `:33–36`). Read the second table as TS-13…TS-16. |
| MXXI-17 | IT1: averaged return gluing. IT3/IT5 are conditional. Source-selected Poisson contraction is OPEN. | PROVED LOCAL / PROVED-CONDITIONAL | #531 `infinity_thread/` |
| MXXI-18 | SE4: energy transport `O(H²/N)`. SE3 is conditional. | PROVED LOCAL / PROVED-CONDITIONAL | #533 `spectral_exorcism/` |
| MXXI-19 | CC1: √-transport `≤4√(H(H+1))/N` on prefixes. CC3: the frequency-ray bound (`\|W_512^x(1)\|<0.902184`, recomputed 0.9021831). CC4/CC8 gluing. K3 all-radius certificates to `N=4096` (`K=2.7` chosen post hoc, flagged). | PROVED LOCAL / CERTIFIED FINITE | #536 `critical_collision/` |
| MXXI-20 | ET1, on the original orbit, for all `A,H≥1`: `\|√C^z_{A,H} − √C^x_{A,H}\| ≤ (π/(15A²))√(H(H+1)(H+2)/6)`, i.e. **transport error `O(A^{−1/2})` at `H=A`, not `o(1)` for the gate**. ET2b holds. | PROVED LOCAL ORIGINAL SOURCE | #538 `epoch_critical_transfer/THEOREMS.md`. **Scope notes:** the PR title "transport o(1)" should read "transport error `O(A^{−1/2})`". `:81` should read "as `A→∞` through all integers `A`". |
| MXXI-21 | ET3: `C^x_{A,A}=o(\log A)` along all `A`, or along `A_j` with `A_{j+1}/A_j→1`, implies normality. ET4a: all-radius `K`-anticlustering implies `C^x_{A,A} ≤ 2K+4(A+1)/(3A)`. ET5: `K≤3` at `A=191,319` over all real radii. | PROVED-CONDITIONAL (premises OPEN) / CERTIFIED FINITE | #538 |
| MXXI-22 | Golden aperture identities GA1–GA3 and GA6–GA9 (for every probability measure). GA4: π normal ⇔ `E_a(μ_A^x)→0`. | PROVED LOCAL / EQUIVALENT-REFORMULATION (limit OPEN) | #540 `golden_aperture_fejer/THEOREMS.md` |
| MXXI-23 | GA5/GA10: fixed-aperture **unsquared** energy transport `\|E_a(μ^z)−E_a(μ^x)\| ≤ 1/(15bA²)`, uniform over dyadic fibers `Q\|A`. This is not a decay rate for `E`. GA11 is conditional. Certificates at `A=79,157,1024,2048` were recomputed independently. | PROVED LOCAL ORIGINAL SOURCE / CERTIFIED FINITE | #540. **Scope note:** ledger GA-09 collides with THEOREMS §GA-09, which is ledger GA-12. |
| MXXI-24 | **GA-09** — "K=3 anti-clustering ⇒ `E_a→0`" — is **REFUTED, with the receipt supplied at integration**. The uniform `A`-point grid on an arc of length `2/3` has `B_A(t)≤A+3A²t` for all `t∈[0,½]`, yet `E_a→√5/9−1/6≈0.08179>0`. | REFUTED (receipt R1) | [`research/2026-11-07/main_xxi_receipts/`](../research/2026-11-07/main_xxi_receipts/README.md) |
| MXXI-25 | #540 `A=4096` golden interval: `E ∈ [0.00015731538591, 0.00015731538592]`, pair count 12817828. It was computed at integration with the documented `--include-4096` in 46.6 s. The dossier says TIMEOUT / NOT COMPUTED, which is stale for this machine. | TESTED MODEL (OBSERVED-FINITE; integration-time run, not a committed receipt) | integration audit §5 |

## C. Independent Pisot leaves (#537, #539)

| ID | Claim | Status | Source / receipt |
|---|---|---|---|
| MXXI-26 | QR-01…QR-06: `O_K=ℤ[φ]`, the Galois action, the Frobenius `φᵖ` mod `p` (by `χ₅(p)`), `ζ_K=ζ·L(χ₅)`, root number `+1`, and the harmonic–Lucas expansion. QR-07 is a real firewall: killing the odd test sector does not remove `L(s,χ₅)`, and it implies no Weil positivity. QR-08/QR-09 are OPEN. | PROVED CLASSICAL (QR-05: imported) / PROVED LOCAL; RH OPEN | #537 `quadratic_galois_tate_bridge/`. **Scope notes:** README `:11` should add "modulo p". RESEARCH `:66` is an exact involution. `test_local_euler_artin_polynomials` is a table check. NEXT §A mutants are unpaid. |
| MXXI-27 | HPB-01…HPB-05 (harmonic–Pisot boundary). HPB-04: `Σ‖t_n‖²/n<∞` forces the mean of `e(t_n)` to 1. C2–C5 golden aperture. | PROVED LOCAL / PROVED CLASSICAL | #539 `harmonic_pisot_boundary/`. **Scope notes:** "anti-normality theorem" covers finite weighted square-distance energy only; it is elementary for Pisot `αⁿ` and does **not** transfer to the BBP orbit. "Uniquely self-calibrating" aperture means unique only under the declared normalization `C=L`. `L(1,χ₅)` "is equivalent to", not "sets", the rate. |
| MXXI-28 | `B_crit = Q_∞ − γ = 2.47730946056315501453` (`γ` is Euler–Mascheroni; depends on the counterterm). For `B=2.45`, the first nonpositive margin is at `N=19`. | TESTED MODEL (OBSERVED; independently recomputed at 400 digits; not interval-certified) | #539 |
| MXXI-29 | The CIRCLE_WINDOW statement "π normal ⟺ `E_{π/φ}(μ_A)→0`" re-expresses the `Q_{1/2}` gate. | PROVED LOCAL (EQUIVALENT-REFORMULATION; not progress) | #539 `CIRCLE_WINDOW.md` |

## D. Open

| ID | Claim | Status | Source / receipt |
|---|---|---|---|
| MXXI-30 | Source-selected decay of any of these: the combined time-return Fejér × golden spatial witness (#535 × #540), the critical Fejér energy `C^x_{A,A}=o(\log A)` (ET3), or Main XX's (LS)/(H2\*). Any valid proof must **fail** on the coherent counterseed `s_*=−π/16`, on the CB-3 same-forcing seeds, and on the GA-09 receipt configuration. | HYPOTHESIS (OPEN) | [`docs/PI_NORMALITY_FRONTIER.md`](PI_NORMALITY_FRONTIER.md) §6 |
