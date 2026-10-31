"""Exact finite controls for the SUCC cylinder-collision construction.

No infinite normality claims come from these numerical probes.
"""
from collections import Counter
from fractions import Fraction
from math import gcd

def r(n):
    assert n>=1
    return Fraction(4,8*n-7)-Fraction(2,8*n-4)-Fraction(1,8*n-3)-Fraction(1,8*n-2)

def bbp_states(N):
    u=Fraction(0)
    for n in range(1,N+1):
        u=16*u+r(n)
        yield u

def certified_word(u,n,m,initial_R=8):
    """Return a certified base-16 word of length m for {16^(n-1)*pi}.
    Works by rational BBP prefix and a provable future-tail interval.
    """
    R=initial_R
    q=16**m
    while R<=128:
        partial=sum((r(n+j)/16**j for j in range(1,R+1)),Fraction(0))
        error=r(n+R+1)/ (15*16**R)
        lo=q*(u+partial)
        hi=q*(u+partial+error)
        if lo.numerator//lo.denominator==hi.numerator//hi.denominator:
            return (lo.numerator//lo.denominator)%q, R
        R*=2
    raise AssertionError('ambiguous cylinder after 128 exact tail terms')

def word_digits(w,m):
    return tuple((w//(16**j))%16 for j in range(m-1,-1,-1))

def collision_energy(words,m):
    N=len(words)
    c=Counter(words)
    return Fraction(16**m * sum(v*v for v in c.values()),N*N)

def fkm_debruijn(k,n):
    """k-ary cyclic de Bruijn word of order n, length k**n."""
    a=[0]*(k*n+1)
    sequence=[]
    def db(t,p):
        if t>n:
            if n%p==0:
                sequence.extend(a[1:p+1])
        else:
            a[t]=a[t-p]
            db(t+1,p)
            for j in range(a[t-p]+1,k):
                a[t]=j
                db(t+1,t)
    db(1,1)
    return sequence

def cyclic_words(sequence,m):
    N=len(sequence)
    return [sum(sequence[(j+k)%N]*16**(m-k-1) for k in range(m)) for j in range(N)]

def zero_words(m,N):
    return [0]*N

def bbp_word_census(N=256, mmax=3):
    out={}
    states=list(bbp_states(N))
    for m in range(1,mmax+1):
        observed=[certified_word(u,n,m) for n,u in enumerate(states,1)]
        words=[w for w,R in observed]
        out[m]={'Q':str(collision_energy(words,m)),
                'Q_decimal':float(collision_energy(words,m)),
                'distinct':len(set(words)),
                'min_R':min(R for w,R in observed),
                'max_R':max(R for w,R in observed)}
        if m>1:
            preceding=[certified_word(states[n-1],n,m-1)[0] for n in range(1,N+1)]
            assert all(words[j]//16==preceding[j] for j in range(N))
        if m>1 and N>1:
            shifted=[certified_word(states[n],n+1,m-1)[0] for n in range(1,N)]
            assert all(words[j]%16**(m-1)==shifted[j] for j in range(N-1))
    return out

if __name__=='__main__':
    cycle=fkm_debruijn(16,2)
    print('debruijn 16-ary order2 length',len(cycle))
    for m in range(1,5):
        print('m',m,'Q_cycle',collision_energy(cyclic_words(cycle,m),m),
              'Q_zero',collision_energy(zero_words(m,256),m))
    print('bbp',bbp_word_census(256,3))

def walsh_defect(words, m):
    """16-channel Walsh defect at child depth m+1, exact Fraction."""
    N=len(words)
    c=Counter(words)
    parents=set(w//16 for w in words)
    total=0
    for v in parents:
        for mask in range(1,16):
            signed=sum(((-1 if ((mask&a).bit_count()&1) else 1)*c.get(16*v+a,0)) for a in range(16))
            total+=signed*signed
    return Fraction(16**m*total,N*N)
