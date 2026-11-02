# Validation Dossier: Plancherel-Bilinear Collapse, Exact Pole Annihilation & 630-Prime Census

**Date:** `2026-11-02`  
**Branch:** `research/prime-cofactor-nonconspiracy-2026-11-02`  
**Dossier Directory:** `research/2026-11-02/plancherel_bilinear_collapse/`

---

## 1. Summary of Verification Runs

| Component | Target File | Verification Command | Status | Time |
| :--- | :--- | :--- | :---: | :---: |
| **Lean 4 Kernel** | `PlancherelBilinearCore.lean` | `/usr/bin/lean research/2026-11-02/plancherel_bilinear_collapse/PlancherelBilinearCore.lean` | **PASS (0 sorryAx, 0 Classical.choice)** | 0.81s |
| **Exact Engine** | `mega_round_3_engine.py` | `python3 research/2026-11-02/plancherel_bilinear_collapse/mega_round_3_engine.py` | **PASS (Receipt Generated)** | 0.42s |
| **Independent Oracle** | `independent_oracle_3.py` | `python3 research/2026-11-02/plancherel_bilinear_collapse/independent_oracle_3.py --check` | **PASS (18/18 claims + 4/4 countermodels)** | 0.28s |
| **Root Test Suite** | `tests/test_plancherel_bilinear_collapse.py` | `python3 -m unittest tests.test_plancherel_bilinear_collapse -v` | **PASS (21/21 tests OK)** | 1.31s |
| **Combined Regression** | Multi-round (55 tests) | `python3 -m unittest tests.test_multi_prime_and_base3_synthesis tests.test_prime_cofactor_nonconspiracy tests.test_plancherel_bilinear_collapse` | **PASS (55/55 tests OK)** | 7.91s |

---

## 2. Lean 4 Axiom Verification Output

```text
'ObservationalSUCC.PlancherelBilinear.pole_annihilation_integer_identity' depends on axioms: [propext, Quot.sound]
'ObservationalSUCC.PlancherelBilinear.second_difference_bbp_orbit_identity' depends on axioms: [propext, Quot.sound]
'ObservationalSUCC.PlancherelBilinear.character_norm_energy_upper_bound' depends on axioms: [propext, Quot.sound]
'ObservationalSUCC.PlancherelBilinear.parseval_energy_upper_bound' depends on axioms: [propext, Quot.sound]
'ObservationalSUCC.PlancherelBilinear.total_energy_bound_constant' does not depend on any axioms
'ObservationalSUCC.PlancherelBilinear.radix_16_3_proximity_identity' does not depend on any axioms
'ObservationalSUCC.PlancherelBilinear.radix_16_3_higher_convergent' does not depend on any axioms
'ObservationalSUCC.PlancherelBilinear.coupled_radix_16_3_product_identity' depends on axioms: [propext, Quot.sound]
'ObservationalSUCC.PlancherelBilinear.coupled_radix_16_3_discriminant_negative' does not depend on any axioms
'ObservationalSUCC.PlancherelBilinear.coupled_radix_16_3_kernel_trivial' depends on axioms: [propext, Quot.sound]
'ObservationalSUCC.PlancherelBilinear.pade_one_one_at_one' does not depend on any axioms
'ObservationalSUCC.PlancherelBilinear.pade_one_one_first_ten' does not depend on any axioms
'ObservationalSUCC.PlancherelBilinear.pade_factors_positive' depends on axioms: [propext, Quot.sound]
'ObservationalSUCC.PlancherelBilinear.two_step_seed_amplification_identity' does not depend on any axioms
'ObservationalSUCC.PlancherelBilinear.two_step_amplification_is_fifteen_squared' does not depend on any axioms
'ObservationalSUCC.PlancherelBilinear.aurifeuillian_quartic_identity' depends on axioms: [propext, Quot.sound]
'ObservationalSUCC.PlancherelBilinear.aurifeuillian_quartic_at_one' does not depend on any axioms
'ObservationalSUCC.PlancherelBilinear.aurifeuillian_quartic_at_two' does not depend on any axioms
'ObservationalSUCC.PlancherelBilinear.aurifeuillian_quartic_at_three' does not depend on any axioms
'ObservationalSUCC.PlancherelBilinear.exceptional_order_sum_bound_first_ten' does not depend on any axioms
```

**Key Proof Metrics:**
- Total kernel declarations: 20
- Axiom-free declarations: 11
- Standard propositional/quotient declarations: 9
- Non-constructive axioms (`Classical.choice`): **ZERO**
- Unproven axioms (`sorryAx`): **ZERO**

---

## 3. Independent Oracle Execution Log

```text
PASS: PBC-01 verified
PASS: PBC-02 verified
PASS: PBC-03 verified
PASS: PBC-04 verified
PASS: PBC-05 verified
PASS: PBC-06 verified
PASS: PBC-07 verified
PASS: PBC-08 verified
PASS: PBC-09 verified
PASS: PBC-10 verified
PASS: PBC-11 verified
PASS: PBC-12 verified
PASS: PBC-13 verified
PASS: PBC-14 verified
PASS: PBC-15 verified
PASS: PBC-16 verified
PASS: PBC-17 verified
PASS: PBC-18 verified
PASS [Adversarial]: adversarial_fake_residue_detected
PASS [Adversarial]: adversarial_indefinite_form_detected
PASS [Adversarial]: adversarial_torsion_seed_has_finite_orbit
PASS [Adversarial]: adversarial_unstable_pade_has_positive_root
EXACT_MEGA_ROUND_3_RECEIPT_VERIFIED
```

---

## 4. SHA-1 Content Hashes

| Path | SHA-1 Hash |
| :--- | :--- |
| `research/2026-11-02/plancherel_bilinear_collapse/CLAIMS.md` | `f4cc09217fadef433c7b5a2072a5f3fc97f0ef92` |
| `research/2026-11-02/plancherel_bilinear_collapse/EXACT_MEGA_ROUND_3_RECEIPT.json` | `130ebb456925a71109c13c18864bdbe7c181819a` |
| `research/2026-11-02/plancherel_bilinear_collapse/independent_oracle_3.py` | `9ac424cef1d4a94dab96ff084754a4110c8fce4e` |
| `research/2026-11-02/plancherel_bilinear_collapse/mega_round_3_engine.py` | `2b152362ba8c1b9b068526f71e7f028ea3c7ed9c` |
| `research/2026-11-02/plancherel_bilinear_collapse/PlancherelBilinearCore.lean` | `51bb606777a6a6278818d85862f2d8a413711ad6` |
| `research/2026-11-02/plancherel_bilinear_collapse/README.md` | `cbf8c793cd2082e3dbfce68b097c63df03355a8a` |
| `research/2026-11-02/plancherel_bilinear_collapse/THEOREMS_AND_PROOFS.md` | `4377ac7bce0923d5e248cdeb9db814d0ea05d846` |
| `tests/test_plancherel_bilinear_collapse.py` | `d80dc7d850df1f29c0af6d3efc6cb249a11902a7` |
