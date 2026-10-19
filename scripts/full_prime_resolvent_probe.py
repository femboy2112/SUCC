#!/usr/bin/env python3
"""Replay the whole-continuum original signed-source prime inverse certificate."""
import argparse
from fractions import Fraction
from hashlib import sha256
import json
from pathlib import Path
import resource
import sys
import time

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from observational_succ.full_prime_resolvent import source_schur_improvement


def budget_receipt(value):
    """Directed rational display plus exact integer-byte digest for huge audits.

    The Bessel denominator can exceed Python's text safety cap. Mathematical
    verification uses the full Fraction; this rendering is not a new bound.
    """
    if isinstance(value,Fraction):
        n,d=value.numerator,value.denominator
        raw=(str(n<0)+':'+format(abs(n),'x')+'/'+format(d,'x')).encode('ascii')
        denominator=10**15
        lower=(n*denominator)//d
        upper=-((-n*denominator)//d)
        return {'outward_lower':str(Fraction(lower,denominator)),
                'outward_upper':str(Fraction(upper,denominator)),
                'exact_signed_hex_fraction_sha256':sha256(raw).hexdigest(),
                'numerator_bits':abs(n).bit_length(),'denominator_bits':d.bit_length()}
    if isinstance(value,dict):return {k:budget_receipt(v)for k,v in value.items()}
    if isinstance(value,(tuple,list)):return [budget_receipt(v)for v in value]
    return value


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--source',action='store_true')
    p.add_argument('--J',type=int,default=8)
    p.add_argument('--M',type=int,default=80)
    p.add_argument('--output')
    p.add_argument('--audit-capsules',action='store_true')
    args=p.parse_args()
    if args.audit_capsules:
        from observational_succ.source_proof_certificate import audit_capsules
        records=json.loads((ROOT/'research/2026-10-18/ROUND2_SIGNED_CAPSULES.json').read_text())
        print(json.dumps(audit_capsules(records,ROOT),sort_keys=True,indent=2))
        return
    if not args.source or not args.output:
        raise SystemExit('The original source and output file must be explicitly selected.')
    if hasattr(sys,'set_int_max_str_digits'):sys.set_int_max_str_digits(50000)
    resource.setrlimit(resource.RLIMIT_AS,(1024**3,1024**3))
    resource.setrlimit(resource.RLIMIT_CPU,(240,240))
    start=time.monotonic()
    result=source_schur_improvement(J=args.J,M=args.M)
    result['source_high_budget_audit']=budget_receipt(result['source_high_budget_audit'])
    result['execution']={'argv':sys.argv,'python':sys.version,
        'elapsed_seconds':time.monotonic()-start,
        'peak_KiB':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        'resource_caps':'240 CPU seconds; 1 GiB address space; single process',
        'authority':'PAPER_PROVED with exact rational instance check; no Lean authority'}
    Path(args.output).write_text(json.dumps(result,default=lambda v:str(v),sort_keys=True,indent=2)+'\n')
    summary={'both_blocks_strictly_improved':result['both_blocks_strictly_improved'],
        'first_window_sign_certified':result['first_window_sign_certified'],'RH_proved':False,
        'sectors':{name:{'gain_PD':d['gain_PD'],'new_lower_PSD':d['new_lower_PSD'],
            'old_lower_approx':[[float(v)for v in row]for row in d['old_lower']],
            'new_lower_approx':[[float(v)for v in row]for row in d['new_lower']],
            'gain_approx':[[float(v)for v in row]for row in d['gain']]}
            for name,d in result['sectors'].items()},'execution':result['execution']}
    print(json.dumps(summary,sort_keys=True,indent=2))


if __name__=='__main__':main()
