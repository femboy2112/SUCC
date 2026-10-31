# Three-place BBP difference resolvent: exact common Gamma moments and pole spectrum

**2026-10-31, research-only.** Stacked on draft PR #429 at head 33d53f576fe2c2e847e51c24ccf7a94aa6ec6f10, with Main XVII as canonical baseline. Original four signed BBP poles and U_0=0 are untouched. **RH and π base-16 normality remain OPEN.** These are elementary/classical paper proofs specialized to the exact source; no scholarly priority claim or automatic phase cancellation.

## TD-01. Original four-pole source has a positive real Gamma hierarchy

Let (w,c) run through (4,7), (-2,4), (-1,3), (-1,2). The authentic rational source is

\[
r(z)=\sum_{w,c}\frac{w}{8z-c}
=\frac{120z^2-89z+16}{(2z-1)(4z-1)(8z-7)(8z-3)}.
\]

The exact source polynomial factors as

\[
\boxed{P(t)=4-2t^3-t^4-t^5
=(1-t)(t^2+2)(t^2+2t+2).}
\]

It is positive on 0≤t<1. For real z≥1, direct Euler integration gives

\[
\boxed{r(z)=\int_0^1t^{8z-8}P(t)\,dt
=\int_0^\infty e^{-(8z-7)u}P(e^{-u})\,du.}\tag{TD01}
\]

In particular the ORIGINAL signed source is positive, strictly decreasing, and completely monotone in this real range; no substitute source or model measure is introduced. Define the exact rational moments for integer y≥1,j≥0,

\[
\boxed{C_j(y)=\sum_{w,c}\frac{w}{(8y-c)^{j+1}}
=\frac1{\Gamma(j+1)}
\int_0^\infty u^j e^{-(8y-7)u}P(e^{-u})\,du>0.}\tag{TD02}
\]

This is a common coefficient family: Archimedean Gamma integration yields exact rational C_j, which can then be evaluated in Q2 or Q3 as rational numbers. The integral itself is NOT interpreted as a p-adic integral. As
\(P(e^{-u})\le15(1-e^{-u})\le15u\),

\[
\boxed{0<C_j(y)<15(j+1)/(8y-7)^{j+2}.}\tag{TD03}
\]

The extra inverse power is genuine cancellation of leading pole weights P(1)=0, retained in the original source.

## TD-02. A single rational infinite series decomposes BOTH source values

For integers 1≤x<y, let h=y−x. Each original pole has the convergent geometric resolvent

\[
\frac{w}{8x-c}=\sum_{j\ge0}\frac{w(8h)^j}{(8y-c)^{j+1}}.
\]

All original four coefficients are retained. Since every denominator 8y−c>8h, the sum converges absolutely in R. Thus

\[
\boxed{r(x)=\sum_{j\ge0}(8h)^j C_j(y),\
r(y)=C_0(y),\
r(x)-r(y)=\sum_{j\ge1}(8h)^j C_j(y).}\tag{TD04}
\]

The positive real Gamma integral separately reproduces the difference:

\[
r(x)-r(y)=\int_0^\infty e^{-(8y-7)u}P(e^{-u})
(e^{8hu}-1)\,du>0.
\]

The infinite series is not an unsupported infinity-minus-infinity cancellation: it is obtained from individually convergent geometric series and an exact shared coefficient chart.

For cutoff J≥1, let S_J=Σ_(1≤j<J)(8h)^j C_j(y). Finite geometric telescoping yields the EXACT rational remainder

\[
\boxed{R_J=r(x)-r(y)-S_J
=(8h)^J\sum_{w,c}
\frac{w}{(8y-c)^J(8x-c)}.}\tag{TD05}
\]

Setting ρ=8h/(8y−7), 0<ρ<1, and using Σ|w|=8 gives

\[
\boxed{|R_J|_\infty\le 8\rho^J/(8x-7).}\tag{TD06}
\]

Both the finite approximation and the exact remainder are rational, allowing independently defined absolute values at every place.

## TD-03. The SAME rational expansion converges in R, Q2, Q3

For integral y, the four original denominators 8y−c have 2-adic valuations (0,2,0,1), respectively. Therefore every ratio 8h/(8y−c) has 2-adic valuation at least v2(h)+1>0. The resolvent converges in Q2 for every integer h.

