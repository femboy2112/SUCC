# Reproducibility and authority

**Pre-push isolated experiment** on CPython 3.13.5; stdlib `Fraction`, `dataclasses` and `unittest`. No float complex-root evaluations, fabricated independent referees or physical observations.

~~~sh
PYTHONPATH=. python -m unittest discover -s tests -p 'test_arity_*py' -v
~~~

**Observed locally:** **26 tests executed, 25 passed, 1 skipped**. The skip is the cross-check against `observational_succ.selected_orbit`, because this first replay was an isolated staging overlay, not a complete SUCC checkout. The exact four-pole transcription, 3-cyclotomic identities, 2×2 Hermitian Lorentz algebra, 4-vertex tetrahedral law, rational Toeplitz factorization and full-rank determinant, same-loop character/boost representations, exact oscillator twist, hostile determinant/parallelogram controls and rational seed alias were exercised.

The unskipped cross-check is designed to compare `bbp_residue_prefix(28)` and `bbp_forcing(n)` against the canonical `SelectedOrbit`/`original_forcing` in the repository's **full checkout**. The exact source and `U_0=0` were not changed.

**Required full-repo replays** by `AGENTS.md` (not yet executed at the branch head; do not attribute the parent's green checks to this change):

~~~sh
python scripts/verify_provenance.py
python -m unittest discover -s tests -p 'test_*.py'
python scripts/observer_foundations_probe.py
python scripts/ordinal_succ_report_probe.py
~~~

The linear algebra and all-N statements in THEOREMS are **paper derivations**. Tests witness exact finite instances, *not* universal verification. No Lean compilation, independent scholarly peer review, hosted CI pass, signed source-bound result, π-normality proof, Goldbach proof or RH proof is claimed. Recheck hosted statuses against the **actual pushed commit SHA**.
