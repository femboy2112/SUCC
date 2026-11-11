"""Exact finite arithmetic probes for SUCC's prime/Archimedean BBP bridge.

No zeta-zero locations, RH oracle, pi digit oracle, or full-suite imports.
Finite identities use Fraction; trigonometric phase calculations are not certified here.
"""
from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
from math import gcd, log


def factor(n: int) -> dict[int,int]:
    if n < 1:
        raise ValueError('positive integer only')
    ans = {}
    p = 2
    while p*p <= n:
        while n%p == 0:
            ans[p] = ans.get(p, 0) + 1
            n //= p
        p += 1
    if n > 1:
        ans[n] = ans.get(n, 0) + 1
    return ans


def prime_power(q: int) -> tuple[int,int] | None:
    if q < 2:
        return None
    f = factor(q)
    if len(f) != 1:
        return None
    return next(iter(f.items()))


def logn_basis(n: int) -> dict[int,int]:
    return factor(n)


def arithmetic_defect(n: int, sequence) -> dict[int, Fraction]:
    """log(n)*a(n) - sum_(d|n) Lambda(d)a(n/d), coefficient of log p."""
    a = sequence(n)
    out = {}
    for p, exponent in factor(n).items():
        out[p] = sum((a - sequence(n//(p**k)) for k in range(1, exponent+1)), Fraction(0))
    return out


def mobius(n: int) -> int:
    f = factor(n)
    if any(k>1 for k in f.values()):
        return 0
    return (-1)**len(f)


def mobius_convolution_a(n: int, sequence) -> Fraction:
    return sum((mobius(d)*sequence(n//d) for d in range(1,n+1) if n%d == 0), Fraction(0))


def dirichlet_coeff_zeta_times_mobius(n: int, sequence) -> Fraction:
    return sum((mobius_convolution_a(d,sequence) for d in range(1,n+1) if n%d==0), Fraction(0))


def ordered_prime_power_edges(indices) -> dict[int,list[tuple[int,int]]]:
    """Map q=p^k to all directed pairs (m,n) with n=q*m, in finite I."""
    s = set(indices)
    result = defaultdict(list)
    for m in sorted(s):
        for n in sorted(s):
            if n <= m or n % m: continue
            q = n // m
            if prime_power(q) is not None:
                result[q].append((m,n))
    return dict(result)


def all_ratios(indices) -> set[Fraction]:
    s = set(indices)
    return {Fraction(n,m) for n in s for m in s if n>m}


def normalized_primitive_coefficient(indices, phases) -> dict[int, Fraction]:
    """Exact coefficients BEFORE (2*kappa(0)*log(p)/sqrt(q)); phases rational here."""
    edges = ordered_prime_power_edges(indices)
    return {q:sum((phases(n)*phases(m)/Fraction(n*m) for m,n in pairs),Fraction(0)) for q,pairs in edges.items()}


def six_diamond(m: int) -> list[int]:
    if m < 1: raise ValueError('m >= 1')
    return [m,2*m,3*m,6*m]


def holonomy_fraction(phases: dict[int,Fraction], circuit: list[int]) -> Fraction:
    """Real phase exponent around the closed circuit modulo 1."""
    if len(circuit)<2 or circuit[0]!=circuit[-1]:
        raise ValueError('cycle must be closed')
    s = sum((phases[v]-phases[u] for u,v in zip(circuit,circuit[1:])),Fraction(0))
    return s % 1


def phase_six_mixed_difference(phases: dict[int,Fraction], m: int) -> Fraction:
    return phases[6*m]-phases[2*m]-phases[3*m]+phases[m]


def original_four_pole_R(j: int) -> Fraction:
    if j < 0: raise ValueError('j >= 0')
    return Fraction(4,8*j+1)-Fraction(2,8*j+4)-Fraction(1,8*j+5)-Fraction(1,8*j+6)


def original_zero_prefix(L:int) -> Fraction:
    if L<0: raise ValueError('L >= 0')
    return sum((original_four_pole_R(j) / (16**(j+1)) for j in range(L)), Fraction(0))


def prime_pair_log_ratio(n: int,p:int) -> Fraction:
    """Integer-lift factor in Y_(pn)-Y_n = Y_n*(16^((p-1)n)-1)."""
    if n<1 or p<2: raise ValueError('bad n or p')
    return Fraction(16**((p-1)*n)-1)


def ensure_rational_compiler_carry(L:int, n:int, h:int=1):
    """Finite-horizon phase without exponentiation of a complex number.
    For seed s=-P_L, Y_n^L(s)=0. For s=0, Y_n^L = 16^n P_L.
    """
    P=original_zero_prefix(L)
    return Fraction(16**n)*P, Fraction(16**n)*(-P+P)



def phase_interval(n: int, L:int=12) -> tuple[Fraction, Fraction]:
    """Certified fractional interval of Y_n=16^n*pi/16, using original BBP tail.

    Returns rational lower and upper and *requires* no integer winding within
    the enclosure, rather than silently dropping carries.
    """
    if n < 1 or L < 1:
        raise ValueError('positive n,L')
    base = original_zero_prefix(L)
    tail = Fraction(1,16**L*(8*L+1)*(8*L+2))
    low,high=16**n*base,16**n*(base+tail)
    if low//1 != high//1:
        raise ValueError('phase interval crosses integer winding')
    return low-low//1, high-high//1


def phase_difference_interval(m:int,n:int,L:int=12) -> tuple[Fraction,Fraction]:
    """Certified fractional interval of Y_n-Y_m; test 1<=m<n."""
    if m<1 or n<=m:
        raise ValueError('require 1<=m<n')
    base=original_zero_prefix(L)
    tail=Fraction(1,16**L*(8*L+1)*(8*L+2))
    scale=16**n-16**m
    low,high=scale*base,scale*(base+tail)
    if low//1 != high//1:
        raise ValueError('phase difference crosses integer winding')
    return low-low//1, high-high//1
