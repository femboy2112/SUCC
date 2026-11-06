# Operation Prime–Character Primal: quotient BBP from its own Frobenius echo

**November 4, 2026.** Exact paper theorem with source-faithful rational/finite-field oracles. **DRAFT, add-only.** Parent PR #497 SHA `4383bd31340af700e312f13d7ef28af090c152d5`, which inherits the zero-seeded four-pole BBP source, p-primary universal pulse theorem, and the second classical BBP formula. All development is on a strictly separate research branch; no edits to main, source, Lean, archived proofs or workflows. **Base-16 π normality and global academic priority remain UNVERIFIED.**

## Definitions and what “quotient” means

Preserve the exact *original source*

\[
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},\quad U_0=0,\quad U_n=16U_{n-1}+r(n).
\]

For a general rational **eight-tap** source `w=(w_1,...,w_8)`, define

\[
P_w(t)=\sum_{j=1}^8w_jt^{j-1},\quad r_w(n)=\sum_{j=1}^8\frac{w_j}{8(n-1)+j},\quad U^w_0=0,\quad U^w_n=16U^w_{n-1}+r_w(n).
\]

The original vector is `p=(4,0,0,-2,-1,-1,0,0)`. The already-identified second π source of #497 has tap vector `p#=(0,8,4,4,0,0,-1,0)`, generating `V_n=U^(p#)_n`. Here **primal quotient** is not literally division of a function by itself. It means a source-defined **finite-group character projection and quotient by a period-zero submodule**; its output has minimal **degree-two rational transfer**, not a newly discovered formula for π. Do not confuse the generating-function coefficient index with original recurrence time n.

## PCQ-01. Source-validated prime-Frobenius monomial representation, for EVERY tap vector

Let `G=(Z/8Z)^*={1,3,5,7}`. Let `chi2(a)=(2/p)=+1` when `a=1,7` and `-1` when `a=3,5`. For `1<=ell<=8`, let `j_a(ell)` be the **least positive** representative of `a*ell mod8` (so residue zero is represented by 8). Define

\[
\boxed{ (S_aw)_\ell
=\chi_2(a)^{8-\ell}\,2^{(j_a(\ell)-\ell)/2}\,w_{j_a(\ell)}. }\tag{PCQ-1}
\]

The exponent is integral because a is odd. Negative exponents are rational powers of 2. This operator is defined on **all of Q^8**, not merely on fitted π coefficients.

**Proof that it comes from actual original p events.** Let `p>8k` be an odd prime with `p≡a(mod8)`; assume each tap's rational denominator is prime to p. At original source time `n`, the denominator `8(n-1)+j` equals `mp` precisely when `j=j_a(m)` and

\[
n=\frac{mp+8-j_a(m)}8.
\]

Because `p>8k`, all source denominators through time `kp` are strictly smaller than `p²`, so a p-pole has valuation exactly -1. At the end of a block of eight multiplier indices, `m=8q+ell`, the arithmetic source clock is `(q+1)p`. Euler's criterion gives

\[
16^{(q+1)p-n} =2^{(8-\ell)p/2-(8-j_a(\ell))/2}
\equiv \chi_2(a)^{8-\ell}2^{(j_a(\ell)-\ell)/2}\pmod p.
\]

This is exactly the weight in (PCQ-1). Across successive full blocks, Fermat gives `16^p≡16(mod p)`; therefore for the actual zero-seeded original rational states,

\[
\boxed{pU^w_{kp}\equiv U^{S_aw}_k\pmod p, \qquad p>8k,\ p\equiv a\pmod8.}\tag{PCQ-2}
\]

The congruence interprets both rationals via their p-integral residues AFTER multiplying the left side by p. It does not mean equality over Q or R. All original pole signs remain intact. The source's **zero initial boundary is used**, not inferred from congruences.

**Proof of group law.** Writing `j_a=j_a(ell)` and `j_ab=j_b(j_a)`, the rational powers of 2 multiply with exponent

`(j_a-ell)/2 + (j_ab-j_a)/2=(j_ab-ell)/2`.

The chi sign multiplies as `chi2(a)^(8-ell)*chi2(b)^(8-j_a)`. Since a is odd, `j_a` and ell have the same parity, so `chi2(b)^(ell-j_a)=1`; therefore the chi product is `chi2(ab)^(8-ell)`. Thus

