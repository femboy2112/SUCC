"""Exact arithmetic for bounded ratios and source-locked 2x3 phase exponents.

No numerical pi oracle, zeta zeros, or probabilistic simulation is used to
prove asymptotic claims. These functions support the paper derivations in
RATIO_FIBER_TORUS.md; finite checks are regression probes only.
"""
from __future__ import annotations

from collections import Counter
from fractions import Fraction
from math import gcd, log


def factor(n: int) -> dict[int, int]:
    if n < 1:
        raise ValueError('n must be positive')
    result: dict[int, int] = {}
    d = 2
    while d*d <= n:
        while n % d == 0:
            result[d] = result.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        result[n] = result.get(n, 0) + 1
    return result


def signed_prime_exponents(n: int, m: int) -> dict[int, int]:
    if n < 1 or m < 1:
        raise ValueError('n,m must be positive')
    a = Counter(factor(n))
    a.subtract(factor(m))
    return {p: v for p, v in sorted(a.items()) if v != 0}


def local_total_variation(n: int, m: int) -> int:
    """Exact integer exp(sum_p |v_p(n/m)| log p)."""
    ans = 1
    for p, v in signed_prime_exponents(n,m).items():
        ans *= p ** abs(v)
    return ans


def prime_compensation_root(n: int, m: int) -> int:
    """Exact integer exp(defect(n,m)/2) = min(n,m)/gcd(n,m)."""
    if min(n, m) < 1:
        raise ValueError('n,m must be positive')
    return min(n,m) // gcd(n,m)


def J_32(A: int) -> list[int]:
    """Indices ell with 2ell and 3ell in the half-open band [A,2A)."""
    if A < 2:
        raise ValueError('A >= 2')
    return list(range((A+1)//2, (2*A-1)//3 + 1))


def K_32(ell: int) -> int:
    if ell < 1:
        raise ValueError('ell positive')
    return 16 ** (2*ell-1) * (16**ell - 1)


def v_p(n: int, p: int) -> int:
    if n < 1 or p < 2:
        raise ValueError('n>0 and p>=2')
    k = 0
    while n % p == 0:
        n //= p
        k += 1
    return k


def is_prime(p: int) -> bool:
    return p >= 2 and len(factor(p)) == 1 and factor(p).get(p) == 1


def ord16_mod_prime(p: int) -> int:
    if p == 2 or not is_prime(p):
        raise ValueError('p must be an odd prime')
    r = 16 % p
    k = 1
    while r != 1:
        r = (r * 16) % p
        k += 1
        if k > p-1:
            raise AssertionError('Fermat order bound violated')
    return k


def K_32_is_divisible(ell: int, p: int) -> bool:
    if ell < 1 or not is_prime(p):
        raise ValueError('ell>=1 and p prime')
    if p == 2:
        return True
    return pow(16, ell, p) == 1


def mixed_exponent(p: int, q: int) -> int:
    if p < 2 or q < 2:
        raise ValueError('p,q>=2')
    return 16 ** (p*q-1) + 1 - 16 ** (p-1) - 16 ** (q-1)


def multiplicative_defect_is_one(alpha: Fraction, h: int, p: int, q: int) -> bool:
    """Exact rational-alpha test for exp(2pi i h alpha D_(p,q)) == 1."""
    return (h * alpha * mixed_exponent(p,q)).denominator == 1


def toral_next(k0: int, k1: int) -> int:
    return 4352*k1 - 1048576*k0


def exact_mean_log_gcd_by_divisors(A: int) -> float:
    """Prime-power count formula for 1/A^2 sum_(n,m) log gcd(n,m)."""
    if A < 2:
        raise ValueError('A>=2')
    count = 0.0
    for q in range(2,2*A):
        f = factor(q)
        if len(f) != 1:
            continue
        p = next(iter(f))
        multiples = (2*A-1)//q - (A-1)//q
        count += log(p)*(multiples / A)**2
    return count


def direct_mean_log_gcd(A: int) -> float:
    return sum(log(gcd(n,m)) for n in range(A,2*A) for m in range(A,2*A)) / (A*A)


def direct_mean_compensation(A: int) -> float:
    return 2 * sum(log(prime_compensation_root(n,m))
                   for n in range(A,2*A) for m in range(A,2*A)) / (A*A)


def r_one_based(n: int) -> Fraction:
    """Authenticated signed BBP pole sum as a separately simplified rational form."""
    if n < 1:
        raise ValueError('n must be >=1')
    return Fraction(120*n*n-89*n+16,
                    (2*n-1)*(4*n-1)*(8*n-7)*(8*n-3))


def source_prefix_one_based(L: int) -> Fraction:
    if L < 1:
        raise ValueError('L>=1')
    return sum((r_one_based(n)/16**n for n in range(1,L+1)),Fraction(0))


def original_phase_fiber_interval(ell: int, h: int, L: int=32) -> tuple[Fraction,Fraction]:
    """Rigorous fractional bounds for h*(Y_(3ell)-Y_(2ell)), zero seed.

    Uses the independently simplified signed rational source and proved
    strict tail bound for pi/16; raises on undecidable integer carry.
    """
    if ell < 1 or h < 1 or L < 1:
        raise ValueError('require ell,h,L positive')
    P = source_prefix_one_based(L)
    eta = Fraction(1,16**L*(8*L+1)*(8*L+2))
    weight = h * (16**(3*ell) - 16**(2*ell))
    lo, hi = weight*P, weight*(P+eta)
    if lo//1 != hi//1:
        raise ValueError('enclosure crosses phase winding')
    return lo-(lo//1),hi-(hi//1)
