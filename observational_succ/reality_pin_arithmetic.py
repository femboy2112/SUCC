"""Certified finite access to the source-authenticated infinite arithmetic operator.

The infinite operator and convergence theorems are in REALITY_PIN_ARITHMETIC_OPERATOR.md.
Rational matrices here enclose log(n); they never silently replace log(n) by n.
Only integer sigma >= 2 is implemented so every prime coefficient is rational.
No physical observation or scalar-boundary cyclicity is certified by this module.
"""
from __future__ import annotations

from fractions import Fraction as Q
from math import isqrt

from observational_succ.boundary_realization_selection import matrix_inverse


class ArithmeticSourceError(ValueError):
    """A source or exact-arithmetic contract was not satisfied."""


def _rational(x):
    if isinstance(x, bool) or not isinstance(x, (int, Q)):
        raise ArithmeticSourceError("exact int/Fraction input required")
    return Q(x)


def _integer(n, minimum=1):
    if isinstance(n, bool) or not isinstance(n, int) or n < minimum:
        raise ArithmeticSourceError("integer out of declared source domain")
    return n


def primes_through(n):
    _integer(n)
    return tuple(p for p in range(2, n + 1)
                 if all(p % d for d in range(2, isqrt(p) + 1)))


def log_interval(x, terms=12):
    """Rational lower/upper enclosure of log(x), x >= 1; exact series tail."""
    x = _rational(x)
    _integer(terms)
    if x < 1:
        raise ArithmeticSourceError("log enclosure requires x >= 1")
    k = 0
    while x >= 2:
        x /= 2
        k += 1

    def atanh_bound(y):
        z = (y - 1) / (y + 1)
        lo = 2 * sum((z ** (2*j + 1) / (2*j + 1)
                      for j in range(terms)), Q())
        tail = 2 * z ** (2*terms + 1) / ((2*terms + 1) * (1-z*z))
        return lo, lo + tail

    a, b = atanh_bound(x)
    l2, u2 = atanh_bound(Q(2))
    return a+k*l2, b+k*u2


def perturbation_bound(lam=1, sigma=2):
    """b >= ||T||, using sum_p p^-sigma <= integral_1^infty x^-sigma dx."""
    lam = _rational(lam)
    _integer(sigma, 2)
    return 2*abs(lam) + Q(2, sigma-1)


def shift(lam=1, sigma=2):
    return perturbation_bound(lam, sigma) + 1


