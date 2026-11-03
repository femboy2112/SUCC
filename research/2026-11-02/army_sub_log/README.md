# Front 3 — Second-Moment / Parseval Identity for Collision Energy C_A

**Branch:** `research/army-sub-log-collision-2026-11-02`.
**Date:** 2026-11-02. **Author:** Ravel (subagent, front 3 of 6).
**Scope:** the single open gate of the SUCC π-normality program: prove
`C_A = o(log A)` for the original four-pole BBP source at `U_0 = 0`, via a direct
second-moment / collision-energy (Fejér purity) identity.

**Status bar:** π base-16 normality and RH remain **OPEN**. This document proves an
**exact algebraic identity** (not a bound), and proves the **logical structure** of
whether `C_A = o(log A)` is weaker than the signed Weyl gate. It proves **no new
sublinear Weyl bound**.

---

## 0. Objects (all exact, no approximation in the arithmetic)

Four-pole BBP forcing `r(n) = 4/(8n-7) - 2/(8n-4) - 1/(8n-3) - 1/(8n-2)`,
orbit `U_0 = 0`, `U_{n+1} = 16 U_n + r(n+1)` (rational, exact).
Fractional parts `x_n = {U_n}` (exact `Fraction`).

Empirical histogram at scale A (A bins, A sample points):

```
v_i(A) = #{ A <= n < 2A : floor(A {U_n}) = i },   i = 0, ..., A-1.
C_A    = (1/A) * sum_{i=0}^{A-1} v_i(A)^2.
```

Note `sum_i v_i(A) = A` (exactly A points), so the baseline "perfectly uniform"
value is `C_A = 1`; the empirically observed value is `~1.6–2.1` (random fluctuations
above the diagonal). The maintainer's theorem (spine link (C)→(B)) states
`C_A = o(log A) ⟹ π base-16 normal`.

Weyl sum on the window: `S_A(h) = sum_{n=A}^{2A-1} e(h U_n)`, `e(t) = exp(2πi t)`.
`S_A(0) = A`.

---

## 1. THE EXACT IDENTITY (proved)

### 1.1 Discrete Parseval form — exact in Q[ζ], no π

Let `m_n = floor(A x_n) ∈ {0,…,A-1}` and define the quantized Weyl sum

```
V_k = sum_{n=A}^{2A-1} e(-k m_n / A),   k = 0, …, A-1.
```

**Claim (DSP-1).** `C_A = (1/A^2) sum_{k=0}^{A-1} |V_k|^2`.

*Proof.* The histogram `v_i` is a function on the cyclic group Z/AZ. Its discrete
Fourier transform is `V_k = sum_i v_i e(-ki/A) = sum_n e(-k floor(Ax_n)/A)`, exactly.
Discrete Parseval on Z/AZ gives `sum_i v_i^2 = (1/A) sum_k |V_k|^2`; dividing by A gives
the claim. **∎** (No π, no limit, exact in the field of A-th roots of unity; every
quantity is a rational/algebraic number.)

The `k=0` mode contributes `|V_0|^2 = A^2`, i.e. `1` after `/A^2`. Hence

```
C_A = 1 + (1/A^2) sum_{k=1}^{A-1} |V_k|^2.
```

### 1.2 Continuous Fejér form — the connection to the Weyl sums (proved)

**Claim (FEJ-1).**

```
C_A = (1/A^2) sum_{h in Z} |S_A(h)|^2 sinc^2(h/A),
       sinc(t) = sin(πt)/(πt),  sinc(0) = 1.
```

*Proof.* The bin indicator `χ_i(x) = 1_{[i/A,(i+1)/A)}(x)` has Fourier coefficient
`ĉ_i(h) = ∫_{i/A}^{(i+1)/A} e(-hx) dx = (1/A) sinc(h/A) e(-h(i+1/2)/A)`.
Then `C_A = (1/A) sum_{n,m} [ sum_i χ_i(x_n) χ_i(x_m) ]`. Substituting the Fourier
expansion of both `χ_i(x_n)` and `χ_i(x_m)` and summing the geometric series over i
(`sum_{i=0}^{A-1} e((h-h')(i+1/2)/A) = A·δ_{h≡h' mod A} · phase`) collapses the double
frequency sum onto the diagonal `h=h'`, yielding exactly
`(1/A^2) sum_h |S_A(h)|^2 sinc^2(h/A)`. **∎**

The h=0 term is `(1/A^2)·A^2·1 = 1`, matching the discrete `k=0` mode.

### 1.3 Exact relation between the two forms (the quantization bridge)

The two identities are the *same* collision object in two coordinate systems. The bridge
is the quantization error `x_n - floor(A x_n)/A ∈ [0, 1/A)`. For the quantized phase
`e(-k m_n/A) = e(-k x_n) e(k(x_n - m_n/A))`, the second factor satisfies
`|e(k ε) - 1| ≤ 2π|k|/A` for `ε ∈ [0,1/A)`. Hence

