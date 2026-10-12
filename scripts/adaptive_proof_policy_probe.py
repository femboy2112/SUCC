#!/usr/bin/env python3
"""Machine-readable finite, original-source adaptive proof-policy receipt."""
import json
from observational_succ.adaptive_proof_policy import adaptive_policy_demo


def main():
    x=adaptive_policy_demo()
    assert x["status"]=="FINITE_ADAPTIVE_SOURCE_PROOF_GAME_EXACT"
    assert x["destructive_original_parity_winning"] is False
    assert x["destructive_reachable_beliefs"]>1
    assert x["nondestructive_original_parity_winning"] is True
    assert x["nondestructive_worst_case"]==2
    assert x["joint_probe_worst_case"]==1
    assert x["reversible_state_changing_conditional_probe"] is True
    assert x["adaptive_conditional_original_parity_winning"] is True
    assert x["adaptive_conditional_worst_case"]==2
    assert x["any_fixed_two_probe_word_succeeds"] is False
    assert x["adaptive_action_words"]==[
        ["Q","R0"],["Q","R0"],["Q","R1"],["Q","R1"]]
    assert x["original_source_given_to_policy"] is False
    assert x["menus_offered_as_free_readings"] is False
    assert x["actual_hardware_or_RH_theorem_claimed"] is False
    print(json.dumps(x,sort_keys=True,indent=2))


if __name__=="__main__":
    main()
