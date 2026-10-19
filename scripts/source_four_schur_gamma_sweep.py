"""One controlled source-Gamma refinement of the FULL signed four-mode S4 lower.

Compare inherited authentic finite-J exact G'_J with J=2 versus J=6,
holding original first-prime a=1/2, complete low A4, the true high source,
center rank-two arithmetic saving, and source mixed moment oracle FIXED.
If an apparent source sign improvement survives exact Loewner comparison,
it is genuine source-certificate information, not an RH proof.
"""
import json
from fractions import Fraction as F

from observational_succ.source_four_prime_schur import CertifiedFourPrimeSchurTrial
from observational_succ.direct_quotient_schur import exact_psd


def floor(x,digits=14):
    x=F(x);n=10**digits
    return str(F(x.numerator*n//x.denominator,n))


def matrix_difference(A,B):
    return tuple(tuple(A[i][j]-B[i][j] for j in range(4))
                 for i in range(4))


def main():
    early=CertifiedFourPrimeSchurTrial(
        J_center=64,J_G=64,J_deriv=2,digits=100,eta=F(1,8)
    )
    better=CertifiedFourPrimeSchurTrial(
        J_center=64,J_G=64,J_deriv=6,digits=100,eta=F(1,8)
    )
    if early["source_sha"]!=better["source_sha"] or \
       early["source_sha"]!="0cc8510b71d178fc79e8d410a86d8b6014cf9178":
        raise ArithmeticError("original source Gamma sweep provenance drift")
    oldS=early["source_corrected_four_S4_Loewner_lower"]
    newS=better["source_corrected_four_S4_Loewner_lower"]
    oldQ=early["source_original_trial_signed_scalar_S4_lower"]
    newQ=better["source_original_trial_signed_scalar_S4_lower"]
    rep={
        "original_source_sha":better["source_sha"],
        "original_real_Gamma_J_compared":(2,6),
        "low_signed_true_source_a4_unchanged":True,
        "true_Gamma_tail_by_B3":True,
        "signed_S4_true_lower_J2_diagonal":tuple(
            floor(oldS[i][i]) for i in range(4)),
        "signed_S4_true_lower_J6_diagonal":tuple(
            floor(newS[i][i]) for i in range(4)),
        "certified_J6_S4_Loewner_above_J2":
            exact_psd(matrix_difference(newS,oldS)),
        "same_center_P1_source_gain":(
            early["source_direction_certificates"]["P1"]["strict_arithmetic_saving"]
            ==better["source_direction_certificates"]["P1"]["strict_arithmetic_saving"]),
        "new_first_window_signed_S4_source_PSD":
            better["arithmetic_source_four_S4_lower_certified_PSD"],
        "new_first_window_signed_S4_verdict":
            better["arithmetic_source_four_S4_verdict"],
        "all_radius_source_certificate":False,"RH_PROVED":False
    }
    print(json.dumps(rep,default=str,indent=2,sort_keys=True))


if __name__=="__main__":
    main()
