# What the integer boundary packet can and cannot determine

**Status: PROVED LOCAL.** For nonnegative integer grade histograms, the
fixed-base prefix packet `M,F(b^-1),...,F(b^-d)` determines the entire
histogram whenever `M<=b^[d(d+1)/2]`. Conversely, explicit equal-mass
integer twins with different zero counts have the same packet at mass
`prod_(r=1)^d(b^r+1)`. These two mass thresholds differ by a bounded
factor, less than `153/64` uniformly for integer `b>=2`.

Consequently the previous `sqrt(2 log_b M)` leading channel count is
optimal **for this prescribed fixed-base prefix observation family**.
It is not a lower bound for arbitrary choices of observation nodes:
one sample at `s=1/(M+1)` already gives `c_0=floor F(s)` if such a node
is permitted. Exact rational observations can contain arbitrarily many
bits. None of these statements supplies a response oracle, a speedup,
an arithmetic histogram realization, or a Goldbach counterexample.

## 1. Object, comparison target and provenance

Fix an integer base `b>=2`. A source is a sequence

\[
c_h\in\mathbb Z_{\ge0},\qquad
M=\sum_{h\ge0}c_h<\infty,\qquad
F_c(z)=\sum_{h\ge0}c_hz^h.
\]

Finite integer mass implies finite support, but no common upper grade is
known or imposed. The observation packet is

\[
\mathcal O_{b,d}(c)=(M,F_c(b^{-1}),\ldots,F_c(b^{-d})),
\qquad d\in\mathbb Z_{\ge0}.
\tag{II0}
\]

Its target is the integer count `c_0`. The mass is supplied exactly and
separately. The same base is used while the prefix length grows. Define
`M_min(b,d)` to be the least integer mass for which two such sources have
the same packet and different zero counts, minimizing over **all finite
supports**. The construction below makes this set nonempty, so its
infimum is an attained integer minimum. It does not assert that our
particular construction attains the minimum.

The comparison is with DF-03 in
[DAMPED_FILTERS.md](../holographic_boundary_filters/DAMPED_FILTERS.md),
which gives an even-degree stable recovery rule from `epsilon_d M<1`,
where `epsilon_d=b^[-d(d+1)/2]`. That earlier rule needs only integral
`c_0` and nonnegative remaining masses; the divisibility result here
uses the stronger promise that **every grade mass is integral**. The
previous fixed-bank arithmetic obstruction and changing-bank mean
result in [FIXED_RESOLUTION.md](../holographic_boundary_filters/FIXED_RESOLUTION.md)
were also inspected. The present twins make no claim about the much
smaller family of histograms realized by `Omega(n+a)+Omega(n-a)-2`.

Repository baseline inspected: commit
`5d9917031855f806fd5c1f9d8b4543ad3ca24bbf`. This note and its two companion
Python files are new artifacts; no prior-round theorem or code was changed.

## 2. II-01: the exact kernel and a strict integer mass barrier

Put

\[
D_d=\frac{d(d+1)}2,\qquad B_d=b^{D_d},\qquad
A_{b,d}(z)=(1-z)\prod_{r=1}^d(1-b^rz).
\tag{II1}
\]

For two sources with the same packet, their difference polynomial
`P=F_c-F_c'` has integer coefficients and vanishes at
`1,b^-1,...,b^-d`. Therefore

\[
P=A_{b,d}Q\quad\text{for some }Q\in\mathbb Z[z].
\tag{II2}
\]

Here is a direct integer proof, including the denominator issue. If an
integer polynomial `P(z)=sum_(j=0)^H p_j z^j` vanishes at `1/k`, with
integer `k>=1`, set `q_0=p_0` and `q_j=p_j+kq_(j-1)`. The terminal
value is

\[
q_H=\sum_{j=0}^H p_jk^{H-j}=k^HP(1/k)=0.
\]

Coefficient comparison gives
`P=(1-kz) sum_(j=0)^(H-1) q_j z^j`, with integer quotient. Peel off
the distinct roots one at a time. Division by one factor preserves all
the other roots, establishing II2 without a rational-to-integer leap.

If `P` is nonzero, its leading coefficient has magnitude at least
`B_d`, because the leading coefficient of `A_(b,d)` is
`(-1)^(d+1) B_d` and the quotient has a nonzero integer leading
coefficient.

