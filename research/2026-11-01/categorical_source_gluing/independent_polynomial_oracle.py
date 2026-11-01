"""Pure-stdlib exact verifier of the SymPy-generated algebraic certificate.

No SymPy import. Coefficients are ascending tuples of integers. This verifies
identities for symbolic z, not merely a finite sample grid. It is not Lean.
"""
from __future__ import annotations
import json
from math import comb
from pathlib import Path

def trim(a):
    a=list(a)
    while len(a)>1 and a[-1]==0:a.pop()
    return tuple(a or [0])
def add(a,b):
    out=[0]*max(len(a),len(b))
    for i,x in enumerate(a):out[i]+=x
    for i,x in enumerate(b):out[i]+=x
    return trim(out)
def scale(a,c):return trim([c*x for x in a])
def mul(a,b):
    out=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):out[i+j]+=x*y
    return trim(out)
def power(a,n):
    out=(1,)
    for _ in range(n):out=mul(out,a)
    return out
def shift(a,c):
    out=[0]*len(a)
    for n,x in enumerate(a):
        for k in range(n+1):out[k]+=x*comb(n,k)*c**(n-k)
    return trim(out)
def eval_at(a,x):
    out=0
    for c in reversed(a):out=out*x+c
    return out

def verify(certificate):
    A=power((-7,8),4)
    D=mul(mul(power((-4,8),2),(-3,8)),(-2,8))
    A1=shift(A,1);D1=shift(D,1)
    def clear(terms,d):
        out=(0,)
        for (i,j),coef in terms:
            p=mul(mul(power(A,i),power(D,d-i)),mul(power(A1,j),power(D1,d-j)))
            out=add(out,scale(p,int(coef)))
        return out
    den=clear(certificate['inverse_denominator_terms'],3)
    num=clear(certificate['inverse_numerator_terms'],3)
    ident=add(mul((0,1),den),scale(num,-1))
    relation=clear(certificate['delay_curve_terms'],4)
    positive=shift(den,1)
    claims={
        'stdlib_symbolic_inverse_identity':ident==(0,),
        'stdlib_delay_curve_identity':relation==(0,),
        'stdlib_inverse_nonzero':den!=(0,),
        'stdlib_original_zero_chart_nonzero':eval_at(den,0)!=0,
        'stdlib_shifted_chart_all_coefficients_positive':all(x>0 for x in positive),
        'stdlib_shifted_chart_matches_receipt':list(positive)==[int(x) for x in certificate['all_horizon_inverse_chart']['shifted_cleared_denominator_coefficients_ascending']],
        'independent_algorithm':'integer coefficient convolution and binomial shift; no SymPy',
        'cleared_inverse_degree':len(den)-1,
    }
    if not all(v for k,v in claims.items() if k.startswith('stdlib_')):
        raise ArithmeticError('exact polynomial certificate failed')
    return claims

if __name__=='__main__':
    receipts=Path(__file__).resolve().parent/'receipts'
    data=verify(json.loads((receipts/'cover_certificate.json').read_text()))
    (receipts/'independent_polynomial_receipt.json').write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps(data,indent=2))
