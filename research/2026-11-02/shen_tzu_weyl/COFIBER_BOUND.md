# The within-cell cofiber of the signed Weyl form: exact structure and decay

**Branch:** `research/shen-tzu-weyl-form-2026-11-02` (subagent fan-out).
**Agent:** Ravel. **Date:** 2026-11-02.
**Question attacked:** Does the within-cell cofiber `C_(N,M)(h)` decay in `M`, and is that
decay controlled by the tail `T_n` alone (provable), or does it require the Diophantine
content of `π`?

## 0. Objects (all proved upstream, WB-01/WB-02)

- Orbit: `U_0 = 0`, `U_{n+1} = 16 U_n + r(n+1)`, `r(n) = 4/(8n-7) − 2/(8n-4) − 1/(8n-3) − 1/(8n-2)`.
- Closed form: `U_n = 16^{n-1}π − T_n`, with the Green tail `T_n = Σ_{j≥1} 16^{-j} r(n+j)`,
  `0 < T_n < (8n+1)^{-2}`, i.e. `T_n = O(1/n²)` (exact leading term `T_n = 1/(64n²) − 7/(512n³) + …`).
- Signed decomposition at resolution `M`:
  ```
  S_N(h)/N = g_M(h) Σ_a e(ha/M)(p_a − 1/M)  +  C_(N,M)(h),
  C_(N,M)(h) = Σ_a e(ha/M) d_(a,h),   d_(a,h) = w_(a,h) − p_a g_M(h),
  g_M(h) = ∫_0^1 e(hs/M) ds,  p_a = #{n ≤ N : a_n = a}/N,  w_(a,h) = (1/N) Σ_{n:a_n=a} e(h s_n/M),
  a_n = ⌊M{U_n}⌋,  s_n = M{U_n} − a_n ∈ [0,1).
  ```

## 1. Exact structure of `s_n` (the within-cell residual)

Since `U_n = 16^{n-1}π − T_n`,

```
{U_n} = {x_n − T_n},   x_n := {16^{n-1}π} ∈ [0,1),  T_n > 0.
```

Because `T_n > 0`, subtracting `T_n` can only *lower* the fractional part, wrapping by at most
one unit. Hence, exactly:

```
{U_n} = x_n − T_n + ε_n,   ε_n := 1[ x_n < T_n ] ∈ {0,1}   (the carry/boundary flag).
```

Therefore the within-cell residual is

```
s_n = M{U_n} − a_n = M(x_n − T_n + ε_n) − a_n,    a_n = ⌊M(x_n − T_n + ε_n)⌋.
```

Two regimes, split by `M·T_n ≶ 1`:

- **Bulk (`M·T_n < 1`, i.e. `n > √M` up to constants):** the tail does *not* cross a bin
  boundary, so `ε_n = 0` and `a_n = ⌊M x_n⌋` (the tail only shifts `x_n` inside its cell).
  Then
  ```
  s_n = M x_n − ⌊M x_n⌋ − M T_n =: σ_n − M T_n,
  ```
  where `σ_n := M x_n − ⌊M x_n⌋ ∈ [0,1)` is the *pure π-phase* within-cell residual
  (equidistributed, O(1)), and `−M T_n` is a **tail perturbation of size `M·O(1/n²)`**.
- **Boundary (`M·T_n ≳ 1`, i.e. `n ≲ √M`):** `ε_n` can be 1 and the bin assignment `a_n`
  itself is tail-sensitive. This affects only `O(√M)` of the `N` points.

**Consequence.** The π-content enters `s_n` through `σ_n = M{16^{n-1}π} − ⌊M{16^{n-1}π}⌋`,
which is *order 1* and equidistributed. The tail enters only as a *perturbation* `M T_n`, small
except for `n ≲ √M`. So `s_n` is **π-phase-dominated, not tail-dominated**, in the bulk.

## 2. Cofiber bound and decay rate

Expand `e(h s_n/M) = e^{2πi h s_n/M}` in the cell. Writing `{U_n} = a_n/M + s_n/M`,
`e(h{U_n}) = e(ha_n/M) e(h s_n/M)`. The cofiber is the *residual* after removing the
cell-mean phase `g_M(h)`:

```
d_(a,h) = (1/N) Σ_{n:a_n=a} [ e(h s_n/M) − g_M(h) ].
```

Taylor-expanding in `s_n/M` (small in the bulk, `s_n/M ≤ 1/M`):

```
e(h s_n/M) = 1 + 2πi h s_n/M + O(h² s_n²/M²),
g_M(h)      = 1 + πi h/M + O(h²/M²)       (from ∫_0^1 e(hs/M) ds).
```

The constant term `1` cancels against `p_a`-weighted `g_M(h)`'s constant term only if
`(1/N)Σ_{n:a_n=a} 1 = p_a` matches — which it does *by definition of `p_a`*. Hence the
**leading surviving term is the first moment of `s_n` within the cell**:

```
d_(a,h) = (2πi h/M) · (1/N) Σ_{n:a_n=a} [ s_n − 1/2 ]  +  O(h²/M²),
```

where `1/2` is the cell midpoint (from `∫_0^1 s ds = 1/2`). Substituting `s_n = σ_n − M T_n`
(bulk), the *tail contribution to the first moment within cell `a`* is

