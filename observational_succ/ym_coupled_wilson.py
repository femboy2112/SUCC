"""Exact polynomial integration for a specified finite SU(2) Wilson graph.

This extends the one-plaquette character construction to ordered, shared-link
holonomies.  SU(2) is the actual unit quaternion sphere, not a finite subgroup.
All returned moments and error certificates are rational.  See the accompanying
coupled_wilson/CONSTRUCTION.md for proofs, costs, and continuum limitations.
"""

from dataclasses import dataclass
from fractions import Fraction as Q
from math import factorial
from typing import Mapping, Sequence

from .ym_succ_character import _natural, _rational


@dataclass(frozen=True, init=False)
class Polynomial:
    """Sparse rational polynomial; exponent tuples retain every link variable."""

    num_variables: int
    terms: tuple[tuple[tuple[int, ...], Q], ...]

    def __init__(self, num_variables: int, terms: Mapping[tuple[int, ...], int | Q]):
        _natural(num_variables)
        cleaned = {}
        for powers, coefficient in terms.items():
            powers = tuple(powers)
            if len(powers) != num_variables:
                raise ValueError("exponent tuple has the wrong dimension")
            for power in powers:
                _natural(power)
            coefficient = _rational(coefficient)
            if coefficient:
                cleaned[powers] = coefficient
        object.__setattr__(self, "num_variables", num_variables)
        object.__setattr__(self, "terms", tuple(sorted(cleaned.items())))

    def _coerce(self, other):
        if not isinstance(other, Polynomial):
            other = Polynomial(self.num_variables, {(0,) * self.num_variables: _rational(other)})
        if self.num_variables != other.num_variables:
            raise ValueError("polynomials use different link carriers")
        return other

    def __add__(self, other):
        other = self._coerce(other)
        terms = dict(self.terms)
        for powers, coefficient in other.terms:
            terms[powers] = terms.get(powers, Q(0)) + coefficient
        return Polynomial(self.num_variables, terms)

    __radd__ = __add__

    def __neg__(self):
        return Polynomial(self.num_variables, {p: -c for p, c in self.terms})

    def __sub__(self, other):
        return self + -self._coerce(other)

    def __rsub__(self, other):
        return self._coerce(other) + -self

    def __mul__(self, other):
        other = self._coerce(other)
        terms = {}
        for p, a in self.terms:
            for q, b in other.terms:
                powers = tuple(x + y for x, y in zip(p, q))
                terms[powers] = terms.get(powers, Q(0)) + a * b
        return Polynomial(self.num_variables, terms)

    __rmul__ = __mul__

    def __pow__(self, power: int):
        _natural(power)
        result = self._coerce(1)
        base = self
        while power:
            if power % 2:
                result = result * base
            base = base * base if power > 1 else base
            power //= 2
        return result

    @property
    def coefficient_bound(self) -> Q:
        """Rational sup-norm bound on the product unit-quaternion carrier."""
        return sum((abs(c) for _, c in self.terms), Q(0))


def constant_polynomial(edge_count: int, value: int | Q) -> Polynomial:
    _natural(edge_count)
    return Polynomial(4 * edge_count, {(0,) * (4 * edge_count): _rational(value)})


def link_quaternion(edge_count: int, edge: int) -> tuple[Polynomial, ...]:
    """Four coordinate polynomials for one zero-based oriented link."""
    _natural(edge_count)
    _natural(edge)
    if edge >= edge_count:
        raise ValueError("link index is outside the graph")
    coordinates = []
    for component in range(4):
        powers = [0] * (4 * edge_count)
        powers[4 * edge + component] = 1
        coordinates.append(Polynomial(4 * edge_count, {tuple(powers): Q(1)}))
    return tuple(coordinates)


def quaternion_product(a, b):
    """Hamilton product, in source path order; never commute the factors."""
    if len(a) != 4 or len(b) != 4:
        raise ValueError("quaternions require four components")
    w, x, y, z = a
    r, s, t, u = b
    return (w*r - x*s - y*t - z*u,
            w*s + x*r + y*u - z*t,
            w*t - x*u + y*r + z*s,
            w*u + x*t - y*s + z*r)


