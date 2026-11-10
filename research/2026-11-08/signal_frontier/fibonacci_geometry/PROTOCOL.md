# Fibonacci circle geometry: protocol before oracle execution

Scope: integer calibration clock; complete oriented complex coordinate readings;
unknown fixed translation and nonzero complex gain; inherited original BBP
signature is retained separately. Calibration clock and source time are distinct.
No new category implementation. Finite belief experiments use SUCC's existing
FiniteCarrier, Instrument and BeliefGame.

Exact checks: Fibonacci return algebra in Q(alpha), alpha²+alpha=1; rational
circle rotations for blind three-point recovery; Euclidean similarity and
reflection controls; cross-resolution curvature transport; adversarial finite
noise at the proved budget; a finite causal belief game that loses its physical
state after calibration while the transcript identifies the source candidate.

Numerical checks, explicitly not certificates: actual golden rotations at
k=2,3,5,8,13,21,34 and independently generated circle coordinates. Test exact
reconstruction, return phase, curvature bias and fixed precision deterioration.
Use mpmath workdps, never global precision mutation. No fitted asymptotic rate.

A complete oriented calibration can recover a circle and its chosen source
phase reference. Integer times alone cannot determine radius/center; distances
alone cannot determine orientation; source-independent calibration cannot prove
original-zero signed covariance decay. These failures must carry explicit
controls rather than narrative assertions.

Golden numerical noise scale is fixed at epsilon=10^-12 before execution;
100-digit arithmetic isolates input-noise sensitivity from machine-rounding.
Noise-free reconstruction uses an independent Cartesian circumcenter algorithm.
The blind three-point precision budget is distinguished from the cheaper
case where the actuator's return phase is already known exactly.
