"""Inertial relative-observer probes for the original, zero-seeded BBP source.

Exact Fraction arithmetic handles the four signed poles, unwrapped original
recurrence, temporal lags, and coordinate/seed kernels. Floating approximations
are DISPLAY-ONLY; infinite normality is not computationally certified here.

Companion paper: README.md. No modifications to the authentic source.
"""
from __future__ import annotations

from fractions import Fraction as Q
from math import cos, sin, pi

BASE=16
CHARGE=BASE-1

def _natural(n: int, name: str, *, minvalue: int=1, maxvalue: int=300):
    if type(n) is not int or not minvalue <= n <= maxvalue:
        raise ValueError(f'{name} must be an int in [{minvalue},{maxvalue}]')
    return n


def forcing(n: int) -> Q:
    """Original four signed BBP poles, r(n)>0, n>=1."""
    _natural(n,'source index',maxvalue=100000)
    return Q(4,8*n-7)-Q(2,8*n-4)-Q(1,8*n-3)-Q(1,8*n-2)


def original_orbit(seed: Q, horizon: int) -> tuple[Q,...]:
    _natural(horizon,'horizon',minvalue=0,maxvalue=300)
    if type(seed) is not Q:
        raise TypeError('seed must be exact Fraction')
    values=[seed]
    for n in range(1,horizon+1):
        values.append(BASE*values[-1]+forcing(n))
    return tuple(values)


def temporal_lag(values: tuple[Q,...], n: int, k: int=1) -> Q:
    _natural(n,'time',minvalue=0)
    _natural(k,'lag')
    if n+k>=len(values):
        raise IndexError('requested time and lag outside supplied orbit')
    return values[n+k]-values[n]


def source_lag(n: int,k: int=1) -> Q:
    """Exact original source contribution U_(n+k)-16^k U_n."""
    _natural(n,'time',minvalue=0)
    _natural(k,'lag',maxvalue=40)
    return sum((BASE**(k-j)*forcing(n+j) for j in range(1,k+1)),Q(0))


def projected_charge(n: int,k: int=1) -> int:
    _natural(n,'time',minvalue=0)
    _natural(k,'lag',maxvalue=40)
    return BASE**k-1


def bound_lag_source_alln(k: int=1) -> Q:
    """Proved upper bound on sum_(n>=1) R_(n,k), independent of seed.

    Uses r(n+j)<=15/(8n+1)^2 and sum_(n>=1)(8n+1)^-2
    <=1/81+int_1^infty (8x+1)^-2 dx =17/648.
    """
    _natural(k,'lag',maxvalue=40)
    return Q(17,648)*(BASE**k-1)


def finite_source_lag_budget(N: int,k: int=1) -> Q:
    _natural(N,'N',maxvalue=200)
    _natural(k,'lag',maxvalue=20)
    return sum((source_lag(n,k) for n in range(1,N+1)),Q(0))


def temporal_observation_kernel(first_time: int=0,k: int=1) -> int:
    """All-frequency exact relative phases identify seeds modulo 1/denom.

    For every n>=first_time, equality of lag-k phases means
    (16^k-1)*16^first_time*(s-t) is integer; equivalence preserved on future.
    """
    _natural(first_time,'first_time',minvalue=0,maxvalue=40)
    _natural(k,'lag',maxvalue=20)
    return (BASE**k-1)*BASE**first_time


def shifted_source_for_new_origin(r: Q, delta: Q) -> Q:
    """Constant coordinate translation V_n=U_n+delta requires r' = r-15delta."""
    if type(r) is not Q or type(delta) is not Q:
        raise TypeError('r and delta must be exact fractions')
    return r-CHARGE*delta


def circle_fraction(q: Q) -> Q:
    if type(q) is not Q:
        raise TypeError('circle phase must be Fraction')
    return q%1


def compatible_seed_suffix_shift(difference: Q, first_time: int) -> Q:
    """For a seed difference in the full relative kernel, return the constant suffix rotation."""
    if type(difference) is not Q:
        raise TypeError('seed difference must be exact')
    denominator=temporal_observation_kernel(first_time,1)
    if (difference*denominator).denominator != 1:
        raise ValueError('difference not in relative-observation kernel')
    return circle_fraction(BASE**first_time*difference)


def eisenstein_sigma_minus3(h: int) -> Q:
    _natural(h,'Fourier mode',maxvalue=300)
    return sum((Q(1,d**3) for d in range(1,h+1) if h%d==0),Q(0))


