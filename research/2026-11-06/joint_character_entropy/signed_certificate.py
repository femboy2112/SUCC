"""Rigorous rational interval for a finite selected SUCC joint Weyl character.

No floating-point trigonometric function is part of a certificate.  The
rational phase grid, Machin pi enclosure, and Taylor/Lagrange remainder
are explicit.  A finite signed bound is NOT an asymptotic normality theorem.
"""
from __future__ import annotations
from fractions import Fraction
from math import factorial, isqrt
from typing import Sequence
from joint_entropy import original_states,tail_enclosure
from independent_oracle import machin_pi16_interval

M = 12
GRID = 2**40
PI_GRID = 2**60
PI_CEILING = Fraction(22,7)
SCALE = 10**12


def certified_pi_grid() -> tuple[Fraction,Fraction]:
    alpha_lo,alpha_hi=machin_pi16_interval(80,26)
    pi_lo,pi_hi=16*alpha_lo,16*alpha_hi
    k=(pi_lo*PI_GRID).numerator//(pi_lo*PI_GRID).denominator
    pi_grid=Fraction(k,PI_GRID)
    assert 3 < pi_grid < pi_lo < pi_hi < PI_CEILING
    return pi_grid,pi_hi-pi_grid


def rational_round(x:Fraction) -> int:
    y=x+Fraction(1,2)
    return y.numerator//y.denominator


def frac_pow_series(theta: Fraction, order: int=M) -> tuple[Fraction,Fraction]:
    """Degree 2M cosine / degree 2M+1 sine; rational, no floats."""
    t2=theta*theta
    cos=Fraction(1)
    ct=Fraction(1)
    sin=theta
    st=theta
    for j in range(1,order+1):
        ct=-ct*t2/Fraction((2*j-1)*(2*j))
        st=-st*t2/Fraction((2*j)*(2*j+1))
        cos+=ct
        sin+=st
    return cos,sin


def lagrange_error(order:int=M) -> Fraction:
    """Sum of real & imaginary Taylor remainder bounds for |theta|<22/7."""
    return (PI_CEILING**(2*order+1)/factorial(2*order+1)
            + PI_CEILING**(2*order+2)/factorial(2*order+2))


def floor_q(x:Fraction) -> int:
    return x.numerator//x.denominator


def ceil_q(x:Fraction) -> int:
    return -floor_q(-x)


def norm_interval(real:Fraction,imag:Fraction,eps:Fraction)->tuple[Fraction,Fraction]:
    """Rigorous sqrt(R^2+I^2) envelope on decimal rational grid."""
    if eps<0:
        raise ValueError("nonnegative error required")
    q=(real*real+imag*imag)*SCALE**2
    low_root=isqrt(floor_q(q))
    high_root=isqrt(ceil_q(q))
    if high_root*high_root<ceil_q(q):
        high_root+=1
    lo=max(Fraction(0),Fraction(low_root,SCALE)-eps)
    hi=Fraction(high_root,SCALE)+eps
    return lo,hi


def source_completed_samples(A:int, *,depth:int=12) -> tuple[tuple[Fraction,Fraction],...]:
    """Exactly enclose the original selected z_n for [A,2A) as lift pairs."""
    if type(A) is not int or A<1:
        raise ValueError("A must be positive integer")
    x=original_states(2*A)
    out=[]
    for n in range(A,2*A):
        lo,hi=tail_enclosure(n,depth)
        out.append((x[n]+lo,x[n]+hi))
    return tuple(out)


def certified_weyl(samples:Sequence[tuple[Fraction,Fraction]],h:int) -> dict:
    """Rigorous |average exp(2 pi i h z)| interval from rational source intervals.

    Any samples of rational lifts (lo,hi) with actual z inside may be used,
    including negative/null controls.  Control h must be integer nonzero.
    """
    if type(h) is not int or h==0 or not samples:
        raise ValueError("nonzero integer h and nonempty sample required")
    pigrid,pierr=certified_pi_grid()
    csum=Fraction(0);ssum=Fraction(0);error=Fraction(0)
    taylor=lagrange_error()
    for lo,hi in samples:
        if lo>hi or hi-lo>Fraction(1,2):
            raise ValueError("invalid or dangerously broad phase interval")
        center=(lo+hi)/2
        phase=(h*center)%1
        if phase>Fraction(1,2):
            phase-=1
        m=rational_round(phase*GRID)
        u=Fraction(m,GRID)
        assert abs(u)<=Fraction(1,2)
        theta=2*pigrid*u
        c,s=frac_pow_series(theta)
        csum+=c;ssum+=s
        # First: source enclosure and quantization on circle, π<=22/7.
        # Second: replacing true π by pigrid, |2u|<=1.
        # Third: Taylor Lagrange remainder, |theta|<22/7.
        error+=PI_CEILING*(abs(h)*(hi-lo)+Fraction(1,GRID))+pierr+taylor
    N=len(samples)
    R=csum/N; I=ssum/N; avg_err=error/N
    lower,upper=norm_interval(R,I,avg_err)
    return {"h":h,"N":N,"lower":lower,"upper":upper,
            "re_poly":R,"im_poly":I,"total_error":avg_err,
            "taylor_error":taylor,"pi_grid_error":pierr}


def decimal_floor(q:Fraction,digits:int=12) -> str:
    d=10**digits; x=floor_q(q*d)
    return f'{x//d}.{x%d:0{digits}d}'


def decimal_ceil(q:Fraction,digits:int=12) -> str:
    d=10**digits; x=ceil_q(q*d)
    return f'{x//d}.{x%d:0{digits}d}'


def short_receipt(v:dict)->dict:
    return {"h":v["h"],"N":v["N"],"rigorous_lower_floor_12dp":decimal_floor(v["lower"]),
            "rigorous_upper_ceil_12dp":decimal_ceil(v["upper"]),
            "rigorous_average_error_ceiling_12dp":decimal_ceil(v["total_error"])}


if __name__=='__main__':
    import json
    r=certified_weyl(tuple((Fraction(j,16),Fraction(j,16)) for j in range(16)),1)
    print(json.dumps(short_receipt(r)))
