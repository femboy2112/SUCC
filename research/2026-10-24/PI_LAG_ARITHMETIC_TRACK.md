# Authentic BBP lag arithmetic: carries, short return cylinders, and the unpaid count

**Authority:** elementary paper proofs and exact finite checks; no new Lean
certification or scholarly-priority claim. Base read at
`ea5f92bbc52468e55b597e52455f24bceedb47b3`. The entire authentic forcing and
initial state are retained in the selected-source executable. **Pi normality
and the selected subpower collision estimate remain open.**

This track turns the requested lag recurrence into a carry-retaining counting
instrument. It proves a directional restriction on consecutive close returns.
It does not convert that restriction into a bound on the total number of returns.
The companion hostile track tests precisely why a uniform argument cannot omit
quantitative selection of the initial state.

## LA-01. Exact count and the two different integer carries

Let `r`, `y_0=0`, and `y_n={16y_(n-1)+r(n)}` have exactly the definitions in
[SCE](PI_SOURCE_COLLISION_ENTROPY.md). For `n>=0`, `l>=1`, write

\[
c_j=\lfloor16y_{j-1}+r(j)\rfloor,\quad
v_{n,l}=y_{n+l}-y_n,\quad
\eta_{n,l}=\lfloor v_{n,l}+1/2\rfloor,\quad
\delta_{n,l}=v_{n,l}-\eta_{n,l}\in[-1/2,1/2).
\]

Define the **positive** forcing difference

\[
f_{n,l}=r(n+1)-r(n+l+1)>0.
\]

Then exact subtraction gives

\[
v_{n+1,l}=16v_{n,l}-f_{n,l}-(c_{n+l+1}-c_{n+1}),
\]

and hence

\[
\delta_{n+1,l}=16\delta_{n,l}-f_{n,l}-\kappa_{n,l},\qquad
\kappa_{n,l}=c_{n+l+1}-c_{n+1}+\eta_{n+1,l}-16\eta_{n,l}\in\mathbb Z.
\]

The centered carry `kappa` is generally **not** the difference of the two source
carries. Discarding the centering terms is an incorrect boundary simplification.
The executable retains every term separately. An exact authentic witness is
`n=1174,l=130,tau=1/32`: both centered differences lie strictly inside the
close arc, the source-carry difference is 15, both centering offsets are 1,
and the centered carry is `15+1-16=0`. Discovery used a floating prefilter;
acceptance and the retained regression use only exact rational comparisons. The usual unwrapped source is
also recovered exactly: if `J_0=0`, `J_n=16J_(n-1)+c_n`, then

\[
16^n\sum_{j=1}^n16^{-j}r(j)=y_n+J_n.
\]

For a window `y_A,...,y_(A+N-1)` and `0<=tau<1/2`, let

\[
V_l(A,N;\tau)=\#\{0\le s<N-l:|\delta_{A+s,l}|\le\tau\}.
\]

Every off-diagonal unordered pair has exactly one positive time lag, so the
ordered close-pair count, including the diagonal, is exactly

\[
Q(A,N;\tau)=N+2\sum_{l=1}^{N-1}V_l(A,N;\tau). \tag{1}
\]

This identity is an exact useful implementation decomposition, not a new
cancellation estimate. The actual target remains to bound the full sum in (1)
at `A=u+1`, `N=3u`, `tau=1/M`.

## LA-02. Source-specific monotonic forcing and explicit beta bounds

Let `g(t)=(1-t)P(t)`, where
`P(t)=4+4t+4t^2+2t^3+t^4`. Direct termwise integration of a finite polynomial
shows

\[
r(n+1)=\int_0^1t^{8n}g(t)\,dt,\qquad
f_{n,l}=\int_0^1t^{8n}(1-t^{8l})(1-t)P(t)\,dt. \tag{2}
\]

All integrands are continuous on the compact interval for `n>=0`, `l>=1`.
They are positive on its interior, proving positivity and strict decrease in
`n`. More generally every alternating finite difference in `n` is positive,
because it introduces a factor `(1-t^8)^k` into (2).

Using `4<=P(t)<=15` and

\[
8l\,t^{8l-1}(1-t)\le1-t^{8l}\le8l(1-t),
\]

