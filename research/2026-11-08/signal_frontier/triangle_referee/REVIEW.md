# Independent hostile audit of the two triangle realizations

**Verdict: no correctness defect found in the reviewed TP and GT paper claims.**
This is a separate derivation and implementation within the same model family,
with inherited repository context. It is not external scholarly refereeing.
The exact reviewed proof hashes are recorded in `RECEIPT.json`. The original-zero
signed covariance estimate and pi base-16 normality remain **OPEN**.

## Reviewed mathematical claims

- **TP1 posterior-valued update.** The circle kernel retains the latent X and
  the original source signature. Its two branches give the stated Pascal
  recursion, and source maps preserving f intertwine the kernel. Removing X
  requires the declared posterior state; the construction does not replace
  the deterministic BBP clock by a Bernoulli sampler.
- **TP2–3 triangle and minimal tomography.** Independently derived the oriented
  barycentric inverse and checked its determinant sign. Reality supplies the
  negative Fourier moments. The interval of exponents from −H to H contains
  m+1 consecutive exponents exactly when2H>=m; the corresponding Vandermonde
  minor is invertible for distinct unit nodes. Below this threshold a real
  null vector with zero total mass gives two strictly positive probability
  vectors in one observation fiber. The target row-span criterion is correct.
  Exact identifiability is explicitly separated from uniform conditioning.
- **TP4 posterior alias.** Recomputed both priors directly: their first two
  f-moments are1/2 and7/25, their depth-two grade vectors are
  (7/25,11/25,7/25), but their third f-moments differ by3/250. The two next
  failure probabilities are41/70 and22/35. These are different priors outside
  the known authentic continuous family, as the paper explicitly states.
- **TP5 clock limits and envelope.** The fixed-a contraction and dominated
  convergence argument applies because0<f,g<1 and e(h alpha)!=1. Both
  constants in TP8 were independently recomputed after t=e^(−8X).
  For the native limit, an independent direct density route is available:
  Q(x)<=15x and Q(x)>=15x e^(−5x), hence
  R(a)>=15/(a+5)^2. The density of Y=aX is bounded by
  ((a+5)/a)^2 y e^(−y), and converges pointwise to y e^(−y). For a>=5 this
  is at most4y e^(−y). The bounded complex binomial integrand converges to
  exp((z−1)y), so dominated convergence yields (2−z)^−2 directly. This
  verifies the changing-law step without incorrectly applying fixed-measure
  dominated convergence to the X variables.
- **GT1–3 geometry and decorated composition.** The word length formula,
  posterior multipliers, and their composition are exact. Grade erasure loses
  spatial positions of01 and10 while preserving their exchangeable latent
  posterior. The explicit random spatial coarsening kernel sends Pi_(m+1)
  to Pi_m; equality after merely forgetting labels is correctly not asserted.
  Integer clock labels require the stated common offset and anchor transport.
- **GT4 infinite discipline.** The fixed-prior address law is projectively
  consistent. The square-subsequence Chebyshev/Borel–Cantelli proof supplies
  the needed strong law. The address-frequency event has full geometric
  measure and source mass precisely mu({x*}); its complement is one common
  geometric null set supporting the rest of the mixture. Thus the continuum
  mixture really is singular off that atom, not an invalid inference that
  mixtures of singular measures are always singular. Endpoints are null
  because every infinite address has probability0 for finite X>0. Native
  changing-prior rows fail projectivity by the stated exact first-bit witness.
- **GT5 finite separation.** Recomputed the density bound on the2eta band,
  both Chebyshev costs, the optimizing eta, the Markov/Chebyshev native
  comparison, and the native coefficient12+8alpha. For the final exponential
  bound, checked the exact integer threshold t, geometric Markov cost
  2^(t−1)E[2^(-J)], and source cost (2/3)^t E[(3/2)^J]. The inequality
  1+g(X)/2<=exp(4X) gives the finite original ratio
  R(4m−7)/R(8m−7) for m>=2. Its limit is4, and both exponential rates are
  strictly negative. The fixed-a rate is
  explicitly nonuniform in a; the separate native result does not create a
  compatible infinite path law.
- **GT6–7 curvature and Farey geometry.** Checked the sine-product deficit,
  the Euclidean area product, the factor2 in Area/(R Delta), the cubic
  asymptotic constants and both finite ratio envelopes. The Cayley boundary
  map, rather than exp(2pi i x), preserves distinct Farey cusps. The displayed
  hyperbolic area integral gives pi, while Euclidean areas tend0. No metric
  or source-probability identification is silently used.

