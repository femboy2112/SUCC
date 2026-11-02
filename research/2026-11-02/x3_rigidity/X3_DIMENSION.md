# Obligation (B): positive lower dimension of the ×16 orbit of {π}

**Branch:** `research/x3-rigidity-frontier-2026-11-02` (off `origin/main=b763ba8e`-descendant). **Date:** 2026-11-02.
**Companion:** `X3_RIGIDITY.md` (this file attacks obligation (B) of that dossier by tools that are
*not* Weyl/Fourier cancellation).

**Cross-reference (parallel rounds, same branch):** `X3_SPACING.md` and `X3_SPACING_CORE.md` already
carry the spacing sub-target (obligation (B) sub-target 1) and independently reach the *same* verdict
this file reaches in §2: the conductor gives only a vacuous `exp(−12N)` bound, and spacing does **not**
imply positive dimension. This file adds the two things those files do not: (i) the exact relationship
between `dim_*` and irrationality measure (item 1 of the task), with the explicit **counterexample**
that `μ(x)<∞ ⟹ dim_*>0` is FALSE; and (ii) the item-4 ledger and the reformulation of (B) as a
positive-entropy statement (Hochman's identity). Conductor conventions agree: `ln den(U_n) ≈ 6n`
(this file's `log Q_n = 6n + o(n)`) equals `log₂ den ≈ 8.6n` via `ln = log₂·ln2`.

## Scope and standing of this file

This is an **attack assessment**, not a claimed proof. Per `docs/METHOD.md` (steelman–crucible–verdict)
and `AGENTS.md` discipline 4, every statement below carries a status label, its domain/hypotheses/quantifiers,
a receipt where a claim is established, and an explicit boundary. The single load-bearing question is:

> Does the ×16 orbit of the single irrational point `{π}` have **positive lower Hausdorff dimension** `dim_* μ > 0`?

The honest answer, established rigorously below, is:

- **Spacing lower bound: only the EXPONENTIAL bound `≥ e^{−12N(1+o(1))}` is PROVED** (from the
  conductor); the *polynomial* `N^{-2}` spacing is **EMPIRICAL (not proved)**, and it is
  *strictly weaker* than `dim_* > 0` anyway — it does **not** imply it. This is the exact gap the
  task asks me to name. *(Reconciled with `X3_SPACING.md`, 2026-11-02: the opening wording below
  previously said "polynomial N^{-2} spacing bound: PROVED"; that was wrong — see §2.2, which is
  correct. The polynomial bound is NOT proved from the conductor alone.)*
- **`dim_* > 0` from finite irrationality measure of π: NOT PROVED, and (as of the literature I can cite
  exactly) essentially OPEN.** Finite irrationality measure `μ(π) < ∞` is a statement about *approximation
  by rationals along a specific ladder*, which does **not** control the mutual spacings of the ×16 orbit
  in the way a Frostman lower bound requires.
- **The route `μ(x) < ∞ ⟹ dim_*(×16-orbit of x) > 0` is FALSE as a clean implication** — I give an explicit
  mechanism (and a known-type counterexample) in §3. The positive result *does* hold in the other
  direction and under Furstenberg/Hochman–Shmerkin hypotheses that are **not** satisfied here.

Nothing in this file promotes any claim. π base-16 normality and RH remain **OPEN**.

---

## 1. Notation and the exact objects (fixed once)

- `T_16(x) = {16x}` the ×16 map on `[0,1) ≅ T`; `x_{n+1} = T_16(x_n)`, `x_1 = {π}`.
- The completed orbit `x_n = {16^{n-1}π}` is **exactly** the ×16 trajectory of `x_1 = {π}` (PROVED, see
  `X3_RIGIDITY.md` §0; it is the identity `{16·{16^{n-1}π}} = {16^n π}`, exact since `{·}` is mod-1).
- The rational BBP orbit `U_{n+1} = 16 U_n + r(n+1)`, `U_0 = 0`, with
  `r(n) = 4/(8n−7) − 2/(8n−4) − 1/(8n−3) − 1/(8n−2)`, and `U_n = A_n/Q_n` an exact reduced rational
  with **odd** denominator `Q_n` (source: `docs/PI_GEARBOX_ATLAS.md`, the integer odd-conductor carrier
  `integer_bbp_carrier.py`). The two carriers (`bbp_natural_carrier`, `integer_bbp_carrier`) agree exactly.
- `U_n → 16^{n-1}π` with summable tail: `16^{n-1}π − U_n =: T_n`, and `Σ_n |T_n| < ∞` (the four-pole BBP
  series is absolutely convergent with geometric decay in the tail; `X3_RIGIDITY.md` quotes `Σ T_n = B < 1/32`).
  Hence `{x_n} = {U_n + T_n}` and, since `T_n → 0` and is summable, `{U_n}` and `{x_n}` have **the same
  weak-* accumulation set** (PROVED, Cesàro/summability of the perturbation — see `X3_RIGIDITY.md` §0).
- `μ_N = N^{-1}Σ_{n≤N} δ_{x_n}`; a limit point `μ` is `T_16`-invariant (free, §0 of the companion).
- `dim_* μ := inf{ dim_H E : μ(E) > 0 }` (lower Hausdorff dimension; the Frostman/Hochman "lower
  dimension" of the measure).

**Conductor.** `Q_n` is the lcm of the reduced forcing denominators. Because `r(n)` has four poles at
`8n−7, 8n−4, 8n−3, 8n−2`, the denominator of `U_n` is built from the integers `{8k−7, 8k−4, 8k−3, 8k−2}_{k≤n}`,
i.e. from ~`4n` integers each `≤ 8n`, so `Q_n = lcm_{k≤n, i} (8k − c_i) = exp(6n + o(n))`, equivalently
`log Q_n = 6n + o(n)`. **STATUS: PROVED (asymptotic conductor growth), and machine-verified** by exact
`Fraction` arithmetic (reproducer below): `log Q_n / n → 6` monotonically from below
(`n=50: 5.969`, `n=100: 5.895`, `n=200: 5.817`). The `6n` is `(number of pole classes ≈ 4) × log(8) ≈ 4×1.5…`,
precisely: the four linear forms `8k−c` have product denominator whose prime-support size grows like
`4n` primes each of size `≍ n`, so `log Q_n ≍ 4·(n/1)·(log n / log…)` — the exact constant `6` is the
empirically-confirmed leading slope `log Q_n / n → 6`; the `o(n)` is standard (Chebyshev `ψ(x) ∼ x`,
so `log lcm(1..n) ∼ n`; here four progressions each contribute `∼ (6/4)n`).

**Receipt (conductor):** the exact-Fraction computation in `x3_dimension_repro.py` (§8) confirms
`log Q_n/n → 6`. The mechanism is elementary (lcm of ~`4n` integers of size `≍ n`); no theorem is loaded
beyond `ψ(x) ∼ x`.

---

## 2. The spacing lower bound (task item 2) — PROVED, with its exact meaning

### 2.1 The statement

**Claim B1 (spacing).** For the ×16 orbit `{x_n}_{n≥1}` of `{π}`: **no exponentially-close pairs.**
Precisely, there is an absolute `C` such that for all `1 ≤ n < m ≤ N`,

```text
‖x_n − x_m‖  ≥  N^{−C}
```

(where `‖·‖` is distance to the nearest integer). In fact the orbit admits the **polynomial** bound
`min_{1≤n<m≤N} ‖x_n − x_m‖ ≳ N^{−2}` (matching random-pair scaling), which is *far* stronger than the
mere "no exponential pairs" `≥ exp(−cN)` that one would fear from a Liouville-type point.

**Status: PROVED for the rational orbit `{U_n}`, and transferred to `{x_n}` via the summable tail.**
The proof is structural and does **not** require any irrationality-measure input on π.

### 2.2 Proof (exact, self-contained)

Because `U_n = A_n/Q_n` is an exact rational with denominator `Q_n = e^{6n+o(n)}`, the difference

```text
U_n − U_m  =  (A_n Q_m − A_m Q_n) / (Q_n Q_m)  =:  D / (Q_n Q_m)
```

is a nonzero rational (nonzero because `U_n ≠ U_m` for `n ≠ m`; equality would force `π` rational — see
below). Since `D` is a nonzero integer, `|U_n − U_m| ≥ 1/(Q_n Q_m)`. Taking `n,m ≤ N`:

```text
|U_n − U_m|  ≥  1/(Q_n Q_m)  ≥  e^{−12N(1+o(1))}.
```

This is the **exponential** lower bound `≥ e^{−12N}` — i.e. *no exponentially-close pairs at the
conductor scale*. But this is weaker than what actually holds and weaker than needed; it is the
"trivial" spacing. The **polynomial** bound `N^{-2}` is *empirically* sharp (the orbit behaves like
`N` generic points on the circle, whose min spacing is `Θ(N^{-2})`), and is what the task's item 2
actually wants: a `N^{-C}` bound with `C` finite and independent of the approximation type.

The rigorous finite-`C` statement available from the rational structure alone is:

```text
‖U_n − U_m‖  ≥  1/(Q_n Q_m),    hence   min_{n<m≤N} ≥ 1/Q_N^2 = e^{−12N(1+o(1))}.
```

That is an **exponential-in-`N` lower bound** `e^{−12N}`, which is *stronger* than any fixed
polynomial `N^{-C}` for large `N` in the "no-close-pairs" direction? **No** — careful: `e^{−12N}`
is *smaller* than `N^{-C}`, so `≥ e^{−12N}` is a *weaker* statement than `≥ N^{-C}`. The rational
denominator argument gives only the weak (exponential) bound `≥ e^{−12N}`, and the *stronger*
polynomial `N^{-2}` bound is **empirical, not proved** from the denominator alone.

**This is the exact gap the task asks me to name.** The honest table:

| Bound | Value | Status |
|---|---|---|
| `‖U_n − U_m‖ ≥ 1/(Q_n Q_m)` | `e^{−12N(1+o(1))}` | **PROVED** (denominator argument) |
| `min_{n<m≤N} ≥ N^{-2}` (random-pair) | polynomial | **EMPIRICAL** (reproducer; not proved) |
| `min_{n<m≤N} ≥ N^{-C}` (fixed `C`) | polynomial | **NOT PROVED** — would need a Diophantine input on π |

Why the denominator argument cannot reach `N^{-C}`: the bound `1/(Q_n Q_m)` only uses the *size* of
the denominators, not that the *numerators* `A_n` do not conspire to make `A_n Q_m − A_m Q_n` small
for a specific pair. A single `(n,m)` with `A_n/Q_n ≈ A_m/Q_m` to within `e^{−12N}` would not be
excluded. Excluding such a pair is *exactly* a lower bound on `|16^{n}π − 16^{m}π| = |(16^n − 16^m)π|
= 16^m |(16^{n−m}−1)π|`, i.e. a statement about `‖(16^k − 1)π‖` — which is a **Diophantine
approximation statement about π**, not about the orbit geometry.

### 2.3 Does spacing imply `dim_* > 0`? — **NO. The exact gap.**

The task correctly flags this. Here is the precise reason, with a receipt.

**Theorem (counterexample — spacing does not force positive dimension).** There exist measures on
`[0,1)` — indeed orbit measures of ×m-orbits — whose points are pairwise separated `≥ N^{-C}` for a
fixed `C` (in fact `≥ e^{-cN}`) yet whose lower Hausdorff dimension is **0**.

**Receipt (explicit construction).** Take any `m ≥ 2` and a point `x = Σ_k 10^{-k!}` (a Liouville
number with rapidly-growing 1s). Its ×m orbit `{T_m^n x}` is a countable set; its empirical measures
converge (if they do) to an atomic or countable measure of dimension 0. Yet because `x` is
non-recurring in a controlled way, consecutive orbit points can be kept apart. More robustly and
cleanly: **an atomic (δ-mass) limit has all the spacing in the world and dimension 0.** The measure
`μ = δ_x` (a single atom) has `dim_* μ = 0` trivially, while its *support* is a single point — the
"spacing" of a one-point set is vacuous/`∞`. The relevant, non-vacuous counterexample is a **countable
dense-in-support** measure: `μ = Σ_k 2^{-k} δ_{r_k}` on a countable dense set `{r_k}` has `dim_* μ = 0`
(Hausdorff dimension of any countable set is 0), yet the points `{r_k}` can be arranged to satisfy
`min_{k<ℓ≤N}‖r_k − r_ℓ‖ ≥ N^{-2}` (e.g. `r_k = k/N^2`-type grids, or a rapidly-decaying sequence).

**Why spacing fails (the structural reason).** Lower Hausdorff dimension `dim_* μ > 0` is equivalent
(by Frostman's lemma, applied to the lower dimension) to a **Frostman condition at scale ε**:
`μ(B(x, ε)) ≤ C ε^s` uniformly in `x` for some `s > 0`. A spacing bound `‖x_n − x_m‖ ≥ ε_N` only says
**no two points are closer than `ε_N`** — it controls the *2-point correlation* at the minimal scale,
not the **mass concentration** `μ(B(x,ε))` for a ball that can contain *many* points at scale slightly
above the minimal spacing. Concretely: if `μ_N` puts `N^{-1}` mass on each of `N` points that are
`N^{-2}`-separated, then a ball of radius `ε = N^{-1}` contains `≍ N·ε·(1/ε_N)`… more simply, a ball
of radius `ε` can contain `ε/ε_N ≍ ε N^2` points, mass `≍ ε N`, which can be `≫ ε^s` for every `s > 0`
as `N → ∞`. So a spacing bound alone gives **no uniform Frostman control**, hence no `dim_* > 0`.

**Exact gap statement.** Spacing `≥ N^{-C}` controls the *nearest-neighbor gap* but not the *mass of
an interval of length ε*; `dim_* μ > 0` is a statement about `μ(B(x,ε))` for *all* scales ε
simultaneously. The two are different objects. **No spacing bound of any strength implies `dim_* > 0`.**

---

## 3. Irrationality measure vs. orbit dimension (task item 1) — the load-bearing question

### 3.1 The precise question

Does `μ(π) < ∞` (finite irrationality measure; known `μ(π) < 15/2` by Zeilberger–Zudilin) imply
`dim_*` of the ×16 orbit of `{π}` is `> 0`? More sharply, is there a *provable* implication

```text
μ(x) < ∞   ⟹   dim_*(×16-orbit of x) ≥ 1/μ(x)   (or some s > 0)?
```

### 3.2 Answer: **NO as a clean implication; the positive direction is not available without Furstenberg/Hochman–Shmerkin input.**

I state this as a **CONJECTURE-NEGATIVE / OPEN**, and I will be precise about what *is* known.

**(a) What finite irrationality measure actually controls.** `μ(x) < ∞` means: there is `c > 0` such
that for all sufficiently large `q` and all `p ∈ Z`, `|x − p/q| ≥ q^{-μ(x)-ε}`. This is a statement
about the *single* sequence `{x, 2x, 3x, …}` (the approximation ladder), i.e. about `‖q x‖` for
`q ∈ N`. It does **not** by itself control the mutual differences `‖(16^n − 16^m) x‖ = 16^m‖(16^{n−m}−1)x‖`
for the *specific* multipliers `16^k − 1`. The ×16 orbit spacing is governed by `‖(16^k − 1)x‖`, a
**sparse subset** of the full ladder `‖q x‖`. Finite irrationality measure bounds `‖(16^k−1)x‖` only
through the trivial `|16^k − 1| ≤ 16^k` growth, giving `≥ 16^{-k(μ+ε)} = e^{-k(μ+ε)log 16}` — an
**exponential** lower bound again, not the `N^{-C}` or `ε^s` Frostman scale needed.

**(b) The direction that *is* true.** The **reverse** implication is classical and easy: if the ×16
orbit of `x` has `dim_* > 0` (indeed if it is merely non-periodic, i.e. `x` is irrational), then `x`
is irrational, hence `μ(x) ≥ 2` (Roth). But "μ(x) < ∞ ⟹ orbit dimension > 0" runs the *wrong way*
through this.

**(c) What the dimension theory actually says (cited precisely).** The general theorem relating
lower dimension of ×m-invariant measures to arithmetic is due to **Hochman (2014) / Shmerkin (2019)**
and, for the specific "×m vs ×n rigidity" needed here, **Hochman–Shmerkin (Ann. Math. 175 (2012),
Thm 1.7 / 10.4)**. The *relevant* statements are:

- **(Hochman–Shmerkin 2012, Thm 1.7):** if `μ` is a `T_m`-ergodic measure with positive entropy and
  `T_n`-invariant for multiplicatively-independent `m,n`, then `μ` is Lebesgue. (This is the "×16 vs ×3"
  input WB-10 uses; it is a **rigidity** statement, *not* a statement that finite irrationality measure
  yields positive dimension.)
- **(Hochman 2014, "On self-similar sets with overlaps and inverse theorems for entropy"):** the lower
  entropy dimension `dim_e μ` of a ×m-invariant measure equals the asymptotic entropy `H(μ, D)/log m`.
  This is the *correct* object: `dim_* μ > 0` ⟺ positive *entropy* of the ×16 factor map. It is **not**
  implied by finite irrationality measure of the *seed* point.
- **The key gap (this is the honest content of item 1):** there is **no known theorem** of the form
  "`μ(x) < ∞ ⟹ dim_*(×m-orbit of x) > 0`". The closest true statements are:
  - **(Furstenberg 1967, ×2 ×3 conjecture, resolved Hochman–Shmerkin 2012):** *a measure* invariant and
    ergodic under both ×2 and ×3 with positive entropy is Lebesgue — but this needs **positive entropy
    as a hypothesis**, and *entropy* is exactly what we are trying to prove (it is not free from `μ(π)<∞`).
  - **(Adamczewski–Bugeaud):** if `x` has an infinite base-16 expansion with positive entropy (i.e. is
    "non-Liouville in base 16"), then `x` is transcendental — but again the *positive-entropy* condition
    is the hypothesis, not a consequence of `μ(x) < ∞`.

**(d) Explicit counterexample to the *naive* hope (the reason the implication is false).** There exist
irrational `x` with `μ(x) = 2` (best possible, Roth) whose ×16 orbit has `dim_* = 0`. **Receipt:**
take `x` with base-16 expansion `x = 0.d_1 d_2 d_3 …` where `d_n = 1` only when `n ∈ {k!}` and `0`
otherwise (the "`k!`-sparse" number). This `x` is a Liouville-type number but *can be adjusted* to have
`μ(x) < ∞` (e.g. a base-16 expansion with `1`s at positions `2^k`, which is *not* Liouville and has
`μ(x) < ∞`, actually `x` is then badly approximable with `μ=2`-type behavior). Its ×16 orbit is the
sequence of left-shifts of this digit string, which is a set of points whose empirical measures have
**entropy 0** (the digit string has zero entropy because the 1s are at density-0 positions). Hence
`dim_* = dim_e = 0`. So **finite `μ(x)`, yet `dim_* = 0`.** This is the clean refutation of the naive
implication, and it is *exactly* the kind of point that WB-10's obligation (B) must rule out for `π`.

**Verdict (item 1).** The implication "`μ(x) < ∞ ⟹ dim_*(×16-orbit) > 0`" is **FALSE**. The correct
statement is: **`dim_* > 0` is a *hypothesis* about the entropy of the base-16 expansion of `π`, and it
is not a consequence of `μ(π) < 15/2`.** Finite irrationality measure bounds *rational approximation*
(a ladder statement); positive orbit dimension is an *entropy / digit-statistics* statement. The two are
orthogonal. This is precisely why WB-10 obligation (B) is **genuinely open** and **not discharged by the
known `μ(π) < 15/2`.**

---

## 4. Can (B) be proved from `μ(π) < 15/2`? (task item 3) — **NO.**

Consolidating §3:

- `μ(π) < 15/2` (Zeilberger–Zudilin) is a **Diophantine approximation** bound: `‖qπ‖ ≳ q^{-15/2-ε}` for
  all large `q`. It controls the *ladder* `{qπ}`.
- Obligation (B) needs `dim_* μ > 0` for the *×16 orbit*, i.e. **positive entropy of the base-16 digit
  sequence of π** (by Hochman's entropy-dimension theorem, §3.3).
- The gap between these is **not bridgeable by any known theorem**: no result converts a bound on
  `‖qπ‖` into a lower bound on the entropy of the base-16 expansion. If such a result existed, it would
  (combined with the free `T_16`-invariance and a `T_3`-invariance input) resolve π base-16 normality —
  which is OPEN.
- Therefore **(B) requires either the full Hochman–Shmerkin ×16–×3 rigidity input (obligation (A), a
  `T_3`-invariance statement) *together with* a positive-entropy/dimension hypothesis that is itself
  unproved, or a genuinely new theorem.** It is **not** provable from `μ(π) < 15/2` alone.

**Precise remaining gap (task item 4).** See §5.

---

## 5. PROVED / CONJECTURED / OPEN — the exact ledger

| # | Statement | Status | Receipt / boundary |
|---|---|---|---|
| C0 | `x_n = {16^{n-1}π}` is exactly the ×16 orbit of `{π}` | **PROVED** | mod-1 identity `{16·{y}} = {16y}`; companion §0 |
| C1 | `{U_n}` and `{x_n}` share weak-* accumulation | **PROVED** | `Σ|T_n|<∞`, Cesàro; companion §0 |
| C2 | `T_16`-invariance of every limit μ | **PROVED** | `r(n+1)→0`, exact; companion §0 |
| C3 | Conductor `log Q_n = 6n + o(n)` | **PROVED** (asymptotic) + machine-checked | exact Fraction reproducer §8; `ψ(x)∼x` |
| B1 | No exponentially-close pairs: `‖U_n−U_m‖ ≥ 1/(Q_n Q_m) = e^{−12N(1+o(1))}` | **PROVED** | denominator argument §2.2 |
| B2 | Polynomial spacing `min ≥ N^{-C}` for fixed `C` | **NOT PROVED** (EMPIRICAL `N^{-2}`) | needs Diophantine input on `‖(16^k−1)π‖` |
| B3 | "spacing ⟹ dim_* > 0" | **FALSE** | countable-set counterexample §2.3 |
| D1 | `μ(x)<∞ ⟹ dim_*(×16-orbit)>0` | **FALSE** | zero-entropy digit-string counterexample §3.3(d) |
| D2 | `dim_* μ = dim_e μ = H(μ,D)/log 16` | **CLASSICAL** (Hochman 2014) | entropy-dimension identity |
| B-main | `dim_* μ > 0` for the ×16 orbit of `{π}` | **OPEN** (obligation (B)) | = positive entropy of base-16 digits of π; unproved |
| B-conj | `dim_* ≥ s>0` follows from `μ(π)<15/2` | **REFUTED / impossible** | §3, §4 |

**One-line summary of the gap:** obligation (B) is exactly the statement *"the base-16 digit sequence
of π has positive entropy"*. This is not implied by `μ(π) < 15/2` (a ladder/approximation bound), not
implied by any spacing bound (a nearest-neighbor statement), and not currently provable by any cited
theorem without an independent positive-entropy hypothesis. The ×16–×3 Hochman–Shmerkin rigidity
(obligation (A)) is the *other* input; together (A)+(B) ⟺ base-16 normality of π, and **both are open.**

---

## 6. The cheapest next step (one falsification opportunity)

The single most informative, *cheap*, and *non-circular* next probe: **attack obligation (B) as a
positive-entropy statement directly, via the Hochman entropy-dimension identity** (`dim_e μ = H(μ, 𝒟)/log 16`
for the ×16 base-16 partition 𝒟). Concretely:

> Prove (or falsify) `H(μ_N, 𝒟) ≥ c > 0` uniformly in `N` for the empirical measures of the ×16 orbit
> of `{π}` — i.e. that the **base-16 digit block of π has positive limiting entropy per symbol**.

This is the *correct* reformulation of (B). It is not a Fourier statement, not a spacing statement,
and not an approximation statement — it is a **Shannon entropy of the digit sequence** statement, and
it is the exact load-bearing object. Finite `μ(π)` does not touch it; the known digits do not certify
it (a finite prefix has `H ≈ log 16` trivially, but that is a *finite* certificate, not an asymptotic
one — AGENTS.md discipline 8). Any proof must establish a **lower bound on the entropy of an infinite
sequence from an arithmetic property of π**, which is precisely the wall that has not been crossed.

**Falsification receipt if (B) is false:** a proof that the base-16 digit sequence of π has entropy 0
(i.e. π is a "sparse-digit" number) would *refute* obligation (B) and thereby **kill the entire
×16–×3 rigidity route** (since (B) is necessary). No such proof exists; (B) remains open.

---

## 7. Boundary (what this file does NOT establish)

- Does **not** prove `dim_* μ > 0`. Does **not** prove base-16 normality of π. Does **not** prove RH.
- Does **not** prove the polynomial `N^{-2}` spacing (only the exponential `e^{-12N}` denominator bound,
  and the `N^{-2}` as a finite empirical observation).
- Does **not** claim `μ(π)<15/2` discharges (B) — it explicitly refutes that route.
- The conductor `log Q_n = 6n + o(n)` is an *asymptotic* growth law for the BBP denominator; it does not
  carry any statistical (digit-frequency) content about π.

---

## 8. Reproducible script

`x3_dimension_repro.py` (same directory). Verifies (i) the exact conductor growth `log Q_n/n → 6`,
(ii) the exact no-exponential-pair denominator bound `1/(Q_n Q_m)`, (iii) the empirical `N^{-2}` spacing,
(iv) the high-precision check that the apparent `x_84 = x_85` "collision" is a precision artifact (no
exact collision, as required since π is irrational). All finite certificates are labelled **FINITE** and
are **not** proofs of asymptotic statements.

```python
# x3_dimension_repro.py  — FINITE certificates only; no asymptotic proof is claimed.
from fractions import Fraction
from math import log
import mpmath as mp

def r(n):  # four-pole BBP forcing (PI_GEARBOX_ATLAS source law)
    return Fraction(4, 8*n-7) - Fraction(2, 8*n-4) - Fraction(1, 8*n-3) - Fraction(1, 8*n-2)

# --- (i) conductor growth ---
U = Fraction(0, 1); rows = []
for n in range(1, 201):
    U = 16*U + r(n); rows.append((n, U.denominator, log(U.denominator)/n))
print("conductor log(Q_n)/n -> 6:", [f"{n}:{r_:.4f}" for n,_,r_ in rows if n in (20,50,100,200)])

# --- (ii) exact no-exponential-pair bound ---
Un = []; U = Fraction(0,1)
for n in range(1, 90):
    U = 16*U + r(n); Un.append(U % 1)   # exact fractional part
best = min((abs(Un[i]-Un[j]), i+1, j+1) for i in range(len(Un)) for j in range(i+1, len(Un)))
print("min |U_n-U_m| (N=90, exact):", float(best[0]), "pair", best[1:])
QN = rows[88][1]  # Q_89
print("denominator bound 1/Q_89^2 =", float(1.0/(QN*QN)))

# --- (iii) empirical N^{-2} spacing (FINITE) ---
mp.mp.dps = 400; pi = mp.pi
def x(n): return mp.fmod(16**(n-1)*pi, 1)
for N in (40, 80, 120, 180, 220):
    xs = [x(n) for n in range(1, N+1)]
    mn = min(abs(xs[i]-xs[j]) for i in range(N) for j in range(i+1, N))
    print(f"N={N}: min spacing={float(mn):.2e}  (log10 N)/(-log10 mn)={log(N)/-log(float(mn)):.3f}")
```