At p=3 define the maximal individual pole depth

\[
\boxed{d(y)=\max_{c=7,4,3,2}v_3(8y-c)\ge1.}
\]

The series converges in Q3 whenever m3=v3(h)>d(y). Under that hypothesis the same pole denominators at x=y−h and y have identical 3-adic valuations. The exact remainder TD05 satisfies three rigorous simultaneous estimates:

\[
\boxed{
|R_J|_\infty\le\frac{8}{8x-7}\rho^J,\quad
v_2(R_J)\ge J(v_2(h)+1)-2,\quad
v_3(R_J)\ge J(m_3-d(y))-d(y).
}\tag{TD07}
\]

These follow termwise using pole valuations and the ultrametric inequality. As J increases the right-hand valuation lower bounds tend to +infinity. This is a genuine common finite-to-global rational series certificate in THREE different completions, with explicit and place-dependent error budgets.

## TD-04. Exact sharp 3-adic source-pole law, improving PR #429

For every integer y the original source derivative satisfies

\[
r'(y)=-8C_1(y),\qquad
\boxed{v_3(r'(y))=-2d(y),\quad v_2(r'(y))=0.}
\]

For p=2, the combined odd-denominator polynomial shows its derivative is a 2-adic unit (the numerator derivative is odd, denominator derivative even). For p=3, classify y mod3. At y≡0 only the pole c=3 is 3-divisible, at y≡1 only c=2 is, and the corresponding original coefficients are units. At y≡2, poles c=7 and c=4 collide modulo3 and differ by exactly 3. If one has larger depth it dominates. If both have the same depth, it must be 1. Write 8y−7=3u, 8y−4=3(u+1), with u≡1 and u+1≡2 modulo3. After multiplying the leading slope by 9, the coefficient is 4/u²−2/(u+1)²≡4−2≡2 mod3: NONZERO. This proves the exact derivative valuation for all integers.

For every m>d(y), with h=6^m, each pole difference has the source-faithful rational form

\[
\frac{w}{8(y-h)-c}-\frac{w}{8y-c}
=\frac{8hw}{(8y-c)(8y-c-8h)}.
\]

Because m is deeper than every pole, the normalized residue mod3 of the two denominator factors is unchanged, so the same non-cancellation proof gives

\[
\boxed{
v_3(r(y-6^m)-r(y))=m-2d(y),\qquad
v_2(r(y-6^m)-r(y))=m.
}\tag{TD08}
\]

The 2-adic identity follows independently from the already established authentic source isometry. This is strictly sharper than the prior bound m−2v3(D(y)) in PR #429: for y≡2 mod3, the combined denominator valuation sums two colliding pole depths, whereas the actual derivative/difference is controlled by their MAXIMUM. Example y=8: v3(D(8))=2 but d(8)=1; the exact output is m−2 for all m>1, not merely a lower bound m−4 with onset m>2. No original source sign is omitted.

## TD-05. All-horizon 3-adic pole-depth distribution and CRT source independence

For k=1 all three integer residues mod3 have d(y)≥1. For k≥2 the four congruences 8y≡7,4,3,2 modulo 3^k define four distinct classes (the four pole constants are pairwise distinct mod9). Therefore

\[
\boxed{\Pr(d(y)\ge1)=1,\qquad
\Pr(d(y)\ge k)=4/3^k\quad(k\ge2).}\tag{TD09}
\]

This is a density of ordinary integer residue classes, NOT a probability law for real π digits. It gives P(d=1)=5/9, deep-pole exceptional density 4/3^k, and exact truncated depth mean

\[
\boxed{\mathbb E[\min(d,K)]=5/3-2/3^K,\qquad
\mathbb E[d]=5/3.}\tag{TD10}
\]

The existing SUCC DSI-4 proves n→U_n mod2^a is a permutation every 2^a steps for the authentic zero-seeded source. The depth min(d(n+1),K) depends only on n+1 mod3^K. CRT therefore shows that over every translated block of length 2^a3^K the BBP dyadic state residue and the original 3-adic pole depth have EXACT product frequencies. This establishes a deterministic joint local source-law, without postulating independent stochastic primes and without identifying it with the real-circle occupation measure.


