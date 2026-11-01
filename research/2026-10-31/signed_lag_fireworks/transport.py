"""Exact budgets for clipped original-four-pole BBP lag transport.

These bounds hold for every real seed; they do not prove selected cancellation.
See TRANSPORT.md. All public numerical outputs are rational or integer.
"""
from fractions import Fraction as F
from math import isqrt


def _validate(N, K, h):
    if type(N) is not int or type(K) is not int or not 1 <= K <= N:
        raise ValueError('integer 1 <= K <= N required')
    if type(h) is not int or h == 0:
        raise ValueError('nonzero integer harmonic required')


def ceil_sqrt_fraction(x):
    x = F(x)
    if x < 0:
        raise ValueError('nonnegative radicand required')
    m = isqrt(x.numerator // x.denominator)
    return m if m*m >= x else m+1


def point_error(n, k, h):
    """Upper on |e(h(U[n+k]-U[n])) - e(h(16**k-1)U[n])|."""
    _validate(n+k, k, h)
    if type(n) is not int or n < 1:
        raise ValueError('positive time required')
    return min(F(2), F(11*abs(h)*(16**k-1), 112*n*n))


def lag_error(N, k, h):
    """Minimum of three valid rational majorants on |C_k-D_k|.

    The square-root majorant is rounded up on a 2**32 rational grid.
    It follows by integrating the decreasing clipped n**(-2) majorant.
    """
    _validate(N, k, h)
    if k >= N:
        return F(0)
    grid = 2**32
    radicand = F(11*abs(h)*(16**k-1), 14)
    square_root = F(ceil_sqrt_fraction(radicand*grid*grid), grid)
    return min(F(2*(N-k)), F(11*abs(h)*(16**k-1), 56), square_root)


def weighted_error(N, K, h):
    _validate(N, K, h)
    return sum((F(2*(K-k), K*K*N)*lag_error(N, k, h)
                for k in range(1, K)), F(0))


def simple_error(N, K, h):
    """Closed majorant 8 B_h 4**K/(9 K**2 N), B_h>=sqrt(11|h|/14)."""
    _validate(N, K, h)
    if K == 1:
        return F(0)
    B = ceil_sqrt_fraction(F(11*abs(h), 14))
    return F(8*B*4**K, 9*K*K*N)


def doubled_clock(N):
    """floor(log_4 N), computed without floating point (zero for N<4)."""
    if type(N) is not int or N < 1:
        raise ValueError('positive integer horizon required')
    k = 0
    while 4**(k+1) <= N:
        k += 1
    return k


def certificate(N, K, h, score):
    """VdC upper bound using a certified signed interval; never clip below zero."""
    _validate(N, K, h)
    lo, hi = map(F, score)
    if lo > hi:
        raise ValueError('ordered interval required')
    bracket = F(1, K)+hi+weighted_error(N, K, h)
    if bracket < 0:
        raise ValueError('inconsistent interval: negative energy upper bound')
    return F(N+K-1, N)*bracket
