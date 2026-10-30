# Sharp exponential conductor growth on the authentic BBP trajectory

**CG-01/02/03: PROVED LOCAL, classical-paper authority.** CG-01/02 independently re-derived
by the arithmetic, signed-CRT and transfer agents after the root derivation.
The reasoners share model family and source provenance; this is not external
peer review or Lean kernel authority. The prime number theorem in fixed
arithmetic progressions is the only asymptotic external input.

For the unchanged four-pole recurrence with `U_0=0`, let `den(x)` denote the
positive reduced denominator of a rational x. Then, with natural logarithms,

\[
\boxed{\log\operatorname{den}(U_n)=6n+o(n),\qquad
\log\operatorname{den}(U_{n+1}-U_n)=6n+o(n).}\tag{CG-1}
\]

In particular, the **smallest exact translated equally spaced circle grid**
containing both `{U_n}` and `{U_(n+1)}` has

\[
\boxed{q_{\min}(n)=\exp(6n+o(n)).}\tag{CG-2}
\]

This sharpens the explicit finite first-window subproduct with logarithmic
weight `(11/3)n+o(n)` in `transfer/TRANSFER_DOSSIER.md`. That elementary
subproduct remains useful because it has no unspecified large-n threshold.
The present result is a constraint on the actual rational source history,
not a statement about distribution of its real-circle phase.

## 1. Nonvanishing at every fixed compressed packet

Use AT-01 from `arithmetic/ARITHMETIC_THEOREMS.md` with depth a=1. For a prime
p, the condensed offset list is `D=(1,4,5,6)` in classes1/5 and
`D=(2,3,4,7)` in classes3/7. At the end of packet l, its residue is the
condensed prefix `V_l`, with coefficients c' equal respectively to

```
(4,-2,-1,-1), (4,-2,-1,-1), (8,4,4,-1), (-32,-16,-16,4).
```

For `s in D`, put `q=8(l-1)+s` and let
`j_s=(pq+8-(pq mod8))/8` be its actual event time. Define the rational number

\[
H_{l,s}=16V_{l-1}+\sum_{s'\in D,\ s'\le s}
                   \frac{c'_{s'}}{8(l-1)+s'}.
\tag{CG-3}
\]

Provided p exceeds the last condensed denominator in packet l, the
term-by-term AT-01 proof, stopped at `j_s`, gives

\[
16^{M_p(l)-j_s}\,pU_{j_s}\equiv H_{l,s}\pmod p.\tag{CG-4}
\]

Every factor of16 is a unit. Between two successive p-pole events, the
residue propagates by multiplication by16, so it stays nonzero if and only
if the residue at the most recent event is nonzero. Equivalently (CG-4)
holds at a later event-free time n with exponent `M_p(l)-n`; negative
exponents are interpreted as inverses modulo p.

**Every rational H in (CG-3) is nonzero.** In the native classes, the first
coefficient is positive and the remaining three are negative. The partial
forcing sums decrease after the first term to the strictly positive complete
forcing r(l); also `U_(l-1)>=0`. Thus all H are positive. In reflected class3,
the first three coefficients are positive and the last is negative, but
`8/(8l-6)>1/(8l-1)` proves even the complete forcing positive. All H are
positive there too. The class7 list and prefix are exactly minus4 times
class3, so every H is negative. This is a sign proof for all l, not a
numerical assertion about sampled packets.

For any fixed K, take the finite set of prime divisors of numerators and
denominators of every H with `1<=l<=K`, in all four classes. Outside that
finite set, none of the first K packet residues vanishes. This explicitly
retains exceptions such as p=19 and p=73; their cancellation cannot be
discarded at finite times.

## 2. Uniform survival of primes comparable to the current time

Fix `0<epsilon<1` and choose `K=ceil(1/epsilon)+2`. If `p>=epsilon n`, every
quotient of a p-divisible native denominator through time n is at most
`(8n-2)/p<8/epsilon`; therefore at most K condensed packets have been seen.
For all sufficiently large n, such primes satisfy `p>8K+7`, `p^2>8n`, and
lie beyond the finite exceptional set above.

It follows uniformly for all those primes that

\[
p\text{ has been born by time }n\quad\Longrightarrow\quad v_p(U_n)=-1.
\tag{CG-5}
\]

This is the load-bearing step: fixed-packet nonvanishing is used before
taking n to infinity, with epsilon held fixed. The exceptional set can grow
with K, so no effective n-threshold uniform in epsilon is claimed.

## 3. Lower bound and its exact constant

For odd p, first births occur at

```
(p+7)/8 in class1, (p+3)/8 in class5,
(p+1)/4 in classes3/7.
```

Thus the logarithmic weight of born primes is

\[
\theta(8n;4,1)+\theta(4n;4,3)+O(\log n)=6n+o(n).
\]

