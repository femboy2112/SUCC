# Two-sided interval certificate for the Green-tail mass `B = Σ_{n≥1} T_n`

**Branch:** `research/green-tail-sharpening-2026-11-02`. **Date:** 2026-11-02.

**Scope.** A *provable* (not merely numerical) two-sided bracket for the Green-tail mass
`B = Σ_{n≥1} T_n`, with (i) explicit-rational constant bounds on each `T_n`, and (ii) explicit
rational endpoints bracketing `B` to more than 6 decimals. Every inequality is proved with the
elementary tools: `r` positive and decreasing, `r(n) ≤ 15/(64(n−1)²)`, geometric tails, and
integral comparison. **No normality claim; π-normality and RH remain OPEN.**

---

## 0. Objects and standing facts (established, not re-derived here)

- `r(m) = 4/(8m−7) − 2/(8m−4) − 1/(8m−3) − 1/(8m−2)`, the four-pole BBP forcing. Exact closed form

  $$
  r(m)=\frac{120m^2-89m+16}{(2m-1)(4m-1)(8m-7)(8m-3)} .
  $$

- `T_n = Σ_{j≥1} 16^{−j} r(n+j)` (the Green tail), and `B = Σ_{n≥1} T_n`.
- Classical BBP: `Σ_{m≥1} 16^{−(m−1)} r(m) = π`.
- Exact identity (PROVED in `GREEN_TAIL_SHARPENING.md`): `B = (S−π)/15`, where `S = Σ_{m≥1} r(m)`.

We rely only on the elementary consequences below, each re-proved in place.

---

## 1. Lemma A — `r` is positive and strictly decreasing

**Statement.** `r(m) > 0` for all `m ≥ 1`, and `r(m) > r(m+1)` for all `m ≥ 1`.

**Proof.** (i) Positivity. The numerator `120m²−89m+16` has discriminant
`89²−4·120·16 = 241`, and its two real roots solve `m = (89 ± √241)/240 ≈ (89 ± 15.52)/240`,
i.e. `m ≈ 0.306` and `m ≈ 0.436`. Both roots are `< 1`, and the numerator is `> 0` at `m=1`
(value `47`), so `120m²−89m+16 > 0` for every integer `m ≥ 1`. Each denominator factor
`(2m−1),(4m−1),(8m−7),(8m−3)` is positive for `m ≥ 1` (minima `1,3,1,5` respectively). Hence
`r(m) > 0`. ∎

(ii) Monotonicity. Put `Δ(m) = r(m) − r(m+1)`. Exact rational simplification gives

$$
\Delta(m)=\frac{3\,P(m)}{(2m-1)(2m+1)(4m-1)(4m+3)(8m-7)(8m-3)(8m+1)(8m+5)},
$$

with `P(m) = 40960m^5 + 15872m^4 − 19456m^3 − 2984m^2 + 2760m − 249`. The denominator is
positive for `m ≥ 1`. All five real roots of `P` lie in `(−0.7, 0.44)`, i.e. strictly below `1`,
and `P(1) = 36903 > 0`; since `P` has positive leading coefficient and no real root at or above
`1`, `P(m) > 0` for all `m ≥ 1`. Hence `Δ(m) > 0`, i.e. `r(m) > r(m+1)`. ∎

*(Numerically: roots ≈ −0.6919, −0.5627, 0.1130, 0.3145, 0.4396.)*

---

## 2. Lemma B — two-sided constant bounds on `T_n`

**Statement.** For all `n ≥ 1`,

$$
\boxed{\ \frac{424/819}{64\,n^2}\ \le\ T_n\ \le\ \frac{1}{64\,n^2}\ }
\qquad\text{i.e.}\quad c_1=\frac{424}{819},\ \ c_2=1 .
$$

**Proof.**

*Upper bound.* Because `r` is decreasing (Lemma A), `r(n+j) ≤ r(n+1)` for `j ≥ 1`, so

$$
T_n=\sum_{j\ge1}16^{-j}r(n+j)\le r(n+1)\sum_{j\ge1}16^{-j}=\frac{r(n+1)}{15}.
$$

