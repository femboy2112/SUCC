# Pascal recurrence order, the base-31 filter, and the remaining transport estimate

**Date:** 2026-10-24. **Status:** exact recurrence and minimality proofs,
an integer-filter construction, and an operational reformulation of the
open symmetry estimate. No real collision-frequency bound or pi-normality
result is claimed. This bounded followup changes no production code or tests.

Notation and source provenance are as in
[the real-kernel dossier](PI_PASCAL_REAL_KERNEL.md):

$$
\alpha=\pi/16,\quad U_n=16^n\alpha-T_n,\quad
A_k=\Delta^kU_0=15^k\alpha-(-1)^kR_{0,k},
\quad D_k=(-1)^k\Delta^kr(1)>0.
$$

## 1. A factorized order-four recurrence for the forcing moments

Let $E$ shift the difference-order variable $k$, and define the backward
operator

$$
\mathcal B=k(E^{-1}-1).
$$

For $h_a(k)=\mathrm B(a,k+1)$ and $k\geq1$, the beta recurrence gives

$$
k h_a(k-1)=(k+a)h_a(k),\qquad
\mathcal B h_a=a h_a.
$$

The authentic moment is the nonzero linear combination

$$
D_k=\frac18[4h_{1/8}(k)-2h_{1/2}(k)-h_{5/8}(k)-h_{3/4}(k)].
$$

Consequently, with

$$
\mathcal P(z)=(8z-1)(2z-1)(8z-5)(4z-3)
=512z^4-1024z^3+712z^2-194z+15,
$$

the exact recurrence is

$$
\boxed{\mathcal P(\mathcal B)D_k=0,\qquad k\geq4.}
$$

The factors are polynomials in the same operator and therefore commute.
The lower bound on $k$ ensures every backward evaluation lies in the
domain where its elementary beta identity applies.

Equivalently, $\sum_{j=0}^4p_j(k)D_{k-j}=0$, where

$$
\begin{aligned}
p_0(k)&=(8k+1)(2k+1)(8k+5)(4k+3),\\
p_1(k)&=-2048k^4-400k^2+6k,\\
p_2(k)&=24k(k-1)(128k^2-128k+51),\\
p_3(k)&=-2048k(k-1)^2(k-2),\\
p_4(k)&=512k(k-1)(k-2)(k-3).
\end{aligned}
$$

### Exact minimality statement

The order is **exactly four over $\mathbb Q(k)$**. Here order means the
span between the first and last shifts in a nonzero homogeneous linear
recurrence with rational-function coefficients, valid for all sufficiently
large integers. This is not a claim about minimal differential-equation
order for an associated generating function.

First, the four $h_a$ are linearly independent over $\mathbb Q(k)$.
Indeed $h_a(k)\sim\Gamma(a)k^{-a}$. Multiplying by a nonzero rational
function changes the leading exponent by an integer. The four distinct
fractional parts of $a$ make the largest resulting exponent unique,
so its leading term cannot cancel.

Suppose an order-$m$ recurrence annihilates $D$, with $m<4$ and forward
coefficients $u_j(k)$. Independence forces it to annihilate each $h_a$:

$$
\sum_{j=0}^m u_j(k)\frac{(k+1)_j}{(k+a+1)_j}=0.
$$

Multiplication by $(k+a+1)_m$ gives a polynomial in $a$ of degree at
most $m$, with four distinct roots. It is identically zero. The terms
indexed by $j$ have distinct degrees $m-j$, so triangular elimination
forces every $u_j=0$, a contradiction. Together with the displayed
order-four recurrence, this proves minimality.

## 2. Exact minimal order five for the Pascal source

Put $F_k=(-1)^kD_k=A_{k+1}-15A_k$ and

$$
\mathcal C=-k(E^{-1}+1).
$$

Conjugating by multiplication by $(-1)^k$ gives
$\mathcal P(\mathcal C)F=0$. Therefore

$$
\boxed{\mathcal P(\mathcal C)(E-15)A=0.}
$$

An explicit six-time version, valid for $k\geq4$, is

$$
\sum_{j=0}^4(-1)^jp_j(k)
\big(A_{k-j+1}-15A_{k-j}\big)=0.
$$

This has order five, and that order is minimal over $\mathbb Q(k)$.
For a proof, suppose $L=\sum_{j=0}^m u_j(k)E^j$ annihilates $A$.
Clear denominators so all $u_j$ are polynomials. Because
$A_k=15^k\alpha+O(k^{-1/8})$ with $\alpha\ne0$, its exponentially
growing contribution forces

$$
\sum_{j=0}^m15^j u_j(k)=0.
$$

Otherwise a nonzero polynomial times $15^k$ would equal a quantity
of at most polynomial growth. Polynomial division in the shift then
gives $L=M(E-15)$, with $M$ of order at most $m-1$. Thus $M$ annihilates
$F$, whose minimal order is four by the sign conjugation above. Hence
$m\geq5$.

