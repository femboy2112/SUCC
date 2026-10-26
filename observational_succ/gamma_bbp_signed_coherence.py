"""Signed Gamma/BBP moment covariances and summable authentic Weyl tails.

Source is the original Coherent Main X BBP recurrence; no pi values or zeros
are inputs. All finite certificates use Fraction. Paper results invoke positive
integral representations and the classical BBP identity pi=sum 16^-k r(k+1).

The signed zero-moment bridge does NOT prove signed π-orbit cancellation,
normality, RH, or physical quantum-vacuum effects.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q

from .zero_one_gamma_bridge import (
    GammaBridgeError, RationalInterval, authentic_bbp_forcing,
    gamma_defect_interval,
)


def _nonnegative_integer(n: int, maximum: int = 100000) -> int:
    if type(n) is not int or not 0 <= n <= maximum:
        raise GammaBridgeError("bounded nonnegative integer required")
    return n


def _moment_g(k: int, terms: int) -> RationalInterval:
    _nonnegative_integer(k)
    return gamma_defect_interval(8*k + 1, terms)


def _moment_b(k: int) -> Q:
    _nonnegative_integer(k)
    return authentic_bbp_forcing(k+1)


@dataclass(frozen=True)
class SourceAnchoredZero:
    """a_k=b_k/g_k; the SIGNED source measure has kth tilted mass zero."""
    reference_moment: int
    source_id: str
    normalizer: RationalInterval
    b_moment: Q
    g_moment: RationalInterval


def moment_anchor(k: int, *, terms: int=24) -> SourceAnchoredZero:
    """Rigorous exact rational bounds for b_k / delta(8k+1)."""
    _nonnegative_integer(k)
    g = _moment_g(k, terms)
    b = _moment_b(k)
    if g.lower <= 0:
        raise GammaBridgeError("insufficient log precision for positive moment")
    a = RationalInterval(b/g.upper, b/g.lower)
    if not (Q(4) < a.lower <= a.upper < Q(30)):
        raise GammaBridgeError("incorrect authentic source or insufficient precision")
    return SourceAnchoredZero(k,"Q:Coherent-Main-X-four-pole-BBP",a,b,g)


@dataclass(frozen=True)
class StrictMomentCrossing:
    k: int
    lag: int
    determinant: RationalInterval
    normalized_signed_moment: RationalInterval
    strictly_positive: bool


def signed_moment_crossing(k: int, lag: int, *, terms: int=30) -> StrictMomentCrossing:
    """Certify b_(k+j)g_k-b_k g_(k+j)>0, j>=1, using exact log bounds.

    Universal paper proof: monotone likelihood ratio P/W=B/C increases
    strictly on (0,1). Under the k-tilted W probability law, Chebyshev
    covariance Cov(R(t),t^(8j))>0. This code verifies a finite instance.
    """
    _nonnegative_integer(k,100000)
    if type(lag) is not int or not 1 <= lag <= 100000:
        raise GammaBridgeError("strictly positive finite moment lag required")
    bk, bj = _moment_b(k), _moment_b(k+lag)
    gk, gj = _moment_g(k,terms), _moment_g(k+lag,terms)
    lower = bj*gk.lower-bk*gj.upper
    upper = bj*gk.upper-bk*gj.lower
    if not lower>0:
        raise GammaBridgeError("inconclusive certificate: enlarge log series terms")
    det=RationalInterval(lower,upper)
    # a_k=b_k/g_k, so normalized sign numerator determinant/g_k.
    signed=RationalInterval(lower/gk.upper,upper/gk.lower)
    return StrictMomentCrossing(k,lag,det,signed,True)


@dataclass(frozen=True)
class CenteredResolventCertificate:
    reference_moment: int
    depth: int
    parameter: Q
    anchor: SourceAnchoredZero
    signed_resolvent: RationalInterval
    finite_positive_terms: tuple[RationalInterval,...]
    upper_tail: Q
    pi_anchor_at_zero: bool


def centered_resolvent_certificate(k: int, *, depth: int=8,
                                   terms: int=30, parameter=Q(1,16)) -> CenteredResolventCertificate:
    """Certify R_B,k(z)-a_k R_G,k(z)>0 for z>0 by positive moments.

    The j=0 coefficient is exactly zero, not numerically estimated.
    For j>=1, every coefficient is positive and strictly <b_(k+j).
    Tail j>=depth bounded by z^depth b_(k+depth)/(1-z)
    because the authentic b tape is decreasing in j.
    """
    _nonnegative_integer(k,50000)
    if type(depth) is not int or not 2 <= depth <= 300:
        raise GammaBridgeError("at least one positive coefficient needed")
    if type(parameter) not in (Q,int):
        raise GammaBridgeError("exact rational spectral parameter required")
    z=Q(parameter)
    if not 0<z<1:
        raise GammaBridgeError("positive resolvent radius below one required")
    anchor=moment_anchor(k,terms=terms)
    vals=[]
    lower=upper=Q(0)
    for j in range(1,depth):
        bj=_moment_b(k+j)
        gj=_moment_g(k+j,terms)
        x=RationalInterval(bj-anchor.normalizer.upper*gj.upper,
                           bj-anchor.normalizer.lower*gj.lower)
        if x.lower<=0 or x.upper>bj:
            raise GammaBridgeError("finite centered sign not certified")
        vals.append(x)
        lower+=z**j*x.lower
        upper+=z**j*x.upper
    upper_tail=z**depth*_moment_b(k+depth)/(1-z)
    return CenteredResolventCertificate(k,depth,z,anchor,
                    RationalInterval(lower,upper+upper_tail),
                    tuple(vals),upper_tail,k==0 and z==Q(1,16))


def authentic_orbit_rational(n: int) -> Q:
    """Exact U_n=16U_(n-1)+r(n), U0=0; no pi value used."""
    _nonnegative_integer(n,10000)
    u=Q(0)
    for j in range(1,n+1):
        u=16*u+authentic_bbp_forcing(j)
    return u


def green_tail_prefix(n: int, depth: int) -> Q:
    """The n-indexed authentic future-source Green tail, finite rational prefix."""
    _nonnegative_integer(n,100000)
    if type(depth) is not int or not 0<=depth<=300:
        raise GammaBridgeError("finite Green-tail cutoff required")
    return sum((authentic_bbp_forcing(n+j)/Q(16**j)
                 for j in range(1,depth+1)),Q(0))


def green_tail_interval(n: int, depth: int) -> RationalInterval:
    """Exact enclosure of T_n=sum_(j>=1) 16^-j*r(n+j).

    r is positive and strictly decreasing, so the unobserved tail after
    depth terms is between first omitted term and the full geometric
    envelope. Upper/lower are rational at EVERY finite horizon.
    """
    _nonnegative_integer(n,100000)
    if type(depth) is not int or not 0<=depth<=300:
        raise GammaBridgeError("bounded nonnegative Green depth required")
    head=green_tail_prefix(n,depth)
    next_value=authentic_bbp_forcing(n+depth+1)
    return RationalInterval(head+next_value/Q(16**(depth+1)),
                            head+next_value/Q(15*16**depth))


def finite_twisted_coboundary(n: int, depth: int) -> tuple[Q,Q,Q]:
    """Prove 16 T_n^(D) - T_(n+1)^(D-1) = r(n+1) exactly, D>=1.

    Finite identity carries the authentic zero-balance, but using
    unmatched finite tail depths would leave an explicit boundary defect.
    """
    _nonnegative_integer(n,100000)
    if type(depth) is not int or not 1<=depth<=300:
        raise GammaBridgeError("a nonzero common finite horizon is needed")
    left=16*green_tail_prefix(n,depth)
    right=green_tail_prefix(n+1,depth-1)
    force=authentic_bbp_forcing(n+1)
    if left-right!=force:
        raise ArithmeticError("BBP forward/backward finite cancellation failed")
    return left,right,force


@dataclass(frozen=True)
class SummableTailBudget:
    """All-horizon upper bound for sum_(n>=1) T_n, not a sampled orbit."""
    certified_n_prefix: int
    green_depth: int
    mass: RationalInterval
    after_prefix_upper: Q
    absolute_upper_by_source: Q


def summable_tail_budget(prefix_count: int=16,depth: int=12) -> SummableTailBudget:
    """A finite rational source certificate for sum_(n>=1) T_n.

    For K=prefix_count, the omitted n>K sum <= (1/15)*sum_(m>=K+2)r(m).
    Since r(m)<=15/[(8m-7)(8m-6)] <=15/(8m-7)^2, integral comparison
    bounds it by 1/(8K+9)^2+1/[8(8K+9)].
    The universal K=0 bound is 17/648. No pi values/digits used.
    """
    _nonnegative_integer(prefix_count,1500)
    if type(depth) is not int or not 1<=depth<=60:
        raise GammaBridgeError("finite positive correction depth required")
    lower=upper=Q(0)
    for n in range(1,prefix_count+1):
        t=green_tail_interval(n,depth)
        lower+=t.lower
        upper+=t.upper
    x=8*prefix_count+9
    after=Q(1,x*x)+Q(1,8*x)
    universal=Q(17,648)
    total=RationalInterval(lower,min(universal,upper+after))
    if total.lower>total.upper:
        raise ArithmeticError("finite bound contradicts universal source tail")
    return SummableTailBudget(prefix_count,depth,total,after,universal)


@dataclass(frozen=True)
class WeylOrbitTransport:
    frequency: int
    horizon: int
    authentic_source_id: str
    uniform_absolute_sum_error: Q
    normalized_error: Q
    tail_mass: RationalInterval
    exact_rational_orbit: bool
    cancellation_established: bool


def weyl_orbit_transport(frequency: int, horizon: int, *,
                         prefix_count: int=16,depth: int=12) -> WeylOrbitTransport:
    """For each integer h, |S_N(h,pi)-sum_(n=1)^N exp(2pi*i*h*U_n)|
       <= 2pi |h| sum_n T_n < 7 |h| * exact rational upper.

    Classical BBP source and pi<22/7 imported. All-N uniform bound is an
    analytic theorem; this is a rational proof budget, not numerical data.
    """
    if type(frequency) is not int or frequency==0 or abs(frequency)>100000:
        raise GammaBridgeError("fixed nonzero integer Fourier frequency required")
    if type(horizon) is not int or not 1<=horizon<=1_000_000:
        raise GammaBridgeError("positive finite observation horizon required")
    budget=summable_tail_budget(prefix_count,depth)
    cap=7*abs(frequency)*budget.mass.upper
    return WeylOrbitTransport(frequency,horizon,"Q:Coherent-Main-X-four-pole-BBP",
                              cap,cap/horizon,budget.mass,True,False)


@dataclass(frozen=True)
class AtomicOrderCountermodel:
    """Strict ordered cross-moments and rational radix-16 resolvent.

    A SYNTHETIC two-atom source—not Euler/BBP—proves that source-blind
    positive moment ordering does not entail digit normality.
    """
    gamma_atoms: tuple[tuple[Q,Q],...]
    source_atoms: tuple[tuple[Q,Q],...]
    rational_resolvent: Q
    strict_cross_moment_order: bool
    authentic: bool


def synthetic_atomic_order_countermodel() -> AtomicOrderCountermodel:
    values=(Q(1,2),Q(3,4))
    weights=(Q(1),Q(1))
    density=(Q(17),Q(47,2)) # 4+26t at t=1/2 and t=3/4
    atoms_g=tuple(zip(values,weights))
    atoms_b=tuple((t,w*r) for t,w,r in zip(values,weights,density))
    resolvent=sum((w/Q(1-t**8/16) for t,w in atoms_b),Q(0))
    mg=lambda k:sum((w*t**(8*k) for t,w in atoms_g),Q())
    mb=lambda k:sum((w*t**(8*k) for t,w in atoms_b),Q())
    ordered=all(mb(k+j)*mg(k)-mb(k)*mg(k+j)>0
                for k in range(6) for j in range(1,7))
    if not ordered or resolvent.denominator==1:
        raise ArithmeticError("synthetic source oracle failed")
    return AtomicOrderCountermodel(atoms_g,atoms_b,resolvent,ordered,False)


@dataclass(frozen=True)
class GammaResidueCertificate:
    """One of eight exact SUCC^8 residue channels of Euler's gamma carrier."""
    residue: int
    steps: int
    moment: RationalInterval
    finite_prefix: RationalInterval
    remainder_upper: Q


