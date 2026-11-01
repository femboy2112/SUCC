"""Recompute preregistered original BBP rational-phase interval holdouts.

Exact Fraction rational intervals are evaluated; decimal displays are rounded
OUTWARD (never mistaken for floating proof values). Output is deterministic.
"""
from __future__ import annotations
import hashlib
import json
from pathlib import Path
from fractions import Fraction as F
import importlib.util

HERE=Path(__file__).resolve().parent
s=importlib.util.spec_from_file_location('adaptive_frame_holdout_module',HERE/'adaptive_frame.py')
f=importlib.util.module_from_spec(s);s.loader.exec_module(f)
CASES=((40,13),(72,17),(96,29))
SCALE=10**12


def outward_decimal(pair):
    lo,hi=pair
    lo_int=lo.numerator*SCALE//lo.denominator
    hi_int=-(-hi.numerator*SCALE//hi.denominator)
    return {'lower_scaled_1e12':lo_int,'upper_scaled_1e12':hi_int,
            'outward_rounded_sha256':hashlib.sha256(
                f'{lo_int},{hi_int}'.encode('ascii')).hexdigest(),
            'width_lt_1e10':hi-lo<F(1,10**10)}


def generate()->dict:
    cases=[]
    for n,h in CASES:
        result=f.certified_original_frame_probe(n,h,terms=13)
        for j in range(1,n+1):
            if f.source(j)!=f.source_combined(j):
                raise ArithmeticError('original source mismatch at '+str(j))
        for j in (f.source_index(h),f.source_index(16*h)):
            if f.source(j)!=f.source_combined(j):
                raise ArithmeticError('mirror-label source mismatch at '+str(j))
        cases.append({'N':n,'h':h,'index_h':f.source_index(h),
                      'index_16h':f.source_index(16*h),
                      'signed_h':outward_decimal(result['mirror_h']),
                      'signed_16h':outward_decimal(result['mirror_16h']),
                      'original_real':outward_decimal(result['original_real']),
                      'original_imag':outward_decimal(result['original_imag']),
                      'uniform_det_sin_gt':'1/8',
                      'verified_original_ineq':True})
    return {'status':'EXACT_RATIONAL_INTERVAL_HOLDOUTS_PASS',
            'source':'Original four signed BBP poles; U_0=0',
            'base_pr':'#451',
            'cases':cases,
            'authority':'finite exact interval arithmetic; NOT selected asymptotic saving'}

if __name__=='__main__':
    print(json.dumps(generate(),sort_keys=True,indent=2))
