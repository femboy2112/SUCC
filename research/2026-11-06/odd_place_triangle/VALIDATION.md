# Validation, hostile controls, and provenance — Operation ODD-PLACE TRIANGLE

**Parent:** exact `45c5d41435fdf94998d81901b0e58b9fa7775106` from existing SUCC #528. **Separate preregistration commit:** `c0eab859aa9a3762ce15fec6da44b1d2fcbb6b74` precedes all new p=181,197,269,293 cycle-magnitude calculations. p=149 amplitudes and the proposed digamma formula were explored before prereg and are explicitly CALIBRATION/analytic derivation, not blind holdouts. Same-model holdout registration is not an external independent witness.

**Runtime:** isolated Python 3.13 environment with standard library for all source states/CRT/birth arithmetic; optional `sympy` and `mpmath` only for a differently coded symbolic/digamma oracle and finite numerical display. No local full clone of SUCC was available (`git ls-remote` DNS failure); code is self-contained and written only under a new research directory.

**Executed commands and raw logs:**

```sh
python -m compileall -q adelic_triangle.py test_adelic_triangle.py independent_oracle.py run_probes.py
python -m unittest discover -v -s . -p 'test_*.py' > LOCAL_TEST_STDOUT.txt 2> LOCAL_TEST_STDERR.txt
python independent_oracle.py > INDEPENDENT_ORACLE_LOG.txt
python run_probes.py > FINITE_RESULTS.json
```

- `compileall` PASS.
- **19/19 focused unittest methods PASS**, no failures/errors. Primary tests use exact Fraction CRT on all original zero-seed n=1..40, three Fourier modes -3/1/2, original source denominator genealogy, and prime births for all p<300, p-plateaux for all p<200. Five local signed/covariance sample magnitudes are displayed with ordinary floats and are **OBSERVED-FINITE**, not certified global cancellation bounds.
- Independently expressed SymPy source numerator, exact CRT using denominator factorization and modular idempotents at 9 original rational times, 15 p-birth controls and digamma/silver numeric identity PASS. This is **same-model, different implementation**, not mathematical priority or blind refereeing.
- Hostile q=1009 compensation exactly preserves p=149 local phases while giving near-aligned real phases; test reports approximate real |mean| >0.99, with a **proved** exact rational angle bound |x_t|≤1/(2q), hence real |mean|≥1−π/q.
- Proven Gauss estimate ≤√p/m uses **classical multiplicative-character Gauss theorem**. Finite float comparisons are diagnostics only; the classical theorem is not established by the tests.
- Exact unweighted source/digamma identity uses Gauss's classical digamma theorem. Floating 70-digit oracle verifies the constant, not by itself a proof; the analytic derivation is in THEOREMS.md.
- Mutation check 4→5 verifies source nonzero harmonic weight sum, altered p-birth residue and emergence of logarithmic term.
- Formal pair-edge co-dual has exact integer determinant -2, correct Q-inverse and mod2 diagonal kernel; NO source-commuting triangle equivalence established.

## Predeclared fresh prime-cycle diagnostics (all finite, floating-display only)

| p | first index | clean interval length | ord_p 16 | p-local | full real | sqrt(p)/ord |
|---:|---:|---:|---:|---:|---:|---:|
|181|23|68|45|0.1530813131|0.1571634838|0.2989694233|
|197|25|74|49|0.1241380108|0.1837551762|0.2864422214|
|269|34|101|67|0.1293452411|0.0554006527|0.2447943204|
|293|37|110|73|0.1294027488|0.0108294571|0.2344827777|

Preseen calibration p=149: first n=19, clean length56, order37, local ~0.1074080183 and full real ~0.1704083523. The changing relative magnitudes show that local Gauss cancellation is NOT the complete real-source story. Finite source-selected phases are computed from exact rational U; numerical sin/cos display has no certified error interval and must not be called an asymptotic inequality.

**Not executed:** full native SUCC >12k suite, root provenance/observer/ordinal scripts, Lean, hosted exact-head CI, external academic review. No status upgrades for π normality, RH or original all-prefix real Weyl. Original source weights, seed, production, old research branches and main remain unchanged. Merge/release/publication not authorized.
