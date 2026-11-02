# Entropy ⟷ Dimension bridge for x3-rigidity obligation (B)

**Branch:** `research/x3-rigidity-machinery-2026-11-02`
**Status:** research note; classical bridge stated with exact citations, SUCC reduction labeled, open gate isolated. **No theorem about π is claimed.**

---

## 0. The object under study

```
x_{n+1} = {16 x_n},   x_1 = {π},
U_n = 16^{n-1} π − T_n,   T_n = Σ_{j≥1} 16^{−j} r(n+j),   U_0 = 0,
r(m) = 4/(8m−7) − 2/(8m−4) − 1/(8m−3) − 1/(8m−2)   (four-pole BBP forcing),
y_n = {16^{n-1} π} = {U_n + T_n}.
```

`μ` is **any** weak-* limit point of the empirical measures `μ_N = (1/N)Σ_{n=1}^N δ_{x_n}`. Since `T_16` is continuous, every such limit is `T_16`-invariant (a standard fact; the push-forward `μ∘T_16^{-1}` and `μ` agree because the shift by one orbit point has vanishing effect as `N→∞`). Obligation **(B)** is

```
(B)    dim_* μ > 0        (positive *lower* dimension).
```

The **digit stream** is the base-16 itinerary of this orbit: `d_n ∈ {0,…,15}` with `x_n ∈ [d_n/16, (d_n+1)/16)`. This is *exactly* the standard base-16 expansion of π. A length-`m` **cylinder** is a word `w ∈ {0,…,15}^m`; it corresponds to the `16^{-m}`-adic interval `[0.w, 0.w + 16^{-m})`.

---

## 1. The Furstenberg/Hochman equivalence (classical, exact)

Let `T_b(x) = {b x}` on `ℝ/ℤ`. For a `T_b`-invariant Borel probability `μ`, let `h_μ(T_b)` denote the **Kolmogorov–Sinai entropy** (log base `e`), and `dim μ` / `dim_* μ` the Hausdorff / lower dimension.

### 1a. The exact entropy–dimension identity (Hochman)

**Theorem (Hochman 2014,** *On self-similar sets with overlaps and inverse theorems for entropy*, Ann. of Math. **180** (2014) 773–822**, § 1.1 / the "dimension = entropy / log b" statement).** Let `μ` be a `T_b`-invariant, **ergodic** probability measure on `ℝ/ℤ` that is **not a point mass**. Then `μ` is exact-dimensional and

```
dim μ  =  h_μ(T_b) / log b.          (HD)
```

This is the exact statement the task attributes to "Hochman's entropy-dimension identity for ×16: `h = dim_* · log 16`." It holds a.e.-`μ`-exactly (not merely as an inequality), *provided* ergodicity and non-atomicity. The direction we need is the trivial corollary:

```
h_μ(T_b) > 0   ⟹   dim μ > 0.        (HD⁺)
```

### 1b. The Furstenberg positive-entropy ⟹ positive-dimension direction

**Theorem (Furstenberg 1967,** *Disjointness in ergodic theory, minimal sets, and a problem in Diophantine approximation*, Math. Systems Theory **1** (1967) 1–49**).** If `μ` is `T_b`-invariant and `h_μ(T_b) > 0`, then `dim_* μ > 0` (in fact `dim μ ≥ h_μ(T_b)/log b`). This is the measure-theoretic core: **positive entropy forces positive dimension**. The converse — positive dimension forces positive entropy — is **false in general** (there exist `×2`-invariant measures with `dim > 0` and `h = 0`; e.g. self-similar measures at sub-maximal dimension with exact overlaps at a single scale, or the classical Sturmian/odometer constructions transported to the circle).

> **Consequence (the honest asymmetry).** The implication we actually need for (B) is the *easy* direction:
> ```
> h_μ(T_16) > 0   ⟹   dim_* μ > 0.     [classical, proved]
> ```
> It is **one-way**. Positive lower dimension does *not* give positive entropy. Therefore (B) is genuinely *weaker* than "the orbit has positive entropy" — a fact that matters for the chain below.

