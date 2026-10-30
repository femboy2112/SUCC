# All prime classes, prime-power returns, and the first precision obstruction

**Authority:** local paper proofs plus exact finite checks; no Lean or scholarly
priority claim. Exact parent is PR #398 at
`1a1524de28b155139d8fe84ea90fc2f117fbb9f3`. The original signed four poles,
`U_0=0`, and all parent theorem contracts are unchanged. These are arithmetic
constraints on that rational trajectory, not estimates of its selected
real-circle signed sums. Base-16 normality of π and RH remain **OPEN**.

Write `Δ=(1,4,5,6)`, `c=(A,B,C,D)` and

\[
 U^c_n=\sum_{j=1}^n16^{n-j}\sum_{\delta\in\Delta}
 \frac{c_\delta}{8(j-1)+\delta}.
\]

The authentic vector is `(4,-2,-1,-1)`. Rational congruence modulo `p^r`
always means reduction in `Z_(p)/p^r Z_(p)`; every displayed congruence has
p-integral operands. A changed irrational seed is not silently assigned a
p-adic reduction.

## AT-01 — a complete four-class prime-power shadow

Let p be an odd prime, a,k positive integers, and `Q=p^a`. Set

\[
 (s_*,\mathcal D)=
 \begin{cases}(6,(1,4,5,6)),&Q\equiv1\pmod4,\\
 (7,(2,3,4,7)),&Q\equiv3\pmod4,
 \end{cases}
 \quad L=8(k-1)+s_*,\quad d_*=QL\bmod8\in\Delta.
\]

Assume **p>L**, and that the four coefficients are p-integral. The legitimate
integer clock is

\[
 \boxed{M_Q(k)=\frac{QL+8-d_*}{8}.}
\]

It is the old `((4k−1)Q+1)/4` in classes 1 and 5. In class 3 it is
`((8k−1)Q+3)/8`; in class 7 it is `((8k−1)Q+7)/8`. Define `V_k`
using the same radix-16 prefix recurrence, but with condensed offsets and
coefficients in this table:

| Q mod 8 | Condensed offsets | Condensed coefficients |
|---|---|---|
| 1 | 1,4,5,6 | A,B,C,D |
| 5 | 1,4,5,6 | −4C,B,−A/4,D |
| 3 | 2,3,4,7 | −8D,A,−2B,C |
| 7 | 2,3,4,7 | 32D,16C,8B,A |

Then

\[
 \boxed{p^a U^c_{M_Q(k)}\equiv V_k\pmod p.}\tag{AT-1}
\]

**Proof.** The greatest native denominator is `QL+6−d_*<pQ`, since
`L<p` and `6−d_*≤5<p`. Therefore it has valuation at most a. After multiplying
by Q and reducing modulo p, only denominators `Qq` survive. They occur exactly
at `q=8(l−1)+s`, `1≤l≤k`, `s∈D`; their actual native offset is
`δ=Qs mod8`, and their original index is `j=(Qq+8−δ)/8`.
There are exactly `4k` such terms. If `t=L−q`, direct subtraction gives

\[
 (M_Q-j)-(k-l)=\frac{(Q-1)t+s_*-s+\delta-d_*}{8}.\tag{AT-2}
\]

Let `χ=(2/p)=(-1)^((p²−1)/8)` and `S_a=1+p+...+p^(a−1)`. Euler's
criterion yields `2^((Q−1)/2)≡χ^a (mod p)`, because `S_a≡a (mod2)`.
Thus the relative multiplier is

\[
 w_s=\chi^{a t}2^{(s_*-s+\delta-d_*)/2}.
\]

The exponent after the factor 2 is an integer; negative exponents denote
p-integral rational powers of 2. The parity of t depends only on s.
The supplementary law makes `χ^a` a function of `Q mod8`, and substitution
gives precisely the four rows of the table. Summing the surviving terms gives
AT-1. This proof uses only exact denominator selection, Euler's criterion and
the supplementary quadratic reciprocity law. ∎

