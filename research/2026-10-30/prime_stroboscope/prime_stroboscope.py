"""Research-only BBP prime stroboscope. All exact rational / modular arithmetic.

Native four-pole BBP source U_0=0, U_n=16 U_{n-1}+r(n).
The prime stroboscope studies a p-primary *component* of rational U_n,
not the real-circle distribution of pi's hexadecimal digits.
"""
from fractions import Fraction
from math import isqrt

OFFSETS = (1, 4, 5, 6)
BBP_COEFFICIENTS = (Fraction(4), Fraction(-2), Fraction(-1), Fraction(-1))


def prime(n: int) -> bool:
    if n < 2:
        return False
    for x in range(2, isqrt(n) + 1):
        if n % x == 0:
            return False
    return True


def source_term(n: int, coefficients=BBP_COEFFICIENTS) -> Fraction:
    if n < 1 or len(coefficients) != 4:
        raise ValueError("native BBP time >=1 and exactly four coefficient channels required")
    return sum((Fraction(c, 8*(n-1)+d) for d, c in zip(OFFSETS, coefficients)), Fraction())


def prefix(n: int, coefficients=BBP_COEFFICIENTS, seed=Fraction()) -> Fraction:
    if n < 0:
        raise ValueError("n must be nonnegative")
    u=Fraction(seed)
    for m in range(1,n+1):
        u=16*u+source_term(m,coefficients)
    return u


def rational_mod_p(r: Fraction, p: int) -> int:
    r=Fraction(r)
    if r.denominator % p == 0:
        raise ValueError("rational has a p-denominator; no mod-p residue")
    return (r.numerator * pow(r.denominator, -1, p)) % p


def strobe_time(p: int, k: int) -> int:
    if not prime(p) or p%8 not in (1,5) or k<1 or p<=8*k-2:
        raise ValueError("prime p == 1 or 5 (mod 8), k>=1, p>8k-2 required")
    numerator=(4*k-1)*p+1
    assert numerator%4==0
    return numerator//4


def mirror_coefficients(coefficients):
    """p == 5 mod8 pole-exchange involution (1,5) with powers -4, -1/4."""
    A,B,C,D=map(Fraction,coefficients)
    return (-4*C,B,-A/4,D)


def predicted_strobe_residue(p: int, k: int, coefficients=BBP_COEFFICIENTS) -> int:
    strobe_time(p,k)
    c=coefficients if p%8==1 else mirror_coefficients(coefficients)
    return rational_mod_p(prefix(k,c),p)


def actual_scaled_residue(p: int, k: int, coefficients=BBP_COEFFICIENTS) -> int:
    """Direct rational orbit p*U_N reduced modulo p (small/moderate N only)."""
    n=strobe_time(p,k)
    return rational_mod_p(p*prefix(n,coefficients),p)


def modular_scaled_residue(p: int, k: int, coefficients=BBP_COEFFICIENTS) -> int:
    """Second route: modulo-p recurrence for p*U_n, without large Fractions.

    Under p>8k-2 each native denominator is less than p^2. Terms with a
    denominator not divisible by p vanish after multiplying by p;
    those with denominator p*q contribute c/q mod p.
    """
    N=strobe_time(p,k)
    v=0
    for n in range(1,N+1):
        new=Fraction()
        for d,c in zip(OFFSETS,coefficients):
            denominator=8*(n-1)+d
            if denominator%p==0:
                if denominator%(p*p)==0:
                    raise AssertionError("p^2 not permitted in stated prime/clock range")
                new+=Fraction(c)/Fraction(denominator//p)
        v=(16*v+rational_mod_p(new,p))%p
    return v


def events(p: int, k: int):
    """(native index, multiplier q, actual pole offset delta, source coefficient)."""
    N=strobe_time(p,k)
    out=[]
    for n in range(1,N+1):
        for d,c in zip(OFFSETS,BBP_COEFFICIENTS):
            denom=8*(n-1)+d
            if denom%p==0:
                out.append((n,denom//p,d,c))
    return tuple(out)


def milestone_times(p:int):
    strobe_time(p,1)
    birth=(p+7)//8 if p%8==1 else (p+3)//8
    four=(p+1)//2
    five=(5*p+3)//8 if p%8==1 else (5*p+7)//8
    six=(3*p+1)//4
    assert birth<four<five<six
    return (birth,four,five,six)


def p_primary_decomposition(u:Fraction,p:int):
    """Exact Q/Z = p-primary character + prime-to-p cofiber (for exponent <=1).

    Return (a,p,b,D): u = a/p+b/D (mod Z), with gcd(p,D)=1.
    If p absent from the reduced denominator, a=0, D=denominator.
    """
    if not prime(p):raise ValueError('prime required')
    u=Fraction(u)
    A,D0=u.numerator,u.denominator
    if D0%p:
        return (0,p,A%D0,D0)
    D=D0//p
    if D%p==0:raise ValueError('higher p valuation not supported')
    a=A*pow(D,-1,p)%p
    b=(A*pow(p,-1,D))%D if D>1 else 0
    diff=u-Fraction(a,p)-Fraction(b,D)
    assert diff.denominator==1
    return a,p,b,D


def order_16(p:int) -> int:
    """Multiplicative order of 16 mod odd prime p, exact (finite calibration)."""
    if not prime(p) or p==2:raise ValueError("odd prime required")
    val=16%p
    d=1
    while val!=1:
        d+=1
        val=(val*16)%p
    assert (p-1)%d==0
    return d
