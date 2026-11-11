# Exact finite Mellin aliases and source authentication

For a polynomial $`P`$ on $`[0,1]`$, write
$`R_P(s)=\int_0^1 x^{8s}P(x)\,dx`$ at nonnegative integer $`s`$.
Its completion is $`\Pi(P)=\int_0^1 P(x)/(1-x^8/16)\,dx`$.
The canonical polynomial is $`P(x)=4-2x^3-x^4-x^5=(1-x)M(x)`$,
where $`M(x)=(x^2+2)(x^2+2x+2)\ge 4`$.
Its four-pole moment sequence is the authentic BBP forcing and $`\Pi(P)=\pi`$.
In the recurrence convention $`U_0=0,\ U_{n+1}=16U_n+R_P(n)`$, the
completed observable at $`n\ge1`$ is $`16^{n-1}\Pi(P)`$.

## Fixed support and the sharp sample count

**PROVED.** Suppose the candidate forcing belongs to the proper simple-pole
class

```math
R(s)=\sum_{a\in\{1,4,5,6\}}\frac{c_a}{8s+a},
\qquad \sum_a c_a=0.
```

The sum constraint is the endpoint condition $`P(1)=0`$. Let
$`D(s)=\prod_a(8s+a)`$. Putting terms over $`D`$ cancels the cubic
coefficient of the numerator. Two such forcings agreeing at any three
distinct nonnegative integer indices are therefore equal as rational
functions. If there is no endpoint constraint, the numerator degree bound
is three and four samples suffice.

The three-sample result is sharp even with the same actual pole support
and positive endpoint-factored source. The perturbation
$`s(s-1)/D(s)`$ has partial-fraction coefficients
$`(3/1280,-1/8,65/256,-21/160)`$ in the displayed pole order. They sum to
zero and the corresponding polynomial perturbation $`\delta P`$ satisfies
$`\|\delta P/(1-x)\|_{\infty,[0,1]}<1`$, as follows by bounding the sum of
the absolute coefficients of the quotient. Adding it to the canonical
polynomial preserves positivity and all four poles. The moments at 0 and
1 agree, and the completion increases strictly since every perturbation
moment at $`s\ge2`$ is positive. The same degree argument gives a general
sample bound of $`u-1`$ with an endpoint constraint when the union of the
two allowed pole sets has size $`u`$.

## Independent ordinary alias verification

**PROVED.** Set $`t=x^8`$. For a positive measure $`\nu`$ with positive
density on $`(0,1)`$, the moment Gram is positive definite on each space
of polynomials in $`t`$. Let $`q`$ be the monic degree $`N+1`$
polynomial orthogonal to $`1,t,\ldots,t^N`$. For real $`z>1`$,
orthogonality applied to $`(q(z)-q(t))/(z-t)`$ gives

```math
q(z)\int \frac{q(t)}{z-t}\,d\nu
=\int \frac{q(t)^2}{z-t}\,d\nu >0.
```

Hence $`q(z)`$ has no real zero for $`z>1`$. Monicity and continuity give
$`q(16)>0`$ without a separate roots theorem.

For $`d\nu=(1-x)\,dx`$, the source
$`P+\epsilon(1-x)q(t)`$, where $`\epsilon=1/\|q\|_1`$ and
$`\|q\|_1`$ is the coefficient norm, is strictly positive on $`[0,1)`$.
Its first $`N+1`$ moments match exactly. Its completion difference
$`\Delta`$ obeys

```math
0<\frac{\epsilon\int q^2\,d\nu}{q(16)}
<\Delta
<\frac{16}{15}\frac{\epsilon\int q^2\,d\nu}{q(16)}.
```

The bounds use $`15<16-t<16`$ almost everywhere and the identity above.
The first changed moment is at $`N+1`$, where the perturbation equals
$`\epsilon\int q^2\,d\nu`$.

## A terminating rational alias with the literal zero seed

**PROVED.** For every $`N\ge0`$ and $`m\ge6`$, there is a rational
polynomial $`P_*`$, strictly positive on $`[0,1)`$ with a simple zero at
$`1`$, satisfying all of the following.

- $`R_{P_*}(j)=R_P(j)`$ for $`0\le j\le N`$. The uncompleted literal
  zero-seed orbit and carries therefore agree through the corresponding
  finite horizon.
- The coefficients of $`x^0,\ldots,x^{m-1}`$ equal those of $`P`$. The
  four canonical poles and their exact residues survive.
- The completed value $`\Pi(P_*)`$ is a dyadic rational. Its own complete
  future tail gives
  $`e^{2\pi i8k\,16^{n-1}\Pi(P_*)}=1`$ for all sufficiently large $`n`$
  and every integer $`k`$.

