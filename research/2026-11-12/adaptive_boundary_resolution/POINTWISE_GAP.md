# Adaptive filters: exact equivalence, individual schedules, and density one

Date: 2026-11-12. Local base inspected:
`5d9917031855f806fd5c1f9d8b4543ad3ca24bbf`. Its exact tree is published
as [commit f4151c4](https://github.com/femboy2112/SUCC/commit/f4151c4ae877ee43c4b7d130174b6bec1dbab9d6)
on the research branch. This bearing uses the preceding
[damped-filter proof](../holographic_boundary_filters/DAMPED_FILTERS.md)
and [fixed/adaptive resolution proof](../holographic_boundary_filters/FIXED_RESOLUTION.md).
No other new front was used in the derivations below.

**Result.** The positive-filter condition becomes exactly Goldbach once
the mass-only integer budget is sufficiently tight. At a much coarser
resolution, an actual per-midpoint degree schedule has the classical
positive aggregate, and an imported quantitative almost-all theorem gives
density-one filter positivity. Neither conclusion controls every large
midpoint. An extra authenticated masked-tail observation can strengthen
a particular certificate; acquiring that observation is an additional
source obligation.

## 1. Hole contract and notation

For an even degree `d>=2` and `0<t<=1/2`, write

\[
q_{d,t}(h)=\frac{t^h\prod_{j=1}^{d-1}(t^h-t^j)}
{\prod_{j=1}^{d-1}(1-t^j)},\qquad
\epsilon_{d,t}=t^{d(d+1)/2}.
\]

The preceding proof establishes, for integer `h>=0`,

\[
q(0)=1,\quad q(h)=0\ (1\le h<d),\quad
-\epsilon\le q(h)\le0\ (h\ge d),\quad q(d)=-\epsilon.
\tag{P0}
\]

For a nonnegative histogram `c_h` of mass at most `M`, put
`B=Σ_h c_h q(h)` and `k=c_0`. Then

\[
0\le k-B\le\epsilon(M-k).
\tag{P1}
\]

The authentic arithmetic histogram at midpoint `n>=2` has

\[
h_n(a)=\Omega(n+a)+\Omega(n-a)-2,\quad0\le a\le n-2,
\quad M_n=n-1,\quad c_0=G(n),
\]

where `G(n)` is the unordered Goldbach count for `2n`, including a prime
diagonal. Its damped response is `B_(d,t)(n)`.

| Proposed statement | Status and quantifier boundary |
|---|---|
| Sharp mass-only completeness and noise threshold | **PROVED LOCAL**, for every admissible integer histogram. |
| A sharper certificate from a masked tail | **PROVED LOCAL**, conditional on that additional authenticated response. |
| Positive aggregate for an individual degree schedule `d_n` | **PROVED LOCAL using classical PNT**, not restricted to one common degree per cutoff. |
| Density-one positivity at order `sqrt(log log n)` degree | **CLASSICAL RESULT TRANSFER**, using a verified quantitative representation theorem. No exceptional-set improvement. |
| Positivity at every sufficiently large midpoint | **OPEN**; under the completeness budget it is equivalent to the corresponding Goldbach assertion. |

The dependency cut is therefore explicit: an authentic pointwise response
estimate is missing. At tight resolution, asserting its sign simply
restates the target. The cheapest falsifiers below are equality-budget
histograms, noise at the adverse endpoint, and spectra with grade one but
no grade zero. These are source-blind countermodels, not counterexamples
to the actual Goldbach conjecture.

## 2. PG01: the exact proof-equivalence boundary — PROVED LOCAL

Fix integer `M>=1`, `d`, and `t`. The following are equivalent:

1. For every nonnegative integer histogram of total mass at most `M`,
   `B>0` if and only if `c_0>0`.
2. `epsilon(M−1)<1`.

**Proof.** If `c_0=0`, P0 gives `B<=0`. If `c_0=k>=1`, P1 gives

\[
B\ge k-\epsilon(M-k)
\ge1-\epsilon(M-1)>0.
\]

Conversely, take `c_0=1`, `c_d=M−1`, and every other count zero. The
tail bound is attained, so `B=1−epsilon(M−1)`. It is nonpositive
when the strict budget fails. QED.

For authentic arithmetic, the sufficient completeness condition is

\[
\boxed{\epsilon_{d_n,t}(n-2)<1.}
\tag{P2}
\]

Whenever P2 holds at a midpoint,

\[
\boxed{B_{d_n,t}(n)>0\quad\Longleftrightarrow\quad G(n)>0.}
\tag{P3}
\]

If it holds for every `n>=N_0`, universally positive filtered responses
on that same tail are equivalent to Goldbach on that tail. This is an
exact useful reformulation, not a weaker arithmetic premise.

Necessity above is for the **mass-only histogram class**. Failure of P2
does not imply an arithmetic failure. At `n=10,d=2,t=1/2`, equality
holds in P2's budget, yet the genuine response is positive and `G(10)=2`.
A known support restriction can also remove the worst grade `d`; then
the optimal mass-only leakage on that smaller class may be below
`epsilon`, or zero. No such source restriction is silently assumed.

### Sharper exact integer recovery

Under the same strict budget,

\[
\boxed{c_0=\max\{0,\lceil B\rceil\}.}
\tag{P4}
\]

For `c_0>=1`, P1 gives `c_0−1<B<=c_0`; for `c_0=0`, `B<=0`
and the clamp returns zero. The same extremal histogram shows that the
budget is sharp for this recovery rule over the mass-only class.
Thus clamping improves the earlier sufficient condition
`epsilon M<1` for the unmodified rule `ceil(B)`. For example,
`d=2,t=1/2,M=8,c_2=8` gives `B=−1`; the unclamped ceiling is wrong,
whereas P4 returns zero and `epsilon(M−1)=7/8<1`.

Integrality matters. The real histogram `c_0=1/16,c_2=15/16`, of
mass one, has positive zero mass but `B=−7/128` at `d=2,t=1/2`.
A source cannot acquire an integer-count guarantee merely by applying
an integer-returning function to an unverified response.

### Noisy completeness pays two errors

Suppose `|Bhat−B|<=E` and the reported lower certificate is
`L=Bhat−E`. It remains sound: `L<=B<=c_0`. It is positive for
**every** admissible noise realization whenever `c_0>=1`, for every
histogram of mass at most `M`, exactly when

\[
\boxed{\epsilon(M-1)+2E<1.}
\tag{P5}
\]

The lower bound is `L>=1−epsilon(M−1)−2E`. Equality is attained by
the extremal histogram above and `Bhat=B−E`. One error measures how
far the observation may have fallen, and the certificate subtracts
another. For one supplied observation the actual test is simply `L>0`;
P5 is the stronger worst-noise completeness guarantee.

## 3. PG02: additional tail information strengthens a certificate

The mass estimate can ignore many cancelled low grades. An authenticated
bound `T_d>=Σ_(h>=d)c_h` gives `c_0−B<=epsilon T_d`.
A weighted tail gives a useful **lower correction** as well.
Define the extra observable

\[
U_d(t)=\sum_{h\ge d}c_ht^h,\quad
\lambda_d=t^{d(d-1)/2},\quad
K_d=\frac{\lambda_d}{\prod_{j=1}^{d-1}(1-t^j)}.
\]

For `h>=d`, direct factorization gives

\[
\frac{-q(h)}{t^h}
=K_d\prod_{j=1}^{d-1}(1-t^{h-j}).
\]

The product increases from `Π_(j=1)^(d−1)(1−t^j)` at `h=d`
toward one. Consequently

\[
\boxed{
B+\lambda_dU_d(t)\le c_0\le B+K_dU_d(t),\qquad
c_0-B\le\epsilon T_d.
}
\tag{P6}
\]

The lower tail factor is attained at grade `d`; the upper factor is
the limiting supremum. This proof works for countably many grades with
finite nonnegative mass. No finite grade ceiling is needed.

If authenticated intervals are supplied for `B` and `U_d`, use their
lower endpoints on the left and upper endpoints on the right. Intersect
the result with `[0,M]`, the previous upper bound
`(B_hi+epsilon M)/(1+epsilon)`, and `B_hi+epsilon T_d` when available.
The executable certificate implements these rational interval operations.

At `d=2,t=1/2,c_0=1,c_2=8`, the original lower response is zero.
Here `U_d=2`, `lambda_d=1/2`, and the corrected lower bound is one.
Thus the additional observation can repair a particular failed filter.
It is not available free from the unmasked responses: `U_d` includes
the spectral cutoff `1_(h>=d)`. Authenticating or deriving that cutoff
is a new source obligation. This enlarged observation class is outside
the previous fixed finite bank of unmasked damped exponentials.

## 4. PG03: genuinely per-midpoint adaptive mean — PROVED LOCAL

Fix `0<t<=1/2`. Choose an even degree `d_n>=2` separately for each
midpoint and set `epsilon_n=t^[d_n(d_n+1)/2]`. No monotonicity is
required. If

\[
\epsilon_n=o((\log n)^{-2}),
\tag{P7}
\]

then

\[
\boxed{
\sum_{2\le n\le X}B_{d_n,t}(n)
\sim\frac{X^2}{(\log X)^2}>0.
}
\tag{P8}
\]

This extends previous FR04, whose single degree `d_X` was common to all
terms below one cutoff. Here an already chosen midpoint retains its own
degree when `X` changes.

**Proof.** P1 gives the exact finite comparison

\[
0\le\sum_{n\le X}\bigl[G(n)-B_{d_n,t}(n)\bigr]
\le\sum_{n\le X}\epsilon_n(n-1).
\tag{P9}
\]

The last sum is `o(X²/log²X)`. To see the quantifiers, fix `eta>0`.
For all sufficiently large `n`, P7 gives
`epsilon_n<=eta/(log n)²`. The part `n<=sqrt(X)` is `O(X)`, since
`epsilon_n<=1/8`. On the remaining range, for sufficiently large `X`,
`log n>=(log X)/2`, so the contribution is at most
`2 eta X²/(log X)²`. Let `eta` tend to zero.

The classical prime number theorem, applied to the nonnegative triangle
of odd-prime pairs, gives `Σ_(n<=X)G(n)~X²/log²X`; the proof and
unordered-pair normalization are recorded in previous FR04. Subtracting
P9 proves P8. No uniform Selberg–Delange theorem for moving nodes is
used. QED.

For any fixed `delta>0`, a sufficient individual schedule is

\[
d_n\ge
\sqrt{\frac{(4+\delta)\log\log n}{\log(1/t)}},
\tag{P10}
\]

rounded up to an even integer at least two for large `n`, with arbitrary
valid choices at the finitely many earlier midpoints. It yields
`epsilon_n<=(log n)^(-2−delta/2)`. This is a sufficient schedule;
no optimality is claimed.

The same conclusion holds for reported lower certificates
`L_n=Bhat_n−E_n` if `|Bhat_n−B_n|<=E_n` and
`Σ_(n<=X)E_n=o(X²/log²X)`, because `B_n−2E_n<=L_n<=B_n`.
The pointwise condition `E_n=o(n/log²n)` suffices by the same split.
Subtracting the cumulative asymptotics also gives a positive sum on
each sufficiently large fixed-ratio shell. None of these sum statements
requires positivity at each midpoint.

## 5. PG04: quantitative almost-all counts transfer to density one

### The precise classical import

Write

\[
R_2(N)=\#\{(p,q):p+q=N,\ p,q\text{ prime}\},
\quad
J_2(N)=\sum_{m=2}^{N-2}\frac1{\log m\log(N-m)}.
\]

The first page of R. C. Vaughan's author-hosted
[*A new estimate for the exceptional set in Goldbach's problem*](https://personal.science.psu.edu/rcv4/personal/Publications/StLouis72.pdf)
(1973, printed page 315) states the classical unconditional estimate

\[
\sum_{N\le Y}|R_2(N)-J_2(N)\mathfrak S(N)|^2
\ll_A Y^3(\log Y)^{-A}\qquad\text{for every fixed }A>0.
\tag{MS}
\]

The definitions and formula were freshly inspected through retrieval
and OCR of the author-hosted scan. This is an **imported classical
theorem**, not a proof supplied by the present filter work. The stronger
displayed formula (1) in that paper has an additional possible
exceptional-zero term; that different formula is not the import here.
The later research exposition by [Bhowmik–Grimmelt, Section 4,
Theorem 4.3](https://link.springer.com/content/pdf/10.1007/s10476-026-00191-z.pdf)
was also inspected as provenance context. Both belong to the same
classical circle-method source family. No effective numerical threshold
or improved exceptional-set exponent is inferred.

For even `N`, the singular series in MS is

\[
\mathfrak S(N)=2C_2
\prod_{\substack{p\mid N\\p>2}}\frac{p-1}{p-2}
\ge2C_2>0,
\qquad C_2=\prod_{p>2}\left(1-\frac1{(p-1)^2}\right).
\tag{P11}
\]

The infinite product is positive because its factors are positive and
their deficits are summable. The import counts genuine primes directly;
no weighted prime-power count is substituted into the target.

### Exact deduction of the quantitative good set

For `N>=4`, each denominator in `J_2(N)` is at most `log²N`, so
`J_2(N)>=(N−3)/log²N`. For an even `N` outside the set

\[
\mathcal E=\{N:\ R_2(N)<\tfrac12J_2(N)\mathfrak S(N)\},
\]

we therefore have

\[
R_2(N)\ge C_2\frac{N-3}{\log^2N}.
\]

On a dyadic range `Y<N<=2Y`, every member of `mathcal E` has
`|R_2−J_2 mathfrak S|` bounded below by a positive constant times
`Y/log²Y`. Apply MS with exponent `A+4` and divide by this squared
threshold. The number of exceptional even `N` in that range is
`O_A(Y/log^A Y)`. Dyadic summation gives the same shape up to `Y`.

The exact ordered/unordered relation is

\[
G(n)=\frac{R_2(2n)+\mathbf1_{\{n\text{ prime}\}}}{2}.
\]

For `n>=3`, use `2n−3>=n` and `log(2n)<=2 log n`. Outside the
inherited exceptional set this gives the explicit convenient bound

\[
\boxed{G(n)\ge\kappa\frac n{\log^2n},\qquad \kappa=C_2/8>0.}
\tag{P12}
\]

For every fixed `A>0`, at most `O_A(X/log^A X)` midpoints `n<=X`
fail this bound. Constants and the starting point are not computed here.

### Transfer to the adaptive filtered certificate

Under P7, the loss `epsilon_n(n−1)` is `o(n/log²n)`. P1 and P12
therefore give, at every sufficiently large midpoint in the good set,

\[
B_{d_n,t}(n)\ge\frac\kappa2\frac n{\log^2n}>0.
\]

Hence

\[
\boxed{
\#\{2\le n\le X:B_{d_n,t}(n)\le0\}
\ll_A\frac X{\log^A X}
\quad\text{for every fixed }A>0.
}
\tag{P13}
\]

The same transfer holds for lower reports `Bhat_n−E_n` if
`E_n=o(n/log²n)`. Their extra worst-case depression is `2E_n`.
The earlier coefficient norm below nine can convert authenticated
individual response-error budgets into such a filtered-error budget.
This is a required source accuracy, not an assertion that the responses
have already been acquired at that accuracy.

**Novelty tax.** P13 recovers an existing almost-all arithmetic result
through the filter envelope. Its exceptions are controlled by the
imported representation estimate; no stronger exceptional-set bound is
proved. Mere almost-all existence `G(n)>=1` would be insufficient at
P10's coarse resolution, since `epsilon_n n` need not be below one.
The quantitative count size in P12 is the load-bearing extra input.

## 6. Countermodels that retain the missing quantifier

A Chen-shaped premise `min h<=1` allows `c_1=M,c_0=0`. Every even
filter annihilates that entire histogram, so `B=0`. Existence of grade
zero **or one** cannot be promoted to existence of grade zero.
This is a countermodel to that implication in the stated grade class,
not an arithmetic counterexample to Chen's theorem or Goldbach.

Likewise, the two histograms `(c_0,c_1)=(2,0)` and `(0,2)` have a
positive sum of lower responses, while the second has no zero grade.
An asymptotic-strength version is also elementary. For sufficiently
large `n` outside the powers of two, set

\[
c_0(n)=\left\lfloor\frac{2n}{\log^2n}\right\rfloor,
\qquad c_1(n)=n-1-c_0(n),
\]

and at powers of two set `c_0(n)=0,c_1(n)=n−1`. Fill the finitely
many early indices with any nonnegative histograms. These are integer
histograms of the correct mass `n−1`, supported in grades zero and one.
For every allowed filter their response is exactly `c_0(n)`.

Elementary summation gives `Σ_(n<=X)2n/log²n~X²/log²X`. Rounding
costs `O(X)`; deleting the powers of two also costs `O(X)`, since their
total size below `X` is less than `2X`. Thus this counterfeit source has
the same leading aggregate scale, a density-one positive response, and
`min h<=1` at every index. It still has infinitely many zero-grade
failures. Source authentication and the all-midpoint quantifier cannot
be supplied by these aggregate successes.

## 7. Executable scope and verdict

[pointwise_certificates.py](pointwise_certificates.py) supplies exact
rational contracts for the sharp witness margin, clamped integer
recovery, and masked-tail intervals. Its inputs do not authenticate
themselves. Integral-count conclusions require the stated promise.
Floats, booleans masquerading as integers, invalid degrees, invalid
parameter ranges, and contradictory interval packets are rejected.

[test_pointwise_certificates.py](test_pointwise_certificates.py) ran
successfully with **13 tests**. The checks include independent Lagrange
versus product evaluation; strict/equality and adverse-noise budgets;
the real-mass mutation; a grade-1000 tail; noisy tail intervals;
Chen-shaped and positive-mean controls; and finite arithmetic at
midpoints `2,...,65` with different degrees at different midpoints.
That arithmetic check compares trial-factorization grades against a
separate direct primality predicate and verifies the exact aggregate
error inequality. It does not fit or certify an asymptotic law.

Reproduce the focused run from the repository root:

```sh
python -m unittest discover -s research/2026-11-12/adaptive_boundary_resolution -p test_pointwise_certificates.py -v
```

This bearing did not run a full repository suite. It is a same-model
research derivation with independent exact calculations, not an
external referee. An unsolicited description of another new front was
reported to the root and was not used or audited here.

The earned change is a sharper equivalence boundary and a true
per-target adaptive aggregate theorem, followed by an explicitly paid
classical density-one transfer. The remaining all-target response
estimate is open. At the complete integer resolution it is an exact
reformulation of Goldbach; at coarser resolution, a universal positive
bound is a sufficient assertion whose converse has not been established
for the arithmetic source. It is strictly stronger than mere zero-grade
existence over the mass-only histogram class, as the equality-budget
countermodel shows. Promoting it for the actual source requires new
pointwise arithmetic control.
