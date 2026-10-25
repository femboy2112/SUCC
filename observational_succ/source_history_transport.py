"""Exact optimal circle transport for source-history preservation probes.

The circle W1 distance uses a weighted-median flux and an exact periodic
1-Lipschitz dual witness. It is not the sorted-line transport cost. The
finite beta <= 4*epsilon + 1/(2J) bridge does not establish that the actual
BBP source satisfies vanishing epsilon, or that pi is normal.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q
from itertools import permutations
from math import factorial

from .pi_source_collision import prime_window

PREREGISTERED_PRIMES = (137, 281, 521)
PREREGISTERED_HISTORY_DEPTHS = (2, 4, 8)


def _integer(value, minimum=0):
    if type(value) is not int or value < minimum:
        raise ValueError("strict integer in the declared domain required")
    return value


def _rational(value):
    if type(value) not in (int, Q):
        raise ValueError("exact integer or Fraction required")
    return Q(value)


@dataclass(frozen=True)
class AtomicProbability:
    """Canonical rational atomic probability on the circle of length one."""

    atoms: tuple[tuple[Q, Q], ...]

    def __post_init__(self):
        if type(self.atoms) not in (tuple, list) or not self.atoms:
            raise ValueError("nonempty tuple/list of (point,mass) atoms required")
        combined = {}
        for atom in self.atoms:
            if type(atom) not in (tuple, list) or len(atom) != 2:
                raise ValueError("each atom must be a (point,mass) pair")
            point, mass = _rational(atom[0]) % 1, _rational(atom[1])
            if mass < 0:
                raise ValueError("W1 input masses must be nonnegative")
            combined[point] = combined.get(point, Q()) + mass
        if sum(combined.values(), Q()) != 1:
            raise ValueError("W1 probability masses must sum exactly to one")
        object.__setattr__(self, "atoms", tuple(sorted(
            (point, mass) for point, mass in combined.items() if mass)))


def _probability(value):
    if type(value) is not AtomicProbability:
        raise ValueError("validated AtomicProbability required")
    return value


def empirical_law(points) -> AtomicProbability:
    if type(points) not in (tuple, list) or not points:
        raise ValueError("nonempty exact point tuple/list required")
    mass = Q(1, len(points))
    return AtomicProbability(tuple((_rational(point), mass) for point in points))


def multiplication_pushforward(measure, multiplier=3) -> AtomicProbability:
    mu = _probability(measure)
    _integer(multiplier, 1)
    return AtomicProbability(tuple((multiplier*x, mass) for x, mass in mu.atoms))


def history_average(measure, depth, multiplier=3) -> AtomicProbability:
    """Positive uniform average of history lengths 0,...,depth-1."""
    mu = _probability(measure)
    _integer(depth, 1)
    _integer(multiplier, 1)
    atoms = []
    current = mu
    for _ in range(depth):
        atoms.extend((point, mass/depth) for point, mass in current.atoms)
        current = multiplication_pushforward(current, multiplier)
    return AtomicProbability(tuple(atoms))


@dataclass(frozen=True)
class CircleW1Certificate:
    knots: tuple[Q, ...]
    cdf_difference: tuple[Q, ...]
    flux_shift: Q
    flux: tuple[Q, ...]
    dual_slopes: tuple[Q, ...]
    dual_potential: tuple[Q, ...]
    cost: Q
    dual_value: Q


def _cdf_steps(first, second):
    delta = {}
    for point, mass in first.atoms:
        delta[point] = delta.get(point, Q()) + mass
    for point, mass in second.atoms:
        delta[point] = delta.get(point, Q()) - mass
    knots = tuple(sorted({Q(), Q(1), *delta.keys()}))
    values = []
    running = Q()
    for point in knots[:-1]:
        running += delta.get(point, Q())
        values.append(running)
    if running != 0:
        raise AssertionError("probability difference did not have mass zero")
    return delta, knots, tuple(values)


def circle_w1_certificate(first, second) -> CircleW1Certificate:
    """Optimal circular W1 by min_c integral |F_mu-F_nu-c|.

    The weighted-median flux gives a feasible circle flow. The explicitly
    constructed periodic dual function has Lipschitz constant at most one
    and attains the same cost, certifying optimality with exact arithmetic.
    """
    mu, nu = _probability(first), _probability(second)
    delta, knots, values = _cdf_steps(mu, nu)
    lengths = tuple(right-left for left, right in zip(knots, knots[1:]))
    accumulated = Q()
    median = values[0]
    for value, length in sorted(zip(values, lengths)):
        accumulated += length
        if accumulated >= Q(1, 2):
            median = value
            break
    below = sum((length for value, length in zip(values, lengths)
                 if value < median), Q())
    above = sum((length for value, length in zip(values, lengths)
                 if value > median), Q())
    equal = 1-below-above
    if equal <= 0 or below > Q(1, 2) or above > Q(1, 2):
        raise AssertionError("weighted median failed its defining inequalities")
    neutral_slope = (above-below)/equal
    slopes = tuple(Q(1) if value < median else Q(-1) if value > median
                   else neutral_slope for value in values)
    potential = [Q()]
    for slope, length in zip(slopes, lengths):
        potential.append(potential[-1]+slope*length)
    flux = tuple(value-median for value in values)
    cost = sum((length*abs(value) for length, value in zip(lengths, flux)), Q())
    phi = dict(zip(knots, potential))
    dual = sum((mass*phi[point] for point, mass in delta.items()), Q())
    if potential[-1] != 0 or any(abs(slope) > 1 for slope in slopes) or dual != cost:
        raise AssertionError("circle primal/dual optimality certificate failed")
    return CircleW1Certificate(knots, values, median, flux, slopes,
                               tuple(potential), cost, dual)


def validate_circle_w1_certificate(first, second, certificate) -> bool:
    """Check an explicit flux/dual witness without recomputing its median."""
    mu, nu = _probability(first), _probability(second)
    if type(certificate) is not CircleW1Certificate:
        raise ValueError("CircleW1Certificate required")
    cert = certificate
    vectors = (cert.knots, cert.cdf_difference, cert.flux,
               cert.dual_slopes, cert.dual_potential)
    if (any(type(vector) is not tuple for vector in vectors)
            or any(type(value) not in (int, Q)
                   for vector in vectors for value in vector)
            or any(type(value) not in (int, Q)
                   for value in (cert.flux_shift, cert.cost, cert.dual_value))):
        return False
    delta, knots, values = _cdf_steps(mu, nu)
    if cert.knots != knots or cert.cdf_difference != values:
        return False
    n = len(values)
    if (len(cert.flux) != n or len(cert.dual_slopes) != n
            or len(cert.dual_potential) != n+1):
        return False
    if cert.dual_potential[0] != 0 or cert.dual_potential[-1] != 0:
        return False
    lengths = tuple(right-left for left, right in zip(knots, knots[1:]))
    for i in range(n):
        if (cert.flux[i] != values[i]-cert.flux_shift
                or abs(cert.dual_slopes[i]) > 1
                or cert.dual_potential[i+1]-cert.dual_potential[i]
                != cert.dual_slopes[i]*lengths[i]):
            return False
    primal = sum((length*abs(flow) for length, flow in zip(lengths, cert.flux)), Q())
    phi = dict(zip(knots, cert.dual_potential))
    dual = sum((mass*phi[point] for point, mass in delta.items()), Q())
    return cert.cost == primal == dual == cert.dual_value and 0 <= primal <= Q(1, 2)


def circle_w1(first, second) -> Q:
    return circle_w1_certificate(first, second).cost


def brute_force_equal_weight_w1(first_points, second_points) -> dict:
    """Independent all-permutation matching oracle, at most eight points.

    Each permutation is evaluated using geodesic pair costs, without CDFs,
    weighted medians, flow variables, or line sorting. Repeated points are
    allowed, and the enumeration count includes repeated equivalent matches.
    """
    if type(first_points) not in (tuple, list) or type(second_points) not in (tuple, list):
        raise ValueError("point tuples/lists required")
    n = len(first_points)
    if n != len(second_points) or not 1 <= n <= 8:
        raise ValueError("equal sample sizes in 1..8 required")
    first = tuple(_rational(x) % 1 for x in first_points)
    second = tuple(_rational(x) % 1 for x in second_points)
    best = None
    best_permutation = None
    for assignment in permutations(range(n)):
        total = Q()
        for i, j in enumerate(assignment):
            separation = abs(first[i]-second[j])
            total += min(separation, 1-separation)
        cost = total/n
        if best is None or cost < best:
            best, best_permutation = cost, assignment
    return {"cost": best, "permutation": best_permutation,
            "assignments_enumerated": factorial(n), "sample_size": n}


def history_preservation_certificate(measure, depth, multiplier=3) -> dict:
    """Finite beta <= (multiplier+1)*epsilon + 1/(2*depth).

    This is a conditional bridge. Actual epsilon tending to zero is not
    asserted. The exact boundary cost is also retained, before replacing it
    by the universal circle-diameter bound.
    """
    mu = _probability(measure)
    _integer(depth, 1)
    _integer(multiplier, 1)
    once = multiplication_pushforward(mu, multiplier)
    averaged = history_average(mu, depth, multiplier)
    shifted_average = multiplication_pushforward(averaged, multiplier)
    future = multiplication_pushforward(mu, multiplier**depth)
    beta = circle_w1(once, mu)
    epsilon = circle_w1(averaged, mu)
    boundary = circle_w1(future, mu)/depth
    average_step = circle_w1(shifted_average, averaged)
    if average_step != boundary:
        raise AssertionError("history telescoping lost signed-difference homogeneity")
    bound = (multiplier+1)*epsilon+Q(1, 2*depth)
    exact_bound = (multiplier+1)*epsilon+boundary
    if beta > exact_bound or boundary > Q(1, 2*depth):
        raise AssertionError("history-preservation bridge failed")
    if depth == 2 and 2*epsilon != beta:
        raise AssertionError("two-history midpoint identity failed")
    return {"history_depth": depth, "multiplier": multiplier,
            "original_support_size": len(mu.atoms),
            "averaged_support_size": len(averaged.atoms),
            "beta": beta, "epsilon": epsilon,
            "exact_boundary_term": boundary,
            "averaged_one_step_defect": average_step,
            "exact_bound": exact_bound, "universal_bound": bound,
            "universal_slack": bound-beta,
            "j2_midpoint_identity": 2*epsilon == beta if depth == 2 else None}


def bbp_history_transport_rows() -> tuple[dict, ...]:
    """All nine preregistered authentic-source rows; no fitted scaling law."""
    rows = []
    for p in PREREGISTERED_PRIMES:
        window = prime_window(p)
        mu = empirical_law(window.states)
        for depth in PREREGISTERED_HISTORY_DEPTHS:
            row = history_preservation_certificate(mu, depth, 3)
            # The inherited positive BBP tail transports these finite rational
            # source laws to the corresponding true pi orbit with explicit costs.
            average_lipschitz = Q(3**depth-1, 2*depth)
            row.update({"prime": p, "first_state_index": window.start+1,
                        "last_state_index": 4*window.start,
                        "window_length": window.length,
                        "source_kind": "authentic rational BBP y-state window",
                        "true_orbit_beta_error_upper": 4*window.tail_bound,
                        "true_orbit_epsilon_error_upper":
                            (1+average_lipschitz)*window.tail_bound,
                        "asymptotic_decay_claim": False})
            rows.append(row)
    return tuple(rows)
