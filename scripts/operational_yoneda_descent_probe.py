#!/usr/bin/env python3
"""Machine-readable exact operational Yoneda and finite proof-policy descent.

Classical full Yoneda is invoked on a REAL bounded belief-path category.
Finite goal-bisimulation and source-coalgebra policy transport are separate
theorems with separately declared hypotheses. No external source attestation
or RH/quantum inference is made.
"""
import json
from observational_succ.operational_yoneda_descent import yoneda_policy_descent_demo


def main():
    x=yoneda_policy_descent_demo()
    assert x["status"]=="OPERATIONAL_YONEDA_SOURCE_POLICY_DESCENT_EXACT"
    assert x["full_yoneda_natural_transforms"]==2
    assert x["full_yoneda_actual_distinct_arrows"]==2
    assert x["restricted_yoneda_natural_transforms"]==1
    assert x["restricted_context_collapses_distinct_arrows"] is True
    assert x["restricted_arrow_pairs_undetected"]==1
    assert x["full_arrow_pairs_detected"]==1
    assert x["minimum_faithful_context_count"]==1
    assert x["minimum_faithful_context_is_source"] is True
    assert x["endpoint_forgetful_functor_is_faithful"] is False
    assert x["source_morphism_induces_checked_actual_functor"] is True
    assert x["induced_functor_context_image_surjective"] is True
    assert x["induced_functor_arrow_tokens_checked"]>0
    assert x["noninjective_carrier_abstraction_preserves_winning_rank"] is True
    assert x["abstract_optimal_rank"]==2
    assert x["concrete_optimal_rank"]==2
    assert x["successful_concrete_policy_source_replays"]==8
    assert x["losing_original_parity_preserved_as_losing"] is True
    assert x["one_probe_model_signature_equal"] is True
    assert x["two_probe_model_signature_equal"] is False
    assert x["two_probe_discriminator"]==["A","B"]
    assert x["good_model_winning_rank"]==2
    assert x["bad_model_has_no_finite_winning_policy"] is True
    assert x["root_bisimulation_rejects_shallow_alias"] is True
    assert x["independent_physical_source_attested"] is False
    assert x["Yoneda_fullness_does_not_imply_physical_or_RH_positivity"] is True
    print(json.dumps(x,sort_keys=True,indent=2))


if __name__=="__main__":
    main()
