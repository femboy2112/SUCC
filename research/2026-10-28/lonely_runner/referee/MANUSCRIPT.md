---
title: A quadratic speed bound for two-entry modifications of the Lonely Runner baseline
date: 28 October 2026
geometry: margin=1in
fontsize: 11pt
---

## Abstract

Let $n\ge5$, remove two distinct integers from $1,\ldots,n-1$, and insert
two integers $n\le w_1<w_2$. We prove that if the resulting unshifted runner
set covers the circle at radius $1/n$, then $w_2<28n^2$. Thus every tight
two-entry modification belongs to an explicit finite search domain, without
a restriction on the removed speeds or a primitivity assumption. The proof
first shows, by elementary interval arguments, that two deletions followed
by one insertion always leave a strict hole. Rational endpoints and periodic
occupancy then control the inserted speeds. For upper-half deletions, a unit
residue at a removed-speed center gives a stronger arithmetic bound; a separate
argument handles an insertion divisible by both removed speeds. The middle
windows come from Zhang's one-entry analysis, and the unit-gap estimate is
due to Goddyn and Wong. All necessary ingredients are proved here. Exact
computations subsequently classify this family through $n=30$. The universal
quadratic theorem is a paper proof; the computational and formal evidence
have separate, explicitly limited scopes.

## 1. Statement and relation to prior work

For a finite nonempty set $V$ of positive integers, put

\[
 \operatorname{LR}(V)=\max_{t\in[0,1]}\min_{v\in V}\|vt\|,
 \qquad \|x\|=\min_{k\in\mathbb Z}|x-k|.
\]

We call $V$ a cover at radius $1/n$ if

\[
 \forall t\in\mathbb R\quad \exists v\in V:\quad \|vt\|\le1/n.
\]

By continuity and periodicity this is equivalent to
$\operatorname{LR}(V)\le1/n$. Tightness means equality. Throughout the paper,
all starting shifts are zero, and $[n-1]=\{1,\ldots,n-1\}$.

**Theorem 1.** Let $n\ge5$, $1\le r_1<r_2\le n-1$, and
$n\le w_1<w_2$ be integers. Set

\[
 S=[n-1]\setminus\{r_1,r_2\},\qquad V=S\cup\{w_1,w_2\}.
\]

If $\operatorname{LR}(V)\le1/n$, then

\[
                         w_2<28n^2.                       \tag{1}
\]

When $2r_1\le n-1$, the more precise bounds

\[
                 w_1<14n,\qquad w_2<28n(n-1)              \tag{2}
\]

hold. When both removals are upper-half and $n\ge7$, we obtain
$w_1<2n^2$ and $w_2<12n^2$.

Zhang [1] classifies one-entry modifications and asks for polynomial growth
bounds for more general modifications. His interval windows supply an important
part of our proof. We formulate their consequences directly for coverage,
rather than inferring a coverage theorem from a statement about equality.
Goddyn and Wong [2] proved the elementary unit-gap bound used below and
classified multiplicative one-entry modifications. Liu [3] determined the
corresponding one-deletion values; here only a directly proved modular lower
witness is needed.

A previously accepted formal proof [4] gives a stronger classification when
both removals are upper-half. Its interfaces were inspected but its complete
proof was not replayed locally. The present proof does not depend on it.
General geometric finite-checking results [5,6] provide broader context;
they do not directly yield the unconditional bound (1) for this source family.
Academic priority of the unrestricted consequence in Theorem 1 remains under
review. No general Lonely Runner Conjecture or classification for all $n$
is asserted.

## 2. Two elementary tools

Write $B_w=\{t:\|wt\|\le1/n\}$. Its connected components on the real line
are the disjoint closed intervals

\[
 \left[{k\over w}-{1\over nw},{k\over w}+{1\over nw}\right],
 \qquad k\in\mathbb Z.                                  \tag{3}
\]

Every connected interval contained in $B_w$ lies in one such band. If all
retained speeds are strictly outside their bad sets on an interval, coverage
forces the inserted speeds to cover that interval.

**Lemma 2 (unit gaps).** Every interval of
$\lfloor r/2\rfloor+1$ consecutive integers contains an integer coprime
to $r\ge2$. If $r\ge7$, the least such guaranteed length $j(r)$
satisfies $j(r)\le r/2-1$.

