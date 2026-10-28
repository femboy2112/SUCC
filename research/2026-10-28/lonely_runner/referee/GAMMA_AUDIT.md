# Referee audit: unrestricted two-entry growth

Audit base: `27af9600ddd8acacea7a1822921083821c5dbf6e`, 2026-10-28.
Status: paper proof and dependency audit; no new kernel authority is asserted.
The writer also participated in the preceding campaign. This is a hostile
reinspection with changed proof dependencies, not a blind external review.

## 1. Exact target and verdict

Let `n>=5`, `1<=r1<r2<n`, `n<=w1<w2` be integers, with zero shifts, and set
`S={1,...,n-1}\{r1,r2}`. Write `||x||=min_{k in Z}|x-k|` and
`LR(V)=max_{t in [0,1]} min_{v in V}||vt||`.

The dangerous premise in GAMMA-05 is

\[
 \forall w\ge n,\qquad LR(S\cup\{w\})>1/n.                 \tag{H}
\]

**Verdict: SURVIVES, with a smaller dependency set.** Sections 2--5 below
prove (H) directly under the negated hypothesis of coverage. They never infer
coverage classification from a theorem stated only for equality. They need
neither the Goddyn--Wong theorem, Liu's exact-value theorem, Kanold's bound,
the externally accepted two-entry classification, nor the general Lonely
Runner Conjecture.

The middle and speed-two interval geometry is adapted from Zhang's primary
proof, rather than claimed as an independent conceptual discovery. New in this
audit is its explicit coverage-only formulation, a short elementary replacement
for the Jacobsthal input, and a rational witness eliminating the remaining
sporadic case without any multiplicative classification. Sections 7--8 give
a quadratic bound for every deleted pair. This has a complete paper proof
and same-model internal algebraic corroboration; it is not an externally
reviewed result or a certified academic-priority claim.

## 2. An elementary gap between units

For `r>=2`, every interval of `floor(r/2)+1` consecutive integers contains an
integer coprime to r. Equivalently, the maximum cyclic gap between consecutive
units modulo r is at most `floor(r/2)+1`.

This is exactly Goddyn--Wong's Lemma 2.1, not a new bound. The following
explicit-unit proof replaces their use of Bertrand's postulate. See
[PRIMARY_PRIORITY.md](PRIMARY_PRIORITY.md) for the original PDF receipt.

Here is a finite symbolic proof, not a bounded scan. For odd `r=2q+1`, use the
units `1,q,q+1,2q`. For `r=4h`, use `1,2h-1,2h+1,4h-1`. For `r=4h+2`, `h>=1`,
use `1,2h-1,2h+3,4h+1`. Repeated entries are discarded. Their cyclic gaps are,
respectively, bounded by

\[
 \max(q-1,2),\quad \max(2h-2,2),\quad \max(2h-2,4).
\]

Every listed number is a unit: in the even cases its gcd with r divides 2 or
4 and the listed number is odd. The inequalities with `floor(r/2)+1` follow
immediately; r=2 has the single unit 1 and cyclic gap 2. An interval between
two consecutive listed units contains at most gap-minus-one nonunits.

For `r>=7` the same proof gives the stronger bound

\[
 j(r)\le r/2-1,                                            \tag{U}
\]

where j(r) denotes the least length that always contains a unit. For
`r=1,...,6`, the exact values are `1,2,2,2,2,4`. This elementary estimate is
much weaker asymptotically than known Jacobsthal estimates, but sufficient
for the present arguments. No novelty is claimed for the unit-gap observation.

## 3. A coverage-only exclusion of middle removals

Fix `3<=r<=(n-1)/2`, write `s=n-r`, and let
`T=({1,...,n-1}\{r}) union {w}`, where `w>=n`.
For a nonzero residue x modulo r, let F(x) be its largest representative in
`[s,n-1]`. Put

\[
 I=\min\{i\ge s:\gcd(i,r)=1\}=s+d.
\]

The block `[s,n-1]` has r consecutive integers, so all these representatives
exist and `I<=n-1<2s`. Section 2 gives `d<=floor(r/2)`.

### Safe windows, with proof of their actual source meaning

For every unit p modulo r, let a be its inverse modulo r. The two intervals

\[
 L_p=\left({p\over r}-{s\over rnF(a)},
                 {p\over r}-{1\over2rn}\right),\qquad
 R_p=\left({p\over r}+{1\over2rn},
                 {p\over r}+{s\over rnF(-a)}\right)          \tag{W}
\]

are safe for every speed in `{1,...,n-1}\{r}` at radius `1/n`.
Only this inclusion is needed; an exact description of the entire safe region
is unnecessary here.

