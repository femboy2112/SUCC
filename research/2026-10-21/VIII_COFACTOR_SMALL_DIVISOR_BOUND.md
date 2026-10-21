# A uniform high-divisor tail bound with one small selected divisor

Date: 2026-10-21. Research branch: `research/viii-referee-2026-10-21`.
Status: **PROVED PAPER**; exact controls **TESTED FINITE**; not Lean-verified.
Classification: new to this project; academic novelty **UNVERIFIED**. This is
an elementary restricted-family theorem, not the full weighted abc moment
bound at or beyond `t=2/3`. All arguments and constants used below are supplied.

## 1. Exact objects and theorem

Fix a real `0<=t<1`. Let `g_t` be multiplicative, with `g_t(1)=1`,
`g_t(p)=0`, and, for every genuine prime p and integer k>=2,

\[
g_t(p^k)=p^{t(k-2)}(p^t-1).
\]

For real `X>=2`, `Q>=X^2`, and `B>=1`, define

\[
T_t(X,Q;B)=
\sum_{\substack{a,b\ge1,\ a+b=c\le X\\\gcd(a,b)=1}}
\ \sum_{\substack{d\mid a,\ e\mid b,\ f\mid c\\
                     def>Q,\ \min(d,e,f)\le B}}
 g_t(d)g_t(e)g_t(f).
\]

The triples are ordered. Each divisor selection is counted separately, even
when selections share a source or cofactors. Primitivity forces d,e,f to be
pairwise coprime. A summand vanishes unless each selected modulus is powerful
or 1. No bound on the prime support or exponent depth is imposed.

Put

\[
\alpha=\frac{1+t}{2},\qquad \sigma=1-\alpha=\frac{1-t}{2},\qquad
C_t=\prod_p\left(1+
 \frac{p^{-(3-t)/2}}{1-p^{-(1-t)/2}}\right),\qquad
K_t=\frac{3C_t^3}{1-\alpha}.
\]

**Small-selected-divisor theorem.** The product defining `C_t` is finite, and
uniformly in the declared real parameters,

\[
\boxed{T_t(X,Q;B)\le K_t B(1+\log B)X^{1+t}
                    \left(\frac{X^2}{Q}\right)^{(1-t)/2}.}
\tag{1}
\]

Moreover `T_t(X,Q;B)=0` if `B<=Q/X^2`. The logarithm is natural.

In particular, set

\[
B_t(X)=\max\left\{1,\frac{X^{1-t}}{1+\log X}\right\}.
\]

Then the actual restricted tail, hence each restricted dyadic shell, satisfies

\[
\boxed{T_t(X,Q;B_t(X))\le K_tX^2
             \left(\frac{X^2}{Q}\right)^{(1-t)/2}.}
\tag{2}
\]

This proves a positive uniform dyadic exponent on a growing selected-divisor
family for every fixed `t<1`, including `2/3<=t<1`. Alternatively, for any fixed
`eta<1-t` and `B=X^eta` with `eta>=0`, its entire high-divisor contribution is
`O_t(X^(1+t+eta)(1+eta log X))=o_t(X^2)`. Constants have no hidden X, Q or B
dependence. The remaining family has **all three selected divisors larger than
the stated cutoff**; (1) is not a bound for that remaining family.

The restricted family is not an eventually empty formal slice. For any integer
m>=5 coprime to 3, take

\[
(a,b,c)=(9(2m+9),m^2,(m+9)^2),\quad
(d,e,f)=(9,m^2,(m+9)^2),\quad(u,v,w)=(2m+9,1,1).
\]

These are primitive source incidences, and at X=c,
`D/X^2=9m^2/(m+9)^2>1`. Their minimum selected divisor is always 9, so every
fixed t<1 eventually admits them to `B_t(X)`. They are highly unbalanced, with
`a/c -> 0`. Choosing `m=2^r`, r>=3, also gives unbounded prime-power depth in e.
Thus the result includes actual unbounded-height and deep-power sources.

## 2. A coefficient carrier estimate allowing arbitrarily deep prime powers

Define a nonnegative multiplicative function h_t by `h_t(1)=1`,
`h_t(p)=h_t(p^2)=0`, and `h_t(p^k)=p^{t(k-1)}` for k>=3. Let s be the square-supported
function `s(r^2)=r^t`, zero away from squares. At a prime power:

- k=0 is an equality;
- k=1 has `g_t(p)=0`;
- k=2 has `g_t(p^2)=p^t-1<=p^t=s(p^2)`;
- k>=3 has `g_t(p^k)<=h_t(p^k)`.

Consequently `g_t(n)<=(s*h_t)(n)` for every integer n: the convolution is
multiplicative and contains each of the displayed local nonnegative terms.
For real Y>=1,

\[
\begin{aligned}
A_t(Y):=\sum_{n\le Y}g_t(n)
 &\le\sum_{j\le Y}h_t(j)\sum_{r\le\sqrt{Y/j}}r^t\\
 &\le Y^\alpha\sum_{j\ge1}\frac{h_t(j)}{j^\alpha}
 = C_tY^\alpha.
\end{aligned}\tag{3}
\]

The elementary bound `sum_{r<=R}r^t<=R^(t+1)` used R>=1 and t>=0.

To justify the last equality, the p-factor is

\[
1+\sum_{k\ge3}p^{t(k-1)-k\alpha}
=1+\frac{p^{-(3-t)/2}}{1-p^{-(1-t)/2}}.
\]

Write `sigma=(1-t)/2>0`. The sum of its nonconstant terms over p is at most
`(1-2^(-sigma))^(-1) sum_{n>=2}n^(-1-sigma)`, which is finite. Finite-prime
products therefore converge; monotone convergence of nonnegative finite Euler
products proves the series/product equality. A coarse fully explicit majorant
is `C_t<=exp(1/[sigma(1-2^(-sigma))])`, using the integral bound for the integer
series. No formal Euler product is promoted without convergence.

The cubic-and-deeper remainder is essential. At `t=2/3`, d=256 gives
`g_t(d)=16(2^(2/3)-1)>4*2^(2/3)=d^(t/2)`, since `2^(2/3)>4/3`. Thus the
tempting square-only bound `g_t(d)<=d^(t/2)` is false. Estimate (3) includes
deep prime powers rather than discarding them. At t=1 its convergence argument
fails; no extension of (1) to t=1 is asserted.

## 3. Source-preserving cofactor injection

Write `a=du`, `b=ev`, `c=fw` with positive integral u,v,w. Fix a selected
summand divisor d. Put `rho=X^2/Q<=1`. Since `D=def>Q`,

\[
vw=\frac{bc}{ef}=\frac{dbc}{D}<d\frac{X^2}{Q}=d\rho.
\tag{4}
\]

For fixed d,v,w, the pair (e,f) determines b,c, hence a=c-b and u=a/d
uniquely when an admissible source exists. Thus this is an injection of actual
incidences into tuples (d,v,w,e,f); it is **not** an assertion of one incidence
per cofactor triple. Drop the additive, divisibility and primitive restrictions
only after making this injection. Nonnegative coefficients and (3) give

\[
\begin{aligned}
T_{t,d\le B}
&\le\sum_{d\le B}g_t(d)
       \sum_{vw<d\rho}A_t(X/v)A_t(X/w)\\
&\le C_t^2X^{2\alpha}\sum_{d\le B}g_t(d)
                       \sum_{vw<d\rho}(vw)^{-\alpha}.
\end{aligned}\tag{5}
\]

Terms with v>X or w>X have no actual source and zero corresponding coefficient
sum. They may be included in the relaxed nonnegative bound; equivalently define
`A_t(Y)=0` for `0<=Y<1`, where `A_t(Y)<=C_tY^alpha` still holds.

For any real L>1 and `0<=alpha<1`,

\[
\begin{aligned}
\sum_{vw<L}(vw)^{-\alpha}
&\le \frac{L^{1-\alpha}}{1-\alpha}\sum_{v<L}\frac1v\\
&\le\frac{L^{1-\alpha}(1+\log L)}{1-\alpha}.
\end{aligned}\tag{6}
\]

The inner power sum is bounded by its elementary integral. If L<=1 the left
side is zero. Apply (6) to `L=d rho`, and use `log(d rho)<=log B` for its
nonempty terms. Then

\[
T_{t,d\le B}\le\frac{C_t^2}{1-\alpha}X^{2\alpha}
 \rho^{1-\alpha}(1+\log B)
 \sum_{d\le B}g_t(d)d^{1-\alpha}
\le\frac{C_t^3}{1-\alpha}B(1+\log B)
 X^{2\alpha}\rho^{1-\alpha}.
\tag{7}
\]

The last step uses `d^(1-alpha)<=B^(1-alpha)` and (3), so the power of B is
exactly one. The identical argument applies when e is the small divisor.

