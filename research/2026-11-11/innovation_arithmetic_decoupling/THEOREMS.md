# Innovation × arithmetic decoupling — theorems

**Baseline:** Main XXIV `071ce1e0ee6ab8f8c07113e901131aa646d6b95d`. Additive research dossier on a
non-main branch. **π base-16 normality, the source-selected signed estimate, original-zero parity
balance and RH remain OPEN.** Nothing here is a proof of normality, and no status is promoted on
finite evidence.

**Status labels.** `PROVED LOCAL` = complete elementary proof in this file (same-model authorship;
not external refereeing, not Lean). `CLASSICAL IMPORT` = cited published theorem, used as stated.
`OBSERVED FINITE` = exact or interval-certified finite computation (see [PROBES](PROBES.md)).
`OPEN` = unproved. Claim IDs `IAD-nn`; the Scott-side statements are `SWT-nn` in
[SCOTT_TRANSPORT.md](SCOTT_TRANSPORT.md).

## 0. Source contract and notation

For integer `n ≥ 1` (and real `t > 7/8` where indicated):

```text
r(n) = 4/(8n-7) - 2/(8n-4) - 1/(8n-3) - 1/(8n-2)
U_0 = 0,  U_n = 16 U_(n-1) + r(n)
T_n = Σ_(j≥1) 16^(-j) r(n+j)
Y_n = U_n + T_n = 16^n x,   x = π/16          (classical BBP import)
```

`e(t) = exp(2πi t)`, `‖t‖` = distance to the nearest integer, `h` a nonzero integer (WLOG `h ≥ 1`
by conjugation). For a seed `s` in the declared module `Q + Qx`:
`U_n(s) = 16^n s + U_n(0)`, `Y_n(s) = U_n(s) + T_n = 16^n (x + s)`. The forcing, `T_n` and all
innovations below are **seed-independent**.

Shell means use `n ∈ [B, 2B)`. The handoff's Basel weights are `p_n = n^(-2)/ω_B`,
`ω_B = Σ_(n=B)^(2B-1) n^(-2)`, `v_n = p_n e(hY_n)` (zero outside the shell), so
`Σ_n v_n = B_B(h)`.

**Positive moment representation (source-attested).** With

```text
g(z) = 4 - 2z³ - z⁴ - z⁵ = (1-z)(z²+2)(z²+2z+2),      4(1-z) ≤ g(z) ≤ 15(1-z) on [0,1],
```

termwise integration gives, for real `t > 7/8`,

```text
r(t) = ∫_0^1 z^(8t-8) g(z) dz,
T_n  = ∫_0^1 z^(8n) G(z) dz,   G(z) = g(z)/(16 - z⁸) = (1-z)/((2-z²)(z²-2z+2)).
```

(`16 - z⁸ = (2-z²)(2+z²)(z²+2z+2)(z²-2z+2)`; `G` is the classical BBP integrand, `T_0 = x`.)
The bracket for `g` holds because `(z²+2)(z²+2z+2)` increases from 4 to 15 on `[0,1]`.

---

## IAD-01 — the weighted lag identity of Main XXIV §4 (PROVED LOCAL; verification of an existing identity)

For `1 ≤ L ≤ B` put `V_L(m) = Σ_(j=0)^(L-1) v_(m+j)`, `E_L = Σ_(m∈Z) |V_L(m)|²`, `S = Σ_n |v_n|²`,
`σ_B = B·S`, and the **normalized window energy** `γ_L = E_L/(L² S) ∈ [0, 1]`. Then

```text
R_(B,L,h) = (B/L) [ E_L/L - S ] = σ_B ( γ_L - 1/L ).                         (1.1)
```

*Proof.* Expanding the square, each diagonal term occurs `L` times and each lag `ℓ` occurs `L-ℓ`
times: `E_L = L·S + 2 Σ_(ℓ=1)^(L-1) (L-ℓ) Re Σ_n v_(n+ℓ) conj(v_n)`. Divide by `L`, subtract `S`,
multiply by `B/L`, and use `v_(n+ℓ) conj(v_n) = p_n p_(n+ℓ) e(h(Y_(n+ℓ)-Y_n))` with
`Y_(n+ℓ) - Y_n = (16^ℓ-1) Y_n`. The lag sum runs over `B ≤ n ≤ 2B-1-ℓ` because `v` vanishes off the
shell. ∎

Checked points (normalization, padding, support, endpoints, signs):

- `1/(2B) ≤ ω_B`, hence `max p_n = p_B ≤ 2/B`, `S ≤ max p_n ≤ 2/B`, `σ_B ≤ 2`; also `σ_B ≥ 1` by Cauchy–Schwarz (`1 = (Σp_n)² ≤ B·S`), and `σ_B → 7/6`.
- `V_L(m) ≠ 0` only for `B-L+1 ≤ m ≤ 2B-1`: `B+L-1` values. Cauchy–Schwarz on
  `L·Σ_n v_n = Σ_m V_L(m)` gives `L²|B_B(h)|² ≤ (B+L-1) E_L`, so with (1.1)

  ```text
  |B_B(h)|² ≤ ((B+L-1)/L) S + ((B+L-1)/B) R  ≤  4/L + 2 max(R_(B,L,h), 0).      (1.2)
  ```

- Trivial range: `0 ≤ γ_L ≤ 1` gives `-σ_B/L ≤ R_(B,L,h) ≤ σ_B(1 - 1/L)`.
- **First informative scale of the prescribed schedule.** For the *coarse* form
  `4/L + 2R⁺` of (1.2), `4/L < 1` needs `L ≥ 5`; for `L(B) = ⌊½ log_16 B⌋` that is
  `B ≥ 16^10 ≈ 1.1·10^12`, and below that scale the coarse form cannot beat `|B_B(h)| ≤ 1`
  whatever `R` is. This threshold is an artefact of the constant 4: the *sharp* middle form of
  (1.2) has leading term `((B+L-1)/L)·S ≈ σ_B/L ≈ 7/(6L)`, which is below 1 already at `L = 2`,
  i.e. from `B ≥ 16^4` on that schedule. (Correction after audit: an earlier draft attributed the
  `16^10` threshold to (1.2) itself.)

The identity is retained as a **conditional proof interface**. No source-derived estimate of `R`
exists; IAD-02 shows that none can be obtained merely by choosing the schedule.

## IAD-02 — schedule-freeness: every Fejér schedule is the same normality restatement (PROVED LOCAL; the converse direction imports the repository's Basel–Tauberian bound and Weyl's criterion)

**Lemma (window-energy monotonicity).** For any complex sequence `v` of finite support and all
integers `1 ≤ J ≤ L`:

