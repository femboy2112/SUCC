"""Frozen source-safe ONE OBJECT/zero-shift residual and contact receipt."""
from __future__ import annotations
import argparse,json
from pathlib import Path
from fractions import Fraction as F

from observational_succ import one_object_relative_residual as r
from observational_succ import one_object_source_residual as s
from observational_succ import one_object_contact_neumann as c
from observational_succ import one_object_true_derivative as t

def diag(values):
    return tuple(tuple(F(values[i]) if i==j else F()
                 for j in range(len(values))) for i in range(len(values)))

def receipt():
    source=s.authenticated_first_window_gate()
    contact=c.original_source_neumann_gate()
    tail=s.genuine_gamma_residual_tail(16)
    K=diag((F(1),F(1,4),F(1,9)))
    D=diag((F(2),F(1,4),F(1,9)))
    B=((F(1),),(F(1,4),),(F(1,9),))
    A=((F(9,10),),)
    before=r.finite_relative_short(A,D,B,K,F(1))
    after=r.finite_relative_short(A,D,B,K,F(1),(0,))
    negative=r.finite_relative_short(((F(4,5),),),D,B,K,F(1),(0,1,2))
    shift=c.contact_shift_certificate(F(1,2),(1,-1),F(2))
    boundary=c.contact_moment_boundary_channels(F(1))
    infinite=r.finite_residual_approaching_zero(8)
    noH1=r.missing_H1_obstruction(8)
    original_dir1=t.genuine_projected_first_legendre_H1_energy(2,128,1)
    original_dir3=t.genuine_projected_first_legendre_H1_energy(2,128,3)
    assert original_dir1["projected_derivative_squared_upper"]<F(1,20)
    assert original_dir3["projected_derivative_squared_upper"]<F(1,25)
    assert before.whole_space_positive_from_lower_schur is False
    assert after.whole_space_positive_from_lower_schur is True
    assert after.true_response==((F(31,36),),)
    assert negative.exact_finite_negative_witness is not None
    assert shift["difference_in_signed_Suzuki_form"]==F(1,6)
    assert contact["raw_legendre_first_two_K"]==((F(1,30),F()),(F(),F(1,210)))
    assert source["kappa"]==F(369,10000)
    assert tail["gamma_cross_H1_error_bound"]==F(66447,4225)
    assert noH1["finite_response"]==8
    assert boundary["boundary_neumann_channels"]==((29,31,F(-1,906948)),(30,32,F(-1,999180)))
    return {
        "schema":"ONE_OBJECT_RELATIVE_NEUMANN_SCHUR_V1",
        "repo_parent_pr104":"88eca261bae1381b83d018163d0945c3434a3385",
        "main_origin":"03db44203147a7b28d445bb9f970fa71360e78c4",
        "original_source_git_blob":source["original_suzuki_git_blob"],
        "original_zeta_radius":"1/2",
        "original_source_low_modes":30,
        "original_source_parity_blocks":[15,15],
        "original_high_relative_neumann_kappa":"369/10000",
        "original_first_two_legendre_neumann_K":["1/30","1/210"],
        "origin_contact_delta_to_K_exact":True,
        "contact_mutation_2_adds_true_neumann_energy":"1/6",
        "contact_mismatch_raw_legendre_K_cross_P29_P31":"-1/906948",
        "contact_mismatch_raw_legendre_K_cross_P30_P32":"-1/999180",
        "contact_mismatch_low_high_cross_rank":2,
        "identity_contact_not_authenticated_from_off_origin_trace":True,
        "Connes_off_identity_sufficient_for_contact":False,
        "toy_full_high_response":"31/36",
        "toy_no_response_sign_conclusive":False,
        "toy_one_response_positive_sign_conclusive":True,
        "toy_original_finite_signed_negative_witness":True,
        "toy_no_bounded_zero_shift_inverse_but_finite_short":True,
        "toy_H1_residual_tail_at_level8":"1/8",
        "toy_nonH1_high_resolvent_diverges":True,
        "original_gamma_tail_H1_delta_J16":"66447/4225",
        "true_source_finiteJ_first_legendre_Q1_H1_squared_upper_lt":"1/20",
        "true_source_finiteJ_first_legendre_Q3_H1_squared_upper_lt":"1/25",
        "true_source_finiteJ_gamma_modes":2,
        "true_source_first_legendre_derivative_grid":128,
        "actual_original_30_mode_projection_uncomputed":True,
        "source_authentic_finiteJ_residual_derivative_gram_constructed":False,
        "original_suzuki_low_schur_sign_proved":False,
        "original_all_radii_positive_proved":False,
        "global_Tate_Connes_identification_complete":False,
        "nontrivial_zero_coordinates_used":False,
        "rh_proved":False,
    }

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--verify",type=Path)
    args=parser.parse_args()
    out=receipt()
    if args.verify:
        expect=json.loads(args.verify.read_text(encoding="utf-8"))
        if expect!=out:
            raise AssertionError("ONE_OBJECT_RESIDUAL_RECEIPT_MISMATCH")
        print("ONE_OBJECT_RELATIVE_RESIDUAL_RECEIPT_VERIFIED")
    else:
        print(json.dumps(out,indent=2,sort_keys=True))

if __name__=="__main__":main()
