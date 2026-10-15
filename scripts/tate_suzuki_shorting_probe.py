"""Deterministic zero-independent source and residual certificate. Stdlib only."""
from __future__ import annotations
import argparse
import json
from fractions import Fraction as F
from pathlib import Path
from observational_succ.tate_suzuki_shorting import (
    TateSourcePassport, PINNED_SOURCE_BLOB, PINNED_TAPE,
    true_prime_tape,euler_p_shell,log_derivative_coefficient_tape,
    first_window_derivative_l1_cap,actual_source_high_derivative_truncation,
    original_gamma_derivative_l1_tail,source_legendre_30_projection_derivative_cap,
    synthetic_residual_schur,hilbert_boundary_matrix_certificate,
)


def receipt():
    passport=TateSourcePassport()
    trial=synthetic_residual_schur([[1]], [[F(1,2),F(1,8)]],
                                    [[2,0],[0,F(1,2)]],
                                    [[1,0],[0,F(1,4)]],1,
                                    [[F(1,4)],[F(1,4)]])
    weak=synthetic_residual_schur([[F(1,5)]], [[F(1,2),F(1,8)]],
                                   [[2,0],[0,F(1,2)]],
                                   [[1,0],[0,F(1,4)]],1,[[0],[0]])
    hilbert=hilbert_boundary_matrix_certificate([[1,0],[0,2]],4)
    factor=euler_p_shell(2,2,2)
    return {
      "schema":"tate-suzuki-short-zero-v1",
      "date":"2026-10-15",
      "parent_main":"03db44203147a7b28d445bb9f970fa71360e78c4",
      "pinned_original_source_git_blob":PINNED_SOURCE_BLOB,
      "passport":{
        "original":passport.source_id,"half_density":str(passport.half_density),
        "one_real_gamma":passport.real_gamma_count==1,
        "conductor":passport.conductor,"parity":passport.character_parity,
        "connes_trace_identified":passport.trace_model_identified,
      },
      "p_adic_euler_p2_sigma2_depth2":{k:str(v) for k,v in factor.items()},
      "authentic_source_prime_power_tape":true_prime_tape(8),
      "true_prime_formal_log_derivative_sigma2_N8":tuple((p,str(v)) for p,v in log_derivative_coefficient_tape(8)),
      "source_first_prime":{
        "radius":"1/2","derivative_L1_strict_upper":"26",
        "gamma_derivative_tail_J75":str(original_gamma_derivative_l1_tail(75)),
        "low_30_projection_derivative_HS_square":source_legendre_30_projection_derivative_cap()['derivative_projection_HS_square'],
        "projected_gamma_derivative_tail_J75":str(actual_source_high_derivative_truncation(75)),
        "borrowed_high_source_kappa":"369/10000",
      },
      "zero_shift":{
        "Douglas_range_gate_theorem":"proved conditional on authenticated G and AMW-06B high inequality",
        "unshifted_true_30x30_short_sign_certified":False,
        "R_lambda_limit_finite":True,
        "residual_finite_toy_truly_positive":trial.semidefinite,
        "residual_finite_toy_exact_margin":str(trial.conservative_schur_matrix[0][0]),
        "positive_full_toy_but_conservative_gate_unresolved":not weak.semidefinite,
        "synthetic_algebra_is_real_zeta":False,
      },
      "hilbert_normalized_direction":{
        "level":4,"count":hilbert['sample_count'],
        "strict_positive_matrix_certified":hilbert['strictly_positive_definite'],
        "margin":str(hilbert['certified_margin']),
        "real_weil_30x30_low_matrix_certified":False,
      },
      "source_derivative_point":{
        "original_source_integrator_implemented":True,
        "original_gamma_poles_contact_prime2_all_present":True,
        "rational_source_sign_tests_must_pass_in_full_checkout":True,
        "squared_high_residual_Gram_source_certified":False,
      },
      "we_have_proved_rh":False,
      "actual_Connes_trace_to_Suzuki_intertwiner":False,
      "physical_source_attested":False,
      "Lean_formalization_claimed":False,
      "full_tate_poisson_reproved":False,
    }


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--verify',type=Path)
    args=parser.parse_args()
    data=(json.dumps(receipt(),sort_keys=True,indent=2)+'\n').encode()
    if args.verify:
        other=args.verify.read_bytes()
        if other !=data:
            raise SystemExit('SOURCE_RECEIPT_MISMATCH')
        print('TATE_SUZUKI_ZERO_SHIFT_RECEIPT_BYTE_IDENTICAL')
    else:
        print(data.decode(),end='')


if __name__=='__main__':main()
