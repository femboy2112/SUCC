# A source-specific obstruction to every fixed finite damped lower filter

**Status: PROVED LOCAL, using an explicitly imported classical mean-value
theorem.** For the genuine arithmetic grading by the number of prime
factors, every fixed finite bank of damped exponentials that is a
pointwise zero-grade minorant has a negative summatory response for all
sufficiently large cutoffs. In particular, every fixed even-degree filter
from [DAMPED_FILTERS.md](DAMPED_FILTERS.md) fails to certify positivity at
infinitely many midpoints.

This is an arithmetic restriction on a specified observation class. It
does **not** assert eventual negativity at each midpoint, refute Goldbach,
or cover filters whose parameters change with the midpoint. The result
uses actual `Ω` weights; it is stronger than a source-blind counterfeit
histogram. The independent same-model derivation is recorded in
[FIXED_RESOLUTION_AUDIT.md](FIXED_RESOLUTION_AUDIT.md).

## 1. Source, target, and classical import

Let `Ω(m)` count prime factors with multiplicity, with `Ω(1)=0`.
For an integer `n>=2` and a fixed real `0<s<1`, define the joint response

\[
F_n(s)=\sum_{a=0}^{n-2}s^{\Omega(n+a)+\Omega(n-a)-2}.
\tag{FR0}
\]

The endpoints are at least two. Grade zero is exactly an unordered
Goldbach pair for `2n`, including the diagonal pair when `n` is prime.
All sums below use this convention.

The sole substantial analytic import is the classical fixed-parameter
mean

\[
A_s(x):=\sum_{m\le x}s^{\Omega(m)}
=C_s x(\log x)^{s-1}
\left(1+O_s\!\left(\frac1{\log x}\right)\right),
\qquad
C_s=\frac1{\Gamma(s)}\prod_p\frac{(1-1/p)^s}{1-s/p}>0.
\tag{SD}
\]

