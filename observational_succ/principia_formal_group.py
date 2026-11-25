"""Exact FUCC prime-square resolvent to height-two formal logarithm.

Finite rational coefficients are a model of a genuine local RH-proof ingredient;
these are NOT CM-theta integrality certificates or a new RH proof.
"""
from __future__ import annotations
from fractions import Fraction
from math import factorial, isqrt
from typing import Sequence

class InvalidFormalSource(ValueError):
    pass


def is_prime(p:int)->bool:
    return p>=2 and all(p%k for k in range(2,isqrt(p)+1))


def log_coefficients(p:int, degree:int)->tuple[Fraction,...]:
    if not is_prime(p) or degree<1:
        raise InvalidFormalSource('expected genuine prime and positive truncation')
    c=[Fraction(0)]*(degree+1); c[1]=Fraction(1)
    j=1
    while p**(2*j)<=degree:
        c[p**(2*j)]=Fraction(1,p**j)
        j+=1
    return tuple(c)


def multiply_truncated(a:Sequence[Fraction],b:Sequence[Fraction],degree:int)->tuple[Fraction,...]:
    out=[Fraction(0)]*(degree+1)
    for i,x in enumerate(a[:degree+1]):
        if not x:continue
        for j,y in enumerate(b[:degree-i+1]):
            if y: out[i+j]+=x*y
    return tuple(out)


def power_truncated(a:Sequence[Fraction],exponent:int,degree:int)->tuple[Fraction,...]:
    if exponent<0 or degree<0:raise InvalidFormalSource('invalid exponent or degree')
    one=(Fraction(1),)+tuple(Fraction(0) for _ in range(degree))
    base=tuple(a[:degree+1])
    if len(base)<degree+1:base+=tuple(Fraction(0) for _ in range(degree+1-len(base)))
    out=one
    while exponent:
        if exponent&1:out=multiply_truncated(out,base,degree)
        base=multiply_truncated(base,base,degree)
        exponent//=2
    return out


def inverse_formal_log(p:int,degree:int)->tuple[Fraction,...]:
    if not is_prime(p) or degree<1:raise InvalidFormalSource('invalid height-two source')
    u=[Fraction(0)]*(degree+1);u[1]=Fraction(1)
    for n in range(2,degree+1):
        residue=Fraction(0);j=1
        while p**(2*j)<=n:
            r=p**(2*j)
            residue+=Fraction(1,p**j)*power_truncated(u,r,n)[n]
            j+=1
        u[n]=-residue
    return tuple(u)


def compose_truncated(f:Sequence[Fraction],u:Sequence[Fraction],degree:int)->tuple[Fraction,...]:
    out=[Fraction(0)]*(degree+1)
    for r,a in enumerate(f[:degree+1]):
        if not a:continue
        ur=power_truncated(u,r,degree)
        for k,v in enumerate(ur):out[k]+=a*v
    return tuple(out)


def valuation(q:Fraction,p:int)->int|None:
    if not is_prime(p):raise InvalidFormalSource('p must be prime')
    q=Fraction(q)
    if not q:return None  # infinite valuation for the zero coefficient
    a=abs(q.numerator);b=q.denominator;v=0
    while a%p==0:a//=p;v+=1
    while b%p==0:b//=p;v-=1
    return v


def factorial_valuation(n:int,p:int)->int:
    if n<0 or not is_prime(p):raise InvalidFormalSource('invalid factorial p valuation')
    v=0
    while n:
        n//=p;v+=n
    return v


def verify_height_two(p:int,degree:int,f:Sequence[Fraction])->dict[str,int]:
    """Check formal inverse and local jet valuation bounds by exact fractions."""
    if not is_prime(p) or degree<1:raise InvalidFormalSource('invalid p/depth')
    f=tuple(Fraction(a) for a in f)
    if any((v is not None and v<0) for v in (valuation(a,p) for a in f)):
        raise InvalidFormalSource('test kernel not p-integral')
    ell=log_coefficients(p,degree)
    u=inverse_formal_log(p,degree)
    composed=compose_truncated(ell,u,degree)
    if composed!=(Fraction(0),Fraction(1))+tuple(Fraction(0) for _ in range(degree-1)):
        raise InvalidFormalSource('inverse identity failed')
    img=compose_truncated(f,u,degree)
    nonzero=0
    for a in range(1,degree+1):
        coeff_val=valuation(u[a],p)
        bound=Fraction(-(a-1),p*p-1)
        if coeff_val is not None and coeff_val<bound:
            raise InvalidFormalSource('height-two inverse valuation failed')
        v=valuation(img[a]*factorial(a),p)
        if v is not None:
            nonzero+=1
            if v < Fraction(factorial_valuation(a,p)) + bound:
                raise InvalidFormalSource('integral test-kernel derivative valuation failed')
    # Resolvent (I - p^-1 V_(p²))^-1 e1, under e_n -> T^n.
    if ell[1]!=1 or any(ell[a] for a in range(2,degree+1)
                            if a not in [p**(2*j) for j in range(1,degree+1) if p**(2*j)<=degree]):
        raise InvalidFormalSource('wrong FUCC-resolvent source support')
    # l(T) - p^-1 l(T^(p²)) = T, coefficientwise.
    for a in range(1,degree+1):
        earlier=ell[a//(p*p)] if a%(p*p)==0 else 0
        if ell[a]-Fraction(earlier,p)!=(1 if a==1 else 0):
            raise InvalidFormalSource('FUCC resolvent recurrence mismatch')
    return {'prime':p,'degree':degree,'nonzero_composed_derivatives':nonzero,
            'inverse_support':sum(a!=0 for a in u)}
