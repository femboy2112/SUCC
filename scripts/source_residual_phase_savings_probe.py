"""Source-conditioned true prime2 center+edge inverse savings from full residual.

The SOURCE-EDGE all-high surplus is a separately reviewed sibling PR #161
PAPER premise, not an integrated assertion on this branch. This computes
source-actual residual moments and exact interval/error robust bounds, but
does not pretend to have independently established the all-high premise.
"""
import argparse
import json
from fractions import Fraction as F

from observational_succ.source_residual_phase_savings import (
    source_conditional_phase_saving
)


def decimal(v, places=10):
    f=F(v)
    power=10**places
    n=(f.numerator*power)//f.denominator
    sign="-" if n<0 else ""
    val=str(abs(n)).zfill(places+1)
    return sign+val[:-places]+"."+val[-places:]


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--verify",action="store_true")
    parser.add_argument("--depths",default="8,16")
    args=parser.parse_args()
    checks=[]
    for jstr in args.depths.split(","):
        J=int(jstr)
        M={8:80,12:100,16:128}.get(J)
        if M is None:
            parser.error("only SHA-pinned source depths 8,12,16")
        r=source_conditional_phase_saving(J=J,M=M,P=18)
        if args.verify:
            assert r["original_source_SHA"]=="0cc8510b71d178fc79e8d410a86d8b6014cf9178"
            assert not r["RH_proved"]
            assert r["has_sibling_PR161_arithmetic_high_surplus_PAPER_PREMISE"]
        sectors={}
        for parity,packet in r["parity_comparisons"].items():
            old=tuple(decimal(packet["old_original_Schur_lower"][i][i])
                      for i in range(2))
            alternative=tuple(decimal(packet["new_conditional_source_Schur_lower"][i][i])
                      for i in range(2))
            sectors[parity]={
                "old_S4_diagonal_lower":old,
                "source_conditional_phase_diagonal_lower":alternative,
                "old_Gershgorin_floor":decimal(packet["old_rational_Gershgorin_floor"]),
                "new_Gershgorin_floor":decimal(packet["conditional_phase_Gershgorin_floor"]),
                "preferred_conditional_source_phase":packet["chosen_phase_probe"],
                "selected_lower_PSD":packet["chosen_Schur_lower_PSD_certified"],
                "center_feature_moment_nominal":
                    tuple(decimal(s) for s in packet["central_feature_nominal"]),
                "center_feature_error_upper":
                    tuple(decimal(s) for s in packet["central_feature_error_upper"])}
        checks.append({"source_depth":J,"parity":sectors,
            "conditional_first_window_S4_PSD":r["conditional_first_window_S4_PSD"]})
    print(json.dumps({
        "program":"ORIGINAL_SUZUKI_RESIDUAL_PHASE_SAVINGS_PR161_CONDITIONAL",
        "source_blob":"0cc8510b71d178fc79e8d410a86d8b6014cf9178",
        "original_source_was_modified":False,
        "source_high_surplus_premise":"SIBLING SOURCE-EDGE PR161 (NOT MERGED OR INDEPENDENTLY PROVED)",
        "depth_comparison":checks,
        "original_S4_unconditional_sign_proved":False,
        "RH_proved":False,
        "verification":"PASS" if args.verify else "UNVERIFIED"},
        sort_keys=True))


if __name__=="__main__":
    main()
