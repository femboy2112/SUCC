"""Critical-frequency calibrated BBP coherent-seed tail; exact rational instrument.

This module does NOT prove pi normality.  All source values are exact Fraction;
its asymptotic chirp statement is justified in PROOFS.md, not by numerical runs.
"""
from __future__ import annotations
from fractions import Fraction as F
from math import gcd, lcm, log


def forcing(n: int) -> F:
    if type(n) is not int or n < 1:
        raise ValueError('positive integer source time required')
    return F(4, 8*n-7) - F(2, 8*n-4) - F(1, 8*n-3) - F(1, 8*n-2)


def forcing_polynomial(n: int) -> F:
    if type(n) is not int or n < 1:
        raise ValueError('positive integer source time required')
    return F(120*n*n - 89*n+16, (2*n-1)*(4*n-1)*(8*n-7)*(8*n-3))


def exact_phase_epoch(A: int, seed: F = F(0)) -> tuple[F, ...]:
    if type(A) is not int or A < 2:
        raise ValueError('A >= 2 required')
    x = F(seed)%1
    result=[]
    for n in range(1,2*A):
        x=(16*x+forcing(n))%1
        if n>=A:
            result.append(x)
    return tuple(result)


def independent_modular_phase_epoch(A: int) -> tuple[F, ...]:
    """Independent common-odd-register evaluator using collapsed polynomial."""
    if type(A) is not int or A < 2:
        raise ValueError('A >= 2 required')
    M=1
    for n in range(1,2*A):
        M=lcm(M,forcing_polynomial(n).denominator)
    assert M%2==1
    v=0
    out=[]
    for n in range(1,2*A):
        r=forcing_polynomial(n)
        v=(16*v+(M//r.denominator)*r.numerator)%M
        if n>=A:
            out.append(F(v,M))
    return tuple(out)


def coherent_tail_bounds(n: int, terms: int = 16) -> tuple[F,F]:
    """Lower and upper exact bounds on T_n = sum_(k>=1)16^-k r(n+k).

    The infinite remainder is at most r(n+terms+1)*16^-terms/15,
    using genuine positive decreasing original forcing.
    """
    if type(n) is not int or n < 1 or type(terms) is not int or terms < 1:
        raise ValueError('n>=1 and positive terms required')
    lower=sum((forcing(n+k)/16**k for k in range(1,terms+1)),F(0))
    upper=lower+forcing(n+terms+1)*F(1,15*16**terms)
    assert F(0)<lower<upper
    return lower,upper


def rigorous_tail_sandwich(n:int,terms:int=16)->dict:
    """Check independent exact finite bounds against the all-n paper theorem."""
    low,high=coherent_tail_bounds(n,terms)
    model=F(1,64*n*n)
    error=F(1,64*n*n*n)
    if not (0<low<high<model and model-low<error):
        raise AssertionError('tail sandwich outside proposed all-n range')
    return {'n':n,'terms':terms,'tail_lower':low,'tail_upper':high,
            'model':model,'max_error':error}


def critical_frequency(A:int,h:int)->int:
    """Exactly integral h*16^j just below A² log(A), for a finite probe.

    This real log is only an instrument choice, NOT a theorem certificate.
    """
    if type(A) is not int or A<2 or type(h) is not int or h==0:
        raise ValueError('A>=2, integer h!=0')
    H=abs(h); target=A*A*log(A)
    if H>target:
        raise ValueError('no nonnegative radix depth for h at this A')
    while 16*H<=target:
        H*=16
    return H


def coherent_chirp_leading_constant()->F:
    """The exact rational prefactor 256, with analytic pi in denominator."""
    return F(256)


def calibration_ratio(A:int,H:int)->F:
    if type(A) is not int or A<2 or type(H) is not int or H<=0:
        raise ValueError('positive epoch and frequency required')
    return F(H,A*A)
