# Validation Dossier: Pi Normality Framework Spine Synthesis

**Date:** `2026-11-02`  
**Branch:** `research/pi-normality-framework-spine-2026-11-02`  
**Dossier Directory:** `research/2026-11-02/pi_normality_framework_spine/`

---

## 1. Summary of Verification Runs

| Component | Target File | Verification Command | Status | Time |
| :--- | :--- | :--- | :---: | :---: |
| **Lean 4 Kernel** | `PiNormalitySpineCore.lean` | `/usr/bin/lean research/2026-11-02/pi_normality_framework_spine/PiNormalitySpineCore.lean` | **PASS (0 sorryAx, 0 Classical.choice)** | 0.88s |
| **Exact Engine** | `pi_normality_spine_engine.py` | `python3 research/2026-11-02/pi_normality_framework_spine/pi_normality_spine_engine.py` | **PASS (Receipt Generated)** | 0.51s |
| **Independent Oracle** | `independent_oracle_spine.py` | `python3 research/2026-11-02/pi_normality_framework_spine/independent_oracle_spine.py --check` | **PASS (18/18 claims + 4/4 countermodels)** | 0.35s |
| **Root Test Suite** | `tests/test_pi_normality_framework_spine.py` | `python3 -m unittest tests.test_pi_normality_framework_spine -v` | **PASS (21/21 tests OK)** | 1.62s |
| **Combined Regression** | Multi-round (76 tests) | `python3 -m unittest tests.test_prime_cofactor_nonconspiracy tests.test_multi_prime_and_base3_synthesis tests.test_plancherel_bilinear_collapse tests.test_pi_normality_framework_spine` | **PASS (76/76 tests OK)** | 10.10s |

---

## 2. Lean 4 Axiom Verification Output

```text
'ObservationalSUCC.PiNormalitySpine.simultaneous_two_prime_pole_annihilation_identity' depends on axioms: [propext, Quot.sound]
'ObservationalSUCC.PiNormalitySpine.coprime_order_lcm_pairs' does not depend on any axioms
'ObservationalSUCC.PiNormalitySpine.gcd_index_scaling_bound' depends on axioms: [propext, Quot.sound]
'ObservationalSUCC.PiNormalitySpine.four_bit_carry_upper_bound' depends on axioms: [propext, Quot.sound]
'ObservationalSUCC.PiNormalitySpine.nilpotent_shift_four_step' depends on axioms: [propext, Quot.sound]
'ObservationalSUCC.PiNormalitySpine.centered_spill_scaling_factor' does not depend on any axioms
'ObservationalSUCC.PiNormalitySpine.tri_radix_lagrange_expansion' depends on axioms: [propext, Quot.sound]
'ObservationalSUCC.PiNormalitySpine.tri_radix_gram_determinant' does not depend on any axioms
'ObservationalSUCC.PiNormalitySpine.tri_radix_determinant_is_ninety_five_squared' does not depend on any axioms
'ObservationalSUCC.PiNormalitySpine.tri_radix_kernel_trivial' depends on axioms: [propext, Quot.sound]
'ObservationalSUCC.PiNormalitySpine.tri_radix_fixed_point_gcd_one' does not depend on any axioms
'ObservationalSUCC.PiNormalitySpine.pade_two_two_denominator_at_one' does not depend on any axioms
'ObservationalSUCC.PiNormalitySpine.pade_two_two_is_one_nineteen_squared' does not depend on any axioms
'ObservationalSUCC.PiNormalitySpine.pade_two_two_first_ten' does not depend on any axioms
'ObservationalSUCC.PiNormalitySpine.third_difference_bbp_orbit_identity' depends on axioms: [propext, Quot.sound]
'ObservationalSUCC.PiNormalitySpine.three_thousand_three_seventy_five_is_fifteen_cubed' does not depend on any axioms
'ObservationalSUCC.PiNormalitySpine.aurifeuillian_quartic_at_three' does not depend on any axioms
'ObservationalSUCC.PiNormalitySpine.exceptional_order_sum_bound_twenty' does not depend on any axioms
```

**Key Proof Metrics:**
- Total kernel declarations: 18
- Axiom-free declarations: 11
- Standard propositional/quotient declarations: 7
- Non-constructive axioms (`Classical.choice`): **ZERO**
- Unproven axioms (`sorryAx`): **ZERO**

---

## 3. Independent Oracle Execution Log

```text
PASS: PNS-01 verified
PASS: PNS-02 verified
PASS: PNS-03 verified
PASS: PNS-04 verified
PASS: PNS-05 verified
PASS: PNS-06 verified
PASS: PNS-07 verified
PASS: PNS-08 verified
PASS: PNS-09 verified
PASS: PNS-10 verified
PASS: PNS-11 verified
PASS: PNS-12 verified
PASS: PNS-13 verified
PASS: PNS-14 verified
PASS: PNS-15 verified
PASS: PNS-16 verified
PASS: PNS-17 verified
PASS: PNS-18 verified
PASS [Adversarial]: adversarial_perturbed_alpha_detected
PASS [Adversarial]: adversarial_indefinite_matrix_detected
PASS [Adversarial]: adversarial_simultaneous_fixed_point_refuted
PASS [Adversarial]: adversarial_vanishing_denominator_detected
EXACT_SPINE_RECEIPT_VERIFIED
```

---

## 4. SHA-1 Content Hashes

| Path | SHA-1 Hash |
| :--- | :--- |
| `research/2026-11-02/pi_normality_framework_spine/CLAIMS.md` | `976c7c432ae011d0b70d0ceb281c8a8acdbb068c` |
| `research/2026-11-02/pi_normality_framework_spine/EXACT_SPINE_RECEIPT.json` | `0c6832709e1b2068f5c7b966a62da145aa7be1e0` |
| `research/2026-11-02/pi_normality_framework_spine/independent_oracle_spine.py` | `f976613d9adcf02aade020c8be4ea803a5112bdd` |
| `research/2026-11-02/pi_normality_framework_spine/PiNormalitySpineCore.lean` | `bda0c069272e9c044bb45a1e0b563b558d8e8059` |
| `research/2026-11-02/pi_normality_framework_spine/pi_normality_spine_engine.py` | `13b7311131b43bd35cd39d9cda2b7fa6a8039163` |
| `research/2026-11-02/pi_normality_framework_spine/README.md` | `ec25ed1ec726a70ce3177990f9f93c60efc7b11b` |
| `research/2026-11-02/pi_normality_framework_spine/THEOREMS_AND_PROOFS.md` | `02ebee25b70658d5480be49ded044a599d56fef8` |
| `tests/test_pi_normality_framework_spine.py` | `bb5bf1c37a1f7abd844ab369f4d319112904939a` |
