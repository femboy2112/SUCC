# Exact local validation — Null Information, 2026-11-23

- Command: `python -m unittest discover -s /tmp/succ_nulljet_20261123 -p 'test_virtual_null_tower.py' -v`
- Outcome: **13 tests, all PASS; 0 errors, 0 failures**, with standard-library exact `Fraction` arithmetic (local run).
- Test file SHA-1/Git blob: `71aa4a0eaa3845a57941199e85fd9e7d32d03441`; remote GitHub blob fetched and checked byte-identical.
- Coverage: original signed four-pole BBP and Mellin coefficients, source analytic-jet normalization, certified actual original-seed first 12 digits from strict rational intervals, synthetic integer null tower at scales 16⁻¹..16⁻⁶, leading-coefficient height, missing-scale mutation, signed digit seam conservation, rational locked-control boundary, and nonnormal irrational control.
- Tests are finite examples and do not verify the universal infinite moment/cylinder/seam/capacity theorems, which have separate paper proofs. Additional remote [phase-germ test](test_phase_germ_no_go.py) SHA `25a6b3777fa21ca00de1c72edc4deff136784eb3`; exact locked-case moving poles and normalized rank-one minors. Additional remote [Hasse-jet test](test_hasse_null_tower.py) Git SHA `b3973e8b414415f2a9861ba1f952a0ab6b4cc8bb` checks factorial blindness at p=2/3/5/7 and an exact radix × prime height prototype. The exponent-two aperture is **conditional on external formalization**, not rerun locally.
- **Not executed**: inherited full SUCC suite, AGENTS required gates, hosted CI, Lean rebuilds, independent external mathematical review, or any π normality asymptotic.
