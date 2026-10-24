"""Exact second-level filtered BBP p^2-source echo and Fermat quotient shear.

Only terms whose BBP forcing denominators are divisible by p^2 are used
in the filtered lift. The full BBP source includes lower p-level forcing.
"""
from __future__ import annotations
from fractions import Fraction as Q
from observational_succ.bbp_source_memory import forcing
from observational_succ.bbp_cyclotomic_birth import _prime, first_witt_holonomy


def integral_reduction(q: Q, p: int, depth: int = 2) -> int:
    """A p-integral rational modulo p^depth, with strict typing."""
    _prime(p)
    if type(depth) is not int or depth < 1:
        raise ValueError("positive p-adic depth required")
    q=Q(q)
    if q.denominator%p == 0:
        raise ValueError("rational is not p-integral")
    modulus=p**depth
    return q.numerator*pow(q.denominator,-1,modulus)%modulus


def source_square_bursts(p: int, k: int) -> tuple[int,int,int,int]:
    """The p^2-divisible four-pole times at inner source step k."""
    _prime(p)
    if p%8 != 1: raise ValueError("p==1 mod 8 required")
    m=(p-1)//8
    if type(k) is not int or not 1<=k<=m:
        raise ValueError("1<=k<=(p-1)/8 required to exclude p^3 poles")
    M=(p*p-1)//8
    return tuple((8*k-a)*M+k for a in (7,4,3,2))


def quotient_relation(p: int) -> tuple[int,int,int]:
    """(q, Fermat Q_2, q_lift), with Q_2=2q and q_lift=q modulo p."""
    _prime(p)
    if p%8 != 1:raise ValueError("p==1 mod 8 required")
    m=(p-1)//8
    M=(p*p-1)//8
    q=first_witt_holonomy(p)
    q2=((pow(2,p-1,p*p)-1)//p)%p
    qlift=((pow(16,M,p*p)-1)//p)%p
    if q2 != 2*q%p or qlift != q:
        raise AssertionError("Fermat quotient return relation invalid")
    return q,q2,qlift


def lift_source_shear(k: int) -> Q:
    """Signed BBP pulse transport: coefficients 5,2,1,0 along event gaps."""
    if type(k) is not int or k<1:raise ValueError("k>=1 required")
    return Q(20,8*k-7)-Q(4,8*k-4)-Q(1,8*k-3)


def direct_filtered_p2_endpoints(p: int, steps: int) -> tuple[int,...]:
    """Exact modular replay of p^2 source events; omits lower-p forcing."""
    _prime(p)
    if p%8 != 1:raise ValueError("p==1 mod 8 required")
    if type(steps) is not int or not 0<=steps<=(p-1)//8:
        raise ValueError("0<=steps<=(p-1)/8")
    mod=p*p
    state=0
    prev=0
    ret=[]
    for k in range(1,steps+1):
        for n,a,coefficient in zip(source_square_bursts(p,k),(7,4,3,2),(4,-2,-1,-1)):
            state=(pow(16,n-prev,mod)*state+integral_reduction(Q(coefficient,8*k-a),p,2))%mod
            prev=n
        ret.append(state)
    return tuple(ret)


def twisted_filtered_p2_endpoints(p: int, steps: int) -> tuple[int,...]:
    """Proved twisted affine recurrence for the same FILTERED p^2-source."""
    _prime(p)
    if p%8 != 1:raise ValueError("p==1 mod 8 required")
    if type(steps) is not int or not 0<=steps<=(p-1)//8:
        raise ValueError("0<=steps<=(p-1)/8")
    mod=p*p
    q=first_witt_holonomy(p)
    c=0
    out=[]
    for k in range(1,steps+1):
        c=(16*(1+8*p*q)*c+integral_reduction(forcing(k),p,2)
           +p*q*integral_reduction(lift_source_shear(k),p,1))%mod
        out.append(c)
    return tuple(out)