For example, write a time in `R_p` as `p/r+u`. Then
`1/(2rn)<u<s/(rnF(-a))<=1/(rn)`. For every retained multiple `kr`, k>=2,
`kr*u>1/n`, and `kr*u<1/r<=1/3`, so its circle distance exceeds `1/n`.
For a nonmultiple i, the residue of ip modulo r is rho in `{1,...,r-1}`.
If rho=r-1, then i<=F(-a), and
`1/r-i*u>1/r-s/(rn)=1/n`. For all other residues, the representative
`rho/r+i*u` stays strictly between `1/n` and `1-1/n`: its lower bound is
`1/r`, and its upper bound is less than `(r-1)/r`. This proves the right
window; reflection gives the left one. All displayed windows are nonempty
because their F-values are at most `n-1<2s`.

As p runs through units, the values F(-a) include I. Thus at least one safe
window has length

\[
 \ell={2s-I\over2rnI}.                                    \tag{W1}
\]

### Arithmetic estimate

We claim

\[
 {4rI\over2s-I}<r(n-2).                                   \tag{W2}
\]

After writing I=s+d and multiplying positive denominators, this is exactly
`d<s(n-6)/(n+2)`. For r>=6, both positive factors on the right are increasing
with n>=2r+1, and

\[
 {s(n-6)\over n+2}\ge{(r+1)(2r-5)\over2r+3}>{r\over2}\ge d.
\]

The strict inequality is equivalent to
`2r^2-9r-10=(r-6)(2r+3)+8>0`. For r=4,5 the exact unit-gap values give d<=1,
while the right side is already respectively `15/11` and `30/13` at the
smallest n. For r=3, d=0 at n=7,8; for n>=9 it is at most 1 and the right
side is at least `18/11`. This proves (W2) in every case.

### Contradiction under coverage alone

Suppose `LR(T)<=1/n`. Every window in (W), including its closure by continuity,
must lie in the bad set of w. Its distinct bad bands have length `2/(nw)` and
positive separating gaps. A connected window must therefore lie in one band.
Equation (W1) gives `w<=4rI/(2s-I)`, hence `w<r(n-2)` by (W2).

Write `w=Kr+c` with `-r/2<c<=r/2`, and put `F_+=F(1)`, `F_-=F(-1)`.
The closed right window at p=1 is covered by a band centered at j/w only if

\[
 {c\over r}+{ws\over rnF_-}-{1\over n}
 \le j-K\le
 {c\over r}+{w\over2rn}+{1\over n}.                       \tag{W3}
\]

An integer `j-K>=1` would force
`c>=r-w/(2n)-r/n>r/2`; an integer `j-K<=-1` would force
`c<=-r+r/n-ws/(nF_-)<-r/2`. Thus `j-K=0`, implying

\[
 c\le {r\over n}-{ws\over nF_-}<0.                        \tag{W4}
\]

The last inequality follows from `ws>=ns>r(n-1)>=rF_-`.
For the left window the corresponding integer bounds are

\[
 {c\over r}-{w\over2rn}-{1\over n}
 \le j-K\le {c\over r}-{ws\over rnF_+}+{1\over n}.
\]

The same exclusion of nonzero integers gives
`c>=ws/(nF_+)-r/n>0`, contradicting (W4). We have proved

\[
 LR(T)>1/n\quad(3\le r\le(n-1)/2)                         \tag{M}
\]

directly. No lower bound for arbitrary runner sets, and no equality
classification, occurred in the argument.

## 4. The remaining small-removal cases

If r=1, the interval `(1/(2n),1/n)` is safe for every speed `2,...,n-1`.
Its length `1/(2n)` is greater than `2/(nw)` for w>=n>=5. It cannot fit in one
w-band, so the one-entry set does not cover. This also directly proves (H)
whenever 1 is among the two deletions.
This interval argument is already in Goddyn--Wong's Theorem 2.3 proof.

For r=2, two safe intervals occur around 1/2. The left one is

\[
 (1/2-\beta,1/2-1/(4n)),\quad
 \beta=\begin{cases}1/(2n)&n\text{ odd},\\
 (n-2)/(2n(n-1))&n\text{ even}.
 \end{cases}                                              \tag{S}
\]

To check this directly, write t=1/2-u. Every even retained speed is at least
4 and has distance vu in `(1/n,1/2)`. Every odd speed has distance `1/2-vu`,
bounded below using the largest odd speed, n-2 or n-1. Both bounds are strict
for u in the stated interval.

