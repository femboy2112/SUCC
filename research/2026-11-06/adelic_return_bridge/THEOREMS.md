# Operation RETURN SEAM — BBP 2-adic odometer, exact carry reconstruction, and real-phase non-continuity

**2026-11-06. New research on isolated PR branch; not a proof of π normality.** The literal original BBP forcing and `U_0=0` are unchanged. `PROVED LOCAL` means complete elementary arguments in this file, NOT an external priority assertion, Lean certificate, or source-selected real Weyl saving. Parent PR #527 supplies the authentic 2-adic source interpolation, isometry, and zero boundary; its formulas are reconstructed explicitly below.

## 0. Source and distinct observations

Use the real and 2-adic rational source

\[
r(z)=\frac{120z^2-89z+16}{(2z-1)(4z-1)(8z-7)(8z-3)}
=\frac4{8z-7}-\frac2{8z-4}-\frac1{8z-3}-\frac1{8z-2},
\quad U_0=0,\ U_{n+1}=16U_n+r(n+1).
\]

The denominators of the **combined rational function** are odd for every integer or 2-adic input. Do not infer this from each separate signed term (one displayed pole has an even denominator). From the source, `r(z)≡z (mod 2)` and its divided difference is an odd 2-adic unit, so `r` is a 2-adic isometry.

Define the 2-adic entire-clock source graph
\[
V(t)=\sum_{j\ge0}16^j r(t-j),\qquad t\in\mathbb Z_2.
\]
Parent #527 proves `V(0)=0` **exactly**, using an antiderivative with 2-adic torsion logarithms; we independently rechecked its two rational derivative identities with SymPy (not a new proof of the logarithm identity). `V` is an isometry, `V(t+1)=16V(t)+r(t+1)`, and consequently `U_n=V(n)` in `Z₂` for every positive integer time n. Each residue map `V mod 2^k` is a permutation. The integer-clock dynamical system in the V-coordinate is
\[
B(v)=V(V^{-1}(v)+1),\quad B(V(n))=V(n+1),
\]
which is **topologically conjugate to the 2-adic adding-one odometer**, not to the real expanding map.

In the real completion `T_n=sum_(j>=1)16^(-j)r(n+j)>0` and `T_n < 1/[15(n+1)^2]` for n>=1. The original BBP identity yields
\[
z_n=\{U_n+T_n\}=\{16^n\beta\},\quad \beta=\pi/16,\quad
x_n=\{U_n\}.
\]
Here `β` is irrational. The real circle discards integer carries; `Z₂` does not. There is no canonical embedding of a real irrational seed π into Q₂.

## 1. RS-01: exact *future source copy* on every 2-power clock — PROVED LOCAL

For k>=1 let Q=2^k, and `S_Q(t)=sum_(j=1)^Q 16^(Q-j)r(t+j)`. Iterating the source recurrence gives, for all t in Z₂,
\[
V(t+Q)=16^QV(t)+S_Q(t).
\]
Because `V` is a 2-adic isometry, `V(t+Q)≡V(t) mod 2^k`. As `v₂(16^Q)=4Q>=k`, the other homogeneous term vanishes modulo `2^k`. Hence
\[
\boxed{S_{2^k}(t)\equiv V(t)\pmod{2^k}\quad\forall t\in Z_2.}\tag{RS1}
\]
In particular `S_(2^k)(n)≡U_n mod2^k` for original literal zero-seeded rational BBP times n>=0. This is the actual four-pole *future forcing* reconstructing the present 2-adic source state at matching resolution. The real value S_Q(n) can be enormous; this is NOT a real modulo-one phase identity. Fixed finite independent `Fraction` controls cover k=1..10 and n=0,7,43,128.

## 2. RS-02: the integer-carry seam and exact finite cross-place reconstruction — PROVED LOCAL

