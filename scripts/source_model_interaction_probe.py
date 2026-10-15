"""Replay exact-rational source/intermodel arithmetic and analysis receipts."""
from __future__ import annotations
import argparse
import json
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from observational_succ.source_model_interaction import interaction_receipt
from observational_succ.source_model_interval_quadrature import certified_real_xi


def receipt() -> dict:
    return {
        'source_model':interaction_receipt(),
        'fully_certified_finite_integral_values':{
            'critical_midpoint':certified_real_xi(__import__('fractions').Fraction(1,2),2,8,1024),
            'negative_even_minus_two':certified_real_xi(-2,2,8,1024),
            'positive_dual_three':certified_real_xi(3,2,8,1024),
        },
        'proof_status':'PROVED_LOCAL classical-import source/theta identities, exact rational finite certificate',
        'nontrivial_zero_coordinates_read':False,
        'global_Suzuki_Weil_positive':False,
        'RH_proved':False,
    }


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--verify',type=Path)
    p.add_argument('--output',type=Path)
    args=p.parse_args()
    data=receipt()
    if args.verify:
        if json.loads(args.verify.read_text())!=data:
            raise SystemExit('SOURCE_MODEL_RECEIPT_MISMATCH')
        print('SOURCE_MODEL_ANALYTIC_GLUING_RECEIPT_VERIFIED')
    else:
        out=json.dumps(data,sort_keys=True,indent=2)+'\n'
        if args.output:
            args.output.write_text(out)
        else:
            print(out,end='')

if __name__=='__main__':
    main()
