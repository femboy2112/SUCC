# Validation: source-twisted Dirichlet pole and full universal-carrier combined suite

**Mathematical status:** BR1–BR9 are local exact algebra plus elementary Dirichlet-series analytic continuation, with independent rational/SymPy/90-digit numeric checks. No external referee or kernel proof; no selected π normality or RH consequence. The weighted source parameter `s` in `D_R(s)` is NOT the BBP initial seed, and the analytic pole at `s=-1` is NOT the finite value `ζ(-1)=-1/12`.

## Proof and controls

- `test_bbp_source_twisted_zeta.py`: 7 tests, exact original four-pole partial-fraction coefficients for n1..512; positive remainder and upper envelope for n2..4095; digamma finite part; finite harmonic/pole remainders; positive rank-two mutant distinguished at the finite part; rough finite Laurent calibration (not asymptotic authority).
- `bbp_twisted_zeta_independent_oracle.py`: separately combined SymPy rational source and 90-digit mpmath Gamma/digamma finite part, honest finite-N comparison at N2048, mutation. Run PASS in saved `bbp_twisted_zeta_oracle_receipt.json`.
- Exact analytic bound `g(n)<=35/(27 n^3)` for n>=2 and positive g1 is derived directly from the unchanged source inequalities. This proves the new meromorphic extension to `Re(s)>-2` except the simple ζ(s+2) pole at s=-1. Finite numerical tests do not establish the analytic theorem.
- Mutant `(5,-5,0,0)` has the same leading residue 15/64 but distinct finite Gamma part; coherent changed seed retains every source-only reading. These are mandatory controls.

## Preserved failed runs and calibrations

1. First standalone test run failed because its test fixture mistakenly used `Fraction(n-1+delta,8)` instead of **`Fraction(n-1)+Fraction(delta,8)`** in the denominator of the expected partial fraction. Original mathematical formula BR2 and independent SymPy oracle were correct. The raw failure remains in `bbp_twisted_zeta_tests_initial_failure.log`; corrected standalone run is 7/7 PASS in `bbp_twisted_zeta_tests.log`.
2. The initial 57-test combined run failed two extremely stringent 1e-99 comparisons because separate imported mpmath test modules set the global precision to 95 dps and overrode the tangent suite's intended 115 dps. Raw combined failure remains `combined_suite_initial_precision_failure.log`. The earlier tangent suite now resets its own precision in `setUpClass`, and the exact standalone manifest updates its byte hash. The naive combined `python -m unittest -q test_carrier_probe.py test_logjet_probe.py test_zeta_allgrade.py test_zeta_tangent_family.py test_bbp_source_twisted_zeta.py` then passed 57/57, raw receipt `combined_suite_final.log`.

The original code and source hashes remain in prior PR417 commits, preserving their provenance. The added fixture and precision corrections are explicit rather than silently rewritten or called math refutations.

**Not run in the current branch:** native SUCC root 10,008-test suite, full AGENTS gates, new Lean theorem, external blind review. Check hosted CI at exact current PR head before asserting any success.
