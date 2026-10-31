# Positive source resolvents, prime germs and certified analytic completion

**PROVED LOCAL paper deductions from classical Gaussian quadrature, moment
theory, Poisson summation and the zeta functional equation.** No scholarly
priority, Lean authority, selected signed saving, pi-normality or RH theorem
is claimed. Parent #417 and siblings #420--#423 are read-only inputs. The
new results here are quantitative original-source specializations and exact
information-loss controls, not new versions of their existing identities.

## A01. The authentic source has a finite-moment resolvent certificate

Retain `c=(4,-2,-1,-1)`, `delta=(1,4,5,6)`, and
`r(n)=sum c_delta/(8n-8+delta)`. The change of variable `x=exp(-8t)` in
the original positive Laplace formula gives the positive measure on (0,1)

    dmu(x) = (1/8) x^(-7/8)
             (4-2 x^(3/8)-x^(1/2)-x^(5/8)) dx,
    mu_k = integral x^k dmu = r(k+1),   mu_0=47/15.

Its density is strictly positive throughout (0,1), integrable at zero,
and has finite total mass. Thus every finite Hankel moment matrix is
positive definite: its quadratic form is the integral of a nonzero
polynomial squared. This source Hausdorff representation is inherited
in substance from earlier SUCC source work; it is not newly discovered.

The original zero-seed boundary is

    alpha = sum_(n>=1) 16^(-n) r(n)
          = integral dmu(x)/(16-x) = pi/16.

The last equality uses the original BBP formula. Tonelli justifies the
sum/integral interchange. All following certificates can be generated
without supplying pi or any of its digits.

Fix d>=1. Let p_d be the monic degree-d orthogonal polynomial for mu.
It exists uniquely and has rational coefficients because its defining
linear system uses the positive definite rational moment matrix. Its d
zeros are simple in (0,1): if it had fewer than d sign-changing roots
there, multiplication by the polynomial formed from those roots would
give a nonzero constant-sign integrand contradicting orthogonality.

Define the rational numbers

    q_d(t) = integral [p_d(t)-p_d(x)]/(t-x) dmu(x),
    R_d(t) = q_d(t)/p_d(t),
    h_d = integral p_d(x)^2 dmu(x).

The center R_d(16) uses exactly mu_0,...,mu_(2d-1), hence r(1),...,r(2d).
The sharper error certificate h_d uses one further moment r(2d+1).

**Exact Markov error identity, for every real t>1:**

    integral dmu(x)/(t-x) - R_d(t)
       = integral p_d(x)^2/(t-x) dmu(x) / p_d(t)^2.                 (A1)

To prove it, subtraction of q_d/p_d first gives the numerator
`integral p_d(x)/(t-x)`. Orthogonality applied to the degree-(d-1)
polynomial `[p_d(t)-p_d(x)]/(t-x)` then replaces that numerator by
`integral p_d(x)^2/(t-x)/p_d(t)`. No numerical root calculation is used.
At t=16 this yields the fully rational strict enclosure

    R_d(16)+h_d/[16 p_d(16)^2] < pi/16
             < R_d(16)+h_d/[15 p_d(16)^2].                       (A2)

The strictness follows from positive density on the open interval, since
1/16 < 1/(16-x) < 1/15 there. It is not a floating-point assertion.

The rationality of the center and bounds is important: irrational
quadrature nodes do not need to be approximated to obtain the certificate.

## A02. Uniform rate and transport to the selected phase

Among monic degree-d polynomials p_d minimizes the squared mu norm: subtract
p_d and use orthogonality. The monic shifted Chebyshev polynomial
`2^(1-2d) T_d(2x-1)` has supremum norm `2^(1-2d)` on [0,1]. Hence

    h_d <= (47/15) 2^(2-4d),
    p_d(16) = product_(j=1)^d (16-x_j) > 15^d.

Substitution in (A1) proves the all-d original-source estimate

    0 < alpha-R_d(16) < 188/(225 * 3600^d).                     (A3)

This has a strictly better asymptotic exponential rate than raw geometric
truncation with the same 2d source values, whose elementary budget is
`16^(-2d) r(2d+1)/15`. The coarse uniform bound (A3) is worse at d=1,2;
the exact data-dependent interval (A2) is sharper in all tested cases.
It is not a source-selected cancellation
theorem. Gaussian/Padé theory is classical; the exact four-pole moment
inputs, rational certificate and explicit bound are this specialization.
The sharper (A2) has been tested against an entirely separate rational
BBP enclosure at d=1..8 and fresh d=11,14,19.

For the authentic zero-seed recurrence, completed phase is `16^n alpha`,
and the rational phase is `U_n=16^n alpha-T_n`. Therefore (A3) implies

    |e(h*16^n alpha)-e(h*16^n R_d(16))|
       <= min(2, (376*pi*|h|/225) 16^n 3600^(-d)).               (A4)

