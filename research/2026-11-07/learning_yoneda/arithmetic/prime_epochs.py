"""Original-source complete prime cycles and exact epoch gluing controls."""
from collections import Counter
from fractions import Fraction as Q
from math import isqrt
from finite_adelic import exact_integer, odd_prime, primes_through, history, principal


def order16(p):
    odd_prime(p)
    value=16%p
    order=1
    while value != 1:
        value=value*16%p
        order+=1
    return order


def window(p):
    odd_prime(p)
    if p % 8 != 1:
        raise ValueError('the clean aligned epoch requires p == 1 mod 8')
    L=(p-1)//4
    return {'p':p,'L':L,'birth':(p+7)//8,'next_pole':(p+1)//2,
            'start':L+1,'stop':2*L+1,'order':order16(p)}


def good_prime(A):
    exact_integer(A,'epoch',1)
    for p in reversed(primes_through(4*A)):
        if p%8==1 and order16(p)**3>p:
            return p
    return None


def variation(A,p):
    exact_integer(A,'epoch',1)
    w=window(p)
    overlap=max(0,min(2*A,w['stop'])-max(A,w['start']))
    return 2*(1-Q(overlap,max(A,w['L'])))


def exact_clean_check(p):
    w=window(p)
    values=history(w['next_pole'])
    # Independently enumerate zeros of the four combined denominator factors.
    poles=[n for n in range(1,w['next_pole']+1)
           if any(f%p==0 for f in (2*n-1,4*n-1,8*n-7,8*n-3))]
    assert poles==[w['birth'],w['next_pole']]
    counts=Counter()
    for n in range(w['birth'],w['next_pole']):
        expected=Q(4*pow(16,n-w['birth'],p)%p,p)
        assert principal(values[n],p)==expected
        if w['start']<=n<w['stop']:
            counts[expected]+=1
    assert w['L']%w['order']==0
    assert len(counts)==w['order']
    assert set(counts.values())=={w['L']//w['order']}
    # The next pole genuinely changes the old continuation by -1/(2p).
    continued=Q(4*pow(16,w['next_pole']-w['birth'],p)%p,p)
    assert principal(values[w['next_pole']]-continued,p)==Q((-pow(2,-1,p))%p,p)
    return w,counts


def gauss_rational_upper(p,h=1):
    w=window(p)
    if type(h) is not int or h%p==0:
        raise ValueError('nonzero additive character modulo p required')
    return Q(isqrt(p)+1,w['order'])
