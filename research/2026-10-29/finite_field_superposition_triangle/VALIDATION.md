# Validation — exact local receipts and integration boundary

**Parent pinned:** `e02933591e7b7486376acb9847e00fd01d9ae498` (#383). Research-only additive files under this directory; no original source or seed changes. No direct git checkout was available in this run's local sandbox (network DNS refused `github.com`), so root-only SUCC validation, Lean checks and hosted exact-head CI are NOT claimed.

## Locally executed before upload

- `python -m unittest -v test_finite_source_triangle.py`: **9 methods PASSED**. Tested exact four-pole rational passport; original source endpoint rows through depth 7 at four/five distinct clocks; posterior path-sum conservation; both orderings of a one-success one-failure diamond; independent source-shift recurrence; exact four-original-pole digamma rational identity and harmonic sum equality and exact harmonic increments through depth 9; seed-blind positive source; exact rational selected fractional points, all grade/carry marks and composed two-step integer carries for four seeds; finite original/fake numeric first-jet calibration.
- `python independent_first_jet_oracle.py`: **PASS**. Independent SymPy reconstruction of source rational factorization, `Q'(0)=15`, `Q''(0)=-59`, exact rational first-jet generating polynomial, first grade correction `-151/960`, integrated original `-49/320`, fake `+1/32`, difference `-59/320`, golden PGF interior root, secondary Gamma–Poisson rank contrast, and a distinct positive rational extra-pole source with the SAME first two endpoint derivatives (source-uniqueness negative control). No import of implementation.
- `python -m compileall -q finite_source_triangle.py test_finite_source_triangle.py independent_first_jet_oracle.py`: exit 0.
- Numerical `n=20,40,80,160,320,640` native exact-rational source sums examined at 60-digit precision in an independent notebook, and `n=60,120,240` in unit tests. These finite observations **do not prove** the asymptotic.
- Expected upload-source SHA-256: `finite_source_triangle.py` `a12e69d86ac5850855e7d81dd5aae8285596e32172c47a27fbbcb35210528328`; `test_finite_source_triangle.py` `64f6db66e79d9c2ebc2a7017edb86b69e72e3a692e696afa65386ef712c73956`; `independent_first_jet_oracle.py` `cbcc5e4812b9a5ed7b87957be65e47754ea422c6ad1dfa1be0e2d4e8eaf685e2`. Verify exact remote bytes before treating them as the executed sources.

## Open mandatory gates

The `AGENTS.md` root commands were **not run on a full checkout**:

```sh
python scripts/verify_provenance.py
python -m unittest discover -s tests -p 'test_*.py'
python scripts/observer_foundations_probe.py
python scripts/ordinal_succ_report_probe.py
```

No hosted CI, full 9k+ tests, formal Lean, independent peer review, physics claim or π-normality result. Do not merge or promote status from this receipt. The first-jet analytic `O(n^-2)` remainder is paper-level and should receive an independently implemented symbolic/interval audit before external assertion.
