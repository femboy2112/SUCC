"""Authentic BBP natural-orbit lag bridge and cyclotomic prime-clock costs.

A source-specific exact/finitely tested *reduction* toward normality.  No
source-selected Fourier saving, pi normality, or independence proof is asserted.
The original BBP rational forcing, integer carrier clock and lift are fixed.
"""
from __future__ import annotations

from fractions import Fraction as Q
from math import gcd, isqrt, lcm

from .bbp_natural_carrier import exact_forcing, forcing_numerator, forcing_denominator


def _integer(value: int, lower: int = 0) -> int:
    if type(value) is not int or value < lower:
        raise ValueError(f"exact integer >= {lower} required")
    return value


def _prime(p: int) -> int:
    _integer(p, 2)
    if any(p % d == 0 for d in range(2, isqrt(p) + 1)):
        raise ValueError("prime required")
    return p


def forcing_upper_remainder(j: int) -> int:
    """15D(j)-64(j-1)^2P(j)>0 for every j>=2 (integer certificate)."""
    _integer(j, 2)
    return (15 * forcing_denominator(j)
            - 64 * (j-1)**2 * forcing_numerator(j))


def lag_source(j: int, lag: int) -> Q:
    """R_{j,k}=U_{j+k}-16^k U_j, source-only, positive rational.

    Exact recurrence, not the circle or an independent-prime model.
    """
    _integer(j, 1); _integer(lag, 1)
    return sum((16**(lag-t)*exact_forcing(j+t)
                for t in range(1, lag+1)), Q())


def lag_positive_upper(j: int, lag: int) -> Q:
    """Strict SHARP-AS-j->infinity R_{j,k}<(16^k-1)/(64*j^2), k fixed."""
    _integer(j, 1); _integer(lag, 1)
    return Q(16**lag-1, 64*j*j)


def lag_window_upper(start: int, length: int, lag: int) -> Q:
    """Finite exact rational certificate on sum R_{n,k} across a window."""
    _integer(start, 1); _integer(length); _integer(lag, 1)
    return Q(16**lag-1, 64) * sum(
        (Q(1, n*n) for n in range(start,start+length)), Q())


def lag_window_geometric_upper(start: int, lag: int) -> Q:
    """Uniform in window length. Finite sum <= 1/(start-1), start>=2."""
    _integer(start, 2); _integer(lag, 1)
    return Q(16**lag-1, 64*(start-1))


def fourier_lag_rational_upper(h: int, start: int, length: int, lag: int) -> Q:
    """Majorizes |sum(e(h(U_(n+k)-U_n))-e(h(16^k-1)U_n))|.

    Uses 2*pi<44/7; rational-only triangle bound, not a computed Fourier sum.
    """
    _integer(start, 1); _integer(length); _integer(lag, 1)
    if type(h) is not int: raise ValueError("integer Fourier frequency required")
    return min(Q(2*length), Q(44*abs(h), 7)*lag_window_upper(start,length,lag))


def source_circle_prefix(length: int) -> tuple[Q, ...]:
    """Exact phases y_0,...,y_length from the ONE natural-number source."""
    _integer(length)
    x=Q()
    output=[x]
    for j in range(1,length+1):
        x=(16*x+exact_forcing(j))%1
        output.append(x)
    return tuple(output)


def exact_lag_phase_defect(phases: tuple[Q, ...], n: int, lag: int) -> Q:
    """Circle angle defect (always 0) after accounting for true forcing."""
    _integer(n, 1);_integer(lag, 1)
    if n+lag>=len(phases): raise ValueError("source window unavailable")
    return (phases[n+lag]-16**lag*phases[n]-lag_source(n,lag))%1


def multiplicative_order_16(p: int, depth: int) -> int:
    """Exact elementary order modulo p**depth; odd primes only."""
    _prime(p);_integer(depth, 1)
    if p == 2:raise ValueError("16 not invertible modulo 2")
    modulus = p**depth
    x=16%modulus
    order=1
    while x!=1:
        x=x*16%modulus
        order+=1
    return order


def clock_blind_lag(prime_depths: tuple[tuple[int,int], ...]) -> int:
    """Least positive lag k for which 16^k=1 mod each chosen p^depth.

    This annihilates the chosen bounded-depth primary torsion characters at
    lag frequency 16^k-1; it does NOT annihilate unbounded deeper terms.
    """
    if type(prime_depths) is not tuple or not prime_depths:
        raise ValueError("nonempty tuple of distinct odd prime/depth pairs required")
    ps=set()
    result=1
    for p,b in prime_depths:
        _prime(p);_integer(b, 1)
        if p==2 or p in ps:raise ValueError("distinct odd primes required")
        ps.add(p)
        result=lcm(result,multiplicative_order_16(p,b))
    return result


def special_clock_valuation(p: int, lag: int) -> int:
    """Source-cyclotomic valuation v_p(16^lag-1) at p=3,5,7,13.

    The clauses implement the relevant LTE statements but are checked
    independently against literal integer exponentiation in tests.
    """
    _integer(lag,1)
    if p not in (3,5,7,13):raise ValueError("supported clocks 3,5,7,13")
    if p in (7,13):
        if lag % 3: return 0
        lag//=3
    a=1
    while lag%p==0:
        lag//=p; a+=1
    return a


def resonance_frequency(phases: tuple[Q, ...]) -> int:
    """Exact finite coherent Fourier resonance h: h*y_n is integral for all n.

    A refutation of a frequency-uniform Weyl bound.  The frequency depends
    on the whole finite window and grows; it does not refute fixed-h Weyl.
    """
    if type(phases) is not tuple or not phases:
        raise ValueError("nonempty exact phase tuple required")
    result=1
    for x in phases:
        if type(x) is not Q:raise ValueError("exact Fraction states required")
        result=lcm(result,x.denominator)
    return result


def gaussian_vdc_certificate(steps: tuple[tuple[int,int], ...], H: int) -> tuple[Q,Q]:
    """Exact classical van der Corput inequality, rational Gaussian entries.

    Return (|S|^2, RHS). No Fourier approximation, no floating arithmetic.
    H in [1,N]. Works for arbitrary rational Gaussian sequences, not just
    unit-circle sequences. C_k = sum z_(n+k)*conj(z_n).
    """
    n=len(steps)
    _integer(H,1)
    if H>n or n==0 or any(type(a) is not int or type(b) is not int for a,b in steps):
        raise ValueError("nonempty integral Gaussian sequence and 1<=H<=N required")
    R=sum(a for a,b in steps)
    I=sum(b for a,b in steps)
    lhs=Q(R*R+I*I)
    energy=sum(a*a+b*b for a,b in steps)
    block=H*energy
    for k in range(1,H):
        re=sum(steps[j+k][0]*steps[j][0]+steps[j+k][1]*steps[j][1]
               for j in range(n-k))
        block+=2*(H-k)*re
    rhs=Q((n+H-1)*block,H*H)
    return lhs,rhs


def fourier_log_schedule(N: int) -> int:
    """Explicit slowly growing proof schedule H=floor(log_16 N /2).

    H->infinity and 16^H<=sqrt(N). Not by itself a Fourier estimate.
    """
    _integer(N,256)
    h=1
    while 16**(2*(h+1))<=N:
        h+=1
    return h
