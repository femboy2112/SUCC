"""Exact finite instruments for the all-gain normality reduction.

The conditional limit theorem is proved in PI_ALL_GAIN_RIGIDITY.md.  These
functions do not prove preservation of the authentic BBP occupation law.
All measures, costs and certificate budgets here are rational.  A certified
upper bound 22/7 for pi is used only in a Fourier Lipschitz budget.
"""

from __future__ import annotations

from fractions import Fraction as Q
from math import isqrt

from .source_history_transport import (
    AtomicProbability, circle_w1, multiplication_pushforward,
)


def _integer(value, minimum=1):
    if type(value) is not int or value < minimum:
        raise ValueError(f"strict integer >= {minimum} required")
    return value


def _rational(value):
    if type(value) not in (int, Q):
        raise ValueError("exact integer or Fraction required")
    return Q(value)


def _probability(value):
    if type(value) is not AtomicProbability:
        raise ValueError("validated AtomicProbability required")
    return value


def primes_through(maximum):
    _integer(maximum)
    return tuple(n for n in range(2, maximum+1)
                 if all(n % d for d in range(2, isqrt(n)+1)))


def uniform_torsion(denominator):
    """Uniform law on all d-torsion points, including zero."""
    _integer(denominator)
    return AtomicProbability(tuple((Q(j, denominator), Q(1, denominator))
                                   for j in range(denominator)))


def gain_average(measure, cutoff):
    """Average the gains 1,...,Q, not the powers of one fixed gain."""
    mu = _probability(measure)
    _integer(cutoff)
    return AtomicProbability(tuple((q*x, mass/cutoff)
                                   for q in range(1, cutoff+1)
                                   for x, mass in mu.atoms))


def rational_gain_limit(measure, maximum_generated_atoms=100_000):
    """The exact Q->infinity gain limit for a rational atomic law.

    Expanding actual BBP denominators can be exponentially expensive.  An
    explicit generation budget prevents accidentally materializing them;
    the two scalar functions below need no such expansion.
    """
    mu = _probability(measure)
    _integer(maximum_generated_atoms)
    if sum(x.denominator for x, _ in mu.atoms) > maximum_generated_atoms:
        raise ValueError("rational gain limit exceeds explicit atom budget")
    return AtomicProbability(tuple((Q(j, x.denominator), mass/x.denominator)
                                   for x, mass in mu.atoms
                                   for j in range(x.denominator)))


def gain_limit_origin_mass(measure):
    """Exact mass at zero after the infinite gain average, without expansion."""
    mu = _probability(measure)
    return sum((mass/x.denominator for x, mass in mu.atoms), Q())


def gain_limit_haar_bound(measure):
    """Convexity bound W1(R mu,Haar)<=sum mass/(4*reduced_denominator)."""
    return gain_limit_origin_mass(measure)/4


def rational_gain_remainder_budget(measure, cutoff):
    """TV(A_Q mu,R mu) upper bound from each exact rational period.

    For a single point with reduced denominator d and r=Q mod d, the TV
    value is exactly r(d-r)/(dQ).  For a mixture convexity gives an upper
    bound; it is not asserted to be an equality.
    """
    mu = _probability(measure)
    _integer(cutoff)
    tv = sum((mass*(cutoff % x.denominator)
              *(x.denominator-cutoff % x.denominator)
              /(x.denominator*cutoff) for x, mass in mu.atoms), Q())
    return {"tv_upper": tv, "w1_upper": tv/2,
            "haar_w1_upper": tv/2+gain_limit_haar_bound(mu)}


def origin_ball_mass(measure, radius):
    """Mass of the CLOSED geodesic ball at zero; radius in [0,1/2]."""
    mu = _probability(measure)
    radius = _rational(radius)
    if not 0 <= radius <= Q(1, 2):
        raise ValueError("circle radius must lie in [0,1/2]")
    return sum((mass for x, mass in mu.atoms if min(x, 1-x) <= radius), Q())


