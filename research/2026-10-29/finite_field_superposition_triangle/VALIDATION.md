# Validation — exact local receipts and integration boundary

**Parent pinned:** `e02933591e7b7486376acb9847e00fd01d9ae498` (#383). Research-only additive files under this directory; no original source or seed changes. No direct git checkout was available in this run's local sandbox (network DNS refused `github.com`), so root-only SUCC validation, Lean checks and hosted exact-head CI are NOT claimed.

## Locally executed before upload

- `python -m unittest -v test_finite_source_triangle.py`: **8 methods PASSED**. Tested exact four-pole rational passport; original source endpoint rows through depth 7 at four/five distinct clocks; posterior path-sum conservation; both orderings of a one-success one-failure diamond; independent source-shift recurrence; harmonic sum equality and exact harmonic increments through depth 9; seed-blind positive source; exact rational selected fractional points, all grade/carry marks and composed two-step integer carries for four seeds; finite original/fake numeric first-jet calibration.
- `python independent_first_jet_oracle.py`: **PASS**. Independent SymPy reconstruction of source rational factorization, `Q'(0)=15`, `Q''(0)=-59`, exact rational first-jet generating polynomial, first grade correction `-151/960`, integrated original `-49/320`, fake `+1/32`, difference `-59/320`, golden PGF interior root, and secondary Gamma–Poisson rank contrast. No import of implementation.
- `python -m compileall -q finite_source_triangle.py test_finite_source_triangle.py independent_first_jet_oracle.py`: exit 0.
- Numerical `n=20,40,80,160,320,640` native exact-rational source sums examined at 60-digit precision in an independent notebook, and `n=60,120,240` in unit tests. These finite observations **do not prove** the asymptotic.
- Expected upload-source SHA-256: `finite_source_triangle.py` `998ff36a2c4cecd2227f8200747e883721c11b6cab9a48d564c3e70dfa8b156e`; `test_finite_source_triangle.py` `6d5c2dfb1a7be209484ba135d99e194e06d4c3fe9848c2874d617488a4c7b286`; `independent_first_jet_oracle.py` `d2d783847676fba96290843dfe4aee7597347ed01b278a92e37107edb6e9022d`. Verify exact remote bytes before treating them as the executed sources.

## Open mandatory gates

The `AGENTS.md` root commands were **not run on a full checkout**:

```sh
python scripts/verify_provenance.py
python -m unittest discover -s tests -p 'test_*.py'
python scripts/observer_foundations_probe.py
python scripts/ordinal_succ_report_probe.py
```

No hosted CI, full 9k+ tests, formal Lean, independent peer review, physics claim or π-normality result. Do not merge or promote status from this receipt. The first-jet analytic `O(n^-2)` remainder is paper-level and should receive an independently implemented symbolic/interval audit before external assertion.
