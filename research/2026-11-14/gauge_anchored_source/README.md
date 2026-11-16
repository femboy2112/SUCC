# Target-relative gauge anchors for Principia Observatoris

Research continuation of draft SUCC PR #629. This round replaces the idea that the observer must pick an **external** absolute instrument as its primary mathematical reference. The better conditional mathematical reference is an **internal, problem-relative covariant pin** `r(gx)=g r(x)` whose comparisons are gauge invariant.

Start with [THEOREMS.md](THEOREMS.md), then [VALIDATION.md](VALIDATION.md). Exact module: `observational_succ/gauge_anchored_observer.py`; tests: `tests/test_gauge_anchored_observer.py`; independent check: `independent_oracle.py`.

The key result is an exact commuting triangle: source-level joint observations and Bayesian filtering pass through the quotient by **actual gauge symmetries** when source action, likelihood and output representation respect the symmetry. This can avoid solving unobservable absolute coordinates and can prevent false source-identification claims. Internal covariance alone is **not** source adequacy, target sufficiency or a physical measurement.

All construction is a declared finite model. No main merge, archived source rewrite, full-root tests or hardware measurements claimed.
