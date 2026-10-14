#!/usr/bin/env python3
"""Deterministic, source-qualified exact/analytic receipt for the heat moonshot.

Analytic quantities are NUMERICAL CHECKS, not certified interval evaluations;
the paper dossier carries the independent universal analytic derivations.
"""
from __future__ import annotations
import json
from fractions import Fraction as Q
from pathlib import Path
import mpmath as mp

from observational_succ.prime_form_heat import (
    AffineSource,affine_commutator,digits_apply,digit_inverse,
    polynomial_heat,fourth_moment_pascal_limit,
    symmetric_pascal_character,symmetric_pascal_error_certificate,
    symmetric_pascal_correlated_character,digit_bulk_character,
    prime_jets_zero_coset,prime_zero_coset_mellin_local,
    tree_depth_limit,local_radix_euler,prime_powers_up_to,
    gaussian_arch_integral,gaussian_arch_factor,
    coset_theta,coset_theta_fourier,residue_fourier_character,
    residue_fourier_character_dual,theta,completed_lambda_split,
    completed_lambda_standard,xi_from_theta,
    prime_jet_mellin_truncated,prime_jet_log_derivative,
    prime_tail_upper_numeric,prime_mellin_heat_integral_numeric,
    spectral_power_mellin_factor,
)


def fs(v):
    if type(v) is Q:
        return f"{v.numerator}/{v.denominator}" if v.denominator != 1 else str(v.numerator)
    if type(v) is int:
        return str(v)
    raise TypeError("Exact receipt accepts only rational quantities")


def num(z,digits=18):
    if isinstance(z,mp.mpc):
        if abs(z.imag)<mp.mpf('1e-30'):
            return mp.nstr(z.real,digits)
        return [mp.nstr(z.real,digits),mp.nstr(z.imag,digits)]
    return mp.nstr(z,digits)


