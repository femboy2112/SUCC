# Positive source-jet residuals, divergent infinite compensation, and exact seed visibility

Paper proofs for the literal four-pole source and its authenticated radial
projection. These strengthen #506's fixed-order jet reconstruction. They do not
bound the original signed Weyl sum. Original pi normality remains OPEN.

Let E be forward shift, `(Ef)(n)=f(n+1)`. Put

    P_o(t)=4-2t^3-t^4-t^5,
    P_r(t)=2-2t-t^2-2t^3-t^4/2-t^5/2+t^6/4,
    rho(t)=-P_r(t)/(16-t^8).

The original forcing and genuine zero-seeded radial state have exact Mellin forms

    r_o(n)=integral_0^1 t^(8n-8) P_o(t) dt,
    Z_n=integral_0^1 t^(8n) rho(t) dt.                    (1)

The second identity follows from the completed radial period zero and its
absolutely convergent discounted tail. No altered seed is hidden in (1).
The source-derived zero at `tau=2-sqrt(2)` has

    rho(t)<0 for 0<t<tau, rho(t)>0 for tau<t<=1,
    rho(0)=-1/8, rho(1)=1/4.

Indeed #504's exact return law gives
`P_r(t)/(1-t^8/16)=4(t^2-4t+2)/[(t^2-2t+2)(2-t^2)]`.
The original P_o is strictly positive for 0<=t<1.

## AD-1. Exact generating function for every source-jet coefficient

Write `u=t^8`, `s=1-u`, and `v(s)=1-(1-s)^(1/8)`. The ratio of the original
forcing density to the radial-state density is

    A(u)=P_o(t)/(t^8 rho(t))
        =4(t-1)(16-t^8)/[t^8(t^2-4t+2)].                 (2)

For verification, factor
`P_o(t)=(1-t)(t^2+2)(t^2+2t+2)` and use
`(t^2+2t+2)(t^2-2t+2)=t^4+4`, `(t^2+2)(2-t^2)=4-t^4`.
Thus near s=0,

    A(1-s)=4 v(s) [16/(1-s)-1]/[1-2v(s)-v(s)^2]
          =sum_(k>=1) b_k s^k.                         (3)

EVERY b_k is a strictly positive rational number. The nonconstant coefficients
of v are positive; `16/(1-s)-1=15+16s+16s^2+...`; and the reciprocal
`1/(1-2v-v^2)` has nonnegative coefficients and constant one. Positivity is
strict in every positive degree because the first product already contributes
`60 [s^k]v>0`.

The unique m-delay polynomial from #506 is precisely

    P_m(E)=-sum_(k=1)^m b_k(1-E)^k
           =sum_(ell=1)^m a_ell^(m)(E^ell-1),
    a_ell^(m)=(-1)^(ell+1) sum_(k=ell)^m binom(k,ell)b_k. (4)

In particular each delay coefficient has the indicated alternating sign.
The first coefficients are

    b_1=15/2, b_2=421/32, b_3=4551/256,
    b_4=179123/8192.

Equation (4) gives the inherited first three delay vectors exactly. A Taylor
zero of order m+1 at t=1 makes `r_o(n)+P_m(E)Z_n=O_m(n^(-m-2))` by (1).
The inherited Vandermonde uniqueness (or triangular coefficient matching in
(3)) identifies this polynomial with the unique source-jet solution.

## AD-2. Every finite residual is positive, and its first surviving jet is exact

For EVERY integer n>=1 and m>=1, define

    epsilon_m(n)=r_o(n)+P_m(E)Z_n.

Then

    epsilon_m(n)>0,                                    (5)
    epsilon_m(n)=[(m+1)! b_(m+1)/32] n^(-m-2)
                 +O_m(n^(-m-3)) as n->infinity.        (6)

This is an all-n signed source inequality and proves that no finite delay order
accidentally removes one extra jet. It is not cancellation of a Weyl character.

Proof of (5). Set `S_m(s)=sum_(k=1)^m b_k s^k`. The residual is the integral
of `t^(8n) rho(t)[A(t^8)-S_m(1-t^8)]`, with the product interpreted continuously
at t=tau. On tau<t<1, rho>0 and s<sigma:=1-tau^8. The positive series (3)
converges there, so its remainder is strictly positive. On 0<t<tau, rho<0,
A(t^8)<0 and S_m>0, so the product is again strictly positive. At t=tau the
product equals `P_o(tau)/tau^8>0`, because the finite polynomial term vanishes
with rho. The complete integrand is integrable for n>=1 by the original form
(1). Its strict positivity on both open subintervals proves the result.

