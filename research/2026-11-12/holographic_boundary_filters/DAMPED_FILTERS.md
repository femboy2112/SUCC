# Cancel low grades from the boundary: a stable damped projector

**Result:** an explicit family of signed boundary filters approximates the
zero-grade mass with error `M*t^[d(d+1)/2]` and coefficient amplification
strictly below nine, uniformly in the even degree `d` and `0<t<=1/2`.
There is no upper bound on the allowed **integer** grades. The arithmetic
application still needs source-authenticated response estimates; binary
Goldbach is **OPEN**.

This continuation was triggered by a failure product of the first round:
the fixed quadratic filter in [GOLDBACH_FILTERS.md](GOLDBACH_FILTERS.md)
certified only nine small midpoints in the independent scan through 257.
The new parameters and arithmetic windows were frozen in
[PREREGISTRATION_DAMPED.md](PREREGISTRATION_DAMPED.md) before execution.

## 1. The object and its boundary responses

Let `c_h>=0`, `h in N_0`, have finite total mass

\[
M=\sum_{h\ge0}c_h<\infty,\qquad F(s)=\sum_{h\ge0}c_hs^h\quad(0<s<1).
\]

The desired internal quantity is `c_0=F(0)`. The boundary can supply
`F(t),F(t^2),...,F(t^d)` with stated absolute errors. It need not identify
every grade. The series converge absolutely; finite support is allowed
but is not needed for the inequalities.

For the Goldbach application, use

\[
h_n(a)=\Omega(n+a)+\Omega(n-a)-2,\quad 0\le a\le n-2,
\qquad c_h=\#\{a:h_n(a)=h\}.
\]

Then `M=n-1`, `c_0=G(n)`, and

\[
F_n(s)=\sum_{a=0}^{n-2}s^{\Omega(n+a)+\Omega(n-a)-2}.
\tag{DF0}
\]

These are coherent, shared-midpoint responses. They are **not** the product
of two separately averaged marginal prime distributions. Evaluating DF0
by factoring every endpoint is the demo's actual method, not a new fast
Goldbach algorithm. A prospective analytic estimate for DF0 must retain
this additive coupling.

## 2. DF-01: the filter and the all-grade error — PROVED LOCAL

For an even integer `d>=2` and `0<t<=1/2`, define

\[
Q_{d,t}(z)=
\frac{z\prod_{j=1}^{d-1}(z-t^j)}{\prod_{j=1}^{d-1}(1-t^j)}
=\sum_{r=1}^d a_rz^r,
\qquad q_{d,t}(h)=Q_{d,t}(t^h),
\qquad \epsilon_d=t^{d(d+1)/2}.
\tag{DF1}
\]

**Theorem.** At integer grades,

\[
q_{d,t}(0)=1,\qquad q_{d,t}(h)=0\quad(1\le h<d),\qquad
-\epsilon_d\le q_{d,t}(h)\le0\quad(h\ge d).
\tag{DF2}
\]

The lower endpoint is attained at `h=d`. Consequently the measured signed
combination

\[
B_{d,t}=\sum_{r=1}^d a_r F(t^r)
\]

satisfies

\[
\boxed{c_0-\epsilon_d(M-c_0)\le B_{d,t}\le c_0.}
\tag{DF3}
\]

**Proof.** The first two assertions follow from the roots and normalization.
For `h>=d`, all `d-1` factors `t^h-t^j` are negative, and their number is
odd. Thus `q(h)<0`. Its absolute value is

\[
g(h)=\frac{t^{h+d(d-1)/2}
\prod_{j=1}^{d-1}(1-t^{h-j})}{\prod_{j=1}^{d-1}(1-t^j)}.
\]

At `h=d` the product cancels, giving `g(d)=epsilon_d`. Successive ratios
satisfy

\[
\frac{g(h+1)}{g(h)}=
t\,\frac{1-t^h}{1-t^{h-d+1}}
\le\frac{t}{1-t}\le1.
\tag{DF4}
\]

