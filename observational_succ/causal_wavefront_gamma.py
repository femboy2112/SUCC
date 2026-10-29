"""Discrete causal wavefronts, exact harmonic pursuit clocks and Oily KL jets.

Research-only additive observer tools. All source dependencies are explicit.
A wavefront or entropy boundary is not a physical GR event horizon, a
Heisenberg uncertainty relation, or an RH/pi-normality theorem.

The authentic positive Oily kernel is R(x)=(1-x)L(x), with
L(x)=1/[(2-x*x)*(x*x-2*x+2)]. Its endpoint jet is Gamma(2,1).
The deflated comparison L(x) has Gamma(1,1). That comparison is a declared
mathematical control and not a claim of a second authenticated BBP forcing.
"""
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction as Q
from functools import lru_cache
from math import log, log2


@dataclass(frozen=True, order=True)
class Event:
    """One event in an explicit 1+1 finite-speed causal model (c=1)."""
    time: int
    position: int

    def __post_init__(self) -> None:
        if type(self.time) is not int or self.time < 0:
            raise ValueError("event time must be a nonnegative integer")
        if type(self.position) is not int:
            raise ValueError("position must be an integer")


def can_signal(source: Event, receiver: Event) -> bool:
    """There exists a path of speed <=1 from source to receiver."""
    dt = receiver.time - source.time
    return dt >= 0 and abs(receiver.position - source.position) <= dt


def frontier_event(t: int) -> Event:
    if type(t) is not int or t < 0:
        raise ValueError("frontier time must be nonnegative")
    return Event(t, t)


def max_speed_one_behind(t: int) -> Event:
    """Null-speed idealized tracker; physically timelike observer it is NOT."""
    if type(t) is not int or t < 1:
        raise ValueError("tracker time must be >=1")
    return Event(t, t-1)


@lru_cache(maxsize=512)
def harmonic(n: int) -> Q:
    if type(n) is not int or n < 0 or n > 20000:
        raise ValueError("0 <= harmonic index <= 20000 required")
    return sum((Q(1, j) for j in range(1, n+1)), Q(0))


def near_null_lag_discrete(n: int, alpha: Q=Q(1)) -> Q:
    """Initial front/observer positions 0/-1, sampled speed v_j=1-alpha/j.

    Then gap=1+alpha*H_n and each speed belongs to [0,1) for 0<alpha<=1.
    """
    alpha=Q(alpha)
    if not Q(0)<alpha<=1:
        raise ValueError("near-null parameter alpha must satisfy 0<alpha<=1")
    return Q(1) + alpha*harmonic(n)


def near_null_lag_continuous(n: int, alpha: Q=Q(1)) -> float:
    """Same t=0 position, continuously integrated v(t)=1-alpha/(1+t)."""
    alpha=Q(alpha)
    if not Q(0)<alpha<=1:
        raise ValueError("near-null parameter alpha must satisfy 0<alpha<=1")
    if type(n) is not int or n < 0:
        raise ValueError("n must be nonnegative integer")
    return 1+float(alpha)*log(n+1)


def sampled_clock_gap(n: int, alpha: Q=Q(1)) -> float:
    """Harmonic left-sum minus exact integral, asymptotically alpha*gamma."""
    return float(near_null_lag_discrete(n, alpha))-near_null_lag_continuous(n, alpha)


def standard_binary_entropy(p: Q) -> float:
    """Shannon entropy of a Bernoulli innovation in bits; declared source law."""
    p=Q(p)
    if not 0<=p<=1:
        raise ValueError("probability must lie in [0,1]")
    if p==0 or p==1:
        return 0.0
    x=float(p)
    return -x*log2(x)-(1-x)*log2(1-x)


def uniform_frontier_residual_bound(m: int, probes: int) -> int:
    """Uniform fresh m-bit frontier and at-most-k binary report bits:

    H(Z | reports) >= max(0,m-k) bits (Shannon chain rule).
    Equality is achieved by independently reporting k of the m frontier bits.
    This does not assert the observer can causally access the current frontier.
    """
    if type(m) is not int or type(probes) is not int or m < 0 or probes < 0:
        raise ValueError("nonnegative integer bit budgets required")
    return max(0, m-probes)


def original_oily_L_at(x: Q) -> Q:
    """Oily endpoint kernel after dividing out its canonical simple zero.

    Source: R(x)=(1-x)/[(2-x²)(x²-2x+2)]. Exact on [0,1].
    """
    x=Q(x)
    if not 0<=x<=1:
        raise ValueError("x must lie on source interval [0,1]")
    return Q(1)/((2-x*x)*(x*x-2*x+2))


def original_oily_R_at(x: Q) -> Q:
    x=Q(x)
    return (1-x)*original_oily_L_at(x)


def finite_beta_jet_kl(a: int) -> tuple[float,float,Q]:
    """For P0=Beta(a+1,1) and P1=Beta(a+1,2), a>=0.

    Exact analytic identities:
      D(P0||P1)=H_(a+1)-log(a+2) -> gamma,
      D(P1||P0)=1+log(a+2)-H_(a+2) -> 1-gamma,
      J(P0,P1)=(a+1)/(a+2) exactly.
    """
    if type(a) is not int or not 0<=a<=19998:
        raise ValueError("a must be integer 0..19998")
    h=harmonic(a+1)
    k=harmonic(a+2)
    forward=float(h)-log(a+2)
    reverse=1+log(a+2)-float(k)
    return forward,reverse,Q(a+1,a+2)


def gamma_jet_symmetric_divergence(k: int) -> Q:
    """For consecutive Gamma(k,1) and Gamma(k+1,1), J=1/k exactly."""
    if type(k) is not int or k<1:
        raise ValueError("Gamma shape k>=1 required")
    return Q(1,k)


def pell_boost_certificate(m: int) -> tuple[Q,Q,Q]:
    """Quadratic Pisot unit beta=(m+sqrt(m²+4))/2 as a rapidity scale.

    Return cosh(chi)^2, sinh(chi)^2, velocity^2 for chi=log(beta).
    All exact rational; no physical velocity/source relationship is inferred.
    """
    if type(m) is not int or m<1:
        raise ValueError("m>=1 required")
    return Q(m*m+4,4),Q(m*m,4),Q(m*m,m*m+4)


def pell_lorentz_null_identity(m: int) -> bool:
    """cosh²(chi)-sinh²(chi)=1 for declared Pisot-frame embedding."""
    c2,s2,_=pell_boost_certificate(m)
    return c2-s2==1