Let `S` be the positive coefficient mass of `P`. Since `P(1)=0`, this
also equals the negative coefficient mass. Removing common mass from
the two histograms gives `S<=M`. For `d>=1`, in fact

\[
S\ge B_d+1.
\tag{II3}
\]

To see the strict extra unit, orient the sign so the leading coefficient
`p_H` is positive. If it were the only positive coefficient, every
negative term would have degree below `H`. For every `0<x<1`,

\[
P(x)=p_Hx^H-\sum_{h<H}|p_h|x^h
<p_Hx^H-\left(\sum_{h<H}|p_h|\right)x^H=0,
\]

contradicting the root `x=1/b`. There must be another positive
coefficient, an integer at least one. Thus `S>=p_H+1>=B_d+1`.

**Theorem II-01.** For every integer `b>=2,d>=1`,

\[
\boxed{M_{\min}(b,d)\ge b^{d(d+1)/2}+1.}
\tag{II4}
\]

More strongly, if `M<=B_d`, the packet determines the **entire integer
histogram** uniquely, not merely its zero count: the argument excluded
every nonzero difference polynomial, even one whose constant is zero.
This is uniqueness, not a polynomial-time decoding claim. A single exact
rational at grade `H` can have a denominator of size `b^H`; unbounded
grade is not a free bit budget.

The hypothesis `d>=1` is necessary for the strict step. At `d=0`, only
the mass is observed and `M_min(b,0)=1`, witnessed by one unit at grade
zero versus one at grade one. At mass zero, no channel is needed.

## 3. II-02: executable twins and a bounded mass gap

Expand `A_(b,d)=sum_h a_h z^h` and take its coefficientwise positive
and negative parts:

\[
c_h^+=\max(a_h,0),\qquad c_h^-=\max(-a_h,0).
\tag{II5}
\]

These are nonnegative integer histograms on grades `0,...,d+1`.
The root at one makes their masses equal; the other roots make all `d`
responses equal. Since the constant coefficient is one, their zero
counts are `1` and `0`.

All coefficients of `A` alternate in sign because every root factor is
`1-kz` with positive `k`. Therefore its coefficient norm is

\[
\sum_h|a_h|=A(-1)=2\prod_{r=1}^d(1+b^r).
\]

Each histogram has mass

\[
U_d:=\prod_{r=1}^d(b^r+1)
=B_d\prod_{r=1}^d(1+b^{-r}).
\tag{II6}
\]

Adding the same `M-U_d` units at grade one to both histograms produces
twins of **every integer mass `M>=U_d`**. The product witness has
growing support as the number of supplied channels grows.

Combining II4 and II6 gives, for `d>=1`,

\[
\boxed{B_d+1\le M_{\min}(b,d)\le U_d<C_bB_d,\qquad
C_b:=\prod_{r=1}^{\infty}(1+b^{-r})<e^{1/(b-1)}.}
\tag{II7}
\]

The strict product comparison is valid because all omitted factors
exceed one. The exponential bound follows from `log(1+x)<x`.
A convenient rational bound, uniform in the base, is `C_b<=C_2<153/64`:
the first four factors at base two multiply to `2295/1024`; the
remaining logarithmic sum is less than `1/16`, and
`exp(1/16)<16/15`. Thus the explicit sufficient uniqueness mass and
explicit ambiguity mass differ by a factor less than `2.391`.

**Do not turn the upper witness into an exact optimum.** At `b=2,d=2`,

\[
A(z)=1-7z+14z^2-8z^3
\]

gives mass-15 twins. But

\[
(1+z)A(z)=1-6z+7z^2+6z^3-8z^4
\]

gives the smaller equal-mass pair

\[
c^+=(1,0,7,6,0),\qquad c^-=(0,6,0,0,8),\qquad M=14.
\]

Their responses at `1/2,1/4` are both `(7/2,49/32)`, while their zero
counts differ by one. Consequently the product construction is not
always mass-minimal. This note establishes `9<=M_min(2,2)<=14`, not
an exact value. In contrast the one-channel bounds coincide:
`M_min(b,1)=b+1`, witnessed by `(1,0,b)` and `(0,b+1,0)`.

## 4. II-03: the leading channel cost, with explicit finite brackets

Let `N_b(M)` be the least prefix length that identifies `c_0` for every
integer histogram of the given mass `M`. It may be smaller than a
particular reconstruction algorithm's channel count. For `M>=1`, set

