"""Fresh exact CDF and lasso checks of the parent's observer instrument."""
from collections import Counter
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import hashlib
import importlib.util
import json
import sys

parent=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('reviewed_observer',parent/'observer.py')
module=importlib.util.module_from_spec(spec)
sys.modules[spec.name]=module
spec.loader.exec_module(module)


def cdf_distance(points):
    counts=Counter(points)
    breaks=sorted(set(points)|{F(0),F(1)})
    mass=F(0);out=F(0);N=len(points)
    for a,z in zip(breaks,breaks[1:]):
        mass+=F(counts[a],N)
        lo,hi=a-mass,z-mass
        out+=(hi*abs(hi)-lo*abs(lo))/2
    return out


def brute_lasso(word):
    N=len(word)
    if not N:return 0
    for size in range(1,N+1):
        for period in range(1,size+1):
            pre=size-period
            if all(word[i]==word[pre+(i-pre)%period] for i in range(pre,N)):
                return size
    raise AssertionError


lassos=0
for N in range(1,11):
    for word in product((0,1),repeat=N):
        want=brute_lasso(word)
        got,witness=module.minimal_states(word)
        assert got==want,(word,got,want)
        a,p=witness
        assert a+p==got
        assert all(word[i]==word[a+(i-a)%p] for i in range(a,N))
        lassos+=1

cases=0
minimum_slack=None
for base in (2,3,5,16):
    for den in (7,17,29):
        for num in (0,1,den//2,den-1):
            for N in (1,2,7,19):
                x=F(num,den);points=[]
                for _ in range(N+1):
                    points.append(x);x=(base*x)%1
                for k in (0,1,3,5):
                    cells=Counter((int(base*u),int(base**k*v)) for u,v in zip(points,points[1:]))
                    totals=Counter()
                    for (d,v),c in cells.items():totals[v]+=c
                    rho=F(0)
                    for v,c in totals.items():
                        # CDF distance for conditional digit grid, in original count units.
                        for threshold in range(base-1):
                            cum=sum(z for (d,w),z in cells.items() if w==v and d<=threshold)
                            rho+=abs(F(cum,N)-F(c*(threshold+1),base*N))/base
                    bound=(base*rho+F(1,base**k)+F(1,N))/(base-1)
                    actual=cdf_distance(points[:-1])
                    assert actual==module.w1_uniform(points[:-1])
                    assert bound==module.transport_bound(cells,k,base)
                    assert actual<=bound,(base,den,num,N,k,actual,bound)
                    slack=bound-actual
                    minimum_slack=slack if minimum_slack is None else min(minimum_slack,slack)
                    cases+=1

print(json.dumps({'status':'PASS','finite_words_brute_lasso':lassos,
    'exact_interval_W1_cases':cases,'minimum_O2_slack':str(minimum_slack),
    'reviewed_inputs':{name:hashlib.sha256((parent/name).read_bytes()).hexdigest()
                       for name in ('OBSERVER_THEOREMS.md','observer.py')},
    'authority':'same-model paper reconstruction and distinct exact implementation'},indent=2))
