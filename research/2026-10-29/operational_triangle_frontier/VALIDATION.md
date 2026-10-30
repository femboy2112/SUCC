# Operation Triangle Genesis — local exact and independent validation receipt

**Scope:** draft additive files from parent #386 (`9c85894428e4ca1f8609d9ea1a79af1f51f1551f`); locally authored/tested in a standalone directory. This receipt does NOT claim execution of all root SUCC tests or hosted CI on the remote branch.

## Actual commands and outputs

```sh
python -m unittest -v test_operational_triangle.py
# Ran 10 tests; OK, no failures. Detailed raw log: focused_tests.log.

python independent_oracle.py > oracle_output.json
# All symbolic assertions passed. 18 finite high-precision integrals:
# 3 distinct (z,t) points × 3 native n values × original/fake source.
# Full output and scaled residuals in oracle_output.json.

python -m compileall -q operational_triangle.py test_operational_triangle.py independent_oracle.py
# exit 0.
```

Focused exact Fraction checks cover original four-pole forcing and positive values; **independently enumerated** ordered word polynomials, grade aggregation and posterior update; two exact routes to the complete joint source/Laplace generating polynomial for three `a`, six depth values, four `z` and three `t` values; posterior mixture reconstruction and strictly positive memory/projection witnesses; harmonic source/path/digamma triple identity; correct exact carry and seed-frequency labels; joint original/fake 59-jet polynomial equality for 16 rational `(z,t)` combinations; and a concrete order-dependent latent A/B countermodel refuting universal grade sufficiency.

The independent oracle imports **neither** the module nor the unit-test reference implementation: SymPy derives the joint correction from separate Gamma moments and checks the explicit polynomial, `z=0` correction `-151/960`, harmonic source first-jet difference `59/320`, and the original/fake decomposition. The numerical branch separately integrates the original four-exponential `Q(y/a)` and the Gamma fake at 75 decimal places. Observed first-order scaled residuals (`n[F_n-F_infty]-J`) shrink as n increases at all tested points; the raw numbers, not merely the verdict, are preserved.

**Numerical holdouts are not interval/proof certificates.** The all-n joint asymptotic and uniform O_T(n^-2) estimate have a mathematical Taylor/dominated-tail derivation in THEOREMS.md; an externally independent full analytic remainder audit is still required before publication/claim promotion. The derivation is not claimed Lean-checked.

## Known failure modes deliberately kept

- Replacing retained `X` with independent restart uses `R(a+8)^2/R(a)^2` instead of `R(a+16)/R(a)` for two failures; difference strictly positive.
- Projecting grade to parity at depth 2 merges distinct conditional source posteriors.
- A non-exchangeable latent sensor has posterior(A|LR)=3/4 versus posterior(A|RL)=1/4, both grade 1; don't universalize sufficient-statistic claim.
- Gamma-matched fake `Q_fake=15x` retains the limiting Gamma–Poisson law but has a different `1/n` joint jet; cubic source perturbation `Q_epsilon=Q+epsilon(1-e^-x)^3` retains the first two source jets and cannot be excluded by FIRST-order source data alone.
- Original selected phase observer under seed-smearing has zero integral for **every** seed. The coherent same-forcing `s=-pi/16` has selected Weyl mean →1; this disproves inferential passage from virtual-seed cancellation to π normality.
- A grade Fourier coefficient divided by tiny `q_j` can amplify measurement error; positive tomography/normality-complete equivalence is not a signed estimate.

## Mandatory checks NOT executed on this research branch

These require a complete checkout/installed dependencies and should be run on the eventual exact integration commit:

```sh
python scripts/verify_provenance.py
python -m unittest discover -s tests -p 'test_*.py'
python scripts/observer_foundations_probe.py
python scripts/ordinal_succ_report_probe.py
```

Also not performed: full 9k+ root test suite, Math Memory build/check, hosted exact-head CI, Lean proof build, independent external peer review, direct finite precision interval certificate of all-n asymptotic, or any π-normality/RH proof. See `INTEGRATION_HANDOFF.md` for exact branch and truth-status integration gates. Historical archives and original source were not edited.
