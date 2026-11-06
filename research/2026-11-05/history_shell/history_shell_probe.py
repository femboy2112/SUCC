"""Authenticated SUCC shell transitions and exact conditional-history controls.

The source and all selected states use exact Fraction. Conditional probabilities
refer to declared uniform within-cylinder models, NOT the selected zero seed.
"""
from fractions import Fraction as Q
from functools import lru_cache
from collections import defaultdict

@lru_cache(None)
def forcing(n):
    assert n>=1
    f=Q(4,8*n-7)-Q(2,8*n-4)-Q(1,8*n-3)-Q(1,8*n-2)
    oracle=Q(120*n*n-89*n+16,(2*n-1)*(4*n-1)*(8*n-7)*(8*n-3))
    assert f==oracle
    return f

@lru_cache(None)
def states(N):
    v=Q(0);out=[v]
    for n in range(1,N+1):
        v=16*v+forcing(n)
        out.append(v)
    return tuple(out)

def block(n,k):
    assert k>=1
    return sum((16**(k-j)*forcing(n+j) for j in range(1,k+1)),Q())

def shell(x,n,m,k):
    """Selected cell, actual branch bit, and conditional uniform-microstate prior."""
    assert m>=1 and k>=1
    x=Q(x)%1
    a=(16**(m+k)*x).__floor__()
    theta=(16**(m+k)*x)%1
    source=16**m*block(n,k)
    q=source.__floor__();delta=source%1
    b=int(theta+delta>=1)
    observed=(16**m*((16**k*x+block(n,k))%1)).__floor__()
    prediction=(a+q+b)%(16**m)
    assert observed==prediction
    return dict(prefix=a,microstate=theta,source_integer=q,source_fraction=delta,
                selected_bit=b,actual_cell=observed,
                alternatives=((a+q)%(16**m),(a+q+1)%(16**m)),
                probabilities=(1-delta,delta))

def original_epoch(A,m,k):
    u=states(2*A-1+k)
    observations=[shell(u[n],n,m,k) for n in range(A,2*A)]
    return dict(A=A,m=m,k=k,count=sum(v['selected_bit'] for v in observations),
       expected=sum((v['source_fraction'] for v in observations),Q()),
       min_delta=min(v['source_fraction'] for v in observations),
       max_delta=max(v['source_fraction'] for v in observations),
       items=observations)

def nonlumpability(d1,d2,m=1):
    """Exact two-stage uncertainty under re-uniformization versus full history."""
    assert m>=1 and 0<=d1<1 and 0<=d2<1
    a,b=Q(d1),Q(d2)
    naive=( (1-a)*(1-b), a*(1-b)+(1-a)*b, a*b )
    c=int(a+b>=1)
    t=(a+b)%1
    direct=tuple((1-t if j==c else t if j==c+1 else Q(0)) for j in range(3))
    tv=sum(abs(x-y) for x,y in zip(naive,direct))/2
    assert tv==2*min(a*b,(1-a)*(1-b))
    return dict(naive=naive,direct=direct,total_variation=tv)

def source_nonlumpability(n,m):
    d1=(16**(m+1)*forcing(n+1))%1
    d2=(16**m*forcing(n+2))%1
    return d1,d2,nonlumpability(d1,d2,m)

def source_future(n,k):
    return block(n,k)

def word_intervals(word,src=None):
    """Exact preimage of a finite first-digit chronological word under Haar seed.

    Each orbit value is x_i={16**i*s + cumulative_source_i}.
    Return disjoint source-seed intervals whose total length is the probability.
    """
    if src is None:src=forcing
    intervals=[(Q(0),Q(1))]
    R=Q(0)
    for i,d in enumerate(word):
        if i:
            R=16*R+src(i)
        assert 0<=d<16
        a=16**i
        pieces=[]
        for lo,hi in intervals:
            q_min=(a*lo+R).__floor__()-2
            q_max=(a*hi+R).__floor__()+2
            for q in range(q_min,q_max+1):
                l=(Q(q)+Q(d,16)-R)/a
                u=(Q(q)+Q(d+1,16)-R)/a
                L=max(lo,l);U=min(hi,u)
                if L<U:pieces.append((L,U))
        intervals=pieces
    return intervals

def word_probability(word,src=None):
    return sum((hi-lo for lo,hi in word_intervals(word,src)),Q())

def root_index(digits):
    return sum(d*16**j for j,d in enumerate(digits))

def prefix_index(digits):
    return sum(d*16**(len(digits)-1-j) for j,d in enumerate(digits))

def main():
    for A,d in ((173,5),(347,5),(691,6)):
        for k in (1,2):
            m=d-k;v=original_epoch(A,m,k)
            print('ORIGINAL',A,m,k,'selected',v['count'],'uniform-model expected',round(float(v['expected']),9),
                  'innovation',round(float(Q(v['count'])-v['expected'])/A,9),
                  'delta range',round(float(v['min_delta']),7),round(float(v['max_delta']),7))
    toy=nonlumpability(Q(1,2),Q(1,2))
    print('TOY direct',toy['direct'],'naive',toy['naive'],'TV',toy['total_variation'])
    for n,m in ((13,2),(29,2),(61,2)):
        a,b,z=source_nonlumpability(n,m)
        print('ORIGINAL SOURCE',n,m,'delta1',float(a),'delta2',float(b),'TV',float(z['total_variation']))
    for length in (1,2,3):
        import itertools
        count=0
        for word in itertools.product(range(16),repeat=length):
            p=word_probability(word)
            assert p==Q(1,16**length),(word,p)
            count+=1
        print('exact IID Haar-seed first digit words',length,count,'PASS')
    print('HISTORY_SHELL_PROBE_PASS')
if __name__=='__main__':main()
