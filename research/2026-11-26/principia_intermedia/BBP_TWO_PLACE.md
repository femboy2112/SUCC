# Authentic BBP complementary observers: forced seams and a two-place obstruction

**Status:** PROVED PAPER under the explicitly defined source-cut model. Classical ingredients; no priority or π-normality claim. The source passport is the original recurrence, not a guessed randomness carrier:

\[
r(n)=4/(8n-7)-2/(8n-4)-1/(8n-3)-1/(8n-2),\quad U_0=0,\quad U_n=16U_{n-1}+r(n).
\]
\[
x=\sum_{n\ge1}16^{-n}r(n)=\pi/16,\quad Q(t)=4-2t^3-t^4-t^5=(1-t)(4+4t+4t^2+2t^3+t^4).
\]

The positive measure μ on u∈[0,1] is the pushforward of Q(t)dt by u=t^8: dμ(u)=Q(u^{1/8})/(8u^{7/8})du. Thus r(k+1)=∫u^k dμ. This is exactly the source of [#689, theorem dossier §§1–2](https://github.com/femboy2112/SUCC/blob/d6fde02a8d810d361b8f7b97fbf3eb029ec6a7d3/research/2026-11-23/null_seed_virtual_tower/THEOREMS.md), rederived here without changing the zero seed. The weighted λ with dλ=dμ/(16−u) satisfies λ([0,1])=x by geometric summation. μ and λ are different readouts: the 2-adic results below apply to μ, not automatically λ.

## B1. Single-cut BBP moment seam hierarchy (PROVED)

Put A_k(a)=∫_0^a u^k dλ(u), B_k(a)=∫_a^1 u^k dλ(u), D_k=A_k−B_k. All cuts preserve A_k+B_k and the same source passport, with D_k(0)<0<D_k(1). Each D_k has a unique root a_k by strict monotonicity and continuity. At a_k, weighting by u makes the left integral strictly smaller than a_k A_k(a_k) and right strictly larger than a_k B_k(a_k). Thus D_{k+1}(a_k)<0, so a_{k+1}>a_k. For any c<d<1, normalized mass below c is at most (c/d)^k λ([0,c])/λ([d,1])→0, hence a_k→1.

The actual density near u=1 obeys Q(t)~15(1−t), 1−u~8(1−t), hence λ'(u)~(1−u)/64. If Y_k=k(1−u) under the normalized u^k λ law, then Y_k converges in distribution to Γ(2,1). Indeed split [0,1] at 1−δ: the low part has exponentially small mass after multiplying by k²; on the upper part substitute y=k(1−u), use (1−y/k)^k≤e^{−y} and λ'(1−y/k)≤C y/k, then dominated convergence yields the unnormalized limiting density y e^{−y}/64 and normalization 1/64. Median convergence follows from strictly increasing continuous limiting CDF around its unique median m. Thus

\[
k(1-a_k)\to m,\qquad (1+m)e^{-m}=1/2.
\]

The compactified coordinate a/(1−a) puts endpoints at 0 and ∞; seam position is asymptotic to k/m. These are moment-observer positions, not digit times or π orbit equidistribution.

## B2. Source-derived simultaneous null partitions (PROVED)

Apply Book VII I4–I7 to μ or λ in the u-coordinate: there is exactly one minimal n-switch partition (up to reversal) for the first n signed moments, and the next moment is nonzero. No single cut nulls the first two. For λ on [1/4,1/2], write t=u^{1/8}. Then 1−t≥(1−u)/8≥1/16, Q(t)≥4(1−t)≥1/4, and 8u^{7/8}(16−u)≤128; hence λ'≥1/512. With L=1/4, I7 gives

\[
\max_{0\le j\le k}|M_j(s)|\ge\frac{1}{4096(32k)^k}\quad(k\ge1)
\]

for any k-switch λ partition. The lower bound is crude but exact and uniform. Infinite binary simultaneous nulls are impossible; finite extremizers weakly cancel but retain total variation. This distinguishes true source loss from a topology's compression of orientation.

## B3. Genuine 2-adic parity obstruction (PROVED)

Use the original t-coordinate and its unweighted source. For k≥0 let

\[
A_k(t)=\frac{4t^{8k+1}}{8k+1}-\frac{2t^{8k+4}}{8k+4}-\frac{t^{8k+5}}{8k+5}-\frac{t^{8k+6}}{8k+6}.
\]

This is an exact primitive of t^{8k}Q(t), so A_k(1)=r(k+1). For t∈Z_(2) (rationals with odd denominator),

\[
2A_k(t)=\frac{8t^{8k+1}}{8k+1}-\frac{t^{8k+4}}{2k+1}-\frac{2t^{8k+5}}{8k+5}-\frac{t^{8k+6}}{4k+3}
\equiv0\pmod2.
\]

All denominators shown are odd; modulo 2 the two odd coefficients multiply powers both congruent to t and cancel. Moreover

\[
r(k+1)=\frac4{8k+1}-\frac1{8k+5}-\frac{3k+2}{(2k+1)(4k+3)}
\equiv k+1\pmod2.
\]

For cuts 0<t_1<...<t_\ell<1 with odd denominators, initial sign ε∈{±1}, the signed moment is

\[
M_k=\epsilon\left((-1)^\ell r(k+1)+2\sum_{i=1}^{\ell}(-1)^{i-1}A_k(t_i)\right).
\]

Therefore M_k∈Z_(2) and M_k≡k+1 mod 2. In particular v_2(M_{2j})=0, so |M_{2j}|_2=1; odd k yields M_k≡0 (no claim of exact higher valuation). This holds for every finite switch budget, not just the sampled grids. It uses the authentic signed coefficients; a different measure is not silently equivalent. For common odd denominator B, k=0 has 15 B^6 M_0 an odd nonzero integer (since 15M_0 is a sum of polynomials 30A_0 with integer coefficients and ±47). Thus |M_0|_∞≥1/(15 B^6). Note that no assertion is made that an arbitrary real cut has a canonical p-adic image.

Odd denominator rationals are dense in R. Approximate the n ordered real roots of I4 by odd-denominator rationals in t-coordinates (u roots mapped by t=u^{1/8}); continuity of primitives implies convergence of every fixed signed moment to that real partition's value, in particular first n to zero. But the even-order residuals remain p-adic units at every finite resolution. More strongly, any sequence of these residuals that converges in Q_2 has a unit limit, because the unit locus is clopen. One may choose approximation accuracy at each n to make the first n real residuals ≤1/n, while all even k remain p-adic units. Thus a real simultaneous-null hierarchy can fail every arithmetic-null test at the same cuts, even with arbitrarily many switches.

This is a direct example of two-place coherence failure, not an appeal to RH, irrationality of π, or normality. A proof of a multi-place null must construct a joint admissible carrier chart or a source-specific bridge; real smallness does not transport for free.

## B4. Even the real median is not rational for μ (PROVED)

For one cut of μ, the signed mass D=2A_0(t)−47/15 obeys

\[
15D=120t-15t^4-6t^5-5t^6-47.
\]

By the rational-root theorem, any rational root in (0,1) could only be t=1/5. But A_0(1/5)≤4/5<47/30, so it is not a root. The real median is algebraic irrational (this is about t, not the λ median or π). On every rational grid t=a/B, D is a nonzero rational with denominator dividing 15 B^6; hence |D|≥1/(15 B^6). On an odd grid, choose a nearest median bracket endpoint; |D|≤8/B from Q≤4. This gives a fully constructive real vanishing residual with persistent 2-adic obstruction. It is a genuinely finite arithmetic seam crossing, rather than an assumption that every real null occurs on the carrier's rational grid.

## B5. Source/seed firewall and next theorem

These cut operators act on the forcing measure, NOT on chronological digit/carry histories. The exact original source and seed are fixed, but an admissible partition is a mathematical readout, not a new legal physical observer maneuver or a certificate of digit statistics. The positivity and moment-balance proofs apply broadly; #689's nonnormal Kempner control shares zero-seed cylinder rigidity and local flatness. The arithmetic parity theorem needs the four-pole measure but does not connect to the R0 Weyl-shell obstruction.

**Next discriminating probe:** from a hypothetical R0 failure derive a source-preserving marked carry/seed observer family, with an explicit transport to signed nulls of a nonzero integral object and bounded arithmetic/real capacity. Prove that real cuts, p-adic cuts, time-grid refinements and carrying are compatible on that object, or derive an unavoidable obstruction. Distinguish odd-denominator chart failure (a boundary of this particular chart) from failure of all allowable charts. Reject counterseed, source aliases, zero carry fields, repeated moment labels, and real-only approximations. No null tower generated just by free choice of cuts can prove R0.

## Finite executable controls

[probe.mjs](probe.mjs) performs exact BigInt rational arithmetic. It compares direct signed interval integrals against the independently formulated alternating primitive using the factored Q polynomial. It enumerates every cut subset of size≤4 for B=3,5,7,9,11, both initial signs, k=0,...,6; tests the parity result and real denominator budget; and brackets the μ median on grids 3^1,...,3^10. It also enumerates LP vertices for five atomic quadratures of μ (exact cell mass, u=(midpoint t)^8, not exact higher continuous moments). All results and limitations in [FINITE_RECEIPT.json](FINITE_RECEIPT.json) and [VALIDATION.md](VALIDATION.md). The universal proofs are above, not inferred from finite counts.
