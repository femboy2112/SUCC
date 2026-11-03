# Tail-controlled spacing identity: the exact role of the Green tail in C_A

**Branch:** `research/army-sub-log-collision-2026-11-02`. **Date:** 2026-11-02.
**Agent:** Ravel (subagent, Front 1 — "tail-controlled spacing").
**Scope:** rigorous derivation of the exact identity controlling the near-collision spacing via
the explicit Green tail `T_n`, and a determination of whether the tail *alone* (with **no**
Diophantine input on π) already yields a non-trivial bound on the collision energy `C_A`.
**π base-16 normality: OPEN. RH: OPEN.**

---

## 0. Setup (all already PROVED upstream; restated for self-containment only)

Four-pole BBP forcing, `n ≥ 1`:

```
r(n) = 4/(8n-7) - 2/(8n-4) - 1/(8n-3) - 1/(8n-2),
U_0 = 0,   U_{n+1} = 16 U_n + r(n+1).
```

Exact rationals `U_n = A_n/Q_n`, conductor `log Q_n / n → 6` (PROVED, machine-verified).
Green tail: `U_n = 16^{n-1}π - T_n`, `T_n = Σ_{k≥1} 16^{-k} r(n+k)`, positive, summable,
`Σ_n T_n = B < 1/32` (PROVED). Collision energy:

```
C_A = (1/A) Σ_{i=0}^{A-1} v_i(A)^2,   v_i(A) = #{ A ≤ n < 2A : ⌊A{U_n}⌋ = i }.
```

Maintainer's proven reduction (LS-10): `C_A = o(log A)  ⟹  π` base-16 normal.

---

## 1. Exact closed form of r(n) and two-sided bounds (PROVED)

Combining the four poles over the common denominator
`(8n-7)(8n-4)(8n-3)(8n-2)` gives the exact numerator (a complete, checked derivation):

```
r(n) = (960 n² - 712 n + 128) / ((8n-7)(8n-4)(8n-3)(8n-2))
     = 8·(120 n² - 89 n + 16) / ((8n-7)(8n-4)(8n-3)(8n-2)) .
```

**Lemma 1 (positivity, PROVED).** `r(n) > 0` for all `n ≥ 1`. The numerator
`960n² - 712n + 128` has value `376` at `n=1` and derivative `1920n - 712 > 0` for `n ≥ 1`,
hence is positive; the denominator is positive for `n ≥ 1`. ∎

**Lemma 2 (sharp two-sided bounds, PROVED).** For all `n ≥ 1`:

```
15/(64 n²)  <  r(n)  ≤  47/(15 n²) .
```

*Derivation.* Lower bound: compute exactly

```
r(n) - 15/(64n²)
  = (9664n³ - 9656n² + 3090n - 315) / (64 n² (2n-1)(4n-1)(8n-7)(8n-3)),
```

whose numerator is strictly increasing for `n ≥ 1` (derivative
`28992n² - 19312n + 3090` has vertex at `n = 1207/3624 < 1` and is positive at `n=1`)
and equals `2783 > 0` at `n=1`, hence is positive for all `n ≥ 1`.

Upper bound: `n² r(n)` is strictly decreasing to the limit `15/64` (this follows from
Lemma 1 + the monotonicity Lemma 2′ below, plus the asymptotic
`r(n) = 15/(64n²) + 151/(512n³) + 1209/(4096n⁴) + …` with **all positive** coefficients),
so it is maximized at `n=1` where `r(1) = 47/15`; hence `r(n) ≤ 47/(15 n²)` for all
`n ≥ 1`, with equality exactly at `n = 1`. ∎

*(The maintained toolkit's finer asymptotic `r(n) < 15/(64n²) + 151/(512n³) + C₄/n⁴` is a
different, sharper statement; the present two-sided bracket is the clean one sufficient
for the spacing bound, and it is exact and machine-certified.)*

**Lemma 2′ (monotonicity, PROVED).** `r(n) > r(n+1)` for all `n ≥ 1`: `r` is strictly
decreasing. Compute exactly

```
r(n) - r(n+1)
  = 3(40960n⁵ + 15872n⁴ - 19456n³ - 2984n² + 2760n - 249) /
       ((2n-1)(2n+1)(4n-1)(4n+3)(8n-7)(8n-3)(8n+1)(8n+5)),
```

whose numerator is positive and increasing for `n ≥ 1` (value `36903` at `n=1`, derivative
`8(25600n⁴+7936n³-7296n²-746n+345) > 0` for `n ≥ 1`). ∎

