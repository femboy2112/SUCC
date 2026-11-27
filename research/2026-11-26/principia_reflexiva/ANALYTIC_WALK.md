# PRF-13/14 — A perpetually forward stochastic analytic clock

This is the direct realization of the author's refined nucleation hypothesis on the arithmetic character carrier, without requiring a reset, a reversible random walk, or a return to the exact starting phase.

## PRF-13. Uniform finite-cylinder hitting on a compact dense flow

Let K=product over primes of unit circles, with product topology. Define the continuous group flow z(t)=(p^(-it))_p from PRF-08. Fix any starting phase X_0 in K. Let independent positive durations E_j have a common law mu with full support on (0,infinity); e.g. Exp(lambda), lambda>0. Set

\[
 X_k=X_0z(E_1+\cdots+E_k).
\]

All moves are forward in the analytic clock. The distribution need not depend on current novelty, labels, or the target. Retain actual sampled durations and any lawful observed phase coordinates. A zero old-frame novelty score is not claimed to generate this distribution; the independent clock is the chosen blind-search policy.

**Theorem.** For every nonempty open cylinder C=pi_F^(-1)(V) with finite set of primes F and nonempty open V in T^F, there is eps_C>0 such that for every k and every starting phase,

\[
 {\mathbb P}(X_{k+1}\in C\mid\mathcal F_k)\ge\epsilon_C .
\]

Consequently the first entrance time tau_C is finite a.s., E tau_C<=1/eps_C in clock steps, and P(tau_C>k)<=(1-eps_C)^k. If E_1 has finite mean m, expected elapsed analytic time to entrance is <=m/eps_C. Every nonempty open set in K contains a cylinder, so it too is hit a.s. Countably many cylinders from a countable base are all visited infinitely often a.s.; hence the sampled orbit is dense almost surely.

**Proof.** Project to the finite torus T^F. Positive-time orbit segments are dense by the same character-average proof as PRF-08, using [0,T]. For each y in T^F choose t_y>0 with y z_F(t_y) in V. Joint continuity supplies an open neighborhood W_y of y and a nonempty open interval I_y contained in (0,infinity) such that W_y z_F(I_y) is contained in V. Compactness gives a finite cover W_1,...,W_J. Let eps_C=min_i mu(I_i)>0 by full support. From any phase one of the W_i applies, and the next independent duration has probability >=eps_C to lie in I_i. This bound is uniform and is measurable conditional on the full history; the observer does not need to know which W_i it occupies to implement its clock. PRF-01 gives the hitting estimates. For expected elapsed time, write sum_{j<=tau} E_j = sum_j 1_{tau>=j} E_j; the event {tau>=j} is determined before the independent E_j, so Tonelli gives m E tau. Apply the hitting argument after every fixed deterministic step and intersect countably many probability-one events to prove infinite visits to every element of a countable base. This is a constructive probability model on the analytic place, not a physical clock claim.

**Certificate transfer.** If a target bridge has a finite sound decoder whose accepting region includes such a cylinder, and that decoder is actually run at the visited observations, then the same bound applies to its first acceptance (plus a separately accounted finite verification cost). For an arbitrary set of acceptable histories, use the appropriate enlarged history state or PRF-04. A hidden accept region with no accessible verifier is not a certificate. An observer can run a countable dovetailed family of candidate decoders; the fairness/finite-cost scheduling obligations still apply. One can use an open region as a robust discriminator only after proving its margin and soundness for the stated source class. A finite set of exact equalities need not define an open region.

This makes the non-starvation assumption true by construction for finite-resolution open targets on the specified analytic place. It does not extend to arbitrary noncompact or transience-prone search spaces.

## PRF-14. Quantitative Fourier convergence and a.s. analytic mapping

Take Exp(lambda) increments. For any nontrivial character chi_n/chi_m with m!=n in N_+ (or any nonzero finite integer prime-exponent vector), write omega=log(n/m)!=0. The one-step character multiplier is

\[
 \phi_\omega=E e^{-i\omega E_1}=\lambda/(\lambda+i\omega).
\]

Thus E chi(X_k)=chi(X_0) phi_omega^k, with modulus decaying as (1+(omega/lambda)^2)^(-k/2). Finite trigonometric polynomials converge in expected value to their Haar integral. The near-colliding arithmetic frequencies omega=log((n+1)/n) approach 0, so this does not give one uniform mixing rate over all characters.

**Almost-sure empirical Haar theorem.** For Y_k=chi(X_k), |Y_k|=1, independence of increments gives |E(Y_j conjugate(Y_i))|=|phi_omega|^(j-i) for j>=i. Therefore

\[
 E\left|N^{-1}\sum_{k=1}^N Y_k\right|^2
 \le {1+2|\phi_\omega|/(1-|\phi_\omega|)\over N}.
\]

For the subsequence N=l^2, Markov's inequality and the ordinary first Borel-Cantelli lemma imply almost-sure convergence of these averages to zero (intersect over positive rational tolerances). Between l^2 and (l+1)^2, the bounded summands give a difference tending to zero. There are countably many characters, so the convergence holds simultaneously for them a.s. Trigonometric cylinder polynomials separate points and are uniformly dense in continuous functions of K by Stone-Weierstrass. Approximation shows the empirical probability measures converge weakly to Haar almost surely. This yields a precise analytic mapping limit with finite-resolution refinement and no external choice of which prime directions to visit. It does not give finite exact knowledge of every analytic coordinate, and expectation/mixing estimates are not arithmetic truth probabilities.

For a finite Dirichlet series F(it), the same character convergence gives the original coefficient via the empirical average of F(i t_k) m^(it_k), for any fixed initial clock and almost every sampled clock sequence. Nonzero finite coefficient separation margins can be targeted by lawful calibrated decoders; exact equality needs independent certification.

### Sharp hostile controls

1. Dense flow and full-support durations do not imply exact hit of a specified singleton phase: choose the 2-coordinate target 1, with t_0=0 and exclude the starting time. The set of positive t with exp(-it log 2)=1 is countable. With continuous independent exponential durations each t_k has a continuous density, so the probability of any exact hit at k>=1 is zero. More generally a prescribed one-coordinate equality has this obstruction. It is not a counterexample to the open-cylinder theorem.
2. Degenerate discrete increments E=2pi/log 2 preserve the 2-coordinate identically; they fail the full-support contract. Continuous-time density does not by itself imply a given discretization explores the space.
3. Tiny open regions can have arbitrarily small eps_C. Countable a.s. coverage is not a uniform finite upper bound on discovery cost.
4. Uniform random physical movement on the infinite 3-regular tree fails as in PRF-03. Compact finite projections plus a full-support analytic time flow are the load-bearing extra structure here.
5. If both rival sources give the same full history, the clock is source-independent randomization and cannot distinguish them. The theorem supplies discovery/coverage, not missing source information.

## Finite exact calibration analogue

On a cycle Z/q, let positive integer increments have geometric law P(E=j)=2^-j (j>=1). For each residue r represented by r in {1,...,q}, P(E=r mod q)=2^(q-r)/(2^q-1). Hence every transition has probability at least 1/(2^q-1) and exact singleton targets are reachable in one step with positive probability. This illustrates why a discrete exact certificate search can differ from a continuous phase search. It is not a numerical discretization proof of the infinite-torus theorem.

**Verdict:** PRF-13/14 are PROVED LOCAL using classical compactness, Fourier characters and elementary probability. The proof covers robust recognizable open-cylinder certificates, not every constructible but unrecognizable semantic tool. This is an example of a genuine carrier-specific fairness proof rather than assuming the desired eventual discovery.
