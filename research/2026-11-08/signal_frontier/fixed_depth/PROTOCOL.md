# Fixed-depth calibration protocol

Parent: `86327467191420d2157eeae5f4cfa1c2c62810da`. Proof baseline remains
`d32342d375f44ddf62221ad6aff2f534abdc0a03`. This note was written after the
symbolic calibration derivation and before executing the oracle. It is not
an independently timestamped preregistration of the derivation.

Hypotheses to distinguish:

1. Uniformly rotated finite-resolution projections preserve the original
   signed response with a known sinc-squared multiplier, up to local-marginal
   discrepancy. No new complement regularity is required.
2. A single fixed origin has the same multiplier. A finite weighted example
   must refute this stronger assertion.
3. Vanishing local discrepancy itself makes the retained response small.
   The complement conjugate to the local character must refute this.
4. Vanishing error at each finite depth proves arbitrary moving-depth
   conclusions. The proof must exhibit a uniform bound or refuse the exchange.

Exact oracle: use rational coordinates/weights, Gaussian-rational values,
and a direct enumeration of every origin interval. Compare partition-based
conditional products against a separately implemented pair-kernel sum.
On uniform rational grids, use formal rational root-of-unity polynomials,
not trigonometric floating point, to compare the origin average to the exact
finite-grid Dirichlet multiplier. Include nontrivial complex complements,
nonuniform weights, repeated positions, empty cells, M=1, and M>N.

No finite output proves the analytic inequality, all-epoch source cancellation,
or pi normality. The paper supplies the general proofs. The root's independent
source sweep supplies finite original-source observations separately.
