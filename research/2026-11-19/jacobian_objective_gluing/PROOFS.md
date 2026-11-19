# Jacobian observability, prime-resolution repair and objective agreement

**Mathematical status:** local algebra/finite analysis proved as stated; asymptotic π-normality claims **OPEN**. Our observer is a mathematical protocol on labelled BBP data, not an experimental physical instrument. The full source and integer chronology are not altered.

## JOG-01. Five-dimensional source-plus-seed Jacobian (EXACT)

Use `β=(7,4,3,2)`, `c=(4,-2,-1,-1)`, and an independently parametrized seed `s` only for **sensitivity/hostile tests**:

\[
r_c(n)=\sum_{j=1}^4\frac{c_j}{8n-\beta_j},\quad
U_n(s,c)=16^n s+\sum_{k=1}^n16^{n-k}r_c(k),
\quad P_M(c)=\sum_{k=1}^M 16^{-k}r_c(k).
\]

For four distinct source times `t1<...<t4`, the observer records four **unwrapped** innovations `I_t=U_t-16U_{t-1}=r_c(t)` and a fifth, anchored observation `s+P_M(c)`. Its exact Jacobian is

\[
J_{M,\mathbf t}=
\begin{pmatrix}
 C_{11}&\cdots&C_{14}&0\\
 \vdots&&\vdots&\vdots\\
 C_{41}&\cdots&C_{44}&0\\
 L_{M,1}&\cdots&L_{M,4}&1
\end{pmatrix},\quad
C_{ij}=\frac1{8t_i-\beta_j},\quad
L_{M,j}=\sum_{n=1}^M\frac{16^{-n}}{8n-\beta_j}.
\]

Therefore `det J = det C`, and the Cauchy product formula yields

\[
\boxed{\det C=\frac{8^6\cdot120\prod_{a<b}(t_b-t_a)}{\prod_{a=1}^4\prod_{j=1}^4(8t_a-\beta_j)}\ne0.}
\]

The finite anchor `s+P_M` approximates the genuine analytic boundary with a **known, authenticated** interval `0 < x-P_M=16^{-M}T_M < 16^{-M}r(M+1)/15`; it is **not** a direct observation of the inaccessible completed real `x`. The literal physical source contract fixes `s=0`; the variable `s` exists to detect counterseed ambiguity. Real parameter rank certifies local identifiability only within the explicitly declared five-dimensional model. A wrapped circle reading without its integer winding is not a substitute for the unwrapped innovations.

**Rank collapse of completed-only observations:** `Y_n(s,c)=16^n(s+x(c))` has sensitivity row `16^n(1,L_1,...,L_4)`. Every finite stack of these completed-only rows has rank one. Source observations plus an anchored fifth channel repair the local identifiability loss; they cannot by themselves prove a Fourier limit.

## JOG-02. An adaptive 3/5/7/11/29-adic rank repair (EXACT)

Assume amplitude perturbations `c_j` are p-adic integers. For each source row `C(t)`, define the **minimal denominator-clearing scale**

\[
a_p(t)=\max(0,-\min_j v_p(C_j(t))),\quad
\widetilde C_p(t)=p^{a_p(t)}C(t)\bmod p\in\mathbb F_p^4.
\]

This definition pays for the pole precision; no rational denominator divisible by p is inverted modulo p. A clock is "clean" (scale zero) iff `8t` misses all residues `β_j mod p`. The number of clean clock classes modulo odd prime p equals `p-|{7,4,3,2} mod p|`. Therefore:

| p | clean residues | consequence |
|--:|--:|---|
| 3 | 0 | every source row meets at least one p-pole |
| 5 | 2 | four **clean** rows can never span four source amplitudes |
| 7 | 3 | four **clean** rows can never span four source amplitudes |
| ≥11 | p−4 | clean four-row rank may be achievable with a lawful schedule |

These are source-specific finite-field obstruction counts, not statements about π-digit statistics.

Start with the Fibonacci clocks `(55,89,144,233)`. Their normalized row ranks for p=(3,5,7,11,29) are `(3,4,4,3,4)`; arithmetic at 3 and 11 loses one first-digit direction. The **forward-only** history `(55,89,144,146,147,233)` repairs them to `(4,4,4,4,4)`. The minimum row scaling exponents reach `(3,2,2,1,0)` respectively. At clock 146, `8*146-7=1161=3^3*43`: this isolates one of the two pole channels whose offsets collide modulo 3. Clock 147 repairs the 11-adic row coincidence. The old 144 observation is retained, not erased or treated as if it never occurred. The p=7 recovery uses pole-aware normalization rather than an impossible four-clean-clock schedule.

