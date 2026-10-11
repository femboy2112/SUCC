#!/usr/bin/env python3
"""Inspect finite evidence for a non-finitely-representable Ind-Yoneda limit.

Only exact integer, valuation and rational arithmetic is used; this tool
does not execute an infinite path, compute zeta zeros, or certify RH.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from observational_succ.infinite_realization import (
    LCMIndRealization, e_enclosure, pi_enclosure, zeta_euler_enclosure,
    escaping_defect_form, escaping_defect_limit, pinned_negative_form,
)


def run(stage=12, terms=12):
    path=LCMIndRealization()
    representative=path.stage(stage)
    first=path.first_missed_prime_power(stage)
    nextstage=path.stage(first)
    uniform_queries=[6,12,30,64,81]
    limiting=path.limit_profile(uniform_queries)
    assert all(nextstage.exponent(p)>=k for p,k in representative.factors)
    positive_limit, tail_start=escaping_defect_limit({1:1,3:2})
    return {
        "status":"FINITE_EXACT_DEMONSTRATION",
        "stage":stage,
        "L_N_prime_valuation_word":representative.label(),
        "all_permitted_divisibility_probes_pass":True,
        "first_future_discriminating_prime_power":first,
        "currently_fails_that_counterfactual_probe":not path.hypothetical_probe(stage,first),
        "subsequent_stage_answers_that_probe":path.hypothetical_probe(first,first),
        "ind_limit":limiting,
        "real_pi_enclosure":pi_enclosure(terms).report(),
        "real_e_enclosure":e_enclosure(terms).report(),
        "zeta_two_safe_Euler_enclosure":zeta_euler_enclosure(stage,2).report(),
        "finite_negative_Q_stage_e_stage":str(escaping_defect_form(stage,{stage:1})),
        "finite_negative_Q_stage_plus_one_e_stage":str(escaping_defect_form(stage+1,{stage:1})),
        "fixed_positive_limit_example":str(positive_limit),
        "fixed_support_stabilization_horizon":tail_start,
        "persistent_negative_control":str(pinned_negative_form(stage+1,{1:1})),
        "proven_scope":"finite calculations illustrating an exact infinite-diagram theorem",
        "not_claimed":"execution of infinity, Archimedean Gamma reconstruction or RH positivity",
    }


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--stage",type=int,default=12)
    p.add_argument("--terms",type=int,default=12)
    p.add_argument("--output",type=Path)
    args=p.parse_args()
    result=run(args.stage,args.terms)
    raw=json.dumps(result,sort_keys=True,indent=2)+"\n"
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(raw,encoding="utf-8")
    else:
        print(raw,end="")


if __name__=="__main__":
    main()