*Proof.* For odd $r=2q+1$, consider the units
$1,q,q+1,2q$. For $r=4h$, use $1,2h-1,2h+1,4h-1$. For
$r=4h+2\ge6$, use $1,2h-1,2h+3,4h+1$. Discard repetitions.
Their maximum cyclic gaps are respectively bounded by

\[
 \max(q-1,2),\qquad \max(2h-2,2),\qquad \max(2h-2,4).
\]

The listed integers are coprime to $r$; in the even cases their gcd with
$r$ divides 2 or 4 and they are odd. The asserted estimates follow.
For $r=2$ the unique unit has cyclic gap 2. Between consecutive listed
units there are gap-minus-one consecutive nonunits. $\square$

The first assertion is Goddyn--Wong's Lemma 2.1 [2]. The explicit unit
construction above replaces their use of Bertrand's postulate. We will also
use the exact small values

\[
                  j(1),\ldots,j(6)=1,2,2,2,2,4.           \tag{4}
\]

**Lemma 3 (periodic occupancy).** For every real interval $J$ of length
$\ell$ and positive integer $w$,

\[
 |J\cap B_w|\le {2\ell\over n}+{2(n-2)\over n^2w}.        \tag{5}
\]

*Proof.* Put $\alpha=2/n$ and write $w\ell=m+u$, where $m$ is an
integer and $0\le u<1$. Full periods contribute $m\alpha$; the remaining
arc meets the bad arc in measure at most $\min(u,\alpha)$. Its excess
over $\alpha u$ is at most $\alpha(1-\alpha)$. Divide by $w$.
A single complete bad band attains this additive constant. $\square$

If two distinct speeds $w_1<w_2$ cover a retained-safe interval, (5) gives

\[
 \ell(1-4/n)<{4(n-2)\over n^2w_1}.                        \tag{6}
\]

The strict inequality uses $w_2>w_1$. The restriction $n>4$ allows
division by $1-4/n$.

## 3. Two deletions and one insertion leave a hole

**Proposition 4.** For every $n\ge5$, distinct deletions
$1\le r_1<r_2<n$, and integer $w\ge n$,

\[
 \operatorname{LR}\bigl(([n-1]\setminus\{r_1,r_2\})\cup\{w\}\bigr)>1/n.
                                                               \tag{7}
\]

We prove this without using a one-entry equality classification. The next
lemma reconstructs the middle-window argument of [1] under coverage alone.

**Lemma 5 (middle removal).** If $3\le r\le(n-1)/2$ and $w\ge n$,
then $([n-1]\setminus\{r\})\cup\{w\}$ is not a cover.

*Proof.* Put $s=n-r$. For nonzero residues $x\pmod r$, let $F(x)$
be the representative of $x$ in $[s,n-1]$. Let

\[
 I=\min\{i\ge s:\gcd(i,r)=1\}=s+d.
\]

Thus $I\le n-1<2s$, and Lemma 2 gives $d\le\lfloor r/2\rfloor$.
For a unit $p\pmod r$, write $a=p^{-1}\pmod r$. All retained speeds
are safe on each of the intervals

\[
 L_p=\left({p\over r}-{s\over rnF(a)},
                 {p\over r}-{1\over2rn}\right),\qquad
 R_p=\left({p\over r}+{1\over2rn},
                 {p\over r}+{s\over rnF(-a)}\right).       \tag{8}
\]

To verify this source statement, write a time in $R_p$ as $p/r+u$.
Then $1/(2rn)<u<1/(rn)$. Every retained multiple $kr$, $k\ge2$,
has distance $kru>1/n$, while $kru<1/r\le1/3$. A nonmultiple whose
residue after multiplication by $p$ is $r-1$ has distance
$1/r-iu>1/n$, because $i\le F(-a)$. Every other nonzero residue stays
strictly between $1/r$ and $(r-1)/r$ after the positive displacement.
Reflection proves the left-window statement. These intervals are nonempty
since all their $F$-values are below $2s$.

One of the right windows has length

\[
                         {2s-I\over2rnI}.                 \tag{9}
\]

We need the inequality

