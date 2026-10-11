#!/usr/bin/env python3
"""Reproduce relative-observer SUCC, concept transport and proof-shaped probes.

The tests are exact and finite. The decoder needs the shared source table,
trusted physical testimony and compatible reasoning. No physical infinity,
genuine source authentication, global bit optimality or RH is claimed.
"""
import json

from observational_succ.relative_delta import (
    relative_delta_demo, position_anchored_demo, proof_shape_and_basis_demo,
)


def main():
    prefix = relative_delta_demo()
    position = position_anchored_demo()
    proof = proof_shape_and_basis_demo()
    assert prefix["status"] == "EXACT_RELATIVE_PATH_VALUE_RELAY"
    assert prefix["recipient_knowledge_steps"] == 1
    assert prefix["no_state_snapshot_or_absolute_probe_names_in_steps"] is True
    assert position["status"] == "EXACT_POSITION_ANCHORED_KNOWLEDGE_SUCC"
    assert position["independent_prior_histories"] is True
    assert position["operational_continuation_verified"] is True
    assert position["old_receiver_event_origin_preserved"] == "Bob"
    assert position["additional_sender_local_frames"] == 2
    assert position["relative_informed_steps"] == 1
    assert proof["status"] == "VERIFIED_CONSERVATIVE_PROOF_PROBE_UPGRADE"
    assert proof["new_physical_instrument_created"] is False
    assert proof["option_alone_determined_result"] is False
    assert proof["proof_after_primitive_evidence_determined_result"] is True
    assert proof["proved_value"] == "1"
    assert proof["parity_physically_observed"] is False
    assert proof["frozen_base_minimum_worst_case_bits_for_eight_arbitrary_bits"] == 8
    assert proof["universal_finite_omega_message_claimed"] is False
    print(json.dumps({
        "status":"EXACT_FINITE_RELATIVE_OBSERVER_TRANSPORT",
        "relative_path_value":prefix,
        "position_anchored":position,
        "evolving_proof_basis":proof,
        "physical_quantum_generalization_claimed":False,
        "arbitrary_infinite_completion_transmitted":False,
        "RH_claimed":False,
    },indent=2,sort_keys=True))


if __name__=="__main__":
    main()
