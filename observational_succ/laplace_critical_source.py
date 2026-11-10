"""Source-authenticated BBP Laplace response, critical h~t^-2, and signed CRT overlap.

Research-only: fixed-h Abel boundary/Weyl cancellation remains OPEN.
The continuous source Laplace density and critical source-only boundary are
not normality certificates. Uses the canonical unchanged duck_bbp.forcing.
"""
from __future__ import annotations

from cmath import exp as cexp
from fractions import Fraction
from math import exp, expm1, pi, sqrt
from observational_succ.duck_bbp import forcing
from observational_succ.adelic_additive_gluing import local_additive_fraction as p_fractional_part


def _nat(n: int, name: str, start: int=0) -> int:
    if type(n) is not int or n < start:
        raise ValueError(f'{name}: integer >= {start} required')
    return n


def source_laplace_moment(n: int) -> Fraction:
    """Exact integral_0^1 t^(8n-8)(4-2t^3-t^4-t^5)dt."""
    _nat(n, 'n', 1)
    return (Fraction(4,8*n-7)-Fraction(2,8*n-4)
            -Fraction(1,8*n-3)-Fraction(1,8*n-2))


def density_polynomial(t: Fraction) -> Fraction:
    """Positive source density on 0<=t<=1; no empirical smoothing."""
    if not isinstance(t, Fraction) or not 0 <= t <= 1:
        raise ValueError('t must be Fraction in [0,1]')
    return 2*(1-t**3)+(1-t**4)+(1-t**5)


def asymptotic_leading() -> Fraction:
    """Exact a = 15/64 from the first nonvanishing pole moment."""
    return Fraction(15,64)


def source_tail_from_r(n: int, depth: int) -> tuple[Fraction,Fraction]:
    """Positive future Green correction and explicit safe omitted tail bound.

    This is a deliberately standalone research check, not a replacement for
    the canonical tighter duck_bbp.tail_interval.
    """
    _nat(n,'n');_nat(depth,'depth')
    lo=sum((forcing(n+j)/16**j for j in range(1,depth+1)),Fraction())
    hi=lo + Fraction(47,225*(n+depth+1)**2*16**depth)
    return lo,hi


def lifted_phases(count: int, seed: Fraction=Fraction(0)) -> tuple[Fraction,...]:
    """Exact reduced REAL phase sequence; unwrapped p-adic history is separate."""
    _nat(count,'count');
    if not isinstance(seed,Fraction): raise ValueError('rational seed required')
    x=seed%1
    out=[x]
    for n in range(1,count+1):
        x=(16*x+forcing(n))%1
        out.append(x)
    return tuple(out)


def ward_phase_residual(phases: tuple[Fraction,...], h: int, n: int) -> Fraction:
    """Exact root-of-unity exponent residual: phase at n+1 minus Ward RHS mod1."""
    _nat(n,'n');
    if n+1>=len(phases): raise ValueError('need n+1 phase')
    if type(h) is not int: raise ValueError('integer character required')
    return (h*phases[n+1]-16*h*phases[n]-h*forcing(n+1))%1


def source_twist(t: float, h: int, cutoff: int) -> complex:
    """Finite partial t sum e^-tn (e(h r(n+1))-1); no infinite certificate.

    Tail after cutoff bounded by 2*t*e^(-t cutoff)/(1-e^-t).
    Complex floating values are diagnostics only.
    """
    if not (t>0) or type(h) is not int: raise ValueError('t>0; h integer')
    _nat(cutoff,'cutoff',1)
    return sum((t*exp(-t*n)*(cexp(2j*pi*float((h*forcing(n+1))%1))-1)
                for n in range(cutoff)), 0j)


def source_twist_tail_bound(t: float, cutoff: int) -> float:
    if t<=0: raise ValueError('t>0')
    _nat(cutoff,'cutoff',0)
    return 2*t*exp(-t*cutoff)/(-expm1(-t))


def ward_boundary_bound(t: float, h: int) -> float:
    """For any seed: (1-e^-t)|E_h(e^-t)| <= min(2,(1-e^-t)(4+3sqrt(K))).

    K = (15*pi/32)*abs(h), using original r(n+1)<15/(64n^2) for n>=1.
    """
    if not t>0 or type(h) is not int: raise ValueError('t>0; h integer')
    if h == 0: return 0.
    return min(2.,-expm1(-t)*(4+3*sqrt(15*pi*abs(h)/32)))