Proof of (6). Near t=1 the bracket is
`b_(m+1)(1-t^8)^(m+1)+O_m((1-t)^(m+2))`. Multiplying by rho gives leading
coefficient `b_(m+1)8^(m+1)/4` times `(1-t)^(m+1)`. The beta integral
`integral_0^1 t^(8n)(1-t)^(m+1)dt`
is asymptotic to `(m+1)!/(8n)^(m+2)`. A fixed interval away from t=1 contributes
exponentially little; after multiplication by t^(8n) the original density's
pole t^-8 is integrable and causes no endpoint difficulty. This gives exactly
`(m+1)!b_(m+1)/32`. The same endpoint expansion pays the next power in (6).

For m=1,2,3, (6) yields respectively
`421/512`, `13653/4096`, `537369/32768`, agreeing with #506. Equation (6),
not finite matching, proves the positive residual coefficient for every m.

## AD-3. The canonical infinite jet compensation diverges at each fixed source time

Define `sigma=1-tau^8` in (0,1), and `K=8(16-tau^8)>0`. For every fixed
R with sigma<R<1,

    b_k=K sigma^(-k-1)+O_R(R^-k).                       (7)

Moreover for each FIXED integer n>=1, with `a=n+1/8`,

    (1-E)^k Z_n= -Gamma(a)/64 * k^(-a)
                  +O_n(k^(-a-1/8)),                   (8)
    epsilon_m(n) ~ [K Gamma(a)/(64 sigma(1-sigma))]
                    sigma^(-m) m^(-a) -> +infinity.    (9)

Thus increasing m without a joint n,m estimate is not a valid way to turn
source-jet transport into exact compensation. For fixed m the residual tends
to zero with n; for every fixed n the canonical residual instead diverges with m.
This is a quantified failure of exchanging those two limits.

Proof of (7). Use the principal analytic eighth root on |s|<1. The only zero
of `1-2v-v^2` there is s=sigma: its corresponding t=2-sqrt2 lies in the image,
while the other root t=2+sqrt2 has magnitude exceeding every eighth root of
`1-s` in that disk. The zero is simple. If N(s) denotes the numerator of (3),
then `v'(sigma)=1/(8 tau^7)` and
`[1-2v-v^2]'(sigma)=-sqrt2/(4 tau^7)`. Direct substitution gives

    lim_(s->sigma) (sigma-s) A(1-s)=8(16-tau^8)=K.

Subtract K/(sigma-s). The difference is analytic throughout |s|<1; its
coefficients are O_R(R^-k) by Cauchy's coefficient bound. This proves (7)
and the precise radius sigma. No heuristic fit of coefficient growth is used.

Proof of (8). From (1), finite binomial expansion gives exactly

    I_k(n):=(1-E)^k Z_n
           =integral_0^1 t^(8n) rho(t)(1-t^8)^k dt
           =(1/8)integral_0^1 u^(a-1)rho(u^(1/8))(1-u)^k du.

At u=0, `rho(u^(1/8))=-1/8+O(u^(1/8))`, uniformly on [0,1] after enlarging
an absolute constant. Consequently

    I_k(n)= -B(a,k+1)/64 + O_n(B(a+1/8,k+1)).

The beta integral asymptotic follows, for example, by scaling u=y/k and
dominated convergence; the usual next-order estimate also follows by expanding
`(1-y/k)^k` on y<=sqrt k and bounding the remaining exponential tail. This
proves (8). In particular I_k(n)<0 eventually for each fixed n.

Combining (7) and (8) gives
`-b_k I_k(n) ~ K Gamma(a)/(64 sigma) sigma^(-k)k^(-a)`.
Its successive backward ratio tends to sigma<1. A geometric domination of
these backward ratios shows that the sum through m is asymptotic to its final
term divided by 1-sigma. The fixed term r_o(n) and finitely many early signs
are negligible. This proves (9). These Gamma/beta factors are analytic integral
constants, not probabilistic weights or new source-normality assumptions.

**A different infinite summation rule is outside this theorem.** Divergence
here refers to the canonical sequence of #506 jet polynomials. The separately
proved bounded/convergent infinite-stencil obstruction in the referee's report
has its own operator-domain hypotheses.

## AD-3b. A growing-order schedule DOES give exponentially accurate transport

The fixed-n divergence must not be promoted into an obstruction to every joint
limit. There is an absolute source-dependent constant C such that, for all
integers n,m>=1,

    0<epsilon_m(n)
      <= C sigma^(-m)[B(n+1/8,m+2)+256^(-n)].           (9a)