def quaternion_conjugate(a):
    if len(a) != 4:
        raise ValueError("quaternions require four components")
    return (a[0], -a[1], -a[2], -a[3])


def _word(edge_count: int, word: Sequence[int]) -> tuple[int, ...]:
    _natural(edge_count)
    result = tuple(word)
    if any(type(e) is not int or e == 0 or abs(e) > edge_count for e in result):
        raise ValueError("words use signed one-based link indices")
    return result


def word_holonomy(edge_count: int, word: Sequence[int]) -> tuple[Polynomial, ...]:
    result = (constant_polynomial(edge_count, 1),) + (constant_polynomial(edge_count, 0),) * 3
    for e in _word(edge_count, word):
        link = link_quaternion(edge_count, abs(e) - 1)
        result = quaternion_product(result, link if e > 0 else quaternion_conjugate(link))
    return result


def word_trace(edge_count: int, word: Sequence[int]) -> Polynomial:
    """Normalized SU(2) trace Re(holonomy), a real polynomial bounded by one."""
    return word_holonomy(edge_count, word)[0]


@dataclass(frozen=True)
class LinkGraph:
    vertex_count: int
    edges: tuple[tuple[int, int], ...]

    def __post_init__(self):
        _natural(self.vertex_count)
        edges = tuple(tuple(e) for e in self.edges)
        for edge in edges:
            if len(edge) != 2 or any(type(v) is not int or not 0 <= v < self.vertex_count for v in edge):
                raise ValueError("each edge must have two declared vertex endpoints")
        object.__setattr__(self, "edges", edges)

    def closed_word(self, word: Sequence[int]) -> tuple[int, ...]:
        word = _word(len(self.edges), word)
        endpoints = [self.edges[e - 1] if e > 0 else self.edges[-e - 1][::-1] for e in word]
        if endpoints and any(endpoints[i][1] != endpoints[(i + 1) % len(endpoints)][0] for i in range(len(endpoints))):
            raise ValueError("Wilson words must be composable closed paths")
        return word


def sphere_monomial_moment(powers: Sequence[int]) -> Q:
    """Normalized S^3 Haar moment, proved by Gaussian polar integration."""
    powers = tuple(powers)
    if len(powers) != 4:
        raise ValueError("a unit quaternion has four coordinates")
    for power in powers:
        _natural(power)
    if any(power % 2 for power in powers):
        return Q(0)
    numerator = Q(1)
    total = 0
    for power in powers:
        half = power // 2
        total += half
        for k in range(half):
            numerator *= Q(2*k + 1, 2)
    return numerator / factorial(total + 1)


def haar_integral(polynomial: Polynomial) -> Q:
    """Integrate all shared variables once under the product SU(2) Haar law."""
    if polynomial.num_variables % 4:
        raise ValueError("the carrier must consist of whole quaternion links")
    result = Q(0)
    for powers, coefficient in polynomial.terms:
        moment = coefficient
        for start in range(0, polynomial.num_variables, 4):
            moment *= sphere_monomial_moment(powers[start:start + 4])
            if not moment:
                break
        result += moment
    return result


def evaluate(polynomial: Polynomial, coordinates: Sequence[int | Q]) -> Q:
    coordinates = tuple(_rational(x) for x in coordinates)
    if len(coordinates) != polynomial.num_variables:
        raise ValueError("coordinate vector has the wrong dimension")
    return sum((c * _monomial_value(p, coordinates) for p, c in polynomial.terms), Q(0))


def _monomial_value(powers, coordinates):
    result = Q(1)
    for power, coordinate in zip(powers, coordinates):
        result *= coordinate**power
    return result


def taylor_polynomial(argument: Polynomial, degree: int) -> Polynomial:
    _natural(degree)
    result = argument._coerce(1)
    term = result
    for k in range(1, degree + 1):
        term = term * argument * Q(1, k)
        result = result + term
    return result