Write the genuine original unwrapped rational state as
\[
U_n=C_n+x_n,\quad C_n=\lfloor U_n\rfloor\in\mathbb Z,\quad x_n=\{U_n\}\in[0,1).
\]
For positive n put `b_n=floor(16x_(n-1)+r(n))`; **these are integer carry increments, not necessarily individual hexadecimal digits**. Then
\[
\boxed{C_n=16C_{n-1}+b_n,
\quad C_n\equiv\sum_{j=0}^{\min(n,\lceil K/4\rceil)-1}16^j b_{n-j}\pmod{2^K}.}\tag{RS2}
\]
The second equality uses `C0=0`; if n=0 the sum is empty. Thus only the last `ceil(K/4)` carry increments affect C_n modulo `2^K`. The exact real circle observation x_n drops C_n, but the 2-adic graph retains it:
\[
\boxed{\{U_n\}\equiv V(n)-C_n\pmod{2^K}\ \text{in }\mathbb Z_2.}\tag{RS3}
\]
The LHS denotes the *rational fractional part*, embedded in Z₂ because its reduced denominator is odd. It is NOT a reduction of the real circle group modulo 2^K; such a group map is not defined.

Let `x_n=a_n/d_n` in lowest terms, `0<=a_n<d_n`, and `d_n` odd. Suppose the source provides d_n and we know the 2-adic state residue `v_n=V(n) mod2^K` **together with** `c_n=C_n mod2^K`. For `2^K >=d_n` define `[q]_(2^K)` as the least nonnegative integer residue. Then
\[
\boxed{a_n=[d_n(v_n-c_n)]_{2^K},\qquad
 e(hU_n)=\exp\bigl(2\pi i h\,[d_n(v_n-c_n)]_{2^K}/d_n\bigr).}\tag{RS4}
\]
Proof: multiplying `x_n≡v_n-c_n` by the odd denominator gives `a_n≡d_n(v_n-c_n)` modulo `2^K`. The already bounded integer `a_n` has a **unique** representative in `[0,d_n)` when `2^K>=d_n`. This is an exact cross-place character identity without a π-digit oracle. It is a reconstruction, NOT a new bound on its signed average.

**Sharp generic precision cost:** If `2^K<d`, then two different allowed numerators `0` and `2^K` give identical modular residue. Without carry C_n, knowing V(n) modulo 2^K and d_n need not constrain a_n at all: for every possible `a in [0,d_n)` choose an integer carry congruent to `v_n-a/d_n (mod 2^K)`. What source/observer rules out is supplied **only** by its actual carry chronology. Predeclared exact original denominators at n=73,149,293,587 have bit lengths 616,1272,2528,5062 respectively; this is a finite trend, NOT an asymptotic lower bound.

**A repaired failed probe:** The first implementation incorrectly used `x_n mod2^K` in place of `U_n mod2^K`, and therefore (correctly) failed equality at same-time-residue pairs. An additional initial test falsely expected wrong-carry reconstruction always to throw; a wrong carry can instead produce a different *plausible* fractional numerator. Both failures and corrections are preserved in logs/VALIDATION. They are direct manifestations of the missing-seam information.

## 3. RS-03: optimal expanding-circle separation constant — PROVED LOCAL

Define circular distance `||t||_T = min_(m in Z)|t-m|`. The expanding map `E_b(x)=b x mod1` with integer b>=2 has this elementary positive-expansivity property:
\[
\boxed{\theta\ne0\pmod1\implies\exists m\ge0:\ \|b^m\theta\|_T\ge1/(b+1).}\tag{RS5}
\]
**Proof.** Assume all distances are strictly below `δ=1/(b+1)`. Pick the unique signed representatives `t_m` in `(-δ,δ)`. Because `t_(m+1)-b t_m` is an integer whose absolute value is less than `(b+1)δ=1`, it must be zero. Thus `t_m=b^m t_0`; boundedness forces t0=0, contradiction. Equality in the constant is sharp: for θ=1/(b+1), `b θ≡-θ (mod1)` and every orbit distance is exactly `1/(b+1)`.

