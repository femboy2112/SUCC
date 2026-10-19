"""Exact finite source-typed form transport and original source provenance probe."""
import argparse
import json
from fractions import Fraction as F
from observational_succ.transported_gamma_boundary import (
    finite_boundary_control, original_source_transport_contract,
)


def main():
    p=argparse.ArgumentParser()
    p.add_argument("--source",action="store_true")
    p.add_argument("--verify",action="store_true")
    a=p.parse_args()
    controls=[finite_boundary_control(n,k,q) for n,k,q in (
        (9,6,F(1,2)),(13,9,F(1,2)),(13,9,F(2,3)),(17,12,F(1,2)))]
    src=original_source_transport_contract() if a.source else None
    if a.verify:
        assert all(m["rank_four_boundary"]==4 and
                   m["even_parity_rank"]==m["odd_parity_rank"]==2 and
                   m["exterior_leakage_identity"] for m in controls)
        if a.source:
            assert src["source_git_blob"]=="0cc8510b71d178fc79e8d410a86d8b6014cf9178"
            assert src["first_real_gamma_alpha"]=="1/2"
            assert not src["S4_positive_proved"]
    print(json.dumps({"program":"SUCC_GAMMA_TRANSPORTED_FORM_2026_10_18",
        "finite_controls":controls,"original_source":src,
        "RH_proved":False,"verification":"PASS" if a.verify else "UNVERIFIED"},
        sort_keys=True))


if __name__=="__main__":
    main()