If the left shell is covered by one w-band with center c and halfwidth
`h=1/(nw)`, its center must be below 1/2. The largest center below 1/2 is
`1/2-1/w` for even w, or `1/2-1/(2w)` for odd w. Reaching the right shell
endpoint therefore forces respectively `w>=4(n-1)` or `w>=2(n-2)`.
Its length forces `w<=8` for odd n and `w<=8(n-1)/(n-3)` for even n.
Even w is impossible for n>=5. Odd w leaves only `(n,w)=(5,7)` or
`(6,9),(6,11),(6,13)`. The exact time 87/200 excludes the last two: the
distances for speeds `1,3,4,5,11,13` are respectively
`87,61,52,35,43,69` divided by 200, all strictly above 1/6.

Consequently a one-entry cover with r=2 can only have `(n,w)=(5,7)` or `(6,9)`.
Their actual tightness is not needed for this necessity statement.

## 5. Complete elementary proof of the one-insertion hole

Suppose `LR(S union {w})<=1/n`. Adding either removed speed shows that both
one-entry sets obtained by deleting r1 or r2 cover.

If either deletion is 1, Section 4 contradicts this. If either is between
3 and `(n-1)/2`, Section 3 contradicts it. If one deletion is 2 in the lower
half, Section 4 leaves just the two sporadic parameter pairs:

* n=5,w=7: the other deletion is 3 or 4. At its center 1/r the retained
  speeds and w all have distance at least 1/r>1/5, because r does not divide 7.
* n=6,w=9: the other deletion is 3,4, or 5. Centers exclude 4 and 5. For
  the deletion pair {2,3}, the retained-plus-inserted speeds are {1,4,5,9};
  at t=13/36 their distances are respectively 13,16,7,9 divided by 36.
  Their minimum 7/36 is strictly greater than 1/6.

Only the case `2r1>n-1` remains. At t=1/r_i every retained baseline speed
has distance at least 1/r_i>1/n. Unless r_i divides w, this center is itself
a hole. Otherwise write `w=m*r1=l*r2`, with positive integers m>l. Then

\[
 m r_1=l r_2\le(m-1)(n-1),\qquad
 m(n-r_1)\ge n-1+m\ge n+1.
\]

Put `u=(n+1)/(n^2*w)` and `t=1/r1+u`. The preceding inequality implies

\[
 u<{n-r_1\over n r_1(n-1)}.
\]

The circle-distance triangle inequality now keeps every retained baseline
speed strictly above `1/r1-(n-1)u>1/n`. For the inserted speed,
`wt` is congruent to `(n+1)/n^2`, which lies strictly between `1/n` and
`1-1/n` for n>=5. This is a rational hole, contradicting coverage.

All cases have been exhausted. This proves (H). In the middle cases the
failure of coverage occurs in an open set; the actual rational band endpoints
also give a rational witness if one is required. This proof uses no primitive
gcd-one assumption on the speed set.

## 6. Quantitative audit of GAMMA-05

The original source-endpoint and periodic-occupancy arguments survive.
If a gap after one insertion has endpoints `(nk+eps)/(nv)` with eps=+-1,
their positive difference is an integer divided by `nuv`, not `n^2uv`.
There is only one inserted velocity, so different-label endpoints give
length at least `1/[n*w1*(n-1)]`; same-label endpoints give at least
`1/(n*w1)`. Coverage by w2 alone forces the connected gap into one w2-band,
whence `w2<=2(n-1)w1`. Equality in the length comparison cannot be discarded.

For any real interval J of length ell and any positive w, put alpha=2/n and
write `w*ell=m+u`, 0<=u<1. Full periods contribute alpha; the remaining arc
intersects the bad arc in length at most `min(u,alpha)`. Therefore

\[
 |J\cap B_w|\le {2\ell\over n}+{2(n-2)\over n^2w}.         \tag{P}
\]

The excess is bounded by `min(u,alpha)-alpha*u<=alpha(1-alpha)`. A complete
bad band attains the additive constant. Thus dropping the boundary term is
false, and the constant is sharp for phase-uniform additive discrepancy.

If J is baseline-safe, its coverage by the two inserted speeds gives

\[
 \ell(1-4/n)\le {2(n-2)\over n^2}(1/w_1+1/w_2)
             < {4(n-2)\over n^2w_1}.                      \tag{P2}
\]

The final strictness uses distinctness `w2>w1`; division requires n>4.
For a baseline-safe point of height mu>1/n, the `(n-1)`-Lipschitz bound
supplies an open safe interval of length `2(mu-1/n)/(n-1)`. Hence

