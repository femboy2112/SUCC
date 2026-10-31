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

