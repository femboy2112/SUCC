"""Exact finite arithmetic for the Bailey–Crandall hexadecimal forcing.

The analytic bounds are proved in formal/duck_pi/BaileyCrandall.lean.
Identifying ``pi_interval`` with geometric pi uses the classical BBP identity;
this Python implementation does not itself certify that imported identity.
No output is evidence of normality or of a uniform cancellation estimate.
"""

from fractions import Fraction


def _natural(value: int, name: str, minimum: int = 0) -> int:
    if type(value) is not int or value < minimum:
        raise ValueError(f"{name} must be an integer >= {minimum}")
    return value


def forcing(m: int) -> Fraction:
    """The exact source forcing r(m), m>=1, with no floating inputs."""
    _natural(m, "m", 1)
    return Fraction(120*m*m - 89*m + 16,
                    (2*m-1)*(4*m-1)*(8*m-7)*(8*m-3))


def coefficient_budget(m: int) -> Fraction:
    """Sharp constant C=47/15 in r(m)<=C/m² on the full m>=1 domain."""
    _natural(m, "m", 1)
    return Fraction(47, 15*m*m)


def tail_budget(n: int) -> Fraction:
    """Unconditional bound t_n<=47/(225(n+1)²) for the specified series."""
    _natural(n, "n")
    return Fraction(47, 225*(n+1)**2)


def tail_interval(n: int, depth: int) -> tuple[Fraction, Fraction]:
    """Strict rational enclosure for sum_{k>=1}16^-k r(n+k).

    The omitted infinite tail is bounded analytically, not estimated from the
    last observed term. Depth zero is legitimate and returns [0, tail_budget].
    """
    _natural(n, "n")
    _natural(depth, "depth")
    partial = sum((forcing(n+k)/16**k for k in range(1, depth+1)), Fraction())
    return partial, partial + tail_budget(n+depth)/16**depth


def lifted_orbit(n: int) -> Fraction:
    """Unreduced recurrence y_0=0, y_(n+1)=16y_n+r(n+1)."""
    _natural(n, "n")
    value = Fraction()
    for m in range(1, n+1):
        value = 16*value + forcing(m)
    return value


def forced_orbit(n: int) -> Fraction:
    """Circle representative in [0,1), reducing at every step."""
    _natural(n, "n")
    value = Fraction()
    for m in range(1, n+1):
        value = (16*value + forcing(m)) % 1
    return value


def pi_interval(terms: int) -> tuple[Fraction, Fraction]:
    """BBP partial sum plus a proved tail budget; classical BBP is a dependency."""
    _natural(terms, "terms")
    low, high = tail_interval(0, terms)
    return 16*low, 16*high


def partial_transport_residual(n: int, depth: int) -> Fraction:
    """Exact zero for the finite shifted source/orbit identity, n>=1."""
    _natural(n, "n", 1)
    _natural(depth, "depth")
    source_partial = pi_interval(n+depth)[0]
    tail_partial = tail_interval(n, depth)[0]
    return 16**(n-1)*source_partial - lifted_orbit(n) - tail_partial
