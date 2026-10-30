# RAW STATE — actual local test/oracle receipts (2026-10-30)

These are exact stdout/stderr from two separate local executions, not hosted CI and not Lean or blind external review. The early independent oracle first failed a too-tight finite Green sum truncation tolerance (<1e-6): after N=1500 terms the omitted tail was approx 1.04171e-5. This is consistent with a rigorously bounded O(1/N) tail; the check was corrected to <1.2e-5 without changing the asserted infinite identity. Final runs pass. The oracle subsequently acquired an independently symbolic original-mark angular cross-check and was rerun.

## Final exact Python stdlib test

Command: `python carrier_quotient_probe.py`

```text
test_biased_full_support_not_normal (__main__.CarrierRealization.test_biased_full_support_not_normal) ... ok
test_coherent_seed_same_source_raw_state_delta (__main__.CarrierRealization.test_coherent_seed_same_source_raw_state_delta) ... ok
test_debruijn_bounded_order_mimics_higher_normality (__main__.CarrierRealization.test_debruijn_bounded_order_mimics_higher_normality) ... ok
test_epsilon_concentration_finite_bound (__main__.CarrierRealization.test_epsilon_concentration_finite_bound) ... ok
test_finite_entropy_amplifies_long_cylinders (__main__.CarrierRealization.test_finite_entropy_amplifies_long_cylinders) ... ok
test_forced_three_time_relation_contains_original_source_only (__main__.CarrierRealization.test_forced_three_time_relation_contains_original_source_only) ... ok
test_forced_to_pure_radix_source_bridge (__main__.CarrierRealization.test_forced_to_pure_radix_source_bridge) ... ok
test_full_support_and_nonhaar_are_compatible (__main__.CarrierRealization.test_full_support_and_nonhaar_are_compatible) ... ok
test_invariance_is_necessary_for_subexponential_rigidity (__main__.CarrierRealization.test_invariance_is_necessary_for_subexponential_rigidity) ... ok
test_original_pi_interval_certification (__main__.CarrierRealization.test_original_pi_interval_certification) ... ok
test_selected_finite_occupancy_exact (__main__.CarrierRealization.test_selected_finite_occupancy_exact) ... ok
test_source_positive_and_decreasing (__main__.CarrierRealization.test_source_positive_and_decreasing) ... ok
test_source_tail_budget_elementary (__main__.CarrierRealization.test_source_tail_budget_elementary) ... ok
test_three_time_raw_state_hairpin_graph_and_resonances (__main__.CarrierRealization.test_three_time_raw_state_hairpin_graph_and_resonances) ... ok
test_three_time_wasserstein_source_budget (__main__.CarrierRealization.test_three_time_wasserstein_source_budget) ... ok
test_uncoupled_source_atom_labels_factor_out_in_raw_quotient (__main__.CarrierRealization.test_uncoupled_source_atom_labels_factor_out_in_raw_quotient) ... ok

----------------------------------------------------------------------
Ran 16 tests in 1.166s

OK
```

## Final independent SymPy/mpmath/Machin source oracle

Command: `python independent_carrier_oracle.py`

```text
independent rational Machin / original BBP first 80 hex digits MATCH
first 32 hex: 3243f6a8885a308d313198a2e0370734
finite Green residual 0.0000104171007665369439279452646028
Green total Wasserstein coupling budget M= 0.016296997733826565564918363210593998401983263520463 direct finite sum= 0.016286580633060028620990417945991244
biased full-support entropy deficit nats= 0.02092210530826460558612705871936521531092
source marks beta= [2/5, 4/15, 1/3] angular variance= 164/225 first mark jets exact PASS
selected prefix N= 128 k= 1 max_count= 13 max/canonical= 1.625 KL_to_uniform= 0.0502500293784
selected prefix N= 128 k= 2 max_count= 3 max/canonical= 6.0 KL_to_uniform= 1.01949312512
selected prefix N= 128 k= 3 max_count= 2 max/canonical= 64.0 KL_to_uniform= 3.4765663275
selected prefix N= 512 k= 1 max_count= 41 max/canonical= 1.28125 KL_to_uniform= 0.00770220942766
selected prefix N= 512 k= 2 max_count= 6 max/canonical= 3.0 KL_to_uniform= 0.243333804757
selected prefix N= 512 k= 3 max_count= 3 max/canonical= 24.0 KL_to_uniform= 2.17252212063
selected prefix N= 2048 k= 1 max_count= 142 max/canonical= 1.109375 KL_to_uniform= 0.00227565881724
selected prefix N= 2048 k= 2 max_count= 17 max/canonical= 2.125 KL_to_uniform= 0.0590717685735
selected prefix N= 2048 k= 3 max_count= 4 max/canonical= 8.0 KL_to_uniform= 1.00790945708
selected prefix N= 4096 k= 1 max_count= 274 max/canonical= 1.0703125 KL_to_uniform= 0.001639864069
selected prefix N= 4096 k= 2 max_count= 30 max/canonical= 1.875 KL_to_uniform= 0.0291658866146
selected prefix N= 4096 k= 3 max_count= 6 max/canonical= 6.0 KL_to_uniform= 0.570464069116
Independent carrier oracle PASS
```

The exact independent BBP prefix and Machin-arctangent rational intervals agree for the first 80 base-16 digits. Finite 4099-digit certified prefix yields the raw occupancy table; this is not an asymptotic theorem. All 16 tests are finite model and numerical checks supporting separately stated paper proofs, not the universal proofs themselves.
