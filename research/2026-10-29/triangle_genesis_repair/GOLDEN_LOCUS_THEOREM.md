# The golden fixed-point locus (Operation Main XVI, P1)

**Status:** PROVED (classical special-function / Galton–Watson analysis), with exact symbolic and
independent numeric checks. Corrects a false global-uniqueness statement in the Main XV apparatus.
**No π normality or RH content.** This is a statement about a declared offspring/endpoint
generating function, not about π's digits.

## 0. Objects

From the Gamma–Poisson emergence class (`operational_triangle_frontier/THEOREMS.md` TG-04) the
declared endpoint / offspring probability generating function is

```
G_{r,θ}(z) = [1 + θ(1 − z)]^{−r},        r > 0, θ > 0, z ∈ [0,1].
```

Write `λ = φ^{−1} = (√5 − 1)/2` (so `λ² + λ − 1 = 0`, `1 + λ = φ`, `λ^{−1} = φ`). Let
`q_{r,θ}` denote the **least fixed point** of `G_{r,θ}` in `[0,1]` (the Galton–Watson extinction
probability of the offspring law when `G` is read as a PGF). The historical fixed-golden mark is
`λ^r`.

## 1. Basic shape of G

For `θ>0, r>0` on `[0,1]`, with `w(z) = 1 + θ(1−z) ∈ [1, 1+θ]`:

- `G(1) = 1`, `G(0) = (1+θ)^{−r} ∈ (0,1)`.
- `G'(z) = rθ·w(z)^{−r−1} > 0` (strictly increasing).
- `G''(z) = r(r+1)θ²·w(z)^{−r−2} > 0` (strictly convex).
- mean `μ := G'(1) = rθ`.

**Standard PGF dichotomy** (convex increasing `G` with `G(1)=1`, `G(0)∈(0,1)`): if `μ = G'(1) > 1`
(supercritical) there is a unique fixed point `q ∈ (0,1)`, it is the least fixed point, and the
iteration `q_{k+1} = G(q_k)` from `q_0 = 0` converges up to it; if `μ ≤ 1` the only fixed point in
`[0,1]` is `q = 1`.

*Self-contained reason for the `μ ≤ 1` case* (the one line the `⇒` direction leans on): put
`h(z) = G(z) − z` on `[0,1]`. Then `h(1) = 0`, `h'(z) = G'(z) − 1`, `h'(1) = μ − 1 ≤ 0`, and `h'`
is strictly increasing (since `G'' > 0`), so `h'(z) < h'(1) ≤ 0` for all `z < 1`; hence `h` is
strictly decreasing on `[0,1]`, giving `h(z) > h(1) = 0`, i.e. `G(z) > z`, for every `z ∈ [0,1)`.
So no fixed point exists in `[0,1)` when `μ ≤ 1`; `q = 1` is the only one. Contrapositive: an
interior fixed point (`q < 1`) forces `μ > 1`.

## 2. The locus theorem

> **Theorem (golden locus).** For every `r > 0`,
> ```
> q_{r,θ} = λ^r    ⇔    θ = θ⋆(r) := λ / (1 − λ^r).
> ```
> Along the curve `θ = θ⋆(r)` the process is supercritical (`rθ > 1`), so `λ^r` is genuinely the
> least (interior) fixed point.

**Proof.**

*(⇐) The curve lands the golden fixed point.* Put `θ = θ⋆(r) = λ/(1−λ^r)` (well-defined and
positive since `0 < λ^r < 1` for `r>0`). Evaluate `w` at `z = λ^r`:
```
w(λ^r) = 1 + θ⋆(r)·(1 − λ^r) = 1 + [λ/(1−λ^r)]·(1 − λ^r) = 1 + λ = φ = λ^{−1}.
```
Hence `G_{r,θ⋆}(λ^r) = w(λ^r)^{−r} = (λ^{−1})^{−r} = λ^r`. So `λ^r` is a fixed point, and it lies
in `(0,1)`. By supercriticality (step below) the least fixed point is the unique interior one, so
`q_{r,θ⋆(r)} = λ^r`.