[Cellarosi, equations (10)–(11), PDF page 5](https://arxiv.org/pdf/1304.6610v2)
states this formula in the larger range `|s|<2`. The version needed here
also follows from [de la Bretèche–Tenenbaum, Theorem 2.1 and equation
(2.1), PDF page 4](https://tenenb.perso.math.cnrs.fr/PPP/On-SD.pdf).
Both passages were inspected. They belong to the same classical
Selberg–Delange source family; citing both is not independent arithmetic
corroboration. The mean theorem is imported, not reproved here.

For completeness, its second formulation has directly checkable
hypotheses for `f_s(m)=s^Ω(m)`. This function is nonnegative and
completely multiplicative. With the theorem's `r=s`, `A=2`, and
`σ=3/4`, the prime-sum hypothesis follows from the classical quantitative
prime number theorem
`Σ_(p<=x) log p=x+O(x/log²x)`. The prime-power condition holds because

\[
\sum_p\left\{\frac{s^2}{p^{3/2}}+
\sum_{\nu\ge2}\frac{s^\nu}{p^{3\nu/4}}\right\}
\ll_s\sum_p p^{-3/2}<\infty.
\]

Its Euler factor is `Σ_(ν>=0)s^ν/p^ν=(1−s/p)^−1`, giving `C_s`.
The logarithm of the normalized Euler factor is `O_s(p^−2)`; hence
the product converges to a strictly positive number. All constants and
limits in this note are for **fixed** parameters unless stated otherwise.

## 2. FR01: the averaged joint response — PROVED LOCAL

**Theorem.** For every fixed `0<s<1`,

\[
\boxed{
\sum_{2\le n\le X} F_n(s)
\sim K_s X^2(\log X)^{2s-2},\qquad
K_s=\frac{C_s^2}{s^2}
\left[\left(1-\frac s2\right)^2+\left(\frac s2\right)^2\right]>0.
}
\tag{FR1}
\]

It suffices to take integer `X`; replacing a real cutoff by its floor
has no effect on the stated asymptotic.

### Step 1: the exact parity constants

Put `w_s(m)=s^(Ω(m)−1)` for `m>=2`. Since `Ω(2m)=1+Ω(m)`, the
even and odd cumulative weights obey the exact identities, for `x>=2`,

\[
W_{s,e}(x):=\sum_{\substack{2\le m\le x\\m\text{ even}}}w_s(m)
=A_s(x/2),
\]

\[
W_{s,o}(x):=\sum_{\substack{2\le m\le x\\m\text{ odd}}}w_s(m)
=\frac{A_s(x)}s-A_s(x/2)-\frac1s.
\tag{FR2}
\]

The last term removes `m=1`. Applying SD at `x` and `x/2` gives

\[
W_{s,e}(x)\sim k_{s,e}x(\log x)^{s-1},\qquad
W_{s,o}(x)\sim k_{s,o}x(\log x)^{s-1},
\]

\[
k_{s,e}=\frac{C_s}{2},\qquad
k_{s,o}=C_s\left(\frac1s-\frac12\right).
\tag{FR3}
\]

Parity is not assigned an unweighted factor of one half: even integers
carry an extra factor `s` before the normalization in `w_s`.

### Step 2: a nonnegative triangular-sum lemma

Suppose a nonnegative sequence `v(m)` has

\[
V(x)=\sum_{m\le x}v(m)\sim kx(\log x)^\beta,\qquad k>0,
\]

with fixed `β`. Then

\[
\sum_{a+b\le Y}v(a)v(b)
\sim\frac{k^2}{2}Y^2(\log Y)^{2\beta}.
\tag{FR4}
\]

Here and below the sequence can be set to zero outside one parity class.
To prove FR4, form the finite measures on `[0,1]`

\[
\mu_Y=\frac1{Y(\log Y)^\beta}
\sum_{m\le Y}v(m)\,\delta_{m/Y}.
\]

For each fixed `0<u<=1`,

\[
\mu_Y([0,u])
=\frac{V(uY)}{Y(\log Y)^\beta}\longrightarrow ku.
\]

Together with convergence of the total mass, this is weak convergence
to `k` times Lebesgue measure. Its product measures converge to `k²`
times area measure. The triangle `u+v<=1` has area `1/2` and boundary
of zero limiting measure. Taking its measure proves FR4. Equivalently,
one can squeeze the triangle between finite rectangle unions and let
their mesh tend to zero. This argument uses positivity and elementary
product measures, not a pointwise additive-correlation hypothesis.

### Step 3: ordered versus unordered pairs

Define the ordered same-parity triangle

\[
T_s(Y)=\sum_{\substack{p,q\ge2\\p+q\le Y\\p\equiv q\pmod2}}
w_s(p)w_s(q).
\]

FR3–FR4 give

\[
T_s(Y)\sim\frac{k_{s,e}^2+k_{s,o}^2}{2}
Y^2(\log Y)^{2s-2}.
\tag{FR5}
\]

Every summand in FR0 corresponds to the unordered pair
`{p,q}={n+a,n−a}` with `p+q=2n`. Off-diagonal pairs appear twice
in `T_s(2X)` and diagonal pairs once. Thus the exact conversion is

\[
\sum_{2\le n\le X}F_n(s)
=\frac12\left[T_s(2X)+D_s(X)\right],\qquad
D_s(X)=\sum_{2\le m\le X}w_s(m)^2.
\tag{FR6}
\]

For `m>=2`, `0<w_s(m)<=1`, so `D_s(X)<=X`. This is negligible
relative to `X²(log X)^(2s−2)`. Inserting `Y=2X` in FR5 pays a factor
four, and conversion to unordered pairs pays a factor one half. The
constant is consequently

\[
k_{s,e}^2+k_{s,o}^2
=C_s^2\left[\frac14+\left(\frac1s-\frac12\right)^2\right]
=K_s,
\]

which proves FR1.

The endpoint `1` was already excluded in FR2 and FR6. If it is
temporarily included with artificial weight `w_s(1)=1/s`, deleting
ordered pairs incident to it costs
`O_s(A_s(2X))=O_s(X(log X)^(s−1))`, again negligible. Neither that
endpoint nor the diagonal can be discarded before checking its cost.

**Normalization controls.** At `X=3`, the genuine response sum is
`F_2(s)+F_3(s)=2+s`. The ordered triangle is `2+2s` and the diagonal
is `2`, recovering `2+s` from FR6. As a separate endpoint calibration,
at `s=1` direct counting gives `Σ_(n=2)^X(n−1)=X(X−1)/2`; the
displayed constant extends to `K_1=1/2`, as required. These identities
check conventions; no finite computation proves the asymptotic.

## 3. FR02: every fixed even filter has a negative mean — PROVED LOCAL

Fix an even integer `d>=2` and `0<t<=1/2`. Let

\[
Q_{d,t}(z)=\frac{z\prod_{j=1}^{d-1}(z-t^j)}
{\prod_{j=1}^{d-1}(1-t^j)}=\sum_{r=1}^d a_rz^r,
\qquad
B_{d,t}(n)=\sum_{r=1}^d a_rF_n(t^r).
\]

These are the previously certified lower filters, with fixed degree
and damping. Their first coefficient is

\[
a_1=\frac{(-1)^{d-1}t^{d(d-1)/2}}
{\prod_{j=1}^{d-1}(1-t^j)}<0.
\tag{FR7}
\]

**Theorem.**

\[
\boxed{
\sum_{2\le n\le X}B_{d,t}(n)
\sim a_1K_tX^2(\log X)^{2t-2}<0.
}
\tag{FR8}
\]

The inequality means the sum is negative for all sufficiently large
`X`. It is not a claim about each individual summand.

**Proof.** FR01 applies to each of the finitely many fixed nodes `t^r`.
For every `r>=2`,

\[
\frac{X^2(\log X)^{2t^r-2}}
{X^2(\log X)^{2t-2}}
=(\log X)^{-2(t-t^r)}\longrightarrow0.
\]

Consequently the `r=1` term dominates the fixed linear combination,
and its coefficient is strictly negative by FR7. QED.

The right side tends to minus infinity. If only finitely many
`B_(d,t)(n)` were negative, the cumulative sum would be bounded below
by the sum of those finitely many negative terms. Therefore infinitely
many responses are negative.

More precisely, for every fixed `0<α<1`, subtraction of FR8 at `X`
and `αX` gives

\[
\sum_{\alpha X<n\le X}B_{d,t}(n)
\sim a_1K_t(1-\alpha^2)X^2(\log X)^{2t-2}<0.
\tag{FR9}
\]

Every sufficiently large multiplicative shell therefore contains a
midpoint at which this fixed lower filter is negative. It can still
be positive at other midpoints in the same shell.

## 4. FR03: every fixed finite damped minorant has this obstruction

The obstruction is not specific to the geometric interpolation formula.
Let

\[
1>s_1>s_2>\cdots>s_m>0,\qquad
q(h)=\sum_{j=1}^m b_js_j^h,
\]

where the nodes and real coefficients are fixed and zero coefficients
have been removed. Suppose this is a pointwise zero-grade minorant:

\[
q(0)=1,\qquad q(h)\le0\quad\text{for every integer }h\ge1.
\tag{FR10}
\]

Define its authentic arithmetic response by

\[
B_q(n)=\sum_{a=0}^{n-2}q\!\left(\Omega(n+a)+\Omega(n-a)-2\right)
=\sum_{j=1}^m b_jF_n(s_j).
\]

It is a valid lower bound for the unordered Goldbach count by FR10.
Nevertheless,

\[
\boxed{
b_1<0,\qquad
\sum_{2\le n\le X}B_q(n)
\sim b_1K_{s_1}X^2(\log X)^{2s_1-2}<0.
}
\tag{FR11}
\]

**Proof.** Divide FR10 by `s_1^h` and send the integer `h` to
infinity. Every ratio `(s_j/s_1)^h` for `j>=2` tends to zero, so
`b_1<=0`. It is nonzero by the indexing convention; therefore `b_1<0`.
FR01 and the strict ordering of the nodes make every `j>=2` summatory
term lower order than the `j=1` term, proving FR11. QED.

The same shell conclusion as FR9 follows with `b_1,K_(s_1),s_1`.
Thus no single fixed finite damped bank obeying FR10 can certify a
positive Goldbach count at every sufficiently large midpoint.

## 5. What this closes, and what it leaves open

The exact filter theorem and this arithmetic obstruction coexist.
For each fixed finite histogram, increasing even degree improves its
lower bound toward the true zero-grade mass. Holding the degree fixed
and letting the arithmetic source size grow is a different limit;
FR02 proves that its signed average is eventually negative. Exchanging
those limits would be an error.

The classical input is a one-variable mean of multiplicative weights.
It is sufficient after averaging over all midpoints because the additive
constraint becomes a two-dimensional triangle. It does not factor the
coupled response at one midpoint into two marginal expectations. That
pointwise additive estimate remains the hard arithmetic obligation.

The result excludes only the stated fixed finite observation class.
It does not exclude:

- nodes, degree, or coefficients depending on the midpoint or cutoff;
- an exact node at zero, which already supplies the desired projector;
- other authenticated boundary observables or infinite filter banks;
- source-specific certificates whose validity does not require a
  pointwise minorant at every integer grade.

No threshold of negativity is numerically claimed. No uniformity in
`d`, `t`, or nodes approaching zero is inherited from the fixed-parameter
argument. In particular, the successful finite count-recovery budget
`t^[d(d+1)/2](n−1)<1` is unaffected: it prescribes a changing resolution
as `n` grows and still requires authentic response acquisition.

The practical next cut is an adaptive source estimate with its
parameter range and errors paid explicitly. It must not assume
positivity of a fixed finite damped minorant at all large targets;
FR03 rules that route out. See [NEXT.md](NEXT.md) for the continuation
contract. This is a locally proved restriction obtained from classical
mean-value theory, not a claim of global novelty or a solution of
binary Goldbach.

## 6. FR04: an adaptive bank recovers a positive mean — PROVED LOCAL

The fixed-bank obstruction has a quantitative positive counterpart.
It follows from the existing filter envelope and the classical prime
number theorem; it does not require a uniform Selberg–Delange estimate
at nodes tending to zero.

Fix `0<t<=1/2`. For each integer cutoff `X>=2`, choose an even
`d_X>=2`, and put

\[
\epsilon_X=t^{d_X(d_X+1)/2}.
\]

The same degree `d_X` is used for **every midpoint in this cutoff's
sum**. The bank may change when the cutoff changes.

**Theorem.** If `epsilon_X=o((log X)^−2)`, then

\[
\boxed{
\sum_{2\le n\le X}B_{d_X,t}(n)
\sim\frac{X^2}{(\log X)^2}>0.
}
\tag{FR12}
\]

For any fixed `delta>0`, a sufficient schedule is to take `d_X>=2`
even and at least

\[
\boxed{
\sqrt{\frac{(4+\delta)\log\log X}{\log(1/t)}}
}
\tag{FR13}
\]

for large `X`, rounding this lower bound up to the next even integer.
Thus an order `sqrt(log log X)` degree suffices for this aggregate
conclusion. This is a sufficient schedule, not a claim of optimality.

**Proof of the prime-pair mean.** Let `G(n)` be the actual unordered
Goldbach count for `2n`, including a prime diagonal. The prime number
theorem gives the cumulative odd-prime weight

\[
\sum_{\substack{p\le y\\p\text{ odd prime}}}1
\sim\frac{y}{\log y}.
\]

Apply the triangular-sum lemma FR4 to the indicator of odd primes,
with `k=1` and `beta=−1`. Its ordered sum over `p+q<=2X` is
asymptotic to `2X²/(log X)²`. The only even-prime pair with even
sum is `(2,2)`. Converting to unordered pairs adds the diagonal
correction `O(π(X))` and divides by two. Consequently

\[
\sum_{2\le n\le X}G(n)
\sim\frac{X^2}{(\log X)^2}.
\tag{FR14}
\]

This is a classical aggregate consequence of the prime number theorem.
It assumes no positivity at any particular midpoint.

**Proof of FR12.** The all-grade envelope in DAMPED_FILTERS.md applies
at every chosen finite degree without an asymptotic parameter
restriction. Since the histogram at midpoint `n` has mass `n−1`,

\[
0\le G(n)-B_{d_X,t}(n)
\le\epsilon_X\bigl(n-1-G(n)\bigr)
\le\epsilon_X(n-1).
\]

Summing this exact inequality yields

\[
\boxed{
0\le\sum_{2\le n\le X}
\bigl[G(n)-B_{d_X,t}(n)\bigr]
\le\epsilon_X\frac{X(X-1)}2.
}
\tag{FR15}
\]

Under the stated hypothesis, FR15 is `o(X²/(log X)²)`.
Combining with FR14 proves FR12. Finally, FR13 implies

\[
\epsilon_X
=\exp\!\left[-\frac{d_X(d_X+1)}2\log(1/t)\right]
\le(\log X)^{-2-\delta/2}
=o((\log X)^{-2}),
\]

which proves the sufficient schedule. QED.

FR04 is a known-result recovery and an application of the quantitative
filter envelope, with no worldwide-priority claim. It supplies an
explicit example of the limit-order distinction: every fixed finite
damped minorant has a negative eventual mean, while this changing
bank has a positive mean. There is no contradiction because its degree
and smallest node change with `X`.

This degree schedule concerns mean response, not exact integer recovery
at every source of mass `X`, which has the stronger sufficient budget
`epsilon_X(X−1)<1`. It also supplies no computational speedup or free
response acquisition. A positive aggregate allows failed certificates
and even zero target counts at individual midpoints. The remaining
pointwise gap is an authenticated, error-paid lower estimate for the
joint filtered response at each sufficiently large midpoint; FR04 does
not provide it.
