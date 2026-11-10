# Provenance, runs and validation — source 16×16 π matrix

- Pinned original parent PR #566: `4caae7652b430974448437bc716da9a3edba5fd9`. Protocol first committed `a07f3646d139be55a565b65fb7318e5709643509` before reading the newly computed 65,536-digit holdout.
- Original four signed BBP rational source, zero seed; no modification of any inherited file. Source finite digits certified via `L=Σ_(j≤K) floor(16^(K+1−j) r(j))`, `L≤16^K π<L+K+1`, guard=24 and guard=32 separately, all K=131072+guard terms; two independent error widths of the same program. Both complete outputs byte-identical.
- Full 131072 digits SHA256 with newline: `4e349f3af293f07c42135caabffe0ce262c7ff282847d71e158f05551cd89a73`; first half matches inherited PR #566 SHA256 `e42ee060201573db4a32a8c8e0a4ccac5a6cb061ae1ac8d71809234c58dfae53`; new half hash with newline `344972a0bd1028032907c0e2c9495ad7943265bde1fdd98d4be1c7de38520d03`.
- Exact `Fraction` arithmetic: 16×16 count matrices and margins, source-independent 225 mixed energy, opposite-character energy from difference counts, Dobrushin bound δ(P) first `497311/8555180`, held-out `123803/2292261`, whole-prefix `481818/13186475`, and full-support nilpotent non-Haar matrix P²=H. A separately executed symbolic SymPy calculation verified P²=H, rank2, eigen mults 1:1/0:15 and mixed energy 3/1024.
- **19/19 focused unit tests PASS** against a temporary API-compatible local fixture for #566 source helpers. This test-only fixture is NOT in the published branch; the GitHub source must be evaluated under exact-head hosted native checks. No full 12k+ root suite, provenance/foundations/ordinal, new Lean, or external referee authority claimed.
- NumPy 16×16 eig/SVD and 1,200 matched-count shuffles per comparison were run locally; the experiment's seed for the **fresh** half is **20261110**, as preregistered. The first-half fixed-count 1,200-shuffle calibration seed is 20261109 but was analyzed before preregistration. First-half opposite-mode mean 0.000230745 and ≈99.2nd percentile; fresh 0.000230040 and ≈22.3rd percentile, fresh 95th percentile 0.000382475. Frozen replication criterion FAILS, recorded explicitly.
- No reason exists to interpret finite-precision eigenvalues or finite-sample shuffle percentiles as interval certificates or a proof of π's normality. Exact rational Dobrushin bounds, unlike the NumPy eigen decomposition, are mathematical source-certified finite assertions.

From SUCC repository root:

```
python -m unittest discover -s tests -p 'test_bbp_spectral_gamma.py' -v
python research/2026-11-09/pi_16x16_gamma_spectrum/reproduce.py
python research/2026-11-09/pi_16x16_gamma_spectrum/reproduce.py --recompute
python scripts/verify_provenance.py
python scripts/observer_foundations_probe.py
python scripts/ordinal_succ_report_probe.py
python -m unittest discover -s tests -p 'test_*.py'
```

The first two research commands use checked-in certified digits and exact table identities; `--recompute` triggers both complete 131,072-term BBP source enclosures and checks the stored source stream. NumPy is optional for numeric eig/SVD diagnostics and shuffled reference replay; no NumPy is imported by the reusable exact stdlib module or its root unit tests.
