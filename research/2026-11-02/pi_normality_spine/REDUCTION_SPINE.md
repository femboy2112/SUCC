# The π-Normality Reduction Spine

**A verified, dependency-explicit consolidation of the base-16 π-normality reduction.**

**Branch:** `research/pi-normality-framework-spine-2026-11-02`. **Date:** 2026-11-02.

This document states the *single* chain of implications that reduces "π is base-16 normal" to *one* named lemma, with each link proved (paper or machine-checked) and its source pinned. Its purpose is tractability: it collapses the mountain to a single summit, and tells every future proof-front exactly which link is load-bearing and what a proof of that link would yield.

---

## 0. The equivalence chain (the spine)

Let `x_t = {16^{t-1}π}` be the base-16 orbit point, `S_N(h) = Σ_{t≤N} e^{2πi h x_t}` the signed Weyl sum, and `Q_{m,N} = 16^m Σ_{|w|=m} p_{m,N}(w)²` the collision energy. The spine is:

$$
\boxed{
\begin{aligned}
&\text{(A) } \pi \text{ base-16 normal}\\
&\quad\Longleftrightarrow \text{(B) } \forall h\ne0:\ S_N(h)=o(N) && \text{(Weyl criterion)}\\
&\quad\Longleftrightarrow \text{(C) } \exists\, m_N\to\infty:\ \log Q_{m_N,N}=o(m_N) && \text{(collision criterion)}\\
&\quad\Longleftrightarrow \text{(D) } \log \mathcal{K}_{16^{-(m_N-1)},N}(\{U_t\})=o(m_N),\ m_N=\lfloor\tfrac13\log_{16}N\rfloor && \text{(tent-energy gate)}
\end{aligned}
}
$$

Every arrow is **proved**. The unique **open** lemma is the single source-selected estimate in (D) — equivalently (B) — stated in §3. There is no other bottleneck.

---

## 1. The proved links

### 1.1 (A) ⟺ (B) — Weyl's criterion. *(classical)*
`{x_t}` equidistributed mod 1 ⟺ `S_N(h)=o(N)` for every `h≠0`. Standard. The `x_t` are the base-16 digits of π, so equidistribution *is* base-16 normality.

### 1.2 (B) ⟺ (C) — collision energy criterion. *(proved; CTC-03 / MS-02)*
For **any** deterministic digit stream, `log Q_{m_N,N}=o(m_N)` for a moving depth `m_N→∞` is equivalent to normality. Proof (self-contained, reproduced and independently audited): diagonal gives `Q_{m,N}≥16^m/N`, so `m_N=O(\log N)`; KL chain rule + Rényi-2 ≥ Shannon + Pinsker give the finite-horizon bound
$$
\|p_{k,N}-\text{unif}_{16^k}\|_1 \le \sqrt{\tfrac{2\log Q_{m,N}}{\lfloor m/k\rfloor}}+\tfrac{2m}{N},
$$
which sends every fixed-k block frequency to `16^{-k}`. *(Audited sharp: Pinsker `√2` is optimal; boundary `2m/N` is loose, true optimum in `[0.21,2]`.)*

### 1.3 (C) ⟺ (D) — the source-conjugate tent-energy gate. *(proved; CTC-05/05b, MS-03)*
`{U_t}` is the authentic rational prefix orbit `U_0=0, U_{t+1}=16U_t+r(t+1)`, with the exact identity `U_t+T_t=16^{t-1}π`, `0<T_t<(8n+1)^{-2}`, `Σ_t T_t = B < 1/32`. Two proved transfers:
- **Green-tail transport (CTC-05):** `|\mathcal K_{\ell,N}(\{U_t+T_t\}) - \mathcal K_{\ell,N}(\{U_t\})| ≤ 2B·16^{2m}/N`, so the tent energy of the *completed* π-orbit and the *rational* orbit differ by `o(1)` at `m_N=\lfloor\log_{16}N/3\rfloor`.
- **Hard/soft domination (CTC-05b):** `Q_{m,N}(y) ≤ (256/15)\mathcal K_{16^{-(m-1)},N}(y)` for every finite orbit.

Together: a source-derived bound on the tent energy `\mathcal K` of the rational orbit `{U_t}` at the moving depth would force `\log Q=o(m)`, hence normality.

### 1.4 The tent energy is a Fourier sum. *(proved; CTC-05)*
$$
\mathcal K_{\ell,N}(\{U_t\}) = \sum_{h\in\mathbb Z}|\hat\mu_N(h)|^2 \operatorname{sinc}^2(\pi h\ell),
\qquad \hat\mu_N(h)=\tfrac1N\sum_{t≤N}e(hU_t),
$$
nonnegative with a constant `h=0` mode. So (D) is *exactly* a statement about the signed Weyl sums `Σ_t e(hU_t)` at frequencies `|h|≤16^{m-1}` — which is (B) in the rational coordinate (see 1.5).

