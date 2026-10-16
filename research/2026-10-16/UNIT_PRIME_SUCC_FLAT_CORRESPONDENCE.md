# Unit-to-prime SUCC: a flat weighted correspondence

**Status:** classical, paper proved under explicit hypotheses; exact finite Fraction checks are separate evidence. This dossier is a source-indexed SUCC integration, not a claim to have invented Euler's product or the Bost–Connes system. RH proved: NO.

## 1. Two noncommuting paths on one source carrier

Let H=ell2(positive integers), with orthonormal e_n. The additive successor S e_n=e_(n+1) and prime dilation V_p e_n=e_(pn) are isometries, and basis checking proves

    V_p S = S^p V_p,     V_p V_q = V_q V_p.

They do NOT commute with each other: for p>1, V_p S differs from S V_p. Let s be complex, n,m positive and define the edge potential c_s(n,m)=(n/m)^s for directed legal S/V_p transitions. Every path from 1 to n has weight n^(-s), by multiplying and telescoping adjacent potential ratios. The generating weights are

    S: n->n+1 has (n/(n+1))^s,
    V_p: n->pn has p^(-s).

The weighted affine braid holds on all finite-support basis states. This is a flat multiplicative coboundary; paths that revisit the same endpoint must NOT be summed indiscriminately. Summing all mixed paths would overcount.

## 2. Hilbert-state theorem UPS-01

Define A_s e_n=(n/(n+1))^s e_(n+1) and B_(p,s)=p^(-s)V_p. For sigma=Re(s)>0, each B_(p,s) has norm p^(-sigma)<1, hence each geometric inverse (I-B_(p,s))^(-1) is bounded. However the infinite product needs a separate domain analysis.

**Theorem (classical):** For every complex s with sigma>1/2, in ell2(N),

    Psi_s = sum_(k>=0) A_s^k e_1
          = lim_(P->infinity) product_(p<=P)(I-p^(-s)V_p)^(-1)e_1
          = sum_(n>=1)n^(-s)e_n.

Proof: A_s^k e_1=(k+1)^(-s)e_(k+1). By unique prime factorization, a finite prime product applied to e_1 has coefficient n^(-s) at each P-smooth integer and zero elsewhere. Distinct states are orthogonal. Their squared coefficient norms are bounded by sum_n n^(-2sigma), which converges exactly for sigma>1/2. The increasing P-smooth sets exhaust positive integers, proving Hilbert convergence and equality. For sigma<=1/2 the candidate vector has infinite norm, so this Hilbert-state theorem fails. QED.

This says the SAME WEIGHTED VECTOR arises by two traversals. It is not operator conjugacy, and the scalar Euler product has a narrower convergence domain.

For sigma>0, the diagonal D_s e_n=n^(-s)e_n gives A_s=D_s S D_s^(-1) and B_(p,s)=D_s V_p D_s^(-1) **on finite-support vectors**. D_s is compact injective with dense range, but D_s^(-1) is unbounded; this is not a bounded or unitary similarity. Although A_s has norm 1, its vacuum orbit sum converges when sigma>1/2; do not assert (I-A_s)^(-1) exists boundedly on all H.

## 3. Convergence with explicit source-tail bounds UPS-02

Write Psi_(s,P) for the prime product vector through genuine primes <=P. Its exact Hilbert error and classical integral estimate are

    ||Psi_s-Psi_(s,P)||²
      = sum_(n has prime factor >P)n^(-2sigma)
      <= sum_(n>P)n^(-2sigma)
      <= P^(1-2sigma)/(2sigma-1)  for sigma>1/2.

The ordinary additive integer prefix has squared tail <=N^(1-2sigma)/(2sigma-1). These give distinct finite observer filtrations converging to the same global state. Runtime tests perform bounded exact coefficient comparisons; they do not prove the infinite inequalities by enumeration.

## 4. The exact unit/nonunit ratio UPS-03

For real beta>1, the vector also belongs to ell1, and coefficient summation is legitimate:

    zeta(beta)=sum_n n^(-beta)=product_p(1-p^(-beta))^(-1).

