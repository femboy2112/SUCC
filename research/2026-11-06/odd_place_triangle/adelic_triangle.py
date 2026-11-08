"""Exact authentic BBP odd-place / source-carrier probes.

Mathematical statements remain in THEOREMS.md. No pi-normality claim.
Fraction arithmetic is authoritative; complex statistics are diagnostics only.
"""
from __future__ import annotations

from fractions import Fraction
from math import cos, sin, pi, sqrt
from functools import lru_cache

WEIGHTS=(4,-2,-1,-1)
POLES=(7,4,3,2)


def source(n: int) -> Fraction:
    if type(n) is not int or n<1:raise ValueError('integer n>=1 required')
    return sum((Fraction(w,8*n-a) for w,a in zip(WEIGHTS,POLES)),Fraction(0))


def denominator(n:int) -> int:
    return (2*n-1)*(4*n-1)*(8*n-7)*(8*n-3)


def numerator(n:int) -> int:
    return 120*n*n-89*n+16


@lru_cache(None)
def state(n:int)->Fraction:
    if type(n) is not int or n<0:raise ValueError('integer n>=0 required')
    if n==0:return Fraction(0)
    return 16*state(n-1)+source(n)


def factorization(q:int)->dict[int,int]:
    """Exact trial division, intended for smooth finite denominators in tests."""
    q=abs(int(q));fac={};p=2
    while p*p<=q:
        if q%p==0:
            k=0
            while q%p==0:q//=p;k+=1
            fac[p]=k
        p=3 if p==2 else p+2
    if q>1:fac[q]=fac.get(q,0)+1
    return fac


def principal_part(x:Fraction|int,p:int)->Fraction:
    """Canonical local principal part in Q/Z of a rational at prime p."""
    x=Fraction(x)
    d=x.denominator;power=1
    while d%p==0:
        d//=p;power*=p
    if power==1:return Fraction(0)
    return Fraction((x.numerator*pow(d,-1,power))%power,power)


def global_odd_fraction(x:Fraction|int)->Fraction:
    x=Fraction(x)
    if x.denominator%2==0:raise ValueError('odd reduced denominator required')
    return sum((principal_part(x,p) for p in factorization(x.denominator)), Fraction(0))%1


def source_prime_support(n:int)->set[int]:
    """Prime divisors possible from source denominators through n, all odd."""
    ps=set()
    for j in range(1,n+1):ps.update(factorization(denominator(j)))
    return ps


def is_prime(p:int)->bool:
    if p<2:return False
    for d in range(2,int(p**.5)+1):
        if p%d==0:return False
    return True


def prime_birth(p:int)->tuple[int,int,int]:
    """(first index, next index, first pole residue c mod p), p>5 prime.

    first and next at p | D(n); c is p*r(n0) in F_p.
    """
    if p<=5 or not is_prime(p):raise ValueError('prime p>5 required')
    first=[]
    for n in range(1,p+1):
        if denominator(n)%p==0:first.append(n)
        if len(first)==2:break
    n0,n1=first
    # Exactly v_p(r(n0))=-1, so p*r(n0) has p-integral residue.
    x=p*source(n0)
    if x.denominator%p==0:raise AssertionError('multiple pole/p^2 at first birth')
    c=(x.numerator*pow(x.denominator,-1,p))%p
    if c==0:raise AssertionError('pole canceled')
    return n0,n1,c


def predicted_prime_birth(p:int)->tuple[int,int]:
    """First-index and source pole coefficient prediction from p mod 8."""
    if p<=5 or not is_prime(p):raise ValueError('prime p>5 required')
    if p%8==1:return (p+7)//8,4%p
    if p%8==5:return (p+3)//8,(-1)%p
    return (p+1)//4,(-pow(2,-1,p))%p


def multiplicative_order(b:int,p:int)->int:
    if b%p==0:raise ValueError('coprime required')
    r=1
    for m in range(1,p):
        r=r*b%p
        if r==1:return m
    raise AssertionError('finite-field order missing')


