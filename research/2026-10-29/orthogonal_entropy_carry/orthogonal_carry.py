"""Original four-pole BBP carry correction, sparse thermodynamic observers.

All source arithmetic is Fraction-exact. None of the code claims pi-normality
or that Shannon information is physical heat. Historical source is read-only.
"""
from __future__ import annotations

from collections import Counter
from fractions import Fraction as Q
from math import comb, gcd, log

RADIX = 16


def authentic_r(n: int) -> Q:
    if type(n) is not int or n < 1:
        raise ValueError("original source index must be positive")
    return (Q(4, 8*n-7) - Q(2, 8*n-4)
            - Q(1, 8*n-3) - Q(1, 8*n-2))


def source_upper_gap(n: int) -> Q:
    """Exact >0 for n>=3, with positive-coefficient translated certificate."""
    if type(n) is not int or n < 3:
        raise ValueError("n>=3 required")
    return Q(1, 2*n*n) - authentic_r(n)


def source_bound_polynomial(n: int) -> int:
    """Numerator of source_upper_gap times its positive denominator."""
    if type(n) is not int or n < 3:
        raise ValueError("n>=3 required")
    return 272*n**4 - 846*n**3 + 680*n**2 - 206*n + 21


def zero_run(n: int) -> int:
    """Largest L with 16^L<=n². All carry corrections at n>=3 force L zeros."""
    if type(n) is not int or n < 3:
        raise ValueError("n>=3 required")
    power, out = 1, 0
    while power*RADIX <= n*n:
        power *= RADIX
        out += 1
    return out


def frac(x: Q) -> Q:
    return x - x.numerator // x.denominator


def step(x: Q, n: int) -> tuple[Q, int, int, bool]:
    """(next phase, literal carry, unforced radix digit, mismatch) at source n."""
    x=frac(Q(x))
    r=authentic_r(n)
    bare = (RADIX*x).numerator // (RADIX*x).denominator
    raw=RADIX*x+r
    carry=raw.numerator//raw.denominator
    return frac(raw), carry, bare, carry!=bare


def forced_run_from_correction(n: int, c: int) -> tuple[Q, list[int]]:
    """Exact adversarial witness: at source n, bare c-1 and forced carry c.

    Select x_before=(c-r(n)/2)/16. Valid for 1<=c<=16, n>=3.
    """
    if type(c) is not int or not 1<=c<=16 or type(n) is not int or n<3:
        raise ValueError("source n>=3, corrected carry c in 1..16")
    r=authentic_r(n)
    before=Q(c,16)-r/32
    x,k,d,m=step(before,n)
    if k!=c or d!=c-1 or not m or x!=r/2:
        raise ArithmeticError("calibration mismatch")
    carries=[]
    for t in range(n+1,n+zero_run(n)+1):
        x,k,_,_=step(x,t)
        carries.append(k)
    return x,carries


def trace(seed: Q, length: int):
    if type(length) is not int or not 1<=length<=10000:
        raise ValueError("length must be 1..10000")
    x=frac(Q(seed))
    result=[]
    for n in range(1,length+1):
        x,carry,digit,mismatch=step(x,n)
        result.append((carry,digit,mismatch))
    return result


def mismatch_bound(N: int, M: int|None=None) -> int:
    """Source theorem: <= M+floor((N-M)/(1+L(M))) for 3<=M<=N."""
    if type(N) is not int or N < 3:
        raise ValueError("N>=3")
    if M is None:
        from math import isqrt
        M=isqrt(N)
        if M*M<N: M+=1
        M=max(3,M)
    if type(M) is not int or not 3<=M<=N:
        raise ValueError("3<=M<=N")
    return M+(N-M)//(zero_run(M)+1)


def empirical_words(xs: list[int], k: int) -> dict[tuple[int,...],Q]:
    if type(k) is not int or k<1 or k>len(xs):
        raise ValueError("1<=k<=length")
    N=len(xs)-k+1
    counts=Counter(tuple(xs[j:j+k]) for j in range(N))
    return {v:Q(count,N) for v,count in counts.items()}