This proves DF2 for **every** higher grade, with no finite ceiling. Multiply
by nonnegative `c_h` and sum. Exchanging the finite sum over `r` and the
absolutely convergent sum over `h` is legitimate. The grades `1,...,d-1`
are actually annihilated; charging all nonzero mass gives the weaker,
convenient bound DF3. QED.

This is the concrete filtering mechanism: place zeros at the first several
unwanted spectral grades, retain unit response at the desired grade, and
make the remaining response have a known sign and a paid envelope.

**First case.** For `d=2`,

\[
Q_{2,t}(z)=\frac{z^2-tz}{1-t},\quad
B_{2,t}=\frac{F(t^2)-tF(t)}{1-t},\quad \epsilon_2=t^3.
\]

It cancels grade one exactly. At `t=1/2` this is `2F(1/4)-F(1/2)`;
its worst downward error is `M/8`. This already improves the simple
single-response positive approximation in a specific, auditable way.

## 3. DF-02: conditioning stays bounded — PROVED LOCAL

Because all roots in DF1 are positive, its nonzero coefficients alternate
in sign. Substitution of `z=-1` therefore yields

\[
\boxed{\sum_{r=1}^d|a_r|
=\prod_{j=1}^{d-1}\frac{1+t^j}{1-t^j}
<\frac{527}{63}<9.}
\tag{DF5}
\]

**Proof of the uniform constant.** Each factor increases with `t`, so
bound by the infinite product at `t=1/2`. Its first four factors have
product `51/7`. For `j>=5`, put `x=2^(-j)<=1/32`; then

\[
\log\frac{1+x}{1-x}\le\frac{2x}{1-x}\le\frac{64}{31}x.
\]

The remaining logarithmic sum is at most `4/31`. Since
`exp(y)<1/(1-y)` for `0<y<1`, the tail product is less than `31/27`.
The product is therefore less than `(51/7)(31/27)=527/63`. This also
bounds every finite initial product. QED.

If each response is supplied as `Fhat_r` with
`|Fhat_r-F(t^r)|<=eta_r`, the computed center
`Bhat=sum_r a_r Fhat_r` has error at most

\[
E=\sum_r|a_r|\eta_r\le9\max_r\eta_r.
\tag{DF6}
\]

Combining with DF3 gives the validated target interval

\[
\boxed{\max(0,\widehat B-E)\le c_0\le
\min\left(M,\frac{\widehat B+E+\epsilon_d M}{1+\epsilon_d}\right).}
\tag{DF7}
\]

An upper budget for `M` suffices. The code accepts asymmetric response
intervals and minimizes each signed term at the correct endpoint before
using this formula. A negative lower bound is inconclusive, not negative
prime mass.

## 4. DF-03: recovering a finite integer count — PROVED LOCAL

If `c_0` is integral and exact responses are available, then

\[
\epsilon_d M<1\quad\Longrightarrow\quad c_0=\lceil B_{d,t}\rceil.
\tag{DF8}
\]

Indeed, DF3 places `B` in `(c_0-1,c_0]`. This includes `c_0=0`: the
ceiling of its negative value of absolute size less than one is zero.
For mere positivity when `c_0>=1`, the slightly weaker condition
`epsilon_d(M-1)<1` suffices to force `B>0`.

With noisy absolute response errors, the feasible interval has width at
most `epsilon_d M+2E` (one may use the weaker upper endpoint
`Bhat+E+epsilon_d M`). If that width is less than one and the supplied
packet is authentic, at most one integer remains. An empty integer
interval is a contradiction of the packet's hypotheses, not a new count.
In particular the sufficient robust condition is

\[
\epsilon_d M+18\max_r\eta_r<1.
\tag{DF9}
\]

At `t=1/2`, choosing even `d` with `d(d+1)/2>log_2 M` is enough in the
noiseless case. Thus the number of response channels grows on the order
of `sqrt(log M)`. **This counts channels, not computation or bit cost.**
Large grades can require large rational denominators; acquiring the
responses is not free. For normalized responses `F/M`, detecting one
integer count requires absolute accuracy of order `1/M`, despite the
bounded amplification. The theorem offers no information-theoretic
compression miracle or automatic speedup.

## 5. DF-04: two observers form a monotone filter ratchet — PROVED LOCAL

