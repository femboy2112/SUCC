# Positive rational non-coboundary sources with rational selected phases

**Status: PROVED LOCAL, PAPER.** Exact finite algebra is independently
checkable; the quantified analytic arguments are given below. Scholarly
priority is unverified. This is a stronger hostile control than the
rational-coboundary counterfeits in
[the Green analysis](PI_SOURCE_GENESIS_GREEN.md).
It does not retain the exact four BBP poles and residues.
**PI NORMALITY PROVED: NO.**

The question was whether positivity, infinite Hankel rank, rational forcing,
a nonzero rational-coboundary invariant, and arbitrarily many correct BBP
tail asymptotic terms could nevertheless coexist with a rational selected
phase. The answer is **yes**, with the complete source contract verified
below. The mechanism is a rational logarithmic derivative whose boundary
integral vanishes. A rational telescoping obstruction does not prevent this
different exact cancellation.

The simplest explicit family is

\[
V_m(t)=F(t)-\frac{(1-t)^{4m}}{4(1+(1-t)^2)},\qquad m\geq1,
\]

where $F$ is the authentic BBP density. Each member is positive, has
rational integral, and retains the same nonzero pole invariant. The
endpoint agreement order tends to infinity with $m$. Section 6 proves
this complete family; the preceding sections establish its smallest
member and all its source contracts.

## 1. A zero-integral rational source

On $0\leq t\leq1$, put

\[
Q(t)=8-8t-4t^2-8t^3-2t^4-2t^5+t^6,
\qquad
L(t)=\frac{Q(t)}{16-t^8}.
\tag{1}
\]

Exact factorization and partial fractions give

\[
Q(t)=(t^2+2)(t^2-4t+2)(t^2+2t+2),
\]

\[
L(t)=\frac{t}{t^2-2}
-\frac{t-1}{t^2-2t+2}
=\frac12\frac{d}{dt}
\log\frac{2-t^2}{t^2-2t+2}.
\tag{2}
\]

All logarithm arguments are positive on this interval. The ratio inside
the logarithm is 1 at both endpoints. Therefore

\[
\int_0^1L(t)\,dt=0.
\tag{3}
\]

This is an elementary exact identity, not a numerical zero detection.
It is compatible with the classical BBP zero relation; the derivation
here uses only polynomial identities, differentiation and the fundamental
theorem of calculus.

## 2. An explicit positive non-coboundary counterfeit

Let the authentic BBP density in the $t$ variable be

\[
F(t)=\frac{4-2t^3-t^4-t^5}{16-t^8}.
\]

Define two other continuous rational densities by

\[
W(t)=\frac{L(t)+1}{4},
\qquad
V(t)=W(t)-\frac{(1-t)^2}{4}.
\tag{4}
\]

They are positive on $[0,1)$ and vanish at 1. This follows from the
following explicit polynomial identities:

\[
W(t)=\frac{(1-t)
 (24+16t+12t^2+4t^3+2t^4+t^6+t^7)}
 {4(16-t^8)},
\tag{5}
\]

\[
V(t)=\frac{(1-t)
 (8+32t+12t^2+4t^3+2t^4+t^6+t^7+t^8-t^9)}
 {4(16-t^8)}.
\tag{6}
\]

In (6), group the last two terms as $t^8(1-t)$; every other displayed
coefficient is positive. The denominator is at least 60. This verifies
positivity throughout the entire integration domain.

By (3),

\[
\int_0^1W(t)\,dt=\frac14,\qquad
\int_0^1V(t)\,dt=\frac14-\frac1{12}=\frac16.
\tag{7}
\]

Define, for integers $n\geq0$,

\[
S_n=\int_0^1t^{8n}V(t)\,dt,
\tag{8}
\]

and, for integers $n\geq1$,

\[
r_V(n)=\int_0^1t^{8n-8}(16-t^8)V(t)\,dt.
\tag{9}
\]

