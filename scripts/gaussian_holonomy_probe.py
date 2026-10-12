#!/usr/bin/env python3
"""Independent finite SUCC/FUCC Gaussian voltage and source functor receipt."""
from __future__ import annotations
import json
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from observational_succ.gaussian_holonomy import (
    GaussianSieve, LiftedLoop, quotient_holonomy, certify_single_loop_elimination,
    verify_refinement_commutes, fucc_path_observations,
)


def report() -> dict:
    prime5=GaussianSieve(((1,2),))
    prime517=GaussianSieve(((1,2),(1,4)))
    prime513=GaussianSieve(((1,2),(2,3)))
    data=[]
    for sieve in (prime5,prime517,prime513):
        r=quotient_holonomy(sieve,1)
        data.append({'rational_primes':list(sieve.primes),
                     'period':r.period,'allowed_residues':r.surviving_residues,
                     'rank':r.rank,'basis':[list(x) for x in r.hermite_basis],
                     'index':r.subgroup_index,'quotient_components':r.quotient_components,
                     'largest_quotient_component':r.largest_finite_quotient_component,
                     'nonzero_witness':None if r.nonzero_cycle is None else {
                        'start':list(r.nonzero_cycle.start),
                        'displacement':list(r.nonzero_cycle.displacement),
                        'steps':[list(s) for s in r.nonzero_cycle.steps]}})
    loop=LiftedLoop((0,1),((1,0),(0,-1),(1,0),(1,0),(1,0),(0,1),(1,0)))
    loop.verify(prime5,1)
    blockers=[]
    for factor in ((2,3),(1,4)):
        hit=certify_single_loop_elimination(prime5,loop,1,factor)
        blockers.append({'factor':list(factor),'norm':hit.norm,
                         'forbidden_repetition_index':hit.forbidden_repetition_index,
                         'maximum_completed_cycles_before_forbidden':hit.maximum_completed_cycles_before_forbidden})
    commute=verify_refinement_commutes(prime5,prime513,((0,1),(1,1)),1)
    primality=fucc_path_observations(prime5,((1,2),(2,1),(3,0),(3,4)))
    assert data[0]['basis']==[[5,0],[0,5]]
    assert data[1]['basis']==[[85,0],[0,85]]
    assert data[2]['rank']==0 and data[2]['largest_quotient_component']==580
    assert [b['forbidden_repetition_index'] for b in blockers]==[1,6]
    return {'source':'authentic split Gaussian prime factors',
            'squared_step_bound':1,'holonomy':data,
            'old_loop':{'start':list(loop.start),'displacement':list(loop.displacement),
                        'cycle_length':len(loop.steps)},'new_prime_blockers':blockers,
            'commuting_refinement_check':commute,
            'fucc_structural_primality_control':primality,
            'all_D_finite_sieve_existence':False,
            'all_prime_only_walks_constructed':False,
            'source_authentication':'declared exact arithmetic inputs'}


if __name__=='__main__':
    print(json.dumps(report(),sort_keys=True,indent=2))