For the **total divisor f**, fix f,u,v. The pair (d,e) determines a,b, hence
c=a+b and w=c/f uniquely when valid. Here

\[
uv=\frac{ab}{de}=\frac{fab}{D}
 <\frac{fX^2}{4Q}\le f\rho,
\]

because `ab<=(a+b)^2/4<=X^2/4`. Repeating (5)--(7) bounds this third slot with
the same constant (and an optional extra factor `4^(-(1-alpha))`). A union
bound over the three small-divisor slots proves (1). Incidences with multiple
small divisors are harmlessly overcounted, never omitted or identified.

For every selected divisor d, its two complementary selected divisors are at
most the two corresponding source coordinates, each <=X. Thus `D<=d X^2`.
The same holds with e or f. If `D>Q`, every selected divisor exceeds `Q/X^2`,
proving the asserted empty-tail criterion.

Finally, `B_t(X)(1+log B_t(X))<=X^(1-t)`: if the maximum is 1 this is immediate;
otherwise `B_t(X)<=X` and division by `1+log X` proves it. Substitution into
(1) proves (2) with all X,Q quantifiers preserved.

## 4. Exact obstruction to a dual singleton or bounded-fiber argument

For every even integer m>=2, define

\[
a=(m^2-1)^2,\quad b=(2m)^2,\quad c=(m^2+1)^2,
\qquad(d,e,f)=(a,b,c),\quad(u,v,w)=(1,1,1).
\]

The roots form a primitive Pythagorean triple: expansion gives a+b=c;
`gcd(m^2-1,2m)=1` since m is even, and the other pairwise gcds follow from
the equation. All selected divisors are powerful. At X=c,

\[
\frac{D}{X^2}=\frac{ab}{c}
=\left(\frac{2m(m^2-1)}{m^2+1}\right)^2>1,
\]

because `2m(m^2-1)>m^2+1` for m>=2. All these different incidences lie over
the **same** cofactor triple. This proves that no universal singleton or fixed
finite bound is possible for cofactor fibers as X varies.

The common-cutoff statement also has unbounded fibers, not merely different
points at different individual cutoffs. For any even M>=2, set
`X=(4M^2+1)^2` and use every even m in `[M,2M]`. Their c-values are <=X. Since

\[
D=4m^2(m^4-1)^2\ge (225/64)m^{10},\qquad
X^2=(4M^2+1)^4\le (17/4)^4M^8,
\]

all these incidences have `D>X^2` once `M^2>(17^4)/(4\cdot225)`; in particular
M>=10 suffices. There are `M/2+1` distinct even parameters. This gives a
quantitative family of at least that many high-divisor incidences in one
cofactor fiber at a common height cutoff.

This is a strategy obstruction, **not** a counterexample to (1), to the full
dyadic candidate, or to a quadratic moment bound for t<1. Indeed these examples
have all three selected divisors growing; for every fixed t>=2/3 they eventually
all exceed B_t(X), the regime not settled by the small-divisor theorem.
In the small-divisor proof the injection retains
the two complementary **divisors**, not just the cofactors.

## 5. Validation, scope and next decisive inequality

Reproduction:

```sh
python -m unittest discover -s tests -p test_viii_hostile_high_divisor.py -v
```

The six exact controls passed on the research worktree. They check:

- the carrier estimate through a **finite** convolution upper bound with
  integer-root interval enclosures at t=0,1/2,2/3,3/4,9/10;
- source-to-cofactor injections in each of the three slots, preserving all
  selected divisors and testing integer weights at t=1 solely for this finite
  identity (the infinite theorem does not include t=1);
- the parameterized Pythagorean obstruction and deep-prime-power majorant
  counterexample;
- exact certification of every rational-power interval by integer powers.

The tests are independent finite support for the written proof, not universal
proofs. No external analytic theorem is imported. The mechanisms are elementary
multiplicative convolution, convergent nonnegative Euler products, divisor
summation, and the classical Pythagorean parameterization. Their particular
application here is new to the project; no literature priority or publication
novelty claim has been established.

The next verdict-changing problem is the full incidence estimate after imposing
`d,e,f>B_t(X)` (or a comparable power cutoff). Removing these three restrictions
from (2) without a new argument is invalid. A future incidence theorem can now
focus on the three-large-divisor region while (1) handles its complementary
region uniformly, including unbounded exponent depth and moving Q.
