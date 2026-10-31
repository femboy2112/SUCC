# Analytic front: frozen questions before new computation

Parent: PR417 `1c6ce7d7ee83a0bd751bde8092e46ff798855fd3`.
Read-only siblings: #420 `1573ec5b8fbd60b251cb16741bd5165271ec6dbf`,
#421 `e14916aa2b4dfc2cce948facc729fb02ce1efafa`,
#422 `e8a4978207871a47466cdbb6f15cc86fae784164`,
#423 `287b9e9214f0214586cb6f0a993e29b58bed496a`.

1. A01: the authentic positive Hausdorff measure produces rational Gaussian
   resolvent approximants to pi/16 with exact Markov error intervals. PASS:
   exact orthogonality and independent rational recurrence agree; a separate
   certified BBP interval lies strictly in the Markov interval. FAIL: any
   inequality or coefficient identity fails. AMBIGUOUS: independent numerical
   calibration alone. Discovery orders d=1..8; fresh d=11,14,19.
2. A02: a uniform bound `188/(225*3600^d)` follows from monic Chebyshev
   extremality and support (0,1). PASS: a written all-d proof and exact
   inequalities at all tested d. This is analytic transport, not cancellation.
3. A03: the same Gaussian quadrature is a positive, rational-valued, zero-seed
   source matching the original first 2d values but with rational completed
   boundary. Predict FAIL for any finite-prefix-to-normality implication;
   PASS for exact prefix matches and fixed-frequency N+O(1) coherence.
   Source mutants (5,-5,0,0), (3,-2,-1,0) and a finite atomic source are typed
   controls; they need not match the authentic constant. Changed seed must
   leave source approximants unchanged and shift the selected boundary.
4. A04: theta/Mellin completion admits a uniform compact-strip finite-lattice
   error bound for every fixed derivative order. Discovery M=1,2,3 at
   s=-1,2,1/3+2i; fresh s=-3,2/7+13i/7,5/4-7i/3 and derivative orders 0,1,2.
   PASS: analytic bound and numerical residual inside it with explicit numeric
   tolerance; numerical agreement is corroboration, not an interval theorem.
5. A05: finite full analytic jets do not identify a general source; complete
   convergent germs identify within a connected analytic domain. #423 already
   proves the identity-theorem boundary. No rediscovery of its flat-shadow
   theorem or #421's polar-source obstruction will be promoted as new.

Separate implementations share this agent/model and classical mathematics;
they are not independent mathematical authorities. No pi-normality or RH
conclusion is predicted. No nontrivial zero location is an input.