```text
√γ_L ≤ √γ_J + J/L,            and   γ_L ≤ γ_J  whenever J | L.                 (2.1)
```

*Proof.* Write `L = kJ + ρ`, `0 ≤ ρ < J`. Then `V_L(m) = Σ_(i<k) V_J(m+iJ) + V_ρ(m+kJ)`. In `ℓ²(Z)`,
translation is isometric, so `√E_L ≤ k√E_J + √E_ρ`, and `E_ρ ≤ ρ² S` by Cauchy–Schwarz. Divide by
`L√S` and use `kJ ≤ L`, `ρ < J`. For `ρ = 0` the second term is absent. ∎

**Theorem.** Fix `h ≠ 0`. Suppose that for every fixed `ℓ ≥ 1` the Cesàro means
`N^(-1) Σ_(n<N) e(h(16^ℓ-1)Y_n)` tend to 0 (true for all `ℓ` if `x` is base-16 normal; equivalent
to the shell means tending to 0, by dyadic decomposition). Then for **every**
integer schedule `L(B) → ∞`:

```text
R_(B,L(B),h) → 0,   quantitatively   R_(B,L,h) ≤ σ_B [ ( √(1/J + R⁺_(B,J,h)/σ_B) + J/L )² - 1/L ]   (2.2)
```

for all `1 ≤ J ≤ L`. Consequently, for every schedule `L(B) → ∞`, `L(B) ≤ B`:

```text
[ ∀h≠0 :  max(R_(B,L(B),h), 0) → 0 ]   ⟺   π is normal in base 16.
```

*Proof.* (2.2) is (2.1) with `γ = 1/L + R/σ_B`. For fixed `J`, `R_(B,J,h)` is a fixed finite
combination of weighted lag sums at the fixed nonzero modes `h(16^ℓ-1)`, `ℓ < J`; the weights
`p_n p_(n+ℓ)` are positive, decreasing and `O(B^(-2))`, and the hypothesis gives partial sums
`Σ_(B≤n<N') e(h(16^ℓ-1)Y_n) = o(B)` uniformly in `B ≤ N' ≤ 2B`; Abel summation gives
`R_(B,J,h) → 0`. Hence `limsup_B γ_(L(B)) ≤ 1/J` for every `J`, so `γ_(L(B)) → 0` and
`R = σ_B(γ - 1/L) → 0` (using `1 ≤ σ_B ≤ 2`). The converse direction is (1.2) plus the existing
Basel–Tauberian and Weyl equivalences (imports). ∎

*Per single mode this is a chain, not an equivalence:* decay of the Weyl sums at the modes
`h(16^ℓ-1)`, `ℓ ≥ 1`, gives `R_(B,L(B),h) → 0` for every schedule, which gives `B_B(h) → 0`. The
equivalence with normality is for all modes together.

**Consequences for Phase 1 of the mission.**

1. *Why unrestricted existence of a slowly growing `L(B)` only recasts normality:* the displayed
   equivalence. It holds for the signed quantity `R`, not only for some diagonal schedule.
2. *Does the prescribed `L(B) = ⌊½ log_16 B⌋` demand stronger frequency uniformity?* **No — this
   suspicion is refuted for the signed Fejér functional.** The window energy is antitone in
   the window length along divisibility, and up to the additive `J/L` in general (2.1), so normality
   pays every schedule at once, including `L(B) = B`. Uniformity
   over the growing frequency set `h(16^ℓ-1)`, `ℓ < L(B)`, *would* be demanded by a term-by-term or
   absolute-value version (`Σ_ℓ (1-ℓ/L)|c_ℓ|`), which is a different statement that this
   argument does not deliver (whether it is strictly stronger is not decided here). The Fejér sum never needs it because it is a positive quadratic form.
3. *What the schedule does control* is only the **rate** in (1.2): `|B_B(h)|² ≤ 4/L + 2R⁺` can
   never certify better than `4/L(B)`.
4. *Relation to SP-01* (`arithmetic_barrier/SPECTRAL_AND_SELECTION.md`): SP-01 trades the mode `h`
   for the modes `h(16^d-1)` at fixed `d` and records NON-IMPROVEMENT. IAD-02 closes the remaining
   loophole in that verdict: letting the lag window grow by any schedule adds no content either.
   The coherent seed `s = -x` has `γ_L = 1 - O(L/B)` and `R ≈ σ_B(1 - 1/L)`, the maximum.

Probes for a finite shell should therefore use a larger window (e.g. `L ≈ √B`), which is
informative already at `B ≥ 25`; nothing is lost.

---

## IAD-03 — innovation calculus (PROVED LOCAL)

Define the temporal innovation `Δ_ℓ(n) = U_(n+ℓ) - 16^ℓ U_n = Σ_(j=1)^ℓ 16^(ℓ-j) r(n+j)`.

**(a) Tail form and exact cancellation in the completed orbit.**

```text
Δ_ℓ(n) = 16^ℓ T_n - T_(n+ℓ),          Y_(n+ℓ) - 16^ℓ Y_n = 0.
```

*Proof.* `16^ℓ T_n = Σ_(j≥1) 16^(ℓ-j) r(n+j)`; the terms `j ≤ ℓ` are `Δ_ℓ(n)` and the terms
`j = ℓ+i` are `Σ_i 16^(-i) r(n+ℓ+i) = T_(n+ℓ)`. The second identity is `Y = U + T`. ∎

The rational innovation is cancelled **exactly** by transported future tails; it is not a forcing
term of `Y`. This is LL-02 of `gaussian_circle_long_lag/LONG_LAG.md` in one-index form:
`D_(n,k) = U_(n+k) - U_n = (16^k-1) U_n + Δ_k(n)` and `E_(n,k) = D_(n,k) + T_(n+k) - T_n =
(16^k-1) Y_n`. Integral form: `Δ_ℓ(n) = ∫_0^1 z^(8n) g(z) (16^ℓ - z^(8ℓ))/(16 - z⁸) dz`.

**(b) Size and derivative bounds.** With `s = 8t - 8 ≥ 0`, the bracket `4(1-z) ≤ g ≤ 15(1-z)` and
`∫_0^1 z^s (1-z) dz = 1/((s+1)(s+2))`, `∫_0^1 z^s ln(1/z)(1-z) dz = (2s+3)/((s+1)²(s+2)²)`:

```text
4/((8t-7)(8t-6))  ≤   r(t)  ≤ 15/((8t-7)(8t-6)),                       t ≥ 1
32(16t-13)/((8t-7)²(8t-6)²) ≤ -r'(t) ≤ 120(16t-13)/((8t-7)²(8t-6)²),   t ≥ 1
r''(t) = 64 ∫_0^1 z^(8t-8) ln²(1/z) g(z) dz > 0.
```

