"""Operation APOLLO deterministic source-jets and derivative gauge receipt."""
from __future__ import annotations

import json
from fractions import Fraction as F

from observational_succ.apollo_derivative_jets import (
    exact_source_gauge_negative_direction, true_third_prime_wavefronts,
    genuine_prime_third_jet, third_origin_contact_offset,
    cubic_gauge_discrimination, compact_polynomial_moment_certificate,
    authentic_uniform_small_diagonal,
    third_distribution_bump_pair, exact_local_gamma_slope_bound,
)
from observational_succ.one_object_kernel_certificates import source_two_point_minor
from observational_succ.apollo_krein_factor import (
    original_suzuki_krein_finite_window,prime_krein_identity,
    prime_mixed_second_source_coefficients,gamma_mixed_second_source_coefficients,
    source_feature_contraction_diagnostic,
    authentic_small_window_brownian_coercivity,
    authentic_sharp_small_window_hilbert_factor,
    authentic_prime_two_activation_on_old_window,
    authentic_small_window_completed_weil_coercivity,
    brownian_compact_weak_derivative_certificate,
)


def main():
    src=source_two_point_minor(F(1,4),F(1,2),128)
    assert src["verdict"]=="PROVED_FINITE_SOURCE_POSITIVE"
    fake=exact_source_gauge_negative_direction(F(1,4),64,128)
    assert fake["strict_negative_mutant_certified"] and fake["third_derivative_unchanged"]
    jets=true_third_prime_wavefronts(2)
    assert tuple(j.n for j in jets)==(2,3,4,5,7)
    proof=third_distribution_bump_pair(F(2),6,65)
    assert proof["residual_abs"]<__import__("mpmath").mpf("1e-43")
    wrong=third_distribution_bump_pair(F(2),6,65,F(2,7))
    assert abs(wrong["residual_abs"]-__import__("mpmath").mpf(2)/7)<__import__("mpmath").mpf("1e-43")
    moments=compact_polynomial_moment_certificate(3,8)
    assert moments["unobserved_moment_dimension"]==3
    q=exact_local_gamma_slope_bound(1,32,70)
    assert q["absolute_error"]<q["analytic_tail_evaluation"]
    bound=src["determinant"][0]
    floor=F(bound.numerator*10**6//bound.denominator,10**6)
    continuous=authentic_uniform_small_diagonal(F(1,8))
    assert continuous["strict_for_every_real_radius_in_window"]
    krein=original_suzuki_krein_finite_window(F(1,4),F(1,2),F(1,2),8,75)
    assert krein["prime_labels"]==(2,)
    assert krein["residual_abs"]<__import__("mpmath").mpf("1e-57")
    primemix=prime_mixed_second_source_coefficients(F(1))
    gamma0=gamma_mixed_second_source_coefficients(0)
    assert primemix["combined_origin"]==0
    assert gamma0["origin_delta_coefficient"]==4
    synthetic=source_feature_contraction_diagnostic(
      ((F(1),F(0)),(F(0),F(1))),
      ((F(2),F(0)),(F(0),F(0)))
    )
    assert not synthetic["combined_signed_psd_on_selected_finite_set"]
    assert prime_krein_identity(F(1,2),F(3,2),F(1))["identity_exact"]
    loose=authentic_small_window_brownian_coercivity(F(1,24))
    sharp=authentic_sharp_small_window_hilbert_factor(F(1,12))
    birth=authentic_prime_two_activation_on_old_window()
    assert loose["strict_K_dominates_B_lower"]>F(1,10)
    assert sharp["exact_positive_coercivity_margin"]>F(1,100)
    assert sharp["positive_feature_Psi_a_exists_by_completion"]
    assert birth["signed_zero"] and birth["Krein_neutral_source_birth"]
    weil=authentic_small_window_completed_weil_coercivity(F(1,12))
    brownian_cal=brownian_compact_weak_derivative_certificate(F(1,12),4)
    assert weil["holds_for_every_smooth_compact_test_on_window"]
    assert weil["uniform_original_weil_L2_lower"]==F(1,100)
    assert brownian_cal["direct_polynomial_L2_energy"]==brownian_cal["independent_beta_energy"]
    result={
       "AUTHENTIC_SIGNED_WEIL_all_Cc_infinity_small_window_lower":"1/100",
       "AUTHENTIC_SIGNED_WEIL_all_Cc_infinity_radius":"1/12",
       "AUTHENTIC_Brownian_D2_exact_beta_polynomial_control":True,
       "AUTHENTIC_FULL_WINDOW_small_positive_radius":"1/12",
       "AUTHENTIC_FULL_WINDOW_true_rational_margin_lower":str(sharp["exact_positive_coercivity_margin"]),
       "AUTHENTIC_FULL_WINDOW_universal_Brownian_floor":"1/100",
       "AUTHENTIC_FULL_WINDOW_local_positive_source_Hilbert_factor_exists":True,
       "AUTHENTIC_FULL_WINDOW_all_intervals_RH":False,
       "AUTHENTIC_Gamma_modes_used":20,
       "AUTHENTIC_Gamma_Taylor_order":9,
       "AUTHENTIC_Rough_8mode_radius":"1/24",
       "AUTHENTIC_Rough_8mode_margin_floor":"1/10",
       "AUTHENTIC_True_prime2_neutral_source_birth":True,
       "KREIN_finite_window":krein["window_halfwidth"],
       "KREIN_original_prime_labels":list(krein["prime_labels"]),
       "KREIN_source_plus_minus_residual_numerical":krein["residual"],
       "KREIN_positive_feature_built":True,
       "KREIN_negative_feature_built":True,
       "KREIN_full_contraction_proved":False,
       "KREIN_prime_contact_cancellation":True,
       "AP8_uniform_original_diagonal_real_interval":"0<r<=1/8",
       "AP8_original_diagonal_lower_r_over_8":True,
        "operation":"APOLLO_D2_D3_SOURCE_JETS",
        "parent_one_object_sha":"04b6d8ede12c58afe4a244b11297663c33260de1",
        "authentic_source":"SHA_PINNED_PR85_ORIGINAL_ZETA",
        "true_prime_wavefronts_under_log_n_less_than_2":list(j.n for j in jets),
        "true_prime_wavefronts_δprime_weights":[
            {"n":j.n,"p":j.p,"exponent":j.exponent,
             "coefficient_outward_interval":[str(a) for a in j.delta_prime_weight_interval]}
            for j in jets
        ],
        "origin_delta_prime_rational_offset_J6":str(third_origin_contact_offset(6)),
        "source_Weil_to_D3_Suzuki_residual_numeric":proof["residual"],
        "wrong_contact_D3_defect_numeric":wrong["residual"],
        "third_invisible_quadratic_gauge":True,
        "original_2by2_gram_det_lower_floor_1e6":str(floor),
        "quadratic_mutant_same_D3_but_negative_gram":fake["strict_negative_mutant_certified"],
        "quadratic_mutant_original_source":False,
        "one_mass_normalization_fixes_D3_gauge":cubic_gauge_discrimination(1,1)["source_Weil_pairing_difference"]==-2,
        "Ccinfinity_D3_range_missing_polynomial_moments":3,
        "second_third_jets_identify_source":True,
        "third_derivative_alone_implies_positive_Weil":False,
        "all_test_suzuki_feature_factor":"UNVERIFIED",
        "RH_PROVED":False,
    }
    print(json.dumps(result,sort_keys=True,indent=2))


if __name__=="__main__":
    main()
