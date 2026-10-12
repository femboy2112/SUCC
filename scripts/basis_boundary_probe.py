#!/usr/bin/env python3
"""Exact user-proposed T({1,4,5},{1,1,1}) and boundary-code receipt.

The math is finite and based on a versioned shared source/probe language.
It does not prove gravitational holography or RH, authenticate physical
source events, execute infinity, or optimize total channel bit cost.
"""
import json

from observational_succ.basis_boundary_transport import finite_boundary_demo


def main():
    j=finite_boundary_demo()
    assert j["status"]=="EXACT_SHARED_BASIS_RELATIVE_BOUNDARY_TRANSPORT"
    assert j["source_packet_directions"]==[1,4,5]
    assert j["source_packet_values"]==[1,1,1]
    assert j["state_transmitted_as_snapshot"] is False
    assert j["receiver_sparse_update_correct"] is True
    assert j["proof_context_value_codes_before"]==3
    assert j["proof_context_value_codes_after"]==1
    assert j["noncommutative_ordered_path_endpoints"]==[3,2]
    assert j["boundary_exact_bandlimited_reconstruction"] is True
    assert j["boundary_unrestricted_high_mode_alias_exists"] is True
    assert j["radial_exact_high_mode_reconstruction"] is True
    assert j["finite_precision_root_six_samples_hide_mode_five"] is True
    assert j["three_of_six_support_min_fixed_bits"]==5
    assert j["critical_line_zero_only_incomplete_for_symmetric_polynomial_family"] is True
    assert j["true_xi_line_zero_locations_claimed_complete"] is False
    assert j["line_zero_control"]["line_zeros_in_both"]==["1/2-i","1/2+i"]
    assert j["line_zero_control"]["extra_offline_zeros_in_one"]==["1/4","3/4"]
    assert j["line_zero_control"]["RH_disproved_or_proved"] is False
    assert j["gravity_holographic_correspondence_proved"] is False
    assert j["total_message_bit_optimality_claimed"] is False
    assert j["RH_claimed"] is False
    print(json.dumps(j,sort_keys=True,indent=2))


if __name__=="__main__":
    main()
