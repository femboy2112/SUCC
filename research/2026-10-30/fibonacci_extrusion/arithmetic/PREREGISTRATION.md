# Fibonacci arithmetic: hypotheses registered before the finite probes

Parent PR408 `7b5a2b4534aa5e71865046ca8d3f723d8002b9fe`.
Original four poles and U0=0 remain fixed. This folder studies derived
observables and explicitly typed controls; it does not replace the source.

1. **FA01, spectral compatibility.** For the Fibonacci matrix
   M=[[1,1],[1,0]], rows L satisfying LM=16L over Z/m are exactly
   (16t,t) with 239t=0. Predict exactly gcd(m,239) rows, only zero over
   Q/R and no primitive solution mod239². Test exhaustive small moduli
   2..40 plus239 and478; algebraic construction at239²,239³ and fresh
   prime moduli257,263. A wrong row/count refutes the finite formula.
2. **FA02, original-source defect.** P(E)=E²−E−1 gives
   P(E)U_n=239U_n+15r(n+1)+r(n+2), with a positive rational source
   defect. Test n=0..96 and seeds0,1/16,2/7; mutants separately.
   Prime239 resonance must NOT make the authentic defect vanish: n=0
   is the decisive exact falsifier. First239-conductor birth is n=60,
   with239U60=-1/2 mod239. Test n<=60 using exact fractions.
3. **FA03, temporal assembly.** Greedy nonconsecutive Fibonacci lengths
   tile every integer interval. Bounds on every translated Fibonacci block
   imply global bounds by the triangle inequality. At exponent1/2,
   sum sqrt(length) <= sqrt(N)/(1-1/sqrt2). Test allN<=4096 and
   fresh N=10007,65537,1000003. This only checks the combinatorial
   mechanism: no authentic signed block premise is assumed or fitted.
4. **FA04, sparse snapshots.** Overwrite k² base16 digits starting at
   position F_k for k>=2. The edit set has density0; every fixed word
   count changes by at most its length times the number of edited sites.
   A normal starting stream therefore stays normal while the pure radix
   phases at times F_k approach0 (indexing made explicit in the paper).
   Test deterministic finite words, counts and snapshot zeros. Finite
   samples corroborate the counting lemma, not the infinite normality claim.
5. **FA05, Fibonacci-lag stability.** Cassini gives a Bezout estimate
   ||x|| <= F_k||F_k x||+F_(k-1)||F_(k+1)x||. The golden rotation
   x=lambda has both sampled distances exponentially small while ||x||
   stays positive; a universal scale-independent lag comparison fails.
   Verify the exact Q(sqrt5) identity and rational interval bounds for
   k=3..24 and fresh k=31,37. This control is a circle rotation, NOT an
   authentic radix16 trajectory.

Pass means exact equality/inequality in the declared domain. Failure is
a counterexample or implementation defect to preserve; numerical agreement
alone is ambiguous for every infinite assertion. Same-model separate
algorithms do not create independent external refereeing.

The prior Fibonacci clock dossier is read at its existing remote-tracking
ref; its source fingerprints are recorded in SOURCE_MANIFEST.json. It
already proves a golden Gamma eigenvalue and declared Fibonacci-clock jets.
Those are inherited, not new discoveries here.

Additional FA01 probe registered before execution: lift the simple root16
of x²−x−1 modulo239 through precision239^5 by the exact Hensel digit
equation. Predict a unique root near16, already different from native16
at precision239². Compute both local matrix and native16 multiplicative
orders modulo239; any equality is local algebra only, never an arithmetic
phase identification.

Fresh selected signed calibration registered before execution: full rational
lag-one phases, with no CRT marginal discarded, on disjoint intervals
[F_k,F_(k+1)), k=7..15, h=1,3,7; holdout k=16, h=11,13.
Count distances >=1/20. Predict more than half in each finite authentic
window, while the coherent same-forcing seed has none whenever
16|h|/(8F_k+1)^3<1/20. A failed half-count refutes only this finite
prediction; passing is OBSERVED, never an asymptotic density theorem.
The true open premise is a uniform selected bound over translated growing
Fibonacci blocks, followed by a sufficient all-frequency signed assembly.
