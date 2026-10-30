# Positive internal arrows with the identical selected pi period

**PROVED LOCAL.** These are changed-source controls, never replacements for the
authentic BBP source. They have zero initial condition and the SAME selected pi
period. Their normality is therefore exactly as open as pi's. This complements
the nonnormal zero-boundary controls in `../signed/`.

Write z=exp(-x), Q(z)=4-2z^3-z^4-z^5 and

    r(n)=integral_0^1 z^(8n-8) Q(z) dz,
    L(Q)=integral_0^1 Q(z)/(16-z^8) dz = pi/16.

The original four coefficients and zero boundary are fixed throughout the
authentic calculations. The enlarged polynomial class is explicitly a control
class. The variable z here is the Laplace-coordinate variable, not the shift
operator spectral variable used by the signed front.

## PF-01: exact period-preserving derivative arrows

For a real polynomial R with R(0)=R(1)=0, set

    D_R(z)=(16-z^8)R'(z),  Q_epsilon=Q+epsilon D_R.

Then L(Q_epsilon)=L(Q). If U^epsilon and U have the same zero boundary,

    U_n^epsilon-U_n = epsilon 8n integral_0^1 z^(8n-1)R(z) dz  (n>=1).

**Proof.** The period difference is epsilon times the integral of R', hence
zero. Define I_n=integral z^(8n)R'. Then I_0=0 and the forcing difference is
epsilon(16 I_(n-1)-I_n). Its unrolled recurrence telescopes to -epsilon I_n.
Integration by parts proves the formula. All finite values are rational when
epsilon and R have rational coefficients. No numerical pi input is needed.

Within the restricted denominator-canceling class D=(16-z^8)P, this describes
ALL zero-period perturbations: integral P=0 iff its polynomial primitive with
R(0)=0 also has R(1)=0. This is not a classification of every polynomial BBP
null relation; other proper rational integrals are outside the statement.

The maps add under R addition, and the displayed rational coordinate changes
intertwine the time-dependent affine recurrences. Composition is explicit;
these are a genuine family of internal transport changes invisible to L.

## PF-02: arbitrary finite jets AND an exact initial forcing prefix

For every integer m>=2 and N>=0, let p_N be the monic orthogonal polynomial
of degree N in u=z^8 for the strictly positive measure

    z^8(1-z)^(m+1) dz,  0<z<1.

Its moments are B(8j+9,m+2), so its coefficients are rational. The Gram matrix
is positive definite: integral |P(z^8)|^2 z^8(1-z)^(m+1) dz>0 for every nonzero
polynomial P. Thus the finite linear system has exactly one solution. Put

    R(z)=z(1-z)^(m+1)p_N(z^8).

Then the following hold simultaneously:

1. The selected period is exactly pi/16.
2. The first N original forcing values AND first N zero-seed orbit values
   agree exactly.
3. Q_epsilon-Q vanishes to order at least m at z=1 (equivalently x=0),
   matching the source Taylor coefficients through degree m-1.
4. For an explicit nonzero rational epsilon, Q_epsilon is strictly positive
   on [0,1), and is distinct from Q.
5. Its first orbit difference at n=N+1 is strictly positive for epsilon>0.

**Proof of 2 and 5.** The orbit difference divided by epsilon 8n is

    integral z^(8n)(1-z)^(m+1)p_N(z^8) dz.

For 1<=n<=N this is the inner product of p_N(u) with u^(n-1), hence zero.
At n=N+1, replace u^N by p_N plus a lower-degree polynomial: the integral is
the strictly positive squared norm of p_N. The recurrence transfers equality
of successive orbit values to equality of forcing values. In particular the
construction is not an accidentally unchanged source.

**Positivity proof.** Write R'=(1-z)^m H(z) and B=sum |coefficients(H)|>0.
The factorization Q=(1-z)(4+4z+4z^2+2z^3+z^4) gives, on [0,1),

    |D_R/Q| <= 4 B (1-z)^(m-1) <= 4B.

Choose epsilon=1/(8B), or any nonzero |epsilon|<=1/(8B). Then
Q_epsilon>=Q/2>0. Source positivity and finite-jet matching are proved for
the whole interval, not inferred from a grid. A sufficiently small rational
epsilon also permits an arbitrarily small uniform relative perturbation.

For N=0 this reduces to R=z(1-z)^(m+1) and

    U_n^epsilon-U_n=epsilon 8n B(8n+1,m+2).

## PF-03: selected signed sums stay within a bounded error

Let C_p=sum |coefficients(p_N)|. Since |p_N(z^8)|<=C_p,

    |U_n^epsilon-U_n|
      <= |epsilon| C_p (m+1)!/(8n)^(m+1).

Consequently for every integer h and every horizon H,

    |sum_(n=1)^H [e(hU_n^epsilon)-e(hU_n)]|
      <= 2pi |h epsilon| C_p (m+1)! 8^(-m-1) (1+1/m).

The bound follows from |e(x)-e(y)|<=2pi|x-y| and
sum n^(-m-1)<=1+1/m. Thus any fixed-frequency normalized Weyl limit is the
same. The controls do not need to fail a normality theorem: they encode the
same pi boundary, and a theorem that rightly extends to them would be useful.

## What this says about the triangle

Rank two, its harmonic/golden/Euler limit, and every prescribed finite depth
of source asymptotic jets can coexist with distinct positive internal source
arrows, even after the exact selected period and a finite arithmetic prefix
are supplied. For normalized rank-two scaling, a perturbation O(x^m) affects
the scaled density at O(a^(-(m-1))); standard dominated Laplace expansion
therefore preserves the earlier coefficients, rather than all finite-a
observables. Exact all-time source observations WOULD distinguish these
kernels. No claim of indistinguishability under every realization is made.

The original four-pole passport excludes these extra-pole controls. A fixed
four-pole rational source is already identifiable by enough exact rational
samples; source identification is separate from proving its selected signed
dispersion. The theorem does not weaken that passport or change it.

## Evidence, dependencies and falsifiers

`period_fiber.py` constructs exact rational witnesses without symbolic algebra;
`independent_oracle.py` uses symbolic integration, matrix inversion and direct
unrolled sums without importing the producer. Seven unit tests, twelve declared
cases and three fresh (m,N) holdouts are executed; raw receipts are in `../receipts/`.
Dropping R(1)=0 is a decisive negative control: R=z yields period shift epsilon.
The separate computational routes share the same model author and are not
independent mathematical referees.

Classical ingredients: Euler's Beta integral, verified from
https://dlmf.nist.gov/5.12.E1; positive moment Gram matrices and orthogonal
polynomials, https://dlmf.nist.gov/18.2. The telescoping mechanism is related to
the older repository rational-coboundary construction in
`observational_succ/duck_bbp_fourier.py`; that older construction did not assert
the present combination of identical pi period, arbitrary exact prefix,
finite-jet agreement and explicit positivity. The orthogonal-polynomial
finite-prefix/finite-jet positive counterfeit mechanism is already present in
`research/2026-10-25/GAMMA_ZERO_ONE_BBP_MOMENT_GEOMETRY.md`, section V. That
construction changes the selected resolvent with a strict sign; the present
extension uses derivative arrows to preserve it exactly. No scholarly
priority is claimed.