\[
L_b(M)=1+\max\{d\ge0:U_d\le M\},\qquad U_0=1,
\]

\[
K_b(M)=\max\left\{1,
\left\lceil\frac{\sqrt{1+8\log_bM}-1}{2}\right\rceil\right\}.
\]

The twin construction and uniqueness theorem give

\[
\boxed{L_b(M)\le N_b(M)\le K_b(M),\qquad
K_b(M)-L_b(M)\in\{0,1\}.}
\tag{II8}
\]

For the last assertion, write `k=K_b(M)`. If `k=1`, then `1<=M<=b`
and both bounds equal one. If `k>=2`, minimality of `k` gives
`B_(k-1)<M<=B_k`. The elementary bound `U_j<B_(j+1)` implies
`U_(k-2)<M`, so `L_b(M)>=k-1`. The upper theorem prevents
`L_b(M)>k`. This is a bracket, not a decision of the one remaining
channel in every case. The implementation computes it using integer
products, avoiding logarithm rounding.

Since `log_b U_d=D_d+O_b(1)`, for every **fixed** base,

\[
\boxed{N_b(M)=\sqrt{2\log_bM}+O_b(1)\quad(M\to\infty).}
\tag{II9}
\]

The earlier even-degree sufficient rule is within **two channels** of
this worst-case optimum. Let `E` be the least even integer at least two
with `B_E>M`. It is sufficient by DF-03. If `E>=4`, minimality gives
`B_(E-2)<=M`, while `U_(E-3)<B_(E-2)`. Hence ambiguity persists with
`E-3` channels and `N_b(M)>=E-2`. If `E=2`, `N_b(M)>=1` suffices.
Thus `0<=E-N_b(M)<=2`. This does not say that the previous rule is
exactly optimal at every mass or that the upper witness is sharp.

At the even-degree endpoint `M=B_d`, the old strict ceiling condition
misses one boundary case. The zero source concentrated at grade `d`
has filtered value `-1`, so unmodified `ceil B` would return `-1`.
Clipping the answer below at zero repairs that endpoint: if `c_0>=1`,
the actual error is at most `(M-c_0)/B_d<1`; if `c_0=0`, clipping
returns zero. The existing interval certificate already clips its
lower endpoint. No prior code was modified here.

### The fixed-base restriction is load-bearing

If the observation node may depend on the mass, take `s=1/(M+1)` for
`M>=1`. Then

\[
0\le F(s)-c_0=\sum_{h\ge1}c_hs^h
\le s(M-c_0)\le\frac{M}{M+1}<1,
\]

so

\[
\boxed{c_0=\lfloor F(1/(M+1))\rfloor.}
\tag{II10}
\]

This is a one-sample exact reconstruction in a different access model.
It defeats any claim that II9 is a universal channel lower bound.
The supplied response still has to be authenticated and acquired at
the changed node, with sufficient exactness. Neither family establishes
a time, bit, or oracle-complexity improvement. The executable control
applies this one-sample rule to the mass-14 twins that collide under
the two fixed base-two channels. The root's companion
[ADAPTIVE_APERTURE.md](ADAPTIVE_APERTURE.md) develops the authentic
interval version and its arithmetic boundary separately.

## 5. II-04: normalized precision cannot be independent of mass

Suppose the observed coordinates are normalized responses `F(b^-r)/M`
with deterministic absolute error at most `eta` in every coordinate,
and the positive integer mass remains known exactly. For any `M>=1`,
compare

\[
c=(1,M-1),\qquad c'=(0,M).
\]

Their zero counts differ by one, and their normalized response gaps are
`(1-b^-r)/M`. The coordinatewise midpoint is a single reported packet
consistent with both sources whenever

\[
\boxed{\eta\ge\frac{1-b^{-d}}{2M}.}
\tag{II11}
\]

No deterministic decoder can certify both target counts from that same
packet. This proves an inverse-mass necessary precision scale for this
adversarial-error model. It does not assume independently random errors
or claim a statistical confidence bound. Normalizing the observations
does not remove the one-count precision cost.

A second witness isolates the final channel. Use the degree-`d-1`
twins, padded to any `M>=U_(d-1)`. Their first `d-1` responses match
exactly, while

