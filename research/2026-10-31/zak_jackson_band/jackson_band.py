"""Exact finite arithmetic for the SUCC flat-top Zak/Jackson alias band.

Mathematical inequalities for the infinite real Green kernel are proved in
PROOFS.md.  Finite functions use exact fractions/integers and do not
claim a pi-normality proof or certified oscillatory quadrature.
"""
from __future__ import annotations

from fractions import Fraction
from math import comb


def four_pole(t: Fraction | int) -> Fraction:
    """Original four signed BBP poles, no modified coefficients or seed."""
    x = Fraction(t)
    if x < 1:
        raise ValueError('Original r domain is x>=1')
    return Fraction(4, 1) / (8*x-7) - Fraction(2, 1) / (8*x-4) - 1/(8*x-3) - 1/(8*x-2)


def four_pole_combined(t: Fraction | int) -> Fraction:
    """Independent combined numerator/denominator for the same rational source."""
    x = Fraction(t)
    if x < 1:
        raise ValueError('Original r domain is x>=1')
    return (120*x*x-89*x+16) / ((2*x-1)*(4*x-1)*(8*x-7)*(8*x-3))


def original_u_prefix(count: int) -> tuple[Fraction, ...]:
    if type(count) is not int or count < 0:
        raise ValueError('Nonnegative integral horizon required')
    out = [Fraction(0)]
    for n in range(1, count+1):
        out.append(16*out[-1]+four_pole(n))
    return tuple(out)


def green_interval(t: int | Fraction, terms: int) -> tuple[Fraction, Fraction]:
    """Exact interval for T(t)=sum_{j>=1}16^-j r(t+j), t>=0.

    Positivity and monotonicity of r imply remainder <16^-terms*r(t+terms+1)/15.
    """
    x = Fraction(t)
    if x < 0 or type(terms) is not int or terms < 1:
        raise ValueError('t>=0 and terms>=1 required')
    partial = sum((four_pole(x+j)/16**j for j in range(1, terms+1)), Fraction())
    tail_upper = four_pole(x+terms+1) / (15*16**terms)
    return partial, partial+tail_upper


def green_telescoping_defect(t: Fraction | int, terms: int) -> Fraction:
    """Exact 16T_J(t)-T_J(t+1)-r(t+1) = -16^-J*r(t+J+1)."""
    x = Fraction(t)
    low, _ = green_interval(x, terms)
    nxt, _ = green_interval(x+1, terms)
    return 16*low-nxt-four_pole(x+1)


def triangular_coefficient(length: int, index: int) -> int:
    """Coefficient of |sum_{j=0}^{L-1} z^j|^2 at z^index."""
    if type(length) is not int or length < 2 or type(index) is not int:
        raise ValueError('length>=2, integer index')
    return max(0, length-abs(index))


def fourth_coefficients(length: int) -> dict[int, int]:
    """Exact |D_L|^4 coefficients via *two triangular convolutions*."""
    if type(length) is not int or not 2 <= length <= 1024:
        raise ValueError('Finite coefficient budget: 2<=L<=1024')
    t = {k: length-abs(k) for k in range(-length+1, length)}
    out = {}
    for k in range(-2*length+2, 2*length-1):
        out[k] = sum(v*t.get(k-j, 0) for j,v in t.items())
    return out


def exact_fourth_normalizer(length: int) -> int:
    if type(length) is not int or length < 2:
        raise ValueError('length>=2')
    return length*(2*length*length+1)//3


def flat_top_coefficients(length: int) -> dict[int, Fraction]:
    """K_L=|D_L|^4/L^4 * D_{3L}^{sym}; nonnegative rational spectrum.

    c_l=1 for |l|<=L+2; c_l=0 for |l|>5L-2, and 0<=c_l<=1.
    """
    a = fourth_coefficients(length)
    width = 2*length-2
    b = {k: Fraction(v, length**4) for k,v in a.items()}
    out = {}
    for freq in range(-5*length+2, 5*length-1):
        lo = max(-width, freq-3*length)
        hi = min(width, freq+3*length)
        out[freq] = sum((b[k] for k in range(lo, hi+1)), Fraction()) if lo <= hi else Fraction()
    return out


