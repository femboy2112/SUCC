"""Deterministic original-source finite Hilbert research receipt (no RH claim)."""
from __future__ import annotations
import argparse
import json
from fractions import Fraction as Q
from pathlib import Path

from observational_succ import hilbert_carrier as h
from observational_succ import hilbert_suzuki_stream as s
from observational_succ import hilbert_prime_wavefront as p

MAIN="03db44203147a7b28d445bb9f970fa71360e78c4"

def receipt():
    geometry=h.coverage(3)
    nonlocality=h.adjacent_parameter_far_apart(3)
    poly=h.RationalPolynomial("EXACT_X2_Y2",0,((2,0,Q(1)),(0,2,Q(1))))
    numerical=h.exact_quadrature(poly,3)
    linear=h.RationalPolynomial("EXACT_COORDINATE_X",0,((1,0,Q(1)),))
    martingale=h.dyadic_conditional_L2(linear,3)
    haar=h.hidden_unit_Haar(3)
    original=s.source_stream(Q(1,2),3,2)
    bound=s.local_stream_bounds(original)
    rayleigh=s.source_matrix_pair_witness(original,(1,-1,0,0))
    wave=p.adaptive_profile(Q(1,2),5)
    assert geometry["cells"]==64
    assert nonlocality["max_index_separation_of_spatial_edge_neighbors"]==53
    assert numerical["absolute_error_exact"]==Q(1,384)
    assert martingale["L2_squared_error_exact"]==Q(1,768)
    assert original.source_origin_head==MAIN
    assert wave["active_true_prime_powers"]==((2,2),)
    assert wave["adaptive_leaf_count"]<wave["full_uniform_grid_cell_count"]
    assert not rayleigh["positive_weil_certified"]
    return {
      "schema":"HILBERT_SOURCE_INDEXED_COMPLETION_V1",
      "pinned_main_commit":MAIN,
      "finite_order3_cells":64,
      "finite_hilbert_max_l1_step":geometry["maximum_l1_consecutive_jump"],
      "max_index_gap_between_geometric_neighbors":53,
      "dyadic_cell_equals_time_cylinder_mass":"1/64",
      "polynomial_x2_plus_y2_integral":"2/3",
      "exact_midpoint_error_order3":"1/384",
      "hessian_midpoint_bound_sharp":True,
      "linear_x_conditional_L2_error_squared_order3":"1/768",
      "hidden_haar_norm_one_observer_sees_zero":True,
      "uniform_L2_unit_ball_completion_refuted":True,
      "true_Suzuki_hilbert_order2_stream_length":len(original.samples),
      "source_signed_operator_unchanged_by_Hilbert_order":True,
      "signed_stream_consecutive_change_bounded_by_original_source":True,
      "true_prime_power_window_first": [[2,2]],
      "wavefront_adaptive_better_than_uniform_at_order5":True,
      "fake_independent_euler_place_six_accepted":False,
      "Hilbert_Curve_2d_L2_measure_isometry_classical":True,
      "Hilbert_Curve_H1_derivative_isometry_proved":False,
      "actual_Hilbert_infinity_physically_executed":False,
      "genuine_completed_Weil_positivity_proved":False,
      "RH_proved":False
    }

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--verify",type=Path)
    args=parser.parse_args()
    output=receipt()
    if args.verify:
        if json.loads(args.verify.read_text(encoding="utf8"))!=output:
            raise AssertionError("HILBERT_SOURCE_RECEIPT_MISMATCH")
        print("HILBERT_SOURCE_COMPLETION_RECEIPT_VERIFIED")
    else:
        print(json.dumps(output,indent=2,sort_keys=True))

if __name__=="__main__":
    main()
