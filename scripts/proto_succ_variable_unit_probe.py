#!/usr/bin/env python3
"""Exact variable one-unit proto-SUCC and unipotent higher derivative receipt.

Formal d is a unit ADDRESS in the universal model; only a p-local invertible
d is a coordinate-gauge change over an entire finite p-clock. No physical
measurement/proof horizon or new zeta gamma continuation is asserted.
"""
import json

from observational_succ.proto_succ_variable_unit import variable_proto_succ_demo


def main():
    x=variable_proto_succ_demo()
    assert x["status"]=="VARIABLE_UNIT_PROTO_SUCC_UNIPOTENT_LIFT"
    assert x["formal_original_one_step"]=="0 -> D"
    assert x["formal_first_five_addresses_in_D_units"]==[0,1,2,3,4]
    assert x["S_one_is_D_equals_one_specialization"] is True
    assert x["SUCC_unit_is_separate_from_absolute_coordinate_one"] is True
    assert x["S_unit_mod_25_with_unit_two_period"]==25
    assert x["unit_inverse_mod_25"]==13
    assert x["normalized_shift_dilation_defect"]=="1-p"
    assert x["raw_shift_dilation_defect"]=="D*(1-p)"
    assert x["symbolic_unit_must_not_be_automatically_assumed_invertible"] is True
    assert x["higher_order_SUCC_jet_formula"]=="x_n=sum_k binom(n,k) Delta^k x_0"
    assert x["quadratic_d0_two_acceleration_three"]==[0,2,7,15,26,40]
    assert x["higher_order_integer_binomial_formula"] is True
    assert x["linear_step_unit_stability_iff_d0_unit_and_acceleration_divisible_by_p"] is True
    assert x["stable_d0_two_a_five_mod_p_five"]["full_clock_gauge_valid_at_every_n"] is True
    assert x["stable_d0_two_a_five_mod_p_five"]["first_nonunit_succ_index"] is None
    assert x["unstable_d0_one_a_four_mod_p_five"]["full_clock_gauge_valid_at_every_n"] is False
    assert x["unstable_d0_one_a_four_mod_p_five"]["first_nonunit_succ_index"]==1
    assert x["changing_unit_can_stop_being_a_local_clock_unit"]["initial_unit_clock_period"]==25
    assert x["changing_unit_can_stop_being_a_local_clock_unit"]["updated_nonunit_clock_period"]==5
    assert x["changing_unit_can_stop_being_a_local_clock_unit"]["same_full_clock_coordinate_isomorphism_survives"] is False
    assert x["d_zero_specialization_loses_normalized_defect_information"] is True
    assert x["prime_jet_clock_period_identity_requires_declared_local_unit"] is True
    assert x["new_RH_Gamma_or_Kubota_Leopoldt_theorem_claimed"] is False
    print(json.dumps(x, sort_keys=True, indent=2))


if __name__=="__main__":
    main()
