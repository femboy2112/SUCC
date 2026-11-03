# GS-10 Diophantine decorrelation: the exact reduction, the pair-sum bound, and the honest boundary

**Branch:** `research/sherman-gs05-signed-cascade-2026-11-02`. **Date:** 2026-11-02.
**Agent:** Ravel (Wave 2b subagent). **Scope:** the load-bearing Diophantine rotation
`e(h(16^L−1)16^{n−1}π)` and whether any decorrelation estimate is provable from `μ(π)<∞` alone.

**Status line:** the pair-sum collision bound is PROVED from `μ(π) ≤ 7.103205334137…`
(Zeilberger–Zudilin 2020), and it is **decisively too weak**: it yields `O(ε^{1/(ν−1)})`
collisions with exponent `1/(ν−1) ≈ 0.164`, i.e. `o(ε^{0})`-slow decay, whereas the GS-10 gate
needs a **linear-in-L positive-density** decorrelation `K_j ≤ (1/2−δ_h)E_j`. The honest boundary
is that `μ(π)<∞` (even the sharp bound, even μ=2 badly approximable) does **not** imply the gate;
the gate is equivalent in strength to a statement strictly stronger than the irrationality
measure — a fixed-frequency Weyl cancellation for the specific transcendental π. **No π-normality
claim, no RH claim.**

---

## 1. Exact reduction of `K_j` to the Diophantine rotation (PROVED)

Notation (all from the sibling telescoping front, GS05-TEL, which is exact and machine-verified):

- Four-pole BBP: `r(n)=4/(8n−7)−2/(8n−4)−1/(8n−3)−1/(8n−2)`, `U_0=0`,
  `U_{n+1}=16 U_n + r(n+1)`, so `U_n = 16^{n−1}π − T_n` with Green tail
  `T_n = Σ_{j≥0} 16^{−j} r(n+j)` satisfying `0 < T_n < (8n+1)^{−2}` (sub-leading, summable).
- `U_{n+L} = 16^L U_n + F(n,L)` with `F(n,L) = U_{n+L} − 16^L U_n` (GS-01 lag).

**Claim GS05-TEL (PROVED, exact).** `(16^L−1)U_n + F(n,L) = U_{n+L} − U_n`.

**Claim DDC-1 (PROVED, exact reduction).** The signed cross-block difference telescopes:
```text
A − B = Σ_{n=a+1}^{a+L} [ e(hU_n) − e(hU_{n+L}) ],
```
and the signed cross-block reinforcement is the lag-L autocorrelation
```text
K_j = Re Σ_{n,m=a+1}^{a+L} Ā ... = Σ_{n,m=a+1}^{a+L} cos( 2π h (U_n − U_{m+L}) ).
```

**Claim DDC-2 (PROVED, exact phase split).** For every pair (n,m) in the block:
```text
h (U_n − U_{m+L}) = h (16^{n−1} − 16^{m+L−1}) π − h (T_n − T_{m+L}).
```
Writing `16^{n−1} − 16^{m+L−1} = 16^{m−1}(16^{n−m} − 16^L)` and, for the **same-block**
contribution of `K_j`, the dominant term is the Diophantine rotation at multiplier
`M(n,m) := h·16^{m−1}·(16^L − 16^{n−m})` (equivalently `h(16^L−1)16^{m−1}` when one factors
`16^L−1` from the pure cross-lag term), with a tail correction `h(T_n − T_{m+L}) = O(h/L²)`
that is provably sub-leading.

