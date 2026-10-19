"""Source-authenticated multi-clamped-response (1/2/3) scope ablation.

Each exact source trial has original four Q4 moments and both zero
boundary traces. No nontrivial zero positions, no fake PSD covariance.
"""
import argparse
import json
from fractions import Fraction as F
from observational_succ.multimode_original_residual import original_multimode_source_schur
from observational_succ.original_continuum_residual import SOURCE_SHA


def dec(v,places=12):
    x=F(v); n=x.numerator*10**places//x.denominator
    prefix="-" if n<0 else ""
    s=str(abs(n)).zfill(places+1)
    return prefix+s[:-places]+"."+s[-places:]


def main():
    p=argparse.ArgumentParser()
    p.add_argument("--verify",action="store_true")
    p.add_argument("--deep",action="store_true")
    args=p.parse_args()
    cases=[(1,8,80),(2,8,80),(3,8,80),
           (1,12,100),(2,12,100)]
    if args.deep:cases.extend(((3,12,100),(2,16,128)))
    rows=[]
    for n,J,M in cases:
        r=original_multimode_source_schur(count=n,J=J,M=M)
        if args.verify:
            assert r["source_sha"]==SOURCE_SHA
            assert r["actual_full_continuum_L2_residual_certified"]
            assert all(len(z["optimal_clamped_correction_coefficients"][0])==n
                       for z in r["parity_schur_blocks"].values())
            assert not r["RH_proved"]
        sector={}
        for name,z in r["parity_schur_blocks"].items():
            sector[name]={
              "genuine_signed_qJ_diagonal_lowers":
                 tuple(dec(z["genuine_qJ_signed_intervals"][i][i][0])
                       for i in range(2)),
              "Q_E_action_residual_diag_sq":
                 tuple(dec(z["surrogate_projected_action_Gram"][i][i])
                       for i in range(2)),
              "true_Gamma_tail_error":tuple(dec(v) for v in z["real_Gamma_tail_errors"]),
              "genuine_S4_lower_diagonal":
                 tuple(dec(z["source_S4_lower"][i][i]) for i in range(2)),
              "source_S4_lower_PSD":z["S4_lower_PSD_certified"],
              "selected_high_coefficients":z["optimal_clamped_correction_coefficients"]}
        rows.append({"corrections":n,"J":J,"source":SOURCE_SHA,"parity":sector,
            "signed_S4_first_window_PSD_proved":r["original_first_window_S4_certified_positive"]})
    print(json.dumps({"program":"ORIGINAL_MULTIMODE_CONTINUUM_ABLATION",
        "rows":rows,"RH_proved":False,
        "verification":"PASS" if args.verify else "UNVERIFIED"},sort_keys=True))


if __name__=="__main__":
    main()