In particular choosing m=n proves the genuine growing-order estimate

    0<epsilon_n(n)<=C(4 sigma)^(-n),  4 sigma>1.         (9b)

Proof. Write `A(1-s)=K/(sigma-s)+R(s)` as above, and fix the Cauchy radius
`R0=511/512`. Since tau>1/2, `sigma<255/256<R0`. Split the Mellin integral at
t=1/2. On t>=1/2, `0<=s=1-t^8<=255/256`. Subtracting the degree-m Taylor
polynomial of the simple pole leaves exactly

    K sigma^(-m-1)s^(m+1)/(sigma-s).

Its product with rho is bounded in absolute value by `C sigma^(-m)s^(m+1)`:
`rho(t)/(sigma-s)=rho(t)/(t^8-tau^8)` extends continuously across t=tau.
Cauchy's bound on R at radius R0 bounds its Taylor remainder, uniformly for
s<=255/256, by `C R0^(-m)s^(m+1)`, which is no larger than the same expression
with sigma in place of R0. The bounded rho factor is harmless. Integrating this
upper bound over t>=1/2 costs at most

    (C/8) sigma^(-m) B(n+1/8,m+2).

On 0<t<1/2 use the original integrand instead of the pole decomposition.
Here `0<P_o(t)<=4`, rho is bounded, and (7) implies
`sum_(k<=m)b_k<=C sigma^(-m)`. The two terms are bounded by
`4 t^(8n-8)` and `C sigma^(-m)t^(8n)`. Their integrals are at most
`C sigma^(-m)256^(-n)` for every n>=1. This proves (9a), including the
interior zero without an illicit absolute singularity.

For m=n, the beta integral satisfies exactly

    B(n+1/8,n+2)
      =integral_0^1 [u(1-u)]^n u^(-7/8)(1-u)du
      <=4^(-n) B(1/8,2)=(64/9)4^(-n).

The 256^(-n) term is smaller. This proves (9b).

Define the time-dependent delayed frame `B_n(n)=P_n(E)Z_n`, using the genuine
radial states through time 2n. The exact recurrence yields

    e(HU_n)e(HB_n(n))=e(16H U_(n-1))e(H epsilon_n(n)).

For all integer H with |H|<=C0 A^2 log A, any unit-bounded complex amplitudes xi_n, and all sharp
subintervals I of [A,2A), therefore

    A^-1 |sum_I xi_n [e(HU_n)e(HB_n(n))-e(16H U_(n-1))]|
       <= C1 A^2 log A (4 sigma)^(-A).                  (9c)

This strengthens #506's fixed-order polynomial error to an exponentially small
source-derived transport defect on a concrete growing-order schedule. It still
does NOT bound either Weyl sum individually. The nonconstant multiplier remains
coupled to the original phase. The frame uses n future delays, and (4),(7) give
`sum_(ell<=m)|a_ell^(m)|=sum_(k<=m)b_k(2^k-1)=Theta((2/sigma)^m)`.
Neither bounded operator norm nor computationally cheap observation is asserted.
All these forcing/frame relations also hold after a homogeneous seed change.

## AD-4. A finite-shift pole invariant excludes exact radial substitution

The original and radial rational forcings are linearly independent over the
ring of finite Laurent shift polynomials C[E,E^-1]:

    P(E)r_o+Q(E)r_r=0 as rational functions => P=Q=0.    (10)

The same conclusion holds if the equality is asserted at every sufficiently
large integer n, since a nonzero rational function has only finitely many zeros.

Proof. The original r_o has pole locations, modulo integer shifts, only
`7/8,1/2,3/8,1/4`. The radial r_r additionally has a nonzero pole at `3/4`
(the j=2 lane). If Q is nonzero, choose its least shift with nonzero coefficient.
At the largest pole in the corresponding 3/4+Z orbit, only this single shifted
radial term contributes; no original-source term has that fractional pole
class. Its residue is nonzero, contradicting cancellation. Hence Q=0.
The same extreme-pole argument on any original lane then gives P=0.

Applying E-16 to an eventual finite constant-coefficient relation
`P(E)U+Q(E)Z=0` yields a relation (10), with a harmless common shift of the
forcing index. Therefore P=Q=0. The authentic angular companion cannot be
replaced by an exact finite shifted radial negative through such a relation.
There is also a direct rational cohomology obstruction. For any pole class
`a+Z`, define on rational functions the finite weighted-residue functional

    R_a(f)=sum_(k in Z) 16^(-k) Res_(x=a+k) f(x).