**Authentic consequence.** At classes 1 and 5, `V_k=U_k`. At classes 3 and 7,
let W be the radix-16 prefix driven by

\[
 w(l)=\frac8{8l-6}+\frac4{8l-5}+\frac4{8l-4}-\frac1{8l-1}.
\]

Then `V_k=W_k` in class 3 and `V_k=−4W_k` in class 7. The reflected source is
a **derived shadow**, not a replacement for the authentic forcing.

In particular every odd p has `p^(2b)≡1 mod8`, so for p>8k−2 and every b≥1,

\[
 \boxed{p^{2b}U_{((4k-1)p^{2b}+1)/4}\equiv U_k\pmod p.}\tag{AT-3}
\]

This removes the missing-prime-class obstruction by using even-depth clocks.
Whenever the right side is nonzero, the selected rational has **exact**
valuation `v_p(U_M)=−2b`. For k=1 this holds for every p≥7 except p=47.
For p=47, k=2 repairs the zero: `U_2≡r(2)=106/819≡10 (mod47)`.
For odd depth, classes 3/7 retain the reflected shadow instead of pretending
that the old clock is integral.

**Precisely limited obstruction.** Multiplication by 3 or 7 modulo 8 carries
the original offset set to `(2,3,4,7)`, different from Δ. Integer shifts of
native time preserve each denominator's residue modulo 8. Hence coefficient
permutation and integer time translation cannot turn this reflected rational
forcing back into the original four-pole forcing. Distinct rational pole
locations also prevent a nonzero rational-function identity identifying them.
This does not rule out more general arithmetic transforms or composite clocks.

**Intermediate-event lemma (for conductor survival).** At condensed packet l
and its offset s, let `q=8(l−1)+s`, `j_s=(Qq+8−(Qq mod8))/8`. Provided
the full l-packet satisfies AT-01's domain,