*(⇒) Only this curve does.* Suppose `q_{r,θ} = λ^r`. Since `λ^r ∈ (0,1)`, the least fixed point is
interior, which (by the dichotomy) forces `μ = rθ > 1`, and `λ^r` satisfies the fixed-point
equation `w(λ^r)^{−r} = λ^r`, i.e. `w(λ^r) = λ^{−1} = 1 + λ`. Thus `θ(1 − λ^r) = λ`, and because
`1 − λ^r > 0` we get `θ = λ/(1 − λ^r) = θ⋆(r)`. ∎

**Supercriticality on the locus.** On `θ = θ⋆(r)`, `μ = rθ⋆(r) = rλ/(1 − λ^r) > 1` ⇔
`f(r) := rλ + λ^r > 1`. Now `f(0) = 1` and
```
f'(r) = λ + λ^r ln λ.
```
Since `ln λ < 0` and `λ^r ≤ 1` for `r ≥ 0`, `λ^r ln λ ∈ [ln λ, 0)`, so `f'(r) ≥ λ + ln λ ≈
0.6180 − 0.4812 = 0.1368 > 0`, and `f'` is strictly increasing to `λ > 0`. A zero of `f'` would
need `λ^r = −λ/ln λ = λ/|ln λ| ≈ 1.284 > 1`, impossible for `r ≥ 0`. Hence `f' > 0` throughout,
`f` is strictly increasing, and `f(r) > f(0) = 1` for all `r > 0`. Therefore `rθ⋆(r) > 1` on the
entire locus. ∎

## 3. Calibration (exact)

| rank `r` | clock `θ⋆(r) = λ/(1−λ^r)` | fixed point `q = λ^r` | mean `rθ` |
|---|---|---|---|
| 1 | `φ` | `λ` | `φ ≈ 1.618` |
| 2 | `1` | `λ²` | `2` |
| 3 | `φ/2` | `λ³` | `≈ 2.427` |

(`θ⋆(1) = λ/(1−λ) = λ/λ² = λ^{−1} = φ`; `θ⋆(2) = λ/(1−λ²) = λ/λ = 1`; `θ⋆(3) = λ/(1−λ³)`, and
`1−λ³ = 1−λ·λ² = 1−λ(1−λ) = 1−λ+λ² = 2λ²` using `λ² = 1−λ`, so `θ⋆(3) = λ/(2λ²) = 1/(2λ) = φ/2`.)
All verified exactly in `golden_locus.py` and by independent root-isolation in
`independent_oracle_xvi.py` for `r = 1,…,6`.

## 4. The restricted uniqueness theorem (the BBP point stays distinguished)

> **Theorem (restricted uniqueness at the authentic clock).** On the slice `θ = 1`,
> `q_{r,1} = λ^r` holds **iff** `r = 2`.

**Proof.** By the locus theorem with `θ = 1`: `θ⋆(r) = 1 ⇔ λ/(1−λ^r) = 1 ⇔ 1 − λ^r = λ ⇔
λ^r = 1 − λ = λ² ⇔ r = 2` (because `0 < λ < 1` makes `r ↦ λ^r` injective). ∎

Hence the original BBP source — which is forced to rank `r = 2` by `Q(x) = 15x − (59/2)x² + O(x³)`
**and** to clock `θ = 1` by `a_n = 8n−7, m = n` (so `8m/a → 1`) — sits at the **unique**
intersection of its own authentic clock slice `{θ = 1}` with the golden locus. The Oily–Macaroni
point `(r,θ) = (2,1)` is therefore distinguished *on its authentic source/clock slice*, exactly as
the author's triangle intends; it is simply **not** the only point of the larger `(r,θ)` family at
which the historical golden mark `λ^r` coincides with the self-consistent root `q_{r,θ}`.

**This corrects** the Main XV statement that `D_λ` and `D_self` "agree only at `(2,1)`". The correct
statement is: the coincidence set is the one-dimensional golden locus `θ = λ/(1−λ^r)`; within the
authentic clock slice `θ = 1` the coincidence is unique at `r = 2`.

