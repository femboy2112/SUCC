#!/usr/bin/env python3
"""Exact reproducible global calibration / source-coincidence receipt.

Run from the SUCC repository root:
    python scripts/wtf_global_calibration_probe.py --write
    python scripts/wtf_global_calibration_probe.py --verify

Receipt carries explicit false proof flags. No numeric pi-oracle involved.
"""
import argparse
import hashlib
import json
from dataclasses import asdict
from fractions import Fraction as Q
from pathlib import Path

from observational_succ import wtf_global_calibration as w

ROOT=Path(__file__).resolve().parent.parent
RECEIPT=ROOT/'research/2026-10-26/WTF_GLOBAL_CALIBRATION_RECEIPT.json'


def encoded(value):
    if isinstance(value, Q):
        return str(value)
    if isinstance(value, (tuple,list)):
        return [encoded(x) for x in value]
    if isinstance(value,dict):
        return {k:encoded(v) for k,v in value.items()}
    if isinstance(value, int) or isinstance(value,str) or value is None or isinstance(value,bool):
        return value
    raise TypeError(type(value))


def source_hashes():
    names=("observational_succ/wtf_global_calibration.py",
           "tests/test_wtf_global_calibration.py",
           "scripts/wtf_global_calibration_probe.py")
    return {rel:hashlib.sha256((ROOT/rel).read_bytes()).hexdigest() for rel in names}


def compute():
    def adaptive_policy(prefix):
        return (Q(1,3) if sum(prefix)%2==0 else Q(2,3),
                Q(1,2) if len(prefix)%2==0 else Q(2,3))
    checked={}
    for k in (4,5,6,7):
        q=1<<k
        r=w.resonance_receipt(q,lambda x:2*x,lambda x:x*x)
        if r.agreements != 4 or r.anti_agreements != 4 or r.primitive_projection_mean:
            raise AssertionError("quadratic collision control failed")
        checked[str(q)]=dict(asdict(r),exact_roots=w.quadratic_exact_roots(k),
                              antipodal_roots=w.quadratic_antipodal_roots(k),
                              indefinitely_extendible_at_next_checkpoint=w.stable_lifts(k))
    actual={}
    for N in (1,2,16,64,127):
        orig=w.authentic_carry_resonance(N)
        mutant=w.authentic_carry_resonance(N,seed_offset=Q(1,3))
        if orig.full_agreement!=orig.primitive_agreement or mutant.full_agreement!=mutant.primitive_agreement:
            raise AssertionError("authentic carry projection disagreement")
        actual[str(N)]={"zero_seed":asdict(orig),"changed_seed_offset_one_third":asdict(mutant)}
    coherent={str(n):w.coherent_changed_seed_countermodel(n)
              for n in (1,2,8,97,257,1024)}
    q=16
    prior=(Q(1,q),)*q
    mixture=tuple(w.global_frame_mixture(q,x,prior) for x in range(q))
    assert mixture==(Q(1),)*q
    rankrows=((-16,1,0,0),(0,-16,1,0),(0,0,-16,1))
    return encoded({
        "schema":"SUCC-WTF-global-reference-v1",
        "source_base_pr_314_sha":"935c2db4c36ff56d90acd82eae30bcce15b6a053",
        "provenance":{"local_source_test_script_sha256":source_hashes(),
                      "native_SUCC_original_forcing_unmodified":True,
                      "full_native_repo_validation_performed_here":False},
        "same_variable_quadratic":checked,
        "source_carry_coherence_false_positive":actual,
        "maximally_coherent_changed_seed_no_go":coherent,
        "adaptive_research_frame_control":{
            "q":q,"postselected_frame_score_every_outcome":q,
            "precommitted_uniform_mixture_scores":mixture,
            "duplicate_same_observation_twofold_null_expectation":w.expected_postselected_frame_score(q,2),
            "linear_macro_rank_gain":w.linear_constraint_rank_gain(rankrows,(-16**3,0,0,1)),
            "source_anchor_rank_gain":w.linear_constraint_rank_gain(rankrows,(1,0,0,0)),
            "predictable_bet_null_tree":w.exact_binary_checkpoint_audit(9,adaptive_policy,Q(4)),
        },
        "status":w.status_flags(),
    })


def render():
    return json.dumps(compute(),sort_keys=True,indent=2,ensure_ascii=False)+'\n'


def verify(path):
    given=Path(path).read_text(encoding='utf-8')
    correct=render()
    if given!=correct:
        raise AssertionError('global calibration receipt mismatch: source/mutation/false normality flag')
    return True


def main():
    p=argparse.ArgumentParser()
    mode=p.add_mutually_exclusive_group(required=True)
    mode.add_argument('--write',action='store_true')
    mode.add_argument('--verify',action='store_true')
    p.add_argument('--receipt',type=Path,default=RECEIPT)
    opts=p.parse_args()
    if opts.write:
        opts.receipt.parent.mkdir(parents=True,exist_ok=True)
        opts.receipt.write_text(render(),encoding='utf-8')
        print('WROTE',opts.receipt)
    else:
        verify(opts.receipt)
        print('VERIFIED EXACT SOURCE-HASHED RECEIPT',opts.receipt)


if __name__=='__main__':main()
