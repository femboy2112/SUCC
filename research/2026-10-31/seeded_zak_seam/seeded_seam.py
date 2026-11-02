"""Exact finite SUCC arithmetic/continuum seam diagnostics.

No π-normality assertion. All source arithmetic uses Fraction; Zak tests use
Gaussian integer sample coefficients, not numerical phases pretending proof.
"""
from __future__ import annotations

from fractions import Fraction
from math import comb


def require_int(n: int, low: int, name: str) -> None:
    if type(n) is not int or n < low:
        raise ValueError(f"{name} must be integer >= {low}")


def require_fraction(x, low: int, name: str) -> Fraction:
    if type(x) not in (Fraction, int):
        raise ValueError(f"{name} requires an integer or exact Fraction")
    x = Fraction(x)
    if x < low:
        raise ValueError(f"{name} must be >= {low}")
    return x


def four_pole(t: Fraction | int) -> Fraction:
    """Original unmodified four-pole source at exact t>=1."""
    t = require_fraction(t, 1, "t")
    return (Fraction(4, 1) / (8*t-7)
            -Fraction(2, 1) / (8*t-4)
            -Fraction(1, 1) / (8*t-3)
            -Fraction(1, 1) / (8*t-2))


def positive_edge_source(t: Fraction | int) -> Fraction:
    """Independent three-positive-edge regrouping of the SAME four poles."""
    t = require_fraction(t, 1, "t")
    a = 8*t-7
    return (2*(1/a-1/(a+3))
            +(1/a-1/(a+4))
            +(1/a-1/(a+5)))


def zero_seed_states(n: int) -> tuple[Fraction, ...]:
    require_int(n, 0, "n")
    states = [Fraction(0)]
    for k in range(1,n+1):
        states.append(16*states[-1]+four_pole(k))
    return tuple(states)


def finite_tail(x: Fraction | int, terms: int) -> Fraction:
    x = require_fraction(x, 0, "x")
    require_int(terms, 0, "terms")
    return sum((Fraction(1,16**j)*four_pole(x+j)
                for j in range(1,terms+1)), Fraction(0))


def finite_transport_defect(x: Fraction | int, terms: int) -> Fraction:
    """Exact: 16 T_J(x)-T_J(x+1)-r(x+1)=-16**(-J)r(x+J+1)."""
    x = require_fraction(x, 0, "x")
    require_int(terms, 0, "terms")
    return 16*finite_tail(x,terms)-finite_tail(x+1,terms)-four_pole(x+1)


def alpha_enclosure(terms: int) -> tuple[Fraction,Fraction]:
    """Exact strict source monotonicity certificate for alpha=pi/16.

    alpha_K < alpha < alpha_K + 16**(-K)*r(K+1)/15.
    """
    require_int(terms, 1, "terms")
    lower = finite_tail(0,terms)
    return lower, lower + Fraction(1,15*16**terms)*four_pole(terms+1)


def finite_past_future_seam(n: int, horizon: int) -> tuple[Fraction,Fraction]:
    """The two coordinates are IDENTICAL exact Fractions for 0<=n<=horizon."""
    require_int(horizon, 0, "horizon")
    require_int(n, 0, "n")
    if n>horizon:
        raise ValueError("n must not exceed horizon")
    q_h=finite_tail(0,horizon)
    u=zero_seed_states(n)[-1]
    return Fraction(16**n)*q_h-u, finite_tail(n,horizon-n)


def periodic_quarter_grid_defect(j:int, quarter:int, amplitude:Fraction|int)->Fraction:
    """Exact epsilon*16^(j+quarter/4)*sin(2*pi*(j+quarter/4)).

    At quarter-grid t=j+k/4: 16^t=16^j*2^k,
    and the sine belongs to {0,1,0,-1,0}. No floating approximation.
    """
    require_int(j, 0, "j")
    if type(quarter) is not int or not 0 <= quarter <= 4:
        raise ValueError("quarter must be an integer from 0 through 4")
    if type(amplitude) not in (Fraction,int):
        raise ValueError("exact amplitude required")
    return Fraction(amplitude)*(16**j)*(2**quarter)*(0,1,0,-1,0)[quarter]


def periodic_quarter_defect(j:int, amplitude:Fraction|int)->Fraction:
    """For Q(x)=alpha+epsilon sin(2πx), delta U(j+1/4)=2*16**j*epsilon.

    All integer-time defects are identically zero. This is an exact identity,
    not a numerical evaluation of pi or a sine implementation.
    """
    return periodic_quarter_grid_defect(j, 1, amplitude)


def zak_integer_corner(samples:tuple[complex,...], shift:int, frequency_quarter:int)->complex:
    """Z(shift,p/4) using exact Gaussian-integer sample phases only.

    samples[j-1]=g(j), nonzero only for 1<=j<=len(samples).
    """
    if not isinstance(samples,tuple) or not samples:
        raise ValueError("nonempty tuple required")
    if type(shift) is not int or type(frequency_quarter) is not int:
        raise ValueError("integer shift/frequency required")
    roots=(1+0j,0-1j,-1+0j,0+1j)
    return sum((v*roots[((j-shift)*frequency_quarter)%4]
                for j,v in enumerate(samples,start=1)),0+0j)


def compact_polynomial_bump_l2(power:int=4)->Fraction:
    """Integral of (1-16x²)^(2*power) over x in [-1/4,1/4].

    The bump itself is (1-16x²)^power inside and zero outside;
    power>=3 yields C^2, sufficient for absolutely summable aliases.
    """
    require_int(power,3,"power")
    return Fraction(1,2)*sum((Fraction((-1)**j*comb(2*power,j),2*j+1)
                for j in range(2*power+1)), Fraction(0))


def global_zak_energy(number_of_bumps:int,power:int=4)->Fraction:
    """For disjoint window bumps and unit-modulus phase, ||Z||_2²=N ||psi||_2².

    This is SEED BLIND; no result about the point seam S_N follows.
    """
    require_int(number_of_bumps,0,"number_of_bumps")
    return number_of_bumps*compact_polynomial_bump_l2(power)
