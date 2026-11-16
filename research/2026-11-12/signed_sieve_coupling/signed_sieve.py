"""Exact finite source-faithful signed sieve / Goldbach coupling laboratory.

No generic asymptotic positivity claim. Standard library, integer arithmetic only.
"""
from __future__ import annotations
from fractions import Fraction
from math import isqrt


def prime_mask(n: int) -> bytearray:
    """Sieve of Eratosthenes, independent primality control in tests."""
    if n < 2:
        return bytearray(n + 1)
    a = bytearray(b'\1') * (n + 1)
    a[0] = a[1] = 0
    for p in range(2, isqrt(n) + 1):
        if a[p]:
            a[p * p:n + 1:p] = b'\0' * ((n - p * p) // p + 1)
    return a


def omega_mask(n: int) -> list[int]:
    """Factor multiplicity by smallest-prime-factor dynamic programming."""
    least = list(range(n + 1))
    for p in range(2, isqrt(n) + 1):
        if least[p] == p:
            for m in range(p * p, n + 1, p):
                if least[m] == m:
                    least[m] = p
    omega = [0] * (n + 1)
    for m in range(2, n + 1):
        omega[m] = 1 + omega[m // least[m]]
    return omega


def icbrt(n: int) -> int:
    """Greatest z with z^3<=n, exactly (no floats)."""
    assert n >= 0
    lo, hi = 0, 1
    while hi ** 3 <= n:
        hi *= 2
    while lo + 1 < hi:
        m = (lo + hi) // 2
        if m ** 3 <= n:
            lo = m
        else:
            hi = m
    return lo


def rough_majorant(primes: bytearray, z: int) -> bytearray:
    """Prime-inclusive z-rough mask q_z(k), k>=2.

    Starts with every k>=2 and eliminates *proper multiples* of primes l<=z.
    Retains the small prime l itself, so q>=1_primes even at the boundary.
    """
    n = len(primes) - 1
    q = bytearray(b'\1') * (n + 1)
    q[0] = q[1] = 0
    for ell in range(2, min(z, n) + 1):
        if primes[ell]:
            start = 2 * ell
            if start <= n:
                q[start:n + 1:ell] = b'\0' * ((n - start) // ell + 1)
    return q


def masks(primes: bytearray, z: int):
    q = rough_majorant(primes, z)
    c = bytearray(len(q))
    s = [0] * len(q)
    for k in range(2, len(q)):
        if q[k]:
            if primes[k]:
                s[k] = +1
            else:
                c[k] = 1
                s[k] = -1
    return q, c, s


def coeff(a, b, N: int) -> int:
    """Exact, ordered additive convolution; both inputs indexed from 0."""
    return sum(int(a[k]) * int(b[N - k]) for k in range(2, N - 1))


def haar_pair(a, b):
    """Exact Haar Gram decomposition into constant band and signed scales."""
    assert len(a) == len(b) and len(a) > 0
    N = len(a)
    L = 1 << (N - 1).bit_length()
    a = list(a) + [0] * (L - N)
    b = list(b) + [0] * (L - N)
    constant = Fraction(sum(a) * sum(b), L)
    bands = []
    width = 2
    while width <= L:
        s = Fraction(0)
        for left in range(0, L, width):
            da = sum(a[left:left + width // 2]) - sum(a[left + width // 2:left + width])
            db = sum(b[left:left + width // 2]) - sum(b[left + width // 2:left + width])
            s += Fraction(da * db, width)
        bands.append((width, s))
        width *= 2
    result = sum(a[k] * b[k] for k in range(L))
    assert constant + sum((term for _, term in bands), Fraction(0)) == result
    return result, constant, bands


def row(N: int, primes: bytearray, z: int):
    assert N >= 4 and N < len(primes)
    q, c, s = masks(primes, z)
    goldbach = coeff(primes, primes, N)
    rough_pairs = coeff(q, q, N)
    one_sided = coeff(q, c, N)
    prime_rough = coeff(primes, q, N)
    semiprime_pairs = coeff(c, c, N)
    signed = coeff(q, s, N)
    assert signed == rough_pairs - 2 * one_sided
    assert signed == 2 * prime_rough - rough_pairs
    assert signed == goldbach - semiprime_pairs
    assert rough_pairs == goldbach + 2 * (one_sided - semiprime_pairs) + semiprime_pairs
    return {"N": N, "cutoff": z, "goldbach_ordered": goldbach,
            "rough_pairs": rough_pairs, "rough_composite_pairs": semiprime_pairs,
            "one_sided_composite_pairs": one_sided,
            "prime_rough_pairs":prime_rough, "signed_lower": signed,
            "certifies": signed > 0}


def midpoint_haar(N: int, primes: bytearray, z: int):
    q, _, s = masks(primes, z)
    a = [q[k] for k in range(2, N - 1)]
    b = [s[N - k] for k in range(2, N - 1)]
    exact, base, bands = haar_pair(a, b)
    return {"N": N, "cutoff": z, "signed_lower": exact,
            "constant": str(base),
            "scale_bands": [{"width": width, "value": str(value)} for width, value in bands]}


def source_mutant(primes: bytearray):
    """Genuine-prime subset with no sums divisible by four."""
    return bytearray(1 if primes[k] and k % 4 == 1 else 0 for k in range(len(primes)))


def verify_row(N, primes, z):
    q, c, s = masks(primes, z)
    R = coeff(primes, primes, N)
    C = coeff(c, c, N)
    L = coeff(q, s, N)
    assert R - C == L
    if (z + 1)**3 > N:
        omega = omega_mask(N)
        for k in range(2, N + 1):
            if q[k]:
                assert omega[k] in (1, 2)
                assert s[k] == -q[k] * (-1) ** omega[k]
    return L