\[
 w_1<{2(n-2)(n-1)\over n(n-4)(\mu-1/n)}.                  \tag{P3}
\]

This verifies the parameter-dependent constant and the original cubic
consequence. The safe interval cannot meet an integer because all baseline
speeds vanish there. Its use requires only a lower bound for mu, not an exact
global maximization formula.

## 7. Elementary quadratic bound with a lower-half deletion

**Theorem.** Under the assumptions in Section 1, suppose `2r1<=n-1` and
`LR(S union {w1,w2})<=1/n`. Then

\[
                 w_1<14n,\qquad w_2<28n(n-1)<28n^2.       \tag{Q}
\]

This covers every pair with at least one lower-half removal, since r1<r2.
It does not establish (Q) for two upper-half removals.

**Proof.** Let D be the least integer >=n+r1 coprime to r1. At a modular
inverse time `t=a/D`, `a*r1=1 mod D`, every retained baseline speed has
distance at least 2/D: residues 0 and +-1 would force i=0, r1, or
`i>=D-r1>=n`. Thus mu>=2/D. This is a direct rational witness and does not
require Liu's exact upper-bound theorem.

For r1>=7, (U) gives
`D<=n+r1+j(r1)-1<=n+3r1/2-2<=(7n-11)/4`.
For r1<=6, the exact small unit-gap values give the same inequality except
at the following five pairs. Their actual least D and the bound (P3) are:

| (n,r1) | D | resulting strict upper bound for w1 |
|---|---:|---:|
| (5,2) | 7 | 56 |
| (6,2) | 9 | 60 |
| (7,3) | 10 | 50 |
| (10,4) | 15 | 72 |
| (14,6) | 23 | 3588/25 |

Each is less than 14n. To see that the table exhausts the small cases,
the crude bounds `D<=n+r1+j(r1)-1` imply the desired inequality respectively
for n>=5,8,9,11,12,16 when r1=1,...,6. The remaining admissible n are
5,6,7 for r1=2; 7,8 for r1=3; 9,10 for r1=4; 11 for r1=5; and 13,14,15
for r1=6. Direct gcds give exactly the five exceptions listed.

In all nonexceptional cases,

\[
 \mu-1/n\ge {n+11\over n(7n-11)}.
\]

Substitute into (P3). The resulting bound
`2(n-2)(n-1)(7n-11)/[(n-4)(n+11)]` is less than 14n because

\[
 7n(n-4)(n+11)-(n-2)(n-1)(7n-11)
 =81n^2-355n+22
 =81(n-5)^2+455(n-5)+272>0.
\]

Section 5 supplies the actual hole after w1. Section 6 then gives
`w2<=2(n-1)w1<28n(n-1)`. This proves (Q). No whole-range finite search or
unreplayed external classification is a premise.

## 8. A quadratic bound for every deleted pair

**Theorem (Q-all).** For all the integers in Section 1,

\[
 LR(S\cup\{w_1,w_2\})\le1/n\quad\Longrightarrow\quad
                         w_2<28n^2.                       \tag{Q-all}
\]

There is no upper-half restriction, primitive normalization, assumed
matching between deletions and insertions, or conjectural premise.
Section 7 proves this when `2r1<=n-1`. Assume henceforth both removals
are in the upper half.

First, (P3) at the safe center 1/r1, with mu=1/r1, gives

\[
 w_1<{2(n-2)r_1(n-1)\over(n-4)(n-r_1)}
 \le{(n-2)^2(n-1)\over n-4}<2n^2.                         \tag{Q0}
\]

Here r1<=n-2, and the final strict inequality follows from
`2n^2(n-4)-(n-2)^2(n-1)=(n-5)(n^2+2n+2)+14>0`.

### Unit-center lemma

If positive integers r,a satisfy r does not divide a, there exists a unit
p modulo r with

\[
                         \|ap/r\|\ge1/6.                  \tag{UC}
\]

Put g=gcd(a,r), q=r/g>1. A unit b modulo q with `||b/q||>=1/6` is explicit:
use b=1 for q=2; b=(q-1)/2 for odd q; b=q/2-1 for q divisible by 4; and
b=q/2-2 for q=2 mod 4 with q>=6. Coprimality follows because the relevant
gcd divides 1, 2, or 4 and b is odd in the even-modulus cases. The minimum
is attained at q=6, so the constant cannot be increased universally.

The map from units modulo r to units modulo q is onto. For completeness,
start with a prescribed unit c modulo q. For each prime dividing r but not
q, prescribe p=1 modulo that prime; together with p=c modulo q these
conditions have a simultaneous solution by the elementary Chinese remainder
theorem. It is divisible by no prime factor of r. Choose
`c=b*(a/g)^(-1) mod q`; then `ap/r` is congruent to b/q, proving (UC).

