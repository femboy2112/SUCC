"""Exact original BBP and Pell/Pisot two-conjugate seam.

Research only. No temporal signed Fourier cancellation is asserted.
All core algebra uses integers/Fraction, not floating point.
"""
from fractions import Fraction
from functools import lru_cache


@lru_cache(maxsize=None)
def pell(k):
    """(p,q) with (1+sqrt2)^k=p+q sqrt2."""
    if k < 0:
        raise ValueError("k>=0")
    p,q=1,0
    for _ in range(k):
        p,q=p+2*q,p+q
    return p,q


def mul(a,b):
    return (a[0]*b[0]+2*a[1]*b[1], a[0]*b[1]+a[1]*b[0])


def independent_power(k):
    out=(1,0)
    for _ in range(k):
        out=mul(out,(1,1))
    return out


def bezout(k):
    """u,v with u*lambda^k+v*lambda^(k+1)=1."""
    q=pell(k)[1]
    qp=pell(k+1)[1]
    sign=(-1)**k
    return sign*qp,-sign*q


def signed_conjugate(k):
    p,q=pell(k)
    return p,-q


def signed_sheet_coefficient(k,conjugate=False):
    u,v=bezout(k)
    a=signed_conjugate(k) if conjugate else pell(k)
    b=signed_conjugate(k+1) if conjugate else pell(k+1)
    return u*a[0]+v*b[0],u*a[1]+v*b[1]


def signed_trace_coefficient(k):
    u,v=bezout(k)
    return 2*(u*pell(k)[0]+v*pell(k+1)[0])


def signed_primitive_coefficient(k):
    u,v=bezout(k)
    return u*pell(k)[0]+v*pell(k+1)[0]


def original_source(n):
    if n<1: raise ValueError("n>=1")
    return sum((Fraction(c,8*n-a) for c,a in
                ((4,7),(-2,4),(-1,3),(-1,2))),Fraction())


def independent_original_source(n):
    return Fraction(120*n*n-89*n+16,
                    (2*n-1)*(4*n-1)*(8*n-7)*(8*n-3))


@lru_cache(maxsize=4096)
def alpha_cut(b):
    if b<0:raise ValueError("b>=0")
    return sum((original_source(j)/16**j for j in range(1,b+1)),Fraction())


def state(n):
    if n<0:raise ValueError("n>=0")
    return 16**n*alpha_cut(n)


def future(n,b):
    """Original normalized finite future R_(n,b)."""
    if not 0<=n<=b:raise ValueError("0<=n<=b")
    return sum((original_source(j)/16**(j-n)
                for j in range(n+1,b+1)),Fraction())


def phase_lift(n,b):
    """Y_(n,b)={U_n}+R_(n,b)=16^n alpha_b-floor(U_n)."""
    U=state(n)
    carry=U.numerator//U.denominator
    return U-carry+future(n,b)


def exact_seam_verify(n,m,b):
    if not 0<=n<=m<=b:raise ValueError("0<=n<=m<=b")
    assert future(n,b)==future(n,m)+future(m,b)/16**(m-n)
    U=state(n); c=U.numerator//U.denominator
    assert phase_lift(n,b)==16**n*alpha_cut(b)-c
    assert phase_lift(n,b)-phase_lift(n,m)==future(m,b)/16**(m-n)
    return True


def original_tail_upper(n):
    if n<0:raise ValueError("n>=0")
    return Fraction(1,(8*n+1)*(8*n+2))


def joint_phase_exponent(n,b,k,h=1,conjugate=False):
    """Signed TWO-channel exact result, a rational exponent modulo Z."""
    p,q=signed_sheet_coefficient(k,conjugate)
    Y=phase_lift(n,b)
    return (h*Y*p,h*Y*q)  # The second component must be exactly zero.


def primitive_phase_exponent(n,k,h=1):
    return h*(state(n)%1)*signed_primitive_coefficient(k)


def integer_trace_phase_exponent(n,k,h=1):
    return h*(state(n)%1)*signed_trace_coefficient(k)


def gamma_trace_exponent_error(n,b,k):
    """(A,B) for e(h L_k x) vs e(h lambda^k Y), divided by h."""
    x=state(n)%1
    R=future(n,b)
    p,q=pell(k)
    return p*(x-R),-q*(x+R)


def sign_sqrt2(A,B):
    """Exact sign of A+B sqrt(2) for rational A,B; no precision loss."""
    A=Fraction(A);B=Fraction(B)
    if not B: return (A>0)-(A<0)
    if not A: return (B>0)-(B<0)
    if A>0 and B>0:return 1
    if A<0 and B<0:return -1
    if A>0 and B<0:return (A*A>2*B*B)-(A*A<2*B*B)
    return (2*B*B>A*A)-(2*B*B<A*A)


def regulator_integer_scale(a):
    """Global minimizer of lambda^-k + lambda^k/(64a^2) over k>=0."""
    if a<1:raise ValueError("a>=1")
    k=0
    while True:
        p,q=pell(k)
        if sign_sqrt2(p-8*a,q)>0:break
        k+=1

    def cost(i):
        p,q=pell(i);sigma=(-1)**i
        f=Fraction(1,64*a*a)
        return p*(sigma+f),q*(-sigma+f)

    best=max(0,k-3)
    for i in range(best+1,k+4):
        a0,b0=cost(i);a1,b1=cost(best)
        if sign_sqrt2(a0-a1,b0-b1)<0:
            best=i
    return best


def phase_error_rational_upper(n,b,k):
    """Exact rational enclosure for Q(sqrt2) exponent mismatch.

    Numerical enclosure is bounded to modest k by a fixed rational sqrt2
    interval; full all-k theorem uses sign_sqrt2 algebra instead.
    """
    lo=Fraction(14142135623730950,10**16)
    hi=Fraction(14142135623730951,10**16)
    assert lo*lo<2<hi*hi
    A,B=gamma_trace_exponent_error(n,b,k)
    return max(abs(A+B*lo),abs(A+B*hi))