\[
 16^{M_Q(l)-j_s}\,p^aU_{j_s}\equiv
 H_{l,s}:=16V_{l-1}+\sum_{s'\le s}
 \frac{c'_{s'}}{8(l-1)+s'}\pmod p.
\]

The proof repeats AT-2 for precisely the events already encountered; the
prefactor is a unit. For the authentic source all native H are strictly
positive: the first partial summand is positive, the remaining negative
summands decrease to the positive full r(l), and U_(l−1)≥0. Reflected class-3
H are also strictly positive, because their first three summands are positive
and the last `−1/(8l−1)` is dominated already by `8/(8l−6)`; W_(l−1)≥0.
Class-7 H are −4 times those values and are strictly negative. Thus for each
fixed finite number of packets these finitely many rational H are nonzero,
and only finitely many primes can cancel an encountered conductor by dividing
one of their numerators. This exact lemma is useful when the packet count is
bounded while p grows; no uniform bound on those exceptional numerators as
the packet count grows is claimed here.

## AT-02 — the exact first correction, not a naive Hensel lift

Keep AT-01's hypotheses. Put

\[
 \theta_p=\frac{\chi\,2^{(p-1)/2}-1}{p}\in\mathbb Z,
 \qquad
 D_k=L V_k-\Big(\sum_s c'_s\Big)\frac{16^k-1}{15},
\]

where `c'` are the condensed coefficients. The latter expression is rational;
the geometric sum `(16^k−1)/15` is an integer. Retain the **next actual
denominator layer**, with its signed source history:

\[
 R_{p,a,k}=\sum_{\substack{1\le j\le M_Q(k),\delta\in\Delta\\
            v_p(8(j-1)+\delta)=a-1}}
 \frac{c_\delta\,16^{M_Q(k)-j}}
 {(8(j-1)+\delta)/p^{a-1}}\quad\in\mathbb Z_{(p)}.
\]

Then the corrected lift is

\[
 \boxed{p^aU^c_{M_Q(k)}\equiv
 V_k+p\big(\theta_p D_k+R_{p,a,k}\big)\pmod{p^2}.}\tag{AT-4}
\]

**Proof.** For a top-layer term the exact relative factor from AT-2 is
`w_s(1+pθ_p)^(S_a t)`. Since `S_a≡1 modp`, this is
`w_s(1+pθ_p t)` modulo p². Summing the t-weighted terms gives
`Σ 16^(k−l)c'_s(L−q)/q = D_k`. The valuation a−1 layer contributes
`pR`; every lower layer is divisible by p². ∎

For the authentic source on native-return clocks, `Σc'=0`, so
`D_k=(8k−2)U_k`. For reflected class 3 it is
`D_k=(8k−1)W_k−(16^k−1)`, and class 7 multiplies that expression by −4.
The remainder R is not an unspecified error: it is an exact, executable sum
over the genuine source denominators. No signed estimate for R is proved here.

**Smallest admissible native-prime counterexample to an uncorrected lift.**
At p=13,k=1, the remote time is 10 and

\[
 13U_{10}-U_1\equiv65\pmod{169},\qquad
 \theta_{13}\equiv8,\quad D_1\equiv11,\quad R_{13,1,1}\equiv8\pmod{13}.
\]

Indeed `8·11+8≡5 (mod13)`, giving the exact discrepancy `13·5=65`.
p=13 is the smallest prime in the native theorem's domain p≡1mod4, p>6.
The discrepancy is not solely a new p²-denominator birth: none exists in this
range. It already comes from exponent distortion **and the regular layer**.
Tests omitting either correction fail.

**All precision layers.** For any r≥1 retain exactly those source denominators
with valuation v satisfying `a−v<r`:

\[
 p^aU_M\equiv\sum_{v=\max(0,a-r+1)}^a p^{a-v}
 \sum_{v_p(d_{j,\delta})=v}
 \frac{c_\delta16^{M-j}}{d_{j,\delta}/p^v}\pmod{p^r}.\tag{AT-5}
\]

This is an exact finite decomposition, **not** a cancellation theorem. The
top relative factor has the exact binomial truncation
`w_s Σ_(i=0)^(r−1) binom(S_a t,i)p^i θ_p^i (mod p^r)`; lower layers are still
required. Thus higher precision has explicit arithmetic terms without an
unjustified claim of a self-reproducing Hensel law.

## AT-03 — every odd prime has all conductor depths, and the reflected gap

For every odd prime p and a≥1, without the k-clock restriction, put Q=p^a.
The first native source denominator divisible by Q occurs at

\[
 b_Q=\begin{cases}(Q+7)/8,&Q\equiv1\pmod8,\\
 (Q+3)/8,&Q\equiv5\pmod8,\\
 (Q+1)/4,&Q\equiv3,7\pmod8.
 \end{cases}
\]

Then

\[
 QU_{b_Q}\equiv
 \begin{cases}4,&Q\equiv1\pmod8,\\-1,&Q\equiv5\pmod8,\\-1/2,&Q\equiv3,7\pmod8
 \end{cases}\pmod p,
 \qquad \boxed{v_p(U_{b_Q})=-a}.\tag{AT-6}
\]

**Proof.** The first possible multiplier q with `Qq mod8∈Δ` is 1 for Q in
classes 1/5 and 2 for Q in classes 3/7. Its channel coefficient divided by q is
respectively 4, −1, or −1/2, all p-units. No earlier source denominator is
divisible by Q. At the birth there is no second Q-divisible denominator and no
pQ-divisible denominator: for Q≥7 this follows from the denominator gap at
most 5 and the maximum denominator less than pQ; Q=3,5 check directly at n=1.
After multiplication by Q, every earlier contribution vanishes modulo p.
The displayed residue is nonzero, proving exact valuation. ∎

This includes the exceptional odd primes 3 and 5. It proves infinitely deep
denominators at explicit times for each odd p. It gives no interval occupancy
bound: denominators can grow along coherent or nearly coherent real phases.

For p>7, before any p² denominator, the four first encounters in classes 3/7
are at multipliers q=2,3,4,7. Their residues are

| p mod8 | q=2 | q=3 | q=4 | q=7 |
|---|---|---|---|---|
| 3 | −1/2 | 16/3 | −19/6 | 130/21 |
| 7 | −1/2 | −4/3 | −19/6 | −520/21 |

Proof is the exact recurrence between encounters. Consecutive transport
factors are `(-8,-1/2,-2)` in class 3 and `(2,2,8)` in class 7, obtained from
Euler's criterion. Add the encountered coefficients divided by q.
Between encounters, `pU_(m+j)≡16^j pU_m`; thus a nonzero residue persists,
and a zero residue remains zero until the next encounter.

**New exact loss control:** p=19 has times `(5,8,10,17)`. Its third residue
vanishes, so the 19 conductor is absent for every n=10,...,16 and returns
at n=17. All displayed residues are nonzero for other eligible primes in
their stated class. This is a first-packet cancellation, distinct from the
parent p=73,k=4 cancellation.

**Period obstruction:** in class 3 the first window has `(p+5)/8` indices,
and in class 7 `(p+1)/8`; the generic order only divides `(p−1)/2`.
At p=11 the window has length 2 but `ord_11(16)=5`. The native p1/p5 full-period
guarantee cannot be transplanted to the reflected birth window.

## AT-04 — exactly typed exceptional source passports and coefficient rigidity

The authentic forcing combines to

\[
 r(n)=\frac{120n^2-89n+16}
 {(2n-1)(4n-1)(8n-7)(8n-3)}.\tag{AT-7}
\]

Its denominator is odd for every integer n. Thus every U_n is 2-integral,
`U_n≡r(n) (mod16)`, and `U_n≡n (mod2)`. This is a literal arithmetic passport,
not the distribution of real-circle digits or a replacement for four-bit Walsh.

For the four linear denominator factors in their displayed order, the
resultants with numerator P are

`6, 20, 1920, −32`.

Indeed for `an+b` the resultant equals `a²P(−b/a)`. The pairwise linear
resultants have no odd prime factor except 3 or 5. Consequently, for every
p≥7 at most one reduced-source denominator factor is divisible by p; if one
is, its entire p-valuation survives in r(n). Only 2,3,5 can be exceptional
for this **single-source-term reduction**. This does not forbid later
cross-time cancellation in U_n, as p=19 and p=73 demonstrate.

At 3 and 5 actual exceptional cancellation exists: r(8) is 3-integral despite
its uncombined p-divisible channels, and r(24) is 5-integral. Exact tests also
retain their first-power conductor births. Nothing in these passports gives
the fixed-prime-power modular period laws of Stoneham sources.

Within the **fixed four-pole support**, Jc=c imposes A=−4C. Add the authentic
source moments `Q(0)=0`, `Q'(0)=15` for
`Q(x)=A+B exp(−3x)+C exp(−4x)+D exp(−5x)`. Then

\[
 B=(19C+15)/2,\quad D=(-15-13C)/2,\quad Q''(0)=-61C-120.
\]

The further authentic second derivative `Q''(0)=−59` forces C=−1 and hence
the unique vector `(4,−2,−1,−1)`. This is elementary fixed-support source
identification, **not** zero-seed selection or a signed phase inequality.
The same-ratio mutant `(4,0,−1,0)` still passes J, while `(5,−2,−1,−1)`
does not. Higher-jet-matched fakes outside the four-dimensional source class
remain possible and are not excluded by this finite-moment theorem.

A stronger explicit control **inside** the fixed support is
`c=(2,11/4,−1/2,−17/4)`. It obeys Jc=c, Q(0)=0 and Q'(0)=15. With t=e^(−x),
its kernel factors as

`Q(t)=(1−t)(17t^4+19t^3+8t²+8t+8)/4>0` for 0<t<1.

Thus positivity and the authentic leading Gamma rank/amplitude still do not
identify BBP even after the p5 ratio is imposed. Its second derivative is
`−179/2`, so the extra authentic second jet rejects it exactly.

## AT-05 — increasing p-adic depth does not select the zero boundary

For every p-integral rational seed s,

\[
 p^a(U_M(s)-U_M(0))=p^a16^M s\equiv0\pmod{p^a}.
\]

Therefore all top r digits for fixed r are seed-blind once a≥r. In particular
the corrected first lift at depth a≥2 is still blind modulo p². At precision
a+1 the seed shift is exactly `p^a16^M s`; this can be nonzero. No family of
fixed-precision, increasing-depth shadow checks identifies U_0=0 among
p-integral rational seeds. Exact/eventual circle aliases and constant twists
are allowed to agree; rational translations preserve integer-base normality.
This is an identification boundary for these probes, not a counterexample to
the selected authentic π trajectory. The coherent irrational counterseed
`s=−π/16` belongs to the real-circle control domain, not this rational congruence
domain.

## AT-06 — the reflected source closes onto the published BBP null relation

The reflected source is not an unrelated constant. Bailey, Borwein and
Plouffe's 1997 paper explicitly gives the radix-16 null vector
`Z=(-8,8,4,8,2,2,-1,0)` on offsets 1,...,8 (PDF page 4, following Theorem 1).
Our coefficient table obeys **W−2U=Z** at the forcing level. Therefore

\[
 \sum_{j\ge1}16^{-(j-1)}w(j)=2\pi.
\]

This null identity is **CLASSICAL PUBLISHED**, not a novelty claim. The
specific linkage to AT-01's missing-prime-class shadows is a local deduction.
Source: [Bailey–Borwein–Plouffe, *On the rapid computation of various
polylogarithmic constants*](https://www.davidhbailey.com/dhbpapers/digits.pdf),
Math. Comp. 66 (1997), 903–913, doi:10.1090/S0025-5718-97-00856-9.

For a direct proof let

\[
 Z(x)=-8+8x+4x^2+8x^3+2x^4+2x^5-x^6,
 \quad F(x)=8\log\frac{x^2-2x+2}{2-x^2}.
\]

Exact differentiation gives

\[
 \frac{Z(x)}{1-x^8/16}
 =\frac{16(x^2-4x+2)}{(x^2-2)(x^2-2x+2)}=F'(x).
\]

The logarithm's ratio equals 1 at both endpoints of [0,1], so the integral
vanishes. Expanding the uniformly convergent geometric series reproduces
the published null sum. Moreover F(x)<0 in the interior. If z(n)=w(n)−2r(n),
then `z(n)=∫_0^1 x^(8n−8)(1−x^8/16) F'(x) dx`. For n≥2 the derivative of
`x^(8n−8)(1−x^8/16)` is strictly positive in (0,1), so integration by parts
proves z(n)>0. Also Z'(x)>0 on [0,1] and Z(1)=15, whence
`z(n)<15/(8n−7)`.

The exact rational correction E_k=W_k−2U_k is the negative future null tail.
For every k≥1 it therefore satisfies

\[
 \boxed{-\frac1{8k+1}<E_k<0,\qquad
 E_k=4k\int_0^1x^{8k-1}\log\frac{x^2-2x+2}{2-x^2}\,dx.}\tag{AT-8}
\]

Here the upper tail bound follows by summing `16^-j·15/(8k+1)` for j≥1;
the integral follows by interchanging the geometric sum and integrating by
parts. In particular the reflected arithmetic shadow is a prefix of **2π**
(or −8π in class 7) with an explicit signed rational correction relative to
2U_k. Small real absolute value of E_k says nothing about its residue modulo p.
This strengthens constant identification without proving real-circle mixing.

There is no rational function g(n) with `g(n)−16g(n−1)=z(n)`. Each of z's
seven nonzero simple poles belongs to a different integer-translation orbit,
at roots `1/8,1/4,3/8,1/2,5/8,3/4,7/8`. In any nonempty such orbit of poles of
a rational g, the minimal pole of g survives in the difference and the shift
of the maximal pole survives as a second pole. A forcing with exactly one
pole per orbit is therefore impossible. Polynomial parts cannot cancel these
endpoints. This refutes a rational finite telescoper, not the published
infinite null identity or more general special-function representations.

## AT-07 — zero seed and every odd conductor depth can coexist with coherence

Use the **changed seven-pole null source** z(n) just defined, with its own zero
seed E_0=0 and `E_n=16E_(n−1)+z(n)`. AT-06 proves
`−1/(8n+1)<E_n<0`, hence for every fixed integer h,

\[
 e(hE_n)\longrightarrow1,
 \qquad \frac1N\sum_{n=1}^N e(hE_n)\longrightarrow1.
\]

The completed radix constant is exactly zero, so it is nonnormal. Nevertheless
for every odd prime p and every integer a>=1, with Q=p^a,

\[
 \boxed{v_p\left(E_{\lceil Q/8\rceil}\right)=-a.}\tag{AT-9}
\]

For Q>=7, the first Q-divisible denominator is Q itself, now that all seven
offsets are present. In its native step it is the only such denominator,
because the maximum denominator is at most Q+6<2Q. Its coefficient is
`Z_(Q mod8)∈{−8,4,2,−1}`, always a unit at an odd p. Every earlier denominator
has smaller p-valuation. Scaling by Q and reducing modulo p proves AT-9.
For the remaining Q=3,5 cases, direct evaluation gives
`E_1=130/21-2*(47/15)=-8/105`, so `v_3(E_1)=v_5(E_1)=-1`.
This separate calculation completes every depth; it does not extend the
unique-event argument to those two small values.

This is a sharp calibration against inferring real cancellation from **zero
seed plus unbounded conductor depths at every odd prime**. Both properties
hold while the selected signed phases are coherent. It does not satisfy the
authentic four-pole source contract and does not refute any source-authenticated
π theorem. Any successful signed CRT estimate must use more than these two
properties; in particular it must exclude this precise correlated complement.

## Claim and next-obligation ledger

| Claim | Status | What remains |
|---|---|---|
| AT-01 four-class, all-depth transport; even-depth native return | PROVED LOCAL, exact finite checks | Independent mathematical review; connect full CRT signed phase |
| AT-02 first lift and all valuation layers | PROVED LOCAL, exact finite checks | Bound the actual signed layer/cofiber interaction; decomposition alone is insufficient |
| Uncorrected mod-p² return | REFUTED | p13,k1 discrepancy 65 mod169 |
| AT-03 universal odd conductor-depth births and packet dynamics | PROVED LOCAL, exact finite checks | Denominator size does not imply occupancy |
| Native-period guarantee for classes 3/7 | REFUTED | p11 length2 versus order5 |
| AT-04 exceptional source passports and fixed-support rigidity | PROVED LOCAL, exact finite checks | Higher source classes and selected phase are outside the theorem |
| AT-05 fixed-precision tower selects zero seed | REFUTED | Exact rational seed aliases survive |
| AT-06 reflected constant 2π / −8π and signed null-tail bound | PUBLISHED null identity + PROVED LOCAL deduction | A small real correction has uncontrolled p-adic residue; signed CRT target remains |
| Rational finite telescoper for the reflected correction | REFUTED | Distinct pole-translation orbits give an exact obstruction |
| Zero seed + every odd-prime conductor depth implies cancellation | REFUTED by AT-07 | Published seven-pole null source is coherent; authentic source is different |
| These results imply normality / RH | NOT CLAIMED | Source-selected signed real-circle interaction is still OPEN |

The decisive next falsifier is a bound on the **actual** complement paired
with these p-primary residues, retaining the zero seed. The p² correction
isolates where omitted information first re-enters, but does not bound it.
No use of the author's Harmonic Numbers / Golden Ratio / Euler–Mascheroni
triangle or Oily–Macaroni attribution is changed by this arithmetic extension.