The O(log n) accommodates the fixed endpoint shifts. The classical
fixed-modulus PNT gives `theta(x;4,1)=theta(x;4,3)=x/2+o(x)`; see
[Bennett--Martin--O'Bryant--Rechnitzer](https://arxiv.org/abs/1802.00085).
Discarding primes below epsilon n costs at most
`theta(epsilon n)=epsilon n+o(n)`. By (CG-5), all remaining born primes
divide the reduced denominator. Hence

\[
\liminf_{n\to\infty}\frac{\log\operatorname{den}(U_n)}n\ge6-\epsilon.
\]

Let epsilon decrease to zero after the liminf. This proves the lower bound6.

For the adjacent difference, use the authentic identity

\[
U_{n+1}-U_n=15U_n+r(n+1).
\]

For p>5 with `v_p(U_n)=-1`, if p divides none of the four native source
denominators at n+1, then r(n+1) is p-integral and the difference also has
valuation -1. The logarithmic weight of the discarded primes is at most
the logarithm of their product, bounded by the product of those four
denominators, hence `O(log n)`. The same lower constant6 follows.

## 4. Upper bound

Each reduced denominator divides the least common multiple of the native
source denominators through n (or n+1 for the difference), because all radix
multipliers and coefficients are integers. Any prime p with exponent1 in
that LCM must have been born. For `p>4n+O(1)`, only its first multiple could
be a native denominator, so only p=1 or5 mod8 is possible. Thus the
first-power logarithmic contribution is at most

\[
\theta(8n+O(1);4,1)+\theta(4n+O(1);4,3)=6n+o(n).
\]

Additional prime powers involve only `p<=sqrt(8n+O(1))`. Their total logarithmic
weight is at most `pi(sqrt(8n+O(1))) log(8n+O(1))=O(sqrt(n) log n)=o(n)`.
The prime2 contributes O(log n) at worst; in fact the combined authentic
source and every U_n are 2-integral. This proves the matching upper bound.

Finally, subtracting two coordinates in a translated q-grid shows that
`q(U_(n+1)-U_n)` must be an integer. Conversely the grid translated to
`{U_n}` with q equal to the difference's reduced denominator contains both
points. Therefore q_min is exactly that denominator, proving (CG-2).

## 5. Fixed-filter dichotomy (CG-03)

Let E denote the forward shift and fix an integer polynomial
`P(z)=sum_(j=0)^d c_j z^j`. The polynomial is fixed before n tends to infinity.
Then

\[
\boxed{
\begin{array}{ll}
P(16)\ne0 &: \log\operatorname{den}(P(E)U_n)=6n+o(n),\\
P(16)=0 &: \log\operatorname{den}(P(E)U_n)=O_P(\log(n+2)).
\end{array}}
\tag{CG-6}
\]

Indeed, iterate the authentic recurrence a fixed j steps to obtain

\[
P(E)U_n=P(16)U_n+F_P(n),\qquad
F_P(n)=\sum_{j=0}^d c_j\sum_{t=1}^j16^{j-t}r(n+t).
\]

The rational function F_P has a denominator dividing the product of the four
source denominators at each of n+1,...,n+d. Its denominator is at most a
constant times `(n+d)^(4d)`. If P(16)=0, this proves the second assertion,
including P=0 with den(0)=1. Otherwise exclude the fixed primes dividing
P(16) and the primes in that source-denominator product. The latter cost
O_P(log n) in logarithmic weight. Every other comparable born prime from
(CG-5) has valuation -1 in P(E)U_n. The lower-bound proof is therefore
unchanged. Its denominator divides the source LCM through n+d, giving the
matching upper bound. This also applies to fixed rational coefficients after
clearing one fixed integer denominator.

For every fixed integer lag ell>=1, take `P(z)=z^ell-1`. Thus
`log den(U_(n+ell)-U_n)=6n+o(n)` and the smallest exact translated grid for
that pair has the same exponential rate. By contrast `(E-16)U_n=r(n+1)`
has a polynomial denominator. This is an arithmetic dichotomy at the radix
eigenvalue, not a mixing or Fourier estimate on the real circle. No uniform
statement for growing degree, lag, or n-dependent coefficients is claimed.

## Consequences and limitations

The exact-grid Stoneham budget obstruction TR-03 strengthens accordingly:
for any fixed `0<c<6`, all sufficiently late consecutive pairs require at
least `exp(cn)` grid sites. A total grid budget O(N) then forces a cut at
every edge after O(log N), and the per-block boundary budget is
`N-O(log N)`, not o(N). This excludes that exact natural-surrogate
certificate even when the partition and grid translations depend on N.

Approximate grids remain outside this theorem. So do signed weights,
source-derived cofiber cancellation and direct interval occupancy estimates.
Large denominator is compatible with proximity to any real phase. The
published null-source control AT-07 has zero initial seed, unbounded depth
at every odd prime, and coherent characters; it differs from BBP's forcing.
Fixed rational seed translations preserve the large-prime proof as well.
No source uniqueness or normality is inferred from conductor growth.

**Next falsifiable arithmetic obligation:** establish the actual primary/
complement lag-one lower bound SC-06, or another full signed bound on those
selected windows. The current conductor proof supplies no bound on that
signed interaction. Pi normality and RH remain OPEN.
