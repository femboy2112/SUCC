# Original π-BBP ×2-adic/3-adic Joint Clock: Solenoid, Exact Haar, and Archimedean No-Go

**2026-10-31. Research only.** Exact base: Main XVII e8598cfa5d32fd1de8e94a3e458a366a0850d59e. Original four signed BBP poles and U_0=0 are unchanged. **π base-16 normality, RH and Furstenberg's zero-entropy ×2×3 measure conjecture remain OPEN.** The finite-to-global local results below are unconditional assuming the earlier fully displayed SUCC DSI-1..4 source-isometry theorem; they use classical CRT, LTE, Pontryagin duality, positive expansivity, and the published Rudolph–Johnson measure theorem with explicit domains. The repository synthesis is not claimed as independent academic novelty.

## 0. Why "RH -> prime spectrum uniform -> π normal" needs a new arrow

For the circle Laplacian the Fourier eigenvalues are n² for n∈Z; indexing a sparse subset by primes does not automatically make any selected orbit equidistributed. RH constrains the zeros of ζ and sharpens prime-counting errors, not the empirical means of e(h16^nπ). There is a stronger classical fact requiring **no RH**: Vinogradov proved {pα} is uniformly distributed mod 1 for **every irrational α**, p over increasing primes. Thus even α=Σ_(j≥1)16^(−2^j), irrational with zero-density nonzero hexadecimal digits and demonstrably nonnormal, has uniformly distributed prime multiples. Its irrationality follows because an eventually periodic digit string cannot have infinitely many isolated 1s with unbounded gaps. This refutes the blanket implication from uniform prime sampling to base-16 normality. A source-correct bridge must control the *lacunary* selected powers 16^n and their joint additive phase, not prime labels alone.

Reference: Champagne–Lê–Liu–Wooley, *Well-distribution modulo one and the primes* (2024), Introduction (Vinogradov's theorem), https://www.math.purdue.edu/~twooley/publ/20240627welldist.pdf. RH status: https://www.claymath.org/millennium/Riemann-Hypothesis/.

## 1. Separate THREE mathematical carriers

1. **Finite CRT quotient** C_(a,b)=Z/(2^a3^b)Z. Its character group is the finite cyclic group Z/(2^a3^b)Z. This is a totally disconnected finite observation system.
2. **Joint profinite time carrier** K=Z₂×Z₃, with diagonal integer successor S(t₂,t₃)=(t₂+1,t₃+1). Integers are dense by CRT. Its continuous character group consists of the torsion rational labels (Z[1/2]/Z)⊕(Z[1/3]/Z), isomorphic to Z[1/6]/Z. This is NOT the circle.
3. **Connected real/adically completed solenoid**
   X_(2,3)=(R×Q₂×Q₃)/ΔZ[1/6], a compact connected group with character group Z[1/6]. Equivalently the inverse limit over a,b≥0 of genuine circles R/(2^a3^b)Z, with natural quotient maps when divisibility increases. The character group of each **circle** R/NZ is the infinite lattice (1/N)Z, **not** Z/NZ. Taking the directed union of these lattices gives Z[1/6], as required. The finite group Z/NZ embeds as the integer-torsion SUBGROUP of the stage circle; its finite dual is not the entire circle dual. See SOLENOID_ERRATUM.md for a counterexample to the existing archive's inaccurate proof.

The scalar maps ×16 and ×3 are commuting AUTOMORPHISMS of X_(2,3), since 16 and 3 are units in Z[1/6]. They act on all three coordinates; 16 is a unit (but not the identity) on Q₃, and 3 is a unit (but not identity) on Q₂. E.g. 16≡7 mod9, 3≡3 mod8. Their prime valuations are complementary, making a rank-two action, not proving measure rigidity.

## 2. Exact original BBP source at 2

Keep
\[
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2}
=\frac{120n^2-89n+16}{(2n-1)(4n-1)(8n-7)(8n-3)},
\quad U_0=0,\quad U_n=16U_{n-1}+r(n).
\]
Every denominator on the right is odd. On Z₂, r(x) is a 2-adic isometry: its divided difference is a 2-adic unit. The already integrated source theorem DSI-1..4 in research/2026-10-24/PI_DYADIC_SOURCE_ISOMETRY.md proves that the uniformly convergent backward Green function
\[
F_2(t)=\sum_{j\ge0}16^j r(t-j)
\]
is a bijective isometry of Z₂, satisfies **F₂(0)=0** by a nontrivial original-source analytic identity, and F₂(n)=U_n for every n≥0. Consequently
\[
v_2(U_s-U_t)=v_2(s-t),\qquad U_{n+2^a}\equiv U_n\pmod{2^a}.
\]
The equality of initial conditions is essential: do not generalize the result to arbitrary changed BBP seeds.

