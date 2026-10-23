"""Exact carry-memory witnesses; rational algebra, not continuum certification.

The phase fibre is a bilateral/Bloch comparison, not a new realization of the
one-based source. The all-time moment polynomial itself applies to that source.
"""
from __future__ import annotations

from fractions import Fraction as Q


def _radix(a):
    if type(a) is not int or a < 2:
        raise ValueError("integer radix >= 2 required")
    return a


def _rational(z):
    if type(z) not in (int, Q):
        raise ValueError("exact rational phase/spectral parameter required")
    return Q(z)


def _horizon(n):
    if type(n) is not int or n < 0:
        raise ValueError("nonnegative integer horizon required")
    return n


def carry_matrix(a, z):
    """T(z)e_r=e_(r+1), T(z)e_(a-1)=z e_0. Unitary iff |z|=1."""
    _radix(a); z = _rational(z)
    rows = [[Q(0) for _ in range(a)] for _ in range(a)]
    for r in range(a-1):
        rows[r+1][r] = Q(1)
    rows[0][-1] = z
    return tuple(map(tuple, rows))


def _multiply(left, right):
    return tuple(tuple(sum((x*y for x, y in zip(row, col)), Q())
                       for col in zip(*right)) for row in left)


def _identity(a):
    return tuple(tuple(Q(i == j) for j in range(a)) for i in range(a))


def moment(a, z, n):
    """u* T(z)^n u as the exact two-point quotient displacement law."""
    _radix(a); z = _rational(z); _horizon(n)
    q, r = divmod(n, a)
    return Q(a-r, a)*z**q + Q(r, a)*z**(q+1)


def basis_moments(a, z, horizon):
    """Independent labelled matrix/basis evolution, no quotient formula."""
    T = carry_matrix(a, z); _horizon(horizon)
    v = (Q(1),)*a
    result = []
    for _ in range(horizon+1):
        result.append(sum(v, Q())/a)
        v = tuple(sum((x*y for x, y in zip(row, v)), Q()) for row in T)
    return tuple(result)


def transfer_numerator(a, z):
    """Coefficients N(t) of sum F_n t^n = N(t)/(1-z t^a)."""
    _radix(a); z = _rational(z)
    return tuple(Q(a-r, a)+Q(r, a)*z for r in range(a))


def memory_kernels(a, z, count):
    """u^* T Q (Q T Q)^j Q T u, with Q=I-u u^*, computed as matrices."""
    T = carry_matrix(a, z); _horizon(count)
    I = _identity(a)
    Qh = tuple(tuple(I[i][j]-Q(1, a) for j in range(a)) for i in range(a))
    left, right = _multiply(T, Qh), _multiply(Qh, T)
    hidden = _multiply(_multiply(Qh, T), Qh)
    power = I
    result = []
    for _ in range(count):
        product = _multiply(_multiply(left, power), right)
        result.append(sum((sum(row, Q()) for row in product), Q())/a)
        power = _multiply(power, hidden)
    return tuple(result)


def reconstruct_with_memory(a, z, horizon):
    """Exact elimination recurrence, with zero hidden initial component."""
    _radix(a); z = _rational(z); _horizon(horizon)
    kernels = memory_kernels(a, z, max(0, horizon-1))
    c = moment(a, z, 1)
    result = [Q(1)]
    for n in range(horizon):
        result.append(c*result[n] + sum(
            (kernels[j]*result[n-1-j] for j in range(n)), Q()))
    return tuple(result)


def hankel_determinant(a, z, size):
    """Exact Gaussian elimination on the scalar moment Hankel matrix."""
    _radix(a); z = _rational(z); _horizon(size)
    rows = [[moment(a, z, i+j) for j in range(size)] for i in range(size)]
    det = Q(1)
    for j in range(size):
        pivot = next((i for i in range(j, size) if rows[i][j]), None)
        if pivot is None:
            return Q(0)
        if pivot != j:
            rows[j], rows[pivot] = rows[pivot], rows[j]
            det = -det
        value = rows[j][j]
        det *= value
        for i in range(j+1, size):
            factor = rows[i][j]/value
            for k in range(j+1, size):
                rows[i][k] -= factor*rows[j][k]
            rows[i][j] = Q(0)
    return det
