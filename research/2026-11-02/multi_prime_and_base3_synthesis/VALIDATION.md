# Validation Receipt — Multi-Prime CRT Cofiber Recurrence & Base-3 Synthesis Mega-Round II (`MPB-01`..`MPB-18`)

**Date:** `2026-11-02`  
**Branch:** `research/prime-cofactor-nonconspiracy-2026-11-02`  
**Parent Main Commit:** `81045770234a114247e43eb08ae5c6d446e9514a`

---

## 1. Standalone Lean 4.14.0 Kernel Verification

**Command:**
```bash
/usr/bin/lean research/2026-11-02/multi_prime_and_base3_synthesis/MultiPrimeBase3Core.lean
```

**Result:** Exit code `0`, 14 constructive theorems verified via `#print axioms`, **zero `sorryAx`**, **zero `Classical.choice`**:
```text
'ObservationalSUCC.MultiPrimeBase3Synthesis.two_prime_scaled_cofiber_step_identity' depends on axioms: [propext, Quot.sound]
'ObservationalSUCC.MultiPrimeBase3Synthesis.three_prime_scaled_cofiber_step_identity' depends on axioms: [propext, Quot.sound]
'ObservationalSUCC.MultiPrimeBase3Synthesis.simultaneous_two_prime_midy_annihilation' depends on axioms: [propext, Quot.sound]
'ObservationalSUCC.MultiPrimeBase3Synthesis.overlap_cone_vanishing_bound' depends on axioms: [propext, Quot.sound]
'ObservationalSUCC.MultiPrimeBase3Synthesis.three_edge_forcing_numerator_check' does not depend on any axioms
'ObservationalSUCC.MultiPrimeBase3Synthesis.cross_radix_coercivity_difference' depends on axioms: [propext, Quot.sound]
'ObservationalSUCC.MultiPrimeBase3Synthesis.hex_ternary_scale_proximity_and_coercivity_gap' does not depend on any axioms
'ObservationalSUCC.MultiPrimeBase3Synthesis.joint_two_radix_trajectory_square_gap' depends on axioms: [propext, Quot.sound]
'ObservationalSUCC.MultiPrimeBase3Synthesis.joint_hex_ternary_constants' does not depend on any axioms
'ObservationalSUCC.MultiPrimeBase3Synthesis.laurent_reduced_factorization_check' does not depend on any axioms
'ObservationalSUCC.MultiPrimeBase3Synthesis.stirling_alpha_first_eight' does not depend on any axioms
'ObservationalSUCC.MultiPrimeBase3Synthesis.aurifeuillian_quadratic_identity' depends on axioms: [propext, Quot.sound]
'ObservationalSUCC.MultiPrimeBase3Synthesis.cyclotomic_aurifeuillian_splittings_verified' depends on axioms: [propext]
'ObservationalSUCC.MultiPrimeBase3Synthesis.ord16_two_adic_exponent_law' depends on axioms: [propext, Quot.sound]
```

---

## 2. Independent Second-Algorithm Oracle & Deterministic Receipt Check

**Command:**
```bash
python3 research/2026-11-02/multi_prime_and_base3_synthesis/independent_oracle_2.py --check
```

**Output:**
```text
EXACT_MEGA_ROUND_2_RECEIPT_VERIFIED
```

---

## 3. Root-Level Regression Test Suite

**Command:**
```bash
python3 -m unittest tests/test_multi_prime_and_base3_synthesis.py -v
```

