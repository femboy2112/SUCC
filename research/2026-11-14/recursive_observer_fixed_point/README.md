# The Recursive Observer — Source-Coupled Posterior and Predictive Closure

**Scope:** 2026-11-14 research slice stacked on [SUCC PR #627](https://github.com/femboy2112/SUCC/pull/627). This is a mathematical model of **source-dependent belief recursion, resource-aware probing, retrospective smoothing and finite predictive reference formation**, not a validated physical theory or new set-theoretic AoC proof.

Start with [THEOREMS.md](THEOREMS.md): RFO-01–09, proof assumptions, source-map obstructions, distinct dynamical and invariant-space fixed points, and exact countermodels.

Run focused code using the repository root:

```sh
PYTHONPATH=. python -m unittest discover -s tests -p 'test_recursive_observer.py' -v
PYTHONPATH=. python research/2026-11-14/recursive_observer_fixed_point/independent_oracle.py
python research/2026-11-14/recursive_observer_fixed_point/independent_symbolic.py
```

**Implemented:** `observational_succ/recursive_observer.py` retains original and current source state in a joint rational belief; checks independently sourced joint transition/output kernels; rejects zero-probability records; proves/implements exact finite budget optimization with source-dependent resource meter; certifies conditional contraction; constructs finite predictive-observability span; and uses that span for finite model comparison. `tests/test_recursive_observer.py` contains the hostility suite; independent oracles enumerate entire hidden histories and derive exact symbolic fixed-point equations.

**Critical types:** (i) a source stochastic law is a hypothesis, not inferred from possibility supports; (ii) the observed outcome may depend on the pre-transition source even after destructive source mutation; (iii) physical cost calibration is separate from probability; (iv) dynamic Bayesian filtering does not require a time-independent equivariant posterior section; (v) recursive belief convergence is not guaranteed; (vi) predictive equivalence is relative to a **common lawful action/output/cost contract**, not source identity.

**Required future work:** validate GitHub CI at the actual head, run full SUCC-mandated validation in a full checkout, commission an adversarial independent mathematical review, attempt Lean formalization of predictive-span finite stabilization and source-dependent Bayes update, and design source-specific predeclared holdouts.
