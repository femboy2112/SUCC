"""Reproduce bounded original zeta-source operator and generic obstruction witnesses.

All results are exact rational, no nontrivial zero coordinates or zeta oracle.
This receipt intentionally does NOT record a certified global sign verdict.
"""
from __future__ import annotations
import argparse
import json
from fractions import Fraction as F
from pathlib import Path

from observational_succ import source_weil_hierarchy as H


def record():
    assert H.assert_original_source_tape()
    st=H.stage(F(1,2),4,4)
    shift=H.certified_upper_negative_depth(st,iterations=5)
    low,high=H.depth_enclosure(st,iterations=5)
    next_errors=[H.continuous_error(F(1,2),j,j*j) for j in (2,4,8)]
    # This is the actual original-source error obligation, but finite stages
    # cannot be promoted to RH by checking only a collection of examples.
    assert all(x>y>0 for x,y in zip(next_errors,next_errors[1:]))
    assert low<=high and shift>=0
    assert H.ldl_positive(H._contrast_quadratic(st.center,shift)) or shift==0
    return {
        "program":"FINITE_SOURCE_WEIL_NEGATIVE_DEPTH",
        "original_source":"AUTHENTIC_Q_ZETA_SUZUKI_2026_1_3",
        "anchored_parent":"3270d4b9d992042c7c2bebbe784916f544ac565c",
        "finite_stage":{"a":"1/2","J":4,"N":4},
        "true_prime_powers":[list(x) for x in H.AUTHENTIC_TAPE],
        "gamma_rung_tail_J2":str(H.gamma_tail(2)),
        "gamma_rung_tail_J4":str(H.gamma_tail(4)),
        "zero_coordinates_used":False,
        "all_test_weil_positivity_proved":False,
        "finite_stage_source_replayed":True,
        "finite_stage_hermitian":all(st.center[i][j]==st.center[j][i]
                                     for i in range(st.N) for j in range(st.N)),
        "bounded_stage_spectral_enclosure_verified":low<=high,
        "analytic_hierarchy_error_decreases_in_demonstrated_stages":True,
        "gamma_contact_interval_in_5_to_6":F(5)<H.contact_iv().lo<=H.contact_iv().hi<F(6),
        "source_interval_width_below_1e_8":H.screw_interval(F(1,2),4).radius()<F(1,10**8),
        "generic_late_horizon_alias":
            str(H.simple_rank_one_negative(4,9)[0])==str(F())
            and H.simple_rank_one_negative(9,9)[0]==-F(1,512),
        "source_sign_certificate":"UNVERIFIED",
    }


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--verify',type=Path)
    args=parser.parse_args()
    r=record()
    if args.verify:
        expected=json.loads(args.verify.read_text(encoding='utf8'))
        if r!=expected:raise AssertionError("SOURCE_WEIL_RECEIPT_MISMATCH")
        print("FINITE_SOURCE_WEIL_EXACT_RECEIPT_VERIFIED")
    else:
        print(json.dumps(r,sort_keys=True,indent=2))


if __name__=='__main__':main()
