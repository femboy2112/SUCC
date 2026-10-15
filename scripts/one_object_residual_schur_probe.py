#!/usr/bin/env python3
"""Deterministic exact scientific receipt; optional real original-source gate."""
from __future__ import annotations
import argparse
import json
from fractions import Fraction
from pathlib import Path
from observational_succ.one_object_residual_schur import schema_receipt, parent_original_source_contract


def normalize(x):
    if isinstance(x, Fraction):return f'{x.numerator}/{x.denominator}'
    if isinstance(x, dict):return {str(k):normalize(v) for k,v in x.items()}
    if isinstance(x, (list,tuple)):return [normalize(v) for v in x]
    return x


def document():
    return json.dumps(normalize(schema_receipt()),sort_keys=True,indent=2)+'\n'


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--verify',type=Path)
    parser.add_argument('--require-authentic-source',action='store_true')
    args=parser.parse_args()
    if args.require_authentic_source:
        genuine=parent_original_source_contract()
        assert genuine['source_git_blob_sha']=='0cc8510b71d178fc79e8d410a86d8b6014cf9178'
        assert genuine['Weil_positivity_proved'] is False
        print('ONE_OBJECT_AUTHENTIC_SOURCE_TATE_WEIL_SUZUKI_VERIFIED')
    txt=document()
    if args.verify:
        if args.verify.read_text()!=txt:
            raise SystemExit('RECEIPT_DRIFT: source/proof claim changed')
        print('ONE_OBJECT_SHORTING_EXACT_RECEIPT_VERIFIED')
    elif not args.require_authentic_source:
        print(txt,end='')

if __name__=='__main__':main()
