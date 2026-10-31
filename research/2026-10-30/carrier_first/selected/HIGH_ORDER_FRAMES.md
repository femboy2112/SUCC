# Bounded-radius rational prime frames for the selected BBP derivative

**PROVED LOCAL (paper): source-to-selected-state transport, not cancellation.**
Parent #417 is `1c6ce7d7ee83a0bd751bde8092e46ff798855fd3`. Read-only #421
`e14916aa2b4dfc2cce948facc729fb02ce1efafa` already constructs forward and
centered rational frames, with errors of orders `16^n/M` and `16^n/M²`.
That work expressly notes that higher order can change the spacing exponent.
The result below executes that extension: a growing-order instrument needs
only polynomially small frame spacing, has an exact sign and rational error
budget, and transfers finite bands through the sampling scale H~N.
It is not an asymptotic bound on either selected Weyl sum or energy.

The interpolation ingredients are classical. See NIST DLMF
[§3.3](https://dlmf.nist.gov/3.3), and Bengt Fornberg, *Generation of Finite
Difference Formulas on Arbitrarily Spaced Grids*, Math. Comp. 51 (1988),
699–706, [author-hosted paper](https://www.colorado.edu/amath/sites/default/files/attached-files/mathcomp_88_fd_formulas.pdf).
The specific source constants, moving-order construction and quantified
interfaces below are derived here; no scholarly-priority claim is made.

## ST1. The actual rational source and marked initial germ

Keep, without alteration,

    R(a)=4/a−2/(a+3)−1/(a+4)−1/(a+5),  a_k=8k−7,
    V(a)=a^4/[(a+3)^2(a+4)(a+5)],
    B_n(u)=product_(k=1)^n V(a_k+u)^(16^(n−k)),  B_0(u)=1.

For −1/2<=u<=1/2 all factors are positive. Set `f_n(u)=log B_n(u)`.
Its derivative at zero is the authentic rational lift `U_n`, with U0=0.
The logarithmic derivative R is completely monotone on a>0 because

    R(a)=integral_0^infinity e^(−at) Q(t) dt,
    Q(t)=2(1−e^(−3t))+(1−e^(−4t))+(1−e^(−5t))>0.

In particular, for every m>=1 and a>=1/2,

    0<R^(2m)(a)<4(2m)!/a^(2m+1)<=8·4^m(2m)!.

The strict upper bound follows directly from the three negative partial
fractions of the even derivative, while the positive integral proves the
lower sign. Hence

    0<f_n^(2m+1)(u)<8·4^m(2m)! (16^n−1)/15.             (1)

## ST2. Exact stencil and a signed Hermite remainder

For integer m>=1 let h_m=1/(2m), u_j=j h_m and

    w_(m,j)=2m (−1)^(j+1) (m!)²/[j(m−j)!(m+j)!], j=1,...,m.

Define a **full signed** observation

    A_(n,m)=sum_(j=1)^m w_(m,j)[f_n(u_j)−f_n(−u_j)].   (2)

The weights are the derivative at zero of the cardinal Lagrange basis
on −m h_m,...,m h_m. To check this without trusting a weight table,
differentiate
`L_j(x)=product_(ell!=j)(x−ell h_m)/(j h_m−ell h_m)` at zero.
For j>0 the zero factor is ell=0; cancellation gives the displayed w.
The weights at negative j are −w and the central weight is zero.
Thus (2) differentiates every polynomial of degree<=2m exactly.

Let P interpolate f at those nodes and put
`omega(x)=product_(j=−m)^m(x−j h_m)`.
The function `f−P−K omega`, with
`K=(f'(0)−P'(0))/omega'(0)`, has all 2m+1 distinct node zeros and a
double zero at zero. Repeated Rolle gives a point xi in (−1/2,1/2)
where its derivative of order 2m+1 is zero. Consequently

    f'(0)−P'(0)= [f^(2m+1)(xi)/(2m+1)!]
                 (−1)^m h_m^(2m)(m!)².                (3)

This proof does not differentiate an unspecified xi in an interpolation
error formula. Combining (1) and (3) proves, for every n,m>=1,

    0 < (−1)^m [U_n−A_(n,m)] < E_(n,m),
    E_(n,m)=8(16^n−1)/(15(2m+1)) · (m!/m^m)².          (4)

E is exactly rational. Even orders are lower observations of U_n; odd
orders are upper observations. The n=0 state is exactly zero.

## ST3. Genuine finite prime observations, with no missing factors

All sampled B_n(u_j) are positive rationals. Therefore (2) is exactly

    A_(n,m)=sum_p beta_(p,n,m) log p,
    beta_(p,n,m)=sum_j w_(m,j)
       [v_p(B_n(u_j))−v_p(B_n(−u_j))].                 (5)

Every sum is finite and every beta is rational. At one source time the
relevant ratio is

    V(a+j/(2m))/V(a−j/(2m))
      =product_(d,c) [(2m(a+d)+j)/(2m(a+d)−j)]^c.

Thus all exponents can be obtained by factoring integers no larger than
`2m(8n−2)+m`; there is no need to form the enormous powered rational B_n.
This is a real logarithmic observation of finite prime factorizations,
not a real derivative of a discrete p-adic valuation and not a claim of
independence among primes. Negative coefficients in (5) are indispensable.

For the original rational additive state, its separate decomposition is
`e(hU_n)=e(h c_p(U_n)) e(h[U_n−c_p(U_n)])` for each p. The second factor
is retained throughout the probe. Formula (5) neither replaces it by an
independent marginal nor identifies it with a Gauss sum.

## ST4. One explicit all-horizon moving order

For n>=1 choose

    m_n=4n+ceil(log2((n+1)²))+4,  A_n=A_(n,m_n).

At least floor(m/2) factors in `m!/m^m=product_(j=1)^m(j/m)` are <=1/2.
Therefore its square is <=`4^(−floor(m/2))<=2^(1−m)`. Substitution into
(4) gives

    |U_n−A_n| <= 1/[15(2m_n+1)(n+1)²]
                 <=1/(120 n³).                        (6)

Since m_n>=10, and `sum_(n>=1)1/(n+1)²<1`, a second useful bound is

    sum_(n>=1)|U_n−A_n| < 1/315.                       (7)

For every nonzero integer h and every N>=1,

    |sum_(n=1)^N e(hU_n)−sum_(n=1)^N e(hA_n)|
         <2pi |h|/315.                                (8)

Here all factors in the actual selected phase remain. This strengthens
the resolution tradeoff of the fixed-order instrument in #421, not the
magnitude estimate for either sum. A cancellation theorem for one side
would transfer to the other, but neither is established here.

## ST5. Moving-band Hilbert transport through H proportional to N

For integer H>=2, define
`Phi_H(x)=(sqrt(1−|h|/H) e(hx))_(|h|<H)`.
Its squared norm is H, and the Fejer kernel is nonnegative, so

    ||Phi_H(x)−Phi_H(z)|| <= min(sqrt(2H),D_H |x−z|),
    D_H=2pi sqrt(H(H²−1)/6).

The square root of the normalized Fejer energy is the norm of the
empirical mean of Phi. Reverse triangle, (6), and the integral comparison
for the decreasing function `min(a,b/x³)` give

    |sqrt(F_(H,N)(U))−sqrt(F_(H,N)(A))|
      <= N^(−1) sum_(n>=1) min(sqrt(2H),D_H/(120n³))
      <= C H^(1/2)(H²−1)^(1/6)/N
      < C H^(5/6)/N,       C³=9pi/(80 sqrt6).           (9)

Indeed `integral_0^infinity min(a,b/x³)dx=(3/2)a^(2/3)b^(1/3)`.
In particular the error is o(1) at H~N. The same feature-space instrument
is inherited from #415; this is its application to the faster-decaying
explicit prime-frame approximation, not a new selected energy estimate.
The logarithms in (5) are exact real numbers; the next section pays the
additional error of finite numerical observation.

## ST6. Observation accuracy and exact recovery on a rational grid

The stencil's total variation is

    Lambda_m=2 sum_j |w_(m,j)| <=4m H_m,

because `(m!)²/[(m−j)!(m+j)!]<=1`. Uniform error epsilon in each
f_n value therefore introduces at most `4m H_m epsilon` additional
state error. If instead every source-level logarithm is known to epsilon,
the powers introduce the further factor `(16^n−1)/15`. If individual
prime logarithms in (5) are measured, the exact error is bounded by
`epsilon sum_p |beta_p|`. None of these factors may be dropped.

Spacing is `1/(2m_n)=Theta(1/n)` and needs O(log n) bits, but the source
weights 16^(n−k) mean logarithmic value accuracy still generally requires
O(n) bits (plus guard bits), with a growing number of frames. This is no
exponential computational speedup or algorithm-independent lower bound.
Factoring cost is not claimed polynomial here.

There is also an exact finite-state reconstruction with an explicit
denominator passport. Let

    D_n=lcm {8k−7,8k−4,8k−3,8k−2:1<=k<=n}.

The recurrence proves `D_n U_n` is an integer. Choose
`m=4n+ceil(log2 D_n)+4`. The same factorial argument gives
`E_(n,m)<1/[15(2m+1)D_n]<1/(4D_n)`.
Measure A_(n,m) by rigorous log intervals of width <1/(2D_n).
Enlarge on the correct side by E from (4). The resulting interval has
width <1/D_n and contains U_n, hence it contains exactly one point of
`D_n^(-1) Z`, which is U_n. Existence follows from the established bound;
uniqueness follows from grid spacing. This observer uses finite positive
rational frames, finite prime factorizations, and convergent logarithm
enclosures; it does not query a pi-digit table or U_n during decoding.
The direct recurrence is ordinarily much cheaper. Also
`log2 D_n<=4n log2(8n)`, so this explicit spacing remains polynomial.

The code's integer logarithm enclosure range-reduces p to [1,2), then
uses y=(x−1)/(x+1)<=1/3 and

    log x=2 sum_(j=0)^(J−1) y^(2j+1)/(2j+1)+R,
    0<=R<=2y^(2J+1)/[(2J+1)(1−y²)].

Each scaled term is rounded down with an explicit 2J-unit budget for
rounding, and all signed rational linear combinations round outward.
The saved integer endpoints, not printed floating summaries, certify the
finite comparisons. Choosing J and the scale to grow eventually makes
every requested finite error budget attainable.

## ST7. Boundary, source and observational adversaries

The approximation is source- and preparation-faithful, but it is not a
zero-seed discriminator by itself. A linear logarithmic initial germ
`g_s(u)=exp(su)` contributes exactly `16^n s` to the stencil because it
differentiates linear polynomials exactly. The same error (4) then holds
for the coherent real seed s=−pi/16; its orbit is nonnormal. Its frame
values need not be rational, so it belongs to the real analytic carrier,
not the rational prime-value subcarrier.

For rational linear germs `g(u)=1+su`, frame values are rational whenever
defined, but the derivative error has the additional high-derivative
term of `16^n log g`; the authentic constant cannot be reused silently.
Rational seed translations are not required to fail normality.

For any one finite grid, the polynomial

    g(u)=1+s u product_(j=1)^m [1−(2mu/j)²]

has g(0)=g(u_j)=g(−u_j)=1 and g'(0)=s. For sufficiently small nonzero
rational s it is positive throughout the grid interval. Thus all its
sampled prime values agree with the zero germ while the actual first jet
changes by 16^n s. This is #421's finite-frame alias in the present grid.
It does not contradict (4): its initial germ is not B0 identically1.
If a single analytic germ agrees on the growing grids for every n,
the nodes 1/(2m_n) accumulate at zero, so analytic uniqueness forces it
to equal1 near zero. This repairs identifiability in the analytic-germ
class, without producing a signed time estimate or a uniform finite
identification theorem on unrestricted germs.

Positive rank-two mutants admit analogous derivative bounds with their
own coefficients; the seven-pole null source, coherent seed and periodic
controls remain coherent despite admitting finite carrier realizations.
The source-independent positive Gamma/Oily/Fibonacci geometry does not
distinguish those paths. No new arithmetic role for Omega_OM is claimed.

## ST8. Fibonacci tilings and the still dark signed inequality

PR413 already proves the appropriate Zeckendorf coverage statement: a
uniform o(F_k) block bound for starts A<=C F_k, for each fixed C, implies
all-horizon cancellation. It also proves the factor239 obstruction and
the authentic forcing defect `239 U_n+15r(n+1)+r(n+2)`. Those are reused
as controls rather than advertised as new results.

A new exact control here shows why checking only **prefix** sums at
Fibonacci horizons is not enough among unit complex sequences. Set the
first five values to (1,−1,1,omega,omega²), where omega³=1, omega!=1.
For every gap [F_k+1,F_(k+1)], k>=5, of length L=F_(k−1), use L/2 copies
of1 followed by L/2 copies of−1 when L is even; when L is odd, use
(L−3)/2 copies of1, then the same number of−1, then (1,omega,omega²).
Every entire gap sums to zero, so S_(F_k)=0 for all k>=5. At the end
of its initial +1 run the normalized magnitude tends to

    1/(2phi+1)>0.

This is a unit-sequence coverage counterexample, **not** a claimed radix16
orbit or a counterexample to original BBP. Its exact coefficients are
checked in Q[omega]/(omega²+omega+1). Genuine source-dependent block
estimates remain necessary. Factoring a finite block into prime frames
or Fibonacci pieces leaves uncontrolled correlations between the pieces.

No proof was found of a fixed-h bound
`|sum_(n=A)^(2A−1)e(hU_n)|<=(1−eta)A` for every sufficiently large A,
let alone o(A). This is the smallest declared signed milestone. The
new transport permits replacing its phases by the explicit full signed
prime-log observations (5) with a paid error; bounding that resulting
sum is the remaining mathematical obligation. Finite tests are not
promoted into a uniform estimate.
