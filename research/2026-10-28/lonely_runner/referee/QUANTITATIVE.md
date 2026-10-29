# Quantitative refinements and limits of the geometric ingredients

Status: CORROBORATED paper derivations with exact hostile tests. Their formal
subsets are identified separately in ../GROWTH_KERNEL.md. These refinements do
not assume a general Lonely Runner lower bound or the earlier external
upper-half classification. Academic novelty remains UNVERIFIED.

Let n>=5, let S=[n-1] minus two distinct speeds r<s, and let n<=u<v.
Assume the unshifted source S union {u,v} covers the circle at radius 1/n.
Write M=max(S), and let mu be any attained lower bound greater than 1/n
for the retained-source minimum. The rational inverse/center witnesses in
the companion manuscript supply such a bound. Set

\[
 \ell=2(\mu-1/n)/M.
\]

The M-Lipschitz inequality gives an open S-safe interval J of length ell.
It cannot wrap past an integer: S is nonempty and its minimum vanishes there.

## 1. A two-band interval bound without measure theory

For any real open interval J covered by the two periodic bad sets B_u,B_v,
where 0<delta=1/n<1/4 and 0<u<v,

\[
 |J|\le 2\delta/u+4\delta/v<6\delta/u.             \tag{T}
\]

Indeed, suppose J meets two distinct closed u-bands. It then contains the
entire intervening open good gap, of length at least (1-2delta)/u.
That gap must be covered by B_v alone, so connectedness forces it into one
v-band of length 2delta/v. But (1-2delta)/u>2delta/v for delta<1/4 and v>u,
a contradiction. Thus J meets at most one u-band. If it meets none, it lies
in one v-band. Otherwise deleting its intersection with the one u-band
leaves at most two open tails, each lying in a single v-band. The lengths
of that band and the two tails give the non-strict inequality in (T).
Taking limits at endpoints is legitimate because the covering bands are
closed. The final strict inequality follows from v>u.

Applied to the safe interval above, this proves

\[
 u<\frac{3M}{n\mu-1}.                              \tag{T1}
\]

The periodic-density argument independently proves

\[
 u<\frac{2(n-2)M}{n(n-4)(\mu-1/n)}.                \tag{T2}
\]

Taking the smaller bound is justified. The two-band argument is stronger
for n=5,6,7, equal at n=8, and weaker for n>8. Neither proof requires an
exact global value for mu. In the implementation the classical deletion
formula chooses a convenient certified height, but is not a premise of
the elementary lower-bound argument.

## 2. An improved unconditional constant

The source-labelled gap theorem, together with the unrestricted
one-insertion hole proved in GAMMA_AUDIT.md, gives

\[
 v\le 2Mu\le2(n-1)u.                              \tag{E}
\]

**Theorem.** Every source in the stated domain satisfying the covering
hypothesis obeys

\[
                         v<2n^3.                 \tag{C}
\]

For n>=7, the elementary deletion witness has height at least 1/(n-2),
so (T2), with M<=n-1, gives the original B_n. Its stronger comparison is

\[
 n^3(n-4)-(n-2)^2(n-1)^2
   =(n-6)(2n^2-n+6)+32>0.
\]

Thus (E) already gives v<2n^3 in this range.

For n=5 the retained source has height at least 2/7. Formula (T1) gives
u<28, and (E) gives v<224<250. For n=6 there are two cases. If speed 5 is
deleted, M<=4; height 2/9 and the weaker M<=5 version of (T1) give u<45,
hence v<8*45=360<432. If speed 5 is retained, both deletions are in {1,2,3,4}.
Their one-deletion heights are 2/7,2/9,1/3,1/4. At least one deleted label
differs from 2, so the retained height is at least 1/4. Formula (T1) gives
u<30 and (E) gives v<300<432. This proves (C).

The original B_5=56 and B_6=60 remain valid; (T1) improves them to 28 and
45 even before the source-specific M refinement. Strict integer enumeration
must use ceil(B)-1, including when B is integral.

## 3. Exact arithmetic of oriented endpoint labels

The left endpoint of a residual gap is the right endpoint of a source band;
the right endpoint is a left endpoint. If their velocities are u,v and
windings k,l, then

\[
 b-a=\frac{n(lu-kv)-u-v}{nuv}>0.                    \tag{A}
\]

For u!=v put g=gcd(u,v), and let c be the representative in {1,...,n} of
-(u/g+v/g) modulo n. The numerator in (A) is g times a positive integer
congruent to c modulo n. Therefore

\[
 b-a\ge\frac{gc}{nuv}.                            \tag{A1}
\]

For u=v, positivity forces l-k>=1 and gives the sharper

\[
 b-a\ge\frac{n-2}{nu}.                            \tag{A2}
\]

These are bounds for actual *oriented* source endpoints. They do not prove
the existence of a residual gap, nor do they apply to the two endpoints of
one bad band. Swapping that orientation is refuted by its width 2/(nu),
which is smaller than (A2) for n>=5. The arithmetic improvements can be
used as pruning conditions when the actual labels are known. They do not
uniformly improve the exponent because c may equal one.

## 4. Sharp ingredients do not make the whole theorem sharp

The additive periodic-occupancy correction 2(n-2)/(n^2u) is attained by
J=[-1/(nu),1/(nu)], one complete bad band. Omitting it is false.

The generic endpoint numerator one is attained algebraically for every
n>=3 by velocities u=n-1, v=n(n-2), k=0,l=1. These two bands have the gap
1/[nuv], and no other band of these two velocities covers its interior.
This is an actual two-source gap. It is **not** a complete retained-baseline
example: lower baseline velocities can fill it. It demonstrates sharpness
of the isolated endpoint lemma only, not sharpness of the cubic theorem.

Likewise the n=24 deletion pair {10,22} has longest retained-source gap
1/684<2/n^2. This refutes a proposed universal 2/n^2 safe interval, not an
improved speed exponent by a different argument. The lower-half quadratic
bound in GAMMA_AUDIT.md instead uses a smaller explicit constant and all
parameter cases, giving u<14n and v<28n(n-1).

## 5. Executed checks and next discriminator

`lonely_runner_referee_bounds.py` constructs explicit coprime witnesses
without importing the exact deletion-value routine. Separate exact tests
check the metric of every retained speed, the cyclic unit gaps, the oriented
integer-endpoint formula, complete two-source interval unions, sharp occupancy,
and strict ceilings. Formula computation alone is not universal proof authority.

The subsequent unit-center argument in GAMMA_AUDIT.md proves the unrestricted
quadratic bound without the unreplayed external classification. The remaining
exponent target is a subquadratic bound or a complete classification. Neither
follows merely because the isolated estimates here are sharp or the finite
census finds only small speeds.
