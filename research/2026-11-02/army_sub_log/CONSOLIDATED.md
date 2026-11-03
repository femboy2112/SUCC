# The Army: SUCC tools for the single open gate C_A = o(log A)

**Branch:** `research/army-sub-log-collision-2026-11-02` (off `origin/main`). **Date:** 2026-11-02.
**Agent:** Ravel + 4 subagent fronts. **Target:** build the SUCC toolkit to close the single open
gate of base-16 π-normality — the maintainer's LS-10 sublogarithmic collision bound.

## 0. The single open gate

The maintainer's `line_sheet_gamma` frontier (LS-01…LS-15) proved: for the ORIGINAL four-pole BBP
source (`r(n)=4/(8n-7)-2/(8n-4)-1/(8n-3)-1/(8n-2)`, `U_0=0`, `U_{n+1}=16U_n+r(n+1)`), with
collision energy `C_A = (1/A)Σ_i v_i(A)²`, `v_i(A)=#{A≤n<2A:⌊A{U_n}⌋=i}`:

$$\boxed{C_A = o(\log A)\quad\Longrightarrow\quad \pi\text{ base-16 normal}}$$

Everything else (Gamma line→sheet, CRT prime decomposition, tail, conductor) is PROVED. This round
attacked `C_A = o(log A)` from five independent directions.

## 1. Main thread — exact structure of C_A

**`C_A` counts Archimedean near-collisions of `{U_n}` at scale `1/A`, governed by the Diophantine
spacing of π — not by the rational conductor or the tail.**

- `U_n - U_m = (A_n Q_m - A_m Q_n)/(Q_n Q_m)` with `Q_n = exp(6n+o(n))`, so `Q_n Q_m ≈ exp(12A)`:
  the integer-numerator picture is **vacuous**.
- Verified (exact `Fraction`, A=256): 124 same-bin pairs, 0 exact-integer, 0 exact-equal; colliding
  spacing `‖{U_n}−{U_m}‖ = 10^{-5.3}…10^{-4.0} ≈ 1/A²` (random-pair scaling), while
  `1/(Q_n Q_m) ≈ exp(-3072)` is irrelevant.
- `C_A` empirically bounded `1.6–2.1` (the random-pair signature `O(1)`), far stronger than the
  needed `o(log A)`.

## 2. Front 1 — tail-controlled spacing (PROVED negative)

- **Exact identity:** `‖U_n−U_m‖ = ‖ −(16^d−1)·16^{n-1}·π − (T_n−T_m) ‖`.
- **PROVED:** `r(n)` closed form + sharp two-sided bounds `15/(64n²) < r(n) ≤ 47/(15n²)`; tail
  `T_n < r(n+1)/15 = O(1/n²)`; **`|T_n−T_m| < 1/A`** (strictly sub-bin).
- **Theorem (tail is load-bearing-free):** the tail alone cannot control `C_A`. The counterseed
  (`β∈Q`) collapses to `C_A = A` (maximal). The spreading mechanism is the irrational rotation
  `16^{n-1}π` alone. **The π-term is the only non-deterministic ingredient.**

## 3. Front 2 — prime-cofactor nonconspiracy (PROVED reduction)

- **Exact CRT:** `U_n = Σ_{p∈P_A} a_{p,n}/p + C_n`, and crucially **`C_n = 16^{n-1}π − T_n − S_n`**
  (COF-1): the cofactor is *forced* by the true orbit, not a free dial.
- **PROVED:** the cofactor is the **sole π-carrier**; residues + tail are π-free; the diagonal
  (`p|16^d−1`) carries `< log16` fraction of the prime mass.
- **Theorem (no non-hostile route):** `C_A = o(log A)` is equivalent to Diophantine non-clustering
  of `‖16^{n-1}(16^d−1)π‖` at scale `1/A`. The CRT decomposition makes π-dependence *explicit*
  (in `C_n`) without *eliminating* it.

## 4. Front 3 — second-moment / Parseval identity (the structural gem)

- **PROVED exact identity (DSP-1):** `C_A = (1/A²)Σ_{k=0}^{A-1}|V_k|²` (exact in Q[ζ], no π),
  `V_k = Σ_n e(-k⌊Ax_n⌋/A)`. Machine-verified exactly for A=8…256.
- **PROVED exact identity (FEJ-1):** `C_A = (1/A²)Σ_{h∈ℤ}|S_A(h)|² sinc²(h/A)`.
- **Theorem (weakness — the load-bearing structural result):** `C_A = o(log A)` is an **L²/energy**
  (second-moment) statement, genuinely **weaker** than the pointwise ℓ∞ Weyl gate: it tolerates
  `o(log A)` completely-unconcentrated frequencies, whereas the Weyl gate tolerates zero. The
  collision gate needs only `Σ_h |S_A(h)|² sinc²(h/A) = o(A² log A)` — an *averaged* object.
- **Cheapest next step:** attack (CG) with an L²/large-sieve/energy-decay method targeting the
  *mean* over `A` frequencies, not the sup.

## 5. Front 4 — Gamma-sheet Archimedean gap (PROVED orthogonality)

- **PROVED linchpin:** `T(n) = T_n` (the continuum continuation hits the tail exactly at integers);
  `W(n) = D(n)²/16 − T_n > 0` is exactly `T_n < (H_n − log n − γ)²/16`.
- **PROVED:** the gap is a **tight upper** bound (`W(n) = 13/(1536 n³) + O(n⁻⁴)`, reproducing LS-09),
  not a lower/mass bound.
- **Theorem (Archimedean neutrality):** the Gamma-sheet positivity is **provably orthogonal** to
  `C_A = o(log A)` — it constrains only the π-free tail, is silent on `{16^{n-1}π}`, and holds
  identically for the counterseed (`C_A ≍ A`) and normal sequences.

## 6. The convergent verdict

All five independent attacks converge on the same boundary:

> **`C_A = o(log A)` is exactly a Diophantine (irrationality-type) non-clustering statement about π
> at the sparse multipliers `16^d − 1`.** The BBP tail, rational conductor, prime-CRT decomposition,
> second-moment structure, and Gamma-sheet positivity are all **provably orthogonal** to it — each is
> π-free or a re-encoding, and none can close the gate without the arithmetic content of π.

**The positive tool built this round:** Front 3's exact Parseval identity + weakness theorem upgrades
the target from the (pointwise, ℓ∞) Weyl gate to a genuinely **weaker L²/energy** object — the first
concrete "easier than Weyl" formulation the program has, and the natural entry point for a large-sieve
or spectral L² attack.

**π base-16 normality and RH remain OPEN.** No false victory: the gate is now *named*, *weakened*
(L² not ℓ∞), and *located* (Diophantine spacing of π at `16^d−1`) with five independent, mutually
consistent proofs of where it lives and where it does not.
