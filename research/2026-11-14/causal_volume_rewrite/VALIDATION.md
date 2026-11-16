# Validation — Source-typed Causal-Volume Rewrite

**2026-11-14.** Working directory: an isolated, additive Python 3.13.5 scaffold with standard-library `Fraction` source checks and an independent SymPy 1.14.0 / mpmath 1.3.0 verifier. It does not contain SUCC's complete checked-out native source tree, so full-root gates are **NOT CLAIMED**.

## Commands actually executed

```sh
PYTHONPATH=. python -m unittest discover -s tests -p 'test_causal_volume_rewrite.py' -v
python research/2026-11-14/causal_volume_rewrite/independent_sympy_oracle.py
python -m compileall -q observational_succ/causal_volume_rewrite.py tests/test_causal_volume_rewrite.py research/2026-11-14/causal_volume_rewrite/independent_sympy_oracle.py
```

- **29/29 focused unittest methods PASSED** (raw `receipts/focused_unittest.log`). They include 128 original four-pole moments, two-register Oily resolvent/finite-grade source checks, 180 seeded rational polynomial-gcd cases, 38 polynomial volume identities, 112 exact origin/successor checks, source-certified Green intervals, 126 positive causal-face differences, additional continuous-volume difference enclosures, exact Gamma endpoint orders, genuine lift/carry, the rational nonnormal source mutant and degree-`8M+1` finite-horizon positive source mutations.
- **Independent SymPy oracle PASSED** (raw `receipts/independent_oracle.log`): exact factorization and residue moments; 15 independent finite volume/successor identities; 42 independently integrated `(-Δ)^k r` terms; 12 moments of the rational nonnormal source; synthetic finite-jet mutant via 9th derivative and real-beta integration.
- **15 high-precision moving-Mellin comparisons PASSED**, checking ratio `M(m(1+iλ))/M(m)` against `(1+iλ)^(-2)` and the rigorous source error bound at `m=32,64,128`, `λ=0,1/8,1/2,1,2`, with mpmath 60-digit quadrature. This is numerical corroboration of an analytic inequality, not a finite proof of an asymptotic statement. A further **12** mpmath comparisons for k=1,2,3 verify the qualitative Gamma(k+2) face limit at two increasing source depths (again, not a finite proof).
- `compileall` of all three Python files PASSED.

## Proof authority

- **Classical/elementary paper derivation:** finite BBP source moment identities, polynomial gcd equality, source-lift recurrence, Gamma endpoint via Laplace rescaling, Hausdorff moment differences and log-convexity. These are analytic assertions with written proofs, not merely tested formulas.
- **New-to-project rational inequality (paper proof + independent numeric controls):** moving complex Mellin phase estimate `(14+12|λ|)/m + 2m² 2^(-m)` for `m>=14`. The constants follow from the original source bounds `R(1−δ)=δ/[1+2δ+2δ³−δ⁴]`, `B1−2B2<=I_m<=B1`, `I_m>=1/(2m²)` and an explicit logarithmic-phase split at `Y=m/2`.
- **Source/observer firewall:** a positive zero-anchored *different* polynomial source has Gamma(2) but rational completion 1/2; the finite-jet mutant matches the completed π value and finitely many Green moments but changes later forcing. These falsify generic conclusions across enlarged source grammars; neither is an alternative admissible *original four-pole source*.
- **Not established:** a positivity-to-normality implication, a canonical Gamma/Oily probability law for the actual deterministic BBP carries, a source-preserving Mellin-to-chronological phase intertwiner, R0, π normality, RH, new physical gauge symmetry or academic priority.

## Required whole-repository gates NOT RUN in this scaffold

```sh
python scripts/verify_provenance.py
python -m unittest discover -s tests -p 'test_*.py'
python scripts/observer_foundations_probe.py
python scripts/ordinal_succ_report_probe.py
```

Check hosted CI at the **new exact GitHub head** before claiming these gates. No Lean proof for the new CV claims is represented by these Python tests. This additive branch intentionally does not modify frozen source, `U_0=0`, imports, workflows, archival claims or main.
