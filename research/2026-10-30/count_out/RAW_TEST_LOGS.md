# Operation COUNT-OUT — raw executed receipts

**Date:** 2026-10-30. Exact source files: `counting_quotient_probe.py` and `independent_oracle.py` in this research package. All outputs below captured from local commands at this turn; no hosted CI results are claimed.

## Exact rational and combinatorial suite

Command: `python counting_quotient_probe.py`

```text
test_34th_moment_count_subtraction_from_direct_group_algebra (__main__.CountingQuotient.test_34th_moment_count_subtraction_from_direct_group_algebra) ... ok
test_bounded_boundary_counting_trilemma (__main__.CountingQuotient.test_bounded_boundary_counting_trilemma) ... ok
test_carry_cocycle_and_coherent_seed_exact (__main__.CountingQuotient.test_carry_cocycle_and_coherent_seed_exact) ... ok
test_counting_quotient_exact_fast_pair_factorization (__main__.CountingQuotient.test_counting_quotient_exact_fast_pair_factorization) ... ok
test_first_balance_radix_count_collision_exact (__main__.CountingQuotient.test_first_balance_radix_count_collision_exact) ... ok
test_full_asymptotic_constant_after_counting_quotient (__main__.CountingQuotient.test_full_asymptotic_constant_after_counting_quotient) ... ok
test_linear_34th_defect_coefficient_h1 (__main__.CountingQuotient.test_linear_34th_defect_coefficient_h1) ... ok
test_normality_not_inherited_by_counting_projection (__main__.CountingQuotient.test_normality_not_inherited_by_counting_projection) ... ok
test_original_source_word_counting_quotient_exact (__main__.CountingQuotient.test_original_source_word_counting_quotient_exact) ... ok
test_perron_operator_erases_selected_coherent_seed (__main__.CountingQuotient.test_perron_operator_erases_selected_coherent_seed) ... ok
test_second_order_counting_defect_bounded_remainder (__main__.CountingQuotient.test_second_order_counting_defect_bounded_remainder) ... ok
test_source_blind_history_given_total_and_oily_tilt (__main__.CountingQuotient.test_source_blind_history_given_total_and_oily_tilt) ... ok
test_source_four_poles_original_contract (__main__.CountingQuotient.test_source_four_poles_original_contract) ... ok
test_three_panel_same_grade_distinct_selected_carries (__main__.CountingQuotient.test_three_panel_same_grade_distinct_selected_carries) ... ok
test_unique_bounded_future_correction_exact_finite_horizon (__main__.CountingQuotient.test_unique_bounded_future_correction_exact_finite_horizon) ... ok

----------------------------------------------------------------------
Ran 15 tests in 2.546s

OK
```

## Separately authored high-precision oracle

Command: `python independent_oracle.py`

```text
N=5 independent exact collision/orbit defect 294.63761546625861495246245322708246
original source digamma S_R 3.38604761959719172193641883143841286
A1 quotient source dephasing 0.362366763550539264432353824612140803
S1 source sine sum (digamma corrected) 1.49755381444151724881328288305181132
B1 adjacent source dispersion 0.157417231288605269809069499713284535
C1 quotient constant -981.16234461232343612188319209512411
certified A1 tail upper 4.5185393829444145e-14
sine-minus-linear correction tail upper 3.3273403852308289e-23
Independent symbolic and high-precision quotient oracle PASS
```

## First rejected controls and repairs

1. **Initial 34th-moment numerical cancellation:** a test subtracted two enormous floating-point Haar moments. It produced an apparent zero defect although the exact group-algebra loss was ~294.637615466... at N=5. The final test accumulates exact-class per-pair dephasing instead and verifies the O(N) formula. The problem was numerical subtraction, not a failure of the finite combinatorial identity.
2. **Finite-tail terminal carry:** the initially expected constant coherent carry 15 at the artificial finite Green horizon M was false: the truncation T_M=0 makes the final carry 16. The *infinite* coherent tail T_n>0 has carry 15 for every n. Final tests preserve the terminal exception and verify it exactly. A boundary change is not silently assimilated into the carrier.
3. **Truncated sine sum masquerading as infinite constant:** direct partial summation of Σ sin(2πr_n) at cutoff 100000 misses an O(1/cutoff) tail and gave C≈−981.1496 instead of the true C≈−981.1623446123. Final independent oracle uses the exact digamma Σr_n and sums only sin(t r_n)−t r_n, whose tail is O(cutoff^−5). The standalone tests label truncated C as approximate and compare with an appropriate tolerance.

The independent exact F-rational source and direct group-algebra computations share the same model definitions. They are different implementations but not independent external mathematical referees. The mathematical all-N statements follow from the paper derivations and stated classical inputs, not finite output counts.
