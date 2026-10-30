# Fibonacci arrows: pre-execution predictions

Parent PR408, exact head `7b5a2b4534aa5e71865046ca8d3f723d8002b9fe`.
All experiments below precede their first execution. Finite exact arithmetic
checks a displayed proof; it does not establish an infinite theorem by census.

1. **Translated Fibonacci/Lucas observations.** On finite native grade support
   retain both endpoint posteriors and all products of harmonic, golden,
   translated Fibonacci and Lucas readouts. Prediction: translations add only
   two independent rational grade functions. At m=6,d=5 a rational nonzero
   cycle remains. PASS: exact null vector plus positive distinct native-source
   couplings, all declared products equal. FAIL: a nonzero asserted defect or
   positivity failure. AMBIGUOUS: only floating rank evidence.
2. **Discrete Fibonacci PGF probes.** At q_n=lambda^(F_(n+2)), evaluate joint
   grade PGFs. Prediction: exact finite Vandermonde reconstruction succeeds,
   but arbitrarily late-grade checkerboards are uniformly almost invisible.
   PASS: exact reconstruction in Q(lambda) and analytic instability bound;
   FAIL: singular matrix for distinct marks or bound violation.
3. **Continuous Fibonacci powers.** Construct finite L2 residuals with Gram
   matrices, integrate twice, and compare an independently derived Cauchy
   product. Prediction: all declared Fibonacci moments vanish, omitted fourth
   moment is positive, and the infinite residual has positive norm. Authentic
   BBP one-place marginals survive in two distinct positive joint couplings.
   PASS: all rational identities and global density bounds; FAIL: a nonzero
   required moment or nonpositive certified infinite-product lower bound.
4. **Composition repair.** Canonical Zeckendorf products should recover ordinary
   integer moments; 4=3+1 should separate the preceding aliases. PASS: exact
   greedy reconstruction and omitted moment. No prediction of signed BBP
   dispersion follows; coherent same-forcing seed must remain indistinguishable
   to source-only probes.

Declared test sets: finite support (m,d)=(6,5); source a=1,17,57; residual
L=0,2,7, depths 3,5,8, and product bounds through Fibonacci index24.
Fresh holdouts reserved: a=97,233; L=12,29; support (7,5); tomography dimensions
2,3,5; residual depths6,9; Zeckendorf integers1000..1300.
The discrete and continuous realization maps must never be conflated.
