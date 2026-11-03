# Literature reconnaissance: the Weyl gate for π base-16 normality

**Branch:** `research/shen-tzu-weyl-form-2026-11-02`. **Date:** 2026-11-02.
**Agent:** Ravel (main thread). **Scope:** precise status of π base-16 normality and what
external theorems apply to the signed Weyl gate `S_N(h) = Σ_{n≤N} e(h·16^{n-1}π) = o(N)`.

## 1. Status of π base-16 normality: OPEN (confirmed)

- **Bailey–Borwein–Calude–Dinneen–Dumitrescu–Yee, "Normality and the Digits of π" (2012):**
  π normality is open in every base; the paper gives strong *statistical* evidence (trillions of
  digits) but no proof. The BBP formula permits *digit extraction* but does **not** imply
  normality (it is a spigot/closed form, not an equidistribution theorem).
- **Bailey–Borwein, "Pi Day Is Upon Us Again and We Still Do Not Know if Pi Is Normal,"
  Amer. Math. Monthly 121 (2014) 191–206:** explicit statement that π normality is unknown.
- **MathOverflow #163451 ("Normality of π in base 16"):** confirmed answer — BBP does not settle
  base-16 normality.

**Conclusion:** there is **no** known non-trivial bound on the specific Weyl sum
`Σ_{n≤N} e(h·16^{n-1}π)`. The orbit `{16^{n-1}π}` has no published equidistribution bound. This is
genuinely open, and any proof would be novel.

## 2. Irrationality measure (the best available Diophantine input)

- **Zeilberger–Zudilin, Moscow J. Comb. Number Theory 9 (2020) 407–419, arXiv:1912.06345:**
  `μ(π) ≤ 7.103205334137…`. (Improves Salikhov's `7.6063…`.)
- **What it gives:** `|π − p/q| ≥ c(ν)/q^ν` for all `ν > 7.103…`. For the orbit multipliers
  `(16^d−1)16^{n-1}`, this yields only `‖(16^d−1)16^{n-1}π‖ ≥ c·(16^d 16^n)^{−ν}` — an
  **exponential** lower bound `≳ 16^{−c(n+d)}`, which is **far too weak** for the gate (needs
  polynomial `1/N^{1+ε}`). This is the same conclusion reached independently by the
  `diophantine-decorr` and `large-sieve-l2` fronts: `μ(π)<∞` does not close the gate.

## 3. BBP formula (Bailey–Borwein–Plouffe 1997)

- The BBP formula `π = Σ_k 16^{-k}(4/(8k+1)−2/(8k+4)−1/(8k+5)−1/(8k+6))` gives a **spigot**
  algorithm (extract the n-th hex digit without computing predecessors). It is the *source* of the
  four-pole orbit, but it is a **closed form**, not an equidistribution statement. It gives no
  information about the *joint* distribution of digits — only pointwise extraction.

## 4. External rigidity theorems (what would apply, and their premises)

- **Hochman–Shmerkin, Ann. Math. 175 (2012) Thm 1.7/10.4:** if `μ` is `T_{16}`-ergodic with positive
  entropy AND `T_3`-invariant (for multiplicatively independent 16, 3), then `μ` = Lebesgue. This is
  the ×16–×3 rigidity route (WB-10). **Needs:** (A) `T_3`-invariance = signed ×3 defect `D_N(h)→0`
  (proved equivalent to measure rigidity, still OPEN — see `prove-obligation-A` round), and (B)
  positive lower dimension `dim_* μ > 0` (still OPEN).
- **Hochman 2014 (self-similar sets with overlaps):** entropy-dimension identity
  `h_μ(T_{16}) = dim_* μ · log 16`. Makes (B) ⟺ positive entropy, still OPEN.
- **Hochman 2024 (αβ sets):** applies to self-similar/affine sets; the π orbit is *not* such a set
  (it is a single orbit, not a self-similar measure with a generating IFS), so this does not
  directly apply.

## 5. What this means for the army

The literature confirms: **the gate is genuinely open, with no known theorem even close.** The only
usable external inputs are:
1. `μ(π) ≤ 7.103…` — proved insufficient (exponential gap).
2. Hochman–Shmerkin rigidity — needs (A)+(B), both independently open, and (B) is the Diophantine
   dimension statement, not easier.
3. BBP — a source, not a theorem.

**Therefore the signed Weyl gate must be closed by genuinely new mathematics** — a source-specific
signed-cancellation estimate on the four-pole orbit that no known theorem supplies. This is exactly
what the five running fronts (cofiber-decay, ward-ladder, van der Corput, p-adic signed phase,
cell-imbalance) are attempting, each from a distinct angle.

**π base-16 normality and RH remain OPEN.**
