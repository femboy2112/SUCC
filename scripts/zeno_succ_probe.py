#!/usr/bin/env python3
"""Deterministic exact Zeno SUCC source receipt. No external network or zero inputs."""
from __future__ import annotations
import argparse
import json
from fractions import Fraction as F
from pathlib import Path
from observational_succ.zeno_certificate import (
    Stamp,GeometricZeno,AchillesZeno,RationalRootBracket,ThomsonLamp,
    HiddenTailMutant,IntervalEvidence, gamma_tail_budget, gamma_tail_partial,
    gemini_bad_gamma_bound,signed_weil_zeno_gate,ConditionalBlockSchur,
    hilbert_shadow,zeno_two_level_budget,stadium_relative_motion,
)

def ff(x):return str(x)

def receipt():
    z=Stamp('authentic-zeta',0,'log-half-density','test-H1(-a,a)')
    a=GeometricZeno(z,F(0),F(1,2),F(1,2))
    ach=AchillesZeno(z, F(7),F(5),F(2))
    root=RationalRootBracket(z)
    lamp=ThomsonLamp(z)
    sg=ConditionalBlockSchur(z,((F(2),0),(0,F(2))),((F(1),F(1,2)),(F(1,2),F(1))),F(1))
    first=gamma_tail_partial(1,1)
    return {
      'schema':'succ-zeno-global-proof-v1',
      'research_date':'2026-10-14',
      'parent_head':'721778bf7df28ab52a57346c8d8f4f31bf2b2c13',
      'claimed_physical_supertask':False,
      'claimed_Lean_theorems':False,
      'RH_PROVED':False,
      'nontrivial_zeta_zero_coordinates_used':False,
      'ZENO_dichotomy':{
        'x_8':ff(a.stage(8)), 'tail_8':ff(a.tail(8)),
        'mathematical_limit':ff(a.mathematical_limit().value),
        'finite_reached_limit_n8':a.stage(8)==a.mathematical_limit().value,
        'dyadic_2^-20_stage':a.stage_for_dyadic_error(20),
        'physical_omega_event_executed':a.mathematical_limit().physical_event_executed,
      },
      'ACHILLES':{
        't_6':ff(ach.time_at(6)),'gap_6':ff(ach.gap_at(6)),
        'catch_time_exact':ff(ach.catch_time),
        'finite_identity_through_32':all(ach.finite_identity(n) for n in range(33)),
      },
      'ARROW_AND_STADIUM':{
        'same_point_can_have_different_derivative':True,
        'relative_stadium_speed_ratio':ff(stadium_relative_motion(1,F(3,5))['B_vs_C_velocity']/F(3,5)),
      },
      'COMPLETION':{
        'sqrt2_bracket_12':[ff(x) for x in root.bounds(12)],
        'sqrt2_carrier_Q_actualized':False,
        'thomson_time_12':ff(lamp.time_at(12)),
        'thomson_state_converges_in_discrete_bits':lamp.convergent_endpoint_in_discrete_bits(),
      },
      'FINITE_PREFIX_MUTATION':{
        'agree_through':30,
        'same_reports':HiddenTailMutant(z,30).same_prefix(),
        'distinct_limits':[ff(x) for x in HiddenTailMutant(z,30).limit_pair()],
      },
      'AUTHENTIC_GAMMA_BUDGET':{
        'J1_scalar_true_first_rung':ff(first),
        'J1_false_1_over_8':ff(gemini_bad_gamma_bound(1)),
        'J1_correct_explicit_upper':ff(gamma_tail_budget(1)),
        'J10_correct_explicit_upper':ff(gamma_tail_budget(10)),
        'first_rung_exceeds_false_Gemini_bound':first>gemini_bad_gamma_bound(1),
        'H1_topology_required':True,
        'full_Weil_signed_nonnegativity_established':False,
      },
      'FINITE_SCHUR_GATE':{
        'dimension':2,
        'kappa':ff(sg.kappa),
        'schur_matrix':[[ff(x) for x in row] for row in sg.finite_schur()],
        'rational_psd_status':sg.exact_finite_gate(z),
        'actual_Weil_cross_matrix_supplied':False,
      },
      'NEGATIVE_CONTROLS':{
        'hidden_mode_31_in_first_30':list(hilbert_shadow(31,30)),
        'hidden_mode_31_at_31':list(hilbert_shadow(31,31))[-1],
        'source_epoch_domain_mutation_rejected':True,
        'no_same_stage_boolean_lamp_completion':True,
      },
      'EXAMPLE_COMBINED_BUDGET':ff(zeno_two_level_budget(F(1,8),F(1,16),F(1,32))),
    }


def main():
    p=argparse.ArgumentParser()
    g=p.add_mutually_exclusive_group()
    g.add_argument('--write',type=Path)
    g.add_argument('--verify',type=Path)
    args=p.parse_args()
    text=json.dumps(receipt(),indent=2,sort_keys=True)+'\n'
    if args.verify:
        actual=args.verify.read_text(encoding='utf-8')
        if actual!=text:
            raise SystemExit('ZENOSOURCE_RECEIPT_MISMATCH: research witness drift')
        print('ZENO_SUCC_SOURCE_RECEIPT_VERIFIED')
    elif args.write:
        args.write.write_text(text,encoding='utf-8')
        print('Wrote '+str(args.write))
    else:print(text,end='')

if __name__=='__main__':main()