`r` is completely monotone. Asymptotically `r(t) ~ 15/(64t²)` and `-r'(t) ~ 15/(32t³)` (the upper
brackets are sharp because `g(z) ~ 15(1-z)` at `z = 1`; directly, the pole coefficients sum to
`4-2-1-1 = 0` and `(4·7 - 2·4 - 3 - 2)/64 = 15/64`). In particular the candidate bounds of the
mission hold with room:

```text
1/(16t³) ≤ -r'(t) ≤ 4/t³     (t ≥ 2),          0 < T_n ≤ r(n+1)/15 ≤ 1/((8n+1)(8n+2)) < 1/(64n²).
```

*Proof of the last line.* Lower: `(8t-7)(8t-6) ≤ 64t²` and `16t-13 ≥ 8t` for `t ≥ 13/8`. Upper: for
`t ≥ 2`, `8t-7 ≥ (9/16)·8t` and `8t-6 ≥ (10/16)·8t`, so `-r'(t) ≤ 1920t/(506.25 t⁴) < 4/t³`. The
tail bound uses `r` decreasing and `Σ_(j≥1)16^(-j) = 1/15`. ∎

**(c) Discrete steps.** `δ(m) = r(m) - r(m+1) = ∫_m^(m+1) (-r')` is positive and strictly
decreasing in `m`, with `1/(16(m+1)³) ≤ δ(m) ≤ 4/m³` for `m ≥ 2`. Hence the innovation step

```text
Δ_ℓ(n) - Δ_ℓ(n+1) = Σ_(j=1)^ℓ 16^(ℓ-j) δ(n+j)
```

is positive, strictly decreasing in `n`, and lies in
`[16^(ℓ-1) δ(n+1), (16/15)·16^(ℓ-1) δ(n+1)]`.

## IAD-04 — the mesoscopic innovation theorem (PROVED LOCAL)

**Kusmin–Landau, discrete form with the sharp constant.** Let `f` be real on integers `a..b` and
`g(n) = f(n+1) - f(n)`. If `g` is monotone and, for one integer `k`, `k+λ ≤ g(n) ≤ k+1-λ` for all
`a ≤ n < b` with `0 < λ ≤ 1/2`, then `|Σ_(n=a)^b e(f(n))| ≤ cot(πλ/2) ≤ 2/(πλ)`.

*Proof.* Replace `f(n)` by `f(n) - kn`; so `k = 0`. With `C_n = 1/(e(g(n)) - 1) = -1/2 -
(i/2) cot(πg(n))` we have `e(f(n)) = C_n (e(f(n+1)) - e(f(n)))`. Summation by parts gives
`Σ_(n=a)^b e(f(n)) = e(f(b))(1 + C_(b-1)) - e(f(a)) C_a + Σ_(n=a+1)^(b-1) e(f(n)) (C_(n-1) - C_n)`.
Since `cot(πg)` is monotone along the sum, `Σ |C_(n-1) - C_n| = ½|cot πg(a) - cot πg(b-1)|`, and
`|C_n| = |1 + C_n| = 1/(2 sin πg(n))`. With all `g(n) ∈ [λ, 1-λ]` the total is at most
`1/sin(πλ) + cot(πλ) = cot(πλ/2)`. ∎

(This is the classical Kusmin–Landau inequality; only the discrete monotone-step hypothesis is
used, so no real-variable derivative is needed. The standard continuous statement is a
CLASSICAL IMPORT cross-check, see [SOURCE_MAP](SOURCE_MAP.md).)

**Theorem (mesoscopic window).** Let `h ≥ 1`, `B ≥ 1`, `ℓ ≥ 1` with `h·16^ℓ ≤ (15/8) B³`. Put
`λ = h·16^(ℓ-2)/(2B+1)³`. Then for **every** integer interval `I ⊂ [B, 2B-1-ℓ]`:

```text
| Σ_(n∈I) e(h Δ_ℓ(n)) |  ≤  cot(πλ/2)  ≤  512 (2B+1)³/(π h 16^ℓ)  <  4401 · B³/(h·16^ℓ).     (4.1)
```

In particular, for `0 < δ < 1/2`, `B^δ ≥ h`, and every lag in the window
`(2+δ) log_16 B ≤ ℓ ≤ (3-δ) log_16 B`:

```text
(1/B) | Σ_(n∈I) e(h Δ_ℓ(n)) |  ≤  4401 · h^(-1) · B^(-δ),    uniformly in the subinterval I.   (4.2)
```

*Proof.* Take `f(n) = -hΔ_ℓ(n)`, so `g(n) = h(Δ_ℓ(n) - Δ_ℓ(n+1)) > 0` is strictly decreasing
(IAD-03c). For `B ≤ n < 2B-1-ℓ`: `g(n) ≥ h·16^(ℓ-1) δ(n+1) ≥ h·16^(ℓ-1)/(16(n+2)³) ≥ λ` and
`g(n) ≤ (16/15) h·16^(ℓ-1)·4/(n+1)³ ≤ (4/15) h·16^ℓ/B³ ≤ 1/2 ≤ 1-λ`. Apply Kusmin–Landau with
`k = 0`; `(2B+1)³ ≤ 27B³`. For (4.2), `16^ℓ ≥ B^(2+δ)` gives the bound and `16^ℓ ≤ B^(3-δ)` with
`B^δ ≥ h` gives the hypothesis. ∎

**Corollaries.**

- *(weights)* For monotone weights `w_n ≥ 0` on the shell, Abel summation and the uniformity in `I`
  give `|Σ w_n e(hΔ_ℓ(n))| ≤ (max w)·cot(πλ/2)`.
