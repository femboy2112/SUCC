# Execution validation and source boundaries

**Date:** 2026-11-14. **Local runtime:** isolated container Python 3 standard library `Fraction`, `unittest`, seeded `random`.

## Actual commands executed

```shell
PYTHONPATH=. python -m unittest discover -s tests -p 'test_*.py' -v
PYTHONPATH=. python research/2026-11-14/gauge_anchored_source/independent_oracle.py
python -m compileall -q observational_succ tests research/2026-11-14/gauge_anchored_source/independent_oracle.py
```

- 17/17 focused exact-rational tests pass, with source/anchor/cost and Bayesian negative controls.
- 150 seeded rational priors plus four point masses checked posterior/quotient commutation against source J; the independent oracle separately enumerated 1,248 rational prior/outcome comparisons using a closed-form source law.
- Compileall passed.
- 2-bit gauge carrier full source orbit set: `((0,3),(1,2))`; external absolute pin gives source-report gauge mismatch; co-moving anchor and relational target have exact equivariance/invariance.
- Three-bit hidden-source mutant demonstrates gauge-invariant current observation does **not** force future predictive closure.
- Raw absolute-bit sensor and absolute-reset mutant deliberately fail covariance checks; correct source likelihood quotient rejects gauge-breaking source readout.

**Certification boundary:** these are exact tests of a declared mathematical source/likelihood. The code has not run against external hardware sensors, and no empirical physical symmetry or energy calibration has been authenticated. No new Lean kernel theorem, full SUCC root validation or external blind review is claimed.
