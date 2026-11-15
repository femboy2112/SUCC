# Validation / claim authority — seed source rank

**Execution:** Isolated Python 3 environment in current research container, 2026-11-14. Focused module uses only stdlib `fractions`, `dataclasses`, and `unittest` (no full SUCC checkout available). The original four-pole forcing and rational source gauge were recovered directly from SUCC primary documents. These are not physical measurements or a new proof of normality.

### Actual commands

```sh
PYTHONPATH=. python -m unittest discover -s tests -p 'test_seed_source_rank.py' -v
PYTHONPATH=. python research/2026-11-14/seed_source_rank/INDEPENDENT_ORACLE.py
python -m compileall -q observational_succ/seed_source_rank.py tests/test_seed_source_rank.py research/2026-11-14/seed_source_rank/INDEPENDENT_ORACLE.py
```

- **13/13** focused standard-library rational tests passed.
- **238/238** independently encoded exact rational source/gauge/finite-shadow controls passed, including independent factorization and the original-null-source residue signs.
- `compileall` passed. Raw local stdout/stderr in `TEST_LOG.txt` and `INDEPENDENT_LOG.txt`.
- One initial test erroneously demanded different source-gauge and wrong-fixed-forcing states at `n=0`, where both equal the prepared rational seed; corrected to check the distinguishing transition for `n>=1`. The original source-gauge identity passed throughout.
- One independent oracle initially compared a degree-six polynomial with an 8-slot coefficient tuple including a **cosmetic trailing zero**. Corrected the comparison to the exact polynomial degree; the full native factorization and residue checks then passed. These are test-harness mistakes, not false source-gauge formulas.

### Status

- **PROVED ELEMENTARY (paper):** source recurrence, seed-to-completion rank map, rational gauge compensation, finite rational moving-horizon shadow, shell `1-O(B^-4)` lower coherence bound.
- **CLASSICAL IMPORT:** Wall rational translation/nonzero scaling normality theorem, π irrationality, classical BBP identity, ordinary Fourier phase inequalities.
- **SUCC IMPORT (not independently reproved):** proper-form rational source moduli and the null polynomial `g_0`, full 7D period-space rigidity via Baker. The independent oracle only checks coefficients/moment identities, not Baker or all limiting periods.
- **OBSERVED FINITE:** exact rational tests and independent source oracle.
- **UNVERIFIED/OPEN:** π normality, weakest R0/R1, selected signed cancellation, universal source admissibility beyond the original rational-polynomial carrier, physical carrier interpretation.

Full SUCC `AGENTS.md` provenance, root tests, observer-foundations probe, ordinal report, Lean and GitHub exact-head CI **not executed locally**. Do not claim external independent proof review or a verified Wall theorem implementation from the finite tests.