The scheduling policy examines only known source-pole algebra and current retained times; it never chooses or rejects a probe based on its observed complex phase or prospective success at Weyl. This is **knowledge-adaptive**, not response-cherry-picked. The rank and exponents are exact finite arithmetic, verified by independent direct rank reductions. They are not global arithmetic source–real-phase estimates.

## JOG-03. Objective gluing despite locally locked observers (EXACT)

Fix any finite complex unit phase stream `z_n(h)` on a shell of length B. Partition the clock indices into nonempty sets `A_a`; let `p_a=|A_a|/B`, `m_a=|A_a|^{-1}Σ_{n∈A_a}z_n`. All reported phasors must be transported into a **common basis** before averaging. Then

\[
W=\sum_a p_a m_a,\quad
\boxed{1-|W|^2=\sum_a p_a(1-|m_a|^2)+\sum_{a<b}p_ap_b|m_a-m_b|^2.}
\]

This is the law of total variance for a unit complex variable, proved by expanding the squares. No probabilistic independence or iid digits assumed. The first term is within-observer dispersion `I_B`, the second between-observer dispersion `D_B`. Each term is nonnegative.

If `A_a` are cells in *rational* phase `θ_n^U={U_n}` of maximum arc width `δ_B`, then for any fixed h with `|h|δ_B≤1/2`, the local mean magnitude obeys `|m_a^U(h)|≥cos(π|h|δ_B)`. Therefore

\[
0\le I_B^U(h)\le\sin^2(\pi|h|\delta_B).
\]

