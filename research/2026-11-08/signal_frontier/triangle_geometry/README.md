# Golden triangles retaining the original positive source

Pi base-16 normality: OPEN. RH: OPEN.

[GT1–7](THEOREMS.md) construct a decorated prefix functor: binary histories
become nested golden arcs, while their authentic measure-valued BBP
posteriors and source marks are retained. Every finite frontier has exact
integer-clock addresses after one declared common phase shift. The triangle
chord defect and area have the user's exact formulas and asymptotic alpha³
refinement ratio; Farey ideal triangles use the distinct Cayley boundary map
and hyperbolic metric.

The strongest source-map result is an exponential finite separation:
for the native Pascal row a=8m-7, m>=2, put p*=alpha² and t=ceil(mp*/2).
Its total variation distance from the geometric arc-length grade law is at least

    1 - 2^(t-1)(1-p*/2)^m - (2/3)^t R(4m-7)/R(8m-7).

The two error terms decay exponentially; the R ratio tends4. At the held-out
m=257, the exact bound is approximately0.99999999245 and the exact distance
approximately0.9999999999997584. These decimals only display exact Q(alpha)
certificates. Source posterior mass and geometric length are demonstrably
different, even though the same history tree supports both.

For a fixed prior across depths, the infinite arc law has Lebesgue component
exactly mu({-log(alpha)/8}) times arc length. The authentic continuous
positive BBP prior therefore gives a singular arc law. Its address history
still learns the retained latent X almost surely. The changing native
priors do not form that infinite projective law: the native result above
is a separate finite-row theorem. None of these auxiliary probability
laws is the deterministic BBP digit orbit.

Executed:7 focused tests;8184 exact arc checks;8184 exact integer-clock
checks;165 independent source-grade comparisons;1533 posterior refinements;
132 Farey checks;12 nonvacuous exact TV-bound checks;12 geometric100-digit
corroborations. [Validation commands and exits](VALIDATION.json),
[exact receipt](EXACT_RECEIPT.json), [numerical receipt](NUMERICAL_RECEIPT.json).

Reproduce:

```sh
python -m unittest discover -s research/2026-11-08/signal_frontier/triangle_geometry -p 'test_*.py' -v
python research/2026-11-08/signal_frontier/triangle_geometry/oracle.py --output /tmp/triangle-geometry-exact.json
python research/2026-11-08/signal_frontier/triangle_geometry/oracle.py --numerical --output /tmp/triangle-geometry-numerical.json
```

The exact oracle uses finite differences of source Laplace moments,
independently compared with the existing binomial-expansion implementation.
Arc endpoints are also compared with a closed address sum. Chord and area
checks use independent Cartesian distances/determinants and do not certify
infinite claims. The paper proves the universal bounds; no new Lean or
external scholarly review is claimed in this subfront.

Audit history: a diagnostic conversion of large Q(alpha) coefficients at
ambient15-digit precision suffered cancellation. Exact sign/TV checks were
unaffected. The display helper now allocates local guarded precision, with a
regression confirming that it preserves ambient precision. The final full
oracle and tests were rerun successfully. The later GT10b/c native bounds
were analytically derived and tested on the already declared finite epochs;
the exponential-bound checks reuse those measurements and are not claimed
as an additional independent holdout. The protocol is a local preregistration,
not a separate Git timestamp.
