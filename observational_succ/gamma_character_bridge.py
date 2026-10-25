"""Exact finite interfaces for Euler's constant and source character clocks.

The companion proof distinguishes successor-time dilation from multiplication
of circle states.  For a bounded sequence, vanishing harmonic windows at BOTH
time dilations 2 and 3 is equivalent to a vanishing ordinary mean.  It is a
Tauberian reformulation, not a proved BBP cancellation theorem.

The original BBP tail bound transports this criterion to pi with an explicit
O_h(N^-2) window cost.  All code below is rational/integer; character phases
and infinite analytic statements retain paper-proof authority.
"""
from __future__ import annotations

from fractions import Fraction as Q
from math import isqrt
from typing import Sequence

from .pi_source_collision import tail_upper


def _integer(value: int, minimum: int = 0) -> int:
    if type(value) is not int or value < minimum:
        raise ValueError(f"integer >= {minimum} required")
    return value


def _rational(value: Q | int) -> Q:
    if type(value) not in (int, Q):
        raise ValueError("exact integer or Fraction required")
    return Q(value)


def harmonic_window(values: Sequence[Q | int], lower: Q | int,
                    upper: Q | int) -> Q:
    """H(upper)-H(lower), H(x)=sum_{1<=n<=x} values[n-1]/n.

    Endpoints are exact nonnegative rationals and reversed windows are signed.
    The finite sequence must cover both endpoints; there is no zero padding.
    """
    lower, upper = _rational(lower), _rational(upper)
    if min(lower, upper) < 0 or max(lower, upper) >= len(values) + 1:
        raise ValueError("window outside the supplied finite sequence")
    if upper < lower:
        return -harmonic_window(values, upper, lower)
    return sum((_rational(values[n - 1]) / n
                for n in range(int(lower) + 1, int(upper) + 1)), Q())


def dilation_path(two_power: int, three_power: int) -> tuple[Q, ...]:
    """A finite exact path from 1 to 2^u 3^v, allowing inverse steps.

    This constructs no statistical invariance.  Each adjacent harmonic-window
    term remains an obligation of the selected coefficient sequence.
    """
    if type(two_power) is not int or type(three_power) is not int:
        raise ValueError("integer exponents required")
    values = [Q(1)]
    for prime, exponent in ((2, two_power), (3, three_power)):
        step = Q(prime) if exponent >= 0 else Q(1, prime)
        for _ in range(abs(exponent)):
            values.append(values[-1] * step)
    return tuple(values)


def source_character_point_bound(n: int, h: int = 1) -> Q:
    """Strict upper on |e(h U_n)-e(h 16^(n-1) pi)| for h!=0.

    U_0=0 and the authentic four-pole source are required.  The imported exact
    tail is 0<T_n<1/((8n+1)(8n+2)); 2*pi<44/7 supplies the rational Lipschitz
    constant.  For h=0 the returned zero is an equality.
    """
    _integer(n, 1)
    if type(h) is not int:
        raise ValueError("integer Fourier frequency required")
    return Q(44, 7) * abs(h) * tail_upper(n)


def source_character_window_bound(n: int, dilation: int,
                                  h: int = 1) -> Q:
    """Exact finite upper on the harmonic source-to-pi window error."""
    _integer(n, 1)
    _integer(dilation, 2)
    return sum((source_character_point_bound(k, h) / k
                for k in range(n + 1, dilation * n + 1)), Q())


def source_character_window_envelope(n: int, dilation: int,
                                     h: int = 1) -> Q:
    """Simple upper C_h(1-p^-2)/(2N^2), C_h=11|h|/112.

    Every integer dilation p>=2 is allowed; the Tauberian theorem uses p=2,3.
    The inequality is strict for h!=0.  No frequency-uniform limit is implied.
    """
    _integer(n, 1)
    _integer(dilation, 2)
    if type(h) is not int:
        raise ValueError("integer Fourier frequency required")
    return Q(11 * abs(h), 112) * (1 - Q(1, dilation**2)) / (2 * n**2)


def source_character_dirichlet_tail_bound(cutoff: int, sigma: int,
                                          h: int = 1) -> Q:
    """Rational specialization of C_h M^(-sigma-1)/(sigma+1).

    The paper theorem holds for real sigma>-1 and gives a holomorphic
    correction in Re(s)>-1.  This exact oracle restricts sigma to nonnegative
    integers so its output is rational without uncertified real powers.
    """
    _integer(cutoff, 1)
    _integer(sigma, 0)
    if type(h) is not int:
        raise ValueError("integer Fourier frequency required")
    return Q(11 * abs(h), 112 * (sigma + 1) * cutoff**(sigma + 1))


def geometric_clock_prefix_mass(epsilon: Q | int, cutoff: int) -> Q:
    """Exact mass through M of q_eps(n)=eps(1+eps)^(-n), n>=1."""
    epsilon = _rational(epsilon)
    _integer(cutoff)
    if epsilon <= 0:
        raise ValueError("positive epsilon required")
    return 1 - (1 + epsilon)**(-cutoff)


def dirichlet_clock_prefix_upper(epsilon: Q | int, cutoff: int) -> Q:
    """Upper on sum_{n<=M} n^(-1-eps)/zeta(1+eps).

    Uses zeta(1+eps)>=1/eps and n^(-eps)<=1; it is a bound, not a numerical
    zeta evaluation.  The returned mass upper is clipped at 1.
    """
    epsilon = _rational(epsilon)
    _integer(cutoff)
    if epsilon <= 0:
        raise ValueError("positive epsilon required")
    return min(Q(1), epsilon * sum((Q(1, n) for n in range(1, cutoff + 1)), Q()))


def clock_total_variation_lower(epsilon: Q | int, cutoff: int) -> Q:
    """Event lower bound on TV(p_eps,q_eps), with TV in [0,1]."""
    return max(Q(), geometric_clock_prefix_mass(epsilon, cutoff)
               - dirichlet_clock_prefix_upper(epsilon, cutoff))


def dyadic_log_periodic_sign(n: int) -> int:
    """A bounded one-clock counterfeit, defined using integer square tests.

    In each [2^k,2^(k+1)), it is +1 before sqrt(2)*2^k and -1 thereafter.
    Its doubling harmonic windows tend to 0, while its ordinary means do not.
    It is NOT an authentic BBP coefficient sequence.
    """
    _integer(n, 1)
    k = n.bit_length() - 1
    return 1 if n*n < 2 * (1 << (2*k)) else -1


def dyadic_control_signed_count(horizon: int) -> int:
    """Independent block-count oracle for the counterfeit's partial sum."""
    _integer(horizon)
    total = 0
    for k in range(horizon.bit_length()):
        lo = 1 << k
        hi = min(horizon, (1 << (k + 1)) - 1)
        if hi < lo:
            break
        last_positive = isqrt(2 * (1 << (2*k)))
        positive = max(0, min(hi, last_positive) - lo + 1)
        total += 2*positive - (hi - lo + 1)
    return total
