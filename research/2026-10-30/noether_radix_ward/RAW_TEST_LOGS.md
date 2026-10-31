# Noether / radix Ward — raw executed logs (2026-10-30)

Unmodified output of final tested local files; standalone runs, not complete SUCC CI.

## noether_probe.log

```text
test_discrete_cotangent_lift_noether_symmetry (__main__.NoetherBBP.test_discrete_cotangent_lift_noether_symmetry) ... ok
test_fixed_prefix_cannot_identify_unique_seed (__main__.NoetherBBP.test_fixed_prefix_cannot_identify_unique_seed) ... ok
test_mod_one_branch_winding_not_curvature (__main__.NoetherBBP.test_mod_one_branch_winding_not_curvature) ... ok
test_no_discard_carry_lift_reconstructs_circle_seed (__main__.NoetherBBP.test_no_discard_carry_lift_reconstructs_circle_seed) ... ok
test_original_four_poles_and_positive_source (__main__.NoetherBBP.test_original_four_poles_and_positive_source) ... ok
test_scalar_relative_phase_has_zero_lifted_loop (__main__.NoetherBBP.test_scalar_relative_phase_has_zero_lifted_loop) ... ok
test_unwrapped_source_corrected_seed_is_exact_first_integral (__main__.NoetherBBP.test_unwrapped_source_corrected_seed_is_exact_first_integral) ... ok
test_3d_local_charge_survives_accelerating_bond (__main__.NoetherWave.test_3d_local_charge_survives_accelerating_bond) ... ok
test_continuous_observer_carrier_noether_energy_exchange (__main__.NoetherWave.test_continuous_observer_carrier_noether_energy_exchange) ... ok
test_exact_discrete_energy_work_balance (__main__.NoetherWave.test_exact_discrete_energy_work_balance) ... ok
test_four_pole_59_square_in_observer_coupling (__main__.NoetherWave.test_four_pole_59_square_in_observer_coupling) ... ok
test_local_continuity_with_complex_source_and_boundary_flux (__main__.NoetherWave.test_local_continuity_with_complex_source_and_boundary_flux) ... ok
test_noether_charge_does_not_force_cancellation (__main__.NoetherWave.test_noether_charge_does_not_force_cancellation) ... ok
test_phase_invariant_discrete_action_and_local_spatial_gauge (__main__.NoetherWave.test_phase_invariant_discrete_action_and_local_spatial_gauge) ... ok
test_pure_gauge_loop_vs_true_link_holonomy (__main__.NoetherWave.test_pure_gauge_loop_vs_true_link_holonomy) ... ok
test_source_fitted_ward_is_vacuous_for_any_phase_word (__main__.NoetherWave.test_source_fitted_ward_is_vacuous_for_any_phase_word) ... ok
test_static_geometry_energy_conserved_and_phase_charge_conserved (__main__.NoetherWave.test_static_geometry_energy_conserved_and_phase_charge_conserved) ... ok
test_time_dependent_geometry_preserves_global_charge (__main__.NoetherWave.test_time_dependent_geometry_preserves_global_charge) ... ok

----------------------------------------------------------------------
Ran 18 tests in 0.084s

OK
```

## radix_ward_probe.log

```text
test_balanced_moment_first_fourth_and_all_below_17_are_seed_blind (__main__.RadixMomentSelection.test_balanced_moment_first_fourth_and_all_below_17_are_seed_blind) ... ok
test_base_b_thresholds_and_exact_source_coboundary (__main__.RadixMomentSelection.test_base_b_thresholds_and_exact_source_coboundary) ... ok
test_exponentially_small_seed_cylinder_has_explicit_transfer_error (__main__.RadixMomentSelection.test_exponentially_small_seed_cylinder_has_explicit_transfer_error) ... ok
test_first_balanced_34th_moment_complete_offdiagonal_formula (__main__.RadixMomentSelection.test_first_balanced_34th_moment_complete_offdiagonal_formula) ... ok
test_first_equal_length_collision_phase_is_source_only (__main__.RadixMomentSelection.test_first_equal_length_collision_phase_is_source_only) ... ok
test_first_radix_carry_signed_moment_has_no_weyl_saving (__main__.RadixMomentSelection.test_first_radix_carry_signed_moment_has_no_weyl_saving) ... ok
test_first_unbalanced_sixteen_to_one_resonance (__main__.RadixMomentSelection.test_first_unbalanced_sixteen_to_one_resonance) ... ok
test_four_pole_source_and_shift_character (__main__.RadixMomentSelection.test_four_pole_source_and_shift_character) ... ok
test_low_equal_length_moments_have_no_additive_collisions (__main__.RadixMomentSelection.test_low_equal_length_moments_have_no_additive_collisions) ... ok
test_radix_selection_rule_for_unbalanced_moments (__main__.RadixMomentSelection.test_radix_selection_rule_for_unbalanced_moments) ... ok

----------------------------------------------------------------------
Ran 10 tests in 0.049s

OK
```

## noether_independent_oracle.log

```text
Original source R(a), 59², coupled observer+field Noether energy, discrete EL: EXACT PASS
16-to-1 source-only radix carry resonance: (4.639398327388934461417285277 - 1.247161880760353207691262681j)
Exponential seed cylinder local average vs selected seed: (0.647724456586019887643665 + 2.84506263266124363858712j) (0.175165280361496752767773 + 2.175849948600363029771j)
Difference 0.81924220566445911017 bound 6.7020643276582255754
Independent SymPy/mpmath oracle PASS
```

## radix_ward_independent_oracle.log

```text
N 4 first 34th balanced moment value: 1480129751586117359.131913
34th moment minus its diagonal: 511.1319134836238660722069
17-factor unbalanced source Ward moment: (2.643699118134018423888197 - 1.118714784913380678667413j)
localized seed cylinder vs exact selected sum: (0.4046760688614825035 + 2.718023562234205763j) (1.584511807243336506 + 2.507487716419684397j)
Independent 90-digit first-collision / source-resonance oracle PASS
```