```
tail first-moment = (2πi h/M) · (1/N) Σ_{n:a_n=a} (−M T_n)
                  = −2πi h · (1/N) Σ_{n:a_n=a} T_n,
```

i.e. the `M` **cancels exactly** for the tail part, leaving a term of size `h · (mean of T_n over
the cell) = O(h/n²)`, *summed over cells* — this is `O(h · Σ_n T_n / N) = O(h B/N)` with
`B = Σ T_n ≈ 0.0163`, i.e. **O(1/N) and independent of M**.

Meanwhile the *π-phase* first moment

```
(2πi h/M) · (1/N) Σ_{n:a_n=a} [σ_n − 1/2]
```

does **not** cancel: `σ_n` is equidistributed in `[0,1)` with no `M`-factor, so this term is
`O(h/M)` per cell before any cancellation, and its sum over cells is governed by the
**Weyl/equidistribution of `{16^{n-1}π}` itself** — the same object as `S_N(h)`.

**Result — the cofiber bound.**

```
|C_(N,M)(h)| ≤ |h| · ( B/N + o(1) )   [tail leg]   +   E_π(N,M,h)   [π-phase leg],
```

with `B = Σ_{n≥1} T_n < 1/61` (proved earlier) giving a **provable, M-independent, O(h/N)
tail contribution**, plus a π-phase term `E_π` that is *exactly the fixed-frequency Weyl
cancellation in disguise* and **not controlled by `T_n` alone**.

Empirically (exact Fraction, `N=512`), `|C_(N,M)(h)|` decays `0.002→0.0001` (h=1) and
`0.023→0.0007` (h=5) as `M: 16→256`, but the decay is **oscillatory, not a clean power law**
(`c·M` and `c·M²` both wander), which is the signature of equidistribution (π-phase), not of
a tail-type `O(1/M)` estimate.

## 3. Is the decay provable? — the load-bearing verdict

**No. The cofiber's decay in `M` is NOT controlled by the tail `T_n = O(1/n²)` alone.**

- The *tail leg* of the cofiber is provably `O(h/N)`, independent of `M`, because the `M` in
  `M T_n` cancels against the `1/M` in the Taylor factor. This is a genuine (small) saving, but
  it **does not improve with `M`**.
- The *decay in `M`* observed empirically comes entirely from the **π-phase leg** `E_π`, which is
  the within-cell Weyl average of `σ_n = M{16^{n-1}π} − ⌊M{16^{n-1}π}⌋`. Bounding `E_π = o(1)`
  in `M` (or `N`) is **equivalent to** the fixed-frequency Weyl bound `Σ_{n≤N} e(h·16^{n-1}π)
  = o(N)` — the summit lemma (RL) itself.

Therefore:

> **The within-cell cofiber does NOT reduce the Weyl gate to the cell-imbalance (collision
> energy) leg.** The cofiber carries the same π-Diophantine content as the full sum `S_N(h)`;
> its apparent `M`-decay is the *same* `o(N)` equidistribution, repackaged at resolution `M`, not
> a tail-controlled cancellation. The "weak flank" (cell imbalance) and "strong flank" (cofiber)
> are **the same object**: both need `{16^{n-1}π}` to equidistribute, i.e. both need (RL).

This **refutes** the TWO_LEGS.md strategy premise ("prove the cell-imbalance leg decays, and
separately bound the cofiber leg"). The cofiber leg is not separable — it *is* the Weyl sum.

## 4. Claim ledger

| # | Claim | Status | Evidence |
|---|---|---|---|
| C1 | `{U_n} = x_n − T_n + ε_n`, `ε_n = 1[x_n < T_n]` | **proved** | `T_n>0`, subtraction wraps ≤1 |
| C2 | `s_n = σ_n − M T_n` (bulk), `σ_n` the π-phase residual | **proved** | §1 |
| C3 | tail leg of cofiber is `O(h·B/N)`, `M`-independent | **proved** | §2 Taylor + `M`-cancellation |
| C4 | π-phase leg `E_π` = fixed-freq Weyl in disguise | **proved** | `σ_n = M x_n − ⌊M x_n⌋`, `x_n={16^{n-1}π}` |
| C5 | cofiber decays in M as clean `O(1/M)` power law | **refuted** | oscillatory; `c·M`, `c·M²` wander |
| C6 | cofiber separable from Weyl sum (reduces to cell-imbalance) | **refuted** | C4: `E_π` ≅ `S_N(h)` |
| C7 | cofiber decay provable from `T_n=O(1/n²)` alone | **refuted** | requires (RL) |

## 5. Boundary (brutally honest)

- I have **not** proven the Weyl cancellation; I have *located* it: the cofiber's `M`-decay is
  `E_π`, the fixed-frequency Weyl average of `{16^{n-1}π}`, and is **not** tail-controlled.
- The `M`-cancellation for the tail leg (C3) is real but `O(1/N)` — it never yields `o(N)`
  savings by itself, and is *independent* of `M`.
- The parent's empirical table is **reproduced exactly** (0.00197/0.02258 at M=16; 0.000125/
  0.000650 at M=256), so the *numbers* are correct; but the *interpretation* ("cofiber provably
  → 0 in M, reduces the gate") is **wrong** — the decay is the Weyl sum, not a free tail bound.
- π base-16 normality and RH remain **OPEN**. No normality claim is made or implied here.