Extend the *mathematical* definition DF1 to every integer `d>=1`.
Odd degrees have a positive higher-grade tail and therefore give upper
bounds, while even degrees give lower bounds. With the same fixed `t`,

\[
\boxed{B_{2,t}\le B_{4,t}\le\cdots\uparrow c_0,
\qquad B_{1,t}\ge B_{3,t}\ge\cdots\downarrow c_0.}
\tag{DF11}
\]

**Proof.** At grades zero and `1,...,d-1`, both filters of degrees `d`
and `d+2` agree. At grades `d,d+1`, the newer filter is exactly zero.
For every higher grade,

\[
\frac{q_{d+2,t}(h)}{q_{d,t}(h)}
=\frac{(t^d-t^h)(t^{d+1}-t^h)}{(1-t^d)(1-t^{d+1})}
\in[0,1/3].
\tag{DF12}
\]

The upper bound follows by replacing the numerator with `t^(2d+1)`;
its largest resulting value for `d>=1,t<=1/2` is `1/3` at `d=1,t=1/2`.
Thus each negative lower tail increases toward zero and each positive
upper tail decreases toward zero. Summing against nonnegative masses
preserves order. The error `M*t^[d(d+1)/2]` tends to zero, proving both
limits. QED.

This supplies a precise version of the coupled-observer idea: the two
current reports are an authenticated lower and upper bound for one shared
source target. They can be compared at the same filter parameter and
normalization, and each additional grade cancellation tightens the bracket.
When the target is an integer and the present bracket contains only one
integer, the observers have a certificate of the count. No comparison of
untransported historical states is involved.

The ordering here is **information refinement**, not elapsed physical
time or an entanglement claim. The implementation exposes only the even
lower filters as its public certificate constructor, deliberately rejecting
an odd degree passed as a lower bound. Tests check both theoretical ladders
by a separate direct-product formula.

## 6. Relation to the earlier Borwein and phase work

The repo already has grade-sensitive Borwein filters with geometrically
small nonprime error; donor #601's `BORWEIN_RATCHET.md` BRT-06 records
`T=P_1+(1/2)P_2`, hence `T^r=P_1+2^(-r)P_2`. That declared two-level
functional calculus even implies `P_1=2T^2-T` exactly. The new family does
not dominate that access model or invent finite prime projectors. It is a
*signed combination of damped generating-function responses* on an
unbounded integer grade set. Relative to simple `t^h`, it cancels several
entire low grades and has the stronger explicit `t^[d(d+1)/2]` envelope
with bounded coefficient norm. The distinction is which authenticated
responses the observer is actually allowed to acquire.

Mathematically the coefficients are Lagrange extrapolation weights for
evaluating `F(0)` from the nodes `t,t^2,...,t^d`. Equivalently they are
finite q-product coefficients. With
`(t;t)_k=product_(j=1)^k(1-t^j)` and `(t;t)_0=1`,

\[
a_r=\frac{(-1)^{d-r}t^{(d-r)(d-r+1)/2}}
{(t;t)_{r-1}(t;t)_{d-r}}.
\tag{DF10}
\]

