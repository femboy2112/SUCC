"""Generalized Euler--Mascheroni SUCC/cell/prime/adelic boundary probes.

Finite rational calculations are exact. Holomorphic continuation, Euler products,
Poisson summation, Basel, and prime-number asymptotics are CLASSICAL IMPORTS.
No RH, pi normality, physical source or Weil-positivity proof is claimed.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q
from math import isqrt, lcm, log


class GeneralizedEulerError(ValueError):
    """Invalid source, index, truncation, normalization or analytic domain."""


def _index(x: int, minimum: int, maximum: int = 100_000) -> int:
    if type(x) is not int or not minimum <= x <= maximum:
        raise GeneralizedEulerError(f"expected integer between {minimum} and {maximum}")
    return x


def primes_through(cutoff: int) -> tuple[int, ...]:
    """Genuine primes only, not independent composite factors."""
    _index(cutoff, 2, 100_000)
    sieve = bytearray(b"\x01") * (cutoff + 1)
    sieve[0:2] = b"\x00\x00"
    for p in range(2, isqrt(cutoff) + 1):
        if sieve[p]:
            sieve[p*p:cutoff+1:p] = b"\x00" * ((cutoff - p*p)//p + 1)
    return tuple(p for p in range(2, cutoff+1) if sieve[p])


def cell_defect_exact(power: int, n: int) -> Q:
    """n^-r - integral_n^(n+1) x^-r dx exactly for integer r=0 or r>=2."""
    _index(power, 0, 20)
    _index(n, 1)
    if power == 1:
        raise GeneralizedEulerError("power 1 uses log((n+1)/n), not rational")
    if power == 0:
        return Q(0)
    area = (Q(1, n**(power-1)) - Q(1, (n+1)**(power-1))) / (power-1)
    return Q(1, n**power) - area


@dataclass(frozen=True)
class RationalCellCertificate:
    """Exact enclosure of zeta(r)-1/(r-1) for integer r>=2."""
    power: int
    cutoff: int
    lower: Q
    upper: Q
    tail_leq: Q


def cell_certificate(power: int, cutoff: int) -> RationalCellCertificate:
    """Delta_r(n)>=0 and Delta_r(n)<=r/(2n^(r+1)), tail<=1/(2N^r)."""
    _index(power, 2, 12)
    _index(cutoff, 1, 5_000)
    lower = sum((cell_defect_exact(power, n) for n in range(1, cutoff+1)), Q(0))
    tail = Q(1, 2*cutoff**power)
    return RationalCellCertificate(power, cutoff, lower, lower+tail, tail)


def literal_zero_power(cutoff: int) -> Q:
    """User's original H_N^(0) - integral_1^N 1 dx equals 1 for every N."""
    _index(cutoff, 1)
    return Q(cutoff) - Q(cutoff-1)


def analytically_continued_zero_power() -> Q:
    """zeta(0)-1/(0-1)=-1/2+1=1/2 (classical continuation)."""
    return Q(1, 2)


def _mp():
    try:
        import mpmath as mp
    except ImportError as exc:
        raise GeneralizedEulerError("mpmath needed for numeric diagnostics") from exc
    return mp


def finite_succ_defect(s, cutoff: int, dps: int = 50):
    """Original finite H_N^(s) - integral_1^N x^-s; NUMERIC diagnostic."""
    _index(cutoff, 1, 100_000)
    _index(dps, 20, 150)
    mp = _mp()
    with mp.workdps(dps):
        z = mp.mpc(s)
        total = mp.fsum(mp.power(n, -z) for n in range(1, cutoff+1))
        integral = mp.log(cutoff) if z == 1 else mp.expm1((1-z)*mp.log(cutoff))/(1-z)
        return +(total-integral)


def continued_gamma(s, dps: int = 50):
    """Entire G(s)=zeta(s)-1/(s-1), not the original limit for Re(s)<=0."""
    _index(dps, 20, 150)
    mp = _mp()
    with mp.workdps(dps):
        z = mp.mpc(s)
        return +(mp.euler if z == 1 else mp.zeta(z)-1/(z-1))


def hurwitz_mesh_limit(s, q, h=1, dps: int = 50):
    """Aligned-cell chart h^-s[zeta(s,q)-q^(1-s)/(s-1)].

    Original finite chart: sum_{k=0}^{N-1}(h(q+k))^-s minus
    h^-1 integral_{hq}^{h(q+N)} x^-s dx.
    At s=1: [-digamma(q)+log(q)]/h.
    """
    _index(dps, 20, 150)
    mp = _mp()
    with mp.workdps(dps):
        z = mp.mpc(s)
        q, h = mp.mpf(q), mp.mpf(h)
        if q <= 0 or h <= 0:
            raise GeneralizedEulerError("positive starting chart and mesh required")
        if z == 1:
            return +((-mp.digamma(q)+mp.log(q))/h)
        return +(mp.power(h, -z)*(mp.zeta(z, q)-mp.power(q, 1-z)/(z-1)))


def finite_hurwitz_mesh(s, q, h, cutoff: int, dps: int = 50):
    """Finite aligned-cell source; NOT the user's original N-1-cell endpoint."""
    _index(cutoff, 1, 100_000)
    _index(dps, 20, 150)
    mp = _mp()
    with mp.workdps(dps):
        z = mp.mpc(s)
        q, h = mp.mpf(q), mp.mpf(h)
        if q <= 0 or h <= 0:
            raise GeneralizedEulerError("positive chart parameters required")
        total = mp.fsum(mp.power(h*(q+k), -z) for k in range(cutoff))
        area = (mp.log((q+cutoff)/q)/h if z == 1 else
                mp.power(h,-z)*(mp.power(q+cutoff,1-z)-mp.power(q,1-z))/(1-z))
        return +(total-area)


