"""Natural successor in reciprocal coordinates; Pascal and BBP mirror rays.

All arithmetic is exact; the projective action and Lucas incidence are
representations of the *same* 2x2 unipotent shear, not the same observable.
Classical harmonic/binomial identities are not π-normality evidence.
"""
from __future__ import annotations

from fractions import Fraction as Q
from math import comb, factorial


def _nat(x: int, minimum: int = 0) -> int:
    if type(x) is not int or x < minimum:
        raise ValueError(f"integer >= {minimum} required")
    return x


def _exact(x: int | Q) -> Q:
    if type(x) not in (int, Q):
        raise ValueError("exact integer/Fraction required")
    return Q(x)


def unipotent_shear(steps: int) -> tuple[tuple[int, int], tuple[int, int]]:
    """J**steps for J=[[1,0],[1,1]]; same matrix as Lucas one-bit zeta."""
    _nat(steps)
    return ((1, 0), (steps, 1))


def mirror_step(x: int | Q, steps: int = 1) -> Q:
    """Projective J**steps: x -> x/(1+steps*x), x>0, steps>=0."""
    x = _exact(x)
    _nat(steps)
    if x <= 0:
        raise ValueError("positive reciprocal coordinate required")
    return x / (1 + steps*x)


def reciprocal_orbit(n: int, steps: int = 0) -> Q:
    """Starting at 1/n, perform steps ordinary integer successors."""
    _nat(n, 1)
    return mirror_step(Q(1, n), steps)


def harmonic(n: int) -> Q:
    _nat(n)
    return sum((Q(1, j) for j in range(1, n+1)), Q())


def harmonic_pascal(n: int) -> Q:
    """Classical alternating binomial identity for H_n, all integer-exact."""
    _nat(n)
    return sum((Q((-1)**(j-1)*comb(n,j), j)
                for j in range(1, n+1)), Q())


def harmonic_difference(n: int, order: int) -> Q:
    """Delta**order H_n, where order>=1 and H_0=0."""
    _nat(n)
    _nat(order, 1)
    return Q((-1)**(order-1)*factorial(order-1),
             (factorial(n+order)//factorial(n)))


def harmonic_mirror_history(n: int) -> tuple[tuple[int, Q, Q], ...]:
    """(integer state, its reciprocal, accumulated mirror SUCC) for 1..n."""
    _nat(n)
    x, h = Q(1), Q()
    out = []
    for j in range(1, n+1):
        h += x
        out.append((j, x, h))
        x = mirror_step(x)
    return tuple(out)


def prime_fucc_log_bracket(n: int, multiplier: int) -> tuple[Q, Q]:
    """Exact lower/upper *rational* enclosure for log(multiplier).

    H_(mn)-H_n < log(m) < H_(mn)-H_n+(m-1)/(2*m*n),
    right Riemann vs trapezoid for integral_n^(mn) dt/t.
    """
    _nat(n, 1)
    _nat(multiplier, 2)
    lo = sum((Q(1,j) for j in range(n+1,multiplier*n+1)),Q())
    hi = lo + Q(multiplier-1,2*multiplier*n)
    return lo,hi


MIRROR_RAY_OFFSETS = (7, 4, 3, 2)
MIRROR_RAY_COEFFICIENTS = (4, -2, -1, -1)


def source_rays(n: int) -> tuple[Q, Q, Q, Q]:
    """Four J**8 successor rays, same original BBP n, not independent sources."""
    _nat(n,1)
    return tuple(Q(1,8*n-c) for c in MIRROR_RAY_OFFSETS)  # type: ignore[return-value]


def bbp_mirror_forcing(n: int) -> Q:
    """Authentic unaltered BBP forcing as four synchronized mirror rays."""
    return sum((Q(a)*x for a,x in zip(MIRROR_RAY_COEFFICIENTS, source_rays(n))),Q())


def source_pole_moment(order: int) -> int:
    """Numerator moment sum coeff*c**order; m0=0, m1=15, m2=151."""
    _nat(order)
    return sum(a*c**order for a,c in zip(MIRROR_RAY_COEFFICIENTS,MIRROR_RAY_OFFSETS))


def source_signed_harmonic_sum(n: int) -> Q:
    """Cumulative BBP forcing, before geometric radix-16 weighting."""
    _nat(n)
    return sum((Q(a)*sum((Q(1,8*j-c) for j in range(1,n+1)),Q())
                for a,c in zip(MIRROR_RAY_COEFFICIENTS,MIRROR_RAY_OFFSETS)),Q())


def counterfeit_mirror_tail(n: int) -> Q:
    """Positive reciprocal-Hausdorff-style tail with rational endpoint 1/128."""
    _nat(n)
    return Q(1, 64*(n+1)*(n+2))


def counterfeit_mirror_force(n: int) -> Q:
    """Non-BBP positive signed 3-ray forcing with same leading 15/(64*n²).

    r*(n)=16*T_(n-1)-T_n = [16/n-17/(n+1)+1/(n+2)]/64.
    A deliberate false source: it does NOT retain BBP four poles.
    """
    _nat(n,1)
    return Q(16,64*n)-Q(17,64*(n+1))+Q(1,64*(n+2))


def counterfeit_mirror_state(n: int) -> Q:
    """Anchored U*_n=16**n/128-T_n; eventual zero-circle orbit."""
    _nat(n)
    return Q(16**n,128)-counterfeit_mirror_tail(n)
