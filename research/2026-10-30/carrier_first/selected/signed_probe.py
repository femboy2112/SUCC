"""Fresh complete CRT phase windows, using pinned read-only interval code."""
from fractions import Fraction as Q
from math import isqrt
from pathlib import Path
import hashlib
import json
import subprocess
import types

from prime_frames import source, primary_part

PIN='f650aab0c8710b502f3e08ec1cb2b351c26b2b3f'
INPUT='research/2026-10-30/selected_finiteband/certified_band.py'


def isprime(p):return p>=2 and all(p%d for d in range(2,isqrt(p)+1))


def order(p):
    x=16%p;k=1
    while x!=1:x=x*16%p;k+=1
    return k


def main():
    raw=subprocess.check_output(['git','show',PIN+':'+INPUT])
    cb=types.ModuleType('pinned_certified_band')
    cb.__file__=INPUT
    exec(compile(raw,INPUT,'exec'),cb.__dict__)
    replacement=6017
    while not (isprime(replacement) and order(replacement)>=64):replacement+=4
    primes=(4201,5009,replacement,7001)
    assert all(isprime(p) and p%4==1 and order(p)>=64 for p in primes)
    starts={p:(p+7)//8 if p%8==1 else (p+3)//8 for p in primes}
    U=[Q()]
    for n in range(1,max(starts.values())+64):U.append(16*U[-1]+source(n))
    def chars(x):
        x=x%1
        return cb.trig(cb.fraction(x.numerator,x.denominator))
    def add(z,w):return cb.add(z[0],w[0]),cb.add(z[1],w[1])
    def norm2(z,N):return cb.div(cb.add(cb.square(z[0]),cb.square(z[1])),N*N)
    rows=[]
    for p in primes:
        A=starts[p]
        parts=[primary_part(U[n],p) for n in range(A,A+64)]
        assert len(set(parts))==64
        for h in (17,19):
            full=((0,0),(0,0));primary=((0,0),(0,0));direct=((0,0),(0,0))
            restore=0
            for n,a in zip(range(A,A+64),parts):
                v=U[n]-a
                zp,zv=chars(h*a),chars(h*v)
                full=add(full,cb.cmul(zp,zv))
                primary=add(primary,zp)
                direct=add(direct,chars(h*U[n]))
                dist=lambda q:min(q%1,1-q%1)
                restore+=dist(h*a)>=Q(1,20) and dist(h*U[n])<Q(1,20)
            f,pr,d=norm2(full,64),norm2(primary,64),norm2(direct,64)
            assert max(f[0],d[0])<=min(f[1],d[1])
            verdict='PASS' if f[1]<cb.S//4 else ('FAIL' if f[0]>=cb.S//4 else 'AMBIGUOUS')
            rows.append({'p':p,'A':A,'L':64,'h':h,'order16':order(p),
                         'full_squared_interval':list(map(str,f)),
                         'direct_squared_interval':list(map(str,d)),
                         'primary_squared_interval':list(map(str,pr)),
                         'bits':cb.P,'verdict':verdict,'primary_far_full_near':restore,
                         'primary_first':str(parts[0])})
    controls=[]
    for label,cs,ds in [('original',(4,-2,-1,-1),(1,4,5,6)),
                        ('wrong_ratio',(5,-2,-1,-1),(1,4,5,6)),
                        ('same_ratio',(4,0,-1,0),(1,4,5,6)),
                        ('positive_rank_matched',(5,-5,0,0),(1,4,5,6)),
                        ('seven_pole_null',(-8,8,4,8,2,2,-1),tuple(range(1,8)))]:
        x=Q();slips=0
        for n in range(1,258):
            y=16*x+sum((Q(c,8*n-8+d) for c,d in zip(cs,ds)),Q())
            if 129<=n<=256:
                t=(y-x)%1;slips+=min(t,1-t)>=Q(1,20)
            x=y
        controls.append({'source':label,'lag_slips':slips,'samples':128})
    assert controls[-1]['lag_slips']==0
    result={'status':'FINITE OBSERVATIONS ONLY','full_product_retained':True,
            'pinned_interval_source':{'commit':PIN,'path':INPUT,'sha256':hashlib.sha256(raw).hexdigest()},
            'rows':rows,'controls':controls,
            'boundary':'No prime independence, no asymptotic estimate, no coverage theorem.'}
    p=Path(__file__).parent/'receipts'/'signed-data.json'
    if p.exists():raise RuntimeError('preserve earlier run')
    p.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
