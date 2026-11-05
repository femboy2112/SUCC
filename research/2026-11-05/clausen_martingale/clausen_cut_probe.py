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