- *(arithmetic progressions: a genuine conditional expectation)* For a modulus `q ≥ 1` with
  `q·h·16^ℓ ≤ (15/8)B³` and any residue `a`, the same proof applied to `n ↦ f(a+qn)` (step
  `g_q ∈ [qλ, 1/2]`, still monotone) gives `|Σ_(n∈I, n≡a (q)) e(hΔ_ℓ(n))| ≤ cot(πqλ/2) ≤ 2/(πqλ)`.
  Let `ℓ < B`, take uniform counting measure on the `B-ℓ` times `n ∈ [B, 2B-1-ℓ]` and the
  clock-residue filtration `F_q = σ(n mod q)`. **Occupied-cell condition: `1 ≤ q ≤ B-ℓ`.** Then
  every residue cell contains at least `⌊(B-ℓ)/q⌋ ≥ 1` times, `⌊y⌋ ≥ y/2` for `y ≥ 1`, and

  ```text
  ‖ E[ Z_(·,ℓ,h) | F_q ] ‖_∞  ≤  cot(πqλ/2)/⌊(B-ℓ)/q⌋  ≤  4/(πλ(B-ℓ))  ≤  8802·B²/((1-ℓ/B) h 16^ℓ).
  ```

  *(Repaired 2026-11-11, second audit.)* The earlier display,
  `(q/(B-ℓ-q))·2/(πqλ) ≤ 4401·B²/((1-(ℓ+q)/B) h 16^ℓ)`, was stated without the occupied-cell
  condition and is **false as written**: `B = 100, ℓ = 1, h = 1, q = 1000` satisfies
  `q·h·16^ℓ ≤ (15/8)B³`, yet every cell holds at most one time, so the left side is `|Z| = 1` while
  the right side is negative. It is correct for `q < B-ℓ` only. The repaired form needs
  `q ≤ B-ℓ`, loses a factor 2 in the constant, and has no `q` in the denominator. For `q > B-ℓ`
  some cells are empty, the occupied ones are singletons, and no saving exists. The regression is
  `test_iad04_progression_occupied_cells` in `test_zsc.py`.

  This is a nontrivial, explicitly bounded conditional innovation law relative to a chosen measure
  and filtration for a fully deterministic sequence. Deterministic dynamics do not obstruct
  conditional expectations; what is missing is a useful conditional law for the *history* factor
  (IAD-05).
- *(asymptotic constant)* Since `δ(m) ~ 15/(32m³)`, the true size of (4.1) is
  `≈ (2/π)·256·B³/(h16^ℓ)` at the top of the shell; 4401 is a safe non-asymptotic constant.

**Complementary obstruction (no innovation-only saving below `2 log_16 B`).** For all `n ≥ B`,
`0 < Δ_ℓ(n) ≤ 16^ℓ r(n+1)/15 < 16^ℓ/(64B²)`, hence

```text
| e(hΔ_ℓ(n)) - 1 | ≤ (π/32) · h · 16^ℓ / B².                                   (4.3)
```

So for `ℓ ≤ ½ log_16 B` the innovation phase is within `(π/32)hB^(-3/2)` of 1, and more sharply
the shell mean of `Z` is `1 - O(h16^(-K))` for every `ℓ ≤ 2 log_16 B - K`. Innovation-only
cancellation starts exactly at `16^ℓ ≍ B²/h`.

**The age ladder (sizes PROVED LOCAL; resonance reading is interpretation).** From the integral
form of IAD-03a, the `k`-th forward difference in `n` of `Δ_ℓ(n)` is
`∫_0^1 z^(8n) (z⁸-1)^k g(z) (16^ℓ - z^(8ℓ))/(16 - z⁸) dz`. It has sign `(-1)^k`, and since
`16^(ℓ-1) ≤ (16^ℓ - z^(8ℓ))/(16 - z⁸) ≤ 16^ℓ/15` on `[0,1]` and
`∫_0^1 z^(8n)(1-z⁸)^k(1-z) dz ≍_k n^(-(k+2))`, its size is `≍_k 16^ℓ/n^(k+2)`. So the phase
`hΔ_ℓ(n)` itself exceeds 1 from `ℓ ≈ 2 log_16 B`, its first difference from `3 log_16 B`, its
second difference from `4 log_16 B`, and so on. Beyond `3 log_16 B` the step `g` is still
decreasing and passes `≍ h16^ℓ/B³` integers across the shell (its total variation there), so the
Kusmin–Landau hypothesis fails; reading each passage as a stationary-phase resonance is the
standard heuristic, not a statement proved here. A *single* pole term `c·16^k/(8m-a)` exceeds 1
already at age `k ≈ log_16 B`: the gap between `1·log_16 B` and `2·log_16 B` is paid by the
four-pole cancellation `4-2-1-1 = 0`, which is purely Archimedean (IAD-09d).

**Beyond the first-derivative window (CLASSICAL IMPORT, not re-proved here).** The real-variable
phase `φ(t) = h Σ_(j=1)^ℓ 16^(ℓ-j) r(t+j)` has every derivative of constant sign with
`|φ^(k)(t)| ≍_k h·16^ℓ/t^(k+2)` on `[B, 2B]` (complete monotonicity of `r`). Van der Corput's
`k`-th derivative test therefore applies: the derivative of order `q+2` gives a power saving for
`B^(q+2^(1-q)+ε) ≤ 16^ℓ ≤ B^(q+4-ε)`, and the union over `q = 0, 1, …, K` covers
`(2+δ) log_16 B ≤ ℓ ≤ K log_16 B` with a saving `B^(-c(K,δ))`, `c > 0`. This is recorded as an
import with OBSERVED FINITE support only; the load-bearing theorem of this dossier is (4.2). For
`ℓ ≫ (log B)^(3/2)` no smooth method is known to this dossier to apply, and for `ℓ ≍ B` the
innovation sum is as hard as the original problem, since
`hΔ_ℓ(n) ≡ h(U_(n+ℓ) - 16^ℓ U_n) (mod 1)`.

**Scope.** (4.2) is an **untwisted, seed-independent** estimate about the forcing alone. It holds
verbatim for the coherent seed `s = -x`, the shadow seeds and every rational seed. It does not
prove, and cannot by itself prove, any statement about π.

---

## IAD-05 — the gauge theorem: the history factor contains the conjugate innovation (PROVED LOCAL)

For a seed `s` in the module, a lag `ℓ ≥ 1` and `n ≥ 1` define

```text
A_n = e(h(16^ℓ-1) U_n(s)),   Z_n = e(hΔ_ℓ(n)),   C_n = e(h(16^ℓ-1) Y_n(s)) = e(h(Y_(n+ℓ)(s) - Y_n(s))),
τ_n = T_(n+ℓ) - T_n ∈ (-T_n, 0).
```

**Theorem (exact gauge identity).**

```text
A_n Z_n = e(h(U_(n+ℓ)(s) - U_n(s))) = C_n · e(-hτ_n),          A_n = C_n · conj(Z_n) · e(-hτ_n).   (5.1)
```

*Proof.* `U_n(s) = Y_n(s) - T_n`, so `A_n = C_n e(-h(16^ℓ-1)T_n)`, and by IAD-03a
`Z_n e(-h(16^ℓ-1)T_n) = e(h(T_n - T_(n+ℓ)))`. ∎