## 3. Exact 3-adic clock and its LIMIT (classical)

Since 16=1+15 and 3 divides 15 but 9 does not, the odd-prime lifting-the-exponent lemma gives, for n≥1,
\[
\boxed{v_3(16^n-1)=1+v_3(n).}
\]
Hence ord_(3^b)(16)=3^(b−1), b≥1, and t↦16^t mod3^b is a bijection from the additive group Z/3^(b−1) onto the multiplicative subgroup 1+3Z/3^bZ. In the 3-adic limit, t↦exp(t log16) is a continuous group isomorphism from Z₃ onto 1+3Z₃, since v₃(log16)=1. The first nontrivial local 3-adic clock thus has a COMPLETE, source-independent arithmetic description.

**Strict type distinction:** this is the 3-adic clock 16^n, NOT U_n∈Z₃. The actual source already has U_1=47/15 and v₃(U_1)=−1; at n=2 the valuation is −2, and at n=7 it is −3. Trying to identify the clock with 3-adic BBP source values silently drops the prime-pole singularities.

## 4. TWTH-01/02 — authenticated all-horizon JOINT product Haar (PROVED LOCAL from inherited DSI and LTE)

Fix integers a,b≥1 and put q=2^a, L=3^(b−1), M=qL. For every starting integer A≥0 define
\[
\Gamma_{a,b}(n)=(U_n\bmod q,\;16^n\bmod3^b),\quad A\le n<A+M.
\]
**Theorem.** Gamma is a bijection from these M consecutive times onto
\[
Z/qZ\times (1+3Z/3^bZ).
\]
**Proof:** If Gamma(s)=Gamma(t), DSI-4 implies s≡t modq. LTE implies s≡t modL. Coprimality gives s≡t modM, hence s=t within the M-window. There are exactly M inputs and M possible outputs, so injectivity implies bijectivity. As Gamma depends only on n modM, the same statement holds for every translated window of length M. QED.

This supplies a **source-authenticated, deterministic, exact** joint distribution. For any N and A, each target pair occurs either floor(N/M) or ceil(N/M) times in A≤n<A+N. In particular any nontrivial product character has exact full-period cancellation and an all-horizon normalized bound
\[
\boxed{\left|\frac1N\sum_{n=A}^{A+N-1}
e\!\left(\frac{r\,U_n^{(q)}}q+\frac{s\,n}{L}\right)\right|
\le\frac{M-1}{N},\quad(r\bmod q,s\bmod L)\ne(0,0).}
\]
Here U_n^(q) is the canonical integer 2-adic residue. The expression is a **finite CRT character** with its exact original-source sign; it is not the Archimedean e(hU_n).

Letting a,b increase, the same ordinary consecutive-time orbit is Haar-equidistributed in
\[
K'=Z_2\times(1+3Z_3).
\]
Precisely, the homeomorphism H:K→K', H(t₂,t₃)=(F₂(t₂),exp(t₃log16)) pushes Haar_K to Haar_K'. Since the diagonal integers are uniformly distributed in K on every fixed finite quotient, their H-images are Haar_K'. Thus the *entire mixed local time clock is solved*, not just separately uniform marginals. This is a standard compact-group/odometer argument anchored to the nontrivial authentic F₂ source law.

## 5. TWTH-03 — why local Haar cannot be continuously "reassembled" as π's expanding real circle (PROVED LOCAL; classical dynamical mechanism)

Let K=Z₂×Z₃, let S(t)=t+(1,1), and let T(x)=16x mod1 on the real circle. Suppose a **continuous** map f:K→R/Z satisfies
\[
f(S(t))=T(f(t))\qquad\text{for EVERY }t\in K.
\]
**Theorem:** f has finite image and f(0) is rational, periodic for T with period whose prime factors lie in {2,3}. Conversely every T-periodic rational α with such a period admits a continuous equivariant map f with f(0)=α.

