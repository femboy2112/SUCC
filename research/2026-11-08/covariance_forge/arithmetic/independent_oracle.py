"""Independent literal-four-pole arithmetic, no production source import."""
from fractions import Fraction as Q
from math import gcd


def check(w):
    states=[Q(0)]
    for n in range(1,w['B']+1):
        r=4/Q(8*n-7)-2/Q(8*n-4)-1/Q(8*n-3)-1/Q(8*n-2)
        states.append(16*states[-1]+r)
    assert states==w['original']
    d=states[-1].denominator
    a=states[-1].numerator
    forbidden={}
    scale=16**w['B']*2**w['K']*(d//w['q'])
    for p in w['used_primes']:
        assert d%p==0 and (d//p)%p!=0
        banned=(-a*pow(scale,-1,p))%p
        forbidden[p]=tuple(m for m in range(w['m0'],w['m0']+w['t']+1) if m%p==banned)
        assert len(forbidden[p])<=1
    blocked=set(m for rows in forbidden.values() for m in rows)
    assert len(blocked)<=w['t']
    expected=next(m for m in range(w['m0'],w['m0']+w['t']+1) if m not in blocked)
    assert expected==w['m']
    assert gcd(a+scale*expected,d)==1
    assert (states[-1]+16**w['B']*w['seed']).denominator==d
    return {'independent_source_states':len(states),'prime_avoidance_checks':len(forbidden),
            'blocked_candidates':len(blocked)}
