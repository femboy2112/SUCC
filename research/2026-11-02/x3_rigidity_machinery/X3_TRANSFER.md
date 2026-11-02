# X3 Transfer / Spectral Route — Obligation (A) Assessment

**Branch:** `research/x3-rigidity-machinery-2026-11-02`
**Date:** 2026-11-02
**Author:** Ravel (openclaw agent)
**Repo:** `femboy2112/SUCC`, checkout `/media/leah/SPANKBANK/SUCCYBOI2/SUCC`
**Scope:** research-only, additive, non-main. No merge/tag/publish.

**Status summary up front (honest labels):**

| Question | Verdict |
|---|---|
| Is the ×16 transfer operator well-defined and does it have a spectral gap? | **PROVED** (classical Perron–Frobenius / Lasota–Yorke). Lebesgue is the unique ×16-invariant measure; contraction rate 1/16 in BV. This is *trivial for base-16* and proves **nothing new** about the ×3 defect. |
| Is `D_N(h) → 0` equivalent to a spectral statement for a single operator? | **NO** — it is equivalent to **joint ×16×3-invariance** of every weak-* limit measure, i.e. a *measure-rigidity* statement, **not** a spectral gap of the ×3 Koopman operator on the ×16-invariant measure. |
| Does a spectral gap for the ×3 Koopman operator on L²(×16-invariant limit) imply `D_N → 0`? | **Only in a vacuous/tautological sense**, and the needed spectral gap is **NOT provable** without assuming what is to be shown (it is the Furstenberg conjecture). |
| Is the transfer-operator route **genuinely new** vs. Weyl cancellation? | **No — it re-encodes the same gate.** The ×16 transfer operator's spectral gap yields only the *modulus* bound DC-1, not signed `o(N)`; the ×3 defect is exactly the Furstenberg ×16×3 joint-invariance wall (already mapped as AR-5 / FK-2 / FK-3). |
| π normality / RH | **OPEN / OPEN.** No new saving established. |

---

## 0. Context (proved reductions, not re-derived)

Source (byte-unchanged): four-pole BBP forcing

$$
r(m)=\frac{4}{8m-7}-\frac{2}{8m-4}-\frac{1}{8m-3}-\frac{1}{8m-2},
\qquad U_0=0,\qquad U_{n+1}=16\,U_n+r(n+1).
$$

Completed orbit (Green tail): `U_n = 16^{n-1}\pi - T_n`, `T_n = Σ_{k≥1} 16^{-k} r(n+k)`.
Circle orbit: `x_{n+1} = {16 x_n}`, `x_1 = {\pi}`. Then `x_n = {16^{n-1}\pi}`.

