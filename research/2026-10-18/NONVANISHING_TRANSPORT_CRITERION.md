# Source-indexed nonvanishing compactness: a finite→global transport criterion

**Target A, Academic Main IV continuation.** Module
`observational_succ/nonvanishing_transport.py`; tests
`tests/test_nonvanishing_transport.py`.

**Status labels used:** CLASSICAL, VERIFIED-EXACT-MODEL, OPEN. **Firewall:**
every returned dict carries `"RH_proved": False`. No nontrivial zeta-zero
ordinate is a construction input; `Λ(p^k)=log p`; one real Archimedean Gamma
ladder `α_j = (4j+1)/2`. A persistent positive matrix coefficient is **not** a
completed Weil form and does **not** prove RH or the all-radii S₄ sign.

## 1. The problem and the no-go it must respect

We want a usable sufficient condition under which a quantity read off the
*finite* source sections (the only thing a finite embodied observer ever
touches) is guaranteed to survive to the *global* (J→∞) limit as a nonzero
number. The naive candidate — "a uniform spectral gap of the finite sections"
— is **forbidden**:

- the genuine source kernel is **compact**, and a compact operator on an
  infinite-dimensional space has **no fixed positive spectral gap** (its
  spectrum accumulates at 0);
- finite sections converge to the global operator only **strongly**, and
  **strong convergence need not be norm convergence**, so spectral data of the
  sections need not converge to spectral data of the limit.

The object that *does* survive strong convergence is a **matrix coefficient**:
for a fixed vector `v`, if `T_J → T` strongly then `⟨v, T_J v⟩ → ⟨v, T v⟩`.
So the criterion is built on **matrix-coefficient survival**, never a gap.

## 2. The criterion (CLASSICAL, elementary)

Let `{T_J}` be finite sections of a fixed bounded operator on a Hilbert space
and let `v` be a fixed vector. Put `c_J = ⟨v, T_J v⟩`. If

- **(i) uniform boundedness** — `|c_J| ≤ B` for a fixed finite `B`;
- **(ii) compatible sections** — the `c_J` are nested / monotone and admit a
  certified **Cauchy remainder** `ρ_J` with `|c_∞ − c_J| ≤ ρ_J → 0`, so a
  single global limit value is consistent with every enclosure; and
- **(iii) persistent floor** — `c_J ≥ f` for a fixed rational `f > 0`,
  justified **structurally for all J** (not merely on the tested J),

then the transported global coefficient exists and `c_∞ ≥ f > 0`: it is
**nonvanishing**. (Proof: (ii) gives convergence `c_J → c_∞`; since `c_J ≥ f`
for all J, the limit `c_∞ ≥ f`. This is monotone/Cauchy convergence of a scalar
sequence — classical and elementary. The content is entirely in *certifying*
(i)–(iii) exactly.)

The persistent object is a **matrix-coefficient survival, not a spectral gap**.
`transport_criterion(sections, uniform_bound, floor)` returns
`certified_nonvanishing=True` only when (i)–(iii) hold on the supplied exact
data *and* the lowers are monotone nondecreasing (the structural witness that
the first-term floor persists to the limit) *and* the enclosures share a common
limit value; otherwise it **refuses** and names the failing hypothesis.

## 3. VERIFIED-EXACT-MODEL instance: the authentic Gamma coefficient

Take the one-real-Gamma heat kernel `K_s = diag(exp(−α_j s))` in the authentic
rung basis (`α_j=(4j+1)/2`, the frozen source ladder authenticated by
`original_source_infinite_gamma_contract`, blob
`0cc8510b71d178fc79e8d410a86d8b6014cf9178`, prime wavefront `((2,2),)`). Its
J-th finite section is `T_J = P_J K_s P_J`. Fix the honest ℓ² vector
`v_j = 1/(j+1)` (so `‖v‖² = Σ 1/(j+1)² < π²/6`), independent of J and of s. The
chosen **rank-one matrix coefficient** is

```
c_J = ⟨v, T_J v⟩ = Σ_{j<J} exp(−α_j s) / (j+1)² ,   s = 1/128 (rational).
```

`s=1/128` keeps `α_{J−1}s = 253/256 < 1` for all `J ≤ 64`, so every exponential
is bracketed **exactly** by the outward alternating-Taylor intervals of
`infinite_gamma_carleman.exp_negative_interval` (Fraction endpoints).

- **(i) uniform bound.** `c_J < Σ 1/(j+1)² < 165/100` — a hard rational ceiling
  (tested); `B` is taken as the fattest exact global upper across the orders.