def laplace_phase_overlap(
        p_part: tuple[complex,...], complement: tuple[complex,...],
        tau: float=0.) -> tuple[complex,complex]:
    """Direct signed Laplace epoch and exact finite cyclic cross-spectrum.

    All cross terms retained; use at genuine BBP epoch only after the source
    components are authenticated. No prime independence or normality claim.
    """
    if len(p_part)!=len(complement) or not p_part or tau<0:
        raise ValueError('two same-length nonempty profiles; tau>=0')
    a=len(p_part)
    weighted=[exp(-tau*j/a)*complement[j] for j in range(a)]
    direct=sum((p_part[j]*weighted[j] for j in range(a)),0j)/a
    ahat=[sum((p_part[j]*cexp(-2j*pi*k*j/a) for j in range(a)),0j)/a
          for k in range(a)]
    bhat=[sum((weighted[j]*cexp(-2j*pi*k*j/a) for j in range(a)),0j)/a
          for k in range(a)]
    overlap=sum((ahat[k]*bhat[-k%a] for k in range(a)),0j)
    return direct,overlap


def laplace_epoch_zero_error(tau: float) -> float:
    """|unweighted mean - Laplace window| <= tau/2, for |a_n|<=1, tau>=0."""
    if tau<0: raise ValueError('tau>=0')
    return tau/2


def source_renormalized_moment(N: int) -> Fraction:
    """D_N=sum_{n<=N}(n*r(n)-a/n), exact rational.

    D_inf exists with |D_inf-D_N| <= (151/512)/N + 1/(2*N^2)
    for N>=2 from the frozen four-pole second and third coefficients.
    Sharp partial sums instead have finite part D_inf + a*EulerGamma.
    """
    _nat(N,'N',1)
    a=Fraction(15,64)
    return sum((n*forcing(n)-a/n for n in range(1,N+1)),Fraction())


def source_renormalized_tail_bound(N: int) -> Fraction:
    """Absolute error budget for the source's Abel/Gamma finite part, N>=2."""
    _nat(N,'N',2)
    return Fraction(151,512*N)+Fraction(1,2*N*N)


def signed_overlap_certificate(
        p_part: tuple[complex,...], complement: tuple[complex,...],
        cutoff: int, tau: float=0.) -> dict[str,float|complex]:
    """Finite signed time-spectrum gate, with a rigorous algebraic form.

    If |p_part|=|complement|=1 and max normalized prefix of p_part <=E,
    low time modes |k|<=K contribute <=sqrt(2K+1) E (1+2pi*K),
    and high modes <=sqrt(sum_(|k|>K)|b_tau_hat(k)|^2).
    Computed floats are diagnostics, not interval certificates.
    """
    n=len(p_part)
    if n!=len(complement) or n<3 or type(cutoff) is not int or not 0<=cutoff<(n-1)//2 or tau<0:
        raise ValueError('equal nonempty profiles; 0<=cutoff<(n-1)//2; tau>=0')
    if any(abs(abs(z)-1)>1e-10 for z in p_part+complement):
        raise ValueError('unit characters required')
    weighted=[exp(-tau*j/n)*complement[j] for j in range(n)]
    fa=[sum((p_part[j]*cexp(-2j*pi*k*j/n) for j in range(n)),0j)/n
        for k in range(n)]
    fb=[sum((weighted[j]*cexp(-2j*pi*k*j/n) for j in range(n)),0j)/n
        for k in range(n)]
    low=[k for k in range(n) if min(k,n-k)<=cutoff]
    high=[k for k in range(n) if min(k,n-k)>cutoff]
    low_value=sum((fa[k]*fb[-k%n] for k in low),0j)
    high_value=sum((fa[k]*fb[-k%n] for k in high),0j)
    pre=0j
    bound=0.
    for z in p_part:
        pre+=z
        bound=max(bound,abs(pre)/n)
    low_upper=sqrt(2*cutoff+1)*bound*(1+2*pi*cutoff)
    high_upper=sqrt(sum(abs(fb[k])**2 for k in high))
    return {'signed_total':low_value+high_value,'signed_low':low_value,
            'signed_high':high_value,'prefix_average_cap':bound,
            'low_upper':low_upper,'high_upper':high_upper,
            'combined_upper':low_upper+high_upper}
