"""SUCC source/seed classification; exact finite rational arithmetic only.

Source model: polynomial g rational, rational initial seed s; BBP forcing
r_g(n) = integral_0^1 z^(8n-8) g(z) dz.

The symbolic seed module Q + Q*x, x=pi/16, is *not* the rational finite
carrier. Classification of normality across Q+Q*x imports D.D. Wall's
classical rational affine normality theorem; this code does NOT decide pi
normality, compute a true infinite seed, or construct a proof of it.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction

Q = Fraction
G_PI = (Q(4), Q(0), Q(0), Q(-2), Q(-1), Q(-1))


def exact(v):
    if type(v) not in (int, Q):
        raise TypeError("Only exact rational data are admitted")
    return Q(v)


def polynomial(coefficients):
    values = tuple(exact(v) for v in coefficients)
    if not values:
        raise ValueError("Polynomial needs at least one coefficient")
    return values


def forcing(n: int, g=G_PI) -> Q:
    if type(n) is not int or n < 1:
        raise ValueError("n must be a positive integer")
    g = polynomial(g)
    return sum((a/Q(8*n-7+j) for j,a in enumerate(g)), Q(0))


def partial(n: int, g=G_PI) -> Q:
    if type(n) is not int or n < 0:
        raise ValueError("nonnegative integer prefix required")
    return sum((forcing(j,g)/16**j for j in range(1,n+1)), Q(0))


def state(n: int, seed=Q(0), g=G_PI) -> Q:
    if type(n) is not int or n < 0:
        raise ValueError("nonnegative integer state index required")
    return 16**n*(exact(seed)+partial(n,g))


def h_moment(n: int, h) -> Q:
    if type(n) is not int or n < 0:
        raise ValueError("nonnegative integer moment index required")
    return sum((a/Q(8*n+j+1) for j,a in enumerate(polynomial(h))),Q(0))


def change_source_gauge(g,seed,h):
    """(g,s) -> (g-(16-z^8)h, s+integral h), all rational."""
    g, h, seed=polynomial(g), polynomial(h), exact(seed)
    coeffs=[Q(0)]*max(len(g),len(h)+8)
    for j,a in enumerate(g): coeffs[j]+=a
    for j,a in enumerate(h):
        coeffs[j]-=16*a
        coeffs[j+8]+=a
    while len(coeffs)>1 and coeffs[-1]==0:
        coeffs.pop()
    return tuple(coeffs),seed+h_moment(0,h)


def source_gauge_check(g,seed,h,max_n: int):
    """Verify U'_n - U_n == a_h(n); ξ_M difference == 16^-M a_h(M)."""
    if type(max_n) is not int or max_n < 0:
        raise ValueError("nonnegative gauge check horizon")
    gp,sp=change_source_gauge(g,seed,h)
    return all(state(n,sp,gp)-state(n,seed,g)==h_moment(n,h)
               and (sp+partial(n,gp))-(exact(seed)+partial(n,g))
                   == h_moment(n,h)/16**n
               for n in range(max_n+1))


@dataclass(frozen=True)
class AffineSeed:
    """Formal a+b*x, x=pi/16, assuming the imported irrationality of pi."""
    a: Q
    b: Q

    def __post_init__(self):
        object.__setattr__(self,"a",exact(self.a))
        object.__setattr__(self,"b",exact(self.b))

    @property
    def completed_coefficients(self):
        """Coefficients of ξ=x+s, not a normality truth decision."""
        return (self.a, Q(1)+self.b)

    @property
    def normality_class(self):
        """Wall's rational-affine theorem: relation, not pi normality verdict."""
        return ("RATIONAL_NONNORMAL" if self.b==-1
                else "EQUIVALENT_TO_PI_BASE16_NORMALITY")

    def raw_state_coefficients(self,n:int):
        if type(n) is not int or n<0:raise ValueError("nonnegative clock")
        return (16**n*(self.a+partial(n)),16**n*self.b)

    def completed_state_coefficients(self,n:int):
        if type(n) is not int or n<0:raise ValueError("nonnegative clock")
        a,b=self.completed_coefficients
        return 16**n*a,16**n*b


def rational_shadow_seed(N:int)->Q:
    """The precomputed finite-depth hostile seed -P_N, not the selected seed."""
    if type(N) is not int or N<1:raise ValueError("positive future depth")
    return -partial(N)


def shadow_state(N:int,n:int)->Q:
    """For n<=N, U_n(-P_N)=-sum_(j=n+1)^N 16^(n-j)r(j)."""
    if type(n) is not int or n<0 or n>N:
        raise ValueError("shadow comparison only up to preparation horizon")
    return state(n,rational_shadow_seed(N))


def shadow_upper(n:int)->Q:
    """|U_n(-P_N)| < r(n+1)/15 for 0<=n<N, any N>n."""
    if type(n) is not int or n<0:raise ValueError("nonnegative n")
    return forcing(n+1)/15


def shell_lock_bound(B:int,h:int=1)->Q:
    """Rational upper bound on (1-Re shell mean) for seed -P_(2B).

    Uses 2*pi^2<20, |U_n|<r(B+1)/15 for B<=n<2B.
    Bound does not assert any particular truth about pi normality.
    """
    if type(B) is not int or B<1 or type(h) is not int:
        raise ValueError("positive shell size and integer h")
    return Q(20*h*h)*shadow_upper(B)**2