It remains to bound `r(n+1)`. We claim

$$
r(n+1)<\frac{15}{64\,n^2}\quad (n\ge1).
$$

Define `f(n)=64\,n^2 r(n+1)`. Exact algebra gives

$$
f(n)=\frac{64\,n^2(120n^2+151n+47)}{(2n+1)(4n+3)(8n+1)(8n+5)},
\qquad
15-f(n)=\frac{5696n^3+7672n^2+2910n+225}{(2n+1)(4n+3)(8n+1)(8n+5)}>0,
$$

since every coefficient in the numerator is positive and the denominator is positive for
`n ≥ 1`. Thus `f(n) < 15`, i.e. `r(n+1) < 15/(64n²)`. Therefore

$$
T_n\le\frac{r(n+1)}{15}<\frac{15}{64\,n^2}\cdot\frac1{15}=\frac{1}{64\,n^2}.
$$

*Lower bound.* Dropping all terms `j ≥ 2` (all positive, by Lemma A),

$$
T_n\ge 16^{-1}r(n+1)=\frac{r(n+1)}{16}.
$$

We claim `r(n+1) ≥ 6784/(819·64)·(1/n²)` for `n ≥ 1`. With `f(n)=64 n² r(n+1)` as above, this is
`f(n) ≥ f(1) = 6784/819`. Indeed the same exact form shows

$$
f(n+1)-f(n)=\frac{64\,Q(n)}{(2n+1)(2n+3)(4n+3)(4n+7)(8n+1)(8n+5)(8n+9)(8n+13)},
$$

with `Q(n)=45568n^6+259456n^5+572808n^4+615308n^3+328475n^2+77097n+4770`, all coefficients
positive, so `f` is strictly increasing. Hence `f(n) ≥ f(1) = 6784/819`. Therefore

$$
T_n\ge\frac{r(n+1)}{16}\ge\frac{6784}{819\cdot64\cdot16}\cdot\frac1{n^2}
=\frac{6784}{838656}\cdot\frac1{n^2}
=\frac{53}{6552}\cdot\frac1{n^2}.
$$

Writing the bound in the requested form `c_1/(64 n²)`, note the exact identity
`(53/6552)·64 = 3392/6552 = 424/819`, so

$$
T_n\ge\frac{53}{6552\,n^2}=\frac{424/819}{64\,n^2},\qquad c_1=\frac{424}{819}=0.517704\ldots .
$$

Thus `c_1 = 424/819`, `c_2 = 1`, and

$$
\frac{424/819}{64\,n^2}\le T_n\le\frac{1}{64\,n^2}.
$$

∎

*(The lower constant `c_1 = 424/819` is uniform and strictly positive; the chain `T_n ≥ r(n+1)/16 ≥ 53/(6552 n²)` is tightest at `n=1` where `f(1)=6784/819`.)*

---

## 3. Exact rational two-sided bracket for `B`

We bound `B = (S−π)/15` with rational endpoints by bracketing `S` and `π` independently.

### 3.1 Bracket `S = Σ_{m≥1} r(m)`

`r` is positive decreasing (Lemma A), so for any integer `M ≥ 1`,

$$
S_M:=\sum_{m=1}^{M}r(m)\ \le\ S\ \le\ S_M+\sum_{m>M}r(m).
$$

