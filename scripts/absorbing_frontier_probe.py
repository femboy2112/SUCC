#!/usr/bin/env python3
"""Machine-readable independent finite absorbing and communication receipts.

No physical infinity, exact real-bit universal encoder, classical LEM
refutation, neural ontology theorem or RH result is claimed.
"""
import json

from observational_succ.absorbing_frames import absorbing_demo
from observational_succ.constructive_frontier import (
    intuitionistic_lem_demo, omega_plus_one_demo, fixed_width_message_capacity)
from observational_succ.interobserver_channels import chromatic_channel_demo


def main():
    closure = absorbing_demo()
    logic = intuitionistic_lem_demo()
    omega = omega_plus_one_demo()
    channel = chromatic_channel_demo()
    assert closure["status"] == "FINITE_ABSORBING_HARD_SUCC_CERTIFIED"
    assert closure["full_hard_succ_identified"] is True
    assert closure["blocked_epistemically_known"] == ["fine"]
    assert closure["physical_barrier_remaining_candidates"] == ["A", "B"]
    assert closure["authenticated_real_world_source"] is False
    assert logic["status"] == "FINITE_KRIPKE_CONSTRUCTIVE_LEM_COUNTERMODEL"
    assert logic["root_forces_P_or_not_P"] is False
    assert logic["classical_excluded_middle_invalidated"] is False
    assert omega["status"] == "SYMBOLIC_NON_OMEGA_CONTINUOUS_CLOSURE"
    assert omega["omega_plus_one_contains_seal"] is True
    assert omega["physical_infinite_iteration_executed"] is False
    assert channel["status"] == "EXACT_INTEROBSERVER_ZERO_ERROR_CHANNEL"
    assert channel["minimum_fixed_width_bits"] == 1
    assert channel["naive_sender_id_fixed_width_bits"] == 2
    assert fixed_width_message_capacity(1) == 2
    result = {
        "status": "ABSORBING_SUCC_FINITE_THEOREM_CONTROLS",
        "absorbing": closure,
        "constructive_logic": logic,
        "omega_limit": omega,
        "finite_channel": channel,
        "unrestricted_real_exact_bit_transmission_claimed": False,
        "RH_claimed": False,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
