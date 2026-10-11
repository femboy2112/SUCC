#!/usr/bin/env python3
"""Exact sources, ordered observations, proof fibers and square holonomy receipt.

No physical source attestation, realized quantum instrument, novel proof
system or RH claim is inferred from the finite results.
"""
import json

from observational_succ.noncommuting_proof_transport import noncommuting_proof_demo
from observational_succ.holonomy_proof_transport import holonomy_proof_demo


def main():
    event=noncommuting_proof_demo()
    frame=holonomy_proof_demo()
    assert event["status"]=="NONCOMMUTING_SOURCE_PROOF_TRANSPORT_EXACT"
    assert event["all_four_two_action_endpoints"]=="00"
    assert event["AB_parity_original_decodable"] is False
    assert event["BA_parity_original_decodable"] is False
    assert event["AB_vs_BA_partition_refinement"] is False
    assert event["BA_vs_AB_partition_refinement"] is False
    assert event["same_shadow_no_future_adaptive_proof"] is True
    assert event["nondestructive_AB_repairs_original_parity"] is True
    assert event["source_joint_read_repairs_original_parity"] is True
    assert event["bisimulation_agrees_with_independent_BFS_for_all_pairs"] is True
    assert event["pre_source_truth_labels_not_leaked_into_reports"] is True
    assert frame["status"]=="EXACT_NONFLAT_PROOF_TRANSPORT_GALOIS_GF2"
    assert frame["nonflat_holonomy_is_identity"] is False
    assert frame["holonomy_order"]==3
    assert frame["path_aware_source_recovered"] is True
    assert frame["first_bit_path_blind_decodable"] is False
    assert frame["is_zero_path_blind_decodable"] is True
    assert frame["invariant_binary_predicates_out_of_16"]==4
    assert frame["flat_all_16_predicates_path_blind_decodable"] is True
    assert frame["connection_physically_measured"] is False
    assert event["quantum_physical_or_RH_theorem_claimed"] is False
    assert frame["quantum_phase_or_RH_theorem_claimed"] is False
    print(json.dumps({"status":"SOURCE_ORDER_AND_HOLONOMY_TRANSPORT_EXACT",
                      "event":event,"frame":frame},sort_keys=True,indent=2))


if __name__=="__main__":
    main()