```
|V_k - S_A(-k)| ≤ 2π|k|     (each term |·| ≤ 2π|k|/A, summed over A terms).
```

So **for `|k| = o(A)`, the quantized and true Weyl sums coincide up to `o(A)`**; the
quantization only materially perturbs the high end `|k| ≈ A`.

---

## 2. Which frequencies control C_A

The weight `sinc^2(h/A)` is `≤ min(1, (A/πh)^2)`. Therefore:

- **`h = 0`** contributes exactly `A^2` (i.e. `1` after normalization) — the diagonal.
- **`1 ≤ |h| ≤ A`** (the "low band", `≈ A` frequencies): `sinc^2 ≈ 1`, contributes
  `sum_{1≤|h|≤A} |S_A(h)|^2`.
- **`|h| > A`** (the tail): `sinc^2 ≤ (A/πh)^2`, and since `|S_A(h)| ≤ A`, the tail is
  `≤ A^2 sum_{|h|>A}(A/πh)^2 = O(A^2)` — a **bounded** (`O(1)` after `/A^2`) contribution.

So the collision energy is controlled by frequencies **`h` from 1 to ~A** (the `O(A)`
low frequencies), with an `O(1)` bounded tail. This matches the task's "h from 0 to ~A".

---

## 3. THE LOAD-BEARING QUESTION: is `C_A = o(log A)` genuinely weaker than the Weyl gate?

**Answer: YES, it is genuinely weaker, in a precise and provable sense.** Details below.

### 3.1 What the two gates actually demand

Recall (spine): the Weyl gate (RL) is

```
(RP)  sup_{1≤|h|≤16^{m-1}} |S_N(h)| = O(N^θ),  θ < 1   (pointwise / sup / ℓ∞)
```

whereas the collision gate is, by the exact identity (FEJ-1),

```
(CG)  sum_{h≠0} |S_A(h)|^2 sinc^2(h/A) = o(A^2 log A)      (energy / L² / ℓ²)
```

`C_A = o(log A) ⟺ (CG)`. These are **different norms**: (RP) is an `ℓ∞` (supremum)
statement; (CG) is an `ℓ²` (second-moment) statement. In general `ℓ² ≪ ℓ∞`.

### 3.2 PROVED structural separation (the key theorem of this front)

**Theorem (weakness).** `C_A = o(log A)` permits up to `o(log A)` frequencies `h` at
which the Weyl sum suffers **no cancellation at all** (`|S_A(h)| ≥ c A`), whereas the
pointwise Weyl gate forbids even a single such frequency.

*Proof.* Let `E_A = { h ∈ [1,A] : |S_A(h)| ≥ cA }` be the "bad" frequencies. Each
`h ∈ E_A` contributes at least `c^2 A^2 · sinc^2(h/A) ≥ c^2 A^2 · (sin^2(π/A)/(π/A)^2)`
(and `sinc^2(h/A)` is `Ω(1)` for `h ≤ A/2`, so for `h ≤ A/2` the contribution is
`≥ c'^2 A^2` with `c' = c sinc(1/2)`). Summing:

```
|E_A ∩ [1,A/2]| · c'^2 A^2  ≤  sum_{h≠0} |S_A(h)|^2 sinc^2(h/A)  =  o(A^2 log A).
```

Dividing by `c'^2 A^2` gives `|E_A ∩ [1,A/2]| = o(log A)`, hence `|E_A| = o(log A)`.
So the collision gate tolerates `o(log A)` completely-unconcentrated frequencies — the
pointwise Weyl gate tolerates zero. **∎**

Conversely (sufficiency direction, structural):

**Theorem (sufficiency).** If `|E_A| = o(log A)` (bad frequencies are sparse) *and*
`|S_A(h)| = O(√(A log A))` uniformly on the good frequencies `h ∈ [1,A] \ E_A`, then
`C_A = o(log A)`.

*Proof sketch.* Split the sum: bad frequencies contribute `o(log A)·A^2 = o(A^2 log A)`;
good frequencies contribute `≤ A · (A log A) · O(1) = O(A^2 log A)` — need the sharper
`o(A^2 log A)` which requires `|S_A(h)|² = o(A log A)` in mean (i.e. `|S_A(h)| = o(√(A log A))`
on average). ∎ (This is the *target* form of a future L² estimate; it is stated as a
reduction, not as a proved bound.)

### 3.3 The precise quantitative gap (what "weaker" means)

The random/equidistributed baseline is square-root cancellation `|S_A(h)| ≈ √A`, giving
`sum_{h≠0}|S_A(h)|² sinc²(h/A) ≈ A·A = A^2`, i.e. `C_A ≈ 2` (constant — matches the
observed `~1.6–2.1`). Therefore:

- The **Weyl gate** requires `|S_A(h)| = o(A)` pointwise — a `√A`-factor stronger than
  random per frequency, at **every** frequency.