def prime_stationarity_costs(measure, maximum_gain):
    mu = _probability(measure)
    return {p: circle_w1(multiplication_pushforward(mu, p), mu)
            for p in primes_through(maximum_gain)}


def composite_stationarity_budgets(prime_costs, maximum_gain):
    """Compose certified prime bounds using epsilon_ab<=epsilon_a+a*epsilon_b.

    The caller must supply valid upper bounds for every needed prime.  The
    returned values are conditional on that certificate contract.  The
    circle diameter bound 1/2 is always available.  All factor orders are
    considered recursively, not assumed to have the same amplification.
    """
    _integer(maximum_gain)
    if type(prime_costs) is not dict:
        raise ValueError("dictionary of certified rational prime bounds required")
    required = primes_through(maximum_gain)
    for p, cost in prime_costs.items():
        _integer(p, 2)
        if any(p % d == 0 for d in range(2, isqrt(p)+1)):
            raise ValueError("stationarity keys must be prime")
        if _rational(cost) < 0:
            raise ValueError("stationarity bounds must be nonnegative")
    if any(p not in prime_costs for p in required):
        raise ValueError("a required prime stationarity certificate is missing")
    bounds = [Q(), Q()]
    for n in range(2, maximum_gain+1):
        candidates = [Q(1, 2)]
        for p in required:
            if p > n:
                break
            if n % p == 0:
                m = n//p
                ep = _rational(prime_costs[p])
                candidates.extend((ep+p*bounds[m], bounds[m]+m*ep))
        bounds.append(min(candidates))
    return tuple(bounds)


def prime_fourier_certificate(measure, cutoff, frequency, radius):
    """Certified upper bound for one real-circle Fourier coefficient.

    Let C_q bound W1(T_q mu,mu).  Dirichlet averaging gives
    |mu_hat(h)| <= mass(B(0,r))+1/(2Qr)
                    +2*pi*(C_|h| + mean_(q<=Q) C_q).
    Actual prime costs are computed with the existing exact primal/dual W1
    instrument; 2*pi is bounded by 44/7.  No trigonometric float is used.
    The certificate is often trivial on small BBP windows: this is retained.
    """
    mu = _probability(measure)
    _integer(cutoff)
    if type(frequency) is not int or frequency == 0:
        raise ValueError("nonzero integer frequency required")
    radius = _rational(radius)
    if not 0 < radius <= Q(1, 2):
        raise ValueError("positive radius <= 1/2 required")
    maximum = max(cutoff, abs(frequency))
    costs = prime_stationarity_costs(mu, maximum)
    bounds = composite_stationarity_budgets(costs, maximum)
    near_zero = origin_ball_mass(mu, radius)
    outside = Q(1, 2*cutoff)/radius
    stationarity = Q(44, 7)*(bounds[abs(frequency)]
                             +sum(bounds[1:cutoff+1], Q())/cutoff)
    raw = near_zero+outside+stationarity
    return {"cutoff": cutoff, "frequency": frequency, "radius": radius,
            "prime_costs": costs, "composite_budgets": bounds,
            "origin_mass": near_zero, "outside_origin_budget": outside,
            "stationarity_budget": stationarity, "raw_upper": raw,
            "fourier_modulus_upper": min(Q(1), raw)}


def integer_gain_readout(previous, current, forcing, gain, base=16):
    """Source-corrected integer stencil, meaningful on circle states.

    When current = base*previous+forcing mod 1 the result is gain*previous
    mod 1.  This exact readout says nothing about preservation of its law.
    """
    _integer(gain)
    _integer(base, 2)
    previous, current, forcing = map(_rational, (previous, current, forcing))
    if (current-base*previous-forcing) % 1:
        raise ValueError("states and forcing do not satisfy the source recurrence")
    return (current+(gain-base)*previous-forcing) % 1