---

## 2. Making the entropy statement machine-checkable

### 2a. Cylinder Shannon entropy and the entropy rate

For the `m`-cylinder partition `ξ_m` of `ℝ/ℤ` into `16^m` half-open `16^{-m}`-cells, define the **cylinder Shannon entropy** of the orbit measure:

```
H_m = H_μ(ξ_m) = −Σ_{|w|=m} μ([w]) log μ([w]).
```

By the Shannon–McMillan–Breiman theorem (valid for any ergodic `μ`; and the *mean* entropy formula `h_μ = lim_m H_m/m` holds by Kolmogorov–Sinai / the Shannon–McMillan theorem without ergodicity — it is the definition of measure entropy via the generating partition `ξ_1`):

```
h_μ(T_16)  =  lim_{m→∞}  H_m / m.          (ENT)
```

The equality is an *identity* (the partition `ξ_1` generates the Borel σ-algebra). **This is exactly the "clean countable statement"** the task requests: `h_μ(T_16) > 0` is equivalent to `liminf_m H_m/m > 0` (equivalently `lim_m H_m/m > 0`, since the limit exists by subadditivity).

### 2b. The empirical objects: `H_m` vs the collision energy `Q_{m,N}`

The existing SUCC reduction works with **empirical** cylinder frequencies and the **collision energy** (a Rényi-2, i.e. `L²`, object), *not* the Shannon entropy:

```
p_{m,N}(w) = N^{-1} #{ 0 ≤ n < N : d_n … d_{n+m−1} = w },
Q_{m,N}    = 16^m Σ_{|w|=m} p_{m,N}(w)^2  ≥ 1,
H_2(m,N)   = −log( Σ_w p_{m,N}(w)^2 )       (Rényi-2 block entropy),
H_m^N      = −Σ_w p_{m,N}(w) log p_{m,N}(w) (empirical Shannon block entropy).
```

The exact finite link between them is the standard Rényi ordering plus concavity of log:

```
H_2(m,N) ≤ H_m^N,        i.e.   −log Σ p² ≤ −Σ p log p      [exact, finite]
log Q_{m,N}  =  m log 16  −  H_2(m,N)                       [exact, finite, EQUALITY]
```

Note the second line is an **identity** (since `Q_{m,N} = 16^m Σ p²` and `H_2 = −log Σ p²`), while the first is a genuine inequality (Rényi-2 ≤ Shannon). There is **no exact finite identity** linking `Q_{m,N}` and the *Shannon* `H_m^N`; the Shannon entropy is not a function of the collision energy alone — the collision energy exactly determines only the Rényi-2 entropy `H_2`, which lower-bounds `H_1`. What *is* exact is the **entropy-rate identity** (ENT) and the **normality ⟺ collision criterion** (MS-02 below). The collision energy `Q_{m,N}` is a *sufficient* instrument for the Shannon entropy rate only through the chain in §3, not through a pointwise identity.

### 2c. Why the "same gate" answer is unavoidable

`H_m` is defined on the **limit measure** `μ`, while `Q_{m,N}` is defined on the **finite empirical measure** `μ_N`. Passing from `Q_{m,N}` to `H_m` requires **two** controlled limits:

```
H_m = lim_N  H_m^N      (μ_N → μ weakly; needs the cylinder continuity),
h_μ  = lim_m  H_m / m.
```

Neither limit is automatic from finite data (cf. MS-04: `Q_{m,N} ≥ max(1, 16^m/N)` always, so sparse sampling inflates `Q` independently of the true entropy).

---

## 3. Does (B) reduce to "liminf H_m/m > 0"? Is it provable from Q_m?

### Answer to the first question: **YES, exactly.**

By (ENT), `h_μ(T_16) > 0 ⟺ liminf_m H_m/m > 0`. Combined with (HD⁺)/(Furstenberg), obligation (B) is implied by the **positive cylinder entropy rate** statement:

```
liminf_{m→∞}  H_m / m  > 0   ⟹   (B) dim_* μ > 0.     [fully classical]
```

So (B) **reduces to** the single clean countable statement `liminf_m H_m/m > 0`. That reduction is classical and carries zero SUCC-specific burden.

### Answer to the second question: **NO — it is the same gate, and here is exactly why.**

The existing SUCC reduction (MS-02, MOVING_SCALE_THEOREM.md) proves the *equivalence between normality and collision-energy decay*:

```
MS-02 (PROVED LOCAL):  for ANY base-16 digit stream,
   (A) stream is normal  ⟺  (B) ∃ m_N → ∞ with log Q_{m_N,N} = o(m_N).
```

But **obligation (B) `dim_* μ > 0` is strictly weaker than normality.** Normality is `μ = Lebesgue` (every cylinder equidistributed, `H_m/m → log 16`, the *maximal* entropy rate). Positive lower dimension only asks that `μ` not be a point mass / not be of dimension zero. A stream can have `dim_* μ > 0` yet be far from normal (e.g. any non-atomic self-similar measure at sub-maximal dimension).

Therefore the collision-energy gate `log Q_{m_N,N} = o(m_N)` (which is the *normality* gate) is **strictly stronger than what (B) needs**. To certify (B) one does *not* need `Q_{m,N} = 16^{o(m)}`; one only needs `H_m/m ≥ c > 0` eventually, equivalently `Σ_w p_m(w)^2 ≤ e^{−c m} · (something)` on the *limit* measure — a far weaker, non-sharp bound. The existing `Q_m` machinery is aimed at the sharp `o(m)` normality threshold, not at the crude "positive rate" threshold.

**Consequence:** proving `liminf H_m/m > 0` for the π orbit **is** the open gate. It is *not* a new object — it is precisely the positive-entropy statement — and it is **weaker** than the MS-03/`log Q = o(m)` normality gate the SUCC reduction is currently set up to prove. There is no free reduction: the SUCC collision machinery, as written, targets a *stronger* conclusion and does not currently contain a proof of the weaker (B) statement either.

---

## 4. The exact chain, link by link

```
(B)   dim_* μ > 0
 ⟸    h_μ(T_16) > 0                        [Furstenberg 1967 / Hochman HD⁺:  PROVED, classical]
 ⟺    lim_m H_m/m > 0                       [Shannon–McMillan / Kolmogorov–Sinai: PROVED, classical]
 ⟺    liminf_m H_m/m > 0                    [limit exists by subadditivity:      PROVED, classical]
 ⟸    "∃ m_N→∞ : log Q_{m_N,N} = o(m_N)"    [MS-02 ⇒ normality ⇒ h = log16:     PROVED (SUCC, local)]
```

**Link classification:**

| Link | Statement | Status | Provenance |
|---|---|---|---|
| L1 | `h_μ(T_16)>0 ⟹ dim_* μ>0` | **classical, proved** | Furstenberg 1967; Hochman 2014 (HD⁺) |
| L2 | `h_μ(T_16) = lim_m H_m/m` (identity) | **classical, proved** | Shannon–McMillan–Breiman; KS via generating `ξ_1` |
| L3 | `∃m_N: log Q_{m_N,N}=o(m_N) ⟹ h>0` | **SUCC reduction, proved** (locally, for any stream) | MS-02 (MOVING_SCALE_THEOREM.md) |
| L4 | `log Q_{m_N,N} = o(m_N)` for the **π orbit** | **OPEN** | MS-03-OPEN; the actual source-selected bound |

**The open gate is L4**, and it is the *same* gate as the π-normality bottleneck already recorded in the SUCC program: the signed two-time cancellation `Σ_{n≤N} e(h U_n) = o(N)` over the moving Fejér band `1 ≤ |h| < H_N ~ N^{1/3}`. There is **no new gate introduced** by the entropy–dimension bridge. What the bridge *adds* is:

1. **(B) is genuinely weaker than normality**, so a *non-sharp* positive-rate bound would already close (B) even if it falls short of normality — a strictly easier target that the existing `Q_m` machinery is not tuned to exploit.
2. The **exact** reduction of (B) to a single countable `liminf H_m/m > 0` statement, which is the clean formulation the route needs.

---

## 5. Claim ledger

| ID | Claim | Status | Notes |
|---|---|---|---|
| ED-01 | `T_16`-invariance of every weak-* limit `μ` of `μ_N` | PROVED (classical) | continuity of `T_16`; standard |
| ED-02 | `h_μ(T_16) > 0 ⟹ dim_* μ > 0` | PROVED (classical) | Furstenberg 1967; Hochman 2014 |
| ED-03 | `h_μ(T_16) = lim_m H_m/m` | PROVED (classical) | SMB / KS, `ξ_1` generates |
| ED-04 | `H_2 ≤ H_1` (Rényi-2 lower bound) for empirical blocks | PROVED (finite, exact) | concavity of log; verified numerically |
| ED-05 | `log Q_{m,N} = m log16 − H_2(m,N)` | PROVED (finite, exact **identity**) | definition of `Q` and `H_2`; verified |
| ED-06 | (B) ⟸ `liminf_m H_m/m > 0` | PROVED (composition of ED-02, ED-03) | classical chain |
| ED-07 | `liminf_m H_m/m > 0` for the π orbit | **OPEN** | positive-entropy gate; not established |
| ED-08 | `log Q_{m_N,N} = o(m_N)` for the π orbit (MS-03) | **OPEN** | the normality gate; strictly stronger than ED-07 |
| ED-09 | Positive dimension ⟹ positive entropy | **FALSE in general** | explicit counterexamples exist (sub-maximal self-similar with exact overlaps); recorded so the asymmetry is not silently upgraded |

**No unproven bound is asserted.** Every "PROVED" entry is classical or a finite exact inequality; every entry touching the π orbit is explicitly OPEN.

---

## 6. Reproducible script

`entropy_dimension_bridge.py` (same directory) computes, for the authentic π orbit at finite `(N, m)`:

- the base-16 digit stream of `{16^{n-1}π}`;
- empirical `m`-cylinder frequencies `p_{m,N}(w)`;
- `H_m^N` (Shannon), `H_2(m,N)` (Rényi-2), `Q_{m,N}`;
- and verifies the finite inequality `H_2 ≤ H_1` (ED-04) and the identity ED-05.

**Run:**
```sh
python3 research/2026-11-02/x3_rigidity_machinery/entropy_dimension_bridge.py
```

**Calibration reading (important):** at fixed `m ~ log_16 N`, the reported `H_m/m` decays toward 0. This is the **MS-04 sample-size firewall** (`Q_{m,N} ≥ 16^m/N`), *not* evidence that the entropy rate is zero. The entropy rate is a **double limit** `lim_m lim_N H_m^N/m`; the single-moving-scale table does not approach it. Finite runs calibrate the implementation only.

---

## 7. Boundary and cheapest next step

**What this note establishes:** the exact classical chain reducing (B) to the countable statement `liminf_m H_m/m > 0`, the asymmetry (positive dimension ⇏ positive entropy), and the precise identification that the SUCC collision-energy gate is a *stronger* (normality) target than (B) requires.

**What it does not establish:** any bound on the π orbit. No `H_m`, no `Q_m` asymptotic, no `dim_* μ` value.

**Cheapest next step:** target the *weaker* (B) directly — seek a **non-sharp positive-rate** certificate `H_m/m ≥ c > 0` for `c ≪ log 16`, rather than the sharp normality decay. Concretely: prove that some fixed small subset of cylinders retains positive `μ`-measure (a "no full concentration" statement), which is weaker than equidistribution and would already close (B). This is a strictly easier arithmetic target than MS-03 and has not been the focus of the existing `Q_m` machinery.
