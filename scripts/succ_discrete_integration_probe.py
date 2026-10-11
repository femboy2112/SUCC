#!/usr/bin/env python3
"""Reproduce exact shared-initial-condition and discrete SUCC derivative transport.

This is a mathematical calculation over rationals. It assumes correctly
sourced increment messages and a separately established polynomial law when
extrapolating a Newton jet. It reports a parallelizable circuit, NOT
physically parallel execution or an RH/Weil/gravitational result.
"""
import json
from observational_succ.succ_discrete_integration import succ_derivative_demo


def main():
    j=succ_derivative_demo()
    assert j["status"]=="EXACT_DISCRETE_SUCC_DERIVATIVE_INTEGRATION"
    assert j["basis_indices"]==[1,2,3,4,5,6]
    assert j["initial_condition_is_receiver_anchored"] is True
    assert j["ordinary_difference_steps"]==4
    assert j["all_intermediate_succ_states_reconstructed"] is True
    assert j["additive_prefix_parallel_dependency_layers"]==2
    assert j["additive_prefix_executed_on_actual_parallel_hardware"] is False
    assert j["polynomial_degree_law"]==2
    assert j["polynomial_reconstructed_states"]==25
    assert j["polynomial_jet_directions_count"]==2
    assert j["law_premise_proved_from_finite_samples_alone"] is False
    assert j["covariant_frame_transport_square_commutes"] is True
    assert j["affine_parallel_dependency_layers"]==1
    assert j["affine_prefix_actually_parallel_executed"] is False
    assert j["real_world_source_measurement_authenticated"] is False
    assert j["RH_claimed"] is False
    print(json.dumps(j,sort_keys=True,indent=2))


if __name__=="__main__":
    main()