**Apply to the original π source.** Let `Q=2^k` with any k>=1 and let `β=π/16`. The initial phase displacement
\[
\theta_Q=(16^Q-1)\beta\not\in\mathbb Z
\]
is nonzero, since β is irrational. For any lower cutoff N, `16^N θ_Q` remains irrational; applying (RS5) gives some m>=0 with `n=N+m` and
\[
\boxed{\|z_{n+Q}-z_n\|_T
=\|16^n\theta_Q\|_T\ge1/17.}\tag{RS6}
\]
This holds at **arbitrarily late** times for **every** 2-adic clock resolution k, although `V(n+Q)≡V(n) mod2^k` exactly. For original *rational* phases x, the triangle inequality and positive real T_n show at the same times
\[
\boxed{\|x_{n+Q}-x_n\|_T
\ge1/17-T_n-T_{n+Q}\ge1/17-2/[15(n+1)^2].}\tag{RS7}
\]
This is a genuine all-horizon real-oscillation theorem for the original selected source, but gives only existence of widely separated phases—not their density, an average signed saving or Haar.

**Sharp decoder floor:** For every k, every arbitrary function `g_k:Z/(2^k)->T`, and every n at which (RS6) holds, `g_k(V(n))=g_k(V(n+Q))`. Triangle inequality gives a decoded error at one of these two indices >=1/34. Because such n occur arbitrarily late,
\[
\boxed{\limsup_{n\to\infty}\|z_n-g_k(V(n)\bmod2^k)\|_T\ge1/34.}\tag{RS8}
\]
The same limit superior for x_n is >=1/34, because T_n->0. No finite-precision, state-only, time-independent 2-adic decoder can approximate the original real phase with a uniformly vanishing pointwise error. This remains true even if g_k uses the original exact source at design time; extra time/carry/history observations can circumvent it, and are not excluded.

## 4. RS-04: classify continuous factors and prohibit measurable Haar factors — PROVED LOCAL / CLASSICAL PRINCIPLES

**Continuous classification.** Suppose `f:Z₂->T` is continuous and obeys `f(t+1)=16f(t)` for every t. By uniform continuity choose k so that for `t≡t' mod2^k`, `||f(t)-f(t')||<1/17`. Addition preserves congruence, so all forward images remain this close. RS5 forces `f(t)=f(t')`; thus f is constant on each cylinder modulo 2^k. Consequently it has a finite periodic image and
\[
\boxed{(16^{2^k}-1)f(0)=0\pmod1.}\tag{RS9}
\]
Conversely any β whose ×16 orbit has period dividing 2^k defines such a continuous factor by `f(t)={16^(t mod2^k) β}`. Because π/16 is irrational, the original real orbit cannot extend to a continuous equivariant factor of the 2-adic odometer. Since V is an isometry, the same impossibility holds for a continuous state-only decoder `g:Z₂->T` sending `V(n)` to z_n and commuting with the conjugated source-clock dynamics.

**Measurable Haar factor obstruction.** Let λ₂ be Haar on Z₂. Suppose measurable f satisfies `f(t+1)=16f(t)` for λ₂-a.e. t. Then `f_*λ₂` CANNOT be Haar on T. Here is an elementary entropy proof, no physical or quantum assumption. Put `d(t)=floor(16 f(t))`. For every ε>0, approximate the measurable digit function in λ₂-disagreement by some `d_K(t)` depending only on `t mod2^K`, with error <ε (finite cylinders generate the Borel σ-algebra). Under the translation odometer, a length-L word of d_K has at most 2^K possible values, hence entropy <=K log2. By the entropy chain rule and per-symbol disagreement continuity, the true length-L word entropy satisfies
\[
H(d(t),\dots,d(t+L-1))\le K\log2+L\bigl[h_2(\varepsilon)+\varepsilon\log15\bigr].
\]
Let L→∞, then ε→0: the observed digit entropy rate is ZERO. Were `f_*λ₂` circle Haar, equivariance would make these first hexadecimal digits IID uniform and yield entropy rate `log16>0`, contradiction. This is the classical entropy-nonincreasing-under-factors mechanism, proved here explicitly for a profinite odometer.

**Scope:** This prohibits an **a.e. equivariant, Haar-to-Haar measurable map** from the odometer to the real ×16 system. It does NOT rule out a selected arithmetic trajectory being real Haar-generic: the countable nonnegative integers form a λ₂-null subset, and an arbitrary measurable map's values on those integers do not determine its measure pushforward. This distinction is essential.

## 5. RS-05: p-adic return-fiber energy as the next nontrivial source-specific probe — PROVED LOCAL identity / OPEN saving