## TD-06. One actual BBP source difference forces EXPONENTIAL denominators at other primes

Take the same two positive original source indices for every m≥2:

\[
x=1,\qquad y_m=1+6^m,\qquad
\Delta_m=r(1)-r(1+6^m).
\]

Now d(y_m)=1<m, so the triple-place TD04/TD07 series is valid simultaneously in R, Q2, Q3. The source-positive real integral is

\[
\boxed{\Delta_m=\int_0^1(1-t^{8\cdot6^m})P(t)\,dt.}\tag{TD11}
\]

Therefore Δ_m increases and approaches r(1)=47/15 in the REAL metric. Since r(2)=106/819<2/15 and r is decreasing, for all m≥2,

\[
\boxed{3<\Delta_m<47/15,\qquad
\lim_{m\to\infty}\Delta_m=47/15\quad\text{in }\mathbb R.}
\]

But TD08 yields

\[
\boxed{v_2(\Delta_m)=m,\qquad v_3(\Delta_m)=m-2,}\tag{TD12}
\]

so these very same finite rational numbers converge to ZERO in both Q2 and Q3.

There is an independently checkable closed rational formula: for every positive h,

\[
\boxed{
r(1)-r(1+h)=
\frac{h(24064h^3+48128h^2+31664h+6853)}
{15(2h+1)(4h+3)(8h+1)(8h+5)}.
}\tag{TD13}
\]

When h=6^m, the cubic factor is odd and a 3-adic unit: 6853≡1 mod3; the denominator has exactly v3=2 from the factors 15 and 4h+3, independently recovering TD12. Since h≡1 mod5, the cubic factor is 4 mod5 while all four linear factors (2h+1),(4h+3),(8h+1),(8h+5) are 5-adic units. The initial factor 15 has exactly one factor5, so the REDUCED denominator B_m has v5(B_m)=1. It has no factors2 or3, because v2(Δ_m),v3(Δ_m) are nonnegative.

Write Δ_m=A_m/B_m in lowest positive terms. Its numerator is divisible by 2^m3^(m−2)=6^m/9. Since Δ_m<47/15, we obtain the rigorous **complementary-prime exposure bound**

\[
\boxed{\gcd(B_m,6)=1,\quad v_5(B_m)=1,\quad
B_m>\frac5{141}6^m.}\tag{TD14}
\]

A nonzero Archimedean source limit simultaneously with local cancellation at 2 and 3 therefore FORCES an exponentially growing denominator supported at other primes, with 5 always present. This proves a precise arithmetic radiation effect. It does NOT prove anything about distribution of those prime factors, zeta-zero positions, or π hexadecimal digit frequencies. The ordinary product formula also gives the exact identity

\[
\prod_{p\ge5}|\Delta_m|_p
=\frac{6^m}{9|\Delta_m|_\infty},
\]

but TD14 is proved directly using integer divisibility and the real bound.

## TD-07. A TRUE noncommuting finite-vs-global Gamma/real horizon (PROVED LOCAL)

For h_m=6^m, y_m=1+h_m, let the finite original-source resolvent partial sum be

\[
S_{m,J}=\sum_{j=1}^{J-1}(8h_m)^j C_j(y_m),\qquad J\ge1.
\]

All terms are positive for real y≥1 by TD02. The Gamma-moment upper bound TD03 yields

\[
\boxed{0\le S_{m,J}
\le\frac{15(J-1)(J+2)}{2(8\cdot6^m+1)^2}.}\tag{TD15}
\]

For every fixed J, S_(m,J)→0 in the real metric as m→∞. But for every fixed m, J→∞ sums the entire positive resolvent and gives Δ_m, whose real limit is 47/15. Therefore

\[
\boxed{
\lim_{m\to\infty}\lim_{J\to\infty}S_{m,J}
=\frac{47}{15},
\qquad
\lim_{J\to\infty}\lim_{m\to\infty}S_{m,J}
=0.
}\tag{TD16}
\]

These are both well-defined iterated limits, with a rigorous counterexample to exchanging them. The obstruction is quantitative: the real geometric ratio 8h_m/(8h_m+1) approaches 1, and its convergence is not uniform in the moving observation horizon. This is a source-specific finite-to-global failure of observer interchange, NOT the naive assignment of a value to a divergent ordinary sum.

