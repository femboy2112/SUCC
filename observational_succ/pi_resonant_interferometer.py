"""Pointed BBP phase-collision probes (research; not a proof of pi normality).

Source passport: ORIGINAL four signed BBP poles, U_0=0, sixteen-fold
successor. Everything here is classical arithmetic/measurement *model*.
The probability of a simulated click is supplied by an explicit observation
channel and is NOT an intrinsic randomness of pi or a physical qubit gate.

No approximate float is a proof certificate. Rational Machin/Taylor intervals
implement finite rigorous click-probability enclosures.
"""
from __future__ import annotations

from fractions import Fraction as F
from math import factorial


def _nat(v: int, *, least: int = 0) -> int:
    if type(v) is not int or v < least:
        raise ValueError(f"Expected exact integer >= {least}")
    return v


def forcing(n: int) -> F:
    _nat(n, least=1)
    return F(4, 8*n-7)-F(2, 8*n-4)-F(1, 8*n-3)-F(1, 8*n-2)


def forcing_leading_bounds(n: int) -> tuple[F, F, F]:
    """For n>=2, 0<r(n)-15/(64 n²)<1/n³; paper proof by shifted polynomials."""
    _nat(n, least=2)
    residual=forcing(n)-F(15,64*n*n)
    assert F(0)<residual<F(1,n**3)
    return forcing(n), F(15,64*n*n), residual


def state(n: int, seed: F = F(0)) -> F:
    """Exact original source state. Other rational seeds only for labelled controls."""
    _nat(n)
    if type(seed) not in (int,F):
        raise ValueError("Symbolic/nonrational seeds require separate source type")
    u=F(seed)
    for j in range(1,n+1):
        u=16*u+forcing(j)
    return u


def source_innovation(n: int, ell: int) -> F:
    _nat(n)
    _nat(ell,least=1)
    val=F(0)
    for j in range(1,ell+1):
        val=16*val+forcing(n+j)
    return val


def innovation_leading(n: int,ell: int) -> tuple[F,F,F]:
    """Delta approx (16^ell-1)/(64 n²), abs error <= 16^ell/(10 n³)."""
    _nat(n,least=2); _nat(ell,least=1)
    lead=F(16**ell-1,64*n*n)
    cap=F(16**ell,10*n**3)
    actual=source_innovation(n,ell)
    assert abs(actual-lead)<=cap
    return actual,lead,cap


def critical_lag(n: int) -> int:
    """Nearest integer logarithmic resonance: 16^ell/(64 n²) in [1/4,4]."""
    _nat(n,least=2)
    target=64*n*n
    k=0
    while 16**(k+1)<=target:
        k+=1
    return k if target*target <= 16**(2*k+1) else k+1


def same_mode_lag_phase(n: int,ell: int,h: int=1,seed: F=F(0)) -> F:
    """THE source-sensitive lag: (U_(n+ell)-U_n) mod1, frequency held fixed."""
    _nat(n);_nat(ell,least=1)
    if type(h) is not int or h==0:raise ValueError("Nonzero integer harmonic")
    return (h*((16**ell-1)*state(n,seed)+source_innovation(n,ell)))%1


def compensated_phase(n: int,ell:int,h:int=1,seed:F=F(0)) -> F:
    """Seed-BLIND compensated lag; cannot alone prove original-source cancellation."""
    _nat(n); _nat(ell,least=1)
    if type(h) is not int or h==0:raise ValueError("Nonzero integer harmonic")
    return (h*(state(n+ell,seed)-16**ell*state(n,seed)))%1


def _atan_interval(q: int, terms:int) -> tuple[F,F]:
    _nat(q,least=2);_nat(terms,least=1)
    partial=sum((F((-1)**k,(2*k+1)*q**(2*k+1)) for k in range(terms)),F(0))
    next_term=F((-1)**terms,(2*terms+1)*q**(2*terms+1))
    return min(partial,partial+next_term),max(partial,partial+next_term)


def pi_interval(terms:int=14) -> tuple[F,F]:
    """Classical Machin pi=16 atan(1/5)-4 atan(1/239); alternating enclosures."""
    a,b=_atan_interval(5,terms),_atan_interval(239,terms)
    return 16*a[0]-4*b[1],16*a[1]-4*b[0]


