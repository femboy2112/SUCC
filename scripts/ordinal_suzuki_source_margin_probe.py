"""Reproducible original Suzuki signed-Gamma ordinal margin receipt.

Input is ORIGINAL SHA-pinned arithmetic (true Λ(p^k)/√p^k, one Gamma,
contact/poles), not a source-neutral PSD surrogate. All finite certified
intervals are exact fractions. Source proof debt remains omega when no
strict sign has been separated. RH never claimed.
"""
from __future__ import annotations

import json
from fractions import Fraction as F

from observational_succ.ordinal_suzuki_source_margins import (
    authentic_suzuki_ordinal_sign_search,
    finite_strict_sign_semidecision_theorem,
    original_zero_margin_stuttering_counterexample,
)


def main():
    baseline=authentic_suzuki_ordinal_sign_search(
        F(1,4),F(1,2),(1,2,4,8,16,32,64,128))
    activated=authentic_suzuki_ordinal_sign_search(
        F(1,8),F(7,8),(1,2,4,8,16,32,64))
    zero=original_zero_margin_stuttering_counterexample(16)
    general=finite_strict_sign_semidecision_theorem()

    assert baseline["signed_source_verdict"]=="CERTIFIED_STRICT_POSITIVE_DEFINITE_2_BY_2"
    assert baseline["last_source_intersection"]["determinant"][0]>0
    assert activated["prime2_original_wavefront_sampled"]
    assert not activated["all_test_original_Weil_PSD_proved"]
    assert not zero["strict_sign_separated_at_any_stage"]
    assert not general["finite_code_global_sign_decider"]
    dec=baseline["last_source_intersection"]["determinant"]
    floor=F(dec[0].numerator*10**6//dec[0].denominator,10**6)

    result={
        "operation":"ORDINAL_TRUE_SOURCE_SUZUKI_FINITE_SIGN_SEPARATION",
        "source":"SHA_PINNED_GENUINE_COMPLETED_ZETA_SUZUKI",
        "points_baseline":["1/4","1/2"],
        "baseline_original_2x2_strict_source_sign":baseline["signed_source_verdict"],
        "baseline_original_source_lower_det_floor_1e6":str(floor),
        "baseline_gamma_stages":list(x["J"] for x in baseline["original_signed_source_stages"]),
        "baseline_gamma_tail_bounds":[str(x["source_gamma_tail_bound"]) for x in baseline["original_signed_source_stages"]],
        "baseline_ordinal_rank_trace":list(baseline["ordinal_proof_rank_trace"]),
        "prime2_active_points":["1/8","7/8"],
        "prime2_authentic_wavefront_detected":activated["prime2_original_wavefront_sampled"],
        "prime2_active_source_result":activated["signed_source_verdict"],
        "prime2_source_debt_if_unresolved":activated["unresolved_ordinal_source_debt"],
        "zero_margin_regulator_budget":zero["regulator_steps"],
        "zero_margin_original_zeta":zero["actual_zeta_witness"],
        "zero_margin_finite_search_did_not_assert_sign":True,
        "strict_nonzero_minor_semidecision":"CLASSICAL_EFFECTIVE_REAL_SOURCE",
        "original_all_test_Weil_PSD_proved":False,
        "RH_PROVED":False,
    }
    print(json.dumps(result,indent=2,sort_keys=True))


if __name__=="__main__":
    main()