**Corollary 1 (decoupling is the correlation, exactly).** For any probability weights on the
shell, with `E` the weighted mean and `|e(-hτ_n) - 1| ≤ 2π|h|T_n ≤ (π/32)|h|B^(-2)`:

```text
| Cov(A, Z) - E[C] |  ≤  |E[Z]| + (π/32)|h| B^(-2),      Cov(A,Z) = E[AZ] - E[A]E[Z].
```

In the mesoscopic window `|E[Z]| ≤ 4401 h^(-1) B^(-δ)·B/(B-ℓ)` (uniform weights on the `B-ℓ`
admissible times), so

```text
A and Z decouple (Cov → 0)   ⟺   the completed lag-ℓ correlation E[C] → 0.
```

The "arithmetic conditional decoupling" of Objective A, taken for the trivial filtration, is
therefore **literally** the lag correlation at frequency `h(16^ℓ-1)`: no reduction has occurred.
For the coherent seed `s = -x`: `C ≡ 1`, `A = conj(Z)·e(-hτ)`, and in the mesoscopic window (where
`E[Z] → 0`) `Cov(A,Z) → 1`: maximal coupling with the *same* innovation. (For short lags `Z ≈ 1`
and the covariance is trivially small for every seed.) The untwisted innovation estimate IAD-04 is blind to this.

**Corollary 2 (no filtration shortcut).** Let `F` be any σ-algebra on the weighted shell and
`a_F = ‖A - E[A|F]‖_1`. Then

```text
| ‖E[Z|F]‖_1 - ‖E[C|F]‖_1 |  ≤  2 a_F + (π/32)|h| B^(-2).                        (5.2)
```

*Proof.* `Z = conj(A)·C·e(-hτ)` because `|A| = 1`. With `Ã = E[A|F]`:
`‖E[Z|F] - conj(Ã)E[C|F]‖_1 ≤ a_F + sup|e(-hτ)-1|`. Also
`| |conj(Ã)E[C|F]| - |E[C|F]| | ≤ 1 - |Ã|`, and on each cell `1 - |Ã| = E|A| - |E A| ≤ E|A - Ã|`,
so `E[1-|Ã|] ≤ a_F`. ∎

So, among filtrations for which `A` is approximately measurable (Objective A.1, `a_F` small),
Objective A.2 (`‖E[Z|F]‖_1` small) holds **iff** the completed orbit already has *cell-by-cell*
lag-ℓ cancellation `‖E[C|F]‖_1 → 0` on that filtration — which implies the global target, since
`|E[C]| ≤ ‖E[C|F]‖_1`, and is a priori a stronger demand (no separating example is claimed). The innovation/history split cannot make the problem easier;
it moves the unknown correlation into `A`. In the opposite extreme (`F` = full clock), `Z` is
`F`-measurable and `E[Z|F] = Z` has modulus one: no decay.

**What the split does establish.** `E[A] = E[C·conj(Z)·e(-hτ)]`: the mean of the rational history
factor is the completed correlation twisted by the explicit smooth chirp `conj(Z)`. Any
source-selected estimate must therefore be an estimate on Weyl sums of the completed orbit at the
frequency `h(16^ℓ-1)`, with or without a smooth chirp. IAD-08 prices such an estimate.

## IAD-06 — what a favourable lag band buys: the sparse van der Corput budget (PROVED LOCAL)

Let `u_n = e(hY_n)/B` on the shell (zero elsewhere), `W_B(h) = Σ u_n`, and for `d ≥ 1`

```text
c_d(B) = (1/B) Σ_(n=B)^(2B-1-d) e(h(16^d-1)Y_n),      c^U_d(B) = (1/B) Σ_(n=B)^(2B-1-d) e(h(U_(n+d)-U_n)).
```

**(a) Exact Archimedean transport (Objective C).**
`|c_d(B) - c^U_d(B)| ≤ 2π|h| max_n |T_(n+d) - T_n| ≤ (π/32)|h|B^(-2)`, uniformly in the lag `d`.
(The two-time difference is transported; replacing `e(h(16^d-1)Y_n)` by `e(h(16^d-1)U_n)` instead
costs `≍ h16^d/B²` by IAD-05 and is useless exactly in the mesoscopic window.) Note
`c^U_d(B)` is the shell mean of `A·Z`.

**(b) Sparse van der Corput.** For a finite set `H ⊂ Z_(≥0)` with `|H| = k`, `D = max H`:

```text
|W_B(h)|²  ≤  (1 + D/B) [ 1/k + (2/k²) Σ_(a>b in H) Re c_(a-b)(B) ].             (6.1)
```

*Proof.* `k·Σ_n u_n = Σ_m Σ_(a∈H) u_(m+a)`, supported on at most `B+D` values of `m`;
Cauchy–Schwarz and `Σ_m u_(m+a) conj(u_(m+b)) = c_(a-b)(B)/B` for `a > b`, `Σ|u|² = 1/B`. ∎

Taking `H = {0, ℓ_0, 2ℓ_0, …, (k-1)ℓ_0}`:

```text
|W_B(h)|² ≤ (1 + (k-1)ℓ_0/B) [ 1/k + (2/k) Σ_(j=1)^(k-1) (1 - j/k) Re c_(jℓ_0)(B) ].   (6.2)
```

**(c) Accounting (Objective D).**

- *One favourable lag* (`k = 2`): `|W_B(h)|² ≤ (1+ℓ_0/B)(1/2 + ½ Re c_(ℓ_0)(B))`. Decay of a single
  completed lag correlation halves the energy budget and nothing more.
- *A favourable band* `[a, b]` of lags supports a difference set `H` with all nonzero differences
  in the band only if `k ≤ 1 + b/a`. The Kusmin–Landau band of IAD-04 has
  `b/a = (3-δ)/(2+δ) < 2`, so it supports only `k = 2`: even a complete twisted theorem on that
  band yields `limsup |W_B(h)|² ≤ 1/2` by this route, never `o(1)`. (A better positive-definite
  kernel on the band cannot change the verdict: the extremal constant is `≈ 0.447` at ratio `3/2`
  by the floating-point LP of OBSTRUCTIONS O-7 — OBSERVED FINITE, not a theorem.)