\[
\boxed{S_aS_b=S_{ab},\quad S_1=I,\quad S_a^2=I.}\tag{PCQ-3}
\]

The operators are weighted permutations, invertible over Q, and act as an exact rational representation of the Klein four group. This is **not** the average of the four p-local sources; they label four possible genuine congruence classes. The action uses the Legendre symbol of 2 as a *multiplicative prime-class character*, never as an impossible additive sign on Q/Z.

Traces on Q^8 are `tr(S_1,S_3,S_5,S_7)=(8,2,4,2)`. Thus character eigenspace dimensions are `(4,2,1,1)` for `1,chi_-4,chi_8,chi_-8`; the full source representation is not asserted irreducible.

## PCQ-02. An actual self-quotient operator, not an imposed reflection

Substitute the original immutable `p`. Exact coefficient evaluation gives

\[
\boxed{S_1p=S_5p=p,\qquad S_3p=S_7p=-\tfrac12p^\sharp.}\tag{PCQ-4}
\]

By the group law, `S_3p#=-2p` and `S_5p#=p#`, so `S_3` is a TRUE involution on the two-dimensional source submodule `M=span_Q{p,p#}`. The optional rescaling `J=-2S_3` satisfies `J(p)=p#`, `J(p#)=4p` and `J²=4I`; **its involution is source-derived** because `J` is the genuine operator `S_3` multiplied by -2, not a formal arrow invented to fit the two formulas.

Let `chi_-4(a)=+1` at a=1,5 and -1 at a=3,7. The group-ring idempotents are

\[
\Pi_\chi=\tfrac14\sum_{a\in G}\chi_{-4}(a)S_a,\qquad
\Pi_1=\tfrac14\sum_{a\in G}S_a.
\]

All 4 character projectors sum to identity on Q^8 and are pairwise orthogonal. For the **one original source**, `S_5p=p`, hence `Pi_chi8 p=Pi_chi-8 p=0`; its actual two-dimensional orbit module decomposes into precisely `1 ⊕ chi_-4`:

\[
\boxed{p_{\rm angular}=\Pi_\chi p=\frac{2p+p^\sharp}{4},\qquad
p_{\rm radial}=\Pi_1 p=\frac{2p-p^\sharp}{4},\qquad p=p_{\rm angular}+p_{\rm radial}.}\tag{PCQ-5}
\]

The `S_3` eigenvalues are **-1 on the angular source** and **+1 on the radial source**. This is different from #481's **central spectral projectors** in `Q(sqrt2) × Q(i)`: those split minimal pole factors; these split prime-Frobenius source-character eigenspaces, and their radial mode contains both real and Gaussian pole contributions. Equating the two splittings is a type error.

The genuine p-primary eigen-relations for any p>8k are

\[
\boxed{
 p\,Y_{kp}\equiv \chi_{-4}(p)Y_k\pmod p,
 \qquad p\,Z_{kp}\equiv Z_k\pmod p,
 \qquad pU_{kp}\equiv Z_k+\chi_{-4}(p)Y_k\pmod p,}\tag{PCQ-6}
\]

where `Y=U^(p_angular)`, `Z=U^(p_radial)`, and the residues of RHS are well-defined since denominators are p-units in this range. This is an exact *selected source* congruence for every eligible p and k, not a statistical temporal cancellation estimate.

## PCQ-03. The source-unique angular representative inside this two-dimensional quotient

The original two BBP kernels are

\[
 K(t)=\frac{P(t)}{1-t^8/16},\qquad
 K^\sharp(t)=\frac{P^\sharp(t)}{1-t^8/16},
\]

with `P=4-2t^3-t^4-t^5` and `P#=8t+4t²+4t³-t⁶`. The projected kernels simplify **as rational functions**:

\[
\boxed{
 K_{\rm angular}(t)=\frac{P_{\rm angular}(t)}{1-t^8/16}
 =\frac4{(t-1)^2+1},
 \qquad
 K_{\rm radial}(t)=\frac{P_{\rm radial}(t)}{1-t^8/16}
 =2\frac{d}{dt}\log\frac{2-t^2}{(t-1)^2+1}.}\tag{PCQ-7}
\]

