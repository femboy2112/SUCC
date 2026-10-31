"""Predeclared exact rational-frame cases; integer endpoints are authority."""
import hashlib
import json
from pathlib import Path
from fractions import Fraction as Q
from prime_frames import *


def serial_vector(v):
    return '\n'.join(f'{p}:{x}' for p,x in v.items())


def main():
    rows=[]
    cases=[('discovery',n,m) for n,m in [(1,1),(2,2),(3,3),(5,4),(8,6)]]
    cases += [('holdout',n,m) for n,m in [(4,5),(7,7),(11,10),(17,13)]]
    cases += [('moving',n,moving_order(n)) for n in (1,3,7,17)]
    for label,n,m in cases:
        vector=prime_vector(n,m)
        lo,hi=linear_log_interval(vector,512,256)
        q=selected(n);e=error_bound(n,m)
        a,b=Q(lo,2**512),Q(hi,2**512)
        err=(q-b,q-a) if m%2==0 else (a-q,b-q)
        assert 0 < err[0] <= err[1] < e,(n,m,err,e)
        rows.append({'label':label,'n':n,'m':m,'bits':512,
                     'frame_interval':[str(lo),str(hi)],'exact_U':str(q),
                     'exact_error_bound':str(e),'prime_count':len(vector),
                     'max_prime':max(vector),'signed_coefficient_l1':str(sum(abs(x) for x in vector.values())),
                     'prime_vector_sha256':hashlib.sha256(serial_vector(vector).encode()).hexdigest()})
    decoding=[]
    for n in (1,2,3,5,9):
        q=reconstruct(n,512,256)
        assert q==selected(n)
        decoding.append({'n':n,'m':reconstruction_order(n),'D':str(source_denominator(n)),
                         'decoded_U':str(q)})
    # Positive rank-two mutant shares the method, with its own factor5 upper bound.
    mutant=[]
    for n,m in [(3,3),(7,7)]:
        lo,hi=frame_interval(n,m,384,192,(5,-5,0,0))
        q=selected(n,coeff=(5,-5,0,0));e=Q(5,4)*error_bound(n,m)
        a,b=(q-hi,q-lo) if m%2==0 else (lo-q,hi-q)
        assert 0<a<=b<e
        mutant.append({'n':n,'m':m,'status':'same transport sign; own constant; not identifying'})
    result={'status':'PASS','authority':'exact integer/rational finite certificates; paper proof supplies all n,m',
            'rows':rows,'rational_decoding':decoding,'rank_matched_mutant':mutant}
    target=Path(__file__).parent/'receipts'/'frame-data.json'
    target.parent.mkdir(exist_ok=True)
    if target.exists(): raise RuntimeError('preserve previous result; choose new output')
    target.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