## 5. Geometry of the locus

- **Monotonicity / range.** `θ⋆(r) = λ/(1−λ^r)` is smooth and strictly decreasing on `(0,∞)`:
  `dθ⋆/dr = λ·λ^r ln λ /(1−λ^r)² < 0`. As `r → 0⁺`, `θ⋆ → +∞`; as `r → ∞`, `θ⋆ → λ⁺`. So
  `θ⋆ : (0,∞) → (λ, ∞)` is a strictly decreasing bijection; each clock `θ > λ` meets the locus at
  exactly one rank. (The lower limit `λ` is the critical floor: `θ ≤ λ` cannot realize a golden
  root at any finite rank.)
- **Constant Laplace-rate invariant.** Along the *entire* locus the rate `ρ := θ⋆(r)(1 − q) =
  θ⋆(r)(1 − λ^r) = λ` is **constant**. Equivalently, with `Y ~ Gamma(r,1)` the fixed-point Laplace
  readout is rate-locked: `E e^{−λY} = (1+λ)^{−r} = φ^{−r} = λ^r = q`. The golden locus is exactly
  the set of `(r,θ)` on which the branching Laplace probe runs at the single golden rate `λ`.
- **Coincidence of the two rank families.** The fixed-golden probe `D_λ(r) = ψ(r) − λ^r` and the
  self-consistent contrast `D_self(r,θ) = ψ(r) − q_{r,θ}` satisfy, by the locus theorem,
  ```
  D_self(r, θ⋆(r)) = ψ(r) − q_{r,θ⋆(r)} = ψ(r) − λ^r = D_λ(r)     for every r > 0.
  ```
  So the golden locus is *precisely* the coincidence set `{D_self = D_λ}`, parametrized by
  `θ = θ⋆(r)`. Off the locus the two families differ (checked numerically). At `(2,1)` this is the
  Oily–Macaroni identity `D_λ(2) = ψ(2) − λ² = (1 − γ) − λ² = λ − γ = Ω_OM`, using `λ² = 1 − λ`.
- **Which positive kernels realize it.** Any admissible positive boundary kernel with
  `Q(x) ~ c x^{r−1}` (`c>0`) under a clock `8m/a → θ` lands the golden fixed point `q = λ^r` **iff**
  its clock satisfies `θ = θ⋆(r)` — a one-parameter family of (rank, clock) pairs. Kernels with
  `rθ ≤ 1` (subcritical/critical: in particular any clock `θ ≤ λ` at any rank, or `r ≤ 1` with
  `θ ≤ 1`, etc.) have `q = 1` and realize **no** interior golden root. Matching the golden fixed
  point is a joint rank-and-clock condition, not a property of the boundary rank alone.

## 6. What this does NOT establish (firewall)

The golden locus is an exact identity about a **declared** branching/Laplace observer of the
Gamma–Poisson emergence class. It is parametrized geometry, not a π statement. It does **not**:

- say the π digit orbit is an offspring process, or that any such process is physical;
- promote Oily–Macaroni from a source/observer specialization to a universal law;
- contribute any signed cancellation. `T_N(h) = o(N)` for the authentic BBP orbit (π base-16
  normality) remains **OPEN**, independently of this locus.

The authentic source-induced boundary (rank `2`, clock `1`, obtained from the four signed poles)
must stay distinguished from an observer parameter `θ` tuned to recover a golden fixed point: the
restricted-uniqueness theorem is exactly the statement that the authentic clock pins the BBP point
uniquely, whereas tuning `θ` lets other ranks sit on the golden locus.

**Dependencies.** Classical Galton–Watson extinction (least fixed point of a supercritical PGF);
Gamma Laplace transform; `ψ(2) = 1 − γ` (NIST DLMF §5.4/§5.5); the golden identity `λ² = 1 − λ`.
Checks: `golden_locus.py` (iteration + sympy certificate), `independent_oracle_xvi.py` (substitution
+ polyroots), `tests/test_triangle_genesis_repair.py::P1GoldenLocus` / `::CrossCheckIndependentOracle`.