def gamma_residue_certificate(residue: int, steps: int, *,
                              terms: int=30) -> GammaResidueCertificate:
    """Gamma=sum_(a=1)^8 Gamma_a, Gamma_a=sum_(k>=0)delta(8k+a).

    For x=8*steps+a, omitted series <= sum_(k>=steps)1/(8k+a)^2
    <=1/x^2+1/(8x) by integral comparison. Lower tail is positive.
    All finite partial terms and remainder caps are exact rational.
    """
    if type(residue) is not int or not 1<=residue<=8:
        raise GammaBridgeError("one of eight authentic positive SUCC residues required")
    _nonnegative_integer(steps,1200)
    lower=upper=Q(0)
    for k in range(steps):
        g=gamma_defect_interval(8*k+residue,terms)
        if g.lower<=0:
            raise GammaBridgeError("insufficient logarithmic precision")
        lower+=g.lower
        upper+=g.upper
    x=8*steps+residue
    tail=Q(1,x*x)+Q(1,8*x)
    return GammaResidueCertificate(residue,steps,
                 RationalInterval(lower,upper+tail),RationalInterval(lower,upper),tail)


def gamma_eight_channel_certificate(steps: int, *, terms: int=30) -> RationalInterval:
    """Exact rational interval for Euler gamma, resolved into SUCC^8 channels.

    Summing finite partial sums over all 8 residue classes equals the
    original successor finite prefix through 8*steps, with no lost cells.
    """
    channels=[gamma_residue_certificate(a,steps,terms=terms) for a in range(1,9)]
    return RationalInterval(sum((c.moment.lower for c in channels),Q()),
                            sum((c.moment.upper for c in channels),Q()))


