# Standalone raw test receipt — 2026-10-30

**Executed locally:**

    python model_carrier_probe.py

    test_coarse_observer_not_closed_under_radix_dynamics ... ok
    test_coherent_carrier_invariant_but_fair_model_disagrees ... ok
    test_exact_finite_future_conditioning_changes_with_resolution ... ok
    test_exact_radix_inverse_is_a_rechart_not_fairness ... ok
    test_fair_operation_contracts_w1_exactly ... ok
    test_fiber_property_needs_constancy_on_equal_model_states ... ok
    test_full_support_biased_bernoulli_branch_deficit ... ok
    test_model_only_iterations_always_approach_haar ... ok
    test_original_four_pole_source_is_not_a_fair_branch_law ... ok
    test_periodic_zero_bernoulli_deficit_is_log16 ... ok
    test_selected_carry_lift_distinguishes_late_circle_alias ... ok
    test_two_cycle_invariant_but_not_fair ... ok

    Ran 12 tests in 0.109s
    OK

**Separately implemented independent_oracle.py:** After repairing initial SyntaxError unmatched parenthesis, final PASS:
- Finite x=1/257 four-cycle: H(D | first future digit)=0.6931471805599453; two future digits=0.
- Biased Bernoulli source: exact KL=log(64/15)/2; entropy rate=log16−KL.
- Fair generator iterations k=1..4: grid supports 16,256,4096,65536 and exact W1 to Haar 1/32,1/512,1/8192,1/131072.
- Actual coherent carrier vs fair model W1=15/32.
- Original four-pole rational and exact Green-tail truncation residual verified.
- Finite-k Pinsker calibration computed.
- Independent SymPy/mpmath oracle PASS.

No complete root suite/hosted CI/Lean/external review was executed. Record initial parser failure rather than silently counting it as a successful run.
