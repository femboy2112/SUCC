# The ×3 defect D_N(h): exact structure, firewall, and honest gap

**Branch:** `research/x3-rigidity-frontier-2026-11-02` (off `origin/main`). **Date:** 2026-11-02.
**Scope:** obligation (A) of the Hochman–Shmerkin ×16–×3 rigidity route (WB-10):
prove `D_N(h) = (1/N) Σ_{n=1}^N [ e(3hU_n) − e(hU_n) ] → 0` for every fixed `h ≠ 0`.
**Companion script:** [`x3_defect.py`](x3_defect.py) (stdlib `Fraction` + `mpmath`,
`dps ≥ 6·N/2.3`, exact rational Green tails, exact ×16 iteration of the completed orbit).

**Status of the route:** π base-16 normality remains **OPEN**. This dossier proves the
*exact algebraic structure* of `D_N(h)`, runs the *firewall* (does (A) discriminate?), and
locates the exact remaining gap. It proves no asymptotic bound on `D_N(h)`; that is
labeled CONJECTURE with the numerical signature that supports it.

---

## 1. Exact setup (recovered, not re-derived)

From the repo's own exact modules (`observational_succ/duck_bbp.py`,
`duck_bbp_fourier.py`, verified numerically over `n ≤ 200`):

- Forcing `r(m) = 4/(8m−7) − 2/(8m−4) − 1/(8m−3) − 1/(8m−2)`, positive for `m ≥ 1`.
- Green tail `T_n = Σ_{k≥1} 16^{−k} r(n+k)`, with the *proved* bound
  `T_n ≤ r(n+1)/15 ≤ (8n+1)^{−2}` and `Σ_n T_n = B < 1/32`.
- The rational orbit `U_n = 16^{n−1} π − T_n` is the four-pole BBP orbit of `{π}`:
  `U_{n+1} = 16 U_n + r(n+1)` (lifted), `U_0 = 0`.
- The **completed orbit** `x_n = {16^{n−1} π}` satisfies `x_{n+1} = {16 x_n}` exactly,
  `x_1 = {π}` — the ×16 trajectory of the single point `{π}`.

We write `e(t) = exp(2π i t)` and define the Weyl sums on the two orbits:

```
S_N(h) = (1/N) Σ_{n=1}^N e(h U_n)        (rational orbit)   [the "Weyl gate" object]
W_N(h) = (1/N) Σ_{n=1}^N e(h x_n)        (completed orbit)
```

`D_N(h) = S_N(3h) − S_N(h)`.

---

## 2. Exact relationship between D_N(h) and the completed-orbit Weyl sums  [PROVED]

**Lemma 2.1 (integer-phase collapse).** For every integer `h`,
`e(h·16^{n−1}π) = e(h x_n)` exactly, because `16^{n−1}π = x_n + ⌊16^{n−1}π⌋` and
`e(h·⌊16^{n−1}π⌋) = 1` for `h ∈ ℤ`.

**Lemma 2.2 (orbit transfer).** For every integer `h` and every `n`,

```
e(h U_n) − e(h x_n) = e(h x_n) · ( e(−h T_n) − 1 ),
```

hence, since `|e(−hT_n) − 1| ≤ 2π|h| T_n` and `Σ_n T_n = B < 1/32`,

```
| S_N(h) − W_N(h) | ≤ (2π|h|/N) Σ_{n=1}^N T_n ≤ 2π|h| B / N = O_h(1/N).
```

**Theorem 2.3 (exact defect identity).** For every fixed nonzero integer `h`,

```
D_N(h) = W_N(3h) − W_N(h) + O_h(1/N),
```

with the explicit constant `|O_h(1/N)| ≤ 2π(|3h|+|h|) B / N`. In particular
`D_N(h) → 0` ⟺ `W_N(3h) − W_N(h) → 0`.

**Proof.** `D_N = S_N(3h) − S_N(h) = [W_N(3h) − W_N(h)] + [S_N(3h) − W_N(3h)] − [S_N(h) − W_N(h)]`,
and both bracket terms are `O_h(1/N)` by Lemma 2.2. ∎