### 1.5 Rational vs completed Weyl sums. *(proved; PI_FRONTIER_CONTRACT preliminary reduction)*
`|S_N(h) - Σ_{t≤N} e^{2πi h U_t}| < (119/648)|h|`, a paper-proved `ℓ¹` tail bound (`Σ T_t ≤ 17/648`). So base-16 normality of π is equivalent to cancellation of the *original rational* `U_t` phases: `Σ_{t≤N} e^{2πi h U_t} = o(N)`.

---

## 2. What has been ruled out (the firewalls that keep the spine *exact*)

Every one of these is a *proved* negative result, recorded so a future front does not waste a round re-attacking a closed door:

| Firewall | Status | What it rules out |
|---|---|---|
| Coherent counterseed `s=-π/16` (`U_t=-T_t`, phases→1) | PROVED | any source-only / positivity / prime-marginal bound |
| `{U_t}` is seed-independent (zero boundary = `β=π`, one bit) | PROVED | zero-boundary as an arithmetic engine |
| Prime windows are a *universal* criterion (PWI-02/03) | PROVED | prime-window reformulation as an easier proof |
| Stoneham mechanism (polynomial period) does not transfer | PROVED | the nearest known positive mechanism (conductor `exp(6n)` vs poly) |
| Galois trace annihilates (SPP-03) | PROVED | conductor growth / trace averaging as a bound |
| `D̂(ℓ)` DFT per-mode decay is Parseval bookkeeping (`~L^{-0.38}`, energy flat at 2.0) | OBSERVED | a "super-Parseval" oscillatory-mode bound |
| Midy complementarity acts only on the `O(1)` carry | PROVED | carry symmetry as a signed-cancellation lever |

---

## 3. The single remaining lemma (the summit)

> **(RL) Signed Weyl cancellation on the authentic orbit.**
> For the rational four-pole orbit `U_0=0, U_{n+1}=16U_n+r(n+1)`, prove that for every fixed `h≠0` there is `\theta_h<1` with
> $$ |S_N^U(h)| = \Big|\sum_{n≤N} e^{2\pi i h U_n}\Big| = O(N^{\theta_h}), $$
> equivalently `\sup_{1≤|h|≤16^{m-1}} |S_N^U(h)|=O(N^\theta)` for some `\theta<1`, `m=\lfloor\log_{16}N/3\rfloor`.

**If (RL) is proved, base-16 normality of π follows** by the spine (1.1)–(1.5). If (RL) is refuted, π is base-16 non-normal. There is no third outcome; the spine is exhaustive.

---

## 4. Dependency map (what a proof of (RL) consumes)

(RL) may use, and only these are known-proved and available:
- The exact four-pole source `r`, `U_n`, `T_n`, `B<1/32` (arithmetic_core.py, Lean-certified below).
- The conductor growth `log den(U_n)=6n+o(n)` (CG-01), the `exp(6n)` exact-grid bound (CG-02).
- The prime-birth residue clock `a_{p,j}=c_p 16^{j-b_p}` and carry recurrence `κ_{p,j}` (PCN-01), Midy (PCN-02), bilinear Gauss bound `|G_p|≤√p` (PCN-03), higher-octave stroboscope (PCN-04).
- The odd-order half-degree cyclotomic law `p|Φ_{2L}(4)` (PCN-16) and the `O(X^{2γ})` exceptional set (PCN-17), the `√p/L` Gauss scale.
- The irrationality measure `μ(π)<15/2` (Zeilberger–Zudilin, external classical input).

**None of these has yet been converted into (RL).** The spine tells a future front exactly this: the target is a *signed* estimate on `Σ e(hU_n)` using the above *proved* arithmetic, and nothing else is needed.

---

## 5. Status

The spine is **complete and exact**: (A)⟺(B)⟺(C)⟺(D) with all links proved and pinned, the unique open lemma (RL) named with full quantifiers, and the firewalls that keep the reduction exact recorded. π base-16 normality and RH remain **OPEN**.

*Finite combinatorial core of the spine (Q_{m,N} positivity, diagonal floor, de Bruijn firewall, KL/Pinsker finite bound) is Lean-checked in `ReductionSpine.lean`; the analytic links (Weyl, Green transfer, tail ℓ¹ bound) are paper-proved with sources pinned above.*