def _center(q:F) -> F:
    r=q%1
    return r if r<=F(1,2) else r-1


def click_phase_interval(phi: F, terms_pi:int=14, terms_cos:int=12) -> tuple[F,F]:
    """Rigorous P(click | phase)=sin²(pi*phi), exact rational interval.

    Mathematically a Hadamard phase-to-click instrument, not a supplied
    physical gate. The derivative wrt pi is bounded by |centered phi|.
    """
    _nat(terms_pi,least=1); _nat(terms_cos,least=1)
    if type(phi) not in (F,int):raise ValueError("Exact rational phase only")
    q=_center(F(phi))
    pl,pu=pi_interval(terms_pi)
    pm=(pl+pu)/2
    t=2*pm*q
    cos_approx=sum(((-1)**k*t**(2*k)/factorial(2*k) for k in range(terms_cos+1)),F(0))
    cos_err=abs(t)**(2*terms_cos+2)/factorial(2*terms_cos+2)
    p=(1-cos_approx)/2
    err=cos_err/2+abs(q)*(pu-pl)/2
    return max(F(0),p-err), min(F(1),p+err)


def click_interval(n:int,h:int=1,*,completed:bool=True,terms_pi:int=14,terms_cos:int=12) -> tuple[F,F]:
    """Exact interval for the authentic original U_n or completed 16^n*pi/16."""
    _nat(n)
    if type(h) is not int or h==0:raise ValueError("Nonzero integer harmonic")
    lo,hi=click_phase_interval((h*state(n))%1,terms_pi,terms_cos)
    if completed:
        _,pihi=pi_interval(terms_pi)
        err=pihi*abs(h)*forcing(n+1)/15  # T_n < r(n+1)/15, derivative |dp/dz|<=pi |h|
        return max(F(0),lo-err),min(F(1),hi+err)
    return lo,hi


def shell_click_interval(B:int,h:int=1,*,completed:bool=True,terms_pi:int=14,terms_cos:int=12) -> tuple[F,F]:
    """Finite B-shell *only*. No all-B bound/normality inference is made."""
    _nat(B,least=1)
    seq=[click_interval(n,h,completed=completed,terms_pi=terms_pi,terms_cos=terms_cos)
         for n in range(B,2*B)]
    return sum((p[0] for p in seq),F(0))/B,sum((p[1] for p in seq),F(0))/B


def inverse_propensity_expectation(outcomes:tuple[F,...],policy:tuple[F,...]) -> F:
    """E[Y/(B*pi(A))] = mean outcome probability; policy known and >0."""
    B=len(outcomes)
    if not B or len(policy)!=B or any(type(p) not in (int,F) for p in policy) or any(F(p)<=0 for p in policy):
        raise ValueError("Full-support finite probability policy")
    if sum(map(F,policy),F(0))!=1:raise ValueError("Policy not normalized")
    if any(type(q) not in (int,F) or not 0<=F(q)<=1 for q in outcomes):
        raise ValueError("Lawful binary potential outcome probabilities")
    return sum((F(policy[i])*F(outcomes[i])/(B*F(policy[i])) for i in range(B)),F(0))


def collision_phase_table(phases:tuple[F,...],h:int=1)->tuple[tuple[F,...],...]:
    """For iid uniform I,J, phases of e(h(U_I-U_J)); exact QQ/Z grid."""
    if not phases or type(h) is not int or h==0:raise ValueError("Nonempty phases and harmonic")
    if any(type(q) not in (int,F) for q in phases):raise ValueError("Exact phases")
    return tuple(tuple((h*(q-r))%1 for r in phases) for q in phases)


def source_click_probability_rational_control(x:F,h:int=1)->tuple[F,F]:
    """Single phase control for rational base-16 orbit points x; not pi."""
    if type(x) not in (F,int) or type(h) is not int or h==0:
        raise ValueError("Exact rational source control")
    return click_phase_interval((h*F(x))%1)


def gamma_depth_two_one_sided_factor() -> tuple[F,F]:
    """(1+i)^(-2) = -i/2, (real,imag); a physical model, not BBP physics."""
    return F(0),-F(1,2)