Then $r_V(n)>0$ and $16S_{n-1}-S_n=r_V(n)$ exactly. Since $V$ is
integrable, $(S_n)$ is bounded, tends to zero by dominated convergence,
and is the unique bounded backward Green solution for this forcing.
Its initial mass is exactly $S_0=1/6$.

Moreover $(16-t^8)V(t)$ is the polynomial with coefficients

\[
(c_0,\ldots,c_{10})
=(2,6,-5,-2,-1/2,-1/2,1/4,0,0,-1/2,1/4).
\tag{10}
\]

Thus the forcing is the explicit rational function

\[
\boxed{r_V(n)=\sum_{j=0}^{10}\frac{c_j}{8n-7+j}.}
\tag{11}
\]

Every denominator in (11) is positive for integer $n\geq1$.
The integral (9), rather than the signs of individual residues, proves
its strict positivity.

With initial state $y_0^V=0$ and

\[
y_{n+1}^V=\{16y_n^V+r_V(n+1)\},
\]

the corrected circle orbit is

\[
\{y_{j+1}^V+S_{j+1}\}
=\{16^{j+1}S_0\}
=\{16^j(8/3)\}
=2/3
\quad(j\geq0).
\tag{12}
\]

Its positive-lag character is identically 1 for every integer frequency,
and the selected phase is not normal. This is an actual forced source
with the stipulated initial state, not an unforced orbit falsely assigned
the BBP forcing.

## 3. A genuine rational-coboundary obstruction

For any rational function $R(z)$ and any fixed representative $a$, define
the finite sum

\[
\mathcal I_a(R)
=\sum_{k\in\mathbb Z}16^{-k}
\operatorname{Res}_{z=a+k}R(z).
\tag{13}
\]

Only finitely many terms can be nonzero. Here the residue is the
coefficient of $(z-a-k)^{-1}$, including when higher-order poles are
present.

**N1.** If a rational function $q$ satisfies

\[
R(z)=16q(z-1)-q(z),
\tag{14}
\]

then $\mathcal I_a(R)=0$ for every $a$.

Proof: writing $b_k=\operatorname{Res}_{z=a+k}q(z)$, translation gives
the residue $16b_{k-1}-b_k$ in (14). Consequently

\[
\sum_k16^{-k}(16b_{k-1}-b_k)
=\sum_k16^{-k}b_k-\sum_k16^{-k}b_k=0.
\]

All sums are finite, so no convergence hypothesis is needed. Polynomial
parts have no residues. This proves the obstruction for arbitrary rational
$q$, not only for simple-pole trial functions.

For the explicit source (11), the pole class $a=3/4$ contains exactly
two nonzero residues:

\[
\operatorname{Res}_{z=3/4}r_V(z)=\frac34,\qquad
\operatorname{Res}_{z=-1/4}r_V(z)=-\frac1{16}.
\]

The second pole has shift index $k=-1$. Therefore

\[
\boxed{\mathcal I_{3/4}(r_V)
=\frac34+16\left(-\frac1{16}\right)=-\frac14\ne0.}
\tag{15}
\]

There is **no rational-function** solution to (14) for $R=r_V$.
If a rational function of $n$ agreed with the tail values $S_n$ at all
nonnegative integers, its recurrence would give a rational-function
identity on infinitely many points and hence everywhere; (15) excludes
this too.

**Rational-value distinction.** Every individual $S_n$ is nevertheless
rational, by $S_0=1/6$, rationality of $r_V(n)$, and the finite recurrence.
The excluded object is a *single rational function of the index* producing
the whole sequence. Rational individual values and a rational-function
realization are different properties.

For a useful invariant explanation, the source (1) has forcing

\[
r_L(n)=\int_0^1t^{8n-8}Q(t)\,dt.
\]

Its class $3/4$ has just the residue $-8/8=-1$. For any polynomial
$P(t)=\sum_jp_jt^j$, its tail readout

\[
B_P(n)=\int_0^1t^{8n}P(t)\,dt
=\sum_j\frac{p_j}{8n+j+1}
\tag{16}
\]