**Construction.** Put $`G(t)=1-t/16`$. For integer $`L\ge1`$ let
$`P_L(x)=P(x)(1-(t/16)^L)`$, so $`P_L/G`$ is a rational polynomial.
Choose $`L`$ with $`8L\ge m`$ and correct by
$`G(t)x^m(1-x)f_L(t)`$, where $`f_L`$ is the unique polynomial of degree
at most $`N`$ solving

```math
\int_0^1 t^j f_L(t)\,d\nu
=16^{-L}R_P(L+j),\qquad
d\nu=G(t)x^m(1-x)\,dx,\qquad 0\le j\le N .
```

The weight is positive on $`(0,1)`$. The Gram matrix is invertible and
rational, and its right-hand side tends to zero. Thus $`f_L`$ has rational
coefficients tending to zero as $`L\to\infty`$, and sufficiently large
$`L`$ gives $`\|f_L\|_1\le1`$. The correction cancels precisely the
first $`N+1`$ moment errors of $`P_L`$.

Take the monic degree $`N+1`$ polynomial $`q`$ for this new weight and set

```math
P_*(x)=P_L(x)+G(t)x^m(1-x)\bigl(f_L(t)+\eta q(t)\bigr).
```

This preserves the moments for any real $`\eta`$, and
$`\Pi(P_*)=C+\eta b`$, where $`C`$ is rational and

```math
b=\int_0^1 x^m(1-x)q(t)\,dx
=16\int \frac{q(t)}{16-t}\,d\nu>0 .
```

The positivity follows from the Cauchy-transform identity above.
Choose a dyadic rational in the open interval
$`(C,C+b/(2\|q\|_1))`$, and solve for $`\eta`$, which is rational.
Then $`P_* /(1-x)\ge 4(1-16^{-L})-1-1/2\ge 9/4`$ on the closed
interval, so the asserted endpoint and positivity hold. The factors
$`x^m`$ and $`t^L`$ preserve the low coefficients. If the chosen dyadic
has denominator $`2^d`$, then $`16^{n-1}\Pi(P_*)`$ is integral for
$`n\ge1+\lceil d/4\rceil`$, giving the claimed phase.

**Finite-prefix corollary.** At fixed $`N,m`$, the center $`C`$ tends
to $`\pi`$ as $`L\to\infty`$, because $`P_L/G`$ converges uniformly
to $`P/G`$ and $`\|f_L\|_1\to0`$. Dyadic choices can approach each
center from above arbitrarily closely. Since $`\pi`$ is irrational, it
lies in the interior of its cylinder for every prescribed finite
hexadecimal prefix. Choosing the completion within that cylinder
preserves the completed digits in the prefix and still gives eventually
constant phase. The same source can therefore pass any fixed joint
test of the forcing prefix, the low polynomial coefficients and the
completed digit prefix.

This construction changes the source while retaining the zero seed.
It is a separate control from retaining the canonical source and changing
the seed. Certifying the presence and residues of the four canonical poles
still leaves the additional-pole controls above. Certifying the complete
support, endpoint cancellation, and three exact values authenticates the
source within the indicated rational class. A finite collection of source
moments, even with the preserved residues and exact boundary convention,
therefore cannot support a cancellation argument uniform over unrestricted
polynomial forcing. An argument using the full source or a growing
sequence of constraints could distinguish these mutants.

## Reproduction

Run `python research/2026-11-10/main_xxiii/mellin_authentication_probe.py`
from the repository root. The probe obtains the orthogonal polynomials
by exact Gram–Schmidt, independently of the donor's Gaussian elimination.
It checks the ordinary alias by a separate exact finite geometric expansion
with a rigorous remainder. The donor calibration at $`N=0`$ gives
$`q(t)=t-1/45`$, and the additional holdouts $`N=9,12,16`$ agree with the
strict completion bounds. The four-pole control and all terminating
holdouts passed with exact rational arithmetic.

| $`N`$ | Coefficients preserved below degree $`m`$ | $`L`$ | Actual pole count | Dyadic denominator | Phase 1 from index |
|---:|---:|---:|---:|---:|---:|
| 0 | 6 | 1 | 14 | $`2^{16}`$ | 5 |
| 4 | 15 | 2 | 21 | $`2^{53}`$ | 15 |
| 9 | 24 | 4 | 31 | $`2^{95}`$ | 25 |
| 12 | 41 | 6 | 38 | $`2^{127}`$ | 33 |
| 16 | 64 | 8 | 45 | $`2^{166}`$ | 43 |

The motivating ordinary alias comes from the intrinsic-carrier donor
bundle. Its ZIP SHA-256 is
`5bdf6fc330a640a3e3837a0c7de5f1af7a398e8e2cce77d53356b076f94d6d10`.
All eleven entries in its internal hash manifest verified. The
terminating extension above uses that donor's orthogonality idea with a
different weight and a polynomial quotient, and the finite probe uses an
independent algorithm. These controls do not imply any cancellation
estimate for the authenticated four-pole source.