The unit term is exactly 1. The nonunit/unit MASS ratio equals zeta(beta)-1. For real sigma>1/2, the nonunit/unit HILBERT-NORM ratio instead equals sqrt(zeta(2sigma)-1). These are distinct observables of the same state, not competing definitions of zeta.

At a prime cutoff P, define Z_P(beta)=product_(p<=P)(1-p^(-beta))^(-1). Every omitted integer has a prime factor >P and hence itself >P, so

    Z_P(beta)-1 <= zeta(beta)-1
                <= Z_P(beta)-1 + P^(1-beta)/(beta-1).

This is a genuine rigorously quantified finite approximation for real beta>1, and exact rational bounds at integer beta>=2 are implemented in unit_prime_succ.py.

## 5. Logarithmic Archimedean clock and prime occupancies UPS-04

Under the fundamental theorem of arithmetic, ell2(N) has basis correspondence with the restricted prime-occupation space ell2(direct-sum_p N0). Each V_p increases exactly one prime coordinate; the additive S changes an entire valuation vector by alpha -> nu(1+product_p p^(alpha_p)). For example, the step 7->8 changes e_7 into 3e_2.

Define H e_n=(log n)e_n on its natural diagonal domain. Then

    [H,S]e_n = log(1+1/n)e_(n+1),
    [H,V_p]e_n = (log p)e_(pn).

The first commutator extends to a compact weighted unilateral shift because log(1+1/n)<=1/n tends to zero, with tail norm at n>N at most 1/(N+1). The second is a fixed multiple of an infinite-rank isometry, noncompact, with essential norm log p. These operators are not unitarily conjugate: dim ker(S*)=1, while dim ker(V_p*) is infinite.

At real beta>1, the diagonal Gibbs law P_beta(n)=n^(-beta)/zeta(beta) has independent prime occupancies with geometric probabilities P(nu_p=k)=(1-p^(-beta))p^(-k beta). Also

    Tr exp(-beta H)=zeta(beta),
    -zeta'(beta)/zeta(beta)=sum_(p,k>=1)(log p)p^(-k beta).

All rearrangements are absolutely convergent. This is the elementary carrier underlying a connection to the classical **Bost–Connes** zeta partition-function system. The construction here does not establish its full C*-algebra, KMS states, or phase transition. The normalized pure vector and diagonal Gibbs state share basis probabilities, but are not equal states on all observables.

Sources: NIST DLMF 27.4 https://dlmf.nist.gov/27.4 ; J.-B. Bost and A. Connes (1995), Selecta Math. 1 (1995), 411-457, https://doi.org/10.1007/BF01589495 .

## 6. Negative controls and SUCC relevance UPS-05

- Fake composite V_6 alongside prime V_2,V_3 double-counts e_6: both 6 and 2*3 are source words. Composite admission must fail.
- Wrong V_p S=S V_p fails on every ordinary positive basis state; the correct braid is V_p S=S^p V_p.
- Additive S and multiplicative V_p have different adjoint defect dimensions. Equal weighted states do not imply the dynamics are unitary-equivalent or the semigroup categories are equivalent.
- This state exists in ell2 for sigma>1/2, but its scalar total mass only converges absolutely for sigma>1.
- The parameter 1/2 is a Hilbert summability threshold; no RH or Weil positivity follows.
- Log p is an ordinary real energy coordinate, not a claim that Q_p converges to R or that the Archimedean Gamma factor has been derived.
- A generic completely multiplicative weight also has an Euler product when its series converges absolutely; the identity does not alone distinguish canonical von Mangoldt, conductor, Gamma or pole laws.

**Next source-specific step:** prove a formally typed flat cocycle/affine braid in YEAN; compare the two filtrations and their observer probe costs; then *separately* test an authenticated Tate/Weil transport with true Euler/Gamma/pole data and mutation controls. Do not import signed Weil positivity as an assumed consequence.

Verdict: CLASSICAL/PAPER PROVED equality of the weighted state, TESTED FINITE instances, REFUTED operator-conjugacy interpretation, RH OPEN.