and integrating `t^a(1-t)^2`, one obtains strict bounds

\[
\frac{64l}{8(n+l)(8(n+l)+1)(8(n+l)+2)}
<f_{n,l}<
\frac{240l}{(8n+1)(8n+2)(8n+3)}. \tag{3}
\]

These hold for **every** `n>=0,l>=1`, not only an asymptotic range. Strictness
follows from strict integrand inequalities on a set of positive measure.
Their source requirements are the exact signed four-pole forcing; rationality
or a generic `O(n^-2)` forcing alone does not supply (2) or the constants.

## LA-03. A close-return run occupies exactly one shrinking rational interval

Fix `n>=0,l>=1,0<tau<1/2` satisfying

\[
f_{n,l}\le15\tau,\qquad17\tau+f_{n,l}<1. \tag{4}
\]

If both `|delta_(n+j,l)|<=tau` and `|delta_(n+j+1,l)|<=tau`, the centered
carry has absolute value at most `17tau+f_(n+j,l)<1`. Since it is an integer,

\[
\kappa_{n+j,l}=0. \tag{5}
\]

Here monotonicity of (2) makes the first-time gate sufficient at every later
step. This proves a literal carry restriction for the actual selected BBP
trajectory whenever two consecutive close visits occur. At the predetermined
scale this gate is eventually available, but it fails at `M=16`: the first
possible `M>=256` occurs at `p>=16^5=1,048,576`. Smaller-prime tests at
`tau=1/256` are off-target diagnostic scales and must be labeled as such.

For any integer `k>=0`, define the rational center

\[
B_{n,l,k}=\sum_{i=0}^{k-1}16^{-i-1}f_{n+i,l}.
\]

Then the following are equivalent for the actual centered lag:

1. `|delta_(n+j,l)|<=tau` for every `0<=j<=k`.
2. `delta_(n,l)` belongs to

\[
I_{n,l,k}=[B_{n,l,k}-16^{-k}\tau,
           B_{n,l,k}+16^{-k}\tau]. \tag{6}
\]

**Proof.** In the forward direction (5) iterates to
`delta_(n+k,l)=16^k(delta_(n,l)-B_(n,l,k))`, giving (6).
Conversely, the real affine iterates with zero centered carry end in
`[-tau,tau]`. Each inverse map `z -> (z+f_(n+i,l))/16` sends `[-tau,tau]`
into itself by `0<f_(n+i,l)<=15tau`. Thus all intermediate real iterates
are in that interval; they are the correct centered representatives, because
`tau<1/2`. Their reductions modulo one agree with the true lag recurrence.
This proves the converse, with both threshold endpoints retained.

The interval has exact length `2tau16^-k`. This is stronger than checking
only the endpoint without verifying its carries: the theorem proves that
here the carry gate and positivity recover every intermediate condition.
It gives an exact rational finite certificate, not a measure estimate for
the actual selected lag.

## LA-04. Quantified directional escape and the surviving positive tracker

If the run in LA-03 begins with `delta_(n,l)<=0`, its interval must meet the
nonpositive half-line. Formula (6), strict monotonicity, and (3) imply the
necessary inequality

\[
(16^k-1)
\frac{64l}{8(n+k-1+l)(8(n+k-1+l)+1)(8(n+k-1+l)+2)}
\le15\tau\qquad(k\ge1). \tag{7}
\]

Indeed `B_(n,l,k)>=f_(n+k-1,l)(1-16^-k)/15`; the lower endpoint of (6)
is positive if the reverse strict inequality in (7) holds. The executable
`nonpositive_escape_bound` certifies exactly this sufficient escape condition.

In a prime window all involved state indices are at most `4u`, so the weaker
but simpler necessary bound is

\[
16^k-1\le
\frac{15\tau\,(32u)(32u+1)(32u+2)}{64l}. \tag{8}
\]

At the predetermined scale `tau=1/M`, `M~p^(2/5)`, this limits a close run
**starting on the nonpositive side** to `O(log p)` transitions, uniformly in
its allowed lag. It does not limit every close run to that length.

To see the exact missing case, define the authentic positive Green difference

\[
a_{n,l}=t_n-t_{n+l}>0.
\]

