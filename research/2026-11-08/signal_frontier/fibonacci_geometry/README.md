# Fibonacci geometry observer

[FG1–6](THEOREMS.md) construct an integer-clock calibration observer with
explicit circle, orientation, source-anchor and noise assumptions. Three
oriented readings recover the unknown center, gain, return phase and curvature.
Fibonacci return phases compose exactly across resolutions, and an anchored
curvature vector is invariant after its declared phase transport.

The observer retains history through the existing SUCC finite belief APIs.
It is not a new category implementation. Integer clock positions alone cannot
identify radius; distances alone cannot identify orientation. The source clock
and calibration clock remain distinct.

For blind calibration at return chord t, coordinate noise epsilon costs
O(epsilon/(R t²)). If the return phase was already calibrated, two readings
cost only O(epsilon/(R t)). This distinguishes learning an unknown geometry
from reusing historical phase knowledge. Both statements have explicit
constants and hypotheses in FG5.

Executed: 7 unit tests; 1,396 exact finite checks; 7 preregistered actual-golden
numerical cases. Exact arithmetic uses independent rational circle models and
Q(alpha) return identities. Actual-golden checks use 100-digit arithmetic and
an independent Cartesian circumcenter algorithm; they are not interval proof
certificates. The parent formal file verifies only integer recurrence algebra.

Reproduce from repository root:

```sh
python -m unittest discover -s research/2026-11-08/signal_frontier/fibonacci_geometry -p 'test_*.py' -v
python research/2026-11-08/signal_frontier/fibonacci_geometry/oracle.py --output /tmp/fibonacci-geometry-exact.json
python research/2026-11-08/signal_frontier/fibonacci_geometry/numerical.py --output /tmp/fibonacci-geometry-numerical.json
```

The covariance transport bound preserves the signed signal and its error.
It does not make that signal small. The same calibrated circle is available
to the coherent same-forcing wrong seed. **Original-zero signed covariance,
pi base-16 normality and RH remain OPEN.**
