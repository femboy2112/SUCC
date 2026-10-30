"""SUCC research-only: primitive four-pole inversion rigidity and native Gamma log.

Exact rational and integer arithmetic. No selected-BBP signed cancellation claim.
The original source is unchanged; these are additive mathematical instruments.
"""
from __future__ import annotations
from fractions import Fraction as F
from math import factorial


def _positive_int(x, name: str) -> int:
    if type(x) is not int or x <= 0:
        raise ValueError(f"{name} must be a positive integer")
    return x


def weights_and_poles(m: int, d: int, p: int, q: int, r: int):
    for name, value in [('m', m),('d',d),('p',p),('q',q),('r',r)]:
        _positive_int(value,name)
    if m<=d: raise ValueError('m>d required')
    W=p+q+r
    return ((0,W),(m-d,-p),(m,-q),(m+d,-r))


def positive_source(a, m=4, d=1, p=2, q=1, r=1) -> F:
    a=F(a)
    if a<=0: raise ValueError('a>0 required')
    return sum((F(c, a+shift) for shift,c in weights_and_poles(m,d,p,q,r)),F())


def numerator_coefficients(m=4,d=1,p=2,q=1,r=1):
    """Quadratic source numerator S*a^2+L*a+C over a*(a+u)*(a+v)*(a+w)."""
    weights_and_poles(m,d,p,q,r)
    u,v,w=m-d,m,m+d
    W=p+q+r
    # Source = W/a - p/(a+u) - q/(a+v) - r/(a+w).
    # Leading a^3 cancels; compute exact coefficient of a^2/a/1.
    S=p*u+q*v+r*w
    L=W*(u*v+u*w+v*w)-p*v*w-q*u*w-r*u*v
    C=W*u*v*w
    return S,L,C


def numerator_root_product(m=4,d=1,p=2,q=1,r=1) -> F:
    S,_,C=numerator_coefficients(m,d,p,q,r)
    return F(C,S)


def self_dual_residual(m=4,d=1,p=2,q=1,r=1) -> int:
    """Zero iff root-shift product equals m^2, for all positive weights."""
    weights_and_poles(m,d,p,q,r)
    return m*(p-r)-d*(p+q+r)


def minimal_weight_solution(max_weight=9):
    _positive_int(max_weight,'max_weight')
    solutions=[]
    for W in range(3,max_weight+1):
        for p in range(1,W-1):
            for q in range(1,W-p):
                r=W-p-q
                if p<=r: continue
                ratio=F(W,p-r)
                if ratio>1:
                    solutions.append((W,p,q,r,ratio))
        if solutions: return solutions
    return []


def R(a) -> F:
    """Authentic source with U0=0 and native a_n=8n-7."""
    return positive_source(a)


def inversion_ratio(a) -> F:
    a=F(a)
    if a<=0: raise ValueError('a>0')
    return F(16)*(a+3)*(a+5)/((3*a+16)*(5*a+16))


def native_a(n: int) -> int:
    _positive_int(n,'n')
    return 8*n-7


def native_ratio(n: int) -> F:
    return inversion_ratio(native_a(n))


def native_log_gap_factors(n: int) -> tuple[F,F]:
    """exp(eta_n)= [(24n-5)/(24n-6)] [(40n-19)/(40n-20)]."""
    _positive_int(n,'n')
    return F(24*n-5,24*n-6), F(40*n-19,40*n-20)


def native_log_gap_ratio(n: int) -> F:
    l,r=native_log_gap_factors(n)
    return l*r


def normalized_native_inversion(n: int) -> F:
    """(15/16)*exp(D(8n-7)) = exp(-eta_n)."""
    return F(15,16)*native_ratio(n)


def gamma_product_exact(N: int) -> F:
    """Finite product P_N = prod_{n<=N} exp(-eta_n); P0=1."""
    if type(N) is not int or N<0:raise ValueError('N nonnegative')
    result=F(1)
    for n in range(1,N+1):
        result*=normalized_native_inversion(n)
    return result


def gamma_product_closed_finite(N: int) -> F:
    """Independent Gamma-rising-factorial certificate (no special functions)."""
    if type(N) is not int or N<0:raise ValueError('N nonnegative')
    def rising(x):
        ans=F(1)
        for j in range(N): ans*=x+j
        return ans
    return rising(F(1,2))*rising(F(3,4))/(rising(F(19,24))*rising(F(21,40)))


def harmonic(N:int)->F:
    if type(N) is not int or N<0:raise ValueError('N nonnegative')
    return sum((F(1,n) for n in range(1,N+1)),F())


def atanh_log_one_plus_bounds(k: int, M:int=5) -> tuple[F,F]:
    """Enclose log(1+1/k) for positive integer k, via 2atanh(1/(2k+1))."""
    _positive_int(k,'k'); _positive_int(M,'M')
    z=F(1,2*k+1)
    low=sum((F(2)*z**(2*j+1)/F(2*j+1) for j in range(M)),F())
    # Each denominator of the omitted sum >=2M+1.
    rem=F(2)*z**(2*M+1)/((2*M+1)*(1-z*z))
    return low,low+rem


def native_log_gap_bounds(n:int,M:int=5)->tuple[F,F]:
    _positive_int(n,'n')
    a,b=atanh_log_one_plus_bounds(24*n-6,M)
    c,d=atanh_log_one_plus_bounds(40*n-20,M)
    return a+c,b+d


def harmonic_finite_part_interval(N:int=128,M:int=5)->tuple[F,F]:
    """Rigorous rational enclosure of K=lim sum(eta_n-1/(15n)).

    The omitted n>N tail is strictly below (7/180)*sum_(n>N)n^-2
    <7/(180*N). Domain N>=1, M>=1.
    """
    _positive_int(N,'N');_positive_int(M,'M')
    low=F(0);up=F(0)
    for n in range(1,N+1):
        l,u=native_log_gap_bounds(n,M)
        low+=l
        up+=u
    h=harmonic(N)/15
    return low-h,up-h+F(7,180*N)


def original_bbp_forcing(n:int)->F:
    return R(native_a(n))


def zero_seed_history(N:int):
    if type(N) is not int or N<0:raise ValueError('N nonnegative')
    out=[F(0)]
    for n in range(1,N+1):out.append(16*out[-1]+original_bbp_forcing(n))
    return tuple(out)


if __name__=='__main__':
    assert numerator_coefficients()==(15,121,240)
    assert self_dual_residual()==0
    assert numerator_root_product()==16
    assert minimal_weight_solution()==[(4,2,1,1,F(4))]
    for n in range(1,101):
        assert native_ratio(n)*F(15,16)==F(1)/native_log_gap_ratio(n)
        assert gamma_product_exact(n)==gamma_product_closed_finite(n)
    print('MINIMAL_POLE_GAMMA_EXACT_PASS 100 clock/product certificates')