is a rational function of $n$. Adding $P$ to a density adds the rational
coboundary $16B_P(n-1)-B_P(n)$ to its forcing, and therefore changes none
of the invariants (13). The densities $W,V$ both contain $L/4$ plus
polynomials, which explains their common invariant $-1/4$.

## 4. Exact all-index proximity to the authentic BBP tail

There is a particularly simple exact difference:

\[
\boxed{F(t)-V(t)=
\frac{(1-t)^4}{4(t^2-2t+2)}
=\frac{(1-t)^4}{4(1+(1-t)^2)}.}
\tag{17}
\]

This follows by multiplication by the nonzero polynomial denominators;
it requires no asymptotic approximation. If

\[
T_n=\int_0^1t^{8n}F(t)\,dt
\]

is the authentic tail, then for every integer $n\geq0$,

\[
\boxed{
\frac3{\prod_{\ell=1}^5(8n+\ell)}
<T_n-S_n<
\frac6{\prod_{\ell=1}^5(8n+\ell)}.}
\tag{18}
\]

Indeed, on $(0,1)$ the reciprocal denominator in (17) is strictly between
$1/2$ and 1, and

\[
\int_0^1t^{8n}(1-t)^4\,dt
=\frac{24}{\prod_{\ell=1}^5(8n+\ell)}.
\]

In particular $S_n$ and $T_n$ have the same asymptotic terms through
$n^{-4}$ and differ by $O(n^{-5})$, while their selected circle trajectories
have completely different known source contracts. Both have leading
coefficient $1/64$ at $n^{-2}$.

The difference can be sharpened asymptotically:

\[
n^5(T_n-S_n)\longrightarrow \frac6{8^5}.
\tag{19}
\]

For example, this follows by applying the beta concentration argument to
the continuous multiplier $[4(1+(1-t)^2)]^{-1}$, whose endpoint value
is $1/4$. This asymptotic statement is not needed for the exact bound (18).

## 5. Strict moment positivity and complete source membership

With $u=t^8$, the density for (8) is

\[
d\mu_V(u)=\frac{V(u^{1/8})}{8u^{7/8}}\,du.
\tag{20}
\]

It is positive on $(0,1)$, behaves integrably as $O(u^{-7/8})$ at zero,
and vanishes linearly at one. Thus, for every $n,k\geq0$,

\[
(-1)^k\Delta^k S_n
=\int_0^1u^n(1-u)^k\,d\mu_V(u)>0.
\]

For every nonzero polynomial $p$,

\[
\int_0^1|p(u)|^2\,d\mu_V(u)>0.
\]

Every finite Hankel matrix is strictly positive definite, and no fixed
finite-dimensional time-homogeneous linear realization exists. These are
the same classical moment arguments used for the authentic source, now
with the counterfeit's own verified density.

Consequently the explicit counterfeit simultaneously has:

- positive rational forcing on all integer $n\geq1$;
- a unique bounded Green tail and the exact forward/backward identity;
- initial state $y_0=0$;
- strict Hausdorff positivity and every Hankel rank;
- a nonzero rational-coboundary pole invariant;
- the authentic tail coefficient $1/64$ and two further matching
  asymptotic orders, with the all-index comparison (18);
- a rational selected boundary phase and identically resonant lag
  characters.

The authentic BBP forcing has no pole in class $3/4+\mathbb Z$; its
invariant there is zero. Equation (15) therefore also proves that this
counterfeit does **not** retain the exact BBP pole data. It is not a
counterexample to a theorem whose hypotheses authenticate those data.

## 6. An explicit arbitrary-order family

**N2.** For every integer $m\geq1$, put $u=1-t$ and define

\[
V_m(t)=F(t)-\frac{u^{4m}}{4(1+u^2)},\qquad
S_n^{(m)}=\int_0^1t^{8n}V_m(t)\,dt.
\tag{21a}
\]

For $m=1$, this is precisely the density $V$ in (4). For all $m\geq1$,

