"""Replay finite exact rational π ternary certificates against pinned source formulae."""
from __future__ import annotations

import argparse
import json
import sys
from fractions import Fraction as Q
from pathlib import Path
if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from observational_succ.pi_ternary_handle import (
    SOURCE_ID, floor_scaled_pi, interval_for, ternary_word
)


def verify(data: dict) -> dict:
    if data.get('policy') != 'source-exact certified ternary digits; NOT BBP-style random access or pi normality':
        raise ValueError('incorrect witness truth boundary')
    start, count = data['start'],data['count']
    if type(start) is not int or type(count) is not int or not 1 <= start <= start+count-1 <= 4096:
        raise ValueError('invalid digit window')
    witnesses = data['witnesses']
    if not isinstance(witnesses,list) or not witnesses:
        raise ValueError('missing witnesses')
    reverse={v:k for k,v in SOURCE_ID.items()}
    matched=[]
    for rec in witnesses:
        source = reverse[rec['source']]
        terms=rec['terms']
        bound=interval_for(source, terms)
        if Q(rec['exact_lower']) != bound.low or Q(rec['exact_upper']) != bound.high:
            raise ValueError('bounds do not match published source and given cutoff')
        if rec['type']!='CERTIFIED_TERNARY_PI_PREFIX_v1' or rec['interval_form'] != bound.form:
            raise ValueError('mismatched source or certificate type')
        end = start+count-1
        if type(rec['fractional_digits']) is not int or rec['fractional_digits']!=end:
            raise ValueError('wrong certified prefix depth')
        import hashlib
        digest=hashlib.sha256((rec['exact_lower']+'\n'+rec['exact_upper']).encode()).hexdigest()
        if rec.get('exact_bounds_sha256')!=digest:
            raise ValueError('modified bound checksum')
        scale=3**end
        floorlo=floor_scaled_pi(bound.low,scale,bound.form)
        floorhi=floor_scaled_pi(bound.high,scale,bound.form)
        if floorlo!=floorhi or floorlo//scale!=3:
            raise ValueError('this interval does not certify a ternary prefix')
        prefix=ternary_word(floorlo-3*scale,end)
        if rec['floor_3pow_n_pi_lower']!=str(floorlo) or rec['floor_3pow_n_pi_upper']!=str(floorhi):
            raise ValueError('incorrect integer floor witnesses')
        if rec.get('certified') is not True or rec['base3_pi']!='10.'+prefix:
            raise ValueError('wrong digits or certification flag')
        matched.append((source,prefix))
    if len({n for n,_ in matched}) != len(matched) or len({s for _,s in matched}) !=1:
        raise ValueError('inconsistent or duplicate source witnesses')
    value=matched[0][1][start-1:]
    if data['digits']!=value:
        raise ValueError('incorrect requested digit substring')
    return {'certified':True,'start':start,'count':count,'digits':value,'sources':[n for n,_ in matched]}


def main(argv=None):
    p=argparse.ArgumentParser(description='Replay a source-authentic ternary pi certificate')
    p.add_argument('certificate',help='JSON created by pi_ternary_digits.py --certificate')
    args=p.parse_args(argv)
    try:
        data=json.loads(Path(args.certificate).read_text(encoding='utf-8'))
        result=verify(data)
    except (OSError,ValueError,KeyError,TypeError,ArithmeticError) as exc:
        print('CERTIFICATE REJECTED:',str(exc),file=sys.stderr)
        return 2
    print('EXACT TERNARY PI CERTIFICATE VERIFIED:',json.dumps(result,sort_keys=True))
    return 0

if __name__=='__main__': raise SystemExit(main())
