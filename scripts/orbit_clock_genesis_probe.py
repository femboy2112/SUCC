#!/usr/bin/env python3
"""Deterministic exact finite tests of the source -> clock -> jet boundary.

Run from repository root. --verify requires exact committed receipt. No floating
point, prime oracle, nontrivial zero, analytic continuation or physical claim.
"""
from __future__ import annotations

import argparse
import json
import sys
from fractions import Fraction
from pathlib import Path

sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from observational_succ.orbit_clock_genesis import (
    RootedCycle,FiniteUnarySource,FreeUnaryRay,periodic_shadow,
    minimal_clock_growth,join_irreducible_periods,source_vs_instrument_no_ghost,
    central_binomial_state_bound,exact_log_current_coefficients,
    minimal_superclock,
)
from observational_succ.clock_incidence_inversion import (
    incidence_mobius,incidence_prime_jets,incidence_lcm_compatibility,
    missing_incidence_arrow_mutation,
)
from observational_succ.topological_clock_factors import (
    RationalContraction,hidden_contraction_same_profinite_point,
)

RECEIPT=Path(__file__).resolve().parents[1]/'research'/'2026-10-17'/'ORBIT_CLOCK_GENESIS_RECEIPT.json'


def run_probe() -> dict:
    rows=minimal_clock_growth(120)
    jumps={str(row['horizon']):row['new_capacity_factor'] for row in rows if row['new_capacity_factor']>1}
    via_incidence=incidence_prime_jets(120)
    if any(Fraction(r['new_capacity_factor'])!=c['ratio'] for r,c in zip(rows,via_incidence)):
        raise AssertionError('independent exact finite source algorithms disagree')
    if rows[-1]['minimum_joint_period']!=incidence_lcm_compatibility(120)['reconstructed_joint_index']:
        raise AssertionError('independent whole-carrier reconstructions disagree')
    source=FiniteUnarySource((1,2,3,1,4),0,'finite-countermodel')
    if source.orbit_signature()['period']!=3 or source.can_factor_to(2):
        raise AssertionError('aperiodic-source gate failed')
    anti=source_vs_instrument_no_ghost(4,5)
    if anti['instrument_is_source_factor']:
        raise AssertionError('synthetic instrument impersonated source')
    rows12=minimal_clock_growth(12)
    seq=[r['minimum_joint_period'] for r in rows12]
    if seq!=[1,2,6,12,60,60,420,840,2520,2520,27720,27720]:
        raise AssertionError('known Chebyshev lcm sequence mismatch')
    prime40=[int(n) for n in join_irreducible_periods(40)]
    cone=RationalContraction().close_different_clock_residues(7,Fraction(1,10**15))
    if not cone['distinct_residues'] or not cone['gap_strictly_below_tolerance']:
        raise AssertionError('topological alias missing')
    proj=hidden_contraction_same_profinite_point(8,(2,3,4,5,6,7,8,9,10,12,15))
    if not proj['all_sampled_profinite_residues_zero']:
        raise AssertionError('profinite coordinate witness malformed')
    # Explicit finite-state witness C_m constructions and no-ghost quotient gate.
    c=RootedCycle.initial('instrument')
    for n in range(1,41):
        if c.period!=n:raise AssertionError('splicing history invalid')
        if n<40:c=c.splice()
    return {
      'RH_proved':False,
      'claim_scope':'classical paper theorems and exact finite authenticated-machine models only',
      'source_orbit':{
         'finite_transient_countermodel':{'preperiod':1,'eventual_period':3,
            'C3_factor_exists':source.can_factor_to(3),'C2_factor_exists':source.can_factor_to(2)},
         'free_ray_is_symbolic_constructor':True,
         'finite_prefix_shadow_100':periodic_shadow(100),
         'self_generated_instrument_no_ghost_C4_and_C5':anti,
      },
      'finite_clock':{
         'fresh_clock_splices_executed_through':40,
         'minimum_universal_period_sequence_through_12':seq,
         'essential_lattice_periods_through_40':prime40,
         'jet_bases_through_40':{k:v for k,v in jumps.items() if int(k)<=40},
         'n6_has_zero_jet': '6' not in jumps,
         'n8_prime_power_source_jet':jumps['8'],
         'lcm_120':str(rows[-1]['minimum_joint_period']),
         'M8_without_C8':minimal_superclock(tuple(k for k in range(1,9) if k!=8))['minimum_period'],
         'M8_with_all_clocks':minimal_superclock(tuple(range(1,9)))['minimum_period'],
         'exact_clock_information_bound_N30':central_binomial_state_bound(30),
      },
      'independent_incidence':{
         'comparison_through':120,
         'mobius_first_12':tuple(incidence_mobius(12)[i] for i in range(1,13)),
         'incidence_product_120':str(incidence_lcm_compatibility(120)['reconstructed_joint_index']),
         'quotient_mutation_gate':missing_incidence_arrow_mutation(6,2),
         'finite_beta2_log_current':{
             str(p):str(w) for p,w in exact_log_current_coefficients(40,2).items()
         },
      },
      'topology':{
         'contraction_injective_orbit_but_no_continuous_finite_factor':'proved analytically using common fixed-point limit',
         'finite_close_residue_control':cone,
         'profinite_factor_with_hidden_continuous_coordinate':proj,
         'full_factor_map_isomorphism_requires_point_separation':True,
      },
      'not_certified':[
        'physical source access to all new finite observers',
        'global no-return from finite transcripts',
        'continuous cyclic quotients from discrete orbit injectivity alone',
        'RH or signed Weil positivity',
      ],
    }


def main():
    p=argparse.ArgumentParser()
    g=p.add_mutually_exclusive_group()
    g.add_argument('--verify',action='store_true')
    g.add_argument('--write-receipt',action='store_true')
    args=p.parse_args()
    # Canonical JSON roundtrip converts tuples to arrays before comparisons.
    output=json.loads(json.dumps(run_probe(),sort_keys=True))
    if args.write_receipt:
        RECEIPT.parent.mkdir(parents=True,exist_ok=True)
        RECEIPT.write_text(json.dumps(output,indent=2,sort_keys=True)+'\n',encoding='utf-8')
    elif args.verify:
        if not RECEIPT.is_file():raise SystemExit('no pinned source receipt')
        expected=json.loads(RECEIPT.read_text(encoding='utf-8'))
        if output!=expected:raise AssertionError('pinned finite source receipt changed')
    print(json.dumps(output,indent=2,sort_keys=True))
    if args.verify:print('ORBIT_CLOCK_GENESIS_SOURCE_VERIFIED: true; RH_PROVED: false')

if __name__=='__main__':main()
