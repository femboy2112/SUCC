# Independent model-front review of FR1--3

Status: **PASS, paper-proof review**. Same-model-family independent assignment;
no external refereeing or Lean claim. Reviewed document SHA256 `cb21ae0b5ffbcda208312d363f261ea0b48983c5b76208542d4c86a1ad8273f3`.

1. Recomputed the large-fold vertex estimate: if both consecutive norms are
   below a=1/32, even-power factorization forces edge error above15/32. At
   most(32/15)sum e edges fail this threshold; each large vertex covers at
   most two surviving edges. This gives exactly equation(1).
2. Recomputed the circle-fiber strip: proximity to a disk center gives
   `|Re(z*conj(d))-|d|^2|<=delta*(1+delta)`. Since |d|>=a/2, its cosine band
   has width parameter at most4delta/a. On[0,pi], the identity for cosu-cosv
   bounds intervalwidth by pi*sqrt(epsilon); reflection gives normalized
   circlelength at mostsqrt(epsilon). Each band has at most two connected
   arcs, costing2Delta in discrepancy.
3. With delta=1/(2048M^2), the union's length bound is exactly1/4. Markov's
   discarded fraction is rho/delta. These reproduce FR1, including its
   finite endpoint term and all signs. Cases of empty bands, repeated
   centers and a negative right side cause no problem.
4. The two source forcing phases cost pi|h| times their positive forcing
   sum. Their common denominator lower bound8n0+1 yields the stated
   30pi|h|/(8n0+1)^2 average bound. For q=2, n0=2m+1, the first marginal
   occupies the macroscopic interval[2m+1,3m]; conditional normality and
   prefix subtraction suffice for arc discrepancy there.
5. The compactness argument is a distinct proof architecture: for nonzero
   d, the two-unit-root fiber of their mean d has at most two first
   coordinates. Haar marginal kills every such finite fiber. Mean zero
   forces the antidiagonal, which simultaneous even powers move to the
   disjoint diagonal. Actual componentwise source transport, not merely
   first-moment transport, gives invariance of weak subsequential limits.

Both normality and infinitely many selected q=2 clocks remain stated
hypotheses in FR2. The result is a conditional approximation obstruction;
it supplies no signed covariance decay estimate and does not exclude
continuous or growing-range observers. The assigned finite predictors'
errors dominate distance to their finite output set in the declared common
phase frame, so the application to the frozen disk-valued table is sound.
