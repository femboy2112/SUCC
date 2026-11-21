# Reflection–Haar source-filter validation — scoped executed receipt

Date: 2026-11-20. Tooling: Python 3.13, standard library, independent SymPy/mpmath (versions captured by runtime if desired). Source fixed: Main XXVI BBP pole vector `(4,−2,−1,−1)`, zero seed `U0=0`. No source replacement.

## Executed local checks

- `python -m compileall -q source_reflection_haar.py test_source_reflection_haar.py independent_sympy_audit.py`: **PASS**.
- `PYTHONPATH=. python -m unittest discover -s . -p 'test_*.py' -v`: **21/21 PASS** (exact `Fraction` algebra, 160 eight-step impulse relations, 150 rational H-filter recurrence checks, 121 unitary synthetic phase settings, perfect factor port separation, calibrated phase-flip control, root indices, invalid domains, source-scope labels).
- `python independent_sympy_audit.py`: **PASS**, **165 scoped independent assertions** (64 exact Taylor coefficient checks; 48 BBP forcing clock checks; exact original polynomial, reciprocal & cyclotomic identities, algebra projector and 11/5 matrix determinant checks; 4 high-precision two-path settings at 85 decimal-digit precision; 4 independent numerical winding computations; matched-jet mutant reciprocal failure and root-radius diagnostic). See `independent_audit_receipt.json` and `independent_audit.log`.
- The matched-first-jet mutant has numeric root moduli approx `(1.297594,1.297594,1.723242,1.723242)` and exactly fails the necessary equal-radius coefficient condition `9=20`; these numerical root radii are diagnostics rather than the proof.
- Checked all relative Markdown links, compiled source scripts, parsed JSON receipt, hashed all packaged files, and verified remote Git blob SHA-1 against exact local bytes after commit. See `sha256_manifest.txt` and raw logs for scoped reproducibility.

## Boundaries

These are source-filter **paper derivations** with executable algebraic controls. No physical two-slit or mirror experiment was performed. Equal incident path amplitudes, coherent common receiver, fixed reference phase and specified wavenumber are experimental premises. The circle zeros are zeros of the Mellin complementary mask `H`, not a demonstrated phase-space orbit for BBP digits. The auxiliary `1/H` impulse is not the BBP radix-digit evolution. The Toeplitz winding uses an analytic symbol chosen from `Q`, not an energy or real-phase normality operator.

**Not run / claimed:** repository-wide >14k tests, root provenance/foundations/ordinal gates, hosted CI, Lean, independent referee, all-B π real-phase signed estimates, R0, base-16 π normality or RH. Source-evaluator M/5/11 correspondence remains explicitly auxiliary.

## Reproduce

```sh
cd research/2026-11-20/bbp_reflected_haar_seam
python -m unittest discover -s . -p 'test_*.py' -v
python independent_sympy_audit.py
python -m compileall -q source_reflection_haar.py test_source_reflection_haar.py independent_sympy_audit.py
```
