#!/usr/bin/env python3
"""A bounded, zero-free Lambert-W / factorial-SUCC / rooted-tree probe.

The W seed never counts as an exact certificate. Explicit integer factorial
comparison and source-history recurrence residuals provide the controls.

python scripts/lambert_succ_probe.py --factorial-stage 32 --tree-stage 40
"""
from __future__ import annotations

import argparse
from fractions import Fraction
from math import factorial
from pathlib import Path
import json
import sys

ROOT=Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0,str(ROOT))

from observational_succ.lambert_succ import (
    invert_factorial_mass, gamma_bulk_defect, gamma_defect_succ,
    rooted_tree_coefficients, rooted_tree_succ_ratio, rooted_tree_count,
    leaf_only_extension_count, tree_functional_residual,
    tree_series_vs_lambert, bulk_branches,
)
from observational_succ.gamma_interferometer import GammaInterferometer


def run(factorial_stage=32,tree_stage=40,dps=65):
    if type(factorial_stage) is not int or not 2<=factorial_stage<=255:
        raise ValueError("factorial stage must lie in 2..255")
    if type(tree_stage) is not int or not 6<=tree_stage<=128:
        raise ValueError("tree stage must lie in 6..128")
    target=factorial(factorial_stage)
    certificate=invert_factorial_mass(target,dps=dps)
    if not certificate.verify():
        raise ArithmeticError("Missing exact SUCC certificate")

    original=rooted_tree_coefficients(tree_stage)
    source_fraud=rooted_tree_coefficients(
        tree_stage,overrides={6:original[6]+Fraction(1,10)}
    )
    import mpmath as mp
    with mp.workdps(dps):
        z=Fraction(1,4)
        check=tree_series_vs_lambert(z,tree_stage,dps=dps)
        branches=bulk_branches("-0.5",dps=dps)
        genuine={n:1 for n in range(1,13)}
        fake=dict(genuine);fake[6]=2
        conn_genuine=GammaInterferometer.from_prefix(genuine,12).connected[6]
        conn_mutant=GammaInterferometer.from_prefix(fake,12).connected[6]
        payload={
            "status":"FINITE_ZERO_FREE_LAMBERT_SUCC_PROBE",
            "factorial_inverse_exact_witness":certificate.report(),
            "gamma_bulk_residual":mp.nstr(gamma_bulk_defect(factorial_stage,dps=dps),30),
            "gamma_succ_residual_increment":mp.nstr(gamma_defect_succ(factorial_stage,dps=dps),30),
            "tree_succ":{
                "stage":tree_stage,
                "coefficient":str(original[tree_stage]),
                "count_labelled_rooted":str(rooted_tree_count(tree_stage)),
                "t_next_over_t_at_n_minus_one":str(rooted_tree_succ_ratio(tree_stage-1)),
                "shadow_leaf_only_at_previous":str(leaf_only_extension_count(tree_stage-1)),
                "tree_functional_residual_at_true_stage":str(tree_functional_residual(original,6)),
                "tree_mutation_at_six":str(tree_functional_residual(source_fraud,6)),
                "series_analytic_principal":mp.nstr(check["principal_limit"],30),
                "series_finite_prefix":mp.nstr(check["truncation"],30),
                "series_error":mp.nstr(check["absolute_error"],10),
                "other_real_branch":mp.nstr(check["other_real_branch"],30),
            },
            "two_branch_bulk_at_y_minus_half":{
                "principal_x_above_one":mp.nstr(branches[0],28),
                "nonprincipal_x_below_one":mp.nstr(branches[1],28)
            },
            "arithmetic_mutation_negative_control":{
                "connected_true_at_6":str(conn_genuine),
                "connected_fake_at_6":str(conn_mutant),
                "W_factorial_inverse_unchanged":True,
                "interpretation":"W seed reads factorial mass, not true Euler connectivity"
            },
            "status_boundary":"classical asymptotic inverse/combinatorial species; no RH inference",
        }
        return payload


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--factorial-stage",type=int,default=32)
    p.add_argument("--tree-stage",type=int,default=40)
    p.add_argument("--dps",type=int,default=65)
    p.add_argument("--output",type=Path)
    args=p.parse_args()
    result=run(args.factorial_stage,args.tree_stage,args.dps)
    t=json.dumps(result,sort_keys=True,indent=2)+"\n"
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(t)
    else:
        print(t,end="")


if __name__=="__main__":
    main()