\[
                     {4rI\over2s-I}<r(n-2).               \tag{10}
\]

It is equivalent to $d<s(n-6)/(n+2)$. If $r\ge6$, the right side is
at least $(r+1)(2r-5)/(2r+3)>r/2\ge d$. The strict step is equivalent
to $2r^2-9r-10=(r-6)(2r+3)+8>0$. For $r=4,5$, (4) gives $d\le1$,
while the right side is already $15/11$ and $30/13$, respectively, at
the smallest admissible $n$. For $r=3$, $d=0$ at $n=7,8$, and for
$n\ge9$ the right side is at least $18/11>d$. This proves (10).

Suppose there were a cover. Each window and its closure must lie in one
$w$-band. Comparing (9) with its length $2/(nw)$ gives
$w\le4rI/(2s-I)<r(n-2)$. Write $w=Kr+c$, with
$-r/2<c\le r/2$, and put $F_+=F(1)$, $F_-=F(-1)$.
Covering the closed right window at $p=1$ by a band centered at $j/w$
requires

\[
 {c\over r}+{ws\over rnF_-}-{1\over n}
 \le j-K\le {c\over r}+{w\over2rn}+{1\over n}.            \tag{11}
\]

If $j-K\ge1$, the right inequality forces
$c\ge r-w/(2n)-r/n>r/2$. If $j-K\le-1$, the left inequality forces
$c<-r/2$. Thus $j-K=0$, giving

\[
                    c\le {r\over n}-{ws\over nF_-}<0.     \tag{12}
\]

The final sign follows from $ws\ge ns>r(n-1)\ge rF_-$.
For the left window the analogous bounds are

\[
 {c\over r}-{w\over2rn}-{1\over n}
 \le j-K\le {c\over r}-{ws\over rnF_+}+{1\over n}.
\]

Again the integer is zero, and hence $c\ge ws/(nF_+)-r/n>0$,
contradicting (12). $\square$

**Lemma 6 (small removals).** A one-entry cover with $r=1$ is impossible.
For $r=2\le(n-1)/2$, coverage is possible only when
$(n,w)=(5,7)$ or $(6,9)$.

*Proof.* For $r=1$, the interval $(1/(2n),1/n)$ is safe for all
speeds $2,\ldots,n-1$. Its length $1/(2n)$ exceeds $2/(nw)$ for
$w\ge n\ge5$, so it cannot fit in one $w$-band. This argument already
appears in [2].

For $r=2$, the left shell

\[
 (1/2-\beta,1/2-1/(4n)),\quad
 \beta=\begin{cases}1/(2n)&n\text{ odd},\\
 (n-2)/(2n(n-1))&n\text{ even}
 \end{cases}                                              \tag{13}
\]

is safe. Indeed, at $t=1/2-u$, retained even speeds have distance
$vu>1/n$, with $vu<1/2$; retained odd speeds have distance $1/2-vu>1/n$,
using the largest odd speed to check the last inequality.

A covering $w$-band has its center below $1/2$: its halfwidth
$1/(nw)\le1/n^2<1/(4n)$ is smaller than the shell's distance from $1/2$.
The largest such center
is $1/2-1/w$ for even $w$, and $1/2-1/(2w)$ for odd $w$.
Reaching the right endpoint of the closed shell forces respectively
$w\ge4(n-1)$ or $w\ge2(n-2)$. The shell length gives $w\le8$ for
odd $n$ and $w\le8(n-1)/(n-3)$ for even $n$. Even $w$ is impossible.
For odd $w$, these inequalities leave only $(5,7),(6,9),(6,11),(6,13)$.
At $t=87/200$, the distances for speeds $1,3,4,5,11,13$ are
$87,61,52,35,43,69$, divided by 200; all exceed $1/6$. Thus the last
two cases fail. This is the shell argument of [1]. $\square$

*Proof of Proposition 4.* If the two-deletion, one-insertion set covered,
adding either missing speed would give two one-entry covers. Lemmas 5--6
exclude every lower-half removal except 2 in the two sporadic cases.
For $n=5,w=7$, the other removal is 3 or 4, and its center $1/r$
is a hole since $r\nmid7$. For $n=6,w=9$, centers exclude other
removals 4 and 5. If the pair is $\{2,3\}$, at $t=13/36$ the speeds
$\{1,4,5,9\}$ have distances $13,16,7,9$, divided by 36, all above $1/6$.

