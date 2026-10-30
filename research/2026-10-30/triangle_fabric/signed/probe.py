"""Declared finite checks; paper proof supplies universal authority."""
import json, sys
from pathlib import Path
from fractions import Fraction as Q
from filters import *
from test_filters import CASES


def enc(x):
    if isinstance(x,Q): return str(x)
    if isinstance(x,dict): return {k:enc(v) for k,v in x.items()}
    if isinstance(x,(list,tuple)): return list(map(enc,x))
    return x

rows=[]
for n,m in CASES:
    f=matched_filter(n,m); p=orthogonal(n,m)
    lo,hi=sign_error_bounds(n,m)
    rows.append(dict(N=n,M=m,holdout=(n,m) in CASES[7:],polynomial=p,filter=f,
        F16=evaluate(f,16),relative_bound=Q(1,15**(n+m)),boundary=boundary(f)[1],
        error_sign=(-1)**m,error_magnitude_interval=[lo,hi],
        next_source_residual=apply_filter(f,n+1)-force(n+1),
        zero_prefix_residuals=[apply_filter(f,k)-force(k) for k in range(1,n+1)],
        jet_residuals=[pole_jet(f,k)-pole_jet((Q(1),),k) for k in range(m+3)]))
dyadic=[]
for n,m in ((0,2),(2,4),(5,4),(8,6)):
    f,row=dyadic_filter(n,m)
    onset=1+(row['denominator_power']+3)//4
    eps=Q(1,15**(n+m))
    row.update(filter=f,onset=onset,relative_bound=eps,
               first_postprefix_residual=apply_filter(f,n+1)-force(n+1))
    row['coherent_rows']=[]
    for h in (1,3,17):
        a=max(onset,24)
        row['coherent_rows'].append(dict(h=h,A=a,
          infinite_weyl_deviation_upper=abs(h)*(1+eps)/Q(8*a-7),
          infinite_lag_energy_upper=Q(1024,5)*h*h*(1+eps)**2/Q((8*a-7)**5),
          tail_sample=tail_from_filter(f,a)))
    dyadic.append(row)
result=dict(status='EXACT FINITE PASS if companion test and oracle pass',
            authority='paper proofs separate from finite checks',
            parent='6cf5050ff2cfd92e7a0c8876da5233be6ff117f5',
            cases=rows,dyadic=dyadic)
out=Path(sys.argv[1])
if out.exists(): raise FileExistsError(out)
out.write_text(json.dumps(enc(result),indent=2)+'\n')
print(json.dumps(dict(filter_cases=len(rows),dyadic_cases=len(dyadic),out=str(out))))
