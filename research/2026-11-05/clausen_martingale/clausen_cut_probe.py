"""Reproducible original-source zero-cylinder Clausen pressure calculation."""
from fractions import Fraction as F
from functools import lru_cache
from math import log
import mpmath as mp
mp.mp.dps=48
TAPS=(F(4),F(0),F(0),F(-2),F(-1),F(-1),F(0),F(0))
def forcing(n):
    a=sum((w/F(8*(n-1)+j) for j,w in enumerate(TAPS,1)),F())
    b=F(120*n*n-89*n+16,(2*n-1)*(4*n-1)*(8*n-7)*(8*n-3))
    assert a==b
    return a
def states(maxn):
    x=F();out={}
    for n in range(1,maxn+1):
        x=16*x+forcing(n);out[n]=x
    return out
def asmp(q): return mp.mpf(q.numerator)/q.denominator
@lru_cache(None)
def primitive(q):
    f=q%1
    if f==0: return mp.mpf(0)
    return -mp.im(mp.polylog(2,mp.e**(2j*mp.pi*asmp(f))))/mp.pi

def pairmean(i,j,K,u):
    Q=F(16**j-16**i,16**K)
    alpha=(u[j]-u[i])%1
    if Q.denominator==1:return mp.mpf(0)
    if i<K<=j:
        delta=F(1,16**(K-i))
        return (primitive(alpha-delta)-primitive(alpha))/asmp(Q)
    return (primitive(alpha+Q)-primitive(alpha))/asmp(Q)

def pressure(A,K,u):
    parts={'future':mp.mpf(0),'cross':mp.mpf(0),'past':mp.mpf(0)}
    for i in range(A,2*A):
        for j in range(i+1,2*A):
            v=pairmean(i,j,K,u)
            part='future' if i>=K else 'cross' if j>=K else 'past'
            parts[part]+=v/A**2
    return parts

def cross_constant():
    return mp.mpf(512)/225*(mp.mpf(1)/15+mp.mpf(16)/225*mp.log(16))

def past_bound(A,t):
    return (t*(t-1)*(1+mp.log(mp.mpf(16)/15))+
        mp.log(16)/3*t*(t-1)*(t+1))/A**2

def verify():
    C=cross_constant()
    for A in (7,11,13):
        u=states(2*A-1)
        for K in sorted(set((A,A+1,A+2,3*A//2,2*A,2*A+3))):
            d=pressure(A,K,u)
            assert abs(d['future'])<mp.mpf('1e-35')
            assert abs(d['cross'])<=C/A**2+mp.mpf('1e-34')
            if K<=2*A:
                assert abs(d['past'])<=past_bound(A,K-A)+mp.mpf('1e-34')
            if K<=A: assert abs(sum(d.values()))<mp.mpf('1e-40')
            print('BBP',A,K,'full',float(sum(d.values())),
                  'cross',float(d['cross']),'past',float(d['past']))
    for A,t in ((64,8),(125,20),(216,36)):
        u={n:F(0) for n in range(A,2*A)}
        d=pressure(A,A+t,u)
        total=float(sum(d.values()))
        leading=-(log(16)/3)*t*(t-1)*(t+1)/A**2
        assert total<0 and abs(d['cross'])<=C/A**2
        print('ZERO-FORCING',A,t,'mean',total,'onset',leading,
              'ratio',total/leading)
    print('CLAUSEN_CUT_PREREGISTERED_HOLDS_PASS')

if __name__=='__main__':
    verify()
