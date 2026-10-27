"""Source-authenticated exact 2-bit sheet/pole + value decoder at odd primes p>=7.

The canonical sheet bit is a finite-level convention. Original numerator
A and denominator D are unchanged. No claim about real-circle pi normality.
"""
from __future__ import annotations
from dataclasses import dataclass
from math import isqrt

def A(x: int) -> int:
    return 120*x*x-89*x+16

def D(x: int) -> int:
    return (2*x-1)*(4*x-1)*(8*x-7)*(8*x-3)

def modulus(p:int,L:int)->int:
    if (type(p) is not int or p<7 or
        any(p%d==0 for d in range(2,isqrt(p)+1)) or
        type(L) is not int or not 1<=L<=8):
        raise ValueError("prime p>=7 and 1<=L<=8 required")
    return p**L

def valuation(t:int,p:int):
    if t==0:raise ValueError("infinite valuation handled separately")
    s=0
    while t%p==0:
        t//=p;s+=1
    return s

def unit_root(v:int,p:int,k:int):
    """Canonical Hensel root; None for quadratic nonresidue."""
    r=next((r for r in range(1,(p+1)//2) if (r*r-v)%p==0),None)
    if r is None:return None
    for i in range(1,k):
        m=p**i
        r+=(-((r*r-v)//m)*pow(2*r,-1,p)%p)*m
    assert (r*r-v)%(p**k)==0
    return r

def shape(a:int,p:int,L:int):
    q=modulus(p,L)
    if type(a) is not int or not 0<=a<q:raise ValueError("target residue")
    b=89*pow(240,-1,q)%q
    c=-241*pow(480,-1,q)%q
    v=(a-c)*pow(120,-1,q)%q
    if not v:return ("critical",b,L//2,None,0)
    z=valuation(v,p)
    if z%2:return ("empty",b,0,None,0)
    s=z//2;k=L-2*s;r=unit_root(v//(p**(2*s)),p,k)
    if r is None:return ("empty",b,s,None,k)
    return ("two",b,s,r,k)

@dataclass(frozen=True)
class Code:
    target:int
    sheet:int
    pole:int
    lift:int

def decode(v:Code,p:int,L:int)->int:
    q=modulus(p,L)
    if (type(v) is not Code or
        type(v.sheet) is not int or v.sheet not in (0,1) or
        type(v.pole) is not int or v.pole not in (0,1)):
        raise ValueError("two valid bit fields required")
    kind,b,s,r,k=shape(v.target,p,L)
    if kind=="empty":raise ValueError("nonexistent square-root fiber")
    if type(v.lift) is not int or not 0<=v.lift<p**s:
        raise ValueError("invalid lifting index")
    if kind=="critical":
        if v.sheet:raise ValueError("no meaningful sign at critical fiber")
        u=p**((L+1)//2)*v.lift
    else:
        u=(p**s)*((1 if v.sheet==0 else -1)*r+v.lift*p**k)
    x=(b+u)%q
    if A(x)%q!=v.target or int(D(x)%p==0)!=v.pole:
        raise ValueError("source identity/pole bit mismatch")
    return x

def encode(x:int,p:int,L:int)->Code:
    q=modulus(p,L)
    if type(x) is not int or not 0<=x<q:raise ValueError("time residue")
    a=A(x)%q
    kind,b,s,r,k=shape(a,p,L)
    assert kind!="empty"
    u=(x-b)%q
    if kind=="critical":
        assert u%p**((L+1)//2)==0
        sheet=0;lift=u//p**((L+1)//2)
    else:
        assert u%p**s==0
        z=u//p**s
        if z%p**k==r:sheet=0
        elif z%p**k==(-r)%p**k:sheet=1
        else:raise ArithmeticError("invalid root sheet")
        sg=1 if sheet==0 else -1
        lift=((z-sg*r)//p**k)%p**s
    v=Code(a,sheet,int(D(x)%p==0),lift)
    assert decode(v,p,L)==x
    return v

def fiber(a:int,p:int,L:int):
    q=modulus(p,L)
    kind,b,s,r,k=shape(a,p,L)
    if kind=="empty":return ()
    out=[]
    for sign in ((0,) if kind=="critical" else (0,1)):
        for j in range(p**s):
            u=(p**((L+1)//2)*j if kind=="critical" else
               p**s*((1 if sign==0 else -1)*r+j*p**k))
            x=(b+u)%q
            out.append(Code(a,sign,int(D(x)%p==0),j))
    assert all(encode(decode(t,p,L),p,L)==t for t in out)
    return tuple(out)

def successor(s:Code,p:int,L:int):
    q=modulus(p,L)
    return encode((decode(s,p,L)+1)%q,p,L)

def pair_count(p:int,L:int):
    modulus(p,L)
    return p**L+L*(p-1)*p**(L-1)

def finite_difference_histogram(p:int):
    modulus(p,1)
    return tuple(sum((A(x)-A(y))%p==a for x in range(p)
                     for y in range(p)) for a in range(p))

if __name__=="__main__":
    for p,L in ((7,1),(7,2),(7,3),(11,2),(241,1)):
        q=p**L
        assert len({encode(x,p,L) for x in range(q)})==q
        assert sum(len(fiber(a,p,L))**2 for a in range(q))==pair_count(p,L)
        print(p,L,q,pair_count(p,L))
    print("Source two-bit plus value exact probe PASS; pi normality OPEN")
