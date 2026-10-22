"""Deterministic exact-source validation of bidirectional marked histories.

--check compares the current source SHA-1 Git blob IDs and exact rational data
against the frozen receipt. This is an integrity/test gate, not Lean authority.
"""
from __future__ import annotations
import hashlib
import json
import sys
from fractions import Fraction as Q
from pathlib import Path

from observational_succ.bidirectional_source_histories import (
    conditioned_bidirectional_path_law, enumerate_stopped_words,
    finite_stopped_pascal, pascal_cotransition_identity,
    project_pascal_words, valuation_edit_lower_bound,
)

ROOT=Path(__file__).resolve().parents[1]
RECEIPT=ROOT/'research/2026-10-22/SOURCE_FAITHFUL_BIDIRECTIONAL_EXACT_RECEIPT.json'
FILES=('observational_succ/bidirectional_source_histories.py',
       'tests/test_bidirectional_source_histories.py')


def git_blob_sha(path):
    data=(ROOT/path).read_bytes()
    return hashlib.sha1(f'blob {len(data)}\0'.encode()+data).hexdigest()


def reproduce():
    model=finite_stopped_pascal((2,3,5),2,2)
    words=enumerate_stopped_words(model)
    overlap_checks=0
    for subset in ((2,3),(2,5),(3,5),(2,),(3,),(5,)):
        smaller=finite_stopped_pascal(subset,2,2)
        if project_pascal_words(model,subset)!=enumerate_stopped_words(smaller):
            raise AssertionError('prime-subset history projectivity failed')
        overlap_checks+=len(enumerate_stopped_words(smaller))
    backward=pascal_cotransition_identity(model)
    layers=(('s',),('x','y'),('ok','bad'))
    kernels=({'s':(('X','x',Q(1,3)),('Y','y',Q(2,3)))},
             {'x':(('win','ok',Q(3,4)),('lose','bad',Q(1,4))),
              'y':(('win','ok',Q(1,5)),('lose','bad',Q(4,5)))})
    double=conditioned_bidirectional_path_law(layers,kernels,{'s':Q(1)},
                                               {'ok':Q(1),'bad':Q(0)})
    if double['forward_histories']!=double['backward_histories']:
        raise AssertionError('backwards full-path mismatch')
    if valuation_edit_lower_bound(64)['min_occupation_L1_edits']!=64:
        raise AssertionError('nonlocality witness failed')
    return {
        'claim_namespace':'SBH-01..09',
        'source_parent':'PR237@391c304e768d073ae747459d279e14d5357092e5',
        'source_git_blob_sha1':{p:git_blob_sha(p) for p in FILES},
        'rational_exact':True,
        'sample_conditional_success_Z':str(double['Z']),
        'forward_reverse_selected_paths':len(double['forward_histories']),
        'stopped_pascal_235_beta2_cap2_words':len(words),
        'stopped_pascal_backward_identites':len(backward),
        'independently_checked_projected_words':overlap_checks,
        'stopped_pascal_empty_word_probability':str(words[()]),
        'high_carry_min_occupation_edits':64,
        'rank_normalized_Gibbs_p2_counterexample':['9/13','99/133'],
        'physics_prime_source_authentication':False,
        'physics_retrocausation_derived':False,
        'Lean_kernel_checked':False,
        'RH_proved':False,
    }


def main():
    actual=reproduce()
    if '--check' in sys.argv:
        frozen=json.loads(RECEIPT.read_text())
        if actual!=frozen:
            print('RECEIPT DRIFT\nactual:',json.dumps(actual,indent=2,sort_keys=True),
                  '\nfrozen:',json.dumps(frozen,indent=2,sort_keys=True))
            raise SystemExit(1)
        print('Exact source-hashed receipt verified')
    print(json.dumps(actual,indent=2,sort_keys=True))


if __name__=='__main__':main()
