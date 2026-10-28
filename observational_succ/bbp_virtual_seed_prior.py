"""Original four-pole BBP recurrence with a DECLARED prior over initial seeds.

An exact control: Haar averaging the initial phase creates zero ENSEMBLE
Fourier expectation for every nonzero frequency, while the original same-
forcing recurrence has a coherent exceptional seed U0=-pi/16. The latter
is an analytic control defined by the authentic BBP infinite series, NOT a
rational seed or a change to the actual U0=0 trajectory.

The expectation is only over a virtual prior, not over the authentic selected
zero-seeded BBP path; it cannot prove base-16 normality of pi.
"""
from fractions import Fraction as F


def authentic_forcing(n: int) -> F:
    if type(n) is not int or n<1:
        raise ValueError("original forcing begins at n=1")
    return (F(4,8*n-7)-F(2,8*n-4)-F(1,8*n-3)-F(1,8*n-2))


def rational_source_passport(n: int) -> F:
    if type(n) is not int or n<1:
        raise ValueError("original source begins at n=1")
    a=120*n*n-89*n+16
    d=(2*n-1)*(4*n-1)*(8*n-7)*(8*n-3)
    return F(a,d)


def selected_rational_state(n: int, seed=F(0)) -> F:
    """Exact finite state U_n=16 U_(n-1)+r(n) from rational U0=seed."""
    if type(n) is not int or not 0<=n<=1000:
        raise ValueError("finite nonnegative time required")
    u=F(seed)
    for j in range(1,n+1):
        u=16*u+authentic_forcing(j)
    return u


def haar_seed_character_expectation(h: int,n: int) -> int:
    """Integral_0^1 exp(2 pi i h (16^n s+U_n(0))) ds =0 exactly.

    This computation describes Haar prior over initial real seed s modulo 1.
    Do not confuse the annealed expectation with the actual U0=0 path.
    """
    if type(h) is not int or h==0 or type(n) is not int or n<0:
        raise ValueError("nonzero integral frequency, nonnegative time")
    return 0


def finite_coherent_tail(n:int,terms:int):
    """Two-sided rational enclosure for -sum_(j>=1)16^-j r(n+j).

    By the genuine BBP identity, this is U_n at the changed irrational
    seed U0=-pi/16. For n>=1, r(k)<=5/(3k²) for every k>=2.
    Returns (strict_lower_bound, strict_upper_bound). If terms=0, upper=0.
    """
    if type(n) is not int or n<1 or type(terms) is not int or not 0<=terms<=256:
        raise ValueError("finite index >=1 and exact finite tail budget required")
    partial=sum((authentic_forcing(n+j)/16**j for j in range(1,terms+1)),F(0))
    remaining=F(1,9*(n+terms+1)**2*16**terms)
    return -partial-remaining,-partial


def changed_seed_abs_bound(n:int)->F:
    """For n>=1: |U_n(-pi/16)|<=1/(9(n+1)^2)."""
    if type(n) is not int or n<1:
        raise ValueError("n >=1")
    return F(1,9*(n+1)**2)


def comoving_arithmetic_state(n:int,seed=F(0))->F:
    """Exact comoving BBP phase lift 16^-n U_n(seed), a finite rational."""
    return selected_rational_state(n,seed)/16**n


def comoving_arithmetic_increment(n:int)->F:
    """Authentic source increment A_n - A_(n-1)=16^-n r(n)."""
    return authentic_forcing(n)/16**n


def comoving_completion_error_upper(n:int)->F:
    """Upper bound π/16 - A_n(0), from the exact original four-pole tail.

    A_n(0)->π/16 by the classical BBP identity. A_n(seed)->seed+π/16,
    which is not uniform-in-seed knowledge about the actual U0=0 history.
    """
    if type(n) is not int or n<1:
        raise ValueError('n>=1 required for certified 4-pole asymptotic')
    return F(1,9*(n+1)**2*16**n)
