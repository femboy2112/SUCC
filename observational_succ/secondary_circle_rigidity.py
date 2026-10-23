"""Finite source-conditioned rigidity for arithmetic reconstructions of S^1.

Mathematical status: paper-proved elementary estimates, rational exact budgets;
not a proof of pi normality. See SECONDARY_CIRCLE_PRIME_RIGIDITY.md.

A supplied sequence of cosine coefficients is NOT automatically authenticated as
moments of a probability measure. Functions that accept such data are conditional
budgets. The finite circle model and the pi interval adapter identify sources.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q
from math import gcd, isqrt
from typing import Sequence


def _natural(value: int, label: str, minimum: int = 1) -> None:
    if type(value) is not int or value < minimum:
        raise ValueError(f"{label}: expected integer >= {minimum}")


def _rat(value: int | Q, label: str) -> Q:
    if type(value) not in (int, Q):
        raise ValueError(f"{label}: exact int or Fraction required")
    return Q(value)


def primes_to(limit: int) -> tuple[int, ...]:
    _natural(limit, "limit")
    out = []
    for p in range(2, limit + 1):
        if all(p % d for d in range(2, isqrt(p) + 1)):
            out.append(p)
    return tuple(out)


def factor_word(value: int) -> tuple[int, ...]:
    """Canonical ordered word in genuine primes; composites not generators."""
    _natural(value, "value")
    factors = []
    n = value
    d = 2
    while d*d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:
        factors.append(n)
    return tuple(factors)


def prime_cosine_edges(cos_moments: Sequence[Q | int]) -> tuple[tuple[int, int, Q], ...]:
    """Exact discrepancies c_(p*k)-c_k for all genuine p*k <= M.

    Index 0 is c_0=1; inputs are conditional until their source is verified.
    """
    if len(cos_moments) < 3:
        raise ValueError("need c_0 through c_M with M>=2")
    c = tuple(_rat(v, "cos moment") for v in cos_moments)
    if c[0] != 1 or any(not -1 <= v <= 1 for v in c):
        raise ValueError("incompatible probability normalization or moment range")
    M = len(c) - 1
    return tuple((p, k, abs(c[p*k] - c[k]))
                 for p in primes_to(M) for k in range(1, M//p+1))


@dataclass(frozen=True)
class RealRigidityBudget:
    """Conditioned on actual moments of a probability measure on T."""
    cutoff: int
    mean_chord: Q
    chord_deficit: Q
    max_prime_cosine_defect: Q
    worst_prime_word_length: int
    propagated_cosine_error: Q
    fejer_integral: Q
    harmonic_bound: Q
    simple_bound: Q


def real_chord_rigidity(cos_moments: Sequence[Q | int]) -> RealRigidityBudget:
    """Certified *conditional* bound for actual probability-measure moments.

    c_h=integral cos(2*pi*h*x) dmu. Let eps=max_|c_pk-c_k|,
    L=floor(log_2 M), eta=max(0,2*c_1). For 1<=h<=M,
    |c_h| <= max(eta/2+L*eps, 1/(M-1)+2L*eps).

    Fejer integral below is also a genuine >=0 diagnostic for actual moments.
    Arbitrary user-provided numbers do not authenticate a measure/source.
    """
    c = tuple(_rat(v, "cos moment") for v in cos_moments)
    edges = prime_cosine_edges(c)
    M = len(c) - 1
    eps = max((v for _, _, v in edges), default=Q(0))
    L = (M).bit_length() - 1
    d = L * eps
    eta = max(Q(), 2*c[1])
    fejer = Q(1) + 2*sum((Q(M-h, M)*c[h] for h in range(1, M)), Q())
    if fejer < 0:
        raise ValueError("claimed moments violate necessary Fejer positivity")
    sharp = max(eta/2+d, Q(1, M-1)+2*d)
    simple = eta/2+Q(1, M-1)+2*d
    return RealRigidityBudget(M, 2-2*c[1], eta, eps, L, d,
                              fejer, min(Q(1), sharp), min(Q(1), simple))


def sqrt_upper(value: Q | int, bits: int = 60) -> Q:
    """Exact rational outward square-root upper bound; no floating point."""
    _natural(bits, "bits")
    q = _rat(value, "nonnegative rational")
    if q < 0:
        raise ValueError("square-root argument must be nonnegative")
    scale = 1 << bits
    lower = isqrt(q.numerator * scale * scale // q.denominator)
    if Q(lower*lower, scale*scale) == q:
        return Q(lower, scale)
    return Q(lower+1, scale)


@dataclass(frozen=True)
class FourierAmplification:
    frequency: int
    base: int
    horizon: int
    replicas: int
    cutoff: int
    max_cosine: Q
    variance_upper: Q
    endpoint_error: Q
    modulus_upper: Q


def amplified_fourier_bound(*, base: int, frequency: int, horizon: int,
                            replicas: int, cosine_band_bound: Q | int,
                            cutoff: int, sqrt_bits: int = 60) -> FourierAmplification:
    """For an *actual* T_b orbit empirical measure, bound |A_(h,N)|.

    If |int cos(2*pi*k*x)dnu_N| <= B for 1<=k<=M and
    M>=|h|(b^(R-1)-1), then |A_h| <= (R-1)/N+
    sqrt(1/R+(1-1/R)B). Rounded outward using exact rational isqrt.
    """
    _natural(base, "base", 2)
    if type(frequency) is not int or frequency == 0:
        raise ValueError("nonzero integer frequency required")
    _natural(horizon, "horizon")
    _natural(replicas, "replicas")
    _natural(cutoff, "cutoff", 2)
    _natural(sqrt_bits, "sqrt_bits")
    B = _rat(cosine_band_bound, "cosine bound")
    if B < 0 or B > 1:
        raise ValueError("cosine bound must lie in [0,1]")
    if cutoff < abs(frequency) * (base**(replicas-1)-1):
        raise ValueError("insufficient frequency band for time-lag covariance")
    variance = Q(1, replicas) + Q(replicas-1, replicas)*B
    offset = Q(replicas-1, horizon)
    bound = min(Q(1), offset + sqrt_upper(variance, sqrt_bits))
    return FourierAmplification(frequency, base, horizon, replicas, cutoff,
                                B, variance, offset, bound)


def joint_rigidity_bound(cos_moments: Sequence[Q | int], *, base: int,
                         frequency: int, horizon: int, replicas: int) -> FourierAmplification:
    budget = real_chord_rigidity(cos_moments)
    return amplified_fourier_bound(base=base, frequency=frequency,
                                   horizon=horizon, replicas=replicas,
                                   cutoff=budget.cutoff,
                                   cosine_band_bound=budget.harmonic_bound)


def mobius(n: int) -> int:
    _natural(n, "n")
    factors = factor_word(n)
    return 0 if len(set(factors)) != len(factors) else (-1)**len(factors)


def ramanujan_sum(modulus: int, frequency: int) -> int:
    """C_q(k)=sum_(d|gcd(q,k)) d*mobius(q/d), exact integer."""
    _natural(modulus, "modulus", 2)
    if type(frequency) is not int:
        raise ValueError("integer frequency required")
    n = gcd(modulus, abs(frequency))
    return sum(d*mobius(modulus//d) for d in range(1, n+1) if n%d == 0)


def doubling_orbit(modulus: int, base: int = 2) -> tuple[int, ...]:
    _natural(modulus, "modulus", 2)
    _natural(base, "base", 2)
    if gcd(modulus, base) != 1:
        raise ValueError("orbit is not a permutation of units")
    result = []
    value = 1
    while value not in result:
        result.append(value)
        value = (value*base) % modulus
    if value != 1:
        raise AssertionError("unit orbit failed to return")
    return tuple(result)


def exact_rational_orbit_cosine(modulus: int, base: int, frequency: int) -> Q:
    """Exact cosine moment when unit group = <base> union -<base>.

    For a general smaller subgroup, a Ramanujan sum is NOT its orbit average;
    this authentic-source check fails closed instead of guessing.
    """
    if type(frequency) is not int or frequency < 0:
        raise ValueError("nonnegative integer frequency")
    orbit = set(doubling_orbit(modulus, base))
    units = {x for x in range(1, modulus) if gcd(x, modulus) == 1}
    if orbit | {(-x) % modulus for x in orbit} != units:
        raise ValueError("unit group is not covered by the signed orbit")
    return Q(ramanujan_sum(modulus, frequency), len(units))


def exact_uniform_polygon_cosine(modulus: int, frequency: int) -> Q:
    """Uniform qth roots, an authentic b-invariant source iff gcd(q,b)=1."""
    _natural(modulus, "modulus", 2)
    if type(frequency) is not int:
        raise ValueError("integer frequency")
    return Q(1) if frequency % modulus == 0 else Q()


def certified_pi_cosine_intervals(base: int, horizon: int, cutoff: int, *,
                                 level: int = 16, precision: int = 85,
                                 order: int = 30) -> tuple[tuple[Q, Q], ...]:
    """True pi orbit cos(2*pi*h*b^j*pi) interval means, h=0..cutoff.

    Reuses the prior circle-source interval and rational Taylor machinery;
    no digits of pi or floating-point pi enter the production oracle.
    """
    _natural(base, "base", 2)
    _natural(horizon, "horizon")
    _natural(cutoff, "cutoff", 2)
    _natural(level, "level")
    _natural(precision, "precision", 15)
    _natural(order, "order", 1)
    if horizon > 12 or cutoff > 96:
        raise ValueError("explicit finite research budget N<=12, M<=96")
    from .circle_collision_rigidity import pi_interval, _cos_enclosure
    pil, piu = pi_interval(level, precision)
    samples = [(Q(1), Q(1))]
    for h in range(1, cutoff+1):
        lo = hi = Q()
        for j in range(horizon):
            al, au = h*base**j*pil, h*base**j*piu
            center = (al+au)/2
            radius = (au-al)/2
            center -= (center+Q(1, 2)).numerator//(center+Q(1, 2)).denominator
            cl, cu = _cos_enclosure(center, radius, pil, piu, order)
            lo += cl
            hi += cu
        samples.append((max(-Q(1),lo/horizon), min(Q(1),hi/horizon)))
    return tuple(samples)


@dataclass(frozen=True)
class IntervalRigidityBudget:
    cutoff: int
    mean_chord_interval: tuple[Q, Q]
    chord_deficit: Q
    max_prime_cosine_defect: Q
    worst_prime_word_length: int
    propagated_cosine_error: Q
    fejer_integral_upper: Q
    harmonic_bound: Q
    simple_bound: Q


def interval_prime_and_chord_budget(intervals: Sequence[tuple[Q, Q]]) -> IntervalRigidityBudget:
    """Outward rational sufficient real moment bound from source intervals.

    Instead of trusting arbitrary point estimates, use all worst-case interval
    endpoints for eps and eta. The Fejer field is an UPPER diagnostic only here,
    not an independently certified exact Fejer integral.
    """
    if len(intervals) < 3:
        raise ValueError("need source enclosures c_0..c_M")
    pairs = tuple((_rat(a, "lower"),_rat(b, "upper")) for a,b in intervals)
    if pairs[0] != (Q(1),Q(1)) or any(a>b or a < -1 or b>1 for a,b in pairs):
        raise ValueError("invalid rational cosine interval")
    M=len(pairs)-1
    eps=Q()
    for p in primes_to(M):
        for k in range(1,M//p+1):
            a,b=pairs[p*k]
            c,d=pairs[k]
            eps=max(eps, abs(a-d), abs(b-c))
    L=M.bit_length()-1
    d=L*eps
    eta=max(Q(),2*pairs[1][1])
    upper=min(Q(1),max(eta/2+d,Q(1,M-1)+2*d))
    simple=min(Q(1),eta/2+Q(1,M-1)+2*d)
    # Source intervals do not uniquely fix the true Fejer integral.
    # This upper is valid but not a certified Fejer measurement.
    fejer_upper=Q(1)+2*sum((Q(M-h,M)*pairs[h][1] for h in range(1,M)),Q())
    if fejer_upper < 0:
        raise ValueError("cosine intervals contradict nonnegative Fejer integral")
    return IntervalRigidityBudget(M, (Q(2)-2*pairs[1][1],
                                      Q(2)-2*pairs[1][0]), eta,
                                  eps, L, d, fejer_upper, upper, simple)


def circle_rotation_commutator(base: int, shift: int | Q) -> Q:
    """Exact obstruction for R_c o T_b vs T_b o R_c in turns.

    Difference of the two maps is (b-1)*c modulo 1, independently of x.
    In particular b=2 forbids all nontrivial coordinate-rotation gauges.
    General homeomorphism rigidity requires the paper proof: the centralizer
    of doubling among circle homeomorphisms is {id, reflection}.
    """
    _natural(base, "base", 2)
    c = _rat(shift, "rotation shift")
    return ((base-1)*c) % 1


def doubled_origin_preimages(depth: int) -> tuple[Q, ...]:
    """Finite dyadic grid fixed pointwise by every orientation-preserving
    homeomorphism h commuting with T_2, by cyclic-order preservation.
    """
    _natural(depth, "depth", 0)
    return tuple(Q(j,1 << depth) for j in range(1 << depth))


@dataclass(frozen=True)
class PrimePathRigidity:
    """Optimal min-plus PRIME-WORD path cost among the supplied edge budgets.

    Exact costs require actual probability-measure cosine observations, or
    certified upper intervals. This is graph-path optimization, not an
    independently established physical or probabilistic independence claim.
    """
    cutoff: int
    path_costs: tuple[Q, ...]
    prime_paths: tuple[tuple[int, ...], ...]
    fejer_weighted_cost: Q
    per_frequency_bounds: tuple[Q, ...]
    uniform_cosine_bound: Q


def minplus_prime_chord_certificate(cos_moments: Sequence[Q | int]) -> PrimePathRigidity:
    """Sharper exact Fejer estimate using the least-cost prime-factor order.

    Cost(1)=0; Cost(n)=min_(p|n)[Cost(n/p)+|c_n-c_(n/p)|].
    Write W=2/(M-1) sum_(n=1)^(M-1)(1-n/M) Cost(n). Then
    |c_h| <= Cost(h)+max(eta/2, 1/(M-1)+W), 1<=h<=M.
    A legal prime path is recorded for every n; no composite primitive admitted.
    """
    c=tuple(_rat(v,"cos moment") for v in cos_moments)
    prior=real_chord_rigidity(c)
    M=prior.cutoff
    paths=[() for _ in range(M+1)]
    costs=[Q() for _ in range(M+1)]
    for n in range(2,M+1):
        choices=[]
        for p in set(factor_word(n)):
            parent=n//p
            choices.append((costs[parent]+abs(c[n]-c[parent]),paths[parent]+(p,)))
        cost,path=min(choices)
        costs[n]=cost
        paths[n]=path
    weighted=Q(2,M-1)*sum((Q(M-n,M)*costs[n] for n in range(1,M)),Q())
    offset=max(prior.chord_deficit/2,Q(1,M-1)+weighted)
    result=[Q(0)]+[min(Q(1),costs[n]+offset) for n in range(1,M+1)]
    return PrimePathRigidity(M,tuple(costs),tuple(paths),weighted,
                             tuple(result),max(result[1:]))


def interval_minplus_prime_chord_certificate(
        intervals: Sequence[tuple[Q,Q]]) -> PrimePathRigidity:
    """Source-interval version; each edge cost is a certified worst-case bound."""
    prior=interval_prime_and_chord_budget(intervals)
    pairs=tuple((_rat(a,"lower"),_rat(b,"upper")) for a,b in intervals)
    M=prior.cutoff
    paths=[() for _ in range(M+1)]
    costs=[Q() for _ in range(M+1)]
    for n in range(2,M+1):
        choices=[]
        for p in set(factor_word(n)):
            parent=n//p
            al,au=pairs[n]
            bl,bu=pairs[parent]
            edge=max(abs(al-bu),abs(au-bl))
            choices.append((costs[parent]+edge,paths[parent]+(p,)))
        cost,path=min(choices)
        costs[n]=cost
        paths[n]=path
    weighted=Q(2,M-1)*sum((Q(M-n,M)*costs[n] for n in range(1,M)),Q())
    offset=max(prior.chord_deficit/2,Q(1,M-1)+weighted)
    result=[Q(0)]+[min(Q(1),costs[n]+offset) for n in range(1,M+1)]
    return PrimePathRigidity(M,tuple(costs),tuple(paths),weighted,
                             tuple(result),max(result[1:]))
