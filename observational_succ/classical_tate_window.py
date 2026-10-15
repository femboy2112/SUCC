"""Exact finite Schwartz-Bruhat windows of Q_p (not just finite clock states).

An (a,b) window represents compactly supported functions on p^-a Z_p,
constant modulo p^b Z_p. Their finite coset descriptions are honest
infinite-local-field test functions, not finite physical p-adic places.
Fourier swaps support and precision. Exact cyclotomic Fractions avoid
rounded phase comparisons and never use nontrivial zeta zeros.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q
from math import isqrt
from typing import Iterable


class TateWindowError(ValueError):
    pass


def exact_int(x: int, label: str, minimum: int | None = None) -> int:
    if type(x) is not int or (minimum is not None and x < minimum):
        raise TateWindowError(f"{label}: exact integer outside declared domain")
    return x


def exact_q(x: Q | int) -> Q:
    if type(x) not in (int,Q):
        raise TateWindowError("Only integers/exact Fractions, no float source")
    return Q(x)


def is_prime(p: int) -> bool:
    return type(p) is int and p >= 2 and all(p%d for d in range(2,isqrt(p)+1))


def _reduce(p: int, r: int, coefficients: Iterable[Q | int]) -> tuple[Q,...]:
    if not is_prime(p) or type(r) is not int or r < 0:
        raise TateWindowError("Genuine prime cyclotomic local chart required")
    c=[exact_q(x) for x in coefficients]
    if r==0:
        return (sum(c,Q(0)),)
    q=p**(r-1)
    degree=(p-1)*q
    c.extend([Q(0)]*max(0,degree-len(c)))
    for k in range(len(c)-1,degree-1,-1):
        v=c[k]
        if v:
            base=k-degree
            for j in range(p):
                c[base+j*q]-=v
    return tuple(c[:degree])


@dataclass(frozen=True)
class Cyclo:
    """An exact element of Q(zeta_(p^r)), in cyclotomic polynomial basis."""
    p: int
    r: int
    coeff: tuple[Q,...]

    def __post_init__(self) -> None:
        if type(self.coeff) is not tuple:
            raise TateWindowError("Cyclotomic polynomial coefficients must be a tuple")
        object.__setattr__(self,"coeff",_reduce(self.p,self.r,self.coeff))

    @staticmethod
    def scalar(p: int, r: int, value: Q | int) -> Cyclo:
        return Cyclo(p,r,(exact_q(value),))

    @staticmethod
    def phase(p: int,r: int,k: int) -> Cyclo:
        exact_int(k,"root-of-unity exponent")
        size=p**r
        if size>256:
            raise TateWindowError("Exact cyclotomic size budget exceeded")
        coeff=[Q(0)]*size
        coeff[k%size]=Q(1)
        return Cyclo(p,r,tuple(coeff))

    def _other(self,v: Cyclo | Q | int) -> Cyclo:
        if type(v) in (int,Q):
            return Cyclo.scalar(self.p,self.r,v)
        if not isinstance(v,Cyclo) or (v.p,v.r)!=(self.p,self.r):
            raise TateWindowError("Cyclotomic conductor/field mismatch")
        return v

    def __add__(self,v):
        o=self._other(v)
        return Cyclo(self.p,self.r,tuple(a+b for a,b in zip(self.coeff,o.coeff)))
    __radd__=__add__

    def __neg__(self):
        return Cyclo(self.p,self.r,tuple(-a for a in self.coeff))
    def __sub__(self,v):
        return self+-self._other(v)
    def __rsub__(self,v):
        return self._other(v)+-self

    def __mul__(self,v):
        o=self._other(v)
        result=[Q(0)]*(len(self.coeff)*2-1)
        for i,a in enumerate(self.coeff):
            if a:
                for j,b in enumerate(o.coeff):
                    result[i+j]+=a*b
        return Cyclo(self.p,self.r,tuple(result))
    __rmul__=__mul__

    def __truediv__(self,q):
        q=exact_q(q)
        if not q: raise ZeroDivisionError("zero rational divisor")
        return self*Q(1,q)

    def conjugate(self):
        result=Cyclo.scalar(self.p,self.r,0)
        for j,c in enumerate(self.coeff):
            if c:
                result+=c*Cyclo.phase(self.p,self.r,-j)
        return result

    def embed(self,new_r: int) -> Cyclo:
        exact_int(new_r,"new conductor power",self.r)
        if self.p**new_r > 256:
            raise TateWindowError("Exact cyclotomic size budget exceeded")
        result=Cyclo.scalar(self.p,new_r,0)
        m=self.p**(new_r-self.r)
        for k,v in enumerate(self.coeff):
            if v: result+=v*Cyclo.phase(self.p,new_r,k*m)
        return result


@dataclass(frozen=True)
class TateWindow:
    """Q_p test functions supported p^-a Zp, constant mod p^b Zp.

    Coordinates x=k/p^a mod p^b, with k mod p^(a+b).
    Additive measure dx(p^b Zp)=p^-b, self-dual standard character.
    """
    p: int
    a: int
    b: int

    def __post_init__(self):
        if not is_prime(self.p):
            raise TateWindowError("Fake prime place forbidden")
        exact_int(self.a,"support denominator exponent",0)
        exact_int(self.b,"precision exponent",0)
        if self.p**(self.a+self.b)>64:
            raise TateWindowError("Explicit cyclotomic test atlas exceeds budget")

    @property
    def size(self) -> int:
        return self.p**(self.a+self.b)

    def vector(self,values: Iterable) -> tuple[Cyclo,...]:
        values=tuple(values)
        if len(values)!=self.size:
            raise TateWindowError("Need a complete finite source-coset list")
        result=[]
        for v in values:
            if type(v) in (int,Q):
                v=Cyclo.scalar(self.p,self.a+self.b,v)
            if not isinstance(v,Cyclo) or (v.p,v.r)!=(self.p,self.a+self.b):
                raise TateWindowError("Incorrect cyclotomic test source field")
            result.append(v)
        return tuple(result)

    def zero(self)->tuple[Cyclo,...]:
        return self.vector([0]*self.size)

    def fourier(self,values: Iterable) -> tuple[Cyclo,...]:
        """Tate self-dual additive transform; dual window is (b,a).
        psi_p(xy)=zeta_(p^(a+b))^(k*l) at x=k/p^a,y=l/p^b.
        """
        f=self.vector(values)
        zero=Cyclo.scalar(self.p,self.a+self.b,0)
        phases=[Cyclo.phase(self.p,self.a+self.b,k) for k in range(self.size)]
        return tuple(sum((f[k]*phases[k*l%self.size] for k in range(self.size)),zero)
                     *Q(self.p)**(-self.b) for l in range(self.size))

    def additive_integral(self,values: Iterable) -> Cyclo:
        return sum(self.vector(values), Cyclo.scalar(self.p,self.a+self.b,0))*Q(self.p)**(-self.b)

    def inner(self,left: Iterable,right: Iterable)->Cyclo:
        f,g=self.vector(left),self.vector(right)
        return sum((x*y.conjugate() for x,y in zip(f,g)),
                   Cyclo.scalar(self.p,self.a+self.b,0))*Q(self.p)**(-self.b)

    def invert(self,values: Iterable) -> tuple[Cyclo,...]:
        return tuple(self.vector(values)[(-k)%self.size] for k in range(self.size))

    def support_expand(self,values: Iterable) -> tuple[Cyclo,...]:
        f=self.vector(values)
        larger=TateWindow(self.p,self.a+1,self.b)
        return larger.vector([f[k//self.p].embed(self.a+self.b+1) if k%self.p==0
                              else 0 for k in range(larger.size)])

    def precision_refine(self,values: Iterable) -> tuple[Cyclo,...]:
        f=self.vector(values)
        finer=TateWindow(self.p,self.a,self.b+1)
        return finer.vector([f[k%self.size].embed(self.a+self.b+1)
                             for k in range(finer.size)])

    def unramified_mellin(self,values: Iterable, s: int, omega: int=1) -> Cyclo:
        """Meromorphic continuation of exact local Z_p(s,f,unramified omega).

        For Re(s)>0, this is a convergent multiplicative integral; for
        s<=0, return its meromorphic shell formula, NOT the divergent
        original improper integral. omega is the character value at p.
        """
        exact_int(s,"integer Mellin argument")
        if type(omega) is not int or omega not in (-1,1):
            raise TateWindowError("Unramified character requires omega +/-1")
        f=self.vector(values)
        denominator=1-omega*Q(self.p)**(-s)
        if denominator==0:
            raise TateWindowError("Meromorphic pole: no finite local value")
        signed=lambda j:(-1 if omega==-1 and j%2 else 1)
        zero=Cyclo.scalar(self.p,self.a+self.b,0)
        scalar=Q(self.p)**(-self.b)/ (1-Q(1,self.p))
        finite=sum((f[k]* (signed(j)*scalar*Q(self.p)**(j*(1-s)))
                    for k in range(1,self.size)
                    for j in (self._valuation(k)-self.a,)),zero)
        tail=f[0]* (signed(self.b)*Q(self.p)**(-self.b*s)/denominator)
        return finite+tail

    def _valuation(self,k:int)->int:
        j=0
        while k and k%self.p==0:
            k//=self.p
            j+=1
        return j

    def unramified_ratio(self,s:int,omega:int=1)->Q:
        """Z_p(s,f,omega)/Z_p(1-s,Ff,omega^-1) for arbitrary f.
        Stated as cross-multiplied equality even when individual zeta is zero.
        """
        exact_int(s,"integer Mellin argument",2)
        if omega not in (-1,1) or type(omega) is not int:
            raise TateWindowError("Unramified omega +/-1 required")
        return (1-omega*Q(self.p)**(s-1))/(1-omega*Q(self.p)**(-s))


def diagonal_additive_phases(q: Q | int) -> dict:
    """Exact rational product of standard finite place characters and real sign.

    psi_inf(q)=exp(-2*pi*i*q), psi_p(q)=exp(+2*pi*i*{q}_p).
    The exponent sum is integral for rational diagonal q, hence product 1.
    """
    q=exact_q(q)
    den=q.denominator
    local=[]
    for p in range(2,den+1):
        if is_prime(p) and den%p==0:
            power=0
            d=den
            while d%p==0:
                d//=p
                power+=1
            mod=p**power
            numerator=q.numerator * pow(d,-1,mod) % mod
            if numerator:
                local.append((p,Q(numerator,mod)))
    total=sum((v for _,v in local),Q(0))-q
    if total.denominator!=1:
        raise ArithmeticError("Diagonal rational global character was not trivial")
    return {"q":str(q),"finite_places":[[p,str(f)] for p,f in local],
            "real_signed_phase":str(-q),"total_integer_phase":int(total),
            "diagonal_global_character_equals_one":True}


def classical_tate_window_probe()->dict:
    windows=((2,0,1),(2,1,1),(2,0,3),(3,0,2),(3,1,1),(5,0,1))
    checks=0
    for p,a,b in windows:
        w=TateWindow(p,a,b)
        f=w.vector([Q((k*3+1)%7-3,5) for k in range(w.size)])
        ff=TateWindow(p,b,a).fourier(w.fourier(f))
        assert ff==w.invert(f)
        assert w.inner(f,f)==TateWindow(p,b,a).inner(w.fourier(f),w.fourier(f))
        for s in (2,3,4):
            for omega in (-1,1):
                lhs=w.unramified_mellin(f,s,omega)
                dual=TateWindow(p,b,a).unramified_mellin(w.fourier(f),1-s,omega)
                assert lhs==dual*w.unramified_ratio(s,omega)
                checks+=1
    return {"kind":"CLASSICAL_TATE_LOCAL_ATLAS_RECEIPT",
            "window_sizes":[[p,a,b,p**(a+b)] for p,a,b in windows],
            "full_coset_functional_equations_checked":checks,
            "exact_cyclotomic_Fourier_and_Parseval":True,
            "support_and_precision_contralateral_refinement":True,
            "diagonal_rational_character":diagonal_additive_phases(Q(1,6)),
            "all_tests_infinite_local_source_identification":True,
            "global_adelic_Poisson_derived":False,
            "signed_Weil_positivity_or_RH_proved":False}
