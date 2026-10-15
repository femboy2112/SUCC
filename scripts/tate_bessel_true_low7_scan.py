"""Actual original signed seven-low Suzuki matrix, exact outward intervals.

This is a source-authenticated finite-J LOW block only, NOT zero-shift
S0=A-R0. The omitted original true Gamma tail is PSD and must NOT be
treated as zero. No nontrivial zeta zeros or fitted surrogate data.
"""
import argparse
import hashlib
import json
from fractions import Fraction as F

from observational_succ.suzuki_legendre_source import authentic_direct_low_matrix
from observational_succ.source_weil_hierarchy import gamma_tail
from observational_succ.one_object_residual_schur import ORIGINAL_SUZUKI_BLOB


def source_low_seven_scan(J=16):
    if type(J) is not int or not 1<=J<=75:
        raise ValueError("Only original analytic Gamma J 1..75")
    stage=authentic_direct_low_matrix(rank=7,J=J,a=F(1,2))
    if not (stage["source"]=="AUTHENTIC_Q_ZETA_SUZUKI_2026_1_3" and
            stage["source_module_blob"]==ORIGINAL_SUZUKI_BLOB and
            stage["omitted_gamma_tail_positive"]):
        raise ArithmeticError("Full original Suzuki source/prime/pole/contact drift")
    mat=stage["interval_matrix"]
    if len(mat)!=7 or any(len(x)!=7 for x in mat):
        raise ArithmeticError("True source 7×7 matrix not produced")
    if not all(mat[i][j]==mat[j][i] for i in range(7) for j in range(7)):
        raise ArithmeticError("Original signed low matrix lacks expected symmetry")
    if not all(mat[i][j].lo==mat[i][j].hi==0 for i in range(7)
               for j in range(7) if (i+j)%2):
        raise ArithmeticError("Original signed low matrix parity drift")
    canonical="\n".join(";".join(f"{e.lo}|{e.hi}" for e in line) for line in mat)
    diagonal=tuple(mat[i][i] for i in range(7))
    width=max((e.hi-e.lo for line in mat for e in line))
    return {
        "source":"SHA_PINNED_ORIGINAL_COMPLETED_ZETA_LOW_SEVEN_SUZUKI",
        "original_source_blob":ORIGINAL_SUZUKI_BLOB,
        "radius":"1/2","low_rank":7,"Gamma_J":J,
        "true_prime_power_labels":[2],
        "original_gamma_signed_low_matrix_sha256":hashlib.sha256(canonical.encode()).hexdigest(),
        "matrix_interval_symmetry":True,
        "source_parity_blocks":[4,3],
        "source_off_parity_zero_exact":True,
        "original_truncated_low_J_diagonals_negative":
            sum(e.hi<0 for e in diagonal),
        "original_truncated_low_J_diagonals_positive":
            sum(e.lo>0 for e in diagonal),
        "original_truncated_low_J_diagonals_ambiguous":
            sum(e.lo<=0<=e.hi for e in diagonal),
        "first_diagonal_outward_interval":[str(diagonal[0].lo),str(diagonal[0].hi)],
        "last_diagonal_outward_interval":[str(diagonal[-1].lo),str(diagonal[-1].hi)],
        "maximum_entry_interval_width":str(width),
        "omitted_original_Gamma_tail_source_PSD":True,
        "omitted_Gamma_kernel_uniform_upper":str(gamma_tail(J)),
        "full_original_A_low_matrix_PSD_certified":False,
        "actual_source_zero_shift_S0_sign_proved":False,
        "all_first_prime_completed_Weil_positive_proved":False,
        "RH_proved":False,
    }


if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--gamma-modes",type=int,default=16)
    args=parser.parse_args()
    print("TATE_BESSEL_TRUE_LOW7_SCAN="+json.dumps(
        source_low_seven_scan(args.gamma_modes),sort_keys=True
    ))