**SGO-09 (#293, PROVED):** `|Σ_{n≤N} e(h·16^{n-1}π) − Σ_{n≤N} e(h U_n)| < (119/648)|h|`.
Hence π is base-16 normal **iff** `Ŝ_N(h)=Σ_{n≤N} e(h U_n) = o(N)` for every fixed `h≠0`.

**DC-1 (#304, PROVED):** `|Σ_{n≤N} e(h U_n)| ≤ N − (1/1250)·max(0, floor(log_8 N) − max(J_0, ceil(log_64|h|)))`.
A **modulus** bound: normalized it tends to 1, **not** `o(N)`.

**The ×3 defect (this task):**

$$
D_N(h) := \frac1N\sum_{n=1}^N\left[e(3h\,U_n)-e(h\,U_n)\right]
= W_N(3h)-W_N(h)+O_h(1/N),
\qquad W_N(h)=\frac1N\sum_{n=1}^N e(h\,x_n).
$$

Fejér-weighted form (task CONTEXT): `D_N(h)=2i N^{-1}Σ e(2hU_n)\sin(2π h U_n)`, self-similar under `h→16h` (since `U_{n+1}=16U_n+r(n+1)`, `r→0`). We take the CONTEXT statements as given.

---

## 1. The ×16 transfer operator and the exact ×3 action on the orbit

### 1.1 Perron–Frobenius (transfer) operator of ×16

On `T = R/Z` with Lebesgue `dx`, the ×16 map `T_{16}: x ↦ 16x mod 1` has Perron–Frobenius operator

$$
(\mathcal P_{16} f)(x)=\frac1{16}\sum_{j=0}^{15} f\!\left(\frac{x+j}{16}\right),
\qquad \mathcal P_{16}: L^1(\mathbb T)\to L^1(\mathbb T).
$$

Its Koopman (composition) operator is

$$
(\mathcal U_{16} f)(x)=f(16x \bmod 1),
\qquad \mathcal U_{16}=\mathcal P_{16}^* \ \text{on}\ L^2(\mathbb T).
$$

**Fourier action (exact, verified):**

$$
\mathcal P_{16}\, e(hx)
=\frac1{16}\sum_{j=0}^{15}e\!\left(\frac{h(x+j)}{16}\right)
=\begin{cases}
e(hx/16), & 16\mid h,\\[2pt]
0, & 16\nmid h,
\end{cases}
\qquad
\mathcal U_{16}\,e(hx)=e(16hx).
$$

So on the Fourier basis `χ_h(x)=e(hx)`:

$$
\mathcal P_{16}^n\,\chi_h=\begin{cases}\chi_{h/16^n},&16^n\mid h\\ 0,&\text{else},\end{cases}
\qquad
\mathcal U_{16}^n\,\chi_h=\chi_{16^n h}.
$$

**Consequence (PROVED, classical):**

- `\mathcal P_{16}` is **not** diagonalizable; on L² it is an isometry on the ladder `h↦16h` (no decay in L²) — it is a **shift**, so it has **no spectral gap in L²** in the strong sense (it is a rank-one isometric shift on the `16^k`-ladder; actually `\mathcal P_{16}` is a *compression/contraction* on the non-multiple modes and an isometry on multiples, so it is mixing on BV but not on L²).
- In **bounded variation** (`\|\cdot\|_{BV}`), Lasota–Yorke gives the classical contraction (this is exactly **WTM-06**, already in the repo):

$$
\operatorname{Var}(\mathcal P_{16}^n f)\le 16^{-n}\operatorname{Var}(f),
\qquad \|\mathcal P_{16}^n f\|_{L^1}\le\|f\|_{L^1}.
$$

- By Ionescu-Tulcea–Marinescu / Hennion quasi-compactness, `\mathcal P_{16}` has **spectral gap** on BV: Lebesgue is the **unique** invariant density, the essential spectral radius is `≤1/16`, and

$$
\|\mathcal P_{16}^n f - \int f\,dx\|_{BV}\le C\,16^{-n}\|f\|_{BV}.
$$

**This is a real spectral gap — but it is the base-16 gap, and it says nothing about ×3.** It establishes only that ×16 is *exactly* the uniformly-expanding base-16 map and that its invariant measure is Lebesgue. Every statement derivable from it (equidistribution of `{16^n x}` for a.e. `x`, mixing of `T_{16}`) is **classical and already known**; it does not touch the signed `o(N)` problem for the *specific* orbit `x_n={16^{n-1}\pi}`.

### 1.2 Exact action of ×3 on the orbit; the free semigroup

The ×3 map `T_3: x↦3x mod 1` acts on the circle. On the orbit, `{3 x_n}` is **not** a translate/shift of `{x_{n+1}}={16 x_n}`: the two maps `T_3` and `T_{16}` commute (both are `x↦ax mod 1`), and since `gcd(3,16)=1` they generate a **free abelian semigroup** `{3^a 16^b : a,b≥0}` (no nontrivial relation `3^a=16^b`). Consequently there is **no source-derived identity** relating `{3x_n}` to `{x_{n+1}}={16x_n}`: for any `n`, `3x_n` and `16x_n` are generically independent points of the orbit of the *joint* action.

Formally, the ×3 **Koopman operator** is

$$
\mathcal U_3\, f(x)=f(3x \bmod 1),
\qquad \mathcal U_3\,\chi_h=\chi_{3h},
$$

and `\mathcal U_3 \mathcal U_{16}=\mathcal U_{16}\mathcal U_3=\mathcal U_{48}`. The defect reads

$$
D_N(h)=\langle \chi_{3h}-\chi_h,\ \nu_N\rangle,
\qquad \nu_N:=\frac1N\sum_{n=1}^N\delta_{x_n},\quad x_n=\{16^{n-1}\pi\}.
$$

So `D_N(h)` is the **Fourier coefficient gap** of the empirical measure `ν_N` between the `3h` and `h` modes — i.e. a probe of how far `ν_N` is from being ×3-invariant.

---

## 2. Is `D_N(h)→0` a *spectral-gap* statement?

**No. It is a measure-rigidity (joint-invariance) statement, and no single-operator spectral gap encodes it.** This is the central honest finding.

### 2.1 The exact equivalence (PROVED, structural)

Let `μ` be any weak-* limit of `(ν_N)`. Telescoping the base-16 orbit gives `(T_{16})_*μ=μ` **automatically** (rank-one dyadic orbit). Then:

$$
D_N(h)\to 0 \ \forall h\neq 0
\quad\Longleftrightarrow\quad
\widehat\mu(3h)=\widehat\mu(h)\ \forall h\neq 0
\quad\Longleftrightarrow\quad
(T_3)_*μ=μ .
$$

*(Forward: Fourier uniqueness; backward: continuity of Fourier transform along the subsequence realizing `μ`.)*

Hence

$$
\boxed{\ D_N(h)\to 0\ \forall h\iff \text{every weak-* limit } μ \text{ is } \times16\times3\text{-invariant.}\ }
$$

This is **precisely** the hypothesis that triggers the **Furstenberg ×16×3 (i.e. ×2×3) measure-rigidity** machinery. It is the statement `AR-5` in the ledger, and it is **CONDITIONAL**, not a spectral gap of any single operator.

### 2.2 The "spectral gap" the task asks about does not do the job

Consider the ×3 **Koopman operator** `\mathcal U_3` acting on `L^2(\mathbb T, μ)` where `μ` is a ×16-invariant limit measure. A "spectral gap" would mean: the only `\mathcal U_3`-invariant functions are constants, with the orthogonal complement contracted. But:

- `\mathcal U_3` has **no spectral gap** on `L^2(μ)` in general. Its invariant functions are exactly `\{f : f(3x)=f(x)\ μ\text{-a.e.}\}`. The operator `\mathcal U_3` is an **isometry** (Koopman of a measure-preserving map), so `\|\mathcal U_3\|=1` and there is **no contraction** — a spectral gap of the form `\|\mathcal U_3^n f - \bar f\|\le θ^n\|f\|`, `θ<1`, is **impossible** for an isometry.

- The correct "gap" is the **unique ergodicity / rigidity** statement: *every* `\mathcal U_{16}`-invariant probability measure `μ` is also `\mathcal U_3`-invariant, and `μ=\text{Lebesgue}`. This is exactly the **Furstenberg ×16×3 measure conjecture**, which is a statement about the **joint action of the semigroup `{16^a 3^b}`**, not a spectral gap of `\mathcal U_3` alone.

- Reformulating in spectral language (Furstenberg's own): the joint-invariance question is whether the **only** `μ` with `a_h=a_{16h}=a_{3h}` (a positive-definite Fourier system) is `a_h=δ_{h,0}` (Haar). The positive-definiteness constraint `a_h=a_{16h}=a_{3h}` admits **non-Haar** solutions (atomic rational periodic orbits, e.g. `α=1/5`, `x_n=1/5`, for which `D_{N,1}^{(3)}=e(3/5)−e(1/5)\neq0`), and admits the **open** zero-entropy non-atomic jointly-invariant counterexamples.

### 2.3 The exact spectral condition (what *would* be sufficient)

The only spectral object that *would* settle `D_N→0` is the **joint** condition:

> **(J)** For every `\mathcal U_{16}`-invariant ergodic measure `μ`, either
> (i) `μ` has positive measure-theoretic entropy (then **Rudolph–Johnson 1990** forces `μ=`Lebesgue), or
> (ii) `μ=`Lebesgue outright.

Condition (i) is **PROVED** (Rudolph–Johnson; the ×2×3 positive-entropy rigidity). Condition (ii) — the **zero-entropy, non-atomic, jointly-invariant** case — is the **OPEN** part of the universal Furstenberg conjecture. It is **not** a spectral gap and is **not** provable from the ×16 transfer operator (whose gap is already exhausted by the base-16 map itself).

**Conclusion of §2:** `D_N(h)→0` is **equivalent** to joint ×16×3-invariance of every limit measure; the *sufficient* rigidity is Rudolph–Johnson (positive entropy, PROVED) plus the universal Furstenberg zero-entropy rigidity (**OPEN**). No single-operator spectral gap on `L^2(μ)` exists or suffices.

---

## 3. Is the transfer-operator route genuinely NEW, or does it re-encode Weyl cancellation?

**It re-encodes the same gate. It is not new, and it does not bypass the signed-cancellation barrier.**

### 3.1 What the ×16 transfer operator actually gives

The Lasota–Yorke / Perron–Frobenius spectral gap of `\mathcal P_{16}` (WTM-05..08) is real but delivers only:

1. Lebesgue = unique ×16-invariant measure, with BV-contraction `16^{-n}`;
2. Fourier-mode flattening `\|\mathcal P_{16}^n χ_h\|_{L^1}≤4|h|16^{-n}` (WTM-08);
3. Hence, via duality, **modulus** bounds `|Σ e(hU_n)|` of the *same order* as DC-1 (i.e. `N − o(N)` territory), **never** signed `o(N)`.

The reason is structural and already recorded in the repo (**SK2-H, "FACT 1"**): van der Corput differencing at lag `k` maps frequency `h→h(16^k−1)`, which **stays inside the ×16 family** — differencing never leaves the x16 ladder, so the transfer-operator gap (which lives on that same ladder) can never *drop degree* to signed cancellation. The ×16 spectral gap is **exhausted** by the base-16 expansion; it is the *same* modulus bound DC-1 in operator clothing.

### 3.2 What the ×3 defect actually is

`D_N(h)→0` is **joint ×16×3-invariance**, i.e. the **Furstenberg ×2×3 route**. This is a *different* (stronger, rigidity-flavored) statement than Weyl cancellation of a single frequency — but it is **not** produced by any transfer-operator gap, and it is **already fully mapped** in the repo:

- **FK-1 / FK-2 (PROVED):** `D_N→0` alone does **not** imply normality (Kempner countermodel: `κ=Σ2^{-2^j}` is transcendental with irrationality exponent 2, `ν_N→δ_0`, `D_N→0`, yet κ is not base-2/16 normal). The missing ingredient is **anti-concentration / atomlessness / entropy**.
- **FK-3:** the residual obstruction is the **zero-entropy, non-atomic, jointly-invariant** measure — the open universal Furstenberg conjecture.
- **AR-5 (CONDITIONAL via Rudolph–Johnson):** unaveraged ×3 defects →0 *plus* no zero-entropy joint components ⇒ π normal. Both premises **OPEN** for the specific BBP orbit.

### 3.3 The honest assessment

| Claim | Status |
|---|---|
| ×16 transfer operator is well-defined, has BV spectral gap 1/16, Lebesgue unique invariant | PROVED (classical; WTM-05..08) |
| That gap implies signed `o(N)` for the BBP orbit | **REFUTED / IMPOSSIBLE** — it yields only modulus DC-1; differencing stays on the ×16 ladder (SK2-H FACT 1) |
| `D_N(h)→0 ⟺` joint ×16×3-invariance of all limits | PROVED (structural, §2.1) |
| `D_N(h)→0` is a spectral gap of `\mathcal U_3` on L²(μ) | **FALSE** — `\mathcal U_3` is an isometry; no gap exists |
| Joint-invariance + positive entropy ⇒ Haar | PROVED (Rudolph–Johnson 1990) |
| Joint-invariance + zero entropy ⇒ Haar | **OPEN** (universal Furstenberg conjecture) |
| Transfer-operator route is genuinely new vs. Weyl | **NO** — same gate (modulus, not signed); ×3 defect = Furstenberg route, already mapped |
| π normality, RH | **OPEN** |

**The transfer operator of ×16 gives a spectral gap that is real but already exhausted by the base-16 map (it is the modulus/DC-1 gate). The ×3 defect is not a spectral-gap statement at all — it is the Furstenberg ×16×3 joint-invariance wall, and its decisive step (zero-entropy rigidity) is the open universal Furstenberg conjecture. No new signed saving is established.**

---

## 4. PROVED / CONJECTURED / GAP

### PROVED (this document, classical + source-scoped)

- **P1.** `\mathcal P_{16}`, `\mathcal U_{16}`, `\mathcal U_3` exact Fourier actions (§1.1, §1.2).
- **P2.** `\mathcal P_{16}` has BV spectral gap `1/16`, Lebesgue unique invariant (Lasota–Yorke / Ionescu-Tulcea–Marinescu).
- **P3.** `D_N(h)→0 ⟺` every weak-* limit of `ν_N` is ×16×3-invariant (§2.1).
- **P4.** `\mathcal U_3` is an isometry on L²(μ); it admits no contraction spectral gap (§2.2).
- **P5.** ×16×3 positive-entropy rigidity ⇒ Haar (Rudolph–Johnson 1990, imported classical).
- **P6.** `D_N→0` does not imply normality (Kempner firewall, FK-1/FK-2).

### CONJECTURED / CONDITIONAL

- **C1 (conditional).** `D_N(h)→0` for all `h≠0` **plus** atomlessness/positive-entropy in every joint component ⇒ π base-16 normal. (Rudolph–Johnson + SGO-09; premises for the *specific* BBP orbit OPEN.)
- **C2 (universal, OPEN).** Furstenberg ×16×3 measure conjecture: the only non-atomic ×16×3-invariant ergodic measure is Lebesgue.

### THE EXACT GAP

> **No transfer-operator spectral gap can convert the ×16 orbit's Weyl sum from the modulus bound DC-1 to signed `o(N)`, because the ×16 gap lives on the same `16^k` Fourier ladder that van der Corput differencing never leaves (SK2-H FACT 1). The ×3 defect `D_N(h)→0` is *equivalent* to joint ×16×3-invariance of every limit measure, whose decisive rigidity step is the universal Furstenberg ×2×3 (×16×3) measure conjecture — resolved only in the positive-entropy case by Rudolph–Johnson; the zero-entropy, non-atomic, jointly-invariant case is OPEN and is exactly the same wall already mapped as AR-5 / FK-3. A spectral gap for the ×3 Koopman operator on L² of the ×16-invariant limit measure does not exist (it is an isometry) and, even if a rigidity gap were posited, it would be the Furstenberg conjecture itself — not a transfer-operator corollary.**

> **Relation to Hochman–Shmerkin (obligation B).** The sibling obligation-B note (`ENTROPY_DIMENSION.md`) correctly identifies that Hochman–Shmerkin (2015, *Equidistribution from fractal measures*) supplies the *conditional* step: a ×16-invariant measure with **positive entropy** (equivalently positive lower dimension) that is *also* ×3-invariant must be Lebesgue — this is the entropy-dimension avatar of Rudolph's positive-entropy rigidity (Hochman `h = dim·log16` + the HS equidistribution theorem). **But this does not discharge obligation (A).** Hochman–Shmerkin still requires the *premise* that the ×16-invariant limit measure is ×3-invariant, i.e. precisely `D_N(h)→0`, which is the object of this document and is **not** produced by any transfer-operator gap. Obligations (A) and (B) are independent and both open for the specific BBP orbit; only their *conjunction* triggers the rigidity to `h=log16` (normality).

---

## 4b. Cross-reference to obligation (B)

This document is obligation **(A)** (×3-invariance via the transfer/spectral route). Its sibling
`ENTROPY_DIMENSION.md` (same directory) is obligation **(B)** (`dim_* μ > 0` ⟺ positive entropy via
Furstenberg/Hochman `h = dim_* · log 16`). The two obligations are **independent premises** that,
jointly, trigger Rudolph–Johnson / Hochman–Shmerkin rigidity to normality. The honest status:

- (A) `D_N(h)→0` = ×3-invariance of the limit measure: **OPEN** (this document; not a spectral gap).
- (B) `dim_* μ > 0` = positive entropy of π's base-16 digits: **OPEN** (finite irrationality exponent does not imply it).
- (A) ∧ (B) ⇒ π base-16 normal: **CONDITIONAL** (Rudolph–Johnson + Hochman `h=dim·log16`).

No single route discharges both; each is a genuinely open, strictly-weaker-than-normality statement.

## 5. Cheapest next step

1. **Attack the zero-entropy joint-invariant classification** for the *specific* BBP orbit — the only genuinely open lever. Specifically: derive a source-specific bound on the **digit-carry constraint** of ×16×3-invariant measures (the FK-3 "zero-entropy digit carry constraint"), aiming to rule out non-atomic zero-entropy joint-invariant components for the four-pole `U_0=0` source. This is the one place a source-specific (non-universal) theorem could advance the gate.
2. **Do not** re-run the ×16 transfer operator or the Weyl cancellation route: both are confirmed to terminate at the modulus/DC-1 wall.
3. Record any *negative* (obstruction) result as a `REFUTED`/`PROVED-negative` ledger entry with receipt; do not mint a new claim namespace without collision check (`tests/test_claim_namespace_collisions`).

**No push, no merge, no publication.** π normality: OPEN. RH: OPEN.
