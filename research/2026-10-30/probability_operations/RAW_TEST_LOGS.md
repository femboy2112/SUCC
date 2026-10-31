# Probability-operation tests — raw receipts

## Exact stdlib test source

Command: `python probability_operations_probe.py`

```
test_coherent_seed_operator_residual_is_strong (__main__.ProbabilityOperationTests.test_coherent_seed_operator_residual_is_strong) ... ok
test_consecutive_tails_are_not_independent_even_for_normal_digits (__main__.ProbabilityOperationTests.test_consecutive_tails_are_not_independent_even_for_normal_digits) ... ok
test_exact_fair_digit_branch_law (__main__.ProbabilityOperationTests.test_exact_fair_digit_branch_law) ... ok
test_idempotent_convolution_not_unique_without_no_atoms (__main__.ProbabilityOperationTests.test_idempotent_convolution_not_unique_without_no_atoms) ... ok
test_if_one_step_operation_defect_vanishes_unique_haar (__main__.ProbabilityOperationTests.test_if_one_step_operation_defect_vanishes_unique_haar) ... ok
test_original_four_pole_and_source_certified_prefix (__main__.ProbabilityOperationTests.test_original_four_pole_and_source_certified_prefix) ... ok
test_periodic_uniform_first_digit_not_normal (__main__.ProbabilityOperationTests.test_periodic_uniform_first_digit_not_normal) ... ok
test_quantized_uniform_blocks_approximate_sqrt_max_law (__main__.ProbabilityOperationTests.test_quantized_uniform_blocks_approximate_sqrt_max_law) ... ok
test_source_certified_pi_state_operation_residual (__main__.ProbabilityOperationTests.test_source_certified_pi_state_operation_residual) ... ok
test_sqrt_max_beta_false_positive (__main__.ProbabilityOperationTests.test_sqrt_max_beta_false_positive) ... ok
test_sqrt_max_is_distributional_not_pathwise (__main__.ProbabilityOperationTests.test_sqrt_max_is_distributional_not_pathwise) ... ok

----------------------------------------------------------------------
Ran 11 tests in 0.016s

OK
BBP certified n=32, epsilon≈0.115532192, state_w1≈0.122901951, bound≈0.125317672
BBP certified n=128, epsilon≈0.043046657, state_w1≈0.045715792, bound≈0.046437268
BBP certified n=256, epsilon≈0.014679133, state_w1≈0.015136004, bound≈0.015918159
```

## Independent SymPy / mpmath / original rational Machin oracle

Command: `python independent_probability_oracle.py`

```
Normal graph-Haar max(x,T16(x)) CDF at 1/3 = 1/8 versus independent 1/9
Uniform inverse-branch moments m=0..6: PASS
Oily rank 2 D= 0.04081832384836198759807474428 analytic= 0.04081832384836198759807474428
Oily rank 3 D= 0.6867163575986774429843142412 analytic= 0.6867163575986774429843142412
Oily rank 4 D= 1.110219634681485017340581746 analytic= 1.110219634681485017340581746
Oily rank 6 D= 1.650389578430959258363515918 analytic= 1.650389578430959258363515918
Gamma(2) = -log(U1*U2), Oily λ−γ reconstructed: PASS
Independent rational Machin BBP first 80 hex digits: MATCH
Independent exact CDF vs quantile W1: N=32, epsilon=0.115532192401, identities MATCH
Independent exact CDF vs quantile W1: N=128, epsilon=0.043046656679, identities MATCH
Independent exact CDF vs quantile W1: N=256, epsilon=0.014679132558, identities MATCH
Independent probability-operations oracle PASS
```

## Scope

All tests are focused on **declared mathematical constructions and finite exact pi-prefix data**, not an actual infinite π-normality proof. Independent CDF-area and quantile algorithms share the same certified source digits. The high-precision Gamma oracle shares the independently established Gamma/probability definitions. No external referee or whole repository gate was run.
