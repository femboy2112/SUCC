"""Deterministic, zero-independent exact mathematical SUCC/Hilbert source receipt."""
from __future__ import annotations

import argparse
import json
from fractions import Fraction as F
from pathlib import Path

from observational_succ.hilbert_zeno import (
    SourceKey, RationalPolynomial2, certify_square, certify_square_adaptive, hilbert_prefix, hilbert_refinement_children,
    hilbert_xy, hilbert_index, optimal_open_path_length, blind_tent,
    QuadraticSource, certify_hilbert_cube, hilbert_cube_error,
    exact_neumann_legendre_2x2, normalized_neumann_legendre_2x2,
    holder_no_go_dimension, hilbert_cube_horizon,
)

PARENT_SHA="03db44203147a7b28d445bb9f970fa71360e78c4"


def Q(value):
    return str(F(value))


def receipt() -> dict:
    square = SourceKey("source:polynomial-two-axis",0,"xy", "[0,1]^2")
    cube = SourceKey("source:bounded-rational-operator",0,"e_j orthonormal","weighted ℓ² cube")
    poly=RationalPolynomial2(square, ((0,0,F(1)),(1,0,F(1,8)),(0,1,-F(1,8))))
    cert=certify_square(poly,3)
    fast=certify_square_adaptive(poly,6)
    missed=blind_tent(3,tuple(i for i in range(64) if i!=17))
    original=tuple(tuple(F(-1) if i==j==4 else F(0) for j in range(5)) for i in range(5))
    discovered=certify_hilbert_cube(QuadraticSource(cube,original,F(1),F(0),True),2)
    shallow=certify_hilbert_cube(QuadraticSource(cube, tuple(tuple(F(0) for j in range(4)) for i in range(4)), F(1),F(0),False),2)
    horizon=hilbert_cube_horizon(F(1),F(1,3))
    k=exact_neumann_legendre_2x2(F(1,2))
    kn=normalized_neumann_legendre_2x2(F(1,2))
    order3=tuple(hilbert_xy(3,i) for i in range(64))
    address=hilbert_prefix(SourceKey("source:quaternary-address",0,"base4","square"),(1,2,0,3))
    return {
        "schema":"succ-hilbert-zeno-cube-v1",
        "date":"2026-10-14",
        "base_main":PARENT_SHA,
        "RH_PROVED":False,
        "original_weil_all_test_sign_proved":False,
        "nontrivial_zero_coordinates_used":False,
        "physical_observation_executed":False,
        "full_Lean_formalization_claimed":False,
        "academic_priority_claimed":False,
        "square":{
            "order":3,
            "cells":cert.samples,
            "first_cell":list(order3[0]),
            "last_cell":list(order3[-1]),
            "unique_cells":len(set(order3)),
            "adjacent_steps":all(abs(x1-x0)+abs(y1-y0)==1 for (x0,y0),(x1,y1) in zip(order3,order3[1:])),
            "inverse_replay":all(hilbert_index(3,*xy)==i for i,xy in enumerate(order3)),
            "path_length":Q(optimal_open_path_length(3)),
            "source_gradient_L":Q(poly.gradient_l1_bound()),
            "observed_min":Q(cert.lowest),
            "global_lower":Q(cert.global_lower),
            "observed_max":Q(cert.highest),
            "global_upper":Q(cert.global_upper),
            "verdict":cert.verdict,
            "adaptive_verdict":fast.verdict,
            "adaptive_evaluations":fast.evaluated_cells,
            "physical_probes":False,
        },
        "source_prefix_completion":{
            "digits":[1,2,0,3],
            "index":address.hilbert_index,
            "cell":list(address.cell),
            "lower_left":[Q(v) for v in address.lower_left],
            "upper_right":[Q(v) for v in address.upper_right],
            "midpoint":[Q(v) for v in address.midpoint],
            "Zeno_Linfty_remaining":Q(address.completion_radius_inf),
            "exact_parent_child_4ary_blocks_level3":all(
                hilbert_refinement_children(3,x,y)==tuple(4*hilbert_index(3,x,y)+j for j in range(4))
                for x in range(8) for y in range(8)
            ),
            "omega_physical_actualization":False,
        },
        "blindness":{
            "unvisited_hilbert_index":17,
            "cell":list(missed.cell),
            "tent_center":[Q(v) for v in missed.center],
            "true_hidden_negative_depth":Q(missed.depth),
            "tent_zero_on_other_63_centers":all(missed.at(F(2*hilbert_xy(3,i)[0]+1,16), F(2*hilbert_xy(3,i)[1]+1,16))==0 for i in range(64) if i!=17),
        },
        "hilbert_cube":{
            "radius_squared":"1/3",
            "d":5,"mesh_level":2,
            "n_grid_points":discovered.evaluated_points,
            "two_axis_error_M1_d5_n2":Q(discovered.grid_to_cube_error),
            "hidden_at_first_d4":shallow.minimum_matrix_value==0,
            "shallow_global_positive_certified":shallow.verdict.startswith("CERTIFIED_GLOBAL_NONNEGATIVE"),
            "deep_negative_witness":Q(discovered.minimum_matrix_value),
            "deep_verdict":discovered.verdict,
            "equality_to_full_H_psd_requires_all_coordinates":True,
            "sample_count_d_eq_n_eq_5":2**25,
            "holder_half_exponent_obstruction_dimension":holder_no_go_dimension(F(1,2)),
            "effective_zeno_horizon_M1_epsilon_one_third":{
                "dimension":horizon.coordinate_depth,
                "mesh_level":horizon.mesh_level,
                "points":horizon.grid_points,
                "certified_error":Q(horizon.error),
                "physical_execution":False,
            },
        },
        "original_Suzuki_source_metric_SEPARATE_FROM_SIGNED_G":{
            "interval_a":"1/2",
            "unnormalized_legendre_P1_P2":[[Q(v) for v in row] for row in k],
            "normalized_legendre_P1_P2":[[Q(v) for v in row] for row in kn],
            "signed_Weil_G_source_matrix_constructed":False,
            "whole_operator_from_two_by_two_K":False,
        },
        "missing_RH_hard_gates":[
            "actual signed 30-moment G source matrix with rigorous errors",
            "global form-topology operator bound M",
            "zero-shift cross-resolvent Douglas range / signed Schur inequality",
            "all a>0 source-derived Weil sign; grid samples alone insufficient",
        ],
    }


def encoded() -> str:
    return json.dumps(receipt(),sort_keys=True,indent=2,ensure_ascii=False)+"\n"


def main() -> None:
    parser=argparse.ArgumentParser()
    parser.add_argument("--verify",type=Path)
    opts=parser.parse_args()
    actual=encoded()
    if opts.verify:
        expected=opts.verify.read_text(encoding="utf-8")
        if expected != actual:
            raise SystemExit("HILBERT_ZENO_SOURCE_RECEIPT_MISMATCH: not byte-identical")
        print("HILBERT_ZENO_SOURCE_CERTIFIED (finite rational checks only; RH PROVED: NO)")
    else:
        print(actual,end="")


if __name__=="__main__":
    main()
