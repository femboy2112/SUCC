# Pascal triangle circle observer

The paper proves a source-preserving posterior-valued circle update, the
triangle's barycentric inverse, and a sharp reduction in coherent measurements:
**ceil(m/2) complex harmonics**, plus known total mass, recover arbitrary real
weights on m+1 distinct circle nodes. A target needs only the real row span
that represents it. Exact invertibility is separate from noise conditioning.

The source history is retained. Two explicit positive priors have identical
triangle masses and different next posterior predictions, showing why an
unknown prior cannot be replaced by those masses. A known authentic prior
still has the inherited grade-sufficiency property.

The original auxiliary source has two different circle-law limits: fixed a
and increasing sensor depth gives Haar, while the native a=8m−7 clock gives
nonzero harmonic limit(2-e(h alpha))^-2. This is a rigorous clock distinction,
not selected BBP time cancellation. The explicit fixed-a envelope in TP8
retains its a- and h-dependent constants. Pi normality and RH remain OPEN.

Validation completed:

- Seven focused tests pass.
- Exact independent Gaussian-rational/polynomial oracle:2650 checks, including
  13 rank/reconstruction cases,12 positive aliases,455 original source masses,
  520 posterior updates,1533 enumerated path contributions,100 canonical
  source-forcing checks and4 posterior-counterexample identities.
-100-digit numerical corroboration:5 actual golden-node reconstructions,
  24 fixed/native source-clock characters and4 independent continuous-source
  quadratures (25 asserted numerical checks). The m=9,12 reconstruction
  holdouts were declared before execution. No interval authority is claimed
  for these numerical observations. Global mpmath precision is preserved.

At m=64,h=1 the fixed-a8 character magnitude is about0.02343, within its
proved0.05791 envelope. The native character is about0.12305, approaching
its derived nonzero limit magnitude0.12579. These finite values illustrate
the paper theorem; no exponent was fitted and no normality inference made.

Reproduce from repository root:

```
python -m unittest discover -s research/2026-11-08/signal_frontier/triangle_posterior -p 'test_*.py'
python research/2026-11-08/signal_frontier/triangle_posterior/oracle.py --output /tmp/triangle-posterior-exact.json
python research/2026-11-08/signal_frontier/triangle_posterior/numerical.py --output /tmp/triangle-posterior-numerical.json
```

Root coordinates native required gates, independent review, commits and the
final artifact manifest. This front introduces no new category classes,
changes no source/production files, and claims no Lean certificate, external
referee approval or worldwide novelty. See THEOREMS.md for exact domains,
quantifiers, maps, proofs and the source-covariance gap.
