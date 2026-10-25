# The BBP four-pole local Fourier multipliers and noncommuting all-prime limits

**Date:** 2026-10-24. **Research-only exact addendum to PR #277.**
Source-authenticated original forcing from #272; JPC-06--12 from the frozen
Joint Carrier research tree. Classical inputs: Ramanujan sums, CRT,
Euler/Mertens prime reciprocals, Riemann integration on compact p-adic rings.
**No pi normality or BBP source-orbit cancellation is proved.**

## 1. The source is the original rational BBP forcing

$$
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},
\quad U_n=16U_{n-1}+r(n),\quad U_0=0.
$$

For p>=7, the four roots in `Z_p` of the four linear denominators occupy
distinct classes mod p. Thus at a given local index t there can be only
one pole term with negative p-valuation; the other three are p-integral.
On its depth-k shell, the active term is exactly `c/(p^k*u)` with c a
p-adic unit and u uniform over `Z_p^*` under Haar conditioned on the
shell. This uses the *literal coefficients* 4,-2,-1,-1, none of which
vanishes modulo p>=7, and the slopes 8,8,8,8, all units at p>=7.

Denote by `lambda_p:Q_p -> Q_p/Z_p -> Q/Z` the standard p-primary
fractional readout, represented as a rational in [0,1). Define
`chi_p(x)=exp(2*pi*i*lambda_p(x))`. The map is additive and trivial on
Z_p. It is a **local character**, NOT a generic independent source law.

## 2. An exact one-place multiplier (JPC-23)

For any odd prime p>=7 and integer frequency h, define

$$
m_p(h)=\int_{\mathbb Z_p}\chi_p(h r(t))\,dt.
$$

At h=0, `m_p(0)=1`. If h!=0 and `a=v_p(h)`, then

$$
\boxed{m_p(h)=1-\frac4{p^{a+1}}-\frac4{p^{a+2}}.}
$$

**Proof.** Outside the four pole classes mod p, all four terms are integral,
so the character is 1. That region has measure `1-4/p`.
Fix one pole. On its shell `v_p(linear_denominator)=k>=1`, the shell has
measure `(p-1)/p^(k+1)`. The other pole terms are integral, so the entire
character is the character of a single unit times `h/(p^k*u)`. Inverting
and multiplying by a unit permutes the residues in `(Z/p^k)^*`. The
conditional mean is the normalized prime-power Ramanujan sum

$$
R_{p,k}(h)=\frac1{\varphi(p^k)}
\sum_{u\in(\mathbb Z/p^k)^*} e(hu/p^k)
=\begin{cases}
1,&k\le a,\\
-1/(p-1),&k=a+1,\\
0,&k\ge a+2.
\end{cases}
$$

The value of the local expectation is therefore an **exact finite sum**
(the deeper shells have zero mean):

$$
\begin{aligned}
m_p(h)&=1-4/p+
4\sum_{k=1}^{a+1}\frac{p-1}{p^{k+1}}R_{p,k}(h)\\
&=1-4/p+4(1/p-1/p^{a+1})-4/p^{a+2}\\
&=1-4/p^{a+1}-4/p^{a+2}.
\end{aligned}
$$

The expression is strictly between 0 and 1 at p>=7 for h!=0.
At h=1, the first cases are

| p | Exact Haar multiplier |
|---:|---:|
| 7 | 17/49 |
| 11 | 73/121 |
| 13 | 113/169 |

At h=7, `m_7(7)=311/343`, confirming the dependence on the actual
Fourier mode's p-valuation. Forcing at p=3 and 5 has colliding simple
poles and a numerator Hensel root; the formula is **NOT** asserted there.

### Independent local controls

The implementation computes the closed formula and a genuinely different
shell-plus-Ramanujan sum and requires *exact Fraction equality*. A third
finite-character oracle enumerates roots of unity over unit groups, marked
numerical rather than an exact certificate; a fourth finite residue
representative sampling of the original source is explicitly noncertifying
near unresolved deep poles. One overambitious early guessed finite
threshold `<1/30` on a ten-prime product was **refuted by the exact
rational product** (~0.03981). The corrected test retains both `>1/30`
and `<1/20` controls; an asymptotic power law is not a ten-prime bound.

## 3. Fixed-prime averages along the ACTUAL integer timeline (JPC-24)

For finite prime set P and h integer, put

$$
B_{N,P}(h)=\frac1N\sum_{n=1}^N\prod_{p\in P}\chi_p(h r(n)).
$$

**Theorem.** If P is finite and consists of distinct primes, then

$$
\boxed{\lim_{N\to\infty}B_{N,P}(h)=\prod_{p\in P}m_p(h).}
$$

For p=3,5, the local mean is defined by its Haar integral and exists;
the explicit JPC-23 formula is used only at p>=7.

