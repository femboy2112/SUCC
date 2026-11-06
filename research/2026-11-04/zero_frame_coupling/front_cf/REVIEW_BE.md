# Independent pass over BE-02 and BE-03

**Verdict: both paper arguments survive this review.** This is a second
same-model agent's derivation, sharing source provenance; it is not external
refereeing or Lean authority. No source, mathematical or quantifier blocker
was found.

## BE-02: complex C2 observer and maximal boundary

Set `F(x)=x^3 w(x)` and `g(x)=e(-c Lambda/x^2)`. Then
`g'=4 pi i c Lambda x^-3 g`. The first integration by parts has the exact
coefficient `F/(4 pi i c Lambda)`. Applying it again to F' gives two
bounded endpoint terms and an integral involving `(x^3 F')'`; these are
uniformly O_(w,c)(Lambda^-2) for every a,b. C2 regularity suffices. Complex
w causes no positivity issue because all estimates use its norm or absolute
variation.

At a maximizing x0, `|F(x0)|=B_w>0`. One inward side has positive length,
and a half-turn point exists there for large Lambda because the real phase
derivative never vanishes. Its distance from x0 is O_c(1/Lambda). The
endpoint exponentials are opposite, while `F(other)=F(x0)+O_w(1/Lambda)`.
Thus the boundary numerator has modulus `2B_w+O_(w,c)(1/Lambda)`, including
complex amplitudes and endpoint maxima. This gives exactly
`B_w/(2 pi |c| Lambda)`. Taking w with compact interior support does not
remove this **maximal-subinterval** contribution.

Substitution `c=ell/32` gives BE3's `16B_w/(pi|ell|)` coefficient.
For the coherent coupled seed `c=(2ell+1)/64` gives BE5's
`32B_w/(pi|2ell+1|)`. No integer ell makes this coefficient vanish.
The reciprocal observer has `B_w=8/3`, confirming both stated constants.
Uniform pointwise source error, finite variation Riemann comparison, and
rounding endpoints each fit `O_(w,ell)((1+Lambda)/A)`. Multiplying by
Lambda needs `Lambda^2/A -> 0`, exactly as stated.

## BE-03: ordinary conditional convergence is genuinely covered

The first step is valid. If the series `sum a_l d_l` converges, its partial
sums converge and are bounded. In a sufficiently late tail, d_l stays
bounded away from zero, and `1/d_l` has finite variation because
`z'(x)=O(x^-2)`. Summation by parts therefore makes `sum a_l` converge:
the terminal product converges and the variation series is absolutely
bounded by the bounded weighted partial sums. Finite initial terms and any
early zero d_l are irrelevant. No absolute convergence of a_l is assumed.

Writing S_N for its partial sums, finite Abel summation yields
`sum_(l<=N) a_l q^l=S_N q^N+(1-q)sum_(l<N)S_l q^l`. The nonnegative
weights sum to q<=1, so the claimed uniform bound by B is correct even for
complex coefficients. Hence `|F_N(q)|<=2B`. Ordinary convergence also
gives the usual Abel endpoint limit, so the limiting symbol F is continuous
on [0,1], including q=1 where F=0. The bound supplies the exact dominated
convergence needed inside every Mellin integral.

The resulting bracket is continuous. Polynomials in t^8 are dense because
t->t^8 is a homeomorphism. Applying the vanishing moments to polynomial
approximants of the conjugate bracket forces its squared modulus integral
to zero; continuity then forces pointwise vanishing. The exact radial
logarithmic derivative has a zero at `2-sqrt(2)`, whereas the original
density is strictly positive there. This is a contradiction independent of
endpoint asymptotics. Indeed continuity at t=0 would supply another
contradiction (`P_o(0)=4`, bounded F and the factor t^8), but the displayed
interior-zero proof already suffices and makes the authentic source
mismatch explicit.

The scope is correctly limited to one fixed coefficient sequence and ordinary
series convergence at every n. No conclusion about n-dependent coefficients,
nonordinary summation or selected Weyl decay is justified or claimed.

### Extension reviewed: finite lookback and eventual identities

The strengthened BE7 with fixed `J>=0`, lags `ell>=-J`, and equality only
for `n>=N>=J+1` also survives. The convergence-to-bounded-partial-sums
argument concerns only positive lags and is unchanged by finitely many
lookback terms. These contribute a finite Laurent polynomial. Consequently
the partial symbols satisfy `|F_L(q)|<=C(1+q^-J)` on `(0,1]`; uniform
boundedness at q=0 is neither needed nor asserted.

For every n>=N the dominated majorant is
`C t^(8n)|K_z(t)|(1+t^(-8J))`. Its worst origin exponent is
`8(n-J)>=8`, so it is integrable. For the eventual moment family, the
weighted bracket
`W=t^(8N-8)P_o+t^(8N)K_z F(t^8)` extends continuously to zero: its
potentially singular factor has worst net exponent `8(N-J)>=8`, and the
remaining analytic power series is bounded near zero. At t=1, Abel
continuity remains valid. Thus the t^8-polynomial density argument applies
exactly as before. At the interior source zero tau, its nonradial term is
`tau^(8N-8)P_o(tau)>0`, contradicting W=0. Finite lookback cannot create a
singularity at tau to evade this contradiction.

The earlier additional endpoint-zero contradiction is specific to the
original future-only presentation; the interior-zero contradiction is the
one used for this extension. No stronger source or convergence hypothesis
has been silently inserted.

## Exact cross-check executed

A separate Python/SymPy/Fraction command verified:

- the exact radial rational/logarithmic derivative identity;
- divisibility of the radial numerator by `t^2-4t+2`;
- the original positive density factorization;
- the finite Abel decomposition and its bound for the conditionally
  convergent example `a_l=(-1)^l/l`, at N=1,2,17,53 and
  q=0,1/7,13/17,1.

It exited zero and printed
`BE_REVIEW_SYMBOLIC_SOURCE_AND_FINITE_ABEL_IDENTITIES_PASS`.
These are finite algebra checks; the convergence and maximality claims are
supported by the paper arguments reviewed above.
