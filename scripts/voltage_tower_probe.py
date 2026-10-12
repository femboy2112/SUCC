#!/usr/bin/env python3
"""Six-climber finite arithmetic proof-shard descent and E's one macro update."""
from __future__ import annotations
import json
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from observational_succ.gaussian_holonomy import GaussianSieve, HolonomyError
from observational_succ.voltage_tower import completed_voltage_climb, VoltageTowerError


def report() -> dict:
    tower=completed_voltage_climb(levels=3)
    proof=tower.final_macro_succ()
    rejected = False
    try:
        completed_voltage_climb(levels=3,source=GaussianSieve(((1,2),(1,4))))
    except HolonomyError:
        rejected = True
    if not rejected:
        raise AssertionError('Bad Gaussian sieve escaped the proof search negative gate')
    if (proof.checked_vertices!=2304 or proof.checked_directed_edges!=4356
            or proof.max_lifted_component!=580 or proof.verified_shards!=6
            or proof.epistemic_macro_updates!=1):
        raise AssertionError('Distributed arithmetic proof not calibrated')
    return {'status':'finite source-verifiable distributed mathematical certificate',
            'sieve_primes':[5,13],'squared_step_bound':1,
            'source_signature':proof.source_signature,
            'verified_source_vertices':proof.checked_vertices,
            'verified_directed_edges':proof.checked_directed_edges,
            'verified_shards':proof.verified_shards,
            'maximum_lifted_component':proof.max_lifted_component,
            'physical_climbers':list(tower.climbers),
            'mathematical_local_checks':len(tower.shards),
            'network_transmissions':len(tower.transport_log),
            'receiver_macro_succ_count':proof.epistemic_macro_updates,
            'causal_log_entries':len(tower.event_log),
            'complete_source_edge_recheck_at_E':proof.mathematical_full_source_check,
            'escaping_5_17_sieve_refused':rejected,
            'candidate_global_potential_constructed_before_climb':True,
            'all_D_sieve_existence_independently_proved':False,
            'zero_time_physical_computation':False}

if __name__=='__main__':
    print(json.dumps(report(),sort_keys=True,indent=2))
