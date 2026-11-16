"""Research-only: original 4-pole BBP log-Green/Gamma windows.

No pi value/digit fixtures. The classical BBP pi equality is an imported
mathematical dependency; this module never infers digit equidistribution.
This is isolated research code, not an installed SUCC production module.
"""
from __future__ import annotations
from fractions import Fraction
import mpmath as mp


def source_r(n: int) -> Fraction:
    if not isinstance(n,int) or n < 1:
        raise ValueError('n must be a positive integer')
    return (Fraction(4, 8*n-7) - Fraction(2, 8*n-4)
            - Fraction(1, 8*n-3) - Fraction(1, 8*n-2))


def original_Q(t):
    return 4-2*t**3-t**4-t**5


def source_g(t):
    """Positive original BBP Green density; use cancellation-free denominator."""
    return (1-t)/((2-t*t)*(t*t-2*t+2))


def K(v):
    """v=-8 log(t): T_n = int exp(-n v) K(v) dv."""
    t=mp.exp(-mp.mpf(v)/8)
    # expm1 avoids cancellation in 1-exp(-v/8) near 0.
    one_minus_t=-mp.expm1(-mp.mpf(v)/8)
    return t*one_minus_t/(8*((2-t*t)*(t*t-2*t+2)))


def green_integral(n, dps: int=50):
    with mp.workdps(dps):
        return mp.quad(lambda y: mp.exp(-y)*K(y/mp.mpf(n))/n,
                       [0,1,5,20,80,mp.inf]) if n>0 else mp.quad(
                           lambda v: K(v), [0,1,5,20,80,mp.inf])


def green_series(n: int, count: int=32):
    if n<0 or count<0: raise ValueError('nonnegative n and count required')
    return sum((source_r(n+j)/16**j for j in range(1,count+1)),Fraction(0))


def fractional_window(n: int, xi=0, beta=0, dps: int=55):
    """F_n(xi,beta): exact complex fractional-step and log-scale integral."""
    if n < 1: raise ValueError('n must be >=1')
    with mp.workdps(dps):
        w=mp.mpc(1,xi)
        beta=mp.mpc(beta)
        if mp.re(beta)<=-2: raise ValueError('Re beta > -2 is required')
        def integrand(y):
            v=y/mp.mpf(n)
            return (mp.exp(-w*y)*(-mp.expm1(-v))**beta*K(v)/n)
        return +mp.quad(integrand,[0,1,5,20,80,mp.inf])


def window_asymptotic(n: int, xi=0, beta=0, order=2, dps=55):
    """Asymptotic to O(n^-order-1) in normalized scale, 0<=order<=2."""
    if order not in (0,1,2): raise ValueError('order must be 0,1,2')
    with mp.workdps(dps):
        beta=mp.mpc(beta)
        w=mp.mpc(1,xi)
        value=mp.gamma(beta+2)/w**(beta+2)
        if order>=1:
            value-= (8*beta+7)/16 * mp.gamma(beta+3)/(n*w**(beta+3))
        if order>=2:
            value+= (48*beta**2+100*beta+55)/384 *mp.gamma(beta+4)/(n*n*w**(beta+4))
        return +(value/(64*mp.power(n,beta+2)))


def four_time_window(n:int,q:int,ell:int=2,xi=0,beta=0,dps:int=55):
    if n<1 or q<1 or ell<1: raise ValueError('n,q,ell must be positive')
    with mp.workdps(dps):
        beta=mp.mpc(beta);w=mp.mpc(1,xi)
        if mp.re(beta)<=-2: raise ValueError('Re beta > -2 required')
        def integrand(y):
            v=y/mp.mpf(n)
            return (mp.exp(-w*y)*(-mp.expm1(-q*v))*(-mp.expm1(-ell*v))
                    *(-mp.expm1(-v))**beta*K(v)/n)
        return +mp.quad(integrand,[0,1,5,20,80,mp.inf])


def four_time_limit(n,q,ell=2,xi=0,beta=0,regime='proportional',dps=55):
    """Leading asymptotics in either q/n finite or q/n -> infinity regimes.

    regime='saturated': q/n -> infinity; 'proportional': q/n -> c>0;
    'sublinear': q/n -> 0 (includes fixed q).
    """
    with mp.workdps(dps):
        w=mp.mpc(1,xi); beta=mp.mpc(beta)
        if regime=='sublinear':
            return +(q*ell*mp.gamma(beta+4)/(64*mp.power(n,beta+4)*w**(beta+4)))
        s=beta+3
        factor=mp.power(w,-s) if regime=='saturated' else (mp.power(w,-s)-mp.power(w+mp.mpf(q)/n,-s))
        return +(ell*mp.gamma(s)*factor/(64*mp.power(n,s)))


def scale_log_character(n:int,xi=0,omega=0,dps=55):
    """Source-conditioned E[exp(-i xi Y) Y^(i omega)], Y=-8n log X.

    This differs from the raw (1-t^8)^(i omega) fractional-difference
    character; the change of reference is deliberately explicit.
    """
    with mp.workdps(dps):
        w=mp.mpc(1,xi); omega=mp.mpf(omega)
        def numerator(y):
            v=y/mp.mpf(n)
            return mp.exp(-w*y)*mp.power(y,1j*omega)*K(v)/n
        val=mp.quad(numerator,[0,1,5,20,80,mp.inf])
        return +(val/green_integral(n,dps=dps))


def gamma_log_target(xi=0,omega=0,dps=55):
    with mp.workdps(dps):
        return +(mp.gamma(2+1j*omega)/(1+1j*xi)**(2+1j*omega))


def tv_budget(n:int,dps=55):
    with mp.workdps(dps):
        if n < 1: raise ValueError('n>=1')
        Z=64*n*n*green_integral(n,dps=dps)
        return +(1-Z), +(mp.mpf(7)/(8*n))