def eisenstein_coefficient(h: int,y: float=1.0) -> float:
    """Existing #375 positive primitive Eisenstein horizontal Fourier coefficient."""
    from math import exp
    if type(y) not in (float,int) or y <= 0:
        raise ValueError('height must be positive')
    _natural(h,'Fourier mode',maxvalue=300)
    return 45.0/(pi**3*y)*(1+2*pi*h*y)*exp(-2*pi*h*y)*float(eisenstein_sigma_minus3(h))


def _unit_phase(q: Q,h: int) -> complex:
    _natural(abs(h),'frequency')
    angle=2*pi*h*float(circle_fraction(q))
    return complex(cos(angle),sin(angle))


def characteristic(values: tuple[Q,...],h: int) -> complex:
    if not values:
        raise ValueError('nonempty phase sequence required')
    _natural(abs(h),'frequency')
    return sum((_unit_phase(v,h) for v in values),0j)/len(values)


def eisenstein_energy(values: tuple[Q,...],y: float=1.0,modes: int=12) -> float:
    """TRUNCATED, NUMERICAL display only (positive finite Fourier energy)."""
    _natural(modes,'modes',maxvalue=300)
    return 2*sum(eisenstein_coefficient(h,y)**2 * abs(characteristic(values,h))**2
                 for h in range(1,modes+1))


def relative_shifted_energy_bound_prefactor(y: float=1.0,k: int=1) -> float:
    """Rigorous algebraic analytic upper prefactor C_y(k) for |Erel-Eb-1|<=C_y/N.

    a_h <= c (1+alpha*h)exp(-alpha*h), c=45*zeta(3)/(pi^3*y).
    We avoid an unverified numerical zeta(3) bound by sum_(d>=1)d^-3<5/4.
    The bound uses 1<zeta(4), so c<=45*(5/4)/(pi^3*y).
    Valid for any positive y. No numeric interval proof is claimed for floating output.
    """
    from math import exp
    if type(y) not in (float,int) or y<=0:
        raise ValueError('height must be positive')
    _natural(k,'lag',maxvalue=40)
    alpha=2*pi*y
    q=exp(-2*alpha)
    sq1=q/(1-q)**2
    sq2=q*(1+q)/(1-q)**3
    sq3=q*(1+4*q+q*q)/(1-q)**4
    c=45*(5/4)/(pi**3*y)
    return float(8*pi*bound_lag_source_alln(k)*c*c*(sq1+2*alpha*sq2+alpha*alpha*sq3))


def displacements(values: tuple[Q,...],first_time: int=1,k: int=1,N: int | None=None) -> tuple[Q,...]:
    _natural(first_time,'first_time',minvalue=0)
    _natural(k,'lag')
    if N is None:
        N=len(values)-first_time-k
    _natural(N,'N')
    if first_time+N+k>len(values):
        raise IndexError('finite orbit horizon')
    return tuple(circle_fraction(values[n+k]-values[n]) for n in range(first_time,first_time+N))



def debiased_displacements(values:tuple[Q,...],first_time:int=1,N:int|None=None)->tuple[Q,...]:
    """Exact source-authenticated quotient observations 15*U_n mod 1.

    delta_n=(U_(n+1)-U_n) mod1, so delta_n-r(n+1)=15*U_n mod1.
    Requires actual original forcing tape (four-pole rational r).
    """
    _natural(first_time,'first_time',minvalue=0)
    if N is None:N=len(values)-first_time-1
    _natural(N,'N')
    if first_time+N+1>len(values):raise IndexError('horizon')
    return tuple(circle_fraction(values[n+1]-values[n]-forcing(n+1))
                 for n in range(first_time,first_time+N))


def projected_values(values: tuple[Q,...],first_time: int=1,k: int=1,N: int | None=None) -> tuple[Q,...]:
    _natural(first_time,'first_time',minvalue=0)
    _natural(k,'lag')
    if N is None:N=len(values)-first_time-k
    _natural(N,'N')
    if first_time+N+k>len(values):raise IndexError('horizon')
    m=BASE**k-1
    return tuple(circle_fraction(m*values[n]) for n in range(first_time,first_time+N))