For any partition mesh `δ_B→0` (equal bins of Fibonacci-count `F_k≈√B` or the golden irrational-rotation mesh of SUCC #549), all local observation families become **perfectly coherent** for each fixed h. Nevertheless,

\[
\boxed{x\text{ base-16 normal}\iff D_B^x(h)\to1\text{ for every fixed }h\ne0,}
\]

where the partitions are defined by the actual orbit phases and have mesh `δ_B→0`. This follows from `|W_B|²=1-I_B-D_B`, `I_B→0`, and Weyl. It is a **normality-equivalent re-encoding**, not a source-derived proof of the limit.

**Objective/finite slice bridge.** Define finite labels using `U_n` and apply the *same labels* to both rational phases `e(hU_n)` and completed phases `e(h(U_n+T_n))`. The original positive BBP tail gives the uniform per-observation bound

\[
\epsilon_B(h)=2\pi|h|\max_{B\le n<2B}T_n <(2\pi|h|/15)r(B+1)=O_h(B^{-2}).
\]

The corresponding centroid differences are at most `ε_B`; the within-family energy differs by at most `2ε_B`, and the between-family energy by at most `4ε_B`. Thus the rational objective-gluing energy faithfully approximates the completed objective-gluing energy at fixed h, independently of how many observation families the finite partition has. The labelled partitions do not require the completed phase to stay in the same bin after the small tail correction.

**Hostile example:** choose M equally spaced unit-circle phases and put one phase in each knowledge cell. Every local observer is *exactly locked* (`I_B=0`), whereas the global mode h not divisible by M cancels (`W=0`, `D_B=1`). Fixed M is not a proof of full normality; this simply refutes the false assertion "every local observer must unlock". A single completed orbit `x=1/15` gives the opposite extreme `W=1` and `D_B=0`.

## JOG-04. Preregistered rational holonomy and signed Weyl bank (EXACT CONDITIONAL)

From `U_{n+ell}-U_n-R_{n,ell}=(16^ell-1)U_n`, define for a **fixed declared** integer pair `(ell,h)`

\[
H_{B;\ell,h}=B^{-1}\sum_{n=B}^{2B-1}\|h(16^\ell-1)U_n\|_{\mathbb T}^2.
\]

As already established in [PR #668](https://github.com/femboy2112/SUCC/pull/668),

\[
1-\Re W_B^\pi(1)\ge\frac{8H_{B;\ell,h}}{h^2(16^\ell-1)^2}
-\frac{2\pi}{15}r(B+1).
\]

Any **proved all-large-B positive liminf** for one such fixed pair implies R0; it is not known. The test fixes `(ell,h)=(1,1),(4,11),(6,7)` before reporting any finite results. The high-frequency two pairs target 7/11 memory compatibility but have a tiny `1/[h(16^ell−1)]²` conversion coefficient; `(1,1)` is the stronger R0 diagnostic.

For signed Weyl, preregister the eight shifts `S=(0,1,5,6,21,22,55,56)` and finite diagnostic modes `h=(1,2,15)`. Define

\[
\mathcal Q^U_{B,h}(S)=B^{-1}\sum_{n=B}^{2B-1}\left|\frac1{|S|}\sum_{t\in S}e(hU_{n+t})\right|^2.
\]

The *signed* Gram identity is

\[
\boxed{\mathcal Q^U_{B,h}(S)=\frac1{|S|}+\frac2{|S|^2}\sum_{u<v\in S}\Re\left[B^{-1}\sum_{n=B}^{2B-1}e(h(U_{n+v}-U_{n+u}))\right].}
\]

Let `T=max S`. Boundary shifting and Cauchy–Schwarz, plus the authentic positive BBP tail, yield

\[
\boxed{|W_B^\pi(h)|\le\sqrt{\mathcal Q^U_{B,h}(S)}+\frac{2T}{B}+\frac{\pi|h|}{32B^2}.}
\]

A **growing**, predeclared `S_B`, with `|S_B|→∞`, `T_B=o(B)` and actual source-specific `Q^U_{B,h}(S_B)→0` for every fixed nonzero h, would prove normality. None of these limits has been established here. In particular, our fixed eight-shift bank cannot make the diagonal `1/8` vanish, and for B≤128 the boundary term renders the numeric upper bound trivial.

## JOG-05. Objective completion and the order of observers (EXACT)

For each finite prefix the observer knows the source-derived rational `P_M`. It has an authentic completion interval

\[
\boxed{P_M<x<P_M+16^{-M}r(M+1)/15.}
\]

The intervals shrink and their common limit is `x=π/16`; for any fixed chronological n, `16^n P_M→16^n x`. At every finite prefix M the rational `P_M` has an eventually periodic or preperiodic base-16 orbit. A finite observer that freezes a rational endpoint and then extends chronological time sees a different limiting problem from the observer refining the source prefix at each fixed n. This is an order-of-limits boundary, **not** a theorem that π is normal.

A classical control makes the distinction decisive: approximate any known base-16 normal point by its truncations at M hexadecimal digits (denominator `16^M`). Each rational truncation eventually maps to 0 under ×16, yet their fixed-n limit is the normal point. Thus local eventual locking of finite approximants does not imply locking of their completed limit. The actual BBP state `U_M` has an odd denominator; the prefix point `P_M=16^{-M}U_M` can additionally have a radix-power denominator and hence an initial preperiod. No claim is made that the resulting finite-period measures converge to Haar.

The original observer's rotation changes its **probe/memory state**. It does not change π or the deterministic BBP source. A genuine physical intervention would require a separately declared carrier interaction. Fifteen rotations by `j/15` commute with ×16 and cannot create source-specific curvature by themselves.

## JOG-06. Hostile division and verdict

- **Same forcing, wrong seed:** `s*=-π/16` gives `U_n(s*)=-T_n→0`, hence each fixed-frequency signed Gram energy tends to 1 although the source four-pole innovation Jacobian is unchanged. Seed anchoring is necessary; local source rank alone cannot prove any Weyl bound.
- **Phase-free spatial control:** uniform finite root grid has perfect local phase coherence and vanishing global low-frequency mode; static observations alone lack chronological source identification.
- **Sparse cold shells:** an irrational with rapidly growing constant-digit blocks can violate R0 while satisfying many local source-agnostic finite checks.
- **Prime-rank mutants:** unscaled modulo-p inversion at p=3/5/7 is mathematically invalid on rows containing source poles. Every result retains the exact denominator-clearing exponent.
- **p=29 resonance:** the Fibonacci–radix homogeneous eigenrow also exists mod 29, so 11-only spectral coincidence is not unique to the original source (PR #668).

**Proved:** exact Cauchy/five-channel Jacobian; nonclean-prime obstruction and repaired 3/5/7/11/29 schedule; source-faithful objective variance with O(B^-2) completion transfer; signed Gram identity and conditional Weyl inequality; explicit hostile controls.

**UNVERIFIED / OPEN:** a positive all-shell bound on authentic source-corrected R0 holonomy, or decay of objective signed Weyl Gram energy for every fixed nonzero frequency. The same-source locked seed proves why geometry and rank alone cannot settle it.
