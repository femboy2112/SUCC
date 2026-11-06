"""Reproducible exact Fraction critical tail/source receipt. Not normality evidence."""
from __future__ import annotations
import argparse,hashlib,json
from pathlib import Path
from critical_chirp import forcing,forcing_polynomial,rigorous_tail_sandwich

HOLDOUT=(137,509,911)
DEVELOPMENT=(1,2,3,4,5,6,7,8,11,16,32,64,127,256)


def row(n:int)->dict:
    z=rigorous_tail_sandwich(n,20)
    assert forcing(n)==forcing_polynomial(n)
    raw={"n":n,"r":str(forcing(n)),"tail_lo":str(z['tail_lower']),
         "tail_hi":str(z['tail_upper']),"main":str(z['model']),
         "error":str(z['max_error'])}
    digest=hashlib.sha256(json.dumps(raw,sort_keys=True,separators=(',',':')).encode()).hexdigest()
    return {"n":n,"source_oracles_equal":True,
            "exact_fraction_record_sha256":digest,
            "n3_scaled_error_lower_bound_display":format(float(n**3*(z['model']-z['tail_upper'])),'.12f'),
            "n3_scaled_error_upper_bound_display":format(float(n**3*(z['model']-z['tail_lower'])),'.12f'),
            "strict_tail_bound":z['tail_upper']<z['model'] and z['model']-z['tail_lower']<z['max_error']}


def receipt()->dict:
    return {"name":"SUCC critical coherent chirp: exact Fraction source tail",
            "parent":"af5c7ba30ea57d725bd334310798357d50f12fce",
            "preregistered_holdout_n":list(HOLDOUT),
            "development_n":list(DEVELOPMENT),
            "status":"finite exact source check; coherent asymptotic paper proof; original zero-seed gate OPEN",
            "pi_base16_normality":"OPEN",
            "rows":[row(n) for n in HOLDOUT]}


def output()->str:
    return json.dumps(receipt(),indent=2,sort_keys=True)+'\n'

if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--write',type=Path)
    p.add_argument('--verify',type=Path)
    args=p.parse_args()
    s=output()
    if args.write: args.write.write_text(s)
    if args.verify:
        assert args.verify.read_text()==s, 'exact Fraction receipt changed'
        print('CRITICAL_CHIRP_FRACTION_RECEIPT_VERIFIED')
    if not args.write and not args.verify: print(s)