It remains to consider two upper-half removals. At $1/r_i$, every
retained speed has distance at least $1/r_i>1/n$. If $r_i\nmid w$,
the inserted speed also does, giving a hole. Otherwise write
$w=mr_1=lr_2$, with $m>l\ge1$. Then

\[
 mr_1=lr_2\le(m-1)(n-1),\qquad m(n-r_1)\ge n-1+m\ge n+1.
\]

Take $u=(n+1)/(n^2w)$. The preceding inequality gives
$u<(n-r_1)/(nr_1(n-1))$. At $t=1/r_1+u$, all retained speeds remain
strictly above $1/r_1-(n-1)u>1/n$. The inserted distance is determined
by $(n+1)/n^2\in(1/n,1-1/n)$, so it too is safe. This contradiction
exhausts all cases. $\square$

## 4. Endpoint spacing and lower-half removals

**Lemma 7.** Under the cover hypothesis of Theorem 1,

\[
                         w_2\le2(n-1)w_1.                 \tag{14}
\]

*Proof.* Proposition 4 gives a nonempty open gap after inserting $w_1$.
Both endpoints are actual endpoints $(nk\pm1)/(nv)$ of source bands.
There are no exceptional endpoints at 0 or 1, which have bad neighborhoods.
For different endpoint labels $u,v$, their positive difference is an
integer divided by $nuv$. At most one label exceeds $n-1$, so the gap
has length at least $1/(nw_1(n-1))$. For equal labels its length is an
integer divided by $nv$, giving an even larger lower bound.
The gap must fit in a single $w_2$-band of length $2/(nw_2)$. $\square$

If the retained minimum has value at least $\mu>1/n$ at some time,
its Lipschitz constant at most $n-1$ gives a safe interval of length
$2(\mu-1/n)/(n-1)$. Equation (6) yields

\[
                  w_1<{2(n-2)(n-1)\over n(n-4)(\mu-1/n)}. \tag{15}
\]

**Proposition 8.** If $2r_1\le n-1$, then (2) holds.

*Proof.* Let $D$ be the least integer at least $n+r_1$ coprime to $r_1$.
Choose $a r_1=1\pmod D$. At $a/D$, every retained speed has distance
at least $2/D$: residues 0 and $\pm1$ would require respectively a
multiple of $D$, the deleted speed $r_1$, or a speed at least
$D-r_1\ge n$. Thus we may use $\mu=2/D$ in (15).

For $r_1\ge7$, Lemma 2 gives

\[
 D\le n+r_1+j(r_1)-1\le n+3r_1/2-2\le(7n-11)/4.          \tag{16}
\]

Using (4), the same estimate holds for smaller $r_1$, except at the five
pairs in the following table. The final column is (15).

| $n,r_1$ | $D$ | strict bound for $w_1$ |
|---|---:|---:|
| $5,2$ | 7 | 56 |
| $6,2$ | 9 | 60 |
| $7,3$ | 10 | 50 |
| $10,4$ | 15 | 72 |
| $14,6$ | 23 | $3588/25$ |

This list is exhaustive without an unbounded computation: the bound
$D\le n+r_1+j(r_1)-1$ implies (16) for $n\ge5,8,9,11,12,16$,
respectively, when $r_1=1,\ldots,6$. Only the intervening admissible
integers $n\ge2r_1+1$ remain, and their gcds give the displayed exceptions.
Each table entry is below $14n$.

Otherwise, (16) gives $\mu-1/n\ge(n+11)/(n(7n-11))$. The bound (15)
is below $14n$, since the required positive numerator is

\[
\begin{split}
 7n(n-4)(n+11)-(n-2)(n-1)(7n-11)
 &=81n^2-355n+22\\
 &=81(n-5)^2+455(n-5)+272>0.
\end{split}
\]

Thus $w_1<14n$. Lemma 7 gives $w_2<28n(n-1)$. $\square$

## 5. Arithmetic centers for upper-half removals

Assume $2r_1>n-1$. The safe center $1/r_1$, used in (15), gives