- *The short lags are not needed.* A band `[(2+δ) log_16 B, K(2+δ) log_16 B]` supports `k = K`
  and (6.2) gives `limsup |W_B(h)|² ≤ 1/K`. Hence:

  > **Sufficient mesoscopic gate (PROVED CONDITIONAL; premise OPEN).** If for some `δ > 0` and
  > every fixed `j ≥ 1`, `limsup_B Re c^U_(j·ℓ_0(B))(B) ≤ 0` with `ℓ_0(B) = ⌈(2+δ) log_16 B⌉`, then
  > the shell means `W_B(h) → 0`.

  The `O(B)` long lags of the near-pair energy (LL-02) and the low lags of the Fejér average are
  both bypassed; only `O(1)` lags per shell, all at scale `log B`, are used. The premise is a
  statement about the twisted products `A·Z` at lags `jℓ_0`; for `j ≥ 2` these lie beyond the
  first-derivative window, in the aliasing regime of the age ladder.

Nothing in IAD-06 is a source estimate. It answers Objective D: a mesoscopic theorem would be
**sufficient** if it covered every multiple of one mesoscopic lag; a single band of ratio `< 2`
closes at most half of the budget; and the innovation theorem IAD-04 by itself closes none of it,
because by IAD-05 the twisted mean is the completed correlation.

---

## IAD-07 — one missing place suffices: adelic indistinguishability (PROVED LOCAL; generalizes PPP-08)

**Theorem.** Let `q` be an odd prime, `M ≥ 1` an integer coprime to `q` (encoding any finite
precision `p^(j_p)` at any finite set `S` of primes `p ≠ q`, including powers of 2), and `K ≥ 1`.
Choose `k` with `q^k ≥ M·16^(K+2)` and `a = M·round(-x q^k / M)`. For the rational seed
`s = a/q^k`:

1. *(same source)* forcing `r`, tails `T_n` and all innovations `Δ_ℓ(n)` are unchanged;
2. *(same finite places)* `U_n(s) - U_n(0) = 16^n a/q^k` lies in `M·Z_p` for every prime `p ≠ q`
   and every `n ≥ 0`. So the two histories have the same class in `Q_p/Z_p` at **every** place
   `p ≠ q` (identical `p`-component of the real phase, identical denominators, identical fresh-prime
   births) and the same residue modulo `p^(j_p)` at every `p ∈ S`;
3. *(coherent real orbit)* `|Y_n(s)| = 16^n|x+s| ≤ ½·16^(n-K-2)` for `0 ≤ n ≤ K`. With `K = 2B`:
   `|W_B(h; s) - 1| ≤ π|h|/(3840B)`; likewise every summand `e(h(Y_(n+d)(s) - Y_n(s)))` with
   `n + d < 2B` is within `π|h|·16^(n+d-2B-2)` of 1, so `|c_d(B; s) - (B-d)/B| ≤ π|h|/(3840B)`
   (the lag sums have `B-d` terms under the `1/B` normalization).

*Proof.* `|x + a/q^k| ≤ M/(2q^k) ≤ ½·16^(-K-2)`. Item 2: `a ∈ MZ` and `q` is a `p`-adic unit.
Item 3: `|e(t)-1| ≤ 2π|t|` and `Σ_(n=B)^(2B-1) 16^(n-2B-2) < 16^(-2)/15 = 1/3840`. ∎

**Consequence (a class of prime-to-real transfers that cannot work).** Call a transfer
*finite-horizon and census-incomplete* if it derives a bound for the shell `[B, 2B)` from
hypotheses that depend on the seed only through the forcing and through local data, at times
`n ≤ 2B`, at places other than one odd prime `q` (classes in `Q_p/Z_p` at all `p ≠ q`; residues to
any finite precision at finitely many of them). `q` may depend on `B`; in particular the class
contains every transfer using only primes `≤ P(B)` for any bound `P(B)` (take `q_B > P(B)`),
e.g. all primes `≤ 16^(2B)`. **No such transfer can conclude `|W_B(h)| ≤ 1-η`, or
`|c_d(B)| ≤ (1-η)(B-d)/B` for any lag, at any shell with `π|h|/(3840B) < η`:** its hypotheses hold
for `s_B = a/q^k` whenever they hold for `s = 0`, and the conclusion fails there. This covers
fresh-prime births, the 2-adic odometer, and prime marginals or joint laws on any set of places
omitting one prime.

*Scope of the no-go (quantifier, added after audit).* The hijack seed depends on the shell. For a
**fixed** rational seed `s`, the completed orbit is that of `x + s`, which is normal iff `x` is
(Wall, import), so `s` and `0` agree asymptotically. The theorem therefore excludes transfers
whose threshold `B_0` is determined by the census data — effective, shell-by-shell statements —
and does not exclude a purely asymptotic statement with a seed-dependent threshold, nor any
argument that uses the Archimedean place directly.

**The missing invariant.** What separates `s = 0` from `s_B` is *census completeness*: the
denominator of `U_n(0)` is supported on primes `≤ 8n-2` (CG-01, `log den = 6n + o(n)`), with no
further place. Equivalently the product-formula closure `{U_n} ≡ Σ_(p ≤ 8n) {U_n}_p (mod 1)` holds
with **no missing term**; for `s_B` the place `q` carries an extra component of height
`q^k ≥ 16^(2B)`. A working finite-horizon transfer *from finite-place data* must therefore use every prime of the
genealogy simultaneously together with an a priori exclusion of extraneous places — a height
statement. PPP-08
(`pi_parity_pressure/PROOFS.md`) is the special case of one selected prime and the denominator
`p·16^(2A+48)+1`; the seed authentication `Z_n = s` of the zero-anchor kernel already rejects all
of these seeds as identities, which is not the same as a transfer theorem that uses the rejection.

**Necessary, not sufficient.** Census completeness and the literal zero seed still do not imply
cancellation: the seven-pole null source of AT-07 (`arithmetic_barrier/arithmetic`) has zero seed,
every odd conductor depth, and completed orbit identically 0. The invariant a transfer must use is
therefore the triple *(complete census, authenticated seed, the specific four-pole forcing)*; IAD-08
states what any estimate built on that triple is forced to imply.

## IAD-08 — the Liouville wall: what any shell estimate must imply (PROVED LOCAL)

**Theorem.** Let `h ≠ 0`, `0 < η < 1`, and let `N ≥ 1`, `m ≥ 0` be integers and `Θ ≥ 1` an
integer multiplier. Put `ε = ‖Θ·16^m x‖`. Then

```text
| (1/N) Σ_(n=m)^(m+N-1) e(hΘ·16^(n-m)·16^m x) - 1 |  ≤  2π|h| ε · 16^N/(15N).              (8.1)
```

Consequently:

(a) *(Weyl form, `Θ = 1`.)* If `|W_B(h)| ≤ 1-η` for all `B ≥ B_0`, then for all `B ≥ B_0`

```text
‖16^B x‖ = ‖16^(B-1) π‖  ≥  (15η/(2π|h|)) · B · 16^(-B),
```

