#!/usr/bin/env python3
"""Exact finite, nondestructive many-observer proof descent receipt."""
from __future__ import annotations
import json
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from observational_succ.diagonal_tower import (
    completed_climb, ice_climber_tower, DiagonalTower,
    destructive_diamond_counterexample,
)


def report() -> dict:
    t=completed_climb(3,45,descend=False)
    baseline=t.readiness_report()
    for level in (2,1):
        t.transmit(f'A{level}',f'B{level-1}')
        t.transmit(f'B{level}',f'A{level-1}')
    t.transmit('A0','E',('evt:p4',))
    t.transmit('B0','E',('evt:p5',))
    snapshot=t.readiness_report()
    t.transmit('A0','E')
    ready=t.readiness_report()
    cert=t.macro_succ()
    cost=t.proof_costs()
    all_sources=[]
    model,_=ice_climber_tower(3)
    for i in range(len(model.sources)):
        clone=completed_climb(3,i)
        c=clone.macro_succ()
        if c.target_value!=model.target[i] or len(c.semantic_minimal)!=2 or len(c.causal_closure)!=6:
            raise AssertionError('Out-of-fit source check failed')
        all_sources.append(c.compatible_sources[0])
    if snapshot['semantic_target']!='1' or len(snapshot['missing_causal_ids'])!=4:
        raise AssertionError('Semantics and lawful causal completion were collapsed')
    if not ready['status']=='PROOF_READY' or cert.macro_updates!=1:
        raise AssertionError('The one receiver macro-update failed')
    return {'model':'six-bit finite original-source world',
            'source_authentication':'DECLARED registry, NOT a physical attestation',
            'all_64_sources_replayed':len(all_sources)==64,
            'initial_E':baseline,'premature_semantic_readout':snapshot,
            'ready_after_causal_relay':ready,
            'certificate':{'target':cert.target_value,
                           'compatible_sources':list(cert.compatible_sources),
                           'semantic_minimal':list(cert.semantic_minimal),
                           'causal_closure':list(cert.causal_closure),
                           'all_received':list(cert.all_received)},
            'costs':cost,
            'destructive_noncommuting_negative':destructive_diamond_counterexample(),
            'physical_instantaneous_computation':False,
            'universal_infinite_tower':False,
            'general_source_changing_evidence_gluing':False}


if __name__=='__main__':
    print(json.dumps(report(),sort_keys=True,indent=2))