Its recurrence is `a_(n+1,l)=16a_(n,l)-f_(n,l)`. Also

\[
a_{n,l}=\sum_{i\ge0}16^{-i-1}f_{n+i,l},\qquad
B_{n,l,k}=a_{n,l}-16^{-k}a_{n+k,l}. \tag{9}
\]

Absolute convergence follows from `0<f_(n+i,l)<=f_(n,l)` and a geometric
majorant; no unlicensed interchange is used. Under (4), the nested intervals
(6) shrink to the single positive tracker `a_(n,l)`. A run of length `k`
therefore requires the rational selected lag to approximate that tracker to
within `16^-k(tau+a_(n+k,l))`.

The selected lag is rational. The tracker is irrational: the BBP identity
and finite recurrence give `t_n=16^(n-1)pi-R_n` for rational `R_n`, so
`a_(n,l)=16^(n-1)(1-16^l)pi` plus a rational number. Classical irrationality
of pi excludes an infinite uninterrupted close run under (4). It supplies
no useful uniform polynomial-scale count of finite runs. The long-run
obstruction is thus quantitatively visible, rather than silently removed.

**Earned source-specific statement:** actual close returns satisfy (5), the
exact interval test (6), and the directional bound (7)/(8), with authenticated
four-pole constants. **Unpaid:** the frequency with which the actual rational
lag enters the positive shrinking intervals (6). A small forcing term does
not make that frequency small.

## LA-05. The repeated local clock contribution is already negligible

For `p=8u+1`, `L=ord_p(16)|u`, `Delta=3u`, the authenticated first-window
states have `y_(u+1+t)=4*16^t/p+w_t mod1` with `w_t` p-integral. For a lag
`l` not divisible by `L`, the rational difference has p-adic valuation exactly
`-1`: its nonzero local numerator cannot be canceled by a p-integral
complement or an integer carry. Thus those pairs can never be exact repeats.

There are exactly `Delta^2/L` ordered pairs whose local phases agree,
including the diagonal. Their contribution to the selected scaled collision
is consequently at most

\[
\frac M L < p^{-1/10}\log p \tag{10}
\]

on the good-prime family at `c=2/5`. This is an immediate selected-source
corollary of the already proved SCE phase multiplicities, not a major new
arithmetic saving for the entire count. All remaining mass comes from
nonresonant lags, whose complete complementary phases remain uncontrolled.
An exact nonzero denominator cannot be substituted for a separation of
size `1/M`: denominators of authentic states are much finer than that scale.

## Controls, failed routes, and verification boundary

The ten focused tests in `tests/test_pi_lag_carry.py` compare the recurrence
with independent unwrapped partial sums; compare lag counting with direct
ordered-pair enumeration and the existing sorted circular counter; retain
source carry differences and both centering offsets; test both endpoints and
nearby excluded points of (6); check beta bounds, monotonicity, directional
escape, phase multiplicities and exact p-denominator obstructions. They do not
prove an infinite theorem; the analytic assertions have the proofs above.

The source-matched dyadic controls from sibling #259 already preserve the
complete forcing and every odd-primary component while producing coherent
finite windows. Their finite coalescence and changed initial condition must
remain explicit. That prior theorem is not claimed as new here. The new
companion hostile track strengthens its observed-prefix boundary.

Failed routes retained:

- `f` small implies smooth lag: false, because the integer centered carry is
  a separate term and the map expands by 16.
- zero centered carry means equal literal source carries: false unless the
  centering corrections have separately been paid.
- nonresonant p-denominator implies real separation `>=1/p`: false for a
  rational number with an additional p-free denominator.
- shrinking run cylinders imply few selected visits: unproved. Their small
  lengths give ensemble statements only; the selected values are not sampled
  from a supplied absolutely continuous distribution.
- absence of an infinite close run supplies the desired `p^{o(1)}` bound:
  false as an implication; finitely long but increasing exceptional runs
  are not controlled.

The next source-specific test is to bound how often the selected positive
lag lies in (6), with `k` comparable to `log p`, summed over nonresonant lags.
Such a bound must retain the actual rational initial values of those lag
processes. Replacing them by Haar, Galois-average, or free carry inputs would
again change the theorem's hypothesis.