### Case A: the first insertion misses a removed divisor

Suppose r is either removed speed and r does not divide w1. Choose p from
(UC), with 0<p<r, and put t0=p/r. Since r is upper-half and p is a unit,
all retained baseline distances at t0 are at least 1/r.
For n>=7 put

\[
 A={n-r\over nr(n-1)},\qquad
 R=\min\left(A,{n-6\over6nw_1}\right)>0.
\]

Every retained baseline speed and w1 has distance strictly greater than 1/n
throughout `(t0-R,t0+R)`, by the circle-distance triangle inequality.
This interval stays in (0,1), since R<=A<1/r.

Final coverage forces w2 to cover this entire connected interval. At its
center, w2 must have distance at most 1/n. That distance is an integer
multiple of 1/r, and 1/r>1/n, so r divides w2. Thus its covering band is
centered exactly at t0. Containment gives `R<=1/(nw2)`, hence

\[
 w_2\le\max\left({r(n-1)\over n-r},{6w_1\over n-6}\right)
       <12n^2.                                           \tag{QA}
\]

The first term is at most `(n-1)^2<n^2`; the second is strictly below
`12n^2/(n-6)<=12n^2` by (Q0). This reasoning does not suppose that the
two removed speeds have distinct assigned covering runners.

### Case B: the first insertion is a common multiple

Suppose both r1 and r2 divide w1. Write `w1=m*r1=l*r2`, so m>l and
`m(n-r1)>=n-1+m`, as in Section 5. Put

\[
 A={n-r_1\over nr_1(n-1)},\quad h={1\over nw_1},\quad
 I=\left({1\over r_1}+h,
          {1\over r_1}+\min\left(A,{n-1\over nw_1}\right)\right).
\]

All retained baseline speeds are safe on I. The lower and upper endpoints
place I strictly after the central w1-band and before the next w1-band.
Moreover

\[
 A-h={m(n-r_1)-(n-1)\over nw_1(n-1)}
      \ge{1\over nr_1(n-1)},
\]

so I has positive length at least

\[
 \min\left({1\over nr_1(n-1)},{n-2\over nw_1}\right).
\]

It must fit inside a single w2-band. Therefore

\[
 w_2\le\max\left(2r_1(n-1),{2w_1\over n-2}\right)<2n^2, \tag{QB}
\]

where (Q0) and n>=5 justify the last inequality. In particular, the upper
endpoint of I explicitly prevents crossing a subsequent w1 bad band.

For the remaining upper-half sizes n=5,6, use Section 5's genuine hole,
Section 6's endpoint bound, and (Q0):
`w2<=2(n-1)w1<4(n-1)n^2<=20n^2<28n^2`.
Together with (QA), (QB), and the lower-half theorem this exhausts all
cases and proves (Q-all).

**Improvement boundary.** The exponent is reduced from three to two by a
paper proof using source arithmetic. The constant 28 is not claimed sharp.
The reduction to units and the near-half representatives are elementary
number theory; their particular use here has not received external priority
certification. Neither the accepted upper-half classification nor Zhang's
growth bound for multiplicative modifications is a dependency.

## 9. Proof authority, hostile controls, and remaining obligations

* Zhang's middle windows and shell are shared mathematical provenance.
  Independent re-expression of their hypotheses is not independent discovery.
* The unrestricted hole proof and (Q) above are paper proofs. Prior Lean
  exports for the upper-half hole do not automatically formalize them.
* The phases must remain zero. Arbitrary shifted bands destroy the center
  divisibility and the integer source-endpoint numerator used here.
* The nonprimitive tight set `{2,4,6,8}` at n=5 must survive; no normalization
  to gcd one is allowed to change the baseline.
* The known n=8 pair R={2,3}, W={11,13} must survive (Q). It prevents an
  unjustified extension of upper-half divisibility to all removed speeds.
* A proposed direct proof using only a universal long baseline gap fails:
  at n=24, R={10,22}, exact band union gives maximum gap 1/684, less than
  2/n^2. This is a finite counterexample to that proposed shortcut, not to (H).
* Equation (Q-all) is the new unrestricted exponent improvement on paper.
  It does not imply an O(n log n) bound, a classification, or a new tight
  configuration. Same-model checks are not independent external review.

Next falsifiers: exact replays of all small unit-gap exceptions; a separate
derivation of the middle-window integer exclusions at c=r/2; strict constant
mutations; and kernel formalization of the unrestricted rational hole.