def source_channels(n, lam=1, sigma=2):
    """Unmerged directed source channels (label, from, to, weight) on 1..n.

    Labels remain separate even when SUCC and V_2 both send 1 to 2.
    """
    _integer(n)
    lam = _rational(lam)
    _integer(sigma, 2)
    channels = [("S", j, j+1, lam) for j in range(1, n)]
    channels += [(f"V_{p}", j, p*j, Q(1, p**sigma))
                 for p in primes_through(n) for j in range(1, n//p+1)]
    return tuple(channels)


def arithmetic_matrix_interval(n, lam=1, sigma=2, terms=12):
    """Loewner lower/upper matrices for P_n K P_n, with c=b+1 fixed globally."""
    _integer(n)
    c = shift(lam, sigma)
    lower = [[Q() for _ in range(n)] for _ in range(n)]
    upper = [[Q() for _ in range(n)] for _ in range(n)]
    for j in range(n):
        lo, hi = log_interval(j+1, terms)
        lower[j][j], upper[j][j] = c+lo, c+hi
    for _, i, j, weight in source_channels(n, lam, sigma):
        for matrix in (lower, upper):
            matrix[i-1][j-1] += weight
            matrix[j-1][i-1] += weight
    return tuple(map(tuple, lower)), tuple(map(tuple, upper))


def _resolvent(matrix, s):
    s = _rational(s)
    if s < 0:
        raise ArithmeticSourceError("certified Laplace domain is s >= 0")
    return matrix_inverse(tuple(tuple(x+(s if i == j else 0)
                                      for j, x in enumerate(row))
                                for i, row in enumerate(matrix)))


def finite_boundary_interval(n, lam=1, sigma=2, s=0, terms=12):
    """Certified m_n(s), not a certificate for the full infinite operator alone."""
    lo, hi = arithmetic_matrix_interval(n, lam, sigma, terms)
    return _resolvent(hi, s)[0][0], _resolvent(lo, s)[0][0]


def galerkin_norm_bound(n, lam=1, sigma=2, s=0, terms=12):
    """Bound ||(K+s)^-1 - P_n(P_n K P_n+s)^-1 P_n||."""
    _integer(n)
    s = _rational(s)
    if s < 0:
        raise ArithmeticSourceError("s >= 0 required")
    b = perturbation_bound(lam, sigma)
    c = b+1
    loglo, _ = log_interval(n+1, terms)
    return ((c+s)/(c+s-b))**2 / (loglo+c+s)


def scalar_tail_bound(n, lam=1, sigma=2, s=0, terms=12):
    """0 <= m(s)-m_n(s) <= b^2/((s+1)^2(log(n+1)+s+1))."""
    _integer(n)
    s = _rational(s)
    if s < 0:
        raise ArithmeticSourceError("s >= 0 required")
    b = perturbation_bound(lam, sigma)
    loglo, _ = log_interval(n+1, terms)
    return b*b / ((s+1)**2 * (loglo+s+1))


def boundary_resolvent_enclosure(n, lam=1, sigma=2, s=0, terms=12):
    """Certified full infinite m(s); upper bound includes the source horizon."""
    lo, hi = finite_boundary_interval(n, lam, sigma, s, terms)
    s = _rational(s)
    return lo, min(Q(1)/(s+1), hi+scalar_tail_bound(n, lam, sigma, s, terms))


def prime_cutoff_resolvent_bound(prime_cutoff, lam=1, sigma=2, s=0):
    """Same c on both operators; prime series tail, with no log approximation."""
    _integer(prime_cutoff)
    perturbation_bound(lam, sigma)
    s = _rational(s)
    if s < 0:
        raise ArithmeticSourceError("s >= 0 required")
    return Q(2, (sigma-1)*prime_cutoff**(sigma-1)) / (s+1)**2


def finite_second_moment(n, lam=1, sigma=2):
    """Exact <1|K_n^2|1>; the log diagonal contributes zero at n=1."""
    _integer(n)
    lam = _rational(lam)
    c = shift(lam, sigma)
    if n == 1:
        return c*c
    return c*c + lam*lam + 2*lam*Q(1, 2**sigma) + sum(
        (Q(1, p**(2*sigma)) for p in primes_through(n)), Q())


def finite_third_moment_interval(n, lam=1, sigma=2, terms=12):
    """Analytic prime-jet formula enclosed with rational logarithm bounds."""
    _integer(n)
    lam = _rational(lam)
    c = shift(lam, sigma)
    q = finite_second_moment(n, lam, sigma)-c*c
    base = c**3 + 3*c*q
    if n >= 3:
        base += 2*lam*(lam+Q(1, 2**sigma))*Q(1, 3**sigma)
    lower = upper = base
    for p in primes_through(n):
        amplitude = Q(1, p**sigma) + (lam if p == 2 else 0)
        a, b = log_interval(p, terms)
        lower += amplitude*amplitude*a
        upper += amplitude*amplitude*b
    return lower, upper


def boundary_moments(matrix, order):
    """Independent exact matrix-power oracle for supplied rational matrices."""
    _integer(order, 0)
    n = len(matrix)
    if n == 0 or any(len(row) != n for row in matrix):
        raise ArithmeticSourceError("nonempty square matrix required")
    a = tuple(tuple(_rational(x) for x in row) for row in matrix)
    v = (Q(1),) + (Q(),)*(n-1)
    result = [v[0]]
    for _ in range(order):
        v = tuple(sum((a[i][j]*v[j] for j in range(n)), Q()) for i in range(n))
        result.append(v[0])
    return tuple(result)


def source_word_endpoint(word, start=1):
    """Positive labelled words; a composite declared primitive is rejected."""
    _integer(start)
    n = start
    for letter in word:
        if letter == "S":
            n += 1
        elif isinstance(letter, int) and not isinstance(letter, bool):
            if letter not in primes_through(letter):
                raise ArithmeticSourceError("FUCC primitive passport is not prime")
            n *= letter
        else:
            raise ArithmeticSourceError("unknown source letter")
    return n


def reciprocal_cutoff_defect(n, p, source):
    """Exact coordinate dictionary for Vp_N* S_N^p - S_N Vp_N*."""
    _integer(n)
    _integer(p, 2)
    _integer(source)
    if source > n:
        raise ArithmeticSourceError("source beyond horizon")
    out = {}
    if source+p <= n and (source+p) % p == 0:
        out[(source+p)//p] = Q(1)
    if source % p == 0 and source//p+1 <= n:
        target = source//p+1
        out[target] = out.get(target, Q())-1
    return {key: value for key, value in out.items() if value}
