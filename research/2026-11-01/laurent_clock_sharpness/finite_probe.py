"""Regenerate exact rational finite receipts, without claiming limit proofs."""
from __future__ import annotations
import json,argparse
from pathlib import Path
import sharpness as x
from fractions import Fraction as F

HERE=Path(__file__).resolve().parent


def receipt():
    out={'scope':'Finite exact checks; all-horizon sharpness requires paper proof.',
         'parent_pr':454,'source':'original 4 signed BBP poles','original_seed':'0; changed seed is explicitly a separate real model',
         'leading':{},'profiles':{},'derivative_checks':[],'negative_control':{}}
    for d in range(1,9):
        out['leading'][str(d)]=str(x.infinite_leading(d))
    for d,c in [(1,F(5,2)),(2,F(7,2)),(3,F(9,2)),(4,F(11,2))]:
        a,r,g=x.limiting_profile(d,c)
        out['profiles'][str(d)]={'c':str(c),'transition_fraction':str(a),'predicted_reduced_limit':str(r),'predicted_gap':str(g)}
    for d,n,k in [(1,101,7),(2,131,17),(3,257,13),(4,503,17),(5,809,11)]:
        checks=x.derivative_certificate(n,k,d)
        out['derivative_checks'].append({'d':d,'n':n,'k':k,'envelopes_pass':all(checks[nm+'_error']<=checks[nm+'_bound'] for nm in ('value','first','second')),
               'scaled_residual':str(x.residual(n,k,d)/16**k),'finite_leading':str(x.finite_leading(k,d)),
               'leading_error_bound':str(checks['value_bound'])})
    out['negative_control']={'d2_n10000':x.mutation_fails_source_contract(10000,1,2),
                             'd3_n10000':x.mutation_fails_source_contract(10000,2,3)}
    return out


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--check',action='store_true')
    a=p.parse_args()
    data=receipt()
    serialized=json.dumps(data,indent=2,sort_keys=True)+'\n'
    output=HERE/'FINITE_RECEIPT.json'
    if a.check:
        assert output.read_text()==serialized,'finite exact receipt differs'
        print('EXACT_FINITE_RECEIPT_MATCH')
    else:
        output.write_text(serialized)
        print('CREATED_EXACT_FINITE_RECEIPT')

if __name__=='__main__':main()
