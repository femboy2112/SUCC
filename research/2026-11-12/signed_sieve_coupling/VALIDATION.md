# Exact local validation and reproducibility ledger

**Run date:** 2026-11-12. Working subtree only. All finite checks were performed in the current execution environment; no claim is made of GitHub-hosted CI, Lean, or independent external refereeing.

Commands (from this directory):

```
python -m unittest -q test_signed_sieve.py
python independent_audit.py
g++ -std=c++17 -O3 -Wall -Wextra -pedantic exact_scan.cpp -o exact_scan
./exact_scan 100000
./exact_scan 500000
```

Results:

- `test_signed_sieve.py`: **16 tests PASS**, 0 failures, exact integer and Fraction arithmetic, independent trial-divisor primality comparison up to 10,000. Verifies signed polarization, source-majority equality, ternary cube-root threshold, Haar Gram, Löwner monotonicity on finite tensors, fixed-cutoff and quartic-style negative controls, and fake-prime source.
- `independent_audit.py`: `{"even_targets":4095,"first_failure":0,"least_signed":1,"limit":8192,...}`. Primality and roughness calculated without importing the production code; direct O(N^2) pair counts.
- `exact_scan.cpp`: integer NTT with modulus `998244353` and root `3`, transform size `<2^23`, lengths chosen to avoid cyclic alias; convolution count `<=X<998244353` for each requested limit. Direct pair audits at the start of each cube-root band and sampled other N. For even N<=500000: **249999 exact finite cases**, zero nonpositive signed lower bounds. 100000 targets above previous exploratory cutoff 300000 are fresh to the exploration. Minimum signed 1 at N=4; fresh holdout minimum 2057 at N=300094.
- Fourth-root cutoff: 8 finite counterexamples through 500000; exact values in `scan_500k.json`. This is a test of a **stronger sufficiency criterion**, not Goldbach itself.
- The original exploratory numpy FFT scan to 300000 in the working investigation supplied orientation only; **it is not a rigorous receipt** and is not presented as independent validation.

**Important scope:** the C++ scan is not a formal proof of the NTT algorithm's correctness; its mathematical operations use a standard well-known modular NTT with spot checks. Coefficient bounds and independent direct checks make this finite test reproducible and much stronger than relying on floating values, but an external certified proof would require validation of compiler/runtime and the algorithm itself.

**Explicitly not run for this additive branch:** SUCC's ~13k full native tests, provenance verification, original observer/ordinal probes, hosted GitHub CI, Lean/theorem-prover builds, and external blind review. No source contract or historical artifact was modified.
