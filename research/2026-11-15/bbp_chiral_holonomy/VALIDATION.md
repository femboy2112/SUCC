# Validation and authority — original BBP 7±4 chiral loop

**Date 2026-11-15.** Tested the exact staged source files under `/mnt/data/bbp_chiral_holonomy/`; no SUCC native repository installation or hosted CI environment is implied.

## Executed checks

- `python -m unittest discover -s . -p 'test_chiral_probe.py' -v` — **20/20 PASS**. The tests cover original rational four-pole algebra at positive and negative clock inputs, unchanged literal zero source, q=16 and 256 original rational return jets modulo 16 and 32, exact order-two source chirality, Pauli anticommutation on finite 4-clock, nested root phase, four-register Walsh reconstruction, truthful Green-tail interval inclusion, original real-circle four-time **numerical smoke only**, coherent wrong seed, rational q-periodic point, exact coboundary-mutant source, 2-adic isometry and disappearance of anticommutation.
- `python independent_audit.py` — **PASS**: distinct SymPy source reconstruction from all four original poles; full polynomial coefficient congruence certificates for `r' mod16` on 4 classes and `r' mod32` on 8 classes; independent numerator calculation proves second Taylor coefficient belongs to `2 Z_2[t, 1/D]`.
- `python make_report.py` — **PASS**; deterministic `FINITE_REPORT.json` with exact integer modular values and clearly labelled *noncertified* complex floats. B=8,16,32 were chosen for bounded finite illustrations, not asymptotic inference or pre-registered new holdouts.
- `python -m compileall -q chiral_probe.py independent_audit.py make_report.py test_chiral_probe.py` — **PASS**.
- Companion `bbp_loop_holonomy` local native test suite re-executed **26/26 PASS**; see its own stored `VALIDATION.md`, `TEST_LOG.txt`, and `ALGEBRA_AUDIT.txt`. These are separate isolated suites, not the >13k native SUCC suite.

## Boundaries

1. Exact modular checks and integer matrices are mathematically rigorous finite calculations. The source polynomial congruences are independently implemented in SymPy and algebraically displayed in `THEOREMS.md`, but are **not Lean kernel-checked**.
2. Complex/sine/cosine values in finite reports use ordinary Python floating arithmetic. The source Green tails used to choose input phase representatives have rigorous rational intervals; **that does not make the final transcendental complex outputs certified intervals**. They are smoke tests, not an experimental physics detection.
3. Infinite theorems are paper proofs with hypotheses. In particular `F(0)=0` from #646 is imported as an unreviewed paper premise *only* where explicitly mentioned for the mutant backward zero. The new finite source loop and anticommutation do not depend on it for `n>=k+1`.
4. No proof of source-selected all-B positive-density energy margin or signed Weyl cancellation; π base-16 normality, R0, physical energy quantization, RH remain **OPEN**.
5. **NOT RUN / NOT CLAIMED:** root `python scripts/verify_provenance.py`; `python -m unittest discover -s tests -p 'test_*.py'`; `python scripts/observer_foundations_probe.py`; `python scripts/ordinal_succ_report_probe.py`; new Lean, hosted CI, independent blind mathematical review. Integration gate required by `AGENTS.md` remains pending.

## Protected scope

Target a dedicated non-main branch stacked on the pinned #646 head. Add files only under `research/2026-11-15/bbp_loop_holonomy/` and `research/2026-11-15/bbp_chiral_holonomy/`; do not change original four-pole production code, the literal zero seed, provenance manifest, archived historical sources, original tests, `.github`, formal/Lean, tags or releases. Commit and Git SHA verification are separate provenance operations and must not be claimed until they return success.
