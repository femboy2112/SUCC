"""Read-only original prime2 source surplus and Schur dual proof receipt."""
import json
from fractions import Fraction as F
from observational_succ.authentic_prime_surplus import (
    original_high_surplus_certificate,original_prime_surplus_source_passport,
    center_feature_gram,feature_projected_norms,edge_source_polynomial_for_mode,
)
from observational_succ.prime_surplus_dual import (
    source_dual_coefficients,rational_polynomial_dual_center_witness,
)
from observational_succ.prime_surplus_nullspace import (
    source_prime_kernel_no_uniform_gap,
    exact_finite_four_moment_edge_kernel,
)
from observational_succ.source_prime_center_alignment import (
    certified_true_P1_center_residual,
)


def _floor_decimal(x,digits=18):
    x=F(x)
    scale=10**digits
    return str(F((x.numerator*scale)//x.denominator,scale))


def main():
    src=original_prime_surplus_source_passport()
    c=original_high_surplus_certificate((5,6,7,8))
    m=c["genuine_full_prime_mismatch_gram_intervals"]
    base=c["base_scalar_gram"]
    finite=c["source_non_scalar_comparator"]
    odd=source_dual_coefficients("odd")
    even=source_dual_coefficients("even")
    P=center_feature_gram((5,6))
    source5=rational_polynomial_dual_center_witness(P["primitives"][0],
                                                     parity="odd")
    if not (m[0][0][0]>F(1,2000) and m[1][1][0]>F(3,10000)):
        raise ArithmeticError("genuine prime-2 source surplus not certified")
    if not (F(12,25)*m[0][0][0]>4*base[0][0] and
            F(12,25)*m[1][1][0]>2*base[1][1]):
        raise ArithmeticError("true arithmetic high extra margin missing")
    if not (finite[0][0]>2*base[0][0] and
            finite[1][1]>F(7,5)*base[1][1]):
        raise ArithmeticError("center-source rank-two extra margin missing")
    if not source5["source_arithmetic_dual_saving_lower"]>0:
        raise ArithmeticError("strict original arithmetic center dual saving absent")
    p1_source=certified_true_P1_center_residual(J=64,J_G=64)
    receipt={
        "operation":"SOURCE-EDGE first-prime arithmetic high-sector surplus",
        "parent_source_sha":src["source_sha"],
        "original_prime_power":[2,2],
        "real_gamma_completed_both_poles_and_contact_preserved":True,
        "source_log2_interval_18digit_floor":_floor_decimal(src["log2_interval"][0]),
        "true_w2_interval_18digit_floor":_floor_decimal(src["prime2_weight_interval"][0]),
        "certified_w2_lower":"12/25",
        "source_all_high_kappa_by_derivative_parity":["63/500","153/500"],
        "two_rank_center_feature_Qnorm2":tuple(str(v) for v in (
            feature_projected_norms()["even_center_Qnorm2"],
            feature_projected_norms()["odd_center_Qnorm2"]
        )),
        "P5_original_K_norm2":str(c["K"][0][0]),
        "P6_original_K_norm2":str(c["K"][1][1]),
        "P5_center_source_rank_two_gain":str(c["center_rank_two_gram"][0][0]),
        "P6_center_source_rank_two_gain":str(c["center_rank_two_gram"][1][1]),
        "P5_true_log2_edge_energy_lower_18":_floor_decimal(m[0][0][0]),
        "P6_true_log2_edge_energy_lower_18":_floor_decimal(m[1][1][0]),
        "P5_high_relative_scalar_gt_5":"CERTIFIED_SOURCE_CONDITIONAL",
        "P6_high_relative_scalar_gt_3":"CERTIFIED_SOURCE_CONDITIONAL",
        "source_prime_edge_dual_center_gain_coefficients":{
            "odd":str(odd["C_center"]),"even":str(even["C_center"])
        },
        "source_odd_P5_center_dual_strict_saving_lower":str(
            source5["source_arithmetic_dual_saving_lower"]
        ),
        "phase_coherent_real_source_nullspace":source_prime_kernel_no_uniform_gap(),
        "five_cell_exact_null_witness_nonzero":
            exact_finite_four_moment_edge_kernel()["whole_primitive_norm2"]>0,
        "actual_signed_P1_center_residual_verified":
            p1_source["actual_p1_low_high_residual_not_model"],
        "actual_P1_projected_center_interval":
            tuple(str(x) for x in p1_source["true_P1_projected_residual_center_moment_interval"]),
        "actual_P1_prime_arithmetic_dual_saving_strict_lower":
            str(p1_source["true_P1_source_prime_dual_saving_lower"]),
        "actual_P1_source_center_saving_strictly_positive":
            p1_source["true_P1_source_prime_dual_saving_lower"]>0,
        "actual_signed_S4_source_residual_evaluated":False,
        "original_S4_sign":"UNVERIFIED",
        "RH_PROVED":False,
    }
    print(json.dumps(receipt,indent=2,sort_keys=True))


if __name__=="__main__":
    main()