\[
A_{b,d-1}(b^{-d})
=(1-b^{-d})\prod_{r=1}^{d-1}(1-b^{r-d})
=\prod_{j=1}^d(1-b^{-j})=:\kappa_{b,d}>0.
\tag{II12}
\]

Only the final normalized coordinate separates them, by
`kappa_(b,d)/M`. Its midpoint has ambiguity radius `kappa_(b,d)/(2M)`.
Thus errors in the last channel alone can hide the new integer
discriminator even when all earlier channels are exact.

The previous stable filter has the matching **order** of sufficient
precision. For even `d` with `epsilon_d M<=1/2`, normalized response
errors `eta<1/(36M)` imply
`epsilon_d M+18M eta<1`, so DF-03's authenticated integer interval
contains at most one integer. Constants are not claimed optimal.
In a fixed-point encoding where absolute error scales as `2^-p`, this
means `p=log_2 M+O(1)` accuracy bits are necessary at this scale and
sufficient with an adequate channel bank. This is a precision statement,
not an exact rational bit-length bound or a total-information theorem.

## 6. Why integrality, support and access cannot be silently changed

If arbitrary nonnegative rational masses are allowed, scale the twins
in II5 by any positive rational factor. Their common mass can become
arbitrarily small, and their zero masses still differ. For example,
scaling by `1/(1000 U_d)` produces mass `1/1000` twins with zero gap
`1/(1000 U_d)`. Thus there is no positive small-mass uniqueness threshold
for an unrestricted rational-valued target. This scaled example does
not retain a unit integer gap and must not be presented as doing so.

The integer theorem's conclusion can also change if one knows a support
ceiling, imposes source-specific relations, changes the nodes, or asks
only for a particular family of sources. Its witnesses use support
through `d+1` (through `d+2` in the improved example). They do not
inhabit every proposed arithmetic source class. The theorem is a
source-blind information obstruction under a declared packet, not a
substitute for authenticating the source map.

Full-histogram exact uniqueness is stronger than zero-count uniqueness
but is not a uniform stability theorem for all grades. Moving a unit
between arbitrarily high adjacent grades changes every fixed finite
bank by arbitrarily little while preserving the zero count. The noise
statement above deliberately targets the zero count.

## 7. Classical connection, validation and remaining uncertainty

The relation between exponential samples, moments and polynomial
annihilators is classical. For a primary comparison, see Peter, Potts
and Tasche, *Nonlinear Approximation by Sums of Exponentials and
Translates*, SIAM J. Sci. Comput. 33(4), 1920-1947 (2011),
[DOI 10.1137/100790094](https://doi.org/10.1137/100790094),
[author-hosted paper](https://www-user.tu-chemnitz.de/~potts/paper/nprony.pdf),
Section 2, Lemmas 2.1-2.2. That inspected passage relates zeros of an
annihilating polynomial to the kernel of a sampled exponential Hankel
matrix. It is context, not an imported proof of this integer mass bound:
here the known observation nodes are roots of a **difference generating
polynomial**. II1-II12 are derived above. No worldwide priority claim
is made for this specialization.

The executable companion is [integer_information.py](integer_information.py),
with [test_integer_information.py](test_integer_information.py). The
bounded validation command is:

```sh
python -m unittest discover -s research/2026-11-12/adaptive_boundary_resolution -p 'test_integer_information.py' -v
```

**Executed:** all 13 bounded tests passed after the final code change.
No full repository suite was run by this child agent; the root owns
repository-wide validation and publication.

The tests include 18 exact product witnesses over bases `2,3,5` and
degrees `1,...,6`, independently evaluated rational response sums;
the mass-15 versus mass-14 control; common padding; omission of the
mass root; a corrupted witness; the last-channel discriminator; common
noisy packets; rational rescaling; finite small-histogram enumeration;
and the mass-dependent one-sample escape. The finite enumeration is a
calibration, not the proof for arbitrary support. The production helper
rejects fractional or boolean counts instead of silently applying the
integer theorem to them.

**Open within this note:** the exact `M_min(b,d)` for `d>=2`, the last
undecided channel when the finite bounds differ, optimal noise constants,
and an efficient decoding algorithm with an explicit bit-cost model.
The next verdict-changing probe for the exact mass problem is a smaller
integer annihilator multiple or a sharper lower-bound argument. None
of these open refinements changes the proved leading channel cost for
the specified fixed-base family.
