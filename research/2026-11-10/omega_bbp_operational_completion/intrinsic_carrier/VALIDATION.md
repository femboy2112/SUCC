# Fast local validation and CI boundary — 2026-11-10

**Scope:** Added source-independent Hilbert-carrier operator and finite positive-Mellin adversarial source alias; parent is research draft #582 at `762c99952fc28c46754cb2d30a3adf0a52816721`. The original four-pole SUCC source and zero seed remain **unmodified**. Native `AGENTS.md` full-suite commands are recorded but **not run in this exploratory child round**, honoring the user's very long CI constraint. The standalone files do not invoke native test autodiscovery in `tests/`.

## Executed commands and receipts

```
cd /mnt/data/succ_intrinsic_carrier_round
python -W error -m unittest discover -s . -p 'test_*.py' -q
# Ran 22 tests in 0.741 s (final rerun 0.705 s) — OK
python independent_carrier_audit.py
# INDEPENDENT PASS: p=2,3,4,5,7 spectra;
# boundary 5 + three six-cell bulk blocks;
# positive N=0 inverse alias difference 0.0001905264841237519187413
```

Runtime Python 3.13.5, `Fraction` exact operator and Mellin source code uses only standard library. Focused test suites have optional `sympy` and `mpmath` numerical/matrix oracle tests that explicitly SKIP on installations lacking those packages; installed here and passed. Separate independent audit requires both.

**Falsifications repaired during local development:** first test compared double-precision `pi/16` to a long rational prefix, rounding the positive tail to zero; replaced by exact longer-prefix rational enclosure. Initial large-n `675/128` asymptotic sample at n=600 was insufficient for the declared .13 absolute tolerance; replaced with n=4800 and .04 tolerance. Both failures retained as development history, then the suite passed. The asymptotic theorem itself is inherited from the parent paper, not proved by these tests.

**Controls exercised:** arithmetic p=2...17; composite primes; commuting pure prime divisibility; 16-branch parity exists for even cyclic bases only; exact five-site boundary plus rank-two 6-block modes; zeta Gibbs trace for β=2,3 with strict tail enclosure; source reindex pi versus pi/16; coherent rational wrong seed; original four-pole orientation finite samples; exact Gram moment-alias N=0...8 and nonzero first unseen moment; independent SymPy nullspace and independent high-precision completion-difference quadrature.

**Paper proof dependencies:** root `README.md` and `PROOFS.md` supply all-N Gram positivity, the strict Cauchy-transform defect interval, operator spectrum, β>1 trace and the prime-indexed norm-convergence region. Finite tests alone are not their universal proofs. The independent SymPy implementation is mathematically differently factored but authored in the same research round, **not a blind referee**.

**CI and external boundary:** No full ~13k SUCC native suite; no hosted CI wait/green claim; no Lean proof build; no OpenQASM compiler/hardware; no new source-selected Weyl estimate; no ζ critical-line selfadjoint operator closure or completed Weil positivity. The GitHub draft PR will record the exact published blob hashes and commit SHA; do not infer them before publication.
