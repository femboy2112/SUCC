# Validation — Recursive Observer Source Coupling and Predictive Fixed Point

**Current research slice:** 2026-11-14, appended only to the draft SUCC #627 ancestry. This is a standalone scaffold because a complete local clone of SUCC was unavailable; upstream source and AGENTS.md were inspected using the GitHub connector. Full repository tests and external physical source authentication must not be claimed.

## Actually executed commands

- Python **3.13.5**, standard-library `fractions.Fraction` for core, all exact rational operations.
- `PYTHONPATH=. python -m unittest discover -s tests -p test_recursive_observer.py -v` — **31 methods PASSED**; exact output in `receipts/focused_tests.log`.
- `PYTHONPATH=. python research/2026-11-14/recursive_observer_fixed_point/independent_oracle.py` — **PASS**; independent raw **5,950 source-path trace** comparisons, **70** unmetered Bayesian budget comparisons, **70** metered budget comparisons, **882** 2-state filter-pair contraction tests, and **300** 3-state predictive-equivalence pair comparisons with direct enumeration of *all* length≤2 action–outcome words (two actions, two outcomes). Raw output in `receipts/independent_oracle.log`.
- `python research/2026-11-14/recursive_observer_fixed_point/independent_symbolic.py` — **PASS** with **SymPy 1.14.0**; rederived exact normalized 2-state maps, repeated-observation fixed root `(sqrt(41)-5)/2`, alternating 2-cycle root `sqrt(19)-4`, exact derivatives and algebraic non-coincident fixed-point countermodel. Log in `receipts/independent_symbolic.log`.
- `python -m compileall -q ...` for the four new Python sources — **PASS**.

## Boundaries and hostile controls

1. Source-tied joint outcome law vs an invalid post-state-only factorization on destructive reset.
2. Zero-likelihood observation returns `None`, not an invented posterior.
3. Original/current state pairs survive destructive resets; the full history still requires additional registers.
4. Source priors affect posterior, even when source table is unchanged.
5. Different costs (and separately declared source-conditioned cost meters) produce distinct optimal legal policies with identical source dynamics.
6. Repeated observation has unique conditional posterior fixed point; alternating outcomes produce a nontrivial 2-cycle.
7. Same posterior fixed point is NOT a certificate of equal next-observation laws; independent Brier scoring yields an exact nonzero expected penalty on the wrong model.
8. Distinct source histories can have identical present-state and future-report law; a fixed backward stochastic section is not required for a history-conditioned posterior.
9. The invariant predictive-span fixed point distinguishes all valid future finite outputs within at most n−1 rounds; exact three-state delayed difference reaches the bound.
10. Independent oracle uses whole-path enumeration and unnormalized raw-mass policy values, not the production filter recursion or normalized Bellman update. **It shares the same declared synthetic source family**, so is not an independent empirical measurement.

## Declared proof authority

- **Paper-proved classical under hypotheses:** RFO-01–08, RFO-10 as in `THEOREMS.md`, with explicit counterexamples limiting RFO-05/06/07/08. These are new-to-SUCC formulations of known finite Bayesian filtering/POMDP/linear realization/fixed-point methods; no scholarly-priority claim.
- **Locally observed once:** executable test and independent oracle receipts listed above. Source is synthetic, so source-map adequacy for the real physical carrier remains **UNVERIFIED**.
- **Never run locally in this slice:** repository-wide `python scripts/verify_provenance.py`; full root unittest suite; `python scripts/observer_foundations_probe.py`; `python scripts/ordinal_succ_report_probe.py`; Lean; external adversarial peer review. After GitHub push, inspect exact head CI separately before claiming final matrix results.

The added project files are disjoint from parent #627's changed paths. Existing source archives, production defaults and `main` remain unmodified. The addendum is a **draft research PR**, not a merge/release/publish action.
