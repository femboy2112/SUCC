# Independent numerical check of actual coupled maxima

At frozen native implementation head
`8755bc7bade06d6a0893d0b7ece080e79a05072b`, the separate diagnostic
`numeric_referee.py` read the coordinator's exact receipt and independently
computed original/lag-one unweighted samples for `(A,h)=(256,7),(512,-3)`.

It constructs the source from the literal eight-slot original and radial
taps on a fixed integer common denominator. It does not import the main
instrument, its character evaluator, or its maximal-chord routine. It uses
mpmath exponentials at 80 and 110 decimal digits, real/imaginary `fsum`
for the epoch mean, and a monotone-chain convex hull of prefix sums followed
by hull-vertex diameter search for the maximum. This differs from the
coordinator's rational character enclosure and exhaustive integer-chord path.

All four numerical maximal values lie within their exact `M_interval`;
all four complex means lie within their declared complex error of the
rational grid center. Every maximizing interval matches the receipt exactly.
The 80-versus-110-digit differences are below `1e-70`. Raw values, witnesses,
precision differences and the inspected receipt hash are retained in
`NUMERIC_REVIEW.json`.

Command, exit zero:

```
python research/2026-11-04/zero_frame_coupling/front_cf/numeric_referee.py \
  > research/2026-11-04/zero_frame_coupling/front_cf/NUMERIC_REVIEW.json
```

This is **numerical corroboration only**. Repeated high precision and a
numerical convex hull are not rigorous enclosure algorithms. The exact
certificate's authority remains its independent rational error proof. This
review modifies neither the main instrument nor any native test or package
file, and does not claim a completed full-native or hosted CI result.
