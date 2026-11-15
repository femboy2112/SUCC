# Validation authority — PSV causal suspension, Gamma and negative zeta

2026-11-14. The exact source rules are reproduced in standard-library Python and independently in SymPy/mpmath, with written mathematical proofs. These are **not** blind independent physical witnesses, new Lean proof certificates or complete native SUCC checkout checks. SUCC OCG/CV historical theorems and the Sondow analytic-continuation theorem are explicit prior dependencies.

Executed in this research scaffold:

```
PYTHONPATH=. python -m unittest discover -s tests -p 'test_causal_suspension_gamma.py' -v
PYTHONPATH=. python research/2026-11-14/causal_suspension_gamma_zeta/independent_oracle.py
python -m compileall -q observational_succ/causal_suspension_gamma.py tests/test_causal_suspension_gamma.py
```

- **19/19** focused exact tests: finite lcm clocks, forward winding and seam, noninteger CRT phantom, rational projection commutation, Gamma mean/variance/Laplace, finite-frequency convergence, signed distributions and their inverses, finite Pascal annihilation, independent eta recurrence, positive even vanishing, and known zeta negative values.
- **Independent SymPy oracle**: 21 Euler/Hasse-vs-zeta formal derivatives, 10 independent parity checks, 8 Gamma distributional inverses.
- **Independent profinite clock oracle**: 342 finite quotient bonds.
- **Independent mpmath**: 6 trivial-zero derivatives checked via completed reflection and positive zeta values, 5 direct Gamma Fourier integrals checked against the closed formula.
- **Compileall PASS.** Exact rational tests and symbolic statements do not rely on floating point; complex Fourier and high precision checks corroborate, not replace, proofs.

**External/source limits:** No real-world causal instrument, physical Lorentz spacetime, quantum theory, actual cosmological inflation, or additional prime source authenticating BBP to zeta was tested. The mathematical suspension/continuation maps are explicitly introduced and checked; compactness alone is not treated as sufficient for a path. No conclusion about nontrivial zeta zeros or π normality is claimed.

**CI/root gates:** full SUCC `verify_provenance.py`, repository-wide unittest, observer and ordinal gates are not run in the isolated scaffold; GitHub CI at exact final head must be checked separately. Any later adjustments to the branch require a new receipt and SHA verification.