**Complementary prime-place behavior.** For any fixed J≥2, the p-adic remainder budgets from TD07 are at least J(m+1)−2 for p=2 and J(m−1)−1 for p=3. They tend to +infinity as m→∞. In fact the FIRST nonzero term j=1 already has the full source local valuations m and m−2 (TD04), while its real magnitude decays O(6^(−2m)) by TD03. The same finite rational term is consequently decisive for p-adic observation, but asymptotically invisible for the real realization. This is precisely why the full coefficient series and its declared completion protocol matter.

## TD-07B. Deep 3-adic BBP source poles cannot alone carry a persistent real Weyl defect

For k≥2 let E_k(A,N) be the positions A≤n<A+N where d(n+1)≥k. Since exactly four residue classes mod3^k meet this condition, elementary finite counting gives, **for every starting index A and every N**,

\[
\boxed{\frac{|E_k(A,N)|}{N}\le\frac4{3^k}+\frac4N.}\tag{TD17}
\]

For arbitrary complex source-selected phases z_n of modulus ≤1 (in particular the TRUE e(hU_n), with original zero-seeded states), deleting those exceptional positions changes the normalized sum by at most their fraction:

\[
\boxed{\left|\frac1N\sum_{A\le n<A+N}z_n-
\frac1N\sum_{\substack{A\le n<A+N\\d(n+1)<k}}z_n\right|
\le\frac4{3^k}+\frac4N.}\tag{TD18}
\]

Thus for ANY declared sequence k_N≥2 tending to infinity, the full and shallow-truncated normalized Weyl means differ by o(1), without assuming independent source phases. In particular, a hypothetical persistent π nonnormality Fourier defect **cannot be supported solely on arbitrarily deep 3-adic source-pole positions**; it must survive on the increasingly comprehensive shallow-source strata. This is an actual all-horizon elimination of one family of attempted mechanisms. It is NOT a saving on the shallow signed sum, so it does not prove normality.

The same bound sharpens the typical-domain restriction of TD08: at any depth m≥2, all but at most 4/3^m+4/N of the original consecutive source positions obey the exact 3-adic finite difference valuation m−2d(n+1). The exceptional depth classes remain separately visible rather than being discarded inside a false uniform 3-adic isometry.

## TD-08. What the theorem does and does not establish for π/RH

**PROVED LOCAL / classical inputs:** TD-01 through TD-07, including positive original-source Gamma moments, a simultaneously convergent three-place rational resolvent with exact finite remainder, the SHARP 3-adic pole non-cancellation theorem, deterministic pole-depth distribution independent of the authenticated dyadic source residue, a forced complementary-prime denominator-growth law, and noncommuting real finite/global limits. Original source labels and all four pole signs are retained. A nearby approximation or same-source changed seed can share some of these universal forcing identities; no seed-dependent phase cancellation has been earned.

**OPEN:** selected zero-boundary Weyl sum o(N), source-derived real ×3 invariance of every π occupation limit, positive entropy in all joint ergodic components, RH, and any theorem RH⇒π normality. The difference of two source values is NOT the difference of the selected real-circle Fourier phases. An exact arithmetic source-transfer identity cannot be silently promoted to an invariant-measure theorem.

**Next verdict-changing probe:** condition the original signed two-time phase increments e(hU_n) on the certified 3-adic pole-depth strata d(n) while preserving the real Green correction and literal U0=0. The exceptional depths have rigorously known relative density 4/3^k; test whether their full complex cofiber interactions permit or rule out a persistent source-selected non-Haar defect. A valid normality-relevant gain must be a new all-horizon SIGNED arithmetic inequality that fails on the coherent same-forcing changed seed and rational periodic controls. Repeating the local pole statistics is NOT such a gain.

**Provenance:** Original BBP source and prior SUCC DSI dyadic isometry; draft #429 half-power 6-adic successor; Operation SUMMATION SNAPSHOT ARROWS. Classical tools: rational geometric series, Gamma Laplace moments, CRT, integer valuations, and product formula. A finite exact Fraction probe and a discoverable unittest file calibrate the claims without claiming Lean kernel authority or external independent refereeing.
