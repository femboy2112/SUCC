# Rank-2 / all-rank validation and execution boundary — 2026-10-27

**Isolated execution:** Python standard library with Fraction. The exact committed module, tests and probe files match the local actually tested git hash-object SHA IDs (checked during GitHub blob creation).

Commands:

~~~sh
python -m unittest discover -s tests -p test_pi_rank_lattice.py -v
python scripts/pi_rank_lattice_probe.py
python -m compileall -q observational_succ/pi_rank_lattice.py tests/test_pi_rank_lattice.py scripts/pi_rank_lattice_probe.py
~~~

**Observed:** 11 tests discovered, 10 PASS, 1 SKIP (upstream SUCC source module absent in isolated tree); probe PASS with 150 independently recomputed original four-pole equalities, 45 exact finite rational Green identities, and 1,428 flat squares at ranks 2,3,4. The numerical phasor tests reduce exact rational phases modulo one *before* float and compare only to a separately proved conservative rational envelope using π<22/7 and integer ceiling square roots. These finite tests do not prove the infinite theorem; its full argument is in the dossier.

**Native repository validation not run:** full SUCC unit tests, provenance, observer-foundations, ordinal report, hosted CI, Lean and outside peer review. Run each independently and record actual logs before merging.

Local, byte-verified Git blob hashes:
- Module: 6eee4fbe52ddf726b6e641cc412f1352854eab18
- Tests: e27921057fc6258e0babf6f434573e7dffff21df
- Probe: 6eafb6ec10974bd2069daa686fcef971c8054c3b

The isolated __init__.py shim was NOT pushed and must not overwrite the actual SUCC package. No main change, release or normality proof is authorized.
