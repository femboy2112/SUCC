#!/usr/bin/env python3
"""Exact prime-local modular SUCC/FUCC Yoneda provenance and quotient receipt."""
import json
from observational_succ.prime_clock_yoneda import arithmetic_yoneda_demo


def main():
    x=arithmetic_yoneda_demo()
    assert x["status"]=="AUTHENTIC_PRIME_SUCC_FUCC_YONEDA_TRANSPORT_EXACT"
    assert x["fine_source_modulus"]==4
    assert x["coarse_source_modulus"]==2
    assert x["genuine_prime_place"]==2
    assert x["genuine_prime_jet"]==3
    assert x["fine_noncommuting_defect"]==2
    assert x["coarse_defect"]==0
    assert x["fine_nonflat_coarse_flat"] is True
    assert x["coarse_source_rank_preserved"] is True
    assert x["both_original_source_ranks_with_read"]==[1,1]
    assert x["both_original_source_ranks_without_read"]==[None,None]
    assert x["induced_actual_observation_functor_verified"] is True
    assert x["ring_source_map_independent_of_simulated_outcomes"] is True
    assert x["different_true_prime_jet_behavioral_alias_exists"] is True
    assert x["declared_jet_source_signature_rejects_alias"] is True
    assert x["arithmetic_source_parameters_physically_authenticated"] is False
    assert x["fake_composite_euler_jet_admitted"] is False
    assert x["RH_claimed"] is False
    print(json.dumps(x,sort_keys=True,indent=2))


if __name__=="__main__":
    main()
