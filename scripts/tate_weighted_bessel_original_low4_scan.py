"""The genuine original SUZUKI four-low signed block (NOT zero-shift short).

Compute true source analytic outward-rational 4×4 Legendre Galerkin A_J
with real Gamma J, contact, true prime2 half-density and BOTH polar
signs. A∞=A_J+positive omitted Gamma. Test PSD via rigorous 2×2 parity
interval determinant bounds; never substitute a positive surrogate.
Even if A∞>0, the actual S0=A∞−R0 is still entirely UNVERIFIED.
"""
import argparse
import hashlib
import json
from fractions import Fraction as F

from observational_succ.suzuki_legendre_source import authentic_direct_low_matrix
from observational_succ.one_object_residual_schur import ORIGINAL_SUZUKI_BLOB
from observational_succ.source_weil_hierarchy import gamma_tail


def original_source_low_four_scan(J=32):
    if type(J) is not int or not 1<=J<=75:
        raise ValueError("True original source Gamma modes require 1<=J<=75")
    s=authentic_direct_low_matrix(rank=4,J=J,a=F(1,2))
    if not (s["source"]=="AUTHENTIC_Q_ZETA_SUZUKI_2026_1_3"
            and s["source_module_blob"]==ORIGINAL_SUZUKI_BLOB
            and s["omitted_gamma_tail_positive"]):
        raise ArithmeticError("Actual Weil/Suzuki source changed")
    A=s["interval_matrix"]
    if not (len(A)==4 and all(len(row)==4 for row in A)
            and all(A[i][j]==A[j][i] for i in range(4) for j in range(4))):
        raise ArithmeticError("True signed low4 Galerkin matrix symmetry")
    if not all(A[i][j].lo==A[i][j].hi==0
               for i in range(4) for j in range(4) if (i+j)%2):
        raise ArithmeticError("Reflection parity source is no longer exact")
    diag=[A[i][i] for i in range(4)]
    blocks=[]
    for x,y in ((0,2),(1,3)):
        a=A[x][x];d=A[y][y];b=A[x][y]
        cross=max(abs(b.lo),abs(b.hi))
        lower=a.lo*d.lo-cross*cross
        positive=(a.lo>0 and d.lo>0 and lower>0)
        blocks.append({
            "Legendre_indices":[x+1,y+1],
            "positive_diagonal_bounds":a.lo>0 and d.lo>0,
            "parity_2x2_principal_determinant_strict_lower":str(lower),
            "source_parity_block_positive_definite":positive,
        })
    true_partial_PD=all(b["source_parity_block_positive_definite"] for b in blocks)
    raw="\n".join(";".join(f"{z.lo}|{z.hi}" for z in row) for row in A)
    return {
        "source":"ORIGINAL_ZETA_COMPLETED_SIGNED_SUZUKI_FOUR_LOW",
        "source_git_blob":ORIGINAL_SUZUKI_BLOB,
        "a":"1/2","low_dimension":4,"Gamma_source_modes":J,
        "true_active_prime_power_labels":[2],
        "source_signed_matrix_sha256":hashlib.sha256(raw.encode()).hexdigest(),
        "source_interval_symmetry":True,
        "source_parity_offblocks_exact_zero":True,
        "source_2x2_blocks":blocks,
        "partial_source_true_Gamma_J_low4_positive_definite":true_partial_PD,
        "full_original_A_infinite_Gamma_low4_PSD_if_partial_PD":true_partial_PD,
        "omitted_Gamma_modes_PSD":True,
        "omitted_Gamma_original_source_kernel_norm_upper":str(gamma_tail(J)),
        "all_diagonal_source_intervals_positive":all(z.lo>0 for z in diag),
        "first_source_diagonal":[str(diag[0].lo),str(diag[0].hi)],
        "last_source_diagonal":[str(diag[-1].lo),str(diag[-1].hi)],
        "actual_zero_shift_low_S0_positive_proved":False,
        "all_first_prime_completed_Weil_test_sign_proved":False,
        "RH_proved":False,
    }


if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--gamma-modes",type=int,default=32)
    args=parser.parse_args()
    print("TRUE_ORIGINAL_FOUR_LOW_SOURCE_SCAN="+json.dumps(
        original_source_low_four_scan(args.gamma_modes),sort_keys=True
    ))
