#!/usr/bin/env python3
"""Machine-readable exact conditional source-backaction and debt/Zeno certificate.

Read this with research/2026-10-11/PROOF_BACKACTION_DEBT_ZENO.md:
the no-go is protocol- and source-class-relative, NOT logical, physical, or RH
incompleteness. No infinite physical computation is executed.
"""
import json
from observational_succ.proof_backaction_debt import proof_backaction_debt_demo


def main():
    x=proof_backaction_debt_demo()
    assert x["status"]=="SOURCE_BACKACTION_PROOF_DEBT_AND_ZENO_EXACT"
    assert x["proportional_debt_first_nine_stages"]==[1,1,2,4,7,11,16,22,29]
    assert x["probe_births_proportional_to_new_knowledge"] is True
    assert x["matching_births_no_finite_zero_certificate"] is True
    assert x["all_zero_proportional_source_never_finitely_certified_under_protocol"] is True
    assert x["all_zero_frozen_support_certified_after_three_reads"] is True
    assert x["single_one_refuted_after_one_read"] is True
    assert x["proof_target_mutated_by_support_growth"] is True
    assert x["old_true_forward_transport_universal"] is False
    assert x["old_refutation_forward_transport_universal"] is True
    assert x["rate_matched_precision_shortfall_stage_0"]==1
    assert x["rate_matched_precision_shortfall_stage_4"]==1
    assert x["rate_matched_precision_first_decodable_stage"] is None
    assert x["overtaking_precision_first_decodable_stage"]==1
    assert x["fixed_capacity_eventually_outrun"] is True
    assert x["early_transient_can_decide_despite_later_debt"] is True
    assert x["transient_earlier_proof_remains_in_joint_history"] is True
    assert x["transient_current_channel_loses_decodability"] is False
    assert x["matched_joint_history_cannot_resolve_original_gap"] is False
    assert x["matched_joint_history_digit_depth"] == 1
    assert x["independent_precision_transport_oracle_matched"]==[False]*5
    assert x["zeno_t_four"]=="15/16"
    assert x["zeno_t_eight"]=="255/256"
    assert x["omega_probe_event_executed"] is False
    assert x["unrestricted_positive_support_gluing"] is False
    assert x["source_restricted_positive_support_gluing"] is True
    assert x["vacuous_source_law_is_not_useful_positive_proof"] is False
    assert x["destructive_single_carrier_original_parity_impossible"] is True
    assert x["independent_carrier_restores_original_parity"] is True
    assert x["physical_information_time_or_RH_theorem_claimed"] is False
    print(json.dumps(x, sort_keys=True, indent=2))


if __name__=="__main__":
    main()
