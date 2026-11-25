"""Exact period-normalized theta jets for the CM lemniscate illustration.

Input classical analytic identification (NOT proved here):
  Theta(z)/Theta(0) = sigma(u)^2 * wp(u), u=omega_bar*z/(2*pi),
  with Weierstrass invariants g2=4, g3=0.
This module reconstructs all finite rational Taylor coefficients from
wp''=6 wp^2-2 and (log sigma)''=-wp, independently of numerical theta sums.
This is NOT an implementation of the RH automorphic theta-lift kernel.
"""
from __future__ import annotations
from fractions import Fraction
from math import factorial


class PeriodSourceError(ValueError):
    pass


def wp_laurent_coefficients(max_k: int) -> tuple[Fraction, ...]:
    """u^2 wp(u) = sum_{k>=0} a_k u^(4k); a0=1, g2=4,g3=0."""
    if not isinstance(max_k, int) or max_k < 0:
        raise PeriodSourceError("invalid CM period jet depth")
    a = [Fraction(1)]
    for k in range(1, max_k+1):
        nonlinear = sum((a[j]*a[k-j] for j in range(1,k)),Fraction(0))
        numerator = 6*nonlinear - (2 if k==1 else 0)
        denominator=(4*k-2)*(4*k-3)-12
        a.append(numerator/denominator)
    return tuple(a)


def sigma2_wp_coefficients(max_k: int) -> tuple[Fraction,...]:
    """Sigma(u)^2 wp(u) = sum f_k u^(4k), f0=1, derived exactly.

    log(sigma(u)/u) = -sum a_k u^(4k) / ((4k)(4k-1));
    f(x) = A(x) exp[-2 sum a_k x^k/((4k)(4k-1))], x=u^4.
    """
    a=wp_laurent_coefficients(max_k)
    b=[Fraction(0)]+[-2*a[k]/((4*k)*(4*k-1)) for k in range(1,max_k+1)]
    exponential=[Fraction(1)]
    for k in range(1,max_k+1):
        value=sum((j*b[j]*exponential[k-j] for j in range(1,k+1)),Fraction(0))/k
        exponential.append(value)
    return tuple(sum((a[j]*exponential[k-j] for j in range(k+1)),Fraction(0))
                 for k in range(max_k+1))


def normalized_theta_period_jets(max_k: int)->tuple[Fraction,...]:
    """r_k=T_(4k)/(T0*(omega_bar/pi)^(4k)) under the classical bridge."""
    f=sigma2_wp_coefficients(max_k)
    return tuple(f[k]*factorial(4*k)/2**(4*k) for k in range(max_k+1))


def lemma_theta_normalization_audit(max_k:int)->dict[str,object]:
    """Finite audit only: denominators divide 4^k for inspected coefficients."""
    r=normalized_theta_period_jets(max_k)
    failures=tuple(k for k,a in enumerate(r) if (4**k*a).denominator!=1)
    if failures:
        raise PeriodSourceError("failed finite CM theta normalization audit")
    return {"degree":max_k,"coefficients":r,
            "integral_normalized_jets":tuple(int(4**k*a) for k,a in enumerate(r))}


def lemniscate_formal_log_coefficients(degree:int)->tuple[Fraction,...]:
    """Classical integral of (1-x^4)^(-1/2), exact monomial coefficients."""
    from math import comb
    if not isinstance(degree,int) or degree<1:
        raise PeriodSourceError("invalid local CM formal logarithm degree")
    c=[Fraction(0) for _ in range(degree+1)]
    for j in range((degree-1)//4+1):
        n=4*j+1
        c[n]=Fraction(comb(2*j,j), 4**j*n)
    return tuple(c)


def first_honda_coordinate_jet(prime:int, unit:int)->Fraction:
    """Degree p^2 of strict coordinate h: l_H(h)=l_E, l_H=T+unit*T^(p^2)/p+...

    This is ONLY the first potentially nonintegral coordinate coefficient.
    An integral first jet does not imply an integral full coordinate change.
    """
    from math import isqrt
    if prime<3 or prime%4!=3 or any(prime%d==0 for d in range(2,isqrt(prime)+1)):
        raise PeriodSourceError("expected genuine inert prime")
    if unit not in (-1,1):
        raise PeriodSourceError("Honda sign unit must be +1 or -1")
    return lemniscate_formal_log_coefficients(prime*prime)[prime*prime]-Fraction(unit,prime)


def signed_honda_coordinate_truncation(prime:int, unit:int, degree:int)->tuple[Fraction,...]:
    """Strict coordinate l_H(h)=l_E mod T^(degree+1) for degree<p^4.

    l_H(z)=z + unit*z^(p^2)/p in this finite range. This finite check
    does NOT prove an integral full-coordinate isomorphism.
    """
    from observational_succ.principia_formal_group import power_truncated
    first_honda_coordinate_jet(prime,unit)  # checks genuine inert prime/sign
    if not isinstance(degree,int) or degree<1 or degree>=prime**4:
        raise PeriodSourceError("unsupported degree; higher p-typical Honda terms required")
    ell=lemniscate_formal_log_coefficients(degree)
    h=[Fraction(0)]*(degree+1)
    h[1]=Fraction(1)
    for n in range(2,degree+1):
        h[n]=ell[n]-Fraction(unit,prime)*power_truncated(h,prime*prime,n)[n]
    return tuple(h)