These polynomial and logarithmic identities were also known in the earlier October 26 SUCC *Two Quadratic Atoms* dossier; they are **not claimed newly discovered**. The new theorem is (PCQ-1)–(PCQ-6): the original prime-Frobenius self-echo *forces exactly those known pieces by a character projector*.

The logarithmic primitive has value 1 at both t=0 and t=1, so `Integral K_radial=0`. The angular channel has period `Integral K_angular=pi`. Thus on `M=span_Q{p,S3p}`, the source period functional `I(w)=∫_0^1 P_w(t)/(1-t^8/16) dt` vanishes exactly on the trivial-character line and is nonzero on the `chi_-4` line:

\[
\boxed{M / \langle p_{\rm radial}\rangle \cong
\langle p_{\rm angular}\rangle;\qquad
\int_0^1 K_{\rm angular}(t)dt=4\,[\arctan(t-1)]_0^1=\pi.}\tag{PCQ-8}
\]

The **pole-support condition** (no `t=±sqrt2` poles) and the original source's normalization select the canonical representative in this declared 2-dim module, NOT a unique formula among every possible formula for π.

## PCQ-04. A truly minimal Gaussian primal carrier, and the signed base-4 formula

Let `Q2(t)=(t-1)^2+1=2(1-t+t²/2)`. The reduced angular rational transfer is

\[
\boxed{K_{\rm angular}(t)=\frac2{1-t+t²/2}=\frac{2+2t+t²}{1+t^4/4}.}\tag{PCQ-9}
\]

Its first impulse coefficients are `(2,2,1,0,-1/2,...)`, satisfying `c_(m+2)=c_(m+1)-c_m/2` and **c_(m+4)=-c_m/4**. The 2×2 Hankel minor `[[2,2],[2,1]]` has determinant `-2`, and the rational transfer's reduced denominator has degree 2, so the minimal reachable/observable **rational linear** realization is EXACTLY dimension 2. There is no one-dimensional Q-linear realization of this transfer. A real 2×2 matrix that realizes it is

\[
G=\frac12\begin{pmatrix}1&-1\\1&1\end{pmatrix},
\quad b=(1,0)^T,\quad c=(2,2),\qquad
K_{\rm angular}(t)=c(I-tG)^{-1}b.
\]

Equivalently, this is one Gaussian complex atom `u=(1+i)/2` satisfying
`u²-u+1/2=0`, `u^4=-1/4`, `u^8=1/16`. The **circle quotient** of its nonzero complex amplitude by positive radial magnitude yields `u/|u|=(1+i)/sqrt2=exp(iπ/4)`. This is a standard complex-polar quotient, not a physical quantum Feynman amplitude. The orientation and source polynomial are retained.

Expanding (PCQ-9) first in **signed radix -4** and integrating term by term gives the compact primal π-series

\[
\boxed{\pi=\sum_{k=0}^{\infty}\frac{(-1)^k}{4^k}\left(\frac2{4k+1}+\frac2{4k+2}+\frac1{4k+3}\right).}\tag{PCQ-10}
\]

This classical arctan/BBP-type identity has no worldwide novelty claim. It explains `4` as the Gaussian quarter-cycle multiplier, while `16=(-4)^2` is the first *positive* scalar return.

## PCQ-05. The primal rational source retains exact 2-integrality and the odd inverse branch

Even though the six taps of `p_angular=(2,2,1,0,-1/2,-1/2,-1/4,0)` individually have denominators with 2, their complete ORIGINAL Mellin moment, after gluing, is

\[
\boxed{r_{\rm angular}(n)=
\frac{30720 n^5-63232 n^4+45792 n^3-13892 n^2+1641 n-48}
{(4n-3)(4n-1)(8n-7)(8n-5)(8n-3)(8n-1)}.}\tag{PCQ-11}
\]

The denominator on RHS is **ODD for every integer n≥1**. Hence `r_angular(n)∈Z_2`, and its literal zero-seeded recurrence `Y_n=16Y_(n-1)+r_angular(n)` also has odd reduced denominator for every n. The same source admissible **odd-denominator inverse circle branch** as #488 therefore remains available after the quotient. Reducing the six taps *separately* in Z2 would be invalid; glue their rational moments first.

As ordinary real n→infinity, the primal forcing and radial forcing have the *opposite* leading terms:

\[
 r_{\rm angular}(n)=\frac{15}{32n}+\frac{113}{256n²}+O(n^{-3}),
\qquad r_{\rm radial}(n)=-\frac{15}{32n}-\frac{53}{256n²}+O(n^{-3}).
\]

Adding yields the original accelerated `r(n)=15/(64n²)+O(n^{-3})`. **The extra analytic `1/n` cancellation is real:** dropping the logarithmic channel makes the rational transfer smaller (dimension 2), but makes its source forcing larger (`1/n` rather than `1/n²`). The original BBP may be understood as the primal π angle together with an exact zero-period analytic **conditioning counterterm**. Do not claim the primal source automatically has better near-pair estimates.

## PCQ-06. ALL-TIME selected real Weyl and collision-current transfer: original ↔ primal

Define the exact, zero-seeded primal and radial rational trajectories

\[
Y_n=U_n^{p_{\rm angular}}=\frac{2U_n+V_n}{4},\quad
Z_n=U_n^{p_{\rm radial}}=\frac{2U_n-V_n}{4},\quad U_n=Y_n+Z_n.
\]

The inherited **all-time** PF-8b bound on the original/dual null difference gives

\[
\boxed{0<Z_n<\frac1{32n+16}\quad(n\ge1).}\tag{PCQ-12}
\]

Thus the *primal* angular orbit and the original complete BBP orbit differ by a pointwise positive radial amount that tends to zero, with source-authenticated universal bounds. For any fixed integer h, using `|exp(2πix)-exp(2πiy)|≤2π|x-y|`:

\[
\boxed{
 \left|\sum_{n=1}^N e(hU_n)-\sum_{n=1}^Ne(hY_n)\right|
 <\frac{\pi|h|}{16}\,H_N.}\tag{PCQ-13}
\]

As `H_N=logN+γ+O(1/N)`, the normalized means differ by `O_h(logN/N)`. Therefore

\[
\boxed{\text{π base16 normal}\quad\Longleftrightarrow\quad
N^{-1}\sum_{n=1}^N e(hY_n)\to0\quad\text{for every fixed }h\ne0.}\tag{PCQ-14}
\]

**This is a rigorous replacement of the original 4-state rational transfer by its 2-state Gaussian primal FOR THE WEYL TEST**, not an assertion that either Weyl sum is small. Because it uses a source-specific `O(1/n)` comparator, it preserves original selected phase at the needed asymptotic fixed-h resolution. General equidistribution stability under `o(1)` perturbations is classical; the contribution is the exact source-derived primal construction and explicit error.

For epoch `[A,2A)` and any real integer harmonic h,

\[
 |c^U_A(h)-c^Y_A(h)|<\frac{2\pi|h|}{32A+16};
\]

uniformly over any band `|h|=o(A)`. For the triangular selected real current 
`J_(A,q)(X)=(q/A²)Σ_(n,t)(1-q||X_n-X_t||)_+`, the source difference `Z_n` lies in `(0,1/(32A+16))`. This and the q-Lipschitz tent give the **deterministic quantitative current bridge**

\[
\boxed{|J_{A,q}(U)-J_{A,q}(Y)|\le\frac{q²}{32A+16}.}\tag{PCQ-15}
\]

At `q≈logA` it is `O(log²A/A)=o(1)`. Hence the still-UNPROVED original current target `J(U)=o(K_A)` is equivalent at this mesh to `J(Y)=o(K_A)`. No selected mixing has been established. The primal construction is therefore a legitimate 2-state replacement FRONT for the hard selected current problem.


## PCQ-07. A second sharp prime theorem: primal denominator mass is **8N**, original mass is **6N**

The universal angular pulse normalizer has a stronger **factorization at EVERY event**. Fix `a in {1,3,5,7}` and let `m=8k+ell`, `k>=0`, `1<=ell<=8`. Write `j_a(ell)` as before, and define the signed transport from the full preceding p-block to event `ell`:

\[
f_a(\ell)=\chi_2(a)^\ell\,2^{(\ell+8-j_a(\ell))/2}\in\mathbb Q^\times.
\]

Since `S_a p_angular=chi_-4(a) p_angular` and `f_a(ell) * [(S_a w)_ell / w_(j_a(ell))] = 16` when nonzero, the true **rational universal event-clock normalizer** (not yet reduced modulo any prime) is