With the same exact T_n subtracted the identical inequality applies to
U_n. It is valid for any integer h and every n>=0, d>=1. If

    d(n) >= ceil((n log16 + a log(n+1))/log3600),

then the right side is at most `376*pi*|h|/[225(n+1)^a]`.
Here `log16/log3600` is approximately 0.3386. For a moving frequency
bound |h|<=H_n, add log H_n to the numerator. This is explicit precision
transport, not a complexity bound: rational heights and exact linear
algebra cost grow with d and are recorded in the probe. No statement
that a finite precision interval avoids every cylinder seam is made.
For any given seam, the exact rational enclosure decides only when the
two endpoint floors agree; otherwise the outcome is ambiguous.

## A03. The same approximants forge sharp positive finite-memory controls

The Gaussian measure `mu_d=sum_j w_j delta_(x_j)` has positive weights
and matches mu through moment 2d-1. This follows by interpolating at the
roots and dividing any degree<=2d-1 polynomial by p_d. Positivity follows
from `w_j=integral l_j(x)^2 dmu>0`, where l_j is its Lagrange polynomial;
the equality with `integral l_j` uses polynomial division and orthogonality.
Its Cauchy transform is precisely R_d(t), by (A1)'s first polynomial
division applied to the discrete measure.

Define a **changed source**, with exact zero boundary,

    r_d(n)=integral x^(n-1) dmu_d(x),
    U_(d,0)=0,   U_(d,n)=16 U_(d,n-1)+r_d(n).

All r_d(n) are rational. Indeed p_d has rational coefficients and its
annihilating recurrence continues the first d rational moments to every
later moment. The sequence is strictly positive, decreasing, and completely
monotone as a discrete moment sequence. It agrees exactly with the authentic
source for n<=2d; hence its selected rational path and literal carry record
agree through that time. It differs at n=2d+1 because h_d>0.

Nevertheless its completed boundary is the rational number R_d(16).
For h equal to its positive denominator in lowest terms and

    T_(d,n)=integral x^n/(16-x) dmu_d(x),
    B_d=sum_(n>=1) T_(d,n)=[R_d(1)-16 R_d(16)]/15,

one has the exact all-horizon signed countercontrol

    |sum_(n=1)^N e(h U_(d,n))-N| <= 2*pi*h*B_d.                 (A5)

Here B_d is finite, positive and rational, since every x_j<1. The proof
is `U_(d,n)=16^n R_d(16)-T_(d,n)` and `|e(v)-1|<=2*pi*|v|`.
The fixed frequency h depends on d and must not be suppressed. These
are nonnormal positive-Hausdorff, finite-memory, zero-seed controls with
an exact original prefix. They are not the original four-pole source.

At least d atoms are necessary to match these moments: the authentic
d-by-d Hankel matrix is positive definite, whereas an s-atom measure
has Hankel rank at most s. Thus the Gaussian d-atom control has minimal
atomic rank for this prefix. Unlike PR415's different order-two cubature,
the atoms/weights need not be rational individually; the entire moment
sequence and completed boundary are rational. No all-asymptotic matching
is claimed; PR421's different shadow provides that obstruction.

The coherent same-forcing seed `-pi/16` leaves every source certificate
(A1)--(A3) unchanged and shifts the completed boundary to zero. Thus neither
positive source rank nor the accelerated approximation proves dispersion.

## A04. A uniform finite-lattice certificate for completed zeta germs

For t>0 the integer-lattice Gaussian theta obeys
`Theta(t)=t^(-1/2)Theta(1/t)` by Poisson summation. The Gaussian and its
Fourier transform are Schwartz functions, so Poisson applies. For Re(s)>1,
absolute convergence at infinity is exponential; at zero duality gives
the leading integrand `t^((Re(s)-3)/2)`, so precisely Re(s)>1 is required
for the untreated Mellin integral. Termwise integration gives twice
`Lambda(s)=pi^(-s/2)Gamma(s/2)zeta(s)`.

Split at t=1 and substitute t -> 1/t below 1. One obtains

    Lambda(s)=1/[s(s-1)]
      +sum_(n>=1) integral_1^infinity exp(-pi*n^2*t)
            [t^(s/2-1)+t^(-(s+1)/2)] dt.                        (A6)

The integral series is entire by compact domination, while the displayed
rational term has exactly the poles at 0,1. Its invariance under s->1-s
proves the functional equation. This is classical, independently audited
here with correct factors of two; it supplies no new zero-line positivity.

Let Lambda_M retain n=1,...,M, and let a<=Re(s)<=b. Choose an integer
K>=max(0,b/2-1,-(a+1)/2). For any derivative order ell>=0, write
`C=3(M+1)^2`. Then the following explicit **rational** bound holds on the
whole strip, with arbitrary imaginary part:

    |(Lambda-Lambda_M)^(ell)(s)|
       <= 2^(2-ell-C) sum_(j=0)^(K+ell)
                  (K+ell)!/[(K+ell-j)! C^(j+1)].                (A7)

