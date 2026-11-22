"""Exact finite FUCC/Riesz and height-two formal-logarithm model.

This proves NO Riemann-hypothesis estimate. Original FUCC prime isometries
are represented by their finite coefficient labels; no fake scalar prime inputs.
"""
from __future__ import annotations
from collections import defaultdict
from fractions import Fraction
from math import comb, factorial


def factorize(n:int)->dict[int,int]:
    if n<1: raise ValueError('n>=1 required')
    out={}
    d=2
    while d*d<=n:
        while n%d==0:
            out[d]=out.get(d,0)+1
            n//=d
        d+=1
    if n>1: out[n]=out.get(n,0)+1
    return out


def fucc_euler_log_coefficients(X:int)->dict[int,Fraction]:
    """For L_X=sum_{p^k<=X} V_{p^k}/k: matrix coefficient at |1>."""
    if X<1: raise ValueError('X positive')
    result={}
    for n in range(2,X+1):
        d=factorize(n)
        if len(d)==1:
            (p,k),=d.items()
            result[n]=Fraction(1,k)
    return result


def fucc_log_commutator_coefficients(X:int)->dict[int,int]:
    """Return n -> p, encoding the coefficient log(p) of V_n.

    No numeric evaluation of transcendental log(p) is performed.
    """
    coeff=fucc_euler_log_coefficients(X)
    out={}
    for n,one_over_k in coeff.items():
        p,k=next(iter(factorize(n).items()))
        assert one_over_k*k==1
        out[n]=p
    return out


def riesz_log_prime_coeffs(X:int)->dict[int,Fraction]:
    """Exact coefficients of log p in S(X)=sum Lambda(n)(X/n-1)."""
    if X<1:raise ValueError('X positive')
    out=defaultdict(Fraction)
    for n,p in fucc_log_commutator_coefficients(X).items():
        out[p]+=Fraction(X,n)-1
    return dict(out)



def fucc_mahler_resolvent_coefficients(p:int,terms:int)->dict[int,Fraction]:
    """Exact coefficients of (I-p^-1 V_(p^2))^-1|1>, truncated by term count.

    Nonzero coefficient at basis |p^(2j)> is p^-j. These are the
    coefficients of l_p(T)=T+sum T^(p^(2j))/p^j, not the original
    critical sqrt(log p)*p^(-k/4) FUCC tower weighting.
    """
    if p<2 or terms<1:raise ValueError('p>=2 and positive term count')
    return {p**(2*j):Fraction(1,p**j) for j in range(terms)}


def fucc_mahler_resolvent_norm_sq(p:int)->Fraction:
    """Exact Hilbert norm squared of the full resolvent vector."""
    if p<2:raise ValueError('p>=2')
    return Fraction(p*p,p*p-1)


def fucc_mahler_residual_coefficients(p:int,terms:int)->dict[int,Fraction]:
    """l_p(T) - p^-1*l_p(T^(p^2)) truncated through p^(2*(terms-1))."""
    base=fucc_mahler_resolvent_coefficients(p,terms)
    cut=p**(2*(terms-1))
    out=dict(base)
    for n,c in base.items():
        if n*p*p<=cut:out[n*p*p]=out.get(n*p*p,Fraction())-c/p
    return {n:c for n,c in out.items() if c}

def poly_mul(a:list[Fraction],b:list[Fraction],N:int)->list[Fraction]:
    out=[Fraction(0) for _ in range(N+1)]
    for i,x in enumerate(a[:N+1]):
        if not x:continue
        for j,y in enumerate(b[:N+1-i]):
            if y:out[i+j]+=x*y
    return out


def poly_pow(a:list[Fraction],e:int,N:int)->list[Fraction]:
    out=[Fraction(1)]+[Fraction(0)]*N
    while e:
        if e&1:out=poly_mul(out,a,N)
        e//=2
        if e:a=poly_mul(a,a,N)
    return out


def inverse_height_two_log(p:int,N:int)->list[Fraction]:
    """Inverse U to l(T)=T+sum T^(p^(2j))/p^j through degree N.

    Uses the z-adically contracting fixed-point equation U=z-sum U^r/p^j.
    """
    if p<2 or N<1:raise ValueError('p>=2,N>=1')
    v=[Fraction(0) for _ in range(N+1)]
    v[1]=1
    updates=[]
    for _ in range(N+2):
        nextv=[Fraction(0) for _ in range(N+1)];nextv[1]=1
        j=1
        while p**(2*j)<=N:
            a=poly_pow(v,p**(2*j),N)
            for k in range(N+1):nextv[k]-=a[k]/p**j
            j+=1
        if nextv==v:break
        v=nextv
    else:raise RuntimeError('formal inversion did not converge')
    return v


def lagrange_U_power_coefficient(p:int,a:int,m:int)->Fraction:
    """Independent Lagrange inversion: [z^a] U(z)^m for a>=m>=1.

    m/a * [t^(a-m)] (1 + sum t^(p^(2j)-1)/p^j)^(-a).
    """
    if not (p>=2 and a>=m>=1):raise ValueError('invalid indices')
    target=a-m
    A=[Fraction(0) for _ in range(target+1)]
    j=1
    while p**(2*j)-1<=target:
        A[p**(2*j)-1]=Fraction(1,p**j)
        j+=1
    power=[Fraction(1)]+[Fraction(0)]*target
    coeff=Fraction(0)
    for k in range(target+1):
        coeff+=(-1)**k*comb(a+k-1,k)*power[target]
        if k<target:power=poly_mul(power,A,target)
    return Fraction(m,a)*coeff


def padic_valuation_fraction(x:Fraction,p:int)->int|None:
    """Return v_p(x); None represents infinity (x=0)."""
    if x==0:return None
    def val(n:int)->int:
        k=0
        while n%p==0:k+=1;n//=p
        return k
    return val(abs(x.numerator))-val(x.denominator)


def valuation_factorial(a:int,p:int)->int:
    s=0
    while a:
        a//=p;s+=a
    return s


def local_model_derivative(p:int,a:int,f_coeff:list[int])->Fraction:
    """For f(T) integer polynomial, compute (d/dz)^a f(U(z)) at z=0."""
    U=inverse_height_two_log(p,a)
    result=[Fraction(0) for _ in range(a+1)]
    power=[Fraction(1)]+[Fraction(0)]*a
    for coeff in f_coeff:
        for j,c in enumerate(power):result[j]+=coeff*c
        power=poly_mul(power,U,a)
    return factorial(a)*result[a]


def local_model_lower_bound(p:int,a:int)->Fraction:
    """Proved lower bound on valuation of the a-th derivative."""
    return Fraction(valuation_factorial(a,p))-Fraction(a-1,p*p-1)


if __name__=='__main__':
    for X in [16,64,256]:
        print('X=',X,'S(X) rational log-prime coefficients=',riesz_log_prime_coeffs(X))
    for p in [2,3,5]:
        U=inverse_height_two_log(p,30)
        for a in [p*p, min(30,p*p+3)]:
            print('p=',p,'a=',a,'inverse coefficient=',U[a],
                  'v_p(a! coeff)=',padic_valuation_fraction(factorial(a)*U[a],p),
                  'lower bound=',local_model_lower_bound(p,a))