\[
\boxed{
 C^{\rm angular}_a(8k+\ell)
 =\chi_{-4}(a)f_a(\ell)
 \left(Y_k+\frac1{16}\sum_{j=1}^{\ell}\frac{w^{\rm angular}_j}{8k+j}\right),
 \quad w^{\rm angular}=(2,2,1,0,-1/2,-1/2,-1/4,0).}\tag{PCQ-16}
\]

**All-event algebraic proof.** At the preceding full source p-block, the normalized state is `chi_-4(a)*Y_k`. Moving `ell` event positions multiplies it by `f_a(ell)`. A new injection `w_(j_a(j))/(8k+j)` enters at event `j`. Transporting it to event `ell` multiplies by `f_a(ell)/f_a(j)`. By the *proven character eigenrelation* and the source time normalization,

`w_(j_a(j))/f_a(j) = chi_-4(a)*w_angular(j)/16`.

Factor `chi_-4(a)*f_a(ell)` out of all terms to obtain (PCQ-16). This holds for **all k,ell**, independent of finite p tests; its mod-p meaning requires the usual `p>m`, `p²>8N` simple-pole conditions.

**Strict positivity for every k and ell.** Each angular forcing moment is positive since `P_angular(t)=(1−t⁴/4)(2+2t+t²)>0` on `[0,1]`, hence `Y_k>=0` and `Y_k>0` for `k>=1`. Each *partial* harmonic sum is also strictly positive: the first tap `2/(8k+1)` is positive, all other positive taps can only help, and the full magnitude of later negative taps is bounded by

\[
\frac{1/2+1/2+1/4}{8k+5}=\frac{5}{4(8k+5)}
 <\frac2{8k+1}.
\]

Therefore the parenthetical factor in (PCQ-16) is **strictly positive** for every `k>=0, 1<=ell<=8`. This certifies every single angular p-pulse as nonzero with **forced sign**

\[
\boxed{\operatorname{sgn}C^{\rm angular}_a(8k+\ell)
 =\chi_{-4}(a)\chi_2(a)^\ell.}\tag{PCQ-17}
\]

This is a universal proof, not extrapolation from tested p classes. The source's prior radial counterterm is absent; unlike the original sparse four-pole source, the projected angular source has **nonzero taps at all FOUR odd positions 1,3,5,7**. Consequently every sufficiently large odd prime, regardless of its mod-8 class, first appears in the projected source by time `n=(p+8-(p mod8))/8`, with a nonzero injection. All odd primes `p<=8N−7` are therefore in the angular source's cumulative conductor by time N, up to fixed exceptions.

Put `D_N^ang=den(Y_N)`, `M_N^ang=lcm_{j<=N} den(r_angular(j))`. All individual source taps have only 2-power rational denominators, and the combined `r_angular(j)` has an **odd** reduced denominator by PCQ-11. Hence

\[
D_N^{\rm ang}\mid M_N^{\rm ang}\mid\operatorname{lcm}(1,2,\dots,8N)_{\rm odd},
\quad\log M_N^{\rm ang}=8N+o(N)
\]

by the classical (ordinary) prime number theorem and the fact that source birth occurs for every generic prime up to `8N−7`. (Repeated prime powers contribute only sublinear mass; upper bound is the standard Chebyshev `psi(8N)~8N`.)

**Selected-state survival proof, with ALL quantifiers.** Fix `eps>0`. For primes `p>eps*N` in that source support, the number of p events before time N is bounded by `8/eps+O(1)` and `p²>8N` for all sufficiently large N. Every possible rational normalizer in this finite **eps-dependent** set is nonzero by (PCQ-17). Taking p larger than every numerator and denominator prime of those finitely many rational numbers forces `pU_N^ang` to be a p-unit, thus `v_p(Y_N)=-1`. Therefore

\[
\boxed{\forall\varepsilon>0\ \exists N_\varepsilon\ \forall N\ge N_\varepsilon\
 \forall\text{ odd prime }p\in(\varepsilon N,\,8N-7]:\quad v_p(Y_N)=-1.}\tag{PCQ-18}
\]

The onset is existential, not numerically certified. Finitely many smaller p may cancel at particular horizons; the theorem does **not** forbid that.