Normalization does not lower the recurrence order. For
$Z_k=A_k/15^k$, a rational-coefficient recurrence is carried to one
of the same order for $A$ by multiplying its shifted coefficients by
powers of 15. Explicitly,

$$
\sum_{j=0}^4(-1)^j15^{4-j}p_j(k)
\big(Z_{k-j+1}-Z_{k-j}\big)=0.
$$

The normalized sequence converges to $\alpha$. This convergence of
rational approximants is separate from uniform distribution of the
unscaled phases $\{A_k\}$.

The rational filters $X_k^{q,d}=(q/15^d)^kA_{dk}$ also have exact
minimal order five for every fixed $q\geq2,d\geq1$. To see this,
put $c=q/15^d$. Their forcing $X_{k+1}^{q,d}-qX_k^{q,d}$ is a sum
of four hypergeometric components of the form

$$
c^{k+1}(-1)^{dk}\,\gamma_a h_a(dk)
\sum_{j=0}^{d-1}15^{d-1-j}(-1)^j
\frac{(dk+1)_j}{(dk+a+1)_j},
$$

where $(\gamma_{1/8},\gamma_{1/2},\gamma_{5/8},\gamma_{3/4})
=(1/2,-1/4,-1/8,-1/8)$. Each successive ratio is rational in
$k$, and each displayed finite sum tends to
$(15^d-(-1)^d)/16\ne0$. Their four fractional asymptotic exponents
remain distinct. Rational-function independence forces any recurrence
for their sum to annihilate each component; a common order-four
recurrence exists by rational linear algebra, and a lower order cannot
have four independent solutions. Finally $q^k\alpha$ dominates the
remaining $O(c^kk^{-1/8})$ term because $q/c=15^d>1$. The same
right-factor argument now uses $E-q$ and proves exact order five.

### What this says about carries

After expanding the order-five recurrence, write it as
$\sum_{i=0}^5q_i(k)A_{k-4+i}=0$, with integer polynomials $q_i$ of
degree at most four. If $A_j=C_j+x_j$, $C_j\in\mathbb Z$ and
$0\leq x_j<1$, then

$$
\sum_{i=0}^5q_i(k)x_{k-4+i}
=-\sum_{i=0}^5q_i(k)C_{k-4+i}\in\mathbb Z.
$$

The magnitude of this integer is at most $\sum_i|q_i(k)|=O(k^4)$.
This is an exact finite relation among six phases and their carries.
Its right side is not an independent or uniformly sampled label.
It is obtained by eliminating the already known four forcing components;
no frequency estimate has been introduced by that elimination.

## 3. Finite holonomic order does not supply the missing statistics

Even the same minimal order and the same four fractional asymptotic
families can occur in a positive, completely clustering rational source.
This control changes the actual recurrence coefficients and source poles.

Let $\mathcal A=\{1/8,1/2,5/8,3/4\}$, take the positive rational
number

$$
c=\left(\sum_{a\in\mathcal A}\frac1{a(a+1)}\right)^{-1},
\qquad
d\rho^*(t)=c(1-t)\sum_{a\in\mathcal A}t^{a-1}\,dt.
$$

Its total mass is 1. Its moments are the finite rational functions

$$
T_n^*=c\sum_{a\in\mathcal A}
\frac1{(n+a)(n+a+1)}.
$$

Set $U_n^*=16^n-T_n^*$ and
$s^*(n)=16T_{n-1}^*-T_n^*$. This gives $U_0^*=0$ and a positive,
completely monotone rational forcing of quadratic decay. Since
$0<T_n^*<1$ for $n\geq1$ and $T_n^*\to0$, its circle states cluster
completely. Its Pascal source is

$$
A_k^*=15^k-(-1)^kc\sum_{a\in\mathcal A}\mathrm B(a,k+2).
$$

The four beta terms have rational successive ratios and distinct
fractional asymptotic exponents. The four forcing components in
$A_{k+1}^*-15A_k^*$ are nonzero rational multiples of those terms.
They remain independent, so their minimal common recurrence order
is four: an order-four recurrence exists by solving the four rational
linear equations for five shifted coefficients, and an order below
four cannot have four independent solutions on a nonsingular tail.
The exponential-term argument from Section 2 then gives minimal
order five for $A^*$.

Thus the bare rank, positivity, quadratic decay, and four exponent
classes do not force real central-branch loss. This control does not
claim the exact BBP recurrence, the full dyadic valuation profile, or
the authentic four poles. Supplying the exact recurrence together
with its initial values specifies the authentic source; proving its
frequency behavior is still the original statistical obligation.

## 4. Base 31 is the first prime admitted by the integer-filter endpoint test

For a fixed integer polynomial $P$ with $P(16)=q$, a vanishing absolute
kernel remainder requires