def future_tail_interval(n: int, depth: int=8) -> tuple[Q,Q]:
    """Certified rational bounds for T_n=sum_(j>=1)16^-j r(n+j).

    r(n+j) decreases in j (positive original Laplace Q), hence
    remaining sum <= 16^-depth*r(n+depth+1)/15.
    """
    _natural(n,'source time',minvalue=0,maxvalue=300)
    _natural(depth,'depth',maxvalue=100)
    lower=sum((forcing(n+j)/BASE**j for j in range(1,depth+1)),Q(0))
    upper=lower+forcing(n+depth+1)/Q(15*BASE**depth)
    return lower,upper


def tail_simple_upper(n:int)->Q:
    """Original positive Oily Green kernel R(x)<=1-x on [0,1]."""
    _natural(n,'source time',minvalue=0,maxvalue=100000)
    return Q(1,(8*n+1)*(8*n+2))


def pi_over16_interval(depth:int=8)->tuple[Q,Q]:
    """Certified original BBP series + future Green tail, no external pi digits."""
    _natural(depth,'depth',maxvalue=100)
    partial=sum((forcing(j)/BASE**j for j in range(1,depth+1)),Q(0))
    return partial, partial+tail_simple_upper(depth)/BASE**depth


def telescoped_lag_budget(N:int,k:int=1)->Q:
    """Exact infinite-tail expression upper bounded using finitely many T_n.

    The sum_(n<=N) (T_n-T_(n+k)) is positive and <= sum_(n<=min(k,N))T_n
    for k<=N, and <=sum_(n<=N)T_n for k>=N. This routine gives a
    certified rational bound by summing the pointwise beta upper envelope.
    """
    _natural(N,'N',maxvalue=100000)
    _natural(k,'lag',maxvalue=100000)
    return sum((tail_simple_upper(n) for n in range(1,min(k,N)+1)),Q(0))


def all_lag_telescoping_bound()->Q:
    """For all k,N>=1, sum_(n<=N)(T_n-T_(n+k)) <17/648."""
    return Q(17,648)


def telescoped_fourier_error_budget(N:int,h:int,k:int=1)->float:
    """Uniform bound versus e(h(16^k-1)16^n alpha); display in floating units."""
    _natural(N,'N',maxvalue=100000)
    _natural(abs(h),'frequency',maxvalue=100000)
    _natural(k,'lag',maxvalue=100000)
    return 2*pi*abs(h)*float(telescoped_lag_budget(N,k))/N



def green_memory_closed_numeric()->float:
    """DISPLAY ONLY of exact source memory constant proved in README.

    sum_(n>=1)T_n = -pi/20 + sqrt(2)*pi/48
                       +log(2)/24 +sqrt(2)*log(1+sqrt(2))/24.
    Do not use this floating approximation as an interval certificate.
    """
    from math import sqrt,log
    return -pi/20+sqrt(2)*pi/48+log(2)/24+sqrt(2)*log(1+sqrt(2))/24


def green_memory_rational_interval(rows:int=30,depth:int=12)->tuple[Q,Q]:
    """Rigorous rational enclosure of sum_(n>=1)T_n.

    Remaining rows n>=rows+1 bounded by integral of (8n+1)^-2:
    sum_(n>rows)T_n<=sum_(n>rows)(8n+1)^-2
                  <=int_rows^infty(8x+1)^-2 dx=1/[8(8rows+1)].
    """
    _natural(rows,'rows',maxvalue=300)
    _natural(depth,'depth',maxvalue=100)
    pieces=[future_tail_interval(n,depth) for n in range(1,rows+1)]
    lower=sum((a for a,_ in pieces),Q(0))
    upper=sum((b for _,b in pieces),Q(0))+Q(1,8*(8*rows+1))
    return lower,upper


def exactly_uniform_grid_pushforward(q:int)->tuple[Q,...]:
    """Finite hostile control: a nonuniform 1/15-arc law pushed to q-grid by multiplication 15."""
    _natural(q,'grid points',maxvalue=1000)
    return tuple(circle_fraction(CHARGE*Q(j,CHARGE*q)) for j in range(q))

if __name__=='__main__':
    orbit=original_orbit(Q(0),33)
    for k in (1,2,3):
        for n in range(1,12):
            assert temporal_lag(orbit,n,k)==projected_charge(n,k)*orbit[n]+source_lag(n,k)
        print('EXACT_ORIGINAL_LAG_PASS',k,'infinite_source_budget<',bound_lag_source_alln(k))
    print('GAUGE_KERNEL_FIRST_TIME_0',temporal_observation_kernel(0))
    print('GAUGE_KERNEL_FIRST_TIME_1',temporal_observation_kernel(1))
    print('RELATIVE_PROBE_STDLIB_PASS')
