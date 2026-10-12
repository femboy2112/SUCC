#!/usr/bin/env python3
"""Exact finite prime-to-Archimedean zeta(-1) transport receipt.

The classical analytic continuation, functional equation and Basel theorem
are external mathematical proof inputs. The finite prime products and tail
bounds are computed as exact fractions. No nontrivial zeros are read.
"""
import json

from observational_succ.zeta_minus_one_transport import (
    zeta_minus_one_transport_demo,
)


def main():
    x=zeta_minus_one_transport_demo()
    assert x["status"]=="ZETA_MINUS_ONE_GLOBAL_EULER_ARCHIMEDEAN_TRANSPORT"
    assert x["local_prime_minus_one_factor"]=="-1/(p-1)"
    assert x["prime_jet_first_return_gap"]=="p-1"
    assert x["shift_dilation_one_step_address_defect"]=="1-p"
    assert x["ax_b_operator_semigroup_relation"]=="V_p S = S^p V_p"
    assert x["same_shift_dilation_defect_rule_for_composite_six"] is True
    assert x["nonprime_affine_defect_does_not_authorize_euler_prime_factor"] is True
    assert x["operator_commutator_claimed_scalar"] is False
    assert x["cuntz_ax_b_finite_arch_completion_proved_here"] is False
    assert x["global_zeta_minus_one_value"]=="-1/12"
    assert x["completed_zeta_symmetric_values"]=="Lambda(-1)=Lambda(2)=pi/6"
    assert x["bost_connes_classical_diagonal_hamiltonian"]=="H|n> = log(n)|n>"
    assert x["bost_connes_partition_function_for_beta_gt_one_is_zeta"] is True
    assert x["bost_connes_positive_beta_two_finite_trace_n_four"]=="205/144"
    assert x["bost_connes_beta_minus_one_finite_trace_n_four"]=="10"
    assert x["bost_connes_analytic_zeta_minus_one_is_not_ordinary_trace"] is True
    assert x["bost_connes_operator_algebra_or_KMS_state_constructed_here"] is False
    assert x["local_factor_partial_products_tend_to_zero"] is True
    assert x["local_continuation_and_global_product_commute"] is False
    assert x["positive_side_prime_product_converges"] is True
    assert x["finite_positive_prime_cutoffs_with_rigorous_tail_bound"][-1]["cutoff"]==47
    assert x["abel_eta_negative_one"]=="1/4"
    assert x["eta_to_zeta_factor_at_minus_one"]=="-3"
    assert x["negative_odd_s_minus_three"]=="1/120"
    assert x["prime_source_mutation_controls"]["two_deletion_analytic_value"]=="1/12"
    assert x["prime_source_mutation_controls"]["two_deletion_bad_reused_zeta_reflection"]=="-1/16"
    assert x["prime_source_mutation_controls"]["fake_six_is_not_a_prime_euler_factor"] is True
    assert x["analytic_continuation_and_functional_equation_are_imported_theorems"] is True
    assert x["source_specific_euler_gamma_completed_weil_RH_bridge_proved"] is False
    assert x["nontrivial_zeta_zeros_used_as_inputs"] is False
    assert x["RH_claimed"] is False
    print(json.dumps(x,indent=2,sort_keys=True))


if __name__=="__main__":
    main()
