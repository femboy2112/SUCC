# EAB — generalized Euler boundary, prime cofinality, theta completion

**Date:** 2026-10-24. **Research branch:** research/generalized-euler-adelic-boundary-2026-10-24.
**Pinned inspected parent:** main@e648df3e4fca73ab6b942232b5ca4b310e9cac08.
**Dossier:** [Generalized Euler–Adelic Boundary](../research/2026-10-24/GENERALIZED_EULER_ADELIC_BOUNDARY.md).
**Source distinction:** classical analytic theorems, exact finite rational checks, and numerical diagnostics never automatically substitute for one another. No proof of RH or pi normality.

| ID | Mathematically quantified statement | Status and falsifier |
| --- | --- | --- |
| EAB-01 | For all complex s with Re(s)>0, the original generalized harmonic-minus-integral cutoff converges locally uniformly to G(s)=zeta(s)-1/(s-1); G extends entire and G(1)=gamma. | **CLASSICAL / PAPER PROVED** using absolutely summable SUCC cell differences. Not literal convergence throughout C. |
| EAB-02 | The original finite cutoffs at s=0 all equal 1, but the entire continuation G(0)=1/2; the two limit orders differ. | **EXACT COUNTEREXAMPLE** to boundary-uniform interpolation. |
| EAB-03 | For real r>0 the positive cell tail is at most 1/(2N^r); integer r>=2 yields exact Fraction endpoint certificates. | **PAPER PROVED / EXACT RATIONAL CHECKED.** |
| EAB-04 | Mesh h>0 and starting chart q>0 give the aligned-cell Hurwitz limit h^-s[zeta(s,q)-q^(1-s)/(s-1)] and value [-digamma(q)+log q]/h at s=1. | **CLASSICAL PAPER PROVED / NUMERIC CHECKS**; shifting q refutes gauge-free gamma. |
| EAB-05 | The derivatives G^(m)(1)=(-1)^m gamma_m are sums of differentiated SUCC cell defects; all infinite coefficients determine G globally, finitely many do not. | **CLASSICAL / PAPER PROVED**, no claim of finite observer completion. |
| EAB-06 | On Re(s)>1, P(s)=-zeta'/zeta is the genuine FUCC prime-power current and obeys G'+P G=(s-1)^-2-P/(s-1). | **CLASSICAL / PAPER PROVED**; fake Euler factor p=6 is a mutated, nonauthentic source. |
| EAB-07 | For real s>1, 0<=zeta(s)-P_X(s)<=X^(1-s)/(s-1); at fixed X, P_X(s)-1/(s-1) tends to negative infinity as s decreases to one. | **PAPER PROVED**; prime completion / pole subtraction do not commute. |
| EAB-08 | For integer q>=2, epsilon=1/q and X=q^(2q), true-prime P_X(1+epsilon) differs from zeta(1+epsilon) by <=1/q. Hence P_X(1+1/q)-q tends to gamma. | **ELEMENTARY PAPER PROVED**, exact integer cutoff and numeric samples; astronomically expensive, no PNT. |
| EAB-09 | Completed B(s)=pi^(-s/2)Gamma(s/2)zeta(s)-1/(s-1)+1/s is entire, reflection-invariant, admits the theta heat integral and B(0)=B(1)=1+gamma/2-log(2sqrt(pi)). | **EXTERNAL CLASSICAL TATE/POISSON / PAPER DERIVED**, numeric theta diagnostics. |
| EAB-10 | Real critical-line positive-type B is insufficient for RH: 2+cos(t) is positive definite, positive for real t, yet zero at pi+i arcosh(2). | **EXACT COUNTERMODEL**, no Weil positivity or RH proof. |
| EAB-11 | For any finite m, finitely many adjusted positive prime Euler exponents preserve zeta pole residue and first m+1 regular Laurent coefficients, but not the true exponent-one source. | **PAPER PROVED FINITE-DIMENSIONAL NULLSPACE**; scalar/finite jets fail to select authentic source. |
| EAB-12 | The symmetric factor 1+c[s(1-s)]^(m+2) preserves completed reflection, both pole residues and first m+1 regular coefficients, yet changes the completed zeta. | **EXACT MUTANT**; functional equation plus finite jets is insufficient. |
| EAB-13 | For r=2, the SUCC cell is 1/[n^2(n+1)]; the external Basel theorem gives pi^2=6(1+sum cells). Its rational bounds certify hexadecimal prefixes using exact integer square roots. | **EXACT FINITE CERTIFICATES GIVEN CLASSICAL BASEL**: N=50 -> 3.243, N=300 -> 3.243F; no normality estimate. |
| EAB-14 | Existing OCG-05 LCM jumps yield the authentic prime-power von Mangoldt current; PNT supplies a weighted-clock limit for gamma. | **CLASSICAL / EXACT FINITE TESTED**; not a new PNT or RH proof. |
| EAB-15 | The present data uniquely select an adelic physical geometry, certify Weil positivity, or prove pi normality. | **UNVERIFIED / NOT CLAIMED**. Source-authentic character families and BBP-specific carry bounds are missing. |

**Controls:** endpoint order at s=0; zeta cancellation at one; mesh q,h mutation; genuine primes vs fake composite six; prime completion order; exact cofinal cutoff; theta s versus 1-s; symmetric nonlocal multiplier; off-axis zero in positive-type kernel; exact rational pi digit interval; OCG prime powers.

**Reproduce:** python -m unittest discover -s tests -p 'test_generalized_euler_adelic.py' -v ; python scripts/generalized_euler_adelic_probe.py --verify.
Then execute repository-wide AGENTS.md validation. The isolated local twelve-group pass is not a hosted CI certificate. **Pi normality and RH remain OPEN.**
