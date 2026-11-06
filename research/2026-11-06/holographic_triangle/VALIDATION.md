# Validation scope — 2026-11-06

The work is based on the connected GitHub source branch (PR #529) and the local exact-rational research-only scripts staged under this directory. `AGENTS.md` and the previous source and claim ledgers are respected. The original BBP four-pole recurrence, literal U0=0, imported manifests and preserved `formal/` theorem declarations are unchanged.

**Preregistration:** source hypothesis and fixed tests were first pushed to GitHub at `3641b5abbba6e1581cc2074e200b46d6cab0cb23`, before running the new local tests. Independent initial mathematical derivation was done before preregistration, so no claim of discovery blindness. Test runs and raw logs follow.

**Exact-focused suite:** `python -m unittest discover -v -s . -p test_*.py`, stderr in `LOCAL_TEST_STDERR.txt`, stdout in `LOCAL_TEST_STDOUT.txt`. Tests include exhaustive small finite-ring edge kernels, seam reconstruction, exact original fraction states, integer carry and boundary dynamics, source mutant and rational ghost, source-prime birth, all-N conditional theorem calibrations at fixed N list, Gamma-harmonic Abel reconstruction. **19/19 focused methods PASS, 0 errors/failures**. Results recorded in raw log.

**Independent implementation:** `independent_oracle.py` does not import `hologram.py`, directly evaluates the combined polynomial source and BBP convolution, original rational phase numerator from residues and carries, and **32 independent exact Fraction checks** including fixed prime witnesses. The mpmath digamma/silver identity is high-precision **NUMERICAL CALIBRATION**, not a proof certificate. The exact proof of Gamma/digamma recurrence and silver formula lives in THEOREMS.md and parent #529. Raw JSON in `INDEPENDENT_ORACLE_RAW.json`.

**Standards and authority:** Bertrand’s theorem is classical and cited, not locally re-proved; its precise use in HT14 is elementary once the original prime birth from #529 is known. The source minimal field factorization is copied as a read-only claim from parallel SUCC PR #481, independently algebraically checked by coefficient multiplication; no cross-PR merge. Every numerical claim is finite.

**NOT EXECUTED at child exact head:** full native 12k+ SUCC suite, root provenance/observer/ordinal probes, formal Lean kernel, hosted Actions exact-head status or independent external referee. This branch is draft research; no main merges, releases, external claims to academic novelty, or π normality promotion.

## Frozen extra preregistration and source-split prime windows

New hypothesis `PREREG_LINEAR_DEPTH.md` was GitHub committed at `5592178c570cd4f179c31afd6444407451f7e722` BEFORE running the additional exact six window probes. It explicitly distinguishes a mathematical proof hypothesized in advance from blinded empirical validation. New `linear_depth_probe.py` and `test_linear_depth.py` check the Gaussian split/inert strip and mutant controls at `n=(8,16,32,64,128,257)`. The added exact tests pass and raw window data are preserved in `LINEAR_DEPTH_RAW.json`; total research-local suite **23/23 PASS**. This uses a classical **PNT in arithmetic progressions** theorem for its asymptotic consequence, not finite extrapolation. There is no new full-native, Lean or hosted CI authority.
