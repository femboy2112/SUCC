# Prescribing the real constant while retaining the full dyadic profile

**Date:** 2026-10-24.
**Parent:** [draft #272](https://github.com/femboy2112/SUCC/pull/272), following
[draft #270](https://github.com/femboy2112/SUCC/pull/270) at
`3acd547ff122368d5694efdab029b3156a292d8a`.
**Status:** PROVED PAPER, with same-model adversarial audit; no Lean or
numerical authority is claimed. This is a changed-source counterexample.

The construction in [PAB-1 through PAB-3](PI_PASCAL_ADVERSARIAL_BOUNDARY.md)
extends to **every prescribed real C>0**, retaining rational source values
at positive integers, the full dyadic profile, fixed precision and decay.
Even adding transcendence does not make these properties sufficient for
half retention. This changes the original BBP four-pole forcing; it supplies
no finite rational-function formula and does not refute the authentic source.

## 1. PCC-1 — arbitrary prescribed constant (PROVED)

Fix C>0, an integer L>=1, and rational reference Newton coefficients
$a_n^*$ satisfying $v_2(a_n^*)=n-1$ for every n>=1. The authenticated
coefficients from [the Pascal source theorem](PI_PASCAL_MAHLER_SOURCE.md)
are an admissible reference. There exist rational coefficients a_n and
an entire function w, real on the real axis, such that

$$
a_n-a_n^*\in2^{n-1+L}\mathbb Z_2,\qquad
\frac32C<w(x)<\frac52C\quad(0\le x\le1).
\tag{PCC-1}
$$

For integers n>=0 define
$$
\eta_n=\int_0^1x^n(1-x)w(x)\,dx,\qquad
H_n=C16^n-\eta_n.
$$

Then $\eta_0=C$, $H_0=0$, and every H_n is rational. For n>=1,

$$
s(n):=H_n-16H_{n-1}=16\eta_{n-1}-\eta_n\in\mathbb Q.
\tag{PCC-2}
$$

The source s has the complete dyadic profile and fixed-precision agreement
specified in Section 3 below, and a compatible completely monotone real
analytic extension specified in Section 4. Its real weighted sum is

$$
\sum_{n\ge1}16^{-n}s(n)=C.
\tag{PCC-3}
$$

The BBP-normalized constant is 16C; the zero-initial-state recurrence is H_n.

## 2. Construction and the rationality distinction

Let L_n(x) be the monic rational polynomial of degree n orthogonal to
lower degrees for the weight 1-x on [0,1]. Its rational Gram matrix has
entries $1/((i+j+1)(i+j+2))$ and is positive definite. As in PAB-2,

$$
\beta_n=\int_0^1x^n(1-x)L_n(x)\,dx
=\int_0^1(1-x)L_n(x)^2\,dx>0
$$

is rational. Put $B_n=\sum_j|[x^j]L_n|n^j$ for the disc |x|<=n and construct

$$
w(x)=2C+\sum_{n\ge1}\lambda_nL_n(x),\qquad
|\lambda_n|B_n<C2^{-n-1}.
\tag{PCC-4}
$$

The lambda_n are now real numbers; their rationality is not required.
At stage n, let $\eta_n^{\rm old}$ be the moment of the existing finite
density and put

$$
A_n=\frac{C16^n-\eta_n^{\rm old}
-\sum_{j<n}a_j n^{\underline j}}{n!}.
$$

Rationals in any fixed dyadic coset are dense in the real line, by the
odd-denominator construction in PAB-2. Choose rational a_n in the coset
of PCC-1 so that

$$
|a_n-A_n|<\frac{\beta_n C2^{-n-1}}{n!B_n},\qquad
\lambda_n=\frac{n!}{\beta_n}(A_n-a_n).
\tag{PCC-5}
$$

This satisfies PCC-4 and sets the n-th moment to the required value;
orthogonality preserves all earlier moments, including $\eta_0=C$.
The compact-disc budgets make the infinite series converge locally
uniformly on the complex plane. On [0,1] their sum is strictly below
C/2, proving positivity and the stated entire extension.

At each nonnegative integer n the Newton series terminates. Consequently

$$
H_n=\sum_{j=1}^n a_j n^{\underline j}\in\mathbb Q.
\tag{PCC-6}
$$

Later corrections preserve this equality exactly. Therefore PCC-2 is
rational. The tail moments eta_n need not be rational: if C is irrational,
every $\eta_n=C16^n-H_n$ is irrational. What is rational is every forcing
moment $\int_0^1x^n(16-x)(1-x)w(x)\,dx=s(n+1)$.

## 3. Full dyadic profile and fixed-precision agreement

The rational coefficients define the single dyadic analytic series

$$
H(t)=\sum_{n\ge1}a_n t^{\underline n},\qquad |t|_2<2.
$$

Since L>=1, PCC-1 gives $v_2(a_n)=n-1$. PAB-1 applies unchanged:
H fixes zero, is a bijective isometry of $\mathbb Z_2$, and

$$
v_2(\Delta^kH(t))=v_2(\Delta^ks(t))=k-1+v_2(k!),
\quad t\in\mathbb Z_2,\ k\ge1,
\tag{PCC-7}
$$

where $s(t)=H(t)-16H(t-1)$. Indeed the leading term of the k-th
difference is a_k k!; the term indexed k+j has excess valuation at
least $j+v_2\binom{k+j}{k}\ge1$. The factor 16 in s cannot cancel
the leading valuation. The Gauss-norm bound on any disc 1<R<2 is
$2(R/2)^n$, justifying convergence and termwise finite differences.

Writing $F^*(t)=\sum a_n^*t^{\underline n}$ and
$s^*(t)=F^*(t)-16F^*(t-1)$, the same termwise calculation gives

$$
v_2\!\left(\Delta^k(H-F^*)(t)\right),\quad
v_2\!\left(\Delta^k(s-s^*)(t)\right)
\ \ge k-1+v_2(k!)+L.
\tag{PCC-8}
$$

Here k>=1 and t is any dyadic integer; zero differences have valuation
infinity. The precision L is fixed in advance, not infinite precision.
Also $\sum_{j\ge0}16^j s(t-j)=H(t)$ by telescoping, so the contracting
particular solution has exactly the prescribed initial value zero.

### PCC-4 — any fixed finite set of prime congruences (PROVED)

Fix a finite prime set S containing 2 and let
$\mathbb Z_{(S)}=\{a/b\in\mathbb Q:p\nmid b\text{ for every }p\in S\}$.
The construction can additionally choose every coefficient in

$$
a_n\in a_n^*+M_n\mathbb Z_{(S)},\qquad
M_n=\prod_{p\in S}p^{e_{p,n}},\qquad
e_{2,n}=n-1+L,\quad
e_{p,n}=\max\{L,v_p(a_n^*)+L\}\ (p\ne2).
\tag{PCC-13}
$$

All exponents are nonnegative integers. This rational coset is real-dense:
take arbitrarily large positive $D\equiv1\pmod{\prod_{p\in S}p}$ and
choose an integer k nearest to $D(A-a_n^*)/M_n$. Then
$a_n^*+M_n k/D$ belongs to the coset and differs from the real target A
by at most $M_n/(2D)$. Thus PCC-5 can meet its unchanged real error budget.
For every n>=1 and p in S this guarantees

$$
v_p(a_n)=v_p(a_n^*),\qquad
v_p(a_n-a_n^*)\ge\max\{L,v_p(a_n^*)+L\}.
\tag{PCC-14}
$$

For p=2, the maximum equals n-1+L. For the authenticated reference, let
U_n and r(n) denote its actual unwrapped source and forcing. Because the
Newton sums at nonnegative integers are finite, with integer falling
factorials, PCC-14 implies, for every p in S,

$$
H_n-U_n\in p^L\mathbb Z_{(p)}\quad(n\ge0),\qquad
s(n)-r(n)\in p^L\mathbb Z_{(p)}\quad(n\ge1).
\tag{PCC-15}
$$

The forcing conclusion follows by subtracting 16 times the preceding
state difference. No claim at negative integer times or about a full
odd-prime analytic interpolation is made. These are rational coefficient
and source-value congruences at a fixed finite collection of places.

In particular S={2,3,5,7,11,13} is allowed while retaining the fixed
Liouville counterexample below. Finite-prime congruences do not imply
invariance of the real orbit law under multiplication by 3: taking C=1/15
instead gives law $\delta_{1/15}$, because 16 is 1 modulo 15, whereas its
tripled law is $\delta_{1/5}$. The vanishing source tail preserves these laws.
Nor can arbitrary-C freedom extend to positive absolute precision at every prime
simultaneously: a nonzero rational difference has valuation zero at some
prime, so such simultaneous congruences would force every difference zero.

## 4. Real forcing and the two-extension boundary

The density bounds give, for n>=0,

$$
\frac{3C}{2(n+1)(n+2)}<\eta_n<\frac{5C}{2(n+1)(n+2)}.
\tag{PCC-9}
$$

For real t>0 define

$$
s_{\mathbb R}(t)=\int_0^1x^{t-1}(16-x)(1-x)w(x)\,dx.
$$

This is real analytic and strictly completely monotone: its k-th
derivative inserts $(\log x)^k$ under a strictly positive integral.
At every positive integer it equals the rational value s(n), with

$$
\frac{45C}{2n(n+1)}<s(n)<\frac{40C}{n(n+1)},\qquad
\sum_{j\ge1}16^{-j}s(n+j)=\eta_n.
\tag{PCC-10}
$$

The last identity follows by telescoping and proves PCC-3 at n=0.
The real and dyadic extensions agree at positive integers through their
rational values. We assert neither rational values at every rational real
argument nor one power series converging in both completions.

## 5. PCC-2 — a fixed transcendental nonnormal constant (PROVED)

Choose once and for all

$$
C=\sum_{j\ge2}16^{-j!}>0.
\tag{PCC-11}
$$

Its base-16 digits are 1 at the distinct positions j! and zero elsewhere;
this expansion is not eventually periodic, so C is irrational. The m-th
truncation has reduced denominator $q_m=16^{m!}$ and error
$0<C-C_m<2q_m^{-m-1}$. If C were algebraic of degree d, an integer
minimal polynomial and the mean-value theorem on a fixed neighborhood
would give $|C-a/q|\ge c q^{-d}$ for rational a/q sufficiently near C:
$q^dP(a/q)$ is a nonzero integer, while $|P(a/q)|\le M|C-a/q|$.
The truncations contradict this inequality. Thus C is transcendental.

For fixed K, among n<N there are at most
$K\#\{j!:j!\le N+K\}=O(K\log(N+K))$ indices whose next K digits
include a 1. Otherwise $x_n=\{16^nC\}\le16^{-K}/15$. First letting
N grow and then K grow proves empirical convergence of x_n to delta_0
on the circle. Since $y_n=\{H_n\}=\{16^nC-\eta_n\}$ and eta_n tends
to zero, the source has the same empirical circle law. C is nonnormal
in base 16, and its binary zero-digit density is also one.

## 6. PCC-3 — quantitative central retention (PROVED)

Take integer u>=1, $W_u=\{u,\ldots,4u-1\}$, N=3u, and
$K_u=\lceil3\log_{16}(4u)\rceil$. Among indices n in [u,4u], mark
those having a factorial position in (n,n+K_u]. There are
$O((\log u)^2)$ marked indices. At every unmarked index,
$x_n\le(4u)^{-3}/15<\eta_n$ for all sufficiently large u, by PCC-9.
Thus, with $\epsilon_u=5C/(2(u+1)(u+2))$,

$$
1-\epsilon_u<y_n=1-\eta_n+x_n<1.
$$

Let G_u consist of n in W_u for which both n and n+1 are unmarked.
Then $|G_u|\ge N-O((\log u)^2)$. Its literal next carry is exactly 15:
the next digit of C16^n is zero, so $x_{n+1}=16x_n$, while the displayed
formula for y at both indices and PCC-2 give
$16y_n+s(n+1)-y_{n+1}=15$. Carries outside G_u are not asserted equal.

Write $\delta_{s,t}$ for the centered representative of $y_t-y_s$.
For each pair in $G_u^2$, both current and successor centered differences
have modulus below epsilon_u; the ordinary differences already are the
centered ones. Their equal literal carries give centered carry zero.
Define the inherited counts

$$
Q_{W_u^+}(\tau)=\#\{(s,t)\in W_u^2:|\delta_{s+1,t+1}|\le\tau\},
\quad
Z_{W_u}(\tau)=\#\{(s,t)\in W_u^2:
|\delta_{s,t}|\le1/32,\ |\delta_{s+1,t+1}|\le\tau\}.
$$

For all sufficiently large u and every $\epsilon_u\le\tau\le1/4$,

$$
(N-O((\log u)^2))^2\le Z_{W_u}(\tau)
\le Q_{W_u^+}(\tau)\le N^2.
\tag{PCC-12}
$$

Therefore the retention ratio tends to 1 uniformly over these radii,
in particular over any prescribed family whose minimum radius is
much larger than u^-2. For every fixed theta<1 and A>=0,
$Z_{W_u}(\tau)\le\theta Q_{W_u^+}(\tau)+AN$ fails for large u.
Canonical representatives concentrate near 1 here; delta_0 is a claim
about the circle, where 0 and 1 are identified.

## 7. Verdict, scope and next falsifiers

**REFUTED:** the listed profile, precision, positivity, decay, rational
values at positive integers, transcendence, and finite-prime source congruences
suffice for half or 1/16 retention. PCC-11/PCC-12 are the receipt.
**OPEN:** the first such saving for the authentic BBP forcing.
The [prime-height boundary](PI_PASCAL_PRIME_HEIGHT.md) still applies to
that fixed rational formula. No numerical test is proof authority here.
Next falsifiers are requiring rational lambda_n, confusing rational source
and tail moments, omitting the successor condition in G_u, or transferring
the construction to fixed finite rational poles without a new argument.
