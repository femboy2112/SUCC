#!/usr/bin/env python3
"""Reproduce the exact finite proof-carrier coherence horizon and its repairs.

This benchmark is NOT a theorem that mathematical proof or RH is impossible.
Only a single destructive classical carrier is disallowed from being copied
or nondestructively probed in the negative control. Positive controls show
precisely which hypotheses must change for proof actualization to work.
"""
import json

from observational_succ.probe_coherence import probe_coherence_demo


def main():
    r=probe_coherence_demo()
    assert r["status"]=="FINITE_SINGLE_CARRIER_SOURCE_COHERENCE_NO_GO"
    assert r["all_initial_sources"]==4
    assert r["proof_support_unreachable_with_one_carrier"] is True
    assert r["after_read_a_original_b_still_meaningful"] is False
    assert r["after_read_b_original_a_still_meaningful"] is False
    assert r["second_probe_current_value_is_still_defined"] is True
    assert r["second_probe_original_source_value_is_no_longer_defined"] is True
    assert r["proof_graph_rewiring"]["status"]=="PROOF_INDUCED_MINIMAL_DEPENDENCY_REWIRING"
    assert r["proof_graph_rewiring"]["unrestricted_minimal_probe_supports"]==[["a","b"]]
    assert r["proof_graph_rewiring"]["with_verified_a_zero_law"]==[["b"]]
    assert r["proof_graph_rewiring"]["with_verified_a_equal_b_law"]==[[]]
    assert r["two_independent_preparations_repair_target"] is True
    assert r["non_destructive_probe_repairs_target"] is True
    assert r["lawful_source_prior_can_decide_without_experiment"] is True
    assert r["global_logical_unprovability_claimed"] is False
    assert r["RH_claimed"] is False
    print(json.dumps(r,sort_keys=True,indent=2))


if __name__=="__main__":
    main()