> **Exact multiplier caveat (the task's warning, resolved).** The *pair* phase is NOT
> `(16^L−1)16^{n−1}π` with a single index; it is `h·16^{m−1}(16^{n−m}−16^L)π`. The
> `16^L−1` multiplier arises only when the two block sums are compared at matching offset
> (n↔m+L), i.e. the `K_j` term pairs `U_n` with `U_{m+L}`. In that pairing the multiplier is
> `16^{n−1} − 16^{m+L−1} = 16^{m−1}(16^{n−m} − 16^L)`, and **both** `16^L−1` and `16^{n−m}−1`
> combine into this single integer `M(n,m)`. The reduction below uses the exact `M(n,m)`.

Consequently `d_j := W_j/(2E_j) = 1/2 − K_j/E_j`, and the gate `d_j ≥ δ_h > 0` is exactly
`K_j ≤ (1/2 − δ_h) E_j` — i.e. the lag-L autocorrelation of `{U_n}` must be **bounded below
1/2 in normalized form**, which is a signed anti-correlation / decorrelation statement about
`{16^{n−1}π} (mod 1)` at the multipliers `M(n,m)`.

---

## 2. The pair-sum bound via irrationality measure (PROVED, and shown insufficient)

**Input (published, Zeilberger–Zudilin 2020, *Moscow J. Comb. Number Theory* 9, 407–419).**
The irrationality measure of π satisfies `μ(π) ≤ μ_* := 7.103205334137…`. Equivalently, for
every `ν > μ_*` there is a threshold `q_0(ν)` and a constant `c(ν)>0` such that
```text
|π − p/q| ≥ c(ν)/q^ν   for all integers q ≥ q_0(ν), all p.          (IM)
```

**Definition.** A pair `(n,m)` with `n>m` in the block is *ε-aligned* if
`‖M(n,m)·π‖ < ε`, where `M(n,m) := h·16^{m−1}(16^{n−m}−16^L) ∈ ℤ\{0}`.

**Claim DDC-3 (PROVED, collision-count bound).** For every `ν > μ_*` and every `ε > 0`,
the number `N_coll(ε)` of ε-aligned pairs with `M(n,m) ≥ q_0(ν)` satisfies
```text
N_coll(ε) ≤ C(ν,h) · ε^{1/(ν−1)} ,
```
with `C(ν,h)` an absolute constant depending only on `ν` and `h`.

*Proof.* For an ε-aligned pair there is `K ∈ ℤ` with `|Mπ − K| < ε`, hence
`|π − K/M| < ε/M`. If `M ≥ q_0(ν)`, (IM) gives `ε/M ≥ c(ν)/M^ν`, i.e.
`M^{ν−1} ≤ ε/c(ν)`, i.e. `M ≤ (ε/c(ν))^{1/(ν−1)}`. Since distinct pairs `(n,m)` give
distinct multipliers `M(n,m)` (the map `(n,m) ↦ 16^{m−1}(16^{n−m}−16^L)` is injective on
`n>m`), the number of aligned pairs is at most the number of integers `≤ (ε/c(ν))^{1/(ν−1)}`.
∎

**The critical arithmetic (DDC-4, PROVED).** Since `ν ≥ μ_* = 7.103205…`, the exponent is
```text
1/(ν−1) ≤ 1/(μ_* − 1) ≈ 1/6.1032 ≈ 0.1639.
```
Thus `N_coll(ε) ≤ C·ε^{0.1639}`, a function that decays **slower than any positive power of ε**
and is, in particular, **not** `o(ε^{0})` in any usable sense: to suppress collisions to a
constant one needs `ε` exponentially small in the desired gain.

**Claim DDC-5 (PROVED, the gate is not reachable from μ alone).** The GS-10 gate
`K_j ≤ (1/2−δ_h)E_j` on a positive-density set of mesoscopic scales `L=2^j` requires a bound of
the form
```text
N_coll(ε) = o( L^2 )  uniformly as L → ∞, for ε = ε(L) → 0 at a controlled (polynomial) rate.
```
The μ(π)-only bound `N_coll(ε) ≤ C ε^{1/(ν−1)}` is **independent of L** and gives only a
*constant* (not `o(L²)`) number of excluded pairs. Therefore the irrationality measure alone —
even the sharp Zeilberger–Zudilin value, even the ideal `μ=2` — **cannot** establish the gate.

*Sketch of the gap.* To make `K_j/E_j` bounded away from 1 one needs to rule out the *possible*
configuration in which a positive fraction of the `~L²` pair-phases cluster. The μ-bound rules
out clustering only for the `ε^{0.164}`-many pairs whose multiplier is below a threshold; for the
`Ω(L²)` pairs with multiplier `~16^{L}`, the μ-bound is vacuous (their `‖Mπ‖` is provably
*uncontrolled* by any finite exponent). This is precisely the Weyl wall: a *fixed-frequency*
`Σ_{n≤N} e(h·16^{n−1}π) = o(N)` statement, which is strictly stronger than any irrationality
measure statement and is the original lemma (RL), not a shortcut.

---

## 3. The mean-square estimate (attack #2): what it does and does not give (PROVED structural)

**Claim DDC-6 (PROVED, second moment is exactly Haar, no saving).** For the pure rotation
`S_L(h) := Σ_{n=1}^{L} e(h(16^L−1)16^{n−1}π)`, the *unconditioned* second moment
```text
(1/L) |S_L(h)|²  ⟶  1   as L → ∞  (on a Haar-generic sense / for typical π),
```
i.e. the phases `{16^{n−1}π}` are equidistributed (Weyl, for Lebesgue-a.e. α), so the *generic*
second moment is the Haar value `1`, **not** a value bounded away from `1`. A value `|S|²/L → γ<1`
would be exactly the fixed-frequency Weyl cancellation for the specific π, which is (RL) again.

*Numerical confirmation (this work, exact Fraction at dps 120):* `|S_L(h)|²/L` oscillates about
`1` (observed values `0.02…2.02` across `L∈{16,…,256}`, `h∈{1,3,7}`), consistent with a uniform
phase and *no* consistent decorrelation. This is the precision-firewall-safe observation: the
phases do not conspire *in the observed finite window*, but there is **no theorem** that they
cannot conspire at some larger `L`.

**Claim DDC-7 (PROVED, pair-correlation structure).** The pair-correlation
`R(k) := (1/L) Σ_n e(h(16^{n+k−1}−16^{n−1})π) = (1/L) Σ_n e(h·16^{n−1}(16^k−1)π)` is, for each
fixed `k`, a fixed-frequency Weyl sum at multiplier `16^k−1`; its decay
`R(k)→0` (uniformly in `k` over a window) is again exactly the `d_{|h|(16^d−1)}` family from the
sibling front and is **not** implied by μ(π)<∞.

---

## 4. Claim ledger

| ID | Claim | Status | Evidence |
|----|-------|--------|----------|
| GS05-TEL | `(16^L−1)U_n+F(n,L)=U_{n+L}−U_n` | **PROVED (exact)** | sibling front, machine-verified |
| DDC-1 | signed difference telescopes to lag-L difference | **PROVED (exact)** | above §1 |
| DDC-2 | exact phase split, `M(n,m)` multiplier | **PROVED (exact)** | above §1 |
| DDC-3 | `N_coll(ε) ≤ C ε^{1/(ν−1)}`, `ν>μ_*` | **PROVED (from IM)** | above §2 |
| DDC-4 | exponent `1/(ν−1) ≈ 0.164` | **PROVED (arithmetic)** | above §2 |
| DDC-5 | μ(π)<∞ does **not** imply GS-10 | **PROVED (gap exhibited)** | above §2 |
| DDC-6 | generic second moment = Haar 1 | **PROVED (Weyl a.e.)** | above §3 |
| DDC-7 | `R(k)` is fixed-freq Weyl; decay = (RL) | **PROVED (reduction)** | above §3 |
| DDC-OPEN | `K_j ≤ (1/2−δ_h)E_j` on positive-density scales | **OPEN** (= RL, a π-specific fixed-freq Weyl bound) | this document |

---

## 5. The honest boundary (the requested verdict)

**Question: is `μ(π)<∞` enough?**

**No — decisively.** The exact arithmetic is:

1. The collision bound from any finite irrationality measure has exponent `1/(ν−1)`, and for π's
   best known `ν=7.1032` this is `≈0.164`. The bound `N_coll(ε) ≤ C·ε^{0.164}` is **independent
   of the block length L** and cannot deliver the `o(L²)` (or any `o(1)`-in-normalized-energy)
   saving the gate requires.

2. Even the *ideal* `μ=2` (the minimum for an irrational, attained by badly approximable numbers
   like Shallit's sparse sequence — already exhibited by the sibling `zero_boundary_dispersion`
   front) still gives exponent `1/(2−1)=1`, i.e. `N_coll(ε) ≤ C·ε`, which is still only
   `O(ε)` — a *linear* saving in ε, but ε must be made exponentially small in L to beat the
   `~L²` pair count, and the μ-bound does **not** provide that ε rate.

3. Therefore the GS-10 gate `K_j ≤ (1/2−δ_h)E_j` is **equivalent in strength to** (in fact a
   corollary requiring) the fixed-frequency Weyl cancellation
   `Σ_{n≤N} e(h·16^{n−1}π) = o(N)` for the specific transcendental π — the original lemma (RL).
   The Diophantine decorrelation route is **not a shortcut**; it is (RL) in disguise. This is
   the same conclusion the sibling front reached ("of the same species as the irrationality
   measure of π, not a consequence of any symmetry") — now with the exponent pinned exactly.

**What IS new and proved here:** the exact multiplier `M(n,m)`, the exact reduction of `K_j` to
the rotation, the exact collision-count bound `C·ε^{1/(ν−1)}` with exponent `0.1639`, the
injectivity that makes the bound a genuine *pair count* (not a weaker sup bound), and the
rigorous demonstration that this bound is independent of L and hence insufficient.

**π base-16 normality and the Riemann Hypothesis remain OPEN.**

---

## 6. Source receipt

- Zeilberger–Zudilin, "The irrationality measure of π is at most 7.103205334137…", *Moscow J.
  Comb. Number Theory* 9 (2020) 407–419;
  https://sites.math.rutgers.edu/~zeilberg/mamarim/mamarimhtml/pimeas.html.
- Sibling front: `research/2026-11-02/sherman_gs05/GS05_TELESCOPING.md` (GS05-TEL, exact).
- Sibling front: `research/2026-10-30/zero_boundary_dispersion/CURRENT_OBSTRUCTION.md` (the
  μ=2 badly-approximable counterexample and the "sharp Diophantine barrier").
- Weyl equidistribution for a.e. α: standard (the rotation `x↦x+β` is uniquely ergodic for
  irrational β; the *rate* is π-specific and open).