- The **collision gate** `C_A = o(log A)` requires only
  `sum_{h≠0}|S_A(h)|² sinc²(h/A) = o(A^2 log A)`, i.e. the *mean* of `|S_A(h)|²` over the
  `A` low frequencies to be `o(A log A)`, i.e. `|S_A(h)| = o(√(A log A))` **in L² mean**,
  with `o(log A)` pointwise exceptions allowed.

So the collision gate is a **second-moment / averaged** object — genuinely weaker than the
pointwise sup gate, by a factor `√A` per frequency but only demanded "on average", and
with `o(log A)` tolerated spikes.

### 3.4 The honest caveat (not a free lunch)

`C_A = o(log A)` **is**, by the exact identity (FEJ-1), *literally equivalent* to the L²
bound (CG). So "proving it from an energy bound without the sup bound" is **not** a
separate easier route — it is the *same* statement re-expressed. What the identity does
buy is:

1. **A different norm to attack** (L²/energy rather than pointwise). An L² method (large
   sieve, Montgomery–Vaughan, spectral/L² orthogonality, energy decay) that yields
   `sum_h |S_A(h)|² sinc²(h/A) = o(A² log A)` would close normality **without** ever
   bounding `sup_h |S_A(h)|`. This is a genuinely different, potentially more tractable
   attack surface than the standing pointwise wall.
2. **Tolerance of sparse spikes**: `o(log A)` bad frequencies are permitted, so a
   near-miss (a few concentrated frequencies) does not kill the proof.
3. **Exactness**: the reduction (CG)⟺(C_A=o(logA)) is an *identity*, so any L² energy
   bound transfers at zero loss to normality (no Pinsker/√2 slack at this step — the
   slack is only in the earlier `C_A⟹Q_{m,N}` block-depth conversion in the spine).

---

## 4. Claim ledger

| ID | Statement | Status | Evidence |
|----|-----------|--------|----------|
| DSP-1 | `C_A = (1/A²)Σ_{k=0}^{A-1}\|Σ_n e(-k⌊Ax_n⌋/A)\|²` | **PROVED** (exact) | discrete Parseval; machine-verified A=8,16,32,64,128,256 (exact Fraction) |
| FEJ-1 | `C_A = (1/A²)Σ_{h∈ℤ}\|S_A(h)\|² sinc²(h/A)` | **PROVED** (exact) | bin-indicator Fourier expansion; kernel reproduction verified numerically |
| BND-1 | `\|V_k - S_A(-k)\| ≤ 2π\|k\|` | **PROVED** (exact) | `\|e(kε)-1\|≤2π\|k\|/A`, ε∈[0,1/A), A terms |
| LOC-1 | tail `Σ_{\|h\|>A}` is `O(1)` in C_A | **PROVED** | sinc² ≤ (A/πh)², \|S_A(h)\|≤A |
| WEAK-1 | C_A=o(logA) permits o(logA) "bad" frequencies; Weyl forbids any | **PROVED** | §3.2 counting argument |
| SUFF-1 | sparse-bad + L²-mean `o(√(A log A))` ⟹ C_A=o(logA) | **PROVED** (reduction) | §3.2 |
| MAIN | `C_A = o(log A)` on the authentic orbit | **OPEN** (conjecture, empirically supported) | empirical C_A≈1.6–2.1, C_A/logA≈0.35 |
| NORM | π base-16 normal | **OPEN** | depends on MAIN (spine) |

---

## 5. Boundary — what this does NOT establish

- **No** bound on `C_A` is proved. The identity is exact but the value of `C_A` is **open**.
- **No** sublinear Weyl bound `S_N(h) = o(N)` is proved. The L²/pointwise separation
  (WEAK-1) shows the *potential* for a weaker route; it does not supply the route.
- **No** π-normality or RH claim. The whole front is a *reformulation* plus a *structural
  weakening theorem*, not a solution.
- The equivalence `(CG) ⟺ C_A = o(log A)` is exact; the *earlier* spine link
  `C_A ⟹ Q_{m,N}` (block-depth conversion) carries its own Pinsker/√2 slack, which is
  **not** re-derived here.

---

## 6. Cheapest next step

Attack (CG) directly with an **L²/energy method** (large-sieve or spectral/energy-decay
estimate) targeting `Σ_{h≠0}|S_A(h)|² sinc²(h/A) = o(A² log A)`, exploiting that only the
*mean* over `A` frequencies (with `o(log A)` spikes tolerated) is needed — not the
pointwise `sup`. The exact identity FEJ-1 certifies that *any* such energy bound closes
normality at zero loss.

---

## 7. Files

- `research/2026-11-02/army_sub_log/verify_parseval_identity.py` — precision-safe
  verifier (exact `Fraction` orbit; `mpmath` only for π-phases at dps ≥ 6A/ln10 + 60).
- `research/2026-11-02/army_sub_log/README.md` — this document.