def total_variation(p:dict, q:dict) -> Q:
    return sum((abs(p.get(w,Q())-q.get(w,Q())) for w in p.keys()|q.keys()), Q())/2


def circular_words(xs: list[int], k: int) -> dict[tuple[int,...],Q]:
    if not xs or type(k) is not int or k<1:
        raise ValueError("nonempty word and positive depth")
    L=len(xs)
    counts=Counter(tuple(xs[(i+j)%L] for j in range(k)) for i in range(L))
    return {w:Q(c,L) for w,c in counts.items()}


def shannon(p:dict) -> float:
    return -sum(float(v)*log(float(v)) for v in p.values() if v>0)


def binary_h(t:float) -> float:
    if t<=0 or t>=1: return 0.0
    return -t*log(t)-(1-t)*log(1-t)


def entropy_continuity_bound(k: int,delta:float) -> float:
    """Fannes coupling bound, natural logarithms; valid for all delta in [0,1]."""
    if type(k) is not int or k<1 or not 0<=delta<=1:
        raise ValueError("positive k; delta in [0,1]")
    m=RADIX**k
    if delta > 1-1/m:
        return log(m)
    return binary_h(delta)+delta*log(m-1)


def entropy_deficit(p:dict, k: int)->float:
    """KL(p || uniform over 16^k) = k log16 - H(p)."""
    return k*log(RADIX)-shannon(p)


def local_pressure(p:dict, potential:dict, default:float=0)->float:
    """Finite empirical thermodynamic observer log E_p exp(f)."""
    from math import exp
    if not p: raise ValueError("nonempty distribution required")
    return log(sum(float(a)*exp(float(potential.get(w,default))) for w,a in p.items()))


def pressure_difference_bound(delta:float, max_abs_potential:float)->float:
    """Universal two-source upper bound 2 exp(2B)*TV for |f|<=B."""
    from math import exp
    if not 0<=delta<=1 or max_abs_potential<0:
        raise ValueError("nonnegative bounds required")
    return 2*exp(2*max_abs_potential)*delta


def primitive_digit(d:int,q:int=6)->int:
    if type(d) is not int or not 0<=d<16 or type(q) is not int or q<1:
        raise ValueError("a base-16 digit and a positive modulus")
    return int(gcd(d,q)==1)


def walsh(digit:int,mask:int)->int:
    if type(digit) is not int or not 0<=digit<16 or type(mask) is not int or not 0<=mask<16:
        raise ValueError("4-bit digit and 4-bit mask")
    return (-1)**((digit & mask).bit_count() % 2)


def walsh_coefficients(p:dict)->list[Q]:
    """Exact 16-coordinate orthogonal Walsh transform of a one-digit law."""
    if any(type(v) is not tuple or len(v)!=1 or not 0<=v[0]<16 for v in p):
        raise ValueError("one-digit keys")
    if sum(p.values(),Q())!=1: raise ValueError("probability law must normalize")
    return [sum((v*walsh(k[0],m) for k,v in p.items()),Q()) for m in range(16)]


def chi2_walsh(p:dict)->Q:
    a=walsh_coefficients(p)
    return sum((t*t for t in a[1:]),Q())


def debruijn16(order:int)->list[int]:
    """Deterministic de Bruijn cycle, no external dependency."""
    if type(order) is not int or not 1<=order<=3:
        raise ValueError("order 1..3 for bounded negative controls")
    alphabet=16
    a=[0]*(alphabet*order+1)
    out=[]
    def db(t,p):
        if t>order:
            if order%p==0: out.extend(a[1:p+1])
        else:
            a[t]=a[t-p]
            db(t+1,p)
            for j in range(a[t-p]+1,alphabet):
                a[t]=j; db(t+1,t)
    db(1,1)
    return out


def stationary_forward_backward_entropy(word:list[int],k:int)->tuple[float,float]:
    """Exact equality algebraically: cyclic H_(k+1)-H_k for both directions."""
    Hk=shannon(circular_words(word,k))
    Hkp=shannon(circular_words(word,k+1))
    return (Hkp-Hk,Hkp-Hk)
