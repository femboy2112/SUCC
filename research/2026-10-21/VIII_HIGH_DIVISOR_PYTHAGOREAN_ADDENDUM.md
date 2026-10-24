# An untruncated sparse Pythagorean family through `t=7/10`

Date: 2026-10-21. Status: **PROVED PAPER**. This is a complementary corollary
to the conic dossier committed at `b013a937497c652a7665d6808bda7b7d250d2758`.
It does not change that dossier or its hashed finite receipt. The mechanism
is **CLASSICAL** parametrization and elementary height counting; the precise
weighted application is **NEW TO PROJECT**, with academic novelty unverified.

The family here is very sparse and becomes unbalanced as its principal
parameter grows. It has **no root-depth or weight cutoff**. Its conclusion
does not extend the unrestricted primitive abc moment.

## Theorem

Let real `X>=2`, `M>=1`, and `0<=t<=1`. Let `P_M(X)` contain once each source

\[
a=(m^2-n^2)^2,\quad b=(2mn)^2,\quad c=(m^2+n^2)^2\le X,
\]

where `m>n>=1` are integers, `gcd(m,n)=1`, `m+n` is odd, and `n<=M`.
The displayed order of the two legs is part of the definition. Then

\[
\boxed{\sum_{P_M(X)}
 \left(\frac{abc}{\operatorname{rad}(abc)}\right)^t
 \le 2^t M^{2t+1}X^{(1+10t)/4}
 \le2 M^{2t+1}X^{(1+10t)/4}.}\tag{A1}
\]

For fixed `M`, this is quadratic for every `0<=t<=7/10`, including the
endpoint. If both orientations of the legs are included, double the displayed
constant. The theorem concerns all source weights in this family, including
all of their powerful-divisor selections.

**Proof.** The polynomial identity gives `a+b=c`. An odd prime common to
`m^2-n^2` and `2mn` would divide both `m` and `n`; the parity hypothesis
excludes two. Hence `gcd(a,b)=1`.

The height constraint implies `m<=X^(1/4)`. There are therefore at most
`M X^(1/4)` eligible parameter pairs, even before the gcd, parity, positivity
and height restrictions are imposed. Counting parameters overcounts any
possible repeated sources and so is a valid upper bound for the source set.
Furthermore

\[
abc=4m^2n^2(m^4-n^4)^2\le4M^2m^{10}\le4M^2X^{5/2}.
\]

Since `abc` is even, `rad(abc)>=2`, giving `H<=2M^2X^(5/2)`.
Multiply the `t`-th power of this bound by the parameter count. The last
inequality in (A1) uses `2^t<=2`. There is no assertion about the
factorization or squarefreeness of `m^2-n^2`, `2mn`, or `m^2+n^2`. QED.

## Growing family and high-divisor consequence

Set `M=X^eta`, `eta>=0`. The exponent in (A1) is exactly

\[
E=(1+10t)/4+(2t+1)\eta.
\]

For `t=17/25>2/3` and `eta=1/100`,

\[
\boxed{\sum_{P_{X^{1/100}}(X)}H^{17/25}
 \le2X^{2467/1250},\qquad 2-2467/1250=33/1250>0.}\tag{A2}
\]

Expand each full source weight by the positive exact coefficients `g_t`.
Any high-divisor subsum over this source family is bounded by the full moment;
all divisor choices and their weights are retained before this inequality.
For a dyadic sector `Q<def<=2Q`, `Q>X^2`, nonemptiness implies
`Q<def<=abc<=X^3/4`. Therefore (A2) also gives

\[
\boxed{I_t^{P}(X,Q)\le2X^2(X^2/Q)^{33/1250}}
\quad(t=17/25,\ M=X^{1/100}).\tag{A3}
\]

No individual prime-power exponent is bounded. For example, the allowed
parameter sequence `m=2^k,n=1`, `k>=1`, has
`b=2^(2k+2)` and an occupied coefficient
`g_1(b)=2^(2k)`. Thus arbitrary prime depth is actually present in this family.
Formula (A3) does not follow from a density-only high-divisor count.

## Exact controls and limits of authority

An independent direct integer check on this worktree tested the 172 coprime,
opposite-parity pairs with `2<=m<=70`, `1<=n<=min(m-1,6)`. It verified the
source equation, global primitivity and the squared rational inequality
`H^2<=4 n^4 c^5`. Five height cutoffs `25,100,1000,10000,1000000` verified the
count budget by the integer comparison `count^4<=M^4 X`, with `M=6`.
All checks passed. The rational exponent calculation returned `2467/1250`
and saving `33/1250` exactly. These finite controls support implementation
arithmetic; the displayed elementary proof supplies the universal statement.
No formal proof-kernel claim, density claim, or external-referee claim is made.

The additional input needed to cover balanced Pythagorean parameters is a
genuine average radical-weight estimate; simply letting `M` approach
`X^(1/4)` in (A1) loses this improvement. The general conic root-depth problem
and the nonsquare powerful-divisor sector remain separate open obligations.