def receipt():
    mp.mp.dps=48
    r={
        "status":"EXACT_SOURCE_TYPED_PRIME_FORM_HEAT_MELLIN_RESEARCH",
        "source_pin":{
            "parent_commit":"a29170d4ff76899b18f2ac17748f42cb336cd20d",
            "arithmetic_carrier":"positive integers with exact primality and von Mangoldt prime powers",
            "spatial_carrier":"real Gaussian Fourier lattice with declared pi normalization",
            "source_authenticated_physical":False,
            "completed_weil_positivity_proved":False,
            "RH_proved":False},
        "affine_digit_carrier":{
            "mixed_radices":[2,3,5],
            "sample_word":[1,2,4],
            "sample_address":digits_apply((2,3,5),(1,2,4)),
            "sample_unique_decode":list(digit_inverse((2,3,5),29)[1]),
            "commutator_2_3_digits_1_1":affine_commutator(2,1,3,1),
            "radix6_affine_valid_not_arithmetic_prime":AffineSource(6).step(3,5)},
        "inner_pascal_heat":{
            "gaussian_x4_heat_constant_at_t_1_2":fs(polynomial_heat((0,0,0,0,1),Q(1,2))[0]),
            "n_20_t_1_2_x4_finite_infinite_gap":list(map(fs,fourth_moment_pascal_limit(20,Q(1,2)))),
            "character_bound_n_200_t_1_u_half":fs(symmetric_pascal_error_certificate(200,1,Q(1,2))),
            "character_error_n_200":num(abs(symmetric_pascal_character(200,1,Q(1,2),dps=48)-mp.exp(-mp.mpf(1)/4))),
            "correlated_mutant_error_n_200":num(abs(symmetric_pascal_correlated_character(200,1,Q(1,2),dps=48)-mp.exp(-mp.mpf(1)/4))),
            "radix6_digit_heat_error_n_800":num(abs(digit_bulk_character(6,800,1,Q(1,2),dps=48)-mp.exp(-mp.mpf(1)/4)))},
        "arithmetic_zero_cosets":{
            "p5_jets_upto_650":[n for n,_,_ in prime_jets_zero_coset(5,650)],
            "radix4_jets_upto_650":[n for n,_,_ in prime_jets_zero_coset(4,650)],
            "radix6_jets_upto_650":[n for n,_,_ in prime_jets_zero_coset(6,650)],
            "p5_local_log_coefficient_s2":fs(prime_zero_coset_mellin_local(5,2)[1]),
            "radix4_local_log_coefficient_s2":fs(prime_zero_coset_mellin_local(4,2)[1]),
            "radix6_local_zero":prime_zero_coset_mellin_local(6,2) is None,
            "prime_power_labels_upto_15":[[n,p,k] for n,p,k in prime_powers_up_to(15)]},
        "source_measure_pole_shift":{
            "p3_sigma2_raw_count":fs(tree_depth_limit(3,2,weighting="raw_count")),
            "p3_sigma2_per_state_p_inverse":fs(tree_depth_limit(3,2,weighting="level_normalized")),
            "p3_genuine_euler_s2":fs(local_radix_euler(3,2)),
            "weighting_is_additional_functional_not_ordinary_trace":True},
    }
    arch=gaussian_arch_factor(2.5+0.75j,dps=48)
    r["archimedean_heat"]={
        "mellin_gaussian_normalization":num(arch),
        "real_gaussian_integral_error":num(abs(arch-gaussian_arch_integral(2.5+0.75j,dps=48))),
        "pi_scaled_error_s2":num(abs(gaussian_arch_factor(2,scale=Q(3,2),dps=48)-gaussian_arch_factor(2,dps=48))),
        "exponent1_vs_exponent2_error_s3":num(abs(spectral_power_mellin_factor(3,1,dps=48)-spectral_power_mellin_factor(3,2,dps=48))),
    }
    p=5;b=2;t=Q(2,5)
    r["finite_fourier_rotation"]={
        "radix":p,"coset":b,"time":"2/5",
        "theta_direct":num(coset_theta(p,b,t,cut=24,dps=48)),
        "theta_dual_error":num(abs(coset_theta(p,b,t,cut=24,dps=48)-coset_theta_fourier(p,b,t,cut=24,dps=48))),
        "dft_r1_error":num(abs(residue_fourier_character(p,1,t,cut=24,dps=48)-residue_fourier_character_dual(p,1,t,cut=24,dps=48))),
        "theta_modular_error_t_2_5":num(abs(theta(t,cut=26,dps=48)-theta(Q(5,2),cut=26,dps=48)/mp.sqrt(mp.mpf(2)/5)))
    }
    s=mp.mpc('0.6','8')
    v=completed_lambda_split(s,cut=9,dps=48)
    r["zero_independent_completed_global"]={
        "s":"0.6+8i",
        "theta_split_lambda":num(v),
        "standard_pi_gamma_zeta_error":num(abs(v-completed_lambda_standard(s,dps=48))),
        "reflection_s_to_1_minus_s_error":num(abs(v-completed_lambda_split(1-s,cut=9,dps=48))),
        "xi_at_zero":num(xi_from_theta(0,dps=48)),
        "xi_at_one":num(xi_from_theta(1,dps=48)),
        "Lambda_at_negative_two_without_zeta_zero_input":num(completed_lambda_split(-2,cut=9,dps=48)),
        "analytic_continuation_is_not_RH":True}
    s=2;N=500
    trunc=prime_jet_mellin_truncated(s,N=N,dps=48)
    full=prime_jet_log_derivative(s,dps=48)
    scale=abs(gaussian_arch_factor(s,dps=48))
    r["prime_jet_to_gamma"]={
        "s":s,"max_integer":N,
        "normalized_truncated_mellin":num(trunc),
        "full_log_derivative_mellin":num(full),
        "residual_abs":num(abs(full-trunc)),
        "rigorous_analytic_tail_majorant_evaluated_numeric":num(scale*prime_tail_upper_numeric(N,s,dps=48)),
        "independent_finite_numeric_heat_integral_error":num(abs(prime_mellin_heat_integral_numeric(2,22,dps=38)-prime_jet_mellin_truncated(2,22,dps=38))),
        "heat_powers_are_exact_source_labels":True,
        "non_euler_radicand_mutants_accepted":False}
    return r


def main():
    import argparse
    parser=argparse.ArgumentParser()
    parser.add_argument('--verify',type=Path,default=None,help='Compare full recomputed receipt against this exact file')
    args=parser.parse_args()
    actual=receipt()
    if args.verify is not None:
        expected=json.loads(args.verify.read_text(encoding='utf-8'))
        if actual!=expected:
            raise SystemExit('RECEIPT_MISMATCH: frozen source not reproducible')
        print('PRIME_FORM_HEAT_RECEIPT_REPLAY_VERIFIED')
    else:
        print(json.dumps(actual,indent=2,sort_keys=True))

if __name__=='__main__': main()
