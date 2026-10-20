# Arithmetic Frontier (Operation Rigidity Forge, Part VII)

> **Academic Main VII status update:** this is a historical method dossier.
> CLOUD-ABC-01/05 now prove the primitive moment bound and full mean for
> 0≤t<2/3; see [the independent reconstruction](ACADEMIC_VII_ABC_REVIEW.md).
> The diagonal t<1/2 ceiling below remains a limitation of that method.
> The endpoint t=2/3 and integer abc remain open. Historical receipts are unchanged.

**Date:** 2026-10-20. **Branch:** `research/rf-arith-2026-10-20` (off `e2f92a6`). **Status:** DRAFT, not merged.
**Modules:** `observational_succ/abc_decomposition.py` (section 6), `observational_succ/goldbach_circle.py` (section 7).
**Tests:** `tests/test_abc_decomposition.py`, `tests/test_goldbach_circle.py` — **31 pass, 0 fail**.
**Firewall:** exact arithmetic throughout; floats appear only in `*_evidence` functions, never as certificates.
**abc OPEN. Binary Goldbach OPEN. RH not used. No new theorem claimed.**

This dossier develops a **different method** from `abc_triple_moment.py` (ABC-TMB-01): where that module runs a
diagonal Cauchy–Schwarz on the second moment, here we decompose `ris(n)` **exactly over its prime-power
exponent layers** — the exact, `eps0 = 0` specialisation of the anatomy decomposition (Lemma 2.2) of
Bernert–Browning–Lichtman–Teräväinen, [arXiv:2410.12234v2](https://arxiv.org/abs/2410.12234) (May 2026) — and
use the decomposition to **localise the obstruction** to pushing past `t = 1/2`. For Goldbach we build an
**exact additive circle-method skeleton** and recover two classical objects.

---

## 6. abc — the exponent-layer anatomy and the exact obstruction past t = 1/2

### 6.0 Re-derivation + census anchor (confirm ABC-TMB-01)

`S_t(X) = Σ_{a+b=c≤X,(a,b)=1} ris(abc)^t ≤ M(t)·M(2t)·X²` for rational `0 ≤ t < 1/2` is **re-confirmed**;
`t = 1/2` is a **Cauchy–Schwarz method limit** (binding inner exponent `θ = 2t < 1`), not a growth threshold.
The anchor is reproduced **two independent ways** (`census_anchor_S1`): Route A `integer_moment(24,1)=557`; Route B
direct enumeration with `ris` rebuilt from the exact layer product (ABC-DEC-01) `= 557`. They agree exactly.

### 6.1 ABC-DEC-01 — exact layer anatomy (BBLT Lemma 2.2, `eps0 = 0`)

**Statement (PROVED LOCAL — exact algebraic identity; machine-checked on `[1,3000)`).**
With the exponent-layer radical `m_j(n) = Π_{p : v_p(n)=j} p`:

> (i) `n = Π_{j≥1} m_j(n)^j`   (ii) `rad(n) = Π_{j≥1} m_j(n)`   (iii) `ris(n) = Π_{j≥2} m_j(n)^{j-1}`,
> the `m_j` are **pairwise coprime**, and if `max_p v_p(n) = E` then every product truncates at `j ≤ E` with
> **no tail** (the `n₀ = 1`, `eps0 = 0` case of BBLT Lemma 2.2, `n = n₀·Π_{j=1}^{d} n_j^j`).

Hence the exact moment factorisation `ris(n)^t = Π_{j≥2} m_j(n)^{t(j-1)}`, and on a primitive triple
(pairwise coprime) `ris(abc)^t = Π_j [m_j(a)m_j(b)m_j(c)]^{t(j-1)}`. This is the SUCC prime-power form of
BBLT's anatomy with the `n^{eps0}` slack replaced by **exact equality** on any bounded-exponent class.
Receipt: `layer_anatomy(n).identity_holds` is `True` for every `n` tested; `bblt_anatomy(n,d)["n0"]==1 ⇔
max_exponent(n)≤d`.

### 6.2 ABC-DEC-02 — the uniform per-layer threshold (the obstruction, localised)

**Statement (PROVED LOCAL conditional on ABC-CLK-02).** The layer-`j` (`v_p = j` exactly) `p`-adic Haar
density is `(p−1)/p^{j+1}` and carries `ris(p^j)^θ = p^{(j−1)θ}`, so its per-prime contribution is
`(p−1)·p^{(j−1)θ − j − 1}`, **leading exponent `(j−1)θ − j`**. The Euler product `Σ_p` converges

> **iff `(j−1)θ − j < −1` ⟺ `θ < 1`, INDEPENDENT of the layer index `j ≥ 2`.**

Consequences (all exact; `layer_mean_leading_exponent`, `uniform_layer_threshold`, `cauchy_schwarz_ceiling`):

- **(a)** the `ris^θ` averaging constant is finite iff `θ < 1`; **every** layer hits the same `θ = 1` wall,
  so the square layer `j = 2` is only the *first* obstruction, not the *only* one.
- **(b)** restricting to a bounded-exponent class `{max v_p ≤ E}` **truncates the layers** (constant
  `M_E(θ) ≤ M(θ)`) but does **not** move the threshold `θ < 1`.
- **(c)** therefore the Cauchy–Schwarz ceiling `t < 1/2` (needs inner `θ = 2t < 1`) is **not liftable** by
  bounding the exponent or deleting any single layer. **Decisive NO-GO for the elementary diagonal route.**

The exact local Haar mean `E_p(θ) = (p−1)/p·(1 + p^{−θ}/(p^{1−θ}−1))` is exposed as a **certified rational
two-sided enclosure** (`local_ris_mean_factor_enclosure`); its product over `p` converges iff `θ < 1` — the
**same threshold** as the rigorous ABC-CLK-02 constant `M(θ)`, cross-confirmed by an independent (Haar-local)
route. (Per the ABC-CLK discipline this is a conditional `p`-adic Haar proportion, **not** an independence
claim for bounded integers.)

### 6.3 ABC-DEC-03 — a different mechanism, and the machinery boundary

**Did a distinctly different mechanism beat `t = 1/2`? HONEST ANSWER: NO (rigorously).**

The different mechanism is the **additive-correlation / circle-method** view of the inner sum
`I(c) = Σ_{a+b=c,(a,b)=1} ris(a)^t ris(b)^t`, which the Cauchy–Schwarz route bounds by its **diagonal**
majorant `D(c) = Σ_{n<c} ris(n)^{2t}` (this is exactly what forces `2t < 1`). The circle-method **heuristic**
predicts `I(c) ≍ c` for **all** `t < 1` (hence `S_t ≍ X²` up to `t < 1`, not `t < 1/2`).

EVIDENCE (`additive_vs_diagonal_evidence`, floats, NOT a certificate): the ratio `I(c)/D(c)` **shrinks** as `c`
grows (`t = 0.7`): `0.202, 0.149, 0.128, 0.096` at `c = 64,128,256,512`, while `I(c)/c` stays `O(1)`
(`0.88, 1.10, 1.49, 1.52`). So the diagonal bound is **increasingly lossy** and the true correlation behaves
like `c` — consistent with the heuristic threshold `t < 1`.

But the census **cannot establish** the `X²` bound past `1/2` (`moment_ratio_growth_evidence`): `S_t(X)/X²`
drifts **upward even for PROVEN `t = 0.4`** (`0.589 → 0.727` over `X=64→512`, approaching its finite limit
from below), so a finite census cannot distinguish a bounded ratio from a slowly growing one. For
`t = 0.9` the drift is faster (`2.13 → 6.57`). This is AGENTS.md item 8 in action: **a finite census is
evidence, never a proof of a uniform bound.**

**Which estimates are elementary vs need machinery** (`machinery_boundary`):

| piece | status | tool |
|---|---|---|
| ABC-DEC-01 layer anatomy | PROVED LOCAL (exact identity) | elementary algebra |
| ABC-DEC-02 per-layer exponents `(j−1)θ−j`, uniform `θ<1`, `t<1/2` ceiling | PROVED LOCAL (cond. ABC-CLK-02) | elementary + Euler product |
| bounded-exponent truncation `M_E(θ) ≤ M(θ)` | PROVED LOCAL | elementary |
| **passing `t = 1/2`** (cancellation in `I(c)` below the diagonal) | **OPEN — not in SUCC** | **BBLT Prop. 3.1 (Fourier 2nd/4th-moment exponential-sum bounds) + Prop. 4.1 (Heath-Brown geometry-of-numbers integer-point counts)** |

SUCC's Euler-product toolkit is **structurally diagonal**: it cannot see the additive constraint `a+b=c`, which
is precisely the cancellation BBLT's Fourier + geometry-of-numbers inputs supply. BBLT's headline is an
**exceptional-set** exponent (Thm 1.2 `N_λ(X) ≪ X^{(23λ+3)/40+ε}`, Thm 1.3 `X^{3/5+ε}` for `λ∈(9/10,1)`) — a
**different object** from the `ris^t` moment, so no exponent comparison is made. **abc stays OPEN.**

### 6.4 The bounded-exponent decomposition theorem — verdict

**ABC-DEC-01 is the recovered bounded-exponent decomposition theorem** (exact layer factorisation of
`ris^t`, exactly the `eps0 = 0` BBLT Lemma 2.2), and **ABC-DEC-02 is the decisive no-go** that pins the exact
obstruction: the `θ = 1` wall is **layer-uniform**, so bounded exponent cannot lift `t < 1/2`. Conditional
lemma: **ABC-CLK-02** (the `ris^θ` Dirichlet-density averaging bound) for the quantitative constant; the
layer exponents themselves are unconditional exact arithmetic.

---

## 7. Goldbach — the exact additive circle-method skeleton

### 7.1 GC-01 — exact finite additive Fourier identity (CLASSICAL; PROVED LOCAL)

With `e(x) = e^{2πix}` and the **additive** carrier `F_N(θ) = Σ_{n=1}^{N-1} Λ(n) e(nθ)`:

> `R_Λ(N) = ∫_0^1 F_N(θ)² e(−Nθ) dθ = [z^N] F_N(z)² = (1/Q) Σ_{j=0}^{Q-1} F_N(ω^j)² ω^{−Nj}` (`ω=e(1/Q)`, `Q ≥ N`).

**It is `F²`, NOT `|F|²`.** Three routes computed **exactly** (sympy) and cross-checked against the direct
additive convolution `goldbach_representation_R_Lambda` for `4 ≤ N < 30` (poly route) and `N ∈ {4,…,10}`
(roots-of-unity route): all match (e.g. `R_Λ(6) = 2 log²2 + log²3`). `R_Lambda_from_fourier_poly`,
`R_Lambda_from_dft`, `fourier_identity_check`.

**Firewall (made exact).** The `|F|²` ("positive-definite autocorrelation") object extracts the **difference**
diagonal `Σ_{a−b=N} Λ(a)Λ(b)`, which is **identically 0** on the window `1 ≤ a,b ≤ N−1` (`difference_diagonal`,
verified `= 0` for `4 ≤ N < 30`). So no positive-definite `|F|²` route reaches the **sum** problem — the sum
problem needs `F²`. This is the exact form of the BS-G1 dichotomy; it is the **additive**, not multiplicative,
carrier (cf. `arithmetic_interactions.illegal_interchange_witness`, `N = 5`).

### 7.2 Genuine prime support vs higher-prime-power contamination (exact)

`support_split(N)` gives the exact split `R_Λ(N) = Σ_{p+q=N, p,q prime} log p log q + (contamination)`, where
contamination collects terms with `a = p^k` or `b = q^l`, `k,l ≥ 2` (`Λ(p^k) = log p`). `decomposition_exact`
is `True` for `4 ≤ N < 60`; e.g. `N = 8` has true pairs `(3,5),(5,3)` and contamination term `(4,4)` (`4 = 2²`).

### 7.3 GC-02 — Hardy–Littlewood singular series (CLASSICAL object + CONJECTURED asymptotic)

**Object (CLASSICAL; exact, certified).** `𝔖(N) = Π_p 𝔖_p(N)`, `𝔖_p(N) = 1 + 1/(p−1)` if `p | N`, else
`1 − 1/(p−1)²`. `𝔖(N) = 0` for `N` odd (the `p = 2`, `N` odd factor `1 − 1/(2−1)² = 0` — the local obstruction
to two odd primes). Computed as a **certified rational two-sided enclosure** `singular_series_enclosure` via the
tail bound `Π_{p>P}(1 − 1/(p−1)²) ∈ [1 − 1/(P−1), 1]`. `twin_prime_constant_enclosure` brackets
`2C₂ ≈ 1.3203236` exactly.

**Asymptotic (CONJECTURED / OPEN).** The major-arc contribution to `R_Λ(N)` is `𝔖(N)·N·(1+o(1))` (CLASSICAL,
via Siegel–Walfisz). The claim that the **full** `R_Λ(N) ~ 𝔖(N)·N` is **binary-Goldbach-type and OPEN**: the
minor-arc smallness is unknown for the binary problem (ternary is Vinogradov's theorem).
`goldbach_main_term_enclosure` returns the **prediction** `𝔖(N)·N` only, clearly labelled.

EVIDENCE (`singular_series_comparison_evidence`, floats): `R_Λ(N)/N` tracks `𝔖(N)` in order of magnitude with
slow convergence (`N=2310`: `R_Λ/N ≈ 4.479` vs `𝔖 ∈ [4.693, 4.695]`). Finite-sample only; **no Goldbach claim.**

### 7.4 Major/minor-arc structure exposed

`farey_major_arcs(Q,N)` exposes the exact major-arc centres `a/q` (`q ≤ Q`, `(a,q)=1`) and radii `1/(qN)`;
`arc_decomposition_summary` labels the major-arc contribution **CLASSICAL** (`𝔖(N)·N`) and the minor-arc bound
**OPEN for binary Goldbach**. No asymptotic is evaluated; the structure is exposed for downstream work.

### 7.5 Recovered classical lemma — verdict

**The recovered exact finite identity is GC-01**: `R_Λ(N) = [z^N] F_N(z)² = ∫_0^1 F_N(θ)² e(−Nθ) dθ`, stated
with full hypotheses (window `M = N−1`, `e(x)=e^{2πix}`, `F²` not `|F|²`), tested exactly on small `N`, labelled
**CLASSICAL**. The singular series `𝔖(N)` is recovered as a CLASSICAL exact object (certified enclosure); its
**asymptotic role stays CONJECTURED/OPEN**. **Binary Goldbach is OPEN; no Goldbach claim is made.**

---

## Ledger

| ID | statement | status | conditional on |
|---|---|---|---|
| ABC-DEC-01 | exact layer anatomy `ris(n)^t = Π_{j≥2} m_j^{t(j-1)}`, `eps0=0` BBLT Lemma 2.2 | PROVED LOCAL (exact identity) | — |
| ABC-DEC-02 | per-layer exponent `(j−1)θ−j`; threshold `θ<1` uniform over `j`; CS ceiling `t<1/2` not liftable | PROVED LOCAL | ABC-CLK-02 (quantitative constant) |
| ABC-DEC-03 | different mechanism does NOT beat `t=1/2`; gap = BBLT Fourier (Prop 3.1) + geometry-of-numbers (Prop 4.1) | NO-GO (gap stated); EVIDENCE labelled | — |
| GC-01 | exact finite additive Fourier identity `R_Λ(N)=[z^N]F²`; `F²≠|F|²` firewall | CLASSICAL / PROVED LOCAL | — |
| GC-02 (object) | Hardy–Littlewood singular series `𝔖(N)`, certified enclosure, `𝔖(odd)=0` | CLASSICAL | — |
| GC-02 (asymptotic) | `R_Λ(N) ~ 𝔖(N)·N` | CONJECTURED / OPEN | binary Goldbach (minor arcs) |

**Next falsification opportunity.** (abc) audit ABC-CLK-02 itself, the one lemma ABC-DEC-02 leans on; or
attempt a bound on `I(c)` using the `a+b=c` constraint that beats the diagonal (would require importing a
Fourier/large-sieve input — flagged as out of SUCC's current toolkit). (Goldbach) attempt a **rigorous**
major-arc evaluation under an explicitly imported Siegel–Walfisz statement and bound the minor-arc measure
exposed in §7.4 — the binary minor-arc bound is where the problem stays OPEN.