For the tail, use the elementary comparison `r(m) ≤ 15/(64(m−1)²)` for `m ≥ 2` (this is
Lemma B's `f(n)<15` restated with `m=n+1`), so

$$
\sum_{m>M}r(m)\le\frac{15}{64}\sum_{m>M}\frac1{(m-1)^2}
=\frac{15}{64}\sum_{k\ge M}\frac1{k^2}
<\frac{15}{64}\int_{M-1}^{\infty}\frac{dx}{x^2}=\frac{15}{64}\cdot\frac{1}{M-1}.
$$

(The integral comparison is valid because `x↦x^{−2}` is decreasing and
`Σ_{k≥M} k^{−2} < ∫_{M−1}^{∞} x^{−2} dx = 1/(M−1)`.) Hence

$$
\boxed{\ S_M\ \le\ S\ <\ S_M+\frac{15}{64(M-1)}=:S_M+\varepsilon_M\ } .
$$

### 3.2 Bracket `π = Σ_{m≥1} 16^{−(m−1)} r(m)`

Similarly, with `π_K := Σ_{m=1}^{K} 16^{−(m−1)} r(m)` (an exact rational),

$$
\pi_K\le\pi\le\pi_K+\sum_{m>K}16^{-(m-1)}r(m)
<\pi_K+16^{-K}\frac{15}{64}\cdot\frac1{K-1}
=:\pi_K+\delta_K .
$$

using `16^{−(m−1)} ≤ 16^{−K}` for `m > K` and the same tail estimate.

### 3.3 Combining

Since `B = (S−π)/15` (PROVED), the bounds propagate:

$$
B_{\mathrm{low}}:=\frac{S_M-\pi_K-\delta_K}{15}\ \le\ B\ \le\ \frac{S_M-\pi_K+\varepsilon_M}{15}
=:B_{\mathrm{up}} .
$$

**Choosing `M = 200000`, `K = 14`** (exact rational `π_K`; `δ_K ≈ 2.5·10^{−19}` is far smaller
than `ε_M ≈ 1.17·10^{−6}/15`), and evaluating `S_M` (a finite sum of rationals, see script), the
interval is

$$
\frac{S_M-\pi_K-\delta_K}{15}=0.016296919608776\ldots ,
\qquad
\frac{S_M-\pi_K+\varepsilon_M}{15}=0.016296997734166\ldots .
$$

Rounding the lower endpoint **down** and the upper endpoint **up** to explicit rationals gives
the certified bracket

$$
\boxed{
\frac{40742299}{2500000000}\ \le\ B\ \le\ \frac{81484989}{5000000000}
}
$$

i.e.

$$
\boxed{\ 0.0162969196\ \le\ B\ \le\ 0.0162969978\ } .
$$

Both endpoints agree to 6 decimals (`0.0162969…`), so `B` is certified to 6 decimals as
`0.016297`, and the true value `B = 0.0162969977338265655…` (exact `(S−π)/15`, digamma closed
form) is strictly inside. The interval has
width `7.82·10^{−8} < 10^{−7}`.

---

## 4. Summary of certified results

| Quantity | Result | Status |
|---|---|---|
| `r(m)` sign/monotonicity | `r>0`, strictly decreasing | **PROVED** (Lemma A) |
| `T_n` lower | `(424/819)/(64 n²) ≤ T_n` | **PROVED** (Lemma B) |
| `T_n` upper | `T_n ≤ 1/(64 n²)` | **PROVED** (Lemma B) |
| `B` bracket | `40742299/2500000000 ≤ B ≤ 81484989/5000000000` | **PROVED** (§3) |
| `B` to 6 decimals | `B = 0.016297…`, width `7.82·10^{−8}` | **PROVED** (§3) |

All endpoints are exact rationals; the finite sums `S_M`, `π_K` are exact rationals; the only
inequalities used are Lemma A, Lemma B, geometric-tail dominance, and the elementary integral
comparison `Σ_{k≥M} k^{−2} < 1/(M−1)`.

---

## 5. Reproducible verification

```sh
python verify_two_sided_B.py
```

The script (stdlib `fractions.Fraction` + `mpmath`) checks, independently:

1. `r(m)` positive and strictly decreasing for `1 ≤ m ≤ N₀` (symbolic-numeric cross-check).
2. `c_1/(64n²) ≤ T_n ≤ 1/(64n²)` for `1 ≤ n ≤ N₀` with `c_1 = 424/819`.
3. `S_M ≤ S ≤ S_M + ε_M` and `π_K ≤ π ≤ π_K + δ_K` (containment of the true values).
4. The final rational bracket contains the high-precision `B = (S−π)/15`.
5. Both endpoints round to `0.016297` (6-decimal agreement).

**No normality claim is made or needed.**
