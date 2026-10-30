"""Research-only, exact rational BBP finite-field/endpoint triangle.

No claim of Pi normality; sensor is a declared auxiliary observation.
Python >=3.10; standard-library only.
"""
from fractions import Fraction
from functools import lru_cache
from math import comb


@lru_cache(maxsize=None)
def R(a: int | Fraction) -> Fraction:
    a = Fraction(a)
    if a <= 0:
        raise ValueError("source a must be positive")
    return 4 / a - 2 / (a + 3) - 1 / (a + 4) - 1 / (a + 5)


def r(n: int) -> Fraction:
    if n < 1:
        raise ValueError("BBP n must be at least 1")
    return R(8*n - 7)


@lru_cache(maxsize=None)
def word_weight(a: int, m: int, j: int) -> Fraction:
    """Probability of any *one* ordered m-bit word with j successes.

    The latent X~mu_a is held across all m conditional Bernoulli steps.
    """
    if m < 0:
        raise ValueError("m must be nonnegative")
    if j < 0 or j > m:
        return Fraction(0)
    numerator = sum(
        ((-1)**k * comb(j,k) * R(a + 8*(m-j+k))
         for k in range(j+1)),
        Fraction(0),
    )
    return numerator / R(a)


def q(a: int, m: int, j: int) -> Fraction:
    """Superposed endpoint mass from all binomially many paths."""
    if j < 0 or j > m:
        return Fraction(0)
    return comb(m,j) * word_weight(a,m,j)


def next_probabilities(a: int, m: int, j: int):
    """Posterior predictive zero and one given any word with grade j."""
    if not 0 <= j <= m:
        raise ValueError("invalid state")
    c = word_weight(a,m,j)
    if c <= 0:
        raise AssertionError("positive source likelihood required")
    fail = word_weight(a,m+1,j) / c
    success = word_weight(a,m+1,j+1) / c
    return fail, success


def triangle_row(a: int, m: int) -> tuple[Fraction, ...]:
    """Build row through posterior updates rather than endpoint formula."""
    row = (Fraction(1),)
    for depth in range(m):
        new = [Fraction(0)] * (depth+2)
        for j,mass in enumerate(row):
            fail,success = next_probabilities(a,depth,j)
            new[j] += mass * fail
            new[j+1] += mass * success
        row = tuple(new)
    return row


def shifted_triangle_row(a: int, m: int) -> tuple[Fraction, ...]:
    """Cross-source recurrence from one exact tilt R(a+8)/R(a)."""
    if m == 0:
        return (Fraction(1),)
    old = shifted_triangle_row(a,m-1)
    shifted = shifted_triangle_row(a+8,m-1)
    z = R(a+8)/R(a)
    return tuple(
        (old[j-1] if j else Fraction(0))
        + z * ((shifted[j] if j < m else Fraction(0)) - (shifted[j-1] if j else Fraction(0)))
        for j in range(m+1)
    )


def harmonic(k: int) -> Fraction:
    if k < 0:
        raise ValueError("k must be nonnegative")
    return sum((Fraction(1,j) for j in range(1,k+1)), Fraction(0))


def harmonic_from_paths(a: int, m: int) -> Fraction:
    return sum((q(a,m,j) * harmonic(j) for j in range(m+1)), Fraction(0))


def harmonic_from_source(a: int, m: int) -> Fraction:
    """H_m - (1/R(a)) sum_{k=1}^m R(a+8k)/k, EXACT."""
    return harmonic(m) - sum((R(a+8*k)/k for k in range(1,m+1)), Fraction(0))/R(a)


def bbp_harmonic(n: int) -> Fraction:
    """The native BBP-diagonal harmonic endpoint readout."""
    return harmonic_from_source(8*n-7, n)


def gamma_matched_harmonic(n: int) -> Fraction:
    """Same source clock, fake R_fake(a)=15/a^2 (no -59/a^3)."""
    a = Fraction(8*n-7)
    return harmonic(n)-sum((a*a/((a+8*k)**2*k) for k in range(1,n+1)),Fraction(0))


def bbp_state(n: int, seed: Fraction = Fraction(0)) -> Fraction:
    """Exact deterministic selected BBP state, not a source sample."""
    if n < 0:
        raise ValueError("BBP time must be nonnegative")
    state = Fraction(seed)
    for k in range(1,n+1):
        state = 16*state+r(k)
    return state


def fractional(x: Fraction) -> Fraction:
    x = Fraction(x)
    return x - x.numerator//x.denominator


def literal_carry(n: int, seed: Fraction = Fraction(0)) -> int:
    """Actual integer branch lost under exponentiation of the circle phase."""
    if n < 1:
        raise ValueError("carry time must be positive")
    exact = 16*fractional(bbp_state(n-1,seed)) + r(n) - fractional(bbp_state(n,seed))
    if exact.denominator != 1:
        raise AssertionError("circle-branch update was not integral")
    return int(exact)


def two_step_carry(n: int, seed: Fraction = Fraction(0)) -> int:
    """Two-step branch lift: kappa^(2)=16*kappa_n+kappa_(n+1)."""
    if n < 1:
        raise ValueError("carry time must be positive")
    exact = (256*fractional(bbp_state(n-1,seed)) + 16*r(n) + r(n+1)
             - fractional(bbp_state(n+1,seed)))
    if exact.denominator != 1:
        raise AssertionError("two-step branch lift was not integral")
    return int(exact)


def graded_selected_points(n: int, seed: Fraction = Fraction(0)):
    """Finite original-source grades marked by exact selected phase/carry.

    Returned phase is a rational fractional turn, NOT a random phase sampler.
    """
    if n < 1:
        raise ValueError("native source clock must be positive")
    a = 8*n-7
    return tuple((j, q(a,n,j), fractional(bbp_state(n+j,seed)),
                  literal_carry(n+j,seed)) for j in range(n+1))