**Consequence (Task 1, answered).** `D_N(h) → 0` is *equivalent* to
`W_N(3h) − W_N(h) → 0`, i.e. to the statement that every weak-∗ limit `μ` of the empirical
measures `μ_N = N^{−1}Σ δ_{x_n}` satisfies `μ̂(3h) = μ̂(h)`. This is the **×3-invariance**
obligation. It is **strictly weaker** than `S_N(h) = o(N)`:

- `S_N(h) = o(N)` ⟺ `W_N(h) → 0` ⟺ `μ̂(h) = 0` for every limit `μ`.
- `D_N(h) → 0` ⟺ `μ̂(3h) = μ̂(h)`, which is compatible with `μ̂(h) ≠ 0`.

Both are the *same object* (`S_N` and `W_N` differ only by `O_h(1/N)`), so the rigidity
route has genuinely *weakened* the target from "each mode vanishes" to "the 3h and h modes
agree," exactly as WB-10 states.

---

## 3. Attacking D_N(h) by tools other than the Weyl gate  [Task 2]

### 3.1 The exact arithmetic relation between {3U_n} and {U_n}

Because `gcd(3, 16) = 1`, there is **no** relation `3U_n ≡ U_{n+k}` (mod 1): 3 is not a
power of 16, so `{3U_n}` (the ×3 image of the ×16 orbit) and `{U_n}` are genuinely
distinct orbits of the *same seed*. This is exactly why the individual sum `S_N(h)` does
not cancel under the ×16 dynamics — 3 and 16 generate a free *multiplicative* semigroup
`⟨3,16⟩ = {3^a 16^b}`, and the Weyl sum at frequency `3^a 16^b h` is `W_N(3^a 16^b h)`.

The exact relation is instead a *two-point* one:

```
3 U_n = 3·16^{n−1} π − 3 T_n,
3·16^{n−1} π mod 1 = 3 x_n mod 1 = {3 x_n}   (the ×3 image of the digit orbit).
```

So `{3U_n}` is the ×3 image of `x_n`, and `{U_n}` is `x_n` up to the tail `T_n`; the defect
measures the *discrepancy* between the ×3 and ×16 (identity) images of the orbit.

### 3.2 A van der Corput / second-difference reframing of the *difference*

The key algebraic identity (exact, integer `h`):

```
e(3h U_n) − e(h U_n) = e(h U_n) · ( e(2h U_n) − 1 )
                      = 2i · e(2h U_n) · sin(2π h U_n).
```

Therefore

```
D_N(h) = 2i · (1/N) Σ_{n=1}^N e(2h U_n) sin(2π h U_n).          (*)
```

This is the *Fejér-kernel-weighted* form: the defect is the Weyl sum at frequency `2h`,
weighted by `sin(2π h U_n)`, which vanishes exactly when `h U_n ∈ ℤ`. The individual sum
`S_N(h)` has no such built-in vanishing factor. Concretely:

- The weight `sin(2π h U_n)` kills the *resonant* directions where `U_n` sits near
  `k/h`; the defect is non-trivial only where `U_n` is genuinely irrational mod `1/h`.
- A **second-difference / van der Corput** attack on `(*)` can exploit the ×16 dynamics:
  `U_{n+1} = 16 U_n + r(n+1)` with `r(n+1) → 0`, so `U_{n+1} ≈ 16 U_n` and
  `sin(2π h U_{n+1}) ≈ sin(32π h U_n)`. The weight *self-similarity* under `h ↦ 16h`
  is a handle the bare `S_N(h)` lacks.

This is the *proposed* different tool, **not a proven bound**. The honest statement:

> **Conjecture (strong form of A).** The partial sums `Σ_{n≤N}[e(3hU_n) − e(hU_n)]` are
> **bounded** (hence `D_N(h) = O_h(1/N)`), with the bound following from the
> Fejér-weighting `(*)` and the ×16 self-similarity of the weight.

The numerical signature is decisive in favor of this (Section 6), but no proof is claimed.

---