\[
0<V_1(t)\leq V_m(t)<F(t)\quad(0\leq t<1),
\tag{21b}
\]

where the middle equality can occur at $t=0$ or $m=1$. Positivity follows
because $0\leq u\leq1$ implies $u^{4m}\leq u^4$, and the strict final
inequality follows from $u>0$ on this domain.

Polynomial division gives

\[
\int_0^1\frac{u^{4m}}{1+u^2}\,du
=\frac{\pi}{4}-\sum_{k=0}^{2m-1}\frac{(-1)^k}{2k+1}.
\tag{21c}
\]

For completeness, division yields the alternating even polynomial
$u^{4m-2}-u^{4m-4}+\cdots+u^2-1$ plus $1/(1+u^2)$.
Termwise integration proves (21c), using only the elementary arctangent
integral. Since $\int F=\pi/16$,

\[
\boxed{
S_0^{(m)}
=\frac14\sum_{k=0}^{2m-1}\frac{(-1)^k}{2k+1}\in\mathbb Q.}
\tag{21d}
\]

Thus the selected phase is the rational number
$4\sum_{k=0}^{2m-1}(-1)^k/(2k+1)$. Its reduced denominator is odd,
because every summand has odd denominator. Multiplication by 16 is
invertible modulo that denominator, so the circle orbit is purely
periodic from time zero. These selected real phases approach $\pi$ from
below as $m\to\infty$, by the alternating-series theorem. The convergence
does not turn any individual rational orbit into a normal orbit.

The forcing from each $V_m$ is rational: the factor
$1+(1-t)^2=t^2-2t+2$ divides $16-t^8$, so multiplying (21a) by
$16-t^8$ gives a polynomial. The forcing is strictly positive by its
positive integral representation.

Moreover

\[
V_m(t)-V_1(t)
=\frac{u^4-u^{4m}}{4(1+u^2)}
\tag{21e}
\]

is a polynomial with rational coefficients. Indeed, $u^{4m}-u^4$ is
divisible by $u^4-1$, and hence by $1+u^2$; $m=1$ gives the zero
polynomial. Equations (15)--(16) now prove

\[
\boxed{\mathcal I_{3/4}(r_{V_m})=-1/4\ne0}
\tag{21f}
\]

for every $m$. The strict Hausdorff and all-order Hankel conclusions
also hold, by positivity of the full-support density.

Finally, for every pair of integers $n\geq0,m\geq1$,

\[
\boxed{
\frac{(4m)!}{8\prod_{\ell=1}^{4m+1}(8n+\ell)}
<T_n-S_n^{(m)}<
\frac{(4m)!}{4\prod_{\ell=1}^{4m+1}(8n+\ell)}.}
\tag{21g}
\]

This is the same beta integral proof as (18), with exponent $4m$.
In particular the density derivatives through order $4m-1$ agree
exactly at 1, and the tail error is $O_m(n^{-4m-1})$.
Given any finite prescribed endpoint order $J$, choose $4m>J$.
This supplies the promised single-source counterexample satisfying
arbitrarily many correct asymptotic terms and the non-coboundary
condition simultaneously.

The formulas define a family of distinct exact sources. They do not
assert that one fixed counterfeit matches the authentic endpoint jet
to every order; analyticity would make that a different question.

## 7. A construction at each prescribed endpoint order

**N3.** Fix an integer $M\geq1$ and a nonzero rational $\epsilon$. There is
an explicitly constructible continuous rational density $V_{M,\epsilon}$
on $[0,1]$ such that:

1. it is strictly positive on $[0,1)$;
2. its integral is rational;
3. its forcing is a positive rational function with
   $\mathcal I_{3/4}=-\epsilon\ne0$;
4. it matches the authentic density $F$ and all its derivatives through
   order $M$ at 1.

Its tail therefore differs from the authentic $T_n$ by
$O_{M,\epsilon}(n^{-M-2})$, while its selected rational phase is eventually
periodic.

