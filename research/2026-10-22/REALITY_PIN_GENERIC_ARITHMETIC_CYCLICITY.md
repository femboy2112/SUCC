# Generic scalar visibility of the arithmetic boundary carrier

**Date:** 2026-10-22. **Theorem:** GAC-1; ledger RP-25.
**Status:** complete paper derivation using the classical global Rellich theorem.
This is not a Lean kernel result, a finite computational certificate, a physical
measurement, or a claim of independent academic novelty.

This strengthens [the operator manuscript](REALITY_PIN_ARITHMETIC_OPERATOR.md).
The full-family assertion and cyclicity at a named parameter remain unresolved.

## Exact statement and source domain

Fix real lambda != 0 and delta > 0. On H = ell²(N_{>=1}), use the actual sources

    D e_n = (log n)e_n,    S e_n = e_(n+1),    V_p e_n = e_(pn),

where p ranges over genuine rational primes. For every real sigma > 1, define

    K_sigma = D + lambda(S+S*) + sum_p p^(-sigma)(V_p+V_p*) + c(sigma)I,
    c(sigma) = 2|lambda| + 2/(sigma-1) + delta.

All operators have the common dense domain

    Dom(D) = {x in H : sum_n (log n)^2 |x_n|^2 < infinity}.

**GAC-1.** There is an at-most-countable set E_(lambda,delta) in (1,infinity)
such that, for every sigma outside E_(lambda,delta), K_sigma has simple spectrum
and e_1 is spectrally cyclic: the closed span of f(K_sigma)e_1 for bounded Borel
functions f is H.

No particular sigma, including 2, is certified by this argument. The combined
exceptional set is not asserted discrete or empty. Polynomial Krylov density,
effective visibility bounds, physical source authentication, and lambda=0 are
separate questions.

## Classical input checked against primary sources