\[
 w_1<{2(n-2)r_1(n-1)\over(n-4)(n-r_1)}
 \le{(n-2)^2(n-1)\over n-4}<2n^2.                         \tag{17}
\]

Here $r_1\le n-2$. The last inequality follows from

\[
 2n^2(n-4)-(n-2)^2(n-1)=(n-5)(n^2+2n+2)+14>0.
\]

**Lemma 9 (a unit center).** If $r,a$ are positive integers and $r\nmid a$,
some integer $p$ coprime
to $r$ satisfies $\|ap/r\|\ge1/6$.

*Proof.* Put $g=\gcd(a,r)$, $q=r/g>1$. A unit $b\pmod q$ at distance
at least $1/6$ from an integer after division by $q$ is explicit:

\[
 b=\begin{cases}
 1,&q=2,\\
 (q-1)/2,&q\text{ odd},\\
 q/2-1,&q\equiv0\pmod4,\\
 q/2-2,&q\equiv2\pmod4,\ q\ge6.
 \end{cases}
\]

The corresponding distances are $1/2$, $1/2-1/(2q)$, $1/2-1/q$,
and $1/2-2/q$. Coprimality is immediate; the minimum $1/6$ occurs at
$q=6$. Reduction of units modulo $r$ onto units modulo its divisor
$q$ is surjective: prescribe a unit modulo $q$ and prescribe 1 modulo
each prime dividing $r$ but not $q$, then apply the Chinese remainder
theorem. Lift $b(a/g)^{-1}\pmod q$ to such a unit $p\pmod r$.
Then $ap/r=b/q\pmod1$. $\square$

Suppose first that $n\ge7$ and some removed $r\nmid w_1$. Choose the
unit $p$ of Lemma 9 with $0<p<r$, and put $t_0=p/r$. All retained
baseline distances there are at least $1/r$. Consequently the interval
of radius

\[
 R=\min\left({n-r\over nr(n-1)},{n-6\over6nw_1}\right)>0  \tag{18}
\]

around $t_0$ is safe for both the retained baseline and $w_1$. It stays
inside $(0,1)$, since $R<1/r$. At the center, final coverage forces
$r\mid w_2$, as a nonzero circle distance with denominator $r<n$
exceeds $1/n$. The entire connected safe interval must lie in the
$w_2$-band centered exactly at $t_0$. Hence

\[
 w_2\le\max\left({r(n-1)\over n-r},{6w_1\over n-6}\right)<12n^2, \tag{19}
\]

using (17) and $n\ge7$.

It remains possible that $w_1$ is divisible by both removals. Write
$w_1=mr_1=lr_2$, $m>l$, so $m(n-r_1)\ge n-1+m$. Define

\[
 A={n-r_1\over nr_1(n-1)},\qquad h={1\over nw_1}.
\]

The interval

\[
 \left({1\over r_1}+h,
 {1\over r_1}+\min\left(A,{n-1\over nw_1}\right)\right)    \tag{20}
\]

is safe for the retained baseline and lies between consecutive $w_1$-bands.
Its length is at least

\[
 \min\left({1\over nr_1(n-1)},{n-2\over nw_1}\right),
\]

because

\[
 A-h={m(n-r_1)-(n-1)\over nw_1(n-1)}\ge{1\over nr_1(n-1)}.
\]

Fitting (20) in one $w_2$-band gives

\[
 w_2\le\max\left(2r_1(n-1),{2w_1\over n-2}\right)<2n^2. \tag{21}
\]

The next-band endpoint in (20) is essential even when $w_1$ is extremely
large. No distinct assignment of insertions to removals has been assumed.

*Completion of Theorem 1.* Proposition 8 handles all pairs with a lower-half
removal. Equations (19)--(21) handle two upper-half removals for $n\ge7$.
For $n=5,6$, (14) and (17) give
$w_2<4(n-1)n^2\le20n^2<28n^2$. These cases exhaust the domain. $\square$

## 6. Finite reduction and computational consequences

**Corollary 10.** For each fixed $n\ge5$, every two-entry cover is found
by testing the finite set of integers

\[
 1\le r_1<r_2<n,\qquad n\le w_1<w_2\le28n^2-1.
\]