i.e. `|π - a/q| ≥ c_(h,η)·(log q)·q^(-2)` for every denominator `q = 16^(B-1)`, `B ≥ B_0`, and every
integer `a`: the base-16 restricted irrationality exponent of π is at most 2. In digits: the run of
identical digits `0` (or `F`) starting after hexadecimal position `B` has length at most
`B - log_16 B + O_(h,η)(1)`.

(b) *(Correlation form, `Θ = 16^ℓ - 1`; the lag may depend on `B`, `1 ≤ ℓ < B`.)* If the lag-ℓ
shell correlation satisfies `|c_ℓ(B)| ≤ (1-η)(B-ℓ)/B` for all large `B`, then for those `B`

```text
‖(16^ℓ-1)·16^B x‖ ≥ (15η/(2π|h|)) · (B-ℓ) · 16^(-(B-ℓ)),
‖16^B x‖          ≥ (15η/(2π|h|)) · (B-ℓ) · 16^(-B)          (because ‖Θy‖ ≤ Θ‖y‖).
```

The factor is `B-ℓ`, the number of terms of the lag sum, **not** `B`. By lag regime
(repaired 2026-11-11, second audit; an earlier summary wrote `c·B·16^(-B)` for every lag):

- *fixed lag*, or any `ℓ(B) ≤ (1-θ)B` with a fixed `θ ∈ (0, 1]` — this includes the logarithmic
  and mesoscopic lags `ℓ ≍ log B`: `B-ℓ ≥ θB`, so `‖16^B x‖ ≥ (15ηθ/(2π|h|))·B·16^(-B)`, the
  Weyl-form conclusion up to the constant `θ`;
- *nearly full-shell lags*, `B-ℓ = k(B) = o(B)`: only `‖16^B x‖ ≥ c·k(B)·16^(-B)`. For bounded `k`
  this is weaker than the Weyl form by a factor `B`, and the hypothesis itself then concerns a sum
  of `k` terms.

The first displayed inequality is the sharper one in every regime: it is the exponent-2 bound at
the denominators `q = 16^(B-1)(16^ℓ-1)`, with nothing lost to the factor `16^ℓ`.

(c) *(Basel weights.)* The same with `B_B(h)` and constant `15η/(4π|h|)`, since `p_n ≤ 2/B`.

*Proof.* `‖hΘ16^n x‖ ≤ |h|16^(n-m) ε` and `|e(t)-1| ≤ 2π‖t‖`; sum the geometric series. If the
mean has modulus `≤ 1-η` the left side of (8.1) is `≥ η`. ∎

**Calibration (CLASSICAL IMPORT; verified against sources on 2026-11-11, see
[SOURCE_MAP](SOURCE_MAP.md)).** In the Amou–Bugeaud normalization, `v_b(ξ)` is the supremum of `v`
with `‖b^n ξ‖ < (b^n)^(-v)` infinitely often, `v_16 = v_2`, and `v_b(ξ) ≤ μ(ξ) - 1`. Conclusion (a)
says `v_16(π) ≤ 1` and, more sharply, `‖16^B x‖ ≥ c·B·16^(-B)` with **no** ε-loss in the exponent.

- *Refereed record:* `μ(π) ≤ 7.103205334137…` (Zeilberger–Zudilin 2020), hence only
  `v_16(π) ≤ 6.1033`, i.e. `‖16^B x‖ ≥ 16^(-6.1033·B)` for large `B` (this is RIO-11 of
  `inertial_origin_q6`). No published improvement specific to denominators `2^n` or `16^n` was
  found, including none via BBP.
- *Unrefereed claims (not imported, not relied on):* a 2026 arXiv preprint claiming
  `μ(π) < 7.1019`, and a 2026 formalized preprint claiming `μ(π) = 2`. Even if `μ(π) = 2` is
  confirmed, it gives `‖16^B x‖ ≥ 16^(-(1+ε)B)`, i.e. runs of length `≤ (1+ε)B` at position `B`,
  which still does **not** reach the wall's `B - log_16 B + O(1)`: the wall sits at the exact
  borderline exponent with a logarithmic gain and no ε.
- *Sharpened in the continuation (ZSC-01 of [CARRY_FLUX](CARRY_FLUX.md)).* The endpoint form
  above uses only the shell that starts at the approximation. Using the best shell that
  contains the coherent stretch, a fixed saving `η` forces
  `‖16^m x‖ ≥ c·16^(-((2-η)/(2+η))·m)`: the restricted exponent must be **strictly below 1**.
  Since `v_16 ≤ μ - 1` and `μ ≥ 2` for every irrational, no bound on the unrestricted
  irrationality exponent — `μ(π) = 2` included — can supply this.

> **Any** all-large-shell estimate of the kind sought — for one mode `h`, with a *fixed* saving
> `η` (not even `η → 1`), for the Weyl sum, or for a single lag correlation at a lag
> `ℓ(B) ≤ (1-θ)B` with fixed `θ > 0` — implies `‖16^B x‖ ≥ c·B·16^(-B)` for all large `B`
> (`c` depends on `h`, `η`, `θ`): `v_16(π) ≤ 1` without ε-loss, where the refereed record is
> `6.1033`. For nearly full-shell lags the conclusion is `c·(B-ℓ)·16^(-B)` only. Outcome A of the
> mission is therefore at least as hard as that Diophantine theorem for π at the denominators
> `16^B`; ZSC-01 shows it is in fact strictly harder.

This is a necessary condition only. It is satisfied by non-normal numbers: for `x' = 1/17` one
has `‖16^B x'‖ = 1/17` for every `B` while `W_B(h; x') = cos(2πh/17) + O(1/B)` (exactly the
cosine for even `B`). The Diophantine type is
**necessary and far from sufficient**: the missing invariant is strictly stronger than height.

**Why this is the right price tag for prime-to-real transfer.** Finite-place information yields
*inequations*: e.g. IAD-09c shows `h(U_(n+ℓ)-U_n) ∉ Z` whenever a fresh prime is born in the
window. Converting an inequation for a rational of denominator `D` into a real separation costs
`1/D`, and here `D = exp((6+o(1))n)` (CG-01) for `n ∈ [B, 2B)`, i.e. `exp(-6B)` or smaller, while
the wall requires the scale `B·16^(-B) = exp(-(2.77…)B)`. The height is exponentially too large,
and the Archimedean tail `T_n ≍ n^(-2)` separating `U_n` from `Y_n` is larger again. Only
transcendence-grade input is known to beat the height, and its current record is the exponent
`7.1033`.