def _source_data(graph, loops, betas, degrees):
    loops = tuple(graph.closed_word(word) for word in loops)
    betas = tuple(_rational(beta) for beta in betas)
    degrees = tuple(_natural(degree) for degree in degrees)
    if not (len(loops) == len(betas) == len(degrees)):
        raise ValueError("one coupling and Taylor degree are required per loop")
    if any(beta < 0 for beta in betas):
        raise ValueError("the character-positive Wilson construction uses beta >= 0")
    if any(degree % 2 for degree in degrees):
        raise ValueError("strict pointwise positivity requires even Taylor degrees")
    return loops, betas, degrees


def factorwise_density(graph: LinkGraph, loops, betas, degrees) -> Polynomial:
    """Strictly positive product of even Taylor factors for closed holonomies."""
    loops, betas, degrees = _source_data(graph, loops, betas, degrees)
    density = constant_polynomial(len(graph.edges), 1)
    for word, beta, degree in zip(loops, betas, degrees):
        density = density * taylor_polynomial(beta * word_trace(len(graph.edges), word), degree)
    return density


def factorwise_error_bound(betas, degrees, observable_bound: int | Q) -> Q:
    """2 M 3^ceil(2 sum beta) sum beta^(K+1)/(K+1)!, with exact inputs."""
    betas = tuple(_rational(beta) for beta in betas)
    degrees = tuple(_natural(degree) for degree in degrees)
    bound = _rational(observable_bound)
    if len(betas) != len(degrees) or any(beta < 0 for beta in betas) or bound < 0:
        raise ValueError("nonnegative bounds/couplings and matching degree list required")
    if any(degree % 2 for degree in degrees):
        raise ValueError("the probability approximation requires even degrees")
    twice_sum = 2 * sum(betas, Q(0))
    ceiling = (twice_sum.numerator + twice_sum.denominator - 1) // twice_sum.denominator
    tails = sum((beta**(degree + 1) / factorial(degree + 1) for beta, degree in zip(betas, degrees)), Q(0))
    return 2 * bound * 3**ceiling * tails


def wilson_expectation(graph: LinkGraph, loops, betas, degrees, observable: Polynomial) -> Q:
    if observable.num_variables != 4 * len(graph.edges):
        raise ValueError("observable belongs to a different graph")
    density = factorwise_density(graph, loops, betas, degrees)
    partition = haar_integral(density)
    if partition <= 0:
        raise ArithmeticError("the strictly positive density must have positive integral")
    return haar_integral(observable * density) / partition


@dataclass(frozen=True)
class CoupledWilsonCertificate:
    graph: LinkGraph
    loops: tuple[tuple[int, ...], ...]
    betas: tuple[Q, ...]
    degrees: tuple[int, ...]
    observable: Polynomial
    tolerance: Q
    density_terms: int
    partition: Q
    numerator: Q
    expectation: Q
    error_bound: Q


def build_wilson_certificate(graph: LinkGraph, loops, betas, observable: Polynomial,
                             tolerance: int | Q) -> CoupledWilsonCertificate:
    """Terminating finite-graph construction; no complexity or cutoff uniformity claim.

    Every step uses rational arithmetic. Dense expansions can grow very large;
    mathematical termination is not a claim of practical large-lattice speed.
    """
    tolerance = _rational(tolerance)
    if tolerance <= 0:
        raise ValueError("tolerance must be strictly positive")
    betas = tuple(betas)
    loops, betas, _ = _source_data(graph, loops, betas, (0,) * len(betas))
    if observable.num_variables != 4 * len(graph.edges):
        raise ValueError("observable belongs to a different graph")
    degree = 0
    degrees = (degree,) * len(betas)
    error = factorwise_error_bound(betas, degrees, observable.coefficient_bound)
    while error > tolerance:
        degree += 2
        degrees = (degree,) * len(betas)
        error = factorwise_error_bound(betas, degrees, observable.coefficient_bound)
    density = factorwise_density(graph, loops, betas, degrees)
    partition = haar_integral(density)
    numerator = haar_integral(observable * density)
    if partition <= 0:
        raise ArithmeticError("the certified density has nonpositive integral")
    return CoupledWilsonCertificate(graph, loops, betas, degrees, observable,
                                   tolerance, len(density.terms), partition,
                                   numerator, numerator / partition, error)