## TR1. A further compatibility diagnosis: law limits are not prefix-point limits

The two valid circle realizations have different infinite behavior even at
one fixed authentic prior. This gives a concrete check on a future proposed
triangle-observer natural transformation.

Let J_m be the number of ones in the first m retained sensor bits and
Z_m=e(J_m alpha). Conditional on any finite X>0, the success probability
p=g(X) lies in(0,1). With probability1 there are infinitely many ones: for
any N, the probability of no success after N is the limit of (1−p)^r as
r→infinity, hence0; take the countable union over N. Integrating over X
preserves this probability-one statement. At every success,

    |Z_(m+1)−Z_m|=|e(alpha)−1|>0.

A convergent complex sequence has consecutive differences tending0.
Consequently **Z_m has no pointwise limit almost surely**, although TP7
proves that its probability laws converge weakly to Haar. In contrast, the
nested golden intervals have diameters at most alpha^(k0+m), so their
address point converges for every infinite path.

Consequently no fixed continuous map from the convergent address points can
produce these nonconvergent grade-circle points at every prefix. In the other
direction, no fixed continuous **injective** circle map can send the
grade-circle sequence to the convergent address sequence: compactness makes
its inverse on its image continuous, which would force the original sequence
to converge. A noninjective constant map or a time/history-dependent transport
is not excluded. These statements do not refute either finite realization
or a product/decorated construction retaining both. They specify which
topology and transport a stronger correspondence would need to supply. No arithmetic cancellation estimate follows
from either limit. The explicit deterministic all-ones path also witnesses
the pointwise nonconvergence without a probabilistic premise.

## Independent finite oracle

`oracle.py` imports no TP/GT implementation, front oracle, or source builder.
It uses exact Fraction Gaussian arithmetic, independent rational row reduction,
a beta-product integral for the original four-pole source, and exact
Q(sqrt5) ordering for geometric total variation. Executed checks:

-18 full-rank minimal menus and18 strictly positive aliases below the bound;
-91 barycentric inversions including boundary weights;
-148 source integral/rational-form cross-checks,15 normalized positive source
 rows,12 source means, and182 posterior refinement identities;
-18 exact source/geometric TV comparisons, including six strictly positive
 lower bounds (two fixed-a and four native), with no floating sign decision;
-4 exact posterior-alias checks,1 native projectivity rejection,64 exact
 Fibonacci return identities, and32 exact same-forcing integer-seed phase/carry
 aliases.

The source row is obtained from beta products

    q_(a,m,j)=binom(m,j)/(8R(a)) *
      [4B(a/8+m−j,j+1)−2B(a/8+3/8+m−j,j+1)
       −B(a/8+1/2+m−j,j+1)−B(a/8+5/8+m−j,j+1)],

where B(x,j+1)=j!/product_(r=0)^j(x+r). Smaller cases are cross-checked
against a separate shifted-R expansion. All comparisons in this oracle are
exact; they check finite instances, not the infinite source theorems.
The paper proofs, their declared classical ingredients and the source-map
scope remain indispensable. No Lean certificate is claimed for this review.

Run from the repository root:

```sh
python research/2026-11-08/signal_frontier/triangle_referee/oracle.py \
  --output /tmp/succ-triangle-referee.json
```

## Source-cancellation boundary

The same-forcing coherent seed −pi/16 shares the positive source prior,
Pascal observers and probe-circle geometry while its signed BBP means tend1.
The reviewed constructions preserve this distinction. A separate exact
authentication control is the integer seed1: U_n(1)=U_n(0)+16^n, so all
integer circle harmonics and carries floor(U_n)−16floor(U_(n−1)) coincide,
although the literal unwrapped boundary differs. Thus even phase plus these
carry marks require the retained initial lift to identify literal seed0.
This is an identity alias, not a nonnormal counterexample; its circle orbit
is identical to the zero-seed orbit. An exact finite
triangle reconstruction is not a proof of a zero-source signed estimate;
appending U0=0 and carries as authenticated marks does not itself supply
such an estimate. The surviving task is the explicit source-preserving,
all-epoch bridge to the retained signed covariance.

**Pi base-16 normality: OPEN. RH: OPEN.**
