# Validation report — Zak–Jackson source-to-band bridge

**Inputs:** Main XVIII base `4eb411e3730a9e7b95480369a438b89d9a433a4b`, parent PR #438 head `6a23d0735f30c68200a93ff4725c54c0cc8b5975`. Additional sibling original-source PR #437 read and cited, not copied. New files are research-only additive; original four BBP signed poles, selected U0=0, all production, Lean, workflows and historical claim authorities unchanged.

## Actually executed local checks

From a local research package that includes the **unchanged uploaded parent PR #438 zip** as well as this new package, run:

    python -m unittest discover -s tests -p 'test_*.py' -q

Observed **51 tests PASS**, zero errors, zero failures. This is **30 new** exact Fraction/integer tests and **21 inherited parent** tests in the same standard-library process. The inherited parent tests are shared provenance and are not independent external witness. Parent helper modules and new helper use unique importlib names and avoid global `independent_oracle` collision.

New exact testing covers all four original poles against an independently combined rational source, rational noninteger source inputs, strict positive/decreasing forcing, selected zero-seeded recursion and Green telescope, nested tail intervals, normalized fourth-power Dirichlet coefficients, four-tuple independent 65,536 path enumeration, exact nonnegative flat-top weight bounds/support/plateau, all ideal ladder transfer shapes, explicit rational constants for the `<99|h|` analytic theorem, coherent high-alias conditional lower bound, periodic horizontal finite-energy selector algebra, and Beta eight-jet source-fake mutation controls, plus deliberately wrong frequency-rectangle and fourth-power coefficients that fail exact recovery, and independent exact stationary-gap/pair-shear/geometric-sum constants behind the continuous-slice energy theorem. Invalid domains and coefficient-budget errors fail closed.

The analytic universal constant and oscillatory-integral estimate are **paper proved** from declared standard lemmas and original P(t); no numeric experiment, unit test or special case is called a universal theorem.

## Secondary optional numerical diagnostic — not proof

`finite_probe.py` uses numpy midpoint quadrature and samples the original source-integral via convergent 16^-j four-pole tail. Executed:

    python research/2026-10-31/zak_jackson_band/finite_probe.py --points 65536

The output file `NUMERICAL_DIAGNOSTIC.json` includes 2× grid resolution comparison on M=1,N=3 and M=2,N=4, PLUS continuous-slice source cross-correlations at N=2,3, at q=pi/16 (approximate) and changed q=1/5. It shows finite band/prefix differences around 10^-7 and 10^-12, respectively, **without certified floating-point error enclosures**. No extrapolation to M→infty or the original signed Weyl gate is warranted; the analytic proof stands without these numbers.

## NOT RUN / NOT CLAIMED LOCALLY

- Complete SUCC 10k+ full root unittest tree (unavailable as full checkout; sandbox network git clone cannot resolve github.com).
- `scripts/verify_provenance.py`, `scripts/observer_foundations_probe.py`, `scripts/ordinal_succ_report_probe.py` on the entire original repo checkout.
- Lean kernel formalization of the new paper arguments, an independent academic referee, certified numeric oscillatory intervals or any π normality / RH proof.
- Exact-head hosted CI until it has run and its status has been inspected separately.

**Reproducer:** Standalone new focused tests:

    python -m unittest discover -s tests -p 'test_zak_jackson_band.py' -v

For full repo, use AGENTS.md mandated commands. Report exact SHA, branch base, test receipt, source signatures and any failing cases before integration. DO NOT merge automatically.