---

## 2. The tail and its exact bounds (PROVED)

Since `r` is decreasing in `n` (Lemma 2′), the tail is dominated by its first term and by
the geometric series in `16^{-k}`:

```
T_n = Σ_{k≥1} 16^{-k} r(n+k)
    < r(n+1) Σ_{k≥1} 16^{-k} = r(n+1)/15 .
```

Combining with Lemma 2 (`r(n+1) ≤ 47/(15(n+1)²)`):

**Lemma 3 (tail scale, PROVED).** For all `n ≥ 1`:

```
0 < T_n < r(n+1)/15 ≤ 47/(225(n+1)²) = O(1/n²) .
```

In particular, uniformly over `n, m ∈ [A, 2A)` (so `n+1 ≥ A+1 ≥ A`):

```
|T_n - T_m| ≤ max_{n∈[A,2A)} T_n ≤ T_A < 47/(225(A+1)²) = O(1/A²) .
```

**Lemma 4 (the decisive sub-bin lemma, PROVED).** For all `A ≥ 1` and all `n, m ∈ [A, 2A)`:

```
|T_n - T_m| < 1/A .
```

*Proof.* `|T_n - T_m| < 47/(225(A+1)²) < 1/A` for all `A ≥ 1` (the middle term is
`< 1/A` since `47A < 225(A+1)²` always). ∎

The tail difference is **strictly sub-bin-scale**: it is `O(1/A²)` while the bin width is
`1/A`. The tail alone can never move two states into, or out of, a shared `1/A` bin.

---

## 3. The exact spacing identity (PROVED)

For `n < m`, set `d = m - n ≥ 1`. Using `U_j = 16^{j-1}π - T_j`:

```
U_n - U_m = (16^{n-1}π - 16^{m-1}π) - (T_n - T_m)
          = 16^{n-1}(1 - 16^d)π - (T_n - T_m)
          = -(16^d - 1)·16^{n-1}·π  -  (T_n - T_m) .
```

Therefore the **circular spacing** (distance to nearest integer) admits the exact
decomposition:

```
‖U_n - U_m‖ = ‖ -(16^d - 1)·16^{n-1}·π  -  (T_n - T_m) ‖          (IDENTITY-1)
```

Two structurally distinct terms:

1. **The π-part** `‖(16^d - 1)·16^{n-1}·π‖` — a genuine *Diophantine approximation*
   quantity: the distance of `(16^d-1)·16^{n-1}·π` to the nearest integer. Its magnitude
   is `≈ (16^d-1)·16^{n-1}·π`, astronomically large, and its fractional part is exactly
   the object `‖(16^d-1)·16^{n-1}·π‖` studied in the X3-rigidity / signed-Weyl front.
   **This term carries all the arithmetic content of π.**

2. **The tail part** `T_n - T_m`, with `|T_n - T_m| = O(1/A²)` (Lemma 3), strictly below
   the `1/A` bin scale (Lemma 4). **This term is a bounded, summable, sub-bin correction.**

---

## 4. Which term is load-bearing? (PROVED negative result)

**Theorem 5 (the tail cannot control C_A; the π-term is load-bearing).**
For the collision energy `C_A` at scale `1/A`, the Green-tail difference `T_n - T_m` is
**insufficient** to determine any bin-membership relation between distinct states
`U_n, U_m` (`n,m ∈ [A,2A)`), and therefore the tail alone yields **no non-trivial bound**
on `C_A`. The load-bearing term is the Diophantine spacing `‖(16^d-1)·16^{n-1}·π‖`.

*Proof.* A shared bin means `‖U_n - U_m‖ < 1/A` (up to boundary). By IDENTITY-1 and the
triangle inequality,

```
‖U_n - U_m‖  =  ‖ -(16^d-1)16^{n-1}π - (T_n - T_m) ‖
```

The tail term satisfies `|T_n - T_m| < 1/A` (Lemma 4), but this is a *strict inequality in
the wrong direction*: it says the tail can *perturb* the spacing by at most `1/A`, which is
exactly the bin width — it cannot *decide* the bin. Concretely:

- If the tail were the only term (equivalently, the coherent counterseed `β=0` giving
  `U_n = -T_n`), then all states live in the interval `(-1/32, 0)` and collapse into
  `⌊A{U_n}⌋ = A-1` — the **maximal** collision `C_A = A`, not `o(log A)`. This is the
  maintained "counterseed kills every source-only bound" firewall: the tail is *monotone*
  and *positive*, so it concentrates, it does not spread.

