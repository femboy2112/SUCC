#!/usr/bin/env python3
"""Replay published baseline, complete local-rule certificates and scoped obstructions."""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import sys

ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT))
from observational_succ.lonely_runner_uniform import (
    UniformRule,poliakova_rule,check_local_uniform,gap_counterexample,
    binary_ladder_rule,binary_ladder_condition,
)


def main():
    p=argparse.ArgumentParser();p.add_argument('--output',type=Path);args=p.parse_args()
    original=poliakova_rule();baseline=check_local_uniform(original)
    assert baseline['local_uniform'] and baseline['gain']==1 and baseline['largest_affected']==192
    altered=UniformRule((8,32,190),original.rephased,original.added)
    failure=check_local_uniform(altered);assert not failure['local_uniform']
    actual=gap_counterexample(altered,**failure['gap'])
    ladder=[]
    for J in range(2,11):
        removed=tuple(range(3,J+1,2));rule=binary_ladder_rule(J,removed)
        assert binary_ladder_condition(J,removed)
        ladder.append({'J':J,'removed_binary_exponents':removed,'gain':rule.gain,
                       'largest_affected':rule.largest_affected})
    source='observational_succ/lonely_runner_uniform.py'
    report={'schema':'SUCC-local-uniform-rational-certificate-v1',
            'primary_source':'https://arxiv.org/html/2609.23952v1',
            'source_sha256':hashlib.sha256((ROOT/source).read_bytes()).hexdigest(),
            'authority':'finite exact certificate backed by paper iff theorem; not sampled times',
            'published_baseline':baseline,'naive_cap190_failure':failure,
            'actual_nonlocality_witness':actual,'sharp_binary_ladder_attainments':ladder,
            'boundary':'No new shifted-LR counterexample for 18<=n<=94; no general local-rule nonexistence claim.'}
    text=json.dumps(report,indent=2)+'\n'
    if args.output:args.output.write_text(text)
    else:print(text,end='')


if __name__=='__main__':main()