def birth_plateau(p:int)->tuple[int,int,int,int,list[int]]:
    n0,n1,c=prime_birth(p)
    m=multiplicative_order(16,p)
    residues=[]
    for t in range(n1-n0):
        u=state(n0+t)
        pp=principal_part(u,p)
        if pp.denominator!=p:raise AssertionError('valuation not exactly -1')
        residues.append(pp.numerator)
        if residues[-1]!=(c*pow(16,t,p))%p:
            raise AssertionError(f'failed source local phase transport: p={p},t={t}')
    return n0,n1,c,m,residues


def complex_character(x:Fraction|int)->complex:
    y=Fraction(x)%1
    z=float(y)
    return complex(cos(2*pi*z),sin(2*pi*z))


def local_cycle_probe(p:int)->dict:
    n0,n1,c,m,res=birth_plateau(p)
    if m>n1-n0:raise ValueError('no full clean cycle before next pole')
    local=sum(complex_character(Fraction(a,p)) for a in res[:m])/m
    real=sum(complex_character(state(n0+t)) for t in range(m))/m
    return {'prime':p,'start':n0,'next_pole':n1,'clean_length':n1-n0,'order':m,
            'local_abs':abs(local),'real_abs':abs(real),
            'gauss_bound':sqrt(p)/m,'first_residues':res[:8]}


def hostile_compensation(p:int,q:int)->dict:
    """Second odd prime can hide an entire p-local canceling cycle."""
    if p==q or not is_prime(p) or not is_prime(q):raise ValueError('distinct primes')
    n0,n1,c,m,res=birth_plateau(p)
    if m>n1-n0:raise ValueError('no full clean period')
    local=[];real=[]
    for a in res[:m]:
        # exact nearest integer to -q*a/p (round-half ties arbitrary)
        # use the exact nearest integer to q*a/p then negate
        b=-((2*q*a+p)//(2*p))
        x=Fraction(a,p)+Fraction(b,q)
        if abs(x)>Fraction(1,2*q):raise AssertionError('bad rounding')
        if principal_part(x,p)!=Fraction(a,p):raise AssertionError('p character changed')
        local.append(complex_character(Fraction(a,p)))
        real.append(complex_character(x))
    return {'p':p,'q':q,'order':m,'local_abs':abs(sum(local)/m),
            'adversarial_real_abs':abs(sum(real)/m),
            'proved_real_lower':1-pi/q}


def edge_pair_map(h:int,g:int,p:int)->tuple[int,int,int]:
    """FORMAL co-dual edge-sum model; not an embedding of phi or gamma."""
    return (h+g,h+p,g+p)


def edge_inverse(e1:int,e2:int,e3:int)->tuple[Fraction,Fraction,Fraction]:
    return (Fraction(e1+e2-e3,2),Fraction(e1+e3-e2,2),
            Fraction(e2+e3-e1,2))


def prime_phase_covariance(p:int)->dict:
    """Split real phase into local p and the exact other-prime twist.

    Complex floating outputs are exploratory diagnostics only.
    """
    n0,n1,c,m,res=birth_plateau(p)
    if m>n1-n0:raise ValueError('incomplete period')
    aa=[complex_character(Fraction(x,p)) for x in res[:m]]
    bb=[complex_character(state(n0+t)-Fraction(res[t],p)) for t in range(m)]
    ma=sum(aa)/m;mb=sum(bb)/m;global_mean=sum(a*b for a,b in zip(aa,bb))/m
    cov=global_mean-ma*mb
    return {'p':p,'order':m,'local_mean_abs':abs(ma),
            'complement_mean_abs':abs(mb),'covariance_abs':abs(cov),
            'global_mean_abs':abs(global_mean),
            'certifiable_bound':sqrt(p)/m+abs(cov),
            'interference_real':(ma*mb).real,'covariance_real':cov.real}