- **(ii) Cauchy remainder.** `α_{j+1}−α_j = 2`, so with `r = exp(−2s)` and
  `w_j² = 1/(j+1)² ≤ 1/(J+1)²` for `j ≥ J`,
  `c_∞ − c_J ≤ (1/(J+1)²)·exp(−α_{J−1}s)·r/(1−r)`,
  bounded above exactly by `(1/(J+1)²)·last_exp_hi·r_hi/(1−r_hi)`. The
  remainders shrink `0.173 → 0.0358 → 0.00559` for J = 16, 32, 64.
- **(iii) persistent floor.** Every term is nonnegative, so `c_J` is monotone
  increasing and `c_J ≥ c_{first term} = exp(−s/2)`, a **structural** floor for
  all J; its exact lower bracket is `≈ 0.99610 > 0`.

Exact results (J = 16, 32, 64):

| J  | `c_J` lower | `c_J` upper | Cauchy remainder ≤ |
|----|-------------|-------------|--------------------|
| 16 | ≈ 1.55147   | ≈ 1.55147   | ≈ 0.17314          |
| 32 | ≈ 1.57267   | ≈ 1.57267   | ≈ 0.03578          |
| 64 | ≈ 1.58040   | ≈ 1.58040   | ≈ 0.00559          |

Transported global coefficient enclosure: `c_∞ ∈ [1.58040, 1.58600]`
(independent long-partial-sum check: `c_∞ ≈ 1.58270`). Certified global floor
`c_∞ ≥ exp(−1/256) ≈ 0.99610 > 0`. **Verdict: VERIFIED-EXACT-MODEL** — the
coefficient transports to a nonvanishing limit, certified by exact rationals at
finite J. (This is not a float "green test"; the certificate is the exact
outward enclosure, and `RH_proved=False`.)

## 4. REQUIRED atomic–Haar hostile control: the criterion must REFUSE

A criterion that fails to reject the vanishing case is overclaimed. The hostile
boundary is the atomic–Haar regime of `institute_atomic_haar`, where the
analogous coefficient **vanishes**. Two independent atomic witnesses:

- **`harmonic_graph_witness(size).source_norm_squared = 1/H_size`** — the
  squared mass of the graph sequence tending to `(0, Haar)`; `H_size → ∞` so
  the coefficient `→ 0` (values `12/25, … → 0` for sizes 4, 16, 64, 256).
- **`haar_unit_mass((2,3,…,p)) = Π (q−1)/q`** — the atomic vacuum mass as the
  prime family grows; the divergent Euler product drives it to 0 (values
  `1/2, 1/3, 4/15, 8/35 → 0`).

Both sequences are exact rationals and **strictly decreasing**. Feeding each to
`transport_criterion` (claiming the largest observed value as a would-be floor)
returns `certified_nonvanishing=False`, with reasons
`no_persistent_floor_coefficient_not_monotone`,
`enclosures_inconsistent_no_common_limit`,
`floor_not_respected_by_finite_data`, and a `vanishing_signature=True`. The
criterion **correctly refuses** — the true limit is 0, so refusal is the right
answer, not a false negative. **Verdict: HOSTILE-CONTROL-REFUSED.**

## 5. Honest boundary — what the true J→∞ limit still requires

This is **finite-J plus a hostile control, not a proof of the global limit for
the genuine operator.** Specifically:

1. The *general criterion* §2 is an elementary classical theorem; it is only as
   strong as its hypotheses, which must be certified **per operator**.
2. It is CERTIFIED here only for the **diagonal** Gamma heat-kernel model, where
   monotonicity and the first-term floor are exact and the J→∞ limit is
   elementary (geometric).
3. For the genuine **non-diagonal** Suzuki OU / S₄–Weil operator, hypothesis
   (iii) — a structurally persistent positive matrix coefficient — is **OPEN**.
   Monotonicity of `⟨P_J v, T P_J v⟩` is *not* automatic for a non-diagonal
   `T ⪰ 0`, so the floor would have to be re-established by the actual source
   structure, which is not done here.
4. Matrix-coefficient survival is deliberately **weaker** than a spectral gap
   (the compact kernel has none) and carries **no completed Weil positivity**.
   A positive coefficient is not a signed Weil form; the four-mode S₄ sign
   remains AMBIGUOUS/OPEN and **RH is not proved**.

**Next falsification opportunity.** Instantiate the criterion on a genuine
off-diagonal finite-section coefficient of the authentic
`authentic_fredholm_feature_gram` / `authentic_full_low_entry` data and test
whether any fixed `v` yields a *monotone* floored coefficient; if none does, the
matrix-coefficient route to nonvanishing transport is itself refuted for the
real operator.
