"""Exact arbitrary-order source-Laurent lag normal forms for SUCC's four poles.

Every finite order is a mathematical model specialization with an exact
remainder. Enlarged signed-lag transport windows are NOT signed cancellation.
No external packages or numerical pi approximations are required.
"""
from __future__ import annotations
from fractions import Fraction as F
from functools import lru_cache

WEIGHTS=(4,-2,-1,-1)
POLES=(F(7,8),F(1,2),F(3,8),F(1,4))


def original_r(n:int)->F:
    if type(n) is not int or n<1:raise ValueError('n must be positive integer')
    return sum((F(w,8*n-int(8*p)) for w,p in zip(WEIGHTS,POLES)),F(0))


def direct_r(n:int)->F:
    if type(n) is not int or n<1:raise ValueError('n must be positive integer')
    return F(120*n*n-89*n+16,(2*n-1)*(4*n-1)*(8*n-7)*(8*n-3))


def true_source_lag(n:int,k:int)->F:
    if type(n) is not int or n<1 or type(k) is not int or k<1:
        raise ValueError('positive integer time and lag required')
    return sum((F(16**(k-j))*original_r(n+j) for j in range(1,k+1)),F(0))


def moment(d:int)->F:
    """M_d=sum_(j>=1) j^d/16^j, Eulerian rational generating function."""
    if type(d) is not int or d<0 or d>36:
        raise ValueError('bounded nonnegative order required')
    x=F(1,16)
    if d==0:return x/(1-x)
    row=[1]
    for n in range(2,d+1):
        row=[(j+1)*(row[j] if j<len(row) else 0)+(n-j)*(row[j-1] if j>0 else 0)
             for j in range(n)]
    a=sum((coef*x**j for j,coef in enumerate(row)),F(0))
    return x*a/(1-x)**(d+1)


@lru_cache(maxsize=1024)
def source_laurent_coeff(a:int,j:int)->F:
    """Coefficient at n^{-(a+1)} of r(n+j) (a>=0)."""
    if type(a) is not int or a<0 or type(j) is not int or j<1:
        raise ValueError('valid Taylor index/source shift required')
    return sum((F(w,8)*(-F(j)+p)**a for w,p in zip(WEIGHTS,POLES)),F(0))


def corrected_lag(n:int,k:int,d:int)->F:
    """Source-derived d-th order truncated lag (powers n^-1 through n^-d).

    d>=2; first 1/n coefficient vanishes by original residue sum zero.
    All source terms are retained through n^-d, with a rigorous exact remainder.
    """
    if type(n) is not int or n<1 or type(k) is not int or k<1 or type(d) is not int or not 2<=d<=36:
        raise ValueError('positive n,k and Laurent order 2..36 required')
    return sum((F(16**(k-j))*sum((source_laurent_coeff(a,j)/n**(a+1)
                                   for a in range(1,d)),F(0))
                for j in range(1,k+1)),F(0))


def residual_bound(n:int,k:int,d:int)->F:
    if type(n) is not int or n<1 or type(k) is not int or k<1 or type(d) is not int or not 2<=d<=36:
        raise ValueError('valid n,k,d required')
    return F(16**k,n**(d+1))*moment(d)


def first_positive_curvature_bound(n:int,k:int)->tuple[F,F,F]:
    """0< A/(64n²)-F_(n,k) < 16^k/(30n³), with A=16^k-1.

    Lower uses r(m)>15/(64m²) (m>=1), and upper uses
    r(n+j)<15/(64 n²) (j>=1), both true for authentic source.
    """
    if type(n) is not int or n<1 or type(k) is not int or k<1:
        raise ValueError('valid n,k required')
    leading=F(16**k-1,64*n*n)
    actual=true_source_lag(n,k)
    eps=F(16**k,30*n**3)
    if not F(0)<leading-actual<eps:
        raise AssertionError('source curvature inequality failed')
    return leading,actual,eps


def integer_ceil_root(n:int,p:int)->int:
    if type(n) is not int or n<0 or type(p) is not int or p<1:
        raise ValueError('nonnegative integer and positive root order required')
    if n<=1:return n
    # Integer bisection, no floating approximation or root dependency.
    lo,hi=0,1
    while hi**p<n:hi*=2
    while lo+1<hi:
        mid=(lo+hi)//2
        if mid**p>=n:hi=mid
        else:lo=mid
    return hi


def fractional_ceil_root(x:F,p:int)->int:
    y=F(x)
    if y<0 or type(p) is not int or p<1:
        raise ValueError('nonnegative rational and positive root order required')
    if y==0:return 0
    lo,hi=0,1
    while F(hi**p)<y:hi*=2
    while lo+1<hi:
        mid=(lo+hi)//2
        if F(mid**p)>=y:hi=mid
        else:lo=mid
    return hi


def per_lag_phase_budget(k:int,h:int,d:int)->F:
    """Rational majorant for |C_(N,k)(h)-D^d_(N,k)(h)| all N>k.

    Clipping min(2,2*pi|h| M_d16^k/n^(d+1)) and monotone integral.
    Pi<22/7; the p-th root is rounded UP by exact integer arithmetic.
    """
    if type(k) is not int or k<1 or type(h) is not int or h==0 or type(d) is not int or not 2<=d<=36:
        raise ValueError('valid k,h,d required')
    p=d+1
    a_over_two=F(22*abs(h),7)*moment(d)*16**k
    ceiling=fractional_ceil_root(a_over_two,p)
    return F(2*p,p-1)*ceiling


def aggregate_transport_budget(n:int,K:int,h:int,d:int)->F:
    """Exactly weighted rational VdC source-error budget for selected lag."""
    if type(n) is not int or n<1 or type(K) is not int or not 1<=K<=n or type(h) is not int or h==0:
        raise ValueError('invalid horizon/clock/harmonic')
    return F(2,K*K*n)*sum(((K-k)*per_lag_phase_budget(k,h,d)
                            for k in range(1,K)),F(0))


def corrected_clock(n:int,d:int)->int:
    """K=min(N,max(1,floor((d+1)log_16 N))), integer exact."""
    if type(n) is not int or n<1 or type(d) is not int or not 2<=d<=36:
        raise ValueError('valid horizon/order required')
    p=d+1
    # K=floor(log_16(n**p)) computed by exact integer comparison.
    v=n**p
    k=0
    while v>=16:
        v//=16;k+=1
    return min(n,max(1,k))


def source_bulk_ratio(n:int,k:int)->F:
    """Exact phase normalization 64n² F_(n,k)/(16^k-1), for diagnostics."""
    if type(n) is not int or n<1 or type(k) is not int or k<1:
        raise ValueError('valid n,k required')
    return F(64*n*n,16**k-1)*true_source_lag(n,k)