def signed_green_memory_lower(*, terms: int=32) -> Q:
    """Source-specific positive excess of BBP vs gamma *summable* memory.

    M_B - a0*M_G = (1/15) sum_(j>=1)(1-16^-j)(b_j-a0*g_j).
    Each j-term is strictly positive, so j=1 alone proves a rational
    positive lower bound: (1/16)*(b_1-a0*g_1) > 0.
    This is NOT the sign of a Fourier/carry correlation.
    """
    first=signed_moment_crossing(0,1,terms=terms)
    return first.normalized_signed_moment.lower/Q(16)


@dataclass(frozen=True)
class GeneralFiniteGreenCertificate:
    """Arbitrary exact rational finite source, not a claim about π."""
    radix: int
    forcing: tuple[Q,...]
    source_orbit: tuple[Q,...]
    green_potentials: tuple[Q,...]
    l1_green_actual: Q
    l1_operator_bound: Q


def finite_green_source(radix: int, forcing: tuple) -> GeneralFiniteGreenCertificate:
    """Finite generic b-T_n+T_(n+1) twisted-zero realization.

    Source n=1..M; T_n=sum_{j>=1,n+j<=M}b^-j*r(n+j) and T_M=0.
    Then U_(n+1)-bU_n = r(n+1) and b T_n-T_(n+1)=r(n+1).
    For n>=1, sum |T_n| <= (sum_(m>=2)|r_m|)/(b-1).
    This is finite algebra, the infinite l1 theorem needs absolute summability.
    """
    if type(radix) is not int or not 2<=radix<=10000:
        raise GammaBridgeError("positive integer radix at least 2 required")
    if not isinstance(forcing,tuple) or not forcing or len(forcing)>200:
        raise GammaBridgeError("finite nonempty source forcing tuple required")
    if any(type(x) not in (int,Q) for x in forcing):
        raise GammaBridgeError("exact rational source forcing required")
    r=tuple(Q(x) for x in forcing)
    M=len(r)
    orbit=[Q(0)]
    for x in r:
        orbit.append(radix*orbit[-1]+x)
    T=tuple(sum((r[n+j-1]/radix**j for j in range(1,M-n+1)),Q())
            for n in range(M+1))
    if any(radix*T[n]-T[n+1]!=r[n] for n in range(M)):
        raise ArithmeticError("generic finite source Green-telescope failed")
    if any(orbit[n]+T[n]!=radix**n*T[0] for n in range(M+1)):
        raise ArithmeticError("generic finite source completion square failed")
    l1=sum((abs(x) for x in T[1:]),Q())
    budget=sum((abs(x) for x in r[1:]),Q())/(radix-1)
    if l1>budget:
        raise ArithmeticError("generic positive/negative l1 Green bound failed")
    return GeneralFiniteGreenCertificate(radix,r,tuple(orbit),T,l1,budget)
