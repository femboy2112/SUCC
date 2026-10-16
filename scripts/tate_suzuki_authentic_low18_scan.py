"""Actual original source low-18 signed Suzuki finite-Γ matrix scan.

This is NOT a proof of source all-test positivity. It authenticates the
genuine low 18×18 interval matrix at a=1/2, Γ J=2 and establishes that
the missing Γ tail is PSD, not an arbitrary signed modeling residual.
The full unshifted zero-resolvent short A-R0 is NOT computed.

Output is a deterministic exact rational diagnostic and SHA256 commitment
to the complete SOURCE interval matrix; no floats decide sign.
"""
from fractions import Fraction as F
from hashlib import sha256
import json

from observational_succ.suzuki_legendre_source import authentic_direct_low_matrix
from observational_succ.source_weil_hierarchy import gamma_tail
from observational_succ.one_object_residual_schur import ORIGINAL_SUZUKI_BLOB


def source_low18_scan():
    stage=authentic_direct_low_matrix(rank=18,J=2,a=F(1,2))
    if not (stage["source"]=="AUTHENTIC_Q_ZETA_SUZUKI_2026_1_3"
            and stage["source_module_blob"]==ORIGINAL_SUZUKI_BLOB
            and stage["omitted_gamma_tail_positive"]):
        raise ArithmeticError("Wrong original signed Weil low-18 source")
    rows=stage["interval_matrix"]
    n=len(rows)
    if n!=18 or any(len(r)!=18 for r in rows):
        raise ArithmeticError("This requires the actual full 18x18 interval")
    symmetry=all(rows[i][j]==rows[j][i] for i in range(n) for j in range(n))
    parity=all(rows[i][j].lo==rows[i][j].hi==0
               for i in range(n) for j in range(n) if (i+j)%2)
    if not symmetry or not parity:
        raise ArithmeticError("Original signed low-18 symmetry or parity failed")
    raw="\n".join(";".join(f"{z.lo}|{z.hi}" for z in row) for row in rows)
    diagonal=tuple(rows[i][i] for i in range(n))
    width=max((z.hi-z.lo for row in rows for z in row),default=F())
    return {
        "source":"PINNED_ORIGINAL_ZETA_SUZUKI_TRUE_P2_GAMMA_POLES_CONTACT",
        "source_git_blob":ORIGINAL_SUZUKI_BLOB,
        "halfwidth":"1/2","rank":18,"Gamma_stage":2,
        "matrix_size":"18x18",
        "parity_split":[9,9],
        "source_interval_symmetry":symmetry,
        "source_parity_zero_exact":parity,
        "matrix_interval_sha256":sha256(raw.encode()).hexdigest(),
        "positive_diagonal_intervals":
            sum(z.lo>0 for z in diagonal),
        "negative_diagonal_intervals":
            sum(z.hi<0 for z in diagonal),
        "ambiguous_diagonal_intervals":
            sum(z.lo<=0<=z.hi for z in diagonal),
        "maximum_source_interval_width":str(width),
        "first_diagonal_interval":[str(diagonal[0].lo),str(diagonal[0].hi)],
        "last_diagonal_interval":[str(diagonal[-1].lo),str(diagonal[-1].hi)],
        "original_missing_Gamma_tail_Krein_PSD":True,
        "original_missing_Gamma_uniform_g_error_bound":str(gamma_tail(2)),
        "source_all_Gamma_low_A_identified":False,
        "source_zero_shift_R0_evaluated":False,
        "source_low_short_S0_positive":False,
        "RH_proved":False,
    }


if __name__=="__main__":
    print("TSF_AUTHENTIC_LOW18_SCAN="+json.dumps(source_low18_scan(),sort_keys=True))