For `Q=2^k`, `M>=1`, `N=QM`, define for fixed nonzero integer h
\[
A_j(h)=M^{-1}\sum_{\ell=0}^{M-1}e(hU_{j+\ell Q}),\qquad
R_{Q,M}(h)=Q^{-1}\sum_{j=0}^{Q-1}|A_j(h)|^2\ge0.
\]
Because n+jQ are exactly the 2-adic return fibers and `V mod 2^k` permutes residues, these groups are also the *same source-state-residue fibers*. By Cauchy–Schwarz,
\[
\boxed{|W_N(h)|^2=|Q^{-1}\sum_j A_j(h)|^2\le R_{Q,M}(h).}\tag{RS10}
\]
Expansion yields an exact source-labelled signed correlation
\[
\boxed{R_{Q,M}(h)=\frac1{QM^2}\sum_{j=0}^{Q-1}\sum_{\ell,t=0}^{M-1}
e\bigl(h[U_{j+\ell Q}-U_{j+tQ}]\bigr).}\tag{RS11}
\]
The diagonal contributes `1/M`, but this is NOT a lower bound: off-diagonal correlations can be negative. A theorem giving `R_{Q(A),M(A)}(h)->0` for every fixed h and a coherent exhaustive choice `N=Q(A)M(A)->∞` would imply real-circle Haar along those N. To prove *all-prefix* normality, the chosen sequence of N must have ratios N_(j+1)/N_j→1, or comparable explicitly controlled intervals; sparse powers of 2 alone cannot certify all times. **This conditional energy criterion is stricter than the plain Weyl sum and remains UNVERIFIED for the actual π orbit.**

The characteristic phase for a return displacement is
\[
e(h[U_{n+Q}-U_n])=e\bigl(h[(16^Q-1)U_n+S_Q(n)]\bigr).
\]
The right side involves the **same exact future-source clone** of RS1, but its 2-adic divisibility is not a real signed cancellation estimate. This isolates the precise time-offset source correlation that needs new arithmetic control.

**Return-energy completion transport and equivalence firewall — PROVED LOCAL.** Replace every raw rational `U_n` in `R_(Q,M)` by the completed phase `z_n={U_n+T_n}` and call the resulting energy `R^z`. Because `|e(hU_n)-e(hz_n)|<=2π|h|T_n`, `|A_j|<=1`, and `||a|²-|b|²|<=2|a-b|` for `|a|,|b|<=1`,
\[
\boxed{|R_{Q,M}(h)-R^z_{Q,M}(h)|
\le\frac{4\pi|h|}{QM}\sum_{n=0}^{QM-1}T_n
\le\frac{4\pi|h|}{QM}\left(\frac\pi{16}+\frac1{15}\right).}\tag{RS11a}
\]
The last inequality uses `T0=π/16` and `T_n<1/[15(n+1)²]` for n>=1. So even the p-adic return-fiber energy asymptotically becomes a functional of the *same completed ×16 orbit*. Every completed off-diagonal return phase is
`e(h(z_(a+(t+d)Q)-z_(a+tQ)))=e(h(16^(dQ)-1)16^(a+tQ)β)`.
This is another family of large-frequency, selected-source Weyl sums, NOT an automatic cancellation by modular return. RS1 identifies the source clone, but its congruence alone does not bound these real characters.

**Failed naive positive candidate.** For one complete 2^k source-clock period, `v_n=V(n) mod2^k` runs over every residue; the reference characters `e(v_n/2^k)` have mean exactly zero for k>=1. Therefore
\[
|W_{2^k}(1)|\le \left(2^{-k}\sum_{n<2^k}|e(U_n)-e(v_n/2^k)|^2\right)^{1/2}.
\]
This is exact by Cauchy and zero reference mean, but **no small L2 mismatch was proved**. In fresh predeclared FLOAT diagnostics K=9,10 the RMS mismatches are about 1.4415 and 1.3907, respectively—too large to beat the trivial bound 1. These floats are *not rigorous certificates*. This is a documented failed route, not a fitted indicator of normality.

### RS-05b: exact two-resolution source/carry disintegration — PROVED LOCAL / OPEN saving

