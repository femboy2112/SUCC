#!/usr/bin/env python3
"""Reproducible exact joint law versus weaker-contract witness."""
import hashlib
import json
import sys
from fractions import Fraction as Q
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from observational_succ.causal_nerode_succ import SourceChart
from observational_succ.cambrian_stochastic_transport import (
    JointInstrument, joint_descent, source_filter, filter_history,
)


def receipt():
    def chart(epoch, states, reports):
        return SourceChart('cambrian-source', epoch, 'declared-basis', states, reports)
    before = chart(0, ('s0','s1'), ('a','a'))
    after = chart(1, ('s0','s1'), ('x','y'))
    bad = JointInstrument('same-marginals', before, after, ('z','w'),
                          ((Q(3,8),Q(1,8),Q(1,8),Q(3,8)),
                           (Q(1,8),Q(3,8),Q(3,8),Q(1,8))))
    witness = joint_descent(bad)
    good = JointInstrument('lawful', before, after, ('z','w'),
                           ((Q(3,8),Q(1,8),Q(1,8),Q(3,8)),)*2)
    positive = filter_history((good,), (Q(1,3),Q(2,3)), ('z',))
    posterior_only = JointInstrument('likelihood', before,
                                    chart(1,('s0',),('x',)),('z','w'),
                                    ((Q(1,4),Q(3,4)),(Q(3,4),Q(1,4))))
    left = source_filter(posterior_only,(Q(1),Q(0)),'z')
    right = source_filter(posterior_only,(Q(0),Q(1)),'z')
    epsilon = Q(1,10007)
    rare = JointInstrument('rare-receipt',before,after,('rare','common'),
                           ((epsilon,1-epsilon,Q(0),Q(0)),
                            (Q(0),1-epsilon,epsilon,Q(0))))
    rare_left=source_filter(rare,(Q(1),Q(0)),'rare')
    rare_right=source_filter(rare,(Q(0),Q(1)),'rare')
    module = ROOT / 'observational_succ/cambrian_stochastic_transport.py'
    return {
        'schema':'succ-cambrian-stochastic-v1',
        'module_sha256':hashlib.sha256(module.read_bytes()).hexdigest(),
        'source_generation':'explicit rational complete finite joint instrument table',
        'base_commit':'5eb09e7cba36ec01b8f9d6834b78b5766fd93935',
        'positive':positive,
        'same_support_same_marginals':{
            'joint_descent':witness.descended,
            'witness':witness.witness,
            'repaired_classes':len(set(pair for _,pair in witness.repaired_reports)),
            'after_z_posteriors':[
                source_filter(bad,(Q(1),Q(0)),'z').posterior,
                source_filter(bad,(Q(0),Q(1)),'z').posterior]},
        'posterior_only_mutant':{
            'same_posterior':left.posterior==right.posterior,
            'evidence':[left.evidence,right.evidence],
            'joint_descent':joint_descent(posterior_only).descended},
        'rare_receipt_boundary':{
            'joint_tv':sum(abs(x-y) for x,y in zip(*rare.rows))/2,
            'receipt_masses':[rare_left.evidence,rare_right.evidence],
            'conditioned_tv':sum(abs(x-y) for x,y in
                                 zip(rare_left.posterior,rare_right.posterior))/2},
        'scope':{'physical_source_authenticated':False,
                 'python_formally_refined_to_lean':False,
                 'adaptive_selector_executed':False,
                 'completed_weil_positivity_or_rh_proved':False}}


if __name__ == '__main__':
    print(json.dumps(receipt(), default=str, indent=2, sort_keys=True))