Translation gives `R_a(Ef)=16 R_a(f)`, so `R_a((E-16)f)=0`. Each occupied
pole class of r_o contains just one nonzero simple residue. Therefore
`(E-16)f=r_o` has NO rational-function solution f. The radial forcing has
nonzero residues in its own individual pole classes and has the same rational
cohomology obstruction, despite its analytic completed period being zero.
A logarithmic boundary-null identity in t is not a rational time-coboundary
identity in n. These are distinct cohomology problems.

This statement does not forbid approximate compensation, nonlinear operations,
or phase coherence modulo a time-dependent integer.

## AD-5. Exact seed visibility and the harmless 1/5 resonance

For the unchanged forcing and real initial seed s,
`U_n(s)-U_n(0)=16^n s`. For a finite integer-character stencil
`P(X)=sum_j c_j X^j`, using valid source times,

    e(sum_j c_j U_(n+j)(s))/e(sum_j c_j U_(n+j)(0))
      =e(16^n P(16)s).                                 (11)

For ANY finite collection of such tests, let G be the gcd of their integer
numbers `16^n P(16)`, taking the gcd of all zeros to be zero. The invisible
seed set is exactly

    {s: Gs is an integer}, if G>0; all real s, if G=0.   (12)

Necessity and sufficiency follow from Bezout's identity. This is a sharp
observability statement: the test family, not its number of repeated uses,
determines which boundaries are identified.

For lag stencils E^ell-1 with positive lags in a nonempty finite set L, every
starting time n>=N, and character one, the gcd is

    G=16^N (16^g-1), g=gcd(L).                          (13)

The identity `gcd(16^a-1,16^b-1)=16^gcd(a,b)-1` follows by the Euclidean
algorithm on the exponents; all later time factors are multiples of 16^N and
include n=N. Ward stencils with factor E-16 have P(16)=0 and erase EVERY
homogeneous seed. Clearing rational coefficients gives the analogous result
on any explicitly chosen common integer character basis.

For s=a/15, in particular s=1/5, `16^n s=s mod1` at every n. If the seed is
assigned to the angular component while radial Z is unchanged, then for every
integer H, every lag ell, every observer amplitude xi_n and every interval I,

    sum_I xi_n e(H(Y_n(s)+Z_(n+ell)))
      =e(Hs) sum_I xi_n e(H(Y_n(0)+Z_(n+ell))).           (14)

Thus EVERY maximal magnitude and pair collision statistic is unchanged.
At the prescribed critical depth, e(H_A(h)s)=e(|h|s). This seed is a useful
boundary-identifiability check, but is not a hostile counterexample to
cancellation: its entire absolute-cancellation behavior agrees with the
original. Any signed factorial effect from this seed factor must first pay
the known global phase e(Hs).

## AD-6. Literal carries restore boundary observability, with a sharp finite scale

Let x_n(s)={U_n(s)} and
`c_n(s)=floor(16x_(n-1)(s)+r_o(n))` be literal source carries. For s,s' in [0,1),

    16^-N(x_N(s)-x_N(s'))
      =(s-s')-sum_(j=1)^N16^-j(c_j(s)-c_j(s')).          (15)

This is exact telescoping of the two fractional recurrences. If the first N
carries agree, then `|s-s'|<16^-N`; if all carries agree, s=s'. For seeds on
an initial Q-grid, agreement through any N with 16^N>=Q forces equality.
The exponential finite scale is sharp over real seeds: for any interior initial seed whose finitely many states avoid circle endpoints,
an open interval of nearby seeds has the same finite carry word, by continuity
of finitely many affine branches. At the initial seed zero in [0,1), the
corresponding assertion is one-sided when its later states avoid endpoints.
The width is at most 16^-N, and it need not equal that upper bound.

For any two seeds, (15) also states exactly what the carries contribute beyond
phase/gap observables. This restores source authentication, but no estimate of
the distribution of the authentic carry words has been derived. Reconstructing
a unique sequence from complete data is not a bound on its signed sums.

## What failed, and what remains

The canonical all-order source-jet approach has a source-specific interior
singularity and a positive residual at every finite order; at fixed n infinite
compensation diverges. A controlled joint schedule m=n nevertheless gives
exponentially accurate signed phase transport by (9c). Exact finite shift substitution is excluded by a pole
class invariant. Those are structural results for the original/radial pair.
They do not deliver the requested critical maximal signed little-o.

The #505 one-prime mutant retains the tested nonternary principal parts and
almost all denominators, but changes injections and literal carries. Equations
(10) and (15) distinguish its generating process from the exact original source.
That discrimination alone supplies no quantitative real mixing estimate. All
original fixed-h Weyl, critical-ratchet, coarse-energy and pi-normality gates
remain OPEN; RH is a separate OPEN program.
