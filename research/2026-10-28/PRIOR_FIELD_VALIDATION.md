# Prior Field × Causal Inflation — local validation record

Date: October 28, 2026. Parent source `f10632ee4c922c95256f80245284c752162dbe2d`. No modifications to original source or Main XIII are proposed.

- Exact standalone Python tests: `PYTHONPATH=. python -m unittest discover -s tests -p 'test_*.py'`: 63 tests collected, 59 passed, 4 **expected** full-checkout source bridge skips (in locally isolated directory). Four skips are not pass claims.
- Staged regression against available local Hopf/Pisot/Wavefront overlay: `PYTHONPATH=. python -m unittest discover -s tests -p 'test_*.py'`: **188 collected, 185 passed, 3 expected full-checkout source import skips**, including **4/4 source bridges against the locally available Main XIII/PR344-equivalent source**. This is NOT the entire live repository.
- Independent SymPy oracle: source resolvent, original four signed BBP poles, exact Jordan powers, chiral source rank-four eight-clock scaling, FLRW null conformal integral, 20 Haar Fourier integrals and the source-derived two-bit sensor no-go and exact nonlinear Bayes magnetization recursion and Pisot Lucas trace algebra: PASS.
- High precision mpmath oracle: source-specific Bayesian likelihood, limiting directional KL trends on original L(x) for m=8,16,32,64,128,256: PASS (numerical consistency only; proof via endpoint Laplace asymptotics in dossier).
- Exact deterministic receipt: all exact fraction identities and finite Bayes accuracy controls written to `INFLATION_PRIOR_EXACT_RECEIPT.json`.
- **Not run/claimed here:** Main XIII whole native test suite, `verify_provenance.py`, observer/ordinal probes, Lean kernel, hosted CI, primary mathematical peer review or empirical cosmology data testing. These remain merge gates.
- **π normality and RH remain OPEN.** A Haar prior produces ensemble cancellation but selected original U0=0 Weyl cancellation is not established.

Execution:

```sh
PYTHONPATH=. python -m unittest discover -s tests -p 'test_*.py'
PYTHONPATH=. python scripts/inflation_prior_exact_probe.py
PYTHONPATH=. python scripts/inflation_prior_sympy_oracle.py
PYTHONPATH=. python scripts/oily_bayesian_inflation_oracle.py
python scripts/verify_provenance.py
python scripts/observer_foundations_probe.py
python scripts/ordinal_succ_report_probe.py
```

The last three commands are *required eventual main-repo validation*; do not misinterpret their listing as proof they were executed in the isolated local context.