This formula follows either from the roots in DF1 and the finite
q-binomial identity, or directly from the Lagrange weights
`product_(s!=r)(-t^s)/(t^r-t^s)`. See
[NIST DLMF 17.2.35](https://dlmf.nist.gov/17.2.E35) for the classical finite
q-binomial expansion. The displayed proofs above stand on their own;
no unverified external theorem is used as an arithmetic premise.

All these scalar grade filters commute. The gain here is from the signed
combination and the known integer spectrum, not from pretending that their
physical ordering is noncommutative. Ordered matrix filters elsewhere in
the dossier address a different source of information.

## 7. Exact finite application, including the failed small filter

The fixed experiment used every combination of midpoints
`10,257,509,1021,2053,4099` and degrees `2,4,6`, always `t=1/2`.
Every `F_n` was computed from genuine finite integer factorization.
[DAMPED_RESULTS.json](DAMPED_RESULTS.json) contains exact rational weights,
responses' resulting intervals, mass budgets and comparisons.

Decimals below display the **unclipped lower filter response** `B`. A
negative number is retained to show the failed bound. The last column is
the separately computed actual unordered Goldbach count for `2n`.

| midpoint n | d=2 lower | d=4 lower | d=6 lower | direct count |
|---:|---:|---:|---:|---:|
| 10 | 1.515625000 | 1.998046875 | 2.000000000 | 2 |
| 257 | 1.352050781 | 13.907478902 | 13.999979907 | 14 |
| 509 | -5.231678963 | 19.817233448 | 19.999947791 | 20 |
| 1021 | -19.361301303 | 29.620452476 | 29.999886488 | 30 |
| 2053 | -45.905214660 | 52.236436008 | 52.999752629 | 53 |
| 4099 | -109.071370861 | 82.449050516 | 83.999483383 | 84 |

Four of eighteen lower responses are negative, fourteen certify positive
zero mass, and eleven of eighteen certificates recover the exact integer
count. Every degree-six certificate recovers the count; degree two loses
power on the larger samples. These are finite, explicitly source-computed
facts, not evidence of a uniform conjectural response estimate.

For `n=4099`, `M=4098`, degree six has leakage `2^-21`; its error budget
`4098/2^21<1` explains exact count recovery *before* inspecting that count.
The success is therefore predicted by the general finite theorem. It is
not an independent test of Goldbach at unbounded targets.

## 8. Required hostile boundaries

- **Odd degree:** the remaining sign is positive, giving an upper filter.
  At `d=3,t=1/2,h=3`, the response is positive although the zero mass is zero.
- **t beyond the certified range:** at `d=2,t=3/4`,
  `q(2)=-27/64` but `q(3)=-567/1024`, violating the claimed tail envelope.
  The sign still gives a lower filter; the specific error bound is false.
- **Continuous grades:** at `d=2,t=1/4,h=1/2`, `z=1/2` gives `Q(z)=1/6>0`
  despite no zero grade. Integer grading, or another proven spectral gap
  and sign domain, is load-bearing.
- **Signed masses:** the step from a pointwise minorant to a mass lower
  bound needs `c_h>=0`. Arbitrary signed spectral weights are outside it.
- **Missing mass/error budgets:** coefficient stability does not control
  the tail mass or authenticate the measured responses. Normalization
  cannot hide the accuracy required to detect a rare single witness.

The exact test suite contains these mutants and compares polynomial
expansion against direct products, every small `0/1/2` histogram, a
grade-1000 control, noisy interval recovery, and both monotone filter
ladders. It has ten named tests.

## 9. The next arithmetic hole

For each midpoint `n`, construct authenticated estimates of the **joint**
responses DF0 and derive a bound

\[
\sum_{r=1}^{d_n}a_r F_n(t_n^r)>E_n
\]

for every sufficiently large `n`, paying the source, truncation and
measurement errors inside `E_n`. That would prove a Goldbach witness.
The present theorem provides the filter and its conditioning budget; it
does not provide that source-specific lower estimate. Taking `d_n` large
enough and evaluating every response exactly recovers finite counting;
it does not remove the original infinite arithmetic difficulty.

This round therefore earns a stable quantitative zero-sector reconstruction
tool and a finite arithmetic application. The meaningful next attack is
whether an analytic, coupled-source bound can evaluate its signed response
without already determining the prime-pair count.

### Completed follow-on: fixed banks cannot supply the uniform bound

After constructing this family, [FIXED_RESOLUTION.md](FIXED_RESOLUTION.md)
proved a source-specific limitation using a checked classical
Selberg--Delange mean. Every fixed finite bank of damped responses on
nodes in `(0,1)` whose grade response is a pointwise zero-sector minorant
has an eventually negative summatory response on the genuine arithmetic
source. It therefore fails at infinitely many midpoints; every sufficiently
large fixed-ratio shell contains a negative response. This does not imply
negative prime counts or negativity at every midpoint.

Thus the next positive route described above must adapt its nodes/order,
use a different observable family, or exploit source-specific constraints
beyond a universal pointwise grade minorant. Fixed-order finite successes
cannot be extrapolated into an all-midpoint estimate.