## IAD-09 — fresh primes: exact local innovation, positive birth mass, no metric content (PROVED LOCAL + one CLASSICAL IMPORT)

Write `r(m) = 4/(8m-7) - 1/(2(2m-1)) - 1/(8m-3) - 1/(2(4m-1))`. For an odd prime `p ≥ 7` an
*event* is a time `m` with `p | (8m-7)(2m-1)(8m-3)(4m-1)`; its *birth* `β(p)` is the first event.

**(a) Births and separation.** `β(p) = (p+7)/8, (p+3)/8, (p+1)/4, (p+1)/4` for
`p ≡ 1, 5, 3, 7 (mod 8)`, through the poles `8m-7`, `8m-3`, `4m-1`, `4m-1` respectively. At each
event exactly one of the four factors is divisible by `p`, and any two distinct events of `p` are
at least `(p-5)/8` apart.

*Proof.* The four event classes are `m ≡ 7/8, 1/2, 3/8, 1/4 (mod p)`. Two factors vanishing at
the same `m` would force `p | 1, 3, 4` or `5`, impossible for `p ≥ 7`. If `m ≠ m'` are events in
different classes, `m - m' ≡ c/8 (mod p)` with `c ∈ {±1,…,±5}` (the pairwise class differences),
so `p | 8(m-m') - c ≠ 0` and `|m - m'| ≥ (p-5)/8`; in the same class `|m - m'| ≥ p`. The smallest
positive solutions give `β(p)`. ∎

**(b) The fresh component is pure innovation.** Let `n ≥ 8`, `1 ≤ ℓ ≤ n/4`, and let `p` be born at
`β(p) = n+j`, `1 ≤ j ≤ ℓ`. Then `U_n ∈ Z_(p)`, `p` has no other event in `(n, n+ℓ]`,
`v_p(U_(n+ℓ) - U_n) = v_p(Δ_ℓ(n)) = -1`, and the `p`-component in `Q_p/Z_p` is

```text
{U_(n+ℓ) - U_n}_p = ρ/p,    ρ ≡ 4·16^(ℓ-j), -16^(ℓ-j), -16^(ℓ-j)/2 (mod p)   for p ≡ 1, 5, 3 or 7 (mod 8).
```

It does not depend on the seed's history at all (for any seed that is `p`-integral).

**(c) Exact inequation.** Under the hypotheses of (b) (`n ≥ 8`, `ℓ ≤ n/4`, a `p`-integral seed), if
the window `(n, n+ℓ]` contains a birth of a prime `p ∤ h`, then `h(U_(n+ℓ) - U_n) ∉ Z`, so
`A_n Z_n ≠ 1`. (Without `ℓ ≤ n/4` a second event of `p` inside the window can cancel the first.) This is an equality-level statement with **no** metric
content: the only general lower bound is `‖h(U_(n+ℓ)-U_n)‖ ≥ 1/den = exp(-(6+o(1))(n+ℓ))`.

**(d) Welding of the two places at a fresh pole.** For a fresh pole term `c·16^k/p` of age
`k = ℓ-j` with `c·16^k ∈ Z` — the poles `8m-7` and `8m-3` at every age, and the pole `4m-1`
(`c = -1/2`) at ages `k ≥ 1` — its class in `Q_p/Z_p` and its real value modulo one are the *same
rational number*. (At age 0 the term `-1/(2p)` of the pole `4m-1` also has the 2-adic component
`1/2`, which the sibling pole `-1/(2(2m-1))` cancels; the weld then holds after removing that
component. Corrected after audit.) While `|c|·16^k < p` (age `< log_16 B + O(1)`) the `p`-adic
component literally equals the real term; afterwards it winds. The real innovation stays `< 1`
until age `2 log_16 B` only because the four simultaneous poles — living at four different places —
cancel to order `1/n²`. Each single place sees none of that cancellation. This is the smallest
exact instance of "full CRT winding is not determined by the prime marginals".

**(e) Birth mass (CLASSICAL IMPORT: prime number theorem in progressions mod 8).** The number of
prime births in `[B, 2B)` (counted with multiplicity) is `(6 + o(1)) B/ln B`: two units each from `p ≡ 1 (8)` in
`(8B, 16B]`, `p ≡ 5 (8)` in `(8B, 16B]` and `p ≡ 3 (4)` in `(4B, 8B]`. Averaged over `n` in the
shell, the number of births in the innovation window `(n, n+ℓ]` is `(6+o(1))ℓ/ln B`. For
`ℓ = c·log_16 B` this mean is `6c/ln 16 ≈ 2.164·c`: between 4.3 and 6.5 across the mesoscopic
window. **Fresh-prime birth events are not a zero-density phenomenon at mesoscopic lag** — a
typical window contains several — but by (c) and IAD-07 their presence carries no averaged
cancellation: the hijacked seed of IAD-07 has exactly the same births, the same fresh components
and correlation `≈ 1`.

---

## Summary of what is and is not established

| | Statement | Status |
|---|---|---|
| IAD-01 | Weighted lag identity, (1.2); the `B ≥ 16^10` threshold belongs to the coarse constant `4/L` only | PROVED LOCAL (verification) |
| IAD-02 | Window-energy monotonicity; every schedule `L(B)→∞` is equivalent to normality; no extra uniformity demanded | PROVED LOCAL |
| IAD-03 | Innovation calculus, moment representation, sharp derivative brackets | PROVED LOCAL |
| IAD-04 | Mesoscopic innovation theorem with constant 4401, uniform on subintervals and progressions; no saving below `2 log_16 B`; age ladder | PROVED LOCAL (higher-derivative extension: CLASSICAL IMPORT, not re-proved) |
| IAD-05 | Gauge identity `A = C·conj(Z)·e(-hτ)`; decoupling ⟺ correlation decay; no filtration shortcut | PROVED LOCAL |
| IAD-06 | Exact transport; sparse van der Corput budget `1/k`; sufficient mesoscopic gate | PROVED LOCAL; gate premise OPEN |
| IAD-07 | One-missing-place indistinguishability; no finite-horizon census-incomplete transfer; census completeness necessary, not sufficient | PROVED LOCAL |
| IAD-08 | Liouville wall: any fixed-saving shell estimate ⟹ restricted exponent ≤ 2 for π at `16^B` | PROVED LOCAL; literature calibration IMPORT |
| IAD-09 | Fresh-prime exact component, inequation, place weld, birth mass `≈ 2.164c` | PROVED LOCAL + PNT-AP IMPORT |
| — | A source-derived bound on `R`, on any `c^U_d`, or on any `W_B(h)` for the zero seed | **OPEN** |
| — | π base-16 normality | **OPEN** |
