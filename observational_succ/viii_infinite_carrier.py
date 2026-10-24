"""Exact finite computations for two fully specified countable mode carriers.

The theorem in VIII_INFINITE_CARRIER.md distinguishes finite energy shells,
consistent cylinders on N_0^N, a Gibbs law on finite support, and heat trace.
Only the explicit linear and dyadic-multiplicity spectra have infinite-tail
interfaces here.  An arbitrary finite list is never evidence for an unseen
infinite tail.  Parameters q are rational, with q=exp(-beta) in the theorem.
"""

from fractions import Fraction
from math import comb, prod


class InfiniteCarrierError(ValueError):
    """An exact-domain or stated convergence hypothesis is unsatisfied."""


def _integer(value, name, minimum=0):
    if type(value) is not int or value < minimum:
        raise InfiniteCarrierError(f"{name} must be an integer >= {minimum}")
    return value


def _q(value):
    if type(value) not in (int, Fraction) or not 0 < value < 1:
        raise InfiniteCarrierError("q must be an exact rational in (0,1)")
    return Fraction(value)


def _weights(weights):
    weights = tuple(weights)
    for weight in weights:
        _integer(weight, "weight", 1)
    return weights


def finite_partition(q, weights):
    """Exact partition of the specified FINITE list, including multiplicity."""
    q = _q(q)
    weights = _weights(weights)
    return prod((1 / (1 - q**w) for w in weights), start=Fraction(1))


def geometric_cylinder_probability(q, weights, occupations):
    """A finite cylinder probability in the independent geometric product.

    This does not assert finite support almost surely; the same finite
    cylinder construction exists even when the full heat trace diverges.
    """
    q = _q(q)
    weights = _weights(weights)
    occupations = tuple(occupations)
    if len(weights) != len(occupations):
        raise InfiniteCarrierError("weights and occupations must have equal length")
    for occupation in occupations:
        _integer(occupation, "occupation")
    return prod(((1 - q**w) * q ** (w * n) for w, n in zip(weights, occupations)), start=Fraction(1))


def finite_energy_coefficients(weights, budget):
    """Exact coefficients for a supplied finite spectrum through budget.

    This is an infinite-carrier count only if a separate theorem proves
    that the list contains every mode affordable at the given budget.
    """
    weights = _weights(weights)
    _integer(budget, "budget")
    coefficients = [0] * (budget + 1)
    coefficients[0] = 1
    for weight in weights:
        for energy in range(weight, budget + 1):
            coefficients[energy] += coefficients[energy - weight]
    return tuple(coefficients)


def linear_energy_coefficients(budget):
    """Full infinite spectrum w_j=j: exactly the partition numbers p(0..X)."""
    _integer(budget, "budget")
    return finite_energy_coefficients(range(1, budget + 1), budget)


def linear_tail_mass(q, J):
    """Exact sum_{j>J} q**j, a bound on total variation of zero padding."""
    q = _q(q)
    _integer(J, "J")
    return q ** (J + 1) / (1 - q)


def linear_total_variation_bound(q, J):
    """Distance between the full Gibbs law and its zero-padded J-mode law."""
    return min(Fraction(1), linear_tail_mass(q, J))


def linear_energy_tail_bound(q, J):
    """Upper bound on expected omitted energy, not just omitted occupation.

    Sum_{j>J} j*q**j/(1-q**j) is bounded by replacing the denominators by
    1-q**(J+1).  The remaining differentiated geometric series is exact.
    """
    q = _q(q)
    _integer(J, "J")
    return q ** (J + 1) * ((J + 1) - J * q) / ((1 - q) ** 2 * (1 - q ** (J + 1)))


def _partition_enclosure(partial, tail_mass):
    if tail_mass >= 1:
        raise InfiniteCarrierError("tail union bound is >=1; increase the cutoff")
    return partial, partial / (1 - tail_mass)


def linear_partition_enclosure(q, J):
    """Rational enclosure of the infinite partition/heat trace for w_j=j.

    Requires q**(J+1)/(1-q)<1 for this particular rational enclosure; this
    is a truncation requirement, NOT the existence criterion (always q<1).
    """
    q = _q(q)
    _integer(J, "J")
    partial = finite_partition(q, range(1, J + 1))
    return _partition_enclosure(partial, linear_tail_mass(q, J))


def linear_budget_tail_bound(q, warmer_q, budget, J):
    """Bound Gibbs probability of TOTAL energy > budget for w_j=j.

    For q<r=warmer_q<1, the Rankin comparison is
    P_q(E>budget) <= (q/r)**(budget+1) * Z(r)/Z(q).
    Use an exact rational upper enclosure at r and finite lower bound at q.
    This energy cutoff is distinct from the J-mode cutoff used to enclose Z.
    """
    q = _q(q)
    warmer_q = _q(warmer_q)
    _integer(budget, "budget")
    _integer(J, "J")
    if not q < warmer_q:
        raise InfiniteCarrierError("warmer_q must be strictly greater than q")
    _, upper = linear_partition_enclosure(warmer_q, J)
    lower = finite_partition(q, range(1, J + 1))
    return min(Fraction(1), (q / warmer_q) ** (budget + 1) * upper / lower)


def dyadic_weight(index):
    """w_j=bit_length(j): exactly 2**(k-1) distinct modes of energy k."""
    _integer(index, "index", 1)
    return index.bit_length()


def dyadic_one_mode_mass(q, K):
    """Sum of q**w_j through complete energy blocks k=1,...,K.

    At q=1/2 this equals K/2 exactly.  Hence the full partition dominates
    1+K/2 for every K and diverges despite finite energy shells.
    """
    q = _q(q)
    _integer(K, "K")
    if q == Fraction(1, 2):
        return Fraction(K, 2)
    return q * (1 - (2 * q) ** K) / (1 - 2 * q)


def dyadic_partial_partition(q, K):
    """Finite partition through 2**K-1 modes, without expanding the list."""
    q = _q(q)
    _integer(K, "K")
    return prod(((1 / (1 - q**k)) ** (2 ** (k - 1)) for k in range(1, K + 1)), start=Fraction(1))


def dyadic_tail_mass(q, K):
    """Exact one-mode mass after block K, only in the convergent q<1/2 regime."""
    q = _q(q)
    _integer(K, "K")
    if q >= Fraction(1, 2):
        raise InfiniteCarrierError("dyadic spectrum has divergent Gibbs partition for q>=1/2")
    return q * (2 * q) ** K / (1 - 2 * q)


def dyadic_partition_enclosure(q, K):
    """Rational infinite-trace enclosure for the actual dyadic spectrum."""
    tail = dyadic_tail_mass(q, K)
    return _partition_enclosure(dyadic_partial_partition(q, K), tail)


def dyadic_energy_coefficients(budget):
    """Full infinite carrier's exact energy counts through budget.

    There are exponentially many affordable modes, but their multiplicity
    can be grouped: (1-z**k)**(-b) has coefficient C(b+n-1,n) at z**(kn).
    No list of 2**budget modes is materialized.
    """
    _integer(budget, "budget")
    coefficients = [0] * (budget + 1)
    coefficients[0] = 1
    for k in range(1, budget + 1):
        multiplicity = 2 ** (k - 1)
        old = coefficients
        coefficients = [
            sum(old[energy - k * n] * comb(multiplicity + n - 1, n)
                for n in range(energy // k + 1))
            for energy in range(budget + 1)
        ]
    return tuple(coefficients)
