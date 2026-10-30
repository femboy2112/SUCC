# Validation — original source Kepler III

**Exact local code:** `selected_phase_probe.py`. **Independent oracle:** `independent_oracle.py`. Python stdlib Fraction for all theorem-critical finite values; SymPy and mpmath only for separately labelled independent symbolic / numerical cross-checks.

- Locally executed 16 exact-Fraction unittest methods: all PASS. The first version failed two test assertions (forgot the L=0 sure-event case and a missing assertEqual argument); both repaired before complete 11/11 re-run. Later added five more tests for sharpness, pure-digit zero blocks, adversarial nested beta and hard-core source relation; 16/16 final PASS.
- Independent oracle: original source factorization, Gamma2 endpoint coefficient `15/64`, six zero-word posterior thresholds, five two-event Haar interval overlaps, nine complex signed-current quadratures, original neutral pi finite history with 160-digit mpmath comparison: PASS.
- The independent oracle's initial exact hard-core assertion was too strong for truncated *midpoint* approximations of irrational Green tails; one overlap was ~3.8e-69 instead of exactly zero because truncated midpoints lose the exact Green transport identity. Corrected the oracle to enclose this numerical truncation effect using its rigorous rational tail bounds, then independently re-ran successfully. The mathematical all-time zero-overlap is a source identity, not a floating midpoint identity.
- Exact rational nested-cylinder construction: 160 selected corrections under a single alternative final beta interval; all source interval memberships certified at the tested horizons. This finite test does NOT prove the infinite constructed seed's asymptotic count; the nested-compact interval proof and Stolz-Cesaro comparison supply universal authority.
- No claim of native full SUCC root suite, hosted exact-head CI, Lean kernel proof, independent mathematical peer review or pi normality proof. No original source file changed in this research package.

Commands:
```
python selected_phase_probe.py
python independent_oracle.py
```