def euler_product_exact(power: int, cutoff: int, *, fake_composite: int | None = None) -> Q:
    """Finite genuine-prime Euler product; injected composite is LABELLED MUTANT."""
    _index(power, 2, 12)
    _index(cutoff, 2, 100_000)
    out = Q(1)
    for p in primes_through(cutoff):
        out *= Q(p**power, p**power-1)
    if fake_composite is not None:
        _index(fake_composite, 4, 10_000)
        if fake_composite in primes_through(fake_composite):
            raise GeneralizedEulerError("mutation must be composite")
        out *= Q(fake_composite**power, fake_composite**power-1)
    return out


@dataclass(frozen=True)
class CofinalPrimeSchedule:
    denominator: int
    epsilon: Q
    cutoff: int
    proved_absolute_euler_error_leq: Q


def cofinal_prime_schedule(denominator: int) -> CofinalPrimeSchedule:
    """X=q^(2q), eps=1/q; 0<=zeta(1+eps)-P_X(1+eps)<=1/q.

    Every n<=X is X-smooth. Missing Dirichlet terms are bounded by
    sum_{n>X} n^-(1+eps) <= X^-eps/eps = 1/q. No PNT required.
    """
    _index(denominator, 2, 32)
    q = denominator
    return CofinalPrimeSchedule(q,Q(1,q),q**(2*q),Q(1,q))


def prime_euler_diagnostic(s, cutoff: int, dps: int = 50):
    """Numeric true-prime P_X(s); requires Re(s)>1. No proof by sampling."""
    _index(cutoff, 2, 100_000)
    _index(dps, 20, 150)
    mp = _mp()
    with mp.workdps(dps):
        z = mp.mpc(s)
        if z.real <= 1:
            raise GeneralizedEulerError("Euler product needs Re(s)>1")
        return +mp.fprod(1/(1-mp.power(p,-z)) for p in primes_through(cutoff))


def theta_balanced_integral(s, modes: int = 7, dps: int = 50):
    """Numeric diagnostic for completed Poisson/theta balanced remainder.

    B(s)=integral_1^inf sum_{n>=1} exp(-pi*n^2*t)
       [t^(s/2)+t^((1-s)/2)] dt/t.
    The all-mode identity B(s)=Lambda(s)-1/(s-1)+1/s is CLASSICAL.
    """
    _index(modes, 1, 12)
    _index(dps, 20, 100)
    mp = _mp()
    with mp.workdps(dps):
        z = mp.mpc(s)
        def f(t):
            heat = mp.fsum(mp.exp(-mp.pi*n*n*t) for n in range(1,modes+1))
            return heat*(mp.power(t,z/2)+mp.power(t,(1-z)/2))/t
        return +mp.quad(f,[1,mp.inf])


def theta_balanced_completed(s, dps: int = 50):
    """Numeric completed-zeta with both poles removed at 0 and 1."""
    _index(dps,20,150)
    mp = _mp()
    with mp.workdps(dps):
        z = mp.mpc(s)
        if z == 0 or z == 1:
            return +(1+mp.euler/2-mp.log(2*mp.sqrt(mp.pi)))
        arch = mp.power(mp.pi,-z/2)*mp.gamma(z/2)
        return +(arch*mp.zeta(z)-1/(z-1)+1/z)


def clock_jump(n: int) -> int:
    """lcm(1..n)/lcm(1..n-1): 1 off prime powers, p at n=p^k."""
    _index(n,2,1_000)
    prev = lcm(*range(1,n))
    current = lcm(prev,n)
    return current//prev


def clock_gamma_diagnostic(cutoff: int) -> float:
    """log(N)-sum_{n<=N}Lambda(n)/n via exact LCM jumps; uses PNT."""
    _index(cutoff,2,700)
    return log(cutoff)-sum(log(clock_jump(n))/n for n in range(2,cutoff+1))


def positive_type_hostile_zero(dps: int = 50):
    """2+cos(t) positive definite and positive on R, yet off-axis zero.

    2+cos(t_i-t_j)=2*1_i*1_j+cos(t_i)*cos(t_j)+sin(t_i)*sin(t_j).
    z=pi+i*acosh(2) yields 2+cos(z)=0.
    """
    _index(dps,20,150)
    mp=_mp()
    with mp.workdps(dps):
        z=mp.pi+1j*mp.acosh(2)
        return {"zero":+z,"residual":+(2+mp.cos(z))}


def pi_squared_from_cells(cutoff: int) -> tuple[Q,Q]:
    """Exact rational pi^2 interval using classical Basel identity as IMPORT."""
    cert=cell_certificate(2,cutoff)
    return 6*(1+cert.lower),6*(1+cert.upper)


def certified_pi_hex_prefix(cutoff: int, digits: int) -> str | None:
    """Certified base-16 prefix from rational endpoint square roots, no pi input.

    Basel theorem is an EXTERNAL prerequisite. No frequency/normality result.
    """
    _index(digits,1,12)
    scale=16**digits
    lo,hi=pi_squared_from_cells(cutoff)
    bottom=isqrt((lo.numerator*scale*scale)//lo.denominator)
    top=isqrt((hi.numerator*scale*scale)//hi.denominator)
    if bottom!=top:
        return None
    return f"{bottom//scale:X}.{bottom%scale:0{digits}X}"


def symmetric_functional_equation_mutant(s: Q, exponent: int = 2, weight: Q = Q(1,10)) -> Q:
    """Non-authentic 1+c[s(1-s)]^k keeps reflection and finite Laurent jets."""
    _index(exponent,2,30)
    if not isinstance(s,Q) or not isinstance(weight,Q):
        raise GeneralizedEulerError("exact rational source and mutation weight required")
    return Q(1)+weight*(s*(1-s))**exponent
