# Validation, actual rounds, and limits

## Environment and baseline

The live GitHub connector resolved main to `b763ba8ef375fbac221e29e4396989a635a6ef36` and the selected parent PR #349 to `ad19e3794f1d8da4a81418d38a4fc731b7d355c7`, tree `69b41162ba80a7004862c9b7d28b302157ed8043`. Root AGENTS.md, CONTRIBUTING.md, METHOD.md, actual Pisot/source-fiber/PCR proof inputs, and the relevant subtree were inspected before publication. This directory is additive; it does not change production imports, archived sources, zero seeds, workflows or historical claim registries.

The local work was an **isolated research overlay, not a complete repository checkout**. Direct git transport failed with `Could not resolve host: github.com`. Connector reads and Git object publication remained available. Therefore this run did not reproduce the full parent native suite, and it does not inherit a passing status from #349's prior CI.

Environment actually used: Python 3.13.5, SymPy 1.14.0, mpmath 1.3.0. The exact core and unit/mutation tests use only the standard library. The independent oracle imports SymPy/mpmath and never imports prime_pisot.py. No Lean installation, formal theorem export, independent human reviewer, or independent model agent is claimed.

## Round-by-round triangulation

| Round | Distinct route / discriminator | Actual outcome |
|---|---|---|
| 1 | Divisor-path enumeration, integer prime charges, Fraction Laplacians, formal Dirichlet convolution, exact quadratic number field | Initial 26-test run exposed a missing reverse division implementation in Quad; raw failure retained in round1-exact.log |
| 2 | Corrected core plus an independently written symbolic companion/channel/field oracle; analytic proof of local-uniform Euler-log convergence | Exact suite reached 27 passes; the proof identifies summable clock displacement, not Pisot alone, as sufficient |
| 3 | Actual code mutations with paired baseline and restore controls | Four mutations were caught, but the conjugate-sign mutant survived a test sharing the inverse/conjugate implementation; round3-mutation-initial.log records the failed detector |
| 4 | Repair by explicit source-polynomial checks, additional inverse-multiplication check; exact radical collision, positive-cosh and off-line-quartet controls | 28 tests pass; all five mutants rejected; unchanged null control passes; symbolic checks total 45 |
| 5 | Frozen-source replay, four fixed complex evaluation points away from supplied zero locations, different prime cutoffs, orbit-log expansion and labeled Dirichlet trace comparison | 28 tests pass again; five mutants rejected again; 45 symbolic checks replay; numerical observations recorded in oracle.json |

The initial failure and the missed mutant are not erased. The missed mutant is an actual provenance lesson: inverse() calls conjugate(), so comparing them alone allowed a correlated sign error to validate itself. The repaired tests check conjugation against `m-beta`, inverse against `beta-m`, and multiplication against the defining polynomial. A separate radical implementation verifies the 11/29 collision.

## Final local evidence

- `python -m unittest -v test_prime_pisot.py`: **28/28 pass**, no skips; latest raw output in `receipts/round5-frozen-exact.log` (0.099 seconds in the recorded run).
- `python mutation_probe.py`: **5/5 false-model mutations rejected**; positive baseline and restored-state controls pass for each, and an unchanged null control passes. Exact failure traces are in `receipts/mutations.json`.
- `python independent_oracle.py`: **45 exact symbolic checks pass**. These include independent PCR characteristic polynomials for dimensions 1 through 12; determinant/marked-trace identities; exact radical collision; field countermodels; and the finite backward-heat calibration.
- Formal Dirichlet logarithm and Mobius extraction checked through cutoffs 40, 160 and 320; coefficient claims remain consequences of the paper proof, not finite extrapolation.
- Four nonzero-input numerical holdouts: `s=1.5`, `0.5+2i`, `0.5+17i`, `0.75-11i`, with 70 decimal digits and prime cutoffs 100 and 10000. Both Pisot and rational non-Pisot corrections were evaluated. No nontrivial zeta zero coordinates were inputs.
- The independently evaluated repeated-prime-orbit log series (p<=97, k<=320) and Euler-factor log differ by approximately `2.137e-51` at `s=0.5+17i`.
- At s=2, the labeled Dirichlet trace through n=3000 differs from `zeta(2)*C_10000(2)` by approximately `0.0002268014881`, within the separately derived missing-integer and clock-tail estimates.
- `python -m compileall -q prime_pisot.py test_prime_pisot.py mutation_probe.py independent_oracle.py`: successful exit, no output.

**Numerical authority:** mpmath outputs are observations, not interval enclosures. The Euler-log tail bound is a proved inequality for exact mathematical quantities; finite evaluation roundoff was not certified. The paper theorem, not an observed agreement, establishes zero-divisor equality. The scripts contain `rh_proved: false` and `roundoff_certified: false` in the numerical receipt.

## Scope of independence and ablations

All routes were orchestrated by one reasoner. Different implementations and algebraic representations are useful but not blind independent witnesses. The core uses Fraction arithmetic modulo a quadratic polynomial; the oracle uses symbolic matrices/radicals and separate ordinary multivariate series; the analytic proof uses uniform convergence. Neither the tests nor the external source descriptions certify one another automatically.

The complete fake-generator x pair-penalty 2x2 experiment includes every cell. Removing Pisot integrality preserves the analytic zero-divisor theorem for rational clocks; removing source labels creates the exact clock collision; removing source coefficient authentication lets the fake-4 Euler system pass zero matching. No transport-free phase or physical interaction claim is inferred from these contrasts.

## Gates NOT run here

The four required root AGENTS.md commands remain unexecuted for this research overlay:

```sh
python scripts/verify_provenance.py
python -m unittest discover -s tests -p 'test_*.py'
python scripts/observer_foundations_probe.py
python scripts/ordinal_succ_report_probe.py
```

No full native suite, hosted head CI, Lean kernel validation, full source-map audit, or peer review is claimed. Research-local tests do not satisfy the complete integration contract. The package is kept out of production discovery and must remain DRAFT until its integration gates are executed on a full checkout.

## CI and publication discipline

One atomic additive commit is planned, containing `[skip ci]`, followed by one draft PR stacked on the pinned #349 branch. This honors the maintainer's request to avoid repeated expensive CI fan-out. No workflow is disabled or weakened. Skip tokens cover push/pull_request events, not every event, and skipped required checks may remain pending. A final exact-head workflow query is the only authority for observed hosted activity; absence of runs is NOT success. Remote Git blob identities are checked against the local manifest after publication.
