# SUCC Pisot Ramification — exact claim ledger

Research 2026-10-30, stacked on Universal N PR #416. Original source and U0=0 untouched.

| ID | Domain, theorem, quantifiers | Status | Adversary and unresolved debt |
|---|---|---|---|
| PIS-01 | 2-colored length grammar a_n=a_(n-1)+3a_(n-2), nonPisot root alpha=(1+sqrt13)/2; binomial b_n=sum_k C(n,k)a_k has Pisot-unit root theta=alpha+1, and signed binomial inverse recovers a | DISCLOSED exact | Changing time generator != conjugating the original dynamical operator |
| PIS-02 | For every positive integer a,b, a 2x2 positive recurrence matrix A=[[a,b],[1,0]] admits a nonnegative integer shift mI making the Perron root Pisot (degree1 or2) | DISCLOSED theorem (quadratic conjugate in [-1/2,1/2]) | False generalization to cubic: complex imaginary part >1 |
| PIS-03 | Generating 1/(1-z-3z²) admits exact nonnegative series sum_(k>=0) 2^k z^(2k) [1/(1-z-z²)]^(k+1), finite coefficientwise | DISCLOSED formal-series/combinatorial bijection | Number of Pisot components grows with n, not bounded fixed finite decomposition |
| PIS-04 | Cubic A companion x³-x²-3 has nonPisot conjugates with abs(Im)>1; no real affine scalar shift Pisotifies | DISCLOSED exact root bound | Degree-1 shift fails, need nonlinear finite arithmetic operation |
| PIS-05 | B=2I+A+A² is strictly positive integer matrix with char x³-8x²+5x-1, det=1, dominant root Pisot unit and A=2I-B^(-1) | DISCLOSED exact polynomial/matrix | B forward dynamics is not one-step conjugate to A forward dynamics |
| PIS-06 | Z[alpha]=Z[theta], change-of-basis det=1; both polynomial discriminants -255, field discriminant squarefree, ramified primes 3,5,17 | DISCLOSED exact algebraic-number theory | Coincidence 255=16²-1 does NOT establish a BBP connection |
| PIS-07 | Positive quadratic P(x)=2+x+x² is MINIMAL polynomial degree for Pisotifying cubic while generating same field: any nonconstant linear integer P keeps conjugate imaginary magnitude >1 | DISCLOSED proof | Constant Pisot integer cannot generate degree3 field |
| PIS-08 | A has determinant 3 (singular mod3); B has determinant1 and inverse over all Z_p. The singularity is relocated to observer A=2I-B^-1 | DISCLOSED exact | Dynamic singularity at p and field discriminant ramification are different facts |
| PIS-09 | Cubic colored 1/3-length grammar admits sum 2^k z^(3k)[1/(1-z-z³)]^(k+1) with Pisot base root of t³-t²-1 | DISCLOSED positive finite counts | Still unbounded number of components at depth n |
| PIS-10 | Every real number field K of degree>1 has a Pisot unit generating it, hence any algebraic integer alpha in K is rational polynomial in such a unit | CLASSICAL Pisot/Salem/Meyer, see JSC 2018 source | Does NOT guarantee integer polynomial P, positive matrix, no loss, or semiring functor |
| PIS-11 | Any nonconstant P∈Z_(>=0)[x] fails to Pisotify the positive 2x2 matrix [[2,1],[1,3]], whose OTHER real conjugate is >1; nevertheless A-I remains positive Pisot | REFUTED naive universal positive-polynomial claim, exact counterexample | Nonnegative coefficients of P vs nonnegative entries of P(A) must not be conflated |
| PIS-12 | Pisot conjugate contraction of B implies the reconstructed original dynamics A is Pisot or forces base16 π normality | REFUTED as inference; A=2I-B^-1 has expanding inverse conjugates | Need original-source/selected zero-boundary phase transport and source-sensitive estimates |
| PIS-13 | All finite arithmetic dynamics can be functorially represented as positive Pisot path systems preserving selected observables and prime place data | UNVERIFIED | Number-field theorem gives field coordinates, NOT positive source-faithful global dynamics |
| PIS-14 | π base16/base3 normality or RH follows from the Pisot ramification of these toy recurrences | UNVERIFIED / OPEN | Different arithmetic source, no new selected signed Weyl/cylinder estimate |

The word ramification is used in three typed senses: positive path-color refinement, reversible Pisot-coordinate algebra, and genuine discriminant prime ramification. Each source/observer relation requires a separate adequacy check. No probability, causal/physical or quantum claim follows from the toy examples.
