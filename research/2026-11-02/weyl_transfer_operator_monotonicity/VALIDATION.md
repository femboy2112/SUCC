# Validation and Replication: Mega-Round V

**Dossier:** Weyl Differencing, Non-Autonomous Transfer Operators, and Hausdorff Tail Monotonicity  
**Branch:** `research/pi-normality-framework-spine-2026-11-02`  
**Date:** 2026-11-02  
**Receipt:** `EXACT_WTM_RECEIPT.json`

---

## 1. Automated Replication Instructions

### Step 1: Run the Standalone Exact Arithmetic Engine
```bash
python3 research/2026-11-02/weyl_transfer_operator_monotonicity/weyl_transfer_operator_monotonicity_engine.py
```
*Expected Output:*
```
Mega-Round V Engine completed with 18 claims. All passed: True
  [WTM-01] PROVED_EXACT
  [WTM-02] PROVED_EXACT
  ...
  [WTM-18] PROVED_EXACT
```

### Step 2: Run the Independent Second-Algorithm Oracle
```bash
python3 research/2026-11-02/weyl_transfer_operator_monotonicity/independent_oracle_wtm.py
```
*Expected Output:*
```
All 18 passed: True
```

### Step 3: Verify Standalone Lean 4 Kernel Proofs
```bash
lean research/2026-11-02/weyl_transfer_operator_monotonicity/WeylTransferMonotonicityCore.lean
```
*Expected Output:*
- Return code `0`.
- Axiom audit: Only `[propext, Quot.sound]` or none at all.
- Exactly zero occurrences of `sorry` or `Classical.choice`.

### Step 4: Run Root-Level Regression Test Suite
```bash
python3 -m unittest tests.test_weyl_transfer_operator_monotonicity
```
*Expected Output:*
- 24 tests passed in $< 1$s.

### Step 5: Run Full 5-Mega-Round Regression Test Suite (100 Tests)
```bash
python3 -m unittest tests.test_prime_cofactor_nonconspiracy \
                   tests.test_multi_prime_and_base3_synthesis \
                   tests.test_plancherel_bilinear_collapse \
                   tests.test_pi_normality_framework_spine \
                   tests.test_weyl_transfer_operator_monotonicity
```
*Expected Output:*
- Ran 100 tests in ~10s. `OK`.

---

## 2. Independent Audit Checklist

- [x] **Zero Sorry / Classical Choice:** `WeylTransferMonotonicityCore.lean` checked with Lean 4.29.1, 0 sorryAx.
- [x] **Clean Epistemic Firewall:** Base-16 normality of $\pi$, RH, and Weil positivity remain strictly OPEN.
- [x] **Exact Receipt Integrity:** `EXACT_WTM_RECEIPT.json` contains full numerical and algebraic parameters for all 18 claims.
- [x] **Adversarial Defenses:** 4 adversarial countermodels (perturbed $\sigma_k$, non-expanding radix, indefinite Gram form, non-monotonic jump) reliably caught and rejected.
- [x] **Non-Regressive Guarantee:** All previous 76 tests plus 24 new tests (100 total) pass concurrently.