**Proof:** T is *positively expansive*. Take c=1/32<1/17. If d(T^n x,T^n y)<c for every n≥0, choose signed differences δ_n∈(−c,c). The integers k_n=16δ_n−δ_(n+1) have |k_n|<17c<1, so k_n=0. Thus δ_n=16^nδ_0 remains bounded for all n, implying x=y.

By uniform continuity of f on compact K, choose a,b large enough that f(t) and f(t+M) are c-close for every t, M=2^a3^b. For every n≥0, t+n and t+M+n remain congruent modulo 2^a in Z₂ and modulo3^b in Z₃; hence T^nf(t) and T^nf(t+M) remain c-close. Positive expansivity forces f(t)=f(t+M) for every t. The subgroup generated by the diagonal element M is dense in 2^aZ₂×3^bZ₃, so continuity implies f factors through the finite quotient K/(2^aZ₂×3^bZ₃), a cyclic group of order M. Its image is finite and T^M f(t)=f(t). Thus (16^M−1)f(t)=0 mod1, and every point is rational with period dividing M. Conversely if T^dα=α and d|2^a3^b, the continuous reduction t↦t mod d on K defines f(t)=T^(t mod d)α, proving the classification. QED.

Since α=π/16 is irrational, **there is NO continuous such equivariant decoder from the two-adic/three-adic odometer into π's selected real-circle orbit**. This is a toolkit-relative **boundary theorem**, not a statement that π normality is logically impossible. The *real coordinate of the full connected solenoid* is exactly the extra carrier data a correct representation must preserve. Neither a source-matched finite CRT marginal nor a purely profinite local model can create the selected expanding real dynamics by a continuous quotient alone.

Positive controls: α=1/17 has period 2, α=1/(16³−1) period 3. Negative periodic control: α=1/(16⁵−1) has least period 5 and cannot arise from this particular 2×3 odometer continuous factor, even though it is rational.

## 6. TWTH-04/05 — exact tripling real-carry and continuous triangle transport

For x∈R/Z choose y={x}∈[0,1), and q=16^m. Put
\[
d_q(x)=\lfloor qy\rfloor,\quad
c_{3,q}(x)=\lfloor3\{qy\}\rfloor\in\{0,1,2\}.
\]
Then
\[
\boxed{d_q(3x)\equiv3d_q(x)+c_{3,q}(x)\pmod q.}
\]
The carry reads the future real fractional tail, not simply the 3-adic clock n mod3^(b−1). Arbitrary finite selected carries can be independently certified from the original BBP rational U_n plus outward Green-tail brackets, rejecting ambiguous seam crossings. The exact probe does this without supplying π digits.

Reuse the classical cardinal triangle hats from draft PR #426:
\(\phi_{q,j}(x)=\max(0,1-q\|x-j/q\|)\), \(\Phi_q=(\phi_{q,j})_j\).
They satisfy **two simultaneous exact refinement laws**
\[
\phi_{q,j}(16x)=\sum_{t=0}^{15}\phi_{16q,j+tq}(x),
\quad
\boxed{\phi_{q,j}(3x)=\sum_{t=0}^2\phi_{3q,j+tq}(x)}.
\]
Both orders refine to the same 48q-grid sum, since ×16 and ×3 commute. This is a commuting square of *observation operators*, not independence or a source-selected statistical theorem.

Define the actual selected tripling defect on original rational source states
\[
\Delta^U_{q,N}=\frac1N\sum_{n=1}^N(\Phi_q(3U_n)-\Phi_q(U_n)).
\]
The completed real orbit is y_n={U_n+T_n}={16^(n−1)π}, and its similarly defined defect is Δ^y. The hats have \(\ell^1\)-Lipschitz constant 2q, so with B=Σ_n T_n<1/32,
\[
\boxed{\|\Delta^y_{q,N}-\Delta^U_{q,N}\|_1
\le \frac{8q}{N}\sum_{n=1}^NT_n <\frac{q}{4N}.}\tag{TWTH-04}
\]
This is a rigorously quantitative, original-source, ZERO-SEED transport of ×3 invariance through the full signed real-circle carrier. For every fixed q, Δ^y_q,N→0 iff Δ^U_q,N→0. The union of triangle sensor spans as q=16^m→∞ is dense in C(R/Z). Consequently every subsequential weak limit of π's empirical ×16 orbit is ×3-invariant **iff** Δ^U_{16^m,N}→0 for all fixed m. These limits are NOT presently proved.

