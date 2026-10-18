"""Source-typed exact arithmetic of inverted Nyman--Beurling modular clocks.

Research-only. The Bernoulli/Haar tail covariance is NOT the full L2 Gram.
No critical-line zeros, zeta values, or RH claim are inputs.
"""
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction as F
from math import gcd, lcm


class CutSourceError(ValueError):
    """Source/precision/horizon/observation certificate unavailable."""


def rat(x):
    if type(x) not in (int, F):
        raise CutSourceError("rational source inputs required (no floats/bools)")
    return F(x)


def small_n(n, maximum=2500):
    if type(n) is not int or not 1 <= n <= maximum:
        raise CutSourceError(f"1 <= exact integer <= {maximum} required")
    return n


def divisors(n):
    small_n(n)
    return tuple(d for d in range(1, n + 1) if n % d == 0)


def mobius(n):
    small_n(n)
    if n == 1:
        return 1
    primes = 0
    x = n
    p = 2
    while p * p <= x:
        if x % p == 0:
            x //= p
            if x % p == 0:
                return 0
            primes += 1
        p += 1
    if x > 1:
        primes += 1
    return -1 if primes % 2 else 1


def jordan_two(n):
    """J_2 = mu * id^2; positive for all n>=1, no prime oracle."""
    return sum(mobius(n // d) * d * d for d in divisors(n))


def phi(n):
    """phi = mu * id, derived from divisor inversion (not a prime oracle)."""
    return sum(mobius(n // d) * d for d in divisors(n))


def clock_lcm(indices):
    if type(indices) is not tuple or not indices:
        raise CutSourceError("finite nonempty tuple of observed clock periods")
    periods = tuple(small_n(n, maximum=160) for n in indices)
    out = 1
    for n in periods:
        out = lcm(out, n)
    return out


def bernoulli_clock_covariance(m, n):
    """Mean_[0,L]({x/m}{x/n}) = 1/4 + gcd^2/(12mn)."""
    small_n(m); small_n(n)
    return F(1, 4) + F(gcd(m, n) ** 2, 12 * m * n)


def gcd_square_kernel(m, n):
    small_n(m); small_n(n)
    return F(gcd(m, n)**2, m*n)


def signed_coefficients(coeffs):
    if type(coeffs) is not tuple or not 1 <= len(coeffs) <= 24:
        raise CutSourceError("finite tuple of <=24 source coefficients")
    return tuple(rat(c) for c in coeffs)


def square_root_tail_energy(coeffs):
    """EXACT arithmetic square root of periodic upper-cut error numerator.

    A_c(x) = 1 - sum_{n=1}^N c_n {x/n}, periodic with L=lcm(1..N).
    mean(A_c^2)=(1-sum c/2)^2 + (1/12)sum_d J2(d)(sum_{d|n}c_n/n)^2.
    """
    c = signed_coefficients(coeffs)
    N = len(c)
    bias = F(1) - sum(c, F(0)) / 2
    incidence = tuple(sum((c[n-1] / n for n in range(d, N+1, d)), F(0))
                      for d in range(1, N+1))
    square_terms = tuple(F(jordan_two(d), 12)*x*x for d, x in enumerate(incidence, 1))
    if any(term < 0 for term in square_terms):
        raise AssertionError("Jordan two positivity failure")
    value = bias*bias+sum(square_terms, F(0))
    return {"value": value, "bias": bias, "incidence": incidence,
            "nonnegative_squares": square_terms, "RH_proved": False,
            "source": "finite clock Haar/Bernoulli; not full L2 norm"}


def clock_period_integral(coeffs, *, max_period=50000):
    """Independent exact finite-clock cell integration; no divisor/Jordan identity.

    For each cell [k,k+1], A(x)=u_k - v x; integrate via midpoint.
    Period L may be exponentially expensive, so enforce a budget.
    """
    c = signed_coefficients(coeffs)
    L = clock_lcm(tuple(range(1, len(c)+1)))
    if L > max_period:
        raise CutSourceError("materialized CRT clock exceeds declared state budget")
    v = sum((a/n for n,a in enumerate(c,1)), F(0))
    total = F(0)
    for k in range(L):
        u = F(1)+sum((a*(k//n) for n,a in enumerate(c,1)), F(0))
        total += (u - v*F(2*k+1,2))**2 + v*v/12
    return {"period": L, "mean_square": total/L,
            "materialized_states": L, "RH_proved": False}


def clock_tail_optimum(N):
    """Exact best periodic *tail numerator*; not best full Hilbert residual.

    S_N = 1^T K_N^{-1}1 = sum_{n<=N} phi(n)^2 / J_2(n)
    minimum = 1/(1+3S_N); coefficients solve normal equations.
    """
    small_n(N,maximum=24)
    S = sum((F(phi(n)**2, jordan_two(n)) for n in range(1,N+1)), F(0))
    low = F(1, 1+3*S)
    # u=K^{-1}1 = D E^{-T}J^{-1} E^{-1}D 1.
    # E^{-1}D1 = phi. E^{-T}v(n)=sum_{k:n|k}mu(k/n)v(k).
    u = tuple(n*sum((F(mobius(k//n)*phi(k), jordan_two(k))
                     for k in range(n,N+1,n)),F(0)) for n in range(1,N+1))
    c = tuple(6*low*x for x in u)
    actual = square_root_tail_energy(c)["value"]
    if actual != low:
        raise AssertionError("arithmetic optimum does not saturate square root")
    return {"N":N,"S":S,"minimum":low,"coefficients":c,
            "calibrated_energy":actual,"RH_proved":False,
            "not_full_Hilbert_optimum":True}


def log_one_plus_one_over(k, terms=12):
    """Certified rational interval for log((k+1)/k), arctanh series.

    z=1/(2k+1), log((1+z)/(1-z))=2 sum z^(2j+1)/(2j+1).
    A positive remainder is <=2*z^(2T+1)/((2T+1)(1-z^2)).
    """
    small_n(k,maximum=10000)
    if type(terms) is not int or not 2 <= terms <= 36:
        raise CutSourceError("2..36 Taylor terms required")
    z = F(1, 2*k+1)
    low = 2*sum((z**(2*j+1)/(2*j+1) for j in range(terms)),F(0))
    remainder = 2*z**(2*terms+1)/((2*terms+1)*(1-z*z))
    return low,low+remainder


def certified_cut_residual(coeffs, R=24, terms=12):
    """Exact-rational enclosure of TRUE squared L2 upper-cut residual.

    Upper cut h=1_{x>1}/x, clock g_n={x/n}/x (J of fractional dilate).
    On [0,1]: error=-sum(c_n/n).
    On [k,k+1], k>=1: error=a_k/x-b, a_k=1+sum c_n floor(k/n),
    b=sum c_n/n. Tail is bounded by (1+sum|c|)^2/R and also by
    alpha/(R+L) <= tail <= alpha*(1/R+L/R^2), where alpha is the
    exact periodic mean-square of A(x)=1-sum c_n {x/n}.
    WARNING: these are *trial bounds*, not certified optimal projection distances.
    """
    c=signed_coefficients(coeffs)
    if type(R) is not int or not 2 <= R <= 10000:
        raise CutSourceError("2..10000 finite observation radius required")
    b=sum((a/n for n,a in enumerate(c,1)), F(0))
    low=b*b
    high=b*b
    for k in range(1,R):
        a=F(1)+sum((v*(k//n) for n,v in enumerate(c,1)), F(0))
        lnlo,lnhi=log_one_plus_one_over(k,terms=terms)
        exact=a*a*F(1,k*(k+1))+b*b
        mult=-2*a*b
        if mult>=0:
            low += exact+mult*lnlo
            high += exact+mult*lnhi
        else:
            low += exact+mult*lnhi
            high += exact+mult*lnlo
    if low < 0:
        # A negative outward LOWER is a legal bound; true integral still >=0.
        low=max(F(0),low)
    L=clock_lcm(tuple(range(1,len(c)+1)))
    alpha=square_root_tail_energy(c)["value"]
    tail_lower = alpha/F(R+L)
    tail_upper = min((F(1)+sum((abs(v) for v in c),F(0)))**2/F(R),
                     alpha*(F(1,R)+F(L,R*R)))
    if not 0<=tail_lower<=tail_upper:
        raise AssertionError("incorrect periodic tail enclosure")
    return {"lower":low+tail_lower,"upper":high+tail_upper,
            "finite_lower":low,"finite_upper":high,
            "tail_lower":tail_lower,"tail_upper":tail_upper,
            "period":L,"tail_Haar_alpha":alpha,
            "unit_interval_obstruction":b*b,
            "source":"full upper-cut L2 trial; interval precision and positive tail",
            "optimal_projection_certified":False,"RH_proved":False}


def inverted_clock_value(n, x):
    """Exact x^{-1}{x/n}; strictly x>0 (fractional part via floor)."""
    small_n(n)
    q=rat(x)
    if q<=0:
        raise CutSourceError("positive argument required")
    v=q/n
    return (v - (v.numerator//v.denominator)) /q


def forward_fractional_value(n,x):
    small_n(n)
    q=rat(x)
    if q<=0:
        raise CutSourceError("positive argument required")
    v=1/(n*q)
    return v-(v.numerator//v.denominator)


def reflected_fractional_value(n,x):
    q=rat(x)
    return forward_fractional_value(n,1/q)/q


@dataclass(frozen=True)
class SourcePassport:
    """Explicit mathematical/source declaration; NOT physical attestation."""
    source_id:str
    epoch:int
    authorized_clocks:tuple[int,...]

    def __post_init__(self):
        if type(self.source_id) is not str or not self.source_id:
            raise CutSourceError("source ID declaration required")
        if type(self.epoch) is not int or self.epoch < 0:
            raise CutSourceError("epoch declaration must be a nonnegative integer")
        if type(self.authorized_clocks) is not tuple or not self.authorized_clocks:
            raise CutSourceError("nonempty finite clock passport required")
        if self.authorized_clocks != tuple(sorted(set(self.authorized_clocks))):
            raise CutSourceError("sorted unique observed clocks required")
        for n in self.authorized_clocks:
            small_n(n)

    def require_prefix(self,N):
        small_n(N)
        expected=tuple(range(1,N+1))
        if self.authorized_clocks[:N] != expected:
            raise CutSourceError("missing source-authenticated finite clock index")
        return True
