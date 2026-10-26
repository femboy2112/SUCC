#!/usr/bin/env python3
"""Deterministic finite signed receipts; --verify rejects a changed receipt."""
from __future__ import annotations
import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from observational_succ.oily_signed_certificate import (  # noqa: E402
    Interval, authentic_signed_certificate, machin_pi_enclosure)

DEFAULT = ROOT / 'research/2026-10-26/OILY_SIGNED_CERTIFICATE_RECEIPT.json'
SOURCE_FILES = ('observational_succ/oily_signed_certificate.py',
                'observational_succ/pi_lag_carry.py',
                'observational_succ/pi_source_collision.py',
                'scripts/oily_signed_certificate_probe.py')


def encode(value):
    if isinstance(value, Fraction):
        return f'{value.numerator}/{value.denominator}'
    if isinstance(value, Interval):
        return {'lower': encode(value.lower), 'upper': encode(value.upper)}
    if isinstance(value, dict):
        return {k: encode(v) for k,v in value.items()}
    if isinstance(value, (list,tuple)):
        return [encode(v) for v in value]
    return value


def receipt():
    # Short construction cases, then disjoint larger held-out time windows.
    cases = [(32,1,8),(32,2,8),(96,1,16),(96,3,16),
             (257,1,17),(257,2,17),(257,7,17)]
    data=[]
    for N,h,L in cases:
        row=authentic_signed_certificate(N,h,L)
        carries=row.pop('carries')
        row['carry_sha256']=hashlib.sha256(json.dumps(carries).encode()).hexdigest()
        data.append(row)
    return encode({'schema':'oily-selected-signed-enclosure-v1',
                   'parent_commit':'a8c7c85b7a1900d422090f1757c174e7aac69f44',
                   'source':'original four-pole, zero seed; finite prefixes only',
                   'source_sha256':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest()
                                    for p in SOURCE_FILES},
                   'pi_normalizer':machin_pi_enclosure(),
                   'cases':data,'infinite_cancellation_proved':False})


def main():
    parser=argparse.ArgumentParser()
    action=parser.add_mutually_exclusive_group(required=True)
    action.add_argument('--write',action='store_true')
    action.add_argument('--verify',action='store_true')
    parser.add_argument('--receipt',type=Path,default=DEFAULT)
    args=parser.parse_args()
    expected=json.dumps(receipt(),indent=2,sort_keys=True)+'\n'
    if args.write:
        args.receipt.write_text(expected)
        print('WROTE',args.receipt.name)
    elif args.receipt.read_text()!=expected:
        print('RECEIPT_MISMATCH',file=sys.stderr)
        return 1
    else:
        print('FINITE_SIGNED_RECEIPT_VERIFIED')
    return 0


if __name__=='__main__':
    raise SystemExit(main())