Stronger parameter bounds from (14)--(19) can reduce this domain. Exact
coverage is decided by the finite union of closed source bands (3) on
$[0,1]$; integer cross-products suffice for all endpoint comparisons.
This finite interval method is established, not a new certification principle.

Two separately implemented exact computations classify the family through
$n=30$. The only covers are

\[
\begin{array}{c|c|c|c}
 n&\{r_1,r_2\}&\{w_1,w_2\}&V\\\hline
 5&\{1,3\}&\{6,8\}&\{2,4,6,8\}\\
 8&\{2,3\}&\{11,13\}&\{1,4,5,6,7,11,13\}.
\end{array}
\]

Both have loneliness exactly $1/n$: exact coverage supplies the upper
bound, and evaluation at $t=1/n$ supplies the lower bound. The first
has gcd 2 and must not be removed by a primitive-only filter. The second
is a known Goddyn--Wong example [2], not a new construction.

The executed searches used the earlier proved parameter-dependent cubic
domains, which contain all possibilities and remain valid after Theorem 1.
For $5\le n\le20$, those domains contained 79,648,374 quadruples. The
extension $21\le n\le30$ covered 923,839,088 quadruples with no survivors;
exact longest-gap, width, and center-divisibility pruning reduced the
individual tests. A separate Fraction implementation, importing no SUCC
search or verifier modules, agreed. The mathematical bound is proved above;
agreement of implementations is not its proof. Reproducible receipts and
the complete pruning derivations accompany the repository dossiers.

## Appendix. Verification and limitations

The paper proof preserves zero shifts, the actual baseline, all deletion
pairs, and nonprimitive speed sets. Positive controls include the established
two-acceleration examples at $n=74$ and $n=284$. Negative controls include
wrong divisibility assignments, omitted coverage gaps, missing periodic
boundary slack, and strict-to-integer rounding errors. The unit-center
constant cannot be increased above $1/6$ without additional hypotheses,
as modulus 6 shows.

Lean evidence and executable evidence must be read by their actual scopes.
The earlier checked development includes a complete rational witness for
the upper-half one-insertion hole and generic source-band coverage semantics.
The new growth formalization proves the complete upper-half implication
$w_2<3n^3$ from actual coverage, including source-gap construction and the
two-band interval estimate. Its 18 exported theorem types, standard-axiom
receipts and three paired false controls delimit this authority. No finite
scan, a priori separation
certificate, or earlier upper-half theorem is advertised as a kernel proof
of the unrestricted quadratic theorem. Theorem 1 remains a paper proof.
Same-model internal reviews are correlated checks, not external peer review.

The constant 28 is not asserted optimal. An $O(n\log n)$ bound for the
unrestricted family, a classification for all $n$, and growth estimates
for three or more modifications are not established here.

## References

1. Y. Zhang, *Tight instances of the Lonely Runner Conjecture: one-entry
   modifications and the growth of speeds*,
   [arXiv:2608.13599v3](https://arxiv.org/html/2608.13599v3), 18 October 2026.
2. L. Goddyn and E. B. Wong, *Tight Instances of the Lonely Runner*,
   Integers **6** (2006), A38.
   [Journal PDF](https://math.colgate.edu/~integers/g38/g38.pdf).
3. D. D.-F. Liu, *From rainbow to the lonely runner: a survey on coloring
   parameters of distance graphs*, Taiwanese J. Math. **12** (2008), 851--871.
   [DOI](https://doi.org/10.11650/twjm/1500404981).
4. JenW1N, accepted source04 proof,
   [Conjectures.io result](https://conjectures.io/results/4c651db1-3b53-48da-ac31-0b0020a8d87c),
   certification reported 9 October 2026. Selected interfaces inspected;
   not locally replayed as an external kernel proof.
5. M. Beck and S. Everett, *Lonely Runner Relations*,
   [arXiv:2609.06259v2](https://arxiv.org/html/2609.06259v2), 23 September 2026.
6. R. D. Malikiosis, F. Santos, and M. Schymura, *Linearly-exponential checking
   is enough for the Lonely Runner Conjecture and some of its variants*,
   Forum Math. Sigma **13** (2025), e164.
   [DOI](https://doi.org/10.1017/fms.2025.10107).
