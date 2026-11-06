"""Preregistered projection ablations and finite de Bruijn prefix."""
from fractions import Fraction as F
from itertools import combinations
import json
from math import lcm

from hostile_probe import forcing, integer_path, orbit, prime, sparse


def debruijn():
    edges = [list(range(16)) for i in range(16)]
    stack, route = [0], []
    while stack:
        if edges[stack[-1]]:
            stack.append(edges[stack[-1]].pop())
        else:
            route.append(stack.pop())
    route.reverse()
    assert len(route)==257 and len(set(zip(route,route[1:])))==256
    numerator = 0
    for digit in route:
        numerator = 16*numerator+digit
    x = F(numerator,16**len(route))
    assert (x*16**len(route)) % 1 == 0
    return {'first_pairs':256, 'distinct_pairs':256, 'zero_from_digit':258}


def run():
    last = 128
    actual, clocks, _ = integer_path(last)
    terms = [F(0)]+[forcing(n) for n in range(1,3*last+1)]
    native = F(round(-clocks[64]*actual[128]/16**128),clocks[64])
    paths = {'genuine':actual,
             'fixed_rational_seed':orbit(terms[:last+1],F(1,7)),
             'source_native_seed':orbit(terms[:last+1],native)}
    for method in ('ternary','dyadic'):
        paths[method]=sparse(terms,clocks,method)[0]
    for label, mutation in (('pole_flip', lambda n:F(2,8*n-2)),
                            ('jet6', lambda n:F(1,(8*n+1)**6))):
        paths[label]=orbit([F(0)]+[terms[n]+mutation(n) for n in range(1,last+1)])
    born=[b for b in range(1,last+1) if prime(8*b-7)]
    passed = {}
    full_prefix = []
    for name,path in paths.items():
        rr=[F(0)]+[path[n]-16*path[n-1] for n in range(1,last+1)]
        newclock = 1
        allclock = True
        for n in range(1,last+1):
            newclock=lcm(newclock,rr[n].denominator)
            allclock &= newclock==clocks[n]
        features = {'G':all(rr[b]==terms[b] for b in born),
                    'P':all((path[n]-actual[n]).denominator % (8*b-7)
                            for b in born for n in range(b,min(2*b,last+1))),
                    'C':allclock,'Z':path[0]==0}
        passed[name] = ''.join(c for c,hit in features.items() if hit)
        if path==actual:
            full_prefix.append(name)
    rows = {''.join(subset) or 'empty': sorted(name for name,s in passed.items() if set(subset)<=set(s))
            for size in range(5) for subset in combinations('GPCZ',size)}
    assert rows['GPCZ']==['dyadic','genuine','ternary']
    assert full_prefix==['genuine']
    return {'features':passed,'survivors':rows,'full_numerator_history':full_prefix,
            'debruijn_prefix':debruijn(),'last':last}

if __name__=='__main__':
    print(json.dumps(run(),indent=2,sort_keys=True))
