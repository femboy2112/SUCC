"""Preregistered authentic records and hostile finite-depth controls."""
import hashlib
import json
from pathlib import Path
from fractions import Fraction as Q
from observer import completed_bbp_word,word_counts,branch_cost,transport_bound,minimal_states,debruijn


def main():
    w=completed_bbp_word(1028)
    rows=[]
    for N in (128,256,512,1024):
        S,witness=minimal_states(w[:N])
        for k in range(4 if N<512 else 5):
            c=word_counts(w,N,k)
            r=branch_cost(c)
            rows.append(dict(N=N,k=k,partition='discovery' if N<512 else 'fresh',
                **{a:str(v) if isinstance(v,Q) else v for a,v in r.items() if a!='N'},
                w1_upper=str(transport_bound(c,k)),minimal_states=S,lasso=witness,
                counts=[[d,v,n] for (d,v),n in sorted(c.items())]))
    controls=[]
    for name,period in [('zero',(0,)),('period01',(0,1)),('binary_debruijn',debruijn(2,5))]:
        b=2 if name=='binary_debruijn' else 16;N=128;ww=(period*((N+7)//len(period)+1))[:N+6]
        for k in range(6):
            r=branch_cost(word_counts(ww,N,k,b),b)
            controls.append(dict(name=name,b=b,k=k,rho=str(r['rho']),deficiency=r['deficiency'],
                                 minimal_states=minimal_states(ww[:N])[0]))
    sparse=tuple(int(i in {3**j for j in range(7)}) for i in range(1,1029))
    controls.append(dict(name='finite-exponent-sparse3',N=1024,minimal_states=minimal_states(sparse[:1024])[0],
                         status='nonnormal infinite control; finite prefix state calculation'))
    out={'status':'PASS finite instrument execution only','word_hex':''.join(format(d,'X') for d in w),
         'word_sha256':hashlib.sha256(bytes(w)).hexdigest(),'selected':rows,'controls':controls,
         'authority':'exact counts/costs; entropy decimals are observations, no interval claims'}
    dest=Path(__file__).parent/'receipts'/'observer-data.json'
    if dest.exists():raise FileExistsError(dest)
    dest.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({'status':out['status'],'word_sha256':out['word_sha256'],
                      'selected':[{k:v for k,v in row.items() if k!='counts'} for row in rows],
                      'controls':controls},indent=2))


if __name__=='__main__':main()