Applying PNT to surviving p, letting `eps↓0` AFTER the liminf, and using the cumulative conductor upper bound yields the new all-N asymptotic

\[
\boxed{
 \log\operatorname{den}(Y_N)=(8+o(1))N,
 \qquad \log\frac{M_N^{\rm ang}}{\operatorname{den}(Y_N)}=o(N).}\tag{PCQ-19}
\]

Contrast the original #497 source theorem `log den(U_N)=(6+o(1))N`. **The quotient reduces minimal rational-transfer state dimension from FOUR to TWO, but INCREASES the realized denominator entropy from exponent 6 to exponent 8**:

\[
\boxed{
\log\frac{\operatorname{den}(Y_N)}{\operatorname{den}(U_N)}=(2+o(1))N,
\qquad 0<U_N-Y_N<\frac1{32N+16}.}\tag{PCQ-20}
\]

Thus two source-authentic rational states become arbitrarily **close in the real metric** while their exact reduced denominators differ by an exponentially large factor. The original logarithmic/radial null channel is a real analytic **conditioning counterterm** that cancels the angular source's leading `1/n` forcing and the accompanying bulk of prime-denominator complexity. This is a source arithmetic complexity statement, NOT a statistical entropy, normality, or quantum result. The all-m strict pulse inequality and PNT are the mathematical proof, not finite ratio fitting.

## PCQ-08. Controls, authority and unearned consequences

1. **Not a world-first π formula:** arctan angle, 2-state Gaussian transfer and signed base-4 BBP are classical/earlier in SUCC October 26. See Barsky–Muñoz–Pérez-Marco, *On the genesis of BBP formulas* (Acta Arith. 198, 2021); MathWorld BBP-Type Formula's original and alternative π series. The new-to-repo composition is (PCQ-1)–(PCQ-6), showing **why** those known angular/radial atoms follow from a **prime-source** V4 action.
2. **Do not claim the S_a action is global time-Galois averaging.** It is a finite-field p-local equality under the precise `p>8k` simple-pole boundary, and an algebraic Q^8 representation, not selected real time equidistribution.
3. **Wrong source mutation:** incrementing original tap w_1 from 4 to 5 destroys original `S_5p=p` and the exact arctan/period-zero quotient. That source would define a different pair of character components; no artificial uniqueness persists.
4. **Wrong Legendre sign:** changing the chi2 factors breaks congruences for classes 3 and 5. This is tested against actual original p-local arithmetic, not only group symmetry.
5. **Wrong seed:** adding a p-integral rational seed e.g. 1/5 preserves **all** p-local echoes at primes p>5, but rotates selected real phase by 1/5; so the p-shadow alone does not authenticate the literal zero seed. This rational rotation does not by itself cause nonnormality; coherent irrational seed controls remain separate.
6. **The quotient is observer-constructible:** start from eight source taps, observe p-residues of actual zero-seeded states at p*K times, derive the prime-class monomial operators using Euler's criterion, then apply the finite-group character projector. The complex angle is established by an exact rational identity with an independently justified arctan primitive. Nothing supplies an already-unproved Haar measure.
7. **The radial null is zero only at analytic completion.** Its selected finite state `Z_n>0` and its source forcing has size `1/n`; it is not a zero vector at each finite step. Character projection and source observer are different operations.
8. **Academic originality:** limited external searches found the classical angle, dual π formula and log-null relations (Barsky et al. 2021), but not yet a source-prime V4 representation with the explicit 2-state original/primal signed-current transfer. Absence from search is NOT a priority proof. Independent specialized referee and wider prior-art review required before any publication-level novelty claim.

**Status ledger:** PCQ-01/02 SOURCE-SPECIFIC paper proofs with exact modular oracles; PCQ-03/04 exact rational/angular classical identities now attached to prime character, no π-digit normality claim; PCQ-05 exact source-specific odd denominator and asymptotic conditioning; PCQ-06 all-time Weyl and current transfer, dependent on #497 PF-8b; PCQ-07 all-pulse angular strict positivity and sharp `8N` selected denominator saturation (classical PNT imported); all finite holdouts OBSERVED. **Actual selected source `J=o(K_A)`, fixed-h Weyl decay, π base-16 normality and RH remain OPEN.**