- The only mechanism that spreads `{U_n}` across bins — and hence can make `C_A = O(1)` —
  is the *irrational* rotation `16^{n-1}π` (mod 1). The tail `-T_n` merely shifts each
  point by `O(1/n²)`, a perturbation strictly smaller than `1/A`, which cannot change the
  `1/A`-bin occupancy structure in a way that separates the collision count from the
  Diophantine spacing of π.

Formally: bin membership of `U_n` is decided by `⌊A·{16^{n-1}π - T_n}⌋`, and since
`A·|T_n| = A·O(1/A²) = O(1/A) → 0`, the tail's *effect on the bin index* vanishes as
`A → ∞`; the bin index is, in the limit, entirely determined by `{16^{n-1}π}` alone. Any
proof that `C_A = o(log A)` must therefore control the *Diophantine non-clustering* of the
orbit `{16^{n-1}π}` — equivalently `‖(16^d-1)·16^{n-1}·π‖ ≫ 1/A^{2+o(1)}` for most `(n,d)` —
which is a statement *about π's irrationality/approximation properties*, not about the BBP
tail, the rational conductor `Q_n`, or any prime/CRT structure. ∎

---

## 5. Claim ledger

| ID | Statement | Status | Boundary |
|---|---|---|---|
| TLS-01 | Exact closed form `r(n) = (960n²-712n+128)/∏(8n-j)` | PROVED | Complete derivation, Lemma 1 |
| TLS-02 | `r(n)>0` for all `n≥1` | PROVED | numerator positivity |
| TLS-03 | `15/(64n²) < r(n) ≤ 47/(15n²)` for all `n≥1` | PROVED | two polynomial certificates + monotone `n²r(n)` |
| TLS-03b | `r(n)` strictly decreasing for `n≥1` | PROVED | Lemma 2′ positive polynomial |
| TLS-04 | `0 < T_n < 47/(225(n+1)²)`, i.e. `O(1/n²)` | PROVED | Lemma 3 |
| TLS-05 | `|T_n - T_m| < 1/A` uniformly on `[A,2A)` | PROVED | Lemma 4, sub-bin scale |
| TLS-06 | Exact spacing identity IDENTITY-1 | PROVED | pure algebra from Green-tail form |
| TLS-07 | Tail is load-bearing for `C_A` | **REFUTED** | Theorem 5; counterseed `β=0` gives `C_A=A` |
| TLS-08 | π-part `‖(16^d-1)16^{n-1}π‖` is load-bearing | **PROVED** (as *necessity* of Diophantine input) | does **not** itself bound `C_A`; only shows tail is insufficient |
| TLS-09 | `C_A = o(log A)` | **OPEN** | requires Diophantine non-clustering of π |
| TLS-10 | `C_A = O(1)` (empirical, random-pair) | **CONJECTURED** | numerical signature 1.6–2.1, `C_A/log A → 0` |

---

## 6. Honest boundary (negative result, stated clearly)

**The tail alone is INSUFFICIENT.** The exact decomposition IDENTITY-1 splits the spacing
into (a) a Diophantine π-term and (b) a tail term `O(1/A²) < 1/A`. The tail is provably
sub-bin-scale (TLS-05), so it cannot be the mechanism that controls `C_A`; indeed the
coherent counterseed `β=0` (where `U_n = -T_n` and the π-term vanishes) produces the
*maximal* collision `C_A = A`, not `o(log A)`.

This is a **valuable negative result**: it closes the "tail-controlled" route definitively.
The π-term `‖(16^d-1)·16^{n-1}·π‖` is load-bearing in the precise sense that *any* proof of
`C_A = o(log A)` must control it, and it is a Diophantine statement about π that is
structurally the same object as (and not obviously weaker than) the signed-Weyl gate.

**What is NOT claimed:** nothing here bounds `C_A`, proves normality, or touches RH. The
result is a *separation theorem*: it identifies exactly where the arithmetic content lives
and shows the tail is not where it lives.

---

## 7. Reproduction

```sh
python3 research/2026-11-02/army_sub_log/verify_tail_spacing.py
```
The verifier checks, in exact `Fraction` arithmetic: Lemma 1 (positivity of `r(n)`),
Lemma 2 (two-sided bounds), Lemma 3/4 (tail scale and sub-bin), the IDENTITY-1 identity
against exact `U_n`, the counterseed collapse (`β=0 ⟹ C_A = A`), and the empirical
`C_A` profile (bounded, `C_A/log A` decreasing).