The 2-adic Haar **census depth** k and exact real-phase **readout depth** K are distinct. Fix N=2^k M and write Q=2^k. Choose `K>=max_(0<=n<N) ceil(log₂(d_n))`, so every original rational fractional state has the unique reconstruction in RS4. For each low-resolution residue `a mod Q`, define
\[
\mathscr E_a(h)=\frac1M\sum_{\substack{0\le n<N\\V(n)\equiv a\pmod Q}}
\exp\left(2\pi ih\frac{[d_n(v_{n,K}-c_{n,K})]_{2^K}}{d_n}\right),
\]
where `v_(n,K)=V(n) mod2^K` and `c_(n,K)=C_n mod2^K`. 2-adic isometry guarantees exactly M terms per a. The exact **source-authenticated, carry-aware joint-character identity** is
\[
\boxed{W_N(h)=\frac1Q\sum_{a\bmod Q}\mathscr E_a(h),\qquad
|W_N(h)|^2\le\frac1Q\sum_{a\bmod Q}|\mathscr E_a(h)|^2.}\tag{RS12}
\]
The RHS is exactly return-fiber energy RS10, but now the real phase is reconstructed solely from **higher-depth** 2-adic state, original integer carries, and original odd denominators. Low-depth p-adic Haar yields the equal weights; it supplies NO bound on the conditional phases. This is the precise mathematical location of the missing source–real cancellation.

There is an elementary resolution obstruction: a complete Haar census modulo 2^K of N time points requires `N>=2^K`, whereas exact numerator reconstruction requires `2^K>=max_n d_n`. In every window for which `max_n d_n>N`, those two requirements are **incompatible** at the same K. Our selected original denominator measurements give an enormous **finite** separation; a universal asymptotic lower bound on original d_n is NOT claimed. The correct possible route is inherently **two-scale**: small k for even p-adic census, large K for exact source/carry phase readout, and a new signed inequality for their conditional coupling.

## 6. Hostile controls and provenance

- `H(n)=n/(2n-1)^4` is a rational 2-adic isometry with H(0)=0, but real `H(n)->0`; a changed rational source `H(n)-16H(n-1)` makes this a legal zero-seeded BBP-form recurrence with exact 2-adic Haar and real non-Haar. **Different source**, no claim to refute original pi.
- The *same original recurrence* with irrational real seed adjusted so completed β=1/5 has a periodic real phase. This is a logical counterexample to generic forcing-only normality, NOT a 2-adic rational seed and NOT the literal zero history.
- β=1/17 gives a period-two ×16 real orbit and a genuine 2-adic-continuous decoder `f(t)` depending on parity; it calibrates the sharp expansivity radius `1/17`. It is non-Haar.
- An irrational sparse-digit β=`sum_(j>=2)16^(-j!)` is NOT normal: positions near a nonzero digit have zero density and the ×16 orbit tends to δ0 in Cesàro measure. Yet RS5/RS6-type real return separations still occur at arbitrarily late times. **Irrationality + sparse phase separation is not signed mixing.** This is not claimed as the original pi value.
- Fully original positive source and literal U0=0 are used for RS1, RS2, RS3, RS4 and RS6–RS8; exact pole-level authentication is retained in proofs. No source mutation is used to promote an original-source result.

**Literature constraints.** Original BBP: Bailey, Borwein, Plouffe (1997), DOI 10.1090/S0025-5718-97-00856-9. General adelic-solenoid separation and entropy: Lind & Ward, *Automorphisms of solenoids and p-adic entropy* (1988), DOI 10.1017/S0143385700004545. Related S-adic equidistribution: Roman Urban, *Equidistribution in the dual group of the S-adic integers* (2014), DOI 10.1007/s10587-014-0143-4. RS1–RS11 elementary derivations are presented directly here; no claim of world novelty. SUCC parent [PR #527](https://github.com/femboy2112/SUCC/pull/527) provides the exact V(0) torsion-log proof and the source isometry. Parent [PR #526](https://github.com/femboy2112/SUCC/pull/526) supplies the observer entropy budget. The missing all-horizon source-selected *real signed* inequality remains OPEN.