**Proof.** Each local rational function `r:Z_p -> Q_p` is continuous
except at finitely many denominator poles. The p-adic additive character
is continuous on Q_p, bounded by 1, so `chi_p(h r(t))` is bounded and
Riemann/Haar integrable on the compact Z_p: the finite singular set has
measure zero. For finite P the product function on `product_(p in P)Z_p`
is similarly integrable. CRT gives exact uniform sampling of every fixed
joint cylinder by the integer sequence n=1,2,...; approximating the
integrable function by cylinder-step functions with arbitrarily small
exceptional pole neighborhoods proves convergence to product Haar. Since
Haar on a finite product is a product measure and every integrand depends
on just its own p-coordinate, the limit factors. QED.

This says fixed-lens local observables equidistribute over their own
proper finite prime domain. It does **not** say the total finite-adelic
source, or the memory-bearing recurrence U_n, has an independent Haar law.

## 4. Prime-cutoff damping with exponent four (JPC-25)

For fixed nonzero integer h and almost all primes p>=7, p does not divide
h, so JPC-23 gives

$$
m_p(h)=1-4/p-4/p^2=1-4/p+O(p^{-2}).
$$

The ratio of this factor to `(1-1/p)^4` differs from 1 by `O(p^-2)`.
Because the product of those ratios converges to a strictly positive
constant and by Mertens' classical theorem,

$$
\boxed{\prod_{7\le p\le X}m_p(h)
\sim\frac{C_h}{(\log X)^4},\qquad C_h>0.}
$$

The finitely many primes dividing h modify only the constant. No false
claim of an `O(X^-4)` bound or a finite-X numerical power law is made.
The exponent 4 records exactly the four nonoverlapping **source poles**.
It is source-specific to this rational forcing, though assembled from
classical Ramanujan/Mertens machinery.

## 5. Noncommuting limits on the actual BBP forcing (JPC-26)

Set

$$
A_{N,X}(h)={1\over N}\sum_{n=1}^N
\prod_{p\le X}\chi_p(h r(n)),
\qquad h\in\mathbb Z\setminus\{0\}.
$$

**Theorem (exact limit-order separation).** For every such h,

$$
\boxed{\lim_{X\to\infty}\lim_{N\to\infty}A_{N,X}(h)=0,}
\qquad
\boxed{\lim_{N\to\infty}\lim_{X\to\infty}A_{N,X}(h)=1.}
$$

**First order.** Fix X and let N tend to infinity. By JPC-24, the
mean equals the product of the finitely many local Haar means. Its
absolute value is at most `product_(7<=p<=X)m_p(h)` (each p=2,3,5
factor has modulus <=1). JPC-25 sends this to zero as X tends to
infinity. No infinite independent Haar state has been asserted to be an
admissible finite adele.

**Second order.** For each fixed source time n, `r(n)` is rational,
with finite denominator prime support. Once X exceeds all its denominator
prime factors, CRT additive characters satisfy

$$
\prod_{p\le X}\chi_p(h r(n))=e(h r(n)).
$$

The authentic forcing satisfies `r(n)>0` and `r(n)<8/n^2`, directly from
its positive numerator and odd-denominator rational product: numerator
`120n^2-89n+16 <120n^2`, denominator is at least
`(n)(3n)(n)(5n)=15n^4`. Consequently `r(n)->0` and
`e(h r(n))->1`. The bounded Cesàro mean therefore tends to 1. In
fact `|N^-1 sum e(hr(n))-1| <32*pi*abs(h)/N`, using
`sum_(n>=1)n^-2<2`, an explicit uniform-in-N budget.

**Important scope:** the surprising 0 vs 1 is a theorem about the
*one-step forcing* along its authentic integer time indices, not a proof
of any normality statement about the accumulated orbit U_n.
It is not a physical Feynman path integral and contains no actual
quantum phase. It is a rigorous warning about exchanging two infinite
observational limits without source admissibility.

## 6. What this makes actionable

We now have a full toy-but-source-authentic cancellation theorem with the
correct inputs and an exactly identified **failure** to transport it to
the object of interest:

- The denominator pole innovations `r(n)` have explicit local Fourier
  damping and CRT factorization on **fixed** prime families.
- The selected source states satisfy `U_n=16U_(n-1)+r(n)`; their local
  characters accumulate historical phases and the clocks
  `ord_(p^k)(16)` share factors. The source statistic we need is
  `sum_(n<N) prod_p chi_p(hU_n)`, NOT `sum_(n<N) prod_p chi_p(h r(n))`.
- The first and second limit orders differ for r, so the local Haar
  product cannot simply be imported as an estimate for U.
- A successful next theorem must control the actual history-dependent
  cross-place covariance (or prove a source-preserving mixing estimate)
  while retaining the authentic integer carry. This is a **probe gap**,
  not lack of a representation and not an established logical boundary.

**Evidence classification:** JPC-23 and JPC-26 are paper-proved with
independently derived exact rational local checks; JPC-24 imports
classical CRT/Haar/Riemann facts; JPC-25 imports classical Mertens. The
claim of a new source-specific `o(N)` estimate for U_n is **UNVERIFIED**.
Scholarly novelty/priority is not independently verified; no Lean proof
was compiled in this round.