Kriegl and Michor, *Differentiable perturbation of unbounded operators*,
Math. Ann. 327 (2003), 191–201,
[arXiv:math/0204060v4](https://arxiv.org/pdf/math/0204060), page 1, Theorem (A),
provides global analytic eigenvalue/eigenvector parameterizations for a
real-analytic self-adjoint curve with common dense domain and compact resolvent.
Page 2 specifies weak analyticity and enumeration with correct multiplicities.
The analytic case is attributed there to Rellich; it assumes no simplicity.

Kato, *Perturbation Theory for Linear Operators*, second edition,
[Chapter VII, Theorem 3.9, printed pp. 392–393](https://webhomes.maths.ed.ac.uk/~v1ranick/papers/kato1.pdf),
gives the corresponding analytic orthonormal eigenvector family for self-adjoint
holomorphic type-(A) families on real intervals. The argument below verifies the
hypotheses and supplies the further no-escape and visibility steps explicitly.

## Proof

### 1. Analytic family, common domain and compact resolvent

For complex z with Re(z)>1 put

    B(z) = lambda(S+S*) + sum_p exp(-z log p)(V_p+V_p*)
           + (2|lambda| + 2/(z-1) + delta)I.

Every V_p has norm one. On a compact subset of this half-plane choose a>1 with
Re(z)>=a. The operator series is uniformly dominated by 2 sum_p p^(-a).
Every derivative of fixed order k is dominated by
2 sum_p (log p)^k p^(-a), which converges by comparison with the integer series.
Thus B is holomorphic in bounded-operator norm. D+B(z) is closed on Dom(D) and
is a holomorphic family of type (A).

For real sigma, B(sigma) is self-adjoint. ARITH-1 proves self-adjointness on the
common domain, K_sigma >= delta I, and compact resolvent. Compactness also
follows from the resolvent identity and the compact diagonal resolvent of D.

Apply the global Rellich theorem after reparameterizing sigma=1+exp(t), t in R,
then compose its functions with t=log(sigma-1). This exactly matches the global
domain in Kriegl–Michor. Obtain countably many real-analytic eigenvalues
E_j(sigma) and normalized norm-real-analytic vectors u_j(sigma), j>=1, satisfying

    K_sigma u_j(sigma) = E_j(sigma)u_j(sigma).

At each parameter the vectors form a complete orthonormal basis and eigenvalues
are enumerated with their multiplicities. These are analytic branch labels;
they need not agree with increasing eigenvalue order at crossings.

### 2. The limiting Jacobi operator is simple and boundary-visible

Set

    J = D + lambda(S+S*) + (2|lambda|+delta)I.

It is self-adjoint on Dom(D) with compact resolvent. Its eigenvector recurrence is

    lambda u_(n-1) + (log n + 2|lambda| + delta - E)u_n
       + lambda u_(n+1) = 0,    u_0 = 0.

Since lambda != 0, u_1=0 forces u_2=0 and inductively every coordinate to vanish.
Moreover u_1 determines every subsequent coordinate. Consequently each
eigenspace is one-dimensional and every eigenvector has nonzero first
coordinate. The spectral projections of this compact-resolvent self-adjoint
operator span H, so e_1 is spectrally cyclic for J.

The difference on the common domain extends to a bounded operator, with

    eta(sigma) := ||K_sigma-J||
               <= 2 sum_p p^(-sigma) + 2/(sigma-1) -> 0.

This is a norm of the bounded difference, not of either unbounded operator.
The prime sum tends to zero by dominated convergence with any fixed sigma_0>1.

### 3. Integrable derivative rules out escape of an analytic eigenbranch

In bounded-operator norm,

    K'_sigma = -sum_p (log p)p^(-sigma)(V_p+V_p*)
               - 2/(sigma-1)^2 I.

For every a>1, Tonelli applied to the nonnegative bounds gives

    integral_a^infinity ||K'_sigma|| d sigma
       <= 2 sum_p p^(-a) + 2/(a-1) < infinity.

Along each normalized analytic eigenbranch, Hellmann–Feynman yields

    E'_j(sigma) = <u_j(sigma), K'_sigma u_j(sigma)>,
    |E'_j(sigma)| <= ||K'_sigma||.

This also holds at crossings for the chosen analytic branch. Domain
differentiation is legitimate: D u_j=(E_j-B(sigma))u_j is analytic in H, so u_j
is analytic in the graph norm of D. The integrable derivative bound makes each
E_j have finite total variation on [a,infinity), hence a finite real limit L_j.

This step is essential. Pointwise convergence of ordered eigenvalues alone
would not exclude a global analytic branch moving through high-energy labels.

For its normalized eigenvector,

    ||(J-E_j(sigma))u_j(sigma)|| <= eta(sigma).

The spectral theorem therefore implies
dist(E_j(sigma),spec(J)) <= eta(sigma). Closedness of the spectrum gives
L_j in spec(J); it is an isolated simple eigenvalue.

### 4. Rank-one spectral windows give distinct limits and nonzero weights

Fix j and a small circle around L_j enclosing no other spectrum of J. Its Riesz
projection Q has rank one. On this contour, the resolvent identity and
||K_sigma-J|| -> 0 give uniform norm convergence of the resolvents and hence
norm convergence Q_sigma -> Q of the corresponding spectral projections.
Their ranks agree eventually: orthogonal projections at distance less than
one have the same finite rank.

Since E_j(sigma)->L_j, u_j(sigma) eventually belongs to ran(Q_sigma). Two
different branches cannot have the same limit, since then two orthonormal
vectors would eventually belong to one rank-one spectral window. Thus

    L_j != L_k for j != k.

For all sufficiently large sigma, Q_sigma projects precisely onto u_j(sigma).
Consequently

    |<e_1,u_j(sigma)>|^2 = <e_1,Q_sigma e_1>
                       -> <e_1,Q e_1> > 0.

The last inequality is the Jacobi recurrence result. Eigenvector phases need
not converge. Each branch has its own eventual window; no common finite sigma
is asserted to make all infinitely many branches simultaneously visible.

### 5. Analytic failure conditions have a countable union of zeros

For j != k, E_j-E_k is real analytic and not identically zero, because its limit
is L_j-L_k != 0. Its zeros in (1,infinity) are discrete and countable.

For each j, a_j(sigma)=<e_1,u_j(sigma)> is real analytic and not identically zero,
since its squared modulus has positive limit. Its real zeros are also discrete
and countable (for a complex-valued analytic function, use a nonidentically-zero
real or imaginary component). Define

    E_(lambda,delta)
      = union_(j<k) {sigma : E_j(sigma)=E_k(sigma)}
        union union_j {sigma : a_j(sigma)=0}.

This set is at most countable. Outside it, all eigenvalues are simple and each
rank-one spectral projection sends e_1 to a nonzero multiple of its eigenvector.
Those eigenvectors span H. This is precisely spectral cyclicity. QED.

The countable union need not be locally finite. Its complement is dense,
residual and of full Lebesgue measure, but these properties certify neither
a specified sigma nor an effective stopping rule.

## What the complete scalar response determines

For a good parameter, the complete exact function

    m_sigma(s) = <e_1,(K_sigma+sI)^(-1)e_1>,    s>0,

determines the cyclic pair (K_sigma,e_1) up to a unitary preserving the boundary
vector, by uniqueness of its scalar spectral measure and the cyclic spectral
theorem.

Measure uniqueness can be seen directly. Fix s_0>0. Derivatives of m determine
every integral (x+s_0)^(-k) d mu(x), k>=1. The zeroth moment is the known
normalization ||e_1||²=1. Under t=(x+s_0)^(-1), these are all polynomial moments
of a finite measure on [0,(delta+s_0)^(-1)]. Polynomial density in continuous
functions determines that pushforward measure and hence the original measure.
This uses the complete resolvent response, not a finite list of unbounded power
moments.

Generic cyclicity removes dark eigensectors for this passive scalar probe. It
does not recover the names S,V_p: a unitary fixing e_1 can change their designated
representations. Source passports and controlled responses remain necessary.
Nor does the result prove that the parameter-to-response map is injective
across a broader family of arithmetic sources.

## Boundaries and next discriminator

- The lambda=0 Jacobi limit is diagonal and e_1 is not cyclic for that limit.
  The proof mechanism fails there; cyclicity of the full prime-interacting
  operator has not been refuted.
- Sigma=2 may lie in the exceptional set. No named parameter is certified.
- Spectral cyclicity does not here prove polynomial Krylov density.
- Positive eigenmode weights may be arbitrarily small. For this infinite
  normalized spectral measure their sum is one, so their infimum is zero.
  Stable finite-energy visibility requires a separate quantitative theorem.
- No finite test or Lean declaration certifies this generic analytic result,
  and no physical measurement or realization selection was performed.
- Generic cyclicity does not authenticate prime sources. The same proof applies
  to analogous norm-analytic decaying perturbations with integrable derivative
  and a visible Jacobi limit. Genuine prime indexing and affine source laws are
  independently supplied inputs.
- The scalar shift defines the mathematical family; it is not an observed or
  predicted physical calibration constant.

The next verdict-changing target is a certificate at (lambda,sigma)=(1,2):
prove simplicity and nonzero boundary weights for every eigenmode, or construct
a genuine dark sector. Classifying the exceptional set and obtaining effective
finite-energy visibility are additional concrete targets.