$$
q\bmod16\in\{0,1,15\},\qquad
q\bmod15\in\{0,1,14\}.
$$

The primes below 31 are $2,3,5,7,11,13,17,19,23,29$. All except 17
fail the first condition; 17 fails the second. The prime 31 passes
both, and the test is attained by the degree-one integer polynomial

$$
P(t)=2t-1,\qquad P(16)=31,\qquad |P(t)|\leq1\quad(0\leq t\leq1).
$$

Consequently

$$
V_k=(2E-1)^kU_0=31^k\alpha-M_k,
\qquad M_k=\int_0^1(2t-1)^k\,d\rho(t)\longrightarrow0.
$$

This is an integer-coefficient filter, so its circle readout from the
full $k+1$ input phases needs no additional division-cover label.
Its coefficient norm is $3^k$.

An explicit all-$k$ absolute bound follows by splitting at $t=1/2$:
$|2t-1|^k\leq(1-t)^k$ on the left and $|2t-1|^k\leq t^k$ on the right.
Thus

$$
|M_k|\leq R_{0,k}+T_k
<\frac{D_k}{15}+\frac1{(8k+1)(8k+2)}
<\frac1{30}\mathrm B(1/8,k+2)+\frac1{(8k+1)(8k+2)}.
$$

The bounds are exact rational quantities. The endpoint behavior of
$w(t)$ gives the sharper asymptotic

$$
M_k\sim(-1)^k\frac{\Gamma(1/8)}{32(2k)^{1/8}}.
$$

Indeed the endpoint $t=0$, after the scaling $t=v/(2k)$, supplies
this term. The endpoint $t=1$ contributes $O(k^{-2})$, and any fixed
interior interval contributes exponentially less. Bounded endpoint
ratios and dominated convergence justify the rescaling, as in the
signed and unsigned kernel proofs in the parent dossier.

The prime-minimality statement is limited to this fixed integer-polynomial,
vanishing-absolute-remainder mechanism. It is not a restriction on
normality transfer by other methods.

## 5. The concrete two-time transport targets

For a selected window $I=\{A,\ldots,B\}$ of $N$ authentic source points,
let $\mu_I=N^{-1}\sum_{n\in I}\delta_{y_n}$.
The fixed degree-one base-3 filter gives the exact equality

$$
\frac{U_{n+1}-U_n}{5}=3U_n+\frac{r(n+1)}5.
$$

If $\nu_I^{(3)}$ is the empirical law of the fractional parts on the
left, the source coupling proves

$$
W_1(\nu_I^{(3)},(T_3)_*\mu_I)
\leq\frac1{5N}\sum_{n\in I}r(n+1)
\leq\frac{r(A+1)}5.
$$

The readout must retain $\lfloor U_{n+1}-U_n\rfloor\bmod5$.
One tripling test needs this fixed five-cover coordinate for each
sample; iterating the rational Pascal filter $k$ times needs the
modulus $5^k$ described in the parent dossier.

For the integer base-31 filter,

$$
2U_{n+1}-U_n=31U_n+2r(n+1),
$$

so the empirical law $\nu_I^{(31)}$ of
$\{2y_{n+1}-y_n\}$ satisfies

$$
W_1(\nu_I^{(31)},(T_{31})_*\mu_I)
\leq\frac2N\sum_{n\in I}r(n+1)
\leq2r(A+1).
$$

Both budgets are $O(A^{-2})$. These formulas use the extra source
entry at $B+1$. If it is unavailable, shorten to $A,\ldots,B-1$;
the original and shortened input empirical laws differ in $W_1$
by at most $1/(2N)$, with the usual multiplier factor when comparing
their pushforwards.

The remaining hypothesis is

$$
W_1(\nu_I^{(3)},\mu_I)\longrightarrow0
\quad\text{or}\quad
W_1(\nu_I^{(31)},\mu_I)\longrightarrow0
$$

on the same selected windows. Up to the proved vanishing source error,
these are precisely the corresponding new invariance conditions.
The finite recurrence and kernel identities do not show either one.
Together with positive all-scale collision dimension, either new
symmetry would be eligible for the inherited rigidity route, since
16 is relatively prime to both 3 and 31. Neither symmetry alone
establishes the missing collision hypothesis.

## 6. Verification and earned conclusion

A read-only exact rational calculation checked the factorized order-four
recurrence at every center $k=4,\ldots,80$, and the order-five source
recurrence at centers $k=4,\ldots,40$. An exact prime enumeration
confirmed the endpoint exclusions through 31. These checks calibrate
the formulas; the all-order and minimality claims rest on the proofs
above. No production or test file was changed for this followup.

The genuine additions are an explicit minimal recurrence, a finite
six-time carry relation, and the first admissible prime integer filter
with a certified source error. The carry relation is a source identity,
not a saving in its real collision count. The operational transport
targets identify exactly what a further proof must estimate.
