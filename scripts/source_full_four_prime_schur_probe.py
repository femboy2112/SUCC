"""Deterministic original-source four-mode arithmetic Schur response receipt.

Zero nontrivial zeta-zero coordinates. All displayed sign conclusions use
source-authenticated rational Loewner or direction-wise test bounds. An
AMBIGUOUS sign is not converted to a negativity theorem.
"""
import json
from fractions import Fraction as F

from observational_succ.source_four_prime_schur import CertifiedFourPrimeSchurTrial
from observational_succ.source_four_center_gram import (
    authenticated_center_rankone_cross_intervals,
    authentic_four_center_certificate,
)
from observational_succ.source_four_edge_gram import authentic_four_edge_moments
from observational_succ.source_four_phase_schur import CertifiedFourPrimeFullPhaseSchurTrial


def _clip_fraction(x,digits=15):
    x=F(x);scale=10**digits
    # EXACT rational downward, purely display; sign proof uses x unchanged.
    return str(F(x.numerator*scale//x.denominator,scale))


def main():
    r=CertifiedFourPrimeSchurTrial(J_center=64,J_G=64,J_deriv=2,
                                   digits=100,eta=F(1,8))
    phase=CertifiedFourPrimeFullPhaseSchurTrial(J_center=64,J_G=64,J_deriv=2,
                                                J_edge=8,digits=100,eta=F(1,8))
    edge20=authentic_four_edge_moments(J=20,J_G=64,digits=100)
    out={
        "source":r["source"],
        "original_frozen_source_sha":r["source_sha"],
        "real_prime2_power_label":r["source_true_prime_power"],
        "source_signed_low4":"ORIGINAL_COMPLETED_SUZUKI",
        "source_all_high_kappa":tuple(str(v) for v in r["kappa_by_derivative_parity"]),
        "all_four_actual_source_center_moment_intervals":tuple(
            tuple(str(t) for t in pair) for pair in r["center_interval_moments"]),
        "moment_order":("int_C0 g1", "int_C0 x*g2", "int_C0 g3", "int_C0 x*g4"),
        "source_certified_center_rankone_offdiagonal_cross_intervals":{
            key:{"lower":str(value["lower"]),"upper":str(value["upper"]),
                 "sign":value["sign"],
                 "NOT_entire_center_cross_sign":value["whole_Gram_cross_sign_NOT_certified"]}
            for key,value in authenticated_center_rankone_cross_intervals(
                authentic_four_center_certificate(J=64,J_G=64)).items()
        },
        "center_odd/even_offdiagonal_nominal":(
            str(r["center_ranktwo_nominal_matrix"][0][2]),
            str(r["center_ranktwo_nominal_matrix"][1][3]),
        ),
        "source_four_Young_eta":str(r["center_Young_eta"]),
        "source_full_4x4_center_Loewner_improvement":tuple(
            tuple(str(x) for x in row) for row in r["center_Loewner_improvement_matrix"]),
        "source_signed_scalar_S4_lower":tuple(
            tuple(str(x) for x in row) for row in r["source_original_trial_signed_scalar_S4_lower"]),
        "source_signed_arithmetic_S4_lower":tuple(
            tuple(str(x) for x in row) for row in r["source_corrected_four_S4_Loewner_lower"]),
        "source_signed_S4_verdict":r["arithmetic_source_four_S4_verdict"],
        "new_center_improvement_PSD_in_Loewner":
            r["improvement_Loewner_nonnegative"],
        "strict_center_gains_for_real_low_directions":{
            name:{
                "lower":_clip_fraction(v["strict_arithmetic_saving"]),
                "original_scalar_S4_directional_lower":
                    _clip_fraction(v["original_scalar_only_S4_lower"]),
                "new_signed_S4_directional_lower":
                    _clip_fraction(v["original_signed_S4_lower"]),
            } for name,v in r["source_direction_certificates"].items()
        },
        "old_analytic_Gamma_only_S4_verdict":r["old_analytic_source_verdict"],
        "P1_agrees_with_independent_original_source_certificate":
            r["actual_source_P1_independent_replay"],
        "first_window_not_RH":True,
        "original_true_prime_edge_J20_moment_intervals":tuple(
            tuple(str(t) for t in p) for p in edge20["intervals"]),
        "original_true_prime_edge_J20_direction_flags":tuple(
            bool(low>0 or high<0) for low,high in edge20["intervals"]),
        "original_true_prime_edge_moment_intervals":tuple(
            tuple(str(t) for t in p) for p in phase["source_edge_intervals"]),
        "original_true_source_complete_center_plus_edge_S4_verdict":
            phase["original_S4_verdict"],
        "exact_source_all_real_cone_S4_certificate":
            phase["exact_all_direction_source_robust_cone_PSD"],
        "signed_four_source_Loewner_certified":
            phase["source_Loewner_lower_PSD"],
        "original_true_source_edge_interval_width":tuple(
            str(t) for t in phase["source_edge_width"]),
        "signed_original_complete_center_plus_edge_4x4_Loewner_lower":tuple(
            tuple(str(t) for t in row)
            for row in phase["original_complete_S4_center_plus_edge_Loewner_lower"]),
        "source_two_edge_four_mode_direction_savings":{
            k:{
                "center":_clip_fraction(v["arithmetic_center_strict_saving"]),
                "edge":_clip_fraction(v["arithmetic_prime_edge_strict_saving"]),
                "total":_clip_fraction(v["total_arithmetic_strict_saving"]),
            } for k,v in phase["full_source_direction_certificates"].items()
        },
        "RH_PROVED":False,
    }
    if not out["P1_agrees_with_independent_original_source_certificate"]:
        raise AssertionError("full source center matrix does not replay old P1")
    if out["RH_PROVED"]:
        raise AssertionError("false claim of RH proof")
    print(json.dumps(out,indent=2,default=str,sort_keys=True))


if __name__=="__main__":
    main()