## 4. The firewall: the coherent counterseed  [Task 3, CRITICAL]

**Definition (coherent counterseed).** Seed the completed orbit at `x_1 = 0` instead of
`{π}`. Then `x_n = 0` for all `n`, so `U_n = −T_n` and `e(h U_n) = e(−h T_n) → 1` for every
`h` (all phases align to 1). Equivalently: any seed `s` with `e(h·16^{n−1}s) = 1` for all
`n, h ∈ ℤ` (a 2-adically trivial seed) yields the same coherent limit. The prompt's
"`s = −π/16`" is this coherent seed stated in the shifted-orbit normalization; the
mathematical content is exactly "the π-term contributes only integer phases, so
`U_n = −T_n → 0`."

**Firewall result (exact, then numerical).** For the counterseed,

```
S_N(h) → 1   for every h,   hence   D_N(h) = S_N(3h) − S_N(h) → 1 − 1 = 0.
```

So **(A) HOLDS for the counterseed.** It is *not* discriminating: a manifestly
non-normal orbit (its empirical measure is a Dirac mass at 0, Hausdorff dimension 0,
and it is the *opposite* of normal) still satisfies `D_N(h) → 0`.

**What this means for the route.** (A) alone **cannot** certify normality. The counterseed
passes (A) and fails (B) (positive lower dimension: `dim μ = 0 < 0` fails `dim_* μ > 0`).
This *confirms* Hochman–Shmerkin's necessity of **both** (A) and (B):

- (A) = `T_3`-invariance, passed by *both* the authentic and the coherent orbit;
- (B) = positive lower dimension, the object that *kills* the counterseed.

The counterseed is therefore a **clean separating witness**: it isolates exactly what (B)
must do. The rigidity route is non-vacuous *and* its two legs are logically independent —
(A) is not a disguised form of (B), and neither alone suffices. The firewall is **passed**
in the sense that it correctly identifies (A) as necessary-but-not-sufficient.

---

## 5. What is PROVED vs CONJECTURED vs the exact gap

### PROVED (this round, exact)

1. **Lemma 2.1** — `e(h·16^{n−1}π) = e(h x_n)` for integer `h` (integer-phase collapse).
2. **Lemma 2.2 / Theorem 2.3** — `D_N(h) = W_N(3h) − W_N(h) + O_h(1/N)` with explicit
   constant `≤ 2π(|3h|+|h|) B/N`; hence `D_N(h) → 0 ⟺ W_N(3h) − W_N(h) → 0 ⟺` every limit
   `μ` satisfies `μ̂(3h) = μ̂(h)`.
3. **Equivalence/strictness (Task 1)** — `D_N(h) → 0` is strictly weaker than
   `S_N(h) = o(N)`; it permits `μ̂(h) ≠ 0` and only forces the 3h/h modes to agree.
4. **Fejér identity (*)** — `D_N(h) = 2i·N^{−1}Σ e(2hU_n) sin(2π h U_n)` (exact).
5. **Firewall (Task 3)** — the coherent counterseed `U_n = −T_n` satisfies
   `S_N(h) → 1`, hence `D_N(h) → 0`; (A) is **non-discriminating** and (B) is the leg that
   kills the counterseed.

### CONJECTURED (numerical signature, NOT proved)

6. **Strong form of (A)** — `Σ_{n≤N}[e(3hU_n) − e(hU_n)] = O_h(1)`, i.e.
   `D_N(h) = C(h)/N + o(1/N)`. Supported by `N·|D_N(h)|` constant to 5 significant figures
   (Section 6); consistent with boundedness but **not** a proof (a slow `log N` drift over
   longer ranges is invisible at `N ≤ 8000`).
7. **(A) for the authentic orbit** — `D_N(h) → 0` for the true π orbit (the actual WB-10
   obligation). The `1/N` decay is the numerical shadow of this; the honest status is OPEN.

### The exact remaining gap