Here is a construction with rational constants and an explicit positivity
proof. Let

\[
A(t)=\sum_{j=0}^{M}
\frac{(F-\epsilon L)^{(j)}(1)}{j!}(t-1)^j,
\qquad V^0(t)=\epsilon L(t)+A(t).
\tag{21}
\]

Every coefficient is rational: the two rational functions are regular at
1 and have rational coefficients. The values and derivatives through
order $M$ match $F$ there. In particular $V^0(1)=0$ and
$(V^0)'(1)=F'(1)=-1$.

The polynomial

\[
N(t)=\epsilon Q(t)+(16-t^8)A(t)
\]

is divisible by $1-t$. Define the rational-coefficient polynomial

\[
D(t)=\frac{N(t)}{1-t}.
\]

The endpoint derivative identity gives exactly $D(1)=15$. Write

\[
D(1-v)=15+\sum_{j=1}^{d}b_jv^j,\qquad
B=\sum_{j=1}^{d}|b_j|,
\]

\[
\delta=\min\left(1,\frac{15}{2(B+1)}\right),\qquad
C=\frac{B+1}{15\delta^M}.
\tag{22}
\]

All of these constants are rational, with $\delta,C>0$. Set

\[
\boxed{
V_{M,\epsilon}(t)=V^0(t)+C(1-t)^{M+1}.}
\tag{23}
\]

The added term does not change derivatives through order $M$ at 1.
For $v=1-t$ with $0\leq v\leq\delta$,

\[
D(1-v)\geq15-B\delta>15/2.
\]

For $\delta\leq v\leq1$, we have $D(1-v)\geq-B$, while

\[
C(16-t^8)v^M\geq15C\delta^M=B+1.
\]

Thus

\[
V_{M,\epsilon}(t)
=\frac{1-t}{16-t^8}
\left[D(t)+C(16-t^8)(1-t)^M\right]>0
\quad(0\leq t<1).
\tag{24}
\]

This proves global positivity, including the endpoints where a numerical
sample would be insufficient.

The integral is rational because $\int L=0$ and all remaining terms in
(23) are polynomials with rational coefficients. Its forcing is rational
because multiplying the density by $16-t^8$ leaves a polynomial. Its pole
invariant is $-\epsilon$: the forcing from $L$ contributes $-1$, while
every polynomial addition contributes a rational coboundary by (16).
The positive full-support density gives all the strict moment and Hankel
properties as before.

Finally, the density difference from $F$ is
$O((1-t)^{M+1})$ near 1. On the rest of the compact interval it is bounded.
Splitting the integral at a fixed interior point, the endpoint portion
is bounded by a constant times
$\mathrm B(8n+1,M+2)=O(n^{-M-2})$, and the other portion decays
geometrically. This proves the stated tail estimate with all convergence
conditions supplied.

For $M=1$ and $\epsilon=1/4$, the unmodified Taylor construction $V^0$
is exactly $W$. For $M=2$ or $M=3$, it is exactly $V$. These particular
instances already have the explicit positivity proofs (5)--(6), so the
extra positive term in (23) is unnecessary for them.

## 8. What this refutes, and what it does not

The simultaneous hypotheses of positive rational forcing, strict infinite
moment rank, a rational non-coboundary obstruction, authenticated zero
initial state, and any prescribed finite number of correct BBP tail
asymptotic terms do **not** force irrationality of the selected phase,
normality, or signed lag cancellation.

This is stronger than testing these hypotheses separately: one actual
source satisfies all of them together. The source class is still weaker
than the exact BBP source because of its additional pole class (15).
No global impossibility of exploiting the actual BBP residues, boundary
identity or a new arithmetic constraint has been proved.

The next source-specific theorem cannot be inferred merely from these
coarse properties, even when combined. It must use information that
distinguishes the authentic four-pole source from this explicitly
authenticated family. An unbounded-horizon signed correlation estimate
using that information would change the normality verdict; the controls
above do not supply it.
