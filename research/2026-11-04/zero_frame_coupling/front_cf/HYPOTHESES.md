# C/F hypotheses before integration

Base: #506 `bc2d7b01` as supplied by the coordinator; the exact local source
head is recorded in validation. All source transforms use the original
four-pole U, its authentic angular Y and radial Z, and forward time.

1. **Many delayed coupled characters should obey a signed Bessel bound.** The
   Gram off-diagonal depends only on `Z_(n+l)-Z_(n+k)`, whose increments are
   separated from integers when `|l-k| Lambda/A <= 1`. Prediction: an actual
   average saving over polynomially many logarithmic lags, also for maximal
   subintervals. This does not predict selection of lag zero.
2. **The common-gauge Gram spectrum should be seed-blind.** Multiplication by
   one unit-modulus angular sequence is unitary. Prediction: the full Gram is
   unchanged under coherent, normal, or 1/5 seed changes, and under an
   artificial anti-companion. A selected-coordinate conclusion needs more.
3. **Separate lag dephasing might control the mixed van der Corput term.**
   Proposed positive outcome: a mixed signed bound derived from original
   carries. Hostile prediction: the same-forcing coherent seed has two small
   marginal lag means but an almost-one product mean. This would reject an
   independence inference while leaving the literal zero-seed question open.
4. **A delayed radial compensation can remove the leading source-tail jet.**
   Prediction: `W=U-(Z_(n+1)-Z_n)/2` has an O(n^-3) completion error and an
   additive O((j+Lambda)/A) high-to-low frequency comparison. It transports
   the unknown fixed-h mean; it is not a saving on that mean.

Fresh exact checks will use n=137,509,911 and d=1,2,5, plus A=191,509,911
for derivative/increment inequalities. They test rational components, not
asymptotic normality. Development used the displayed symbolic coefficients.
The common declared character is `e(Hx)`; covariance means `E[AB]-E[A]E[B]`,
without complex conjugation. No stochastic independence is assumed.

Controls: genuine zero seed; coherent seed -pi/16; normal counterseeds of
read-only #505; unchanged radial Z with angular channel zero; artificial
`Y*=-Z_(n+l0)`; and the same-forcing angular seed shift 1/5. Their source maps
remain distinct. No factorial interaction is inferred from this logical list.