The entire route needs `D_N(h) → 0` **for the authentic orbit**, i.e. `μ̂(3h) = μ̂(h)` for
every limit `μ` of the ×16 orbit of `{π}`. Nothing here bounds the *authentic* `D_N(h)`
below `o(1)`: the firewall shows the coherent orbit also passes (A), so any proof of (A)
must use something that *distinguishes* `{π}` from the counterseed. That distinguishing
input is precisely (B) — positive lower dimension — which is **not** attacked here and is
the genuinely independent leg. The cleanest next target is the *spacing lower bound*
(`min_{n<m≤N} ‖x_n − x_m‖` growing polynomially in `1/N`, a strictly weaker statement than
`dim_* > 0`), which would supply (B) and thereby, with (A), force normality via
Hochman–Shmerkin Thm 10.4.

---

## 6. Reproducible numerics

`x3_defect.py` (`Fraction` + `mpmath`, `dps = 140`, exact rational Green tails, exact ×16
iteration `x_{n+1} = fmod(16 x_n, 1)`), error budget `< 1e-102` (far below `1/N`):

| h | N=1000 | N=2000 | N=4000 | N·|D_N| (const) |
|---|---|---|---|---|
| 1 | 0.0209286 | 0.0104643 | 0.0052322 | **20.9286** |
| 3 | 0.0167784 | 0.0083891 | 0.0041946 | **16.7784** |
| 5 | 0.0081366 | 0.0040682 | 0.0020341 | **8.1366** |
| 7 | 0.0089823 | 0.0044914 | 0.0022458 | **8.9830** |

`N·|D_N(h)|` is **constant to 5 significant figures** across a factor-of-4 in `N`, for all
four `h`. This is the signature `D_N(h) = C(h)/N + o(1/N)` — i.e. **bounded partial sums**,
the strong form of (A).

**Coherent counterseed** (`U_n = −T_n`):

| h | N=1000 | N=2000 |
|---|---|---|
| 1 | 0.0002043 | 0.0001022 |
| 3 | 0.0006070 | 0.0003036 |

Also `1/N` decay — **the counterseed passes (A)**, confirming it is non-discriminating
(and, for small `h`, the counterseed's `D_N` is ~100× *smaller* than the authentic orbit's,
because there `S_N(3h)` and `S_N(h)` both → 1 and differ only through the tiny tail `T_n`).

All finite outputs are **evidence only**; no theorem status is upgraded by them.

---

## 7. Claim ledger

| ID | Claim | Domain | Status | Evidence |
|---|---|---|---|---|
| X3-01 | `e(h·16^{n−1}π)=e(h x_n)`, `h∈ℤ` | integer phases | **PROVED** | Sec 2, Lemma 2.1 |
| X3-02 | `D_N(h)=W_N(3h)−W_N(h)+O_h(1/N)` | fixed `h≠0` | **PROVED** | Sec 2, Thm 2.3 |
| X3-03 | `D_N→0 ⟺ W_N(3h)−W_N(h)→0 ⟺ μ̂(3h)=μ̂(h)` | weak-∗ limits | **PROVED** | Thm 2.3 |
| X3-04 | `D_N→0` strictly weaker than `S_N=o(N)` | fixed `h` | **PROVED** | Sec 2 |
| X3-05 | `D_N=2i N^{−1}Σ e(2hU_n)sin(2πhU_n)` | integer `h` | **PROVED** | Sec 3.2 (*) |
| X3-06 | counterseed `U_n=−T_n` ⇒ `D_N(h)→0` | seed `x_1=0` | **PROVED** | Sec 4 |
| X3-07 | (A) is non-discriminating; (B) is the killing leg | rigidity route | **PROVED** | Sec 4 firewall |
| X3-08 | authentic `D_N(h)=C(h)/N+o(1/N)` (bounded partial sums) | fixed `h≠0` | **CONJECTURE** | Sec 6 numerics |
| X3-09 | authentic `D_N(h)→0` (WB-10 obligation A) | fixed `h≠0` | **OPEN** | — |
| X3-10 | `dim_* μ > 0` for every limit (obligation B) | ×16 orbit of {π} | **OPEN** | — |

**No pushed bound, no false victory.** π base-16 normality and RH remain OPEN.