**Output:**
```text
test_adversarial_countermodels_2 (tests.test_multi_prime_and_base3_synthesis.TestMultiPrimeBase3SynthesisMegaRound.test_adversarial_countermodels_2) ... ok
test_input_guards (tests.test_multi_prime_and_base3_synthesis.TestMultiPrimeBase3SynthesisMegaRound.test_input_guards) ... ok
test_mpb01_simultaneous_multi_prime_cofiber (tests.test_multi_prime_and_base3_synthesis.TestMultiPrimeBase3SynthesisMegaRound.test_mpb01_simultaneous_multi_prime_cofiber) ... ok
test_mpb02_two_prime_midy_and_twisted_gauss (tests.test_multi_prime_and_base3_synthesis.TestMultiPrimeBase3SynthesisMegaRound.test_mpb02_two_prime_midy_and_twisted_gauss) ... ok
test_mpb03_prime_window_overlap_cone_support (tests.test_multi_prime_and_base3_synthesis.TestMultiPrimeBase3SynthesisMegaRound.test_mpb03_prime_window_overlap_cone_support) ... ok
test_mpb04_three_edge_decomposition_and_pole_isolation (tests.test_multi_prime_and_base3_synthesis.TestMultiPrimeBase3SynthesisMegaRound.test_mpb04_three_edge_decomposition_and_pole_isolation) ... ok
test_mpb05_and_mpb06_k_step_and_scale_bridge (tests.test_multi_prime_and_base3_synthesis.TestMultiPrimeBase3SynthesisMegaRound.test_mpb05_and_mpb06_k_step_and_scale_bridge) ... ok
test_mpb07_and_mpb08_strided_diophantine_thresholds (tests.test_multi_prime_and_base3_synthesis.TestMultiPrimeBase3SynthesisMegaRound.test_mpb07_and_mpb08_strided_diophantine_thresholds) ... ok
test_mpb09_reduced_trinomial_and_alphas (tests.test_multi_prime_and_base3_synthesis.TestMultiPrimeBase3SynthesisMegaRound.test_mpb09_reduced_trinomial_and_alphas) ... ok
test_mpb10_eulerian_annihilation (tests.test_multi_prime_and_base3_synthesis.TestMultiPrimeBase3SynthesisMegaRound.test_mpb10_eulerian_annihilation) ... ok
test_mpb11_pade_borel_approximants (tests.test_multi_prime_and_base3_synthesis.TestMultiPrimeBase3SynthesisMegaRound.test_mpb11_pade_borel_approximants) ... ok
test_mpb12_second_order_difference_zero_seed (tests.test_multi_prime_and_base3_synthesis.TestMultiPrimeBase3SynthesisMegaRound.test_mpb12_second_order_difference_zero_seed) ... ok
test_mpb13_midpoint_centered_transport (tests.test_multi_prime_and_base3_synthesis.TestMultiPrimeBase3SynthesisMegaRound.test_mpb13_midpoint_centered_transport) ... ok
test_mpb14_nilpotent_dyadic_shift (tests.test_multi_prime_and_base3_synthesis.TestMultiPrimeBase3SynthesisMegaRound.test_mpb14_nilpotent_dyadic_shift) ... ok
test_mpb15_walsh_block_covariance (tests.test_multi_prime_and_base3_synthesis.TestMultiPrimeBase3SynthesisMegaRound.test_mpb15_walsh_block_covariance) ... ok
test_mpb16_aurifeuillian_quarter_degree (tests.test_multi_prime_and_base3_synthesis.TestMultiPrimeBase3SynthesisMegaRound.test_mpb16_aurifeuillian_quarter_degree) ... ok
test_mpb17_ord16_two_adic_law (tests.test_multi_prime_and_base3_synthesis.TestMultiPrimeBase3SynthesisMegaRound.test_mpb17_ord16_two_adic_law) ... ok
test_mpb18_sharpened_quarter_degree_sieve (tests.test_multi_prime_and_base3_synthesis.TestMultiPrimeBase3SynthesisMegaRound.test_mpb18_sharpened_quarter_degree_sieve) ... ok
test_saved_receipt_and_lean4_kernel_verification (tests.test_multi_prime_and_base3_synthesis.TestMultiPrimeBase3SynthesisMegaRound.test_saved_receipt_and_lean4_kernel_verification) ... ok

----------------------------------------------------------------------
Ran 19 tests in 4.124s

OK
```

---

## 4. Zero Regressions on Round 1 and Repository Probes

- `python3 -m unittest tests/test_prime_cofactor_nonconspiracy.py -v` $\to$ `Ran 15 tests, OK`
- `python3 scripts/verify_provenance.py` $\to$ `"status": "SOURCE_PROVENANCE_VERIFIED"` (`72` items)
- `python3 scripts/observer_foundations_probe.py` $\to$ `"status": "OBSERVATIONAL_SUCC_FORMAL_FOUNDATIONS"`
- `python3 scripts/ordinal_succ_report_probe.py` $\to$ `"status": "FINITE_ORDINAL_SUCC_SECOND_ORDER_WEIL_PROBE"`

---

## 5. Git Blob SHA-1 Hashes

| Git Blob SHA-1 | File Path |
| :--- | :--- |
| `c6f2a0102aba7b3c9f7c7eba6599d9d7df30bc54` | `research/2026-11-02/multi_prime_and_base3_synthesis/MultiPrimeBase3Core.lean` |
| `82eca0d70134043e34149e9c610b3d4174b5a16f` | `research/2026-11-02/multi_prime_and_base3_synthesis/mega_round_2_engine.py` |
| `009f9c3079bb7c36444ce4c70218a651704a51db` | `research/2026-11-02/multi_prime_and_base3_synthesis/independent_oracle_2.py` |
| `25eb7b6f4dc037fac4b1845c041fb3d446c19c2b` | `research/2026-11-02/multi_prime_and_base3_synthesis/EXACT_MEGA_ROUND_2_RECEIPT.json` |
| `78d2816fa3c6d4c77d270266c7aee6116be44978` | `research/2026-11-02/multi_prime_and_base3_synthesis/THEOREMS_AND_PROOFS.md` |
| `37e9de01f24bc712d34246cdebb1fa95f7ae743e` | `research/2026-11-02/multi_prime_and_base3_synthesis/CLAIMS.md` |
| `85cafc144098a010259de9be83aa4d44b8cad11e` | `research/2026-11-02/multi_prime_and_base3_synthesis/README.md` |
| `a75264ba168f6694fe0e61f1432fa2788950ee81` | `tests/test_multi_prime_and_base3_synthesis.py` |