def flat_top_coefficient(length: int, freq: int) -> Fraction:
    """Direct coefficient without materializing the whole array (finite small L)."""
    if type(freq) is not int:
        raise ValueError('Integral frequency required')
    if abs(freq)<=length+2:
        return Fraction(1)
    if abs(freq)>5*length-2:
        return Fraction(0)
    d4 = fourth_coefficients(length)
    return Fraction(sum(v for k,v in d4.items() if abs(freq-k)<=3*length),length**4)


def ideal_linear_ladder_weights(count: int, depth: int) -> tuple[Fraction, ...]:
    """Exact output weights of *ideal toy* e(16^n s), using flat-top K.

    n=1,...,count, cutoff L=16^depth. This symbolic statement is valid at
    any depth; it is not an exact model of the nonlinear authentic BBP lift.
    """
    if not all(type(v) is int for v in (count, depth)) or not 1 <= depth <= count:
        raise ValueError('Need positive integer depth<=count')
    L = 16**depth
    return tuple(Fraction(int(n<=depth)) for n in range(1,count+1))


def analytic_constant_bound(h: int) -> Fraction:
    """Purely rational upper estimate on uniform theorem constant (<99|h|).

    Uses 3<pi<22/7, 8/3<log16<3, 3/16<=q<=1/4.
    Does not replace analytic proof of kernel localization in PROOFS.md.
    """
    if type(h) is not int or h==0:
        raise ValueError('Nonzero integer harmonic')
    a=abs(h)
    return Fraction(2926,35)*a + Fraction(1,1024) + 15 + Fraction(7,60*a)


def guaranteed_band_error(h: int) -> int:
    """Theorem bound |band_{N,16^M}-S_M|<99|h|, N>=M>=1."""
    if type(h) is not int or h==0:
        raise ValueError('Nonzero integer harmonic')
    return 99*abs(h)


def coherent_high_alias_lower_bound(full_horizon: int, depth: int, h: int) -> Fraction:
    """Strict lower bound on unfiltered complement for fixed q=1/5.

    Uses the inherited global true BBP Green tail mass <1/32 and pi<22/7.
    The result may be negative: that means the finite lower bound is vacuous.
    """
    if type(full_horizon) is not int or type(depth) is not int or not 1 <= depth <= full_horizon:
        raise ValueError('1<=depth<=full_horizon')
    if type(h) is not int or h == 0:
        raise ValueError('Nonzero integer harmonic')
    return Fraction(full_horizon-depth) - Fraction(99*abs(h)) - Fraction(11*abs(h),56)


def horizontal_action_coefficient(epsilon: Fraction | int, periods: int) -> Fraction:
    """For Q(t)=q+eps*sin(2*pi*t), action on [0,periods] is
    (2*pi**2) * (returned exact rational coefficient).

    This is an analytic identity, not a numerical evaluation of pi.
    The condition of FINITE total action on [0,infty) selects eps=0.
    """
    e=Fraction(epsilon)
    if type(periods) is not int or periods<0:
        raise ValueError('Nonnegative integer periods required')
    return periods*e*e


def stationary_band_gap_lower(n: int) -> int:
    """Strict lower bound on U'(n+1-1/4)-U'(n+1/4), all canonical q.

    The actual gap is >3*16**n-1, by the original monotone Green derivative.
    """
    if type(n) is not int or n < 1:
        raise ValueError('Positive integer cell required')
    return 3*16**n-1


def pair_derivative_lower(m: int) -> Fraction:
    """Uniform lower for U'(m+t)-U'(n+t), m>n>=1, |t|<=1/4."""
    if type(m) is not int or m<2:
        raise ValueError('Upper cell index >=2 required')
    return Fraction(16**m,8)


def continuous_slice_error_upper_rational(h: int) -> Fraction:
    """Strict rational upper for |int|Z(t,0)|^2 - N*int psi^2|.

    Paper proof gives <8/(75*pi*|h|)<8/(225*|h|).
    """
    if type(h) is not int or h==0:
        raise ValueError('Nonzero integer harmonic')
    return Fraction(8,225*abs(h))