Indeed the omitted Gaussian series is bounded by
`exp(-pi(M+1)^2 t)/(1-exp(-pi(2M+3)t))`. On t>=1 its denominator is >1/2.
The two ell-th differentiated powers contribute at most
`2^(1-ell) t^K(log t)^ell <= 2^(1-ell)t^(K+ell)`.
Replace pi by 3 and use repeated integration by parts. Finally
`exp(-C)<2^(-C)` gives (A7). Pole terms cancel in the difference, so the
bound remains valid across 0 and1 for the analytic remainder. This is
truncation error only; numerical rounding requires its own enclosure.

## A05. What the complete prime-weighted germ does and does not identify

Near z=0, all factors in the following normalized ratio are nonzero.
Choose the analytic logarithms that vanish at zero. The true functional
equation, divided by its value at -1, gives

    zeta(-1+z)/zeta(-1)
       =(2*pi)^z cos(pi*z/2) Gamma(2-z) zeta(2-z)/zeta(2).

After subtracting the three displayed Archimedean logarithms, the
corrected analytic germ is `G(z)=log[zeta(2-z)/zeta(2)]`. For k>=1,

    G^(k)(0)=sum_(n>=2) Lambda(n)(log n)^(k-1)/n^2.              (A8)

The first correction is `log(2*pi)+gamma-1`, recovering #417's scalar
identity. The whole family is stronger data: these are all moments of
the positive measure

    nu=sum_(n>=2) Lambda(n)n^(-2) delta_(log n) on [0,infinity).

It has finite exponential moments for every real t<1. Among positive
measures on [0,infinity), its full moment sequence determines it uniquely:
if another measure shares the moments, Tonelli applied to exp(t x),
0<t<1, proves the same finite exponential moments; analytic Laplace
transforms then agree near zero and throughout their common connected
half-plane, and uniqueness of the Fourier transform after exponential
damping identifies the measure. Thus the **entire corrected germ**, with
the stipulated analytic and positivity class, identifies the full
prime-power support and weights. A scalar special value does not.

There is a particularly arithmetic finite-jet countercontrol. Fix K>=1,
put `epsilon=1/(2*4^(K+1)*2^K)`, and change only the nu masses at
`x_j=(j+1)log2`, j=0,...,K, by

    delta nu_j=epsilon*log2*(-1)^j binom(K,j).                   (A9)

Every new mass stays positive: its change is at most half the smallest
original mass `log2/4^(K+1)`. Pascal differences annihilate polynomials
of degree<K, so moments 0,...,K-1 agree exactly. Moment K changes by
`epsilon*(-1)^K K!*(log2)^(K+1)`, which is nonzero. Consequently the first
K corrected germ derivatives agree and the next does not. The underlying
support is still the actual prime-power support; the weights have changed.
These are positive weighted-Dirichlet fakes, **not** the von Mangoldt law,
not Euler products with the original integer exponents, and not alternate
values of zeta. In fact the divisor identity `log n=sum_(d|n)Lambda(d)`
already fails at n=2, since its sole nonzero divisor weight was changed.
Thus this is not a counterexample inside the exact multiplicative arithmetic
law. It identifies precisely the source condition that the finite jets lose.

For k>=1 and integer X>=max(3,2^k), the finite prime-power cutoff in (A8)
has positive omitted tail bounded by

    (1/X) sum_(j=0)^k k!/(k-j)! * (log X)^(k-j).                 (A10)

Use Lambda(n)<=log n, monotonicity of (log x)^k/x^2 beyond X, and the
integral test followed by integration by parts. Hence the full germ is
an operational family of separately error-controlled finite prime probes.
Neither (A8) nor (A10) supplies a selected BBP character inequality.

## Provenance and remaining signed obligation

Classical ingredients were checked against primary reference pages:
[DLMF Gauss quadrature](https://dlmf.nist.gov/3.5#v),
[orthogonal polynomials and continued fractions](https://dlmf.nist.gov/18.2#x),
[zeta reflection](https://dlmf.nist.gov/25.4), and
[Mellin integral domains](https://dlmf.nist.gov/25.5).
The derivations above are supplied in full; those pages are not asserted
to contain the source-specific constants, probes or countercontrols.

#417 supplies the scalar/all-negative-integer first tangents; #421 supplies
spectral residues, source translation and all-order shadows; #423 supplies
the general full-germ identity-theorem boundary. None is silently merged.
The Harmonic/Golden/Euler--Mascheroni/Fibonacci roles and Oily--Macaroni
authorship remain as in main's operational triangle. Gamma and gamma are
load-bearing in the reflected normalization; no golden or Fibonacci
parameter was derived from the prime germ or the Padé approximants.

The source-specific improvement is (A2)--(A4), a certified finite-to-global
analytic transfer. The smallest remaining signed task is still to control
the selected characters after this reconstruction. The Gaussian positive
countermodels show why accurate finite transport cannot substitute for an
all-horizon source-and-boundary-sensitive inequality.
