#!/usr/bin/env python3
"""Zero-list-independent exact/proved-bound receipt for SUCC all-place model gluing."""
from __future__ import annotations
import argparse
import json
from fractions import Fraction as Q
from pathlib import Path

import mpmath as mp

from observational_succ.all_places_zeta import (
    SourceIndexedPlaceAtlas, additive_character_integer_defect,
    continuation_tail_rational, crt_source, fake_composite_source_contradiction,
    finite_sieved_dirichlet, finite_sieve_source_zero_prediction,
    glued_unit_sieve, glued_xi, local_fractional_part,
    model_interaction_mellin_residual, place_primes,
    prime_unit_shell_factor, primitive_self_dual_clock,
    product_formula_rational, ramanujan_crt_factorized, ramanujan_exact,
    squarefree_modulus, symmetric_model_mutant,
    theta_unit_sieve_mobius, theta_units_spatial, theta_units_spectral,
    totient, twisted_reflection_defect,
)


def qtext(v):
    v=Q(v)
    return str(v.numerator) if v.denominator==1 else f"{v.numerator}/{v.denominator}"


def fmt(z, n=20):
    z=mp.mpc(z)
    return {"real":mp.nstr(z.real,n,strip_zeros=False),
            "imag":mp.nstr(z.imag,n,strip_zeros=False)}


def receipt():
    mp.mp.dps=70
    first=SourceIndexedPlaceAtlas('Q-integers-v1',0,'self-dual-psi', (2,))
    second=SourceIndexedPlaceAtlas('Q-integers-v1',0,'self-dual-psi',(3,))
    united=first.join(second)
    s=mp.mpc('0.4','6.0')
    err=continuation_tail_rational(6,9,60,7,24)
    val_m2=glued_unit_sieve(2,0,13,85,70)
    val_m6=glued_unit_sieve(6,0,13,85,70)
    val_m6_eps=glued_unit_sieve(6,mp.mpf('0.0000001'),13,85,70)/mp.mpf('0.0000001')
    theta_sp=theta_units_spatial(6,Q(1,2),30,70)
    theta_du=theta_units_spectral(6,Q(1,2),85,70)
    theta_mo=theta_unit_sieve_mobius(6,Q(1,2),30,70)
    num,mod=crt_source((1,2,4),(2,3,5))
    source_q=Q(7,12)
    return {
        "source":"SUCC: declared source of Q, p-adic places and Gaussian real place",
        "status":"CLASSICAL IDENTITIES + PROVED FINITE/ANALYTIC BOUNDS; NO RH CLAIM",
        "provenance":{"branch":"research/all-places-model-interaction-zeta-2026-10-14",
                      "parent":"55307fec354be0c671562233ca744907cf716ca5",
                      "zero_list_used":False,
                      "physical_source_authenticated":False,
                      "adelic_Tate_theorem_fully_mechanized":False},
        "carrier_model":{"source_id":united.source_id,
                          "prime_places":list(united.primes),
                          "arch_gaussian_once":True,
                          "fake_composite_6_rejected":True},
        "rational_diagonal":{"x":qtext(source_q),
                             "p2_fraction":qtext(local_fractional_part(source_q,2)),
                             "p3_fraction":qtext(local_fractional_part(source_q,3)),
                             "additive_character_defect":additive_character_integer_defect(source_q),
                             "product_formula":qtext(product_formula_rational(source_q))},
        "finite_prime_clocks":{"local_p2_s2":qtext(prime_unit_shell_factor(2,2)),
                               "local_p3_s2":qtext(prime_unit_shell_factor(3,2)),
                               "selfdual_p2_r3_frequency8":primitive_self_dual_clock(2,3,8),
                               "selfdual_p2_r3_frequency7":primitive_self_dual_clock(2,3,7),
                               "crt_three_places":{"integer":num,"modulus":mod},
                               "ramanujan_c6_1":ramanujan_exact(6,1),
                               "ramanujan_c6_6":ramanujan_exact(6,6),
                               "crt_fourier_c6_6":ramanujan_crt_factorized((2,3),6)},
        "sieve_phase":{"m":6,"t":"1/2",
                       "spatial":fmt(theta_sp),
                       "spectral":fmt(theta_du),
                       "mobius":fmt(theta_mo),
                       "phase_error":fmt(theta_sp-theta_du)},
        "analytic_interactions":{"complex_test":fmt(s),
                                 "source_model_2_and_3_vs_6_residual":fmt(model_interaction_mellin_residual(2,3,s,12,85,70)),
                                 "twisted_reflection_residual_m6":fmt(twisted_reflection_defect(6,s,12,85,70)),
                                 "imaginary_clock_s2pi_i_over_log2_sieve_zero":fmt(glued_unit_sieve(2,2j*mp.pi/mp.log(2),13,85,70)),
                                 "glued_xi_test":fmt(glued_xi(s,13,13,70)),
                                 "xi_at_0":fmt(glued_xi(0,13,13,70)),
                                 "xi_at_1":fmt(glued_xi(1,13,13,70))},
        "outside_euler":{"completed_m2_at_0":fmt(val_m2),
                         "completed_m6_at_0":fmt(val_m6),
                         "completed_m6_derivative_proxy":fmt(val_m6_eps),
                         "predicted_slope_m6":fmt(-mp.log(2)*mp.log(3)),
                         "m2_zero_order":finite_sieve_source_zero_prediction((2,))['order'],
                         "m6_zero_order":finite_sieve_source_zero_prediction((2,3))['order']},
        "bounded_global_evaluation":{"strip_abs_real_max":7,
                                     "primal_cutoff":9,
                                     "dual_cutoff":60,
                                     "rational_upper_bound":qtext(err),
                                     "value":fmt(glued_unit_sieve(6,s,9,60,70))},
        "negative_controls":{"fake6":fake_composite_source_contradiction(6),
                             "sampling_symmetric_mutant_at_2":qtext(symmetric_model_mutant((2,3,4),2)),
                             "sampling_symmetric_mutant_at_half":qtext(symmetric_model_mutant((2,3,4),Q(1,2))),
                             "fake_place_not_equal_to_pair":True,
                             "no_global_sign_claim":True}
    }


def render():
    return json.dumps(receipt(),indent=2,sort_keys=True,ensure_ascii=False)+"\n"


def main():
    p=argparse.ArgumentParser()
    p.add_argument("--output",type=Path)
    p.add_argument("--verify",type=Path)
    args=p.parse_args()
    b=render()
    if args.verify:
        if not args.verify.exists() or args.verify.read_text()!=b:
            raise SystemExit("ALL_PLACES_ZETA_RECEIPT_MISMATCH")
        print("ALL_PLACES_ZETA_RECEIPT_REPLAY_VERIFIED")
    elif args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(b)
        print("ALL_PLACES_ZETA_RECEIPT_CREATED")
    else:
        print(b,end="")

if __name__=='__main__':main()