## 7. TWO honest measure-rigidity contracts, and why one is insufficient

For every real α, any weak limit μ of \(N^{-1}\sum_{n<N}\delta_{\{16^nα\}}\) is ×16-invariant by elementary telescoping. The previous section supplies an exact source test for additional ×3 invariance.

**Contract A, unconditional *conditional theorem* from classical Rudolph–Johnson:** If every weak limit μ is jointly ×16/×3-invariant and every jointly ergodic component of μ has positive entropy for ×16, then every such component is Haar, hence μ is Haar; π is base-16 normal. One may replace the component condition by the *uniform all-scale collision exponent* proved sufficient in the earlier SUCC PI_BASE_THREE_RIGIDITY.md via Bourgain–Lindenstrauss–Michel–Venkatesh's nonergodic Rudolph–Johnson measure-domination theorem and an iterative remainder elimination. Neither selected source premise is established.

**Contract B, depending on the OPEN Furstenberg zero-entropy conjecture:** If every weak limit is ×3 invariant, atomless, and the universal Furstenberg ×16×3 conjecture holds, then π is normal. The conjecture remains open. Transcendence or finite irrationality exponent of π alone does not supply positive measure entropy, atomlessness of occupation limits, or source-specific tripling invariance (see Kempner countermodel, research/2026-10-27-furstenberg-kempner/).

**Positive entropy of the total nonergodic μ is NOT enough.** The exactly jointly invariant mixture μ=ηλ+(1−η)δ₀ (0<η<1) has entropy η log16, is non-Haar, and has a positive entropy component plus zero-entropy atomic component. The original Rudolph–Johnson theorem requires joint ergodicity, or a condition excluding every bad component; the nonergodic domination theorem gives μ≥ηλ, not μ=λ. This is a mandatory hostile control.

Reference: Rudolph (1990), https://doi.org/10.1017/S0143385700005629 ; Bourgain–Lindenstrauss–Michel–Venkatesh, Theorem 1.3, https://www.math.ias.edu/~akshay/research/blmv.pdf .

## 8. The actual OPEN mixed-phase interaction

The local source-selected joint CRT sum vanishes over every full period at nontrivial finite characters. The missing real phase is the factor \(e(hU_n)\). A source-complete signed joint object is
\[
W_{a,b,N}(h;r,s)=\frac1N\sum_{n=0}^{N-1}
 e(hU_n)\,e\!\left(\frac{r(U_n\bmod2^a)}{2^a}+\frac{s n}{3^{b-1}}\right).
\]
At h=0 and (r,s) nontrivial, the local result gives O(2^a3^(b−1)/N) and indeed exact full-period zero. At h≠0 NO comparable selected all-horizon saving is proved, even at (r,s)=(0,0), where this is precisely the original π Weyl problem. One cannot average the real factor independently of the CRT labels.

The smallest distinctly useful next theorem would bound the *authentic selected* tripling defect Δ^U_{q,N}(j)→0 for at least one nontrivial fixed q,j by a genuine four-pole signed estimate, surviving AT-07 and changed-seed controls, then extend over the complete sensor hierarchy; independently prove a source-derived positive collision dimension or an entropy condition for every jointly ergodic limit component. **An estimate of a single q,j is genuine partial progress but is not π normality.**

## 9. What was certified versus what remains dark

- **PROVED LOCAL / inherited DSI:** original F₂ source bijective isometry and zero-boundary agreement.
- **CLASSICAL + PROVED LOCAL:** full 3-adic primitive clock; exact joint product CRT windows; profinite joint Haar, classical dual repair; continuous equivariant decoder finite-image no-go; real ×3 finite carry and source-tail triangle transport.
- **OBSERVED FINITE:** Fraction tests for selected source, 3-adic pole strata, joint periods 16/48/144/768, full product character balances, exact source-completed tripling digit carries.
- **REFUTED inference:** circle Fourier dual is finite; rank-two local Haar ⇒ real π Haar; mere prime-multiple equidistribution ⇒ π normal; single positive entropy average ⇒ Haar; topological commutation alone ⇒ selected ×3 invariance.
- **OPEN:** original π-selected real ×3 invariance, uniform all-scale nonconcentration/component entropy, full zero-entropy Furstenberg conjecture, π normality, RH, RH-to-selected-phase transport.

No code was written to the source archive or main. No publication, formal Lean authority, or resolution of Furstenberg's conjecture is claimed.
